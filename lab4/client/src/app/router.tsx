import { lazy } from 'react';
import { Routes, Route } from 'react-router-dom';
import { HomePage } from 'pages/HomePage';

const ApproximationPage = lazy(() => import('pages/ApproximationPage'));

export const AppRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/approximation" element={<ApproximationPage />} />
    </Routes>
  );
};