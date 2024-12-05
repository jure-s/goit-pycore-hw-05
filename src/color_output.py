from colorama import Fore
from typing import List, Optional, Dict  # Додано імпорт Dict

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
