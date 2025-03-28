from system.methods_enum import SystemMethod  # type: ignore
from system.model import System  # type: ignore

from math import sin, cos

systems: list[System] = [
    System(
        f1=lambda x, y: x**2 + y**2 - 1,
        f2=lambda x, y: x**2 - y - 0.5,
        text="x^2 + y^2 - 1; x^2 - y - 0.5",
    ),
    System(
        f1=lambda x, y: sin(x) + cos(y),
        f2=lambda x, y: sin(2 * x) + y**2,
        text="sin(x) + cos(y); sin(2x) + y^2",
    ),
]

system_methods: list[SystemMethod] = [
    SystemMethod.NEWTON,
]
