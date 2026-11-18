# Làn Codex A · Việc A7 · Hỏi ý kiến Codex: quy trình nào đưa VFX lên 8 điểm

Anh (07/11 09:25): "việc tạo video từ ảnh hoặc video từ prompt khó có thể đạt 8 điểm ngay phải k, vậy để đạt 8 điểm cần những yếu tố và quy trình làm như nào, bạn đã tham khảo cả ý kiến của codex chưa?"

Codex đã chấm hơn 400 clip (làn C). Việc này hỏi Codex với vai **người phản biện**: đọc dữ liệu chấm và bản nháp quy trình của Claude dưới đây, chỉ ra chỗ sai, chỗ thiếu, rồi đề xuất quy trình tốt hơn. Không làm media, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`.** Đầu ra: `docs/work/consult/codex-path-to-8.md`, mở đầu bằng **tóm tắt ≤ 300 từ** (tiếng Việt), sau đó là phần chi tiết.

## Dữ liệu để đọc
- `.local/video-review/results/*.json`: điểm, lý do, `best`, prompt làm lại.
- `docs/codex-queue/laneC-report.md`: lỗi hay gặp mỗi đợt, đợt làm thử `redo-01` (0/10 lên 8, trung bình 5,60 → 5,95).
- Điểm theo cách tạo: từ ảnh trung bình 5,3 (17/184 clip ≥ 7, cao nhất 7,5); từ chữ trung bình 4,9 (5/129 ≥ 7, cao nhất 7,0).
- Chuẩn và luật:
  - `docs/games/VFX_STANDARD.md`;
  - `.agents/skills/game-vfx-production/SKILL.md` (và `references/runtime-packaging.md`, cách lai đang chờ anh chốt);
  - luật trong `AGENTS.md`: ảnh tham chiếu trước, không tạo hình chỉ từ prompt, 2 giám khảo mù ≥ 8,5 trong bản chơi.

## Bản nháp quy trình của Claude (để phản biện)
1. **Chấm đúng chỗ.** Clip nguồn chỉ là một lớp. Trong game thương mại, một lớp khói hay tia đứng riêng cũng không đạt 8. Điểm 8 thuộc về **hiệu ứng đã ghép** trong bản chơi. Vì vậy chấm 2 tầng:
   - **(a) clip nguồn:** đạt hay trượt theo tiêu chí kỹ thuật (lề, nền sạch, không vật thừa, có đoạn dùng được, hình đúng);
   - **(b) hiệu ứng ghép:** chấm vẻ đẹp từ 1 đến 10 trong bản chơi.
2. **Ba lỗi lớn của làn C và cách chữa:**
   - **"giữ ảnh rồi nhấp sáng, không tụ–bung–tan, không về đen, vòng lặp không khép":** AI không điều khiển nổi nhịp. Nhịp phải do engine làm (đường cong scale và alpha, ăn mòn bằng mặt nạ, cắt đúng đoạn sống của clip, đổi tốc độ, flipbook lệch pha cho vòng lặp), không đòi clip tự làm;
   - **"đổi hình, phình, cắt mép, sàn hay vật thừa":** chữa bằng ảnh đầu đúng lề và đúng nền (Codex vẽ, anh duyệt), làm 3–4 take rồi chọn, và cắt hoặc lọc nền sau khi tạo;
   - **"hình dán phẳng, viền neon đều, ít hào quang":** chữa bằng ảnh đầu có nhiều lớp, cộng các lớp engine (lõi HDR mảnh, bloom, lấp lánh, đốm sáng bằng sprite vẽ, vết đất, đèn, rung camera, âm).
3. **Quy trình mỗi chiêu hay hiệu ứng:**
   1. thiết kế 5 pha và danh sách lớp;
   2. lấy tham chiếu từ art đã duyệt;
   3. hình có dáng: ảnh đầu, anh duyệt, rồi image-to-video 3–4 take; chất liệu: Blender (hoặc text-to-video chất liệu);
   4. kiểm kỹ thuật clip nguồn (tầng a);
   5. ghép trong lab: nhịp, lớp, đèn, phản ứng quái, âm;
   6. chấm tầng b trong bản chơi;
   7. sửa lớp yếu nhất. Tối đa 3 vòng, sau đó đổi cách.

## Câu hỏi cho Codex
1. Bản nháp sai hay thiếu ở đâu? Có bằng chứng nào trong dữ liệu chấm cho thấy khác đi?
2. Với từng nhóm, hướng nào cho xác suất lên 8 cao nhất, và vì sao: chiêu từ trời (cột, sao băng), dải và lưỡi chém, hào quang lặp, khói và nổ, ấn và vòng đất, hiện hình thần thú, UI và thẻ.
3. Trong hơn 400 clip, những clip nào dùng làm lớp nguồn tốt ngay bây giờ (tầng a đạt) dù điểm vẻ đẹp dưới 8? Liệt kê tối đa 30, kèm đoạn nên cắt.
4. Ảnh đầu phải thế nào để image-to-video giữ hình, không phình và tan đúng: lề, nền, tư thế, độ sáng, số lớp.
5. Nên chấm lại làn C theo 2 tầng không? Nếu có, sửa thước chấm thế nào cho gọn.
6. **Chia việc sau khi chốt.** Anh (07/11 09:30):
   - ảnh và video **về cơ bản đã đạt**, chỉ cần Blender hoặc chỉnh thêm để lên trên 8, thì **giữ lại cho Codex chỉnh**;
   - cái nào **thực sự chưa đạt** thì **làm lại lần lượt từng cái**;
   - chạy **3 luồng**, mỗi luồng có danh sách việc đầy đủ trong file.

   Đề xuất cách phân loại mọi clip (và ảnh nguồn) thành các nhóm sau, kèm tiêu chí đo được:
   - **GIỮ-CHỈNH:** tầng a đạt; nêu cụ thể cần chỉnh gì: cắt đoạn, nhịp engine, lớp Blender phụ, lọc nền…;
   - **LÀM-LẠI-ẢNH:** có hình, cần ảnh đầu mới rồi image-to-video;
   - **LÀM-LẠI-BLENDER:** chất liệu;
   - **BỎ.**

   Rồi đề xuất cách chia ba nhóm cần làm vào 3 luồng không đụng file của nhau, và thứ tự ưu tiên: thứ đang dùng trong lab trước.
7. **Mẫu Blender D1** (`docs/codex-queue/laneD1-report.md`, `.local/blender-samples/`): có đáng làm lô không, hay chỉ dùng Blender làm lớp phụ (tia, bụi, khói) chồng lên clip Firefly?

**Tự kiểm:** sau khi viết xong, tự phản biện bản trả lời một lượt. Sửa đến khi tự thấy đạt hai lần liên tiếp rồi mới kết thúc; ghi kết quả từng lần tự kiểm ở cuối file.

## Ranh giới
Chỉ ghi `docs/work/consult/codex-path-to-8.md`. Không sửa media, mã hay hàng việc. Không lệnh git ghi, không mở cổng mạng, không mở trình duyệt.

## Hết hạn mức
Ghi phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
