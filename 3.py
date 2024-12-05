import sys
from pathlib import Path
from src.color_output import *
from src.log_parser import *
from colorama import Fore, Style, init

levels = ["error", "info", "debug", "warning"]

init(autoreset=True)

def main():
    level: str = None
    log_file_path = Path(__file__).parent / 'logs' / 'application.log'  

    try:
        _, *args = sys.argv

        if len(args) == 0:
            if not log_file_path.exists() or not log_file_path.is_file():
                raise FileNotFoundError(f"File with path '{log_file_path}' not found")
        else:

            if len(args) > 1:
                if not args[1] in levels:
                    raise ValueError("Wrong level argument")
                else:
                    level = args[1].lower()

        logs = load_logs(log_file_path)
        filtered_logs = filter_logs_by_level(logs, level) if level is not None else logs

        display_log_counts(count_logs_by_level(logs), level)
        display_log_details(filtered_logs, level)

    except Exception as err:
        print(Fore.RED + "Error: " + str(err))

if __name__ == "__main__":
    main()
