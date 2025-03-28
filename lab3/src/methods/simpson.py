from typing import Any

import numpy as np

from methods.method import IMethod


class SimpsonMethod(IMethod):
    name = "Simpson"
    runge_k_const = 4

    def _evaluate_integral(self, n: int) -> float:
        a = self.integral.left
        b = self.integral.right
        f = self.integral.f

        # Get partition of [a; b]
        x = np.linspace(a, b, n + 1)
        h = (b - a) / n

        even_values = 0
        odd_values = 0
        for i in range(1, n):
            if i % 2 == 0:
                even_values += f(x[i])
            else:
                odd_values += f(x[i])

        result: float = h / 3 * (f(x[0]) + 4 * odd_values + 2 * even_values + f(x[n]))
        return result
