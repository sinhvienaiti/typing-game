# Lô Firefly 1: Clear Wind, Phi Kiếm và Ngự Kiếm Quyết (02/11/2026)

Lô đầu của lát cắt demo: Clear Wind với K0 Phi Kiếm và K1 Ngự Kiếm Quyết, đủ năm pha, có lớp P phép bậc thấp (`magic-cast`, `magic-hit`). Lớp P bậc cao (`magic-release`, `magic-impact`) nằm ở lô 1b cùng K2, K5. Prompt chép nguyên từ [`WEAPON_AUDIO.md`](WEAPON_AUDIO.md) §3 (soát lượt 3, 02/11).

**Cách tạo:** Firefly → Generate Sound Effects, model Adobe (không dùng model đối tác). Chép đúng prompt. Mỗi lần tạo cho 4 bản.

**Nơi bỏ file:** `~/AudioLab/inbox/firefly/immortality-cultivation/<Id>/`, mỗi id một thư mục, tên thư mục đúng cột Id. Giữ nguyên tên file Firefly đặt, không đổi tên.

| # | Id | Prompt | Lần tạo | Số bản | Dùng cho |
|---|---|---|---|---|---|
| 1 | `tt-sfx-magic-hit` | `bright magical strike, crystalline energy burst, sparkling, sharp attack, punchy, dry` | 2 | 8 | trúng K0, K1 (lớp phép) |
| 2 | `tt-sfx-item-clearwind` | `magical jade ring chiming, radiant crystalline sparkle, sharp attack, bright` | 1 | 4 | nốt chữ ký khi trúng; kiếm hiện; vệt bay |
| 3 | `tt-sfx-sword-ring` | `enchanted steel blade ringing, bright shimmering ping, sharp attack, dry, isolated` | 1 | 4 | nốt xác nhận trúng |
| 4 | `tt-sfx-sword-hit-head` | `spirit sword striking stone armor, sharp metallic crack, punchy, dry, isolated` | 2 | 8 | đầu tiếng trúng |
| 5 | `tt-sfx-sword-hit-body` | `heavy sword energy slash impact, dense, punchy, saturated, cinematic, dry` | 2 | 8 | thân trúng |
| 6 | `tt-sfx-elem-kim-burst` | `explosive radiant metal shard burst, sharp shimmering impact, powerful` | 1 | 4 | hệ Kim khi trúng |
| 7 | `tt-sfx-magic-cast` | `swift sparkling spell burst, bright shimmering whoosh, sharp attack, dry` | 2 | 8 | phát K0, K1; lóe kiếm rời vai |
| 8 | `tt-sfx-sword-draw` | `fantasy sword unsheathed, bright ringing steel shing, sharp attack, dry, isolated` | 2 | 8 | đầu tiếng phát |
| 9 | `tt-sfx-sword-swing` | `powerful sword slash, energy-charged whoosh, fast, heavy, cinematic, dry` | 2 | 8 | thân phát |
| 10 | `tt-sfx-elem-kim-ignite` | `radiant metal energy surging, bright glittering sparkle, sharp attack` | 1 | 4 | hệ Kim khi phát; vệt bay |
| 11 | `tt-sfx-magic-trail` | `glittering magical energy streak, fast shimmering whoosh, bright, intense` | 1 | 4 | bay; hạt lấp lánh khi kiếm hiện |
| 12 | `tt-sfx-sword-flyby` | `enchanted flying sword whizzing past, sharp singing whoosh, fast, intense` | 2 | 8 | bay K0; mỗi kiếm K1 rời vai |
| 13 | `tt-sfx-magic-aura` | `glowing magical aura shimmer, sparkling crystalline tail, ethereal, wide, no transient` | 1 | 4 | đuôi hào quang |
| 14 | `tt-sfx-sword-tail` | `magical sword clash echoing across vast canyon, shimmering rolling echo, no transient` | 1 | 4 | đuôi vang hẻm núi |
| 15 | `tt-sfx-common-sub` | `huge sub bass impact, deep pressure wave, cinematic` | 1 | 4 | sub ở kiếm 3 của K1 và bản Chớp |

**Tổng:** 15 id, 22 lần tạo, 88 bản.

Khi Audio Lab nhận game này, danh sách lô chuyển sang `docs/games/audio/firefly/immortality-cultivation.json` theo `schema.json` (WEAPON_AUDIO.md §4.3 bước 0, việc mở 16); tới lúc đó bảng này là nguồn.
