/**
 * Main JavaScript for Portfolio Website
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // ==========================================
    // 1. Theme Toggle Logic
    // ==========================================
    const themeToggleBtns = document.querySelectorAll('[data-theme-toggle]');
    const root = document.documentElement;

    themeToggleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const currentTheme = root.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            root.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    });

    // ==========================================
    // 2. Mobile Navigation Menu
    // ==========================================
    const navToggle = document.getElementById('nav-toggle-btn');
    const navMenu = document.getElementById('navbar-nav');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
            navToggle.setAttribute('aria-expanded', !isExpanded);
            navMenu.classList.toggle('is-active');
        });
    }

    // ==========================================
    // 3. Modern Page Transitions (Fade)
    // ==========================================
    if (document.startViewTransition) {
        document.addEventListener('click', (e) => {
            const link = e.target.closest('a');
            
            // Only intercept internal links
            if (link && 
                link.href && 
                link.href.startsWith(window.location.origin) && 
                link.target !== '_blank' &&
                !link.href.includes('#')) {
                
                e.preventDefault();
                
                document.startViewTransition(async () => {
                    // Wait 50ms to let the fade-out start smoothly
                    await new Promise(resolve => setTimeout(resolve, 50));
                    window.location.href = link.href;
                });
            }
        });
    }
});