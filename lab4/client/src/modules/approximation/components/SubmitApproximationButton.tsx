import { useState } from "react";

import { Button, Spinner } from "react-bootstrap";

import { ApiService } from "@approximation/api/api";
import { ApproximationResponse } from "@approximation/api/types";
import { Point } from "@common/types";

interface SubmitApproximationButtonProps {
  points: Point[];
  onResults: (results: ApproximationResponse) => void;
  onError?: (error: string) => void;
}

export const SubmitApproximationButton: React.FC<
  SubmitApproximationButtonProps
> = ({ points, onResults, onError }) => {
  const [isLoading, setIsLoading] = useState(false);

  const handleAnalyze = async () => {
    try {
      setIsLoading(true);
      const results = await ApiService.analyzePoints(points);
      onResults(results);
    } catch (err) {
      onError?.(err instanceof Error ? err.message : "Неизвестная ошибка");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="analysis-controller mt-3">
      <Button variant="success" onClick={handleAnalyze} disabled={isLoading}>
        {isLoading ? (
          <>
            <Spinner animation="border" size="sm" className="me-2" />
            Анализ...
          </>
        ) : (
          "Начать"
        )}
      </Button>
    </div>
  );
};
