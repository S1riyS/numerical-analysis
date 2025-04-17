import math

from libs.approximation.methods.core.enums import ApproximationType
from libs.approximation.methods.core.method import IMethod
from libs.approximation.methods.linear import LinearMethod
from libs.approximation.models.result import ApproximationResult
from libs.approximation.models.validation import ValidationResult


class LogarithmicMethod(IMethod):
    type_ = ApproximationType.LOGARITHMIC

    def validate(self) -> ValidationResult:
        if all([x > 0 for x in self.xs]):
            return ValidationResult(success=True)
        return ValidationResult(success=False, message="All X values must be greater than 0")

    def run(self) -> ApproximationResult:
        log_xs = list(map(math.log, self.xs))

        # Linear approximation of (log(x), y)
        linear_approximation = LinearMethod(log_xs, self.ys)
        linear_result = linear_approximation.run()

        a = linear_result.parameters["a"]
        b = linear_result.parameters["b"]

        # f(x) = a + b * log(x)
        result_function = lambda x: a + b * math.log(x)

        return ApproximationResult(
            result_function,
            parameters={
                "a": a,
                "b": b,
            },
        )
