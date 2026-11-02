# Lô Firefly 03/11/2026: tiếng chiêu và tiếng hô mẫu

Theo canon D58, anh muốn Claude tự tạo âm thanh cho chiêu ("chúng ta có firefly cơ mà, sao bạn không tạo"). Claude tạo trong tab Firefly của anh, đêm 03/11, khoảng 01:50–02:20.

- **Tiếng hiệu ứng:** Generate Sound Effects, chỉ dùng model Adobe.
- **Tiếng hô:** Generate Speech, model Firefly Speech của Adobe, tiếng Phổ thông (Mandarin, China).

## Kết quả

- **Tiếng hiệu ứng:** 28 id, 46 lượt tạo, 184 bản. Mỗi lượt cho 4 bản WAV 48 kHz stereo. Firefly đẩy đỉnh mọi bản lên 0 dB.
  - 15 id là lô 1 đã soạn trong [`WEAPON_AUDIO_FIREFLY_BATCH1.md`](WEAPON_AUDIO_FIREFLY_BATCH1.md), chép đúng prompt.
  - 13 id mới cho lớp uy lực (D58): tiếng nền khi tung tuyệt kỹ, tiếng hút vào im lặng, chuông ngọc, bầy kiếm, sông kiếm dâng, nhát chém khổng lồ, sấm trầm, trúng thịt, trúng vỏ giáp, thú tan thành linh quang, bắn mực, tiếng lướt của cảnh cận, chí mạng.
- **Tiếng hô mẫu:** 6 bản, giọng nữ cho Lam. Đây là mẫu để chọn giọng và cách hô; câu chốt theo danh mục chiêu mới.
  - 万剑……朝宗！
  - 万锋——听诏！ (hai giọng)
  - 剑心所至，天地皆开！ (hai giọng)
  - 疾！
- **Trang nghe để anh chọn:** http://127.0.0.1:8781/review/tu-tien-firefly-1/index.html (máy chủ nhỏ ở scratchpad của phiên).
  - Mỗi bản có trình phát, độ dài, LUFS và đỉnh.
  - Nút "Lưu lựa chọn" ghi vào `~/AudioLab/review/tu-tien-firefly-1/picks/`.
- **File gốc:** `~/AudioLab/inbox/firefly/immortality-cultivation/<id>/<id>.v1-try<k>-var<j>.wav`, không đưa vào Git.

## Prompt lô mới

| Id | Prompt | Giây | Lượt |
|---|---|---|---|
| `tt-sfx-ult-world-drone` | `ominous deep celestial drone swelling, vast heavenly pressure, rising, cinematic, no transient` | 6 | 2 |
| `tt-sfx-ult-vacuum` | `sudden air suction into total silence, reversed whoosh, cinematic` | 1,5 | 2 |
| `tt-sfx-jade-bell` | `deep jade temple bell strike, long shimmering resonant tail, majestic` | 6 | 2 |
| `tt-sfx-sword-swarm` | `hundreds of flying swords rushing overhead, dense metallic whooshing wind, powerful, cinematic` | 5 | 2 |
| `tt-sfx-sword-river-swell` | `massive metallic swell rising into the sky, reversed shimmering steel, epic, cinematic` | 3 | 2 |
| `tt-sfx-giant-slash` | `colossal sword slash cleaving the air, enormous sharp swoosh with thunderous low impact, epic` | 2,5 | 2 |
| `tt-sfx-thunder-low` | `deep rolling thunder boom, massive low impact, cinematic` | 4 | 1 |
| `tt-sfx-hit-flesh` | `heavy blade slicing into beast flesh, wet punchy impact, powerful, dry` | 1,5 | 2 |
| `tt-sfx-hit-chitin` | `sword striking hard insect chitin shell, sharp crunchy crack, punchy, dry` | 1,5 | 2 |
| `tt-sfx-beast-death-burst` | `magical beast dissolving into a burst of spirit light, shimmering whoosh, powerful` | 2,5 | 2 |
| `tt-sfx-ink-burst` | `ink splash burst with paper tearing whoosh, sharp, dry` | 1,5 | 1 |
| `tt-sfx-cutin-whoosh` | `dramatic anime cut-in swoosh, sharp whoosh with shimmering metallic ring, cinematic` | 1,5 | 2 |
| `tt-sfx-crit-ping` | `critical hit metallic ping with sparkling burst, bright, punchy` | 1 | 2 |

## Ghi chú

- **Tiếng hô bằng ElevenLabs** (anh cho phép riêng cho tiếng hô) chưa tạo được. Firefly hiện hộp "Start using partner models": bấm OK là chấp nhận điều khoản cho mọi model đối tác và xác nhận người dùng trên 18 tuổi. Việc đó anh phải tự bấm, nên Claude bấm Cancel.
  - Firefly Speech của Adobe đọc được tiếng Phổ thông, nhưng giọng thiên về đọc, ít chất hô.
  - ElevenLabs v4 có thẻ cảm xúc (`[shouting]`), nhưng các giọng mặc định là giọng Anh nói tiếng Trung.
- **Firefly chỉ chạy một việc tạo mỗi lúc,** và tab chạy nền bị trình duyệt hãm. Tạo âm phải để tab Firefly ở phía trước.
- **Audio Lab chưa nhận game này** (chỉ có `dragon-hold`, `typing-defense`, `typing-survival`). Bước cắt, đặt mức theo bậc, OGG và dòng giấy phép làm khi anh chọn xong. Giấy phép: tiếng hiệu ứng theo điều khoản model Adobe; tiếng hô ghi riêng model đã dùng.
