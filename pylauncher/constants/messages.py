from constants.colors import Colors

# Information
ALL_PASSED = f"{Colors.FG.GREEN}All elements have passed validation.{Colors.RESET}"
CLOSING = f"Closing the program...{Colors.RESET}"

# Warning
SOME_NOT_PASS = f"{Colors.FG.YELLOW}Some elements did not pass validation.{Colors.RESET}"

# Error
NO_LIST = f"{Colors.FG.RED}Err: No list was provided to run. {CLOSING}"
NO_LIST_FILE = f"{Colors.FG.RED}Err: The file list.json does not exist.\nCreate a list.json file in pylauncher/lists directory and complete it according to the documentation.\nDocumentation can be found in the README.md file attached to the project.{Colors.RESET}"
NO_FILE = f"{Colors.FG.RED}Err: File in the defined path does not exist, program is skipped.\n{Colors.RESET}"
NO_PATH = f"{Colors.FG.RED}Err: File path does not exist, program is skipped.\n{Colors.RESET}"
NO_PASSED_VALIDATION = f"{Colors.FG.RED}Err: No item in the list passed validation. {CLOSING}"

POSSIBLE_START_FAILURE = "it is possible that the program will not start, or will start incorrectly."
