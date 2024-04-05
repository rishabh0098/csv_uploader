import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Routes, Route } from "react-router-dom";
import { UploadData } from "./components/UploadData";

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand navbar-dark bg-info">
          CSV Uploader Tool
      </nav>
      <div className="container m-10">
        <Routes>
          <Route path="/" element={<UploadData />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
