# Phiếu 428 — Tạm dừng do hạn mức Codex

- Ngày kiểm tra: 16/11/2026 (giờ Việt Nam).
- Kiểm tra lại lúc 22:55 ngày 16/11/2026: đã dùng **86%**, còn **14%**; cửa sổ 10.080 phút. Nguồn: `rate_limits` trong session Codex mới nhất, `rollout-2026-11-16T22-55-11-01a1e511-c7ab-7713-ab5b-4fc1fab6e75f.jsonl`. Điều kiện chặn vẫn còn; tiếp tục giữ nguyên các tệp đã có.
- Theo AGENTS.md và skill `agent-orchestration`: dưới 15% chỉ được nhận việc tạo ảnh; không được cắt flipbook, sửa mã hoặc đo kiểm. Thời điểm đặt lại do hệ thống trả về: **22/11/2026 19:20:12 +07** (`resets_at: 1795350012`).

## Đã làm

- Đọc phiếu và hướng dẫn liên quan; kiểm tra hạn mức trước khi xử lý tài sản.
- Ghi báo cáo này. Không tạo hoặc ghi đè atlas; không sửa `burst-v2.ts`, `burst-layers.ts` hay `VFX_LIBRARY.md`; không chạy build hoặc bộ kiểm thử của game; không thực hiện thao tác Git thay đổi dữ liệu.

## Chưa làm và bước tiếp tục

1. Dùng `tools/vfx-flipbook/` cắt đoạn 0–2,0 giây của `blood/firefly-raw/blood-big-burst.v5-try2.mp4` thành 32 khung, lưới 8×4, tách nền đen, lề ≥10%, 8 khung cuối mờ dần về 0, pivot tại điểm chạm đất; xuất bộ `blood-big-burst-v4.{atlas.png,json,uastc.ktx2}` mới.
2. Chỉ đổi hậu tố sang `-v4` cho `blood-big-burst` trong `games/.wt-ic-lab-all/src/lab/burst-v2.ts`; giữ các lớp giọt, vũng và sắc đỏ thẫm.
3. Cập nhật `docs/games/tu-tien/skills/VFX_LIBRARY.md`, chạy các kiểm tra của phiếu và lưu ảnh 8 khung vào nơi được phép.

Chưa có kết quả nghiệm thu hoặc ảnh để owner duyệt. Lần chạy tiếp theo cần đọc lại hạn mức; chỉ tiếp tục khi quy tắc cho phép. Giữ nguyên mọi file đang có của các agent khác.
