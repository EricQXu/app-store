# Cross-platform App Store PWA
This is an installable cross-platform App Store PWA that has offline caching support. This is a project currently under development. Feel free to contribute if you are on my team!

## How to Install
Open up your Terminal and type the following:

    cd ./Downloads
    git clone https://github.com/EricQXu/passion-project-html
 Then, open `~/Downloads/passion-project-html-main` in VS Code. Inside VS Code, install the Live Server extension. After that, open `index.html` and right-click and click "Open with Live Server". (If the webpage opens with a non-Chromium based browser, paste the URL into a Chromium-based browser.) Now, you will see the install button on the URL bar and you can now install it.

## To-do
- [optional] add/remove comments and/or clean up codebase by grouping files of same category together (we don't have to do this, but we should do this if we are going to re-write the project later on or do something with it in the future after the hackathon)
- [optional] prompt user to switch browsers to a Chromium-based browser if they are using Firefox or a Firefox-based browser upon load on landing page (index.html) 
- [experimental feature] test if ```sudo mount .dmg```, ```sudo cp .app /Applications```, ```sudo umount .dmg``` works
- [experimental feature] if the above works great, maybe re-consider reworking scripts to do that instead of homebrew
- [planning] create a mockup of home.html, create.html, work.html, entertainment.html, social.html, and develop.html
- [feature] make the mockup of the above into reality by coding it
- [feature] attach links to apps in carousel on home.html
- [feature] add app ratings and other features/sections (see your OS's built-in App Store as an example) into the garageband app page
- [feature] duplicate the garageband app info page and make a page for every app and link it to home.html, create.html, etc.
- [optional feature] add a "Buy Me a Coffee" button for donations and "Contribute" button that links to the GitHub repo page on the left navbar
- [bug] fix light/dark/system theme mode inconsistency between the main pages and app info page (JS: I forgot if it was embeded inside an HTML or if it was an external JS file, but anyways, fix it there)
- [bug] fix bug where when you click on "Home", it takes you to index.html instead of home.html
- [bug] fix wrong icons in the left navbar
- [cosmetic] change purple accent color and highlight color to some other color
- [cosmetic] 
- [bug fix] fix broken search box on index.html and create.html and ... (maybe integrate in-website Google Search to search your site?) OR just delete the search bar altogether
- [feature] include screenshot on landing page (index.html) (screenshot 1: Windows 11, screenshot 2: macOS Ventura/Sonoma, screenshot 3: Linux Arch w/ Hyprland)
- [feature] deploy web app to Vercel (not GoDaddy since we may lose access to the domain after CruzHacks)


If time allows...
- [feature] implement "sign-in with Google" button with favorited apps for each user
- [cosmetic] implement gaussian blur into the website
- [AI feature] implement AI summaries of user-written reviews
- [AI feature] implement AI recommendations of each app (ex. pros vs. cons of different web browser and which web browser is best for which group of people)
- [AI feature] implement a help section in the navbar where you can ask AI for app recommendations
- IMPORTANT! When implementing any AI-powered features or any feature requiring an API (ex. ChatGPT, Google Cloud, etc.), do NOT leak the API-key or secrets by pushing it to GitHub. Instead, in the API-key or secret field in your code, link it to an external file named 'secret.txt' and list that 'secret.txt' file on .gitignore so that you do NOT push it onto GitHub. When publishing the website using Vercel, provide the API-key or API-secret when prompted, which should be the ONLY time you provide an API key online.
