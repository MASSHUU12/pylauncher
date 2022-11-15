import psutil
from helpers.log import Log

from constants.colors import Colors
from constants.messages import PREPARING_FOR_CLOSING


def close(list: dict[str, dict[str, dict[str, str | list[str]]]]) -> None:
    '''
    Closes programs from list
    '''

    Log.all(PREPARING_FOR_CLOSING)

    for program in list:

        try:
            # Get program path
            p = str(list[program]["path"])

            # Remove path and get program name
            programName = p.split("\\")[-1]

            # Remove extension from name
            cleanName = programName.rsplit(".", 1)[0]

            try:
                for process in (process for process in psutil.process_iter() if process.name().startswith(cleanName)):
                    Log.all(f"{Colors.FG.GREEN}", "")
                    Log.all(
                        f"Terminating {Colors.BOLD}{program}{Colors.RESET} {Colors.FG.GREEN}(pid={process.pid}).", "")
                    Log.all(f"{Colors.RESET}")

                    process.kill()
            except psutil.NoSuchProcess:
                Log.error(
                    f"{Colors.FG.RED}There was a problem while stopping {program}, some processes may still work.{Colors.RESET}")
        except KeyError:
            Log.warn(
                f"{Colors.FG.YELLOW}Misconfigured list for {program} program, skipping.{Colors.RESET}")
            continue
