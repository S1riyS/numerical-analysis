import numpy
from scipy.differentiate import derivative  # type: ignore

from equation.methods.method import IEquationMethod  # type: ignore
from equation.model import Equation  # type: ignore
from equation.result import EquationResult  # type: ignore
from types_ import Math1DFunction  # type: ignore

steps = 100
MAX_ITERS = 10_000


class SimpleIterationsMethod(IEquationMethod):
    name = "Метод простой итерации"

    def __init__(self, equation: Equation, left: float, right: float, epsilon: float, decimal_places: int, log: bool):
        super().__init__(equation, left, right, epsilon, decimal_places, log)

    def __get_phi(self) -> Math1DFunction:
        f = self.equation.function

        df_is_positive = True
        df_max = -float("inf")
        for x in numpy.linspace(self.left, self.right, steps):
            df = derivative(f, x).df
            df_max = max(df_max, abs(df))
            if df < 0:
                df_is_positive = False

        lbd = 1 / df_max
        if df_is_positive:
            lbd = -lbd

        return lambda x: x + 1 / lbd * f(x)

    def check(self):
        if not self.equation.root_exists(self.left, self.right):
            return False, "Отсутствует корень на заданном промежутке или корней > 2"

        phi = self.__get_phi()

        print("phi'(a) = ", abs(derivative(phi, self.left).df))
        print("phi'(b) = ", abs(derivative(phi, self.right).df))
        for x in numpy.linspace(self.left, self.right, steps):
            if abs(derivative(phi, x).df) >= 1:
                return False, f"Не выполнено условие сходимости метода |phi'(x)| < 1 на интервале при x = {x}"

        return True, ""

    def solve(self) -> EquationResult:
        f = self.equation.function
        x = 1

        phi = self.__get_phi()

        iteration = 0
        while True:
            iteration += 1

            if iteration == MAX_ITERS:
                print(f"Достигнуто максимальное количество итераций ({iteration})")

            x_prev = x
            x = phi(x)

            if self.log:
                print(
                    f"{iteration}: xk = {x_prev:.4f}, f(xk) = {f(x_prev)}, "
                    f"xk+1 = 𝜑(𝑥𝑘) = {x:.4f}, |xk - xk+1| = {abs(x - x_prev):}"
                )

            if abs(x - x_prev) <= self.epsilon and abs(f(x)) <= self.epsilon:
                break

        return EquationResult(x, f(x), iteration, self.decimal_places)
