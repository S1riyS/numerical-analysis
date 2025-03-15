from abc import ABC, abstractmethod

from system.model import System  # type: ignore
from system.result import SystemResult  # type: ignore


class ISystemMethod(ABC):
    def __init__(self, system: System, x0: float, y0: float, epsilon: float, decimal_places: int):
        self.system = system
        self.x0 = x0
        self.y0 = y0
        self.epsilon = epsilon
        self.decimal_places = decimal_places

    @abstractmethod
    def solve(self) -> SystemResult: ...
