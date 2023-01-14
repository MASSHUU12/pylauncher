import json
from pathlib import Path

from helpers.exit_with_err import exit_with_err as close
from constants.messages import NO_LIST_FILE, CLOSING
from constants.colors import Colors


def get_programs_list(list_program: str) -> dict[str, dict[str, dict[str, str | list[str]]]]:
    """
    Returns information about programs to run from a list configured by the user
    """

    # Path to the file with lists
    path = Path(__file__).parent / "../lists/list.json"

    try:
        # Open file and read json data
        with path.open() as f:
            # Whole json file
            data = json.load(f)
    except FileNotFoundError:
        close(NO_LIST_FILE)

    try:
        if len(data[list_program]) > 0:
            # Returns specific list from file as json data
            return data[list_program]

        # If data is empty exit program
        close(f"{Colors.FG.YELLOW}List {list_program} is empty. {CLOSING}")
    except KeyError:
        # If list doesn't exist, close program
        close(f"{Colors.FG.YELLOW}List {list_program} doesn't exist. {CLOSING}")
