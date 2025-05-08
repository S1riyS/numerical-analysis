import { Card } from "react-bootstrap";

import { Point } from "@common/types";

import { PointInput } from "./PointInput";

interface PointsTableProps {
  points: Point[];
  onPointChange: (index: number, field: keyof Point, value: string) => void;
  onRemovePoint: (index: number) => void;
  minPoints: number;
}

export const PointsTable: React.FC<PointsTableProps> = ({
  points,
  onPointChange,
  onRemovePoint,
  minPoints,
}) => {
  return (
    <Card className="mb-2 pb-2">
      <Card.Body className="pb-0">
        <Card.Title>Таблица точек</Card.Title>
        {points.map((point, index) => (
          <PointInput
            key={index}
            point={point}
            onXChange={(value) => onPointChange(index, "x", value)}
            onYChange={(value) => onPointChange(index, "y", value)}
            onRemove={() => onRemovePoint(index)}
            canRemove={points.length > minPoints}
          />
        ))}
      </Card.Body>
    </Card>
  );
};
