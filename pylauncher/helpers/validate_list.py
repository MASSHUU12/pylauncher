from pathlib import Path

from helpers.exit_with_err import exit_with_err as close
from helpers.log import Log

from constants.messages import (
    NO_FILE, NO_PATH, NO_PASSED_VALIDATION, ALL_PASSED, SOME_NOT_PASS)
from constants.colors import Colors


def validate_list(list: dict[str, dict[str, dict[str, str | list[str]]]]) -> list[
        dict[str, dict[str, dict[str, str | list[str]]]]]:
    """
    Reads the list of user-defined programs and validate it
    """

    validated = []

    for program in list:
        details = {
            "program": program,
            "path": "",
            "options": []
        }

        Log.all(f"Validating {program} configuration:")

        # Check if user defined path to the file,
        # if path doesn't exist continue with next program
        try:
            Log.all(f"Path: {list[program]['path']}")

            # Check if file exists
            file = Path(str(list[program]["path"]))

            if file.is_file():
                details["path"] = list[program]["path"]
            else:
                # If file does not exist continue with next program
                Log.error(NO_FILE)
                continue
        except (KeyError, TypeError):
            Log.error(NO_PATH)
            continue

        # Check if user defined optional options for program startup
        try:
            if len(list[program]['options']) > 0:
                details["options"] = list[program]["options"]

            Log.all(f"Options: {str(details['options'])}")
        except KeyError:
            Log.all(f"Options: {str(details['options'])}")

        # Append validated data
        validated.append(details)

        Log.all(f"{Colors.FG.GREEN}Success{Colors.RESET}\n")

    if len(validated) <= 0:
        # If no item has passed validation terminate the program
        close(NO_PASSED_VALIDATION)
    elif len(validated) == len(list):
        Log.all(ALL_PASSED + "\n")
    else:
        Log.warn(SOME_NOT_PASS)
        Log.warn(f"{Colors.FG.GREEN}Passed:{Colors.RESET} {len(validated)}")
        Log.warn(
            f"{Colors.FG.RED}Skipped:{Colors.RESET} {len(list) - len(validated)}\n")

    return validated
