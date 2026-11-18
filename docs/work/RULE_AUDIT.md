# Soát luật mỗi tối (owner 12/11/2026: "Đồng ý làm cổng chặn")

Luật nào máy kiểm được thì đã là cổng chặn (không tốn token). Luật cần đọc ngữ cảnh thì soát mỗi tối trong bản tổng kết 23:00 bằng **một agent Sonnet 5.5, effort low**, chỉ đọc. Kết quả ghi vào mục "Vi phạm luật" của `docs/work/review/<ngày>.md`; vi phạm nào lặp lại hai ngày thì đề xuất biến thành cổng.

## Cổng chặn bằng máy (đã chạy)
| Luật | Cổng | Ở đâu |
|---|---|---|
| Phiếu Codex qua phản biện | dòng `Phản biện: PASS` trong phiếu | `tools/codex-run/run.sh` G1 |
| Một làn Codex | từ chối khi đã có `codex exec` | `run.sh` G2 |
| Codex còn < 15 %: chỉ ảnh | đọc `rate_limits`, phiếu phải dùng `image_gen` | `run.sh` G3 |
| Mẫu trước khi làm cả lô | phiếu có `Lô:` phải có `Mẫu đã gửi: <đường dẫn có thật>` | `run.sh` G4 |
| Không media trong Git; add theo đường dẫn | hook PreToolUse | `.claude/hooks/guard-git.sh` |
| Video có hình phải có ảnh tham chiếu | job không có `still` mà thiếu `"material": true` bị từ chối | `.local/ff-bridge/sprint/video-driver.js` |
Nhật ký từ chối của Codex: `.local/codex-runs/gate-refusals.log`.

## Agent soát kiểm gì (đọc transcript và tệp trong ngày)
1. Model và effort: phiên và agent con dùng đúng model theo việc (Haiku / Sonnet / Opus 5.5) theo bộ nhớ `model-fable-51-effort-per-task`.
2. Linh kiện trước: không job ảnh, video, âm nào tạo trọn cảnh một chiêu (AGENTS.md "Components first").
3. Ảnh tham chiếu: mọi job tạo ảnh hay video có tham chiếu của mình; không ảnh bên thứ ba.
4. Mẫu cho anh trước lô: lô ảnh, video, âm có mẫu đã gửi anh trước.
5. Lab: mỗi vòng có hàng SCORECARD, không lùi cột nào mà không ghi lý do; giám khảo mù hai vòng một lần.
6. VFX: không gỡ lớp nào mà không có lớp thay đẹp hơn; vật bị thay đưa vào `VFX_LIBRARY.md`.
7. Âm thanh: tính năng mới có sự kiện âm và clip nghe thử.
8. Báo anh: việc kẹt hay dừng được báo ngay; không để Codex hay Firefly rảnh khi còn việc ảnh.
9. Token: không gọi cả ChatGPT lẫn Gemini cho một câu hỏi; không đọc tệp lớn khi chỉ cần một đoạn.
Mỗi vi phạm: luật nào, ở đâu (tệp hoặc giờ), hậu quả, đề xuất cổng nếu máy kiểm được.
