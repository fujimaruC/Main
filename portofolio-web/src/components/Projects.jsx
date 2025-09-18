import React from 'react';
import { ScrollAnimation } from './ScrollAnimation';

const Projects = () => {
  const projects = [
    {
      id: 2,
      title: "Task Management (Via Terminal)",
      description: "A submit and choice task management with local storage.",
      image: "assets/images/project1.png",
      technologies: ["Javascript", "Local Storage", "User-friendly", "Terminal"],
      demoLink: "#",
      codeLink: "#"
    },
    {
      id: 3,
      title: "Portfolio Website",
      description: "A modern portfolio website with smooth animations and dark/light theme.",
      image: "assets/images/project3.png",
      technologies: ["React", "GSAP", "Styled Components", "Newbie"],
      demoLink: "#",
      codeLink: "#"
    },
    {
      id: 6,
      title: "Data-list App (excel export, Terminal)",
      description: "A fully user-friendly terminal Data-store platform with Excel export data functionality and simple choice.",
      image: "assets/images/project2.png",
      technologies: ["Javascript", "Excel", "Terminal", "Local Storage"],
      demoLink: "#",
      codeLink: "#"
    }
  ];

  return (
    <section id="projects" className="projects">
      <div className="container">
        <ScrollAnimation>
          <h2 className="section-title">Featured Projects</h2>
        </ScrollAnimation>

        <ScrollAnimation animation="fade-in">
          <p className="projects-intro">
            Here are some of my recent projects. Each one has been carefully crafted to 
            deliver a great user experience while solving real-world problems.
          </p>
        </ScrollAnimation>

        <div className="projects-grid">
          {projects.map((project, index) => (
            <ScrollAnimation 
              key={project.id} 
              animation={index % 2 === 0 ? "slide-in-left" : "slide-in-right"}
              delay={index * 0.2}
            >
              <div className="project-card">
                <div className="project-image">
                  <img src={project.image} alt={project.title} />
                  <div className="project-overlay">
                    <div className="project-links">
                      <a href={project.demoLink} className="btn btn-sm" target="_blank" rel="noopener noreferrer">
                        Live Demo
                      </a>
                      <a href={project.codeLink} className="btn btn-sm btn-outline" target="_blank" rel="noopener noreferrer">
                        View Source
                      </a>
                    </div>
                  </div>
                </div>
                <div className="project-info">
                  <h3>{project.title}</h3>
                  <p>{project.description}</p>
                  <div className="project-tech">
                    {project.technologies.map((tech, techIndex) => (
                      <span key={techIndex} className="tech-tag">{tech}</span>
                    ))}
                  </div>
                </div>
              </div>
            </ScrollAnimation>
          ))}
        </div>

        <ScrollAnimation animation="fade-in">
          <div className="more-projects">
            <p>Want to see more of my work?</p>
            <a href="https://github.com/fujimaruC" className="btn" target="_blank" rel="noopener noreferrer">
              Visit My GitHub
            </a>
          </div>
        </ScrollAnimation>
      </div>
    </section>
  );
};

export default Projects;