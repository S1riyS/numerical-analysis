import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './app/App';
import reportWebVitals from './app/reportWebVitals';

// Получаем корневой элемент
const container = document.getElementById('root') as HTMLElement;

// Создаем корень рендеринга
const root = createRoot(container!); // ! - утверждение, что элемент существует

// Рендерим приложение
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Измерение производительности
reportWebVitals();