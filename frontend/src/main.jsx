import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import { routes } from './routes/index.jsx'
import 'react-toastify/dist/ReactToastify.css';
  
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={routes}>
    </RouterProvider>
  </React.StrictMode>,
)
