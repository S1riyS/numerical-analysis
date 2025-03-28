from enum import Enum
from typing import Any

from methods.method import IMethod
from methods.rectangle import RectangleMethod, RectangleMethodMode
from methods.simpson import SimpsonMethod
from methods.trapezoid import TrapeziodMethod
from models.integral import Integral


class MethodType(Enum):
    RECTANGLE = "rectangle"
    TRAPEZAIOD = "trapezoid"
    SIMPSON = "simpson"


class MethodFactory:
    def __init__(self, integral: Integral, epsilon: float):
        self.integral = integral
        self.epsilon = epsilon

    def get_method(self, type_: MethodType, **kwargs: Any) -> IMethod:
        if type_ == MethodType.RECTANGLE:
            mode = kwargs.get("mode", None)
            if mode is None or not isinstance(mode, RectangleMethodMode):
                return RectangleMethod(self.integral, self.epsilon)
            return RectangleMethod(self.integral, self.epsilon, mode)

        elif type_ == MethodType.TRAPEZAIOD:
            return TrapeziodMethod(self.integral, self.epsilon)

        elif type_ == MethodType.SIMPSON:
            return SimpsonMethod(self.integral, self.epsilon)

        raise ValueError("Unknown method type")
