# Kiểm kê chuỗi trước khi sửa · Phiếu 154

Ngày 29/10/2026. Quét AST TypeScript trên 79 file nguồn, tổng cộng 2.155 literal/đoạn tĩnh của template trong `shared/game-kit/**/*.ts`; bỏ `node_modules`, test và chú thích. Rà cả các literal ASCII: tìm được `cao`, `Nhanh`; các từ `trong`, `sau`, `thieu` cũng thuộc bộ chặn. Mỗi dòng là một vị trí, kể cả khi cùng chuỗi lặp lại.

Có 87 vị trí: 9 người chơi thấy, 71 báo cáo dev, 7 bộ ký tự IME. Không có literal nghĩa từ tiếng Việt trong mã ngoài test; các trường nghĩa lấy dữ liệu lúc chạy và giữ nguyên. Bộ ký tự IME không phải chữ hiển thị, giữ nguyên bằng ngoại lệ đúng file, đúng binding và đúng giá trị.

| File | Dòng | Chuỗi | Ai thấy |
|---|---:|---|---|
| `shared/game-kit/balance/bands.ts` | 23 | <code>"Thư giãn"</code> | Báo cáo dev |
| `shared/game-kit/balance/bands.ts` | 23 | <code>"Cân bằng"</code> | Báo cáo dev |
| `shared/game-kit/balance/bands.ts` | 23 | <code>"Thử thách"</code> | Báo cáo dev |
| `shared/game-kit/balance/bands.ts` | 25 | <code>"Thắng"</code> | Báo cáo dev |
| `shared/game-kit/balance/bands.ts` | 26 | <code>"Biên S"</code> | Báo cáo dev |
| `shared/game-kit/balance/bands.ts` | 27 | <code>"Áp lực P"</code> | Báo cáo dev |
| `shared/game-kit/balance/bands.ts` | 28 | <code>"Nhàn I"</code> | Báo cáo dev |
| `shared/game-kit/balance/bands.ts` | 29 | <code>"Ngộp O"</code> | Báo cáo dev |
| `shared/game-kit/balance/bands.ts` | 30 | <code>"Gần thua N"</code> | Báo cáo dev |
| `shared/game-kit/balance/bands.ts` | 31 | <code>"Quãng Q"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 87 | <code>"Cùng vùng cuốn"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 88 | <code>"Không quá dễ"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 89 | <code>"Không quá khó"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 90 | <code>"Chuẩn thắng ẩu"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 91 | <code>"Gõ là sức chính"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 92 | <code>"Chiến thuật có nghĩa"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 93 | <code>"Bộ điều nhịp nhẹ tay"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 94 | <code>"Học không bị lấn"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 95 | <code>"Khớp người thật"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 146 | <code>"trong dải"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 146 | <code>"lệch: "</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 146 | <code>"thấp"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 146 | <code>"cao"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 146 | <code>"thiếu"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 159 | <code>" · tắt nhịp"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 172 | <code>"không đồng thời S ≥ 90 % và I ≥ 20 %"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 178 | <code>"novice · Cân bằng"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 178 | <code>"thắng "</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 179 | <code>"child · Thư giãn"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 179 | <code>"thắng "</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 186 | <code>"S chậm chắc &gt; S ẩu"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 189 | <code>&#96;hạ quái ${</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 189 | <code>"chuẩn nhanh hơn"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 191 | <code>"chuẩn hạ sớm hơn (Q thấp hơn)"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 192 | <code>"standard/sloppy · thời gian hạ quái hoặc Q"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 202 | <code>"thắng "</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 212 | <code>&#96;thắng ${</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 212 | <code>"Tốt hơn Kém ≥ 10 điểm %"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 223 | <code>} bậc/đợt, khoảng sinh ${</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 223 | <code>} bậc/đợt, trong ±${</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 225 | <code>"nhật ký bộ điều nhịp"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 227 | <code>"standard · tắt nhịp"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 231 | <code>"đạt"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 231 | <code>"trượt"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 231 | <code>"cổng học của game"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 232 | <code>"cổng học của game"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 247 | <code>&#96;lệch ≤ ${</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 247 | <code>"lệch: "</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 249 | <code>"buổi chơi thử của người thật"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 260 | <code>"ĐẠT"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 260 | <code>"TRƯỢT"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 260 | <code>"THIẾU SỐ"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 265 | <code>"&#124; # &#124; Cổng &#124; Kết quả &#124; Số đo &#124;"</code> | Báo cáo dev |
| `shared/game-kit/balance/gates.ts` | 268 | <code>"thiếu: "</code> | Báo cáo dev |
| `shared/game-kit/balance/pace.ts` | 110 | <code>"Tay bạn đang chậm dần: nghỉ vài phút rồi chơi tiếp nhé."</code> | Người chơi |
| `shared/game-kit/balance/pace.ts` | 111 | <code>"Bạn gõ nhanh nhưng hay sai: chậm lại một nhịp sẽ được Hoàn hảo nhiều hơn."</code> | Người chơi |
| `shared/game-kit/balance/pace.ts` | 112 | <code>"Gõ chắc từng chữ trước, tốc độ sẽ tự lên."</code> | Người chơi |
| `shared/game-kit/balance/pace.ts` | 113 | <code>"Nhịp gõ chưa đều: giữ một tốc độ vừa phải cho mọi từ."</code> | Người chơi |
| `shared/game-kit/balance/pace.ts` | 114 | <code>"Từ mới còn lạ: đọc nghĩa và nghe phát âm trước khi gõ."</code> | Người chơi |
| `shared/game-kit/balance/pace.ts` | 115 | <code>"Khi đông quái, chọn một từ và gõ dứt điểm rồi mới sang từ khác."</code> | Người chơi |
| `shared/game-kit/balance/pace.ts` | 116 | <code>"Bạn đang tiến bộ đều. Giữ phong độ!"</code> | Người chơi |
| `shared/game-kit/balance/typist.ts` | 86 | <code>"Trẻ em"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 86 | <code>"Hồ sơ trẻ em"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 87 | <code>"Mới"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 87 | <code>"Người mới tập gõ"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 88 | <code>"Chậm chắc"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 88 | <code>"Gõ chậm nhưng chuẩn"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 89 | <code>"Chuẩn"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 89 | <code>"Người chơi tham chiếu"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 90 | <code>"Khá"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 91 | <code>"Ẩu"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 91 | <code>"Gõ nhanh nhưng ẩu"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 92 | <code>"Nhanh"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 92 | <code>"Người gõ giỏi"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 93 | <code>"Không gõ"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 93 | <code>"Kiểm \"gõ là sức chính\""</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 94 | <code>"Chỉ gõ"</code> | Báo cáo dev |
| `shared/game-kit/balance/typist.ts` | 94 | <code>"Kiểm \"hỗ trợ cần thiết\""</code> | Báo cáo dev |
| `shared/game-kit/feedback/profiles.ts` | 51 | <code>"HOÀN HẢO"</code> | Người chơi |
| `shared/game-kit/input/keys.ts` | 45 | <code>"àáạảãâầấậẩẫăằắặẳẵ"</code> | Dữ liệu kỹ thuật IME; không hiển thị |
| `shared/game-kit/input/keys.ts` | 46 | <code>"èéẹẻẽêềếệểễ"</code> | Dữ liệu kỹ thuật IME; không hiển thị |
| `shared/game-kit/input/keys.ts` | 47 | <code>"ìíịỉĩ"</code> | Dữ liệu kỹ thuật IME; không hiển thị |
| `shared/game-kit/input/keys.ts` | 48 | <code>"òóọỏõôồốộổỗơờớợởỡ"</code> | Dữ liệu kỹ thuật IME; không hiển thị |
| `shared/game-kit/input/keys.ts` | 49 | <code>"ùúụủũưừứựửữ"</code> | Dữ liệu kỹ thuật IME; không hiển thị |
| `shared/game-kit/input/keys.ts` | 50 | <code>"ỳýỵỷỹ"</code> | Dữ liệu kỹ thuật IME; không hiển thị |
| `shared/game-kit/input/keys.ts` | 51 | <code>"đ"</code> | Dữ liệu kỹ thuật IME; không hiển thị |
| `shared/game-kit/speech/speech.ts` | 128 | <code>"Thiết bị không có giọng đọc tiếng Anh"</code> | Người chơi |
