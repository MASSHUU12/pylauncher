import subprocess

from constants.colors import Colors
from constants.messages import POSSIBLE_START_FAILURE

from helpers.log import log


def run(list: list[dict[str, dict[str, dict[str, str | list[str]]]]]) -> None:
    '''
    Runs programs from list
    '''

    for program in list:
        log(
            f"Launching {Colors.BOLD}{program['program']}{Colors.RESET}", end="")

        try:
            subprocess.Popen(
                [str(program["path"]), " ".join(program["options"]) if len(program['options']) > 0 else ''])

            launch_success(program)
        except Exception:
            launch_failure(program)


def launch_success(program) -> None:
    log(f"{Colors.FG.GREEN}{Colors.BOLD}")
    log(
        f"{program['program']}{Colors.RESET} {Colors.FG.GREEN}should now be running.{Colors.RESET}")
    log(f"{Colors.RESET}")


def launch_failure(program) -> None:
    log(f"{Colors.FG.RED}", "error")
    log(
        f"There was an error while starting {program['program']}, {POSSIBLE_START_FAILURE}", "error")
    log(f"{Colors.RESET}", "error")
