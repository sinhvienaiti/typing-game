# Phiếu chạy làn chung: mỗi lần chạy làm đúng MỘT việc kế tiếp trong danh sách của làn

Anh (07/11 12:05): "đảm bảo chia list việc đầy đủ ra file md, để giảm tải việc bạn không phải can thiệp nhiều".

Tên làn có trong tên dòng của hàng chờ: `lane1-run-…`, `lane2-run-…`, `lane3-run-…`. Danh sách tương ứng là `docs/work/codex-lanes/LANE-1.md`, `LANE-2.md`, `LANE-3.md`.

**Model:** theo cột "Mức" của việc (`medium` hoặc `high`). Hàng chờ chạy ở `high`; với việc ghi `medium`, làm gọn và không xem ảnh quá mức cần.

## Cách làm mỗi lần chạy
1. Mở danh sách của làn, **giữ khoá** `mkdir docs/work/codex-lanes/.lock-LANE-<n>`. Không lấy được thì chờ 5 s, thử lại, tối đa 5 phút.
2. **Chọn việc:** việc đầu tiên có trạng thái `todo` mà:
   - mọi việc trong cột "Cần xong trước" đã `done`;
   - cột "Cổng" trống hoặc đã ghi `✅`. Cổng do anh hoặc Claude mở; **không bao giờ tự mở cổng**.
3. **Không có việc nào chọn được:** ghi một dòng "không có việc: chờ <cổng hay việc nào>" vào báo cáo của làn, nhả khoá, **dừng ngay** (không đọc thêm file nào).
4. **Có việc:** đổi trạng thái thành `doing` kèm giờ, nhả khoá. Làm việc **đúng theo phiếu ở cột "Phiếu"**, gồm ranh giới, "Đạt khi" và luật hết hạn mức của phiếu đó.
5. **Xong:**
   - giữ khoá lại;
   - đổi trạng thái thành `done` (hoặc `blocked: <lý do một dòng>`);
   - điền cột "Đầu ra";
   - nhả khoá;
   - ghi ≤ 6 dòng vào báo cáo của làn (`docs/codex-queue/laneL<n>-report.md`).
6. **Không làm hai việc** trong một lần chạy, kể cả việc kế tiếp nhỏ.

## Luật chung
- Chạy nhỏ: tối đa 15 ảnh mỗi lần chạy; quá thì chia việc và ghi vào báo cáo.
- `.agents/skills/game-vfx-production/references/path-to-8.md`: §1 tầng A, §5 ảnh đầu, §7 bước nhỏ và ngân sách hiệu năng.
- Không lệnh git ghi, không mở cổng mạng, không mở trình duyệt, không chạy Firefly (Claude làm).
- Blender chỉ qua `.local/blender-queue/`.
- Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
