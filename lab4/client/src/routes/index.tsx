import React from "react";

import ApproximationPage from "@approximation/pages/ApproximationPage";
import HomePage from "@common/pages/HomePage";

export type Route = {
  element: React.ReactNode;
  path: string;
};

const routes: Route[] = [
  { element: <HomePage />, path: "/" },
  { element: <ApproximationPage />, path: "/approximation" },
];

export default routes;
