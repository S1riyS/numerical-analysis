import { createRoot } from "react-dom/client";

import { StrictMode } from "react";

import App from "./App";

// Render application
createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
