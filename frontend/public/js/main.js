document.addEventListener('DOMContentLoaded', function() {
  console.log('Astrology website loaded successfully');

  // Add event listeners to the sidebar menu items
  const menuItems = document.querySelectorAll('.nav-menu li a');
  
  menuItems.forEach(item => {
    item.addEventListener('click', function(e) {
      e.preventDefault();
      
      // Show a simple message when a menu item is clicked
      const content = document.querySelector('.content');
      content.innerHTML = `<h2>${this.textContent}</h2><p>Content for ${this.textContent} will be loaded soon.</p>`;
      
      // If clicking on Daily Horoscopes, we could show a sign selector
      if (this.textContent === 'Daily Horoscopes') {
        const signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 
                       'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'];
        
        let signSelector = '<div class="sign-selector"><h3>Select Your Sign:</h3><div class="signs-grid">';
        
        signs.forEach(sign => {
          signSelector += `<div class="sign-item" data-sign="${sign}">${sign.charAt(0).toUpperCase() + sign.slice(1)}</div>`;
        });
        
        signSelector += '</div></div>';
        content.innerHTML += signSelector;
        
        // Add event listeners to sign items
        setTimeout(() => {
          const signItems = document.querySelectorAll('.sign-item');
          signItems.forEach(item => {
            item.addEventListener('click', function() {
              const sign = this.getAttribute('data-sign');
              // In a real app, this would call the API function from api.js
              console.log(`Selected sign: ${sign}`);
              content.innerHTML += `<div class="loading">Loading horoscope for ${sign}...</div>`;
              
              // Simulate API call
              setTimeout(() => {
                content.querySelector('.loading').remove();
                content.innerHTML += `<div class="horoscope-result">
                  <h3>${sign.charAt(0).toUpperCase() + sign.slice(1)} Daily Horoscope</h3>
                  <p>The stars are aligned for you today. Trust your instincts and embrace new opportunities.</p>
                </div>`;
              }, 1000);
            });
          });
        }, 100);
      }
    });
  });
}); 