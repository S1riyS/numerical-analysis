import { ApproximationResponse } from '@approximation/api/types';
import { resultToFunction, resultToLatex, typeToName } from '@approximation/utils/mappers';
import { FunctionPlot } from '@common/components';
import { Point } from '@common/types';
import { Card, Tab, Tabs, Alert } from 'react-bootstrap';
import { InlineMath } from 'react-katex';
import { useMemo } from 'react';

interface ResultsViewProps {
  results: ApproximationResponse;
  points: Point[]
}

export const ResultsView: React.FC<ResultsViewProps> = ({ results, points }) => {
  const minX = Math.min(...points.map(point => point.x));
  const maxX = Math.max(...points.map(point => point.x));
  const padding = (maxX - minX) * 0.1;

  return (
    <Card>
      <Card.Body>
        <Card.Title>Результаты анализа</Card.Title>

        <Tabs defaultActiveKey="linear" className="mb-3">
          {results.results.map((result, index) => {
            // Memoize the function based on the result
            const plotFunction = useMemo(
              () => resultToFunction(result),
              [JSON.stringify(result)] // Serialize the result for comparison
            );

            return (
              <Tab
                key={index}
                eventKey={result.type_}
                title={
                  <>
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
                    <h5>Параметры модели</h5>
                    <InlineMath math={`f(x) = ${resultToLatex(result)}`}></InlineMath>
                    <ul>
                      {result.data?.parameters && Object.entries(result.data.parameters).map(([key, value]) => (
                        <li key={key}>
                          <strong>{key}:</strong> {value.toFixed(4)}
                        </li>
                      ))}
                    </ul>

                    <h5 className="mt-3">Метрики качества</h5>
                    <ul>
                      <li><strong>MSE:</strong> {result.data?.mse?.toFixed(4)}</li>
                      <li><strong>Коэффициент детерминации:</strong> {result.data?.coefficient_of_determination?.toFixed(4)}</li>
                      <li><strong>Мера отклонения:</strong> {result.data?.measure_of_deviation?.toFixed(4)}</li>
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