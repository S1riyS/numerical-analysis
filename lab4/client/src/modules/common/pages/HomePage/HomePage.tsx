import styles from './HomePage.module.css';
import { LabCard } from '@common/components';

const HomePage = () => {
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
          <LabCard
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

export default HomePage;