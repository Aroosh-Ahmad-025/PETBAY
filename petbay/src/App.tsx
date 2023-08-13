// App.tsx
import React from 'react';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { AuthState, loginUser, logoutUser } from './redux/authReducer'; // Import the actions
import Login from './components/Auth/Login';
import Home from '././components/Home';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const isAuthenticated = useSelector((state : any) => state.auth.isAuthenticated);

 // const isAuthenticated = true;
  return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />} />
          {isAuthenticated ? (
            <Route path="/home" element={<Home />} />
          ) : (
            <Route path="/" element={<Login />} />
          )}
        </Routes>
      </BrowserRouter>
  );
}

export default App;
