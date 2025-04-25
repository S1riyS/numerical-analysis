import React, { useEffect, useRef, useState } from 'react';
import { ApproximationResult, Point } from 'api/types';

import 'katex/dist/katex.min.css';
import { InlineMath } from 'react-katex';
import { capitalize } from 'utils/strings';

import styles from './GraphCard.module.css'; // New stylesheet

interface GraphCardProps {
  result: ApproximationResult;
  points: Point[];
  isBest: boolean;
}

const GraphCard: React.FC<GraphCardProps> = ({ 
  result, 
  points,
  isBest 
}) => {
  const graphRef = useRef<HTMLDivElement>(null);
  const [graphError, setGraphError] = useState(false);
  const desmosScriptRef = useRef<HTMLScriptElement | null>(null);
  const calculatorRef = useRef<any>(null);

  useEffect(() => {
    if (!graphRef.current || !result.success || !result.data) return;

    const loadDesmos = () => {
      // Check if script is already loaded or loading
      if (desmosScriptRef.current || window.Desmos) {
        if (window.Desmos) {
          createCalculator();
        }
        return;
      }

      const script = document.createElement('script');
      script.src = 'https://www.desmos.com/api/v1.10/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6';
      script.async = true;
      script.id = 'desmos-script'; // Add an ID for easy identification
      
      script.onload = () => {
        if (window.Desmos) {
          createCalculator();
        } else {
          setGraphError(true);
        }
      };
      
      script.onerror = () => setGraphError(true);
      
      document.head.appendChild(script);
      desmosScriptRef.current = script;
    };

    const createCalculator = () => {
      try {
        if (calculatorRef.current) {
          calculatorRef.current.destroy();
        }

        const calculator = window.Desmos.GraphingCalculator(graphRef.current!, {
          keypad: false,
          expressions: false,
          settingsMenu: false,
          zoomButtons: false,
        });

        calculatorRef.current = calculator;

        // Set graph bounds based on data
        const xValues = points
          .map(p => parseFloat(p.x))
          .filter(x => !isNaN(x));
        
        const yValues = points
          .map(p => parseFloat(p.y))
          .filter(y => !isNaN(y));

        if (xValues.length > 0 && yValues.length > 0) {
          const padding = 2;
          const xMin = Math.min(...xValues) - padding;
          const xMax = Math.max(...xValues) + padding;
          const yMin = Math.min(...yValues) - padding;
          const yMax = Math.max(...yValues) + padding;
          
          calculator.setMathBounds({
            left: xMin,
            right: xMax,
            bottom: yMin,
            top: yMax
          });
        }

        // Add points
        calculator.setExpression({
          id: 'points',
          type: 'table',
          columns: [
            { values: xValues.map(String), latex: 'x' },
            { values: yValues.map(String), latex: 'y' }
          ],
          lines: false,
          points: true,
          pointStyle: 'OPEN',
          pointSize: 12,
          color: '#FF0000'
        });

        // Add function with styling
        const functionExpression = getFunctionExpression(result);
        if (functionExpression) {
          calculator.setExpression({
            id: 'function',
            latex: functionExpression,
            lineWidth: 3,
            color: '#3B82F6',
            lineStyle: 'SOLID'
          });
        }
      } catch (err) {
        setGraphError(true);
      }
    };

    loadDesmos();

    return () => {
      // Clean up calculator
      if (calculatorRef.current) {
        calculatorRef.current.destroy();
        calculatorRef.current = null;
      }
      
      // Clean up script tag
      if (desmosScriptRef.current) {
        document.head.removeChild(desmosScriptRef.current);
        desmosScriptRef.current = null;
      }
    };
  }, [result]);

  const getFunctionExpression = (result: ApproximationResult): string | null => {
    if (!result.success || !result.data) return null;
    
    const params = result.data.parameters;
    switch (result.type_) {
      case 'linear': return `${params.a} + ${params.b}x`;
      case 'quadratic': return `${params.a} + ${params.b}x + ${params.c}x^2`;
      case 'cubic': return `${params.a} + ${params.b}x + ${params.c}x^2 + ${params.d}x^3`;
      case 'exponential': return `${params.a}e^{${params.b}x}`;
      case 'logarithmic': return `(${params.b})\\ln(x) + (${params.a})`;
      case 'power': return `${params.a}x^{${params.b}}`;
      default: return null;
    }
  };

  return (
    <div className={styles['graph-card']}>
      <h3>{isBest && '👑'} {capitalize(result.type_)} function</h3>
      
      {!result.success ? (
        <div className={styles['graph-error']}>
          {result.message || `Failed to calculate ${result.type_} approximation`}
        </div>
      ) : !result.data ? (
        <div className={styles['graph-error']}>
          No data available for this approximation
        </div>
      ) : graphError ? (
        <div className={styles['graph-error']}>
          Failed to load graph visualization
        </div>
      ) : (
        <div 
          ref={graphRef} 
          className={styles['desmos-graph-container']}
        />
      )}
      
      {result.success && result.data && (
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
            <strong>Function:</strong> {' '}
            {getFunctionExpression(result) ? (
              <InlineMath math={'f(x) = ' + getFunctionExpression(result)} />
            ) : (
              'N/A'
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default GraphCard;