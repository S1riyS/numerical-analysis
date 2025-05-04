import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';


// Render application
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
);
