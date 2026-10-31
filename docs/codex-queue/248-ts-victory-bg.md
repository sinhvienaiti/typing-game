# Phiếu 248 · Last Line · Nền màn thắng v2: phải đọc ra chiến thắng

**Nguồn:**
- Phiếu `121-ts-menu-backgrounds.md` và báo cáo của nó. Khối STYLE, câu REF, thang M/Q, khổ 1536 × 1024, cách cắt 16 : 9 (`1536x864+0+80`) và Kiểm của 121 vẫn áp dụng. Phiếu này chỉ ghi chỗ khác.
- Claude nhận `results-win-bg` của 121 ngày 31/10 16:30 và gắn vào game. Giám khảo độc lập chấm màn thắng **7** trong game:
  - ảnh không đọc ra chiến thắng: bầy quái vẫn lao tới, nổ ở góc trên phải, mặt sàn cùng màu đá vụn tối với màn thua, không có gì vàng hay rực rỡ;
  - nhân vật bị kẹp giữa mép phải của bảng kết quả (khoảng 77 % bề ngang ở 1280 × 720) và mép màn hình; găng tay chạm khung, áo choàng bị màn hình cắt.
- So với màn thắng của Clash Royale hay Kingdom Rush, khoảnh khắc này còn phẳng.
- Chủ dự án 31/10 05:15: Codex gần hết hạn mức, tạm chỉ giao việc tạo ảnh. Phiếu này chỉ có tạo ảnh và hậu kỳ.

**Báo cáo:** `docs/codex-queue/248-report.md` (tiếng Việt) và thư mục `docs/codex-queue/248/`. Model `gpt-6.1-sol`, mức `high`.

## Việc

Một ảnh, `games/typing-survival/art-src/ui/screens-epic/results-win-bg.v2.png` (cùng `.v2.prompt.txt`, `.v2.512.png`), lượt sinh `results-win-bg.v2-tryN.*`, tối đa 3 lượt. Đính kèm `art-src/concepts/b-lightbearer-keyart.png` (câu REF) và `results-win-bg.png` hiện tại để giữ nhân vật, vật liệu và nơi chốn.

Phần riêng (EN, dán sau STYLE, rồi dòng REF):

`Scene: the moment of victory at dawn on the causeway. The Lightbearer stands tall and calm, facing the viewer at three-quarter view, one gauntlet raised, both sentinel guns hovering at her shoulders in a quiet salute. The last foes have burst into drifting golden sparks; no foe is still charging and nothing is exploding. A broad wave of warm gold light breaks over the black hole's ring behind her like a sunrise, washing the wet deck in gold and lighting long rim light on her armour and cape. Light dust and embers float upward. The mood is triumphant, majestic and hopeful, clearly brighter and warmer than a defeat. The hero stands in the right third: her whole figure, cape included, lies between 66 % and 92 % of the image width, with clear space to the right edge. The left 62 % of the image is a calmer, darker stretch of deck and distant towers for the results panel.`

**Kiểm riêng (thêm vào Kiểm của 121):**
1. **Chỗ nhân vật:** trên bản cắt 16 : 9, hộp bao của nhân vật cùng áo choàng nằm trọn trong 66–92 % bề ngang. Ghi toạ độ (đo tay trên ảnh, ghi cách đo).
2. **Vùng bảng:** 8–62 % bề ngang, 15–90 % chiều cao của bản cắt: độ lệch chuẩn luma ≤ 0,14, luma trung bình ≤ 0,40.
3. **Khác màn thua:** luma trung bình của bản cắt cao hơn `results-lose-bg` ít nhất 0,04; hue trung vị nằm trong dải vàng cam (30–55°). Ghi số.
4. **Dựng thử** `_review/248-mock.jpg`: bản cắt 16 : 9 có một khối kính tối 60 % ở 8–62 % bề ngang (chỗ bảng kết quả), đặt cạnh `results-lose-bg` dựng cùng cách. Xem: bảng đọc rõ, nhân vật không bị bảng hay mép màn che, hai màn khác nhau ngay khi nhìn.

**Giới hạn ảnh:** công cụ ảnh trả 429 hoặc báo thử lại sau thì dừng, giữ nguyên mọi file, và ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM`.

## Chỉ được ghi

- `games/typing-survival/art-src/ui/screens-epic/results-win-bg.v2*` (mới).
- `games/typing-survival/art-src/_review/248*`.
- `docs/codex-queue/248-report.md`, `docs/codex-queue/248/`.

## Cấm

- Sửa hay xoá `results-win-bg.png` và mọi ảnh đã có.
- Chép vào `public/`, sửa `selection.json` hay mã.
- Lệnh Git ghi; dev server, trình duyệt.
- Tu Tiên; `.wt-*`.

## Nhận

- Claude chấm từ 8 theo thang M/Q của 121, rồi chấm lại trong game ở 1280 × 720 và 1920 × 1080 sau khi gắn.
