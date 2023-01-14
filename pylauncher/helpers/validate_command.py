from helpers.exit_with_err import exit_with_err as close

from constants.messages import NO_CORRECT_ARGUMENTS
from constants.constants import COMMAND_OPEN, COMMAND_CLOSE


def validate_command(command: str) -> None:
    """
    Check if user passed correct command
    """

    low = command.lower()
    if low not in (*COMMAND_OPEN, *COMMAND_CLOSE):
        close(NO_CORRECT_ARGUMENTS)
