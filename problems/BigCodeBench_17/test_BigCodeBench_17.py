
# # TEST CASES
# import unittest
# from unittest.mock import patch, MagicMock
# import sys
# from pathlib import Path

# # Add the project root (cs520_exercise2) to Python path
# sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# from minimax.minimax_m2_free_problem17 import *
# class TestCases(unittest.TestCase):
#     @patch('psutil.process_iter')
#     @patch('subprocess.Popen')
#     def test_process_not_found_starts_process(self, mock_popen, mock_process_iter):
#         # Simulating no running process
#         mock_process_iter.return_value = []
#         result = task_func('random_non_existent_process')
#         self.assertEqual(result, "Process not found. Starting random_non_existent_process.")
#         mock_popen.assert_called_once_with('random_non_existent_process')
#     @patch('psutil.process_iter')
#     @patch('subprocess.Popen')
#     def test_process_found_restarts_process(self, mock_popen, mock_process_iter):
#         # Simulating a running process
#         process = MagicMock()
#         process.name.return_value = 'notepad'
#         mock_process_iter.return_value = [process]
#         result = task_func('notepad')
#         self.assertEqual(result, "Process found. Restarting notepad.")
#         # Expecting terminate called on the process and then restarted
#         process.terminate.assert_called_once()
#         mock_popen.assert_called_once_with('notepad')
#     @patch('psutil.process_iter')
#     @patch('subprocess.Popen')
#     def test_process_terminates_and_restarts_multiple_instances(self, mock_popen, mock_process_iter):
#         # Simulating multiple instances of a running process
#         process1 = MagicMock()
#         process2 = MagicMock()
#         process1.name.return_value = 'multi_instance'
#         process2.name.return_value = 'multi_instance'
#         mock_process_iter.return_value = [process1, process2]
#         result = task_func('multi_instance')
#         self.assertEqual(result, "Process found. Restarting multi_instance.")
#         process1.terminate.assert_called_once()
#         process2.terminate.assert_called_once()
#         mock_popen.assert_called_once_with('multi_instance')

# if __name__ == "__main__":
#     unittest.main()

import unittest
from unittest.mock import patch, MagicMock, call
import psutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from minimax.minimax_m2_free_problem17 import *

class TestCases(unittest.TestCase):
    @patch('psutil.process_iter')
    @patch('subprocess.Popen')
    def test_process_not_found_starts_process(self, mock_popen, mock_process_iter):
        mock_process_iter.return_value = []
        result = task_func('random_non_existent_process')
        self.assertEqual(result, "Process not found. Starting random_non_existent_process.")
        mock_popen.assert_called_once_with('random_non_existent_process')

    @patch('psutil.process_iter')
    @patch('subprocess.Popen')
    def test_process_found_restarts_process(self, mock_popen, mock_process_iter):
        process = MagicMock()
        process.name.return_value = 'notepad'
        mock_process_iter.return_value = [process]
        result = task_func('notepad')
        self.assertEqual(result, "Process found. Restarting notepad.")
        process.terminate.assert_called_once()
        mock_popen.assert_called_once_with('notepad')

    @patch('psutil.process_iter')
    @patch('subprocess.Popen')
    def test_process_terminates_and_restarts_multiple_instances(self, mock_popen, mock_process_iter):
        process1 = MagicMock()
        process2 = MagicMock()
        process1.name.return_value = 'multi_instance'
        process2.name.return_value = 'multi_instance'
        mock_process_iter.return_value = [process1, process2]
        result = task_func('multi_instance')
        self.assertEqual(result, "Process found. Restarting multi_instance.")
        process1.terminate.assert_called_once()
        process2.terminate.assert_called_once()
        mock_popen.assert_called_once_with('multi_instance')

    # NEW TEST CASES for better coverage

    @patch('time.sleep')
    @patch('psutil.process_iter')
    @patch('subprocess.Popen')
    def test_process_with_exe_extension(self, mock_popen, mock_process_iter, mock_sleep):
        """Test matching process names with .exe extension"""
        process = MagicMock()
        process.name.return_value = 'notepad.exe'
        mock_process_iter.return_value = [process]
        result = task_func('notepad')
        self.assertEqual(result, "Process found. Restarting notepad.")
        process.terminate.assert_called_once()
        process.wait.assert_called_once_with(timeout=3)
        mock_sleep.assert_called_once_with(0.5)
        mock_popen.assert_called_once_with('notepad')

    @patch('psutil.process_iter')
    @patch('subprocess.Popen')
    def test_nosuchprocess_exception_handled(self, mock_popen, mock_process_iter):
        """Test that NoSuchProcess exception is caught and handled"""
        process = MagicMock()
        process.name.side_effect = psutil.NoSuchProcess(pid=123)
        mock_process_iter.return_value = [process]
        result = task_func('test_process')
        # Should continue and start the process despite exception
        self.assertEqual(result, "Process not found. Starting test_process.")
        mock_popen.assert_called_once_with('test_process')

    @patch('psutil.process_iter')
    @patch('subprocess.Popen')
    def test_accessdenied_exception_handled(self, mock_popen, mock_process_iter):
        """Test that AccessDenied exception is caught and handled"""
        process = MagicMock()
        process.name.return_value = 'protected_process'
        process.terminate.side_effect = psutil.AccessDenied(pid=123)
        mock_process_iter.return_value = [process]
        result = task_func('protected_process')
        # Should still attempt to start the process
        mock_popen.assert_called_once_with('protected_process')

    @patch('psutil.process_iter')
    @patch('subprocess.Popen')
    def test_timeout_expired_exception_handled(self, mock_popen, mock_process_iter):
        """Test that TimeoutExpired exception is caught and handled"""
        process = MagicMock()
        process.name.return_value = 'slow_process'
        process.wait.side_effect = psutil.TimeoutExpired(seconds=3)
        mock_process_iter.return_value = [process]
        result = task_func('slow_process')
        self.assertEqual(result, "Process found. Restarting slow_process.")
        process.terminate.assert_called_once()
        mock_popen.assert_called_once_with('slow_process')

    @patch('time.sleep')
    @patch('psutil.process_iter')
    @patch('subprocess.Popen')
    def test_sleep_called_when_process_found(self, mock_popen, mock_process_iter, mock_sleep):
        """Test that time.sleep is called when a process is found"""
        process = MagicMock()
        process.name.return_value = 'notepad'
        mock_process_iter.return_value = [process]
        task_func('notepad')
        mock_sleep.assert_called_once_with(0.5)

    @patch('time.sleep')
    @patch('psutil.process_iter')
    @patch('subprocess.Popen')
    def test_no_sleep_when_process_not_found(self, mock_popen, mock_process_iter, mock_sleep):
        """Test that time.sleep is NOT called when process is not found"""
        mock_process_iter.return_value = []
        task_func('nonexistent')
        mock_sleep.assert_not_called()

    @patch('psutil.process_iter')
    @patch('subprocess.Popen')
    def test_mixed_processes_only_terminates_matching(self, mock_popen, mock_process_iter):
        """Test that only matching processes are terminated"""
        process1 = MagicMock()
        process2 = MagicMock()
        process3 = MagicMock()
        process1.name.return_value = 'notepad'
        process2.name.return_value = 'chrome'
        process3.name.return_value = 'notepad.exe'
        mock_process_iter.return_value = [process1, process2, process3]
        
        result = task_func('notepad')
        
        self.assertEqual(result, "Process found. Restarting notepad.")
        process1.terminate.assert_called_once()
        process2.terminate.assert_not_called()  # Should NOT be terminated
        process3.terminate.assert_called_once()
        mock_popen.assert_called_once_with('notepad')

if __name__ == "__main__":
    unittest.main()