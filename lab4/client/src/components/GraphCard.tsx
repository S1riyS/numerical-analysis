// src/components/GraphCard.tsx
import React, { useEffect, useRef } from 'react';
import { ApproximationResult } from '../api/types';

interface GraphCardProps {
  result: ApproximationResult;
  points: { x: string; y: string }[];
  index: number;
}

const GraphCard: React.FC<GraphCardProps> = ({ result, points, index }) => {
  const graphRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!window.Desmos || !graphRef.current) return;

    const calculator = window.Desmos.GraphingCalculator(graphRef.current, {
      keypad: false,
      expressions: false
    });

    // Add original points
    const xs = points.map(p => parseFloat(p.x)).filter(x => !isNaN(x));
    const ys = points.map(p => parseFloat(p.y)).filter(y => !isNaN(y));
    
    if (xs.length > 0 && ys.length > 0 && xs.length === ys.length) {
      calculator.setExpression({
        id: 'points',
        type: 'table',
        columns: [
          { values: xs.map(String), id: 'x', latex: 'x' },
          { values: ys.map(String), id: 'y', latex: 'y' }
        ],
        lines: false,
        points: true
      });
    }

    // Add the approximation function
    const functionExpression = getFunctionExpression(result);
    if (functionExpression) {
      calculator.setExpression({
        id: 'function',
        latex: functionExpression
      });
    }

    return () => {
      calculator.destroy();
    };
  }, [result, points]);

  const getFunctionExpression = (result: ApproximationResult): string | null => {
    const params = result.data.parameters;
    switch (result.type_) {
      case 'linear': return `y=${params.a}x+${params.b}`;
      case 'quadratic': return `y=${params.a}+${params.b}x+${params.c}x^2`;
      case 'cubic': return `y=${params.a}+${params.b}x+${params.c}x^2+${params.d}x^3`;
      case 'exponential': return `y=${params.a}e^{${params.b}x}`;
      case 'logarithmic': return `y=${params.a}+${params.b}log(x)`;
      case 'power': return `y=${params.a}x^{${params.b}}`;
      default: return null;
    }
  };

  return (
    <div className="graph-card">
      <h3>{result.type_} Function</h3>
      <div className="graph" ref={graphRef}></div>
      <div className="parameters">
        <h4>Parameters:</h4>
        <ul>
          {Object.entries(result.data.parameters).map(([key, value]) => (
            <li key={key}>
              <strong>{key}:</strong> {value.toFixed(6)}
            </li>
          ))}
        </ul>
        <h4>Quality Metrics:</h4>
        <ul>
          <li><strong>Deviation:</strong> {result.data.measure_of_deviation.toFixed(6)}</li>
          <li><strong>MSE:</strong> {result.data.mse.toFixed(6)}</li>
          <li><strong>R²:</strong> {result.data.coefficient_of_determination.toFixed(6)}</li>
        </ul>
        <div className="function-expression">
          <strong>Function:</strong> {getFunctionExpression(result)}
        </div>
      </div>
    </div>
  );
};

export default GraphCard;