import json
import os


def setup_problem_folders(json_file_path, base_output_dir="problems"):
    """
    Read problems from JSON file and create a folder for each problem
    with the testing script and problem information.

    Args:
        json_file_path (str): Path to the JSON file containing problems
        base_output_dir (str): Base directory where problem folders will be created

    Returns:
        list: List of created folder paths
    """
    # Read the JSON file
    with open(json_file_path, 'r') as f:
        problems = json.load(f)

    # Create base output directory if it doesn't exist
    if not os.path.exists(base_output_dir):
        os.makedirs(base_output_dir)

    created_folders = []

    for problem in problems:
        # Extract task_id and sanitize it for folder name
        task_id = problem['task_id']
        folder_name = task_id.replace('/', '_')  # Replace / with _
        folder_path = os.path.join(base_output_dir, folder_name)

        # Create folder for this problem
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Create the test file
        test_file_path = os.path.join(folder_path, f'test_{folder_name}.py')
        with open(test_file_path, 'w') as f:
            # Write the imports and function signature from complete_prompt
            f.write(problem['complete_prompt'])
            f.write("\n\n")

            # Write the test cases
            f.write("# TEST CASES\n")
            f.write(problem['test'])
            f.write("\n\n")

            # Add main block to run tests
            f.write('if __name__ == "__main__":\n')
            f.write('    unittest.main()\n')

        created_folders.append(folder_path)
        print(f"Created folder: {folder_path}")

    return created_folders


if __name__ == "__main__":
    # Run the setup
    json_path = "hard_problems_5.json"

    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found!")
        print("Please run load_5_problem.py first to generate the JSON file.")
    else:
        folders = setup_problem_folders(json_path)
        print(f"\n✓ Successfully created {len(folders)} problem folders:")
        for folder in folders:
            print(f"  - {folder}")
