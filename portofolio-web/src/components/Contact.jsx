import React, { useState } from 'react';
import { ScrollAnimation } from './ScrollAnimation';
import emailjs from '@emailjs/browser';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  });
  
  const [formStatus, setFormStatus] = useState({
    submitted: false,
    success: false,
    message: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
  e.preventDefault();

    emailjs.send(
      'service_h60w1u8',
      'template_tfeic3r',
      {
        from_name: formData.name,
        from_email: formData.email,
        subject: formData.subject,
        message: formData.message,
      },
      'hxi5F3d8HGmD__IxX'
    )
    .then(() => {
      setFormStatus({
        submitted: true,
        success: true,
        message: 'Message sent successfully! I will get back to you soon.'
      });
      setFormData({ name: '', email: '', subject: '', message: '' });
    })
    .catch((error) => {
      console.error('EmailJS Error:', error);
      setFormStatus({
        submitted: true,
        success: false,
        message: 'Oops! Something went wrong. Please try again later.'
      });
    });
  };

  return (
    <section id="contact" className="contact">
      <div className="container">
        <ScrollAnimation>
          <h2 className="section-title">Get In Touch</h2>
        </ScrollAnimation>

        <div className="contact-content">
          <ScrollAnimation animation="slide-in-left">
            <div className="contact-info">
              <div className="contact-card">
                <i className="contact-icon">📧</i>
                <h3>Email</h3>
                <p>devfujimaru@gmail.com</p>
              </div>
              
              <div className="contact-card">
                <i className="contact-icon">📱</i>
                <h3>Phone</h3>
                <p>0816-4903-7312</p>
              </div>
              
              <div className="contact-card">
                <i className="contact-icon">📍</i>
                <h3>Location</h3>
                <p>Balikpapan, Indonesian</p>
              </div>
              
              <div className="social-links">
                <h3>Follow & Contact Me</h3>
                <div className="social-icons">
                  <a href="https://wa.me/6281649037312?text=Halo%20aku%20dari%20website%20kamu%20nih!" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
                    <i className="social-icon">WhatsApp</i>
                  </a>
                  <a href="https://instagram.com/jxri.co" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                    <i className="social-icon">Instagram</i>
                  </a>
                </div>
              </div>
            </div>
          </ScrollAnimation>

          <ScrollAnimation animation="slide-in-right">
            <div className="contact-form-container">
              <h3>Send Me a Message</h3>
              
              {formStatus.submitted && (
                <div className={`form-message ${formStatus.success ? 'success' : 'error'}`}>
                  {formStatus.message}
                </div>
              )}
              
              <form className="contact-form" onSubmit={handleSubmit}>
                <div className="form-group">
                  <input
                    type="text"
                    name="name"
                    id="name"
                    placeholder="Your Name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                  />
                </div>
                
                <div className="form-group">
                  <input
                    type="email"
                    name="email"
                    id="email"
                    placeholder="Your Email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                  />
                </div>
                
                <div className="form-group">
                  <input
                    type="text"
                    name="subject"
                    id="subject"
                    placeholder="Subject"
                    value={formData.subject}
                    onChange={handleChange}
                    required
                  />
                </div>
                
                <div className="form-group">
                  <textarea
                    name="message"
                    id="message"
                    rows="6"
                    placeholder="Your Message"
                    value={formData.message}
                    onChange={handleChange}
                    required
                  ></textarea>
                </div>
                
                <button type="submit" className="btn">Send Message</button>
              </form>
            </div>
          </ScrollAnimation>
        </div>
      </div>
    </section>
  );
};

export default Contact; 