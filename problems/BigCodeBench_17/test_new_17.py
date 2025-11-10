# test_BigCodeBench_17.py
import pytest
from unittest.mock import patch, MagicMock
import psutil
import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Define all solutions to test
SOLUTION_MODULES = [
    'minimax.minimax_m2_free_problem17',
    'minimax.minimax_m2_free_problem17_2',
    'minimax.minimax_m2_free_problem17_3',
]

def get_task_func(module_name):
    """Import and return task_func from module"""
    module = importlib.import_module(module_name)
    return module.task_func

@pytest.fixture(params=SOLUTION_MODULES, ids=lambda x: x.split('.')[-1])
def task_func(request):
    """Fixture that provides each solution's task_func"""
    return get_task_func(request.param)

@patch('psutil.process_iter')
@patch('subprocess.Popen')
def test_process_not_found_starts_process(mock_popen, mock_process_iter, task_func):
    mock_process_iter.return_value = []
    result = task_func('random_non_existent_process')
    assert result == "Process not found. Starting random_non_existent_process."
    mock_popen.assert_called_once_with('random_non_existent_process')

@patch('psutil.process_iter')
@patch('subprocess.Popen')
def test_process_found_restarts_process(mock_popen, mock_process_iter, task_func):
    process = MagicMock()
    process.name.return_value = 'notepad'
    mock_process_iter.return_value = [process]
    result = task_func('notepad')
    assert result == "Process found. Restarting notepad."
    process.terminate.assert_called_once()
    mock_popen.assert_called_once_with('notepad')

@patch('time.sleep')
@patch('psutil.process_iter')
@patch('subprocess.Popen')
def test_process_with_exe_extension(mock_popen, mock_process_iter, mock_sleep, task_func):
    process = MagicMock()
    process.name.return_value = 'notepad.exe'
    mock_process_iter.return_value = [process]
    result = task_func('notepad')
    assert result == "Process found. Restarting notepad."
    process.terminate.assert_called_once()
    process.wait.assert_called_once_with(timeout=3)
    mock_sleep.assert_called_once_with(0.5)
    mock_popen.assert_called_once_with('notepad')

@patch('psutil.process_iter')
@patch('subprocess.Popen')
def test_nosuchprocess_exception_handled(mock_popen, mock_process_iter, task_func):
    process = MagicMock()
    process.name.side_effect = psutil.NoSuchProcess(pid=123)
    mock_process_iter.return_value = [process]
    result = task_func('test_process')
    assert result == "Process not found. Starting test_process."
    mock_popen.assert_called_once_with('test_process')

# Add all other tests...