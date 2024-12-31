import unittest
from app.logParser import parserLogs
import os

class test_serverLogs(unittest.TestCase):
    def test_parse(self):
        errors = None
        log_file_path = "logs/server.logs"
        print("Absolute path:", os.path.abspath(log_file_path))
        if not os.path.exists(log_file_path):
            print("not exist")
        else:
            print("File Logs Exist")
            parser = parserLogs()
            errors = parser.parse_logs(log_file_path)
            print("ERRORS ", errors)
            if errors:
                errors = parser.summarizeErrors(errors)
                print("ERRORS NEW ", errors)
            else:
                print("no error found   ")
        self.assertIsNotNone(errors, "Expected errors, but got None.")

