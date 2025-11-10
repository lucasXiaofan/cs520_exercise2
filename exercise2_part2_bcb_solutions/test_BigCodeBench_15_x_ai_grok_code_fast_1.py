import subprocess
import csv
import os

def task_func(commands_file_path, output_dir_path):
    if not os.path.exists(commands_file_path):
        raise FileNotFoundError(f"File {commands_file_path} not found")
    
    os.makedirs(output_dir_path, exist_ok=True)
    
    output_files = []
    with open(commands_file_path, 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader, 1):
            if not row:
                continue
            command = row[0]
            output_file = os.path.join(output_dir_path, f'command_{idx}_output.txt')
            output_files.append(output_file)
            try:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                with open(output_file, 'w') as out_f:
                    if result.returncode == 0:
                        out_f.write(result.stdout)
                    else:
                        out_f.write(f"Error executing command '{command}': {result.stderr}\nExit code: {result.returncode}")
            except Exception as e:
                with open(output_file, 'w') as out_f:
                    out_f.write(f"Error executing command '{command}': {str(e)}\n")
    return output_files
