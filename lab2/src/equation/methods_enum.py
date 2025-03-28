from enum import Enum


class EquationMethod(Enum):
    CHORD = "Метод хорд"
    NEWTON = "Метод Ньютона"
    SIMPLE_ITERATIONS = "Метод простых итераций"

    def __str__(self):
        return f"{self.value}"
