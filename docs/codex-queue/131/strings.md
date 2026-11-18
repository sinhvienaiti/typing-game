# Bảng duyệt chữ · Phiếu 131

Đường dẫn tính từ `games/.wt-dh-codex`; số dòng theo HEAD nền, không dịch chuyển dòng mã. Mỗi template là một chuỗi, kể cả literal con trong biểu thức; không đếm trùng. Test mới quét chữ nằm trong `tests/english-ui.test.ts`, không có chuỗi cũ để đối chiếu.

Tổng **369 chuỗi đổi**, gồm **325 chuỗi nguồn/trang** và **44 kỳ vọng/fixture test**. **28 dòng** gắn cờ đo ký tự; đây là phép sàng lọc, không phải đo tràn chữ bằng trình duyệt. Các fragment ghép và tên đầy đủ có thể dài hơn nhưng không nằm trong nút/ô nhỏ.

| file:dòng | chuỗi cũ | chuỗi mới | ghi chú |
| --- | --- | --- | --- |
| <code>src/app/app.ts:80</code> | <code>"Dễ"</code> | <code>"Easy"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (2 → 4 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/app/app.ts:80</code> | <code>"Thường"</code> | <code>"Normal"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:80</code> | <code>"Khó"</code> | <code>"Hard"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (3 → 4 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/app/app.ts:205</code> | <code>"Rồng Giữ Ải · "</code> | <code>"Dragonhold · "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:205</code> | <code>" · đang nạp từ…"</code> | <code>" · loading words…"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:258</code> | <code>"Tạm dừng"</code> | <code>"Paused"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:260</code> | <code>"Tạm dừng"</code> | <code>"Paused"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:261</code> | <code>"↑ ↓ chọn · Enter chọn · Esc tiếp tục"</code> | <code>"↑ ↓ select · Enter pick · Esc resume"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:341</code> | <code>"Tiếp tục"</code> | <code>"Resume"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:342</code> | <code>"Chơi lại ải"</code> | <code>"Replay"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:343</code> | <code>"Tốc độ gõ"</code> | <code>"Type speed"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:365</code> | <code>"Tốc độ gõ: "</code> | <code>"Type speed: "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:380</code> | <code>"Chọn tốc độ khác thì ải chơi lại từ đầu."</code> | <code>"A new speed restarts the stage."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:405</code> | <code>"Chơi lại ải với tốc độ "</code> | <code>"Replay at "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:430</code> | <code>"Bấm hoặc gõ phím bất kỳ để tiếp"</code> | <code>"Click or press any key to resume"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:535</code> | <code>"Thẻ Ôn"</code> | <code>"Review"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:535</code> | <code>"Học trước"</code> | <code>"Preview"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:553</code> | <code>"Chơi lại ải ở mức "</code> | <code>"Replay on "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:708</code> | <code>"Tua nhanh chỉ dùng trong đợt và lúc nghỉ"</code> | <code>"Fast forward: waves and breaks only"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:709</code> | <code>"Còn chữ trên quái: gõ hết rồi mới tua nhanh"</code> | <code>"Type all visible words before fast forwarding"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:710</code> | <code>"Quái đã vào Vùng Chữ, chữ sắp hiện: chưa tua nhanh được"</code> | <code>"Foes in the Word Zone: wait for their words"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:830</code> | <code>"Hãy tắt bộ gõ tiếng Việt (Unikey, Telex) để gõ từ tiếng Anh"</code> | <code>"Turn off Vietnamese input (Unikey, Telex) to type English"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:830</code> | <code>"Máu Hỏa Long thấp: "</code> | <code>"Hoa Long low HP: "</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/app/app.ts:830</code> | <code>" uống Small Potion"</code> | <code>" use Small Potion"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/app.ts:882</code> | <code>"Bấm hoặc gõ phím bất kỳ để bắt đầu"</code> | <code>"Click or press any key to start"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/pace-card.ts:27</code> | <code>"Tốc độ gõ"</code> | <code>"Type speed"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/pace-card.ts:28</code> | <code>"Bạn gõ nhanh cỡ nào?"</code> | <code>"How fast do you type?"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/pace-card.ts:29</code> | <code>"Quái đến dày hay thưa, từ dài hay ngắn theo tốc độ này. Chưa biết: gõ mười ngón không nhìn phím thì chọn 35, còn nhìn phím thì chọn 20–25. Hết ải, game đo tốc độ thật của bạn cho lần sau."</code> | <code>"This sets foe pace and word length. Unsure? Pick 35 if you touch type, or 20–25 if you look at the keys. After each stage, your measured speed helps set the next one."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/pace-card.ts:53</code> | <code>"Mới tập gõ: nên chơi mức Dễ, quái thưa và chậm hơn. ⇧↵ chọn tốc độ này và chơi mức Dễ."</code> | <code>"New typist? Try Easy for fewer, slower foes. ⇧↵ picks this speed and Easy."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/pace-card.ts:56</code> | <code>"Chơi mức Dễ ở "</code> | <code>"Play Easy at "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/pace-card.ts:109</code> | <code>" · đang dùng"</code> | <code>" · in use"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/pace-card.ts:116</code> | <code>"Phím "</code> | <code>"Keys "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/pace-card.ts:116</code> | <code>" chọn · ↑ ↓ rồi Enter"</code> | <code>" select · ↑ ↓ then Enter"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/pace-card.ts:116</code> | <code>" · Esc quay lại"</code> | <code>" · Esc back"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:56</code> | <code>"Mới tập gõ"</code> | <code>"Beginner"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:57</code> | <code>"Còn nhìn phím"</code> | <code>"Eyes on keys"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:58</code> | <code>"Gõ chậm"</code> | <code>"Slow"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:59</code> | <code>"Hơi chậm"</code> | <code>"Steady"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:60</code> | <code>"Vừa, người chơi chuẩn"</code> | <code>"Average"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:61</code> | <code>"Khá nhanh"</code> | <code>"Brisk"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:62</code> | <code>"Nhanh"</code> | <code>"Fast"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:64</code> | <code>"Rất nhanh"</code> | <code>"Very fast"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:144</code> | <code>"Số đo: "</code> | <code>"Timed: "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:145</code> | <code>"Đúng "</code> | <code>"Hit "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:145</code> | <code>" % phím"</code> | <code>" % keys"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:145</code> | <code>", đo qua "</code> | <code>", over "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:145</code> | <code>" ải"</code> | <code>" stages"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (3 → 7 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/app/typing-pace.ts:155</code> | <code>"Đang dùng: "</code> | <code>"In use: "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:179</code> | <code>"theo số đo"</code> | <code>"measured"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:179</code> | <code>"cổng game đặt"</code> | <code>"portal preset"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/app/typing-pace.ts:179</code> | <code>"đã chọn"</code> | <code>"picked"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/content/data/maps.ts:35</code> | <code>"Cầu và Suối"</code> | <code>"Bridge and Brook"</code> | Chỉ đổi giá trị nameVi; giữ khóa và dữ liệu luật. ⚑ Dài hơn 20% (11 → 16 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/content/data/maps.ts:41</code> | <code>"Đường Cầu"</code> | <code>"Bridge Lane"</code> | Chỉ đổi giá trị nameVi; giữ khóa và dữ liệu luật. ⚑ Dài hơn 20% (9 → 11 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/content/data/maps.ts:49</code> | <code>"Đường Suối"</code> | <code>"Brook Lane"</code> | Chỉ đổi giá trị nameVi; giữ khóa và dữ liệu luật. |
| <code>src/content/data/maps.ts:58</code> | <code>"Đường Trời"</code> | <code>"Sky Lane"</code> | Chỉ đổi giá trị nameVi; giữ khóa và dữ liệu luật. |
| <code>src/content/data/stages.ts:13</code> | <code>"Ải 1 · Cầu và Suối"</code> | <code>"Stage 1 · Bridge and Brook"</code> | Chỉ đổi giá trị nameVi; giữ khóa và dữ liệu luật. ⚑ Dài hơn 20% (18 → 26 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/debut-card.ts:21</code> | <code>"(lính rêu) Đi bộ tới bệ rồi chém Hỏa Long."</code> | <code>"Walks to the platform and slashes Hoa Long."</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/debut-card.ts:21</code> | <code>"Gõ chữ trên đầu nó; Grove Warden chặn được."</code> | <code>"Type its word; Grove Warden can block it."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:22</code> | <code>"(kiến gai) Cả bầy mang một chữ: gõ một lần là trúng cả bầy."</code> | <code>"The swarm shares one word: type it to hit them all."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:23</code> | <code>"(ong bắp cày gai) Bay trên Đường Trời, dừng cách bệ 10 m rồi bắn; bẫy sàn không trúng."</code> | <code>"Flies along Sky Lane and fires from 10 m away; ground traps cannot hit it."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:23</code> | <code>"Net Launcher kéo nó xuống đất."</code> | <code>"Net Launcher grounds it."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:24</code> | <code>"(cung thủ rêu) Dừng cách bệ 12 m và bắn Hỏa Long tới khi bị hạ."</code> | <code>"Stops 12 m away and fires at Hoa Long until defeated."</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/debut-card.ts:24</code> | <code>"Gõ nó trước; Sky Fire trúng cả nhóm."</code> | <code>"Type it first; Sky Fire hits the group."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:25</code> | <code>"(heo rừng nanh lớn) Báo vạch đỏ rồi húc thẳng vào bệ."</code> | <code>"Marks a red line, then charges the platform."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:25</code> | <code>"Grove Warden chặn, Spikes làm chậm."</code> | <code>"Grove Warden blocks it; Spikes slow it."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:26</code> | <code>"(sói héo mục) Chạy nhanh theo bầy, vồ qua lính chặn."</code> | <code>"Runs in fast packs and leaps past blockers."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:26</code> | <code>"Spikes làm chậm; gõ từng con sớm."</code> | <code>"Spikes slow them; type each wolf early."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:27</code> | <code>"(lính rêu cầm cờ) Tướng địch: cắm cờ, quân trong 5 m quanh Banner đánh mạnh hơn 25 %."</code> | <code>"A general that plants a Banner: foes within 5 m deal 25 % more damage."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:27</code> | <code>"Gõ chữ trên Banner để nhổ cờ; chuỗi từ làm nó mất hào quang."</code> | <code>"Type the Banner word to remove it; word chains strip the aura."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:117</code> | <code>"Tướng địch mới"</code> | <code>"New general"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:117</code> | <code>"Quái mới"</code> | <code>"New foe"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/debut-card.ts:121</code> | <code>"Khắc chế: "</code> | <code>"Counter: "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:147</code> | <code>"Đồ tiêu hao đang hồi"</code> | <code>"Item recharging"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:148</code> | <code>"Hết đồ tiêu hao: mua thêm lúc nghỉ"</code> | <code>"No items: buy more at a break"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:149</code> | <code>"Hết đồ tiêu hao: mua thêm lúc nghỉ"</code> | <code>"No items: buy more at a break"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:150</code> | <code>"Chưa dùng được đồ lúc này"</code> | <code>"Cannot use items now"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:151</code> | <code>"Ải đã bắt đầu"</code> | <code>"Stage started"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:152</code> | <code>"Ải không còn đợt nào"</code> | <code>"No waves left"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:153</code> | <code>"Chỉ gọi sớm được lúc nghỉ"</code> | <code>"Call early during breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:154</code> | <code>"Chỉ vào đợt sớm được lúc nghỉ"</code> | <code>"Start waves during breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:155</code> | <code>"Nhà chưa đổ nát, chưa cần sửa"</code> | <code>"House intact: no repair needed"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:156</code> | <code>"Đã mua đủ số lần trong ải"</code> | <code>"Stage purchase limit reached"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:157</code> | <code>"Không có mục tiêu: kỹ năng chưa dùng, không mất hồi chiêu"</code> | <code>"No target: skill unused, cooldown unchanged"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:161</code> | <code>"Chưa đủ Gold"</code> | <code>"Need Gold"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:162</code> | <code>"Việc này chỉ làm được lúc nghỉ"</code> | <code>"Only during breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:163</code> | <code>"Kỹ năng đang hồi"</code> | <code>"Skill recharging"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:164</code> | <code>"Dragon Rage chưa đầy"</code> | <code>"Dragon Rage not full"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:165</code> | <code>"Tối Thượng: cách lần trước ít nhất 45 s"</code> | <code>"Ultimate: wait at least 45 s between uses"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:166</code> | <code>"Ô đã có món"</code> | <code>"Slot full"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:167</code> | <code>"Món này không đặt được ở ô đó"</code> | <code>"Item does not fit this slot"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:168</code> | <code>"Đã đủ giới hạn"</code> | <code>"Limit reached"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:169</code> | <code>"Món chưa mở"</code> | <code>"Item locked"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:170</code> | <code>"Túi đồ tiêu hao đã đầy"</code> | <code>"Item bag full"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:171</code> | <code>"Ô này chưa có món"</code> | <code>"Empty slot"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:172</code> | <code>"Đã ở cấp cao nhất"</code> | <code>"Max level"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:173</code> | <code>"Món đang dựng"</code> | <code>"Building"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:174</code> | <code>"Không có ô này"</code> | <code>"No such slot"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:175</code> | <code>"Hỏa Long đang choáng"</code> | <code>"Hoa Long stunned"</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/hud.ts:179</code> | <code>"Chưa dùng được kỹ năng"</code> | <code>"Cannot use skill yet"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:180</code> | <code>"Chưa dùng được đồ"</code> | <code>"Cannot use item yet"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:181</code> | <code>"Chưa mua được"</code> | <code>"Cannot buy"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:182</code> | <code>"Chưa đặt được"</code> | <code>"Cannot place"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:183</code> | <code>"Chưa nâng được"</code> | <code>"Cannot upgrade"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:184</code> | <code>"Chưa bán được"</code> | <code>"Cannot sell"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:185</code> | <code>"Chưa gọi sớm được"</code> | <code>"Cannot call early"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:186</code> | <code>"Chưa bắt đầu được"</code> | <code>"Cannot start"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:191</code> | <code>"Chưa làm được lúc này"</code> | <code>"Cannot do this now"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:244</code> | <code>"Đợt"</code> | <code>"Wave"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (3 → 4 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/hud.ts:248</code> | <code>"Chuỗi"</code> | <code>"Chain"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:260</code> | <code>"Tạm dừng (Esc)"</code> | <code>"Pause (Esc)"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:266</code> | <code>"Camera về hướng chuẩn ("</code> | <code>"Reset camera ("</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:277</code> | <code>"Cấp Rồng trong ải"</code> | <code>"Dragon stage level"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:281</code> | <code>"Bạch Long"</code> | <code>"Bach Long"</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/hud.ts:281</code> | <code>"dẫn đường"</code> | <code>"guide"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:282</code> | <code>"Bạch Long đứng cạnh dẫn lời, chưa vào trận"</code> | <code>"Bach Long guides you from the sidelines"</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/hud.ts:287</code> | <code>"Hỏa Long"</code> | <code>"Hoa Long"</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/hud.ts:289</code> | <code>"Giáp"</code> | <code>"Armor"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (4 → 5 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/hud.ts:294</code> | <code>"Khiên"</code> | <code>"Shield"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:324</code> | <code>"Từ Khẩn"</code> | <code>"Urgent"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:324</code> | <code>"Dragon Roar: gõ Từ Khẩn khi quái áp sát (một lần mỗi đợt)"</code> | <code>"Dragon Roar: type the Urgent Word as foes close in (once per wave)"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:328</code> | <code>"Đồ tiêu hao ("</code> | <code>"Item ("</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:337</code> | <code>"): khi Dragon Rage đầy"</code> | <code>"): requires full Dragon Rage"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (22 → 28 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/hud.ts:399</code> | <code>"Ô đồ tiêu hao trống: mua Small Potion lúc nghỉ"</code> | <code>"Empty item slot: buy Small Potion at a break"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:421</code> | <code>&#96;Bày binh · &lt;b&gt;${keyLabel("enter")}&lt;/b&gt; để bắt đầu&#96;</code> | <code>&#96;Prepare · &lt;b&gt;${keyLabel("enter")}&lt;/b&gt; to start&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/hud.ts:422</code> | <code>&#96;Đợt ${upcomingWave(w)} sắp tới&#96;</code> | <code>&#96;Wave ${upcomingWave(w)} incoming&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/hud.ts:426</code> | <code>&#96;Nghỉ · &lt;b&gt;${keyLabel("enter")}&lt;/b&gt; để vào đợt ${upcomingWave(w)}&#96;</code> | <code>&#96;Break · &lt;b&gt;${keyLabel("enter")}&lt;/b&gt; for wave ${upcomingWave(w)}&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/hud.ts:428</code> | <code>&#96;Nghỉ giữa đợt · đứng chờ khi mở ${held}&#96;</code> | <code>&#96;Break · waiting for ${held}&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/hud.ts:429</code> | <code>"Nghỉ giữa đợt"</code> | <code>"Wave break"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:430</code> | <code>&#96;Đang giữ ải · đợt &lt;b&gt;${w.wave}&lt;/b&gt;&#96;</code> | <code>&#96;Defending · wave &lt;b&gt;${w.wave}&lt;/b&gt;&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/hud.ts:431</code> | <code>"Giữ ải thành công"</code> | <code>"Stage cleared"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:432</code> | <code>"Dragon Platform thất thủ"</code> | <code>"Dragon Platform lost"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:447</code> | <code>" · khiên "</code> | <code>" · shield "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:452</code> | <code>"Cấp Rồng "</code> | <code>"Dragon L"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:452</code> | <code>" % tới cấp sau"</code> | <code>" % to next level"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:469</code> | <code>"Dragon Roar: đã dùng trong đợt này"</code> | <code>"Dragon Roar: used this wave"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:469</code> | <code>"Dragon Roar: gõ Từ Khẩn khi quái áp sát (một lần mỗi đợt)"</code> | <code>"Dragon Roar: type the Urgent Word as foes close in (once per wave)"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/hud.ts:482</code> | <code>"Ô trống"</code> | <code>"Empty"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:315</code> | <code>"Bày binh"</code> | <code>"Prepare"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:315</code> | <code>"Nghỉ"</code> | <code>"Break"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (4 → 5 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/learning-frame.ts:317</code> | <code>'&lt;span class="dh-learn__idle"&gt;Gõ chữ đầu của một từ để khóa&lt;/span&gt;'</code> | <code>'&lt;span class="dh-learn__idle"&gt;Type the first letter to lock&lt;/span&gt;'</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:326</code> | <code>' &lt;span class="dh-learn__badge"&gt;MỚI&lt;/span&gt;'</code> | <code>' &lt;span class="dh-learn__badge"&gt;NEW&lt;/span&gt;'</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:338</code> | <code>"Vừa học: "</code> | <code>"Learned: "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:443</code> | <code>"Học trước"</code> | <code>"Preview"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:455</code> | <code>"HỌC TRƯỚC · TỪ MỚI CỦA ẢI"</code> | <code>"PREVIEW · NEW STAGE WORDS"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:461</code> | <code>"Gõ lại từ · Enter nộp · Tab nghe lại · Esc bỏ từ này · Esc 2 lần bỏ hết"</code> | <code>"Retype · Enter submit · Tab replay · Esc skip word · Esc twice skip all"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:467</code> | <code>"Có chữ sai: Backspace để sửa, Enter để nộp"</code> | <code>"Typo: Backspace to fix, Enter to submit"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:492</code> | <code>"Đúng! +5 Gold đầu ải"</code> | <code>"Right! +5 Gold at start"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:492</code> | <code>"Chưa đúng: "</code> | <code>"Try again: "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:564</code> | <code>"Thẻ Ôn"</code> | <code>"Review"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:614</code> | <code>"THẺ ÔN"</code> | <code>"REVIEW"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:615</code> | <code>"Nghe rồi gõ từ"</code> | <code>"Listen and type"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:615</code> | <code>"Xem nghĩa rồi gõ từ"</code> | <code>"Read meaning and type"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:622</code> | <code>"Enter nộp · Tab nghe lại · Esc đóng thẻ"</code> | <code>"Enter submit · Tab replay · Esc close"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:645</code> | <code>"Đúng! +10 Gold"</code> | <code>"Right! +10 Gold"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/learning-frame.ts:651</code> | <code>"Chưa đúng, nhớ lại nhé"</code> | <code>"Try to recall the word"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:66</code> | <code>"Ô bẫy"</code> | <code>"Trap"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:66</code> | <code>"Bệ nhà"</code> | <code>"Pad"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:66</code> | <code>"Điểm giữ"</code> | <code>"Hold spot"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:69</code> | <code>"Món này không hợp ô này"</code> | <code>"Item does not fit slot"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:70</code> | <code>"Ô đã có món"</code> | <code>"Slot full"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:71</code> | <code>"Chỉ đặt lúc nghỉ đợt"</code> | <code>"Place during breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:72</code> | <code>"Chưa đủ Gold"</code> | <code>"Need Gold"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:73</code> | <code>"Đã đủ số món này"</code> | <code>"Item limit reached"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:74</code> | <code>"Món chưa mở"</code> | <code>"Item locked"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:75</code> | <code>"Không có ô này"</code> | <code>"No such slot"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:81</code> | <code>"Thiếu "</code> | <code>"Need "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:284</code> | <code>" · vòng ngoài"</code> | <code>" · outer ring"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:284</code> | <code>" · vòng trong"</code> | <code>" · inner ring"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:306</code> | <code>"Chỉ đặt món lúc nghỉ đợt"</code> | <code>"Place items during breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:326</code> | <code>"Chỉ sửa món lúc nghỉ đợt"</code> | <code>"Edit items during breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:330</code> | <code>"Chưa có món nào để sửa"</code> | <code>"No items to edit"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:361</code> | <code>"Đã ở cấp cao nhất"</code> | <code>"Max level"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:524</code> | <code>"Bộ Mang Theo không có món cho ô này"</code> | <code>"No loadout item fits this slot"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:527</code> | <code>" · cấp "</code> | <code>" · Lv. "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:533</code> | <code>"Bấm lần nữa để nâng"</code> | <code>"Again to upgrade"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:533</code> | <code>"Cấp tối đa"</code> | <code>"Max level"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:533</code> | <code>"Nâng cấp "</code> | <code>"Upgrade "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:533</code> | <code>" · thiếu "</code> | <code>" · need "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:538</code> | <code>"Bấm lần nữa để bán"</code> | <code>"Press again to sell"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:538</code> | <code>"Bán"</code> | <code>"Sell"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (3 → 4 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/placement-ui.ts:603</code> | <code>" · cấp "</code> | <code>" · Lv. "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:640</code> | <code>&#96;Đợt kế: &lt;b&gt;${count}&lt;/b&gt; quái qua đường này&#96;</code> | <code>&#96;Next wave: &lt;b&gt;${count}&lt;/b&gt; foes on this lane&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/placement-ui.ts:642</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("enter")}&lt;/span&gt; đặt · &lt;span class="dh-key"&gt;Esc&lt;/span&gt; hủy&#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("enter")}&lt;/span&gt; place · &lt;span class="dh-key"&gt;Esc&lt;/span&gt; cancel&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/placement-ui.ts:645</code> | <code>" · cấp "</code> | <code>" · Lv. "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:649</code> | <code>"Cấp tối đa"</code> | <code>"Max level"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:649</code> | <code>&#96;&lt;span class="dh-key"&gt;=&lt;/span&gt; nâng cấp ${cursorSlot.level + 1}: &lt;span class="dh-money"&gt;${cost} Gold&lt;/span&gt;&#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;=&lt;/span&gt; upgrade ${cursorSlot.level + 1}: &lt;span class="dh-money"&gt;${cost} Gold&lt;/span&gt;&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/placement-ui.ts:649</code> | <code>&#96; · &lt;b&gt;thiếu ${lack} Gold&lt;/b&gt;&#96;</code> | <code>&#96; · &lt;b&gt;need ${lack} Gold&lt;/b&gt;&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/placement-ui.ts:651</code> | <code>&#96;&lt;span class="dh-key"&gt;-&lt;/span&gt; bán: &lt;span class="dh-money"&gt;+${sellRefund(w, cursor)} Gold&lt;/span&gt;&#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;-&lt;/span&gt; sell: &lt;span class="dh-money"&gt;+${sellRefund(w, cursor)} Gold&lt;/span&gt;&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/placement-ui.ts:654</code> | <code>&#96;Bấm &lt;span class="dh-key"&gt;${up ? "=" : "-"}&lt;/span&gt; lần nữa để ${up ? "nâng" : "bán"}&#96;</code> | <code>&#96;Press &lt;span class="dh-key"&gt;${up ? "=" : "-"}&lt;/span&gt; again to ${up ? "upgrade" : "sell"}&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/placement-ui.ts:674</code> | <code>"Hết ô trống cho món này · &lt;span class=\"dh-key\"&gt;Esc&lt;/span&gt; hủy"</code> | <code>"No free slot for this item · &lt;span class=\"dh-key\"&gt;Esc&lt;/span&gt; cancel"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:674</code> | <code>&#96;&lt;span class="dh-key"&gt;←&lt;/span&gt;&lt;span class="dh-key"&gt;→&lt;/span&gt;&lt;span class="dh-key"&gt;↑&lt;/span&gt;&lt;span class="dh-key"&gt;↓&lt;/span&gt; đổi ô · &lt;span class="dh-key"&gt;${keyLabel("enter")}&lt;/span&gt; đặt · &lt;span class="dh-key"&gt;Esc&lt;/span&gt; hủy · chữ cái vẫn gõ quái&#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;←&lt;/span&gt;&lt;span class="dh-key"&gt;→&lt;/span&gt;&lt;span class="dh-key"&gt;↑&lt;/span&gt;&lt;span class="dh-key"&gt;↓&lt;/span&gt; move · &lt;span class="dh-key"&gt;${keyLabel("enter")}&lt;/span&gt; place · &lt;span class="dh-key"&gt;Esc&lt;/span&gt; cancel · letters still type foes&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/placement-ui.ts:675</code> | <code>&#96;Sửa món: &lt;span class="dh-key"&gt;←&lt;/span&gt;&lt;span class="dh-key"&gt;→&lt;/span&gt; chọn · &lt;span class="dh-key"&gt;=&lt;/span&gt; nâng (2 lần) · &lt;span class="dh-key"&gt;-&lt;/span&gt; bán (2 lần) · &lt;span class="dh-key"&gt;Esc&lt;/span&gt; thoát&#96;</code> | <code>&#96;Edit: &lt;span class="dh-key"&gt;←&lt;/span&gt;&lt;span class="dh-key"&gt;→&lt;/span&gt; pick · &lt;span class="dh-key"&gt;=&lt;/span&gt; upgrade (twice) · &lt;span class="dh-key"&gt;-&lt;/span&gt; sell (twice) · &lt;span class="dh-key"&gt;Esc&lt;/span&gt; exit&#96;</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/placement-ui.ts:730</code> | <code>"Hết ô trống cho món này"</code> | <code>"No free slot for this item"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:195</code> | <code>"Hỏa Long gục ở đợt "</code> | <code>"Hoa Long fell on wave "</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/results.ts:197</code> | <code>". Gõ chữ trên đầu quái để Hỏa Long phun lửa vào chúng."</code> | <code>". Type foes' words to make Hoa Long breathe fire at them."</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/results.ts:199</code> | <code>", phần lớn vì Héo lan: quái mang chữ đứng trong Vùng Chữ mà chưa bị gõ thì rút máu Hỏa Long. Gõ quái gần bệ trước, dùng "</code> | <code>", mainly from Blight: untyped foes in the Word Zone drain Hoa Long's HP. Type foes nearest the platform first; use "</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/results.ts:199</code> | <code>" Fire Breath khi quái dồn."</code> | <code>" Fire Breath when foes crowd in."</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (26 → 32 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/results.ts:200</code> | <code>" vì quái đánh tới bệ. Đặt lính chặn và bẫy ở đường đông quái hơn."</code> | <code>" as foes reached the platform. Place blockers and traps on busier lanes."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:202</code> | <code>"Hỏa Long còn "</code> | <code>"Hoa Long has "</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/results.ts:202</code> | <code>" % máu: trọn ba sao."</code> | <code>" % HP: all three stars."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:204</code> | <code>"Hỏa Long còn "</code> | <code>"Hoa Long has "</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/ui/results.ts:204</code> | <code>" % máu. Giữ từ "</code> | <code>" % HP. Keep at least "</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (15 → 21 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/results.ts:204</code> | <code>" % để có "</code> | <code>" % for "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:204</code> | <code>" sao."</code> | <code>" stars."</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (5 → 7 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/results.ts:209</code> | <code>"Mới học"</code> | <code>"Learned"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:209</code> | <code>"Từ mới"</code> | <code>"New"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:209</code> | <code>"Gõ sai"</code> | <code>"Errors"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:209</code> | <code>"Cần ôn"</code> | <code>"Review"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:209</code> | <code>"Gõ tốt"</code> | <code>"Good"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:249</code> | <code>"Sổ Từ Ải"</code> | <code>"Wordbook"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:260</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("enter")}&lt;/span&gt;Về cổng game&#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("enter")}&lt;/span&gt;Game portal&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/results.ts:284</code> | <code>"Giữ Ải thành công"</code> | <code>"Stage cleared"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:286</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("enter")}&lt;/span&gt; xem kết quả&#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("enter")}&lt;/span&gt; results&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/results.ts:313</code> | <code>"Giữ Ải thành công"</code> | <code>"Stage cleared"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:313</code> | <code>"Dragon Platform thất thủ"</code> | <code>"Dragon Platform lost"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:314</code> | <code>" đợt"</code> | <code>" waves"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (4 → 6 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/results.ts:314</code> | <code>"thua ở đợt "</code> | <code>"lost at wave "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:319</code> | <code>"Gold còn"</code> | <code>"Gold left"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:320</code> | <code>"Gold kiếm được"</code> | <code>"Gold earned"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:321</code> | <code>"Độ chuẩn"</code> | <code>"Accuracy"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:322</code> | <code>"Từ mới đã học"</code> | <code>"New learned"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:323</code> | <code>"Từ đã gặp"</code> | <code>"Words seen"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:326</code> | <code>" từ · "</code> | <code>" words · "</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (6 → 9 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/results.ts:326</code> | <code>" từ gõ sai"</code> | <code>" mistyped"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:336</code> | <code>" lỗi"</code> | <code>" errors"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (4 → 7 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/results.ts:343</code> | <code>"Nghe "</code> | <code>"Play "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:351</code> | <code>"Chưa gõ từ nào trong ải này."</code> | <code>"No words typed this stage."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:352</code> | <code>"Chơi lại ải"</code> | <code>"Replay"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:352</code> | <code>"Thử lại"</code> | <code>"Retry"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/results.ts:356</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("call-early")}&lt;/span&gt;Thua 2 lần: chơi lại mức ${easier}&#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("call-early")}&lt;/span&gt;Lost twice: retry on ${easier}&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/results.ts:358</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("rotate-left")}&lt;/span&gt;&lt;span class="dh-key"&gt;${keyLabel("rotate-right")}&lt;/span&gt; chọn nút · &#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("rotate-left")}&lt;/span&gt;&lt;span class="dh-key"&gt;${keyLabel("rotate-right")}&lt;/span&gt; buttons · &#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/results.ts:359</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("tilt-up")}&lt;/span&gt;&lt;span class="dh-key"&gt;${keyLabel("tilt-down")}&lt;/span&gt; chọn từ&#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("tilt-up")}&lt;/span&gt;&lt;span class="dh-key"&gt;${keyLabel("tilt-down")}&lt;/span&gt; words&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/shop-strip.ts:47</code> | <code>"Chỉ đặt lúc nghỉ"</code> | <code>"Place in breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:47</code> | <code>"Lúc nghỉ"</code> | <code>"Break"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:48</code> | <code>"Mua lúc nghỉ"</code> | <code>"Buy in breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:48</code> | <code>"Lúc nghỉ"</code> | <code>"Break"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:49</code> | <code>"Hết ô trống"</code> | <code>"No free slots"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:49</code> | <code>"Hết ô"</code> | <code>"Full"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:50</code> | <code>"Túi đã đầy"</code> | <code>"Bag full"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:50</code> | <code>"Túi đầy"</code> | <code>"Full"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:60</code> | <code>&#96;(chông nhọn) Chậm ${e.slowPct} %, ${e.dps} sát thương mỗi giây trên đường&#96;</code> | <code>&#96;Slows ${e.slowPct} %, ${e.dps} damage per second on lane&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/shop-strip.ts:61</code> | <code>&#96;(bom quả thông) Nổ ${e.damage} sát thương khi ≥ ${trap.triggerMin} quái, đẩy lùi ${metres(e.pushMm)}; nạp ${sec(trap.rechargeMs)}&#96;</code> | <code>&#96;Blast: ${e.damage} damage at ≥ ${trap.triggerMin} foes, knockback ${metres(e.pushMm)}; recharge ${sec(trap.rechargeMs)}&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/shop-strip.ts:62</code> | <code>&#96;(máy phóng lưới) Kéo ${e.targets &gt; 1 ? e.targets : "một"} quái bay thấp xuống đất trong ${sec(e.groundMs)}, tầm ${metres(trap.area.radiusMm)}; nạp ${sec(trap.rechargeMs)}&#96;</code> | <code>&#96;Grounds ${e.targets &gt; 1 ? e.targets + " low flyers" : "one low flyer"} for ${sec(e.groundMs)}, range ${metres(trap.area.radiusMm)}; recharge ${sec(trap.rechargeMs)}&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/shop-strip.ts:66</code> | <code>&#96;(lều thảo dược) Hồi ${viNumber(house.effect.healPmPerS / 10)} % máu mỗi giây cho phe ta trong ${metres(house.radiusMm)}; đủ 5 lần gõ hạ quái gần nhà: hồi ${house.pulse.healPct} %&#96;</code> | <code>&#96;Heals allies ${viNumber(house.effect.healPmPerS / 10)} % HP per second within ${metres(house.radiusMm)}; 5 typed kills nearby: heal ${house.pulse.healPct} %&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/shop-strip.ts:70</code> | <code>&#96;(vệ binh rêu) Lính chặn ${unit.blockSlots} quái, ${unit.hp} máu, đánh ${unit.attack.damage} mỗi ${sec(unit.attack.periodMs)}&#96;</code> | <code>&#96;Blocks ${unit.blockSlots} foes, ${unit.hp} HP, deals ${unit.attack.damage} every ${sec(unit.attack.periodMs)}&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/shop-strip.ts:74</code> | <code>&#96;(bình hồi máu nhỏ) Hồi ${item.effect.healPct} % máu Hỏa Long trong ${sec(item.effect.durationMs)}; dùng trong đợt&#96;</code> | <code>&#96;Restores ${item.effect.healPct} % of Hoa Long's HP over ${sec(item.effect.durationMs)}; use during waves&#96;</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/shop-strip.ts:77</code> | <code>&#96;(tim rồng) +${buy.effect.pct} % máu tối đa Hỏa Long, hồi luôn phần tăng&#96;</code> | <code>&#96;+${buy.effect.pct} % max HP for Hoa Long; heals the added HP&#96;</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/shop-strip.ts:77</code> | <code>&#96;(vảy cứng) +${buy.effect.amount} ${buy.effect.kind === "armour" ? "Giáp" : "Kháng phép"} Hỏa Long&#96;</code> | <code>&#96;+${buy.effect.amount} ${buy.effect.kind === "armour" ? "Armor" : "Magic resist"} Hoa Long&#96;</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/shop-strip.ts:84</code> | <code>"Thiếu "</code> | <code>"Need "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:95</code> | <code>"Chỉ đặt lúc nghỉ"</code> | <code>"Place in breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:97</code> | <code>"Hết ô trống"</code> | <code>"No free slots"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:101</code> | <code>"Đã đặt "</code> | <code>"Placed "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:109</code> | <code>"Mua lúc nghỉ"</code> | <code>"Buy in breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:110</code> | <code>"Túi đã đầy"</code> | <code>"Bag full"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:114</code> | <code>"Có "</code> | <code>"Held "</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (3 → 5 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/shop-strip.ts:123</code> | <code>"Đủ "</code> | <code>"Max "</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (3 → 4 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/shop-strip.ts:123</code> | <code>" lần"</code> | <code>" buys"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (4 → 5 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/shop-strip.ts:124</code> | <code>"Mua lúc nghỉ"</code> | <code>"Buy in breaks"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:136</code> | <code>"Đã mua "</code> | <code>"Bought "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:176</code> | <code>"Bộ Mang Theo"</code> | <code>"Loadout"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:208</code> | <code>"chưa mua được"</code> | <code>"cannot buy yet"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:215</code> | <code>"Bấm lại phím "</code> | <code>"Press key "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:215</code> | <code>" để mua "</code> | <code>" to buy "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:216</code> | <code>&#96;Bấm lại &lt;span class="dh-key"&gt;${cell.key}&lt;/span&gt; để mua ${cell.nameVi} (${cell.price ?? 0} Gold)&#96;</code> | <code>&#96;Press again &lt;span class="dh-key"&gt;${cell.key}&lt;/span&gt; to buy ${cell.nameVi} (${cell.price ?? 0} Gold)&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/shop-strip.ts:281</code> | <code>"Thiếu"</code> | <code>"Need"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:286</code> | <code>" (phím "</code> | <code>" (key "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/shop-strip.ts:296</code> | <code>&#96;Phím &lt;b&gt;1–${Math.min(9, cells.length)}&lt;/b&gt; chọn món · &lt;span class="dh-key"&gt;\&#96;&lt;/span&gt; sửa món đã đặt&#96;</code> | <code>&#96;Keys &lt;b&gt;1–${Math.min(9, cells.length)}&lt;/b&gt; pick item · &lt;span class="dh-key"&gt;\&#96;&lt;/span&gt; edit placed items&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/tags.ts:456</code> | <code>"Quái"</code> | <code>"Foe"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:457</code> | <code>"Bầy"</code> | <code>"Mob"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:458</code> | <code>"Tinh anh"</code> | <code>"Elite"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:459</code> | <code>"Tướng"</code> | <code>"Gen."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:460</code> | <code>"Ấn Phá"</code> | <code>"Seal"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:461</code> | <code>"Nhổ cờ"</code> | <code>"Unflag"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:462</code> | <code>"Từ Ngắt"</code> | <code>"Stop"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:464</code> | <code>"Chữ Chiêu"</code> | <code>"Skill"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:465</code> | <code>"Từ Trợ"</code> | <code>"Aid"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:466</code> | <code>"Từ Kích"</code> | <code>"Trigger"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:467</code> | <code>"Bộ phận"</code> | <code>"Part"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:468</code> | <code>"Cụm Ấn"</code> | <code>"Seals"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:469</code> | <code>"Vật"</code> | <code>"Obj"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/tags.ts:892</code> | <code>"MỚI"</code> | <code>"NEW"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/ui-preview.ts:193</code> | <code>"Rồng Giữ Ải · xem UI"</code> | <code>"Dragonhold · UI preview"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/ui-preview.ts:217</code> | <code>&#96;&lt;div class="${LEARNING_FRAME_CLASSES.recent}"&gt;Vừa học: bridge · honey · valley&lt;/div&gt;&#96;</code> | <code>&#96;&lt;div class="${LEARNING_FRAME_CLASSES.recent}"&gt;Learned: bridge · honey · valley&lt;/div&gt;&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/ui-preview.ts:231</code> | <code>"Tạm dừng (menu dừng do integrator làm)"</code> | <code>"Paused (preview)"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/ui-preview.ts:231</code> | <code>"Camera về hướng chuẩn"</code> | <code>"Reset camera"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:81</code> | <code>"Tướng"</code> | <code>"Gen."</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:128</code> | <code>"Đợt cuối"</code> | <code>"Last wave"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:128</code> | <code>"Đợt "</code> | <code>"Wave "</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (4 → 5 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/wave-card.ts:129</code> | <code>" đường"</code> | <code>" lanes"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:130</code> | <code>"có quái bay"</code> | <code>"with flyers"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:131</code> | <code>"có tướng địch"</code> | <code>"with generals"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:151</code> | <code>"Nhịp đợt: khối sáng là đỉnh, chấm là lúc từng toán vào"</code> | <code>"Wave pace: bright blocks mark peaks; dots mark group arrivals"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:252</code> | <code>"Yên"</code> | <code>"—"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:255</code> | <code>" · tướng địch"</code> | <code>" · general"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:255</code> | <code>" · bay"</code> | <code>" · flying"</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (6 → 9 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/wave-card.ts:273</code> | <code>"Quái bay ×"</code> | <code>"Flyers ×"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:273</code> | <code>" trên "</code> | <code>" on "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:273</code> | <code>": bẫy sàn không trúng, dùng Net Launcher"</code> | <code>": ground traps cannot hit them; use Net Launcher"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:275</code> | <code>"Quái bay "</code> | <code>"Flyers "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:281</code> | <code>"Tướng địch: "</code> | <code>"General: "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:283</code> | <code>"Tướng "</code> | <code>"Gen. "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:284</code> | <code>"Tướng địch"</code> | <code>"General"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:289</code> | <code>"Đợt nhẹ"</code> | <code>"Breather"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:290</code> | <code>"Đợt nhẹ hơn sau tướng địch: quái đến thưa hơn, kịp bày lại binh"</code> | <code>"Lighter wave after a general: fewer foes, time to regroup"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:348</code> | <code>"Đợt "</code> | <code>"Wave "</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (4 → 5 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/ui/wave-card.ts:352</code> | <code>"Bày binh"</code> | <code>"Prepare"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:353</code> | <code>&#96;tới sau &lt;b&gt;${clockSeconds(left ?? 0)} s&lt;/b&gt;&#96;</code> | <code>&#96;in &lt;b&gt;${clockSeconds(left ?? 0)} s&lt;/b&gt;&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/wave-card.ts:354</code> | <code>"chờ bạn"</code> | <code>"ready"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:359</code> | <code>"Bắt đầu ải"</code> | <code>"Play"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:359</code> | <code>"Vào đợt "</code> | <code>"Wave "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:366</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("call-early")}&lt;/span&gt;Gọi sớm&#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("call-early")}&lt;/span&gt;Early&#96;</code> | Dịch nhãn/chữ hiển thị. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>src/ui/wave-card.ts:369</code> | <code>"Quái sắp vào từ các đường sáng"</code> | <code>"Foes will enter along the lit lanes"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:369</code> | <code>"Đặt bẫy, lính, nhà trước"</code> | <code>"Set traps, units, houses"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/ui/wave-card.ts:380</code> | <code>"Đợt "</code> | <code>"Wave "</code> | Dịch nhãn/chữ hiển thị. ⚑ Dài hơn 20% (4 → 5 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>src/view/banners.ts:259</code> | <code>"Cắm Cờ"</code> | <code>"Plant"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/view/bench.ts:742</code> | <code>"không có bộ đếm GPU"</code> | <code>"GPU timer unavailable"</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/view/bench.ts:744</code> | <code>"không tin cậy trên ANGLE/Metal (đo được "</code> | <code>"unreliable on ANGLE/Metal (measured "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/view/bench.ts:745</code> | <code>"không tin cậy: dài hơn cả khung ("</code> | <code>"unreliable: longer than frame ("</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/view/heroes.ts:227</code> | <code>"heroes: Hỏa Long model failed, placeholder kept"</code> | <code>"heroes: Hoa Long model failed, placeholder kept"</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/view/heroes.ts:294</code> | <code>"heroes: Bạch Long model failed, placeholder kept"</code> | <code>"heroes: Bach Long model failed, placeholder kept"</code> | Dịch nhãn/chữ hiển thị. Tên riêng phiên tự Latin. |
| <code>src/view/stage.ts:506</code> | <code>"Xem đất · "</code> | <code>"Terrain · "</code> | Dịch nhãn/chữ hiển thị. |
| <code>src/view/stage.ts:506</code> | <code>" · chuột phải xoay, lăn chuột thu phóng, chuột giữa kéo · ← → ↑ ↓ · Alt + ↑/↓ · Alt + 0"</code> | <code>" · right drag rotate, scroll zoom, middle drag pan · ← → ↑ ↓ · Alt + ↑/↓ · Alt + 0"</code> | Dịch nhãn/chữ hiển thị. |
| <code>tests/app/pace-card.test.ts:49</code> | <code>"Mới tập gõ: nên chơi mức Dễ, quái thưa và chậm hơn. ⇧↵ chọn tốc độ này và chơi mức Dễ."</code> | <code>"New typist? Try Easy for fewer, slower foes. ⇧↵ picks this speed and Easy."</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/app/pace-card.test.ts:71</code> | <code>" Chơi mức Dễ ở 15 WPM"</code> | <code>" Play Easy at 15 WPM"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/app/pace-card.test.ts:125</code> | <code>"Chọn tốc độ khác thì ải chơi lại từ đầu."</code> | <code>"A new speed restarts the stage."</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/app/pace-card.test.ts:126</code> | <code>"Chọn tốc độ khác thì ải chơi lại từ đầu."</code> | <code>"A new speed restarts the stage."</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/app/typing-pace.test.ts:103</code> | <code>"Đang dùng: 70 WPM"</code> | <code>"In use: 70 WPM"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/app/typing-pace.test.ts:105</code> | <code>"70 WPM (cổng game đặt)"</code> | <code>"70 WPM (portal preset)"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/hud.test.ts:73</code> | <code>"Chưa đủ Gold"</code> | <code>"Need Gold"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/hud.test.ts:74</code> | <code>"Chưa dùng được kỹ năng"</code> | <code>"Cannot use skill yet"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/hud.test.ts:75</code> | <code>"Đồ tiêu hao đang hồi"</code> | <code>"Item recharging"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/hud.test.ts:76</code> | <code>"Kỹ năng đang hồi"</code> | <code>"Skill recharging"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/hud.test.ts:77</code> | <code>"Ải đã bắt đầu"</code> | <code>"Stage started"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/hud.test.ts:79</code> | <code>"Tối Thượng: cách lần trước ít nhất 45 s"</code> | <code>"Ultimate: wait at least 45 s between uses"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/placement.test.ts:50</code> | <code>"Thiếu 20 Gold"</code> | <code>"Need 20 Gold"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/placement.test.ts:51</code> | <code>"Ô đã có món"</code> | <code>"Slot full"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/placement.test.ts:52</code> | <code>"Chỉ đặt lúc nghỉ đợt"</code> | <code>"Place during breaks"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/results-screen.test.ts:91</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("enter")}&lt;/span&gt;Về cổng game&#96;</code> | <code>&#96;&lt;span class="dh-key"&gt;${keyLabel("enter")}&lt;/span&gt;Game portal&#96;</code> | Đồng bộ kỳ vọng/fixture. Giữ nội suy số/phím; chỉ đổi cách diễn đạt. |
| <code>tests/ui/results-screen.test.ts:174</code> | <code>"Dễ"</code> | <code>"Easy"</code> | Đồng bộ kỳ vọng/fixture. ⚑ Dài hơn 20% (2 → 4 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>tests/ui/results.test.ts:67</code> | <code>"Héo lan"</code> | <code>"Blight"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/results.test.ts:68</code> | <code>"lính chặn"</code> | <code>"blockers"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/results.test.ts:70</code> | <code>"Hỏa Long phun lửa vào chúng."</code> | <code>"Hoa Long breathe fire at them."</code> | Đồng bộ kỳ vọng/fixture. Tên riêng phiên tự Latin. |
| <code>tests/ui/results.test.ts:85</code> | <code>"Hỏa Long còn 73 % máu. Giữ từ 80 % để có 3 sao."</code> | <code>"Hoa Long has 73 % HP. Keep at least 80 % for 3 stars."</code> | Đồng bộ kỳ vọng/fixture. Tên riêng phiên tự Latin. |
| <code>tests/ui/results.test.ts:88</code> | <code>"đợt 7"</code> | <code>"wave 7"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:34</code> | <code>"Thiếu 30 Gold"</code> | <code>"Need 30 Gold"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:34</code> | <code>"Thiếu 30"</code> | <code>"Need 30"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:37</code> | <code>"Chỉ đặt lúc nghỉ"</code> | <code>"Place in breaks"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:37</code> | <code>"Lúc nghỉ"</code> | <code>"Break"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:38</code> | <code>"Mua lúc nghỉ"</code> | <code>"Buy in breaks"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:46</code> | <code>"Hết ô trống"</code> | <code>"No free slots"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:46</code> | <code>"Hết ô"</code> | <code>"Full"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:47</code> | <code>"Túi đã đầy"</code> | <code>"Bag full"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:48</code> | <code>"Đủ 3 lần"</code> | <code>"Max 3 buys"</code> | Đồng bộ kỳ vọng/fixture. ⚑ Dài hơn 20% (8 → 10 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>tests/ui/shop-strip.test.ts:49</code> | <code>"Đã mua 1/3"</code> | <code>"Bought 1/3"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:53</code> | <code>"(chông nhọn) Chậm 25 %, 8 sát thương mỗi giây trên đường"</code> | <code>"Slows 25 %, 8 damage per second on lane"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:54</code> | <code>"(bình hồi máu nhỏ) Hồi 25 % máu Hỏa Long trong 2 s; dùng trong đợt"</code> | <code>"Restores 25 % of Hoa Long's HP over 2 s; use during waves"</code> | Đồng bộ kỳ vọng/fixture. Tên riêng phiên tự Latin. |
| <code>tests/ui/shop-strip.test.ts:55</code> | <code>"(vảy cứng) +15 Giáp Hỏa Long"</code> | <code>"+15 Armor Hoa Long"</code> | Đồng bộ kỳ vọng/fixture. Tên riêng phiên tự Latin. |
| <code>tests/ui/shop-strip.test.ts:56</code> | <code>"(tim rồng) +10 % máu tối đa Hỏa Long, hồi luôn phần tăng"</code> | <code>"+10 % max HP for Hoa Long; heals the added HP"</code> | Đồng bộ kỳ vọng/fixture. Tên riêng phiên tự Latin. |
| <code>tests/ui/shop-strip.test.ts:57</code> | <code>"0,3 % máu mỗi giây"</code> | <code>"0,3 % HP per second"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/shop-strip.test.ts:58</code> | <code>"(máy phóng lưới) Kéo một quái bay thấp xuống đất trong 3 s, tầm 11 m; nạp 15 s"</code> | <code>"Grounds one low flyer for 3 s, range 11 m; recharge 15 s"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/wave-card.test.ts:41</code> | <code>"Đường Cầu"</code> | <code>"Bridge Lane"</code> | Đồng bộ kỳ vọng/fixture. ⚑ Dài hơn 20% (9 → 11 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>tests/ui/wave-card.test.ts:42</code> | <code>"Đường Suối"</code> | <code>"Brook Lane"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/wave-card.test.ts:43</code> | <code>"Đường Trời"</code> | <code>"Sky Lane"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/wave-card.test.ts:50</code> | <code>"Đợt 1 · 2 đường"</code> | <code>"Wave 1 · 2 lanes"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/wave-card.test.ts:64</code> | <code>"Đợt cuối · 2 đường · có quái bay · có tướng địch"</code> | <code>"Last wave · 2 lanes · with flyers · with generals"</code> | Đồng bộ kỳ vọng/fixture. |
| <code>tests/ui/wave-card.test.ts:66</code> | <code>"Tướng"</code> | <code>"Gen."</code> | Đồng bộ kỳ vọng/fixture. |
| <code>index.html:2</code> | <code>lang="vi"</code> | <code>lang="en"</code> | Ngôn ngữ trang/tên game/mô tả. |
| <code>index.html:6</code> | <code>Rồng Giữ Ải: gõ từ tiếng Anh để Hỏa Long phun lửa, giữ Bệ Rồng trước Bầy Héo.</code> | <code>Dragonhold: type English words to unleash dragon fire and defend the Dragon Platform from the Blight Horde.</code> | Ngôn ngữ trang/tên game/mô tả. ⚑ Dài hơn 20% (77 → 107 ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế. |
| <code>index.html:7</code> | <code>Rồng Giữ Ải</code> | <code>Dragonhold</code> | Ngôn ngữ trang/tên game/mô tả. |
