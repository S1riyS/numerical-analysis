from dataclasses import dataclass

from libs.ode.types import Function2D, Function3D


@dataclass(frozen=True)
class FunctionData:
    str_expr: str
    func: Function2D
    exact_solution: Function3D
