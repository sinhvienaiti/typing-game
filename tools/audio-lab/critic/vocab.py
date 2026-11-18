"""CLAP vocabularies (§4.4: 15-25 labels per game), material contrast pairs and AST expectations.

Labels are English prompts (CLAP was trained on English captions). Specs may override.
"""
from __future__ import annotations

GENERIC = [
    "a sci-fi laser gun shot", "a big explosion", "a metal impact clang", "a wooden hit knock",
    "a bronze bell strike", "a body punch hit", "a fire breath whoosh", "a low engine hum loop",
    "an industrial machine drone", "a user interface click", "a keyboard key click",
    "a gun shot", "an animal roar", "an alarm siren", "a magic chime", "an arrow shot from a bow",
    "a crowd of monsters dying", "a forest ambience",
]

GAMES = {
    "dragon-hold": [
        "a dragon breathing fire, roaring flame whoosh", "a dragon roar", "a fire impact with crackling embers",
        "an arrow shot from a bow", "an arrow hitting wood", "a pine cone bomb explosion", "a monster growl",
        "a creature footstep on leaves", "a forest ambience with birds and wind", "a small bell chime",
        "a harp pluck", "a wooden key click", "a user interface click", "a metal sword hit", "a magic sparkle",
        "a goblin dying", "a heavy body thump", "a war horn", "a gas stove hiss", "a crackling campfire",
    ],
    "typing-defense": [
        "a hollow bamboo knock", "a wooden block hit", "a bronze bell strike", "a gong hit",
        "a plucked zither note", "paper rustling", "an ink splash puff", "a frame drum hit",
        "an arrow released from a bow", "a village ambience with insects at night", "a bamboo flute note",
        "a firecracker", "a metallic sci-fi clang", "a user interface click", "a coin clink",
        "a villager calling out", "a wooden door creak", "a rooster crow",
    ],
    "typing-survival": [
        "a heavy industrial autocannon shot", "a thin toy laser pew", "a metal impact clang",
        "an electric arc zap", "an alarm siren", "a big explosion", "an industrial machine drone",
        "a steel door slam", "a robot servo whir", "an alien creature screech", "a squishy alien death",
        "a power-up chime", "a mechanical keyboard click", "a user interface beep", "metal debris rattle",
        "a deep rumble", "a gas leak hiss", "a sci-fi laser gun shot",
    ],
    "space-typing": [
        "a sci-fi laser gun shot", "a big explosion", "a spaceship engine hum", "a shield impact",
        "a user interface click", "a power-up chime", "a missile launch", "an alarm siren",
        "a metal impact clang", "an electric zap", "a keyboard key click", "a warp whoosh",
        "a robot voice beep", "a deep space ambience", "debris hitting a hull",
    ],
}

# §4.4 examples: (wanted material, wrong material) per game and group.
CONTRAST = {
    ("typing-defense", "hit_small"): [("a hollow bamboo knock", "a metallic sci-fi clang")],
    ("typing-defense", "hit_heavy"): [("a hollow bamboo knock", "a metallic sci-fi clang")],
    ("typing-defense", "ui"): [("a hollow bamboo knock", "a metallic sci-fi clang")],
    ("typing-survival", "shot_gun"): [("a heavy industrial autocannon shot", "a thin toy laser pew")],
    ("dragon-hold", "whoosh"): [("a dragon's roaring fire breath", "a gas stove hiss")],
}

# Groups where CLAP was right in the PoC (A.4): only these get a default expected label.
GROUP_EXPECTED = {
    "explosion": ["a big explosion"],
}

PAM_PAIR = ("the sound is clear and clean.", "the sound is noisy and with artifacts.")

# AST: expected labels only for real-world categories (§4.4).
AST_EXPECTED = {
    "explosion": ["Explosion", "Boom", "Burst, pop", "Fireworks", "Firecracker", "Gunshot, gunfire", "Artillery fire"],
    "shot_gun": ["Gunshot, gunfire", "Machine gun", "Cap gun", "Artillery fire", "Fusillade", "Explosion"],
    "creature": ["Roar", "Growling", "Animal", "Roaring cats (lions, tigers)", "Wild animals", "Howl", "Hiss",
                 "Snake", "Dog", "Bird", "Squawk", "Screaming"],
}
SPEECH = {"Speech", "Male speech, man speaking", "Female speech, woman speaking", "Child speech, kid speaking",
          "Speech synthesizer", "Narration, monologue", "Conversation"}
VOICE_GROUPS: set[str] = set()     # groups where speech is expected (none yet: voices are recorded)


def labels_for(game: str | None, override: list[str] | None) -> list[str]:
    return list(override) if override else list(GAMES.get(game or "", GENERIC))


def contrast_for(game: str | None, group: str, override) -> list[tuple[str, str]]:
    if override:
        return list(override)
    return list(CONTRAST.get((game, group), []))
