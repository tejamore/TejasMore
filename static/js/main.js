// Footer year
document.getElementById('year').textContent = new Date().getFullYear();

// Scroll-reveal: fade/slide elements into view as they enter the viewport
const revealEls = document.querySelectorAll('.reveal');

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  revealEls.forEach((el) => observer.observe(el));
} else {
  // Fallback: show everything immediately
  revealEls.forEach((el) => el.classList.add('is-visible'));
}
