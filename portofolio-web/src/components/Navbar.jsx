import React, { useState, useEffect } from 'react';
import ThemeToggle from './ThemeToggle';

const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  const scrollToSection = (sectionId) => {
    const section = document.getElementById(sectionId);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
      setMenuOpen(false);
    }
  };

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 50) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header className={`navbar ${scrolled ? 'scrolled' : ''}`}>
      <div className="container navbar-container">
        <a href="#" className="logo" onClick={() => scrollToSection('hero')}>
          Home
        </a>

        <button 
          className={`mobile-menu-btn ${menuOpen ? 'open' : ''}`} 
          onClick={toggleMenu}
          aria-label="Toggle menu"
        >
          <span></span>
          <span></span>
          <span></span>
        </button>

        <nav className={`nav-links ${menuOpen ? 'open' : ''}`}>
          <ul>
            <li>
              <a href="#about" onClick={() => scrollToSection('about')}>About</a>
            </li>
            <li>
              <a href="#skills" onClick={() => scrollToSection('skills')}>Skills</a>
            </li>
            <li>
              <a href="#projects" onClick={() => scrollToSection('projects')}>Projects</a>
            </li>
            <li>
              <a href="#contact" onClick={() => scrollToSection('contact')}>Contact</a>
            </li>
          </ul>
          <ThemeToggle />
        </nav>
      </div>
    </header>
  );
};

export default Navbar;