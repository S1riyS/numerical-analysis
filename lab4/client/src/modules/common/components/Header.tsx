import { Container, Navbar } from "react-bootstrap";
import { TbMathFunction } from "react-icons/tb";

import React from "react";

interface HeaderProps {
  author?: string;
  group?: string;
}

export const Header: React.FC<HeaderProps> = ({ author, group }) => {
  return (
    <Navbar className="bg-body-tertiary mb-3">
      <Container fluid className="px-4">
        <Navbar.Brand href="/">
          <TbMathFunction /> Вычислительная математика
        </Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end">
          <Navbar.Text>
            {author} {group}
          </Navbar.Text>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};
