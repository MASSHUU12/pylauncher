class Colors:
    """
    Class for printing colored text
    """

    RESET = '\033[0m'
    BOLD = '\033[01m'
    DISABLE = '\033[02m'
    UNDERLINE = '\033[04m'
    REVERSE = '\033[07m'
    STRIKETHROUGH = '\033[09m'
    INVISIBLE = '\033[08m'

    class FG:
        """
        Set foreground color
        """

        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        ORANGE = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        YELLOW = '\033[93m'
        PINK = '\033[95m'
        LIGHTBLUE = '\033[94m'
        LIGHTRED = '\033[91m'
        LIGHTGREEN = '\033[92m'
        LIGHTCYAN = '\033[96m'
        LIGHTGREY = '\033[37m'
        DARKGREY = '\033[90m'

    class BG:
        """
        Set background color
        """

        BLACK = '\033[40m'
        RED = '\033[41m'
        GREEN = '\033[42m'
        ORANGE = '\033[43m'
        BLUE = '\033[44m'
        PURPLE = '\033[45m'
        CYAN = '\033[46m'
        LIGHTGREY = '\033[47m'
