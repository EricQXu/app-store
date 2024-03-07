#!/bin/bash
# to make this script executable, cd into the directory where this file is located, then run "sudo chmod +x ./brew-chrome.sh" (without quotes)
# check if Google Chrome is already installed
# run defaults read "/Applications/Google Chrome.app/Contents/Info.plist" CFBundleIdentifier to get application id
# "command -v brew" checks whether or not the command "brew" exists. If command "brew" exists, the output would be the full installation path of the command "brew" (a.k.a. the package homebrew). If the command "brew" does not exist, there is no output. "&> /dev/null" sends the output of the previous command to /dev/null, a special file location where all output is deleted after being ran
cd /Applications
if ls -l | grep -i "Google Chrome" &> /dev/null; then
	echo "Google Chrome is already installed on this machine!"
elif command -v brew &> /dev/null; then
	# install brew package evernote
	echo "Installing Google Chrome..." && brew install --cask evernote && echo "Google Chrome has been successfully installed"
else
	# install homebrew and then install brew package evernote
	echo "Homebrew, a package manager that installs the requested app via command line, is not installed on this system" && echo "Installing Homebrew..." && /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && (echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> ~/.zprofile && eval "$(/usr/local/bin/brew shellenv)" && echo "Homebrew package manager has been successfully installed and added to PATH" && echo "Installing Google Chrome from Homebrew Package Manager..." && brew install --cask evernote && echo "Google Chrome has been successfully installed."
fi
