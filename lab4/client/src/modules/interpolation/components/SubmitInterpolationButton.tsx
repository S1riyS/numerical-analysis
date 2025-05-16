// components/SubmitButton.tsx
import React from "react";

import { Button, Spinner } from "react-bootstrap";

interface SubmitInterpolationButtonProps {
  isLoading: boolean;
  onClick: () => void;
  disabled?: boolean;
}

export const SubmitInterpolationButton: React.FC<SubmitInterpolationButtonProps> = ({
  isLoading,
  onClick,
  disabled = false,
}) => {
  return (
    <Button
      variant="primary"
      onClick={onClick}
      disabled={isLoading || disabled}
      className="w-100 py-2"
    >
      {isLoading ? (
        <>
          <Spinner
            as="span"
            animation="border"
            size="sm"
            role="status"
            aria-hidden="true"
          />
          <span className="ms-2">Вычисляем...</span>
        </>
      ) : (
        "Вычислить"
      )}
    </Button>
  );
};
