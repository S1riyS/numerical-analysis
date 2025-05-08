import React from "react";

import { Link } from "react-router-dom";

import styles from "./LabCard.module.css";

// Assuming you have a corresponding CSS module

interface LabCardProps {
  title: string;
  description: string;
  to: string;
}

export const LabCard: React.FC<LabCardProps> = ({ title, description, to }) => {
  return (
    <Link to={to} className={styles.card}>
      <h3 className={styles.title}>{title}</h3>
      <p className={styles.description}>{description}</p>
    </Link>
  );
};
