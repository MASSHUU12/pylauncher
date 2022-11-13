import subprocess

from constants.colors import Colors
from constants.messages import POSSIBLE_START_FAILURE


def run(list: list[dict[str, dict[str, dict[str, str | list[str]]]]]) -> None:
    '''
    Runs programs from list
    '''

    for program in list:
        print(f"Launching {Colors.BOLD}{program['program']}{Colors.RESET}")

        try:
            subprocess.Popen(
                [str(program["path"]), " ".join(program["options"]) if len(program['options']) > 0 else ''])

            launch_success(program)
        except Exception:
            launch_failure(program)


def launch_success(program) -> None:
    print(f"{Colors.FG.GREEN}{Colors.BOLD}")
    print(
        f"{program['program']}{Colors.RESET} {Colors.FG.GREEN}should now be running.")
    print(f"{Colors.RESET}")


def launch_failure(program) -> None:
    print(f"{Colors.FG.RED}")
    print(
        f"There was an error while starting {program['program']}, {POSSIBLE_START_FAILURE}")
    print(f"{Colors.RESET}")
