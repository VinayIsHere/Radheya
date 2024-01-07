import { createBrowserRouter } from "react-router-dom";
import App from "@/App";
import Modal from "@/components/ui/modal";
import Root from "./root";
export const routes = createBrowserRouter([
  {
    element: <Root />,
    children: [
      {
        path: "/modal",
        element: <Modal />,
      },
      { path: "/*", element: <App /> },
    ],
  },
]);
