from typing import List

from libs.interpolation.methods.core.enums import (
    InterpolationMethod,
    PointInterpolationMethod,
)
from pydantic import BaseModel, ConfigDict, Field, model_validator


class FloatRoundedBaseModel(BaseModel):
    model_config = ConfigDict(json_encoders={float: lambda v: round(v, 5)})


class PointsList(FloatRoundedBaseModel):
    xs: List[float] = Field(min_length=2)
    ys: List[float] = Field(min_length=2)

    @model_validator(mode="after")
    def length_match(self) -> "PointsList":
        if len(self.xs) != len(self.ys):
            raise ValueError("Lengths of xs and ys must match")
        return self

    @model_validator(mode="after")
    def xs_unique(self) -> "PointsList":
        if len(set(self.xs)) != len(self.xs):
            raise ValueError("All xs must be unique")
        return self


class InterpolationRequest(FloatRoundedBaseModel):
    points: PointsList
    method: InterpolationMethod
    x_value: float


class InterpolationData(FloatRoundedBaseModel):
    y_value: float
    f_expr: str


class InterpolationResponse(FloatRoundedBaseModel):
    method: InterpolationMethod
    points: PointsList
    x_value: float
    success: bool
    message: str | None = None
    data: InterpolationData | None


class PointInterpolationRequest(FloatRoundedBaseModel):
    points: PointsList
    method: PointInterpolationMethod
    x_value: float


class PointInterpolationData(FloatRoundedBaseModel):
    f_expr: str
    y_value: float


class PointInterpolationResponse(FloatRoundedBaseModel):
    method: PointInterpolationMethod
    points: PointsList
    x_value: float
    success: bool
    message: str | None = None
    data: PointInterpolationData | None
