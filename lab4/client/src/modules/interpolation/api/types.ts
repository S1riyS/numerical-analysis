import {
  InterpolationMethod,
  PointInterpolationMethod,
} from "@interpolation/types";

export interface PointsList {
  xs: number[];
  ys: number[];
}

export interface InterpolationData {
  f_expr: string;
}

export interface InterpolationRequest {
  points: PointsList;
  method: InterpolationMethod;
}

export interface InterpolationResponse {
  method: InterpolationMethod;
  points: PointsList;
  success: boolean;
  message: string | null;
  data: InterpolationData | null;
}

export interface PointInterpolationData {
  f_expr: string;
  y_value: number;
}

export interface PointInterpolationRequest {
  points: PointsList;
  method: PointInterpolationMethod;
  x_value: number;
}

export interface PointInterpolationResponse {
  method: PointInterpolationMethod;
  points: PointsList;
  x_value: number;
  success: boolean;
  message: string | null;
  data: PointInterpolationData | null;
}
