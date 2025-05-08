import { Container } from "react-bootstrap";

import { LabCard } from "@common/components";

const HomePage = () => {
  const labWorks = [
    {
      title: "Аппроксимация функций",
      description: "Лабораторная работа №4",
      path: "/approximation",
    },
  ];

  return (
    <Container>
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
    </Container>
  );
};

export default HomePage;
