# Cross-platform App Store PWA
This is an installable cross-platform App Store PWA that has offline caching support. This is a project currently under development. Feel free to contribute by opening a pull request!

## How to Install
Open up your Terminal and type the following:

    cd ./Downloads
    git clone https://github.com/EricQXu/passion-project-html
 Then, open `~/Downloads/passion-project-html-main` in VS Code. Inside VS Code, install the Live Server extension. After that, open `index.html` and right-click and click "Open with Live Server". (If the webpage opens with a non-Chromium based browser, paste the URL into a Chromium-based browser.) Now, you will see the install button on the URL bar and you can now install it.

## To-do
- attach links to apps in carousel on home.html
- clean up codebase
- attach the correct install script to the correct app info page and fix install script if there are any issues
- change purple accent color and highlight color to some other color
- [experimental feature] test if ```sudo mount .dmg```, ```sudo cp .app /Applications```, ```sudo umount .dmg``` works
- [experimental feature] if the above works great, maybe re-consider reworking scripts to do that instead of homebrew

### Bugs to Clean Up
- fix light/dark/system theme mode inconsistency between the main pages and app info page (JS: I forgot if it was embeded inside an HTML or if it was an external JS file, but anyways, fix it there)
- fix wrong icons in the left navbar
- [bug fix] fix broken search box on index.html and create.html and ... (maybe integrate in-website Google Search to search your site?) OR just delete the search bar altogether

### Optional Features
- prompt user to switch browsers to a Chromium-based browser if they are using Firefox or a Firefox-based browser upon load on landing page (index.html)
- add a "Buy Me a Coffee" button for donations and "Contribute" button that links to the GitHub repo page on the left navbar

### We might do this if we have time (or you can contribute to this part!):
- [feature] implement "sign-in with Google" button with favorited apps for each user
- [cosmetic] implement gaussian blur into the website ⚠️  Doesn't sound possible without a re-write, but we'll try
- [AI feature] implement AI summaries of user-written reviews
- [AI feature] implement AI recommendations of each app (ex. pros vs. cons of different web browser and which web browser is best for which group of people)
- [AI feature] implement a help section in the navbar where you can ask AI for app recommendations
- IMPORTANT! When implementing any AI-powered features or any feature requiring an API (ex. ChatGPT, Google Cloud, etc.), do NOT leak the API-key or secrets by pushing it to GitHub. Instead, in the API-key or secret field in your code, link it to an external file named 'secret.txt' and list that 'secret.txt' file on .gitignore so that you do NOT push it onto GitHub. When publishing the website using Vercel, provide the API-key or API-secret when prompted, which should be the ONLY time you provide an API key online.
