from enum import Enum


class EquationMethod(Enum):
    CHORD = "Метод хорд"
    NEWTON = "Метод Ньютона"
    SIMPLE_ITERATIONS = "Метод простых итераций"

    def __repr__(self):
        return f"{self.value}"
