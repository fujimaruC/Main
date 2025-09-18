import React from 'react';
import { ScrollAnimation } from './ScrollAnimation';

const About = () => {
  return (
    <section id="about" className="about">
      <div className="container">
        <ScrollAnimation>
          <h2 className="section-title">About Me</h2>
        </ScrollAnimation>

        <div className="about-content">
          <ScrollAnimation animation="slide-in-left">
            <div className="about-image">
              <img src="assets/images/profile.jpg" alt="About Me" />
            </div>
          </ScrollAnimation>

          <div className="about-text">
            <ScrollAnimation animation="fade-in">
              <h3>Who am I?</h3>
              <p>
                I'm an IT enthusiast who's interested in many technologies and always 
                curious about how a system works. Things I've studied so far include web development, 
                cybersecurity, app development (entry level), and I also spend my free time playing video games. 
                I bring focus and logic to everything I do, with attention to detail.
              </p>
            </ScrollAnimation>

            <ScrollAnimation animation="fade-in" delay={0.2}>
              <h3>My Journey</h3>
              <p>
                My journey on IT encthutiac began years ago. Since then, I've 
                worked on numerous projects, studying more abouut Cybersecurity, and lots self projects.
                Continuously learning and adapting to new technologies and best practices.
              </p>
            </ScrollAnimation>

            <ScrollAnimation animation="fade-in" delay={0.4}>
              <div className="about-details">
                <div className="detail-item">
                  <span className="detail-title">Name:</span>
                  <span className="detail-info">Jericho Mikael</span>
                </div>
                <div className="detail-item">
                  <span className="detail-title">Email:</span>
                  <span className="detail-info">jericholimbong@gmail.com</span>
                </div>
                <div className="detail-item">
                  <span className="detail-title">Location:</span>
                  <span className="detail-info">Indonesia, Balikpapan</span>
                </div>
                <div className="detail-item">
                  <span className="detail-title">Availability:</span>
                  <span className="detail-info">Cybersecurity Trainee</span>
                </div>
              </div>
            </ScrollAnimation>

            <ScrollAnimation animation="fade-in" delay={0.6}>
              <a href="#contact" className="btn">Get In Touch</a>
            </ScrollAnimation>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;