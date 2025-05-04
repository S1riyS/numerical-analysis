import numpy as np
from libs.approximation.methods.core.enums import ApproximationType
from libs.approximation.methods.core.method import IMethod
from libs.approximation.models.result import ApproximationResult
from libs.approximation.models.validation import ValidationResult
from libs.approximation.utils.statistic import compute_pearson_correlation
from libs.approximation.utils.system import solve_system


class LinearMethod(IMethod):
    type_ = ApproximationType.LINEAR

    def validate(self):
        return ValidationResult(success=True)

    def run(self) -> ApproximationResult:
        sx = sum(self.xs)
        sxx = sum(x**2 for x in self.xs)
        sy = sum(self.ys)
        sxy = sum(x * y for x, y in zip(self.xs, self.ys))

        A = np.array([[self.n, sx], [sx, sxx]])
        B = np.array([sy, sxy])

        print("DEBUG")
        print(f"n: {self.n}")
        print(f"sx: {sx}")
        print(f"sxx: {sxx}")
        print(f"sy: {sy}")
        print(f"sxy: {sxy}")

        a, b = solve_system(A, B)

        # f(x) = a + bx
        result_function = lambda x: a + b * x

        pearson_correlation = compute_pearson_correlation(self.xs, self.ys)
        return ApproximationResult(
            result_function,
            parameters={
                "a": a,
                "b": b,
                "pearson_correlation": pearson_correlation,
            },
        )
