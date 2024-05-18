function showHideDLbtn(download, incompatibleMsg) {
    var os = getOS();
    var url = '';
    
    // Set the URL based on the OS
    if (os === 'Mac OS') {
        document.getElementById('incompatibleMsg').style.display = 'none'; //Will hide msg
        document.getElementById('download').style.display = 'block'; //Will show download btn
    } else if (os === 'iOS') {
        url = '';
    } else if (os === 'Windows') {
        document.getElementById('incompatibleMsg').style.display = 'none'; //Will hide msg
        document.getElementById('download').style.display = 'block'; //Will show download btn
    } else if (os === 'Android') {
        url = '';
    } else if (os === 'Linux') {
        document.getElementById('incompatibleMsg').style.display = 'none'; //Will hide msg
        document.getElementById('download').style.display = 'block'; //Will show download btn
    }    
}
	
function downloadFile() {
    var os = getOS();
    var url = '';
    
    // Set the URL based on the OS
    if (os === 'Mac OS') {
        url = 'GarageBand_10.3.4.dmg';
    } else if (os === 'iOS') {
        url = 'https://cdn.cloudflare.steamstatic.com/client/installer/steam.deb';
    } else if (os === 'Windows') {
        url = 'GarageBand_10.3.4.dmg';
    } else if (os === 'Android') {
        url = 'https://cdn.cloudflare.steamstatic.com/client/installer/steam.deb';
    } else if (os === 'Linux') {
        url = 'https://cdn.cloudflare.steamstatic.com/client/installer/steam.deb';
    }
    
    // Trigger the file download
    if (url !== '') {
        var link = document.createElement('a');
        link.href = url;
        link.download = 'Garageband';
        link.click();
    }
}

function getOS() {
    var userAgent = window.navigator.userAgent,
        platform = window.navigator.platform,
        macosPlatforms = ['Macintosh', 'MacIntel', 'MacPPC', 'Mac68K'],
        windowsPlatforms = ['Win32', 'Win64', 'Windows', 'WinCE'],
        iosPlatforms = ['iPhone', 'iPad', 'iPod'],
        os = null;
    
    if (macosPlatforms.indexOf(platform) !== -1) {
        os = 'Mac OS';
    } else if (iosPlatforms.indexOf(platform) !== -1) {
        os = 'iOS';
    } else if (windowsPlatforms.indexOf(platform) !== -1) {
        os = 'Windows';
    } else if (/Android/.test(userAgent)) {
        os = 'Android';
    } else if (!os && /Linux/.test(platform)) {
        os = 'Linux';
    }
    
    return os;
}

const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");


toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
})

searchBtn.addEventListener("click" , () =>{
    sidebar.classList.remove("close");
})

modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");
    if (body.classList.contains("dark")) {
      modeText.innerText = "Light mode";
      localStorage.setItem("darkMode", "true");
    } else {
      modeText.innerText = "Dark mode";
      localStorage.setItem("darkMode", "false");
    }
  });
  
document.addEventListener('DOMContentLoaded', function() {
    if (localStorage.getItem("darkMode") === "true") {
        document.body.classList.add('dark');
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add('dark');
    }
});

// Use this code block and comment out the block of code above if u don't want it to depend on system theme setting. In addition, in style.css, you may want to enclose body.dark with @media (prefers-color-scheme: dark) {}
//   // Check the dark mode state on page load
// if (localStorage.getItem("darkMode") === "true") {
//     body.classList.add("dark");
//     modeText.innerText = "Light mode";
// } else {
//     body.classList.remove("dark");
//     modeText.innerText = "Dark mode";
// }









window.onload = function() {
    showHideDLbtn(download, incompatibleMsg)
};