// Check if the browser is Firefox or Safari
const isFirefox = navigator.userAgent.toLowerCase().indexOf('firefox') > -1;
const isSafari = /^((?!chrome|android).)*safari/i.test(navigator.userAgent);

if (isFirefox || isSafari) {
  // Display a popup message for unsupported browsers
  window.addEventListener('load', () => {
    alert("We're sorry, but your browser isn't compatible with our site. To enjoy all features, try using Brave, Chromium, Google Chrome, Microsoft Edge, Opera, or Vivaldi.");
  });
} else {
  // Continue with your existing code for Chromium-based browsers
  const installBtn = document.getElementById("installBtn");
  let deferredPrompt;

  window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent Chrome 67 and earlier from automatically showing the prompt
    e.preventDefault();
    // Stash the event so it can be triggered later.
    deferredPrompt = e;
    // Update UI notify the user they can add to home screen
    installBtn.style.display = 'inline-block';
  });

  installBtn.addEventListener('click', (e) => {
    // hide our user interface that shows our A2HS button
    installBtn.style.display = 'none';
    // Show the prompt
    deferredPrompt.prompt();
    // Wait for the user to respond to the prompt
    deferredPrompt.userChoice
      .then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
          console.log('User accepted the A2HS prompt');
          window.alert("Close this window, go to chrome://apps (or Start Menu if you are using Windows), and then launch the App Store from there.");
        } else {
          console.log('User dismissed the A2HS prompt');
        }
        deferredPrompt = null;
      });
  });
}