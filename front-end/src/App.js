import React, {useState, useEffect} from "react";
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Home from "./components/Home";
import NavBar from "./components/NavBar";
import SignUp from "./components/SignUp";
import './App.css';

function App() {
  return (
      <BrowserRouter>
      <NavBar></NavBar>
        <Routes>
          <Route path="/" Component={Home}></Route>
          <Route path="/signup" Component={SignUp}></Route>
        </Routes>
      </BrowserRouter>

  );
}

export default App;
