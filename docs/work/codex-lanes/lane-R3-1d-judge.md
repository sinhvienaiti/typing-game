# Vòng 3 · Bước 1d (thử lại) · Chấm mù quái nhận đòn và cả chiêu Cột Lôi

> **Chưa chạy (07/11 16:30).** Lần thử lại này được chấm bằng bảng 3 giám khảo Claude với nhãn trung tính mới (`docs/work/consult/r3-step1b-panel.md`), so thẳng với bản cuối vòng 2 trong cùng một lượt chấm. Phiếu này chỉ dùng nếu bảng đó không kết luận được.

**Ảnh:** `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/r3-step1b/tp-ab/TP/{play,caster}/{X,Y}-sheet.jpg`.
- Góc `play` là góc chính: quái nhận đòn (nghiêng ra khỏi điểm giáng, nhún, chớp viền) ở giây 1,07–1,30, và cả chiêu.
- Góc `caster` để kiểm bước 1 không bị hỏng.
- **Không mở** `_private/` trước khi chấm xong.

Lần thử lại sau một lần TRƯỢT: chỉ đổi đường nghiêng thân quái. **Không mở bất kỳ file `docs/work/consult/*-verdict.md` nào trước khi khoá điểm** (chúng lộ nhãn X/Y vì cùng seed). Mốc để so có sẵn ở đây:
- cả chiêu ở góc play, vòng 2: **6,5**;
- phản ứng quái của lần trước: nhịp và lực 4,5, tương tác và đúng việc 5,5;
- caster bước 1 (bản đạt): tụ lực 7,5 / 7,5 / 8,0 / 8,0 / 8,0; phóng 7,5 / 7,5 / 7,0 / 7,5 / 7,5 (5 trục §1 theo thứ tự).

**Mức `high`.** Một lần chạy, tối đa 6 ảnh. Kết quả ghi vào `docs/work/consult/r3-step1b-verdict.md`, mở đầu bằng tóm tắt ≤ 120 từ.

1. Chấm X và Y theo 5 cột tầng B (`.agents/skills/game-vfx-production/references/path-to-8.md` §1), thang 1–10, **riêng cho pha chạm và phản ứng quái** ở góc `play`. Ghi lỗi lớn nhất kèm thời điểm.
2. Chấm thêm **cả chiêu** ở góc `play` (1–10, kèm một dòng giải thích). Đây là con số để theo dõi tiến tới 8.
3. Ở góc `caster`: điểm pha tụ lực và phóng có giữ được như mốc caster ở trên không.
4. Khoá điểm, rồi mới mở `_private/key.json` và tính chênh lệch.
5. **Kết luận theo §7:**
   - ĐẠT (luật vòng 3) khi pha chạm và phản ứng quái tăng ≥ 1 ở "nhịp và lực" hoặc "tương tác và đúng việc" **và điểm cả chiêu ở góc play tăng** so với 6,5 của vòng 2, không trục nào tụt.
   - Hiệu năng đã đo: PERF_LINE
   - Nếu TRƯỢT: ghi lý do chính, và phần nào của cả chiêu đang giữ điểm ở 6,5.

Không sửa media, mã hay danh sách. Không lệnh git ghi, không mở cổng mạng, không mở trình duyệt.
