document.addEventListener('DOMContentLoaded', () => {
    // 1. Create and inject the Theme Toggle Button
    const toggleBtn = document.createElement('button');
    toggleBtn.className = 'theme-toggle';
    toggleBtn.innerHTML = '☀️ Light Mode';
    document.body.appendChild(toggleBtn);

    // 2. Check LocalStorage for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'light') {
        document.body.classList.add('light-mode');
        toggleBtn.innerHTML = '🌙 Dark Mode';
    }

    // 3. Handle Toggle Click
    toggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('light-mode');
        
        if (document.body.classList.contains('light-mode')) {
            localStorage.setItem('theme', 'light');
            toggleBtn.innerHTML = '🌙 Dark Mode';
        } else {
            localStorage.setItem('theme', 'dark');
            toggleBtn.innerHTML = '☀️ Light Mode';
        }
    });

    // 4. Smooth Fade-in Animation for Cards
    const cards = document.querySelectorAll('.unit-card, .question-card, .glass-panel');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100 * index); // Staggered fade in
    });
});
