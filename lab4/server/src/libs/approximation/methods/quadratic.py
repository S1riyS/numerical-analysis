import numpy as np
from libs.approximation.methods.core.enums import ApproximationType
from libs.approximation.methods.core.method import IMethod
from libs.approximation.models.result import ApproximationResult
from libs.approximation.models.validation import ValidationResult
from libs.approximation.utils.system import solve_system


class QuadraticMethod(IMethod):
    type_ = ApproximationType.QUADRATIC

    def validate(self) -> ValidationResult:
        return ValidationResult(success=True)

    def run(self) -> ApproximationResult:
        sx1 = sum(self.xs)
        sx2 = sum(x**2 for x in self.xs)
        sx3 = sum(x**3 for x in self.xs)
        sx4 = sum(x**4 for x in self.xs)

        sy = sum(self.ys)
        sxy = sum(x * y for x, y in zip(self.xs, self.ys))
        sxxy = sum(x**2 * y for x, y in zip(self.xs, self.ys))

        A = np.array(
            [
                [self.n, sx1, sx2],
                [sx1, sx2, sx3],
                [sx2, sx3, sx4],
            ]
        )
        B = np.array([sy, sxy, sxxy])

        a, b, c = solve_system(A, B)

        # f(x) = a + bx + cx^2
        result_function = lambda x: a + b * x + c * x**2

        return ApproximationResult(
            result_function,
            parameters={
                "a": a,
                "b": b,
                "c": c,
            },
        )
