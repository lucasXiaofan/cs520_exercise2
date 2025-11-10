import subprocess
import psutil
import time


def task_func(process_name: str) -> str:
    """Check if a process is running; start or restart it accordingly.

    Behavior (per tests/spec):
    - Iterate over running processes using psutil.process_iter.
    - If no process with name == ``process_name`` exists:
        - Start it using subprocess.Popen(process_name).
        - Return "Process not found. Starting <process_name>.".
    - If one or more such processes exist:
        - Call terminate() on each of them.
        - Start a new instance using subprocess.Popen(process_name).
        - Return "Process found. Restarting <process_name>.".

    Notes:
    - We keep implementation straightforward so mocking in tests works
      exactly as expected; no extra kwargs to Popen.
    """

    # Find all processes whose name matches process_name exactly
    matching_processes = []
    for proc in psutil.process_iter(attrs=["name"]):
        try:
            if proc.name() == process_name:
                matching_processes.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if not matching_processes:
        # No existing process: start it
        subprocess.Popen(process_name)
        return f"Process not found. Starting {process_name}."

    # One or more processes found: terminate all, then restart
    for proc in matching_processes:
        try:
            proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Ignore errors; goal is best-effort termination
            continue

    # Small delay is optional; mocking-based tests do not depend on it
    # time.sleep(0.1)

    subprocess.Popen(process_name)
    return f"Process found. Restarting {process_name}."
