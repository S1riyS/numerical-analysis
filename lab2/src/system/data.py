from system.methods_enum import SystemMethod  # type: ignore
from system.model import System  # type: ignore

systems: list[System] = [
    System(
        f1=lambda x, y: x**2 + y**2 - 1,
        f2=lambda x, y: x**2 - y - 0.5,
        text="x^2 + y^2 - 1; x^2 - y - 0.5",
    )
]

system_methods: list[SystemMethod] = [
    SystemMethod.NEWTON,
]
