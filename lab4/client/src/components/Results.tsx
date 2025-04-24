// src/components/Results.tsx
import React from 'react';
import GraphCard from './GraphCard';
import { ApiResponse, Point } from '../api/types';

interface ResultsProps {
  results: ApiResponse | null;
  points: Point[];
}

const Results: React.FC<ResultsProps> = ({ results, points }) => {
  if (!results) return null;

  return (
    <div className="results-section">
      <h2>Approximation Results</h2>
      <div className="graphs-container">
        {results.results.map((result, index) => (
          <GraphCard 
            key={result.type_} 
            result={result} 
            points={points} 
            index={index} 
          />
        ))}
      </div>
    </div>
  );
};

export default Results;