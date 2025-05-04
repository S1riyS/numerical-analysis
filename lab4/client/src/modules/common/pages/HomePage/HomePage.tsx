import { PointsManager } from '@common/components/PointsManager';
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
    <div className="random">
      <h2>Лабораторные работы</h2>
      <div className="random">
        {labWorks.map((work) => (
          <LabCard
            key={work.path}
            title={work.title}
            description={work.description}
            to={work.path}
          />
        ))}
      </div>
      <PointsManager minPoints={8} maxPoints={12}></PointsManager>
    </div>
  );
};

export default HomePage;