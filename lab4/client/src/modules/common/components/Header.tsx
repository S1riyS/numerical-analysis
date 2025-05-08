import React from "react";

import { Container, Nav, Navbar } from "react-bootstrap";
import { FaGithub } from "react-icons/fa";
import { TbMathFunction } from "react-icons/tb";

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
          <Nav>
            <Navbar.Text>
              {author} {group}
            </Navbar.Text>
            <Nav></Nav>
            <Nav.Link
              href="https://github.com/S1riyS/numerical-analysis/tree/main/lab4"
              target="_blank"
              rel="noopener noreferrer"
            >
              <FaGithub size={24} />
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};
