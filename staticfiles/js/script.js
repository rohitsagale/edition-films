// Mobile Navigation Toggle
const navToggle = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');

navToggle.addEventListener('click', () => {
 navMenu.classList.toggle('active');
 navToggle.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(link => {
 link.addEventListener('click', () => {
  navMenu.classList.remove('active');
  navToggle.classList.remove('active');
 });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
 anchor.addEventListener('click', function (e) {
  e.preventDefault();
  const target = document.querySelector(this.getAttribute('href'));
  if (target) {
   target.scrollIntoView({
    behavior: 'smooth',
    block: 'start'
   });
  }
 });
});

// Navbar background change on scroll
window.addEventListener('scroll', () => {
 const navbar = document.querySelector('.navbar');
 if (window.scrollY > 100) {
  navbar.style.background = 'rgba(255, 255, 255, 0.98)';
  navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
 } else {
  navbar.style.background = 'rgba(255, 255, 255, 0.95)';
  navbar.style.boxShadow = 'none';
 }
});

// Intersection Observer for animations
const observerOptions = {
 threshold: 0.1,
 rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
 entries.forEach(entry => {
  if (entry.isIntersecting) {
   entry.target.style.opacity = '1';
   entry.target.style.transform = 'translateY(0)';
  }
 });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', () => {
 const animatedElements = document.querySelectorAll('.service-card, .gallery-item, .video-card, .stat-item');

 animatedElements.forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(30px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(el);
 });
});

// Form validation
function validateForm(form) {
 let isValid = true;
 const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');

 inputs.forEach(input => {
  if (!input.value.trim()) {
   isValid = false;
   input.style.borderColor = 'var(--error)';
  } else {
   input.style.borderColor = '';
  }
 });

 return isValid;
}

// Initialize all forms
document.addEventListener('DOMContentLoaded', () => {
 const forms = document.querySelectorAll('form');
 forms.forEach(form => {
  form.addEventListener('submit', function (e) {
   if (!validateForm(this)) {
    e.preventDefault();
    alert('Please fill in all required fields.');
   }
  });
 });
});

// Video play functionality
document.querySelectorAll('.video-thumbnail').forEach(thumbnail => {
 thumbnail.addEventListener('click', function () {
  const videoUrl = this.dataset.videoUrl;
  if (videoUrl) {
   window.open(videoUrl, '_blank');
  }
 });
});

// Loading animation
window.addEventListener('load', () => {
 document.body.classList.add('loaded');
});

// Counter animation for stats
function animateCounter(element, target, duration = 2000) {
 let start = 0;
 const increment = target / (duration / 16);
 const timer = setInterval(() => {
  start += increment;
  if (start >= target) {
   element.textContent = target + '+';
   clearInterval(timer);
  } else {
   element.textContent = Math.floor(start) + '+';
  }
 }, 16);
}

// Initialize counter animation when stats are in view
const statsObserver = new IntersectionObserver((entries) => {
 entries.forEach(entry => {
  if (entry.isIntersecting) {
   const statNumber = entry.target.querySelector('.stat-number');
   const target = parseInt(statNumber.textContent);
   animateCounter(statNumber, target);
   statsObserver.unobserve(entry.target);
  }
 });
}, { threshold: 0.5 });

// Observe stats elements
document.querySelectorAll('.stat-item').forEach(stat => {
 statsObserver.observe(stat);
});