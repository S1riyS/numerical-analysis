from enum import Enum


class ODEMethodType(str, Enum):
    EULER = "EULER"
    RUNGE_KUTTA = "RUNGE_KUTTA"
    ADAMS = "ADAMS"
