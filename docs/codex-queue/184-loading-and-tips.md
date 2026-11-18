# Phiếu 184 · Ba game · Tranh màn tải và ba tranh mẹo chơi mỗi game (12 ảnh)

**Vì sao:** lúc tải map và các thẻ mẹo hiện chỉ có chữ. Chủ dự án 28/10: mọi chi tiết UI có hình thật. Chủ dự án 29/10: giao thêm việc cho Codex.

**Báo cáo:** `docs/codex-queue/184-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

## Luật chung

Như phiếu 176 (`docs/codex-queue/176-portal-covers.md`, đọc trước): repo cha, ảnh là media không vào Git, tối đa 3 lượt sinh mỗi ảnh, giữ `.tryN.*`, mức nhận M ≥ 8 theo game thương mại và Q ≥ 8, không chữ trong ảnh, cấm git có ghi, cấm sửa mã, cấm Tu Tiên, KA1 md5 trên thư mục đích. Phong cách theo khối STYLE của từng game trong `docs/games/ART_DIRECTION_2026-10-28.md` (Wordwoven §2.2, Dragonhold §3.2, Last Line §4.3 hướng B); đính kèm ảnh chủ đạo đã có của game làm tham chiếu nhân vật và màu.

## Ảnh

Mỗi game: `loading` 1920 × 1080 (một cảnh rộng của map 1, chừa dải dưới 20 % yên cho thanh tải và câu mẹo) và ba tranh mẹo `tip-1`, `tip-2`, `tip-3` 1024 × 640 (minh họa một thao tác, không chữ), ở `games/<id>/art-src/ui/loading/`.

| Game | Ba mẹo |
|---|---|
| Dragonhold | gõ trọn từ để rồng phun lửa; đặt bẫy trên làn trước đợt; gõ không sai để có đòn mạnh |
| Wordwoven | gõ lời gọi để dân làng xây nhà; Word Shot từ tháp; giữ chuỗi gõ đúng để lên bậc |
| Last Line | hai súng canh bắn theo từ ở hai bến; gõ đúng liền tay để giữ đường; chọn súng trước ải |

**Kiểm:** khổ đúng; dải dưới 20 % của `loading` đủ tối cho chữ trắng WCAG ≥ 7; mỗi tranh mẹo đọc ra thao tác ở 320 × 200; tờ `games/typing-defense/art-src/_review/184-sheet.jpg`; KA5.

**Xong khi:** mười hai ảnh có bản chọn, tự chấm M ≥ 8 và Q ≥ 8.
