# Phiếu 130 · Quét sau sửa

Ngày 29/10/2026. Dữ liệu thô: `scan-after.json`; chạy từ repo cha: `node docs/codex-queue/130/scan.mjs scan-after.json`. Quét rộng `[À-ỹđĐ]` trả 96 đoạn; 8 đoạn chỉ có ký hiệu, không có chữ Việt. Test lọc ký hiệu và chuẩn hóa Unicode NFC.

**Chữ Việt người chơi thấy từ các literal được phép sửa: 0.** Nghĩa học từ được giữ nguyên. Kit không sửa; lời khuyên và nhãn PERFECT đã có bản tiếng Anh cục bộ.

## Ngoài kit

| file:dòng | còn lại | phân loại |
|---|---|---|
| <code>src/app/vocab.ts:13</code> | <code>good:tốt bad:tệ big:to small:nhỏ cold:lạnh hot:nóng fast:nhanh slow:chậm happy:vui sad:buồn light:ánh_sáng<br>dark:tối water:nước fire:lửa earth:đất river:sông ocean:đại_dương planet:hành_tinh star:ngôi_sao<br>moon:mặt_trăng house:ngôi_nhà window:cửa_sổ garden:khu_vườn kitchen:nhà_bếp bread:bánh_mì apple:quả_táo<br>orange:quả_cam lemon:quả_chanh teacher:giáo_viên doctor:bác_sĩ friend:bạn_bè family:gia_đình mother:mẹ<br>father:bố child:đứa_trẻ people:mọi_người jump:nhảy run:chạy swim:bơi write:viết read:đọc listen:nghe speak:nói<br>think:nghĩ learn:học quick:nhanh yellow:màu_vàng violet:màu_tím zebra:ngựa_vằn under:bên_dưới idea:ý_tưởng<br>kind:tử_tế voice:giọng_nói</code> | <code>Nghĩa từ FALLBACK; giữ nguyên.</code> |
| <code>src/content/stage-rules.ts:149</code> | <code>: more Rèn levels than bays</code> | <code>Diagnostic validateChapter nội bộ; không hiển thị cho người chơi, nằm ngoài quyền sửa content.</code> |
| <code>src/view/crowd.ts:87</code> | <code>// x: hit flash (white hot), y: hurt (elites glow red), z: the Giáp affix (gold veins), w: the foe’s own phase.</code> | <code>Chú thích bên trong GLSL; không phải chữ hiển thị.</code> |

**Ngoại lệ cần Claude biết:** literal `: more Rèn levels than bays` ở `src/content/stage-rules.ts:149` là thông báo kiểm dữ liệu, không phải mục tiêu/luật/mô tả hiển thị. Phiếu cấm sửa chuỗi content không hiển thị nên giữ nguyên. Test có ngoại lệ đúng file + đúng literal + đúng lời gọi `problems.push`; không bỏ cả file hoặc toàn bộ diagnostic. Vì vậy danh sách quét thô còn thêm một diagnostic ngoài ba loại nêu trong tiêu chí “Còn sót”; không khẳng định toàn bộ src chỉ còn ba loại đó.

## Kit giữ nguyên

| file:dòng | literal còn chữ Việt |
|---|---|
| <code>src/kit/balance/bands.ts:23</code> | <code>Thư giãn</code> |
| <code>src/kit/balance/bands.ts:23</code> | <code>Cân bằng</code> |
| <code>src/kit/balance/bands.ts:23</code> | <code>Thử thách</code> |
| <code>src/kit/balance/bands.ts:25</code> | <code>Thắng</code> |
| <code>src/kit/balance/bands.ts:26</code> | <code>Biên S</code> |
| <code>src/kit/balance/bands.ts:27</code> | <code>Áp lực P</code> |
| <code>src/kit/balance/bands.ts:28</code> | <code>Nhàn I</code> |
| <code>src/kit/balance/bands.ts:29</code> | <code>Ngộp O</code> |
| <code>src/kit/balance/bands.ts:30</code> | <code>Gần thua N</code> |
| <code>src/kit/balance/bands.ts:31</code> | <code>Quãng Q</code> |
| <code>src/kit/balance/gates.ts:87</code> | <code>Cùng vùng cuốn</code> |
| <code>src/kit/balance/gates.ts:88</code> | <code>Không quá dễ</code> |
| <code>src/kit/balance/gates.ts:89</code> | <code>Không quá khó</code> |
| <code>src/kit/balance/gates.ts:90</code> | <code>Chuẩn thắng ẩu</code> |
| <code>src/kit/balance/gates.ts:91</code> | <code>Gõ là sức chính</code> |
| <code>src/kit/balance/gates.ts:92</code> | <code>Chiến thuật có nghĩa</code> |
| <code>src/kit/balance/gates.ts:93</code> | <code>Bộ điều nhịp nhẹ tay</code> |
| <code>src/kit/balance/gates.ts:94</code> | <code>Học không bị lấn</code> |
| <code>src/kit/balance/gates.ts:95</code> | <code>Khớp người thật</code> |
| <code>src/kit/balance/gates.ts:146</code> | <code>trong dải</code> |
| <code>src/kit/balance/gates.ts:146</code> | <code>lệch: </code> |
| <code>src/kit/balance/gates.ts:146</code> | <code>thấp</code> |
| <code>src/kit/balance/gates.ts:146</code> | <code>thiếu</code> |
| <code>src/kit/balance/gates.ts:159</code> | <code> · tắt nhịp</code> |
| <code>src/kit/balance/gates.ts:172</code> | <code>không đồng thời S ≥ 90 % và I ≥ 20 %</code> |
| <code>src/kit/balance/gates.ts:178</code> | <code>novice · Cân bằng</code> |
| <code>src/kit/balance/gates.ts:178</code> | <code>thắng </code> |
| <code>src/kit/balance/gates.ts:179</code> | <code>child · Thư giãn</code> |
| <code>src/kit/balance/gates.ts:179</code> | <code>thắng </code> |
| <code>src/kit/balance/gates.ts:186</code> | <code>S chậm chắc &gt; S ẩu</code> |
| <code>src/kit/balance/gates.ts:189</code> | <code>hạ quái </code> |
| <code>src/kit/balance/gates.ts:189</code> | <code>chuẩn nhanh hơn</code> |
| <code>src/kit/balance/gates.ts:191</code> | <code>chuẩn hạ sớm hơn (Q thấp hơn)</code> |
| <code>src/kit/balance/gates.ts:192</code> | <code>standard/sloppy · thời gian hạ quái hoặc Q</code> |
| <code>src/kit/balance/gates.ts:202</code> | <code>thắng </code> |
| <code>src/kit/balance/gates.ts:212</code> | <code>thắng </code> |
| <code>src/kit/balance/gates.ts:212</code> | <code>Tốt hơn Kém ≥ 10 điểm %</code> |
| <code>src/kit/balance/gates.ts:223</code> | <code> bậc/đợt, khoảng sinh </code> |
| <code>src/kit/balance/gates.ts:223</code> | <code> bậc/đợt, trong ±</code> |
| <code>src/kit/balance/gates.ts:225</code> | <code>nhật ký bộ điều nhịp</code> |
| <code>src/kit/balance/gates.ts:227</code> | <code>standard · tắt nhịp</code> |
| <code>src/kit/balance/gates.ts:231</code> | <code>đạt</code> |
| <code>src/kit/balance/gates.ts:231</code> | <code>trượt</code> |
| <code>src/kit/balance/gates.ts:231</code> | <code>cổng học của game</code> |
| <code>src/kit/balance/gates.ts:232</code> | <code>cổng học của game</code> |
| <code>src/kit/balance/gates.ts:247</code> | <code>lệch ≤ </code> |
| <code>src/kit/balance/gates.ts:247</code> | <code>lệch: </code> |
| <code>src/kit/balance/gates.ts:249</code> | <code>buổi chơi thử của người thật</code> |
| <code>src/kit/balance/gates.ts:260</code> | <code>ĐẠT</code> |
| <code>src/kit/balance/gates.ts:260</code> | <code>TRƯỢT</code> |
| <code>src/kit/balance/gates.ts:260</code> | <code>THIẾU SỐ</code> |
| <code>src/kit/balance/gates.ts:265</code> | <code>&#124; # &#124; Cổng &#124; Kết quả &#124; Số đo &#124;</code> |
| <code>src/kit/balance/gates.ts:268</code> | <code>thiếu: </code> |
| <code>src/kit/balance/pace.ts:110</code> | <code>Tay bạn đang chậm dần: nghỉ vài phút rồi chơi tiếp nhé.</code> |
| <code>src/kit/balance/pace.ts:111</code> | <code>Bạn gõ nhanh nhưng hay sai: chậm lại một nhịp sẽ được Hoàn hảo nhiều hơn.</code> |
| <code>src/kit/balance/pace.ts:112</code> | <code>Gõ chắc từng chữ trước, tốc độ sẽ tự lên.</code> |
| <code>src/kit/balance/pace.ts:113</code> | <code>Nhịp gõ chưa đều: giữ một tốc độ vừa phải cho mọi từ.</code> |
| <code>src/kit/balance/pace.ts:114</code> | <code>Từ mới còn lạ: đọc nghĩa và nghe phát âm trước khi gõ.</code> |
| <code>src/kit/balance/pace.ts:115</code> | <code>Khi đông quái, chọn một từ và gõ dứt điểm rồi mới sang từ khác.</code> |
| <code>src/kit/balance/pace.ts:116</code> | <code>Bạn đang tiến bộ đều. Giữ phong độ!</code> |
| <code>src/kit/balance/typist.ts:86</code> | <code>Trẻ em</code> |
| <code>src/kit/balance/typist.ts:86</code> | <code>Hồ sơ trẻ em</code> |
| <code>src/kit/balance/typist.ts:87</code> | <code>Mới</code> |
| <code>src/kit/balance/typist.ts:87</code> | <code>Người mới tập gõ</code> |
| <code>src/kit/balance/typist.ts:88</code> | <code>Chậm chắc</code> |
| <code>src/kit/balance/typist.ts:88</code> | <code>Gõ chậm nhưng chuẩn</code> |
| <code>src/kit/balance/typist.ts:89</code> | <code>Chuẩn</code> |
| <code>src/kit/balance/typist.ts:89</code> | <code>Người chơi tham chiếu</code> |
| <code>src/kit/balance/typist.ts:90</code> | <code>Khá</code> |
| <code>src/kit/balance/typist.ts:91</code> | <code>Ẩu</code> |
| <code>src/kit/balance/typist.ts:91</code> | <code>Gõ nhanh nhưng ẩu</code> |
| <code>src/kit/balance/typist.ts:92</code> | <code>Người gõ giỏi</code> |
| <code>src/kit/balance/typist.ts:93</code> | <code>Không gõ</code> |
| <code>src/kit/balance/typist.ts:93</code> | <code>Kiểm &quot;gõ là sức chính&quot;</code> |
| <code>src/kit/balance/typist.ts:94</code> | <code>Chỉ gõ</code> |
| <code>src/kit/balance/typist.ts:94</code> | <code>Kiểm &quot;hỗ trợ cần thiết&quot;</code> |
| <code>src/kit/feedback/profiles.ts:51</code> | <code>HOÀN HẢO</code> |
| <code>src/kit/input/keys.ts:45</code> | <code>àáạảãâầấậẩẫăằắặẳẵ</code> |
| <code>src/kit/input/keys.ts:46</code> | <code>èéẹẻẽêềếệểễ</code> |
| <code>src/kit/input/keys.ts:47</code> | <code>ìíịỉĩ</code> |
| <code>src/kit/input/keys.ts:48</code> | <code>òóọỏõôồốộổỗơờớợởỡ</code> |
| <code>src/kit/input/keys.ts:49</code> | <code>ùúụủũưừứựửữ</code> |
| <code>src/kit/input/keys.ts:50</code> | <code>ỳýỵỷỹ</code> |
| <code>src/kit/input/keys.ts:51</code> | <code>đ</code> |
| <code>src/kit/speech/speech.ts:128</code> | <code>Thiết bị không có giọng đọc tiếng Anh</code> |

`src/kit/feedback/profiles.ts:51` còn HOÀN HẢO nhưng Last Line ghi đè bằng PERFECT trong FEEL. ADVICE_VI còn trong kit nhưng skillReport/adviceText dùng ADVICE_EN. `src/kit/speech/speech.ts:128` còn thông báo thiếu giọng đọc; Last Line không gắn callback setSpeechNotice nên thông báo này hiện không hiển thị. Các hàng kit còn lại là bảng tên hoặc bộ ký tự của module dùng chung; để Claude xử lý tại nguồn kit.

## Phạm vi test

`tests/english-ui.test.ts` quét literal TS/JS, các đoạn template, literal CSS và nội dung index.html. Bỏ `src/kit/**`, chỉ bỏ hằng FALLBACK trong `src/app/vocab.ts`, chú thích GLSL nói trên và đúng diagnostic đã ghi. Không miễn nguyên file hiện nghĩa từ. Các file đọc/hiện vi vẫn được quét literal: `src/app/vocab.ts`, `src/app/results.ts`, `src/view/hud.ts`, `src/view/strip.ts`, `src/view/screens.ts`; dữ liệu `word.vi`/`entry.vi` được giữ nguyên. Test kiểm cả template lồng và chữ dấu tách rời.

## Chú thích còn tiếng Việt ngoài kit

Giữ nguyên chú thích cũ; không tạo chú thích tiếng Việt mới trong mã.

| file:dòng | chú thích |
|---|---|
| <code>src/app/main.ts:45</code> | <code>* Tuyến Cuối (index.html), stage S0 &quot;Bản thử dọc&quot; (docs/BUILD_S0.md), theme</code> |
| <code>src/app/main.ts:46</code> | <code>* &quot;Vành Chân Trời&quot; (docs/changelog/2026-10-23-theme.md): the vocabulary</code> |
| <code>src/app/main.ts:47</code> | <code>* loads, the title screen waits (keyboard first: Bắt đầu, Chơi tiếp, Cài đặt,</code> |
| <code>src/app/main.ts:48</code> | <code>* Kho súng · Học từ), the world steps at 60 Hz in a session, the 3D stage</code> |
| <code>src/app/main.ts:52</code> | <code>* settings screen&#x27;s volumes, shake, pronunciation, mode and &quot;Nhịp tự điều&quot;),</code> |
| <code>src/app/main.ts:87</code> | <code>/** The mode (Thư giãn, Cân bằng, Thử thách) and &quot;Nhịp tự điều theo cách bạn gõ&quot;. */</code> |
| <code>src/app/main.ts:150</code> | <code>/** A run has begun: the title then offers &quot;Chơi tiếp&quot;, and the ship and quality wait for the next page. */</code> |
| <code>src/app/main.ts:221</code> | <code>/** During a run, a new mode or &quot;Nhịp tự điều&quot; waits for the next one. */</code> |
| <code>src/app/main.ts:419</code> | <code>// A run&#x27;s header is fixed when its world is made: another mode or &quot;Nhịp tự điều&quot; takes a new page.</code> |
| <code>src/app/main.ts:720</code> | <code>/** The stored skill profile, blended (what the &quot;Hồ sơ gõ&quot; panel shows). */</code> |
| <code>src/app/dev.ts:51</code> | <code>/** Every bay&#x27;s word as the scenarios type it (with Thiếu chữ&#x27;s hidden letters). */</code> |
| <code>src/app/journey.ts:2</code> | <code>* Hành trình (docs/BUILD_S1.md §4, R1 part): choose a stage of chapter 1</code> |
| <code>src/app/journey.ts:5</code> | <code>* stage&#x27;s reference kit (§4.1 &quot;Chơi một ải lẻ&quot;: its bays, Rèn levels to the</code> |
| <code>src/app/journey.ts:71</code> | <code>/** A stage&#x27;s stars (§4.1): won · armour ≥ 50 % · accuracy ≥ the rule&#x27;s bar (95 %, 90 % on Thiếu chữ). */</code> |
| <code>src/app/journey.ts:286</code> | <code>/** &quot;khắc: Ray · được: Pháo Sao&quot; for a row. */</code> |
| <code>src/app/motion.ts:20</code> | <code>/** The settings row (&quot;Giảm chuyển động&quot;): stores the choice and the stylesheet follows at once. */</code> |
| <code>src/app/menu.ts:2</code> | <code>* The keyboard menus of Tuyến Cuối (title, settings, the armory placeholder,</code> |
| <code>src/app/menu.ts:13</code> | <code>/** A setting&#x27;s value as shown (&quot;70 %&quot;, &quot;Bật&quot;); ← → change it. */</code> |
| <code>src/app/results.ts:5</code> | <code>* &quot;Hồ sơ gõ&quot; panel.</code> |
| <code>src/app/results.ts:51</code> | <code>* run (test pass 27/10: &quot;tiến bộ đều&quot; showed on a first run and under a loss</code> |
| <code>src/app/results.ts:63</code> | <code>/** The &quot;Hồ sơ gõ&quot; panel: the measured numbers, the advice, and what the next run will be. */</code> |
| <code>src/app/skill.ts:2</code> | <code>* The player&#x27;s skill profile in Tuyến Cuối (docs/games/BALANCE.md §2, §4.1,</code> |
| <code>src/app/skill.ts:97</code> | <code>* hard learning rule (Thiếu chữ, Nghĩa: typed from memory, slower than the</code> |
| <code>src/app/skill.ts:143</code> | <code>/** What the &quot;Hồ sơ gõ&quot; panel and the results line show. */</code> |
| <code>src/content/balance.ts:2</code> | <code>* Tuyến Cuối&#x27;s balance data (docs/games/BALANCE.md §4, §9.3; changelog</code> |
| <code>src/content/balance.ts:69</code> | <code>* lengths and Nhanh, and whether the in-run director runs. &quot;Nhịp tự điều</code> |
| <code>src/content/balance.ts:70</code> | <code>* theo cách bạn gõ: Tắt&quot; plays the standard pace: k = 1, E 35, no director</code> |
| <code>src/content/balance.ts:75</code> | <code>/** The guns on the bays (bay order), their Rèn levels, how many bays, the armour the line starts with. */</code> |
| <code>src/content/balance.ts:81</code> | <code>* stage&#x27;s learning factor ρ (spawns × k × ρ), the telegraph scale (R3) and</code> |
| <code>src/content/balance.ts:82</code> | <code>* the recall words (Nghĩa, R2). The same seed, header and keys give the same run.</code> |
| <code>src/content/balance.ts:98</code> | <code>* ρ (§7.3, §11.1): capacity with the rule&#x27;s familiarity over capacity with</code> |
| <code>src/content/balance.ts:100</code> | <code>* The stage&#x27;s spawns run at k × ρ: a typist on k&#x27;s floor still gets room</code> |
| <code>src/content/balance.ts:112</code> | <code>/** The kit for a stage: its bays, armour and Rèn levels, the levels going to the guns in the order they were picked. */</code> |
| <code>src/content/balance.ts:118</code> | <code>/** The standard typist&#x27;s view (E 35, 95 %, CV 0.25): ρ when &quot;Nhịp tự điều&quot; is off. */</code> |
| <code>src/content/balance.ts:121</code> | <code>/** The whole header of a stage run: the pace, the stage, its kit and ρ (from the typist&#x27;s view; the standard one when the pace is fixed). */</code> |
| <code>src/content/balance.ts:154</code> | <code>* next pack&#x27;s spawn interval −7 %, one Bọc Thép affix on the next plain pack,</code> |
| <code>src/content/balance.ts:161</code> | <code>* is Trụ vững&#x27;s, the trial&#x27;s.</code> |
| <code>src/content/stage-s0.ts:2</code> | <code>* The S0 stage, kept as the trial (&quot;Trận thử&quot;, docs/BUILD_S1.md §8):</code> |
| <code>src/content/stage-s0.ts:42</code> | <code>/** A surge&#x27;s strength in a run: its rate × a seeded draw in [lo, hi]; with `storm.chance` a &quot;dữ dội&quot; one from `storm.spread`. */</code> |
| <code>src/content/stage-rules.ts:15</code> | <code>/** Trụ vững: still standing when the time runs out. */</code> |
| <code>src/content/stage-rules.ts:17</code> | <code>/** Săn Đầu Đàn: `need` of the leaders arriving at `leaders` (s); lost when more than leaders − need get through; `cap` s at most. */</code> |
| <code>src/content/stage-rules.ts:29</code> | <code>/** The reference kit a stage is balanced for (§8): bays, Rèn levels (the first chosen gun gets the first), armour. */</code> |
| <code>src/content/stage-rules.ts:78</code> | <code>/** Thiếu chữ: words of up to `short` letters hide one letter, longer ones two; never the first, never two side by side. */</code> |
| <code>src/content/stage-rules.ts:82</code> | <code>* Vết nứt (§7.2): every `period` s from `first`, warned `warn` s ahead by a</code> |
| <code>src/content/stage-rules.ts:87</code> | <code>* magazine lost its extra damage (Mới, Trẻ em and Tia + Pháo Sao on stage 3).</code> |
| <code>src/content/stage-rules.ts:98</code> | <code>/** Săn: once enough leaders fall the horde pulls back: `retreat` s of fading, harmless, then the stage is won. */</code> |
| <code>src/content/threat.ts:6</code> | <code>* Σ weight × the best mark any of its guns has on the row (● 1, ○ 0.5, ✕ 0).</code> |
| <code>src/content/threat.ts:55</code> | <code>/** A kit&#x27;s score on a stage&#x27;s rows: Σ weight × the best mark among its guns. */</code> |
| <code>src/content/chapter-1.ts:2</code> | <code>* Chapter 1 &quot;Hành Lang VC-7&quot; (docs/BUILD_S1.md §8): stages 1–4 in R1 (5–9</code> |
| <code>src/content/chapter-1.ts:3</code> | <code>* in R2, the boss in R3). Rates at k = 1 in Cân bằng are starting points</code> |
| <code>src/content/chapter-1.ts:6</code> | <code>* How R1 reads §8&#x27;s &quot;Toán (tỉ lệ toán)&quot;: the share of the stage&#x27;s foes that</code> |
| <code>src/content/chapter-1.ts:8</code> | <code>* rows: &quot;lính&quot; is the scouts&#x27; share of their members) are the rest. A Trâu</code> |
| <code>src/content/chapter-1.ts:9</code> | <code>* pack is a Trâu with 5 mines behind it, a Khiên pack a Khiên with a wedge</code> |
| <code>src/content/chapter-1.ts:20</code> | <code>* of near guns (Xung + Tán reach 11.7 m) bled armour from foes it could not</code> |
| <code>src/content/chapter-1.ts:28</code> | <code>* pack more (more foes broke Ẩu, Mới and Trẻ em first). Stage 3 keeps 1</code> |
| <code>src/content/chapter-1.ts:31</code> | <code>* Khiên packs 13 → 10 %: at k 1.2–1.25 Khá and Nhanh, whose Xung + Pháo Sao</code> |
| <code>src/content/rules.ts:18</code> | <code>* The near zone (docs/games/BALANCE.md §3 &quot;vòng gần&quot;, §5): foes at z ≤ `z`</code> |
| <code>src/content/rules.ts:25</code> | <code>* Continuous pressure (BALANCE.md §5): the Bầy Hố Đen leaches the line&#x27;s</code> |
| <code>src/content/rules.ts:37</code> | <code>* The elite affix &quot;Bọc Thép&quot; (S0 called it &quot;Giáp&quot;; renamed in S1 so it</code> |
| <code>src/content/rules.ts:38</code> | <code>* does not clash with the line&#x27;s GIÁP bar or the foes&#x27; Vỏ): every member of</code> |
| <code>src/content/rules.ts:39</code> | <code>* a plain pack (mines, scouts, Tách) spawns with `hp` × its hit points and</code> |
| <code>src/content/rules.ts:84</code> | <code>/** Store sizes (the Ultra crowd cap fits). Bullets hold Xung rounds and Tán pellets; shells are Pháo Sao&#x27;s. */</code> |
| <code>src/content/foes.ts:2</code> | <code>* The horde&#x27;s kinds (docs/BUILD_S1.md §6): Bầy and Lính from S0 (numbers</code> |
| <code>src/content/foes.ts:3</code> | <code>* unchanged), Trâu (Vỏ), Khiên (an energy shield in front), Tách (breaks</code> |
| <code>src/content/foes.ts:4</code> | <code>* into three shards), its Mảnh, and Đầu Đàn (the hunt&#x27;s leader, of the</code> |
| <code>src/content/foes.ts:5</code> | <code>* Trâu family). Metres, seconds, hit points. Armour (Vỏ) comes off every</code> |
| <code>src/content/foes.ts:7</code> | <code>* their own list beside the grid (sim/hits.ts). R1 review: Mảnh 7 HP (§6</code> |
| <code>src/content/foes.ts:8</code> | <code>* had 9: a Xung round or a Tán pellet then took two hits a shard, and Tán,</code> |
| <code>src/content/foes.ts:10</code> | <code>* two). Đầu Đàn 300 HP (§6 had 360), × the mode and k as it spawns. R1</code> |
| <code>src/content/foes.ts:11</code> | <code>* close: Trâu Vỏ 5 → 4, as the clean magazine lost its extra damage on a</code> |
| <code>src/content/foes.ts:13</code> | <code>* a way through Vỏ; Trẻ em on stage 3, Xung + Tán on stage 2).</code> |
| <code>src/content/foes.ts:21</code> | <code>/** Vỏ: taken off every blow (at least 1 is left). */</code> |
| <code>src/content/foes.ts:32</code> | <code>/** Mass in the crowd&#x27;s push apart (a Trâu shoulders the swarm aside). */</code> |
| <code>src/content/foes.ts:34</code> | <code>/** Tán&#x27;s pellets push it back. */</code> |
| <code>src/content/foes.ts:36</code> | <code>/** Shield hit points (Khiên), 0 for none. */</code> |
| <code>src/content/foes.ts:38</code> | <code>/** May carry the Bọc Thép affix (plain packs only). */</code> |
| <code>src/content/foes.ts:58</code> | <code>/** A Trâu or Đầu Đàn closer than `z` charges: head down, `speed` × its stride. */</code> |
| <code>src/content/foes.ts:62</code> | <code>* Khiên&#x27;s energy shield: a 2.6 m wall `ahead` m in front of the body,</code> |
| <code>src/content/foes.ts:63</code> | <code>* turning toward the ship at most `turn` rad/s. Xung rounds and Tán pellets</code> |
| <code>src/content/foes.ts:65</code> | <code>* burns it; Pháo Sao falls past it. Broken, it never comes back and its</code> |
| <code>src/content/foes.ts:70</code> | <code>/** Tách breaks into `shards` Mảnh spread across `spread` m. */</code> |
| <code>src/content/foes.ts:78</code> | <code>/** Đầu Đàn&#x27;s escort: 8 mines walking ahead of it. */</code> |
| <code>src/content/guns.ts:3</code> | <code>* finished word. Xung and Tia are S0&#x27;s (numbers unchanged); Tán, Ray and</code> |
| <code>src/content/guns.ts:4</code> | <code>* Pháo Sao are new. Numbers are starting points tuned with the bots</code> |
| <code>src/content/guns.ts:16</code> | <code>/** Magazines a gun holds (the firing one included) at levels 1–2, and at level 3 (Rèn). */</code> |
| <code>src/content/guns.ts:22</code> | <code>* Typing quality of the loading word (S0&#x27;s numbers): Chuẩn (0 errors) ×1.06</code> |
| <code>src/content/guns.ts:24</code> | <code>* in S1, &quot;Băng Chuẩn xuyên Vỏ&quot;: a clean magazine meets armour × 0.75. On a</code> |
| <code>src/content/guns.ts:26</code> | <code>* damage; its reward is the Vỏ it pierces and the crit). The trial keeps ×1.06.</code> |
| <code>src/content/guns.ts:30</code> | <code>/** Rèn: damage per blow by level (1–3), magazines held by level. */</code> |
| <code>src/content/guns.ts:59</code> | <code>* Tán: 6 volleys in 2.3 s, 7 pellets fanned ±18° each, a 9 m radius, 7 a</code> |
| <code>src/content/guns.ts:80</code> | <code>* R1 guns 75 → 95, R1 close 112: two shots a Trâu (220 at k = 1; 2 × 111 =</code> |
| <code>src/content/guns.ts:85</code> | <code>* Ray&#x27;s fire control in a kit with no near gun (Ray + Pháo Sao; R1 guns, as</code> |
| <code>src/content/guns.ts:87</code> | <code>* first, a Đầu Đàn alone before it. Without it Ray kept to scouts and Trâu</code> |
| <code>src/content/guns.ts:92</code> | <code>* Pháo Sao: 4 shells in 3 s, each flying 0.7 s to the heaviest cluster (by</code> |
| <code>src/content/guns.ts:95</code> | <code>* stop them, and Vỏ meets them × 0.5 (the thin top). §5.1 started at 6</code> |
| <code>src/content/guns.ts:96</code> | <code>* shells, 3 m, 26 → 13: a pack died to a shell and every kit with Pháo Sao</code> |
| <code>src/content/guns.ts:98</code> | <code>* (G3c tuning: a kit with Pháo Sao and no near gun lost at the line); R1 close 22 → 23.</code> |
| <code>src/content/guns.ts:103</code> | <code>* Heavy guns (Ray, Pháo Sao) take words `short` / `long` letters longer at the</code> |
| <code>src/audio/theme-audio.ts:2</code> | <code>* The sound of Tuyến Cuối, &quot;Vành Chân Trời&quot; (docs/audio/THEME_SOUND_LIST.md):</code> |
| <code>src/audio/theme-audio.ts:75</code> | <code>/** S1 sounds: their bus, and the least time between two (ms; a sweep of blows on Vỏ is one ring, not a buzz). */</code> |
| <code>src/audio/music.ts:2</code> | <code>* The music placeholder of Tuyến Cuối, made in code until real stems exist</code> |
| <code>src/audio/gun-audio.ts:3</code> | <code>* in code on ThemeAudio&#x27;s buses like the rest of &quot;Vành Chân Trời&quot;: Tán&#x27;s</code> |
| <code>src/audio/gun-audio.ts:5</code> | <code>* cracking release with a tail, Pháo Sao&#x27;s mortar thump, whistle and deep</code> |
| <code>src/audio/gun-audio.ts:6</code> | <code>* burst, a blow ringing off Vỏ, a shield&#x27;s hum struck and its glass breaking,</code> |
| <code>src/audio/gun-audio.ts:7</code> | <code>* a Tách cracking apart, Đầu Đàn&#x27;s horn and fall, a rift&#x27;s groan and tearing</code> |
| <code>src/audio/gun-audio.ts:117</code> | <code>/** Each sound&#x27;s notes on an open voice; `pitch` × (Pháo Sao&#x27;s bursts climb a semitone each in a chain). */</code> |
| <code>src/audio/synth.ts:2</code> | <code>* Small Web Audio building blocks for the industrial palette of Tuyến Cuối:</code> |
| <code>src/view/chunks.ts:3</code> | <code>* light steel chunks whose edges glow hot (Lính&#x27;s electric, Đầu Đàn&#x27;s gold, a</code> |
| <code>src/view/chunks.ts:4</code> | <code>* Bọc Thép&#x27;s pale gold), cool to a steel rim over 1.2 s (a Trâu&#x27;s or Đầu</code> |
| <code>src/view/chunks.ts:5</code> | <code>* Đàn&#x27;s smoulder: its small ones over 4.8 s, its big ones hotter over 7.2 s,</code> |
| <code>src/view/theme.css:2</code> | <code>* Tuyến Cuối, theme &quot;Vành Chân Trời&quot;: an old steel station holding the last</code> |
| <code>src/view/theme.css:39</code> | <code>/* Guns (each its own hue): Xung electric blue, Tia heat, Tán amber, Ray white-blue, Pháo Sao vermilion. */</code> |
| <code>src/view/gun-rules.ts:35</code> | <code>* radius on the deck (m). A big kill and a Pháo Sao burst 5 &gt; Ray 4 &gt; Tán 3</code> |
| <code>src/view/gun-rules.ts:97</code> | <code>/** A Trâu&#x27;s and Đầu Đàn&#x27;s big chunks (§12, §13: up from §4.5&#x27;s 0.6–0.8 m, and more of them, to read as a field of wreckage 13 m out). */</code> |
| <code>src/view/gun-rules.ts:114</code> | <code>* ±`spread` rad, by the gun of the killing blow: Pháo Sao throws from the</code> |
| <code>src/view/gun-rules.ts:115</code> | <code>* burst&#x27;s centre and highest, Ray along its line and fastest, Tán along the</code> |
| <code>src/view/gun-rules.ts:125</code> | <code>/** A Trâu or Đầu Đàn, whatever killed it: all round, a field of wreckage (§13). */</code> |
| <code>src/view/ship-rules.ts:16</code> | <code>* Đầu Đàn; the ship aims for `share` of their weighted x, clamped ±`max`, on a</code> |
| <code>src/view/ship-rules.ts:17</code> | <code>* spring (ω, ζ, speed ≤ vmax) and banks −vx × 7° (±14°). Under `minWeight`</code> |
| <code>src/view/ship-rules.ts:19</code> | <code>* wander ramps over Σw `fade` (0.3 → 0.7) so a pack crossing 0.5 does not</code> |
| <code>src/view/ship-rules.ts:31</code> | <code>/** The near horde&#x27;s sums (Σw·x, Σw·z, Σw) over a foe store&#x27;s live slots. */</code> |
| <code>src/view/ship-rules.ts:135</code> | <code>* (Ray charging or firing 5 &gt; Pháo Sao 4 &gt; Tán 3 &gt; Xung 2 &gt; Tia 1), at most</code> |
| <code>src/view/ship-rules.ts:136</code> | <code>* ±50°, on a spring with ζ 0.7 (a slight overshoot: it snaps onto Ray&#x27;s</code> |
| <code>src/view/ship-rules.ts:138</code> | <code>* blow it faces the near horde&#x27;s weighted centre (from Σw 0.3, the drift&#x27;s</code> |
| <code>src/view/screens.ts:3</code> | <code>* survival.css with theme.css&#x27;s variables): the title &quot;Tuyến Cuối&quot; (with the</code> |
| <code>src/view/screens.ts:4</code> | <code>* mode), settings (with &quot;Nhịp tự điều&quot;), the armory and learning placeholder,</code> |
| <code>src/view/screens.ts:5</code> | <code>* the typing profile &quot;Hồ sơ gõ&quot;, pause and the results (with one line of</code> |
| <code>src/view/ship.ts:11</code> | <code>* FX_CORE for Pháo Sao) and join the sim&#x27;s path within 3 m (§4.1). Reduced</code> |
| <code>src/view/ship.ts:28</code> | <code>/** Muzzle sockets: the centre gun, Xung&#x27;s left and right, the core (Pháo Sao fires upward from it). */</code> |
| <code>src/view/strip.ts:14</code> | <code>* it the clean streak&#x27;s LED (&quot;SẠCH ×N&quot;, shown with the plate); a rift&#x27;s</code> |
| <code>src/view/strip.ts:169</code> | <code>/** A word finished: the word white-hot for 2 frames, then &quot;word · meaning ✓&quot; (or &quot;word ✓&quot; over the meaning when one line is too wide; &quot;word ✓ · ĐẦY&quot;). */</code> |
| <code>src/view/hud.ts:9</code> | <code>* its gun (name, colour, magazine LEDs: 2, or 3 at Rèn 3; a top stripe that</code> |
| <code>src/view/hud.ts:11</code> | <code>* than 26 px; Thiếu chữ&#x27;s hidden letters as &quot;_&quot; until typed or shown) and</code> |
| <code>src/view/hud.ts:19</code> | <code>* Top: armour, clock, kills, the objective&#x27;s plate (Săn: &quot;PACK LEADER 1/3&quot;), a</code> |
| <code>src/view/hud.ts:43</code> | <code>* (1.05 m), where the plate hid every muzzle flash, Tán&#x27;s flame tongues and</code> |
| <code>src/view/hud.ts:357</code> | <code>/** The objective&#x27;s plate: Săn counts leaders down and through. */</code> |
| <code>src/view/survival.css:2</code> | <code>* Tuyến Cuối HUD and screens (docs/BUILD_S0.md §7): DOM over the canvas,</code> |
| <code>src/view/survival.css:107</code> | <code>/* A bay without a gun: a dark steel plate (bay 3 opens at the Mốc, bay 4 later). */</code> |
| <code>src/view/survival.css:260</code> | <code>/* The typing profile (&quot;Hồ sơ gõ&quot;) and the results&#x27; advice line. */</code> |
| <code>src/view/hazard-fx.ts:2</code> | <code>* Effects that stand in the corridor (docs/BUILD_S1.md §12): Khiên&#x27;s energy</code> |
| <code>src/view/hazard-fx.ts:3</code> | <code>* walls and Vết nứt&#x27;s cracks, each one instanced shader quad (one draw call</code> |
| <code>src/view/typing-feel.ts:35</code> | <code>/** The gun colours (GUN ids: Xung, Tia, Tán, Ray, Pháo Sao); Ray&#x27;s mark in its ink (its white-blue drowned in Tia&#x27;s light). */</code> |
| <code>src/view/bolts.ts:5</code> | <code>* vanguard-bolt (Draconis: dragon-fireball), Tán solar-lance-bolt, Ray holds</code> |
| <code>src/view/bolts.ts:6</code> | <code>* frost-seraph-bolt at its muzzle while armed, Pháo Sao&#x27;s shells are</code> |
| <code>src/view/scene.ts:2</code> | <code>* The stage of Tuyến Cuối, &quot;Vành Chân Trời&quot; (docs/BUILD_S0.md §3, theme</code> |
| <code>src/view/scene.ts:33</code> | <code>* &quot;Nhìn từ trên xuống nghiêng 55°&quot;: the view is tilted 55° away from straight</code> |
| <code>src/view/screens-journey.ts:7</code> | <code>* what it counters and where it is poor, &quot;dài tới +1 chữ&quot; for the heavy guns, the</code> |
| <code>src/view/screens-journey.ts:8</code> | <code>* Rèn level the stage gives), the stage&#x27;s threats with a yellow mark where</code> |
| <code>src/view/gunfx.ts:6</code> | <code>* (shots.ts, the feel pass). Pháo Sao&#x27;s bursts close together chain, each a</code> |
| <code>src/view/gunfx.ts:8</code> | <code>*   Vỏ: a blow it stopped throws orange sparks back; a clean magazine&#x27;s</code> |
| <code>src/view/gunfx.ts:10</code> | <code>*   Khiên: its wall ripples where struck (hazard-fx ShieldWalls), sparks</code> |
| <code>src/view/gunfx.ts:11</code> | <code>*   slide off; broken, blue glass flies. Tách: a cracking flash as it splits.</code> |
| <code>src/view/gunfx.ts:12</code> | <code>*   Đầu Đàn: a swaying gold beacon above it and a gold stripe on the floor.</code> |
| <code>src/view/gunfx.ts:13</code> | <code>*   Trâu: dust rings on the deck under the nearest ones as they stomp.</code> |
| <code>src/view/gunfx.ts:30</code> | <code>/** Pháo Sao&#x27;s bursts this close (ms) chain: each a semitone higher, at most 4 steps. */</code> |
| <code>src/view/gunfx.ts:93</code> | <code>// A leader down (Săn): a T4 blow, a 45 ms stop, its fall.</code> |
| <code>src/view/gunfx.ts:155</code> | <code>/** A blow on Vỏ: stopped (orange sparks bounce back) or a clean magazine&#x27;s pierce (a white-blue streak); false when Vỏ took no part. `k`: far blows draw larger. */</code> |
| <code>src/view/gunfx.ts:169</code> | <code>/** Per frame: Đầu Đàn&#x27;s beacons, Trâu&#x27;s stomps, a rift&#x27;s glow. */</code> |
| <code>src/view/gunfx.ts:188</code> | <code>/** Đầu Đàn&#x27;s beacon and floor stripe; the stomp dust under the nearest Trâu. */</code> |
| <code>src/view/combat.ts:40</code> | <code>/** The gun of a killing blow (its chunks&#x27; throw): Xung and the rest, Tia, Tán, Ray, Pháo Sao. */</code> |
| <code>src/view/combat.ts:184</code> | <code>// Vỏ that stopped most of a blow: a tick, never a big hit.</code> |
| <code>src/view/combat.ts:195</code> | <code>// Beam ticks roll up per 4 m along the ray, not per foe: two or three numbers, not a stack; Tán&#x27;s pellets per foe.</code> |
| <code>src/view/combat.ts:197</code> | <code>// §4.3: a foe in Pháo Sao&#x27;s ring is heard in gun.phao.burst (one sound, never a stack of hits on top).</code> |
| <code>src/view/combat.ts:199</code> | <code>// §4.6: Xung&#x27;s blows shake by their tier; Tia, Tán, Ray and Pháo Sao only by their shot (shots.ts).</code> |
| <code>src/view/combat.ts:201</code> | <code>// Ray: a 12 ms stop at most every 300 ms (the hit stop&#x27;s own spacing); none for Tia, Tán or Pháo Sao.</code> |
| <code>src/view/combat.ts:353</code> | <code>// A Trâu or Đầu Đàn breaks like a heap of kills: T3, heavy debris.</code> |
| <code>src/view/crowd.ts:6</code> | <code>* their speed, bob and sway; Trâu and Đầu Đàn step heavily (1.1 Hz, the body</code> |
| <code>src/view/crowd.ts:8</code> | <code>* they charge; Đầu Đàn is drawn 1.25× a Trâu with gold veins; Khiên walks</code> |
| <code>src/view/crowd.ts:9</code> | <code>* hunched; Tách staggers and throbs at 2 Hz; a hit flashes white, knocks</code> |
| <code>src/view/crowd.ts:15</code> | <code>* kind wears the &quot;Bầy Hố Đen&quot; layer below.</code> |
| <code>src/view/crowd.ts:45</code> | <code>/** How far a blow pushes each kind back (a Trâu barely moves: 0.03 m against 0.12). */</code> |
| <code>src/view/crowd.ts:48</code> | <code>/** The Giáp affix draws a foe this much larger (and its veins gold). */</code> |
| <code>src/view/crowd.ts:54</code> | <code>* &quot;Bầy Hố Đen&quot;, the horde&#x27;s shared material layer (one new faction from the</code> |
| <code>src/view/crowd.ts:89</code> | <code>// x: hit flash (white hot), y: hurt (elites glow red), z: the Giáp affix (gold veins), w: the foe&#x27;s own phase.</code> |
| <code>src/view/crowd.ts:110</code> | <code>/** Per kind: body tint, vein colour (above 1 blooms), hairline, vein strength. Trâu and Đầu Đàn: deep gold; Khiên: blue. */</code> |
| <code>src/view/crowd.ts:253</code> | <code>// Heavy ones step at 1.1 Hz: the body leans onto the planted side; a charge drops the head; Đầu Đàn holds its head up; Khiên walks hunched.</code> |
| <code>src/view/crowd.ts:259</code> | <code>// Tách throbs at 2 Hz.</code> |
| <code>src/view/crowd.ts:265</code> | <code>// Bob: mines and shards quick, Tách lurching, heavy ones dipping 6 cm at each step.</code> |
| <code>src/view/theme.ts:2</code> | <code>* The 3D side of the &quot;Vành Chân Trời&quot; theme (src/view/theme.css holds the</code> |
| <code>src/view/theme.ts:3</code> | <code>* DOM side): one palette for the stage, the horde&#x27;s &quot;Bầy Hố Đen&quot; layer and</code> |
| <code>src/view/theme.ts:47</code> | <code>/** A Bọc Thép (armoured) foe&#x27;s death: gold. */</code> |
| <code>src/view/theme.ts:49</code> | <code>// S1 guns (theme.css&#x27;s --tan, --ray, --phao): Tán amber, Ray white-blue, Pháo Sao vermilion.</code> |
| <code>src/view/theme.ts:60</code> | <code>/** A blow Vỏ stopped: orange sparks bouncing back. */</code> |
| <code>src/view/theme.ts:62</code> | <code>/** A clean magazine piercing Vỏ: a white-blue streak. */</code> |
| <code>src/view/theme.ts:64</code> | <code>/** Khiên&#x27;s energy wall and its glass when it breaks. */</code> |
| <code>src/view/theme.ts:67</code> | <code>/** Đầu Đàn&#x27;s beacon: gold. */</code> |
| <code>src/view/type-rules.ts:61</code> | <code>* its crit and Vỏ pierce, docs/BUILD_S1.md §5.1). The first wrong key in a</code> |
| <code>src/view/shots.ts:6</code> | <code>* sparks, a 1.5 px shove); Tán: three flame tongues, smoke, casings, amber</code> |
| <code>src/view/shots.ts:7</code> | <code>* bolts; Pháo Sao: an upward flash, shells ≥ 4 % of the view long, a burst a</code> |
| <code>src/view/shots.ts:8</code> | <code>* fifth of the view; a Trâu&#x27;s or Đầu Đàn&#x27;s death as its own event (bigKill);</code> |
| <code>src/view/shots.ts:255</code> | <code>/** A Trâu or Đầu Đàn (`leader`: a quarter bigger, gold) killed at sim (x, z), its own event sized on the view (§12, §13): f0–f2 a warm flash, round and gold where Ray&#x27;s line is thin and white-blue, the lane lit round it; a fireball rolling up and out; a dark cloud as wide as the flash with lit edges, laid over the deck and the beams 3.5–4.5 s, embers drifting out of it; a scorch 9 s whose cracks glow 7 s; a small ring. Returns its stop (T3). */</code> |
| <code>src/view/shots.ts:293</code> | <code>/** A blow&#x27;s look by gun (Combat draws numbers and sounds); `armour`: Vỏ&#x27;s look is drawn (gunfx). */</code> |
| <code>src/view/shots.ts:436</code> | <code>/** Pháo Sao&#x27;s shells: crimson bolts nose-first along their arcs, a fading trail, the landing ring tightening. */</code> |
| <code>src/sim/projectiles.ts:2</code> | <code>* Rounds in flight (Xung rounds and Tán pellets: each step a segment,</code> |
| <code>src/sim/projectiles.ts:5</code> | <code>* gun deals: Vỏ off each blow (at least 1 left; a clean magazine meets less</code> |
| <code>src/sim/projectiles.ts:6</code> | <code>* of it), Tán&#x27;s knock-back, a Tách breaking into shards (spawned after the</code> |
| <code>src/sim/projectiles.ts:22</code> | <code>* recoil and the numbers); `pierce` × the foe&#x27;s Vỏ comes off the blow.</code> |
| <code>src/sim/projectiles.ts:66</code> | <code>/** Splits waiting for the end of the step: x, z, Bọc Thép. */</code> |
| <code>src/sim/projectiles.ts:81</code> | <code>/** The step&#x27;s dead Tách break: SPLIT.shards Mảnh across SPLIT.spread m, inside the walls. */</code> |
| <code>src/sim/projectiles.ts:115</code> | <code>/** Deals `damage` to shield `k` (Tia burns it, Tán&#x27;s pellets wear it); it breaks at 0. */</code> |
| <code>src/sim/weapons.ts:3</code> | <code>* the run&#x27;s kit at its Rèn level. A finished word loads one magazine (two at</code> |
| <code>src/sim/weapons.ts:5</code> | <code>* damage (Chuẩn, Rèn), fire rate (Nhanh), crit chance, and the share of Vỏ</code> |
| <code>src/sim/weapons.ts:32</code> | <code>/** 1 when the kit has no near gun (Xung, Tia, Tán): Ray takes the line first (RAY_DUTY). */</code> |
| <code>src/sim/weapons.ts:34</code> | <code>/** Per bay: its gun (−1 none), Rèn level, magazines it can hold, magazines held (the firing one included). */</code> |
| <code>src/sim/weapons.ts:39</code> | <code>/** Per bay × MAG_CAP magazines (the firing one first): damage and fire-rate multipliers, crit chance, Vỏ met, perfect (1). */</code> |
| <code>src/sim/hits.ts:5</code> | <code>* MAX_RADIUS: Trâu, Đầu Đàn) are not in the grid: they sit in a short list</code> |
| <code>src/sim/stage.ts:2</code> | <code>* The stage&#x27;s objective (docs/BUILD_S1.md §7.1): Trụ vững is won when the</code> |
| <code>src/sim/stage.ts:3</code> | <code>* time runs out with armour left; Săn Đầu Đàn when `need` leaders fall (the</code> |
| <code>src/sim/move.ts:5</code> | <code>* ship), a slight sideways wobble, scouts holding a firing line, Trâu and</code> |
| <code>src/sim/move.ts:6</code> | <code>* Đầu Đàn charging the last metres, Khiên turning its shield toward the</code> |
| <code>src/sim/move.ts:7</code> | <code>* ship, and a push apart (by mass: a Trâu shoulders the swarm aside)</code> |
| <code>src/sim/move.ts:45</code> | <code>/** sin(2π p) without trigonometry (deterministic everywhere): Bhaskara&#x27;s parabola pair. */</code> |
| <code>src/sim/move.ts:96</code> | <code>/** S1 kinds&#x27; stride: Trâu and Đầu Đàn charge inside CHARGE.z, a Khiên whose shield broke hurries. */</code> |
| <code>src/sim/words.ts:12</code> | <code>* Thiếu chữ hides one letter of a word (two from 7 letters): never the</code> |
| <code>src/sim/words.ts:56</code> | <code>/** Thiếu chữ: bit i set when letter i is hidden, and when a wrong key showed it. */</code> |
| <code>src/sim/words.ts:132</code> | <code>/** Thiếu chữ: picks the hidden letters of bay `slot`&#x27;s new word. */</code> |
| <code>src/sim/words.ts:206</code> | <code>// The lock let go: a word dropped (BALANCE.md §3 &quot;bỏ khóa&quot;).</code> |
| <code>src/sim/spawn.ts:4</code> | <code>* and ρ, over the director&#x27;s spawn interval scale) accrues foes owed; once a</code> |
| <code>src/sim/spawn.ts:6</code> | <code>* block, wedge or line, scouts in its back rows, the Bọc Thép affix on some</code> |
| <code>src/sim/spawn.ts:7</code> | <code>* plain packs (sim/pace.ts). Special packs (a Trâu or a Khiên leading mines,</code> |
| <code>src/sim/spawn.ts:8</code> | <code>* a group of Tách) take their share of the foes from their `from` time,</code> |
| <code>src/sim/spawn.ts:11</code> | <code>* Đầu Đàn walk in at the hunt&#x27;s times with their escort. A group that would</code> |
| <code>src/sim/spawn.ts:95</code> | <code>/** A foe of `kind` at (x, z), its shield with it (Khiên). */</code> |
| <code>src/sim/spawn.ts:108</code> | <code>* A special pack: a Trâu (block of 5 mines behind it; its hit points × the</code> |
| <code>src/sim/spawn.ts:109</code> | <code>* mode and k) or a Khiên (a wedge of 6 behind its shield) in front, or a</code> |
| <code>src/sim/spawn.ts:110</code> | <code>* group of Tách (plain: it may carry Bọc Thép).</code> |
| <code>src/sim/spawn.ts:135</code> | <code>// A Trâu&#x27;s hit points × the mode and k, as a Đầu Đàn&#x27;s (R1 guns: a child in Thư giãn met S1&#x27;s full Trâu, B3).</code> |
| <code>src/sim/spawn.ts:148</code> | <code>* A Đầu Đàn and its escort walk in: 8 mines ahead (× the mode and k, 4–12),</code> |
| <code>src/sim/spawn.ts:150</code> | <code>* a child in Thư giãn met the full leader), its horn a telegraph.</code> |
| <code>src/sim/stores.ts:40</code> | <code>/** Foe `mark` bits: its shield broke (it walks faster), it is charging (Trâu, Đầu Đàn close in). */</code> |
| <code>src/sim/stores.ts:45</code> | <code>* the Bọc Thép affix; maxHp: its hit points at spawn; shield: its shield&#x27;s</code> |
| <code>src/sim/stores.ts:96</code> | <code>/** Bullet kinds: a Xung round, a Tán pellet. */</code> |
| <code>src/sim/stores.ts:100</code> | <code>* Xung rounds and Tán pellets. flags: the hit&#x27;s flags (crit, perfect, gun…).</code> |
| <code>src/sim/stores.ts:102</code> | <code>* pierce: the armour a blow meets (× Vỏ); bay: the bay that fired it.</code> |
| <code>src/sim/stores.ts:160</code> | <code>/** Pháo Sao shells: where and when they land (the view draws their arc from the muzzle), their blow. */</code> |
| <code>src/sim/stores.ts:188</code> | <code>* Khiên&#x27;s energy shields: a wall SHIELD.width wide, its centre (x, z)</code> |
| <code>src/sim/pace.ts:7</code> | <code>*   elite   one Bọc Thép affix on the next plain pack (or off the next armoured one);</code> |
| <code>src/sim/pace.ts:240</code> | <code>* A new plain pack&#x27;s affix: every ELITE.every-th from ELITE.from s carries Bọc Thép;</code> |
| <code>src/sim/events.ts:16</code> | <code>/** Tán fires a volley (slot: bay; x, z: the muzzle; dx, dz: the fan&#x27;s axis; value: pellets). */</code> |
| <code>src/sim/events.ts:22</code> | <code>/** Pháo Sao launches a shell (slot: bay; ref: shell id; x, z: where it lands; value: flight seconds). */</code> |
| <code>src/sim/events.ts:30</code> | <code>/** A Tách breaks (slot, ref: the Tách; x, z; value: shards). */</code> |
| <code>src/sim/events.ts:34</code> | <code>/** A Đầu Đàn walks in at the gate (slot, ref: it; x, z). */</code> |
| <code>src/sim/events.ts:53</code> | <code>* Bọc Thép (an armoured foe); S1: the blow&#x27;s gun (Tán, Ray, Pháo Sao), Vỏ</code> |
| <code>src/sim/events.ts:54</code> | <code>* took some of it, a clean magazine pierced Vỏ, a knock-back, a big foe.</code> |
| <code>src/sim/plan.ts:8</code> | <code>* the run&#x27;s scales (mode, pace k, the stage&#x27;s ρ).</code> |
| <code>src/sim/plan.ts:23</code> | <code>* (`surgeSpread`), a &quot;dữ dội&quot; one at the storm chance (halved by a heavy</code> |
| <code>src/sim/plan.ts:66</code> | <code>/** A surge starting is a telegraph (the &quot;ĐỈNH TRÀN&quot; banner): an event once, as it begins. */</code> |
| <code>src/sim/world.ts:2</code> | <code>* The Tuyến Cuối world and its fixed 60 Hz step (docs/BUILD_S0.md §1,</code> |
| <code>src/sim/world.ts:14</code> | <code>* the kit, ρ) is set before the first step from the player&#x27;s skill profile</code> |
| <code>src/sim/world.ts:59</code> | <code>/** ρ: the stage&#x27;s learning factor (spawns × k × ρ). */</code> |
| <code>src/sim/world.ts:81</code> | <code>// ρ is a stage factor like the mode&#x27;s: it scales the stage&#x27;s pace as k does.</code> |
| <code>src/sim/hazards.ts:2</code> | <code>* Hazards (docs/BUILD_S1.md §7.2). R1 has Vết nứt: every period from its</code> |
| <code>src/sim/hazards.ts:4</code> | <code>* a telegraph), then pours RIFT.foes mines (× the mode, k and ρ, 4–12) over</code> |
| <code>src/sim/guns/phao.ts:2</code> | <code>* Pháo Sao (docs/BUILD_S1.md §5.1): 6 shells a magazine in 3 s, each flying</code> |
| <code>src/sim/guns/aim.ts:27</code> | <code>* never reached. Its strips are then even in angle, by tan(θ/2) = aim / (L +</code> |
| <code>src/sim/guns/ray.ts:7</code> | <code>* at once. Target (fire control, ./aim.ts): Đầu Đàn, then Trâu, Khiên, a</code> |
| <code>src/sim/guns/tan.ts:2</code> | <code>* Tán (docs/BUILD_S1.md §5.1): 6 volleys a magazine in 2 s, each 7 pellets</code> |
