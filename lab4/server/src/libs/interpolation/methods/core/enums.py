from enum import Enum


class InterpolationMethod(str, Enum):
    LAGRANGE = "LAGRANGE"
    NEWTON_DIVIDED_DIFFERENCES = "NEWTON_DIVIDED_DIFFERENCES"
    NEWTON_FINITE_DIFFERENCES = "NEWTON_FINITE_DIFFERENCES"


class PointInterpolationMethod(str, Enum):
    STIRLING = "STIRLING"
    BESSEL = "BESSEL"
