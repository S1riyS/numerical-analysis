from typing import Any

import numpy as np

from methods.method import IMethod


class TrapeziodMethod(IMethod):
    name = "Trapezoid"
    runge_k_const = 2

    def _evaluate_integral(self, n: int) -> float:
        a = self.integral.left
        b = self.integral.right
        f = self.integral.f

        # Get partition of [a; b]
        x = np.linspace(a, b, n + 1)
        h = (b - a) / n

        accumulator = 0
        for i in range(1, n - 1):
            accumulator += f(x[i])

        result: float = h / 2 * (f(x[0]) + f(x[n]) + 2 * accumulator)
        return result
