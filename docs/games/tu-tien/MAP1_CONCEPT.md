# Thanh Thạch Ải — ý tưởng map 1 theo camera thật (v1.0, 01/11/2026)

> **Vai:** ý tưởng viết trước khi vẽ, theo bài học §2 của [`../LESSONS_FROM_THREE_GAMES.md`](../LESSONS_FROM_THREE_GAMES.md). Gửi ChatGPT duyệt và vẽ đè (Chat mode, thinking High) bằng [`MAP1_CHATGPT_MESSAGE.md`](MAP1_CHATGPT_MESSAGE.md); anh đính kèm hai ảnh nền. Bản duyệt của ChatGPT ghi vào `MAP1_CHATGPT_REVIEW.md`, rồi ý tưởng lên v1.1.
> **Nguồn:** [`00-canon.md`](00-canon.md) §8.1–8.3, D48, D52, D53; [`ART_AUDIO_VFX_PLAN.md`](ART_AUDIO_VFX_PLAN.md) §0.1, §2, §3.2; ảnh đo `games/immortality-cultivation/tmp/plan-2026-11-01/legend-prep-1080.png` và `greybox-prep-1080.png`.

## 1. Camera và khung (số đo, không đổi)

- Camera nhìn về bắc từ phía nam, nghiêng 55° dưới chân trời, FOV dọc 28°, cố định, không zoom. Sân 40 × 26 m: x −20…+20 (đông dương), z −18 (mép xa, cổng) … +8 (mép gần, phía Sơn Môn). Trận Tâm ở (0; 0).
- 1920 × 1080: mép xa y 84, rộng 261 → 1659 (35 px/m); Trận Tâm (960; 611); mép gần y 920, rộng 39 → 1881 (46 px/m); Bàn Quyết (DOM) che từ y ≈ 930.
- **Không thấy trời**: mép trên khung ở 41° dưới chân trời. Mọi thứ trong khung là mặt đất và mặt trên của vật, nhìn từ trên xuống.
- **Ngân sách chiều cao** (sau D53, headroom ~5,5 m): vật ở mép xa cao tới ~5 m lọt khung; ở z −10 tới ~8 m; từ z −5 trở vào không giới hạn thực tế. Trước D53 chỉ 2,5 m ở mép xa: ảnh legend có cột mẫu 2,5 m.
- **Vùng ngoài sân nhìn thấy**: dải trên (ngoài mép xa) ~130 px sau D53; hai tam giác bên rộng nhất ở mép xa (~7,5 m đất mỗi bên), thu về ~1 m ở mép gần; dải dưới nằm dưới Bàn Quyết.

## 2. Bố cục (tọa độ mét; mọi vị trí gameplay cố định)

| Vùng | Ở đâu | Vẽ gì |
|---|---|---|
| **Trận Tâm** | (0; 0), đĩa r 3 m | Đĩa đá xanh lát vòng đồng tâm, lõi là một khối ngọc trắng ngà phát linh quang (nguồn sáng phụ lạnh), vòng rune khắc chìm sáng mờ; 4 cột đá thấp 0,8 m ở 4 hướng |
| **Kết Giới** | vòng r 9 m | Đường khảm ngọc trắng ngà 0,25 m trong đá, khi nhìn kỹ thấy hoa văn mây; shader làm nó thở. Trong vòng: đá lát mịn, tối và yên (vùng chữ nổi) |
| **Tâm nhãn** | (0; +3) | Ô đá tròn r 1 m khắc hoa văn, phía nam Trận Tâm, chỗ người chơi đứng đầu trận |
| **Hai hành lang thú** | từ cổng A (−15; −18) và B (+15; −18) tới mép Kết Giới, rộng ~5 m | Đá lát phẳng mòn bóng, **sáng hơn đá quanh ≥ 1,3 lần**, vết cào và vết mực loang ở gần cổng; mép hành lang là rãnh thoát nước có rêu |
| **Đất ngoài hành lang** | phần còn lại trong sân | Đá lát lớn kém đều, rêu xanh xám ở khe, vài phiến nứt, bậc thấp 0,2 m đổi cao độ nhẹ ở hai bên để sân không phẳng lì (không chặn đường) |
| **Trận Trụ T, P** | (−6,4; −7,7), (+6,4; −7,7), r 0,9 m | Cột đá xanh 4,5 m, đỉnh có bệ ngọc và một vòng sắt cũ; bản nứt là texture thứ hai |
| **6 ô cơ quan** | ô1 (−10,2; −12,3) dải 4 × 2, ô3 (+10,2; −12,3) dải, ô2 (−11,5; −8), ô4 (+11,5; −8), ô5 (−10; −2), ô6 (+10; −2) trụ r 0,8 | Ổ cắm đá khắc chìm (chỉ hiện khi bày trận, lúc nghỉ): dải là rãnh đá có lỗ cắm; trụ là bệ tròn có vòng khắc |
| **Cổng A, B** | (∓15; −18), rộng ~5 m | Cổng ải đá: hai trụ đá vuông lớn + xà đá, mái ngói chàm xám dốc thấp, rộng, nhìn từ trên thấy ngói và đầu đao; đèn lồng đá hai bên (ánh ấm nhỏ); cao ≤ 5 m |
| **Lối trời** | từ (±20; −18) | Không có vật; chỉ sương mỏng tụ ở hai góc trên để thú bay đọc được |
| **Mép xa (z −18) ngoài cổng** | dải trên | Tường thấp 1,2 m bằng đá xếp; sau tường là **biển mây** nhìn từ trên, vài đỉnh vách đá vôi nhô lên, tán tùng; không có đường chân trời |
| **Hai bên (x ±20)** | tam giác bên | Lan can đá thấp; ngoài lan can là mép vách rơi xuống biển mây, tán tùng cổ bám vách (chỉ thấy ngọn), tảng đá vôi, sương |
| **Mép gần (z +8)** | dưới, cạnh Bàn Quyết | Đầu bậc đá đi xuống Sơn Môn, hai trụ lan can có đèn đá; phần lớn nằm dưới Bàn Quyết |

## 3. Ánh sáng và thứ bậc độ sáng

- **Một nguồn chính:** nắng sớm xiên từ đông bắc (trên phải khung), góc thấp ~30°, hơi ấm; bóng dài về tây nam để cột, cổng, bậc có khối. Bóng không đổ lên hành lang nhiều (hành lang phải sáng).
- **Fill:** sương lạnh xanh chàm từ biển mây hắt lên; lớp sương thấp 0,3 m ngoài Kết Giới, không vào trong vòng.
- **Nguồn phụ:** linh quang Trận Tâm trắng ngà (điểm sáng nhất sau nắng); đèn đá ở cổng và lan can ấm nhỏ (điểm nhìn thứ ba).
- **Thứ tự mắt nhìn:** 1 Trận Tâm → 2 hai cổng (và thú đổ vào) → 3 hai Trận Trụ → 4 viền sương. Không điểm sáng lạc nào khác.
- **Giá trị (đo sau khi có tranh):** hành lang 1,3× đá quanh; trong Kết Giới mid-dark; viền ngoài sân tối nhất; Trận Tâm sáng nhất; không vùng nào có độ sáng ≥ 0,95 quá 6 % sân.

## 4. Màu dành cho tín hiệu (môi trường không dùng ở cường độ cao)

Đỏ `#FF4A4A` đòn địch · cam `#FFB020` khẩn · vàng kim `#FFC83A` tiền · xanh ngọc `#7FF5E0` sức gõ, Hộ thân, Kết Giới. Môi trường: đá xanh xám, rêu lục xám, gỗ nâu sẫm, ngói chàm xám, ngọc trắng ngà, sương chàm; đỏ son chỉ ở dấu triện nhỏ trên UI. Mắt thú sáng xám tím.

## 5. Chất liệu (một họ cho cả map)

Đá vôi xanh xám kiểu Ninh Bình – Hà Giang (phiến lát, cột, lan can, cổng), rêu và địa y, gỗ lim sẫm (xà, cửa), ngói âm dương chàm xám, ngọc trắng ngà (khảm, lõi Trận Tâm), sắt cũ (vòng cột, đèn), sương. Không ngói vàng cung đình, không đèn lồng đỏ, không chữ Hán, không rồng vàng.

## 6. Sự sống

Sương trôi chậm qua cổng; lá tùng rơi thưa; đèn đá nhấp nháy nhẹ; vài con hạc rất nhỏ trên biển mây xa (ngoài sân, không bao giờ trong vùng chơi); cỏ núi lay ở mép bên. Không động vật trong sân.

## 7. Dựng được bằng gì

- Tripo: cổng ải, Trận Tâm, Trận Trụ, 3 cơ quan, phi kiếm, đá vôi; đèn đá nhỏ (vật nhỏ 12k) thêm vào §7 của plan nếu ChatGPT giữ.
- Đất: 6 ô PBR từ ambientCG (CC0) + lớp vẽ Firefly; 8 decal; lưới sân có cao độ nhẹ.
- Viền ngoài sân: 3 lớp tranh Firefly nhìn từ trên (biển mây, đỉnh vách và tùng, sương gần), cỏ bụi thẻ.
- Shader: Kết Giới, linh quang, sương thấp, ô cơ quan; hậu kỳ: bloom đúng luật, SMAA, sương theo khoảng cách.
- Nguồn CC0 thử: đá vôi và tùng quét thật từ Poly Haven cho viền.

## 8. Điều ChatGPT cần trả lời

Điểm trên 10 so với game thương mại cùng loại; khoảng trống lớn nhất (bố cục, tỉ lệ, chiều sâu, ánh sáng, chất liệu, sự sống, dễ đọc); đề xuất giữ bố cục gameplay; một tranh vẽ đè đúng khung; ba dòng ghi đã đổi gì.
