from abc import ABC, abstractmethod
from typing import List

from libs.approximation.methods.core.enums import ApproximationType
from libs.approximation.models.result import ApproximationResult
from libs.approximation.models.validation import ValidationResult


class IMethod(ABC):
    """Abstract base class for approximation methods."""

    def __init__(self, x: List[float], y: List[float]):
        self.xs = x
        self.ys = y
        self.n = len(x)

        if len(x) != len(y):
            raise ValueError("X and Y must have the same length")

    @property
    @abstractmethod
    def type_(self) -> ApproximationType: ...

    @abstractmethod
    def validate(self) -> ValidationResult: ...

    @abstractmethod
    def run(self) -> ApproximationResult: ...
