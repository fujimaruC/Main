    import React, { useEffect, useRef } from 'react';
import { ScrollAnimation } from './ScrollAnimation';

const Hero = () => {
  const profileRef = useRef(null);
  
  useEffect(() => {
    const handleScroll = () => {
      const scrollY = window.scrollY;
      const profileElement = profileRef.current;
      
      if (profileElement) {
        profileElement.style.transform = `translateY(${scrollY * 0.2}px) rotate(${scrollY * 0.02}deg)`;
        profileElement.style.opacity = 1 - (scrollY * 0.001);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <section id="hero" className="hero">
      <div className="container hero-container">
        <div className="hero-content">
          <ScrollAnimation animation="fade-in">
            <h1>Hello, I'm <span className="highlight">Jericho A.K.A Riko</span></h1>
          </ScrollAnimation> 
          
          <ScrollAnimation animation="slide-in-left" delay={0.2}>
            <h2>Web Developer & Cybersecurity trainee</h2>
          </ScrollAnimation>
          
          <ScrollAnimation animation="fade-in" delay={0.4}>
            <p>
              “There are lots of ways to open a file, not just one.”
            </p>
          </ScrollAnimation>
          
          <ScrollAnimation animation="fade-in" delay={0.6}>
            <div className="hero-buttons">
              <a href="#projects" className="btn">View My Work</a>
              <a href="#contact" className="btn btn-outline">Contact Me</a>
            </div>
          </ScrollAnimation>
        </div>
        
        <div className="hero-image">
          <ScrollAnimation animation="slide-in-right">
            <div className="profile-container">
              <img 
                ref={profileRef}
                src="assets/images/profile.jpg" 
                alt="Profile" 
                className="profile-image"
              />
              <div className="profile-shape"></div>
            </div>
          </ScrollAnimation>
        </div>
      </div>
    </section>
  );
};

export default Hero;