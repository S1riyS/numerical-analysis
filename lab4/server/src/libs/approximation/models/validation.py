from dataclasses import dataclass
from typing import Optional


@dataclass
class ValidationResult:
    success: bool
    message: Optional[str] = None
