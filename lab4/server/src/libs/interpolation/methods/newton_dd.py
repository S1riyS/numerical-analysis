from functools import lru_cache

import sympy as sp  # type: ignore
from libs.interpolation.methods.core.base_solver import BaseSolver
from libs.interpolation.methods.core.enums import InterpolationMethod
from libs.interpolation.models.result import InterpolationResult
from libs.interpolation.models.validation import InterpolationValidation
from libs.interpolation.utils.converter import to_sp_float


class NewtonDividedDifferencesSolver(BaseSolver):
    interpolation_method = InterpolationMethod.NEWTON_DIVIDED_DIFFERENCES

    def validate(self) -> InterpolationValidation:
        return InterpolationValidation(success=True, message=None)

    def solve(self) -> InterpolationResult:
        x = sp.Symbol("x")
        n = len(self.xs)

        polynomial: sp.Expr = self._compute_dd(0, 0)
        xs_prod = 1
        for k in range(1, n):
            xs_prod *= x - to_sp_float(self.xs[k - 1])
            polynomial += to_sp_float(self._compute_dd(0, k)) * xs_prod

        f_expr: sp.Expr = sp.simplify(polynomial).expand()
        y_value = sp.lambdify(x, f_expr, "math")(to_sp_float(self.x_value))
        return InterpolationResult(expr=f_expr, y_value=float(str(y_value)))

    @lru_cache()
    def _compute_dd(self, i: int, order: int) -> float:
        if order == 0:
            return self.ys[i]
        num = self._compute_dd(i + 1, order - 1) - self._compute_dd(i, order - 1)
        denom = self.xs[i + order] - self.xs[i]
        return num / denom
