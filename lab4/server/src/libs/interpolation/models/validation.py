from dataclasses import dataclass


@dataclass
class InterpolationValidation:
    success: bool
    message: str | None
