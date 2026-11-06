# Phiếu 329 · Tu Tiên · Lab: panel nút gọn lại, không che màn hình (tên ngắn, chữ đầy đủ khi rê chuột, phím H thu gọn)

Anh (06/11 21:25): "cái tên kỹ năng dài quá che hết cả màn hình game r, sao chưa chỉnh lại vậy, kêu codex chỉnh lại đi". Panel nút bên trái của lab rộng khoảng 1.000 px vì các nút phím 8, 9, M, K, C ghi cả câu giải thích tiếng Việt.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/329-report.md` (tiếng Việt, ngắn).

## Nơi làm
- Worktree: `W = games/.wt-ic-lab-panel`, nhánh `codex/lab-compact-panel`, tách từ `codex/lab-hybrid-flipbook` (`2185b5e`, đã có thanh chiêu và cảnh A/B). Claude đã tạo sẵn, kèm liên kết `art-src` và `node_modules`.
- **Được ghi:** chỉ `W/src/lab/skills-main.ts` và báo cáo.
- **Cấm:** lệnh git ghi; sửa file khác; mở cổng mạng; mở trình duyệt.

## Lời giải đã chốt (tất cả trong khối `// Panel.` của `skills-main.ts`, khoảng dòng 1764–1955, trừ hai dòng ở cấp module)
1. **Cấp module**, ngay cạnh `let bar: SkillBar | null = null;`: thêm `let togglePanel: (() => void) | null = null;`.
2. **Bộ phím** (trong `window.addEventListener("keydown", …)`): thêm nhánh `else if (e.key === "h" || e.key === "H") togglePanel?.();`. Phím H hiện chưa dùng (đã kiểm bằng grep).
3. **Tên ngắn cho nút.** Giữ nguyên mảng `names`: thanh chiêu vẫn đọc tooltip từ đó. Thêm `["H", "Panel: collapse / expand"]` vào cuối literal `names`, sau `I`. Thêm hằng `SHORT: Record<string, string>` ngay sau khối `if (greybox !== null) { … }`:

   | Phím | Nhãn ngắn |
   |---|---|
   | 0 | Flying Sword |
   | 1 | Threefold Sword |
   | 2 | Cloud-Piercing Line (khi `greybox !== null`: Twin Dragons, grey box) |
   | 3 | Sword Aegis |
   | 4 | Flowing-Light Step |
   | 5 | Falling Sword Array |
   | 6 | Milky-Way Sword Rain |
   | 7 | Sword Convergence |
   | 8 | Pillars & ultimates |
   | 9 | Skills expansion |
   | M | Meteor rain |
   | K | Word streak |
   | C | Channel |
   | B | Enemy blow |
   | R | Reset |
   | W | Next sword |
   | E | Next element |
   | Z | Zoom |
   | O | Orbit camera |
   | A | Sword aura |
   | T | Word tags |
   | I | Icon style |
   | H | Hide panel |
   | L | Grey box: next layout |
   | N | Grey box: restore |
   | V | Grey box: boss at A |

4. **Nút:** trong vòng `for (const [key, name] of names)`:
   - `b.textContent = key + " · " + (SHORT[key] ?? name)`;
   - `b.title = name` (câu đầy đủ hiện khi rê chuột);
   - style: `text-align:left;padding:3px 8px;font-size:12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;background:rgba(14,18,26,.78);color:#e6e9ef;border:1px solid #3a4558;border-radius:5px;cursor:pointer`.
5. **Panel gọn:** đổi `panel.style.cssText` thành `position:fixed;left:12px;top:12px;z-index:10;width:240px;max-height:calc(100vh - 24px);overflow-y:auto;display:flex;flex-direction:column;gap:4px;font:12px system-ui;color:#e6e9ef`.
6. **Thu gọn bằng H hoặc bấm tiêu đề:**
   - Tạo `const content = document.createElement("div")` với style `display:flex;flex-direction:column;gap:4px`.
   - **Mọi** lệnh `panel.append(…)` hiện có trong khối Panel (nút phím, WPM, typed, các ô chọn, aura…) đổi thành `content.append(…)`.
   - Tạo nút tiêu đề `header` (chữ `Lab panel · H`, cùng style nút ở bước 4, thêm `font-weight:600`), `header.onclick = () => togglePanel?.()`.
   - Trước dòng `document.body.append(panel);` thêm `panel.append(header, content);`.
   - Gán `togglePanel` (trong khối Panel, trước `document.body.append(panel)`):
     ```ts
     let collapsed = false;
     try { collapsed = localStorage.getItem("lab.panel.collapsed") === "1"; } catch { /* private mode */ }
     const applyPanel = () => {
       content.style.display = collapsed ? "none" : "flex";
       panel.style.width = collapsed ? "auto" : "240px";
     };
     applyPanel();
     togglePanel = () => {
       collapsed = !collapsed;
       applyPanel();
       try { localStorage.setItem("lab.panel.collapsed", collapsed ? "1" : "0"); } catch { /* ignore */ }
       bar?.avoid(panel);
     };
     ```
   - Giữ nguyên `bar?.avoid(panel);` ngay sau `document.body.append(panel);`.

## Kiểm
- `cd W && npx tsc --noEmit` sạch.
- `cd W && npx vitest run tests/lab tests/view --maxWorkers=4` qua; trước phiếu là 45 file / 530 test.
- `git diff --stat` chỉ có `src/lab/skills-main.ts`.

## Xong khi
Các lệnh kiểm qua. Báo cáo ghi số dòng đổi, kết quả kiểm, và độ rộng panel mới. Claude kiểm trong trình duyệt sau.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`); làm xong phiếu thì không ghi.
