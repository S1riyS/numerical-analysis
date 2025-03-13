from random import uniform

from algorithm import simple_iterations
from cli.commands.command import ICommand
from cli.commands.common.epsilon_reader import EplisonReader
from cli.commands.common.size_reader import SizeReader
from cli.console.printer import Printer


class RandomCommand(ICommand, SizeReader, EplisonReader):
    def execute(self):
        Printer.header("Выбран режим генерации случайной матрицы")
        n = self._read_size()
        matrix = self.__create_matrix(n)
        epsilon = self._read_epsilon()
        Printer.success("Генерация случайной матрицы завершена")

        Printer.new_line()
        simple_iterations.solve(matrix, epsilon)

    def get_name(self):
        return "Случайная матрица"

    def __create_matrix(self, n: int) -> list[list[float]]:
        matrix = [[0.0 for _ in range(n + 1)] for _ in range(n)]
        for i in range(n):
            row_abs_sum = 0
            for j in range(n + 1):
                matrix[i][j] = uniform(-5, 5)
                row_abs_sum += abs(matrix[i][j])
            matrix[i][i] = row_abs_sum + 1

        Printer.default("Случайная матрица:")
        for row in matrix:
            for elem in row:
                print(f"{elem:.2f}", end="\t")
            Printer.new_line()
        return matrix
