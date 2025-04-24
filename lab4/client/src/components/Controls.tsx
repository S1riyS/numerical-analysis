// src/components/Controls.tsx
import React, { ChangeEvent } from 'react';

interface ControlsProps {
  onAddPoint: () => void;
  onClearAll: () => void;
  onFileUpload: (e: ChangeEvent<HTMLInputElement>) => void;
  onSubmit: () => void;
  onSave: () => void;
  pointsCount: number;
  hasResults: boolean;
  loading: boolean;
}

const Controls: React.FC<ControlsProps> = ({
  onAddPoint,
  onClearAll,
  onFileUpload,
  onSubmit,
  onSave,
  pointsCount,
  hasResults,
  loading,
}) => (
  <div className="controls">
    <button onClick={onAddPoint} disabled={pointsCount >= 12}>
      Add Point
    </button>
    <button onClick={onClearAll}>Clear All</button>
    <div className="file-upload">
      <label>
        Load from File
        <input
          type="file"
          accept=".txt,.csv"
          onChange={onFileUpload}
          style={{ display: 'none' }}
        />
      </label>
    </div>
    <button onClick={onSubmit} disabled={loading}>
      {loading ? 'Processing...' : 'Calculate Approximation'}
    </button>
    {hasResults && (
      <button onClick={onSave}>Save Results</button>
    )}
  </div>
);

export default Controls;