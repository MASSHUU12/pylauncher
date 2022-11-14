import sys
from helpers.log import log


def exit_with_err(message: str) -> None:
    '''
    Function to shut down the program in case of a critical error.
    Displays the reason for program termination
    '''

    log(message, "error")
    sys.exit()
