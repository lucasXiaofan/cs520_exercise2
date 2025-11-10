# CS520 Exercise 2: Automated Testing & Coverage Analysis

**Author:** XiaoFan Lu
**GitHub:** https://github.com/lucasXiaofan/cs520_exercise2

## Overview

This project evaluates automated testing and code coverage for LLM-generated solutions, following a three-part analysis:
1. **Part 1:** Baseline coverage measurement of Exercise 1 solutions
2. **Part 2:** Iterative test improvement using LLM-assisted test generation
3. **Part 3:** Fault detection validation through seeded bug analysis

**Key Finding:** Branch coverage targeting error paths and exception handling provides significantly better fault detection (5x improvement) than simple line coverage.

---

## Repository Structure

```
cs520_exercise2/
├── README.md                              # This file
├── coverage_analysis.md                   # Complete analysis report (all parts)
├── llm_code_agent.py                      # LLM agent for test generation
│
├── multi_solution_variants/               # Part 1: Exercise 1 solutions (4 variants per problem)
│   ├── solution_02_*.py through solution_14_*.py
│   └── test_*.py                          # Original test files
│
├── exercise2_part2_bcb_solutions/         # Part 2: BigCodeBench solutions
│   ├── solution_*_15.py                   # Problem 15 solutions (4 variants)
│   ├── solution_*_17.py                   # Problem 17 solutions (4 variants)
│   ├── solution_*_buggy.py                # Part 3: Buggy versions
│   └── __init__.py
│
├── exercise2_part2_bcb_2problems/         # Part 2: Test suites
│   ├── test_BigCodeBench_15.py            # 26 tests (19 added iteratively)
│   └── test_BigCodeBench_17.py            # 29 tests (27 added iteratively)
│
└── coverage_html_all/                     # Coverage reports (HTML)
    └── index.html                         # Open this to view coverage
```

---

## Part 1: Baseline Coverage

**Objective:** Measure coverage of Exercise 1 solutions using original benchmark tests.

### Models & Prompts Used
- **DeepSeek V3** (`deepseek/deepseek-chat-v3`) with Chain-of-Thought and Self-Planning
- **Gemini Flash 2.0** (`gemini-2.0-flash-exp`) with Chain-of-Thought and Self-Planning

### Summary Results

| Problem | Tests Passed | Line Coverage | Branch Coverage | Notes |
|---------|-------------|---------------|-----------------|-------|
| Maximum Pizza Slices | 1/1 ✓ | 4.3% (2/46) | 20 branches | Low coverage - only 3 parseable solutions, single test insufficient |
| Number of Times All Blue | 1/1 ✓ | 8.0% (2/25) | 12 branches | Low coverage - 3 solutions, most edge cases untested |
| Unhappy Friends | 1/1 ✓ | 2.2% (2/92) | 62 branches | Very low - complex nested logic barely touched |
| Minimum Swaps to Make Grid Valid | 1/1 ✓ | 64.8% (46/71) | 42 branches | Good coverage - main swap logic well exercised |
| Mix Strings | 3/3 ✓ | 100% (46/46) | 34 branches | Perfect coverage - 3 diverse tests cover all paths |
| Contains Cycle in Grid | 1/1 ✓ | 28.9% (26/90) | 68 branches | Low - DFS recursion barely explored |
| Number of Permutations with DI Sequence | 1/1 ✓ | 37.8% (17/45) | 34 branches | Low - DP state space mostly untested |
| Least Operators to Express Target | 1/1 ✓ | 12.8% (5/39) | 20 branches | Very low - complex recursive DP minimally tested |
| Longest Common Subsequence | 1/1 ✓ | 8.1% (3/37) | 18 branches | Very low - 2D DP table logic untested |
| Exchange Sort | 3/3 ✓ | 17.1% (7/41) | 24 branches | Low - swap counting logic largely untested |
| Minimum Total (Triangle) | 2/2 ✓ | 70.2% (40/57) | 34 branches | Good - bottom-up DP mostly covered |
| Longest Consecutive Sequence | 1/1 ✓ | 8.3% (2/24) | 18 branches | Very low - hash-based logic barely touched |

**Full report:** See `coverage_analysis.md` Part 1

### How to Reproduce

```bash
# View HTML coverage report
open coverage_html_all/index.html

# Or regenerate coverage
cd multi_solution_variants
uv run pytest --cov=. --cov-report=html --cov-report=term
```

---

## Part 2: LLM-Assisted Test Improvement

**Objective:** Use LLM agents to iteratively improve test coverage until convergence.

### Problems Selected
- **BigCodeBench 15:** CSV Command Executor (subprocess, CSV parsing, error handling)
- **BigCodeBench 17:** Process Manager (psutil, process lifecycle, exception handling)

### Benchmark Change Justification
The original APP benchmark from Exercise 1 was too simple - uncovered branches were unreachable with valid inputs. BigCodeBench provides more realistic, production-like code challenges requiring comprehensive error handling and edge case testing.

### Prompt Used

```
go to folder exercise2_part2_bcb_2problems, for each problem
check its relevant solution in exercise2_part2_bcb_solutions
do not modify existing test cases, add new test cases to increase the line or branch coverage, prevent duplicate test cases.
you need comments the new test cases you created, to specify from the old one.
after append new testcases to both problems,
summarize in few sentence what you improved,
if nothing to add explain why
your task is done
```

**Execution:** `python llm_code_agent.py`

### Iterative Results

#### Problem 15: CSV Command Executor

| Iteration | Coverage | Change | Tests Added | Focus |
|-----------|----------|--------|-------------|-------|
| Baseline | 52% | - | 6 tests | Initial test suite |
| 1 | 54% | +2% | 6 tests | Exception handling (timeout, stderr, directory creation) |
| 2 | 56% | +2% | 2 tests | Return value formats, file write operations |
| 3 | 58% | +2% | 11 tests | CSV edge cases, unicode, metacharacters, long output |
| **Final** | **58%** | **+6%** | **19 total** | - |

#### Problem 17: Process Manager

| Iteration | Coverage | Change | Tests Added | Focus |
|-----------|----------|--------|-------------|-------|
| Baseline | 28% | - | 3 tests | Basic process operations |
| 1 | 30% | +2% | 12 tests | psutil exceptions (NoSuchProcess, AccessDenied, ZombieProcess) |
| 2 | 31% | +1% | 5 tests | Edge cases, special characters, empty iterators |
| 3 | 31% | 0% | 10 tests | Popen exceptions, wait logic, complete termination flows |
| **Final** | **31%** | **+3%** | **27 total** | - |

**Convergence:** Problem 17 plateaued at iteration 3 (0% improvement), suggesting remaining uncovered lines require system-level conditions or are defensive unreachable code.

**Redundancy Prevention:** LLM was explicitly prompted to "read the entire test file and prevent duplicate test cases" in each iteration.

**Full iteration details:** See `coverage_analysis.md` Part 2

### How to Reproduce

```bash
# Run tests with coverage
uv run pytest exercise2_part2_bcb_2problems/test_BigCodeBench_15.py --cov=../exercise2_part2_bcb_solutions --cov-report=html --cov-report=term
uv run pytest exercise2_part2_bcb_2problems/test_BigCodeBench_17.py --cov=../exercise2_part2_bcb_solutions --cov-report=html --cov-report=term

# View coverage reports
open bcbp15_html/index.html
# or 
open bcbp17_html/index.html
```

---

## Part 3: Fault Detection Analysis

**Objective:** Validate that coverage improvements actually catch bugs through seeded bug testing.

### Problem 15: CSV Command Executor

**Bugs Injected:**
1. **Off-by-one error:** `command_index = 0` instead of `1` (mixing 0-based vs 1-based indexing)
2. **Wrong return code check:** `returncode != 1` instead of `== 0` (misunderstanding error codes)
3. **Missing whitespace filter:** Incomplete CSV edge case handling

**Results:** 7 out of 26 tests failed (27% failure rate)

**Tests that caught bugs:**
- All 7 failures from bug #2 (wrong return code check)
- `test_invalid_command`, `test_command_with_timeout`, `test_mixed_commands`, etc.
- Tests specifically checking error message output caught the bug immediately

**Gap identified:** Off-by-one bug not caught because tests verify file existence, not exact filenames

### Problem 17: Process Manager

**Bugs Injected:**
1. **Substring matching:** `process_name in proc.name()` instead of `== proc.name()` (over-matching)
2. **Missing exception handling:** Only caught `NoSuchProcess`, dropped `AccessDenied` and `ZombieProcess`
3. **No wait after terminate:** Missing `proc.wait()` causing race conditions

**Results:** 15 out of 29 tests failed (52% failure rate)

**Tests that caught bugs:**
- 8 crashes from missing exception handling (bug #2)
- 6 failures from missing wait logic (bug #3)
- Exception handling tests from iteration 1 were critical - without them, only 3/15 bugs would've been caught

### Key Findings

✅ **Branch coverage >> line coverage** - All bugs caught were in error paths
✅ **Iterative improvement = 5x fault detection** - Exception handling tests from iterations 1-3 were the bug finders
❌ **Coverage isn't perfect** - Off-by-one bug slipped through behavioral tests
💡 **ROI insight:** Focus on error paths, exception handling, and boundary conditions

**Full analysis:** See `coverage_analysis.md` Part 3

### How to Reproduce Seeded Bug Testing

```bash
# Buggy versions are in exercise2_part2_bcb_solutions/solution_*_buggy.py

# Temporarily modify test files to use buggy versions
# In test_BigCodeBench_15.py, change SOLUTION_MODULES to:
# ["exercise2_part2_bcb_solutions.solution_anthropic_claude_haiku_4_5_15_buggy"]

# Run tests
uv run pytest test_BigCodeBench_15.py -v
uv run pytest test_BigCodeBench_17.py -v

# Restore original SOLUTION_MODULES after testing
```

---

## Deliverables Checklist

- ✅ **Baseline coverage table** (Part 1) - See above and `coverage_analysis.md`
- ✅ **LLM prompts** (Part 2) - See "Prompt Used" section
- ✅ **Before/after coverage** (Part 2) - See "Iterative Results" tables
- ✅ **Fault detection write-up** (Part 3) - See above and `coverage_analysis.md`
- ✅ **GitHub repository** - https://github.com/lucasXiaofan/cs520_exercise2
  - ✅ Exercise 1 source code (`multi_solution_variants/`)
  - ✅ Test files - baseline + improved (`exercise2_part2_bcb_2problems/`)
  - ✅ Coverage scripts/configs (`pyproject.toml`, test commands above)
  - ✅ HTML coverage reports (`coverage_html_all/index.html`)

---

## Tools & Dependencies

**Python:** 3.11+
**Testing:** pytest, pytest-cov
**LLM Agent:** Custom implementation using Claude Sonnet 4.5

### Installation

```bash
# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

---

## Key Takeaways

1. **Simple benchmarks hide problems** - APP benchmark was too basic; BigCodeBench revealed real testing challenges
2. **LLM test generation works** - Systematic prompt engineering can improve coverage 6%+ with targeted tests
3. **Convergence happens** - Coverage plateaus when remaining code requires system-level conditions
4. **Branch coverage = bug detection** - Error paths and exception handling have 5x better fault detection ROI
5. **Coverage ≠ correctness** - High coverage doesn't guarantee semantic correctness (off-by-one example)

**Bottom line:** Invest in branch coverage for error paths, not just line coverage for happy paths.

---

## References

- BigCodeBench: https://github.com/bigcode-project/bigcodebench
