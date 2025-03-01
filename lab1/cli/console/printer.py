import stat

from cli.console.color import ConsoleColors


class Printer:
    @staticmethod
    def new_line():
        print()

    @staticmethod
    def default(text):
        print(text)

    @staticmethod
    def header(text):
        print(ConsoleColors.HEADER + text + ConsoleColors.ENDC)

    @staticmethod
    def error(text):
        print(ConsoleColors.FAIL + text + ConsoleColors.ENDC)

    @staticmethod
    def warning(text):
        print(ConsoleColors.WARNING + text + ConsoleColors.ENDC)

    @staticmethod
    def success(text):
        print(ConsoleColors.OKGREEN + text + ConsoleColors.ENDC)

    @staticmethod
    def info(text):
        print(ConsoleColors.OKBLUE + text + ConsoleColors.ENDC)
