import { forwardRef, useImperativeHandle, useState } from "react";

import { Card, Col, Form, Row } from "react-bootstrap";

import { Point } from "@common/types";

type MathFunction = (x: number) => number;

interface FunctionOption {
  name: string;
  callable_func: MathFunction;
}

interface FunctionInputProps {
  onEvaluate?: (points: Point[]) => void;
}

export interface FunctionInputHandle {
  handleEvaluate: () => Point[];
}

export const FunctionInput = forwardRef<
  FunctionInputHandle,
  FunctionInputProps
>(({ onEvaluate }, ref) => {
  // Available function options
  const functionOptions: FunctionOption[] = [
    { name: "Экспонента (y = e^x)", callable_func: (x) => Math.exp(x) },
    { name: "Синус (y = sin(x))", callable_func: (x) => Math.sin(x) },
    { name: "Косинус (y = cos(x))", callable_func: (x) => Math.cos(x) },
  ];

  // State for user inputs
  const [selectedFunctionIndex, setSelectedFunctionIndex] = useState<number>(0);
  const [a, setA] = useState<number>(-1);
  const [b, setB] = useState<number>(1);
  const [n, setN] = useState<number>(5);
  const [_, setPoints] = useState<Point[]>([]);

  // Calculate points based on current inputs
  const calculatePoints = (): Point[] => {
    if (n <= 0) return [];
    if (a >= b) return [];

    const step = (b - a) / (n - 1);
    const calculatedPoints: Point[] = [];
    const selectedFunction =
      functionOptions[selectedFunctionIndex].callable_func;

    for (let i = 0; i < n; i++) {
      const x = a + i * step;
      const y = selectedFunction(x);
      calculatedPoints.push({ x: `${x}`, y: `${y}` });
    }

    return calculatedPoints;
  };

  // Handle evaluation (can be called from parent component via ref)
  const handleEvaluate = () => {
    const newPoints = calculatePoints();
    setPoints(newPoints);
    if (onEvaluate) {
      onEvaluate(newPoints);
    }
    return newPoints;
  };

  // Expose the handleEvaluate function to parent via ref
  useImperativeHandle(ref, () => ({
    handleEvaluate,
  }));

  return (
    <Card className="mb-4">
      <Card.Header as="h5">Функция на интервале</Card.Header>
      <Card.Body>
        <Form>
          <Form.Group as={Row} className="mb-3">
            <Form.Label column sm={3}>
              Функция:
            </Form.Label>
            <Col sm={9}>
              <Form.Select
                value={selectedFunctionIndex}
                onChange={(e) => {
                  setSelectedFunctionIndex(parseInt(e.target.value));
                }}
              >
                {functionOptions.map((option, index) => (
                  <option key={option.name} value={index}>
                    {option.name}
                  </option>
                ))}
              </Form.Select>
            </Col>
          </Form.Group>

          <Row className="mb-3">
            <Col sm={6}>
              <Form.Group>
                <Form.Label>Начало интервала:</Form.Label>
                <Form.Control
                  type="number"
                  value={a}
                  onChange={(e) => setA(parseFloat(e.target.value))}
                />
              </Form.Group>
            </Col>
            <Col sm={6}>
              <Form.Group>
                <Form.Label>Конец интервала:</Form.Label>
                <Form.Control
                  type="number"
                  value={b}
                  onChange={(e) => setB(parseFloat(e.target.value))}
                />
              </Form.Group>
            </Col>
          </Row>

          <Form.Group className="mb-3">
            <Form.Label>Количество точек:</Form.Label>
            <Form.Control
              type="number"
              min="2"
              value={n}
              onChange={(e) => setN(parseInt(e.target.value))}
            />
          </Form.Group>
        </Form>
      </Card.Body>
    </Card>
  );
});

FunctionInput.displayName = "FunctionEvaluator";
