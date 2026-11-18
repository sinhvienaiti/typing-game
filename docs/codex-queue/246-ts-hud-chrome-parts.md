# Phiếu 246 · Last Line · Mảnh vỏ HUD thay phần CSS: sọc cảnh báo, thanh vỏ tàu, bến bị khoá

**Nguồn:**
- **Luật chung của đợt: mục "Luật chung của đợt 242–246" trong `docs/codex-queue/242-ts-icons-real-size.md`** (tên file, hậu kỳ, giới hạn ảnh, cấm, nhận). Kiểm 3–8 của 242 viết cho icon; mảnh ở phiếu này dùng phần kiểm riêng bên dưới.
- Phiếu khung gốc `127-ts-ui-frames.md` (`ui/frames-epic/`): khổ, cách cắt chín mảnh, file `.json`, chất liệu hướng B.
- Lượt chấm thứ hai (31/10, khoảng 16:00), giám khảo Last Line 7,1:
  - sọc cảnh báo dưới mỗi tiêu đề, dải trên đầu bến và dải băng thông báo là `repeating-linear-gradient` của CSS; luật mỹ thuật cấm vật thay thế vẽ bằng mã;
  - phần đầy của thanh vỏ tàu là `linear-gradient` với mặt nạ chia ô của CSS;
  - bến bị khoá là tấm kính mờ trong suốt, đèn tường hành lang lọt qua thành một mảnh nâu lạc.

**Báo cáo:** `docs/codex-queue/246-report.md` (tiếng Việt) và thư mục `docs/codex-queue/246/`. Model `gpt-6.1-sol`, mức `high`.

## Việc

Thư mục `games/typing-survival/art-src/ui/frames-epic/`. Mỗi mảnh kèm `<tên>.json` (`size`, `slice` hoặc `repeat`, `fill`) như `button.json`.

| Tên | Cỡ trong game (720p) | Ý (EN) |
|---|---|---|
| `hazard-strip` | cao 6–10 px, dài tuỳ ý | a worn industrial hazard stripe band: diagonal orange and black stripes on a steel strip, a thin bevel along both long edges, small rivets at the ends; the middle repeats seamlessly sideways |
| `hazard-strip-neutral` | như trên | the same band with the orange stripes replaced by light grey, so the game can tint it per gun colour |
| `hull-track` | cao 14–18 px, rộng 300–420 px | an empty segmented hull bar channel: dark graphite glass in a white-gold steel frame, ten faint segment dividers |
| `hull-fill` | như trên | the same channel filled with bright volt-blue energy, segment dividers still visible |
| `hull-fill-low` | như trên | the same filled channel in hot alarm red-orange with a slight flicker glow, for low hull |
| `bay-sealed` | khoảng 120 × 160 px | an opaque sealed bay door plate: heavy steel shutter with hazard-orange corner marks and a central lock socket, fully opaque so nothing shows through |

- `hazard-strip` và `hazard-strip-neutral`: khổ nguồn 2048 × 128; giữa lặp ngang không thấy nối (kiểm: ghép ba bản nối đuôi, chênh luma ở mối nối ≤ 0,03). `json` ghi `repeat: "x"` và độ rộng mũ hai đầu.
- `hull-track`, `hull-fill`, `hull-fill-low`: khổ nguồn 1536 × 128, ba ảnh chồng khít (IoU alpha ≥ 0,97); viền cắt chín mảnh không quá 30 % chiều cao. Luma lòng rãnh: `hull-fill` cao hơn `hull-track` ít nhất 0,2.
- `bay-sealed`: khổ nguồn 768 × 1024, alpha 255 trong toàn bộ thân tấm (không có vùng bán trong suốt ngoài dải mép 3 px).

**Kiểm riêng:**
1. KA1 md5, khổ, alpha sạch như 242.
2. **Cỡ thật:** ghép trên ảnh chụp HUD trận đã có của Claude nếu tìm thấy trong `games/typing-survival/tmp/ui-art/`, nếu không thì trên `ui/frames-epic/panel-large.png`: thanh vỏ ở 0 %, 30 % (bản `low`), 70 %, 100 %; dải sọc dưới một tiêu đề dài 400 px; tấm bến khoá có ổ khoá `ui/icons/lock.png` ở giữa, cỡ 40 px. Xuất 720p và 1080p 1×, thêm phóng ×4.
3. KA5 tự chấm ở tờ 720p 1×.

## Chỉ được ghi

- `games/typing-survival/art-src/ui/frames-epic/{hazard-strip,hazard-strip-neutral,hull-track,hull-fill,hull-fill-low,bay-sealed}.*` (mới), cùng lượt sinh `.tryN.*`.
- `games/typing-survival/art-src/_review/246*`.
- `docs/codex-queue/246-report.md`, `docs/codex-queue/246/`.
