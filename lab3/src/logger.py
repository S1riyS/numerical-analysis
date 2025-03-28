from enum import Enum
from io import TextIOWrapper
from typing import Any


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5


# ANSI color codes
class Colors:
    DEBUG = "\033[36m"  # Cyan
    INFO = "\033[32m"  # Green
    WARNING = "\033[33m"  # Yellow
    ERROR = "\033[31m"  # Red
    CRITICAL = "\033[1;31m"  # Bold Red
    RESET = "\033[0m"  # Reset to default


def log_level_to_str(level: LogLevel) -> str:
    color = {
        LogLevel.DEBUG: Colors.DEBUG,
        LogLevel.INFO: Colors.INFO,
        LogLevel.WARNING: Colors.WARNING,
        LogLevel.ERROR: Colors.ERROR,
        LogLevel.CRITICAL: Colors.CRITICAL,
    }.get(level, Colors.RESET)

    return f"{color}{level.name}{Colors.RESET}"


class Logger:
    def __init__(
        self,
        file: None | TextIOWrapper | Any = None,
        min_level: LogLevel = LogLevel.DEBUG,
        use_colors: bool = True,
    ) -> None:
        self.file = file
        self.min_level = min_level
        self.use_colors = use_colors

    def set_min_level(self, min_level: LogLevel) -> None:
        self.min_level = min_level

    def set_use_colors(self, use_colors: bool) -> None:
        self.use_colors = use_colors

    def log(
        self,
        *args: Any,
        level: LogLevel = LogLevel.INFO,
        sep: str = " ",
        end: str = "\n",
    ) -> None:
        if level.value < self.min_level.value:
            return

        level_str = log_level_to_str(level) if self.use_colors else f"[{level.name}]"
        print(f"[{level_str}]", *args, sep=sep, end=end, file=self.file)

    def debug(self, *args: Any, sep: str = " ", end: str = "\n") -> None:
        self.log(*args, level=LogLevel.DEBUG, sep=sep, end=end)

    def info(self, *args: Any, sep: str = " ", end: str = "\n") -> None:
        self.log(*args, level=LogLevel.INFO, sep=sep, end=end)

    def warning(self, *args: Any, sep: str = " ", end: str = "\n") -> None:
        self.log(*args, level=LogLevel.WARNING, sep=sep, end=end)

    def error(self, *args: Any, sep: str = " ", end: str = "\n") -> None:
        self.log(*args, level=LogLevel.ERROR, sep=sep, end=end)

    def critical(self, *args: Any, sep: str = " ", end: str = "\n") -> None:
        self.log(*args, level=LogLevel.CRITICAL, sep=sep, end=end)


def singleton(class_: Any) -> Any:
    instances = {}

    def getinstance(*args: Any, **kwargs: Any) -> Any:
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class GlobalLogger(Logger):
    pass
