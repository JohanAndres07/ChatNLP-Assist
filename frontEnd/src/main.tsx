import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "../src/index.css";
import App from "./App.tsx";

const rootElement = document.getElementById("root");
if (rootElement) {
	createRoot(rootElement).render(
		<StrictMode>
			<App />
		</StrictMode>,
	);
} else {
	console.error("Root element not found!");
}
