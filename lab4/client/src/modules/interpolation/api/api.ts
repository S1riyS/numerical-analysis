import { Point } from "@common/types";
import {
  InterpolationMethod,
  PointInterpolationMethod,
} from "@interpolation/types";

import {
  InterpolationRequest,
  InterpolationResponse,
  PointInterpolationRequest,
  PointInterpolationResponse,
  PointsList,
} from "./types";

export class ApiService {
  private static apiBaseUrl = "http://localhost:8000/api";

  private static preparePoints(points: Point[]): PointsList {
    const xs = points.map((p) => parseFloat(p.x));
    const ys = points.map((p) => parseFloat(p.y));

    if (xs.some(isNaN) || ys.some(isNaN)) {
      throw new Error("All coordinates must be numbers");
    }

    return { xs, ys };
  }

  private static async makeRequest<T>(
    endpoint: string,
    body: object,
  ): Promise<T> {
    const response = await fetch(`${this.apiBaseUrl}${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      const responseJson = await response.json();
      if (responseJson.detail) {
        // Pydantic error
        const errorMessages = responseJson.detail.map((error: any) => {
          // Extract field name from loc (skip 'body' and take the last element)
          const fieldPath = error.loc.slice(1).join('.');
          return ` ${fieldPath}: ${error.msg}`;
        }).join('\n');
        
        throw new Error(`Validation errors:\n${errorMessages}`);
      } else {
      throw new Error(`Server error: ${response.status}`);
      }
    }

    return await response.json();
  }

  static async interpolate(
    points: Point[],
    method: InterpolationMethod,
    xValue: number
  ): Promise<InterpolationResponse> {
    const pointsList = this.preparePoints(points);
    const request: InterpolationRequest = {
      points: pointsList,
      method,
      x_value: xValue, 
    };

    return this.makeRequest<InterpolationResponse>("/interpolation/", request);
  }

  static async interpolatePoint(
    points: Point[],
    method: PointInterpolationMethod,
    xValue: number,
  ): Promise<PointInterpolationResponse> {
    const pointsList = this.preparePoints(points);
    const request: PointInterpolationRequest = {
      points: pointsList,
      method,
      x_value: xValue,
    };

    return this.makeRequest<PointInterpolationResponse>(
      "/interpolation/point",
      request,
    );
  }
}
