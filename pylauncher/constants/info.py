from constants.colors import Colors
from constants.constants import VERSION, REPO_LINK

from helpers.log import log


def info() -> None:
    log(f"{Colors.BOLD}PyLauncher {VERSION}\n")
    log("Made by MASSHUU12. Source code is available to everyone under the standard MIT license.")
    log(
        f"Source code with new features and improvements can be found here: {REPO_LINK}\n")
    log(f"{Colors.RESET}")
