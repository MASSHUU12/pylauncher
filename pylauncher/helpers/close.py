import psutil
from helpers.log import log

from constants.colors import Colors
from constants.messages import PREPARING_FOR_CLOSING


def close(list: dict[str, dict[str, dict[str, str | list[str]]]]) -> None:
    '''
    Closes programs from list
    '''

    log(PREPARING_FOR_CLOSING)

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
                    log(f"{Colors.FG.GREEN}Terminating {Colors.BOLD}{program}{Colors.RESET} {Colors.FG.GREEN}(pid={process.pid}).{Colors.RESET}")
                    process.kill()
            except psutil.NoSuchProcess:
                log(f"{Colors.FG.RED}There was a problem while stopping {program}, some processes may still work.{Colors.RESET}", "error")
        except KeyError:
            log(f"{Colors.FG.YELLOW}Misconfigured list for {program} program, skipping.{Colors.RESET}", "warning_error")
            continue
