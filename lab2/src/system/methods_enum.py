from enum import Enum


class SystemMethod(Enum):
    NEWTON = "Метод Ньютона"

    def __str__(self):
        return f"{self.value}"
