from dataclasses import dataclass


@dataclass
class ErrorResponse:
    scope: str
    message: str


@dataclass
class ResultResponse:
    value: float
    partition_number: int
