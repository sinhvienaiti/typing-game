# Phiếu 130 · Bảng duyệt bản tiếng Anh

Ngày 29/10/2026. `file:dòng` trỏ bản sau sửa trong worktree `games/.wt-ts-codex`. 278 thay đổi chữ hiển thị (270 đoạn/thuộc tính trực tiếp + 7 lời khuyên cục bộ + 1 nhãn kit ghi đè), cộng 8 dòng test phụ thuộc chữ cũ. Không đổi id hay giá trị luật chơi.

Tên súng/quái theo `docs/games/NAMES_EN.md`; quyết định 28/10 trong AGENTS thay phần quy tắc ngôn ngữ 27/10 của tài liệu đó. Giáp sống của tàu gọi Hull, Vỏ quái gọi armor. Tàu chọn ở Options dùng nhãn ngắn Rig; chất lượng Med/Hi, nhạc BGM, số hạ KO. Claude cần duyệt các cách viết tắt này.

Độ dài tính số ký tự Unicode, bỏ thẻ HTML, giữ khoảng trắng. Mảnh literal được nối phải tính cả trường. `lengths.json` kiểm 5.304 lượt menu, 69 biến thể khác nhau: 0 nhãn/giá trị/ghi chú vượt 120%. Đã rút ngắn ghi chú Campaign và hai mô tả độ khó sau lượt kiểm đầu. Đây là kiểm nguồn, không phải xác nhận chữ không tràn khi render.

| file:dòng | chuỗi cũ | chuỗi mới | ghi chú |
|---|---|---|---|
| <code>src/app/journey.ts:127</code> | <code>Ải </code> | <code>Stage </code> | <code>Dòng cũ 127. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/journey.ts:128</code> | <code>Qua ải </code> | <code>Clear </code> | <code>Dòng cũ 128. Độ dài literal 7 → 6.</code> |
| <code>src/app/journey.ts:128</code> | <code> để mở</code> | <code> to unlock</code> | <code>Dòng cũ 128. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/journey.ts:131</code> | <code>Quay lại</code> | <code>Back</code> | <code>Dòng cũ 131. Độ dài literal 8 → 4.</code> |
| <code>src/app/journey.ts:131</code> | <code>Màn chính</code> | <code>Main menu</code> | <code>Dòng cũ 131. Độ dài literal 9 → 9.</code> |
| <code>src/app/journey.ts:142</code> | <code>Nạp súng</code> | <code>Loadout</code> | <code>Dòng cũ 142. Độ dài literal 8 → 7.</code> |
| <code>src/app/journey.ts:142</code> | <code>Chọn </code> | <code>Pick </code> | <code>Dòng cũ 142. Độ dài literal 5 → 5.</code> |
| <code>src/app/journey.ts:142</code> | <code> trong 5 súng</code> | <code> of 5 guns</code> | <code>Dòng cũ 142. Độ dài literal 13 → 10.</code> |
| <code>src/app/journey.ts:143</code> | <code>Quay lại</code> | <code>Back</code> | <code>Dòng cũ 143. Độ dài literal 8 → 4.</code> |
| <code>src/app/journey.ts:143</code> | <code>Chọn ải</code> | <code>Stages</code> | <code>Dòng cũ 143. Độ dài literal 7 → 6.</code> |
| <code>src/app/journey.ts:278</code> | <code>Swarm giữa sân</code> | <code>Swarm mid-lane</code> | <code>Dòng cũ 278. Độ dài literal 14 → 14.</code> |
| <code>src/app/journey.ts:279</code> | <code>Swarm sát vạch</code> | <code>Swarm at line</code> | <code>Dòng cũ 279. Độ dài literal 14 → 13.</code> |
| <code>src/app/journey.ts:280</code> | <code>Scout và đạn Scout</code> | <code>Scout and shots</code> | <code>Dòng cũ 280. Độ dài literal 18 → 15.</code> |
| <code>src/app/journey.ts:281</code> | <code>Brute, Pack Leader (Vỏ)</code> | <code>Brute, Pack Leader (armor)</code> | <code>Dòng cũ 281. Độ dài literal 23 → 26.</code> |
| <code>src/app/journey.ts:283</code> | <code>Splitter và Shard</code> | <code>Splitter and Shard</code> | <code>Dòng cũ 283. Độ dài literal 17 → 18.</code> |
| <code>src/app/journey.ts:291</code> | <code>khắc: </code> | <code>vs: </code> | <code>Dòng cũ 291. Độ dài literal 6 → 4.</code> |
| <code>src/app/journey.ts:291</code> | <code>được: </code> | <code>OK: </code> | <code>Dòng cũ 291. Độ dài literal 6 → 4.</code> |
| <code>src/app/journey.ts:303</code> | <code>Luật </code> | <code>Rule </code> | <code>Dòng cũ 303. Độ dài literal 5 → 5.</code> |
| <code>src/app/journey.ts:309</code> | <code>Trụ vững </code> | <code>Hold for </code> | <code>Dòng cũ 309. Độ dài literal 9 → 9.</code> |
| <code>src/app/journey.ts:310</code> | <code>Săn </code> | <code>Hunt </code> | <code>Dòng cũ 310. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:67</code> | <code>Thấp</code> | <code>Low</code> | <code>Dòng cũ 67. Độ dài literal 4 → 3.</code> |
| <code>src/app/main.ts:67</code> | <code>Vừa</code> | <code>Med</code> | <code>Dòng cũ 67. Đã rút gọn cho ô nhỏ. Độ dài literal 3 → 3.</code> |
| <code>src/app/main.ts:67</code> | <code>Cao</code> | <code>Hi</code> | <code>Dòng cũ 67. Đã rút gọn cho ô nhỏ. Độ dài literal 3 → 2.</code> |
| <code>src/app/main.ts:67</code> | <code>Cực cao</code> | <code>Ultra</code> | <code>Dòng cũ 67. Độ dài literal 7 → 5.</code> |
| <code>src/app/main.ts:70</code> | <code>Tắt</code> | <code>Off</code> | <code>Dòng cũ 70. Độ dài literal 3 → 3.</code> |
| <code>src/app/main.ts:70</code> | <code>Theo máy</code> | <code>System</code> | <code>Dòng cũ 70. Độ dài literal 8 → 6.</code> |
| <code>src/app/main.ts:70</code> | <code>Bật</code> | <code>On</code> | <code>Dòng cũ 70. Độ dài literal 3 → 2.</code> |
| <code>src/app/main.ts:108</code> | <code>Trình duyệt này không chạy được WebGL, nên Tuyến Cuối không chơi được ở đây.</code> | <code>This browser does not support WebGL. Last Line cannot run here.</code> | <code>Dòng cũ 108. Độ dài literal 76 → 63.</code> |
| <code>src/app/main.ts:179</code> | <code>TIẾP TẾ +</code> | <code>REPAIR +</code> | <code>Dòng cũ 179. Độ dài literal 9 → 8.</code> |
| <code>src/app/main.ts:179</code> | <code> GIÁP</code> | <code> HULL</code> | <code>Dòng cũ 179. Độ dài literal 5 → 5.</code> |
| <code>src/app/main.ts:189</code> | <code>TRỤ VỮNG!</code> | <code>LINE HELD!</code> | <code>Dòng cũ 189. Độ dài literal 9 → 10.</code> |
| <code>src/app/main.ts:189</code> | <code>TUYẾN ĐÃ VỠ</code> | <code>LINE LOST</code> | <code>Dòng cũ 189. Độ dài literal 11 → 9.</code> |
| <code>src/app/main.ts:189</code> | <code>VƯỢT ẢI!</code> | <code>CLEARED!</code> | <code>Dòng cũ 189. Độ dài literal 8 → 8.</code> |
| <code>src/app/main.ts:189</code> | <code>ẢI THẤT THỦ</code> | <code>STAGE LOST</code> | <code>Dòng cũ 189. Độ dài literal 11 → 10.</code> |
| <code>src/app/main.ts:220</code> | <code>Bật</code> | <code>On</code> | <code>Dòng cũ 220. Độ dài literal 3 → 2.</code> |
| <code>src/app/main.ts:220</code> | <code>Tắt</code> | <code>Off</code> | <code>Dòng cũ 220. Độ dài literal 3 → 3.</code> |
| <code>src/app/main.ts:222</code> | <code>Áp dụng từ trận sau</code> | <code>Applies next run</code> | <code>Dòng cũ 222. Độ dài literal 19 → 16.</code> |
| <code>src/app/main.ts:228</code> | <code>Hành trình</code> | <code>Campaign</code> | <code>Dòng cũ 228. Độ dài literal 10 → 8.</code> |
| <code>src/app/main.ts:228</code> | <code>Chương 1 · ải 1–</code> | <code>Chapter 1 · stages 1–</code> | <code>Dòng cũ 228. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:228</code> | <code> · chọn ải, nạp súng</code> | <code> · pick stage and guns</code> | <code>Dòng cũ 228. Độ dài literal 20 → 22.</code> |
| <code>src/app/main.ts:229</code> | <code>Trận thử lại</code> | <code>New trial</code> | <code>Dòng cũ 229. Độ dài literal 12 → 9.</code> |
| <code>src/app/main.ts:229</code> | <code>Trận thử</code> | <code>Trial</code> | <code>Dòng cũ 229. Độ dài literal 8 → 5.</code> |
| <code>src/app/main.ts:229</code> | <code>Bỏ </code> | <code>End </code> | <code>Dòng cũ 229. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:229</code> | <code>trận</code> | <code>run</code> | <code>Dòng cũ 229. Độ dài literal 4 → 3.</code> |
| <code>src/app/main.ts:229</code> | <code>Ải </code> | <code>Stage </code> | <code>Dòng cũ 229. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:229</code> | <code> đang dở, vào trận thử mới</code> | <code> to start a new trial</code> | <code>Dòng cũ 229. Độ dài literal 26 → 21.</code> |
| <code>src/app/main.ts:229</code> | <code>Pulse Gun và Heat Beam · giữ hành lang </code> | <code>Pulse Gun and Heat Beam · hold for </code> | <code>Dòng cũ 229. Độ dài literal 39 → 35.</code> |
| <code>src/app/main.ts:229</code> | <code> phút</code> | <code> min</code> | <code>Dòng cũ 229. Độ dài literal 5 → 4.</code> |
| <code>src/app/main.ts:230</code> | <code>Chơi tiếp</code> | <code>Resume</code> | <code>Dòng cũ 230. Độ dài literal 9 → 6.</code> |
| <code>src/app/main.ts:230</code> | <code>Về trận đang tạm dừng</code> | <code>Resume your paused run</code> | <code>Dòng cũ 230. Độ dài literal 21 → 22.</code> |
| <code>src/app/main.ts:230</code> | <code>Chưa có trận đang dở</code> | <code>No run to resume</code> | <code>Dòng cũ 230. Độ dài literal 20 → 16.</code> |
| <code>src/app/main.ts:231</code> | <code>Chế độ</code> | <code>Mode</code> | <code>Dòng cũ 231. Độ dài literal 6 → 4.</code> |
| <code>src/app/main.ts:232</code> | <code>Hồ sơ gõ</code> | <code>Profile</code> | <code>Dòng cũ 232. Độ dài literal 8 → 7.</code> |
| <code>src/app/main.ts:232</code> | <code>Tốc độ, độ chính xác, lời khuyên</code> | <code>Speed, accuracy, advice</code> | <code>Dòng cũ 232. Độ dài literal 32 → 23.</code> |
| <code>src/app/main.ts:233</code> | <code>Cài đặt</code> | <code>Options</code> | <code>Dòng cũ 233. Độ dài literal 7 → 7.</code> |
| <code>src/app/main.ts:233</code> | <code>Âm thanh, rung, nhịp, tàu, chất lượng hình</code> | <code>Audio, shake, pace, ship, graphics</code> | <code>Dòng cũ 233. Độ dài literal 42 → 34.</code> |
| <code>src/app/main.ts:234</code> | <code>Kho súng · Học từ</code> | <code>Armory · Learn</code> | <code>Dòng cũ 234. Độ dài literal 17 → 14.</code> |
| <code>src/app/main.ts:234</code> | <code>5 súng: băng đạn, tầm; cách học từ</code> | <code>5 guns: ammo, range; word learning</code> | <code>Dòng cũ 234. Độ dài literal 34 → 34.</code> |
| <code>src/app/main.ts:237</code> | <code>Đổi được khi chưa có trận dở (bỏ trận để đổi)</code> | <code>End your run to change this</code> | <code>Dòng cũ 237. Độ dài literal 45 → 27.</code> |
| <code>src/app/main.ts:239</code> | <code>Âm hiệu ứng</code> | <code>Effects</code> | <code>Dòng cũ 239. Độ dài literal 11 → 7.</code> |
| <code>src/app/main.ts:240</code> | <code>Nhạc</code> | <code>BGM</code> | <code>Dòng cũ 240. Đã rút gọn cho ô nhỏ. Độ dài literal 4 → 3.</code> |
| <code>src/app/main.ts:241</code> | <code>Rung màn hình</code> | <code>Screen shake</code> | <code>Dòng cũ 241. Độ dài literal 13 → 12.</code> |
| <code>src/app/main.ts:241</code> | <code>Đang tắt bởi ?shake=0</code> | <code>Off via ?shake=0</code> | <code>Dòng cũ 241. Độ dài literal 21 → 16.</code> |
| <code>src/app/main.ts:242</code> | <code>Giảm chuyển động</code> | <code>Reduce motion</code> | <code>Dòng cũ 242. Độ dài literal 16 → 13.</code> |
| <code>src/app/main.ts:242</code> | <code>Tàu không trôi, không lao; chữ không nảy</code> | <code>No ship drift or lunges; no letter bounce</code> | <code>Dòng cũ 242. Độ dài literal 40 → 41.</code> |
| <code>src/app/main.ts:243</code> | <code>Đọc từ tiếng Anh</code> | <code>Read words aloud</code> | <code>Dòng cũ 243. Độ dài literal 16 → 16.</code> |
| <code>src/app/main.ts:244</code> | <code>Nhịp tự điều theo cách bạn gõ</code> | <code>Adapt pace to your typing</code> | <code>Dòng cũ 244. Độ dài literal 29 → 25.</code> |
| <code>src/app/main.ts:244</code> | <code>Swarm dày thưa theo hồ sơ gõ của bạn</code> | <code>Swarm density follows your profile</code> | <code>Dòng cũ 244. Độ dài literal 36 → 34.</code> |
| <code>src/app/main.ts:244</code> | <code>Nhịp chuẩn cố định, không điều trong trận</code> | <code>Fixed pace throughout the run</code> | <code>Dòng cũ 244. Độ dài literal 41 → 29.</code> |
| <code>src/app/main.ts:245</code> | <code>Tàu</code> | <code>Rig</code> | <code>Dòng cũ 245. Đã rút gọn cho ô nhỏ. Độ dài literal 3 → 3.</code> |
| <code>src/app/main.ts:246</code> | <code>Chất lượng hình</code> | <code>Graphics</code> | <code>Dòng cũ 246. Độ dài literal 15 → 8.</code> |
| <code>src/app/main.ts:247</code> | <code>Xong</code> | <code>Done</code> | <code>Dòng cũ 247. Độ dài literal 4 → 4.</code> |
| <code>src/app/main.ts:252</code> | <code>Quay lại</code> | <code>Back</code> | <code>Dòng cũ 252. Độ dài literal 8 → 4.</code> |
| <code>src/app/main.ts:255</code> | <code>Chơi tiếp</code> | <code>Resume</code> | <code>Dòng cũ 255. Độ dài literal 9 → 6.</code> |
| <code>src/app/main.ts:256</code> | <code>Cài đặt</code> | <code>Options</code> | <code>Dòng cũ 256. Độ dài literal 7 → 7.</code> |
| <code>src/app/main.ts:256</code> | <code>Âm thanh, rung, đọc từ</code> | <code>Audio, shake, speech</code> | <code>Dòng cũ 256. Độ dài literal 22 → 20.</code> |
| <code>src/app/main.ts:257</code> | <code>Về màn chính</code> | <code>Main menu</code> | <code>Dòng cũ 257. Độ dài literal 12 → 9.</code> |
| <code>src/app/main.ts:257</code> | <code>Trận giữ nguyên, chơi tiếp được</code> | <code>Your run stays paused</code> | <code>Dòng cũ 257. Độ dài literal 31 → 21.</code> |
| <code>src/app/main.ts:262</code> | <code>Ải </code> | <code>Lv </code> | <code>Dòng cũ 262. Đã rút gọn cho ô nhỏ. Độ dài literal 3 → 3.</code> |
| <code>src/app/main.ts:263</code> | <code>Chơi lại</code> | <code>Retry</code> | <code>Dòng cũ 263. Độ dài literal 8 → 5.</code> |
| <code>src/app/main.ts:263</code> | <code>Chơi lại ải</code> | <code>Retry stage</code> | <code>Dòng cũ 263. Độ dài literal 11 → 11.</code> |
| <code>src/app/main.ts:264</code> | <code>Chọn ải</code> | <code>Stages</code> | <code>Dòng cũ 264. Độ dài literal 7 → 6.</code> |
| <code>src/app/main.ts:264</code> | <code>Hành trình</code> | <code>Campaign</code> | <code>Dòng cũ 264. Độ dài literal 10 → 8.</code> |
| <code>src/app/main.ts:265</code> | <code>Màn chính</code> | <code>Main menu</code> | <code>Dòng cũ 265. Độ dài literal 9 → 9.</code> |
| <code>src/app/main.ts:282</code> | <code>Bầy Hố Đen tràn ra từ mép hố đen. Gõ từ trên hai bến súng để nạp đạn; súng tự bắn. Gõ không lỗi thì đạn xuyên Vỏ và dễ chí mạng.</code> | <code>The Black Hole Horde pours in. Type words on two gun bays to reload; guns fire automatically. Flawless words pierce armor and boost critical hits.</code> | <code>Dòng cũ 282. Độ dài literal 128 → 146.</code> |
| <code>src/app/main.ts:283</code> | <code>TÀU </code> | <code>SHIP </code> | <code>Dòng cũ 283. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:283</code> | <code> · HÌNH </code> | <code> · GFX </code> | <code>Dòng cũ 283. Độ dài literal 8 → 7.</code> |
| <code>src/app/main.ts:288</code> | <code>Đổi tàu hoặc chất lượng hình thì trang tải lại khi bấm Xong.</code> | <code>Changing ships or graphics reloads the page when you press Done.</code> | <code>Dòng cũ 288. Độ dài literal 60 → 64.</code> |
| <code>src/app/main.ts:293</code> | <code>, tầm </code> | <code>, range </code> | <code>Dòng cũ 293. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:293</code> | <code>, từ có thể dài hơn 1 chữ</code> | <code>, words up to 1 letter longer</code> | <code>Dòng cũ 293. Độ dài literal 25 → 29.</code> |
| <code>src/app/main.ts:295</code> | <code>Gõ không lỗi: xuyên Vỏ (Vỏ chỉ chặn 75 %) và dễ chí mạng; ở Trận thử đòn mạnh thêm 6 %.</code> | <code>Flawless words face 75 % armor and boost critical hits; Trial hits gain 6 % damage.</code> | <code>Dòng cũ 295. Độ dài literal 87 → 83.</code> |
| <code>src/app/main.ts:296</code> | <code>Mỗi từ gõ xong được ghi vào sổ học chung của portal (mã typing-survival).</code> | <code>Every word you finish enters the portal&#x27;s shared learning log (typing-survival).</code> | <code>Dòng cũ 296. Độ dài literal 73 → 80.</code> |
| <code>src/app/main.ts:304</code> | <code>TRẬN THỬ</code> | <code>TRIAL</code> | <code>Dòng cũ 304. Độ dài literal 8 → 5.</code> |
| <code>src/app/main.ts:304</code> | <code>ẢI </code> | <code>STAGE </code> | <code>Dòng cũ 304. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:305</code> | <code>Giữ hành lang </code> | <code>Hold the lane for </code> | <code>Dòng cũ 305. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:305</code> | <code> phút</code> | <code> min</code> | <code>Dòng cũ 305. Độ dài literal 5 → 4.</code> |
| <code>src/app/main.ts:313</code> | <code>Ải </code> | <code>Stage </code> | <code>Dòng cũ 313. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:578</code> | <code>GIỮ TUYẾN!</code> | <code>HOLD THE LINE!</code> | <code>Dòng cũ 578. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:578</code> | <code>ẢI </code> | <code>STAGE </code> | <code>Dòng cũ 578. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/main.ts:635</code> | <code>Tắt bộ gõ tiếng Việt để gõ</code> | <code>Switch to an English keyboard</code> | <code>Dòng cũ 635. Độ dài literal 26 → 29.</code> |
| <code>src/app/main.ts:635</code> | <code>Từ dự phòng (máy chủ không có từ vựng)</code> | <code>Backup words (server vocabulary unavailable)</code> | <code>Dòng cũ 635. Độ dài literal 38 → 44.</code> |
| <code>src/app/main.ts:702</code> | <code>Tuyến Cuối</code> | <code>Last Line</code> | <code>Dòng cũ 702. Độ dài literal 10 → 9.</code> |
| <code>src/app/results.ts:19</code> | <code>Thời gian</code> | <code>Time</code> | <code>Dòng cũ 18. Độ dài literal 9 → 4.</code> |
| <code>src/app/results.ts:20</code> | <code>Hạ</code> | <code>KO</code> | <code>Dòng cũ 19. Đã rút gọn cho ô nhỏ. Độ dài literal 2 → 2.</code> |
| <code>src/app/results.ts:21</code> | <code>Chính xác</code> | <code>Accuracy</code> | <code>Dòng cũ 20. Độ dài literal 9 → 8.</code> |
| <code>src/app/results.ts:22</code> | <code>Từ đã gõ</code> | <code>Words</code> | <code>Dòng cũ 21. Độ dài literal 8 → 5.</code> |
| <code>src/app/results.ts:42</code> | <code>Hồ sơ gõ (trung bình các trận) nay là </code> | <code>Your profile now averages </code> | <code>Dòng cũ 41. Độ dài literal 38 → 26.</code> |
| <code>src/app/results.ts:42</code> | <code> WPM, chính xác </code> | <code> WPM, accuracy </code> | <code>Dòng cũ 41. Độ dài literal 16 → 15.</code> |
| <code>src/app/results.ts:43</code> | <code>Trận này ít từ quá, chưa tính vào hồ sơ gõ.</code> | <code>Too few words: no profile update this run.</code> | <code>Dòng cũ 42. Độ dài literal 43 → 42.</code> |
| <code>src/app/results.ts:44</code> | <code>Bạn rời bàn phím lâu, trận này không tính vào hồ sơ gõ.</code> | <code>Too much time away: this run did not count toward your profile.</code> | <code>Dòng cũ 43. Độ dài literal 55 → 63.</code> |
| <code>src/app/results.ts:45</code> | <code>Trận này lệch xa thường lệ, chưa tính vào hồ sơ gõ.</code> | <code>Unusual results: this run did not update your profile.</code> | <code>Dòng cũ 44. Độ dài literal 51 → 54.</code> |
| <code>src/app/results.ts:57</code> | <code>Chưa có số đo: chơi vài trận để có lời khuyên theo cách bạn gõ.</code> | <code>Play a few runs to get advice based on your typing.</code> | <code>Dòng cũ 56. Độ dài literal 63 → 51.</code> |
| <code>src/app/results.ts:58</code> | <code>Tuyến vỡ: nạp súng trước đỉnh tràn, và khi Swarm dày, gõ dứt điểm từng từ.</code> | <code>Line lost: reload before surges. Finish each word before switching when Swarm crowds in.</code> | <code>Dòng cũ 57. Độ dài literal 74 → 88.</code> |
| <code>src/app/results.ts:59</code> | <code>Trận đầu đã vào hồ sơ gõ: chơi thêm để có lời khuyên theo cách bạn gõ.</code> | <code>Your first run is in your profile. Play more for personal advice.</code> | <code>Dòng cũ 58. Độ dài literal 70 → 65.</code> |
| <code>src/app/results.ts:70</code> | <code>đo đủ</code> | <code>ready</code> | <code>Dòng cũ 69. Độ dài literal 5 → 5.</code> |
| <code>src/app/results.ts:70</code> | <code>đang đo </code> | <code>sampling </code> | <code>Dòng cũ 69. Độ dài literal 8 → 9.</code> |
| <code>src/app/results.ts:70</code> | <code>mặc định</code> | <code>default</code> | <code>Dòng cũ 69. Độ dài literal 8 → 7.</code> |
| <code>src/app/results.ts:73</code> | <code>Tốc độ (WPM)</code> | <code>Speed (WPM)</code> | <code>Dòng cũ 72. Độ dài literal 12 → 11.</code> |
| <code>src/app/results.ts:74</code> | <code>Chính xác</code> | <code>Accuracy</code> | <code>Dòng cũ 73. Độ dài literal 9 → 8.</code> |
| <code>src/app/results.ts:75</code> | <code>Nhận từ mới</code> | <code>Word delay</code> | <code>Dòng cũ 74. Đã rút gọn cho ô nhỏ. Độ dài literal 11 → 10.</code> |
| <code>src/app/results.ts:76</code> | <code>Độ đều</code> | <code>Rhythm</code> | <code>Dòng cũ 75. Độ dài literal 6 → 6.</code> |
| <code>src/app/results.ts:76</code> | <code>lệch ±</code> | <code>±</code> | <code>Dòng cũ 75. Độ dài literal 6 → 1.</code> |
| <code>src/app/results.ts:76</code> | <code> % mỗi từ</code> | <code> % / word</code> | <code>Dòng cũ 75. Độ dài literal 9 → 9.</code> |
| <code>src/app/results.ts:80</code> | <code>Đã chơi </code> | <code>Played </code> | <code>Dòng cũ 79. Độ dài literal 8 → 7.</code> |
| <code>src/app/results.ts:80</code> | <code> trận</code> | <code> runs</code> | <code>Dòng cũ 79. Độ dài literal 5 → 5.</code> |
| <code>src/app/results.ts:80</code> | <code>, chưa đủ số đo: đang dùng mặc định của chế độ</code> | <code>; still sampling: using mode defaults</code> | <code>Dòng cũ 79. Độ dài literal 46 → 37.</code> |
| <code>src/app/results.ts:80</code> | <code>Chưa có trận nào: hồ sơ đang dùng mặc định của chế độ </code> | <code>No runs yet: using defaults for </code> | <code>Dòng cũ 79. Độ dài literal 54 → 32.</code> |
| <code>src/app/results.ts:82</code> | <code>Trận tới: </code> | <code>Next run: </code> | <code>Dòng cũ 81. Độ dài literal 10 → 10.</code> |
| <code>src/app/results.ts:82</code> | <code>, nhịp ×</code> | <code>, pace ×</code> | <code>Dòng cũ 81. Độ dài literal 8 → 8.</code> |
| <code>src/app/results.ts:82</code> | <code>, từ </code> | <code>, words </code> | <code>Dòng cũ 81. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/results.ts:82</code> | <code> chữ, tự điều trong trận.</code> | <code> letters, adapting during play.</code> | <code>Dòng cũ 81. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/app/results.ts:82</code> | <code>Trận tới: </code> | <code>Next run: </code> | <code>Dòng cũ 82. Độ dài literal 10 → 10.</code> |
| <code>src/app/results.ts:83</code> | <code>, nhịp chuẩn cố định (đã tắt tự điều).</code> | <code>, fixed pace (adaptation off).</code> | <code>Dòng cũ 82. Độ dài literal 38 → 30.</code> |
| <code>src/app/skill.ts:161</code> | <code>Hai trận thắng dễ liền: thử chế độ </code> | <code>Two easy wins in a row: try </code> | <code>Dòng cũ 159. Độ dài literal 35 → 28.</code> |
| <code>src/app/skill.ts:163</code> | <code>Hai trận thua liền: chế độ </code> | <code>Two losses in a row: </code> | <code>Dòng cũ 161. Độ dài literal 27 → 21.</code> |
| <code>src/app/skill.ts:163</code> | <code> sẽ dễ thở hơn.</code> | <code> may feel easier.</code> | <code>Dòng cũ 161. Độ dài literal 15 → 17.</code> |
| <code>src/view/hud.ts:57</code> | <code>MỚI · BRUTE · (QUÁI LỰC LƯỠNG) VỎ </code> | <code>NEW · BRUTE · HEAVY FOE · ARMOR </code> | <code>Dòng cũ 57. Độ dài literal 34 → 32.</code> |
| <code>src/view/hud.ts:58</code> | <code>MỚI · PACK LEADER · (THỦ LĨNH BẦY) VỎ </code> | <code>NEW · PACK LEADER · ARMOR </code> | <code>Dòng cũ 58. Độ dài literal 38 → 26.</code> |
| <code>src/view/hud.ts:59</code> | <code>MỚI · SHIELD GUARD · (LÍNH MANG KHIÊN) CHẮN ĐẠN PHÍA TRƯỚC</code> | <code>NEW · SHIELD GUARD · BLOCKS FRONTAL SHOTS</code> | <code>Dòng cũ 59. Độ dài literal 58 → 41.</code> |
| <code>src/view/hud.ts:60</code> | <code>MỚI · SPLITTER · (QUÁI TÁCH MẢNH) VỠ 3 SHARD</code> | <code>NEW · SPLITTER · SPLITS INTO 3 SHARDS</code> | <code>Dòng cũ 60. Độ dài literal 44 → 37.</code> |
| <code>src/view/hud.ts:131</code> | <code>GIÁP</code> | <code>HULL</code> | <code>Dòng cũ 131. Độ dài literal 4 → 4.</code> |
| <code>src/view/hud.ts:139</code> | <code>còn lại</code> | <code>left</code> | <code>Dòng cũ 139. Độ dài literal 7 → 4.</code> |
| <code>src/view/hud.ts:144</code> | <code>hạ / 3 s</code> | <code>KO / 3 s</code> | <code>Dòng cũ 144. Độ dài literal 8 → 8.</code> |
| <code>src/view/hud.ts:269</code> | <code>ĐỈNH TRÀN </code> | <code>SURGE </code> | <code>Dòng cũ 269. Độ dài literal 10 → 6.</code> |
| <code>src/view/hud.ts:269</code> | <code> · DỮ DỘI</code> | <code> · FIERCE</code> | <code>Dòng cũ 269. Độ dài literal 9 → 9.</code> |
| <code>src/view/hud.ts:278</code> | <code>Tổng </code> | <code>Total </code> | <code>Dòng cũ 278. Độ dài literal 5 → 6.</code> |
| <code>src/view/hud.ts:360</code> | <code>SWARM RÚT LUI</code> | <code>SWARM RETREATS</code> | <code>Dòng cũ 360. Độ dài literal 13 → 14.</code> |
| <code>src/view/hud.ts:360</code> | <code> · LỌT </code> | <code> · PAST </code> | <code>Dòng cũ 360. Độ dài literal 7 → 8.</code> |
| <code>src/view/hud.ts:363</code> | <code>SWARM RÚT LUI!</code> | <code>SWARM RETREATS!</code> | <code>Dòng cũ 363. Độ dài literal 14 → 15.</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>quái Brute</code> | <code>Brute</code> | <code>Dòng cũ 17. Độ dài literal 10 → 5.</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>quái Pack Leader</code> | <code>Pack Leader</code> | <code>Dòng cũ 17. Độ dài literal 16 → 11.</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>quái Shield Guard</code> | <code>Shield Guard</code> | <code>Dòng cũ 17. Độ dài literal 17 → 12.</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>luật Săn</code> | <code>Hunt rule</code> | <code>Dòng cũ 17. Độ dài literal 8 → 9.</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>hiểm họa Rift</code> | <code>Rift hazard</code> | <code>Dòng cũ 17. Độ dài literal 13 → 11.</code> |
| <code>src/view/screens-journey.ts:17</code> | <code>luật Thiếu chữ</code> | <code>Gaps rule</code> | <code>Dòng cũ 17. Độ dài literal 14 → 9.</code> |
| <code>src/view/screens-journey.ts:21</code> | <code>(bầy quái) </code> | <code>(horde) </code> | <code>Dòng cũ 21. Độ dài literal 11 → 8.</code> |
| <code>src/view/screens-journey.ts:21</code> | <code> máu, đông</code> | <code> HP, many foes</code> | <code>Dòng cũ 21. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/view/screens-journey.ts:22</code> | <code>(lính trinh sát) đứng 6–9 m bắn tàu</code> | <code>(ranged) shoots the ship from 6–9 m</code> | <code>Dòng cũ 22. Độ dài literal 35 → 35.</code> |
| <code>src/view/screens-journey.ts:23</code> | <code>(quái lực lưỡng) Vỏ </code> | <code>(heavy) armor </code> | <code>Dòng cũ 23. Độ dài literal 20 → 14.</code> |
| <code>src/view/screens-journey.ts:23</code> | <code> máu, dẫn 5 Swarm</code> | <code> HP, leads 5 Swarm</code> | <code>Dòng cũ 23. Độ dài literal 17 → 18.</code> |
| <code>src/view/screens-journey.ts:24</code> | <code>(thủ lĩnh bầy) Vỏ </code> | <code>(leader) armor </code> | <code>Dòng cũ 24. Độ dài literal 18 → 15.</code> |
| <code>src/view/screens-journey.ts:24</code> | <code> máu, 8 Swarm hộ tống</code> | <code> HP, 8 Swarm escorts</code> | <code>Dòng cũ 24. Độ dài literal 21 → 20.</code> |
| <code>src/view/screens-journey.ts:25</code> | <code>(lính mang khiên) khiên </code> | <code>(guard) shield </code> | <code>Dòng cũ 25. Độ dài literal 24 → 15.</code> |
| <code>src/view/screens-journey.ts:25</code> | <code> chắn đạn từ phía trước</code> | <code> blocks frontal shots</code> | <code>Dòng cũ 25. Độ dài literal 23 → 21.</code> |
| <code>src/view/screens-journey.ts:26</code> | <code>(quái tách mảnh) vỡ thành 3 Shard</code> | <code>(splitter) breaks into 3 Shards</code> | <code>Dòng cũ 26. Độ dài literal 33 → 31.</code> |
| <code>src/view/screens-journey.ts:32</code> | <code>Giữ tuyến tới khi hết giờ. Hết giáp là thua.</code> | <code>Hold until time runs out. No hull means defeat.</code> | <code>Dòng cũ 32. Độ dài literal 44 → 47.</code> |
| <code>src/view/screens-journey.ts:33</code> | <code>Pack Leader tới ở giây </code> | <code>Pack Leaders arrive at </code> | <code>Dòng cũ 33. Độ dài literal 23 → 23.</code> |
| <code>src/view/screens-journey.ts:33</code> | <code> (tiếng tù và). Hạ </code> | <code> s (horn cue). Defeat </code> | <code>Dòng cũ 33. Độ dài literal 19 → 22.</code> |
| <code>src/view/screens-journey.ts:33</code> | <code> con thì Swarm rút lui; để lọt quá </code> | <code> to make Swarm retreat; let more than </code> | <code>Dòng cũ 33. Độ dài literal 35 → 38.</code> |
| <code>src/view/screens-journey.ts:33</code> | <code> con là thua.</code> | <code> pass and you lose.</code> | <code>Dòng cũ 33. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/view/screens-journey.ts:37</code> | <code>Không có hiểm họa.</code> | <code>No hazards.</code> | <code>Dòng cũ 37. Độ dài literal 18 → 11.</code> |
| <code>src/view/screens-journey.ts:38</code> | <code>Rift (vết nứt không gian): mỗi </code> | <code>Rift (space tear): every </code> | <code>Dòng cũ 38. Độ dài literal 31 → 25.</code> |
| <code>src/view/screens-journey.ts:38</code> | <code> s, tường trái hoặc phải sáng cam </code> | <code> s, the left or right wall glows orange for </code> | <code>Dòng cũ 38. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/view/screens-journey.ts:38</code> | <code> s trước khi đổ Swarm ra ở </code> | <code> s before Swarm emerges at </code> | <code>Dòng cũ 38. Độ dài literal 27 → 27.</code> |
| <code>src/view/screens-journey.ts:38</code> | <code> m. Giữ một súng gần có băng lúc sắp nứt.</code> | <code> m. Keep a close-range gun loaded before it opens.</code> | <code>Dòng cũ 38. Văn bản hướng dẫn/tiêu đề lớn; Claude kiểm chữ ở 1280 và 1920.</code> |
| <code>src/view/screens-journey.ts:42</code> | <code>Mỗi từ ẩn một chữ, từ có ít nhất bảy chữ ẩn hai. Chữ đầu luôn hiện. Nghĩa và phiên âm vẫn hiện. Gõ sai chữ ẩn sẽ hiện chữ đúng.</code> | <code>One letter is hidden; words of seven or more hide two. First letters, meanings and pronunciation stay visible. Wrong guesses reveal hidden letters.</code> | <code>Dòng cũ 42. Độ dài literal 127 → 147.</code> |
| <code>src/view/screens-journey.ts:43</code> | <code>Từ và nghĩa hiện trên bến. Từ đang gõ hiện lớn phía trên mũi tàu. Bến đang gõ hiện phiên âm và nghĩa. Gõ xong, từ và nghĩa hiện cùng dấu ✓.</code> | <code>Bays show words and meanings. Your active word sits large above the ship. Its bay shows pronunciation and meaning. Finish to see the word, meaning and ✓.</code> | <code>Dòng cũ 43. Độ dài literal 139 → 153.</code> |
| <code>src/view/screens-journey.ts:52</code> | <code>&lt;h1&gt;HÀNH TRÌNH&lt;/h1&gt;</code> | <code>&lt;h1&gt;CAMPAIGN&lt;/h1&gt;</code> | <code>Dòng cũ 52. Độ dài literal 10 → 8.</code> |
| <code>src/view/screens-journey.ts:53</code> | <code>&lt;div class=&quot;sv-title-en&quot;&gt;CHƯƠNG 1 · HÀNH LANG VC-7&lt;/div&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> | <code>&lt;div class=&quot;sv-title-en&quot;&gt;CHAPTER 1 · VC-7 CORRIDOR&lt;/div&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> | <code>Dòng cũ 53. Độ dài literal 25 → 25.</code> |
| <code>src/view/screens-journey.ts:55</code> | <code>&lt;p class=&quot;sv-note&quot;&gt;Mỗi ải có trang bị riêng: số bến, cấp Rèn, giáp. Ải sau mở khi qua ải trước.&lt;/p&gt;</code> | <code>&lt;p class=&quot;sv-note&quot;&gt;Each stage sets bays, Forge levels, and hull. Clear a stage to unlock the next.&lt;/p&gt;</code> | <code>Dòng cũ 55. Độ dài literal 76 → 79.</code> |
| <code>src/view/screens-journey.ts:56</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; chọn · &lt;kbd&gt;Enter&lt;/kbd&gt; xem ải · &lt;kbd&gt;Esc&lt;/kbd&gt; quay lại</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; select · &lt;kbd&gt;Enter&lt;/kbd&gt; brief · &lt;kbd&gt;Esc&lt;/kbd&gt; back</code> | <code>Dòng cũ 56. Độ dài literal 37 → 34.</code> |
| <code>src/view/screens-journey.ts:62</code> | <code>&lt;h1&gt;ẢI </code> | <code>&lt;h1&gt;STAGE </code> | <code>Dòng cũ 62. Văn bản hướng dẫn/tiêu đề lớn; Claude kiểm chữ ở 1280 và 1920.</code> |
| <code>src/view/screens-journey.ts:65</code> | <code>&lt;dt&gt;Mục tiêu&lt;/dt&gt;&lt;dd&gt;&lt;b&gt;</code> | <code>&lt;dt&gt;Goal&lt;/dt&gt;&lt;dd&gt;&lt;b&gt;</code> | <code>Dòng cũ 65. Độ dài literal 8 → 4.</code> |
| <code>src/view/screens-journey.ts:66</code> | <code>&lt;dt&gt;Hiểm họa&lt;/dt&gt;&lt;dd&gt;</code> | <code>&lt;dt&gt;Hazard&lt;/dt&gt;&lt;dd&gt;</code> | <code>Dòng cũ 66. Độ dài literal 8 → 6.</code> |
| <code>src/view/screens-journey.ts:67</code> | <code>&lt;dt&gt;Luật học&lt;/dt&gt;&lt;dd&gt;&lt;b&gt;</code> | <code>&lt;dt&gt;Learning&lt;/dt&gt;&lt;dd&gt;&lt;b&gt;</code> | <code>Dòng cũ 67. Độ dài literal 8 → 8.</code> |
| <code>src/view/screens-journey.ts:68</code> | <code>&lt;dt&gt;Trang bị&lt;/dt&gt;&lt;dd&gt;</code> | <code>&lt;dt&gt;Gear&lt;/dt&gt;&lt;dd&gt;</code> | <code>Dòng cũ 68. Độ dài literal 8 → 4.</code> |
| <code>src/view/screens-journey.ts:68</code> | <code> bến · Rèn </code> | <code> bays · Forge </code> | <code>Dòng cũ 68. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/view/screens-journey.ts:68</code> | <code> · giáp </code> | <code> · hull </code> | <code>Dòng cũ 68. Độ dài literal 8 → 8.</code> |
| <code>src/view/screens-journey.ts:71</code> | <code>&lt;em&gt;MỚI&lt;/em&gt;</code> | <code>&lt;em&gt;NEW&lt;/em&gt;</code> | <code>Dòng cũ 71. Độ dài literal 3 → 3.</code> |
| <code>src/view/screens-journey.ts:73</code> | <code>&lt;p class=&quot;sv-note&quot;&gt;Ải này dạy: </code> | <code>&lt;p class=&quot;sv-note&quot;&gt;This stage teaches: </code> | <code>Dòng cũ 73. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/view/screens-journey.ts:75</code> | <code>&lt;kbd&gt;Enter&lt;/kbd&gt; nạp súng · &lt;kbd&gt;Esc&lt;/kbd&gt; chọn ải</code> | <code>&lt;kbd&gt;Enter&lt;/kbd&gt; loadout · &lt;kbd&gt;Esc&lt;/kbd&gt; stages</code> | <code>Dòng cũ 75. Độ dài literal 28 → 26.</code> |
| <code>src/view/screens-journey.ts:84</code> | <code>&lt;h1&gt;NẠP SÚNG&lt;/h1&gt;</code> | <code>&lt;h1&gt;LOADOUT&lt;/h1&gt;</code> | <code>Dòng cũ 84. Độ dài literal 8 → 7.</code> |
| <code>src/view/screens-journey.ts:85</code> | <code>&lt;div class=&quot;sv-title-en&quot;&gt;ẢI </code> | <code>&lt;div class=&quot;sv-title-en&quot;&gt;STAGE </code> | <code>Dòng cũ 85. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/view/screens-journey.ts:85</code> | <code> · CHỌN </code> | <code> · PICK </code> | <code>Dòng cũ 85. Độ dài literal 8 → 8.</code> |
| <code>src/view/screens-journey.ts:92</code> | <code>&lt;em&gt;BẾN </code> | <code>&lt;em&gt;BAY </code> | <code>Dòng cũ 92. Độ dài literal 4 → 4.</code> |
| <code>src/view/screens-journey.ts:92</code> | <code> · RÈN </code> | <code> · FORGE </code> | <code>Dòng cũ 92. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/view/screens-journey.ts:94</code> | <code> · tầm </code> | <code> · range </code> | <code>Dòng cũ 94. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/view/screens-journey.ts:94</code> | <code> · từ dài tới +1 chữ</code> | <code> · words +1 letter</code> | <code>Dòng cũ 94. Độ dài literal 20 → 18.</code> |
| <code>src/view/screens-journey.ts:95</code> | <code>&lt;p class=&quot;sv-good&quot;&gt;khắc: </code> | <code>&lt;p class=&quot;sv-good&quot;&gt;vs: </code> | <code>Dòng cũ 95. Độ dài literal 6 → 4.</code> |
| <code>src/view/screens-journey.ts:96</code> | <code>&lt;p class=&quot;sv-poor&quot;&gt;kém: </code> | <code>&lt;p class=&quot;sv-poor&quot;&gt;bad: </code> | <code>Dòng cũ 96. Độ dài literal 5 → 5.</code> |
| <code>src/view/screens-journey.ts:101</code> | <code>&lt;div class=&quot;sv-threats&quot;&gt;&lt;b&gt;Ải này gặp gì · tỉ trọng&lt;/b&gt;</code> | <code>&lt;div class=&quot;sv-threats&quot;&gt;&lt;b&gt;Stage threats · share&lt;/b&gt;</code> | <code>Dòng cũ 101. Độ dài literal 24 → 21.</code> |
| <code>src/view/screens-journey.ts:106</code> | <code>BẮT ĐẦU</code> | <code>START</code> | <code>Dòng cũ 106. Độ dài literal 7 → 5.</code> |
| <code>src/view/screens-journey.ts:106</code> | <code> · CÒN ⚠</code> | <code> · GAPS ⚠</code> | <code>Dòng cũ 106. Độ dài literal 8 → 9.</code> |
| <code>src/view/screens-journey.ts:106</code> | <code>CHỌN THÊM </code> | <code>PICK </code> | <code>Dòng cũ 106. Độ dài literal 10 → 5.</code> |
| <code>src/view/screens-journey.ts:106</code> | <code> SÚNG</code> | <code> GUNS</code> | <code>Dòng cũ 106. Độ dài literal 5 → 5.</code> |
| <code>src/view/screens-journey.ts:108</code> | <code>&lt;kbd&gt;1&lt;/kbd&gt;–&lt;kbd&gt;5&lt;/kbd&gt; chọn hoặc bỏ · &lt;kbd&gt;←&lt;/kbd&gt;&lt;kbd&gt;→&lt;/kbd&gt; di chuyển · &lt;kbd&gt;Enter&lt;/kbd&gt; chọn · &lt;kbd&gt;Esc&lt;/kbd&gt; quay lại ải</code> | <code>&lt;kbd&gt;1&lt;/kbd&gt;–&lt;kbd&gt;5&lt;/kbd&gt; toggle · &lt;kbd&gt;←&lt;/kbd&gt;&lt;kbd&gt;→&lt;/kbd&gt; move · &lt;kbd&gt;Enter&lt;/kbd&gt; select · &lt;kbd&gt;Esc&lt;/kbd&gt; brief</code> | <code>Dòng cũ 108. Độ dài literal 62 → 47.</code> |
| <code>src/view/screens-journey.ts:119</code> | <code>Vượt ải</code> | <code>Clear</code> | <code>Dòng cũ 119. Độ dài literal 7 → 5.</code> |
| <code>src/view/screens-journey.ts:119</code> | <code>Giáp còn ≥ 50 %</code> | <code>Hull ≥ 50 %</code> | <code>Dòng cũ 119. Độ dài literal 15 → 11.</code> |
| <code>src/view/screens-journey.ts:119</code> | <code>Chính xác ≥ </code> | <code>Accuracy ≥ </code> | <code>Dòng cũ 119. Độ dài literal 12 → 11.</code> |
| <code>src/view/screens.ts:66</code> | <code>&lt;div class=&quot;sv-title-tag&quot;&gt;&lt;span class=&quot;sv-dot&quot;&gt;&lt;/span&gt;TRẠM VC-7 · VÀNH CHÂN TRỜI&lt;/div&gt;</code> | <code>&lt;div class=&quot;sv-title-tag&quot;&gt;&lt;span class=&quot;sv-dot&quot;&gt;&lt;/span&gt;STATION VC-7 · THE HORIZON&lt;/div&gt;</code> | <code>Dòng cũ 66. Độ dài literal 26 → 26.</code> |
| <code>src/view/screens.ts:67</code> | <code>&lt;h1 class=&quot;sv-title-name&quot;&gt;TUYẾN CUỐI&lt;/h1&gt;</code> | <code>&lt;h1 class=&quot;sv-title-name&quot;&gt;LAST LINE&lt;/h1&gt;</code> | <code>Dòng cũ 67. Độ dài literal 10 → 9.</code> |
| <code>src/view/screens.ts:68</code> | <code>&lt;div class=&quot;sv-title-en&quot;&gt;LAST LINE&lt;/div&gt;</code> | <code>&lt;div class=&quot;sv-title-en&quot;&gt;HOLD THE LINE&lt;/div&gt;</code> | <code>Dòng cũ 68. Văn bản hướng dẫn/tiêu đề lớn; Claude kiểm chữ ở 1280 và 1920.</code> |
| <code>src/view/screens.ts:73</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; chọn · &lt;kbd&gt;Enter&lt;/kbd&gt; vào · &lt;kbd&gt;Esc&lt;/kbd&gt; quay lại</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; select · &lt;kbd&gt;Enter&lt;/kbd&gt; play · &lt;kbd&gt;Esc&lt;/kbd&gt; back</code> | <code>Dòng cũ 73. Độ dài literal 34 → 33.</code> |
| <code>src/view/screens.ts:79</code> | <code>&lt;h1&gt;CÀI ĐẶT&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> | <code>&lt;h1&gt;OPTIONS&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> | <code>Dòng cũ 79. Độ dài literal 7 → 7.</code> |
| <code>src/view/screens.ts:82</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; chọn · &lt;kbd&gt;←&lt;/kbd&gt;&lt;kbd&gt;→&lt;/kbd&gt; đổi · &lt;kbd&gt;Esc&lt;/kbd&gt; xong</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; select · &lt;kbd&gt;←&lt;/kbd&gt;&lt;kbd&gt;→&lt;/kbd&gt; change · &lt;kbd&gt;Esc&lt;/kbd&gt; done</code> | <code>Dòng cũ 82. Độ dài literal 27 → 32.</code> |
| <code>src/view/screens.ts:88</code> | <code>&lt;h1&gt;KHO SÚNG · HỌC TỪ&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> | <code>&lt;h1&gt;ARMORY · LEARN&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> | <code>Dòng cũ 88. Độ dài literal 17 → 14.</code> |
| <code>src/view/screens.ts:94</code> | <code>&lt;kbd&gt;Enter&lt;/kbd&gt; hoặc &lt;kbd&gt;Esc&lt;/kbd&gt; quay lại</code> | <code>&lt;kbd&gt;Enter&lt;/kbd&gt; / &lt;kbd&gt;Esc&lt;/kbd&gt; back</code> | <code>Dòng cũ 94. Độ dài literal 23 → 16.</code> |
| <code>src/view/screens.ts:100</code> | <code>&lt;h1&gt;HỒ SƠ GÕ&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> | <code>&lt;h1&gt;TYPING PROFILE&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> | <code>Dòng cũ 100. Văn bản hướng dẫn/tiêu đề lớn; Claude kiểm chữ ở 1280 và 1920.</code> |
| <code>src/view/screens.ts:105</code> | <code>&lt;kbd&gt;Enter&lt;/kbd&gt; hoặc &lt;kbd&gt;Esc&lt;/kbd&gt; quay lại</code> | <code>&lt;kbd&gt;Enter&lt;/kbd&gt; / &lt;kbd&gt;Esc&lt;/kbd&gt; back</code> | <code>Dòng cũ 105. Độ dài literal 23 → 16.</code> |
| <code>src/view/screens.ts:111</code> | <code>&lt;h1&gt;TẠM DỪNG&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> | <code>&lt;h1&gt;PAUSED&lt;/h1&gt;&lt;div class=&quot;sv-hazard&quot; aria-hidden=&quot;true&quot;&gt;&lt;/div&gt;</code> | <code>Dòng cũ 111. Độ dài literal 8 → 6.</code> |
| <code>src/view/screens.ts:113</code> | <code>&lt;kbd&gt;Esc&lt;/kbd&gt; chơi tiếp · &lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; chọn · &lt;kbd&gt;Enter&lt;/kbd&gt; vào</code> | <code>&lt;kbd&gt;Esc&lt;/kbd&gt; resume · &lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; select · &lt;kbd&gt;Enter&lt;/kbd&gt; play</code> | <code>Dòng cũ 113. Độ dài literal 35 → 35.</code> |
| <code>src/view/screens.ts:122</code> | <code>NHẤN PHÍM BẤT KỲ ĐỂ VÀO TRẬN</code> | <code>PRESS ANY KEY TO PLAY</code> | <code>Dòng cũ 122. Độ dài literal 28 → 21.</code> |
| <code>src/view/screens.ts:122</code> | <code>ĐANG NẠP…</code> | <code>LOADING…</code> | <code>Dòng cũ 122. Độ dài literal 9 → 8.</code> |
| <code>src/view/screens.ts:123</code> | <code>Trong trận: &lt;kbd&gt;Esc&lt;/kbd&gt; tạm dừng</code> | <code>In play: &lt;kbd&gt;Esc&lt;/kbd&gt; pause</code> | <code>Dòng cũ 123. Độ dài literal 24 → 18.</code> |
| <code>src/view/screens.ts:129</code> | <code>VƯỢT ẢI!</code> | <code>CLEARED!</code> | <code>Dòng cũ 129. Độ dài literal 8 → 8.</code> |
| <code>src/view/screens.ts:129</code> | <code>ẢI THẤT THỦ</code> | <code>STAGE LOST</code> | <code>Dòng cũ 129. Độ dài literal 11 → 10.</code> |
| <code>src/view/screens.ts:129</code> | <code>TRỤ VỮNG!</code> | <code>LINE HELD!</code> | <code>Dòng cũ 129. Độ dài literal 9 → 10.</code> |
| <code>src/view/screens.ts:129</code> | <code>TUYẾN ĐÃ VỠ</code> | <code>LINE LOST</code> | <code>Dòng cũ 129. Độ dài literal 11 → 9.</code> |
| <code>src/view/screens.ts:136</code> | <code> từ gần nhất · và </code> | <code> latest words · </code> | <code>Dòng cũ 136. Độ dài literal 18 → 16.</code> |
| <code>src/view/screens.ts:136</code> | <code> từ khác đã vào sổ học&lt;/p&gt;</code> | <code> more in your learning log&lt;/p&gt;</code> | <code>Dòng cũ 136. Độ dài literal 22 → 26.</code> |
| <code>src/view/screens.ts:138</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; chọn · &lt;kbd&gt;Enter&lt;/kbd&gt; vào · &lt;kbd&gt;Esc&lt;/kbd&gt; màn chính</code> | <code>&lt;kbd&gt;↑&lt;/kbd&gt;&lt;kbd&gt;↓&lt;/kbd&gt; select · &lt;kbd&gt;Enter&lt;/kbd&gt; play · &lt;kbd&gt;Esc&lt;/kbd&gt; menu</code> | <code>Dòng cũ 138. Độ dài literal 35 → 33.</code> |
| <code>src/view/strip.ts:197</code> | <code>ĐẦY</code> | <code>MAX</code> | <code>Dòng cũ 197. Đã rút gọn cho ô nhỏ. Độ dài literal 3 → 3.</code> |
| <code>src/view/strip.ts:206</code> | <code>SẠCH ×</code> | <code>CLEAN ×</code> | <code>Dòng cũ 206. Đã rút gọn cho ô nhỏ. Độ dài literal 6 → 7.</code> |
| <code>src/content/balance.ts:28</code> | <code>Thư giãn</code> | <code>Relaxed</code> | <code>Dòng cũ 28. Độ dài literal 8 → 7.</code> |
| <code>src/content/balance.ts:28</code> | <code>Swarm thưa, đi chậm: gõ thong thả, học từ là chính</code> | <code>Sparse, slow Swarm: take your time and learn words</code> | <code>Dòng cũ 28. Độ dài literal 50 → 50.</code> |
| <code>src/content/balance.ts:29</code> | <code>Cân bằng</code> | <code>Balanced</code> | <code>Dòng cũ 29. Độ dài literal 8 → 8.</code> |
| <code>src/content/balance.ts:29</code> | <code>Căng vừa sức: lúc dồn, lúc thở</code> | <code>Fair pressure, room to breathe</code> | <code>Dòng cũ 29. Độ dài literal 30 → 30.</code> |
| <code>src/content/balance.ts:30</code> | <code>Thử thách</code> | <code>Challenge</code> | <code>Dòng cũ 30. Độ dài literal 9 → 9.</code> |
| <code>src/content/balance.ts:30</code> | <code>Swarm dày, đỉnh tràn gắt: giữ tuyến là kỳ công</code> | <code>Dense Swarm, fierce surges: hold the line</code> | <code>Dòng cũ 30. Độ dài literal 46 → 41.</code> |
| <code>src/content/chapter-1.ts:41</code> | <code>Ca trực đầu</code> | <code>First Shift</code> | <code>Dòng cũ 41. Độ dài literal 11 → 11.</code> |
| <code>src/content/chapter-1.ts:59</code> | <code>Săn Pack Leader</code> | <code>Hunt Pack Leader</code> | <code>Dòng cũ 59. Độ dài literal 15 → 16.</code> |
| <code>src/content/chapter-1.ts:76</code> | <code>Vách nứt</code> | <code>Rift Wall</code> | <code>Dòng cũ 76. Độ dài literal 8 → 9.</code> |
| <code>src/content/chapter-1.ts:93</code> | <code>Khiên sáng</code> | <code>Shield Glow</code> | <code>Dòng cũ 93. Độ dài literal 10 → 11.</code> |
| <code>src/content/guns.ts:130</code> | <code>pháo xung liên thanh</code> | <code>rapid pulse cannon</code> | <code>Dòng cũ 130. Độ dài literal 20 → 18.</code> |
| <code>src/content/guns.ts:130</code> | <code> viên trong 2,4 s vào con gần vạch nhất</code> | <code> rounds in 2.4 s at the foe nearest the line</code> | <code>Dòng cũ 130. Độ dài literal 39 → 44.</code> |
| <code>src/content/guns.ts:130</code> | <code>Trận thử: </code> | <code>Trial: </code> | <code>Dòng cũ 130. Độ dài literal 10 → 7.</code> |
| <code>src/content/guns.ts:130</code> | <code> viên</code> | <code> rounds</code> | <code>Dòng cũ 130. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/content/guns.ts:131</code> | <code>tia nhiệt quét</code> | <code>heat sweep</code> | <code>Dòng cũ 131. Độ dài literal 14 → 10.</code> |
| <code>src/content/guns.ts:131</code> | <code>tia 12 m cháy 2,5 s, quét về cụm dày</code> | <code>12 m beam, 2.5 s burn, sweeps groups</code> | <code>Dòng cũ 131. Độ dài literal 36 → 36.</code> |
| <code>src/content/guns.ts:132</code> | <code>súng chùm đẩy lùi</code> | <code>scatter knockback</code> | <code>Dòng cũ 132. Độ dài literal 17 → 17.</code> |
| <code>src/content/guns.ts:132</code> | <code>6 loạt × 7 viên xòe, đẩy lùi Swarm sát tàu</code> | <code>6 bursts × 7 pellets, repel close Swarm</code> | <code>Dòng cũ 132. Độ dài literal 42 → 39.</code> |
| <code>src/content/guns.ts:133</code> | <code>súng ray xuyên hàng</code> | <code>piercing rail gun</code> | <code>Dòng cũ 133. Độ dài literal 19 → 17.</code> |
| <code>src/content/guns.ts:133</code> | <code>3 phát xuyên 6 con, phá khiên</code> | <code>3 shots pierce 6, break shields</code> | <code>Dòng cũ 133. Độ dài literal 29 → 31.</code> |
| <code>src/content/guns.ts:134</code> | <code>pháo cối nổ vùng</code> | <code>blast mortar</code> | <code>Dòng cũ 134. Độ dài literal 16 → 12.</code> |
| <code>src/content/guns.ts:134</code> | <code>4 quả nổ 2,5 m vào cụm nặng</code> | <code>4 blasts, 2.5 m vs heavy groups</code> | <code>Dòng cũ 134. Độ dài literal 27 → 31.</code> |
| <code>src/content/guns.ts:148</code> | <code>Swarm giữa sân</code> | <code>Swarm mid-lane</code> | <code>Dòng cũ 148. Độ dài literal 14 → 14.</code> |
| <code>src/content/guns.ts:149</code> | <code>Swarm sát vạch</code> | <code>Swarm at line</code> | <code>Dòng cũ 149. Độ dài literal 14 → 13.</code> |
| <code>src/content/guns.ts:150</code> | <code>Scout và đạn Scout</code> | <code>Scout and shots</code> | <code>Dòng cũ 150. Độ dài literal 18 → 15.</code> |
| <code>src/content/guns.ts:151</code> | <code>Brute, Pack Leader (Vỏ)</code> | <code>Brute, Pack Leader (armor)</code> | <code>Dòng cũ 151. Độ dài literal 23 → 26.</code> |
| <code>src/content/guns.ts:152</code> | <code>Shield Guard và toán sau khiên</code> | <code>Shield Guard and cover</code> | <code>Dòng cũ 152. Độ dài literal 30 → 22.</code> |
| <code>src/content/guns.ts:153</code> | <code>Splitter và Shard</code> | <code>Splitter and Shard</code> | <code>Dòng cũ 153. Độ dài literal 17 → 18.</code> |
| <code>src/content/stage-rules.ts:62</code> | <code>Trụ vững</code> | <code>Hold out</code> | <code>Dòng cũ 62. Độ dài literal 8 → 8.</code> |
| <code>src/content/stage-rules.ts:62</code> | <code>Săn Pack Leader</code> | <code>Hunt Pack Leader</code> | <code>Dòng cũ 62. Độ dài literal 15 → 16.</code> |
| <code>src/content/stage-rules.ts:74</code> | <code>Chuẩn</code> | <code>Normal</code> | <code>Dòng cũ 74. Độ dài literal 5 → 6.</code> |
| <code>src/content/stage-rules.ts:75</code> | <code>Thiếu chữ</code> | <code>Gaps</code> | <code>Dòng cũ 75. Độ dài literal 9 → 4.</code> |
| <code>src/content/stage-s0.ts:56</code> | <code>Trận thử</code> | <code>Trial</code> | <code>Dòng cũ 56. Độ dài literal 8 → 5.</code> |
| <code>index.html:2</code> | <code>lang=&quot;vi&quot;</code> | <code>lang=&quot;en&quot;</code> | <code>Dòng cũ 2. Độ dài literal 9 → 9.</code> |
| <code>index.html:10</code> | <code>&lt;title&gt;Tuyến Cuối&lt;/title&gt;</code> | <code>&lt;title&gt;Last Line&lt;/title&gt;</code> | <code>Dòng cũ 10. Độ dài literal 10 → 9.</code> |
| <code>index.html:13</code> | <code>aria-label=&quot;Hành lang Tuyến Cuối&quot;</code> | <code>aria-label=&quot;Last Line corridor&quot;</code> | <code>Dòng cũ 13. Độ dài literal 33 → 31.</code> |
| <code>index.html:14</code> | <code>TUYẾN CUỐI · đang tải…</code> | <code>LAST LINE · loading…</code> | <code>Dòng cũ 14. Độ dài literal 22 → 20.</code> |
| <code>src/app/english.ts:5</code> | <code>Tay bạn đang chậm dần: nghỉ vài phút rồi chơi tiếp nhé.</code> | <code>Your hands are slowing down. Take a few minutes to rest.</code> | <code>Bản dịch cục bộ; giữ nguyên id và cách kit chọn lời khuyên. Nguồn cũ: src/kit/balance/pace.ts:110. Độ dài literal 55 → 56.</code> |
| <code>src/app/english.ts:6</code> | <code>Bạn gõ nhanh nhưng hay sai: chậm lại một nhịp sẽ được Hoàn hảo nhiều hơn.</code> | <code>You type fast but make mistakes. Slow down for more perfect words.</code> | <code>Bản dịch cục bộ; giữ nguyên id và cách kit chọn lời khuyên. Nguồn cũ: src/kit/balance/pace.ts:111. Độ dài literal 73 → 66.</code> |
| <code>src/app/english.ts:7</code> | <code>Gõ chắc từng chữ trước, tốc độ sẽ tự lên.</code> | <code>Focus on each letter first. Speed will follow.</code> | <code>Bản dịch cục bộ; giữ nguyên id và cách kit chọn lời khuyên. Nguồn cũ: src/kit/balance/pace.ts:112. Độ dài literal 41 → 46.</code> |
| <code>src/app/english.ts:8</code> | <code>Nhịp gõ chưa đều: giữ một tốc độ vừa phải cho mọi từ.</code> | <code>Keep a steady, comfortable pace for every word.</code> | <code>Bản dịch cục bộ; giữ nguyên id và cách kit chọn lời khuyên. Nguồn cũ: src/kit/balance/pace.ts:113. Độ dài literal 53 → 47.</code> |
| <code>src/app/english.ts:9</code> | <code>Từ mới còn lạ: đọc nghĩa và nghe phát âm trước khi gõ.</code> | <code>Read new words&#x27; meanings and listen before typing.</code> | <code>Bản dịch cục bộ; giữ nguyên id và cách kit chọn lời khuyên. Nguồn cũ: src/kit/balance/pace.ts:114. Độ dài literal 54 → 50.</code> |
| <code>src/app/english.ts:10</code> | <code>Khi đông quái, chọn một từ và gõ dứt điểm rồi mới sang từ khác.</code> | <code>When foes crowd in, finish one word before switching.</code> | <code>Bản dịch cục bộ; giữ nguyên id và cách kit chọn lời khuyên. Nguồn cũ: src/kit/balance/pace.ts:115. Độ dài literal 63 → 53.</code> |
| <code>src/app/english.ts:11</code> | <code>Bạn đang tiến bộ đều. Giữ phong độ!</code> | <code>You are making steady progress. Keep it up!</code> | <code>Bản dịch cục bộ; giữ nguyên id và cách kit chọn lời khuyên. Nguồn cũ: src/kit/balance/pace.ts:116. Mảnh ghép/câu: kiểm độ dài cả trường, không tính riêng đoạn này; xem lengths.json.</code> |
| <code>src/view/gun-rules.ts:16</code> | <code>HOÀN HẢO</code> | <code>PERFECT</code> | <code>Ghi đè riêng nhãn hiển thị trong FEEL; không sửa kit. Nguồn cũ: src/kit/feedback/profiles.ts:51. Dòng cũ 15. Độ dài literal 8 → 7.</code> |
| <code>tests/small-labels.test.ts:21</code> | <code>const detail = /&lt;dt&gt;Luật học&lt;\/dt&gt;&lt;dd&gt;&lt;b&gt;[^&lt;]+&lt;\/b&gt; · ([\s\S]*?)&lt;\/dd&gt;/.exec(html)![1]!;</code> | <code>const detail = /&lt;dt&gt;Learning&lt;\/dt&gt;&lt;dd&gt;&lt;b&gt;[^&lt;]+&lt;\/b&gt; · ([\s\S]*?)&lt;\/dd&gt;/.exec(html)![1]!;</code> | <code>Test so chuỗi cũ; chỉ đổi nhãn/fixture/regex tương ứng.</code> |
| <code>tests/small-labels.test.ts:25</code> | <code>expect(detail).toContain(&quot;phiên âm&quot;);</code> | <code>expect(detail).toContain(&quot;pronunciation&quot;);</code> | <code>Test so chuỗi cũ; chỉ đổi nhãn/fixture/regex tương ứng.</code> |
| <code>tests/small-labels.test.ts:33</code> | <code>expect(renderJourney(screen)).toContain(&quot;Ải 2 · Săn Pack Leader&quot;);</code> | <code>expect(renderJourney(screen)).toContain(&quot;Stage 2 · Hunt Pack Leader&quot;);</code> | <code>Test so chuỗi cũ; chỉ đổi nhãn/fixture/regex tương ứng.</code> |
| <code>tests/small-labels.test.ts:35</code> | <code>expect(renderJourney(screen)).toContain(&quot;ẢI 2 · SĂN PACK LEADER&quot;);</code> | <code>expect(renderJourney(screen)).toContain(&quot;STAGE 2 · HUNT PACK LEADER&quot;);</code> | <code>Test so chuỗi cũ; chỉ đổi nhãn/fixture/regex tương ứng.</code> |
| <code>tests/small-labels.test.ts:37</code> | <code>kind: &quot;end&quot;, menu: new Menu([]), mode: &quot;Cân bằng&quot;, won: true,</code> | <code>kind: &quot;end&quot;, menu: new Menu([]), mode: &quot;Balanced&quot;, won: true,</code> | <code>Test so chuỗi cũ; chỉ đổi nhãn/fixture/regex tương ứng.</code> |
| <code>tests/small-labels.test.ts:38</code> | <code>stats: [], words: [], advice: &quot;&quot;, note: &quot;&quot;, stage: &quot;Ải 2 · &quot; + stage.name,</code> | <code>stats: [], words: [], advice: &quot;&quot;, note: &quot;&quot;, stage: &quot;Stage 2 · &quot; + stage.name,</code> | <code>Test so chuỗi cũ; chỉ đổi nhãn/fixture/regex tương ứng.</code> |
| <code>tests/small-labels.test.ts:39</code> | <code>})).toContain(&quot;ẢI 2 · SĂN PACK LEADER · CÂN BẰNG&quot;);</code> | <code>})).toContain(&quot;STAGE 2 · HUNT PACK LEADER · BALANCED&quot;);</code> | <code>Test so chuỗi cũ; chỉ đổi nhãn/fixture/regex tương ứng.</code> |
| <code>tests/theme.test.ts:49</code> | <code>expect(visible).toContain(&quot;TUYẾN CUỐI&quot;);</code> | <code>expect(visible).toContain(&quot;LAST LINE&quot;);</code> | <code>Test so chuỗi cũ; chỉ đổi nhãn/fixture/regex tương ứng.</code> |
