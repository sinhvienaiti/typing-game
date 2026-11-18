# Làn Codex C · Duyệt chất lượng từng video Firefly, chỉ ra clip phải làm lại

Anh (07/11 01:50): "tôi muốn bạn cho codex review từng cái chưa được review để xem cái nào k đạt thì sẽ cần tạo lại, tôi cần video phải đẹp, phong cách, đầy đủ các chi tiết, bùng nổ, hiệu ứng đẹp, mạnh mẽ, 1 số video kém chất lượng, hoặc quá cơ bản thì đều cần được xử lý làm lại".

**Model `gpt-6.1-sol`, mức `high`.** Mỗi lần chạy làm **đúng một đợt**: file đầu tiên trong `.local/video-review/todo/` (thứ tự tên) mà **chưa có** `.local/video-review/results/<cùng tên>`. Làm xong đợt đó thì dừng.

## Dữ liệu
- `.local/video-review/clips.json`: mỗi bản take có `key`, `job`, `take`, `sheet`, `video`, `mode` (image-to-video hay text-to-video), `still`, `use`, `prompt`, `loop`.
- `sheet` là tấm 6 khung (10, 25, 40, 55, 70, 90 % thời lượng, xếp 3×2, mỗi ô 320 px trên nền đen). Xem từng tấm bằng `view_image`, mỗi lần một tấm.
- Nếu tấm ghép không đủ để kết luận (chuyển động, chỗ nối vòng lặp), được trích thêm khung bằng `ffmpeg` vào `.local/video-review/tmp-<đợt>/`, rồi xoá khi xong đợt.

## Thước chấm (thang 1–10 cho mỗi mục)
So với VFX của game thương mại cao cấp phong cách anime/donghua (Genshin Impact, Honkai: Star Rail, Wuthering Waves, Naraka), không so với các clip khác trong đợt.
1. **Cuốn hút, phong cách:** sang, đẹp, hiện đại, đúng chất tiên hiệp thần thoại; không quê, không nhạt, không chung chung.
2. **Chi tiết, nhiều lớp:** lõi sáng, quầng, lấp lánh, đốm sáng, lớp phụ; không phải một hình phẳng.
3. **Lực, bùng nổ:** với đòn, chiêu, nổ, quái, boss phải mạnh và dứt khoát. Với vòng lặp nền, UI, hào quang thì chấm độ thanh lịch và sống động thay cho lực.
4. **Chuyển động:** mượt, có nhịp rõ (tụ, bung, tan), không đứng im, không biến dạng méo mó.
5. **Đúng việc:** đúng `use` và `prompt` (hình, màu hệ, vai trò). Image-to-video phải giữ đúng hình của ảnh đầu.
6. **Kỹ thuật:** hình chính nằm trong khung, nền đen sạch; không chữ, logo, khung, vật thừa (tay cầm, người, đồ vật lạ); vòng lặp (`loop: true`) không có chỗ giật rõ.

**Cách cho điểm:**
- `overall` là phán đoán tổng, không phải trung bình. 8 nghĩa là "đưa vào game cao cấp được ngay". Hình cơ bản, màu phẳng, ít lớp, chuyển động yếu thì ≤ 6.
- Đừng dễ dãi: thà ít clip đạt mà đạt thật.

**Kết luận mỗi bản take:**
- `PASS`: `overall` ≥ 8 và không có lỗi nặng ở mục 6.
- `REDO`: dưới 8, hoặc có lỗi nặng.
- `DROP`: clip thử hay bản thừa không cần cho game. Ghi lý do.

Việc có nhiều take thì chọn `best`, take tốt nhất. Việc đạt nếu `best` đạt; các take còn lại không cần làm lại.

## Prompt làm lại (cho mỗi REDO, viết `newPrompt` tiếng Anh)
- Mở đầu đúng như prompt cũ: `High-end donghua animation effect, glowing, soft bloom, rich layered detail:`.
- Sửa đúng điều đã chê. Thêm lớp hào quang quanh hình chính: lấp lánh, sao nhỏ, đốm sáng mịn, quầng và vòng sáng mềm, viền lung linh. Đòn và chiêu phải bùng nổ, nhiều lớp. Màu theo hệ của việc.
- Giữ nền đen thuần, camera cố định, lề rộng, không chạm mép khung.
- **Image-to-video:** giữ nguyên ảnh đầu (không đổi `still`), chỉ đổi lời tả chuyển động. Hình của ảnh không được biến mất hay đổi dạng.
- **Text-to-video:** chỉ khi `kind` là `material`, cho chất liệu thuần (lửa, khói, tia, bụi, sóng, đốm). Nếu clip tả một vật có hình dạng rõ (rồng, binh khí, ấn, người) mà là text-to-video, ghi `needsStill: true` và mô tả ngắn ảnh cần vẽ trước. Không viết prompt cho loại này.
- Không nhắc tên game, hãng hay nhân vật có bản quyền trong prompt.

## Đầu ra mỗi đợt
1. `.local/video-review/results/batch-XX.json`: mảng các mục `{ key, job, take, kind, scores: {appeal, detail, power, motion, fit, technical}, overall, verdict, best, reasons, newPrompt, needsStill, stillBrief }`.
   - `kind`: `material` khi clip chỉ là chất liệu thuần (tia lửa, khói, bụi, sương, dòng chảy, đốm sáng), `shaped` khi có hình rõ (vòng, cổng, ấn, cột, rồng, binh khí, mảnh vỡ có dáng, khung thẻ). Luật của anh (05/11): `shaped` bắt buộc vẽ ảnh và được duyệt trước, rồi mới làm image-to-video; chỉ `material` được làm từ chữ. `reasons` ngắn, tiếng Việt, nói rõ điều thấy được.
2. Thêm vào `docs/codex-queue/laneC-report.md` một đoạn ≤ 8 dòng cho đợt:
   - số take đã xem, số PASS, REDO, DROP;
   - 3 lỗi hay gặp nhất;
   - các job tốt nhất làm mốc.

## Ranh giới
- **Chỉ ghi:** `.local/video-review/results/`, `.local/video-review/tmp-*`, báo cáo.
- **Không sửa:** video, ảnh, manifest, hàng việc Firefly hay mã.
- **Không:** lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Đạt khi
- Mọi `key` trong đợt có đúng một mục trong file kết quả, và file đọc được bằng `JSON.parse`.
- Mỗi REDO có `newPrompt`, hoặc có `needsStill: true` kèm `stillBrief`.

## Hết hạn mức
Ghi phần đã xong vào file kết quả (đợt dở dang ghi tên `batch-XX.partial.json`). Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
