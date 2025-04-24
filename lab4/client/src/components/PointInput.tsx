// src/components/PointInput.tsx
import React from 'react';
import { Point } from '../api/types';

interface PointInputProps {
  point: Point;
  index: number;
  onChange: (index: number, field: 'x' | 'y', value: string) => void;
  onRemove: (index: number) => void;
  showRemove: boolean;
}

const PointInput: React.FC<PointInputProps> = ({ 
  point, 
  index, 
  onChange, 
  onRemove, 
  showRemove 
}) => (
  <div className="point-input">
    <span>Point {index + 1}:</span>
    <input
      type="number"
      placeholder="X"
      value={point.x}
      onChange={(e) => onChange(index, 'x', e.target.value)}
      step="any"
    />
    <input
      type="number"
      placeholder="Y"
      value={point.y}
      onChange={(e) => onChange(index, 'y', e.target.value)}
      step="any"
    />
    {showRemove && (
      <button onClick={() => onRemove(index)} className="remove-btn">
        ×
      </button>
    )}
  </div>
);

export default PointInput;