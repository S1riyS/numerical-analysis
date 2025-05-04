import { AnalysisResponse } from "@approximation/api/types";
import { ResultsView, SubmitApproximationButton } from "@approximation/components";
import { PointsManager } from "@common/components/PointsManager";
import { Point } from "@common/types";
import { useState } from "react";
import { Alert, Col, Container, Row } from "react-bootstrap";

const ApproximationPage: React.FC = () => {
  const [points, setPoints] = useState<Point[]>([]);
  const [results, setResults] = useState<AnalysisResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleAnalysisComplete = (results: AnalysisResponse) => {
    setResults(results);
    setError(null); // Clear any previous errors on success
  };

  const handleAnalysisError = (error: string) => {
    setError(error);
    setResults(null); // Clear results if there's an error
  };

  return (
    <Container fluid className="px-4">
      <Row>
        <Col md={6} lg={4}>
          <PointsManager 
            minPoints={8} 
            maxPoints={12} 
            onPointsChange={setPoints}
          >
          </PointsManager>
          <hr />
          <SubmitApproximationButton 
            points={points}
            onResults={handleAnalysisComplete}
            onError={handleAnalysisError}
          />
        </Col>
        <Col md={6} lg={8}>
          {error && <Alert variant="danger">{error}</Alert>}
          {results ? (
            <ResultsView results={results} />
          ) : (
            <div className="placeholder-results">
              <h4>Результаты анализа</h4>
              <p>Данные появятся здесь после выполнения анализа</p>
            </div>
          )}
        </Col>
      </Row>
    </Container>
  );
};

export default ApproximationPage;