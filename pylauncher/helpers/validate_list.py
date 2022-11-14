from pathlib import Path

from helpers.exit_with_err import exit_with_err as close
from constants.messages import (
    NO_FILE, NO_PATH, NO_PASSED_VALIDATION, ALL_PASSED, SOME_NOT_PASS)
from constants.colors import Colors


def validate_list(list: dict[str, dict[str, dict[str, str | list[str]]]]) -> list[dict[str, dict[str, dict[str, str | list[str]]]]]:
    '''
    Reads the list of user-defined programs and validate it
    '''

    validated = []

    for program in list:
        details = {
            "program": program,
            "path": "",
            "options": []
        }

        print(f"Validating {program} configuration:")

        # Check if user defined path to the file,
        # if path doesn't exist continue with next program
        try:
            print(f"Path: {list[program]['path']}")

            # Check if file exists
            file = Path(str(list[program]["path"]))

            if file.is_file():
                details["path"] = list[program]["path"]
            else:
                # If file does not exist continue with next program
                print(NO_FILE)
                continue
        except (KeyError, TypeError):
            print(NO_PATH)
            continue

        # Check if user defined optional options for program startup
        try:
            if len(list[program]['options']) > 0:
                details["options"] = list[program]["options"]

            print(f"Options: {str(details['options'])}")
        except KeyError:
            print(f"Options: {str(details['options'])}")

        # Append validated data
        validated.append(details)

        print(f"{Colors.FG.GREEN}Success{Colors.RESET}\n")

    if len(validated) <= 0:
        # If no item has passed validation terminate the program
        close(NO_PASSED_VALIDATION)
    elif len(validated) == len(list):
        print(ALL_PASSED + "\n")
    else:
        print(SOME_NOT_PASS)
        print(f"{Colors.FG.GREEN}Passed:{Colors.RESET} {len(validated)}")
        print(f"{Colors.FG.RED}Skipped:{Colors.RESET} {len(list) - len(validated)}\n")

    return validated
