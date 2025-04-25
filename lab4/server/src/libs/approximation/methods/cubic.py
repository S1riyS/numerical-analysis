import numpy as np
from libs.approximation.methods.core.enums import ApproximationType
from libs.approximation.methods.core.method import IMethod
from libs.approximation.models.result import ApproximationResult
from libs.approximation.models.validation import ValidationResult
from libs.approximation.utils.system import solve_system


class CubicMethod(IMethod):
    type_ = ApproximationType.CUBIC

    def validate(self) -> ValidationResult:
        return ValidationResult(success=True)

    def run(self) -> ApproximationResult:
        sx1 = sum(self.xs)
        sx2 = sum(x**2 for x in self.xs)
        sx3 = sum(x**3 for x in self.xs)
        sx4 = sum(x**4 for x in self.xs)
        sx5 = sum(x**5 for x in self.xs)
        sx6 = sum(x**6 for x in self.xs)

        sy = sum(self.ys)
        sxy = sum(x * y for x, y in zip(self.xs, self.ys))
        sxxy = sum(x**2 * y for x, y in zip(self.xs, self.ys))
        sxxxy = sum(x**3 * y for x, y in zip(self.xs, self.ys))

        A = np.array(
            [
                [self.n, sx1, sx2, sx3],
                [sx1, sx2, sx3, sx4],
                [sx2, sx3, sx4, sx5],
                [sx3, sx4, sx5, sx6],
            ]
        )
        B = np.array([sy, sxy, sxxy, sxxxy])

        a, b, c, d = solve_system(A, B)

        # f(x) = a + bx + cx^2 + dx^3
        result_function = lambda x: a + b * x + c * x**2 + d * x**3

        return ApproximationResult(
            result_function,
            parameters={
                "a": a,
                "b": b,
                "c": c,
                "d": d,
            },
        )
