document.addEventListener('DOMContentLoaded', function() {
  const inputArea = document.querySelector('.input-area');
  
  inputArea.addEventListener('click', function() {
    this.classList.add('rainbow-glow');
  });

  inputArea.addEventListener('blur', function() {
    this.classList.remove('rainbow-glow');
  });
});