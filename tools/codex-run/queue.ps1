# Run Codex tickets one after another from a list file, riding out ChatGPT usage limits.
#
#   powershell -File tools\codex-run\queue.ps1 -List .local\codex-lane-b.txt [-WaitFor codex-run-after-limit]
#
# List lines: name | brief | cwd | effort | sandbox   (blank lines and lines starting with # are skipped;
# effort defaults to high, sandbox to workspace-write). A ticket whose run hits the usage limit is retried
# after the time Codex names ("try again at 8:54 AM"), and one whose connection dropped is retried after
# 2 minutes, up to -MaxTries times in all; failed log dirs are kept.
param(
  [Parameter(Mandatory = $true)] [string]$List,
  # Wait until no other process whose command line contains this text is running (another queue).
  [string]$WaitFor = '',
  [int]$MaxTries = 4
)
$ErrorActionPreference = 'Continue'
$root = Resolve-Path (Join-Path $PSScriptRoot '..\..')
Set-Location $root
$run = Join-Path $PSScriptRoot 'run.ps1'

function Stamp { Get-Date -Format 'dd/MM HH:mm' }

if ($WaitFor) {
  while ($true) {
    $busy = Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
      Where-Object { $_.ProcessId -ne $PID -and $_.CommandLine -like "*$WaitFor*" -and $_.CommandLine -notlike '*queue.ps1*' }
    if (-not $busy) { break }
    Start-Sleep -Seconds 60
  }
  "$(Stamp) wait over: no '$WaitFor' left"
}

# Codex says "try again at 8:54 AM"; return that moment (tomorrow if it has passed) plus 2 minutes.
function LimitResume($events) {
  $m = Select-String -Path $events -Pattern 'try again at (\d{1,2}:\d{2}\s*[AP]M)' | Select-Object -Last 1
  if (-not $m) { return (Get-Date).AddMinutes(30) }
  $t = [datetime]::ParseExact($m.Matches[0].Groups[1].Value.ToUpper(), 'h:mm tt', [Globalization.CultureInfo]::InvariantCulture)
  $at = (Get-Date).Date.Add($t.TimeOfDay)
  if ($at -le (Get-Date)) { $at = $at.AddDays(1) }
  return $at.AddMinutes(2)
}

$items = Get-Content -Encoding UTF8 (Resolve-Path $List) | Where-Object { $_.Trim() -and -not $_.TrimStart().StartsWith('#') }
foreach ($line in $items) {
  $f = $line.Split('|') | ForEach-Object { $_.Trim() }
  $name = $f[0]; $brief = $f[1]
  $cwd = if ($f.Count -gt 2 -and $f[2]) { $f[2] } else { '.' }
  $effort = if ($f.Count -gt 3 -and $f[3]) { $f[3] } else { 'high' }
  $sandbox = if ($f.Count -gt 4 -and $f[4]) { $f[4] } else { 'workspace-write' }
  $log = Join-Path $root ".local\codex-runs\$name"
  for ($try = 1; $try -le $MaxTries; $try++) {
    if (Test-Path $log) { Rename-Item $log ("$name-prev-" + (Get-Date -Format 'MMddHHmm')) -ErrorAction SilentlyContinue }
    "$(Stamp) start $name (try $try, $effort, $sandbox)"
    powershell -NoProfile -ExecutionPolicy Bypass -File $run -Name $name -Brief $brief -Cwd $cwd -Effort $effort -Sandbox $sandbox | Out-Null
    $code = $LASTEXITCODE
    $events = Join-Path $log 'events.jsonl'
    $limited = (Test-Path $events) -and (Select-String -Path $events -Pattern 'usage limit' -Quiet)
    # A dropped connection ends the run without a report; image tickets skip finished files, so a rerun is cheap.
    $dropped = ($code -ne 0) -and (Test-Path $events) -and (Select-String -Path $events -Pattern 'stream disconnected' -Quiet)
    "$(Stamp) end $name exit $code$(if ($limited) { ' (usage limit)' } elseif ($dropped) { ' (connection dropped)' })"
    if ($dropped) { Start-Sleep -Seconds 120; continue }
    if (-not $limited) { break }
    $resume = LimitResume $events
    "$(Stamp) waiting for the limit to reset at $($resume.ToString('dd/MM HH:mm'))"
    while ((Get-Date) -lt $resume) { Start-Sleep -Seconds 60 }
  }
}
"$(Stamp) queue done"
