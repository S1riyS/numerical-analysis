from typing import Callable, TypeAlias

Function1D: TypeAlias = Callable[[float], float]
Function2D: TypeAlias = Callable[[float, float], float]
Function3D: TypeAlias = Callable[[float, float, float], float]
