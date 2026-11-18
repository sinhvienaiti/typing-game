# Phiếu 245 · Ba game · Hàng danh sách, nút Close của bảng nhanh; bóng hình quái cỡ nhỏ của Last Line

**Nguồn:**
- **Luật chung của đợt: mục "Luật chung của đợt 242–246" trong `docs/codex-queue/242-ts-icons-real-size.md`.** Phiếu này chỉ ghi chỗ khác.
- Phiếu khung gốc: Dragonhold `162-dh-ui-frames.md` (`ui/frames/`), Wordwoven `115-td-ui-frames.md` (`ui/frames-epic/`, bản `.v2`), Last Line `127-ts-ui-frames.md` (`ui/frames-epic/`). Khổ, cách cắt chín mảnh và file `.json` theo các phiếu đó.
- Phiếu chân dung quái Last Line và các bản `.v2` ở `ui/foes/`.
- Lượt chấm thứ hai (31/10, khoảng 16:00):
  - danh sách Keyboard sound của bảng Sound là listbox web mặc định; Dragonhold và Wordwoven chưa có ảnh hàng thường và hàng đang chọn;
  - Close là nút chữ ở đầu bảng, cả ba game;
  - ở Last Line, chân dung Brute, Pack Leader và Scout thu về 20–24 px đều thành cùng một con ngài nâu; Swarm thành một chấm.

**Báo cáo:** `docs/codex-queue/245-report.md` (tiếng Việt) và thư mục `docs/codex-queue/245/`. Model `gpt-6.1-sol`, mức `high`.

## Việc A · Hàng danh sách (Dragonhold, Wordwoven)

Last Line dùng lại `button` và `button-active` của 127, không làm ở phiếu này.

| Game · tên | Ý (EN) |
|---|---|
| Dragonhold · `list-row` | a long, low list row plate: dark slate inset with a thin warm-gold rim, plain flat middle that stretches sideways |
| Dragonhold · `list-row-active` | the same plate with an ember-gold inner glow along the rim and a small glowing gem marker at the left end |
| Wordwoven · `list-row` | a long, low list row plate: dark jade lacquer with a fine cream filigree edge, plain flat middle that stretches sideways |
| Wordwoven · `list-row-active` | the same plate with a warm amber lantern glow along the rim and a small lantern-gold marker at the left end |

- Thư mục: Dragonhold `ui/frames/`, Wordwoven `ui/frames-epic/`.
- Khổ nguồn 1536 × 256, kèm `<tên>.json` (`size`, `slice` trái/phải/trên/dưới, `fill`) như `button.json` của cùng game. Hàng cao khoảng **34 px ở 720p**, nên viền cắt không quá 25 % chiều cao.
- Cặp thường/đang chọn chồng khít: IoU mặt nạ alpha ≥ 0,95.
- **Kiểm cỡ thật:** ghép năm hàng (một hàng đang chọn) rộng 300 px, cao 34 px (720p) và 450 × 51 (1080p) bằng chín mảnh, chữ tên bộ phím (ví dụ "Raindrop Tile", "Hail Stone") bằng font hệ thống, trên mảnh `panel-large` của game; xuất 1× và phóng ×4. Hàng đang chọn phải thấy ngay ở 1×.

## Việc B · Nút Close (ba game)

| Game · tên | Ý (EN) |
|---|---|
| Dragonhold · `close` | a round close button: an ember-gold X on a dark slate disc with a forged-iron rim |
| Wordwoven · `close` | a round close button: a cream-and-gold X on a jade disc with a bronze rim |
| Last Line · `close` | a round close button: a white-gold X on a graphite disc with a thin electric-cyan seam |

- Thư mục: Dragonhold `ui/frames/`, Wordwoven `ui/frames-epic/`, Last Line `ui/frames-epic/`.
- Khổ và thu nhỏ như icon (1024², `.256`, `.128`, `.64`); cỡ trong game **32 / 44**.
- Kiểm 3–8 của 242, với nhãn trống, trên góc trên phải của `panel-large` thật.

## Việc C · Bóng hình quái cỡ nhỏ (Last Line)

Thư mục `games/typing-survival/art-src/ui/foes/`, tên `<quái>.small.png` (cùng bản thu `.256`, `.128`, `.64`), lượt sinh `<quái>.small.tryN.*`. Đính kèm chân dung đã có của đúng con quái đó (bản `.v2` nếu có) để giữ nhận diện.

| Quái | Ý (EN) |
|---|---|
| `brute` | a bulky, horned, front-on mass with a wide stance, heavy shoulders |
| `pack-leader` | the Brute's bulk with a tall glowing crown crest and a lighter gold rim, clearly taller than the Brute |
| `scout` | a thin dart shape with long swept-back wings, pointed nose |
| `swarm` | a small spiky mine with a bright core |
| `shield-guard` | a creature hidden behind one tall front shield slab |
| `splitter` | a round body visibly cracked into two halves with a glowing seam |

- Đây là **bóng hình cho cỡ 20–28 px**, không phải chân dung thu nhỏ: một khối đặc, viền tối dày, mỗi con một dáng ngoài rõ. Giữ màu chủ của từng con để người chơi nối được với chân dung.
- Cỡ trong game 24 / 36 (hàng Strong/Weak và dải mối đe dọa).
- **Kiểm riêng:** sáu con khác dáng từng đôi, IoU ≤ 0,70 ở 24 px (chặt hơn mốc chung). Ô so sánh sáu con xếp một hàng ở 24 px 1× trên `word-plate` thật, kèm tên dưới mỗi con.

## Chỉ được ghi

- `games/dragon-hold/art-src/ui/frames/{list-row,list-row-active,close}.*` (mới).
- `games/typing-defense/art-src/ui/frames-epic/{list-row,list-row-active,close}.*` (mới).
- `games/typing-survival/art-src/ui/frames-epic/close.*` (mới).
- `games/typing-survival/art-src/ui/foes/<quái>.small.*`, `<quái>.small.try*.*` (mới) cho sáu con ở bảng Việc C.
- `games/{dragon-hold,typing-defense,typing-survival}/art-src/_review/245*`.
- `docs/codex-queue/245-report.md`, `docs/codex-queue/245/`.
