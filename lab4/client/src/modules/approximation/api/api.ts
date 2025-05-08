import { Point } from "@common/types";

import { ApproximationResponse } from "./types";

export class ApiService {
  static async analyzePoints(points: Point[]): Promise<ApproximationResponse> {
    const xs = points.map((p) => parseFloat(p.x));
    const ys = points.map((p) => parseFloat(p.y));

    if (xs.some(isNaN) || ys.some(isNaN)) {
      throw new Error("Все координаты должны быть числами");
    }

    const response = await fetch("http://localhost:8000/api/approximation", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ xs, ys }),
    });

    if (!response.ok) {
      throw new Error(`Ошибка сервера: ${response.status}`);
    }

    return await response.json();
  }
}
