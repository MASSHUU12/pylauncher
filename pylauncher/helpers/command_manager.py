from helpers.get_programs_list import get_programs_list
from helpers.validate_list import validate_list
from helpers.run import run
from helpers.close import close

from constants.constants import COMMAND_OPEN, COMMAND_CLOSE


def command_manager(command: str, selectedList: str) -> None:
    '''
    The function that activates the selected option
    '''

    # List of programs
    list = get_programs_list(selectedList)

    # Validated list of programs
    validated = validate_list(list)

    low = command.lower()
    if low in COMMAND_OPEN:
        # Run validated programs
        run(validated)

    if low in COMMAND_CLOSE:
        # Close validated programs
        close(validated)
