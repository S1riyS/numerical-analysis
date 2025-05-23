import numpy as np

from libs.ode.methods.core.method import ODEMethod
from libs.ode.types import Function1D
from schemas.ode import ODERequestSchema


class MultiStepODEMethod(ODEMethod):
    def __init__(
        self,
        data: ODERequestSchema,
        max_N: int,
        exact_solution: Function1D,
    ) -> None:
        super().__init__(data, max_N)
        self.exact_solution = exact_solution

    def _get_current_accuracy(self) -> float:
        diffs = [abs(self.exact_solution(x) - y) for x, y in zip(self.xs, self.ys)]
        return np.max(diffs)
