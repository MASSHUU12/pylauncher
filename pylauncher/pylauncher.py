import sys

from helpers.exit_with_err import exit_with_err as close
from helpers.settings_loader import settings_loader
from helpers.validate_command import validate_command
from helpers.command_manager import command_manager

from constants.messages import NO_ARGUMENTS
from constants.info import info


def main(argv: list[str]) -> None:
    '''
    The main function of the program
    '''

    info()

    # Load settings
    settings_loader()

    if len(argv) < 2:
        close(NO_ARGUMENTS)

    # Check if passed command is valid
    validate_command(argv[0])

    # Run selected command
    command_manager(argv[0], argv[1])


if __name__ == "__main__":
    main(sys.argv[1:])
