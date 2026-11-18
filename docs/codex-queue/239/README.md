# Hồ sơ phiếu 239 · Last Line

Ngày 31/10/2026, tiếp tục từ sáu nguồn `c2` đã biết. Báo cáo chính: [239-report.md](../239-report.md).

- [Nhật ký hai lượt sinh mới](generation-record.json): công cụ tích hợp `image_gen.imagegen`, prompt nguyên văn nằm cạnh từng PNG trong `art-src/ui/icons/`.
- [Tờ xem bản chọn](../../../games/typing-survival/art-src/_review/239/sheet-candidates-v3.jpg): 256 px, 1080p, 720p, kiểm riêng 20/24 px, bốn icon súng và HUD mẫu thương mại.
- [Tờ so sánh sáu icon](../../../games/typing-survival/art-src/_review/239/comparisons-candidates-v3.jpg): đủ cả chevron đơn/đôi, súng chéo và tháp đôi; mở ở 100% để giữ cỡ thật.
- [Số đo](../../../games/typing-survival/art-src/_review/239/measurements-v3.json), [hậu kỳ](../../../games/typing-survival/art-src/_review/239/processing-v3.json), [khổ/kênh](../../../games/typing-survival/art-src/_review/239/identify-final-v3.txt).
- [Bản chốt cũ](../../../games/typing-survival/art-src/_review/239/prev/): đủ 12 PNG và 3 prompt, chép trước khi ghi đè.

Mọi tờ và script cũ v1/v2 giữ nguyên. Bộ v3 mới là bộ trình duyệt của lần này. Không chép vào `public/`; đang chờ Claude chấm từ 8.

## Chạy lại phép kiểm

Tại repo cha, không cần cài gói, mở game, trình duyệt hay mạng:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 games/typing-survival/art-src/_review/239/final-audit-v3.py
```

Script kiểm pixel bản thu và băm; chỉ ghi lại hồ sơ kiểm trong `239/`. Các script tạo ảnh `process-v3.py`, `audit-v3.py`, `sheets-v3.py` giữ nguyên đầu ra đã có; `deliver-v3.py` là nhật ký thao tác giao có hàng rào băm trước, không dùng lại để ghi đè sau khi đã giao.
