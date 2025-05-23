from abc import ABC, abstractmethod

import numpy as np
from numpy.typing import NDArray

from schemas.ode import ODERequestSchema, ODEResponseSchema


class ODEMethod(ABC):
    DIVERGENCE_THRESHOLD: float = 1e10

    previous_yn: float | None = None

    def __init__(self, data: ODERequestSchema, max_N: int) -> None:
        self.f = data.f
        self.eps = data.eps

        self.x0 = data.x0
        self.xn = data.xn
        self.y0 = data.y0

        self._set_partition(data.N)

        self._max_N = max_N

    def _set_partition(self, n: int) -> None:
        """Sets `N`, `h`, `xs` and `ys` based on number of points `n`"""
        self.N = n

        self.xs: NDArray[np.float64] = np.linspace(
            self.x0,
            self.xn,
            self.N,
            dtype=np.float64,
        )
        self.ys: NDArray[np.float64] = np.zeros(self.N, dtype=np.float64)
        self.ys[0] = self.y0

        self.h = self.xs[1] - self.xs[0]

    def solve(self) -> ODEResponseSchema:
        while True:
            self._run_method()
            if (self._get_current_accuracy() <= self.eps) or (2 * self.N >= self._max_N):
                break

            self.previous_yn = self.ys[self.N - 1]
            self._set_partition(self.N * 2)  # Double the number of points

        return ODEResponseSchema(
            xs=self.xs,
            ys=self.ys,
            accuracy=self._get_current_accuracy(),
            N=self.N,
        )

    @abstractmethod
    def _run_method(self) -> None:
        """Runs the method. Updates `xs`, `ys` and possibly `N`, `h`"""

    @abstractmethod
    def _get_current_accuracy(self) -> float: ...
