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
    <>
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
      </>
  );
};
