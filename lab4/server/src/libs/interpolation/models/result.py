from dataclasses import dataclass

import sympy as sp  # type: ignore


@dataclass
class InterpolationResult:
    expr: sp.Expr
    y_value: float


@dataclass
class PointInterpolationResult:
    expr: sp.Expr
    y_value: float
