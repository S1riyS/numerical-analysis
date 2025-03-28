from dataclasses import dataclass
from enum import Enum


class DiscontinuityKind(Enum):
    REMOVABLE = "Removable"
    JUMP = "Jump"
    ESSENTIAL = "Essential"

    def __str__(self) -> str:
        return f"{self.value} discontinuity"


@dataclass
class Discontinuity:
    x: float
    kind: DiscontinuityKind

    def __str__(self) -> str:
        return f"{self.kind} at x = {round(self.x, 4)}"
