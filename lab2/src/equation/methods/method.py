from abc import ABC, abstractmethod
from typing import Tuple

from equation.model import Equation  # type: ignore
from equation.result import EquationResult  # type: ignore


class IEquationMethod(ABC):
    name = None

    def __init__(self, equation: Equation, left: float, right: float, epsilon: float, decimal_places: int):
        self.decimal_places = decimal_places
        self.epsilon = epsilon
        self.right = right
        self.left = left
        self.equation = equation

    @abstractmethod
    def solve(self) -> EquationResult: ...

    def check(self) -> Tuple[bool, str]:
        return True, ""
