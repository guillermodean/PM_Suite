# installer/your_installer_script.ps1

# Check if running with administrative privileges
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "Please run this script as an administrator."
    Write-Host "Right-click on PowerShell and choose 'Run as administrator.'"
    exit
}

# Define installation path
$installPath = "C:\Program Files\PM_Suite"

# Specify log file path
$logFilePath = Join-Path $installPath "install_log.txt"

# Start transcript logging
Start-Transcript -Path $logFilePath

try {
    # Create installation directory
    New-Item -ItemType Directory -Path $installPath -Force | Out-Null

    # Copy files to installation directory
    $mainExePath = Join-Path $PSScriptRoot "..\dist\main\main.exe"

    if ($mainExePath -ne $null -and (Test-Path $mainExePath)) {
        Copy-Item -Path $mainExePath -Destination $installPath -Force
    }
    
    $scriptsPath = Join-Path $PSScriptRoot "..\scripts"
    if (Test-Path $scriptsPath) {
        Copy-Item -Path $scriptsPath -Destination $installPath -Recurse -Force
    }
    
    $pmsuitePath = Join-Path $PSScriptRoot "..\installer\pmsuite.ps1"
    if (Test-Path $pmsuitePath) {
        Copy-Item -Path $pmsuitePath -Destination $installPath -Recurse -Force
    }

    $staticPath = Join-Path $PSScriptRoot "..\static"
    if (Test-Path $staticPath) {
        Copy-Item -Path $staticPath -Destination $installPath -Recurse -Force
    }

    $licensePath = Join-Path $PSScriptRoot "..\LICENSE"
    if (Test-Path $licensePath) {
        Copy-Item -Path $licensePath -Destination $installPath -Force
    }

    $internalPath = Join-Path $PSScriptRoot "..\dist\main\_internal"
    if (Test-Path $internalPath) {
        Copy-Item -Path $internalPath -Destination $installPath -Recurse -Force
    }

    $readmePath = Join-Path $PSScriptRoot "..\README.md"
    if (Test-Path $readmePath) {
        Copy-Item -Path $readmePath -Destination $installPath -Force
    }

    # Create a shortcut on the desktop
    $desktopPath = [System.IO.Path]::Combine($env:USERPROFILE, "Desktop", "PM_suite.lnk")
    $targetPath = [System.IO.Path]::Combine($installPath, "main.exe")
    $WScriptShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WScriptShell.CreateShortcut($desktopPath)
    $Shortcut.TargetPath = $targetPath
    $Shortcut.Save()

    # Add installation directory to the PATH environment variable
    $installPathBin = Join-Path $installPath "bin"
    [Environment]::SetEnvironmentVariable("PATH", "$installPathBin;$env:PATH", [EnvironmentVariableTarget]::Machine)



    # Display a message about updating PATH
    Write-Host "The installation directory has been added to the PATH variable. You can now run 'pmsuite' from PowerShell or CMD."


    Write-Host "Installation completed. You can now run 'pm_suite' in PowerShell to start the program."
}
catch {
    # Log any errors
    Write-Host "Installation failed. Error: $_"
}
finally {
    # Stop transcript logging
    Stop-Transcript
}
