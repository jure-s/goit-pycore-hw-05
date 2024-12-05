import re
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    match = re.match(r"(\S+ \S+) (\S+) (.*)", line)
    if match:
        return {
            "datetime": match.group(1),
            "level": match.group(2),
            "message": match.group(3)
        }
    return {}

def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return [log for log in logs if log["level"].lower() == level.lower()]

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {"info": 0, "debug": 0, "error": 0, "warning": 0}
    for log in logs:
        level = log["level"].lower()
        if level in counts:
            counts[level] += 1
    return counts
