// src/components/Results.tsx
import React from 'react';
import GraphCard from './GraphCard';
import { ApiResponse, Point } from 'api/types';
import styles from './Results.module.css';

interface ResultsProps {
  results: ApiResponse | null;
  points: Point[];
}

const Results: React.FC<ResultsProps> = ({ results, points }) => {
  if (!results) return null;

  // Find the best approximation (lowest MSE)
  let bestType: string | null = null;
  let lowestMSE = Infinity;
  
  results.results.forEach(result => {
    if (result.success && result.data && result.data.mse < lowestMSE) {
      lowestMSE = result.data.mse;
      bestType = result.type_;
    }
  });

  return (
    <div className={styles.resultsSection}>
      <h2 className={styles.sectionTitle}>Approximation Results</h2>
      
      <div className={styles.gridContainer}>
        {results.results.map((result) => (
          <div key={result.type_} className={styles.gridItem}>
            <GraphCard 
              result={result} 
              points={points} 
              isBest={result.type_ === bestType && result.success}
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Results;