from dataclasses import dataclass
from typing import Callable, Dict


@dataclass
class ApproximationResult:
    function: Callable[[float], float]
    parameters: Dict[str, float]
