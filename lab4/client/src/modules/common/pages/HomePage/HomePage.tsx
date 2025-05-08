import { Col, Container, Row } from "react-bootstrap";

import { LabCard } from "@common/components";

const HomePage = () => {
  const labWorks = [
    {
      title: "Аппроксимация функций",
      labNumber: 4,
      description:
        "Нахождение функций, которые максимально приближают целевую функцию, заданную набором точек",
      path: "/approximation",
    },
  ];

  return (
    <Container>
      <h2 className="mb-3">Лабораторные работы</h2>
      <Row>
        {labWorks.map((work) => (
          <Col md={6} lg={4}>
            <LabCard
              key={work.path}
              title={work.title}
              labNumber={work.labNumber}
              description={work.description}
              to={work.path}
            />
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default HomePage;
