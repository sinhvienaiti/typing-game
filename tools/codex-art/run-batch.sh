#!/bin/bash
# run-batch.sh <jobs-file> [dry]  — compose each prompt verbatim from the pack, generate with Codex, copy to the destination
D=/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/ea3cd405-f9d2-442c-a760-74fe0277c6ca/scratchpad/codex-art
jobs=$1; mode=$2; fails=0
while IFS='|' read -r name canvas ref dest md item rest; do
  [ -z "$name" ] && continue
  IFS='|' read -r -a parts <<< "$rest"
  if ! python3 -I $D/compose.py "$md" "$item" "${parts[@]}" > $D/prompts/$name.txt 2> $D/prompts/$name.err; then echo "COMPOSE_FAIL $name $(tail -1 $D/prompts/$name.err)"; continue; fi
  [ "$mode" = dry ] && { echo "ok $name $(wc -w < $D/prompts/$name.txt)w"; continue; }
  [ -f "$dest" ] && { echo "SKIP_EXISTS $name"; continue; }
  out=$($D/gen.sh "$name" "$canvas" $D/prompts/$name.txt "$ref" 2>&1 | tail -1)
  if [ -f "$out" ]; then mkdir -p "$(dirname "$dest")"; cp "$out" "$dest"; cp $D/prompts/$name.txt "${dest%.png}.prompt.txt"; echo "DONE $name $(sips -g pixelWidth -g pixelHeight "$out" | tail -2 | awk '{print $2}' | paste -sd x -)"; fails=0
  else echo "GEN_FAIL $name: $out"; fails=$((fails+1)); [ $fails -ge 3 ] && { echo "STOP after 3 failures"; exit 3; }; fi
done < "$jobs"
echo BATCH_END
