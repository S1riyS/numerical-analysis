import typing as t

from algorithm import simple_iterations
from cli.commands.command import ICommand
from cli.commands.common.epsilon_reader import DEFAULT_EPSILON
from cli.console.printer import Printer
from cli.converters.float import convert2float
from cli.errors import SizeError


class FileCommand(ICommand):
    def __init__(self):
        self.eps = DEFAULT_EPSILON

    def execute(self):
        Printer.header("Выбран режим чтения из файла")
        filename = self.__read_filename()
        matrix, eps = self.__read_matrix_from_file(filename)
        if matrix is not None and eps is not None:
            Printer.success("Чтение из файла завершено")

            Printer.new_line()
            simple_iterations.solve(matrix, eps)
        else:
            Printer.error("Чтение из файла завершено с ошибкой")

    def get_name(self):
        return "Ввод из файла"

    def __read_filename(self) -> str:
        Printer.info("Ввод имени файла:")
        return input("Введите имя файла: ")

    def __read_matrix_from_file(self, path: str) -> tuple[t.Optional[list[list[float]]], t.Optional[float]]:
        # Read file
        with open(path, "r") as file:
            lines = file.readlines()

        n_str, eps_str = lines[0].split()
        try:
            # Read size
            n = int(n_str)
            if n <= 0 or n > 20:
                raise SizeError("Размерность матрицы должна быть 1 <= N <= 20")
            # Read epsilon
            eps = convert2float(eps_str)
            self.eps = eps

        except ValueError:
            Printer.error("Вводите только числа")
            return None, None
        except SizeError as e:
            Printer.error(e.message)
            return None, None

        try:
            # Read matrix
            matrix = []
            for row_index, line in enumerate(lines[1:]):
                # Validate matrix height
                if row_index + 1 > n:
                    raise SizeError(f"В матрице слишком много строк (должно быть {n})")
                # Validate row length
                row = list(map(float, line.split()))
                if len(row) != n + 1:
                    raise SizeError(
                        f"Размерность строки не соответствует требуемой ({n} + 1 = {n + 1}, получено {len(row)})"
                    )
                matrix.append(row)

        except ValueError:
            Printer.error("Вводите только числа")
            return None, None
        except SizeError as e:
            Printer.error(e.message)
            return None, None

        return matrix, eps
