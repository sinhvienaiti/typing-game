import pytest

from sampler.naming import midi_to_note, note_to_midi, parse_sample_name
from sampler.sfz import parse_sfz


@pytest.mark.parametrize("name, desc, note, dyn, vel, rr, mic", [
    ("EWHarp_Normal_A#1_v2_RR1.wav", "ewharp-normal", "A#1", None, 2, 1, None),
    ("B1_f_1.wav", "", "B1", "f", None, 1, None),
    ("b2_mf_1.wav", "", "b2", "mf", None, 1, None),
    ("sus_A#3_r01_main.wav", "sus", "A#3", None, None, 1, "main"),
    ("Anvil_Hit1_v1_rr1_Mid.wav", "anvil-hit1", None, None, 1, 1, "mid"),
    ("gong_2_f.wav", "gong-2", None, "f", None, None, None),
    ("gong_scrape_mf.wav", "gong-scrape", None, "mf", None, None, None),
    ("hit_light2.mp3", "hit", None, "p", None, 2, None),
    ("hit_full2_loudest_ST.mp3", "hit", None, "fff", None, 2, "st"),
    ("FX_01.wav", "fx-01", None, None, None, None, None),
    ("Gliss_Dwn_Med_ff_1.wav", "gliss-dwn-med", None, "ff", None, 1, None),
    ("wood_click3_vl2.wav", "wood-click3", None, None, 2, None, None),
    ("TB_hit_C4_v2_1.wav", "tb-hit", "C4", None, 2, 1, None),
    ("Marimba_hit_Outrigger_B2_loud_01.wav", "marimba-hit-outrigger", "B2", "f", None, 1, None),
    ("Xylo_Medium_C4_ff_01_far.wav", "xylo-medium", "C4", "ff", None, 1, "far"),
    ("Triangle3-HitFM_v1_rr2_Sum.wav", "triangle3-hitfm", None, None, 1, 2, "sum"),
    ("LDFlute_susNV_A3_v1_1.wav", "ldflute-susnv", "A3", None, 1, 1, None),
])
def test_parse_library_names(name, desc, note, dyn, vel, rr, mic):
    n = parse_sample_name(name)
    assert (n.descriptor, n.note, n.dyn, n.vel_layer, n.rr, n.mic) == (desc, note, dyn, vel, rr, mic)


def test_note_numbers():
    assert note_to_midi("C4") == 60
    assert note_to_midi("A#1") == 34
    assert note_to_midi("Bb2") == note_to_midi("A#2") == 46
    assert note_to_midi("b2") == 47
    assert note_to_midi("Cs4") == 61
    assert note_to_midi("72") == 72
    assert midi_to_note(47) == "B2"
    with pytest.raises(ValueError):
        note_to_midi("H2")


def test_layer_rank_orders_dynamics_and_v_numbers():
    soft, loud = parse_sample_name("x_C4_pp_rr1"), parse_sample_name("x_C4_ff_rr1")
    assert soft.layer_rank < loud.layer_rank
    assert parse_sample_name("x_C4_v1").layer_rank < parse_sample_name("x_C4_v3").layer_rank


SFZ_VSCO = r"""<control>
default_path=Woodwinds\Flute\susNV\
<global>
ampeg_release=0.7
<group> //Begin Group
<region>
sample=LDFlute_susNV_A3_v1_1.wav
lokey=67
hikey=70
pitch_keycenter=69
lovel=0
hivel=62
volume=12
<region> sample=LDFlute_susNV_A3_v3_1.wav pitch_keycenter=a4 lovel=63 hivel=127
"""

SFZ_VCSL = """// Generation Options: --notuning
<group>
ampeg_release=0.300000
<region>
lovel=0
hivel=65
sample=Dan Tranh/Normal/B1_mf_1.wav
pitch_keycenter=47
offset=57
"""


def test_sfz_default_path_inheritance_and_note_names(tmp_path):
    regions = parse_sfz(tmp_path / "FluteSusNV.sfz", SFZ_VSCO)
    assert len(regions) == 2
    r0, r1 = regions
    assert r0.sample == tmp_path / "Woodwinds/Flute/susNV/LDFlute_susNV_A3_v1_1.wav"
    assert (r0.keycenter, r0.get("lovel"), r0.get("hivel"), r0.get("volume")) == (69, 0, 62, 12.0)
    assert r0.get("ampeg_release") == 0.7            # inherited from <global>
    assert r1.keycenter == 69 and r1.get("lovel") == 63


def test_sfz_sample_path_with_spaces(tmp_path):
    (r,) = parse_sfz(tmp_path / "Chordophones/Zithers/Dan Tranh - Normal.sfz", SFZ_VCSL)
    assert r.sample == tmp_path / "Chordophones/Zithers/Dan Tranh/Normal/B1_mf_1.wav"
    assert (r.keycenter, r.get("offset"), r.get("ampeg_release")) == (47, 57, 0.3)
