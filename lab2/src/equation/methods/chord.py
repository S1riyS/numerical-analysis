import numpy as np

from equation.methods.method import IEquationMethod  # type: ignore
from equation.result import EquationResult  # type: ignore


class ChordMethod(IEquationMethod):
    name = "Метод хорд"

    def check(self):
        root_exists = self.equation.root_exists(self.left, self.right)
        return root_exists, "Отсутствует корень на заданном промежутке или корней > 2" if not root_exists else ""

    def solve(self) -> EquationResult:
        f = self.equation.function
        a = self.left
        b = self.right
        epsilon = self.epsilon
        iteration = 0

        x = a - (b - a) * f(a) / (f(b) - f(a))

        iteration = 0
        last_x = x

        while iteration < 10_000:
            iteration += 1

            if f(a) * f(x) < 0:
                b = x
            else:
                a = x

            x = a - (b - a) * f(a) / (f(b) - f(a))

            if np.abs(f(x)) <= epsilon and abs(x - last_x) <= epsilon:
                break

            last_x = x

        return EquationResult(x, f(x), iteration, self.decimal_places)
