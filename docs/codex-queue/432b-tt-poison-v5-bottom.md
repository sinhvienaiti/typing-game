# Phiếu 432b: Độc -v5 bị cắt ngang thẳng ở chân


Phản biện: PASS (Sonnet, 17/11)
**Owner miễn luật hạn mức (nguyên văn):** "tôi đã nói cứ cho codex làm đi, tôi sẽ reset codex sau"; "cho codex làm việc đi, nó vẫn còn kìa".

## Bối cảnh
Chụp `poison-big-burst-v5` (`typing-game-review/owner-review/2026-11-17/tu-tien/poison-v5.jpg`): to hơn bản cũ nhiều, nhưng có một đường cắt ngang thẳng ở điểm pivot, nửa dưới khói bị mất.

## Việc
1. Kiểm ảnh atlas `games/immortality-cultivation/art-src/lab/vfx/poison/poison-big-burst-v5.atlas.png`: nếu khói bị cắt trong atlas, cắt lại từ `poison/firefly-raw/poison-big-burst.v3-try2.mp4` với vùng lấy đủ phần dưới; nếu do pivot/ground-card trong lab, sửa dòng `poison-big-burst` trong `games/.wt-ic-lab-all/src/lab/burst-v2.ts` (hạ pivot, bỏ cắt, đáy mờ dần 15–20 %).
2. Không ghi đè: bản atlas mới là `-v5b` nếu cần cắt lại.

## Nghiệm thu
- Script đo: không hàng pixel nào ở vùng giữa ô có bước nhảy alpha > 0,3 giữa hai hàng kề nhau (không có mép cắt cứng); lề ≥ 10 %; kiểm kiểu 0 lỗi.
- Chỉ sửa `burst-v2.ts` dòng độc và file mới trong `art-src/lab/vfx/poison/`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/432b-report.md`.
