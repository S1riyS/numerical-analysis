import { Point } from "@common/types";
import { PointsList } from "@interpolation/api/types";
import {
  InterpolationMethod,
  PointInterpolationMethod,
} from "@interpolation/types";

export function interpolationMethodToName(method: InterpolationMethod): string {
  switch (method) {
    case InterpolationMethod.LAGRANGE:
      return "Лагранжа";
    case InterpolationMethod.NEWTON_DIVIDED_DIFFERENCES:
      return "Ньютона с разделенными разностями";
    case InterpolationMethod.NEWTON_FINITE_DIFFERENCES:
      return "Ньютона с конечными разностями";
  }
}

export function pointInterpolationMethodToName(
  method: PointInterpolationMethod,
): string {
  switch (method) {
    case PointInterpolationMethod.STIRLING:
      return "Стирлинга";
    case PointInterpolationMethod.BESSEL:
      return "Бесселя";
  }
}

export function XsYsListToPoints(pointsList: PointsList): Point[] {
  const { xs, ys } = pointsList;

  // Check if the arrays are of equal length
  if (xs.length !== ys.length) {
    throw new Error("xs and ys arrays must be of equal length");
  }

  return xs.map((x, index) => ({
    x: x.toString(),
    y: ys[index].toString(),
  }));
}
