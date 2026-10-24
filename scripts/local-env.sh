#!/usr/bin/env bash
# Source from launchers so a Terminal opened before bootstrap can run them too.
if [[ "$(uname -s)" == "Darwin" ]]; then
  local_brew="$(command -v brew || true)"
  if [[ -z "$local_brew" && -x /opt/homebrew/bin/brew ]]; then
    local_brew=/opt/homebrew/bin/brew
  fi
  if [[ -n "$local_brew" ]]; then
    local_brew_prefix="$("$local_brew" --prefix)"
    export PATH="$local_brew_prefix/bin:$local_brew_prefix/sbin:$PATH"
    if [[ -x "$local_brew_prefix/opt/node@24/bin/node" ]]; then
      export PATH="$local_brew_prefix/opt/node@24/bin:$PATH"
    fi
  fi
  unset local_brew local_brew_prefix
fi

# Linux / WSL (the Dell laptop): node comes from nvm, Chrome from Chrome for Testing,
# Blender from a Linux build. Windows .exe tools cannot take /mnt/... paths.
if [[ "$(uname -s)" == "Linux" ]]; then
  if ! command -v node >/dev/null 2>&1 && [[ -s "${NVM_DIR:-$HOME/.nvm}/nvm.sh" ]]; then
    export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
    # shellcheck disable=SC1091
    . "$NVM_DIR/nvm.sh"
  fi
  if [[ -z "${CHROME_PATH:-}" ]]; then
    local_chrome="$(ls -d "$HOME"/.cache/chrome-for-testing/chrome/linux-*/chrome-linux64/chrome 2>/dev/null | tail -1)"
    [[ -n "$local_chrome" ]] && export CHROME_PATH="$local_chrome"
    unset local_chrome
  fi
  if [[ -z "${BLENDER_BIN:-}" ]]; then
    local_blender="$(ls -d "$HOME"/.local/blender/blender-*-linux-x64/blender 2>/dev/null | tail -1)"
    [[ -n "$local_blender" ]] && export BLENDER_BIN="$local_blender"
    unset local_blender
  fi
fi
