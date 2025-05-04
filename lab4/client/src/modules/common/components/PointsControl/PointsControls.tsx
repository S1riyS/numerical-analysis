import { ChangeEvent, forwardRef } from 'react';
import styles from './Controls.module.css';

interface PointsControlsProps {
  onAddPoint: () => void;
  onClearAll: () => void;
  onFileUpload: (e: ChangeEvent<HTMLInputElement>) => void;
  onSubmit: () => void;
  onSave: () => void;
  pointsCount: number;
  hasResults: boolean;
  loading: boolean;
}

export const PointsControls = forwardRef<HTMLInputElement, PointsControlsProps>(({
  onAddPoint,
  onClearAll,
  onFileUpload,
  onSubmit,
  onSave,
  pointsCount,
  hasResults,
  loading,
}, ref) => (
  <div className={styles.container}>
    {/* Row 1: Add Point and Clear All */}
    <div className={styles.buttonRow}>
      <button 
        className={`${styles.btn} ${styles.primary}`} 
        onClick={onAddPoint} 
        disabled={pointsCount >= 12}
      >
        Add Point
      </button>
      <button 
        className={`${styles.btn} ${styles.warning}`} 
        onClick={onClearAll}
      >
        Clear All
      </button>
    </div>

    {/* Row 2: File Operations */}
    <div className={styles.buttonRow}>
    <button className={`${styles.btn} ${styles.fileUpload}`}>
      Load from File
      <input
        type="file"
        accept=".txt,.csv"
        onChange={onFileUpload}
        className={styles.fileInput}
        ref={ref}
      />
    </button>
      {hasResults && (
        <button 
          className={`${styles.btn} ${styles.success}`} 
          onClick={onSave}
        >
          Save Results
        </button>
      )}
    </div>

    {/* Row 3: Calculate Approximation */}
    <div className={styles.buttonRow}>
      <button 
        className={`${styles.btn} ${styles.submit}`} 
        onClick={onSubmit} 
        disabled={loading}
      >
        {loading ? (
          <span className={styles.loading}>
            <span className={styles.spinner}></span>
            Processing...
          </span>
        ) : (
          'Calculate Approximation'
        )}
      </button>
    </div>
  </div>
));
