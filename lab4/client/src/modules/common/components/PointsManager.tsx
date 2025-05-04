import { useState } from 'react';
import { PointsTable } from './PointsTable';
import { PointsControls } from './PointsControls';
import { Point } from '@common/types';

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
    Array(minPoints).fill(0).map(() => ({ x: '', y: '' }))
  );

  const updatePoints = (newPoints: Point[]) => {
    setPoints(newPoints);
    onPointsChange?.(newPoints);
  };

  const handlePointChange = (index: number, field: keyof Point, value: string) => {
    const newPoints = [...points];
    newPoints[index] = { ...newPoints[index], [field]: value };
    updatePoints(newPoints);
  };

  const handleAddPoint = () => {
    if (points.length < maxPoints) {
      updatePoints([...points, { x: '', y: '' }]);
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
    const validPoints = data.filter(item => 
      typeof item.x === 'string' && typeof item.y === 'string'
    ).slice(0, maxPoints);
    
    if (validPoints.length >= minPoints) {
      updatePoints(validPoints);
    } else {
      alert(`Минимальное количество точек: ${minPoints}`);
    }
  };

  return (
    <div className="points-manager">
      <PointsTable
        points={points}
        onPointChange={handlePointChange}
        onRemovePoint={handleRemovePoint}
        minPoints={minPoints}
      />
      
      <div className="mt-2 mb-2 text-muted">
        Точки: {points.length} (min: {minPoints}, max: {maxPoints})
      </div>

      <PointsControls
        onAddPoint={handleAddPoint}
        onFileUpload={handleFileUpload}
        maxPoints={maxPoints}
        currentCount={points.length}
      />
    </div>
  );
};