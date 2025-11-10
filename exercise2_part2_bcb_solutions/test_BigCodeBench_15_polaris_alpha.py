import csv
import os
import subprocess
from pathlib import Path


def task_func(commands_file_path, output_dir_path):
    """Execute shell commands listed in a CSV file and save outputs to files.

    - Reads commands from the first column of a CSV file without headers.
    - For each command, creates an output file in ``output_dir_path`` named
      ``command_{index}_output.txt`` (1-based index) containing:
        - stdout if the command succeeds.
        - An error message and exit code if it fails.
    - Returns a list of filenames created (not full paths) to match tests.

    Raises:
    - FileNotFoundError: If ``commands_file_path`` does not exist.
    """
    commands_path = Path(commands_file_path)
    if not commands_path.is_file():
        raise FileNotFoundError(f"Commands file not found: {commands_file_path}")

    # Ensure output directory exists
    output_dir = Path(output_dir_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_files = []

    with commands_path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for idx, row in enumerate(reader, start=1):
            # Skip completely empty rows
            if not row or (len(row) == 1 and row[0].strip() == ""):
                continue

            command = row[0].strip()
            # Build deterministic output filename
            filename = f"command_{idx}_output.txt"
            file_path = output_dir / filename

            try:
                completed = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                )

                # Collect output content
                content_parts = []
                if completed.stdout:
                    content_parts.append(completed.stdout)
                if completed.stderr:
                    # Even on success, stderr (e.g., warnings) is useful
                    content_parts.append(completed.stderr)

                # If command failed (non-zero exit), append descriptive error
                if completed.returncode != 0:
                    content_parts.append(
                        f"Error executing command: '{command}'\nExit code: {completed.returncode}\n"
                    )

                content = "".join(content_parts)

            except Exception as exc:  # pragma: no cover - safety net
                content = (
                    f"Error executing command: '{command}'\n"
                    f"Exception: {exc}\n"
                )

            with file_path.open("w", encoding="utf-8") as f:
                f.write(content)

            # Tests expect list elements to be filenames, not full paths
            output_files.append(filename)

    return output_files
