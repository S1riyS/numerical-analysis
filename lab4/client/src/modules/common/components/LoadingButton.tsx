import { Button, ButtonProps, Spinner } from "react-bootstrap";

import React from "react";

interface LoadingButtonProps extends ButtonProps {
  isLoading: boolean;
  icon?: React.ReactNode;
}

const LoadingButton: React.FC<LoadingButtonProps> = ({
  isLoading,
  icon,
  ...props
}) => {
  return (
    <Button disabled={isLoading} {...props}>
      <>
        {!!icon && !isLoading && icon}
        {isLoading && <Spinner animation="border" size="sm" />} {props.children}
      </>
    </Button>
  );
};

export default LoadingButton;
