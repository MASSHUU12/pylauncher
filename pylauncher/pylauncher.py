import sys

from helpers.get_programs_list import get_programs_list
from helpers.exit_with_err import exit_with_err as close
from helpers.validate_list import validate_list
from helpers.run import run
from helpers.settings_loader import settings_loader

from constants.messages import NO_LIST
from constants.info import info


def main(argv: list[str]) -> None:
    '''
    The main function of the program
    '''

    info()

    # Load settings
    settings_loader()

    if len(argv) <= 0:
        close(NO_LIST)

    # List of programs to run
    list = get_programs_list(argv[0])

    # Validated list of programs ready to run
    validated_list = validate_list(list)

    # Run validated programs
    run(validated_list)


if __name__ == "__main__":
    main(sys.argv[1:])
