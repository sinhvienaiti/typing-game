# Local background music

Put personal/local audio files in this folder.

Supported index extensions:

- .mp3
- .m4a
- .aac
- .wav
- .ogg
- .webm

Then run:

```bash
pnpm music:index
```

The command writes `index.local.json`, which is ignored by Git. The portal loads that local index first and falls back to the tracked empty `index.json`.

Example:

```text
shared/music/
├── README.md
├── index.json
├── Chill Study.mp3
├── Piano Focus.m4a
└── index.local.json
```

Commercial music files should remain local and should not be committed to the repository.
