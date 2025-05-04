// src/components/PointInput.tsx
import React from 'react';
import styles from './PointInput.module.css';
import { Point } from '@common/api/types';

interface PointInputProps {
  point: Point;
  index: number;
  onChange: (index: number, field: 'x' | 'y', value: string) => void;
  onRemove: (index: number) => void;
  showRemove: boolean;
}

export const PointInput: React.FC<PointInputProps> = ({ 
  point, 
  index, 
  onChange, 
  onRemove, 
  showRemove 
}) => (
  <div className={styles.pointInput}>
    <span className={styles.pointLabel}>Point {index + 1}:</span>
    <input
      type="number"
      placeholder="X"
      value={point.x}
      onChange={(e) => onChange(index, 'x', e.target.value)}
      step="any"
      className={styles.coordInput}
    />
    <input
      type="number"
      placeholder="Y"
      value={point.y}
      onChange={(e) => onChange(index, 'y', e.target.value)}
      step="any"
      className={styles.coordInput}
    />
    {showRemove && (
      <button onClick={() => onRemove(index)} className={styles.removeBtn}>
        ×
      </button>
    )}
  </div>
);