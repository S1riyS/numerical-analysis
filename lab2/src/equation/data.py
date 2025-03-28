import math

from equation.methods_enum import EquationMethod  # type: ignore
from equation.model import Equation  # type: ignore

equations: list[Equation] = [
    Equation(lambda x: (2.74 * x**3 - 1.93 * x**2 - 15.28 * x - 3.27), "2.74*x^3 - 1.93*x^2 - 15.28*x - 3.27"),
    Equation(lambda x: (math.sin(3 * x) + 2 * math.cos(2 * x) + 1 / 2), "sin(3x) + 2*cos(2x) + 1/2"),
    Equation(lambda x: (x / 3 - 4 * (x + 2) ** (1 / 4)), "x/3 - 4*(x + 2)^(1/4)"),
    Equation(lambda x: (math.e**x + math.cos(x) - 1), "e^x + cos(x) - 1"),
]


equation_methods: list[EquationMethod] = [
    EquationMethod.CHORD,
    EquationMethod.NEWTON,
    EquationMethod.SIMPLE_ITERATIONS,
]
