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
