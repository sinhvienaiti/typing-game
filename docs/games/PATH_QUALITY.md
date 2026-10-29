# Đường đi trên map: luật và mức nhận

Chủ dự án, 29/10/2026 sáng: "phần đường đi cũng phải làm thật đẹp, chứ đường đi nhìn như kiểu lấy ngón tay quệt dài như kia nó rất xấu".

Áp cho cả ba game: lối quái đi và đường làng của Wordwoven, làn và đường núi của Dragonhold, đường đắp của Last Line. Đường là thứ người chơi nhìn suốt trận, ngay dưới thẻ chữ, nên phải đẹp ngang công trình.

## 1. "Vệt quệt" là gì (cấm)

- Một dải màu đều bề rộng, mép mờ đều như vết bút lông.
- Một màu phẳng hay một texture kéo giãn, không có hướng chạy dọc đường.
- Không có mép, không có bờ, không có vật nào bên đường.
- Đường nằm phẳng trên cỏ như dán lên, không lún, không có vai đường.

## 2. Đường đẹp có gì (bắt buộc)

1. **Chất liệu chạy dọc đường.** Đá lát, phiến đá, vệt bánh xe hay thớ đất xếp theo hướng đi. UV chạy theo chiều dài đường; mật độ texel lệch ≤ 20 % giữa đoạn thẳng và đoạn cong.
2. **Mặt cắt có ít nhất ba lớp:** lõi đường (đá lát hay đất nện), vai đường mòn (đất, sỏi, đá vỡ, cỏ thưa), rồi cỏ. Dải chuyển giữa lớp rộng 0,3–0,8 m, mép có nhiễu, không thẳng, không mờ đều.
3. **Bề rộng thay đổi:** ±10–20 % dọc đường, rộng ra ở khúc cua và ngã ba, hẹp lại ở chỗ có bờ đá.
4. **Có độ sâu:** lõi đường thấp hơn vai 3–8 cm, hoặc có bó vỉa, viên đá bờ. Đổ bóng của bờ thấy được ở camera chơi.
5. **Đồ bên đường** cứ 2–6 m một món: viên đá bờ, khóm cỏ trùm mép, phiến đá vỡ, vũng nước, lá rụng. Ở khúc cua, ngã ba, đầu cầu thì có vật lớn: cột đèn, mốc đá, hàng rào, bậc đá.
6. **Đọc rõ ở xa:** luma lõi đường ≥ luma cỏ + 0,15. Nền dưới thẻ chữ vẫn theo luật của từng game: tấm tối dưới thẻ, hoặc làm đường tối đi ở chỗ có thẻ.
7. **Không hình vẽ bằng mã thay ảnh:** đường dùng texture và decal thật (phiếu Codex), cộng mesh hay shader để dựng hình đường. Shader chỉ trộn ảnh thật và tạo nhiễu mép, không vẽ hoa văn thay ảnh.

## 3. Ảnh cần (phiếu Codex)

| Game | Phiếu | Nội dung |
|---|---|---|
| Wordwoven | 122 (`road-paved`, `trail-worn`), 123 tờ c | Lõi đá lát vôi, vai mòn; tờ decal mép đường |
| Dragonhold | 155 | Lõi đá lát hoa cương, vai sỏi đất; tờ decal mép đường |
| Last Line | 125 (`deck-tile`, `deck-edge`, `deck-decals`) | Mặt đường đắp, gờ lan can, decal; luật mục 2 áp cho làn |

## 4. Mã (làn map của từng game)

- Đường dựng thành dải mesh theo spline của lối đi (hoặc shader trên đất có UV dọc đường), với các lớp ở mục 2.2, bề rộng thay đổi, lún và bờ.
- Rải decal và vật bên đường theo luật mục 2.5, có hạt ngẫu nhiên cố định (cùng map thì cùng kết quả).
- Không đổi sim: lối quái đi, ô đặt nhà và va chạm giữ nguyên. Ván vàng giữ nguyên.

## 5. Mức nhận

- Tờ chụp đường ở camera mặc định và ở 55°, 1280 và 1920. Kèm một khung cắt sát đoạn cong và một khung cắt ngã ba hay đầu cầu.
- Giám khảo độc lập chấm M (thang ART_DIRECTION §1.3) riêng cho đường, so với ảnh tham chiếu của chủ dự án. Đạt khi M ≥ 8 và giám khảo trả lời "không" cho câu "Đường có trông như vệt quệt không?".
- Số đo: luma lõi trừ cỏ ≥ 0,15; bề rộng dải chuyển 0,3–0,8 m; bề rộng thay đổi ±10–20 %; texel lệch ≤ 20 %.
