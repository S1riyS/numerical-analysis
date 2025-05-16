import { useState } from "react";

import { Button, Card, Col, Row } from "react-bootstrap";

import { Point } from "@common/types";

import { PointsControls } from "./PointsControls";
import { PointsTable } from "./PointsTable";

interface PointsManagerProps {
  minPoints?: number;
  maxPoints?: number;
  onPointsChange?: (points: Point[]) => void;
  children?: React.ReactNode;
}

export const PointsManager: React.FC<PointsManagerProps> = ({
  minPoints = 2,
  maxPoints = 10,
  onPointsChange,
}) => {
  const [points, setPoints] = useState<Point[]>(
    Array(minPoints)
      .fill(0)
      .map(() => ({ x: "", y: "" })),
  );

  const updatePoints = (newPoints: Point[]) => {
    setPoints(newPoints);
    onPointsChange?.(newPoints);
  };

  const handlePointChange = (
    index: number,
    field: keyof Point,
    value: string,
  ) => {
    const newPoints = [...points];
    newPoints[index] = { ...newPoints[index], [field]: value };
    updatePoints(newPoints);
  };

  const handleAddPoint = () => {
    if (points.length < maxPoints) {
      updatePoints([...points, { x: "", y: "" }]);
    }
  };

  const handleRemovePoint = (index: number) => {
    if (points.length > minPoints) {
      const newPoints = points.filter((_, i) => i !== index);
      updatePoints(newPoints);
    }
  };

  const handleFileUpload = (data: Point[]) => {
    // Фильтрация и валидация загруженных точек
    const validPoints = data
      .filter(
        (item) => typeof item.x === "number" && typeof item.y === "number",
      )
      .slice(0, maxPoints);

    if (validPoints.length >= minPoints) {
      updatePoints(validPoints);
    } else {
      alert(`Минимальное количество точек: ${minPoints}`);
    }
  };

  return (
    <Card>
      <Card.Header as="h5">Ввод точек</Card.Header>
      <Card.Body>
        <PointsTable
          points={points}
          onPointChange={handlePointChange}
          onRemovePoint={handleRemovePoint}
          minPoints={minPoints}
        />
      </Card.Body>
      <Card.Footer>
        <PointsControls
          onAddPoint={handleAddPoint}
          onFileUpload={handleFileUpload}
          maxPoints={maxPoints}
          currentCount={points.length}
        />
      </Card.Footer>
    </Card>
  );
};
