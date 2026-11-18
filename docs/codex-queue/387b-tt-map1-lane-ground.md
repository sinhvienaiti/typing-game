# Phiếu 387b · Tu Tiên · Map 1 một đường: mặt đất bằng ô 383b (sau 387a)

> Anh duyệt bề rộng 12 m (16/11: "đồng ý"); camera B 42° và map một đường chốt 15/11 theo đề xuất (DECISIONS 15/11 17:4x, 16/11). Tách từ phiếu 387 (ba vòng critic FAIL vì quá lớn) thành 387a → 387b → 387c, làm theo thứ tự. Lời giải do Claude viết. Không ghi Git.

Phản biện: PASS (critic Claude mới, 16/11)

**Model `gpt-6.1-sol`, mức `high`. Một làn.** Báo cáo `docs/codex-queue/387b-report.md`. Chỉ chạy khi 387a đã nghiệm thu.

Đọc trước: `docs/games/tu-tien/MAP1_WIDE.md` §13 (13.3, 13.4), greybox `G/tmp/shots/map1-wide/lane-w12.png` và script `G/tmp/shots/map1-wide/lane-width.mjs`. `G = games/immortality-cultivation`.

## Việc
1. **Mặt đất bằng ô 383b** (thay nền thủ tục trong `view/ground.ts`, giữ nét viền mực): chép `G/art-src/ground/thanh-thach/{lane-paving,court-paving,court-cracked,formation-worn,moss-patch,rubble-edge}.v2.png` vào `G/public/assets/ground/thanh-thach/` (đổi ra WebP chất lượng 90, giữ 1024², ghi md5 vào `media.md5` như các asset khác; không thêm vào Git). Một `ShaderMaterial` trên lưới đất phủ sân cộng váy (x ±40, z −60…+16): lặp ô 4 m; trọng số theo khoảng cách tới đường (cùng mảng điểm với sim): trong đường `lane-paving`, mép đường 1 m chuyển sang `rubble-edge` + `moss-patch`; ngoài đường `court-paving` trộn `court-cracked` theo nhiễu giá trị (seed theo stage); đĩa r 9 m quanh Trận Tâm `formation-worn`. Mặt đường **sáng hơn sân ≥ 1,15** (đo luma trung bình như báo cáo 383b). Ngoài x ±22: tối dần thành màu vực (giữ `GROUND_COLOURS.surround`), chưa có tranh biển mây (việc sau).
2. Váy đất phủ cả khung khi trượt mép tới kẹp của 387a (x ±40, z −60…+16), không lộ nền trống ở góc khung.
3. Tranh 384b (`G/art-src/concept/map1-lane.v1-try3.png`) và 384b-sheet chỉ là tham chiếu nhìn (độ sáng đường, rêu, mép, tông); không nối tranh vào game.
4. Hiệu năng: đo p95 ở High (trần 12 ms), 1920 × 1080, đỉnh đợt 3, trước/sau.

## Kiểm và nộp
- `npm run typecheck`, `npm test` xanh (sim không đổi: golden phải giữ nguyên so với sau 387a).
- Test: danh sách URL của bộ nạp đủ 6 ảnh (kiểm danh sách, không đọc file thật trong vitest vì WebP ngoài Git), trọng số đường dùng cùng mảng `lane.pointsMm`; luma đường/sân ≥ 1,15 trên ảnh chụp.
- Chụp như 387a vào `.../map1-lane-build/387b/` kèm `ABOUT.md`, tấm ghép trước/sau và cạnh tranh 384b. Xoá khung thô của mình.

Cấm: sửa `src/lab/five-thunder.ts` hay mọi thứ Ngũ Lôi; đổi góc nhìn khác ngoài góc mặc định (bốn góc nhìn 13/11 là việc riêng); ghi Git.
