# pmsuite.ps1

$installPath = "C:\Program Files\PM_suite"
$mainExePath = Join-Path $installPath "main.exe"

if (Test-Path $mainExePath) {
    Start-Process -FilePath $mainExePath -NoNewWindow
} else {
    Write-Host "main.exe not found. Please ensure that the installation path is correct."
}
