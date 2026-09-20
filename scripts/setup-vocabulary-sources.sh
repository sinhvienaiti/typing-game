#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/.cache/vocabulary-sources"

THICHHOC_URL="https://github.com/thichhoc-org/thichhoc-dict.git"
THICHHOC_REV="4d6e92e8bcf8e3e762410c2b0a9f98fea8e62e5b"
CEFR_URL="https://github.com/openlanguageprofiles/olp-en-cefrj.git"
CEFR_REV="d4e45b75b38f27b30dfc5c44d8c571aec7e7092f"
WORDFREQ_VERSION="3.1.1"
ESDB_URL="https://github.com/en-wl/wordlist.git"
ESDB_REV="1e5b7d3a72f47a71da5d28686c1dd4b397178485"

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

prepare_wordfreq() {
  destination="$SOURCE_DIR/wordfreq"
  mkdir -p "$destination"

  python3 -m pip install --disable-pip-version-check --quiet "wordfreq==$WORDFREQ_VERSION"
  python3 - "$destination/ranking.tsv" <<'PY'
from pathlib import Path
import sys
from wordfreq import top_n_list, zipf_frequency

output = Path(sys.argv[1])
words = top_n_list("en", 60000, wordlist="best", ascii_only=True)
with output.open("w", encoding="utf-8") as handle:
    for rank, word in enumerate(words, 1):
        if word.isalpha() and word.isascii() and len(word) >= 2:
            handle.write(f"{rank}\t{zipf_frequency(word, 'en')}\t{word.lower()}\n")
PY

  curl -fsSL "https://raw.githubusercontent.com/rspeer/wordfreq/912caf64b657478d1dff1138efdc078947d54bb1/LICENSE.txt" -o "$destination/LICENSE.txt"
  curl -fsSL "https://raw.githubusercontent.com/rspeer/wordfreq/912caf64b657478d1dff1138efdc078947d54bb1/NOTICE.md" -o "$destination/NOTICE.md"
}

prepare_esdb() {
  destination="$SOURCE_DIR/esdb"
  checkout_source "$ESDB_URL" "$destination" "$ESDB_REV"

  (
    cd "$destination"
    make >/dev/null
    ./scowl --db scowl.db word-list 70 A 1 --deaccent --wo-poses=abbr --categories=
  ) | awk '/^[a-z]+$/' | sort -u > "$destination/words.txt"
}

mkdir -p "$SOURCE_DIR"
checkout_source "$THICHHOC_URL" "$SOURCE_DIR/thichhoc-dict" "$THICHHOC_REV"
checkout_source "$CEFR_URL" "$SOURCE_DIR/olp-en-cefrj" "$CEFR_REV"
prepare_wordfreq
prepare_esdb

echo "Vocabulary sources ready at pinned versions/revisions."
