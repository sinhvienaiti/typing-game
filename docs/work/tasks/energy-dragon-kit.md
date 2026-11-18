# Rồng năng lượng dùng chung cho kỹ năng · chờ sau Ngũ Lôi (12/11/2026)

**Anh nói (12/11 19:0x–19:2x):** họ "tạo ra 1 con rồng khá dài và đẹp, sau đó họ làm các dạng uốn lượn rất đẹp, sau đó họ chỉ cần tạo số lượng rồng uốn lượn phù hợp với góc quay"; "đồng ý, xong ngũ lôi r tiếp tục"; "với con rồng hoặc bất kỳ ảnh nào cũng cần tôi kiểm tra trước".
Video anh gửi là của game khác: chỉ mô tả bằng lời, không đưa vào công cụ AI, không lưu vào repo.

**Điều thấy được (mô tả):** một con rồng năng lượng vẽ bằng nét sáng (viền đầu, sừng, vây, thân dài đuôi tan), một màu chủ đạo trên nền tối; dùng lại: một con lao chéo, một con quấn quanh mục tiêu, 5–8 con toả từ tâm, nhiều con chồng thành biển rồng ở chiêu cuối; ghép trận pháp chữ cổ, quầng tâm, hạt, số sát thương.

**Kế hoạch (luật linh kiện):**
1. Codex vẽ một con rồng dài bằng nét sáng, thân chia đốt đều, ở bộ màu một hệ; vài biến thể đầu và đuôi. **Gửi anh kiểm trước**; không dùng khi anh chưa duyệt.
2. Lab: cơ chế rồng chạy theo đường cong (uốn mesh hoặc dải theo spline, vẽ nhiều con cùng lúc), 3–4 kiểu đường: lượn quanh người, lao thẳng, toả vòng, xoắn ốc lên.
3. Ghép thử một tuyệt kỹ: tám con toả vòng + sương + trận pháp; clip cho anh, rồi giám khảo mù.
Nguyên liệu sẵn có để xem lại: `games/immortality-cultivation/art-src/lab/models/{qi-dragon,energy-dragon}`, `docs/work/tasks/twin-dragons.md`.

## Bước 2 · rồng chạy theo đường cong trong lab (15/11 17:4x)
Anh (15/11): tạm làm theo đề xuất của điều phối vì chưa có thời gian xem. Ngũ Lôi tạm giữ v37 (chờ chấm mù sau 18/11), nên lab chuyển sang rồng.
Linh kiện (Codex 375, 376), trong `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`: đầu `S/energy-dragon-head.v1-try2.png`; thân lặp liền `S/energy-dragon-body.v2-try5.png` (thân dày, phiếu 376); đuôi `S/energy-dragon-tail.v2-try3.png`; chân `S/energy-dragon-claw.v1-try1.png`. Kiểm tên try đúng trong `docs/codex-queue/375-report.md`, `376-report.md` hoặc thư mục.
1. **Cơ chế "rồng theo đường"** (tệp mới, ví dụ `src/lab/dragon-path.ts`, trang hoặc nút riêng trong lab; không đụng `five-thunder.ts`): thân là dải lưới uốn theo một spline 3D (CatmullRom), dán texture thân lặp dọc chiều dài; đầu và đuôi là thẻ gắn hai đầu, xoay theo tiếp tuyến; 2–4 chân gắn dọc thân; dải hướng về camera (billboard quanh trục spline) để không lộ mặt phẳng. Thân thu nhỏ dần về đuôi. Rồng trôi dọc đường (texture offset + điểm đầu tiến dần), cộng sáng, bộ màu bạch kim.
2. **Bốn kiểu đường mẫu:** lượn quanh người chơi; lao thẳng từ người chơi tới bầy quái; tám con toả vòng từ tâm (như anh mô tả trong video tham khảo); xoắn ốc đi lên.
3. **Vẽ nhiều con một lượt** (instancing hoặc gộp lưới), đo p95 với 1, 8, 16 con.
4. **Chụp:** mỗi kiểu đường một clip ngắn 1280×720 ở góc 1 và góc 2b, một tấm khung; giao ở `owner-review/2026-11-15/tu-tien/energy-dragon/` kèm ABOUT.md, số đo ở `captures/tu-tien/energy-dragon/measurements.md`.
Thân 376 có vết tối ở chỗ nối khúc: nếu lộ khi chạy, làm mờ chéo chỗ nối bằng shader (không vẽ lại). Không commit. Model Opus 5.5, effort medium. Báo cáo ≤ 250 chữ.
