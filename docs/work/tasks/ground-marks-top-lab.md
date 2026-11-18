# Dấu đất nhìn từ trên vào lab · 11/11/2026

**Ai làm:** phiên lab-flipbooks, trong `games/.wt-ic-lab-all` (nhánh `codex/lab-all`). **Không commit, không push.** Chỉ đụng tệp flipbook và khai báo của các dấu dưới đây; **không đụng tệp của chiêu sét** (phiên khác đang làm `docs/work/tasks/five-thunder-lab.md`).

## Việc
Anh đã chọn bản Codex cho dấu đất Ám và Quang (11/11). Video Firefly của chúng đã có, nhìn thẳng từ trên, tròn đều:
- `V/i2v-dark-ground-mark-top-i2v3/take{1,2}.mp4`
- `V/i2v-light-ground-mark-top-i2v3/take{1,2}.mp4`
- `V/i2v-thunder-scorch-crack-top-i2v3/take{1,2}.mp4` (chỉ làm flipbook và ghi vào manifest; **không nối vào chiêu**, phiên kia nối)

`V = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video`.

1. Với mỗi việc, chọn bản tốt hơn theo kiểm máy như đợt 53 clip (đoạn dùng được, không vật lạ, nằm trọn khung, nền đen); ghi lựa chọn và lý do vào `.local/s2/picks-i2v3.json` (thêm mục, không sửa mục cũ).
2. Làm flipbook (atlas, ktx2, mp4 1080p) bằng đúng công cụ đã dùng cho 53 clip; giữ file cũ dưới tên `.old`.
3. Thay dấu đất Ám và Quang trong lab bằng flipbook mới. Dấu là thẻ phẳng trên đất: kiểm rằng nó **tròn khi nhìn từ trên** và thành elip đúng phối cảnh ở camera chơi, không bị nghiêng hai lần.

## Xong khi
- Thư mục `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/ground-marks-top/` có `ABOUT.md` và tấm trước/sau của hai dấu ở camera chơi và camera nhìn từ trên.
- Test liên quan chạy qua. Xoá khung thô của mình. Báo cáo ≤ 200 chữ.

## Kết quả (lab-flipbooks, 11/11 23:58)
- Chọn take1 cho cả ba (kiểm máy + dải khung; lý do ghi trong `.local/s2/picks-i2v3.json`, 3 mục thêm cuối). Take2 của cả ba đều có khói trôi lệch hoặc lan tới mép.
- `dark-ground-mark`, `light-ground-mark`: thay tại chỗ, cùng id/vai/thư mục, ô mới **512×512** (tròn từ trên; ô cũ 512×288 là elip xiên vẽ sẵn), 31 khung @ 6 fps, `view: "top"`, `previous` ghi bản cũ; file cũ giữ `<id>.old.atlas.png/.json`. Ám vẫn `layer: rim`. Có mp4 1080p (`video`, 1080×1080, 121 khung) và `.uastc.ktx2` (md5 khớp).
- `thunder-scorch-crack-top` (thư mục `thunder`): mục mới, `role: "scorch"` + `roleHint: "groundMark"` để không lọt vào vòng chọn `groundMark` của chiêu Lôi; phiên chiêu sét nối. Có atlas, ktx2, mp4.
- Lab vẽ dấu bằng `layFlat` với `span = size` (thẻ vuông phẳng trên đất): từ trên nhìn tròn, ở camera chơi thành elip đúng phối cảnh, không nghiêng hai lần (`light-after-pillar-marks-play.jpg`). Bản cũ cũng đã được ép vuông nên khác biệt ở camera chơi là chi tiết dấu, không phải hình dạng.
- Bảng chủ `tools/vfx-flipbook/immortality-cultivation.json`: 3 dòng mới (`aspect 1:1`, ô 512², `frames 36` vì atlas 8×8×512 = 4096² vượt giới hạn 12 Mpix của bộ nén KTX2).
- Test: `vitest` clip-skills, element-clips, painted-sigils, meteor-rain: 105/105 qua. `validate-manifests`: mọi manifest đọc được (riêng `sigils` rỗng, của phiên khác, như trước).
- Lab 3146 đã tắt khi nhận việc; khởi động lại bằng `ic-lab-combined` (worktree `.wt-ic-lab-all`), trang hay tải lại vì phiên chiêu sét đang sửa `src/`.
