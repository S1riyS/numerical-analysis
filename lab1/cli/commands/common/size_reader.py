from cli.console.printer import Printer
from cli.errors import SizeError


class SizeReader:
    def _read_size(self) -> int:
        Printer.info("Ввод размерности матрицы:")

        size = 0
        valid_size = False
        while not valid_size:
            try:
                # Read and validate size
                size = int(input("Введите размерность матрицы (n <= 20): "))
                if size > 20 or size < 0:
                    raise SizeError("Размерность матрицы должна быть 0 <= N <= 20")
                valid_size = True

            except ValueError:
                Printer.error("Вводите только целые числа")
            except SizeError:
                Printer.error("Размерность N матрицы должна быть 0 <= N <= 20")

        return size
