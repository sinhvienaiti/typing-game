# Phiếu 242 · Last Line · Vẽ lại 11 icon HUD, kết quả và hồ sơ để đọc được ở cỡ thật

**Nguồn:**
- Phiếu `149-ts-ui-hud.md`, `150-*`, `151-*`, `152-*` và báo cáo của chúng; các lượt làm lại 237–240. Phong cách, tham chiếu bộ và khối STYLE-UI hướng B (Lightbearer, `docs/games/ART_DIRECTION_2026-10-28.md` §4.3) vẫn áp dụng. Phiếu này chỉ ghi chỗ khác.
- Lượt chấm thứ hai (31/10, khoảng 16:00, workflow `ui-art-pass-2`): hai giám khảo độc lập chấm UI Last Line **7,3** và **7,1** khi đã gắn vào game, ở 1280×720 và 1920×1080. Các icon dưới đây vẫn đọc sai **ở cỡ thật trong game**, dù trên tờ 256 px trông ổn.
- Bài học (Claude, 31/10): chấm icon ở cỡ vẽ trong game, không chấm trên tờ phóng to. Chi tiết sơn tay biến thành vệt mờ ở 16–24 px.
- Chủ dự án 31/10 05:15: Codex gần hết hạn mức, tạm chỉ giao việc tạo ảnh. Phiếu này chỉ có tạo ảnh và hậu kỳ.

**Báo cáo:** `docs/codex-queue/242-report.md` (tiếng Việt) và thư mục `docs/codex-queue/242/`. Model `gpt-6.1-sol`, mức `high`.

## Luật chung của đợt 242–246 (các phiếu sau dẫn lại mục này)

**Thứ tự ưu tiên:** đọc đúng ở cỡ thật > đẹp ở cỡ lớn. Một icon đẹp ở 256 px mà đọc sai ở 24 px là **trượt**.

**Khối SMALL-SIZE (EN), thêm vào sau khối KIND ICON trong mọi prompt icon của đợt này:**

```
SMALL-SIZE: designed to be read at 20-32 pixels in a game menu. One chunky, closed silhouette that fills the frame. A thick dark outline about 5-6 percent of the icon width all round. Large simple shapes only: no thin rods, spokes, rings, filigree, chains or hair-thin lines. At most one bright accent colour. Surface engraving only as faint texture that may vanish at small size. No text, no numbers, no frame or background plate.
```

- Last Line: thân sứ trắng ngà và thép, lõi lam như bộ đã nhận. Được thêm một điểm cam cảnh báo nhỏ khi giúp nghĩa (cảnh báo, hạ địch). Bớt hoa văn đồng: giám khảo chê bộ icon "filigree" lệch với giao diện công nghiệp sọc cảnh báo.
- Mỗi prompt = khối STYLE-UI của game + khối KIND ICON của phiếu gốc + khối SMALL-SIZE + phần riêng của ảnh (cột "Ý mới") + dòng nền.
- Đính kèm 2–3 icon **đã nhận và đọc tốt ở cỡ nhỏ** của cùng game làm tham chiếu bộ. Last Line: `ui/icons/streak.png`, `ui/icons/lock.png`, `ui/parts/mag-full.png`.

**Tên file (không ghi đè gì cả):**
- Lượt sinh: `<tên>.r2-tryN.png` và `<tên>.r2-tryN.prompt.txt` (N = 1, 2, 3), cùng thư mục với icon cũ.
- Bản chọn: `<tên>.r2.png` (1024², sRGB, RGBA), `<tên>.r2.256.png`, `.r2.128.png`, `.r2.64.png` (thu Lanczos thẳng từ bản gốc, không làm nét bản 64), `<tên>.r2.prompt.txt`.
- Icon mới chưa có file: `<tên>.png` và các bản thu như trên, lượt sinh `<tên>.tryN.*`.
- Claude là người trỏ game sang bản `.r2` khi gắn. Codex không sửa manifest, không chép vào `public/`.

**Nền và lề:** như phiếu 180 (Last Line nền trong suốt; hộp bao alpha > 16 có cạnh dài 68–72 % cạnh ảnh, lệch tâm ≤ 2 %). Công cụ trả khung khác 1024² thì thu đều cả vật rồi đệm trong suốt như báo cáo 149; **không co không đều**.

**Hậu kỳ:** `docs/games/ART_ACCEPTANCE.md` §5. Tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh. Không xoá, san phẳng hay phủ phần vẽ.

**Mỗi ảnh tối đa 3 lượt sinh.** Lượt sau sửa đúng chỗ trượt của lượt trước, ghi vào báo cáo.

**Kiểm bắt buộc (ghi số vào báo cáo, script lưu ở `docs/codex-queue/<số>/` và chạy lại được):**

1. **KA1 md5:** `md5 -r` mọi file trong các thư mục đích trước khi ghi và sau khi giao; `diff` chỉ có dòng thêm.
2. **Khổ và alpha sạch:** như Kiểm 2–3 của phiếu 180.
3. **Cỡ thật (mới, quan trọng nhất):**
   - Thu bản gốc về **đúng cỡ 720p và 1080p** ghi trong bảng của phiếu.
   - Đặt lên **mảnh UI thật của game** chứ không phải nền phẳng: Last Line cắt từ `ui/frames-epic/button.png` (hàng menu) và `ui/frames-epic/panel-large.png` (bảng), Dragonhold từ `ui/frames/`, Wordwoven từ `ui/frames-epic/` (bản `.v2` nếu có). Bên phải icon in nhãn tiếng Anh của hàng (cột "Nhãn") bằng font hệ thống, cao bằng 60 % cỡ icon.
   - Xuất các ô đó **ở đúng 1×, không phóng**, rồi thêm một bản phóng ×4 bằng point (nearest) để người chấm nhìn rõ pixel.
4. **Độ đặc (mới):** ở cỡ 720p, mặt nạ alpha > 128 sau phép mở (opening) với ô vuông 2×2 còn **≥ 80 %** số pixel. Nét mảnh sẽ trượt kiểm này. Ghi số từng ảnh.
5. **Độ phủ (mới):** diện tích alpha > 128 chiếm **≥ 30 %** diện tích hộp bao (bóng hình đặc, không phải nét vẽ). Ghi số.
6. **Tương phản:** như Kiểm 4 của 180, trên mảnh UI thật ở Kiểm 3.
7. **Khác dáng:** ở 32 px, IoU mặt nạ alpha với mọi icon trong cột "So với" ≤ 0,80. Ghi bảng.
8. **Đọc mù:** với mỗi ảnh, nhìn ô 720p ở 1× và viết ra 3–5 chữ nó trông giống gì, **trước** khi đọc lại cột "Ý mới". Nếu câu đó trùng hay gần với cột "Đang đọc thành" (giám khảo), ảnh trượt dù các số khác đạt.
9. **Tờ xem** `art-src/_review/<số>-sheet.jpg`:
   - hàng 1: bản gốc ở 256 px;
   - hàng 2: ô cỡ thật 1080p (1×) trên mảnh UI thật, kèm nhãn;
   - hàng 3: ô cỡ thật 720p (1×) trên mảnh UI thật, kèm nhãn;
   - hàng 4: bản phóng ×4 của hàng 3;
   - hàng 5: ô so sánh cạnh các icon ở cột "So với", cùng cỡ 720p;
   - hàng 6: icon cũ (bản đang dùng) cạnh bản mới, cùng cỡ 720p.
10. **KA5 tự chấm** (ART_ACCEPTANCE §2.2, 5 tiêu chí × 0–2) **ở ô 720p 1×**, không phải ở 256 px. "Đọc được" chỉ được 2 khi Kiểm 8 đạt.

**Giới hạn ảnh:** công cụ ảnh trả 429 hoặc báo thử lại sau thì dừng, giữ nguyên mọi file, viết báo cáo phần đã xong, và ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `CODEX-WAIT-UNTIL: unknown`). Lần chạy lại tiếp từ phần đã xong.

**Cấm (cả đợt):**
- ghi đè, đổi tên, xoá file có sẵn, kể cả mọi `try*` cũ;
- chép vào `public/`; sửa mã, manifest hay tài liệu (trừ báo cáo);
- dev server, trình duyệt, mạng ngoài công cụ tạo ảnh;
- mọi lệnh Git ghi;
- ghi vào game khác ngoài game của phiếu; Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`); `.wt-*`.

**Nhận:** Claude chấm lại **trong game** ở 1280×720 và 1920×1080 sau khi gắn, từ 8. Icon trượt lần này không có lượt thứ tư trong cùng phiếu.

## Việc của phiếu 242

Thư mục: `games/typing-survival/art-src/ui/icons/`.

| Tên | Nhãn (cho Kiểm 3) | Cỡ 720p / 1080p | Đang đọc thành (giám khảo) | Ý mới (EN, cho prompt) | So với |
|---|---|---|---|---|---|
| `next-stage` | Next stage | 28 / 40 | biển cấm vào, dấu trừ trong vòng | a bold right-pointing arrow whose arrowhead takes at least 60 percent of the width, bursting out of an open half-ring gate on its left (a C-shaped arc open to the right); never a closed ring, never a bar across a ring | `menu-play`, `streak`, `retry` |
| `bay-full` | (đầu bến, không nhãn) | 20 / 28 | vương miện, cái lược lam | three upright shells held together in a chunky clip, side view, bright tips, dark outline | `stat-evenness.r2`, `../parts/mag-full` |
| `kills` | Kills | 28 / 40 | lông vũ, bút lông, dao găm | a targeting reticle (four thick ticks around a centre) with a bold X struck through the centre, compact round silhouette, small orange hit glow | `stat-accuracy.r2`, `objective` |
| `stat-accuracy` | Accuracy | 28 / 40 | bông tuyết, la bàn | a bullseye target of three thick concentric rings with a short bolt stuck in the centre, seen front-on | `kills.r2`, `objective`, `clock.r2` |
| `stat-evenness` | Steadiness | 28 / 40 | ba cục pin, ống nghiệm | a spirit level: a thick horizontal bar with a centred window holding one cyan bubble | `bay-full.r2`, `stat-wpm.v2` |
| `stat-new-word` | New-word read | 28 / 40 | viên ngọc, đồng tiền | an open eye above a small word card (a tile with two text bars, no letters) | `stat-words`, `learning-rule` |
| `stat-words` (mới) | Words | 28 / 40 | (thẻ Words đang dùng icon bàn phím) | two stacked word cards with bold text bars, the front card tilted slightly, no letters | `stat-new-word.r2`, `keyboard.r2` |
| `keyboard` | Keyboard input | 28 / 40 | hộp quà, khiên, lưới 2×2, logo cửa sổ | a wide 2:1 keyboard slab seen from the front and slightly above, three rows of chunky keys and one long space bar | `../parts/keycap`, `stat-words` |
| `clock` | Time | 22 / 32 | vòng làm mới, gần giống icon Retry | a stopwatch: round body, a crown button on top, one thick hand, no arrows around the rim | `retry`, `stat-time` |
| `hazard` | Hazard | 28 / 40 | thùng cam, hòn đá nứt | a warning triangle with a thick orange-and-black striped rim and a jagged crack mark inside | `warning`, `surge` |
| `rift` | Rift | 24 / 32 | tia sét tím ngoằn ngoèo | a vertical tear in space shaped like an eye, widest in the middle, violet glow inside, jagged dark edges | `surge`, `warning` |

`music` **không vẽ lại**: Claude dùng `vol-music` (đã đọc đúng) cho hàng Music. `menu-profile`, `menu-armory`, `repair-pod`, `reduced-motion` đã qua lượt chấm hai, không động tới.

**Kiểm riêng:** `kills` cạnh `stat-accuracy` phải khác ngay ở 28 px (một là kính ngắm gạch chéo, một là bia vòng tròn); ghi IoU của cặp này.

## Chỉ được ghi

- `games/typing-survival/art-src/ui/icons/<tên>.r2-try*.*`, `<tên>.r2.*` cho mười tên có sẵn ở bảng trên; `stat-words.try*.*`, `stat-words.*` (mới).
- `games/typing-survival/art-src/_review/242*`.
- `docs/codex-queue/242-report.md`, `docs/codex-queue/242/`.
