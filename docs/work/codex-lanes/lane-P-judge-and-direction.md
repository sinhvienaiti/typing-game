# Phiếu làm thử · Chấm mù trước và sau, rồi đề xuất hướng tiếp theo

Bối cảnh: `docs/work/tasks/vfx-pilot-0711.md`. Lần quay 3 (`pilot-ab-v3`, 11:05) có:
- **P3 sao băng Hỏa:** góc `play` và `close`;
- **P4 tia trúng đòn:** chỉ góc `close`;
- **P1 cổng boss:** chiếm 0,0017 % khung ở cả bản cũ và bản mới. Lỗi ở khâu gắn (cổng quá nhỏ), không quay được;
- **P2 vòng Huyết:** chưa có chiêu nào trong lab dùng vai trò này.

Anh (07/11 10:05): "nếu tăng thì chúng ta sẽ áp dụng cho cả các video sau, nếu chưa tăng, cần kêu codex tìm ra hướng mới để cho nó tăng lên r lại thử tiếp".

**Model `gpt-6.1-sol`, mức `high`.** Một lần chạy, **tối đa 8 ảnh**. Kết quả ghi `docs/work/consult/codex-pilot-verdict.md`: mở đầu bằng **tóm tắt ≤ 200 từ** tiếng Việt, rồi phần chi tiết.

## Việc 1 · Chấm mù tầng B
- Ảnh trong `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/pilot-ab-v3/`:
  - `P3/play/{X,Y}-sheet.jpg`, `P3/close/{X,Y}-sheet.jpg`;
  - `P4/close/{X,Y}-sheet.jpg`.
- **Không mở** `_private/`.
- Chấm X và Y riêng từng hiệu ứng theo 5 cột tầng B (`.agents/skills/game-vfx-production/references/path-to-8.md` §1), thang 1–10, kèm lỗi lớn nhất (pha nào, lúc nào).
- **Lưu ý về P4:** chiêu dùng để kích đòn (`channel`) vẽ các luồng trắng lớn che hiện trường. Ghi rõ điều đó làm việc so sánh khó đến đâu.
- Sau khi chấm xong mới mở `_private/key.json` để biết bản nào là bản mới, rồi tính chênh lệch.

## Việc 2 · Hướng tiếp theo (nếu không tăng ≥ 1 điểm ở mọi hiệu ứng)
Dựa trên điểm, lỗi lớn nhất và những gì quan sát được, trả lời:
1. **Vì sao thay một lớp nguồn không nâng được tầng B?** Ví dụ: hiệu ứng ghép vẫn y nguyên các lớp khác; nguồn mới chỉ sửa lề và nhịp, chứ không sửa cái làm hiệu ứng trông yếu.
2. **Hướng mới cụ thể để điểm tăng.** Ví dụ: làm lại cả một hiệu ứng ghép đủ năm pha (chọn một chiêu đang trong lab, như Cột Lôi `pillar-thunder-single` đã có mẫu B8), thiết kế lại danh sách lớp, rồi mới chọn nguồn cho từng lớp. Ghi danh sách lớp, nguồn cho mỗi lớp (có sẵn, làm từ ảnh, Blender hay sprite vẽ), và cái mỗi lớp góp vào điểm.
3. **Cách đo vòng 2** sao cho thấy được chênh lệch. Gồm:
   - camera và cỡ đúng như người chơi thấy;
   - cách kích không bị chiêu khác che;
   - sửa cỡ cổng boss trong lab;
   - nối vòng Huyết vào một chiêu.
4. Ước lượng công việc và token theo luật chạy nhỏ (mỗi lần chạy một bước).

## Ranh giới
Chỉ ghi `docs/work/consult/codex-pilot-verdict.md`. Không sửa media, mã hay hàng việc. Không lệnh git ghi, không mở cổng mạng, không mở trình duyệt.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
