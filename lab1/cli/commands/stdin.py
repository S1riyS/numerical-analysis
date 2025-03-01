from algorithm import simple_iterations
from cli.commands.command import ICommand
from cli.commands.common.epsilon_reader import EplisonReader
from cli.commands.common.size_reader import SizeReader
from cli.console.printer import Printer
from cli.converters.float import convert2float
from cli.errors import SizeError


class StdinCommand(ICommand, SizeReader, EplisonReader):
    def execute(self):
        Printer.header("Выбран режим ввода с клавиатуры")
        n = self._read_size()
        matrix = self.__read_matrix(n)
        epsilon = self._read_epsilon()

        Printer.new_line()
        simple_iterations.solve(matrix, epsilon)

    def get_name(self):
        return "Ввод с клавиатуры"

    def __read_matrix(self, n: int) -> list[list[float]]:
        Printer.info("Ввод матрицы:")
        Printer.info('Например для строки: x_1 + 2.5*x_2 + 5*x_3 = 3 следует ввести "1 2.5 5 3"')

        matrix = []
        for i in range(n):
            is_row_valid = False
            while not is_row_valid:
                try:
                    # Read and validate row
                    row = input(f"Введите строку {i+1} матрицы: ").split()
                    data = list(map(convert2float, row))
                    if len(row) != n + 1:
                        raise SizeError(
                            f"Размерность строки не соответствует требуемой ({n} + 1 = {n + 1}, получено {len(row)})"
                        )

                    # Save row to matrix
                    matrix.append(data)
                    is_row_valid = True

                except ValueError:
                    Printer.error("Вводите только числа")
                except SizeError as e:
                    Printer.error(e.message)

        return matrix
