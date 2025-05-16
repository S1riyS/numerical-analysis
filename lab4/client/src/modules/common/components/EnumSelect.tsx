import React from "react";

import { Form } from "react-bootstrap";

interface EnumSelectProps<T extends string> {
  enumObj: Record<string, T>;
  value: T;
  onChange: (value: T) => void;
  getLabel: (value: T) => string;
  label?: string;
  disabled?: boolean;
  className?: string;
}

export function EnumSelect<T extends string>({
  enumObj,
  value,
  onChange,
  getLabel,
  label,
  disabled = false,
  className = "",
}: EnumSelectProps<T>) {
  // Get enum values (handles both traditional and const string enums)
  const enumValues = Object.values(enumObj) as T[];

  const handleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    onChange(e.target.value as T);
  };

  return (
    <Form.Group className={className}>
      {label && <Form.Label>{label}</Form.Label>}
      <Form.Select value={value} onChange={handleChange} disabled={disabled}>
        {enumValues.map((enumValue) => (
          <option key={enumValue} value={enumValue}>
            {getLabel(enumValue)}
          </option>
        ))}
      </Form.Select>
    </Form.Group>
  );
}
