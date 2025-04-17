import math

from libs.approximation.methods.core.enums import ApproximationType
from libs.approximation.methods.core.method import IMethod
from libs.approximation.methods.linear import LinearMethod
from libs.approximation.models.result import ApproximationResult
from libs.approximation.models.validation import ValidationResult


class PowerMethod(IMethod):
    type_ = ApproximationType.POWER

    def validate(self) -> ValidationResult:
        xs_are_positive = all([x > 0 for x in self.xs])
        ys_are_positive = all([y > 0 for y in self.ys])

        if xs_are_positive and ys_are_positive:
            return ValidationResult(success=True)
        return ValidationResult(success=False, message="All X and Y values must be greater than 0")

    def run(self) -> ApproximationResult:
        log_xs = list(map(math.log, self.xs))
        log_ys = list(map(math.log, self.ys))

        # Linear approximation of (log(x), log(y))
        linear_approximation = LinearMethod(log_xs, log_ys)
        linear_result = linear_approximation.run()

        a = math.exp(linear_result.parameters["a"])
        b = linear_result.parameters["b"]

        # f(x) = a * x^b
        result_function = lambda x: a * x**b

        return ApproximationResult(
            result_function,
            parameters={
                "a": a,
                "b": b,
            },
        )
