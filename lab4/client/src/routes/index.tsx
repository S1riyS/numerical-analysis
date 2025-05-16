import React from "react";

import ApproximationPage from "@approximation/pages/ApproximationPage";
import HomePage from "@common/pages/HomePage";
import InterpolationPage from "@interpolation/pages/InterpolationPage";

export type Route = {
  element: React.ReactNode;
  path: string;
  breadcrumb: string;
};

const routes: Route[] = [
  { element: <HomePage />, path: "/", breadcrumb: "Главная" },
  {
    element: <ApproximationPage />,
    path: "/approximation",
    breadcrumb: "Аппроксимация",
  },
  {
    element: <InterpolationPage />,
    path: "/interpolation",
    breadcrumb: "Интерполяция",
  },
];

export default routes;
