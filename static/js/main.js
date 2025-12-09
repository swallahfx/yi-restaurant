// ===== MAIN JAVASCRIPT FILE =====

document.addEventListener('DOMContentLoaded', function() {
    initializeNavigation();
    initializeScrollEffects();
    initializeModals();
    initializeDatePickers();
    initializeAnimations();
});

// ===== NAVIGATION =====
function initializeNavigation() {
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navbar = document.getElementById('navbar');
    
    // Mobile navigation toggle
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });
        
        // Close mobile menu when clicking on links
        const navLinks = navMenu.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
                document.body.classList.remove('menu-open');
            });
        });
    }
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!navbar.contains(e.target) && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
            document.body.classList.remove('menu-open');
        }
    });
}

// ===== SCROLL EFFECTS =====
function initializeScrollEffects() {
    const navbar = document.getElementById('navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Add/remove scrolled class
        if (scrollTop > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Hide/show navbar on scroll
        if (scrollTop > lastScrollTop && scrollTop > 200) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    }, false);
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
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
}

// ===== MODAL FUNCTIONALITY =====
function initializeModals() {
    const overlay = document.getElementById('overlay');
    
    // Create overlay if it doesn't exist
    if (!overlay) {
        const overlayDiv = document.createElement('div');
        overlayDiv.id = 'overlay';
        overlayDiv.className = 'overlay';
        document.body.appendChild(overlayDiv);
    }
}

function openReservationModal() {
    const modal = document.getElementById('reservation-modal');
    const overlay = document.getElementById('overlay');
    
    if (modal) {
        modal.style.display = 'flex';
        overlay.style.display = 'block';
        document.body.style.overflow = 'hidden';
        
        // Animate in
        setTimeout(() => {
            modal.style.opacity = '1';
            overlay.style.opacity = '1';
        }, 10);
        
        // Auto-focus first input
        const firstInput = modal.querySelector('input[type="text"], input[type="email"]');
        if (firstInput) {
            firstInput.focus();
        }
        
        // Pre-fill with order data if available
        if (typeof localStorage !== 'undefined') {
            const preOrder = localStorage.getItem('preOrder');
            if (preOrder) {
                const messageField = modal.querySelector('textarea[name="message"]');
                if (messageField) {
                    const orderItems = JSON.parse(preOrder);
                    const orderText = orderItems.map(item => 
                        `${item.name} x${item.quantity}`
                    ).join(', ');
                    messageField.value = `Pre-order: ${orderText}`;
                }
            }
        }
    }
}

function closeReservationModal() {
    const modal = document.getElementById('reservation-modal');
    const overlay = document.getElementById('overlay');
    
    if (modal && overlay) {
        modal.style.opacity = '0';
        overlay.style.opacity = '0';
        document.body.style.overflow = 'auto';
        
        setTimeout(() => {
            modal.style.display = 'none';
            overlay.style.display = 'none';
        }, 300);
    }
}

// ===== DATE PICKER INITIALIZATION =====
function initializeDatePickers() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    
    dateInputs.forEach(input => {
        // Set minimum date to today
        const today = new Date().toISOString().split('T')[0];
        input.min = today;
        
        // Set maximum date to 3 months from now
        const maxDate = new Date();
        maxDate.setMonth(maxDate.getMonth() + 3);
        input.max = maxDate.toISOString().split('T')[0];
    });
}

// ===== ANIMATIONS =====
function initializeAnimations() {
    // Intersection Observer for scroll animations
    const observeElements = document.querySelectorAll(
        '.feature-card, .dish-card, .side-card, .gallery-item, .team-member, .value-card'
    );
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Staggered animation delay
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    entry.target.classList.add('animated');
                }, index * 100);
                
                // Unobserve after animation
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '50px'
    });
    
    // Setup elements for animation
    observeElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
        observer.observe(el);
    });
    
    // Parallax effect for hero sections
    const heroSections = document.querySelectorAll('.hero, .page-hero');
    
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        
        heroSections.forEach(hero => {
            const heroBackground = hero.querySelector('.hero-bg');
            if (heroBackground) {
                heroBackground.style.transform = `translateY(${scrolled * 0.3}px)`;
            }
        });
    });
}

// ===== FORM HANDLING =====
function validateForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(field => {
        field.classList.remove('error');
        
        if (!field.value.trim()) {
            field.classList.add('error');
            isValid = false;
        }
        
        // Email validation
        if (field.type === 'email' && field.value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(field.value)) {
                field.classList.add('error');
                isValid = false;
            }
        }
        
        // Phone validation (basic)
        if (field.type === 'tel' && field.value) {
            const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
            if (!phoneRegex.test(field.value.replace(/\s/g, ''))) {
                field.classList.add('error');
                isValid = false;
            }
        }
    });
    
    return isValid;
}

// Add form validation styles
const style = document.createElement('style');
style.textContent = `
    .form-group input.error,
    .form-group select.error,
    .form-group textarea.error {
        border-color: var(--error-color);
        box-shadow: 0 0 0 3px rgba(231, 76, 60, 0.1);
    }
    
    .form-group input.error:focus,
    .form-group select.error:focus,
    .form-group textarea.error:focus {
        border-color: var(--error-color);
        box-shadow: 0 0 0 3px rgba(231, 76, 60, 0.2);
    }
`;
document.head.appendChild(style);

// ===== UTILITY FUNCTIONS =====
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// ===== NOTIFICATION SYSTEM =====
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i>
            <span>${message}</span>
            <button onclick="this.parentElement.parentElement.remove()">&times;</button>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.opacity = '1';
        notification.style.transform = 'translateX(0)';
    }, 10);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => notification.remove(), 300);
    }, 5000);
}

// ===== LOADING STATES =====
function setLoadingState(button, loading = true) {
    if (loading) {
        button.dataset.originalText = button.textContent;
        button.textContent = 'Loading...';
        button.disabled = true;
        button.classList.add('loading');
    } else {
        button.textContent = button.dataset.originalText || 'Submit';
        button.disabled = false;
        button.classList.remove('loading');
    }
}

// ===== KEYBOARD ACCESSIBILITY =====
document.addEventListener('keydown', function(e) {
    // Close modal on Escape key
    if (e.key === 'Escape') {
        const openModal = document.querySelector('.modal[style*="display: flex"]');
        if (openModal) {
            closeReservationModal();
        }
    }
    
    // Navigate menu with arrow keys
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        const activeElement = document.activeElement;
        const navLinks = Array.from(document.querySelectorAll('.nav-link'));
        const currentIndex = navLinks.indexOf(activeElement);
        
        if (currentIndex !== -1) {
            e.preventDefault();
            let nextIndex;
            
            if (e.key === 'ArrowDown') {
                nextIndex = (currentIndex + 1) % navLinks.length;
            } else {
                nextIndex = currentIndex === 0 ? navLinks.length - 1 : currentIndex - 1;
            }
            
            navLinks[nextIndex].focus();
        }
    }
});

// ===== TOUCH GESTURES =====
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', function(e) {
    touchStartX = e.changedTouches[0].screenX;
});

document.addEventListener('touchend', function(e) {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
});

function handleSwipe() {
    const swipeThreshold = 100;
    const difference = touchStartX - touchEndX;
    
    if (Math.abs(difference) > swipeThreshold) {
        if (difference > 0) {
            // Swipe left - could implement gallery navigation
            console.log('Swipe left');
        } else {
            // Swipe right - could implement gallery navigation
            console.log('Swipe right');
        }
    }
}

// ===== PERFORMANCE OPTIMIZATIONS =====
// Lazy load images when they become visible
function initializeLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Preload critical assets
function preloadCriticalAssets() {
    const criticalAssets = [
        '/static/css/main.css',
        // Add other critical assets here
    ];
    
    criticalAssets.forEach(asset => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.href = asset;
        link.as = asset.endsWith('.css') ? 'style' : 'script';
        document.head.appendChild(link);
    });
}

// ===== ERROR HANDLING =====
window.addEventListener('error', function(e) {
    console.error('JavaScript error:', e.error);
    // Could send error reports to analytics service here
});

window.addEventListener('unhandledrejection', function(e) {
    console.error('Unhandled promise rejection:', e.reason);
    // Could send error reports to analytics service here
});

// ===== EXPORT FUNCTIONS FOR GLOBAL USE =====
window.openReservationModal = openReservationModal;
window.closeReservationModal = closeReservationModal;
window.showNotification = showNotification;
window.setLoadingState = setLoadingState;
window.validateForm = validateForm;

// Initialize lazy loading if elements exist
if (document.querySelectorAll('img[data-src]').length > 0) {
    initializeLazyLoading();
}

// Preload critical assets
preloadCriticalAssets();

console.log('Yí Restaurant website initialized successfully!');
