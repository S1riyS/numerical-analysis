import { useCallback, useMemo } from "react";

import { Alert, Button, Card, Col, Row, Tab, Tabs } from "react-bootstrap";
import { FaFileDownload } from "react-icons/fa";
import { InlineMath } from "react-katex";

import { ApproximationResponse } from "@approximation/api/types";
import { FunctionType } from "@approximation/types";
import {
  resultToFunction,
  resultToLatex,
  typeToName,
} from "@approximation/utils/mappers";
import { getBestApproximationType } from "@approximation/utils/response";
import { FunctionPlot } from "@common/components";
import { Point } from "@common/types";

interface ResultsViewProps {
  results: ApproximationResponse;
  points: Point[];
}

export const ResultsView: React.FC<ResultsViewProps> = ({
  results,
  points,
}) => {
  const parsedXs = points.map((point) => parseFloat(point.x));
  const minX = Math.min(...parsedXs);
  const maxX = Math.max(...parsedXs);
  const padding = (maxX - minX) * 0.1;

  const bestApproximationType = getBestApproximationType(results);

  const handleDownload = useCallback(() => {
    // Create copies of the data to ensure it doesn't change after API calls
    const dataToExport = {
      points: [...points], // Creates a new array with copied points
      results: results ? { ...results } : null, // Creates a new object if results exists
    };

    // Create JSON string
    const jsonString = JSON.stringify(dataToExport, null, 2);

    // Create blob and download
    const blob = new Blob([jsonString], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "approximation_data.json";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }, [results]);

  return (
    <Card>
      <Card.Body>
        <Card.Title>
          <Row className="justify-content-between">
            <Col xs="auto">Результаты анализа</Col>
            <Col xs="auto">
              <Button onClick={handleDownload} variant="outline-secondary">
                <FaFileDownload /> Сохранить
              </Button>
            </Col>
          </Row>
        </Card.Title>

        <Tabs defaultActiveKey={FunctionType.LINEAR} className="mb-3">
          {results.results.map((result, index) => {
            // Memoize the function based on the result
            const plotFunction = useMemo(
              () => resultToFunction(result),
              [JSON.stringify(result)], // Serialize the result for comparison
            );

            return (
              <Tab
                key={index}
                eventKey={result.type_}
                title={
                  <>
                    {bestApproximationType == result.type_ ? "👑 " : ""}
                    {typeToName(result.type_)}
                  </>
                }
              >
                {result.success ? (
                  <div className="mt-3">
                    <FunctionPlot
                      func={plotFunction}
                      minX={minX - padding}
                      maxX={maxX + padding}
                      points={points}
                    />
                    <h5>
                      Приближение:{" "}
                      <InlineMath
                        math={`f(x) = ${resultToLatex(result)}`}
                      ></InlineMath>
                    </h5>
                    <h5 className="mt-3">Параметры модели</h5>
                    <ul>
                      {result.data?.parameters &&
                        Object.entries(result.data.parameters).map(
                          ([key, value]) => (
                            <li key={key}>
                              <strong>{key}:</strong> {value.toFixed(4)}
                            </li>
                          ),
                        )}
                    </ul>

                    <h5 className="mt-3">Метрики качества</h5>
                    <ul>
                      <li>
                        <strong>MSE:</strong> {result.data?.mse?.toFixed(4)}
                      </li>
                      <li>
                        <strong>Коэффициент детерминации:</strong>{" "}
                        {result.data?.coefficient_of_determination?.toFixed(4)}
                      </li>
                      <li>
                        <strong>Мера отклонения:</strong>{" "}
                        {result.data?.measure_of_deviation?.toFixed(4)}
                      </li>
                    </ul>
                  </div>
                ) : (
                  <Alert variant="danger" className="mt-3">
                    {result.message}
                  </Alert>
                )}
              </Tab>
            );
          })}
        </Tabs>
      </Card.Body>
    </Card>
  );
};
