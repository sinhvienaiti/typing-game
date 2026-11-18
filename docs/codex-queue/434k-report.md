# Phiếu 434k — Sét Lôi: thay lớp vẽ bằng code bằng art có sẵn

Ngày 18/11/2026, Claude làm. Giữ nguyên dáng 434j đã duyệt: sét C lan bốn tầng, 7 cột Ngũ Lôi, dải mây bão.

## Thay đổi (chỉ `src/lab/thunder-ult-chain.ts`, `cloud-volume.ts`, thêm `thunder-ult-review-k.mjs`, `thunder-ult-deliver-k.mjs`)

- **L1 `ChainArcs` bỏ hẳn khỏi hiệu ứng.** Gân trong mây: 2–4 ô flipbook `thunder-five-lingering-arcs-wg` lát dọc đường gân (scale đều 2,6 m, không kéo giãn) cộng một ô `thunder-release` mờ ở giữa. Hồ quang dư trên quái sống sót: ô thứ hai của cùng flipbook, lệch vị trí và khung, thay ruy băng. Pool arcs 16→28. Class `ChainArcs` còn trong `thunder-ult-chain-space.ts` nhưng không được dùng; `sections` trả mảng rỗng.
- **L6 vùng xám:** bỏ blob tròn dự phòng của `CloudVolume` (khi chưa có ảnh mây thì không vẽ gì). Lôi không gọi `deck.flash` nữa (vầng sáng theo khoảng cách); ánh chớp mây đến từ ô `thunder-release` và hai PointLight thật.
- **L4 vùng xám (wash):** đã bị `clear()` mỗi khung từ trước, không hiển thị; giữ nguyên.
- Không cần Firefly: mọi lớp đều có art phù hợp.

## Số đo (Chrome headless, server 3148, nền #353a40, 1280×720)

Vòng 1 và vòng 3 (đủ 840 khung). Phủ ngang 67,73%; 4 tầng, tối đa 20 tia, góc nhỏ nhất 61,23°; 7 cột, tối đa 3 chồng, cách nhỏ nhất 5,69 m. Trắng tối đa **2,19%** (≤6%). p95 vòng 1 **5,9 ms**, vòng 3 **15,7 ms** (đạt ≤16,7 nhưng máy đang có Chrome của làn khác chạy song song, nên số vòng 3 bị nhiễu). `tsc` 0 lỗi, không rơi pool, không exception. Mọi cổng của deliver đạt; 7/7 tiếng cột khớp.

Nhận xét mắt: Alt+1/Alt+2 giống 434j; gân mây khó thấy ở góc chơi (vốn nhỏ), cần owner xem clip.

## Giao nộp

- `owner-review/2026-11-18/tu-tien/thunder-art-k.jpg` và `.mp4` (7 s, 30 fps, hai camera, có tiếng); dòng 434k trong `ABOUT.md`.
- Số đo: `captures/tu-tien/thunder-ult-434k/round-3/measure.json`, `final-gates.json`.

Chưa chấm mù 8,5. Đã xóa khung thô của phiếu. Chrome do driver đóng và tự xóa profile. Không commit, không dừng server 3148.
