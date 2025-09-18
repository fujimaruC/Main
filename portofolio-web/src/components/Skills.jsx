import React, { useEffect, useRef } from 'react';
import { ScrollAnimation } from './ScrollAnimation';

const Skills = () => {
  const skillsData = [
    { name: "HTML5/CSS3", percentage: 90 },
    { name: "JavaScript", percentage: 75 },
    { name: "Bug Bounty", percentage: 90 },
    { name: "Python", percentage: 75 },
    { name: "UI/UX Design", percentage: 80 },
    { name: "App development", percentage: 70 }
  ];

  const skillBarsRef = useRef([]);
  
  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const index = skillBarsRef.current.indexOf(entry.target);
            if (index !== -1) {
              const skillBar = entry.target.querySelector('.skill-percentage');
              skillBar.style.width = `${skillsData[index].percentage}%`;
              skillBar.classList.add('animate');
            }
          }
        });
      },
      { threshold: 0.2 }
    );

    skillBarsRef.current.forEach(ref => {
      if (ref) observer.observe(ref);
    });

    return () => {
      skillBarsRef.current.forEach(ref => {
        if (ref) observer.unobserve(ref);
      });
    };
  }, [skillsData]);

  return (
    <section id="skills" className="skills">
      <div className="container">
        <ScrollAnimation>
          <h2 className="section-title">My Skills</h2>
        </ScrollAnimation>

        <div className="skills-content">
          <ScrollAnimation animation="fade-in">
            <p className="skills-intro">
              I'm proficient in a range of frontend and backend technologies,
              continuously expanding my skillset to deliver the best solutions.
            </p>
          </ScrollAnimation>

          <div className="skills-grid">
            <div className="technical-skills">
              <ScrollAnimation animation="fade-in">
                <h3>Technical Skills</h3>
              </ScrollAnimation>

              {skillsData.map((skill, index) => (
                <div 
                  key={index} 
                  className="skill-item"
                  ref={el => skillBarsRef.current[index] = el}
                >
                  <div className="skill-info">
                    <span className="skill-name">{skill.name}</span>
                    <span className="skill-percentage-text">{skill.percentage}%</span>
                  </div>
                  <div className="skill-bar">
                    <div 
                      className="skill-percentage"
                      style={{ width: '0%' }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>

            <div className="soft-skills">
              <ScrollAnimation animation="slide-in-right">
                <div className="card">
                  <h3>Soft Skills</h3>
                  <ul className="soft-skills-list">
                    <li>Problem Solving</li>
                    <li>Creativity & Innovation</li>
                    <li>Communication</li>
                    <li>Time Management</li>
                    <li>Adaptability</li>
                    <li>Attention to Detail</li>
                  </ul>
                </div>
              </ScrollAnimation>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Skills;