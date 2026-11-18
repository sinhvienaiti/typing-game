# Phiếu 130 · Kiểm kê trước sửa

Ngày 29/10/2026. Đường dẫn mã tính từ `games/.wt-ts-codex`; dòng ở bản trước sửa. Quét AST literal và từng phần template bằng TypeScript, HTML quét từng dòng. Bỏ chú thích, nghĩa từ và diagnostic nội bộ; dấu `×` nằm trong khoảng `[À-ỹ]` nhưng không phải chữ Việt.

266 đoạn literal/dòng HTML có chữ Việt mà người chơi đọc trong phạm vi cho sửa. Các đoạn nối bằng `+` được tách đúng ranh giới literal để duyệt không bỏ sót. Hai nhãn ASCII `Cao`, `Xong`, thuộc tính `lang` và phụ đề ASCII cũng được sửa và có trong bảng duyệt.

| file:dòng | chuỗi cũ |
|---|---|
| <code>index.html:10</code> | <code>    &lt;title&gt;Tuyến Cuối&lt;/title&gt;</code> |
| <code>index.html:13</code> | <code>    &lt;div id=&quot;svStage&quot; class=&quot;sv-stage&quot;&gt;&lt;canvas id=&quot;svCanvas&quot; aria-label=&quot;Hành lang Tuyến Cuối&quot;&gt;&lt;/canvas&gt;&lt;/div&gt;</code> |
| <code>index.html:14</code> | <code>    &lt;div id=&quot;svHud&quot; class=&quot;sv-hud&quot; aria-live=&quot;polite&quot;&gt;&lt;div class=&quot;sv-loading&quot;&gt;TUYẾN CUỐI · đang tải…&lt;/div&gt;&lt;/div&gt;</code> |
| <code>src/app/journey.ts:127</code> | <code>Ải </code> |
| <code>src/app/journey.ts:128</code> | <code>Qua ải </code> |
| <code>src/app/journey.ts:128</code> | <code> để mở</code> |
| <code>src/app/journey.ts:131</code> | <code>Quay lại</code> |
| <code>src/app/journey.ts:131</code> | <code>Màn chính</code> |
| <code>src/app/journey.ts:142</code> | <code>Nạp súng</code> |
| <code>src/app/journey.ts:142</code> | <code>Chọn </code> |
| <code>src/app/journey.ts:142</code> | <code> trong 5 súng</code> |
| <code>src/app/journey.ts:143</code> | <code>Quay lại</code> |
| <code>src/app/journey.ts:143</code> | <code>Chọn ải</code> |
| <code>src/app/journey.ts:278</code> | <code>Swarm giữa sân</code> |
| <code>src/app/journey.ts:279</code> | <code>Swarm sát vạch</code> |
| <code>src/app/journey.ts:280</code> | <code>Scout và đạn Scout</code> |
| <code>src/app/journey.ts:281</code> | <code>Brute, Pack Leader (Vỏ)</code> |
| <code>src/app/journey.ts:283</code> | <code>Splitter và Shard</code> |
| <code>src/app/journey.ts:291</code> | <code>khắc: </code> |
| <code>src/app/journey.ts:291</code> | <code>được: </code> |
| <code>src/app/journey.ts:303</code> | <code>Luật </code> |
| <code>src/app/journey.ts:309</code> | <code>Trụ vững </code> |
| <code>src/app/journey.ts:310</code> | <code>Săn </code> |
| <code>src/app/main.ts:67</code> | <code>Thấp</code> |
| <code>src/app/main.ts:67</code> | <code>Vừa</code> |
| <code>src/app/main.ts:67</code> | <code>Cực cao</code> |
| <code>src/app/main.ts:70</code> | <code>Tắt</code> |
| <code>src/app/main.ts:70</code> | <code>Theo máy</code> |
| <code>src/app/main.ts:70</code> | <code>Bật</code> |
| <code>src/app/main.ts:108</code> | <code>Trình duyệt này không chạy được WebGL, nên Tuyến Cuối không chơi được ở đây.</code> |
| <code>src/app/main.ts:179</code> | <code>TIẾP TẾ +</code> |
| <code>src/app/main.ts:179</code> | <code> GIÁP</code> |
| <code>src/app/main.ts:189</code> | <code>TRỤ VỮNG!</code> |
| <code>src/app/main.ts:189</code> | <code>TUYẾN ĐÃ VỠ</code> |
| <code>src/app/main.ts:189</code> | <code>VƯỢT ẢI!</code> |
| <code>src/app/main.ts:189</code> | <code>ẢI THẤT THỦ</code> |
| <code>src/app/main.ts:220</code> | <code>Bật</code> |
| <code>src/app/main.ts:220</code> | <code>Tắt</code> |
| <code>src/app/main.ts:222</code> | <code>Áp dụng từ trận sau</code> |
| <code>src/app/main.ts:228</code> | <code>Hành trình</code> |
| <code>src/app/main.ts:228</code> | <code>Chương 1 · ải 1–</code> |
| <code>src/app/main.ts:228</code> | <code> · chọn ải, nạp súng</code> |
| <code>src/app/main.ts:229</code> | <code>Trận thử lại</code> |
| <code>src/app/main.ts:229</code> | <code>Trận thử</code> |
| <code>src/app/main.ts:229</code> | <code>Bỏ </code> |
| <code>src/app/main.ts:229</code> | <code>trận</code> |
| <code>src/app/main.ts:229</code> | <code>Ải </code> |
| <code>src/app/main.ts:229</code> | <code> đang dở, vào trận thử mới</code> |
| <code>src/app/main.ts:229</code> | <code>Pulse Gun và Heat Beam · giữ hành lang </code> |
| <code>src/app/main.ts:229</code> | <code> phút</code> |
| <code>src/app/main.ts:230</code> | <code>Chơi tiếp</code> |
| <code>src/app/main.ts:230</code> | <code>Về trận đang tạm dừng</code> |
| <code>src/app/main.ts:230</code> | <code>Chưa có trận đang dở</code> |
| <code>src/app/main.ts:231</code> | <code>Chế độ</code> |
| <code>src/app/main.ts:232</code> | <code>Hồ sơ gõ</code> |
| <code>src/app/main.ts:232</code> | <code>Tốc độ, độ chính xác, lời khuyên</code> |
| <code>src/app/main.ts:233</code> | <code>Cài đặt</code> |
| <code>src/app/main.ts:233</code> | <code>Âm thanh, rung, nhịp, tàu, chất lượng hình</code> |
| <code>src/app/main.ts:234</code> | <code>Kho súng · Học từ</code> |
| <code>src/app/main.ts:234</code> | <code>5 súng: băng đạn, tầm; cách học từ</code> |
| <code>src/app/main.ts:237</code> | <code>Đổi được khi chưa có trận dở (bỏ trận để đổi)</code> |
| <code>src/app/main.ts:239</code> | <code>Âm hiệu ứng</code> |
| <code>src/app/main.ts:240</code> | <code>Nhạc</code> |
| <code>src/app/main.ts:241</code> | <code>Rung màn hình</code> |
| <code>src/app/main.ts:241</code> | <code>Đang tắt bởi ?shake=0</code> |
| <code>src/app/main.ts:242</code> | <code>Giảm chuyển động</code> |
| <code>src/app/main.ts:242</code> | <code>Tàu không trôi, không lao; chữ không nảy</code> |
| <code>src/app/main.ts:243</code> | <code>Đọc từ tiếng Anh</code> |
| <code>src/app/main.ts:244</code> | <code>Nhịp tự điều theo cách bạn gõ</code> |
| <code>src/app/main.ts:244</code> | <code>Swarm dày thưa theo hồ sơ gõ của bạn</code> |
| <code>src/app/main.ts:244</code> | <code>Nhịp chuẩn cố định, không điều trong trận</code> |
| <code>src/app/main.ts:245</code> | <code>Tàu</code> |
| <code>src/app/main.ts:246</code> | <code>Chất lượng hình</code> |
| <code>src/app/main.ts:252</code> | <code>Quay lại</code> |
| <code>src/app/main.ts:255</code> | <code>Chơi tiếp</code> |
| <code>src/app/main.ts:256</code> | <code>Cài đặt</code> |
| <code>src/app/main.ts:256</code> | <code>Âm thanh, rung, đọc từ</code> |
| <code>src/app/main.ts:257</code> | <code>Về màn chính</code> |
| <code>src/app/main.ts:257</code> | <code>Trận giữ nguyên, chơi tiếp được</code> |
| <code>src/app/main.ts:262</code> | <code>Ải </code> |
| <code>src/app/main.ts:263</code> | <code>Chơi lại</code> |
| <code>src/app/main.ts:263</code> | <code>Chơi lại ải</code> |
| <code>src/app/main.ts:264</code> | <code>Chọn ải</code> |
| <code>src/app/main.ts:264</code> | <code>Hành trình</code> |
| <code>src/app/main.ts:265</code> | <code>Màn chính</code> |
| <code>src/app/main.ts:282</code> | <code>Bầy Hố Đen tràn ra từ mép hố đen. Gõ từ trên hai bến súng để nạp đạn; súng tự bắn. Gõ không lỗi thì đạn xuyên Vỏ và dễ chí mạng.</code> |
| <code>src/app/main.ts:283</code> | <code>TÀU </code> |
| <code>src/app/main.ts:283</code> | <code> · HÌNH </code> |
| <code>src/app/main.ts:288</code> | <code>Đổi tàu hoặc chất lượng hình thì trang tải lại khi bấm Xong.</code> |
| <code>src/app/main.ts:293</code> | <code>, tầm </code> |
| <code>src/app/main.ts:293</code> | <code>, từ có thể dài hơn 1 chữ</code> |
| <code>src/app/main.ts:295</code> | <code>Gõ không lỗi: xuyên Vỏ (Vỏ chỉ chặn 75 %) và dễ chí mạng; ở Trận thử đòn mạnh thêm 6 %.</code> |
| <code>src/app/main.ts:296</code> | <code>Mỗi từ gõ xong được ghi vào sổ học chung của portal (mã typing-survival).</code> |
| <code>src/app/main.ts:304</code> | <code>TRẬN THỬ</code> |
| <code>src/app/main.ts:304</code> | <code>ẢI </code> |
| <code>src/app/main.ts:305</code> | <code>Giữ hành lang </code> |
| <code>src/app/main.ts:305</code> | <code> phút</code> |
| <code>src/app/main.ts:313</code> | <code>Ải </code> |
| <code>src/app/main.ts:578</code> | <code>GIỮ TUYẾN!</code> |
| <code>src/app/main.ts:578</code> | <code>ẢI </code> |
| <code>src/app/main.ts:635</code> | <code>Tắt bộ gõ tiếng Việt để gõ</code> |
| <code>src/app/main.ts:635</code> | <code>Từ dự phòng (máy chủ không có từ vựng)</code> |
| <code>src/app/main.ts:702</code> | <code>Tuyến Cuối</code> |
| <code>src/app/results.ts:18</code> | <code>Thời gian</code> |
| <code>src/app/results.ts:19</code> | <code>Hạ</code> |
| <code>src/app/results.ts:20</code> | <code>Chính xác</code> |
| <code>src/app/results.ts:21</code> | <code>Từ đã gõ</code> |
| <code>src/app/results.ts:41</code> | <code>Hồ sơ gõ (trung bình các trận) nay là </code> |
| <code>src/app/results.ts:41</code> | <code> WPM, chính xác </code> |
| <code>src/app/results.ts:42</code> | <code>Trận này ít từ quá, chưa tính vào hồ sơ gõ.</code> |
| <code>src/app/results.ts:43</code> | <code>Bạn rời bàn phím lâu, trận này không tính vào hồ sơ gõ.</code> |
| <code>src/app/results.ts:44</code> | <code>Trận này lệch xa thường lệ, chưa tính vào hồ sơ gõ.</code> |
| <code>src/app/results.ts:56</code> | <code>Chưa có số đo: chơi vài trận để có lời khuyên theo cách bạn gõ.</code> |
| <code>src/app/results.ts:57</code> | <code>Tuyến vỡ: nạp súng trước đỉnh tràn, và khi Swarm dày, gõ dứt điểm từng từ.</code> |
| <code>src/app/results.ts:58</code> | <code>Trận đầu đã vào hồ sơ gõ: chơi thêm để có lời khuyên theo cách bạn gõ.</code> |
| <code>src/app/results.ts:69</code> | <code>đo đủ</code> |
| <code>src/app/results.ts:69</code> | <code>đang đo </code> |
| <code>src/app/results.ts:69</code> | <code>mặc định</code> |
| <code>src/app/results.ts:72</code> | <code>Tốc độ (WPM)</code> |
| <code>src/app/results.ts:73</code> | <code>Chính xác</code> |
| <code>src/app/results.ts:74</code> | <code>Nhận từ mới</code> |
| <code>src/app/results.ts:75</code> | <code>Độ đều</code> |
| <code>src/app/results.ts:75</code> | <code>lệch ±</code> |
| <code>src/app/results.ts:75</code> | <code> % mỗi từ</code> |
| <code>src/app/results.ts:79</code> | <code>Đã chơi </code> |
| <code>src/app/results.ts:79</code> | <code> trận</code> |
| <code>src/app/results.ts:79</code> | <code>, chưa đủ số đo: đang dùng mặc định của chế độ</code> |
| <code>src/app/results.ts:79</code> | <code>Chưa có trận nào: hồ sơ đang dùng mặc định của chế độ </code> |
| <code>src/app/results.ts:81</code> | <code>Trận tới: </code> |
| <code>src/app/results.ts:81</code> | <code>, nhịp ×</code> |
| <code>src/app/results.ts:81</code> | <code>, từ </code> |
| <code>src/app/results.ts:81</code> | <code> chữ, tự điều trong trận.</code> |
| <code>src/app/results.ts:82</code> | <code>Trận tới: </code> |
| <code>src/app/results.ts:82</code> | <code>, nhịp chuẩn cố định (đã tắt tự điều).</code> |
| <code>src/app/skill.ts:159</code> | <code>Hai trận thắng dễ liền: thử chế độ </code> |
| <code>src/app/skill.ts:161</code> | <code>Hai trận thua liền: chế độ </code> |
| <code>src/app/skill.ts:161</code> | <code> sẽ dễ thở hơn.</code> |
| <code>src/content/balance.ts:28</code> | <code>Thư giãn</code> |
| <code>src/content/balance.ts:28</code> | <code>Swarm thưa, đi chậm: gõ thong thả, học từ là chính</code> |
| <code>src/content/balance.ts:29</code> | <code>Cân bằng</code> |
| <code>src/content/balance.ts:29</code> | <code>Căng vừa sức: lúc dồn, lúc thở</code> |
| <code>src/content/balance.ts:30</code> | <code>Thử thách</code> |
| <code>src/content/balance.ts:30</code> | <code>Swarm dày, đỉnh tràn gắt: giữ tuyến là kỳ công</code> |
| <code>src/content/chapter-1.ts:41</code> | <code>Ca trực đầu</code> |
| <code>src/content/chapter-1.ts:59</code> | <code>Săn Pack Leader</code> |
| <code>src/content/chapter-1.ts:76</code> | <code>Vách nứt</code> |
| <code>src/content/chapter-1.ts:93</code> | <code>Khiên sáng</code> |
| <code>src/content/guns.ts:130</code> | <code>pháo xung liên thanh</code> |
| <code>src/content/guns.ts:130</code> | <code> viên trong 2,4 s vào con gần vạch nhất</code> |
| <code>src/content/guns.ts:130</code> | <code>Trận thử: </code> |
| <code>src/content/guns.ts:130</code> | <code> viên</code> |
| <code>src/content/guns.ts:131</code> | <code>tia nhiệt quét</code> |
| <code>src/content/guns.ts:131</code> | <code>tia 12 m cháy 2,5 s, quét về cụm dày</code> |
| <code>src/content/guns.ts:132</code> | <code>súng chùm đẩy lùi</code> |
| <code>src/content/guns.ts:132</code> | <code>6 loạt × 7 viên xòe, đẩy lùi Swarm sát tàu</code> |
| <code>src/content/guns.ts:133</code> | <code>súng ray xuyên hàng</code> |
| <code>src/content/guns.ts:133</code> | <code>3 phát xuyên 6 con, phá khiên</code> |
| <code>src/content/guns.ts:134</code> | <code>pháo cối nổ vùng</code> |
| <code>src/content/guns.ts:134</code> | <code>4 quả nổ 2,5 m vào cụm nặng</code> |
| <code>src/content/guns.ts:148</code> | <code>Swarm giữa sân</code> |
| <code>src/content/guns.ts:149</code> | <code>Swarm sát vạch</code> |
| <code>src/content/guns.ts:150</code> | <code>Scout và đạn Scout</code> |
| <code>src/content/guns.ts:151</code> | <code>Brute, Pack Leader (Vỏ)</code> |
| <code>src/content/guns.ts:152</code> | <code>Shield Guard và toán sau khiên</code> |
| <code>src/content/guns.ts:153</code> | <code>Splitter và Shard</code> |
| <code>src/content/stage-rules.ts:62</code> | <code>Trụ vững</code> |
| <code>src/content/stage-rules.ts:62</code> | <code>Săn Pack Leader</code> |
| <code>src/content/stage-rules.ts:74</code> | <code>Chuẩn</code> |
| <code>src/content/stage-rules.ts:75</code> | <code>Thiếu chữ</code> |
| <code>src/content/stage-s0.ts:56</code> | <code>Trận thử</code> |
| <code>src/view/hud.ts:57</code> | <code>MỚI · BRUTE · (QUÁI LỰC LƯỠNG) VỎ </code> |
| <code>src/view/hud.ts:58</code> | <code>MỚI · PACK LEADER · (THỦ LĨNH BẦY) VỎ </code> |
| <code>src/view/hud.ts:59</code> | <code>MỚI · SHIELD GUARD · (LÍNH MANG KHIÊN) CHẮN ĐẠN PHÍA TRƯỚC</code> |
| <code>src/view/hud.ts:60</code> | <code>MỚI · SPLITTER · (QUÁI TÁCH MẢNH) VỠ 3 SHARD</code> |
| <code>src/view/hud.ts:131</code> | <code>GIÁP</code> |
| <code>src/view/hud.ts:139</code> | <code>còn lại</code> |
| <code>src/view/hud.ts:144</code> | <code>hạ / 3 s</code> |
| <code>src/view/hud.ts:269</code> | <code>ĐỈNH TRÀN </code> |
| <code>src/view/hud.ts:269</code> | <code> · DỮ DỘI</code> |
| <code>src/view/hud.ts:278</code> | <code>Tổng </code> |
| <code>src/view/hud.ts:360</code> | <code>SWARM RÚT LUI</code> |
| <code>src/view/hud.ts:360</code> | <code> · LỌT </code> |
| <code>src/view/hud.ts:363</code> | <code>SWARM RÚT LUI!</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>quái Brute</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>quái Pack Leader</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>quái Shield Guard</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>luật Săn</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>hiểm họa Rift</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>luật Thiếu chữ</code> |
| <code>src/view/screens-journey.ts:21</code> | <code>(bầy quái) </code> |
| <code>src/view/screens-journey.ts:21</code> | <code> máu, đông</code> |
| <code>src/view/screens-journey.ts:22</code> | <code>(lính trinh sát) đứng 6–9 m bắn tàu</code> |
| <code>src/view/screens-journey.ts:23</code> | <code>(quái lực lưỡng) Vỏ </code> |
| <code>src/view/screens-journey.ts:23</code> | <code> máu, dẫn 5 Swarm</code> |
| <code>src/view/screens-journey.ts:24</code> | <code>(thủ lĩnh bầy) Vỏ </code> |
| <code>src/view/screens-journey.ts:24</code> | <code> máu, 8 Swarm hộ tống</code> |
| <code>src/view/screens-journey.ts:25</code> | <code>(lính mang khiên) khiên </code> |
| <code>src/view/screens-journey.ts:25</code> | <code> chắn đạn từ phía trước</code> |
| <code>src/view/screens-journey.ts:26</code> | <code>(quái tách mảnh) vỡ thành 3 Shard</code> |
| <code>src/view/screens-journey.ts:32</code> | <code>Giữ tuyến tới khi hết giờ. Hết giáp là thua.</code> |
| <code>src/view/screens-journey.ts:33</code> | <code>Pack Leader tới ở giây </code> |
| <code>src/view/screens-journey.ts:33</code> | <code> (tiếng tù và). Hạ </code> |
| <code>src/view/screens-journey.ts:33</code> | <code> con thì Swarm rút lui; để lọt quá </code> |
| <code>src/view/screens-journey.ts:33</code> | <code> con là thua.</code> |
| <code>src/view/screens-journey.ts:37</code> | <code>Không có hiểm họa.</code> |
| <code>src/view/screens-journey.ts:38</code> | <code>Rift (vết nứt không gian): mỗi </code> |
| <code>src/view/screens-journey.ts:38</code> | <code> s, tường trái hoặc phải sáng cam </code> |
| <code>src/view/screens-journey.ts:38</code> | <code> s trước khi đổ Swarm ra ở </code> |
| <code>src/view/screens-journey.ts:38</code> | <code> m. Giữ một súng gần có băng lúc sắp nứt.</code> |
| <code>src/view/screens-journey.ts:42</code> | <code>Mỗi từ ẩn một chữ, từ có ít nhất bảy chữ ẩn hai. Chữ đầu luôn hiện. Nghĩa và phiên âm vẫn hiện. Gõ sai chữ ẩn sẽ hiện chữ đúng.</code> |
| <code>src/view/screens-journey.ts:43</code> | <code>Từ và nghĩa hiện trên bến. Từ đang gõ hiện lớn phía trên mũi tàu. Bến đang gõ hiện phiên âm và nghĩa. Gõ xong, từ và nghĩa hiện cùng dấu ✓.</code> |
| <code>src/view/screens-journey.ts:52</code> | <code>&lt;h1&gt;HÀNH TRÌNH&lt;/h1&gt;</code> |
| <code>src/view/screens-journey.ts:53</code> | <code>&lt;div class=&quot;sv-title-en&quot;&gt;CHƯƠNG 1 · HÀNH LANG VC-7&lt;/div&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> |
| <code>src/view/screens-journey.ts:55</code> | <code>&lt;p class=&quot;sv-note&quot;&gt;Mỗi ải có trang bị riêng: số bến, cấp Rèn, giáp. Ải sau mở khi qua ải trước.&lt;/p&gt;</code> |
| <code>src/view/screens-journey.ts:56</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; chọn · &lt;kbd&gt;Enter&lt;/kbd&gt; xem ải · &lt;kbd&gt;Esc&lt;/kbd&gt; quay lại</code> |
| <code>src/view/screens-journey.ts:62</code> | <code>&lt;h1&gt;ẢI </code> |
| <code>src/view/screens-journey.ts:65</code> | <code>&lt;dt&gt;Mục tiêu&lt;/dt&gt;&lt;dd&gt;&lt;b&gt;</code> |
| <code>src/view/screens-journey.ts:66</code> | <code>&lt;dt&gt;Hiểm họa&lt;/dt&gt;&lt;dd&gt;</code> |
| <code>src/view/screens-journey.ts:67</code> | <code>&lt;dt&gt;Luật học&lt;/dt&gt;&lt;dd&gt;&lt;b&gt;</code> |
| <code>src/view/screens-journey.ts:68</code> | <code>&lt;dt&gt;Trang bị&lt;/dt&gt;&lt;dd&gt;</code> |
| <code>src/view/screens-journey.ts:68</code> | <code> bến · Rèn </code> |
| <code>src/view/screens-journey.ts:68</code> | <code> · giáp </code> |
| <code>src/view/screens-journey.ts:71</code> | <code>&lt;em&gt;MỚI&lt;/em&gt;</code> |
| <code>src/view/screens-journey.ts:73</code> | <code>&lt;p class=&quot;sv-note&quot;&gt;Ải này dạy: </code> |
| <code>src/view/screens-journey.ts:75</code> | <code>&lt;kbd&gt;Enter&lt;/kbd&gt; nạp súng · &lt;kbd&gt;Esc&lt;/kbd&gt; chọn ải</code> |
| <code>src/view/screens-journey.ts:84</code> | <code>&lt;h1&gt;NẠP SÚNG&lt;/h1&gt;</code> |
| <code>src/view/screens-journey.ts:85</code> | <code>&lt;div class=&quot;sv-title-en&quot;&gt;ẢI </code> |
| <code>src/view/screens-journey.ts:85</code> | <code> · CHỌN </code> |
| <code>src/view/screens-journey.ts:92</code> | <code>&lt;em&gt;BẾN </code> |
| <code>src/view/screens-journey.ts:92</code> | <code> · RÈN </code> |
| <code>src/view/screens-journey.ts:94</code> | <code> · tầm </code> |
| <code>src/view/screens-journey.ts:94</code> | <code> · từ dài tới +1 chữ</code> |
| <code>src/view/screens-journey.ts:95</code> | <code>&lt;p class=&quot;sv-good&quot;&gt;khắc: </code> |
| <code>src/view/screens-journey.ts:96</code> | <code>&lt;p class=&quot;sv-poor&quot;&gt;kém: </code> |
| <code>src/view/screens-journey.ts:101</code> | <code>&lt;div class=&quot;sv-threats&quot;&gt;&lt;b&gt;Ải này gặp gì · tỉ trọng&lt;/b&gt;</code> |
| <code>src/view/screens-journey.ts:106</code> | <code>BẮT ĐẦU</code> |
| <code>src/view/screens-journey.ts:106</code> | <code> · CÒN ⚠</code> |
| <code>src/view/screens-journey.ts:106</code> | <code>CHỌN THÊM </code> |
| <code>src/view/screens-journey.ts:106</code> | <code> SÚNG</code> |
| <code>src/view/screens-journey.ts:108</code> | <code>&lt;kbd&gt;1&lt;/kbd&gt;–&lt;kbd&gt;5&lt;/kbd&gt; chọn hoặc bỏ · &lt;kbd&gt;←&lt;/kbd&gt;&lt;kbd&gt;→&lt;/kbd&gt; di chuyển · &lt;kbd&gt;Enter&lt;/kbd&gt; chọn · &lt;kbd&gt;Esc&lt;/kbd&gt; quay lại ải</code> |
| <code>src/view/screens-journey.ts:119</code> | <code>Vượt ải</code> |
| <code>src/view/screens-journey.ts:119</code> | <code>Giáp còn ≥ 50 %</code> |
| <code>src/view/screens-journey.ts:119</code> | <code>Chính xác ≥ </code> |
| <code>src/view/screens.ts:66</code> | <code>&lt;div class=&quot;sv-title-tag&quot;&gt;&lt;span class=&quot;sv-dot&quot;&gt;&lt;/span&gt;TRẠM VC-7 · VÀNH CHÂN TRỜI&lt;/div&gt;</code> |
| <code>src/view/screens.ts:67</code> | <code>&lt;h1 class=&quot;sv-title-name&quot;&gt;TUYẾN CUỐI&lt;/h1&gt;</code> |
| <code>src/view/screens.ts:73</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; chọn · &lt;kbd&gt;Enter&lt;/kbd&gt; vào · &lt;kbd&gt;Esc&lt;/kbd&gt; quay lại</code> |
| <code>src/view/screens.ts:79</code> | <code>&lt;h1&gt;CÀI ĐẶT&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> |
| <code>src/view/screens.ts:82</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; chọn · &lt;kbd&gt;←&lt;/kbd&gt;&lt;kbd&gt;→&lt;/kbd&gt; đổi · &lt;kbd&gt;Esc&lt;/kbd&gt; xong</code> |
| <code>src/view/screens.ts:88</code> | <code>&lt;h1&gt;KHO SÚNG · HỌC TỪ&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> |
| <code>src/view/screens.ts:94</code> | <code>&lt;kbd&gt;Enter&lt;/kbd&gt; hoặc &lt;kbd&gt;Esc&lt;/kbd&gt; quay lại</code> |
| <code>src/view/screens.ts:100</code> | <code>&lt;h1&gt;HỒ SƠ GÕ&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> |
| <code>src/view/screens.ts:105</code> | <code>&lt;kbd&gt;Enter&lt;/kbd&gt; hoặc &lt;kbd&gt;Esc&lt;/kbd&gt; quay lại</code> |
| <code>src/view/screens.ts:111</code> | <code>&lt;h1&gt;TẠM DỪNG&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> |
| <code>src/view/screens.ts:113</code> | <code>&lt;kbd&gt;Esc&lt;/kbd&gt; chơi tiếp · &lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; chọn · &lt;kbd&gt;Enter&lt;/kbd&gt; vào</code> |
| <code>src/view/screens.ts:122</code> | <code>NHẤN PHÍM BẤT KỲ ĐỂ VÀO TRẬN</code> |
| <code>src/view/screens.ts:122</code> | <code>ĐANG NẠP…</code> |
| <code>src/view/screens.ts:123</code> | <code>Trong trận: &lt;kbd&gt;Esc&lt;/kbd&gt; tạm dừng</code> |
| <code>src/view/screens.ts:129</code> | <code>VƯỢT ẢI!</code> |
| <code>src/view/screens.ts:129</code> | <code>ẢI THẤT THỦ</code> |
| <code>src/view/screens.ts:129</code> | <code>TRỤ VỮNG!</code> |
| <code>src/view/screens.ts:129</code> | <code>TUYẾN ĐÃ VỠ</code> |
| <code>src/view/screens.ts:136</code> | <code> từ gần nhất · và </code> |
| <code>src/view/screens.ts:136</code> | <code> từ khác đã vào sổ học&lt;/p&gt;</code> |
| <code>src/view/screens.ts:138</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; chọn · &lt;kbd&gt;Enter&lt;/kbd&gt; vào · &lt;kbd&gt;Esc&lt;/kbd&gt; màn chính</code> |
| <code>src/view/strip.ts:197</code> | <code>ĐẦY</code> |
| <code>src/view/strip.ts:206</code> | <code>SẠCH ×</code> |

Bảy lời khuyên và nhãn HOÀN HẢO lấy động từ kit được liệt kê ở bảng duyệt cùng nguồn kit; không có literal tiếng Việt của chúng trong app trước sửa.
