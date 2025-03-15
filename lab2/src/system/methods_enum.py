from enum import Enum


class SystemMethod(Enum):
    NEWTON = "Метод Ньютона"

    def __repr__(self):
        return f"{self.value}"
