from helpers.config import Config


class Log:
    """
    Basic log system.
    Prints message based on user config.
    """

    @staticmethod
    def all(message: str, end: str = "\n") -> None:
        """
        Display when logLevel == "all"
        """

        if Config.logLevel == "all":
            print(message, end=end)

    @staticmethod
    def warn(message: str, end: str = "\n") -> None:
        """
        Display when logLevel == "warning_error"
        """

        if Config.logLevel == "warning_error":
            print(message, end=end)

    @staticmethod
    def error(message: str, end: str = "\n") -> None:
        """
        Display when logLevel == "error"
        """

        if Config.logLevel == "error":
            print(message, end=end)
