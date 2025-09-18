import React from 'react';
import { useScrollAnimation } from '../hooks/useScrollAnimation';

export const ScrollAnimation = ({ 
  children, 
  animation = 'fade-in', 
  threshold = 0.1,
  delay = 0 
}) => {
  const { ref, isVisible } = useScrollAnimation(threshold);
  
  return (
    <div 
      ref={ref} 
      className={`${animation} ${isVisible ? 'visible' : ''}`}
      style={{ transitionDelay: `${delay}s` }}
    >
      {children}
    </div>
  );
};