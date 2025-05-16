import React from "react";

import { Breadcrumb, Container, Nav, Navbar } from "react-bootstrap";
import { FaGithub } from "react-icons/fa";
import { TbMathFunction } from "react-icons/tb";
import { Link, useLocation } from "react-router-dom";

import routes from "/src/routes";

interface HeaderProps {
  author?: string;
  group?: string;
}

export const Header: React.FC<HeaderProps> = ({ author, group }) => {
  const location = useLocation();
  const pathnames = location.pathname.split("/").filter((x) => x);
  const showBreadcrumbs = location.pathname !== "/";

  return (
    <Navbar className="bg-body-tertiary mb-3">
      <Container fluid className="px-4">
        <Link to={"/"}>
          <Navbar.Brand>
            <TbMathFunction /> Вычислительная математика
          </Navbar.Brand>
        </Link>

        {showBreadcrumbs && (
          <Breadcrumb bsPrefix="breadcrumb mb-0">
            <Breadcrumb.Item linkAs={Link} linkProps={{ to: "/" }}>
              Главная
            </Breadcrumb.Item>
            {pathnames.map((_, index) => {
              const last = index === pathnames.length - 1;
              const to = `/${pathnames.slice(0, index + 1).join("/")}`;
              const name = routes.filter((route) => route.path === to)[0]
                .breadcrumb;

              return last ? (
                <Breadcrumb.Item active key={to}>
                  {name}
                </Breadcrumb.Item>
              ) : (
                <Breadcrumb.Item linkAs={Link} linkProps={{ to }} key={to}>
                  {name}
                </Breadcrumb.Item>
              );
            })}
          </Breadcrumb>
        )}

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
