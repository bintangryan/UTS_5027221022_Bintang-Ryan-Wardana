import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard'; // Mengimpor komponen Dashboard
import History from './components/History'; // Mengimpor komponen History
import NavbarComponent from './components/NavbarComponent';

function App() {
  return (
    <Router>
      <NavbarComponent />
      <Routes>
        <Route path="/" element={<Dashboard />} /> {/* Menggunakan komponen Dashboard */}
        <Route path="/history" element={<History />} /> {/* Menggunakan komponen History */}
      </Routes>
    </Router>
  );
}

export default App;
