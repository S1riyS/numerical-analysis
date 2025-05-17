import { useRef, useState } from "react";

import { Card, Col, Container, Form, Row, Tab, Tabs } from "react-bootstrap";

import { PointsManager } from "@common/components";
import { EnumSelect } from "@common/components/EnumSelect";
import { Point } from "@common/types";
import { ApiService } from "@interpolation/api/api";
import {
  InterpolationResponse,
  PointInterpolationResponse,
} from "@interpolation/api/types";
import { FunctionInput, FunctionInputHandle } from "@interpolation/components";
import { ResultView } from "@interpolation/components/ResultView";
import { SubmitInterpolationButton } from "@interpolation/components/SubmitInterpolationButton";
import {
  InterpolationMethod,
  PointInterpolationMethod,
} from "@interpolation/types";
import {
  interpolationMethodToName,
  pointInterpolationMethodToName,
} from "@interpolation/utils/mappers";

enum PointInputTypeKey {
  TABLE = "table",
  FUNCTION = "function",
}

enum MethodTypeKey {
  INTERPOLATION = "interpolation",
  POINT = "point",
}

const ApproximationPage: React.FC = () => {
  const [tablePoints, setTablePoints] = useState<Point[]>([]);
  const [_, setFunctionPoints] = useState<Point[]>([]);

  const evaluatorRef = useRef<FunctionInputHandle>(null);

  const [pointsInputType, setPointsInputType] = useState<PointInputTypeKey>(
    PointInputTypeKey.TABLE,
  );
  const [methodType, setMethodType] = useState<MethodTypeKey>(
    MethodTypeKey.INTERPOLATION,
  );

  const [interpolationMethod, setInterpolationMethod] =
    useState<InterpolationMethod>(InterpolationMethod.LAGRANGE);

  const [pointInterpolationMethod, setPointInterpolationMethod] =
    useState<PointInterpolationMethod>(PointInterpolationMethod.STIRLING);
  const [pointX, setPointX] = useState<number>(0);

  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState<
    InterpolationResponse | PointInterpolationResponse
  >();
  const [error, setError] = useState<string>();

  const handleSubmit = async () => {
    setIsLoading(true);
    setError(undefined);

    try {
      let points: Point[];
      if (pointsInputType === PointInputTypeKey.TABLE) {
        points = tablePoints;
      } else {
        if (evaluatorRef.current) {
          points = evaluatorRef.current.handleEvaluate();
        } else {
          points = [];
        }
      }

      if (methodType === MethodTypeKey.INTERPOLATION) {
        const response = await ApiService.interpolate(
          points,
          interpolationMethod,
        );
        setResult(response);
      } else {
        const response = await ApiService.interpolatePoint(
          points,
          pointInterpolationMethod,
          pointX,
        );
        setResult(response);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown error occurred");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Container fluid className="px-4">
      <Row>
        <Col md={6} lg={4}>
          {/* Выбор вида ввода точек */}
          <Row className="mb-3">
            <Tabs
              defaultActiveKey={pointsInputType}
              onSelect={(k) => setPointsInputType(k as PointInputTypeKey)}
              className="mb-3"
            >
              {/* Points table input tab */}
              <Tab key={1} eventKey={PointInputTypeKey.TABLE} title="Таблица">
                <PointsManager
                  minPoints={2}
                  maxPoints={8}
                  onPointsChange={setTablePoints}
                ></PointsManager>
              </Tab>

              {/* Function input tab */}
              <Tab
                key={2}
                eventKey={PointInputTypeKey.FUNCTION}
                title="Функция"
              >
                <FunctionInput
                  ref={evaluatorRef}
                  onEvaluate={(calculatedPoints) => {
                    setFunctionPoints(calculatedPoints);
                  }}
                ></FunctionInput>
              </Tab>
            </Tabs>
          </Row>

          {/* Выбор вида интерполяции */}
          <Card className="mb-3">
            <Card.Header as="h5">Параметры</Card.Header>
            <Card.Body>
              <EnumSelect
                enumObj={InterpolationMethod}
                value={interpolationMethod}
                onChange={setInterpolationMethod}
                getLabel={interpolationMethodToName}
                label="Метод:"
              />
            </Card.Body>
          </Card>

          {/* Кнопка запуска */}
          <SubmitInterpolationButton
            isLoading={isLoading}
            onClick={handleSubmit}
          ></SubmitInterpolationButton>
        </Col>

        <Col md={6} lg={8}>
          <ResultView result={result} error={error} />
        </Col>
      </Row>
    </Container>
  );
};

export default ApproximationPage;
