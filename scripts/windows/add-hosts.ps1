# Adds every typing-game host from scripts/setup-nginx.sh (HOSTS=(...)) to the Windows hosts file.
# Run once in an elevated PowerShell (Run as administrator), from anywhere:
#   powershell -ExecutionPolicy Bypass -File D:\typing-game\scripts\windows\add-hosts.ps1
# Safe to re-run: hosts already present are skipped. Writes a backup next to the hosts file first.
$ErrorActionPreference = 'Stop'
$hostsFile = Join-Path $env:SystemRoot 'System32\drivers\etc\hosts'
$setup = Join-Path $PSScriptRoot '..\setup-nginx.sh'

$principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
  throw 'Run this script from an elevated PowerShell (Run as administrator).'
}

# HOSTS=( ... ) block of setup-nginx.sh, one host per line.
$text = Get-Content -Raw $setup
$block = [regex]::Match($text, 'HOSTS=\((?<body>[^)]*)\)').Groups['body'].Value
$wanted = [regex]::Matches($block, '[a-z0-9.-]+\.local') | ForEach-Object { $_.Value } | Select-Object -Unique
if (-not $wanted) { throw "No hosts found in $setup" }

$current = Get-Content $hostsFile
$present = $current | Where-Object { $_ -notmatch '^\s*#' } | ForEach-Object { ($_ -split '\s+') } | Where-Object { $_ }
$missing = $wanted | Where-Object { $present -notcontains $_ }
if (-not $missing) { "All $($wanted.Count) hosts are already in $hostsFile"; exit 0 }

Copy-Item $hostsFile "$hostsFile.typing-game.bak" -Force
Add-Content -Path $hostsFile -Value ("127.0.0.1 " + ($missing -join ' ')) -Encoding ascii
ipconfig /flushdns | Out-Null
"Added: $($missing -join ', ')"
"Backup: $hostsFile.typing-game.bak"
