import React from "react";
import HomePage from "@common/pages/HomePage";
import ApproximationPage from "@approximation/pages/ApproximationPage";

export type Route = {
  element: React.ReactNode;
  path: string;
};

const routes: Route[] = [
  { element: <HomePage />, path: "/" },
  { element: <ApproximationPage />, path: "/approximation" },
];

export default routes;