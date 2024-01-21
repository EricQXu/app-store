#!/bin/bash
# before running this script, go into terminal and run "chmod +x steam.sh" (without quotes) after changing directory (cd) into the directory where this file is located in terminal
if [ -f /etc/os-release ]; then
    # freedesktop.org and systemd
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID
elif type lsb_release >/dev/null 2>&1; then
    # linuxbase.org
    OS=$(lsb_release -si)
    VER=$(lsb_release -sr)
elif [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    OS=$DISTRIB_ID
    VER=$DISTRIB_RELEASE
elif [ -f /etc/debian_version ]; then
    # Older Debian/Ubuntu/etc.
    OS=Debian
    VER=$(cat /etc/debian_version)
elif [ -f /etc/SuSe-release ]; then
    # Older SuSE/etc.
    ...
elif [ -f /etc/redhat-release ]; then
    # Older Red Hat, CentOS, etc.
    ...
else
    # Fall back to uname, e.g. "Linux <version>", also works for BSD, etc.
    OS=$(uname -s)
    VER=$(uname -r)
fi
echo "Detected OS: $OS" && echo "Installing steam for $OS..."
if [ "$OS" == "Linux Debian" ] || [ "$OS" == "Linux Ubuntu" ] || [ "$OS" == "Linux Mint" ] || [ "$OS" == "Linux PopOS" ] || [ "$OS" == "Linux ZorinOS" ] || [ "$OS" == "Linux Kubuntu" ] || [ "$OS" == "Linux ZorinOS" ]; then
    if command -v steam &> /dev/null
    then
        echo "steam is already installed on this system."
    else
        sudo apt update && sudo apt install steam && echo "steam installed"
    fi
elif [ "$OS" == "Linux Arch" ] || [ "$OS" == "Linux Manjaro" ] || [ "$OS" == "Linux Arctix" ] || [ "$OS" == "Linux SteamOS" ]; then
    if command -v steam &> /dev/null
    then
        echo "steam is already installed on this system."
    else
        sudo pacman -Syu steam && echo "steam installed"
    fi
elif "$OS" == "Linux Manjaro"; then
    if command -v steam &> /dev/null
    then
        echo "steam is already installed on this system."
    else
        pamac install steam && echo "steam installed"
    fi
elif [ "$OS" == "Linux Fedora" ] || [ "$OS" == "Linux CentOS" ] || [ "$OS" == "Linux Red Hat" ] || [ "$OS" == "Linux Red Hat Enterprise" ]; then
    if command -v steam &> /dev/null
    then
        echo "steam is already installed on this system."
    else
        sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm && sudo dnf install steam && echo "steam installed"
    fi
elif "$OS" == "Linux AmongOS"; then
    echo "You are sus. Out of all the distros out there, why would you pick AmongOS to daily drive? Only one word: sus!"
fi
