# Quét sau sửa · Phiếu 131

Quét toàn bộ `src/` bằng AST literal/template, đồng thời lưu quét thô đúng `[À-ỹđĐ]` tại [remaining-raw.txt](remaining-raw.txt). Khoảng ký tự thô còn bắt dấu nhân × và IPA; đó không phải chữ tiếng Việt. Các mục dưới đây là chữ Việt thực.

## Nghĩa từ vựng được giữ

**15 literal/template** trong `src/ui/ui-preview.ts`: 14 trường `vi` và một mẫu DOM hiện nghĩa “khu rừng”. Test không bỏ qua cả file: chỉ cho phép trường `vi` và đúng template nghĩa này. Các file `src/ui/learning-frame.ts`, `src/ui/results.ts`, `src/app/learning.ts` đọc/hiện trường `vi` động; không chứa nghĩa Việt literal mới.

| file:dòng | Chuỗi còn lại |
| --- | --- |
| <code>src/ui/ui-preview.ts:152</code> | <code>"cây cầu"</code> |
| <code>src/ui/ui-preview.ts:153</code> | <code>"mật ong"</code> |
| <code>src/ui/ui-preview.ts:154</code> | <code>"thung lũng"</code> |
| <code>src/ui/ui-preview.ts:155</code> | <code>"khu rừng"</code> |
| <code>src/ui/ui-preview.ts:156</code> | <code>"con sông"</code> |
| <code>src/ui/ui-preview.ts:157</code> | <code>"hòn đá"</code> |
| <code>src/ui/ui-preview.ts:158</code> | <code>"mũi tên"</code> |
| <code>src/ui/ui-preview.ts:159</code> | <code>"cái khiên"</code> |
| <code>src/ui/ui-preview.ts:160</code> | <code>"lá cờ"</code> |
| <code>src/ui/ui-preview.ts:161</code> | <code>"con sói"</code> |
| <code>src/ui/ui-preview.ts:162</code> | <code>"chiếc lá"</code> |
| <code>src/ui/ui-preview.ts:163</code> | <code>"con rồng"</code> |
| <code>src/ui/ui-preview.ts:164</code> | <code>"ngôi làng"</code> |
| <code>src/ui/ui-preview.ts:165</code> | <code>"sấm"</code> |
| <code>src/ui/ui-preview.ts:216</code> | <code>&#96;&lt;div class="${LEARNING_FRAME_CLASSES.ipa}"&gt;/ˈfɔːrɪst/&lt;/div&gt;&lt;div class="${LEARNING_FRAME_CLASSES.meaning}"&gt;khu rừng&lt;/div&gt;&#96;</code> |

## Kit chép nguyên trạng

**86 literal/template**. Không sửa `src/kit/**`; Claude chuyển các nhãn dùng khi chơi sang kit gốc rồi đồng bộ sau. Có cả chữ chẩn đoán/cân bằng; ghi đầy đủ để tránh sót.

| file:dòng | Chuỗi còn lại |
| --- | --- |
| <code>src/kit/balance/bands.ts:23</code> | <code>"Thư giãn"</code> |
| <code>src/kit/balance/bands.ts:23</code> | <code>"Cân bằng"</code> |
| <code>src/kit/balance/bands.ts:23</code> | <code>"Thử thách"</code> |
| <code>src/kit/balance/bands.ts:25</code> | <code>"Thắng"</code> |
| <code>src/kit/balance/bands.ts:26</code> | <code>"Biên S"</code> |
| <code>src/kit/balance/bands.ts:27</code> | <code>"Áp lực P"</code> |
| <code>src/kit/balance/bands.ts:28</code> | <code>"Nhàn I"</code> |
| <code>src/kit/balance/bands.ts:29</code> | <code>"Ngộp O"</code> |
| <code>src/kit/balance/bands.ts:30</code> | <code>"Gần thua N"</code> |
| <code>src/kit/balance/bands.ts:31</code> | <code>"Quãng Q"</code> |
| <code>src/kit/balance/gates.ts:87</code> | <code>"Cùng vùng cuốn"</code> |
| <code>src/kit/balance/gates.ts:88</code> | <code>"Không quá dễ"</code> |
| <code>src/kit/balance/gates.ts:89</code> | <code>"Không quá khó"</code> |
| <code>src/kit/balance/gates.ts:90</code> | <code>"Chuẩn thắng ẩu"</code> |
| <code>src/kit/balance/gates.ts:91</code> | <code>"Gõ là sức chính"</code> |
| <code>src/kit/balance/gates.ts:92</code> | <code>"Chiến thuật có nghĩa"</code> |
| <code>src/kit/balance/gates.ts:93</code> | <code>"Bộ điều nhịp nhẹ tay"</code> |
| <code>src/kit/balance/gates.ts:94</code> | <code>"Học không bị lấn"</code> |
| <code>src/kit/balance/gates.ts:95</code> | <code>"Khớp người thật"</code> |
| <code>src/kit/balance/gates.ts:146</code> | <code>"trong dải"</code> |
| <code>src/kit/balance/gates.ts:146</code> | <code>"lệch: "</code> |
| <code>src/kit/balance/gates.ts:146</code> | <code>"thấp"</code> |
| <code>src/kit/balance/gates.ts:146</code> | <code>"thiếu"</code> |
| <code>src/kit/balance/gates.ts:159</code> | <code>&#96;${bot} · ${MODE_LABELS[mode]}${director ? "" : " · tắt nhịp"}&#96;</code> |
| <code>src/kit/balance/gates.ts:159</code> | <code>" · tắt nhịp"</code> |
| <code>src/kit/balance/gates.ts:172</code> | <code>"không đồng thời S ≥ 90 % và I ≥ 20 %"</code> |
| <code>src/kit/balance/gates.ts:178</code> | <code>"novice · Cân bằng"</code> |
| <code>src/kit/balance/gates.ts:178</code> | <code>"thắng "</code> |
| <code>src/kit/balance/gates.ts:179</code> | <code>"child · Thư giãn"</code> |
| <code>src/kit/balance/gates.ts:179</code> | <code>"thắng "</code> |
| <code>src/kit/balance/gates.ts:186</code> | <code>"S chậm chắc &gt; S ẩu"</code> |
| <code>src/kit/balance/gates.ts:189</code> | <code>&#96;hạ quái ${standard.killSeconds.toFixed(2)} s vs ${sloppy.killSeconds.toFixed(2)} s&#96;</code> |
| <code>src/kit/balance/gates.ts:189</code> | <code>"chuẩn nhanh hơn"</code> |
| <code>src/kit/balance/gates.ts:191</code> | <code>"chuẩn hạ sớm hơn (Q thấp hơn)"</code> |
| <code>src/kit/balance/gates.ts:192</code> | <code>"standard/sloppy · thời gian hạ quái hoặc Q"</code> |
| <code>src/kit/balance/gates.ts:202</code> | <code>"thắng "</code> |
| <code>src/kit/balance/gates.ts:212</code> | <code>&#96;thắng ${pct(high.win)} vs ${pct(low.win)}&#96;</code> |
| <code>src/kit/balance/gates.ts:212</code> | <code>"Tốt hơn Kém ≥ 10 điểm %"</code> |
| <code>src/kit/balance/gates.ts:223</code> | <code>&#96;${row.stepsPerWave.toFixed(2)} bậc/đợt, khoảng sinh ${pct(row.spawnMin)}–${pct(row.spawnMax)}&#96;</code> |
| <code>src/kit/balance/gates.ts:223</code> | <code>&#96;≤ ${maxSteps} bậc/đợt, trong ±${pct(cap)}&#96;</code> |
| <code>src/kit/balance/gates.ts:225</code> | <code>"nhật ký bộ điều nhịp"</code> |
| <code>src/kit/balance/gates.ts:227</code> | <code>"standard · tắt nhịp"</code> |
| <code>src/kit/balance/gates.ts:231</code> | <code>"đạt"</code> |
| <code>src/kit/balance/gates.ts:231</code> | <code>"trượt"</code> |
| <code>src/kit/balance/gates.ts:231</code> | <code>"cổng học của game"</code> |
| <code>src/kit/balance/gates.ts:232</code> | <code>"cổng học của game"</code> |
| <code>src/kit/balance/gates.ts:247</code> | <code>&#96;lệch ≤ ${Math.round(tolerance * 100)} %&#96;</code> |
| <code>src/kit/balance/gates.ts:247</code> | <code>"lệch: "</code> |
| <code>src/kit/balance/gates.ts:249</code> | <code>"buổi chơi thử của người thật"</code> |
| <code>src/kit/balance/gates.ts:260</code> | <code>"ĐẠT"</code> |
| <code>src/kit/balance/gates.ts:260</code> | <code>"TRƯỢT"</code> |
| <code>src/kit/balance/gates.ts:260</code> | <code>"THIẾU SỐ"</code> |
| <code>src/kit/balance/gates.ts:265</code> | <code>"&#124; # &#124; Cổng &#124; Kết quả &#124; Số đo &#124;"</code> |
| <code>src/kit/balance/gates.ts:268</code> | <code>"thiếu: "</code> |
| <code>src/kit/balance/pace.ts:110</code> | <code>"Tay bạn đang chậm dần: nghỉ vài phút rồi chơi tiếp nhé."</code> |
| <code>src/kit/balance/pace.ts:111</code> | <code>"Bạn gõ nhanh nhưng hay sai: chậm lại một nhịp sẽ được Hoàn hảo nhiều hơn."</code> |
| <code>src/kit/balance/pace.ts:112</code> | <code>"Gõ chắc từng chữ trước, tốc độ sẽ tự lên."</code> |
| <code>src/kit/balance/pace.ts:113</code> | <code>"Nhịp gõ chưa đều: giữ một tốc độ vừa phải cho mọi từ."</code> |
| <code>src/kit/balance/pace.ts:114</code> | <code>"Từ mới còn lạ: đọc nghĩa và nghe phát âm trước khi gõ."</code> |
| <code>src/kit/balance/pace.ts:115</code> | <code>"Khi đông quái, chọn một từ và gõ dứt điểm rồi mới sang từ khác."</code> |
| <code>src/kit/balance/pace.ts:116</code> | <code>"Bạn đang tiến bộ đều. Giữ phong độ!"</code> |
| <code>src/kit/balance/typist.ts:86</code> | <code>"Trẻ em"</code> |
| <code>src/kit/balance/typist.ts:86</code> | <code>"Hồ sơ trẻ em"</code> |
| <code>src/kit/balance/typist.ts:87</code> | <code>"Mới"</code> |
| <code>src/kit/balance/typist.ts:87</code> | <code>"Người mới tập gõ"</code> |
| <code>src/kit/balance/typist.ts:88</code> | <code>"Chậm chắc"</code> |
| <code>src/kit/balance/typist.ts:88</code> | <code>"Gõ chậm nhưng chuẩn"</code> |
| <code>src/kit/balance/typist.ts:89</code> | <code>"Chuẩn"</code> |
| <code>src/kit/balance/typist.ts:89</code> | <code>"Người chơi tham chiếu"</code> |
| <code>src/kit/balance/typist.ts:90</code> | <code>"Khá"</code> |
| <code>src/kit/balance/typist.ts:91</code> | <code>"Ẩu"</code> |
| <code>src/kit/balance/typist.ts:91</code> | <code>"Gõ nhanh nhưng ẩu"</code> |
| <code>src/kit/balance/typist.ts:92</code> | <code>"Người gõ giỏi"</code> |
| <code>src/kit/balance/typist.ts:93</code> | <code>"Không gõ"</code> |
| <code>src/kit/balance/typist.ts:93</code> | <code>"Kiểm \"gõ là sức chính\""</code> |
| <code>src/kit/balance/typist.ts:94</code> | <code>"Chỉ gõ"</code> |
| <code>src/kit/balance/typist.ts:94</code> | <code>"Kiểm \"hỗ trợ cần thiết\""</code> |
| <code>src/kit/feedback/profiles.ts:51</code> | <code>"HOÀN HẢO"</code> |
| <code>src/kit/input/keys.ts:45</code> | <code>"àáạảãâầấậẩẫăằắặẳẵ"</code> |
| <code>src/kit/input/keys.ts:46</code> | <code>"èéẹẻẽêềếệểễ"</code> |
| <code>src/kit/input/keys.ts:47</code> | <code>"ìíịỉĩ"</code> |
| <code>src/kit/input/keys.ts:48</code> | <code>"òóọỏõôồốộổỗơờớợởỡ"</code> |
| <code>src/kit/input/keys.ts:49</code> | <code>"ùúụủũưừứựửữ"</code> |
| <code>src/kit/input/keys.ts:50</code> | <code>"ỳýỵỷỹ"</code> |
| <code>src/kit/input/keys.ts:51</code> | <code>"đ"</code> |
| <code>src/kit/speech/speech.ts:128</code> | <code>"Thiết bị không có giọng đọc tiếng Anh"</code> |

## Chú thích và dữ liệu biên soạn

Ba template lớn chứa chữ Việt chỉ trong chú thích CSS/GLSL: <code>src/ui/learning-frame.ts:134</code>, <code>src/view/crowd.ts:416</code>, <code>src/view/telegraphs.ts:68</code>. Các chú thích mã còn lại được giữ; xem từng dòng trong quét thô. `src/view/maps/L2-cau.map.json:7` nhắc “Đường Suối” trong trường `brief` dành cho biên soạn cảnh, không phải chữ người chơi thấy; không đổi nội dung cảnh.

## Ngoài phạm vi ghi: trang dev âm thanh

**15 literal** trong `src/audio/dev/harness.ts`, cùng chữ HTML của `src/audio/dev/harness.html`. Đây là trang kiểm âm thanh riêng, không được game import. Cả hai đường dẫn đều ngoài danh sách được ghi; hiện chưa sửa hay tự ý thêm ngoại lệ vào test. Test quét nghiêm ngặt đang đỏ với 16 mục (15 literal và 1 file HTML). Đã hỏi chủ dự án chọn ngoại lệ trang dev hoặc mở quyền dịch; đang chờ trả lời. Vì vậy chưa thể xác nhận điều kiện “còn lại chỉ nghĩa từ vựng, kit và chú thích”.

| file:dòng | Chuỗi còn lại |
| --- | --- |
| <code>src/audio/dev/harness.ts:324</code> | <code>"Âm "</code> |
| <code>src/audio/dev/harness.ts:334</code> | <code>"Bầy 200 quái…"</code> |
| <code>src/audio/dev/harness.ts:338</code> | <code>"200 quái, 6 s: đỉnh "</code> |
| <code>src/audio/dev/harness.ts:338</code> | <code>" · tiếng tối đa "</code> |
| <code>src/audio/dev/harness.ts:338</code> | <code>" · phím "</code> |
| <code>src/audio/dev/harness.ts:341</code> | <code>"Nhường tiếng…"</code> |
| <code>src/audio/dev/harness.ts:345</code> | <code>"Nhạc…"</code> |
| <code>src/audio/dev/harness.ts:348</code> | <code>"Nhạc 14 s: Rừng 0–6 s, thêm Đợt từ ô nhịp kế · đỉnh "</code> |
| <code>src/audio/dev/harness.ts:351</code> | <code>"Phát âm từ: "</code> |
| <code>src/audio/dev/harness.ts:353</code> | <code>"Chạy thật (AudioContext)…"</code> |
| <code>src/audio/dev/harness.ts:355</code> | <code>"createAudio thật: "</code> |
| <code>src/audio/dev/harness.ts:355</code> | <code>" tiếng, nhạc "</code> |
| <code>src/audio/dev/harness.ts:355</code> | <code>", lỗi "</code> |
| <code>src/audio/dev/harness.ts:370</code> | <code>"Xong: đạt"</code> |
| <code>src/audio/dev/harness.ts:370</code> | <code>"Xong: có lỗi"</code> |
