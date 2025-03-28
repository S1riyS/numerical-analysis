from enum import Enum
from typing import Any

import numpy as np

from methods.method import IMethod
from models.integral import Integral


class RectangleMethodMode(Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"


class RectangleMethod(IMethod):
    name = "Rectangle"
    runge_k_const = 2

    def __init__(self, integral: Integral, epsilon: float, mode: RectangleMethodMode = RectangleMethodMode.LEFT):
        super().__init__(integral, epsilon)
        self.mode = mode

    def _evaluate_integral(self, n: int) -> float:
        a = self.integral.left
        b = self.integral.right
        f = self.integral.f

        # Get partition of [a; b]
        x = np.linspace(a, b, n + 1)
        h = (b - a) / n

        # Based on method - create array of points at which function will be evaludated
        if self.mode == RectangleMethodMode.LEFT:
            points = x[:-1]
        elif self.mode == RectangleMethodMode.CENTER:
            points = (x[:-1] + x[1:]) / 2
        elif self.mode == RectangleMethodMode.RIGHT:
            points = x[1:]
        else:
            raise ValueError("Invalid mode for rectangle method")

        # Calculate resulting value
        result: float = h * np.sum([f(points[i]) for i in range(n)])
        return result

    def __str__(self) -> str:
        return f"{super().__str__()} (mode={self.mode.value})"
