import re
import os
from datetime import datetime
import unittest

class parserLogs(unittest.TestCase):
    def parse_logs(self,log_file):
        error_pattern = [
            r"ERROR",
            r"CRITICAL",
            r"500 Internal Server Error",
            r"Connection Refused",
            r"Timeout"
        ]

        compiled_pattern = [re.compile(pattern) for pattern in error_pattern]
        errors = []
        with open(log_file) as file:
            for line in file:
                for pattern in compiled_pattern:
                    if pattern.search(line):
                        timeStamps = self.extract_timestamps(line)
                        errors.append((timeStamps,line.strip()))
                        break
        return errors

    def extract_timestamps(self,log_line):
        timestamp_patterns = [
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}",  # ISO 8601 format
            r"\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2}",  # Apache/Nginx format
        ]

        for idx in range(len(timestamp_patterns)):
            records = timestamp_patterns[idx]
            match = re.search(records,log_line)
            if match:
                try:
                    return datetime.strptime(match.group(),"%Y-%m-%dT%H:%M:%s")
                except ValueError:
                    return match.group()
        return "Unknown TimeStamps"
        
    def summarizeErrors(self,errors):
            res = []
            for timestamps,message in errors:
                print(f"Timestamp: {timestamps}, Message: {message}")
                res.append(f"Timestamp: {timestamps}, Message: {message}")
            return res
            