import numpy as np
from libs.approximation.methods.core.enums import ApproximationType
from libs.approximation.methods.core.method import IMethod
from libs.approximation.models.result import ApproximationResult
from libs.approximation.models.validation import ValidationResult
from libs.approximation.utils.statistic import compute_pearson_correlation


class LinearMethod(IMethod):
    type_ = ApproximationType.LINEAR

    def validate(self):
        return ValidationResult(success=True)

    def run(self) -> ApproximationResult:
        sx = sum(self.xs)
        sxx = sum(x**2 for x in self.xs)
        sy = sum(self.ys)
        sxy = sum(x * y for x, y in zip(self.xs, self.ys))

        A = np.array([[sxx, sx], [sx, self.n]])
        B = np.array([sxy, sy])

        a, b = np.linalg.solve(A, B)

        # f(x) = ax + b
        result_function = lambda x: a * x + b

        pearson_correlation = compute_pearson_correlation(self.xs, self.ys)
        return ApproximationResult(
            result_function,
            parameters={
                "a": a,
                "b": b,
                "pearson_correlation": pearson_correlation,
            },
        )
