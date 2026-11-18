# Phiếu 301 · Tu Tiên · Ảnh 2D kỹ năng mở rộng (thần thú và pháp bảo), 16 lần gọi `image_gen`

Anh (05/11 ~20:10): "tu tiên có rất nhiều loại kỹ năng đa dạng ... kỹ năng hoá thân, gọi thần ... thần thú ... pháp bảo, hãy kêu gemini tìm sau đó đưa chatgpt hoặc codex tạo ảnh 2d", và "tăng mạnh việc tạo ảnh". Gemini (4 Argon, Cao) đã đề xuất 30 thiết kế, tự duyệt PASS hai lần liền: `docs/games/tu-tien/source/gemini-skills-expansion-2026-11-05.md`. Phiếu này vẽ 16 trong số đó. Có một phiếu Codex khác chạy song song cho phần còn lại; anh cho phép tăng thêm làn. Prompt đã chốt, không cần phản biện.

**Model `gpt-6.1-sol`, mức `high`. Đúng 16 lần gọi `image_gen`, mỗi thiết kế một lần, không gọi thêm, không tự sửa lại.**

**Báo cáo:** `docs/codex-queue/301-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`

**Được ghi:** chỉ thêm file mới vào `D` (`cp -n`, không ghi đè) và `docs/codex-queue/301-report.md`.
**Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở file nguồn Gemini ở trên, tìm mục của thiết kế (theo mã và id trong bảng), lấy **nguyên văn** đoạn "2D Still Prompt".
2. Mở các ảnh tham chiếu trong bảng bằng `view_image` (ảnh của mình, anh đã duyệt). Gọi `image_gen` tạo mới, khổ ngang 16:9, kèm các ảnh đó. Prompt gửi đi gồm:
   - câu đầu: `Use the attached images only as the style reference for light, translucency, glow, sparkle and finish; do not copy their shapes or subjects.`
   - rồi đoạn "2D Still Prompt" nguyên văn;
   - với dòng ghi "thêm câu màu Ám", thêm câu cuối: `Colour rule: black shadow energy with dark-crimson ember light only; no purple, no violet, no cyan.`
3. Chép kết quả từ `~/.codex/generated_images/...` bằng `cp -n` thành `D/<tên ra>.png`, giữ khổ thật.
4. Ghi `D/<tên ra>.prompt.txt`: công cụ (Codex `image_gen`), các ảnh tham chiếu, prompt đã gửi nguyên văn, khổ thật.

| Mã | Tên ra | Ảnh tham chiếu | Ghi chú |
|---|---|---|---|
| C1 | `azure-cloud-dragon.v1-try1` | `D/pillar-thunder-field-clean.v1-try1.jpg` + `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/spirit-dragon/qi-dragon.v1-try3.png` |  |
| C2 | `white-fiend-tiger.v1-try1` | `D/kiem-edict-sky-gates.v1-try1.jpg` + `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/spirit-dragon/qi-dragon.v1-try3.png` |  |
| C3 | `vermilion-solar-phoenix.v1-try1` | `D/fire-slash-arc.v1-try1.jpg` + `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/spirit-dragon/qi-dragon.v1-try3.png` |  |
| C4 | `abyssal-xuanwu-tortoise.v1-try1` | `D/water-ground-mark-clean.v1-try1.jpg` + `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/spirit-dragon/qi-dragon.v1-try3.png` |  |
| C5 | `auspicious-thunder-qilin.v1-try1` | `D/pillar-thunder-field-clean.v1-try1.jpg` + `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/spirit-dragon/qi-dragon.v1-try3.png` |  |
| C6 | `astral-kunpeng-leviathan.v1-try1` | `D/water-ground-mark-clean.v1-try1.jpg` + `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/spirit-dragon/qi-dragon.v1-try3.png` |  |
| C7 | `all-knowing-baize-spirit.v1-try1` | `D/pillar-light-judgement-clean.v1-try1.jpg` + `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/spirit-dragon/qi-dragon.v1-try3.png` |  |
| C8 | `nine-tailed-celestial-fox.v1-try1` | `D/ice-slash-arc-clean.v1-try1.jpg` + `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/spirit-dragon/qi-dragon.v1-try3.png` |  |
| D1 | `mountain-crushing-imperial-seal.v1-try1` | `D/ult-earth-ink-peaks.v1-try1.jpg` |  |
| D2 | `primordial-chaos-bell.v1-try1` | `D/kiem-edict-sky-gates.v1-try1.jpg` |  |
| D3 | `blade-swallowing-immortal-gourd.v1-try1` | `D/kiem-edict-sky-gates.v1-try1.jpg` |  |
| D4 | `nine-dragon-refining-cauldron.v1-try1` | `D/fire-slash-arc.v1-try1.jpg` |  |
| D5 | `seven-treasure-suppressing-pagoda.v1-try1` | `D/pillar-light-judgement-clean.v1-try1.jpg` |  |
| D6 | `yin-yang-void-mirror.v1-try1` | `D/pillar-light-judgement-clean.v1-try1.jpg` |  |
| D7 | `five-element-heavenly-silk.v1-try1` | `D/ult-wind-firmament-clean.v1-try1.jpg` |  |
| D8 | `twelve-stem-nether-banners.v1-try1` | `D/blood-slash-arc.v1-try1.jpg` | thêm câu màu Ám |

## Xong khi
- Đủ 16 bộ `.png` và `.prompt.txt` trong `D`. Báo cáo ghi khổ thật, số lần gọi `image_gen` (phải là 16), một câu nhận xét mỗi ảnh (đúng ý thiết kế không, có chữ, mặt người thật hay nền không đen không).

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
