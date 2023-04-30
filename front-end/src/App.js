import React, {useState, useEffect} from "react";
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Home from "./components/Home";
import NavBar from "./components/NavBar";
import SignUp from "./components/SignUp";
import SignIn from "./components/SignIn";
import './App.css';
import UserProfile from "./components/UserProfile";
import Footer from "./components/Footer";
import AddProject from "./components/AddProject";
import ProjectPage from "./components/ProjectPage";

function App() {
  const [SignedID, setSignedID] = useState('')
  const handleSignIn = (userID) =>{
    setSignedID(userID)
  }
  return (
      <BrowserRouter>
      <NavBar SignedID={SignedID}></NavBar>
        <Routes>
          <Route path="/" Component={Home}></Route>
          <Route path="/signup" Component={SignUp}></Route>
          <Route path="/signin" element={<SignIn setID = {handleSignIn}></SignIn>} ></Route>
          <Route path='/profile' element={<UserProfile SignedID={SignedID}></UserProfile>}></Route>
          <Route path="/addproj" element={<AddProject SignedID={SignedID}></AddProject>}></Route>
          <Route path='/project/:id/' Component={ProjectPage}></Route>
        </Routes>
      </BrowserRouter>

  );
}

export default App;
