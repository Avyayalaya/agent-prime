param(
    [ValidateSet("preview", "quick-trial", "onboard")]
    [string]$Mode,
    [switch]$Yes,
    [switch]$NoBrowser,
    [switch]$SkipDashboard,
    [switch]$SkipVerify,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ExtraArgs
)

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$scriptPath = Join-Path $root "meta\scripts\first_run.py"

$pythonCommand = $null
if (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCommand = @("py", "-3")
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCommand = @("python")
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $pythonCommand = @("python3")
} else {
    Write-Error "Python 3.10+ is required to run Agent Prime first-time setup."
    exit 1
}

$scriptArgs = @($scriptPath)
if ($Mode) { $scriptArgs += @("--mode", $Mode) }
if ($Yes) { $scriptArgs += "--yes" }
if ($NoBrowser) { $scriptArgs += "--no-browser" }
if ($SkipDashboard) { $scriptArgs += "--skip-dashboard" }
if ($SkipVerify) { $scriptArgs += "--skip-verify" }
if ($ExtraArgs) { $scriptArgs += $ExtraArgs }

if ($pythonCommand.Length -gt 1) {
    & $pythonCommand[0] $pythonCommand[1] @scriptArgs
} else {
    & $pythonCommand[0] @scriptArgs
}
exit $LASTEXITCODE
