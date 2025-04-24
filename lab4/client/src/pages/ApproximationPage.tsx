// src/App.tsx
import React, { useState } from 'react';
import PointInput from 'components/PointInput';
import Controls from 'components/Controls';
import Results from 'components/Results';
import { Point, ApiRequest, ApiResponse } from 'api/types';
import './ApproximationPage.module.css';

const ApproximationPage: React.FC = () => {
  const [points, setPoints] = useState<Point[]>([
    { x: '', y: '' }, { x: '', y: '' }, { x: '', y: '' }, { x: '', y: '' },
    { x: '', y: '' }, { x: '', y: '' }, { x: '', y: '' }, { x: '', y: '' }
  ]);
  const [results, setResults] = useState<ApiResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handlePointChange = (index: number, field: 'x' | 'y', value: string) => {
    const newPoints = [...points];
    newPoints[index] = { ...newPoints[index], [field]: value };
    setPoints(newPoints);
  };

  const addPoint = () => {
    if (points.length < 12) {
      setPoints([...points, { x: '', y: '' }]);
    }
  };

  const removePoint = (index: number) => {
    if (points.length > 8) {
      const newPoints = [...points];
      newPoints.splice(index, 1);
      setPoints(newPoints);
    }
  };

  const clearAll = () => {
    setPoints(points.map(() => ({ x: '', y: '' })));
    setResults(null);
    setError(null);
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        const content = event.target?.result as string;
        const lines = content.split('\n').filter(line => line.trim() !== '');
        
        if (lines.length < 2) {
          throw new Error('File must contain at least 2 lines (X and Y coordinates)');
        }

        const xs = lines[0].trim().split(/\s+/).map(Number);
        const ys = lines[1].trim().split(/\s+/).map(Number);

        if (xs.length !== ys.length) {
          throw new Error('X and Y coordinates must have the same number of values');
        }

        if (xs.length < 8 || xs.length > 12) {
          throw new Error('Number of points must be between 8 and 12');
        }

        if (xs.some(isNaN) || ys.some(isNaN)) {
          throw new Error('All values must be numbers');
        }

        const newPoints = xs.map((x, i) => ({
          x: x.toString(),
          y: ys[i].toString()
        }));

        setPoints(newPoints);
        setError(null);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Invalid file format');
      }
    };
    reader.readAsText(file);
  };

  const submitData = async () => {
    const xs: number[] = [];
    const ys: number[] = [];

    for (const point of points) {
      const x = parseFloat(point.x);
      const y = parseFloat(point.y);
      
      if (isNaN(x) || isNaN(y)) {
        setError('All points must have valid X and Y coordinates');
        return;
      }
      
      xs.push(x);
      ys.push(y);
    }

    if (xs.length < 8 || xs.length > 12) {
      setError('Number of points must be between 8 and 12');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch('http://localhost:8000/api/approximation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ xs, ys } as ApiRequest),
      });

      if (!response.ok) {
        throw new Error(`API request failed with status ${response.status}`);
      }

      const data: ApiResponse = await response.json();
      setResults(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch approximation results');
    } finally {
      setLoading(false);
    }
  };

  const saveToFile = () => {
    if (!results) return;

    const dataToSave = {
      input: points.map(p => ({ x: parseFloat(p.x), y: parseFloat(p.y) })),
      results: results.results
    };

    const blob = new Blob([JSON.stringify(dataToSave, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'approximation_results.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="app">
      <h1>Function Approximation Tool</h1>
      
      <div className="input-section">
        <h2>Input Points (8-12 points)</h2>
        <div className="points-grid">
          {points.map((point, index) => (
            <PointInput
              key={index}
              point={point}
              index={index}
              onChange={handlePointChange}
              onRemove={removePoint}
              showRemove={points.length > 8}
            />
          ))}
        </div>
        
        <Controls
          onAddPoint={addPoint}
          onClearAll={clearAll}
          onFileUpload={handleFileUpload}
          onSubmit={submitData}
          onSave={saveToFile}
          pointsCount={points.length}
          hasResults={!!results}
          loading={loading}
        />
        
        {error && <div className="error">{error}</div>}
      </div>

      <Results results={results} points={points} />
    </div>
  );
};

export default ApproximationPage;