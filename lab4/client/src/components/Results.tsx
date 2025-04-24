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

  // Разбиваем результаты на пары для сетки
  const resultPairs = [];
  for (let i = 0; i < results.results.length; i += 2) {
    resultPairs.push(results.results.slice(i, i + 2));
  }

  return (
    <div className={styles.resultsSection}>
      <h2 className={styles.sectionTitle}>Approximation Results</h2>
      
      <div className={styles.gridContainer}>
        {results.results.map((result) => (
          <div key={result.type_} className={styles.gridItem}>
            <GraphCard result={result} points={points} />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Results;