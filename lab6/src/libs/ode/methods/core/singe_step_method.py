from abc import abstractmethod

from libs.ode.methods.core.method import ODEMethod


class SingleStepODEMethod(ODEMethod):
    @property
    @abstractmethod
    def order_of_accuracy(self) -> int: ...

    def _get_current_accuracy(self) -> float:
        if self.previous_yn is None:
            return float("inf")

        current_yn = self.ys[-1]
        numerator: float = abs(current_yn - self.previous_yn)
        denominator: int = 2**self.order_of_accuracy - 1

        return numerator / denominator
