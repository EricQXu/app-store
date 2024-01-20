This folder is dedicated for working components that are to be implemented into the project.
/testing/download-button-context-aware contains files to get an OS-specific download button working
/testing/sample-scripts contain shell scripts that will download the sample app (Chrome, VLC, Sublime Text, etc.) with just running taht one sample app. This is OS-dependent and run on each respective OS from each respective folder.


---------------------------

Some Notes on how to try out /testing/sample-scripts:
(1) To get Windows and Linux running on a Mac, try Parallels and UTM Virtual Machine, respectively.
(2) To get Windows and Mac running on Linux, try running QEMU Virt-Manager and sickcodes/Docker-OSX, respectively.
(3) To get Linux and Mac running on Windows, try running WSL and running the second option in (2) through WSL, respectively.
