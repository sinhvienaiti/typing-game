# Run one Codex task (a markdown brief) non-interactively and keep its logs.
#
#   powershell -File tools\codex-run\run.ps1 -Name dh-m0-images-1 -Brief docs\codex-queue\001-dh-m0-images.md -Cwd games\dragon-hold
#
# Codex CLI 0.164+ is needed for gpt-6.1-sol (the 0.146 build inside Cursor only reaches gpt-5.6-sol).
# Logs: .local\codex-runs\<Name>\{brief.md, events.jsonl, last.md, err.txt}
param(
  [Parameter(Mandatory = $true)] [string]$Name,
  [Parameter(Mandatory = $true)] [string]$Brief,
  [string]$Cwd = '.',
  [string]$Model = 'gpt-6.1-sol',
  [ValidateSet('high', 'xhigh', 'max')] [string]$Effort = 'high',
  [ValidateSet('read-only', 'workspace-write')] [string]$Sandbox = 'workspace-write',
  [string[]]$Image = @()
)
$ErrorActionPreference = 'Stop'
$root = Resolve-Path (Join-Path $PSScriptRoot '..\..')
$codex = if ($env:CODEX_BIN) { $env:CODEX_BIN } else { 'D:\_tools\codex-0.164.0\codex-x86_64-pc-windows-msvc.exe' }
if (-not (Test-Path $codex)) { throw "Codex CLI not found at $codex (set CODEX_BIN)" }

$log = Join-Path $root ".local\codex-runs\$Name"
New-Item -ItemType Directory -Force $log | Out-Null
$workdir = Resolve-Path (Join-Path $root $Cwd)
$briefText = Get-Content -Raw -Encoding UTF8 (Resolve-Path (Join-Path $root $Brief))

$preamble = @"
You are Codex working for the owner of the typing-game repo (D:\typing-game) on a Windows 11 laptop.
House rules for this task:
- Do exactly the task below. Touch only the paths it allows. Never run git commit, git push, git reset, git clean or git stash.
- git, node and pnpm exist only inside WSL Ubuntu (wsl -e bash <script>); you usually do not need them.
- Images: use your built-in image generation tool (image_gen). Save every image where the task says, with its exact prompt next to it as <name>.prompt.txt.
- Sounds must follow tools/audio-lab/DECISIONS.md Q6 (shaped by the action, no cheap puff/pop/thump sounds); write prompts affirmatively.
- Docs in Vietnamese with full diacritics, in the existing style of the folder.
- End with a short report: what you made (paths), what you skipped and why, anything the owner must look at.

TASK
"@

$prompt = $preamble + "`n" + $briefText
Set-Content -Path (Join-Path $log 'brief.md') -Value $prompt -Encoding UTF8

$imgArgs = @(); foreach ($i in $Image) { $imgArgs += @('-i', (Resolve-Path $i)) }
# The prompt goes in on stdin ("-"): briefs can be longer than a Windows command line, and stdin keeps UTF-8 intact.
# --disable memories: the owner's Codex memory writer failed inside a run (apply_patch on memory_summary.md).
$cxArgs = @('exec', '-m', $Model, '-c', "model_reasoning_effort=`"$Effort`"", '--disable', 'memories', '--skip-git-repo-check',
  '-s', $Sandbox, '-C', $workdir, '--json', '-o', (Join-Path $log 'last.md')) + $imgArgs + @('-')

$env:OPENAI_API_KEY = $null; $env:CODEX_API_KEY = $null   # use the owner's ChatGPT login, never an API key
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
# Windows PowerShell 5.1 turns every stderr line of a native command into an error record; with
# ErrorActionPreference Stop that aborted a whole run on one logged warning. Codex logs to stderr freely.
$ErrorActionPreference = 'Continue'
$prompt | & $codex @cxArgs > (Join-Path $log 'events.jsonl') 2> (Join-Path $log 'err.txt')
$code = $LASTEXITCODE
"exit $code"
if (Test-Path (Join-Path $log 'last.md')) { Get-Content -Encoding UTF8 (Join-Path $log 'last.md') }
exit $code
