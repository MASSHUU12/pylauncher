from helpers.config import Config


def log(message: str, type: str = "all", end: str = "\n") -> None:
    '''
    Print messages based on user settings
    '''

    if Config.logLevel == "all" and type in ("all", "warning_error", "warning", "error"):
        print(message, end=end)
        return

    if Config.logLevel == "warning_error" and type in ("warning_error", "warning", "error"):
        print(message, end=end)
        return

    if Config.logLevel == "error" and type == "error":
        print(message, end=end)
        return
