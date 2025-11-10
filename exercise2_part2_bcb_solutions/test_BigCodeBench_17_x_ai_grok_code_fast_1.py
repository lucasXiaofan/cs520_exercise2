import psutil
import subprocess
import time

def task_func(process_name: str) -> str:
    running = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            running = True
            proc.terminate()
    if running:
        time.sleep(0.1)
        subprocess.Popen(process_name)
        return f"Process found. Restarting {process_name}."
    else:
        subprocess.Popen(process_name)
        return f"Process not found. Starting {process_name}."
