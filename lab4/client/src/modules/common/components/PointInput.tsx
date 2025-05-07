import { Point } from '@common/types';
import { Form, Row, Col, Button } from 'react-bootstrap';

interface PointInputProps {
  point: Point;
  onXChange: (value: string) => void;
  onYChange: (value: string) => void;
  onRemove: () => void;
  canRemove: boolean;
}

export const PointInput: React.FC<PointInputProps> = ({
  point,
  onXChange,
  onYChange,
  onRemove,
  canRemove
}) => {
  return (
    <Row className="mb-1 align-items-center g-1">
      <Col md={4}>
        <Form.Control
          type="number"
          step={0.1}
          value={point.x}
          onChange={(e) => onXChange(e.target.value)}
          placeholder="X"
        />
      </Col>
      <Col md={4}>
        <Form.Control
          type="number"
          step={0.1}
          value={point.y}
          onChange={(e) => onYChange(e.target.value)}
          placeholder="Y"
        />
      </Col>
      <Col md={4}>
        <Button
          variant="outline-danger"
          onClick={onRemove}
          disabled={!canRemove}
          className="w-100"
        >
          Удалить
        </Button>
      </Col>
    </Row>
  );
};