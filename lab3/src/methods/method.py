from abc import ABC, abstractmethod
from typing import Optional, Tuple

from config import INTITIAL_PARTITION_NUMBER, MAX_ITERATIONS
from logger import GlobalLogger
from models.integral import Integral
from models.response import ErrorResponse, ResultResponse

logger = GlobalLogger()


class IMethod(ABC):
    def __init__(self, integral: Integral, epsilon: float):
        self.integral = integral
        self.epsilon = epsilon

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def runge_k_const(self) -> int: ...

    @abstractmethod
    def _evaluate_integral(self, n: int) -> float: ...

    def validate(self) -> Tuple[bool, Optional[ErrorResponse]]:
        return True, None

    def solve(self) -> ResultResponse:
        logger.debug(f"Running {self} with epsilon: {self.epsilon}")

        n = INTITIAL_PARTITION_NUMBER
        prev_evaluation = self._evaluate_integral(n)
        logger.debug(f"Initial evaluation with n={n}: value={prev_evaluation:.5f}")

        for _ in range(MAX_ITERATIONS):
            n *= 2
            current_evaluation = self._evaluate_integral(n)
            logger.debug(f"Current evaluation with n={n}: value={current_evaluation:.5f}")

            if self.__check_precision(prev_evaluation, current_evaluation):
                logger.debug(f"Desired prescision of {self.epsilon} is reached with n={n} partitions")
                break

            prev_evaluation = current_evaluation

        return ResultResponse(value=current_evaluation, partition_number=n)

    def __check_precision(self, previous_evaludation: float, current_evaludation: float) -> bool:
        """Implementation of Runge Rule (an empirical way to estimate the error)"""
        delta: float = (previous_evaludation - current_evaludation) / (2**self.runge_k_const + 1)
        return abs(delta) < self.epsilon

    def __str__(self) -> str:
        return f"{self.name} method"
