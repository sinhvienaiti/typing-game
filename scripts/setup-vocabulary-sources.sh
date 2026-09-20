#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/.cache/vocabulary-sources"

THICHHOC_URL="https://github.com/thichhoc-org/thichhoc-dict.git"
THICHHOC_REV="4d6e92e8bcf8e3e762410c2b0a9f98fea8e62e5b"
CEFR_URL="https://github.com/openlanguageprofiles/olp-en-cefrj.git"
CEFR_REV="d4e45b75b38f27b30dfc5c44d8c571aec7e7092f"

checkout_source() {
  url="$1"
  destination="$2"
  revision="$3"

  if [ ! -d "$destination/.git" ]; then
    git clone --filter=blob:none "$url" "$destination"
  fi

  git -C "$destination" fetch --depth 1 origin "$revision"
  git -C "$destination" checkout --detach "$revision"
}

mkdir -p "$SOURCE_DIR"
checkout_source "$THICHHOC_URL" "$SOURCE_DIR/thichhoc-dict" "$THICHHOC_REV"
checkout_source "$CEFR_URL" "$SOURCE_DIR/olp-en-cefrj" "$CEFR_REV"

echo "Vocabulary sources ready at pinned revisions."
