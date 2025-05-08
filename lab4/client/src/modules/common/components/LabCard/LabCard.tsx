import React from "react";

import { Card } from "react-bootstrap";
import { FaFlask } from "react-icons/fa";
import { Link } from "react-router-dom";

import styles from "./LabCard.module.css";

interface LabCardProps {
  title: string;
  labNumber: number;
  description: string;
  to: string;
}

export const LabCard: React.FC<LabCardProps> = ({
  title,
  description,
  labNumber,
  to,
}) => {
  return (
    <Link to={to} className={styles.link}>
      <Card className={styles.card}>
        <Card.Header>
          <FaFlask /> Лабораторная работа №{labNumber}
        </Card.Header>
        <Card.Body>
          <Card.Title>{title}</Card.Title>
          <Card.Text>{description}</Card.Text>
        </Card.Body>
      </Card>
    </Link>
  );
};
