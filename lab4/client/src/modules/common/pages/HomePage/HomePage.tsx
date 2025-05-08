import { Col, Container, Row } from "react-bootstrap";

import { LabCard } from "@common/components";

const HomePage = () => {
  const labWorks = [
    {
      title: "Аппроксимация",
      labNumber: 4,
      description:
        "Нахождение функций, которые максимально приближают исходную функцию, заданную набором точек",
      path: "/approximation",
    },
    {
      title: "Интерполяция",
      labNumber: 5,
      description:
        "Нахождение значений функции, заданной набором точек, в тех точках, где она не задана явно.",
      path: "/interpolation",
    },
  ];

  return (
    <Container>
      <h2 className="mb-3">Лабораторные работы</h2>
      <Row>
        {labWorks.map((work, index) => (
          <Col md={6} lg={4} key={index} className="mb-3">
            <LabCard
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
