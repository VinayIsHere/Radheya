import React from "react";
import { Outlet } from "react-router-dom";
import { ToastContainer } from "react-toastify";

const Root = () => {
  return (
    <>
      <Outlet />
      <ToastContainer />
    </>
  );
};

export default Root;
