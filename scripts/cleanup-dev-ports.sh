#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PROJECT_ONLY=false

if [[ "${1:-}" == "--project-only" ]]; then
  PROJECT_ONLY=true
  shift
fi

if [[ "$#" -eq 0 ]]; then
  echo "Usage: $0 [--project-only] <port> [port ...]"
  exit 1
fi

if ! command -v lsof >/dev/null 2>&1; then
  echo "lsof is required to check development ports."
  exit 1
fi

targets=()
target_count=0

for port in "$@"; do
  if [[ ! "$port" =~ ^[0-9]+$ ]]; then
    echo "Invalid port: $port"
    exit 1
  fi

  pids="$(lsof -tiTCP:"$port" -sTCP:LISTEN 2>/dev/null || true)"

  for pid in $pids; do
    cwd="$(lsof -a -p "$pid" -d cwd -Fn 2>/dev/null | sed -n 's/^n//p' | head -n 1)"

    if [[ "$cwd" != "$ROOT_DIR" && "$cwd" != "$ROOT_DIR/"* ]]; then
      if [[ "$PROJECT_ONLY" == "true" ]]; then
        continue
      fi

      echo "Port $port is already used by a process outside this project."
      echo "PID: $pid"
      echo "cwd: ${cwd:-unknown}"
      echo "Stop that process manually, then run the dev command again."
      exit 1
    fi

    targets+=("$pid:$port")
    target_count=$((target_count + 1))
  done
done

if [[ "$target_count" -gt 0 ]]; then
  for target in "${targets[@]}"; do
    pid="${target%%:*}"
    port="${target##*:}"
    echo "Stopping stale typing-game process on port $port (PID $pid)..."
    kill "$pid" 2>/dev/null || true
  done
fi

if [[ "$PROJECT_ONLY" == "true" ]]; then
  if [[ "$target_count" -gt 0 ]]; then
    for target in "${targets[@]}"; do
      pid="${target%%:*}"
      port="${target##*:}"

      for _ in {1..30}; do
        if ! lsof -a -p "$pid" -iTCP:"$port" -sTCP:LISTEN >/dev/null 2>&1; then
          break
        fi
        sleep 0.1
      done

      if lsof -a -p "$pid" -iTCP:"$port" -sTCP:LISTEN >/dev/null 2>&1; then
        echo "Typing-game process PID $pid is still listening on port $port."
        exit 1
      fi
    done
  fi
  exit 0
fi

for port in "$@"; do
  for _ in {1..30}; do
    if [[ -z "$(lsof -tiTCP:"$port" -sTCP:LISTEN 2>/dev/null || true)" ]]; then
      break
    fi
    sleep 0.1
  done

  if [[ -n "$(lsof -tiTCP:"$port" -sTCP:LISTEN 2>/dev/null || true)" ]]; then
    echo "Port $port is still in use after stopping the old project process."
    exit 1
  fi
done
