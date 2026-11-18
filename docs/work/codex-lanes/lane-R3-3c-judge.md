# Vòng 3 · Bước 3c · Chấm mù dư âm trên mặt đất và cả chiêu Cột Lôi

**Ảnh** (chỉ mở các file này): `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/r3-step3/panel/`
- `<nhãn>-sheet.jpg`: 12 khung ở góc chơi (mỗi khung thu nhỏ 4 lần từ 1920×1080), có thời điểm trên khung.
- `<nhãn>-hit-crops.jpg`: 8 khung từ 1,07 đến 2,97 s, vùng cắt 640×360 quanh điểm giáng ở độ phân giải thật. Đây là chỗ để xem dư âm: mặt đất sau khi cột rút, điện dư, và vết để lại.
- Ba bản H, N, Q: cùng cảnh, cùng seed, cùng camera, chỉ khác mã hiệu ứng. Không biết bản nào cũ hay mới.

**Mù:** không mở thư mục cha hay bất kỳ file nào khác (không `_private`, không `_panel-key`, không `docs/work/consult/*`, không mã nguồn, không git). Cần phóng to thì cắt bằng `magick` vào `/private/tmp/claude-501/-Volumes-SS990TPRO-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/judge-r3-3/` (thư mục riêng của lượt này; Claude sẽ dọn sau).

**Mức `high`.** Một lần chạy, tối đa 12 ảnh xem. Kết quả ghi vào `docs/work/consult/r3-step3-verdict.md`, mở đầu bằng tóm tắt ≤ 120 từ.

1. Với mỗi bản, ghi điều thấy **trước khi chấm**: dư âm từ 1,30 đến 2,97 s (mặt đất có giữ vết tích không, vết tối hay sáng, có khe sáng nguội dần không, tan từ mép vào hay biến mất đột ngột, có tách khỏi điện dư không, có đọc được ở góc chơi không), rồi cả chiêu.
2. Chấm 5 trục tầng B (`.agents/skills/game-vfx-production/references/path-to-8.md` §1, chỉ đọc §1), thang 1–10, **riêng cho pha dư âm (1,30–2,97 s)**. Ghi lỗi lớn nhất kèm thời điểm.
3. Chấm **cả chiêu** ở góc chơi (1–10, kèm một dòng giải thích), chuẩn game thương mại; 8,5 là mức nghiệm thu.
4. Xếp hạng ba bản cho pha dư âm và cho cả chiêu. Hai bản không phân biệt được thì ghi rõ.
5. **Khoá điểm** vào file kết quả trước, rồi mới mở `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/r3-step3/_panel-key/key.json` để biết nhãn. Không sửa phần đã khoá.
6. **Kết luận theo luật vòng 3:** ĐẠT khi bản mới (`r3-step3` X trong khoá) hơn **bản trước đó** (`r3-step2` X) ≥ 1 điểm ở "nhịp và lực" hoặc "tương tác và đúng việc" của pha dư âm **và** điểm cả chiêu tăng, không trục nào tụt. Hiệu năng đã đo: ĐẠT, Δp95 −1,6 ms; p95 A 9,4 ms, B 7,8 ms. Bản quay chỉ có một nền sân, nên chưa kiểm nền sáng và nền tối. Nếu TRƯỢT: ghi lý do chính và một thay đổi cụ thể nhất.

Không sửa media, mã hay danh sách. Không lệnh git ghi, không mở cổng mạng, không mở trình duyệt.
