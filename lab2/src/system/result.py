from dataclasses import dataclass


@dataclass
class SystemResult:
    root_x: float
    root_y: float
    iterations: int
    decimal_places: int

    def __str__(self):
        return (
            f"Найденное решение системы:\n"
            f"x = {round(self.root_x, self.decimal_places)}\n"
            f"y = {round(self.root_y, self.decimal_places)}\n"
            f"Число итераций: {self.iterations}"
        )
