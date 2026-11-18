# Phiếu 322 · Tu Tiên · Lab: thanh chiêu có biểu tượng ở đáy màn hình (phím 0–9), đổi kiểu biểu tượng

Anh (06/11 19:00): "cho codex 1 làn xử lý ảnh, 1 làn xử lý lab". Codex vừa vẽ 110 biểu tượng kỹ năng (phiếu 316, 319) theo hai kiểu **ink-gold** và **jewel-crest**. Luật đã học: biểu tượng phải được xem ở đúng cỡ thật, đúng chỗ của nó trên thanh chiêu, không chỉ trên tấm ghép. Phiếu này thêm vào lab một thanh chiêu ở đáy màn hình, để anh xem và đổi qua lại hai kiểu.

**Model `gpt-6.1-sol`, mức `xhigh`.** Báo cáo: `docs/codex-queue/322-report.md` (tiếng Việt, ngắn).

## Nơi làm
- Worktree riêng (Claude đã tạo): `W = games/.wt-ic-lab-skillbar`, nhánh `codex/lab-skill-bar`, tách từ `claude/lab-element-kits` (`b8ebd51`). `W/art-src` và `W/node_modules` là liên kết sang `games/immortality-cultivation/`.
- **Được ghi:** `W/src/lab/skill-bar.ts` (mới), `W/src/lab/skills-main.ts`, `W/src/lab/clip-skills.ts` (chỉ thêm một hàm đọc, xem bước 2), `W/tests/lab/skill-bar.test.ts` (mới), và báo cáo.
- **Cấm:** mọi lệnh git ghi; sửa file khác; mở cổng mạng; sửa ảnh trong `art-src`.

## Ảnh biểu tượng
- Thư mục phục vụ: `/art-src/lab/ui/skill-icons/` (`W/art-src/lab/ui/skill-icons/`).
- Tên tệp: `<style>-<id>.v1-<try>-48.png`.
  - `<style>` là `ink-gold` hoặc `jewel-crest`.
  - `<try>` là `try2` cho `flowing-light-step` và `asura-six-arms-avatar`; mọi id khác dùng `try1`.
- Dùng đúng bản 48 px, hiện ở 48×48 CSS px (`image-rendering: auto`), không phóng to hay thu nhỏ.

## Lời giải đã chốt
1. **`src/lab/skill-bar.ts` (mới)** xuất:
   - `type IconStyle = "ink-gold" | "jewel-crest"`.
   - `KEY_ICONS: Readonly<Record<"0"|"1"|"2"|"3"|"4"|"5"|"6"|"7", string | null>>`, bảng cố định:

     | Phím | Id |
     |---|---|
     | 0 | `flying-sword` |
     | 1 | `sword-qi-strike` |
     | 2 | `null` (phím 2 của lab đang là lưỡi liềm Nhất Tuyến Xuyên Vân, chưa có biểu tượng); khi lab chạy với `?key2=twin-pearl` thì dùng `twin-dragons` |
     | 3 | `returning-sword-guard` |
     | 4 | `flowing-light-step` |
     | 5 | `falling-sword-array` |
     | 6 | `milky-way-sword-rain` |
     | 7 | `myriad-edges-hear-the-edict` |

     Ghi chú trong mã: phím 7 của lab tên "Vạn Kiếm Triều Tông", biểu tượng theo danh sách sản xuất là "Vạn Phong Thính Chiếu"; anh sẽ chốt tên.
   - Hàm thuần `iconSrc(style: IconStyle, id: string, base = "/art-src/lab/ui/skill-icons/"): string` theo luật tên ở trên.
   - Hàm thuần `keyIcon(key: string, key2Twin: boolean): string | null`: phím `"2"` khi `key2Twin` → `"twin-dragons"`, còn lại `(KEY_ICONS as Readonly<Record<string, string | null>>)[key] ?? null` (phím ngoài 0–7 → `null`; viết như vậy để `strict` không báo TS7053).
   - `type SkillBarState = { style: IconStyle; slots: { key: string; id: string | null; src: string | null; missing: boolean }[] }` (xuất).
   - Lớp `SkillBar`:
     - `constructor(parent: HTMLElement, opts: { style: IconStyle })`.
     - `setSlot(key: string, id: string | null, name: string)`: đặt biểu tượng và tooltip của một ô.
     - `setStyle(style)`: đổi kiểu, nạp lại mọi `<img>`.
     - `flash(key)`: nhấp sáng ô khi chiêu được tung.
     - `avoid(el: HTMLElement)`: né panel. Đặt thanh ở giữa đáy, rồi nếu khung của thanh giao với `el.getBoundingClientRect()` thì đặt `left = Math.max(12, Math.min(r.right + 12, innerWidth - barWidth - 12))` px và bỏ `translateX(-50%)`. Nhớ `el` và chạy lại khi `resize`.
     - `state(): SkillBarState` để thăm dò.
   - Constructor dựng sẵn đủ 10 ô (phím 0–9), ban đầu ô nào cũng ở trạng thái "no icon".
   - `skill-bar.ts` **không chạm `document` hay `window` ở cấp module** (chỉ trong constructor và phương thức), để test chạy được trong môi trường node.
2. **`src/lab/clip-skills.ts`:** thêm vào `ClipSkillRunner` một hàm đọc công khai:
   ```ts
   selectedId(): string | null {
     return this.showcase.current() ?? this.showcase.ids()[0] ?? null;
   }
   ```
   Không sửa gì khác ở file này.
3. **Giao diện (DOM, chỉ trong lab):**
   - Một dải cố định ở giữa đáy, cách đáy 16 px, `z-index` 8: dưới cut-in (`cutin.ts`, gốc tràn màn `z-index:9`), bộ đếm chuỗi và grey box (9), panel (10); trên thẻ chữ (5). Không được che cut-in.
   - Panel bên trái rộng khoảng 970 px, cao khoảng 1.030 px. Thanh né panel bằng `bar.avoid(panel)` (bước 1). **Gọi ngay sau dòng `document.body.append(panel)`** (khoảng dòng 1879), không gọi lúc tạo thanh: lúc đó panel chưa nằm trong trang nên khung của nó toàn số 0.
   - 10 ô cho phím 0–9, ô 56×56 px, cách nhau 6 px. Mỗi ô có ảnh 48 px ở giữa và chữ số phím ở góc dưới phải, cỡ 11 px, màu `#e6e9ef`, có bóng chữ.
   - Nền dải `rgba(14,18,26,.78)`, viền `1px solid #3a4558`, bo 8 px, giống các nút panel. Tooltip (`title`) là tên kỹ năng tiếng Anh.
   - **Ô chưa có biểu tượng:** khi id là `null` hoặc ảnh lỗi (`onerror`), ô để trống, chỉ có chữ số và dòng chữ nhỏ "no icon" màu `#8a94a6`. Không vẽ hình thay thế nào bằng CSS hay canvas: luật cấm hình vẽ bằng mã.
   - **`flash(key)`:** viền ô sáng màu sức gõ `#7FF5E0` (`box-shadow 0 0 10px`) và phóng `scale(1.08)` rồi về 1 trong 350 ms, bằng CSS transition. Đây chỉ là phản hồi giao diện, không vẽ hình.
4. **`skills-main.ts`:**
   - **Phạm vi biến:** khai `let bar: SkillBar | null = null;` ở cấp module, trước bộ xử lý phím (khoảng dòng 1652). Tạo thanh **bên trong** khối `if (params.get("ui") !== "0") {` của panel, ngay sau khối `if (greybox !== null) { names[2] = …; names.push(…) }` (khoảng dòng 1737), khi `params.get("bar") !== "0"`. Như vậy ảnh chụp cũ dùng `ui=0` giữ nguyên.
   - Kiểu ban đầu từ `?icons=jewel` (→ `jewel-crest`), mặc định `ink-gold`.
   - Phím `I` (cả `i`) đổi kiểu, chỉ khi `bar !== null`. `I` hiện chưa dùng. Thêm nút `["I", "Icon style: ink-gold / jewel-crest"]` vào **cuối** literal `names`, sau `T`.
   - **Ô 0–7:** `bar.setSlot(k, keyIcon(k, greybox !== null), tên)`. **Tooltip:** phần sau dấu ` · ` cuối cùng của `names[k][1]`; riêng phím 2 khi `greybox !== null` dùng `Twin Dragons, One Burning Pearl`.
   - **Ô 8 và 9:** khai `function refreshClipSlots(): void` ở cấp module, cạnh `let bar`:
     - mở đầu bằng `if (bar === null) return;` (phím 8, 9 vẫn chạy khi `ui=0` hay `bar=0`);
     - nhớ id cuối của mỗi ô trong hai biến cấp module, khởi đầu là `undefined`, để lần gọi đầu luôn đặt ô;
     - đặt ô 8 từ `clipSkills.selectedId()` và ô 9 từ `clipSkills9.selectedId()`, chỉ gọi `setSlot` khi id đổi; tooltip là chính id.

     Gọi `refreshClipSlots()`:
     - lúc tạo thanh;
     - **đăng ký mới** `showcase.onList(refreshClipSlots)` và `expansion.onList(refreshClipSlots)`, ngay sau khi tạo thanh. Hiện chỉ có `sc.onList(fill)` (khoảng dòng 1837); `onList` cộng thêm vào danh sách nên đăng ký thêm là an toàn. Danh sách chỉ đầy khi manifest tải xong (`showcase.ts` khoảng dòng 503), nên lúc đầu `selectedId()` là `null`;
     - sau mỗi nhánh 8, 9 của bộ phím, cả chọn lẫn tung;
     - trong hai hàm `cast` của `showcaseList` (khoảng dòng 1849 và 1856).
   - **Nhánh 8, 9 của bộ phím** hiện là một biểu thức `void (cond ? selectNext() : cast())`. Tách thành `if/else`. Gọi `bar?.flash("8")` hoặc `bar?.flash("9")` ở nhánh tung, với chuỗi `"8"`/`"9"`, không dùng `e.key` (Shift cho ra `*` hay `(`).
   - **Phím 0–7:** đổi nhánh `if (slot) type(slot)` thành `if (slot) { const held = cutin.active; type(slot); if (!held) bar?.flash(e.key); }`. Phải đọc `cutin.active` **trước** `type()`: `type()` bỏ qua phím khi cut-in đang chạy, còn phím 6 (`type("k5")`) tự mở cut-in ngay, nên đọc sau sẽ luôn là `true` và phím 6 không bao giờ sáng.
   - **`__lab`:** biến này có kiểu (`declare global { … __lab?: { … } }`, khoảng dòng 2038). Thêm `skillBar(): SkillBarState | null;` vào kiểu đó, và mục `skillBar: () => bar?.state() ?? null` vào literal `window.__lab = { … }` (khoảng dòng 2328, trong async IIFE).
5. **Test `tests/lab/skill-bar.test.ts`:** môi trường node như cấu hình hiện có, không thêm `@vitest-environment`, không cài gói nào. Chỉ test hàm thuần:
   - `iconSrc` cho `ink-gold`/`jewel-crest`, id thường (`try1`) và hai id `try2`.
   - `KEY_ICONS` đủ 8 phím 0–7, phím 2 là `null`.
   - `keyIcon("2", true)` là `twin-dragons`, `keyIcon("2", false)` là `null`, `keyIcon("0", false)` là `flying-sword`, `keyIcon("8", false)` là `null`.
   - Mọi id khác `null` trong `KEY_ICONS`, cộng `twin-dragons`, có tệp thật ở cả hai kiểu. Thư mục: `fileURLToPath(new URL("../../art-src/lab/ui/skill-icons/", import.meta.url))`; dùng `it.skipIf(!existsSync(dir))` khi thư mục không có.

## Ghi chú từ phản biện vòng 3 (PASS)
- `bar` có thể là `null` (`?bar=0`), nên viết `bar?.avoid(panel)`.
- Tooltip của ô 8/9 khi id là `null`: truyền `id ?? ""`.
- Báo cáo ghi bề rộng cửa sổ tối thiểu để thanh không nằm dưới panel (khoảng 982 + 12 + bề rộng thanh + 12 px).

## Kiểm
- `cd W && npx tsc --noEmit` sạch.
- `cd W && npx vitest run tests/lab/skill-bar.test.ts tests/lab/clip-skills.test.ts tests/lab/showcase.test.ts` qua.
- `cd W && npx vitest run tests/lab` qua (không làm hỏng test lab khác).
- Không chạy trình duyệt. Claude sẽ kiểm trong lab sau.

## Xong khi
Các lệnh kiểm qua. Báo cáo ghi:
- file đã sửa, số dòng thêm, kết quả từng lệnh kiểm;
- id nào của phím 8, 9 không có biểu tượng. Đọc `art-src/lab/vfx/ult/manifest.json` và `art-src/lab/vfx/expansion/manifest.json`, chỉ giữ id qua bộ lọc `roles` và `rejected` của `ULT_SHOWCASE`/`EXPANSION_SHOWCASE` (`showcase.ts` khoảng dòng 189–196), rồi so với tệp ảnh. Dự kiến: phím 8 thiếu `sky-gate-open-close` (`ult-dark` bị loại), phím 9 không thiếu;
- lưu ý: trên màn hình DPR 2, ảnh 48 px hiện phóng 2 lần.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
