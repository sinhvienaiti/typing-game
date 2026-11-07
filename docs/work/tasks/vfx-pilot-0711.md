# Làm thử quy trình mới trên 4 hiệu ứng trước khi áp cho cả kho

**Mục tiêu (≤ 3 dòng):** đo xem quy trình mới (`path-to-8.md`) có làm điểm tầng B tăng thật không, chấm trên hiệu ứng đã ghép trong lab, cùng camera và seed, so trước và sau. Tăng rõ thì áp cho cả kho. Không tăng thì Codex tìm hướng mới rồi thử lại.
**Cách đã chốt:** anh, 07/11 10:05: "chúng ta nên thử vài video lại trước, để xem sau khi triển khai theo quy trình mới, chất lượng video có tăng hay k, nếu tăng thì chúng ta sẽ áp dụng cho cả các video sau, nếu chưa tăng, cần kêu codex tìm ra hướng mới để cho nó tăng lên r lại thử tiếp".
**Trong lúc làm thử:** phân loại toàn kho (S2) tạm dừng sau bước đang chạy. Không vẽ ảnh hàng loạt, không chạy Blender hàng loạt.

## 4 hiệu ứng làm thử (mỗi cái đại diện một đường làm lại)
| # | Hiệu ứng trong lab | Mục manifest (thay cùng id khi bật `?pilot=1`) | Đường làm lại | Ai làm nguồn |
|---|---|---|---|---|
| P1 | Cổng xoáy khi boss xuất hiện (B1) | `boss/boss-entrance-vortex` | Ảnh try2 anh duyệt → Firefly image-to-video (2 take) | Claude (Firefly) |
| P2 | Vòng xung kích Huyết | `blood/blood-ring-burst` | Ảnh try2 anh duyệt → Firefly image-to-video (2 take) | Claude (Firefly) |
| P3 | Sao băng Hỏa (phím M, mẫu năm pha) | `fire/i2v-fire-comet` | GIỮ-CHỈNH: cắt đoạn, đường bao engine, lớp còn thiếu | Codex S1 (dòng 1 của `vfx-streams/stream-1-keep.md`) |
| P4 | Tia trúng đòn trên quái (làn 6) | `beast/beast-hit-spark-burst` | Blender: tia có hướng, ≥ 24 khung | Codex S3 (việc S3-1…3) |

## Các bước
1. **Nguồn:**
   - P1, P2: Firefly image-to-video, đang chạy;
   - P3: S1 làm một dòng;
   - P4: S3 làm từng việc.
   - Mỗi nguồn qua tầng A (5 ô, `path-to-8.md` §1).
2. **Gắn vào lab sau cờ `?pilot=1`** (một phiếu lab nhỏ):
   - nạp manifest đè từ `art-src/lab/vfx-pilot-2026-11-07/<kit>/manifest.json` cho đúng 4 id trên;
   - đường bao engine theo recipe (P3), không đổi gì khi tắt cờ.
3. **Quay trước và sau:**
   - Claude quay trong lab 3146, cùng camera chơi, seed, đồng hồ cố định, nền sáng và tối, 1080p;
   - tấm 6 khung và clip ngắn cho mỗi hiệu ứng, tắt và bật `?pilot=1`.
4. **Chấm tầng B:**
   - Codex, mỗi hiệu ứng một lần chạy, ≤ 12 ảnh;
   - không cho Codex biết bản nào là trước hay sau (nhãn X/Y);
   - 5 cột của `path-to-8.md` §1, điểm 1–10 kèm lỗi lớn nhất.
5. **Kết luận:**
   - tăng ≥ 1 điểm trung bình và không hiệu ứng nào giảm → áp quy trình cho cả kho (bật lại S2, S1, rồi vẽ ảnh và Blender theo danh sách);
   - không đạt → Codex tìm hướng mới dựa trên lỗi lớn nhất của từng hiệu ứng, rồi thử lại vòng 2.
   - Gửi anh video trước và sau cùng điểm.

## Nhật ký
- 07/11 10:05 · Claude · lập kế hoạch; P1, P2 đang chạy Firefly (cổng xoáy take1 xong 09:50); S3-1 xong, S3-2 đang chạy; S2 dừng sau bước 01.
- 07/11 10:00 · Claude · P1, P2 xong trên Firefly (4 take, 09:48–09:57). Giữ hình đúng ảnh try2; chuyển động nhẹ (cổng xoay, vòng lung linh, chưa tự nở) → nhịp nở và tan để engine làm qua `envelope`. Gửi anh tấm 4 take (`owner-review/2026-11-07/tu-tien/pilot-i2v/`). Phiếu lắp nguồn `lane-P-assemble-sources.md` xếp sau S3.
