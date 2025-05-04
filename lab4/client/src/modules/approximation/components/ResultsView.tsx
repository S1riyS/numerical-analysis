import { AnalysisResponse } from '@approximation/api/types';
import { Card, Tab, Tabs, Alert, Badge } from 'react-bootstrap';

interface ResultsViewProps {
  results: AnalysisResponse;
}

export const ResultsView: React.FC<ResultsViewProps> = ({ results }) => {
  return (
    <Card>
      <Card.Body>
        <Card.Title>Результаты анализа</Card.Title>
        
        <Tabs defaultActiveKey="linear" className="mb-3">
          {results.results.map((result, index) => (
            <Tab
              key={index}
              eventKey={result.type_}
              title={
                <>
                  {result.type_}
                  {result.success && (
                    <Badge bg="success" className="ms-2">✓</Badge>
                  )}
                </>
              }
            >
              {result.success ? (
                <div className="mt-3">
                  <h5>Параметры модели</h5>
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
          ))}
        </Tabs>
      </Card.Body>
    </Card>
  );
};