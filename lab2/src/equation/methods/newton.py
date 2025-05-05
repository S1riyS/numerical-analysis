from scipy.differentiate import derivative  # type: ignore

from equation.methods.method import IEquationMethod  # type: ignore
from equation.result import EquationResult  # type: ignore


class NewtonMethod(IEquationMethod):
    name = "Метод Ньютона"

    def solve(self) -> EquationResult:
        f = self.equation.function
        x0 = self.left

        epsilon = self.epsilon
        iteration = 0

        while True:
            iteration += 1

            df = derivative(f, x0).df
            x1 = x0 - f(x0) / df

            if abs(x1 - x0) < epsilon and f(x1) < epsilon:
                break

            x0 = x1

        return EquationResult(x1, f(x1), iteration, self.decimal_places)
