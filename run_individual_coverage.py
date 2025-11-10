"""
Run coverage tests for each individual solution separately

This script:
1. Runs pytest with coverage for each solution file
2. Collects coverage metrics (line %, branch %, test status)
3. Generates 4 separate tables (one per LLM+prompt combination)
"""

import subprocess
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple
import sys

# Problem definitions with test counts
PROBLEMS = {
    '02': {'name': 'Maximum Pizza Slices', 'test_count': 1},
    '03': {'name': 'Number of Times All Blue', 'test_count': 1},
    '04': {'name': 'Unhappy Friends', 'test_count': 1},
    '05': {'name': 'Minimum Swaps to Make Grid Valid', 'test_count': 1},
    '06': {'name': 'Mix Strings', 'test_count': 3},
    '07': {'name': 'Contains Cycle in Grid', 'test_count': 1},
    '08': {'name': 'Number of Permutations with DI Sequence', 'test_count': 1},
    '10': {'name': 'Least Operators to Express Target', 'test_count': 1},
    '11': {'name': 'Longest Common Subsequence', 'test_count': 1},
    '12': {'name': 'Exchange Sort', 'test_count': 3},
}

VARIANTS = ['deepseek_cot', 'deepseek_self_planning', 'gemini_cot', 'gemini_self_planning']


def get_python_cmd():
    """Get Python command (prefer uv run)"""
    if Path("pyproject.toml").exists():
        return ["uv", "run", "python"]
    return [sys.executable]


def run_coverage_for_solution(solution_file: str, test_pattern: str) -> Dict:
    """Run coverage test for a single solution file"""

    python_cmd = get_python_cmd()

    # Run pytest with coverage - use broader scope to capture imports
    cmd = python_cmd + [
        "-m", "pytest",
        "test_individual_solutions.py",
        "-k", test_pattern,
        "-v",
        "--cov=individual_solutions",
        "--cov-report=term-missing",
        "--cov-branch",
        "--tb=no",
        "-q"
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )

        # Parse output
        output = result.stdout + result.stderr

        # Extract test status
        test_passed = result.returncode == 0

        # Extract coverage from output
        line_coverage = extract_line_coverage(output, solution_file)
        branch_coverage = extract_branch_coverage(output, solution_file)

        return {
            'test_passed': test_passed,
            'line_coverage': line_coverage,
            'branch_coverage': branch_coverage,
            'output': output
        }

    except subprocess.TimeoutExpired:
        return {
            'test_passed': False,
            'line_coverage': {'percent': 0, 'lines': '0/0'},
            'branch_coverage': {'percent': 0, 'branches': '0/0'},
            'output': 'TIMEOUT'
        }
    except Exception as e:
        return {
            'test_passed': False,
            'line_coverage': {'percent': 0, 'lines': '0/0'},
            'branch_coverage': {'percent': 0, 'branches': '0/0'},
            'output': str(e)
        }


def extract_line_coverage(output: str, solution_file: str) -> Dict:
    """Extract line coverage percentage from pytest-cov output"""
    # Look for line like: "individual_solutions/solution_02_deepseek_cot.py   18   0   6   0   100%"
    # Format: Name  Stmts  Miss  Branch  BrPart  Cover  Missing
    pattern = rf'individual_solutions/{re.escape(solution_file)}\s+(\d+)\s+(\d+)\s+\d+\s+\d+\s+(\d+)%'
    match = re.search(pattern, output)

    if match:
        total = int(match.group(1))
        missed = int(match.group(2))
        percent = int(match.group(3))
        covered = total - missed
        return {
            'percent': percent,
            'lines': f'{covered}/{total}'
        }

    # Check for stub files (2 statements, all missed)
    stub_pattern = rf'individual_solutions/{re.escape(solution_file)}\s+2\s+2\s+0\s+0\s+0%'
    if re.search(stub_pattern, output):
        return {
            'percent': 0,
            'lines': '0/2',
            'note': 'stub'
        }

    return {'percent': 0, 'lines': '0/0'}


def extract_branch_coverage(output: str, solution_file: str) -> Dict:
    """Extract branch coverage from pytest-cov output"""
    # Look for the specific solution line with branch data
    # Format: "individual_solutions/solution_02_deepseek_cot.py   18   0   6   0   100%"
    # Fields: Name  Stmts  Miss  Branch  BrPart  Cover  Missing
    pattern = rf'individual_solutions/{re.escape(solution_file)}\s+\d+\s+\d+\s+(\d+)\s+(\d+)\s+\d+%'
    match = re.search(pattern, output)

    if match:
        total_branches = int(match.group(1))
        partial_branches = int(match.group(2))

        if total_branches > 0:
            # Branches are considered covered if not partial
            covered_branches = total_branches - partial_branches
            percent = int((covered_branches / total_branches) * 100)
            return {
                'percent': percent,
                'branches': f'{covered_branches}/{total_branches}',
                'partial': partial_branches
            }
        elif total_branches == 0:
            return {
                'percent': 100,
                'branches': '0/0',
                'partial': 0
            }

    return {'percent': 0, 'branches': '0/0', 'partial': 0}


def categorize_solution(solution_file: str, result: Dict) -> str:
    """Generate one-line explanation for the solution"""
    line_cov = result['line_coverage']
    branch_cov = result['branch_coverage']

    # Check if stub (2 lines = unparseable Gemini code)
    if line_cov.get('lines') == '2/2':
        return "Unparseable code - stub returns None"

    # Check if stub with note
    if line_cov.get('note') == 'stub':
        return "Unparseable code - stub returns None"

    # Check if test failed
    if not result['test_passed']:
        line_pct = line_cov.get('percent', 0)
        if line_pct < 30:
            return "Failed test - low coverage, likely signature mismatch"
        else:
            return "Failed test - wrong output/logic error"

    # Categorize by coverage for passing tests
    line_pct = line_cov.get('percent', 0)

    if line_pct == 100:
        return "Perfect coverage - all lines executed"
    elif line_pct >= 80:
        return "High coverage - most lines executed"
    elif line_pct >= 50:
        return "Moderate coverage - partial execution"
    elif line_pct >= 20:
        return "Low coverage - minimal execution"
    else:
        return "Very low coverage - barely tested"


def generate_coverage_table(variant: str, results: Dict) -> str:
    """Generate markdown table for one variant"""

    # Table header
    table = f"\n## {variant.replace('_', ' ').title()} Coverage Results\n\n"
    table += "| Solution | Problem | Line Coverage | Branch Coverage | Tests Passed | Explanation |\n"
    table += "|----------|---------|---------------|-----------------|--------------|-------------|\n"

    # Sort by solution number
    for prob_num in sorted(PROBLEMS.keys()):
        solution_file = f"solution_{prob_num}_{variant}.py"
        problem_info = PROBLEMS[prob_num]
        problem_desc = problem_info['name']
        test_count = problem_info['test_count']

        if solution_file not in results:
            continue

        result = results[solution_file]
        line_cov = result['line_coverage']
        branch_cov = result['branch_coverage']

        # Format test status as "passed/total"
        if result['test_passed']:
            test_status = f"{test_count}/{test_count} ✓"
        else:
            test_status = f"0/{test_count} ❌"

        explanation = categorize_solution(solution_file, result)

        # Format branch coverage with partial info if present
        branch_str = f"{branch_cov['percent']}% ({branch_cov['branches']})"
        if branch_cov.get('partial', 0) > 0:
            branch_str += f" [{branch_cov['partial']} partial]"

        table += f"| {solution_file} | {problem_desc} | "
        table += f"{line_cov['percent']}% ({line_cov['lines']}) | "
        table += f"{branch_str} | "
        table += f"{test_status} | {explanation} |\n"

    return table


def main():
    """Main execution"""

    print("="*80)
    print("Running Individual Coverage Tests")
    print("="*80)

    # Run coverage for each solution
    results = {}

    for prob_num in sorted(PROBLEMS.keys()):
        print(f"\n{'='*80}")
        print(f"Problem {prob_num}: {PROBLEMS[prob_num]['name']}")
        print(f"{'='*80}")

        for variant in VARIANTS:
            solution_file = f"solution_{prob_num}_{variant}.py"
            test_pattern = f"test_{prob_num}_{variant}"

            print(f"  Testing {solution_file}...", end=" ", flush=True)

            result = run_coverage_for_solution(solution_file, test_pattern)
            results[solution_file] = result

            # Check if it's a stub
            line_cov_str = result['line_coverage'].get('lines', '0/0')
            is_stub = line_cov_str == '2/2'

            status = "✓" if result['test_passed'] else "❌"
            line_pct = result['line_coverage'].get('percent', 0)

            if is_stub:
                print(f"{status} ({line_pct}% - STUB/unparseable)")
            else:
                print(f"{status} ({line_pct}% line coverage)")

    # Generate 4 separate tables
    print(f"\n{'='*80}")
    print("Generating Coverage Tables")
    print(f"{'='*80}")

    output_file = Path("individual_coverage_tables.md")

    with open(output_file, 'w') as f:
        f.write("# Individual Solution Coverage Tables\n")
        f.write("\nGenerated from individual solution testing\n")
        f.write(f"\nTotal solutions tested: {len(results)}\n")

        for variant in VARIANTS:
            table = generate_coverage_table(variant, results)
            f.write(table)

    print(f"\n✓ Coverage tables written to: {output_file}")

    # Save raw results as JSON for further analysis
    json_file = Path("individual_coverage_results.json")
    with open(json_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"✓ Raw results saved to: {json_file}")

    print(f"\n{'='*80}")
    print("Coverage Testing Complete!")
    print(f"{'='*80}\n")


if __name__ == '__main__':
    main()
