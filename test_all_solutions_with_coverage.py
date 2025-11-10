"""
Comprehensive Coverage Testing for Multiple LLM Solutions

This script:
1. Loads solutions from part_2_testing_results (2 models × 2 strategies = 4 solutions per problem)
2. Dynamically creates solution modules for each variant
3. Runs pytest with coverage to measure how well tests cover each solution
4. Generates coverage reports comparing all 4 solutions per problem

Usage:
    python test_all_solutions_with_coverage.py

Requirements:
    - pytest
    - pytest-cov
"""

import json
import os
import sys
import shutil
from pathlib import Path
from typing import Dict, List, Any
import subprocess


class SolutionExtractor:
    """Extracts and organizes solutions from test results"""

    def __init__(self, results_dir: str = "part_2_testing_results"):
        self.results_dir = Path(results_dir)
        self.solutions = {}  # problem_id -> {model_strategy: {name, code}}

    def load_results(self) -> Dict[str, Any]:
        """Load all JSON result files"""
        results = {}

        for json_file in self.results_dir.glob("*.json"):
            with open(json_file, 'r') as f:
                data = json.load(f)
                model_name = self._extract_model_name(data['model'])
                results[model_name] = data

        return results

    def _extract_model_name(self, full_model_name: str) -> str:
        """Extract short model name (e.g., 'deepseek' from 'deepseek/deepseek-chat-v3')"""
        if 'deepseek' in full_model_name.lower():
            return 'deepseek'
        elif 'gemini' in full_model_name.lower():
            return 'gemini'
        else:
            return full_model_name.split('/')[-1]

    def extract_all_solutions(self) -> Dict[str, Dict[str, Dict[str, str]]]:
        """
        Extract all solutions organized by problem

        Returns:
            {
                'problem_0': {
                    'deepseek_cot': {'name': 'func_name', 'code': '...'},
                    'deepseek_self_planning': {...},
                    'gemini_cot': {...},
                    'gemini_self_planning': {...}
                },
                ...
            }
        """
        results = self.load_results()
        solutions = {}

        for model_name, data in results.items():
            if 'tests' not in data:
                continue

            for problem_id, problem_data in data['tests'].items():
                if problem_id not in solutions:
                    solutions[problem_id] = {}

                # Extract solutions for each strategy
                for strategy_name, strategy_data in problem_data.get('strategies', {}).items():
                    variant_name = f"{model_name}_{strategy_name}"

                    # Only include if code exists and is non-empty
                    if strategy_data.get('code') and strategy_data.get('name'):
                        solutions[problem_id][variant_name] = {
                            'name': strategy_data['name'],
                            'code': strategy_data['code']
                        }

        return solutions


class SolutionModuleGenerator:
    """Generates Python modules for each solution variant"""

    def __init__(self, output_dir: str = "multi_solution_variants"):
        self.output_dir = Path(output_dir)

    def generate_all_modules(self, solutions: Dict[str, Dict[str, Dict[str, str]]]):
        """Generate solution modules for all problems and variants"""

        # Clean and recreate output directory
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True)

        # Create __init__.py to make it a package
        (self.output_dir / "__init__.py").write_text("")

        # Generate a module for each problem
        for problem_id, variants in solutions.items():
            self._generate_problem_module(problem_id, variants)

    def _generate_problem_module(self, problem_id: str, variants: Dict[str, Dict[str, str]]):
        """Generate a single module containing all variants for one problem"""

        module_path = self.output_dir / f"{problem_id}.py"

        lines = [
            f'"""Solutions for {problem_id} - All variants"""',
            '',
            '# This file is auto-generated. Do not edit manually.',
            ''
        ]

        for variant_name, solution_data in variants.items():
            function_name = solution_data['name']
            code = solution_data['code']

            # Create a unique function name for this variant
            variant_function_name = f"{function_name}_{variant_name}"

            lines.append(f"# ========== {variant_name.upper()} ==========")
            lines.append("")

            # Replace the original function name with variant-specific name
            modified_code = self._rename_function(code, function_name, variant_function_name)
            lines.append(modified_code)
            lines.append("")
            lines.append("")

        module_path.write_text('\n'.join(lines))

    def _rename_function(self, code: str, old_name: str, new_name: str) -> str:
        """Rename function definition (handle both 'def' and 'class')"""
        lines = code.split('\n')
        modified_lines = []

        for line in lines:
            # Replace function definition
            if line.strip().startswith(f'def {old_name}('):
                line = line.replace(f'def {old_name}(', f'def {new_name}(', 1)
            # Replace class definition (if it's a class method)
            elif line.strip().startswith(f'class {old_name}'):
                line = line.replace(f'class {old_name}', f'class {new_name}', 1)

            modified_lines.append(line)

        return '\n'.join(modified_lines)


class TestFileGenerator:
    """Generates pytest test file that tests all variants"""

    def __init__(self, test_file_path: str = "test_multi_solutions.py"):
        self.test_file_path = Path(test_file_path)

    def generate_test_file(self, solutions: Dict[str, Dict[str, Dict[str, str]]]):
        """Generate comprehensive test file for all solutions"""

        lines = [
            '"""',
            'Auto-generated pytest file to test all solution variants with coverage',
            '',
            'Run with:',
            '    pytest test_multi_solutions.py -v',
            '',
            'Run with coverage:',
            '    pytest test_multi_solutions.py -v --cov=multi_solution_variants --cov-report=html --cov-report=term-missing',
            '"""',
            '',
            'import pytest',
            'import sys',
            'from pathlib import Path',
            '',
            '# Add multi_solution_variants to path',
            'sys.path.insert(0, str(Path(__file__).parent / "multi_solution_variants"))',
            '',
        ]

        # Generate test classes based on the original test_all_problems.py structure
        test_definitions = self._get_test_definitions()

        for problem_id in sorted(solutions.keys()):
            if problem_id not in test_definitions:
                continue

            problem_num = int(problem_id.split('_')[1])
            test_def = test_definitions[problem_id]
            variants = solutions[problem_id]

            lines.append(f"# ========== Problem {problem_num} Tests ==========")
            lines.append(f'class Test{test_def["class_name"]}:')
            lines.append(f'    """')
            lines.append(f'    {test_def["description"]}')
            lines.append(f'    """')
            lines.append('')

            # Generate test methods for each variant
            for variant_name in sorted(variants.keys()):
                function_name = variants[variant_name]['name']
                variant_function_name = f"{function_name}_{variant_name}"

                for test_idx, test_case in enumerate(test_def['test_cases']):
                    test_method_name = f"test_{variant_name}_{test_idx + 1}"

                    lines.append(f"    def {test_method_name}(self):")
                    lines.append(f'        """Test {variant_name} variant - case {test_idx + 1}"""')

                    # Import the variant function
                    lines.append(f"        try:")
                    lines.append(f"            from {problem_id} import {variant_function_name}")
                    lines.append(f"        except ImportError:")
                    lines.append(f'            pytest.skip("Solution not available")')
                    lines.append(f"")

                    # Add the test assertion
                    assertion = self._generate_assertion(
                        variant_function_name,
                        test_case['input'],
                        test_case['expected']
                    )
                    lines.append(f"        {assertion}")
                    lines.append("")

            lines.append("")

        self.test_file_path.write_text('\n'.join(lines))

    def _get_test_definitions(self) -> Dict[str, Dict]:
        """Define test cases for each problem based on test_all_problems.py"""

        return {
            'problem_0': {
                'class_name': 'Problem0Base91',
                'description': 'Problem 0: Base91 Encode/Decode',
                'test_cases': [
                    {'input': '">OwJh>Io0Tv!8PE"', 'expected': '"Hello World!"'},
                    {'input': '"fPNKd"', 'expected': '"test"'},
                ]
            },
            'problem_1': {
                'class_name': 'Problem1MaxPizza',
                'description': 'Problem 1: Maximum Pizza Slices',
                'test_cases': [
                    {'input': '[1, 2, 3, 4, 5, 6]', 'expected': '10'},
                ]
            },
            'problem_2': {
                'class_name': 'Problem2AllBlue',
                'description': 'Problem 2: Number of Times All Blue',
                'test_cases': [
                    {'input': '[2, 1, 3, 5, 4]', 'expected': '3'},
                ]
            },
            'problem_3': {
                'class_name': 'Problem3UnhappyFriends',
                'description': 'Problem 3: Unhappy Friends',
                'test_cases': [
                    {'input': '4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]]', 'expected': '2'},
                ]
            },
            'problem_4': {
                'class_name': 'Problem4MinSwaps',
                'description': 'Problem 4: Minimum Swaps to Make Grid Valid',
                'test_cases': [
                    {'input': '[[0, 0, 1], [1, 1, 0], [1, 0, 0]]', 'expected': '3'},
                ]
            },
            'problem_5': {
                'class_name': 'Problem5Mix',
                'description': 'Problem 5: Mix Strings',
                'test_cases': [
                    {'input': '"looping is fun but dangerous", "less dangerous than coding"', 'expected': '"1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"'},
                    {'input': '"Are they here", "yes, they are here"', 'expected': '"2:eeeee/2:yy/=:hh/=:rr"'},
                    {'input': '"Lords of the Fallen", "gamekult"', 'expected': '"1:ee/1:ll/1:oo"'},
                ]
            },
            'problem_6': {
                'class_name': 'Problem6ContainsCycle',
                'description': 'Problem 6: Contains Cycle in Grid',
                'test_cases': [
                    {'input': '[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]', 'expected': 'True'},
                ]
            },
            'problem_7': {
                'class_name': 'Problem7DISequence',
                'description': 'Problem 7: Number of Permutations with DI Sequence',
                'test_cases': [
                    {'input': '"DID"', 'expected': '5'},
                ]
            },
            'problem_8': {
                'class_name': 'Problem8MaxValueReverse',
                'description': 'Problem 8: Maximum Value After Reverse',
                'test_cases': [
                    {'input': '[2, 3, 1, 5, 4]', 'expected': '10'},
                ]
            },
            'problem_9': {
                'class_name': 'Problem9LeastOps',
                'description': 'Problem 9: Least Operators to Express Target',
                'test_cases': [
                    {'input': '3, 19', 'expected': '5'},
                ]
            },
            'problem_10': {
                'class_name': 'Problem10ExchangeSort',
                'description': 'Problem 10: Exchange Sort',
                'test_cases': [
                    {'input': '[9, 9, 7, 7, 8, 8]', 'expected': '4'},
                    {'input': '[8, 8, 7, 8]', 'expected': '1'},
                    {'input': '[9, 7, 9]', 'expected': '1'},
                ]
            },
            'problem_11': {
                'class_name': 'Problem11MinimumTotal',
                'description': 'Problem 11: Minimum Total (Triangle)',
                'test_cases': [
                    {'input': '[[-10]]', 'expected': '-10'},
                    {'input': '[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]', 'expected': '11'},
                ]
            },
            'problem_12': {
                'class_name': 'Problem12LongestConsecutive',
                'description': 'Problem 12: Longest Consecutive Sequence',
                'test_cases': [
                    {'input': '[100, 4, 200, 1, 3, 2]', 'expected': '4'},
                ]
            },
            'problem_13': {
                'class_name': 'Problem13LongestCommonSubseq',
                'description': 'Problem 13: Longest Common Subsequence',
                'test_cases': [
                    {'input': '"abcde", "ace"', 'expected': '3'},
                ]
            },
        }

    def _generate_assertion(self, function_name: str, input_str: str, expected_str: str) -> str:
        """Generate assertion statement for a test case"""

        # For class-based solutions (like Solution.method)
        if '.' not in function_name:
            # Regular function call
            return f"assert {function_name}({input_str}) == {expected_str}"
        else:
            # Class method (e.g., Solution().maxSizeSlices)
            class_name = function_name.split('.')[0]
            method_name = function_name.split('.')[1]
            return f"assert {class_name}().{method_name}({input_str}) == {expected_str}"


class CoverageRunner:
    """Runs pytest with coverage and generates reports"""

    def __init__(self, test_file: str = "test_multi_solutions.py"):
        self.test_file = test_file
        self.python_cmd = self._get_python_executable()

    def _get_python_executable(self) -> list:
        """Get the appropriate Python executable (prefer uv run if available)"""
        # Check if we're in a uv-managed project
        if Path("pyproject.toml").exists() and shutil.which("uv"):
            return ["uv", "run", "python"]
        # Check if we're in an activated venv
        elif hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            return [sys.executable]
        # Fall back to system Python
        else:
            return [sys.executable]

    def _check_pytest_cov_installed(self) -> bool:
        """Check if pytest-cov is installed"""
        try:
            # Try importing pytest_cov module directly
            result = subprocess.run(
                self.python_cmd + ["-c", "import pytest_cov"],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except:
            return False

    def run_coverage_tests(self):
        """Run pytest with coverage reporting"""

        print("\n" + "="*80)
        print("Running Coverage Tests for All Solution Variants")
        print("="*80 + "\n")

        # Check if pytest-cov is available
        has_coverage = self._check_pytest_cov_installed()

        if has_coverage:
            print("✓ pytest-cov detected - running with coverage analysis\n")
            # Run pytest with coverage
            cmd = self.python_cmd + [
                "-m", "pytest",
                self.test_file,
                "-v",
                "--cov=multi_solution_variants",
                "--cov-report=html:coverage_html",
                "--cov-report=term-missing",
                "--cov-branch",
                "--tb=short"
            ]
        else:
            print("⚠ pytest-cov not found - running tests without coverage")
            print("  To enable coverage, install: pip install pytest-cov\n")
            # Run pytest without coverage
            cmd = self.python_cmd + [
                "-m", "pytest",
                self.test_file,
                "-v",
                "--tb=short"
            ]

        try:
            result = subprocess.run(cmd, check=False, capture_output=False)

            if has_coverage:
                print("\n" + "="*80)
                print("Coverage report generated in: coverage_html/index.html")
                print("="*80 + "\n")

            return result.returncode == 0

        except Exception as e:
            print(f"Error running tests: {e}")
            return False


def main():
    """Main orchestration function"""

    print("="*80)
    print("Multi-Solution Coverage Testing Tool")
    print("="*80)
    print()

    # Step 1: Extract solutions
    print("Step 1: Extracting solutions from JSON results...")
    extractor = SolutionExtractor()
    solutions = extractor.extract_all_solutions()

    total_problems = len(solutions)
    total_variants = sum(len(variants) for variants in solutions.values())
    print(f"  ✓ Found {total_problems} problems with {total_variants} total solution variants")

    for problem_id in sorted(solutions.keys()):
        variant_count = len(solutions[problem_id])
        print(f"    - {problem_id}: {variant_count} variants")

    # Step 2: Generate solution modules
    print("\nStep 2: Generating solution modules...")
    generator = SolutionModuleGenerator()
    generator.generate_all_modules(solutions)
    print(f"  ✓ Generated modules in: multi_solution_variants/")

    # Step 3: Generate test file
    print("\nStep 3: Generating test file...")
    test_generator = TestFileGenerator()
    test_generator.generate_test_file(solutions)
    print(f"  ✓ Generated test file: test_multi_solutions.py")

    # Step 4: Run coverage tests
    print("\nStep 4: Running coverage tests...")
    runner = CoverageRunner()
    success = runner.run_coverage_tests()

    if success:
        print("\n✓ All tests completed successfully!")
    else:
        print("\n⚠ Some tests failed or errors occurred")

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
