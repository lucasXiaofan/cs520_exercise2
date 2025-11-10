"""
DSPy Code Agent for Test Generation with Branch Coverage Analysis

This agent uses DSPy's ReAct pattern to:
1. Read source code files
2. Run coverage analysis with pytest
3. Identify uncovered branches
4. Generate new test cases to increase branch coverage

Usage:
    agent = create_test_agent()
    result = agent(
        file_path="path/to/solution.py",
        test_file_path="path/to/test_file.py"
    )
"""

import dspy
import os
import subprocess
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables and configure DSPy
load_dotenv()
model_name = "deepseek/deepseek-chat-v3"
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)
lm = dspy.LM(
    model_name,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    api_base="https://openrouter.ai/api/v1"
)
dspy.configure(lm=lm)


def bashtool(command: str) -> str:
    """
    Execute bash commands and return the output.

    Args:
        command: The bash command to execute

    Returns:
        The stdout/stderr output from the command
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        output = result.stdout
        if result.stderr:
            output += f"\n[STDERR]: {result.stderr}"
        if result.returncode != 0:
            output += f"\n[EXIT CODE]: {result.returncode}"
        return output
    except subprocess.TimeoutExpired:
        return "[ERROR]: Command timed out after 30 seconds"
    except Exception as e:
        return f"[ERROR]: {str(e)}"

class TestGenerationSignature(dspy.Signature):
    """You are an expert software testing engineer specializing in branch coverage analysis.

    Your task is to:
    1. Analyze the given source code to understand its logic and control flow
    2. Review existing test coverage reports to identify uncovered branches
    3. Generate NEW test cases that will cover the missing branches
    4. Ensure tests are comprehensive, covering edge cases and boundary conditions

    Focus on:
    - Conditional statements (if/elif/else)
    - Loop branches (for/while)
    - Exception handling (try/except)
    - Early returns and edge cases
    - Boolean expressions and short-circuit evaluation
    """

    file_path: str = dspy.InputField(desc="Path to the source code file to analyze")
    test_file_path: str = dspy.InputField(desc="Path to the existing test file (optional)")

    analysis: str = dspy.OutputField(
        desc="Analysis of the code structure, control flow, and coverage gaps"
    )
    new_tests: str = dspy.OutputField(
        desc=(
            "Complete pytest test code that can be added to increase branch coverage. "
            "Include test class, test methods, assertions, and edge cases. "
            "Format as valid Python/pytest code."
        )
    )

agent = dspy.ReAct(
    TestGenerationSignature,
    tools=[
        bashtool,
    ]
)


class QA(dspy.Signature):
    question: str = dspy.InputField()
    history: dspy.History = dspy.InputField()
    answer: str = dspy.OutputField()

predict = dspy.Predict(QA)
history = dspy.History(messages=[])

while True:
    question = input("Type your question, end conversation by typing 'finish': ")
    if question == "finish":
        break
    outputs = predict(question=question, history=history)
    print(f"\n{outputs.answer}\n")
    history.messages.append({"question": question, **outputs})

dspy.inspect_history()


# class TestGenerationPipeline(dspy.Module):
#     """
#     A complete pipeline for generating tests to increase branch coverage.
#     """

#     def __init__(self):
#         super().__init__()
#         self.coverage_analyzer = dspy.ChainOfThought(CoverageAnalysisSignature)
#         self.test_generator = dspy.ChainOfThought(TestCaseGenerationSignature)

#     def forward(self, file_path: str, test_file_path: str = None):
#         """
#         Generate tests for a given source file.

#         Args:
#             file_path: Path to the source file
#             test_file_path: Path to existing test file (optional)

#         Returns:
#             Generated test code
#         """
#         # Step 1: Read the source code
#         with open(file_path, 'r') as f:
#             source_code = f.read()

#         # Step 2: Read existing tests if provided
#         existing_tests = ""
#         if test_file_path and os.path.exists(test_file_path):
#             with open(test_file_path, 'r') as f:
#                 existing_tests = f.read()

#         # Step 3: Run coverage analysis
#         # Extract module path from file path
#         module_path = file_path.replace('.py', '').replace('/', '.')
#         coverage_report = run_coverage_tool(module_path, test_file_path)

#         # Step 4: Analyze coverage gaps
#         coverage_analysis = self.coverage_analyzer(
#             source_code=source_code,
#             coverage_report=coverage_report
#         )

#         # Step 5: Generate new test cases
#         test_generation = self.test_generator(
#             source_code=source_code,
#             uncovered_branches=coverage_analysis.uncovered_lines,
#             existing_tests=existing_tests
#         )

#         return test_generation


# def main():
#     """
#     Example usage of the test generation agent.
#     """
#     # Example 1: Using the ReAct agent
#     print("=== Creating Test Generation Agent ===\n")
#     agent = create_test_agent()

#     # Example file paths
#     example_file = "deepseek_cot_solutions/solution_1.py"
#     example_test = "test_all_problems.py"

#     print(f"Analyzing: {example_file}")
#     print(f"Test file: {example_test}\n")

#     # Run the agent
#     result = agent(
#         file_path=example_file,
#         test_file_path=example_test
#     )

#     print("=== Agent Analysis ===")
#     print(result.analysis)
#     print("\n=== Generated Test Cases ===")
#     print(result.new_tests)

#     # Example 2: Using the pipeline
#     print("\n\n=== Using Test Generation Pipeline ===\n")
#     pipeline = TestGenerationPipeline()

#     result = pipeline(
#         file_path=example_file,
#         test_file_path=example_test
#     )

#     print("=== Pipeline Generated Tests ===")
#     print(result.test_code)


# if __name__ == "__main__":
#     main()
