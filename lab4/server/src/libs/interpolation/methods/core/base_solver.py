from abc import ABC, abstractmethod
from typing import List

from libs.interpolation.methods.core.enums import InterpolationMethod
from libs.interpolation.models.result import InterpolationResult
from libs.interpolation.models.validation import InterpolationValidation


class BaseSolver(ABC):
    def __init__(self, x: List[float], y: List[float], x_value: float):
        self.xs = x
        self.ys = y
        self.x_value = x_value
        self.n = len(x)

        if len(x) != len(y):
            raise ValueError("X and Y must have the same length")

    @property
    @abstractmethod
    def interpolation_method(self) -> InterpolationMethod: ...

    @abstractmethod
    def solve(self) -> InterpolationResult: ...

    @abstractmethod
    def validate(self) -> InterpolationValidation: ...
