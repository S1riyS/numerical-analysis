import { Point } from '@common/types';
import { Form, Row, Col, Button } from 'react-bootstrap';
import { FaRegTrashCan } from 'react-icons/fa6';
import { MdDeleteForever } from 'react-icons/md';

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
      <Col md={5}>
        <Form.Control
          type="number"
          step={0.1}
          value={point.x}
          onChange={(e) => onXChange(e.target.value)}
          placeholder="X"
        />
      </Col>
      <Col md={5}>
        <Form.Control
          type="number"
          step={0.1}
          value={point.y}
          onChange={(e) => onYChange(e.target.value)}
          placeholder="Y"
        />
      </Col>
      <Col md={2}>
        <Button
          variant="outline-danger"
          onClick={onRemove}
          disabled={!canRemove}
          className="w-100"
        >
          <FaRegTrashCan />
        </Button>
      </Col>
    </Row>
  );
};