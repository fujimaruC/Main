import React from 'react';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-logo">
            <a href="#hero">Jericho Web Project</a>
          </div>
          
          <div className="footer-links">
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
          </div>
          
          <div className="footer-social">
            <a href="https://github.com/fujimaruC" target="_blank" rel="noopener noreferrer" aria-label="GitHub">GitHub</a>
            <a href="https://play.picoctf.org/users/loliHunters" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">PicoCTF</a>
            <a href="https://ctf.hackthebox.com/team/overview/220605" target="_blank" rel="noopener noreferrer" aria-label="Twitter">HackTheBox</a>
          </div>
        </div>
        
        <div className="footer-bottom">
          <p>&copy; {currentYear} Jericho. All rights reserved.</p>
          <p>Designed & Built with Love</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;