#!/usr/bin/env bash
# Bash/WSL/macOS entrypoint; Node is already required by this project.
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec node "$script_dir/sync-agent-skills.mjs" "$@"
