"""
Generate individual solution files for each LLM+prompt combination

This script creates 40 separate solution files:
- 10 problems (based on coverage_analysis.md)
- 4 variants each (deepseek_cot, deepseek_self_planning, gemini_cot, gemini_self_planning)

Output: individual_solutions/ directory with files like:
  - solution_02_deepseek_cot.py
  - solution_02_deepseek_self_planning.py
  - solution_02_gemini_cot.py
  - solution_02_gemini_self_planning.py
  - ...
"""

import os
import re
from pathlib import Path
from typing import Dict, Optional

# Mapping from coverage_analysis.md solution files to problem files
PROBLEM_MAPPING = {
    'solution_2': ('problem_1', 'Maximum Pizza Slices', 'maxSizeSlices'),
    'solution_3': ('problem_2', 'Number of Times All Blue', 'numTimesAllBlue'),
    'solution_4': ('problem_3', 'Unhappy Friends', 'unhappyFriends'),
    'solution_5': ('problem_4', 'Minimum Swaps to Make Grid Valid', 'minSwaps'),
    'solution_6': ('problem_5', 'Mix Strings', 'mix'),
    'solution_7': ('problem_6', 'Contains Cycle in Grid', 'containsCycle'),
    'solution_8': ('problem_7', 'Number of Permutations with DI Sequence', 'numPermsDISequence'),
    'solution_10': ('problem_9', 'Least Operators to Express Target', 'leastOpsExpressTarget'),
    'solution_11': ('problem_13', 'Longest Common Subsequence', 'longestCommonSubsequence'),
    'solution_12': ('problem_10', 'Exchange Sort', 'exchangeSort'),
}

VARIANTS = ['deepseek_cot', 'deepseek_self_planning', 'gemini_cot', 'gemini_self_planning']

def extract_solution_code(problem_file: Path, variant: str, function_name: str) -> Optional[str]:
    """Extract solution code for a specific variant from problem file"""
    if not problem_file.exists():
        return None

    content = problem_file.read_text()

    # Find the section for this variant
    variant_upper = variant.upper()
    pattern = rf'# =+ {re.escape(variant_upper)} =+\s*\n(.*?)(?=\n# =+|$)'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        code = match.group(1).strip()
        if code and not code.startswith('# No solution'):
            # Convert class methods to standalone functions
            code = convert_to_standalone_function(code, function_name, variant)
            return code

    return None


def convert_to_standalone_function(code: str, base_function_name: str, variant: str) -> str:
    """Convert class method or rename standalone function to match expected name"""

    # Add common imports at the top
    imports = """from typing import List, Optional, Dict, Set, Tuple
from collections import defaultdict, deque, Counter
import heapq
import functools

"""

    lines = code.split('\n')

    # Check if it's a class definition
    if code.strip().startswith('class'):
        # Find the method definition inside the class
        result_lines = []
        found_method = False
        method_indent = 0
        in_class = False

        for i, line in enumerate(lines):
            # Skip the class declaration line
            if line.strip().startswith('class '):
                in_class = True
                continue

            # Look for method definition with 'self' parameter
            if in_class and 'def ' in line and '(self' in line:
                # Extract parameters (everything after 'self, ')
                # Handle return type annotations like -> int:
                match = re.search(r'def\s+\w+\(self(?:,\s*)?(.*?)\)(?:\s*->\s*.*?)?:', line)
                if match:
                    params = match.group(1)
                    # Start of new standalone function
                    result_lines.append(f'def {base_function_name}({params}):')
                    found_method = True
                    method_indent = len(line) - len(line.lstrip())
                    continue

            if found_method:
                # Remove class-level indentation (one level)
                if line.strip():  # Non-empty line
                    current_indent = len(line) - len(line.lstrip())
                    # Check if we've left the method (back to class level or less)
                    if current_indent <= method_indent and line.strip() and not line.strip().startswith('#'):
                        break
                    # Remove one indentation level (4 spaces)
                    if current_indent > method_indent:
                        result_lines.append(line[4:])
                    else:
                        result_lines.append(line)
                else:
                    result_lines.append(line)

        if found_method:
            return imports + '\n'.join(result_lines)

    # If it's already a standalone function, just rename it if needed
    func_pattern = rf'def (\w+)\('
    func_match = re.search(func_pattern, code)

    if func_match:
        old_func_name = func_match.group(1)
        # Replace the function name
        code = re.sub(rf'def {re.escape(old_func_name)}\(',
                     f'def {base_function_name}(', code, count=1)

    return imports + code

def create_stub_solution(function_name: str, description: str) -> str:
    """Create stub function that returns None for unparseable code"""
    return f'''"""
{description}

This solution was not parseable from the LLM output.
"""

def {function_name}(*args, **kwargs):
    """Unparseable solution - returns None"""
    return None
'''

def generate_solution_file(
    solution_id: str,
    problem_id: str,
    description: str,
    function_name: str,
    variant: str,
    output_dir: Path
):
    """Generate individual solution file for one variant"""

    # Read from multi_solution_variants
    problem_file = Path('multi_solution_variants') / f'{problem_id}.py'

    code = extract_solution_code(problem_file, variant, function_name)

    # Format output filename: solution_02_deepseek_cot.py
    solution_num = solution_id.replace('solution_', '')
    output_filename = f'solution_{solution_num:0>2}_{variant}.py'
    output_path = output_dir / output_filename

    if code:
        # Use extracted code
        header = f'''"""
{description}
Variant: {variant}
"""

'''
        full_content = header + code + '\n'
    else:
        # Create stub for unparseable code
        full_content = create_stub_solution(function_name,
                                            f"{description}\nVariant: {variant}")

    output_path.write_text(full_content)
    print(f"  Created: {output_filename} {'(stub)' if not code else ''}")

def main():
    """Generate all individual solution files"""

    print("="*80)
    print("Generating Individual Solution Files")
    print("="*80)

    # Create output directory
    output_dir = Path('individual_solutions')
    if output_dir.exists():
        import shutil
        shutil.rmtree(output_dir)
    output_dir.mkdir()

    # Create __init__.py
    (output_dir / '__init__.py').write_text('')

    # Generate solution files
    total_created = 0
    total_stubs = 0

    for solution_id, (problem_id, description, function_name) in PROBLEM_MAPPING.items():
        print(f"\n{solution_id} ({description}):")

        for variant in VARIANTS:
            problem_file = Path('multi_solution_variants') / f'{problem_id}.py'
            code = extract_solution_code(problem_file, variant, function_name)

            generate_solution_file(
                solution_id, problem_id, description,
                function_name, variant, output_dir
            )

            total_created += 1
            if not code:
                total_stubs += 1

    print(f"\n{'='*80}")
    print(f"Total files created: {total_created}")
    print(f"Stub files (unparseable): {total_stubs}")
    print(f"Parseable files: {total_created - total_stubs}")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
