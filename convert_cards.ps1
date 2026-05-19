<#
.SYNOPSIS
    PowerShell wrapper for the Spanish Playing Cards conversion script.

.DESCRIPTION
    This script provides a Windows-friendly way to run the convert_cards.py Python script.
    It checks for Python and required dependencies before execution.

.PARAMETER Formats
    Target formats (choices: png, jpeg, webp, avif, svg_optimized). Default: png.

.PARAMETER Width
    Target width in pixels. Default: 207.

.PARAMETER Height
    Target height in pixels. Default: 319.

.PARAMETER Quality
    Image quality (1-100). Default: 90.

.EXAMPLE
    .\convert_cards.ps1 -Formats webp, avif -Width 414 -Height 638
#>

param (
    [string[]]$Formats = @("png"),
    [int]$Width = 207,
    [int]$Height = 319,
    [int]$Quality = 90,
    [string[]]$InputFiles = @()
)

# Check for Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python not found. Please install Python from https://python.org"
    exit 1
}

# Check for dependencies
Write-Host "Checking dependencies..." -ForegroundColor Cyan
python -c "import cairosvg, PIL, scour, pillow_avif" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Missing dependencies. Attempting to install..." -ForegroundColor Yellow
    python -m pip install cairosvg pillow pillow-avif-plugin scour
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to install dependencies. Please run: pip install cairosvg pillow pillow-avif-plugin scour"
        exit 1
    }
}

# Construct arguments for the Python script
$pythonArgs = @("convert_cards.py")
$pythonArgs += "--formats"
$pythonArgs += $Formats
$pythonArgs += "--width"
$pythonArgs += $Width
$pythonArgs += "--height"
$pythonArgs += $Height
$pythonArgs += "--quality"
$pythonArgs += $Quality

if ($InputFiles.Count -gt 0) {
    $pythonArgs += "--input"
    $pythonArgs += $InputFiles
}

# Run the script
Write-Host "Starting conversion..." -ForegroundColor Green
python $pythonArgs

if ($LASTEXITCODE -eq 0) {
    Write-Host "Finished successfully!" -ForegroundColor Green
} else {
    Write-Host "Conversion failed. Please ensure Cairo is installed (e.g., via GTK for Windows)." -ForegroundColor Red
}
