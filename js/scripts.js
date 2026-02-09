// Navbar Scroll Effect
document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.navbar');
    
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.style.boxShadow = "0 4px 20px rgba(0,0,0,0.08)";
            } else {
                navbar.style.boxShadow = "0 2px 10px rgba(0,0,0,0.03)";
            }
        });
    }
});

