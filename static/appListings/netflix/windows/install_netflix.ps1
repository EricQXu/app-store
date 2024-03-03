<# 
	no need to run sudo
	run in Terminal: "set-executionpolicy bypass -scope process" (without quotes)
	run in Terminal: "powershell -file %USERPROFILE%\Downloads\test.ps1" (without quotes) 
#>
if exist "C:\Program Files\Sublime Text\sublime_text.exe" (
    echo "Sublime Text 4 is already installed on this system"
) else (
    echo "Installing Sublime Text 4..."; winget install --id=SublimeHQ.SublimeText.4  -e; echo "Sublime Text 4 installed"
)
