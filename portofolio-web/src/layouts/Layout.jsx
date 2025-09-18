import React from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { ThemeProvider } from '../context/ThemeContext';

const Layout = ({ children }) => {
  return (
    <ThemeProvider>
      <div className="app">
        <Navbar />
        <main>{children}</main>
        <Footer />
      </div>
    </ThemeProvider>
  );
};

export default Layout;