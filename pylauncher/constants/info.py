from constants.colors import Colors
from constants.constants import VERSION, REPO_LINK


def info() -> None:
    print(f"{Colors.BOLD}PyLauncher {VERSION}\n")
    print("Made by MASSHUU12. Source code is available to everyone under the standard MIT license.")
    print(
        f"Source code with new features and improvements can be found here: {REPO_LINK}\n")
    print(f"{Colors.RESET}")
