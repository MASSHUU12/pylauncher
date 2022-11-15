from constants.colors import Colors
from constants.constants import VERSION, REPO_LINK

from helpers.log import Log


def info() -> None:
    Log.all(f"{Colors.BOLD}PyLauncher {VERSION}\n")
    Log.all("Made by MASSHUU12. Source code is available to everyone under the standard MIT license.")
    Log.all(
        f"Source code with new features and improvements can be found here: {REPO_LINK}\n")
    Log.all(f"{Colors.RESET}")
