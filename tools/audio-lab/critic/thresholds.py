"""Numbers of the critic, with the plan section they come from (docs/games/AUDIO_PIPELINE.md).

L1 numbers are the exact §4.3.1 thresholds. L1b and L2 numbers are starting points
(§4.3.2, §4.3.3: "chưa kiểm chứng") to be recalibrated with owner ratings (§4.6).
"""
from __future__ import annotations

SCHEMA_FILE = "audiolab.critic.file/1"
SCHEMA_BATCH = "audiolab.critic.batch/1"
VERSION = "0.1.0"

# §4.3.1 L1 hygiene gate.
L1 = {
    "clip_level": 0.999,           # |x| >= 0.999 FS ...
    "clip_run": 3,                 # ... on 3 consecutive samples = clipped
    "flat_run": 4,                 # 4 consecutive samples with the same magnitude ...
    "flat_min_dbfs": -20.0,        # ... above -20 dBFS = flat top
    "flat_guard_step": 1.2e-4,     # ours: ignore smooth crests (entry and exit step < ~4 LSB at 16 bit)
    "plateau_jump_rel": 0.95,      # ours: a run entered and left by a jump >= ~its height is a drawn square
    "flat_near_peak": 10 ** (-1.0 / 20),   # ours: a flat run is a clip ceiling only within 1 dB of the channel peak
    # ours (deviation from §4.3.1, see hygiene.clip_scan): float/lossy files count only truly flat
    # full-scale runs (decoder overshoot is not clipping); 8-bit PCM skips the flat-top test.
    "dc_max": 0.001,               # 0.1 % FS
    "true_peak_max_dbtp": -1.0,
    "duration_tol": 0.20,          # vs spec card
    "tail_floor_db": -60.0,        # decays to -60 dB (re peak) before the end ...
    "tail_fade_min_ms": 5.0,       # ... or ends with a fade of >= 5 ms
    "tail_fade_drop_db": 12.0,     # ours: what counts as a fade (drop over the last 5 ms)
    "loop_window_ms": 50.0,        # last 50 ms vs first 50 ms
    "loop_jump_max_dbfs": -40.0,   # sample jump at the seam (beyond the file's normal P95 step)
    "loop_rms_max_db": 1.0,
    "loop_centroid_max_rel": 0.10,
    "sample_rate": 48000,
    "stereo_corr_min": 0.0,        # stereo files: correlation must be > 0
    "music_bar_tol_ms": 1.0,
    "silent_dbfs": -60.0,          # ours: nothing above -60 dBFS = silent file
    "head_level_dbfs": -60.0,      # head silence = time before the first sample above -60 dBFS
}

# §4.3.2 L1b model-artefact flags (flag only in batch 1).
L1B = {
    "pre_echo_window_ms": 30.0,
    "pre_echo_guard_ms": 2.0,      # ours: skip the 2 ms right before the onset (the attack itself)
    "pre_echo_max_db": -40.0,      # energy re peak
    "smear_band": (2000.0, 16000.0),   # ours: the crack layer whose rise time we time
    "smear_min_rel_db": -30.0,     # ours: only when that layer peaks within 30 dB of the full band
    "smear_attack_max_ms": 5.0,    # ours: crack rise above min(5 ms, group attack limit) = smeared
    "smear_pre_ms": 2.0,           # ours: the crack is looked for from 2 ms before the onset ...
    "smear_window_ms": 50.0,       # ... to 50 ms after it (later HF events are tail, not attack)
    "hiss_band": (8000.0, 16000.0),
    "hiss_flatness_min": 0.35,     # ours (no refs): tail flatness high ...
    "hiss_flatness_rise": 0.10,    # ... and rising vs the body ...
    "hiss_share_rise_db": 6.0,     # ... and the 8-16 kHz share rising
    "hiss_abs_floor_dbfs": -90.0,  # ignore dither-level hiss
    "swirl_band": (4000.0, 16000.0),
    "wobble_max_cents": 20.0,
    "stereo_corr_min": 0.3,
    "mono_loss_max_db": 3.0,
    "noise_floor_max_dbfs": -60.0,
    "refs_min": 3,                 # refs of the same group needed for P90-based flags
    "refs_pct": 90.0,
    # ours (batch 0b review), loops only: events that make a short loop recognisable on repeat
    "loop_knock_db": 10.0,         # 10 ms level over the 1 s running median (above 100 Hz)
    "loop_knock_max_s": 0.15,      # ... and short (a gust is not a knock)
    "loop_chirp_prom_db": 24.0,    # one bin in 1.5-9 kHz over the band median (tonal, bird-like)
    "loop_chirp_rise_db": 6.0,     # ... while the band rises over its running median
    "loop_band_range_db": 8.0,     # a 1/6-octave band (1.5-12 kHz) whose level re the bed moves this much
    "loop_band_over_db": 3.0,      # ... more than the median band moves (it comes and goes on its own)
    "loop_knock_low_band": (20.0, 200.0),   # ours (review 2): a wind-mic thump hidden under the full band
    "loop_knock_low_min_s": 0.03,  # ... lasts >= 30 ms (a 10 ms low-band level jitters by chance)
    "loop_tone_rise_db": 15.0,     # tonal event (4096-pt STFT bin): over its own 1 s running median ...
    "loop_tone_prom_db": 12.0,     # ... over the +-500 Hz neighbours (+-100 Hz excluded) ...
    "loop_tone_band_rise_db": 4.0,  # ... while its +-1 kHz band rises (H s2001: 3.93 kHz, 18/13/5 dB)
    "comb_prom_db": 6.0,           # decoder comb (k x 44100/256 Hz above 10 kHz): median line prominence
    "comb_level_min_db": -75.0,    # ... only when the lines are not far under the loop's spectral peak
    "near_mono_corr": 0.98,        # stereo card, but the channels are (near) identical ...
    "near_mono_side_db": -10.0,    # ... or the side channel sits >= 10 dB under the mid (review 2: corr 0.886)
    # ours (review 2): channel balance of stereo files, broadband and per band (20-150, 150-1k, 1-4k, 4-16k)
    "lr_balance_max_db": 1.5,
    "lr_band_balance_max_db": 3.0,
    # ours (review 2): two onsets in one shot: the >= 2 kHz band peaks, dips and comes back
    "double_onset_after_ms": (12.0, 40.0),
    "double_onset_db": -6.0,       # the second peak within 6 dB of the first ...
    "double_onset_rise_db": 4.0,   # ... and >= 4 dB over the dip between them ...
    "double_onset_dip_db": -6.0,   # ... after the band fell >= 6 dB under the first (a clank's beating is not)
    "double_onset_min_rel_db": -30.0,   # only when that band peaks within 30 dB of the full band
}

# §4.3.3 / §4.4 L2 and learned-layer rules.
L2 = {
    "short_s": 0.3,                # §4.4: < 300 ms -> learned layers score a 3-4 s repetition
    "rep_min_s": 3.0,
    "rep_max_s": 4.0,
    "rep_plays": 10,
    "lufs_m_pad_s": 0.4,           # LUFS-M max after padding to 0.4 s
    "lufs_block_short_s": 0.1,     # pyloudnorm block_size for short sounds (§3.4)
    "refs_min": 5,                 # §4.3.3: P10-P90 of approved refs replace the targets
    "speaker_hpf_hz": 200.0,       # test F small speaker
    "phone_hpf_hz": 400.0,
    "psycho_max_s": 2.0,           # MoSQITo sharpness on at most the first 2 s of the active part
    "roughness_max_s": 0.5,        # roughness (slow) on the first 0.5 s only
    "norm_lufs_m": -20.0,          # §4.3.3 common level; psychoacoustics run at this level
}

LEARNED = {
    "ast_low_conf": 0.10,          # §4.4: top confidence < 0.1 -> "hard to recognise"
    "ast_expected_min": 0.05,
    "ast_forbid_min": 0.20,        # ours: a forbidden label counts at top-1 or at >= 0.2 in the top-5
    "clap_topk": 3,
    "ref5": 5,                     # §4.5 / L5: >= 5 approved refs
    "ref10_dirty": 10,             # §4.4: dirty families get audiobox at >= 10
    "kad_min": 20,                 # §4.4: KAD for the whole set at >= 20 refs
}

# §4.5 weights per stage: (L2, L3, L4, L5).
WEIGHTS = {
    "batch1": (0.6, 0.3, 0.1, 0.0),
    "batch1-dirty": (0.9, 0.0, 0.1, 0.0),
    "ref5": (0.45, 0.25, 0.1, 0.2),
    "ref5-dirty": (0.45, 0.0, 0.1, 0.2),
}
RANK_GAP_ASK = 3                   # §4.5: L2 and L3 ranks differ by more than 3
TOP_READ = 6                       # §4.5: Claude reads the cards of the top 6
PROBE_RATE = 0.30                  # §4.6: probe at about 30 % of ids
Z_FLOOR = {"L2": 0.05, "L3": 0.25, "L4": 0.5, "L5": 0.02}   # ours: std floor for z-scores
