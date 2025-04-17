from typing import List, Type

from libs.approximation.methods.core.method import IMethod

from .cubic import CubicMethod
from .exponential import ExponentialMethod
from .linear import LinearMethod
from .logarithmic import LogarithmicMethod
from .power import PowerMethod
from .quadratic import QuadraticMethod

approximation_methods: List[Type[IMethod]] = [
    LinearMethod,
    QuadraticMethod,
    CubicMethod,
    ExponentialMethod,
    LogarithmicMethod,
    PowerMethod,
]

__all__ = [method.__name__ for method in approximation_methods]
