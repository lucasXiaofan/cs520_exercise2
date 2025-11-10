# Assignment Instruction


# Exercise 2: Automated Testing & Coverage

**Assignment Type:** Individual  
**Submission:** Must be completed and submitted independently by each student.  
**Deadline:** Nov 10, 11:59PM EST (late submissions not accepted)

_Submit via GradeScope. For late submission approval, contact TA Abhishek Varghese (avarghese@umass.edu) at least 24 hours in advance (exceptions for last-minute emergencies)._  
_Accepted extension reasons: medical, religious/funerary, university events (conference, athletic, field trip, performance), extenuating non-academic (military, illness, jury duty, car accident). Other course deadlines or interviews are **not** legitimate reasons._

***

## Objective

Using your solutions from **Exercise 1**, design and run automated tests, and collect code coverage with automated tools:
- Measure baseline coverage.
- Use LLMs to improve tests.
- Analyze coverage vs. fault detection.

***

## Scope & Prerequisites

- Use the same problems you completed in Exercise 1.
- Keep original prompts and solutions accessible for reference.
- **Languages:** Java or Python.
  - Java: JaCoCo
  - Python: `pytest-cov`

***

## Part 1 — Baseline Coverage (30% – 6 points)

1. Set up automated coverage collection for your A1 solutions (_use tests from your benchmark_).
2. For each problem, report at least:
   - Number of tests passed
   - Line coverage and branch coverage (if supported)
   - One-line interpretation (e.g., "low branch coverage due to untested error path")
3. Include a **single summary table** for all problems:  
   `problem → line %, branch %, notes`

***

## Part 2 — LLM-Assisted Test Generation & Coverage Improvement (50% – 10 points)

Select **two** problem sets (problem, benchmark test suite, LLM solution) with room for improvement.

1. Prompt an LLM to produce new or improved unit tests.
   - _Example:_ “Produce tests that increase branch coverage for conditions X/Y.”
2. Run coverage again using new/improved tests.
3. For each problem:
   - Prompts used to generate tests (paste in your report)
   - Before/after coverage numbers (line & branch) and brief explanation
   - Note on redundancy (did the LLM produce duplicate/near-duplicate tests? De-duplication process)
4. Repeat steps 1–3, accumulating LLM-generated tests until **convergence**.
   - _Convergence criteria:_ Coverage(i) - Coverage(i-2) ≤ 3% for 3 consecutive iterations.
   - Prefer branch coverage for convergence if supported; otherwise, use line coverage.

***

## Part 3 — Fault Detection Check (20% – 4 points)

Coverage alone isn’t enough. Evaluate whether your test suite catches bugs.

For each of the two problems, choose one:
- **Seeded bug check:** Introduce a small, realistic bug (_off-by-one, wrong boundary, exception handling, etc._) into your A1 solution and re-run tests. Did they fail?
- **Buggy baseline comparison:** Run tests against a known buggy version (e.g., earlier failed Exercise 1 attempt). Did improved tests catch the bug?

**Report for each:**
- The bug you injected/compared, and why it’s realistic
- Whether tests failed as expected and which tests caught it
- Short conclusion linking coverage ↔ fault detection (e.g., “branch ↑ uncovered the else path that exposed the bug”)

***

## Tooling Requirements

- **Python:** pytest, pytest-cov, coverage (HTML + XML reports)
- **Java:** JaCoCo (Gradle `jacocoTestReport` or Maven `jacoco:report`)

***

## Deliverables

Submit **one PDF document** on the course platform.

Include:
- Baseline coverage table (Part 1)
- LLM prompts for two problems (Part 2)
- Before/after coverage numbers and commentary (Part 2)
- Fault detection write-up (bug injected, which tests caught it) (Part 3)
- **GitHub repo link** containing:
  - Source code from Exercise 1
  - Test files (baseline + improved)
  - Scripts/configs for coverage
  - Coverage reports (HTML/XML), or instructions to reproduce locally

***

## Resources

- [pytest documentation](https://docs.pytest.org/en/stable/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/index.html)
- [Pytest + Coverage.py video](https://youtu.be/6toeRpugWjI?si=KiCUo2Selb9CAyzs)
- [How to create tests in python (video)](https://youtu.be/EgpLj86ZHFQ?si=cAVztZeUn8FIKUbE)
- [Article - LambdaTest: What is Pytest Coverage & Generate Pytest Coverage Report](https://www.lambdatest.com/blog/pytest-code-coverage-report/)
- [Article - Pytest with Eric: How To Generate Beautiful & Comprehensive Pytest Code Coverage Reports](https://pytest-with-eric.com/pytest-best-practices/pytest-code-coverage-reports/#Testing-With-Random-Data-%E2%80%94-Good-Idea)

