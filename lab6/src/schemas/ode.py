from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from libs.ode.methods.core.enums import ODEMethodType
from libs.ode.types import Function2D


@dataclass(frozen=True)
class ODERequestSchema:
    # Interval [x0; xn]
    x0: float
    xn: float
    # Initial condition y0 = f'(x0)
    y0: float
    f: Function2D
    # Number of points
    N: int
    # Accuracy
    eps: float
    # Method
    method: ODEMethodType


@dataclass(frozen=True)
class ODEResponseSchema:
    xs: NDArray[np.float64]
    ys: NDArray[np.float64]
    accuracy: float
    N: int
