from decimal import getcontext

from cli.console.printer import Printer


def main(): ...


if __name__ == "__main__":
    try:
        getcontext().prec = 100  # Кол-во знаков после запятой
        main()
    except KeyboardInterrupt:
        Printer.warning("\nРабота программы прервана")
        exit(0)
