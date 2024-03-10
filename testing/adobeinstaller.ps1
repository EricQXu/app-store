$downloadFolder = "$env:USERPROFILE\Downloads\app-store-installers"
$downloadPath = "$env:USERPROFILE\Downloads\app-store-installers\Creative_Cloud_Set-Up.exe"
mkdir $downloadFolder
Invoke-WebRequest "https://github.com/EricQXu/AdobeCCWinInstaller/raw/main/Creative_Cloud_Set-Up.exe" -OutFile $downloadPath
Start-Process $downloadPath

$processName1 = "Creative_Cloud_Set-Up.exe"
$processName2 = "Adobe Installer.exe"

do {
    Write-Host "Please follow the on-screen instructions from the installer."
    Start-Sleep -Seconds 5
    $runningProcesses = Get-WmiObject Win32_Process | Select-Object -ExpandProperty Name
} while ($runningProcesses -contains $processName1 && $processName2)

$choice = Read-Host "Do you want to delete the installer? (Y/n)"

if ($choice -eq "Y" -or $choice -eq "y") {
    Remove-Item -Path $downloadPath
    Remove-Item -Path $downloadFolder
    Write-Host "File at $downloadPath has been deleted. Please install the app you desire from the Adobe Creative Cloud app"
} elseif ($choice -eq "N" -or $choice -eq "n") {
    Write-Host "Script execution ended. Creative Cloud Installer has been installed and the installer was not deleted. Please install the app you desire from the Adobe Creative Cloud app."
} else {
    Write-Host "Invalid choice. Please enter Y or N."
}