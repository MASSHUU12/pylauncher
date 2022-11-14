import json
from pathlib import Path

from constants.messages import NO_CONFIG, NO_CONFIG_FILE, CONFIG_LOADING
from constants.colors import Colors

from helpers.log import log
from helpers.config import Config


def settings_loader() -> None:
    '''
    Load settings from file
    '''

    # Path to the file with settings
    path = Path(__file__).parent / "../config/config.json"

    try:
        # Open file and read json data
        with path.open() as f:
            # Whole json file
            data = json.load(f)
    except FileNotFoundError:
        log(NO_CONFIG_FILE, "warning_error")
        return

    try:
        # No settings provided
        if len(data["config"]) < 0:
            log(NO_CONFIG, "warning_error")
            return

        # Loading and validating settings
        for config in data["config"]:
            if config == "logLevel":
                if data["config"][config] in ("all", "warning_error", "error", "off"):
                    Config.logLevel = data["config"][config]
                else:
                    log(
                        f"{Colors.FG.YELLOW}Value of {data['config'][config]} in {config} is invalid. Using the default value.{Colors.RESET}", "warning_error", end="\n\n")

    except KeyError:
        log(NO_CONFIG, "warning_error")
        return
