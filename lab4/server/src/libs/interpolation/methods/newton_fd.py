from math import factorial

import sympy as sp  # type: ignore
from libs.interpolation.methods.core.base_solver import BaseSolver
from libs.interpolation.methods.core.enums import InterpolationMethod
from libs.interpolation.models.result import InterpolationResult
from libs.interpolation.models.validation import InterpolationValidation
from libs.interpolation.utils.converter import to_sp_float


class NewtonFiniteDifferencesSolver(BaseSolver):
    interpolation_method = InterpolationMethod.NEWTON_FINITE_DIFFERENCES

    def validate(self) -> InterpolationValidation:
        hs = [self.xs[i + 1] - self.xs[i] for i in range(len(self.xs) - 1)]
        dhs = [abs(hs[i + 1] - hs[i]) for i in range(len(hs) - 1)]
        if max(dhs) > 1e-6:
            return InterpolationValidation(
                success=False, message="xs are not evenly distributed"
            )
        return InterpolationValidation(success=True, message=None)

    def solve(self) -> InterpolationResult:
        h = self.xs[1] - self.xs[0]
        n = len(self.xs)

        x = sp.symbols("x")
        polynomial: sp.Expr = 0
        product_term: sp.Expr = 1
        for i in range(n):
            coeff = to_sp_float(
                self._compute_finite_difference(0, i) / (factorial(i) * h**i)
            )

            if i > 0:
                product_term *= x - to_sp_float(self.xs[i - 1])
            polynomial += coeff * product_term if i > 0 else coeff

        f_expr: sp.Expr = sp.simplify(polynomial).expand()
        y_value = sp.lambdify(x, f_expr, "math")(to_sp_float(self.x_value))
        return InterpolationResult(expr=f_expr, y_value=float(str(y_value)))

    def _compute_finite_difference(self, i: int, order: int) -> float:
        if order == 0:
            return self.ys[i]
        a = self._compute_finite_difference(i + 1, order - 1)
        b = self._compute_finite_difference(i, order - 1)
        return a - b
