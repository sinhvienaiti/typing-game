# Phiếu 389: Dựng lại tuyệt kỹ băng bám theo ảnh tham chiếu 386

Phản biện: PASS (Sonnet, 16/11)

## Bối cảnh
Owner 16/11/2026 chê bản lưới 3D của phiếu 385 "xấu đến đáng sợ… tự style", và yêu cầu: "tạo ảnh trước, sau đó làm theo ảnh đó". Phiếu 386 đã vẽ xong các ảnh trong `games/immortality-cultivation/art-src/concept/ult-ice/`. Claude đã chọn các bản dùng (theo miễn trừ ảnh của owner ngày 15/11).

## Ảnh đích và thành phần (bắt buộc dùng đúng các file này)
- Bố cục và cảm giác đích: `ult-ice-moment-a.v1-try1.png`. Mặt băng phủ hình bầu dục, hàng trăm cụm tinh thể dày đặc ở vành và rải khắp, một bông tinh thể sáng ở tâm, sương và lấp lánh.
- Cụm tinh thể: `ult-ice-crystal-clusters.v1-try1.png`, gồm 4 biến thể.
- Mảnh vỡ, bụi và lấp lánh: `ult-ice-shards-sparkle.v1-try1.png`.
- Vỏ băng bọc quái: `ult-ice-round-shell.v1-try1.png`.
- Mặt băng nứt (tile được): `ult-ice-cracked-surface.v1-try1.png`.

## Việc
Trong `games/.wt-ic-lab-all/src/lab/ice-ult-layered.ts`, làm bản v3 và đặt làm mặc định. Giữ v1, v2 và bản video cũ để so sánh: v2 bật bằng tham số URL, video cũ bằng phím Y.
1. Cắt các thành phần trên thành sprite hoặc atlas bằng script: tách nền đen thành alpha, cắt từng ô, xuất KTX2 hoặc PNG vào `art-src/lab/vfx/ice-ult/`. Không vẽ lại, không tự tạo hình bằng code.
2. Thay lưới 3D tự nghĩ của v2 bằng sprite cụm tinh thể đặt dựng đứng, quay về camera quanh trục đứng (billboard trục Y). Số lượng 120–200 cụm, nhiều cỡ và có xoay lật. Mật độ dày ở vành vùng 30 m như ảnh đích, rải thưa khắp sân, và dày thêm quanh quái. Tinh thể mọc theo vòng sóng từ người tung chiêu.
3. Mặt băng: decal mặt đất dùng texture nứt (tile), lan theo vòng sóng, mép mềm, rồi tan 2,5 s.
4. Tâm: một bông tinh thể sáng, đây là điểm nhấn duy nhất, lõi HDR ngắn khi trúng đòn. Lấy từ cụm tinh thể xếp toả tròn hoặc từ `ice-big-burst` có sẵn.
5. Quái: vỏ băng lấy từ ảnh `round-shell`, đặt dạng billboard ôm quanh từng quái, cỡ theo bán kính quái. Hết 3 s trói thì vỏ vỡ thành sprite mảnh vỡ và bụi lấp lánh.
6. Sương thấp và lấp lánh dùng ảnh `shards-sparkle`. Các lớp phụ giữ nhạt, mỗi kênh ≤ 0,9.
7. Giữ chớp màn, khựng hình, số sát thương, âm băng; thêm âm tinh thể mọc và vỡ từ thư viện âm băng có sẵn.

## Nghiệm thu
- Chụp ảnh lab ở góc trên và góc sau lưng, đặt cạnh `ult-ice-moment-a` trong cùng một ảnh so sánh. Bản v3 phải nhìn giống ảnh đích về mật độ, chất băng và bố cục. Không có thú vẽ sẵn.
- 100 quái trên `stress.html`: p95 ≤ 16,7 ms. Nếu sandbox chặn đo, ghi rõ trong báo cáo.
- Ghi các thành phần mới vào `docs/games/tu-tien/skills/VFX_LIBRARY.md`.
- Chỉ sửa `src/lab/ice-ult-layered.ts`, file mới trong `src/lab/`, và `art-src/lab/vfx/ice-ult/`. Không đụng `view/ground.ts`, `rules.ts` hay các file của phiếu bản đồ 387.
- Không commit, không đưa media vào Git, không đổi nhánh.

## Giao nộp
Ảnh so sánh đặt trong `typing-game-review/owner-review/2026-11-16/tu-tien/ult-ice-v3/`, kèm `ABOUT.md` (purpose, made-by, doc, delete-when). Báo cáo `docs/codex-queue/389-report.md`.
