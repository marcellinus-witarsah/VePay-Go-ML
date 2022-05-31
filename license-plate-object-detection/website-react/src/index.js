import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

// const rootElement = ReactDOM.createRoot(document.getElementById("root"));
// rootElement.render(<CameraLive />);
// rootElement.render(<CameraLive />);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
