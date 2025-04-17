from typing import Dict, List, Optional

from libs.approximation.methods.core.enums import ApproximationType
from pydantic import BaseModel, Field, model_validator


class ApproximationRequest(BaseModel):
    xs: List[float] = Field(min_length=8, max_length=12)
    ys: List[float] = Field(min_length=8, max_length=12)

    @model_validator(mode="after")
    def length_match(self):
        if len(self.xs) != len(self.ys):
            raise ValueError("Lenths of xs and ys must match")
        return self


class ApproximationResultData(BaseModel):
    """Data class for successful approximation"""

    measure_of_deviation: float
    mse: float
    coefficient_of_determination: float
    parameters: Dict[str, float]


class ApproximationResultSchema(BaseModel):
    """Data class for approximation result"""

    type_: ApproximationType
    success: bool
    message: Optional[str] = None
    data: Optional[ApproximationResultData] = None


class ApproximationResponse(BaseModel):
    results: List[ApproximationResultSchema]
