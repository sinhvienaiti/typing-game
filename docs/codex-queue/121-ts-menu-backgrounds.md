# Phiếu 121 · Last Line · Nền màn chính, nạp súng, hành trình, kết quả và logo "Last Line" (7 ảnh) · chờ chủ dự án chọn hướng

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Last Line; thứ tự 7). Màn chính hôm nay là một bảng chữ trên cảnh 3D hố đen (chấm 6,5/10 theo mức chợ); màn nạp súng, thẻ ải, kết quả là bảng chữ trên nền tối.

**Chỉ chạy sau khi chủ dự án chọn hướng ở phiếu 112.** Phiếu viết cho hướng đề xuất **B · Lightbearer**. Chủ dự án chọn A hay C thì Claude thay khối STYLE, STYLE-UI và câu nhân vật trước khi xếp phiếu vào làn.

**Báo cáo:** `docs/codex-queue/121-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-survival/art-src/_refs/owner-epic-2026-10-28.webp`. Lấy mức chi tiết, ánh sáng, chiều sâu và cảm giác quy mô; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, cắt, đổi khổ, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/121/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả `ui/title-horizon.png`, `arena/*`); xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, chữ ký, khung, viền, HUD trong ảnh, trừ chữ logo "Last Line" của ảnh `logo`. Mọi chữ hiện trong ảnh là tiếng Anh.
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-survival/art-src/` (đệ quy) trước khi ghi (`_review/121/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: có mốc lớn làm người chơi nhỏ lại, ít nhất ba lớp sâu (gần, giữa, xa) và trời, ánh sáng có hướng, màu theo kịch bản, chi tiết hoàn thiện. 7 là game indie dễ chịu, nhưng quy mô và ánh sáng thường. 6 là gọn mà chung chung, ánh sáng phẳng. 5 là tranh đẹp nhưng sai tầm. 4 là hình phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Nơi ghi:** `games/typing-survival/art-src/ui/screens-epic/` (thư mục mới).

**Chỉ được ghi:**
- `ui/screens-epic/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`, `<tên>.alpha.png`, `<tên>.512.png`;
- `games/typing-survival/art-src/_review/121-*.jpg`, `games/typing-survival/art-src/_review/121/`;
- `docs/codex-queue/121-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; hai ảnh của hướng đã chọn ở phiếu 112 (`art-src/concepts/b-*.png` khi chọn B); màn hôm nay `games/typing-survival/tmp/map1-audit/sheets/sheet-screens-1920x1080.jpg` (bảng menu ở trái, thẻ ải và năm thẻ súng ở giữa, kết quả ở giữa).

### Khối prompt (nguyên văn)

**STYLE** (mở đầu prompt của sáu ảnh nền)
```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**STYLE-UI** (mở đầu prompt của `logo`; câu cuối "No text, ..." được thay bằng khối LOGO)
```text
Premium science-fiction game interface art for Last Line: dark smoked glass over graphite steel, fine white-gold filigree lines, thin constellation lines and small glyph marks at the corners, electric cyan and orange-gold light accents, a faint inner glow. Crisp, finished and richly detailed like the interface of a top commercial sci-fi action game, with clean bevels and sharp edges, readable at small size. Shown flat and straight on, no perspective, no scenery. No text, letters, numbers, signature or watermark.
```

**REF** (đính kèm ảnh của phiếu 112 hướng đã chọn): `Use the attached image only to keep the same hero, sentinel guns, foes, place, colours and materials. Paint the new scene as described.`

### Bảy ảnh

| Tên | Khổ | Màn | Phần riêng (dán sau STYLE, rồi dòng REF) |
|---|---|---|---|
| `menu-bg` | 1536 × 1024 | màn chính | `Scene: the Lightbearer stands alone at the far end of the causeway, seen from behind and a little to the right, cape moving in the solar wind, her two sentinel guns floating at her shoulders, facing the black hole; the accretion disk fills the right two thirds of the sky. The left 40% of the image is darker and calm (deep navy steel and shadow) for the menu panel.` |
| `briefing-bg` | 1536 × 1024 | thẻ ải | `Scene: the great gate at the start of the causeway, its doors half open onto the deck and the black hole beyond, warning lights in cyan and orange along the gate frame, dust in the light shafts. The centre 60% × 70% of the image is calmer and darker for the briefing panel.` |
| `loadout-bg` | 1536 × 1024 | nạp súng | `Scene: the Armory, a tall vaulted hall inside the station: five empty cradles of light stand in a row on a raised dais, each with a thin beam of cyan or orange light, the black hole seen through a huge round window behind them. The middle band of the image, from 30% to 80% of the height, is calmer for a row of five gun cards.` |
| `journey-bg` | 1536 × 1024 | hành trình | `Scene: a high view of the whole causeway curving across the void toward the black hole, four glowing beacons spaced along it from near to far, broken station rings around it. The beacons are small round lights, no text.` |
| `results-win-bg` | 1536 × 1024 | thắng | `Scene: after victory: the Lightbearer stands tall on a deck strewn with shattered black glass, her sentinels lowered, a warm gold light washing over the causeway from the disk, the last foes dissolving into sparks. The centre 50% × 70% is calmer for the results panel.` |
| `results-lose-bg` | 1536 × 1024 | thua | `Scene: after defeat: the Lightbearer kneels on a cracked deck, one sentinel fallen and dark, red alarm light and smoke, the horde a dark wave in the distance under the black hole. The centre 50% × 70% is calmer for the results panel.` |
| `logo` | ảnh rộng ~3 : 1, nền `#FF00FF` | màn chính | STYLE-UI (thay câu cuối) + `Game logo lettering that reads exactly Last Line: two words, eight letters L-a-s-t and L-i-n-e, capital L in both words, on one line with one space. Sharp white-gold letters with a thin dark graphite outline and a faint electric cyan inner glow; one bright horizontal line of light cuts through the middle of the letters like an event horizon, with a small orange-gold flare where it leaves the last letter. Epic, premium, crisp and easy to read, like the logo of a top commercial sci-fi game. Centred, nothing else in the image. Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the logo contains no pink, magenta or bright purple at all.` |

**Hậu kỳ (`logo`):** tách nền bằng `tools/art-normalize/key-alpha.sh` (đọc README); ra `logo.alpha.png` (cạnh dài bằng nguồn) và `logo.512.png`.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-survival/art-src/` (đệ quy).
2. **Khổ:** sáu ảnh nền 1536 × 1024; `logo` cạnh dài ≥ 1536 ở nguồn. Khác thì cắt giữa rồi thu bằng Lanczos, không phóng to; ghi lệnh.
3. **Chính tả logo:** cắt phóng 4× từng chữ cái, đặt cạnh "Last Line" in bằng một font hệ thống (ghi tên font). Đúng hai từ L-a-s-t, L-i-n-e. Sai một chữ là loại lượt đó.
4. **Không chữ lạc:** sáu ảnh nền không có chữ, số, HUD.
5. **Alpha sạch** (`logo`): min 0, max 255; 0 % px có alpha > 0 mà hue 285–330° và S > 0,5; không viền hồng ở phóng 4×; bbox cách mép ≥ 24 px.
6. **Chỗ cho bảng:** trên bản cắt 16 : 9 ở giữa (1536 × 864), vùng lặng ghi ở từng ảnh có độ lệch chuẩn luma ≤ 0,12 và luma trung bình ≤ 0,40, để chữ kem và trắng đọc rõ. Ghi số.
7. **Dựng thử** `_review/121-mock.jpg`: mỗi nền ở 16 : 9 với một khối kính tối mờ 60 % đúng vùng lặng (menu, thẻ ải, năm thẻ súng, kết quả), `logo.alpha.png` trên `menu-bg`. Xem: bảng đọc rõ, cảnh vẫn hùng vĩ.
8. **Cùng bộ:** luma trung bình của sáu nền lệch nhau ≤ 0,10 (trừ `results-lose-bg`); hue trung vị lệch ≤ 20°.
9. **Tờ so với tham chiếu** `_review/121-vs-ref.jpg`: `menu-bg` có logo, `loadout-bg`, `journey-bg` và ảnh tham chiếu, cùng cao 640 px; hàng dưới là màn chính hôm nay (cắt từ `sheet-screens-1920x1080.jpg`). Ghi một dòng cho mỗi ảnh: "đứng cạnh được" hay "chưa", và vì sao.
10. **KA5 mức chợ:** M và Q cho từng bản chọn, ở cỡ đầy đủ và ở 384 px.

**Xong khi:** bảy ảnh có bản chọn, qua mục 2–6 và 8, mỗi ảnh tự chấm M ≥ 8, Q ≥ 8. Logo sau 3 lượt vẫn sai chính tả thì ghi "không đạt, dùng font"; Claude dựng chữ bằng font của game.
