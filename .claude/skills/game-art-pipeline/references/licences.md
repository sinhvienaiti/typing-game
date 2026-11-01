# Free assets and licences

The rule text lives in [SHARED_SYSTEMS_BAR.md](../../../../docs/games/SHARED_SYSTEMS_BAR.md) §5. The sources researched so far, with their clause checks, are in [FREE_ASSET_SOURCES.md](../../../../docs/games/FREE_ASSET_SOURCES.md), and what we use is in `docs/games/THIRD_PARTY.md`. The owner, 01/11/2026: "có thể dùng các loại tài nguyên, thư viện, source có sẵn miễn sao nó miễn phí và được cho phép thương mại ở game của chúng ta, chứ k dùng các loại bị giới hạn".

## 1. Allowed

- **Code:** MIT, BSD, ISC, Apache-2.0 and MPL-2.0 (use the library's files unmodified). Zlib, keeping the copyright notice in source (for example pmndrs `postprocessing`).
- **Assets:**
  - CC0.
  - CC-BY, with a full credit line on the game's Credits page. Some sources need an exact line per item; ESA/Webb and ESA/Hubble images do.
  - Free custom licences that allow commercial use with no payment and no in-game credit, and forbid only reselling the asset itself as a pack. Example: Quaternius Asset License v1.0 (QAL). Record the download date and the licence text word for word, because QAL §7 applies the version in force when you obtained the asset.
- **Third-party models** under CC0 or QAL may ship in the games (owner, 01/11).

## 2. Banned

- **Restricted Creative Commons:** NC (non-commercial), ND (no derivatives) and SA (share-alike).
- **GPL, AGPL, LGPL** when modified or statically linked.
- **Unclear terms:**
  - "free" or "royalty-free" with no clear licence;
  - anything with no clear licence at all;
  - paid content.
- **Assets from other games,** including Monkeytype (GPL-3.0).
- **Licences checked and refused:**
  - Mixamo (Adobe terms not verifiable);
  - Fab Standard and Sketchfab Standard;
  - BlenderKit "Royalty Free" and ShareTextures "Custom CC0";
  - RenderCrate (terms ban AI);
  - Megascans after 2024 (paid, Fab);
  - Unity Asset Store (custom EULA);
  - Gaea Community (non-commercial).
- **Anything tagged NoAI.**
- **Audio-specific bans:** see [audio.md](audio.md) §4.

## 3. Verify on the page, never from a list

- **Read the licence on the asset's own page** or in the repo's LICENSE file. Quote the exact words in `THIRD_PARTY.md` and note the date.
  - Do not trust aggregator lists, ChatGPT summaries or a pack's description on another site.
- **Read the clauses, not only the licence name:** attribution, "no redistribution as a pack", AI use, NFT. FREE_ASSET_SOURCES.md §9 has the checks done so far.
  - Shipping files inside a web game is fine under "no pack redistribution" clauses.
  - Merging assets into our own GLBs and KTX2 atlases keeps them from looking like a loose pack.
- **When two pages of one source disagree, follow the stricter.** Quaternius's pack pages say CC0 while its licence page says QAL; treat it as QAL.
- **No scraping, no scripted bulk downloads.** Poly Haven's terms forbid scraping, and ShareTextures forbids automated downloads. Download item by item.
- **Downloads:**
  - Free packs that meet §1 no longer need per-pack approval from the owner (01/11). They still need a full row in `THIRD_PARTY.md`.
  - A custom licence outside §1 is the owner's decision.
  - Your session's own permission prompts still apply.
- **Where packs live:** outside the repos (for example `~/VFXLab/packs/`), with a pointer file. Never in Git.

## 4. What may go into an AI tool

Never send these to ChatGPT, Gemini, Tripo or any cloud AI:
- models tagged NoAI;
- assets under the Sketchfab or Fab Standard licence;
- Mixamo files;
- assets taken through the Poly Pizza service (its terms forbid AI use);
- Sonniss audio, or any sound or image with a Sonniss layer. This includes Claude: touch Sonniss files only through local signal measurements (AUDIO_PIPELINE §10.2).

Screenshots of CC0 assets are fine as visual references.

## 5. When to source instead of generating

- **After two rounds without a real score gain, offer the sourcing route in the same report,** not after more rounds. Owner, 31/10, after dragon fire went 11 rounds and still scored about 6: "sao bạn cứ nhất thiết phải tự tạo, sao k đưa tôi loại bạn muốn" and "lấy gì đảm bảo bạn làm tiếp mà đạt được".
- **Write a search brief in the repo.** Cover what is needed, the style, licence rules, formats (alpha sheets, frame size, poly budget) and a return table. Model it on `docs/games/vfx/ASSET_SEARCH_BRIEF.md`.
  - The owner may hand the brief to ChatGPT.
  - Treat what comes back as candidates to verify (§3), not as answers.
- **Test a pack before integrating it:** on the existing bench, with two blind judges and a stop rule (for example, stop if it does not reach the bar within a day).
- **Sourcing does not lower the bar.**
  - Flat low-poly packs (Kenney, KayKit, Poly Pizza) read as toys. Use them for blockout only, never as main art.
  - Mixed free assets rarely form a set: the best of 58 checked landmark models scored 7, and they did not match each other.
  - Real-world-scan materials, HDRIs and rendered flipbooks (Poly Haven, ambientCG, cgbookcase, Unity Labs, JangaFX) are what move a scene toward the reference.
