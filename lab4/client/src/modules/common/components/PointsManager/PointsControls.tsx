import { Button, Form, Stack } from "react-bootstrap";
import { FaFileImport } from "react-icons/fa";

import { useRef } from "react";

import { Point } from "@common/types";

interface PointsControlsProps {
  onAddPoint: () => void;
  onFileUpload: (data: Point[]) => void;
  maxPoints: number;
  currentCount: number;
}

export const PointsControls: React.FC<PointsControlsProps> = ({
  onAddPoint,
  onFileUpload,
  maxPoints,
  currentCount,
}) => {
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        try {
          const data = JSON.parse(event.target?.result as string) as Point[];
          onFileUpload(data);

          // Сбрасываем значение input после загрузки
          if (fileInputRef.current) {
            fileInputRef.current.value = "";
          }
        } catch (error) {
          alert("Ошибка чтения файла");
        }
      };
      reader.readAsText(file);
    }
  };

  return (
    <Stack direction="horizontal" gap={2}>
      <Button
        variant="primary"
        onClick={onAddPoint}
        disabled={currentCount >= maxPoints}
      >
        Добавить точку
      </Button>

      <Form.Group controlId="formFile" className="ms-auto">
        <Form.Label className="mb-0 btn btn-outline-secondary">
          <FaFileImport style={{ marginRight: "6px" }} />
          Загрузить из файла
          <Form.Control
            type="file"
            accept=".json"
            onChange={handleFileUpload}
            hidden
            ref={fileInputRef}
          />
        </Form.Label>
      </Form.Group>
    </Stack>
  );
};
