import React, { useMemo } from "react";

import { Card, Col, Row } from "react-bootstrap";
import { InlineMath } from "react-katex";

import { FunctionPlot } from "@common/components";
import { Point } from "@common/types";
import {
  InterpolationResponse,
  PointInterpolationResponse,
} from "@interpolation/api/types";
import { XsYsListToPoints } from "@interpolation/utils/mappers";
import { fExprToFunction, fExprToKatex } from "@interpolation/utils/parse";

interface ResultViewProps {
  result?: InterpolationResponse | PointInterpolationResponse;
  error?: string;
}

// Type guards for precise type checking
function isPointInterpolationResponse(
  response: InterpolationResponse | PointInterpolationResponse,
): response is PointInterpolationResponse {
  return (response as PointInterpolationResponse).x_value !== undefined;
}

function hasValidData<T extends { data: any }>(
  response: T,
): response is T & { data: NonNullable<T["data"]> } {
  return response.data !== null;
}

export const ResultView: React.FC<ResultViewProps> = ({ result, error }) => {
  if (error) {
    return (
      <Card className="mt-3 border-danger">
        <Card.Header className="bg-danger text-white">Ошибка</Card.Header>
        <Card.Body>
          <Card.Text>{error}</Card.Text>
        </Card.Body>
      </Card>
    );
  }

  if (!result) return null;

  if (!result.success) {
    return (
      <Card className="mt-3 border-danger">
        <Card.Header className="bg-danger text-white">
          Ошибка вычисления
        </Card.Header>
        <Card.Body>
          <Card.Text>
            {result.message || "Неизвестная ошибка при выполнении интерполяции"}
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }

  if (!hasValidData(result)) {
    return (
      <Card className="mt-3 border-warning">
        <Card.Header className="bg-warning text-white">Результат</Card.Header>
        <Card.Body>
          <Card.Text>
            Вычисления выполнены успешно, но данные отсутствуют
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }

  const callable_function = useMemo(
    () => fExprToFunction(result.data.f_expr),
    [JSON.stringify(result)],
  );
  if (!callable_function) {
    return (
      <Card className="mt-3 border-warning">
        <Card.Header className="bg-warning text-white">Результат</Card.Header>
        <Card.Body>
          <Card.Text>
            Вычисления выполнены успешно, но функция не может быть вычислена
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }

  const latex = fExprToKatex(result.data.f_expr);
  const minX = Math.min(...result.points.xs);
  const maxX = Math.max(...result.points.xs);
  const padding = (maxX - minX) * 0.1;

  return (
    <Card className="mt-3">
      <Card.Header as={"h5"}>Результат</Card.Header>
      <Card.Body>
        <FunctionPlot
          func={callable_function}
          minX={minX - padding}
          maxX={maxX + padding}
          points={XsYsListToPoints(result.points)}
          singlePoint={{
                  x: result.x_value.toString(),
                  y: result.data.y_value.toString(),
                } as Point}
        />
          <>
            <Row className="mt-2">
              <Col sm={4}>Функция:</Col>
              <Col sm={8} className="font-monospace">
                <InlineMath math={`f(x) = ${latex}`}></InlineMath>
              </Col>
            </Row>
            <Row className="mt-2">
              <Col sm={4}>Значение функции:</Col>
              <Col sm={8} className="font-monospace">
                <InlineMath
                  math={`f(${result.x_value.toFixed(6)}) = ${result.data.y_value.toFixed(6)}`}
                ></InlineMath>
              </Col>
            </Row>
          </>
      </Card.Body>
    </Card>
  );
};
