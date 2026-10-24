# 06 — Solo, tổ đội, bot và online cho chế độ Tu tiên giữ ải thú triều

> **Ngày:** 24/10/2026 · **Mảng:** solo, đội 2–3 người, Thất Tinh 7 ghế (mở rộng), bot bù ghế, đồng bộ online trên Cloudflare gói Free.
> **Trạng thái:** đề xuất để chủ dự án duyệt. Mọi con số ghi "thử" là số thử, chưa có dữ liệu chơi thật.
> **Ký hiệu nguồn:** [video] = bản quay QCBH của chủ dự án; [Codex §n] = `TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md`; [web: …] = đã tra; [trí nhớ] = chưa xác minh; [repo: …] = mã/tài liệu trong dự án.

## 1. Tóm tắt

- **Thứ tự làm:** Độc tu + bot (MVP) → Phân thân bạn đạo (đồng hành bất đồng bộ, rẻ) → Lưỡng Nghi 2 người realtime trong phòng bạn bè → Tam Tài 3 người + ghép nhanh → Thất Tinh 7 ghế là sự kiện (1–3 người thật, còn lại bot hoặc phân thân).
- **Ghế trận là vai, không phải tọa độ:** mỗi ghế có vai (Công, Hộ, Trận, Ngự thú), một trận nhãn và một hướng thú tràn tới. Ghế luôn đủ nhờ bot. Bot chạy trong sim tất định nên không tốn băng thông.
- **Công bằng giữa người gõ nhanh và chậm:** mỗi ghế có nhịp k riêng theo hồ sơ của người ngồi ghế đó (công thức `paceK` ở BALANCE.md §4.1). Người gõ nhanh nhận hướng đông hơn và việc phụ tùy chọn; người chậm không bị kéo theo nhịp người nhanh. Thưởng tính theo thời gian có mặt và kết quả học của chính người đó, không theo damage hay đòn kết liễu.
- **Kỹ thuật:** máy chủ không chạy sim thú triều. Mọi máy chạy cùng một sim tất định (số nguyên, 60 Hz, có mã băm như `games/dragon-hold/src/sim`). Một Durable Object (DO) làm trạm chuyển lệnh: đóng dấu tick rồi phát lại, không dùng timer. Ước tính khoảng 200 request DO cho một trận 12 phút 3 người, tức trần lý thuyết khoảng 500 trận/ngày trên gói Free. Nếu để máy chủ chạy sim bằng alarm 20 Hz thì chỉ được khoảng 7 trận/ngày.
- **Tách quyền:** thế giới chung (thú, ải, trận, bot) là sim tất định. Vị trí, máu và đồ nhặt của **chính mình** do máy mình giữ. Ở MVP, thú nhắm ải và trận nhãn, không đuổi theo người. Loot cá nhân tính cục bộ theo seed nên không cần đồng bộ loot.
- **Rớt mạng hoặc AFK:** sau 10 s (thử), bot giữ ghế. Khi người chơi quay lại, quyền điều khiển trả ở biên hành động. Máu boss không co giãn. Rời phòng bạn bè không bị phạt.
- **Học:** mỗi người một bộ từ riêng, không bao giờ hai người tranh một từ, mỗi người tối đa một từ khẩn tại một thời điểm. Trong đợt, liên lạc bằng "truyền âm nhanh" (câu tiếng Anh có sẵn, bấm phím chức năng hoặc chuột), không gõ chat tự do vì sẽ chiếm ô nhập.

## 2. QCBH làm thế nào (chỉ phần liên quan)

| Quan sát | Nguồn | Bài học cho ta |
|---|---|---|
| QCBH là game một người; bản Switch ghi 1 người chơi | [web: [Wikipedia](https://en.wikipedia.org/wiki/Tale_of_Immortal), [Nintendo](https://nintendo.co.uk/Games/Nintendo-Switch-download-software/Tale-of-Immortal-2509020.html)] | Không có mẫu co-op để học. Phần đội và online là thiết kế riêng của dự án |
| Combat realtime nhìn từ trên xuống, đi tự do, đánh bầy quái, có bộ đếm hạ quái và minimap dạng đồ thị phòng (nút đỏ là boss) | [video 1:40–3:20, t148, t180] | Combat nền một người đã đủ hay. Ta thay đồ thị phòng bằng chuỗi đợt thú triều quanh một ải |
| Một sinh vật nhỏ đi theo nhân vật trong trận | [video t148, t180] | Pet đi theo chủ, không chiếm ghế (Codex §14.1 giữ đúng) |
| Nút "Trốn" (Esc) ở góc trái dưới, cả khi đánh boss | [video t180, boss_12] | Solo được rút lui. Trong đội, "rút" là nhường ghế cho bot, không bỏ đồng đội giữa đợt |
| Đồ rơi trên đất có nhãn tên; cuộn "Chiến đấu kết thúc / Thu hoạch được đạo cụ" sau boss | [video t180, t256] | Kết toán từng trận. Ta dùng loot cá nhân, thu gom sau đợt (Codex §1.7) |
| Lớp phủ của người stream "Counting death: 1" | [video] | Đây là bộ đếm riêng của người stream, chưa đủ để suy ra luật chết. Ta không dùng chết vĩnh viễn |
| Tông môn có đại trận; công tông môn khác do tông chủ phát động; phá trận cần trưởng lão và đệ tử hợp lực đánh thần thú tông môn | [web: tóm tắt kết quả tìm kiếm của [thảo luận Steam](https://steamcommunity.com/app/1468810/discussions/0/3118172724621705341); chưa mở được trang] | Ý "nhiều người cùng giữ một đại trận" khớp ghế trận. Ở QCBH đó là NPC; ở ta là người hoặc bot |
| Quan hệ NPC: đạo lữ, kết bái, sư đồ; NPC có thể giúp hoặc hại người chơi | [trí nhớ] | Phân thân bạn đạo (mục 4.7) là bản "người thật" của ý đồng hành, không cần mô phỏng NPC |
| Sự kiện "thú triều" riêng trong QCBH | [web: tìm "鬼谷八荒 兽潮" ngày 24/10, không ra kết quả] | Không dựa vào. Vòng thú triều là thiết kế riêng |

Kết luận: phần đáng học là **đồng hành giúp người chơi một mình không lẻ loi** và **đại trận cần nhiều vị trí**. Tên, UI, sự kiện và cách chơi online đều tự thiết kế.

## 3. Codex V2.2 nói gì về mảng này: giữ, sửa, bỏ

| Nội dung Codex | Quyết định | Lý do |
|---|---|---|
| Ba hình thức: solo thuần, một người + bot, nhiều người + bot bù [§14.1] | **Giữ** | Đúng yêu cầu. Bot cũng giúp thử cân bằng trước khi có mạng |
| Bot lấp ghế trước trận hoặc ở checkpoint, không sinh thêm giữa đợt [§14.1, §15] | **Giữ, thêm** | Thêm: người mới chỉ vào thay ghế bot ở nghỉ giữa đợt (mục 4.8) |
| Bảng trận 2/3/4/5/7 vị trí [§14.2] | **Sửa** | Chỉ làm Độc tu (1), Lưỡng Nghi (2), Tam Tài (3); Thất Tinh (7) làm sự kiện. **Bỏ** Tứ Tượng và Ngũ Hành: mỗi cỡ đội cần cân bằng và nội dung riêng, trong khi lượng người chơi ít |
| Trận nhãn là quyền đảm nhiệm, không khóa tọa độ; ra ngoài không làm sập trận [§14.3] | **Giữ** | Khớp với đi lại tự do [§1.6] |
| HP cá nhân và một hộ trận chung [§14.3] | **Giữ, nói rõ** | Hộ trận chung là Trận khí của ải. Thua khi ải vỡ, không phải khi cả đội gục |
| Hợp trận bất đồng bộ, nhãn chậm chỉ làm tích chậm [§14.4] | **Giữ** | Đây là nền của công bằng tốc độ |
| Không dùng người nhanh nhất để tăng áp lực cả đội [§14.4] | **Giữ, cụ thể hóa** | Dùng nhịp k theo ghế và hướng riêng (mục 4.3) |
| Luật bot: không biết trước, không có túi loot, không tạo mastery; mất kết nối thì bot thay; đổi quyền ở biên hành động [§15] | **Giữ, thêm số** | Chờ 10 s (thử). Duel PvP dùng 30 s [repo: `src/duel/authority.ts` `reconnectGraceMs`], nhưng co-op để bot thay sớm thì ít hại hơn |
| "Người rớt mạng được bot thay không làm HP boss co giãn" [§15] | **Giữ, thêm** | Thêm luật nhịp k của ghế chuyển dần sang nhịp bot trong 10 s, chỉ áp cho thú sinh sau (mục 4.5) |
| Loot cá nhân, không giành đồ [§1.7, RV33] | **Giữ, đơn giản hóa** | Loot quay riêng theo seed từng người, tính tại máy. Không cần đồng bộ |
| Không một người dừng cả server; đội có pha kế hoạch chung riêng [§6.3, RV12] | **Giữ** | Đội không pause. "Tạm nghỉ" là giao ghế cho bot |
| Lập chiêu co-op [§6.3], điều quân nhiều tuyến cho đội [§7] | **Bỏ khỏi co-op MVP** | Đồng bộ đồng hồ phức tạp, dễ quá tải. Để sau khi solo đã chứng minh được |
| Tự Cường / Đồng Tu [§12.2] | **Giữ** | Độc tu dùng Tự Cường; ghế Hộ và Trận trong đội dùng Đồng Tu |
| Credit đóng góp support, tránh last-hit [§22.3] | **Giữ cho màn kết**, **không gắn vào thưởng** | Thưởng theo có mặt cho đơn giản và khó lạm dụng (mục 4.4) |
| Lộ trình P4 Tam Tài với bot trước P6 co-op người thật [§27] | **Giữ thứ tự, sửa nội dung P6** | P6 không đồng bộ loot, không đưa vị trí vào sim ở MVP (mục 4.6) |
| "Chưa có netcode" [§15 dòng cuối] | **Bổ sung** | Mục 4.6 đề xuất kiến trúc và ngân sách gói Free |
| Chưa nói về voice chat, chat gõ chữ trong đội | **Bổ sung** | Mục 6: truyền âm nhanh, push-to-talk khi dùng Voice |

## 4. Đề xuất hệ thống cho game giữ ải thú triều

### 4.1 Ghế, vai và trận (dữ liệu)

```ts
type Role = "cong" | "ho" | "tran" | "ngu_thu";
type FormationId = "doc_tu" | "luong_nghi" | "tam_tai" | "that_tinh";
type Seat = {
  id: number;                 // 0..6
  role: Role;
  sector: SectorId;           // hướng thú tràn mà ghế này chịu chính
  node: Vec2i;                // trận nhãn: điểm cố định gần cổng ải
  controller:
    | { kind: "human"; playerId: string; inputMode: "typing" | "voice" | "hybrid" }
    | { kind: "bot"; preset: BotId; avatar?: AvatarSnapshot };   // BotId của kit
  kPermille: number;          // nhịp k của ghế, 750..1300
};
type Formation = { id: FormationId; seats: Seat[]; charge: number[]; gateQi: number };
```

| Vai | Việc chính trong đợt | Ô liên tục (luôn có từ để gõ) | Giá trị khi gõ chậm |
|---|---|---|---|
| **Công** | Dọn bầy, phá giáp tinh anh, giữ hướng của mình | Đòn chính | Thấp nhất: hợp người gõ nhanh |
| **Hộ** | Khiên cổng và đồng đội, khiêu khích kéo thú về điểm mình, giải trạng thái, cứu người gục | Hộ khí (nạp khiên) | Cao: cần đúng lúc hơn cần nhanh |
| **Trận** | Nạp trận nhãn, đặt và chuyển cơ quan, làm chậm, kích Hợp trận | Nạp nhãn | Cao: tích lũy theo từ đúng, không theo tốc độ tức thời |
| **Ngự thú** | Lệnh pet giữ một hướng hoặc tập kích tinh anh | Hiệu lệnh | Vừa: pet tự đánh khi chưa có lệnh |

- Độc tu có 1 ghế, ải có 1–2 hướng, trận nhãn tự nạp chậm. Người chơi có thể thêm 1–2 bot "đạo đồng" để thành Lưỡng Nghi hoặc Tam Tài.
- Lưỡng Nghi: Công + (Hộ hoặc Trận hoặc Ngự thú). Tam Tài: Công + Hộ + (Trận hoặc Ngự thú). Một lớp nhân vật đáp ứng 1–2 vai theo deck [Codex §14.2].
- **Hợp trận:** khi mọi trận nhãn đủ nạp, ghế Trận (hoặc bot) kích một đòn quét các hướng. Nhãn chậm làm tích chậm, không hủy [Codex §14.4]. Bot nạp theo nhịp của bot.

### 4.2 Vòng chơi một trận (12–15 phút, thử)

1. **Vào ghế:** chọn trận, chọn vai, bot lấp ghế trống. Khóa cỡ trận, phiên bản nội dung, seed và nhịp k từng ghế.
2. **Đợt 1–8:** mỗi đợt 60–90 s. Thú tràn theo hướng. Người chơi đi tự do, gõ, nói hoặc dùng Hybrid để tung chiêu.
3. **Nghỉ giữa đợt 25 s:** thu gom loot cá nhân, mua nhanh 1 món, đổi một ô chiêu, ôn 3 từ (tùy chọn). Có kiểm sẵn sàng; im lặng tính là sẵn sàng. Đây là lúc lưu checkpoint và lúc người mới vào thay ghế bot.
4. **Thú vương (boss) ở đợt cuối:** có đòn báo trước, cửa sổ phá thế, mỗi người một ấn riêng.
5. **Kết toán:** đợt đã giữ, loot cá nhân, từ đã học, và đóng góp theo vai (chỉ để xem).

### 4.3 Co giãn theo ghế: công bằng tốc độ

- `k_ghế = clamp(C(E_eff)/C_ref; 0,75; 1,30)`, lấy từ hồ sơ năng lực của người ngồi ghế đó (BALANCE.md §4.1; bot dùng preset của bot). Kênh Voice dùng hồ sơ đo riêng của kênh Voice.
- **Thú thường** của hướng nào thì sinh theo `k` của ghế đó. **Thú chung** (tinh anh, boss) theo trung bình `k` các ghế.
- Thú lọt khỏi hướng của mình sẽ đi vào sân trong trước cổng. Đồng đội nào rảnh có thể giúp; đây là chỗ phối hợp tự nhiên.
- Khoảng 0,75–1,30 không bù hết chênh lệch giữa 25 WPM và 70 WPM. Phần dư của người nhanh đi vào **Truy kích** tùy chọn: săn tinh anh ngoài trận để lấy thêm loot cá nhân, có rủi ro, không ảnh hưởng áp lực cả đội.
- Bộ điều nhịp (PaceDirector) chạy riêng cho từng ghế trong sim, cùng trần như BALANCE §4.2. Nó không đổi máu thú đang sống.
- Không có bảng DPS. Màn kết hiện mỗi người một mục mạnh nhất theo Codex §22.3.

### 4.4 Thưởng và loot cá nhân

- **Loot:** mỗi thú chết rơi đồ riêng cho **mỗi** người đang có mặt. Lượt quay dùng `hash(matchSeed, playerId, beastId)` qua `RngStream` của kit, nên máy nào cũng tính ra cùng kết quả mà không cần gửi qua mạng. Ai hạ thú không quan trọng. Đồ thường tự hút trong bán kính gần và được thu gom ở nghỉ giữa đợt. Bot không có loot [Codex §15].
- **Thưởng đợt (thử):** `Thưởng_i = Gốc(bậc ải) × Σ_đợt(qua_đợt × cómặt_i)`. `cómặt` lấy 0, 0,5 hoặc 1 theo phần thời gian trong đợt người đó còn kết nối và không AFK.
- **Ngộ (thưởng học):** tính từ từ của chính người đó: đúng, từ mới, từ đến hạn ôn. Không phụ thuộc đồng đội.
- **Đồng tu:** người thật trong đội có thêm +10 % thưởng đợt (thử), trần theo ngày. Không có vật liệu cốt lõi chỉ đội mới lấy được [Codex §15].
- **Kiểm phía máy chủ** (khi có tài khoản): DO ký **biên nhận trận** gồm matchId, ghế, số đợt đã qua (theo mã băm đa số) và thời gian có mặt từng người. Worker ví chỉ cộng thưởng trong trần ngày, dùng lại logic `WALLET_PHASE 3` [repo: `games/space-typing/cloud/src/wallet.ts`].

### 4.5 Thất bại, AFK, rớt mạng

| Tình huống | Luật (số thử) |
|---|---|
| Máu cá nhân về 0 | **Gục** (gửi sự kiện `DOWNED` có dấu tick, trận nhãn ngừng nạp). Đồng đội hoặc bot đứng trong 3 m và hoàn thành **một từ bất kỳ** là cứu. Không ai cứu thì tự dậy tại trận nhãn sau 15 s. Không chết vĩnh viễn |
| Trận khí ải về 0 | **Ải thất thủ.** Giữ 100 % thưởng các đợt đã qua. Cả đội bỏ phiếu "thủ lại đợt" từ checkpoint trong 20 s; im lặng tính là đồng ý; bot luôn đồng ý |
| Rớt mạng | Giữ ghế 10 s, avatar đứng yên. Sau đó DO phát `SEAT_CONTROL → bot`, bot đứng đúng vị trí cuối. `k` của ghế chuyển dần sang `k` bot trong 10 s, chỉ cho thú sinh sau |
| Quay lại | Nhận checkpoint đợt và nhật ký lệnh, tua nhanh, rồi lấy lại ghế ở biên hành động. Một nhân vật không bao giờ nhận lệnh từ cả người lẫn bot cùng lúc [Codex §15] |
| AFK có kết nối | 45 s không có hành động hợp lệ khi đợt đang có nguy cơ: nhắc. 75 s: bot hỗ trợ ghế cho tới khi người gõ lại. Thời gian AFK không tính `cómặt` |
| Muốn nghỉ | Solo: pause. Đội: nút "Tạm nghỉ" giao ghế cho bot, bấm lại để lấy về |
| Rời trận | Phòng bạn bè: không phạt. Ghép nhanh: rời 3 trận liên tiếp trong ngày thì chờ 5 phút mới ghép lại được |
| Lệch sim (desync) | Mã băm khác đa số: tải ảnh chụp từ máy khác. Lệch 3 lần: ghế đó sang bot, người đó vào lại ở đợt sau |
| DO khởi động lại | Mọi máy vẫn giữ trạng thái. DO mới lấy checkpoint đợt gần nhất (mã băm khớp đa số) và trận chơi lại từ đầu đợt đó |

### 4.6 Kiến trúc online

**Đề xuất: sim tất định ở mọi máy, DO làm trạm chuyển lệnh, tách quyền "thế giới chung / bản thân".**

| Ai giữ | Gồm |
|---|---|
| **Sim tất định chung** (mọi máy chạy y hệt) | Thú, đường đi, máu thú, Trận khí ải, trận nhãn, Hợp trận, bot (gồm vị trí và quyết định của bot, RNG riêng), pet, thú vương, đòn báo trước, và loot (quay theo người nhưng tất định) |
| **Máy của chính người chơi** | Vị trí và di chuyển của mình, máu của mình (né đòn báo trên đất, nhận sát thương vùng của thú ở gần), nhặt đồ của mình |
| **DO `TideRoom`** | Xác thực, chia ghế, seed, T0, đóng dấu tick lúc nhận lệnh, phát lại, giữ nhật ký lệnh của đợt hiện tại trong RAM, lưu 1 dòng mỗi đợt, so mã băm, quyết định bot thay ghế, ký biên nhận |

- **Ràng buộc thiết kế để tách quyền dùng được:** thú chỉ nhắm cổng, trận nhãn, bot và điểm khiêu khích. Điểm khiêu khích là một lệnh tung chiêu nên nằm trong sim. Thú không đổi đường vì vị trí người thật. Đòn báo của boss đặt theo trận nhãn hoặc hướng, không bám theo người. Người chơi vẫn đi tự do để vào tầm, né, vào vùng trận, nhặt đồ và cứu đồng đội. Solo dùng **cùng luật** để nội dung làm một lần chạy được cả hai chế độ.
- **Lệnh tung chiêu mang điểm xuất phát.** `CAST{seat, seq, slot, actionId, wordId, target, origin}`. Sim dùng `origin` để tính tầm, vùng trận và hướng chiêu. DO kiểm `origin` hợp lý so với vị trí báo gần nhất (tốc độ tối đa × thời gian + dư), sai thì từ chối.
- **Độ trễ:** sim mọi máy chạy chậm hơn đồng hồ phòng B = 150 ms (9 tick, thử). Chiêu của mình bắt đầu hoạt ảnh ngay (đây chỉ là phần trình bày); đòn trúng khi sim tới tick đã đóng dấu, khoảng 200 ms sau khi gõ xong. Bản thân mình đi ngay, không trễ, nên không gây cảm giác cứng. Solo B = 0.
- **Lệnh tới muộn** (mạng giật quá B): tua lại từ ảnh chụp, mỗi 30 tick chụp một lần, giữ 8 ảnh. Nếu muộn quá 4 s thì xin ảnh chụp từ máy khác.
- **Vị trí của đồng đội:** `MOVE_HINT{pos, dest|dir}` chỉ để hiển thị, không vào sim. Gửi khi đổi ý định và 1 Hz khi đang đi; máy khác nội suy 100–200 ms.
- **Không gửi từng phím.** Duel gửi `TYPE_CHAR` từng ký tự [repo: `src/duel/protocol.ts`]; co-op chỉ gửi lệnh khi đã hoàn thành từ. Thống kê học ghi ở máy như solo.
- **Kiểm đồng bộ:** gửi mã băm FNV-1a của thế giới mỗi 300 tick (5 s) [repo: `games/dragon-hold/src/sim/hash.ts`]. HELLO mang phiên bản giao thức và mã băm nội dung; khác bản thì không vào phòng.
- **Bảo mật** như Duel D-FINAL-13 và §50.1: WSS, token phiên trong HELLO, Origin allowlist, giới hạn cỡ và tần suất tin, heartbeat, reconnectToken, bỏ `seq` cũ hoặc trùng.

**Ngân sách gói Free** (một trận 12 phút, 3 người thật; mỗi người khoảng 0,4 lệnh chiêu/s + 1 MOVE_HINT/s + 0,2 mã băm/s + 0,2 ping/s ≈ 1,8 tin/s):

| Phương án | Request DO/trận | Duration | Trận/ngày (trần) | Băng thông xuống/máy | Ghi chú |
|---|---:|---|---:|---|---|
| **A. Trạm chuyển lệnh, Hibernation, không timer (đề xuất)** | ≈ 3.900 tin ÷ 20 ≈ **200** | Chỉ khi xử lý tin; rảnh thì không tính | **≈ 500** | ≈ 0,5–1 KB/s | Rủi ro gian lận "máu của mình" (mục 8) |
| B. DO chạy sim, alarm 20 Hz | 14.400 alarm + 200 ≈ 14.600 | Thức cả trận | **≈ 7** | 300 thú × ~9 B × 10 Hz ≈ 27 KB/s | Alarm tính như request: không dùng được |
| C. DO chạy sim, setInterval | ≈ 200 | 720 s × 0,125 GB = 90 GB-s | **≈ 144** (13.000 GB-s ÷ 90) | ≈ 27 KB/s | Chống gian tốt nhất nhưng chạm trần duration sớm |

- Giới hạn DO gói Free: 100.000 request/ngày; tin WebSocket gửi lên tính theo tỉ lệ 20:1; tin gửi xuống không tính phí; 13.000 GB-s/ngày, tính 128 MB cho mỗi object; object rảnh và có thể ngủ (hibernation) thì không bị tính duration; alarm tính là request; CPU mỗi lần gọi 30 s; 1.000 request/s mỗi object; chỉ hỗ trợ dạng SQLite; 100.000 dòng ghi/ngày [web: [DO pricing](https://developers.cloudflare.com/durable-objects/platform/pricing/), [DO limits](https://developers.cloudflare.com/durable-objects/platform/limits/)].
- **Hạn mức chia chung cả tài khoản Cloudflare** với chat và API của Space Typing [repo: `games/space-typing/docs/ONLINE_CLOUDFLARE_DEPLOY.md` §3.1, §6]. Đề xuất dành tối đa 50 % request DO cho co-op, khoảng 250 trận/ngày. Khi đạt 80 % mức đó, phòng mới tự chuyển sang "chơi cùng bot" và báo rõ cho người chơi.
- Không ghi SQLite theo từng lệnh (100.000 dòng ghi/ngày). Chỉ ghi 1 dòng mỗi đợt và 1 dòng mỗi phòng.
- Cần đo bằng Dashboard (Durable Objects → Metrics) trước khi mở ghép nhanh. Câu "rảnh thì không tính duration" lấy theo tài liệu giá, chưa đo với dự án.

### 4.7 Đồng hành bất đồng bộ: Phân thân bạn đạo

- Người chơi xuất **mã phân thân** gồm: lớp nhân vật, vai, deck, pet, chỉ số và hồ sơ gõ (E, a, CV, thời gian nhận từ, lấy từ `SkillProfile`). Bạn nhập mã đó và mang phân thân vào một ghế bot. Phân thân chạy bằng `HumanTypist` với tham số của chủ mã.
- **Kẹp sức mạnh** theo ngân sách của bậc ải: tối đa 1,1 × mức khuyến nghị. Vì vậy mã bị sửa tay cũng không phá được ải, và chưa cần máy chủ.
- Khi có tài khoản: danh sách phân thân của bạn bè và nhóm đọc từ D1. Chủ phân thân nhận "Hộ đạo điểm" mỗi lần được mượn, tối đa 5 lần/ngày (thử).
- Phân thân không tạo sự kiện học và không nhận loot.

### 4.8 Ghép trận

- **Phòng bạn bè trước:** mã phòng 6 ký tự; mời qua danh sách bạn và nhóm nếu dùng tài khoản Space [repo: `cloud/src/social.ts`]. Không cần hàng đợi công khai.
- **Ghép nhanh sau:** một DO `TideLobby` (Hibernation) xếp hàng theo bậc ải, dải từ vựng và cỡ trận (2 hoặc 3). **Không ghép theo WPM**, vì nhịp k theo ghế đã lo phần đó. Chờ 25 s mà chưa đủ người thì vào luôn với bot.
- **Nhảy vào giữa trận:** người ghép muộn vào thay ghế bot ở nghỉ giữa đợt. Nhờ đó khi ít người online, không ai phải ngồi chờ.
- DO được tạo gần nơi có request đầu tiên; người chơi Việt Nam nhiều khả năng vào máy ở Singapore hoặc Hồng Kông [trí nhớ, cần đo RTT].

### 4.9 MVP và sau MVP

| Mốc | Nội dung | Điều kiện qua |
|---|---|---|
| **M1 (MVP) Độc tu + bot** | Sim tất định sẵn sàng cho lockstep; ghế, vai, Hợp trận; bot đạo đồng; loot cá nhân theo seed; gục và cứu; rút lui; checkpoint đợt; mã băm | Cổng B1–B9 với đội bot hỗn hợp; mã băm khớp qua 20 seed |
| M2 Phân thân bạn đạo | Mã phân thân, kẹp sức mạnh; danh sách bạn nếu có tài khoản | Phân thân không vượt 1,1 × ngân sách; không tạo sự kiện học |
| M3 Lưỡng Nghi realtime | `TideRoom`, giao thức, lớp mạng ở client, tua lại, đồng bộ lại, bot thay ghế, phòng bạn bè | Cổng N1–N5 (mục 7) |
| M4 Tam Tài + ghép nhanh | 3 ghế người, `TideLobby`, nhảy vào giữa trận, chặn khi gần hết hạn mức | Hàng đợi có trần chờ 25 s; DO ≤ 250 request/trận |
| M5 Thất Tinh (sự kiện tuần) | 7 ghế, 1–3 người thật, còn lại bot hoặc phân thân; một ải đặc biệt | Màn hình không quá tải (Codex §26.9); FPS đạt với 7 ghế |
| Sau nữa | Đại trận cộng đồng bất đồng bộ (các trận solo góp Trấn khí cho nhóm), bảng xếp hạng theo cỡ đội và preset với bộ điều nhịp tắt, cho thú đuổi người (đưa di chuyển vào sim) | Có dữ liệu cho thấy cần |

**Bỏ hoặc hoãn:** 7 người thật ghép công khai, Tứ Tượng và Ngũ Hành, lập chiêu co-op, điều quân co-op, chat gõ tự do trong đợt, PvP.

## 5. Solo và đội: khác biệt và luật công bằng

| | Độc tu | Độc tu + bot | Đội 2–3 người | Thất Tinh |
|---|---|---|---|---|
| Ghế | 1 | 2–3 | 2–3 (bot bù) | 7 |
| Pause | Có | Có | Không ("Tạm nghỉ" giao ghế cho bot) | Không |
| Trận | Tiểu trận tự nạp | Đủ nhãn, bot nạp | Đủ nhãn | Đại trận, hợp kích theo pha |
| Nhịp | k của mình | k mình + preset bot | k theo từng ghế | k theo từng ghế |
| Trễ mạng B | 0 | 0 | 150 ms | 150 ms |
| Thưởng | 100 % | 100 % | 100 % + 10 % đồng tu | Thưởng sự kiện |
| Bảng điểm (sau này) | Riêng | Riêng | Riêng theo cỡ đội | Riêng |

**Luật công bằng:**

1. **Tốc độ gõ:** k theo ghế; không ai chịu nhịp của người khác; người nhanh có Truy kích tùy chọn. Cổng kiểm: trong đội hỗn hợp (bot Mới 25 + Nhanh 70 + Chuẩn 35), P, I, O của **từng ghế** nằm trong dải Cân bằng của BALANCE §3. Tỉ lệ thắng của đội lệch tối đa ±5 điểm % so với đội toàn bot Chuẩn.
2. **Typing và Voice:** cùng cooldown, cùng damage [Codex §1.4]. Kênh Voice có hồ sơ C riêng (gồm độ trễ chốt ASR), nên k của ghế Voice phản ánh đúng sức của kênh. Timer đòn báo tính theo kênh của từng người [Codex §16.1].
3. **Không tranh từ:** mỗi người một bộ từ riêng; từ trên ô chỉ người đó thấy; mục tiêu thuộc về người đang khóa (học từ Duel D-FINAL-04).
4. **Không tranh đồ:** loot cá nhân, nên chạy nhanh không giành được của ai.
5. **Không cộng dồn hỗ trợ:** aura và buff theo ID và bucket [Codex §12.5, §23.1]. Đội 3 ghế Hộ không bất tử.
6. **Đổi cỡ đội không lén đổi chỉ số:** ngân sách trận bằng tổng năng lực các ghế. Một người + 2 bot và 3 người có cùng cấu trúc. Rớt mạng không co giãn máu boss.
7. **Bot không gánh hộ:** sức mạnh bot cố định theo bậc ải (preset Chuẩn), không tăng theo người chơi. Bot giữ vai, không tự giành phần kết liễu.

**Bất đồng bộ hay realtime:**

| | Phân thân (bất đồng bộ) | Realtime |
|---|---|---|
| Cảm giác đội | Vừa: có "bạn" trong trận nhưng không trò chuyện | Cao |
| Chi phí máy chủ | ≈ 0 (mã) hoặc vài lần đọc D1 | DO, ≈ 200 request/trận |
| Rủi ro | Thấp | Lệch sim, mạng giật, rớt mạng |
| Công sức | S–M | L |
| Phụ thuộc lượng người chơi | Không | Có |

## 6. Gắn với học tiếng Anh (Typing, Voice, Hybrid)

- **Từ nào ở đâu:**
  - Ô chiêu lấy từ bài học của chính người đó (deck của kit).
  - Ô liên tục (Nạp nhãn, Hộ khí, Đòn chính) ưu tiên **từ đang ôn**, ngắn, đã quen, để giữ nhịp.
  - Ấn phá thế của thú vương và ấn Hợp trận dùng **từ đến hạn ôn**.
  - Từ mới chỉ ra lúc đầu đợt và ở nghỉ giữa đợt, không ra trong lúc boss đang báo đòn. Tỉ lệ từ mới theo hồ sơ từng người (BALANCE §4.1).
- **Tránh quá tải:**
  - Mỗi người tối đa 1 từ khẩn tại một thời điểm.
  - Sự kiện đội chia cho mỗi người **một** ấn riêng trong cửa sổ 6–8 s (thử), không cần gõ cùng lúc [Codex §14.4].
  - Cứu đồng đội dùng từ bất kỳ đang có, không thêm ô mới.
  - Từ của đồng đội ẩn mặc định; người chơi chỉ thấy biểu tượng chiêu và hiệu ứng.
- **Truyền âm nhanh:** 6 câu tiếng Anh có sẵn ("Hold the gate!", "Need a shield!", "On my way!", "Elite left!", "Ready!", "Thank you!"), gọi bằng F1–F6 hoặc bánh xe chuột giữa. Đây là thêm một lần gặp tiếng Anh có ngữ cảnh. Không mở chat gõ tự do trong đợt, để chữ cái luôn thuộc về bài học [Codex §1.2]. Ở nghỉ giữa đợt thì mở chat được.
- **Voice trong đội:**
  - Gợi ý push-to-talk (giữ một phím) khi chơi đội, vì tiếng nói chuyện với bạn sẽ bị ASR nhận thành câu trả lời.
  - Khi đang trong cuộc gọi, gợi ý chuyển sang Hybrid hoặc Typing.
  - Không phát TTS từ của đồng đội.
  - Kết quả ASR chỉ chốt một lần theo ID hành động [Codex §1.4].
- **Chỉ người thật tạo sự kiện học.** Bot, phân thân và pet không tạo sự kiện học [Codex §15, §22.2]. Thống kê học ghi qua `learning/bridge` như khi chơi solo.
- **Tu luyện chọn chữ** (Minh, chữ thường, Tâm ma) là hoạt động solo ngoài trận, vì phụ thuộc nhịp riêng từng người. Không đưa vào co-op ở MVP.

## 7. Tái sử dụng và chi phí sản xuất

| Dùng lại | Đường dẫn | Dùng cho |
|---|---|---|
| Sim số nguyên 60 Hz, luật ranh giới, mã băm | `games/dragon-hold/src/sim/fixed.ts`, `sim/hash.ts`, `games/dragon-hold/AGENTS.md` (không trig, không `Math.random`) | Sim sẵn sàng cho lockstep ngay từ M1 |
| RNG có seed, trạng thái băm được | `shared/game-kit/platform/rng.ts` | Loot theo người, miền RNG riêng của bot |
| Bot gõ như người, hồ sơ năng lực, nhịp k, bộ điều nhịp, FlowMeter, cổng | `shared/game-kit/balance/{typist,profile,pace,director,flow,gates}.ts`; `docs/games/BALANCE.md` §4, §6, §7 | Bot ghế, phân thân, k theo ghế, cổng công bằng |
| Định tuyến từ, phiên gõ, deck | `shared/game-kit/typing/{router,session,decks}.ts` | Bộ từ riêng từng người, không trùng tiền tố |
| Voice | `shared/game-kit/speech/speech.ts`; skill `voice-typing-runtime` | Hồ sơ kênh Voice, chốt một lần |
| Cầu nối học | `shared/game-kit/learning/{bridge,events}.ts` | Chỉ người thật phát sự kiện học |
| DO có Hibernation, kiểm Origin | `games/space-typing/cloud/src/chat.ts`, `cloud/wrangler.jsonc` | Mẫu cho `TideRoom` và `TideLobby` |
| Giao thức Duel: HELLO/WELCOME, phiên bản, reconnectToken, `seq`, trần 4.096 B, `SET_BOT` | `games/space-typing/src/duel/protocol.ts` | Khung tin nhắn co-op (gửi lệnh chiêu thay vì từng phím) |
| Phiên, chờ kết nối lại, heartbeat | `games/space-typing/src/duel/authority.ts` (`reconnectGraceMs`), `server/duel/ws-server.ts` (HELLO 5 s, heartbeat 10/20 s) | Logic phiên. **Lưu ý:** Duel online hiện là server Node, chưa chuyển sang DO (`ONLINE_CLOUDFLARE_DEPLOY.md` §1), nên chỉ dùng lại mẫu, không có hạ tầng sẵn |
| Bot dùng chung đường lệnh, không gian lận | Duel master plan D-FINAL-16, §43.1; `src/duel/bots.ts` | Nguyên tắc bot ghế |
| Bạn bè, nhóm, ví máy chủ | `games/space-typing/cloud/src/{social,wallet}.ts` | Mời phòng, biên nhận thưởng (khi có tài khoản) |

| Hạng mục | Cỡ |
|---|---|
| Ghế, vai, Hợp trận trong sim + AI bot ghế (HumanTypist + ưu tiên theo vai) | M |
| Độc tu + bot: gục và cứu, rút lui, checkpoint đợt | M |
| Loot cá nhân theo seed | S |
| Mã phân thân (xuất, nhập, kẹp) | S |
| Phân thân qua tài khoản + Hộ đạo điểm | M |
| `TideRoom` + giao thức + lớp mạng client + tua lại + đồng bộ lại + bot thay ghế | **L** |
| Bộ kiểm nhiều máy headless (trễ, jitter, mất gói, thử lệch sim) | M |
| `TideLobby` ghép nhanh + nhảy vào giữa trận + chặn hạn mức | M |
| Truyền âm nhanh | S |
| Thất Tinh: phần mạng / phần nội dung | S / M–L |

**Cổng kiểm mạng (thử):**
- N1: 2–3 máy headless, cùng seed và cùng lệnh, cho mã băm khớp 100 % qua 20 seed × 15 phút.
- N2: trễ 150 ± 50 ms, mất 2 % gói: không lệch sim; tua lại p95 < 5 ms.
- N3: rớt mạng 30 s thì bot thay trong 10 s; quay lại bắt kịp ≤ 3 s.
- N4: ≤ 250 request DO cho một trận 3 người 12 phút.
- N5: đội hỗn hợp tốc độ đạt luật 1 ở mục 5.

## 8. Rủi ro và câu hỏi cho chủ dự án

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Lệch sim giữa trình duyệt (số thực, thứ tự duyệt) | Cao | Luật sim số nguyên của dragon-hold, test ranh giới, mã băm 5 s, cổng N1 trước khi mở online |
| Ít người online nên hàng đợi trống | Cao | Phòng bạn bè trước; ghép nhanh chờ tối đa 25 s rồi chơi với bot; nhảy vào giữa trận |
| Hạn mức Free dùng chung với Space | Vừa | Không timer, không ghi theo lệnh, chặn ở 80 % hạn mức, đo Dashboard |
| Tự khai máu và vị trí của mình nên có thể bật bất tử | Vừa | Chỉ ảnh hưởng người gian lận trong PvE; kiểm `origin`; thưởng có trần ngày và biên nhận DO; không có PvP |
| Máy yếu không chạy nổi sim hàng trăm thú cho cả đội | Vừa | Trần thực thể sim; một thực thể "cụm bầy" vẽ thành 5–10 con (đông là nhờ phần hình); bench như dragon-hold |
| Chênh tốc độ làm người chậm thấy vô dụng | Vừa | k theo ghế; vai Hộ và Trận hợp người chậm; không có bảng DPS |
| Voice chat làm ASR nhận sai | Vừa | Push-to-talk, gợi ý Hybrid hoặc Typing |
| Thất Tinh phình phạm vi | Vừa | Chỉ làm sự kiện, tối đa 3 người thật |

**Câu hỏi (kèm phương án đề xuất):**

1. **Sau solo, làm co-op bất đồng bộ hay realtime trước?** Đề xuất: Phân thân bạn đạo (M2) trước, rồi Lưỡng Nghi realtime (M3). Phân thân rẻ, có cảm giác đội sớm, và kiểm vai và thưởng trước khi viết lớp mạng.
2. **Tối đa bao nhiêu người thật trong một trận?** Đề xuất: 3. Thất Tinh 7 ghế là sự kiện có 1–3 người thật, còn lại bot hoặc phân thân.
3. **Tài khoản: dùng chung tài khoản Space Typing hay để lưu cục bộ?** Đề xuất: co-op dùng mã phòng và danh tính khách, tiến trình lưu cục bộ như các game đã tách. Nối tài khoản khi portal có tài khoản chung. Worker co-op riêng (`tu-tien-coop`) để không đụng API Space; WebSocket gửi token trong HELLO như Duel, không dựa vào cookie.
4. **Thú có đuổi theo người không?** Đề xuất: MVP **không**. Thú nhắm cổng, trận nhãn, bot và điểm khiêu khích. Nhờ vậy vị trí người không phải vào sim, rẻ và mượt. Chỉ đưa di chuyển vào lockstep nếu playtest cho thấy thiếu cảm giác bị săn.
5. **Đội có được thưởng nhiều hơn solo không?** Đề xuất: +10 % đồng tu có trần ngày, không có vật liệu chỉ đội mới có.
6. **Mở ghép nhanh công khai ngay khi ra co-op?** Đề xuất: chưa. Chỉ phòng bạn bè. Mở ghép nhanh khi giờ cao điểm có khoảng ≥ 20 người cùng online (thử).
7. **Có chết vĩnh viễn hoặc mất đồ khi thua như cảm giác nặng của QCBH?** Đề xuất: không. Dùng gục và cứu; thất thủ vẫn giữ thưởng các đợt đã qua; độ căng đến từ đợt và boss.
8. **Cho phép một đội trộn Typing, Voice và Hybrid?** Đề xuất: có. Mỗi người chọn kênh riêng; k theo kênh; gợi ý push-to-talk.
9. **Bảng xếp hạng co-op?** Đề xuất: chưa làm ở MVP. Sau này xếp theo số đợt giữ được, tách theo cỡ đội, kênh và preset, bộ điều nhịp tắt (BALANCE §1.6).
