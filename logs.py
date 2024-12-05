import re
from typing import List, Dict, Optional
from colorama import Fore

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

def display_log_counts(counts: Dict[str, int], level: Optional[str] = None):
    print(f"{'Level':<10}{'Count'}")
    print("-" * 20)
    
    for level_key, count in counts.items():
        if level_key == "info":
            print(f"{Fore.GREEN}{level_key.upper():<10}{count}")
        elif level_key == "debug":
            print(f"{Fore.CYAN}{level_key.upper():<10}{count}")
        elif level_key == "error":
            print(f"{Fore.RED}{level_key.upper():<10}{count}")
        elif level_key == "warning":
            print(f"{Fore.YELLOW}{level_key.upper():<10}{count}")
    print("\n")

def display_log_details(logs: List[dict], level: Optional[str] = None):
    if level:
        print(f"Log details for level: {Fore.YELLOW}{level.upper()}")
    else:
        print(f"{Fore.WHITE}All logs:")
    
    for log in logs:
        if log["level"].lower() == "info":
            print(f"{Fore.GREEN}{log['datetime']} - {log['message']}")
        elif log["level"].lower() == "debug":
            print(f"{Fore.CYAN}{log['datetime']} - {log['message']}")
        elif log["level"].lower() == "error":
            print(f"{Fore.RED}{log['datetime']} - {log['message']}")
        elif log["level"].lower() == "warning":
            print(f"{Fore.YELLOW}{log['datetime']} - {log['message']}")
    print("\n")
