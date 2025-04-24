import React from 'react';
import { Card } from 'components/Card';
import styles from './HomePage.module.css';

export const HomePage: React.FC = () => {
  const labWorks = [
    {
      title: 'Аппроксимация функций',
      description: 'Лабораторная работа №4',
      path: '/approximation'
    }
  ];

  return (
    <div className={styles.container}>
      <h2>Лабораторные работы</h2>
      <div className={styles.grid}>
        {labWorks.map((work) => (
          <Card
            key={work.path}
            title={work.title}
            description={work.description}
            to={work.path}
          />
        ))}
      </div>
    </div>
  );
};