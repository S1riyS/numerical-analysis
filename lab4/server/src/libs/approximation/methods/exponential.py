import math

from libs.approximation.methods import linear
from libs.approximation.methods.core.enums import ApproximationType
from libs.approximation.methods.core.method import IMethod
from libs.approximation.methods.linear import LinearMethod
from libs.approximation.models.result import ApproximationResult
from libs.approximation.models.validation import ValidationResult


class ExponentialMethod(IMethod):
    type_ = ApproximationType.EXPONENTIAL

    def validate(self) -> ValidationResult:
        if all([y > 0 for y in self.ys]):
            return ValidationResult(success=True)
        return ValidationResult(success=False, message="All Y values must be greater than 0")

    def run(self) -> ApproximationResult:
        log_ys = list(map(math.log, self.ys))

        # Linear approximation of (x, log(y))
        linear_approximation = LinearMethod(self.xs, log_ys)
        linear_result = linear_approximation.run()

        a = math.exp(linear_result.parameters["a"])
        a = round(a, 5)
        b = linear_result.parameters["b"]

        # f(x) = a * e^(bx)
        result_function = lambda x: a * math.exp(b * x)

        return ApproximationResult(
            result_function,
            parameters={
                "a": a,
                "b": b,
            },
        )
