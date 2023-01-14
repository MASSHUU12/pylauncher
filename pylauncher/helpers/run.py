import subprocess

from constants.colors import Colors
from constants.messages import POSSIBLE_START_FAILURE

from helpers.log import Log


def run(list: list[dict[str, dict[str, dict[str, str | list[str]]]]]) -> None:
    """
    Runs programs from list
    """

    for program in list:
        Log.all(
            f"Launching {Colors.BOLD}{program['program']}{Colors.RESET}", end="")

        try:
            subprocess.Popen(
                [str(program["path"]), " ".join(program["options"]) if len(program['options']) > 0 else ''])

            launch_success(program)
        except Exception:
            launch_failure(program)


def launch_success(program) -> None:
    Log.all(f"{Colors.FG.GREEN}{Colors.BOLD}")
    Log.all(
        f"{program['program']}{Colors.RESET} {Colors.FG.GREEN}should now be running.{Colors.RESET}")
    Log.all(f"{Colors.RESET}")


def launch_failure(program) -> None:
    Log.error(f"{Colors.FG.RED}")
    Log.error(
        f"There was an error while starting {program['program']}, {POSSIBLE_START_FAILURE}")
    Log.error(f"{Colors.RESET}")
