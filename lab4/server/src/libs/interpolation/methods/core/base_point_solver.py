from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List

from libs.interpolation.methods.core.enums import PointInterpolationMethod
from libs.interpolation.models.result import PointInterpolationResult
from libs.interpolation.models.validation import InterpolationValidation


class BasePointSolver(ABC):

    def __init__(
        self,
        x: List[float],
        y: List[float],
        x_value: float,
    ):
        self.xs = x
        self.ys = y
        self.x_value = x_value
        self.n = len(x)

        if len(x) != len(y):
            raise ValueError("X and Y must have the same length")

    @property
    @abstractmethod
    def point_interpolation_method(self) -> PointInterpolationMethod: ...

    @abstractmethod
    def solve(self) -> PointInterpolationResult: ...

    @abstractmethod
    def validate(self) -> InterpolationValidation: ...
