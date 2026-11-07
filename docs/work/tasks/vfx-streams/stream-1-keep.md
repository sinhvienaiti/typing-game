# Luồng 1 · GIỮ-CHỈNH · danh sách việc

Quy trình: `.agents/skills/game-vfx-production/references/path-to-8.md` (§1 tầng A, §2, §4). Phiếu làn: `docs/work/codex-lanes/lane-S1-keep-tune.md`.

**Cột trạng thái:**
- `todo` · `doing` · `A-PASS` (đã có bản dẫn xuất và recipe);
- `A-FAIL→S2` (chuyển luồng 2, ghi lý do) · `A-FAIL→S3`;
- `NEE` (chưa đủ bằng chứng).

Mỗi dòng xong mới sang dòng kế. Hàng 1–20 là 20 ứng viên Codex chọn khi phản biện, nằm ở mục §4 của `docs/work/consult/codex-path-to-8.md`. Đoạn cắt ở đó là **đề xuất, cần soi từng khung**. Các hàng sau do việc phân loại toàn kho (T0, luồng 2) thêm vào, theo thứ tự ưu tiên.

| # | Key | Đợt · điểm cũ | Đoạn (giây nguồn) · vai trò | Chỉnh cụ thể | Trạng thái |
|---|---|---|---|---|---|
| 1 | `i2v-fire-comet__take1` | batch-05 · 7 | 0,50–3,50; thân sao băng | Giữ nội hỏa, bay bằng engine; thêm sheath/glint thật và impact riêng, không đòi thân tự nổ. | todo |
| 2 | `i2v-ice-comet__take1` | batch-05 · 7 | 0,50–3,50; đầu/đuôi băng | Giữ mạng băng; lớp sương lạnh, mảnh và lõi mảnh riêng; kiểm nhấp sáng khi tăng tốc. | todo |
| 3 | `i2v-earth-comet-v2__take1` | batch-05 · 7 | 0,50–3,50; thân Thổ | Giữ hướng và cấu trúc v2; bụi có alpha, tia và impact tách. Không phục hồi v1 đã bị thay thế. | todo |
| 4 | `i2v-metal-comet-v2__take1` | batch-06 · 7 | 0,50–3,50; thân Kim | Giữ sợi bạc; dòng đuôi và glint lệch nhịp, xung đầu khi release riêng. | todo |
| 5 | `i2v-poison-comet-v2__take1` | batch-07 · 7 | 0,50–2,75; thân Độc | Tránh phần đầu mềm dần về cuối; giọt/tia tím từ art riêng; kiểm độ giữ thể tích. | todo |
| 6 | `i2v-star-comet__take1` | batch-07 · 7 | 0,50–3,50; thân Tinh | Giữ mạng sao và vị trí; thêm hạt đuôi đa cỡ có nhịp, đường bay thật. | todo |
| 7 | `i2v-thunder-comet__take1` | batch-07 · 6,5 | 0,50–2,75; lớp thân Lôi | Giữ sét nội bộ; bổ sung lõi/sheath mảnh và xung, không đẩy cả đầu mềm thành trắng. | todo |
| 8 | `i2v-water-comet__take1` | batch-08 · 6,5 | 0,50–3,50; lớp thân Thủy | Giữ vân chảy; bọt/giọt riêng, nhịp di chuyển và chạm đất; kiểm đầu dạng lưới ở cỡ chơi. | todo |
| 9 | `i2v-blood-crescent-sym__take1` | batch-04 · 6 | 0,50–3,50; hình kiếm khí cân | Dùng làm thân/texture có reveal hướng tâm–mũi; thêm radiance, erosion cuối; chưa duyệt loop. | todo |
| 10 | `i2v-ice-crescent-sym__take1` | batch-06 · 7 | 0,50–3,50; hình kiếm khí băng | Giữ mặt tinh thể và hai sừng; chuyển động quét/bay và đuôi do engine, hạt từ art. | todo |
| 11 | `i2v-dark-slash-arc__take1` | batch-05 · 6 | 0,50–2,75; texture cung đỏ | Bỏ yêu cầu clip diễn toàn nhát; reveal theo cung, xói đuôi, tàn bằng mask. Nếu cần khối đen phải có alpha/lớp tối riêng. | todo |
| 12 | `i2v-ice-slash-arc__take1` | batch-06 · 6 | 0,50–3,50; texture cung tinh thể | Giữ chi tiết đang gần tĩnh; đặt vào mặt phẳng chém, thêm quét sáng và erosion. Không chỉ tua nhanh đoạn giữ hình. | todo |
| 13 | `i2v-water-slash-arc__take1` | batch-08 · 6,5 | 0,50–2,75; thân cung nước | Giữ hình trước co/tan muộn; trích chất liệu, nhịp chém/đuôi và giọt riêng. Đoạn cuối đen chỉ là tài liệu tham khảo, chưa chọn cho timing thật. | todo |
| 14 | `i2v-star-caster-seal__take1` | batch-07 · 7 | 0,50–2,75; ấn sustain ngắn | Giữ tâm rỗng; reveal và xung tâm–vành riêng. MAE 1,20× của toàn clip không chứng nhận cửa sổ này loop. | todo |
| 15 | `i2v-thunder-caster-seal__take1` | batch-07 · 6,5 | 0,50–2,75; ấn sustain ngắn | Giữ rune, thêm nhánh sét bò/hạt nâng riêng; kiểm mối nối mới dù MAE toàn clip 1,09×. | todo |
| 16 | `i2v-metal-caster-seal__take1` | batch-06 · 7 | 0,50–2,75; lớp ấn Kim | Giữ đường bạc và tâm rỗng; thêm chiều sâu sáng/tối, pulse riêng; tránh chồng thêm một đĩa trắng. | todo |
| 17 | `i2v-water-ground-mark__take2` | batch-08 · 6,5 | 0,50–2,75: lớp năng lượng; 4,50–5,00: khảo sát base đá | Giữ hai phần thành hai lớp nếu matte tách sạch; nếu không, dùng still đá gốc. Erosion năng lượng riêng để đá còn lại; không luma-key mất đá. | todo |
| 18 | `i2v-ult-ice-cold-silence__take2` | batch-08 · 7,5 | 0,50–3,50; nền/lớp cảnh băng tĩnh | Giữ ý tĩnh lặng; thêm sương bò tinh thể và chuyển tiếp đầu/cuối riêng. Không hứa nâng điểm bằng rung/nổ. | todo |
| 19 | `i2v-ult-thunder-nine-heavens__take2` | batch-08 · 7,5 | 0,50–3,50; lớp mây/cuộn thư/sét | Dùng lớp sân khấu; xung giáng và chạm chân ấn riêng. Bản v2 đang nối ở lab: không thay ngược v2 bằng v1 chỉ vì v1 điểm cao hơn. | todo |
| 20 | `i2v-ult-water-profound-sea-v2__take3` | batch-08 · 7,5 | 0,50–3,50; mặt xoáy nền | Giữ màu, bọt và lòng xoáy; nếu chiêu cần sóng đổ thật, làm lớp sóng chủ lực riêng, không gọi mặt xoáy lay nhẹ là đã đủ. | todo |
