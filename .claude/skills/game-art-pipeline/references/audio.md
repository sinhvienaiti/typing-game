# Audio: real files, judged by the critic and the owner's ears

The living pipeline is [AUDIO_PIPELINE.md](../../../../docs/games/AUDIO_PIPELINE.md): spec, generate, measure, listen, ingest. The per-game Firefly sound lists are in `docs/games/audio/firefly/` (one JSON and one Markdown file per game, plus a README). This file holds the rules that apply to every game. Combat sound has its own direction in §5, and it wins over any rule written for keyboard sounds, in this file, the pipeline or a game's sound list.

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
- **Combat hits hard.** Shots, impacts, kills, explosions and big events are powerful, explosive, reverberant and cinematic, at commercial-game level (§5). Keys and UI stay light and pleasant.

## 2. Route

- **Firefly Generate Sound Effects** (Adobe's Firefly Audio model; never partner models) is the current route, set by the owner on the evening of 29/10 (`docs/HANDOFF_CURRENT.md`, the Firefly sound row). The steps are list, generate, score, ingest:
  1. Write the per-event list with English prompts in the game's file under `docs/games/audio/firefly/`. Combat ids get one prompt per layer (§5.6).
  2. Generate takes into `~/AudioLab/inbox/firefly/<game>/<event-id>/`, keeping Firefly's own file names. The owner generates them on his account; an agent does it in his signed-in Firefly tab only when he asks for that batch.
  3. Ingest with Audio Lab (`tools/audio-lab/`): trim, onset, loudness, hygiene, OGG, and a manifest with licence rows, landing in staging. Combat layers are stacked and processed offline first (§5.7).
  4. Send the owner previews. Wire a sound only after his OK.
- **Other sources** follow AUDIO_PIPELINE §3 by category: CC0 libraries, sounds built in code only where the pipeline allows it, and local models with commercial-safe licences. They also follow its licence log (§10).

## 3. Who judges sound

- **Agents cannot hear.** The two "judges" for a sound are:
  - the Audio Lab layered critic (AUDIO_PIPELINE §4), which must pass every gate;
  - the owner, listening blind on the Listening Board with loudness-matched takes and fixed labels.
  - Shared keyboard sound profiles need 9 ([SHARED_SYSTEMS_BAR.md](../../../../docs/games/SHARED_SYSTEMS_BAR.md)).
- **Machine scores rank and flag; they do not choose.** Optimising toward the critic's numbers pulls sound toward clean but bland (Goodhart's law). Keep a "most different" take, and a low-ranked one, in the listening list.
- **Key sounds stay natural.** The owner picked the take that kept its tails, droplets, highs and loud/soft contrast. Hard cuts, heavy EQ and equal levels killed the effect. This is a rule for keys, never for combat (§5.1).
- **Test sounds in context,** in the game's real mix: the "word done, reward sound, spoken word" chain is where the voice gets masked most easily, and a big wave at top typing speed is where combat gets flattened.
- **Key latency probe, for the next Typing Feel change:** at 10–20 keys/s, measure keydown to sound start (p50 and p95), jitter, voice cuts and GC pauses (`shared/game-kit/feedback/typing-fx/audio.ts`, TYPING_FEEL_SERVICE §8). Proposed bar: p95 ≤ `outputLatency` + 20 ms. The kit already plays native Web Audio: no switch to Howler or Tone.js.

## 4. Stop rule and banned sources

- **Stop rule:**
  - At most 3 prompt rounds per id (per layer id for combat).
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

## 5. Combat sound: power, layering, space

Owner, 02/11/2026, on Last Line's combat sounds: "nó quá kiểu nhỏ nhẹ và thiếu sự mạnh mẽ, bùng nổ, âm thanh vang vọng, tại sao bạn cứ làm ra những cái âm thanh nghe kiểu đơn giản, thiếu sự chiến đấu, bùng nổ, đầy chiến ý vậy".

**Style: cinematic and magical, not realistic** (owner, 02/11/2026: "chúng ta k làm ra kiểu âm thanh như thật… phải bùng nổ, đẹp, hào quang, thu hút của các phim anime hoặc các thần thoại"). Fantasy and xianxia skills sound like anime and mythic spectacle: energy surges, shimmering whooshes, crystalline chimes, choir or synth swells, sub booms, sparkling tails, huge reverberant impacts. Real recordings (steel, stone, water) are raw ingredients under a magical layer, never the whole cue; a foley-real cue fails even when it is clean. A modern-military game such as Last Line keeps its weapons grounded but just as big and cinematic.

This section covers every combat event in every game: shots, skills, traps, impacts, kills, explosions, enemy attacks, surges and bosses. Keys, UI and word-done sounds keep their own rules (§3, AUDIO_PIPELINE §6.2). Sources were read on 02/11/2026 and are listed in §5.11. Numbers marked "start" are starting values to tune by ear in the play mix.

### 5.1 The trap we fell into

- **Keyboard rules ran combat.** Rules written for key sounds were applied to guns and kills: soft, short tails, non-fatiguing; 1–4 kHz cut within 30 ms; tails only under 1 kHz or over 4 kHz; every short file normalised to one loudness.
- **Prompts asked for small sounds.** Last Line's Firefly list said "small", "quiet", "faint", "gentle onset", "soft distant decay", "restrained", "compact" and "below one kilohertz", in long sentences chaining sounds with "followed by". Adobe's own guide asks for the opposite (§5.6).
- **One take per sound.** No layers, no space, no reverb, and levels evened out.
- **The mix flattened what was left.** `games/typing-survival/src/audio/theme-audio.ts:153` sends every bus through a glue compressor (threshold −12, ratio 8, attack 2 ms). Measured in Chromium:
  - WebAudio added about +5 dB of automatic makeup gain to quiet input;
  - 12 dB of input range came out as 3.8 dB;
  - a 30 ms burst got no attack lift.

  The guns bus (0.42) also sat under the keys bus (0.5), and guns dipped −6 dB under every spoken word.
- **The rule this produced:** fatigue is fixed with short peaks and hierarchy, never with smaller combat sounds. Halo Infinite's team found long, heavily compressed, over-saturated gun assets tiring and moved to a sharp attack with a quick decay. A combat prompt, spec or mix setting copied from the keyboard rules is a defect.

### 5.2 Two rule sets

| | Typing feedback (`key.*`, word-done, UI) | Combat impact (everything else in a fight) |
|---|---|---|
| Character | Soft, short, natural tails | Sharp attack, dense body, low weight, a signature layer, a space tail |
| Variation | Natural; 6–10 variants for keys | 3–5 variants on heads and bodies; hit and kill confirms nearly fixed, so players learn them |
| Space | Dry | Baked tail plus an in-game reverb send (§5.8) |
| Level | Even, below combat | Tiers (§5.4): routine shots smaller, so big events can be large |
| Ducking | Keys dip under the spoken word | Music, tails and the reverb return dip under the word; dry hits at most −3 dB; big events duck routine combat |
| Frequency | Strict (AUDIO_PIPELINE §6.2, §6.4) | §5.5 |

### 5.3 Layer recipe per event class

Build each combat sound from ingredients, never from one take. Layers follow the five VFX phases (charge, release, travel, impact, aftermath).

- **Start offsets:** mechanics at 0 when used; head at 0 (+5–10 ms with mechanics); body +2–5 ms after the head; sub +4–8 ms.
- **Process each layer for its job** (§5.7), then stack, then glue.

| Event class | Layers (lengths are start values) | Notes |
|---|---|---|
| Rapid shot (4 or more a second) | HEAD crack 15–40 ms at 2–8 kHz; BODY 80–150 ms, saturated; LOW punch 60–80 Hz, 60–120 ms; MECH clack on a burst's first shot only | Shared TAIL stem with at most 2 voices; one longer release tail when firing stops |
| Heavy shot (shotgun, rail, cannon) | CHARGE 0.2–1.2 s (rising whine or pre-verb swell) with a 40–80 ms dip before the release; HEAD; MECH slam; BODY 100–250 ms; SUB drop 40–80 Hz, 120–220 ms | Baked TAIL 1–3 s plus a 150–350 ms slapback. DOOM's Gauss rifle: a short impulse that cuts to silence, then the big one |
| Beam or sustained cast | IGNITE crack and whoosh-in, 100–150 ms; LOOP roar 3–5 s, seamless; low BED loop; CRACKLE one-shots on top; STOP whoosh-down 300–450 ms with a tail | Slow filter movement keeps the loop alive |
| Launched or explosive (mortar, grenade, fireball) | LAUNCH thump and tube ring; TRAVEL whistle with doppler; IMPACT crack, boom (body an octave down, saturated), sub 30–50 Hz, debris | Pre-duck the music 60–100 ms before a known impact; TAIL rolling echo and debris rain, 1–2 s |
| Hit confirm | Bright, tonal tick 25–90 ms plus a punchy short body | Gather hits within about 38 ms, one sound per batch; higher tiers add layers (sub, then tail), not only gain |
| Swarm kill | Crunch or burst plus a short low thump, 100–220 ms | At most 3–4 at once; past 6 kills in 100 ms play one mass-kill layer with more body; pitch may climb with a streak |
| Elite or big kill | Impact, sub, a metal ring or short braam, tail 1–2 s | Music dips about −3 dB |
| Big event (boss hit, surge, ultimate, boss death, breach saved) | Pre-verb swell, crack, body, sub drop, long tail 2–3 s | Priority P0: ducks routine combat; rare |
| Enemy attack | Wind-up tell (rising, one per attack), strike, impact on the hero | The tell never changes, so players learn it |

### 5.4 Loudness and hierarchy

Every combat file carries its tier. Normalise it to the tier's momentary max (400 ms window, file padded with silence), not to one shared level, and keep bus and catalog gains near unity so the file means what it says.

| Tier | Class | Momentary max (LUFS, start) | Notes |
|---|---|---|---|
| T0 | Keys | As AUDIO_PIPELINE §4.3.3 (−28 to −24 in the mix) | Light; never over combat |
| T1 | UI, small alerts | −30 to −22, not over keys | |
| T2 | Rapid shots, beam loop | −19 to −17 | Rapid fire sums 3–4 LU higher over short windows |
| T3 | Hits, swarm kills | −20 to −16 | Louder hit tiers come from more layers |
| T4 | Heavy shots, beam ignition, elite kills | −15 to −12 | |
| T5 | Explosions, big kills, surges, boss hits | −12 to −9 | Long reverberant tail; music pre-ducked |
| T6 | Ultimates, boss death | −10 to −8 | Rare; music and ambience duck |

- **Loud tiers need a lower crest.** Reaching T5–T6 at a true peak of −1 dBTP needs a soft clip before the limiter (§5.7 step 8). More limiting alone stalled about 1 dB short in tests.
- **Priority and voice budget** (Overwatch threat buckets, Battlefield HDR priority, Diablo IV instance limits). Start limits per group:
  - rapid shot 4–6, heavy shot 2–3, beam 1;
  - hit 6, swarm kill 3–4, big event 1;
  - a global cap of 24–40 voices (24 on phones).

  Steal the oldest voice of the same group, then the lowest priority. Keys and the spoken word have their own pool and are never stolen by combat.
- **Event ducking** (WebAudio has no sidechain, so automate a gain):
  - a P0 event ducks routine combat to about 0.6 (−4.5 dB) within 8–12 ms, holds 120–250 ms and recovers over about 300 ms;
  - music −4 to −6 dB, ambience −6 dB, keys at most −2 dB.
- **The spoken word in learning games.** The word is the lesson and must be heard.
  - Duck music, tails and the reverb return under it.
  - Dip dry weapon hits at most −3 dB. DOOM's team never ducked weapons, not even under dialogue.
  - A game's design doc may set deeper dips; changing it is the owner's call.
- **Mix targets.** Measure on a 2–5 minute capture at top typing speed with a big wave, heavy shots with kills and a boss; never per file.
  - −18 ±2 LUFS integrated, ≤ −1 dBTP, loudness range 10–18 LU.
  - T5 events stand 6–10 LU above the integrated level in short-term windows.
  - Combat peaks sit clearly above the typing sounds.
  - Never run `loudnorm` on a one-shot.

### 5.5 Frequency roles: readable words, full power

| Band | Combat | Keys and word-done sounds |
|---|---|---|
| 30–80 Hz | Sub of heavy shots, explosions and big kills; rapid shots get a short 60–80 Hz punch | None |
| 80–300 Hz | Bodies and booms | Key bodies stay under 800 Hz |
| 300 Hz–1 kHz | Bodies; tails cut 2–4 dB here, where mud builds | |
| 1–4 kHz (speech) | Shot and hit bodies may sound here for their 80–250 ms; tails, loops and the reverb return dip 2–4 dB here and duck under the word | Onset only: down 15 dB within 100 ms (AUDIO_PIPELINE §6.2) |
| 4–10 kHz | Cracks, sizzle, debris, the bright edge of the hit tick | Key clicks |
| Pitched | Hit and kill confirms are tonal, so they separate from noisy key clicks in the same band | Rewards on the game's scale |

- **The space carries the epic feel; the dry hit carries the information.** Tails are high-passed at 150–250 Hz and low-passed at 6–7 kHz, so they never muddy the sub or bury the word.
- **The keyboard band rule is for `key.*` only:** sub under 120 Hz, 1–4 kHz only in the first 30 ms, tails under 1 kHz or over 4 kHz.

### 5.6 Firefly prompt wording

Adobe's guide (checked in the browser on 02/11):
- describe the sound directly, with adjectives and verbs;
- separate traits with commas;
- one sound per prompt; long sentences and chained sounds ("... followed by ...") are its listed don'ts;
- wording sets intensity: its example is "Very loud explosion" against "Soft explosion";
- each generation gives 4 variations.

Rules for combat prompts:
- **Format:** about 12 words at most, comma-separated, one layer per prompt, in English. Template: `[source + action], [size or weight], [character], [space: tail prompts only]`.
- **Never use:** small, quiet, faint, soft, gentle, subtle, restrained, compact, delicate, tiny, thin, muted, light, low-volume, non-fatiguing, "short tail" for the whole sound, frequency specs ("below 900 hertz"), "followed by", or the "an edited sequence of ..., each one followed by a second of silence" template.
- **Use:** very loud, massive, powerful, explosive, violent, heavy, deep, punchy, sharp attack, cinematic, booming, thunderous, saturated, distorted, metallic, echoing, rolling echo, debris.
- **Head stems** ask for "dry, isolated", because the space is added later. **Tail stems** ask for the space and "no transient".
- **Voice guide** for envelope-critical layers: the owner records the shape, for example "mmmm-KRAK" for a rail charge and release, "pshh-BOOM" for a mortar. Firefly follows the timing and energy of the voice.

Example prompts (sci-fi; swap the source nouns for a fantasy game):

| Layer | Prompt |
|---|---|
| Rapid shot HEAD | `plasma bolt shot, sharp electric crack, punchy, dry` |
| Rapid shot BODY | `powerful plasma blaster shot, heavy, dense, punchy` |
| LOW | `deep energy thump, punchy, short` |
| Beam IGNITE | `laser beam ignition, violent electric burst, sharp attack` |
| Beam LOOP | `intense continuous heat ray, roaring plasma, powerful` |
| Beam CRACKLE | `fierce electric arcs crackling, sharp sparks` |
| Beam STOP | `energy beam shutting down, powerful descending whoosh, echoing` |
| Shotgun HEAD | `sci-fi shotgun blast, explosive crack, sharp attack` |
| Shotgun BODY | `heavy energy shotgun blast, massive punch` |
| Rail CHARGE | `railgun charging, rising electric whine, intense` |
| Rail DISCHARGE | `massive railgun shot, violent electric crack, very loud` |
| SUB | `huge sub bass impact, deep pressure wave, cinematic` |
| Mortar LAUNCH | `heavy mortar launch, deep thump, powerful` |
| Mortar TRAVEL | `plasma shell whistling, rising whine` |
| Explosion HEAD | `massive energy explosion, sharp crack, very loud` |
| Explosion BODY | `huge cinematic explosion, deep boom, powerful` |
| Hit | `hard energy impact on armor, sharp, punchy` |
| Kill | `creature shattering, glass and energy burst, punchy` with `short deep impact thump, punchy` |
| Big event | `gigantic explosion, very loud, cinematic` with `massive shockwave, deep sub bass, rumble` |
| TAIL | `gunshot echo in huge empty steel hangar, no transient` or `explosion echoing across vast canyon, rolling echo` |
| Fantasy example | `dragon fire breath, roaring flames, powerful, sharp attack` |

### 5.7 Offline layering chain

Tested on ffmpeg 9.0.2 (Homebrew) on 02/11 with stand-in layers. The tests checked syntax, timing and levels, not taste. sox is not installed on the Mac mini, so the sox lines are untested. Run the commands in bash, because zsh does not split `$FF`.

**Gotchas:**
- **`alimiter`** defaults to `level=1`, which pushes the output to 0 dBFS: always set `level=0`. It limits sample peaks only, so run it at 192 kHz (`aresample=192000,alimiter=...,aresample=48000`) to keep the true peak under −1 dBTP.
- **`afir` levels:** `dry` and `wet` are the input and output gains, not a mix, and `dry=0` is silence. The output is wet only.
- **`afir` length:** the output is as long as the input, so pad the input with `apad=pad_dur=<IR length>`.
- **`afir` normalisation:** `irnorm` swings the wet level by tens of dB. Set the tail level by measurement, never by a fixed number. A fixed `irnorm=1, volume=0.2` left a tail near −60 dBFS, which is inaudible.
- **`amix`** divides its inputs by default: use `normalize=0`.
- **`asoftclip`:** `oversample=4` cut the level by 5–6 dB on 9.0.2. Leave it off, or measure after it.
- **`loudnorm`:** never on a one-shot. Short files miss the target or measure −inf.
- **Codecs:** this build has no libsoxr, rubberband or libvorbis. Encode the game's OGG with libopus or another tool.

1. **Measure** momentary max, true peak and crest:

   ```bash
   mmax() { ffmpeg -hide_banner -nostats -v verbose -i "$1" -af "apad=pad_dur=3,ebur128=framelog=verbose" -f null - 2>&1 | grep -o ' M: *-\?[0-9.]*' | awk '{print $2}' | sort -g | tail -1; }
   tp() { ffmpeg -hide_banner -nostats -i "$1" -af "apad=pad_dur=3,ebur128=peak=true" -f null - 2>&1 | grep -A1 "True peak:" | grep -o 'Peak: *-\?[0-9.inf]*' | awk '{print $2}'; }
   crest() { ffmpeg -hide_banner -nostats -i "$1" -af astats -f null - 2>&1 | grep -A40 Overall | awk -F: '/Peak level dB/{p=$2}/RMS level dB/{r=$2}END{printf "%.1f\n", p-r}'; }
   ```

2. **Prepare each layer for its job** (the bands are start values):

   ```bash
   FF="ffmpeg -hide_banner -loglevel error -y"
   $FF -i head.wav -af "aresample=48000,highpass=f=1800,afade=t=out:st=0.04:d=0.03,atrim=0:0.08" -ac 2 L_head.wav
   $FF -i body.wav -af "aresample=48000,highpass=f=90,equalizer=f=300:t=q:w=1.2:g=-3,lowpass=f=9000,afade=t=out:st=0.12:d=0.10,atrim=0:0.25" -ac 2 L_body.wav
   $FF -i sub.wav -af "aresample=48000,lowpass=f=140,highpass=f=30,afade=t=out:st=0.08:d=0.15,atrim=0:0.25,pan=stereo|c0=0.5*c0+0.5*c1|c1=0.5*c0+0.5*c1" L_sub.wav
   ```

   Weight from a bright source: pitch the body down an octave (`asetrate=48000*0.5,aresample=48000,lowpass=f=150`), or three semitones tape-style (`asetrate=48000*0.8409,aresample=48000`; the sound gets longer). A synthesised falling sine is allowed as the sub layer of a real file:

   ```bash
   $FF -f lavfi -i "aevalsrc='0.9*sin(2*PI*(45*t+65*0.03*(1-exp(-t/0.03))))*exp(-t/0.12)':s=48000:d=0.45" -af "afade=t=in:d=0.002,afade=t=out:st=0.38:d=0.07" sub.wav
   ```

3. **Stack with offsets, keep the punch, cap the true peak.** The head starts at 0, the body at +2 ms and the sub at +4 ms. A parallel compressor with a 25 ms attack lets the crack through and thickens the body; then a tanh soft clip and a limiter at 192 kHz:

   ```bash
   $FF -i L_head.wav -i L_body.wav -i L_sub.wav -filter_complex \
   "[1]adelay=2|2[b];[2]adelay=4|4[s];[0][b][s]amix=inputs=3:weights=1 0.9 1:normalize=0:duration=longest,asplit=2[x][y];\
   [y]acompressor=threshold=0.06:ratio=8:attack=25:release=90:makeup=3[c];[x][c]amix=inputs=2:weights=1 0.6:normalize=0,\
   asoftclip=type=tanh:threshold=0.85,aresample=192000,alimiter=limit=0.84:attack=1:release=40:level=0,aresample=48000[o]" \
   -map "[o]" shot_dry.wav
   ```

   Test: 0.25 s, −1.5 dBTP, momentary max −12.8. With mechanics, add a fourth input at `adelay=0` and shift the others by +5–10 ms.

4. **Make our own impulse response.** It is our own work, so it needs no licence. Two pink-noise seeds give stereo width; an exponential decay, a darker top and early taps give the slap of far steel walls:

   ```bash
   $FF -filter_complex "anoisesrc=d=2.5:c=pink:a=0.5:r=48000:seed=7[l];anoisesrc=d=2.5:c=pink:a=0.5:r=48000:seed=11[r];\
   [l][r]join=inputs=2:channel_layout=stereo,afade=t=out:st=0:d=2.5:curve=exp,lowpass=f=7000,aecho=0.9:0.6:95|180|310:0.45|0.3|0.2" -t 2.5 ir_own.wav
   ```

   Use 3–4 s for a vaster space and for big events. A measured CC0 IR (§5.8) sounds more real; try both.

5. **Bake the tail a set number of LU under the dry shot.** The tail gets a 25 ms pre-delay, a 200 Hz–6.5 kHz band and a level set by measurement: 8 LU under for routine shots, 6 LU under for big events.

   ```bash
   IRLEN=$(ffprobe -v error -show_entries format=duration -of csv=p=0 ir_own.wav); BELOW=8
   $FF -i shot_dry.wav -i ir_own.wav -filter_complex "[0]apad=pad_dur=$IRLEN,adelay=25|25,highpass=f=200,lowpass=f=6500[s];[s][1]afir=irnorm=2[w]" -map "[w]" -c:a pcm_f32le tail_raw.wav
   G=$(awk -v d="$(mmax shot_dry.wav)" -v w="$(mmax tail_raw.wav)" -v b=$BELOW 'BEGIN{printf "%.2f",(d-b)-w}')
   $FF -i tail_raw.wav -af "volume=${G}dB,areverse,silenceremove=start_periods=1:start_threshold=-70dB,areverse,afade=t=out:st=$(awk -v l=$IRLEN 'BEGIN{print l-0.4}'):d=0.4" -c:a pcm_s24le shot_tail.wav
   ```

   Ship the tail as its own file (`<id>.tail`), so the code can cap tail voices and duck tails apart from the dry hit.

6. **Make a listening copy:** dry plus tail, with the tail ducked under the hit so it blooms after it:

   ```bash
   $FF -i shot_dry.wav -i shot_tail.wav -filter_complex "[0]apad=pad_dur=$IRLEN,asplit=2[d][k];[1][k]sidechaincompress=threshold=0.05:ratio=4:attack=2:release=250[w];\
   [d][w]amix=inputs=2:normalize=0:duration=longest,aresample=192000,alimiter=limit=0.84:level=0,aresample=48000,areverse,silenceremove=start_periods=1:start_threshold=-70dB,areverse[o]" \
   -map "[o]" -c:a pcm_s24le shot_full.wav
   ```

   Test: 1.6 s, −1.6 dBTP, momentary max −12.7, the tail at +500 ms about 19 dB under the peak. For a slapback from far walls, add `aecho=0.8:0.7:180|330:0.35|0.2` inside any graph.

7. **Make a pre-verb swell for a charge.** It ends exactly where the shot starts:

   ```bash
   $FF -i shot_dry.wav -i ir_own.wav -filter_complex "[0]areverse,apad=pad_dur=$IRLEN,highpass=f=200[r];[r][1]afir=irnorm=2,areverse,silenceremove=start_periods=1:start_threshold=-60dB,afade=t=in:d=0.3:curve=exp,aresample=192000,alimiter=limit=0.7:level=0,aresample=48000[o]" -map "[o]" -c:a pcm_s24le preverb.wav
   ```

8. **Set the tier** with a true-peak-safe limiter. For T5–T6, drive the sound into a soft clipper first, then set the level the same way:

   ```bash
   T=-12   # the tier's momentary max
   G=$(awk -v m="$(mmax shot_full.wav)" -v t=$T 'BEGIN{printf "%.2f",t-m}')
   $FF -i shot_full.wav -af "volume=${G}dB,aresample=192000,alimiter=limit=-1.3dB:attack=0.5:release=40:level=false,aresample=48000" -c:a pcm_s24le shot_T4.wav
   # T5-T6: clip first, then repeat the two lines above on clipped.wav with T=-9
   $FF -i shot_full.wav -af "volume=6dB,asoftclip=type=tanh" -c:a pcm_f32le clipped.wav
   ```

   Test: a −12 target gave −12.1 at −1.2 dBTP. A −10 target without clipping stalled at −10.6. With +6 dB into the tanh clip first, a −9 target gave −9.5 at −1.4 dBTP.

9. **Make variants:** 3–5 per head and body; hit and kill confirms stay nearly fixed.

   ```bash
   for st in -1.5 -0.75 0 0.75 1.5; do r=$(awk -v s=$st 'BEGIN{printf "%.5f",2^(s/12)}')
     $FF -i shot_dry.wav -af "asetrate=48000*$r,aresample=48000,aresample=192000,alimiter=limit=0.84:level=0,aresample=48000" -c:a pcm_s24le "shot_dry_$st.wav"; done
   ```

   At run time, add a random ±60 cents on heads and bodies.

**sox equivalents** (untested here; syntax from the Debian sox(1) manual):
- wet-only reverb stem: `sox dry.wav wet.wav gain -3 pad 0 2.5 reverb -w 70 40 100 100 25 -4` (reverberance, HF damping, room scale, stereo depth, pre-delay ms, wet gain dB);
- saturation: `overdrive 8 20`;
- pitch without changing length: `pitch -300` (−3 semitones); tape-style: `speed 0.84`;
- peak normalise: `gain -n -1.5`; simple limiter: `gain -l 6`; fades: `fade q 0.002 0 0.3`.

### 5.8 Reverb: baked tails plus an in-game send

- **Use both, not one.**
  - DOOM 2016 baked a reverb layer per space into each weapon, Halo Infinite authored tails per space, and Call of Duty plays reflections where the sound meets the world.
  - A game with one main space bakes a tail layer per weapon (§5.7 step 5, or a Firefly tail take, high-passed) and adds a light shared send that glues every sound into the same place.
  - A game with several spaces swaps the tail layers by space.
- **The in-game send:** one shared convolver per space, because its cost grows with the IR's length.
  - Chain: send → 20–30 ms pre-delay → high-pass 150–250 Hz → ConvolverNode → low-pass 6–7 kHz → return.
  - Start send levels: rapid shot 0.08–0.12, heavy shot 0.2–0.3, explosion and big kill 0.35–0.45, hit 0.05, swarm kill 0.1, keys and UI 0.
  - The return ducks under the spoken word.
  - On low tiers, bake tails at load with an OfflineAudioContext instead.
- **WebAudio facts** (W3C spec, and measured in Chromium):
  - DynamicsCompressorNode adds automatic makeup gain, `(1 / curve(1.0))^0.6`.
  - It has a fixed 6 ms look-ahead and no sidechain input.
  - Its defaults are threshold −24, knee 30, ratio 12, attack 3 ms, release 250 ms.
  - ConvolverNode normalises its IR by default and takes a 1, 2 or 4-channel buffer at the context's sample rate (`decodeAudioData` resamples).
- **The mix chain:**
  - No fast compressor on a combat bus.
  - Each combat bus gets a slow-attack glue (start: threshold −18, knee 6, ratio 3, attack 25 ms, release 150 ms). It let a burst's first 5 ms through 3.9 dB above the rest.
  - A gain after it undoes the automatic makeup: about 0.6 × |threshold| × (1 − 1/ratio) dB, so −7.2 dB for −18/3. The old −12/8 glue predicted 6.3 dB and measured +5.1. Measure it in an OfflineAudioContext.
  - One master safety limiter that rarely works (start: threshold −3, knee 0, ratio 20, attack 1 ms, release 80 ms), then a trim, so the gameplay capture stays at or under −1 dBTP.
  - Keys and UI bypass the combat compressor.

  ```ts
  // One shared space per scene; ir is at ctx.sampleRate.
  const space = new GainNode(ctx);
  const spaceReturn = new GainNode(ctx, { gain: 0.5 }); // ducks under the spoken word
  space.connect(new DelayNode(ctx, { delayTime: 0.025 }))
    .connect(new BiquadFilterNode(ctx, { type: "highpass", frequency: 180 }))
    .connect(new ConvolverNode(ctx, { buffer: ir }))
    .connect(new BiquadFilterNode(ctx, { type: "lowpass", frequency: 6500 }))
    .connect(spaceReturn).connect(master);

  // Each combat bus: level -> duck -> slow glue -> undo makeup -> master, plus a send.
  function combatBus(sendLevel: number) {
    const level = new GainNode(ctx), duck = new GainNode(ctx);
    const glue = new DynamicsCompressorNode(ctx, { threshold: -18, knee: 6, ratio: 3, attack: 0.025, release: 0.15 });
    const unMakeup = new GainNode(ctx, { gain: 10 ** (-0.6 * 18 * (1 - 1 / 3) / 20) }); // about -7.2 dB; measure
    level.connect(duck).connect(glue).connect(unMakeup).connect(master);
    duck.connect(new GainNode(ctx, { gain: sendLevel })).connect(space);
    return { input: level, duck };
  }

  // Event ducking without cancelAndHoldAtTime.
  function duck(p: AudioParam, depthDb: number, at: number, hold = 0.15, attackTc = 0.008, releaseTc = 0.13) {
    p.cancelScheduledValues(at);
    p.setValueAtTime(p.value, at);
    p.setTargetAtTime(10 ** (depthDb / 20), at, attackTc);
    p.setTargetAtTime(1, at + hold, releaseTc);
  }
  ```

- **Impulse responses** (licences read on each page on 02/11):

  | Source | Licence | Use |
  |---|---|---|
  | Our own IR (§5.7 step 4) | Our work, no licence | First choice for a sci-fi or fantasy space |
  | [Freesound, Tim_Verberne "Impulse Responses" pack](https://freesound.org/people/Tim_Verberne/packs/30310/): tunnel, parking garages, mountain ranges, ravines; digitally modelled for game sound | CC0 (checked on item pages) | Garage or tunnel for steel and concrete; mountain or ravine for huge distance |
  | Freesound [djericmark Long Parking Garage](https://freesound.org/people/djericmark/sounds/732457/), [Fission9 Artificial Cave](https://freesound.org/people/Fission9/sounds/455295/), [LewisEmmott5 Large Stairwell](https://freesound.org/people/LewisEmmott5/sounds/732025/), [Sadiquecat industrial chimney](https://freesound.org/people/Sadiquecat/sounds/861997/) | CC0 | Real measured spaces |
  | [University of York OpenAIR mirror](https://sites.google.com/york.ac.uk/music-technology-masterclass/home/1-acoustics): Hoffmann Lime Kiln, R1 Nuclear Reactor Hall, Railway tunnel, Terry's Factory Warehouse | CC BY 4.0; credit "OpenAIR" on the Credits page | Vast halls and tunnels for big events. The main OpenAIR site returned "Account Suspended" |
  | Voxengo, EchoThief, MIT IR Survey, Sonic Palimpsest, Airwindows | Custom, or no licence on the source's own page | Not used. A custom licence is the owner's decision ([licences](licences.md) §3) |

### 5.9 Sources, the stop rule and CC0 libraries

- **Firefly first, for ingredients.** Write one prompt per layer; each generation gives 4 variations. Pick by the measurements first, then by ear at matched loudness.
- **CC0 libraries give raw layers, never the finished sound.** They are mostly retro or small. Use them:
  - from the start, for what AI does badly: heads under 50 ms, mechanics, metal clacks, debris;
  - as the next source when the stop rule fires.

  Checked: [Kenney Sci-fi Sounds](https://kenney.nl/assets/sci-fi-sounds) and [Impact Sounds](https://kenney.nl/assets/impact-sounds) (CC0); OpenGameArt [The Free Firearm Sound Library](https://opengameart.org/content/the-free-firearm-sound-library) and [50 CC0 Sci-Fi SFX](https://opengameart.org/content/50-cc0-sci-fi-sfx) (CC0); [Lentikula Sci-Fi Weapon Shots](https://lentikula.itch.io/sci-fi-weapon-shots-sfx-freecc0) (CC0, 48 kHz/24-bit, made without AI); Freesound items filtered to CC0 or CC-BY (record each item's AI-training preference as well). Sonniss stays out of every AI step (§4).
- **The stop rule (§4) counts per layer id.** At most 3 prompt rounds. After 3 rounds with fewer than 3 takes passing the gates, or after two owner rejections in a row, change the source in this order:
  1. a CC0 layer;
  2. our own processing: pitch-down, saturation, a synthesised sub inside a real file;
  3. our own recording: a voice guide or foley;
  4. the "record or buy later" list.
- **Pilot before the set.** Build one rapid shot, one heavy shot, the hit, the kill and one space first. The owner listens blind in the real play mix before the other weapons are made.

### 5.10 Acceptance for combat sound

The machine checks flag problems; they do not choose (§3).
- Every file is at or under −1 dBTP, with its momentary max inside its tier (§5.4).
- Shot and hit heads have a crest (peak minus RMS) of 12 dB or more before tiering. T5–T6 keep 10 dB or more after clipping (start).
- T4–T6 carry at least 25 % of their energy under 150 Hz.
- T4–T6 listening copies still carry energy at +500 ms, no lower than −30 dB under their peak. Tail stems are high-passed at 150 Hz or more.
- The mix capture meets §5.4. AUDIO_PIPELINE test D (density) holds, and test C (the spoken word) holds with the ducking of §5.4.
- The ear decides: the Audio Lab gates, then the owner blind on the Listening Board in the real play mix. Each sound needs 8.5 or more for power, punch and space as well as fit.

### 5.11 Sources read on 02/11/2026

- [Halo Infinite, Inside Infinite, March 2021](https://www.halowaypoint.com/news/inside-infinite-march-2021): Impact, Mech, Sci-fi and Tails layers; tails per space; a sharp attack and quick decay instead of long, compressed assets; not every sound over the top; threat order sets each gun's volume.
- [DOOM 2016, ADSR Q&A](https://www.adsrsounds.com/news/the-sound-design-of-doom-exclusive-qa/): weapons never ducked; baked reverb layer per space; the Gauss pre-impulse; distortion.
- [Battlefield: Bad Company HDR audio, GDC 2009 slides](https://media.gdcvault.com/gdc09/slides/GDC09_Clerwall_HDRAudio.pdf): every sound matters, but not at the same time; HDR is not compression; priority from a base value and loudness.
- [Overwatch, GDC 2016 slides](https://media.gdcvault.com/gdc2016/Presentations/Lawlor_Neumann_Overwatch_Play_by_Sound.pdf): threat buckets, culling, indoor and outdoor space, quad delay, minimal variation for quick reactions.
- [Diablo IV, Blizzard, October 2021](https://news.blizzard.com/en-gb/article/23731236/diablo-iv-quarterly-updateoctober-2021): a clean but punchy mix, random playback, instance limits, skills built from cast, travel and impact parts, reverbs and echoes.
- [Call of Duty: Modern Warfare (2019)](https://blog.activision.com/call-of-duty/2019-07/Modern-Warfare-Initial-Intel-Creating-an-Orchestra-of-Incredible-Audio-Effects-Weapon-Sounds-in-Call-of-Duty-Modern-Warfare): reflections where sound meets the world; big echoes in open areas.
- [Apex Legends audio update, October 2025](https://www.ea.com/games/apex-legends/apex-legends/news/showdown-audio-update): multiband sidechain, voice priority, a focused mix, a threat system, snapshots.
- [Destiny 2, Inverse](https://www.inverse.com/gaming/destiny-2-sounds-lorentz-driver-stasis): pop, body and tail; punchy, big, explosive.
- [Mark Kilborn, Pro Sound Effects](https://blog.prosoundeffects.com/how-to-sound-design-first-person-shooter-gunshot-sound-effects-with-mark-kilborn) and [Chuck Russom, Designing Sound](https://designingsound.org/2010/04/chuck-russom-special-gun-sound-design/): gun layer models.
- [HDR audio in Wwise, Designing Sound](https://designingsound.org/2013/06/21/finding-your-way-with-high-dynamic-range-audio-in-wwise/): loudness as priority.
- Adobe Firefly: [writing sound effect prompts](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-audio/writing-effective-text-prompts-for-sound-effects-generation.html), [voice to sound effects](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-audio/voice-to-sound-effects.html).
- WebAudio: [MDN DynamicsCompressorNode](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode), [MDN ConvolverNode](https://developer.mozilla.org/en-US/docs/Web/API/ConvolverNode), [Paul Adenot's Web Audio performance notes](https://padenot.github.io/web-audio-perf/).
- Loudness: [Audiokinetic, mastering a game](https://audiokinetic.com/en/mastering-a-game-with-wwise-part1) (Sony: consoles −24 LUFS ±2, mobile −18, −1 dBTP, loudness range up to 20 LU).
