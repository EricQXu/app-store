<# 
	no need to run sudo
	run in Terminal: "set-executionpolicy bypass -scope process" (without quotes)
	run in Terminal: "powershell -file %USERPROFILE%\Downloads\test.ps1" (without quotes) 
#>
if exist "C:\'Program Files (x86)'\Google\Chrome\Application\chrome.exe" (
    echo "Google Chrome is already installed on this system"
) else (
    echo "Installing Google Chrome..."; winget install -e --id Google.Chrome; echo "Google Chrome installed"
)
