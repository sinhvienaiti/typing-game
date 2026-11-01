# Audio: real files, judged by the critic and the owner's ears

The living pipeline is [AUDIO_PIPELINE.md](../../../../docs/games/AUDIO_PIPELINE.md): spec, generate, measure, listen, ingest. The per-game Firefly sound lists are in `docs/games/audio/firefly/` (one JSON and one Markdown file per game, plus a README). This file holds the rules that apply to every game.

## 1. What is required

- **Real audio files only.** Synthesized placeholder sounds are a defect, the same as code-drawn art.
- **Every event has a sound and an effect:**
  - each typed letter, word done, wrong key and combo;
  - every attack and skill;
  - every foe's spawn, move, attack, hit and death;
  - every UI open, close, hover and click;
  - rewards, waves and bosses.
  - Keep a coverage matrix per game and fill every cell.
- **Typing games are niche,** so sound must fit and must be attractive. Simple or perfunctory sounds are not acceptable.

## 2. Route

- **Firefly Generate Sound Effects** (Adobe's Firefly Audio model; never partner models) is the current route, set by the owner on the evening of 29/10 (`docs/HANDOFF_CURRENT.md`, the Firefly sound row). The steps are list, generate, score, ingest:
  1. Write the per-event list with English prompts in the game's file under `docs/games/audio/firefly/`.
  2. Generate takes into `~/AudioLab/inbox/firefly/<game>/<event-id>/`, keeping Firefly's own file names. The owner generates them on his account; an agent does it in his signed-in Firefly tab only when he asks for that batch.
  3. Ingest with Audio Lab (`tools/audio-lab/`): trim, onset, loudness, hygiene, OGG, and a manifest with licence rows, landing in staging.
  4. Send the owner previews. Wire a sound only after his OK.
- **Other sources** follow AUDIO_PIPELINE §3 by category: CC0 libraries, sounds built in code only where the pipeline allows it, and local models with commercial-safe licences. They also follow its licence log (§10).

## 3. Who judges sound

- **Agents cannot hear.** The two "judges" for a sound are:
  - the Audio Lab layered critic (AUDIO_PIPELINE §4), which must pass every gate;
  - the owner, listening blind on the Listening Board with loudness-matched takes and fixed labels.
  - Shared keyboard sound profiles need 9 ([SHARED_SYSTEMS_BAR.md](../../../../docs/games/SHARED_SYSTEMS_BAR.md)).
- **Machine scores rank and flag; they do not choose.** Optimising toward the critic's numbers pulls sound toward clean but bland (Goodhart's law). Keep a "most different" take, and a low-ranked one, in the listening list.
- **Key sounds stay natural.** The owner picked the take that kept its tails, droplets, highs and loud/soft contrast. Hard cuts, heavy EQ and equal levels killed the effect.
- **Test sounds in context,** in the game's real mix: the "word done, reward sound, spoken word" chain is where the voice gets masked most easily.

## 4. Stop rule and banned sources

- **Stop rule:**
  - At most 3 prompt rounds per id.
  - After 3 rounds with fewer than 3 takes passing the gates, or after the owner rejects twice in a row, change the source. Order: library, then code, then own recording.
  - If that fails too, put the id on the "record or buy later" list.
- **Banned:**
  - non-commercial model weights (AudioGen, MusicGen, MAGNeT, MMAudio, AudioLDM, TangoFlux and the others in AUDIO_PIPELINE §3.5), not even for comparison;
  - BBC Sound Effects (personal and educational use only);
  - Pixabay (bans machine-learning use; unclear origin);
  - Freesound NC or Sampling+;
  - sounds lifted from other games;
  - Sonniss in any AI step, Claude included: only local signal measurements touch it (AUDIO_PIPELINE §10.2).
- **Heavy data stays out of Git and repos.** Weights, libraries, candidates and ratings live in `~/AudioLab/`. Ask before cleaning it; it is large and it is the owner's working set.
