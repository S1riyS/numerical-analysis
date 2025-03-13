from decimal import Decimal
from cli.console.printer import Printer
from cli.converters.float import convert2decimal

DEFAULT_EPSILON = Decimal('0.001')


class EplisonReader:
    def _read_epsilon(self):
        Printer.info("Ввод точности:")
        Printer.info(f"Значение по умолчанию - {DEFAULT_EPSILON} (нажмите Enter для ввода значения по умолчанию)")

        valid_epsilon = False
        epsilon = 0

        while not valid_epsilon:
            try:
                # Read and validate epsilon
                epsilon_input = input("Введите точность: ")
                if epsilon_input == "":
                    epsilon = DEFAULT_EPSILON
                else:
                    epsilon = convert2decimal(epsilon_input)

                valid_epsilon = True
            except ValueError:
                Printer.error("Вводите только числа")

        return epsilon
