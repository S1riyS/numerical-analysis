import React from 'react';
import { Container, Navbar } from 'react-bootstrap';

interface HeaderProps {
  author?: string;
  group?: string;
}

export const Header: React.FC<HeaderProps> = ({ author, group }) => {
  return (
    <Navbar className="bg-body-tertiary mb-3">
      <Container>
        <Navbar.Brand href="/">Вычислительная математика</Navbar.Brand>
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