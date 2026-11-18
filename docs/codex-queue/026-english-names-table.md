# Phiếu 026 · Ba game · Bảng tên tiếng Anh cho danh từ trong game (chỉ đọc mã, không trình duyệt)

**Bối cảnh:** chủ dự án chốt ngày 27/10/2026, luật nằm trong `AGENTS.md` của repo cha, mục "In-game names":
- Game dạy tiếng Anh, nên người chơi thấy danh từ trong game bằng tiếng Anh: trụ, bẫy, nhà, lính, loại quái, món đồ, súng. Ví dụ "Pine Bomb", không phải "Bom Hạt Thông".
- Câu, gợi ý, menu vẫn bằng tiếng Việt.
- Lần đầu một tên xuất hiện (thẻ ra mắt, chú thích ở cửa hàng), tên có thể kèm một nghĩa tiếng Việt ngắn.
- Nhân vật độc nhất giữ tên riêng: hai Rồng (Hỏa Long, Bạch Long), Draconis, Bà Cú Mực, các boss có tên như Mộc Tinh, Đại Bàng Tinh.

Việc đổi tên sẽ làm theo từng game, sau khi làn của game đó xong. Phiếu này chỉ lập **bảng đề xuất**, để Claude duyệt rồi đưa chủ dự án xem.

**Thư mục làm việc:** repo cha (`.`).

**Chỉ được ghi:**
- `docs/games/NAMES_EN.md`: tiếng Việt có dấu; tên đề xuất thì bằng tiếng Anh.
- `docs/codex-queue/026-report.md`.

**Cấm:**
- sửa bất cứ file nào trong `games/**`, vì ba làn của Claude đang sửa mã ở đó;
- lệnh git có ghi;
- mạng;
- dev server;
- đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`).

## Nguồn đọc

- **Rồng Giữ Ải:**
  - mã: `games/dragon-hold/src/content/data/{enemies,generals,our-side,maps,stages,waves}.ts`, `src/content/rules.ts`, chữ hiện trên màn trong `src/ui/**` và `src/app/**`;
  - thiết kế: `docs/games/dragon-lane/02-enemies-generals-bosses.md`, `03-our-side-shop-traps-support.md`;
  - id model: `games/dragon-hold/art-src/3d/SOURCES.json`, `tools/map-factory/registry/out/assets.dragon-hold.json`.
- **Lời Gọi:**
  - mã: `games/typing-defense/src/content/slice-1a.ts`, `rules.ts`, `src/ui/**`, `src/view/words/cards.ts`;
  - thiết kế: `games/typing-defense/docs/td/TYPING_DEFENSE_DESIGN.md`;
  - id model: `tools/map-factory/registry/out/assets.typing-defense.json`.
- **Tuyến Cuối:**
  - mã: `games/typing-survival/src/content/{guns,foes,chapter-1,stage-rules,stage-s0,threat,rules}.ts`, `src/view/hud.ts`, `src/app/**`;
  - thiết kế: `games/typing-survival/docs/BUILD_S1.md`.

## Việc

1. **Liệt kê** mọi danh từ người chơi thấy, mỗi game một bảng: trụ, tháp, nhà, công trình, bẫy, lính, đơn vị phe ta, loại quái, tướng địch, món đồ, súng, kỹ năng có tên-vật (ví dụ "Lưới Phóng"), tài nguyên (Vàng, Gỗ, Vảy…). Mỗi tên lấy từ chuỗi thật trong mã, không lấy từ trí nhớ.
2. **Mỗi dòng ghi:**

   | id trong mã | Tên Việt hiện tại | Tên tiếng Anh đề xuất | Nghĩa Việt ngắn (cho lần đầu) | Loại | Chỗ hiện (file:dòng, đếm số chỗ) | Ghi chú |

   - **Tên tiếng Anh:**
     - Viết hoa từng từ (Title Case), dài 1–3 từ, dễ hiểu với người mới học.
     - Ưu tiên tên đã có trong id model, ví dụ `moss-grunt` → Moss Grunt, `pine-bomb` → Pine Bomb, `net-launcher` → Net Launcher, `herb-hut` → Herb Hut, `moss-warden` → Moss Warden, `blight-wolf` → Blight Wolf, `tusk-boar` → Tusk Boar, `thorn-wasp` → Thorn Wasp, `thorn-ant` → Thorn Ant.
     - Trong một game, không có hai tên trùng nhau hay gần giống nhau.
   - **Nhân vật độc nhất:** ghi "giữ tên riêng" và không đề xuất tên tiếng Anh.
   - **Tên không chắc thuộc loại danh từ phải đổi** (ví dụ tên kỹ năng là động từ, tên chế độ, tên vùng đất): đưa vào bảng "Cần Claude xem", không tự quyết.
   - **Va chạm với từ người chơi phải gõ:** nếu tên tiếng Anh trùng một từ trong bộ từ vựng chung (`shared/vocabulary/levels/*.json`, trường `en`), ghi "trùng từ gõ: <cấp>". Đó không phải lỗi, nhưng cần biết.
3. **Tóm tắt mỗi game:** số tên phải đổi, số tên giữ, số chỗ hiện phải sửa. Cũng nêu những file chứa chuỗi sẽ phải sửa khi đổi tên: UI, nội dung, test, golden nếu chuỗi có trong golden.

## Kiểm (bắt buộc)

1. Mỗi "Tên Việt hiện tại" có ít nhất một chỗ hiện ghi được `file:dòng`. Kiểm bằng một lệnh `rg -F` cho mỗi tên và dán số dòng tìm được vào báo cáo.
2. Không có hai tên tiếng Anh trùng nhau trong một game. Kiểm bằng một lệnh `node` nhỏ đọc bảng và in số trùng, phải bằng 0.
3. `git status --short` chỉ thêm `docs/games/NAMES_EN.md` và `docs/codex-queue/026-report.md` vào những gì đã có từ trước. Các dòng có sẵn của làn khác thì ghi lại, không đụng.

## Báo cáo `docs/codex-queue/026-report.md`

- Số tên theo từng game và từng loại.
- Bảng "Cần Claude xem".
- Kết quả ba lệnh kiểm.

**Xong khi:** `NAMES_EN.md` có đủ ba game và ba lệnh kiểm đạt.
