import "katex/dist/katex.min.css";

import { useState } from "react";

import { Alert, Col, Container, Row } from "react-bootstrap";
import { PiMathOperations } from "react-icons/pi";

import { ApproximationResponse } from "@approximation/api/types";
import {
  ResultsView,
  SubmitApproximationButton,
} from "@approximation/components";
import { PointsManager } from "@common/components";
import { Point } from "@common/types";

const ApproximationPage: React.FC = () => {
  const [points, setPoints] = useState<Point[]>([]);
  const [results, setResults] = useState<ApproximationResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleAnalysisComplete = (results: ApproximationResponse) => {
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
          ></PointsManager>
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
            <ResultsView results={results} points={points} />
          ) : (
            <Container
              className="d-flex justify-content-center align-items-center flex-column"
              style={{ height: "100%" }}
            >
              <Row>
                <PiMathOperations size={128} />
              </Row>
              <Row>
                <i className="mt-3">Пока что здесь ничего нет...</i>
              </Row>
            </Container>
          )}
        </Col>
      </Row>
    </Container>
  );
};

export default ApproximationPage;
