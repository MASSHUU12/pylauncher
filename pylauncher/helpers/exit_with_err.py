import sys
from helpers.log import Log


def exit_with_err(message: str) -> None:
    '''
    Function to shut down the program in case of a critical error.
    Displays the reason for program termination
    '''

    Log.error(message)
    sys.exit()
