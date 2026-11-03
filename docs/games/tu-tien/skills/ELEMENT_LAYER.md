# Element layer: weapon × element (canon D59, 03/11/2026)

Anh chốt sáng 03/11: người chơi chọn **hệ** riêng, độc lập với **phái vũ khí**. Lời anh: "khi người chơi kết hợp cả vũ khí và hệ, ví dụ hệ hoả, thì hiệu ứng của vũ khí chủ đạo phải là lửa, hoặc nếu kỹ năng có tính hệ thuỷ, thì hiệu ứng của kỹ năng đó khi tung ra chủ đạo sẽ là thuỷ".

Tài liệu này là thiết kế để dựng. Nguồn nghiên cứu: ChatGPT (Chat, thinking High) và Gemini (Argon, mức Cao) trả lời độc lập cùng một đề bài ba phần, ở [`source/element-materials-*`](source/). Đây là ý kiến thứ hai, đã đối chiếu nhưng chưa mở lại từng link; nguồn nào dùng tới thì kiểm nguồn đó.

## 1. Hai lớp của một chiêu

| Vũ khí (Sword, Sabre, Spear) giữ | Hệ (8 hệ) giữ |
|---|---|
| đường bay, số lượng, độ tỏa, góc quạt, đội hình | chất liệu của thân, mép, lõi |
| kích thước vật bay, nhịp, chọn mục tiêu | vật chất phụ (tàn lửa, bọt nước, mảnh đá, lá) |
| cử chỉ của Lam, camera | hành vi theo pha (nén rồi bùng, chảy tiếp, ngưng lại) |
| bóng dáng món đang cầm (D55) | va chạm, trạng thái mặt đất, phản ứng trên thú |
| | điểm nhấn màn hình, ánh sáng, tiếng |

- **Luật cứng: thay, không chồng.** Chọn Hỏa thì vẽ chính hình đó bằng bộ chất Hỏa. Không vẽ lớp Kim rồi rắc thêm hạt lửa lên trên.
  - Mỗi lớp Kim có một lớp thay thế: chất vật bay, tia lửa khi trúng, mảnh vỡ, vết cắt trên đất, điểm nhấn màn hình, kiểu chết.
  - Lý do thứ hai là ngân sách: chồng lớp thì vượt trần khung hình.
- **Bộ hiện tại của Kiếm (trắng bạc, lam ngọc, mép trắng nóng) là bộ chất Metal.**
- **Không vẽ riêng từng tổ hợp:** 3 bộ hình × 8 bộ chất, thay vì 24 tổ hợp × 6 chiêu.
- **Hào quang quanh kiếm bay** là một lớp **hình** của vũ khí; hệ chỉ cấp chất cho nó qua mục `swordAura` (`SwordAuraLook`) của bộ chất. Ba hướng cho anh chọn: [`SWORD_AURA.md`](SWORD_AURA.md).
- **Kiểu lửa và lớp lấp lánh quanh các hình của chiêu** (lửa va chạm, tia lửa, sao, vòng, tia sáng, ánh chạy trên ấn; lời anh 03/11: lửa phím 1 "hơi xấu", tia lửa "khá là thô", chiêu phải "lấp lánh, long lanh hào quang"): chẩn đoán, nghiên cứu đã kiểm, ba hướng trên bảng hình và kế hoạch lab ở [`FIRE_STYLE.md`](FIRE_STYLE.md).
- **Hào quang quanh từng chiêu, từng pha** (phím 0–7, Metal và Fire): bảng kiểm, xếp hạng chỗ thiếu, bảy lớp dùng chung, mục `radiance` của bộ chất, ngân sách và thứ tự làm ở [`SKILL_RADIANCE.md`](SKILL_RADIANCE.md).

## 2. Luật và cách đọc của từng hệ

Mỗi hệ có một **động từ chính** để nhận ra ngay ở 40–100 px dưới camera 55°, trước cả màu.

| Hệ | Động từ | Vũ khí trở thành | Nhận ra ngay khi | Làm rẻ khi |
|---|---|---|---|---|
| Metal | align → shear | kiếm thật, mép trắng nóng, đường thẳng như thước | đội hình khóa lại rồi một nhát cắt sạch | vệt mềm, đường cong, phát sáng như đũa nhựa |
| Fire | compress → burst | lưỡi lửa nung trắng vàng, quấn lửa cam | mọi thứ hút vào một lõi nhỏ rồi bung mạnh | lửa trong mờ thành lớp màn cam, cam bị bạc thành màu da |
| Water | flow → engulf | khối nước liền, chảy theo đường cong chữ S | khối nước cong vẫn chảy tiếp qua và vòng quanh mục tiêu | lưới xanh nhạt trong mờ, mép mềm, như thạch hay khói ma |
| Thunder | mark → judge | vũ khí đánh dấu, sét giáng thẳng từ trời | cột sét dọc từ mép trên khung hình | màn hình đầy nhánh điện |
| Wood | grow → claim | cành, gai mọc dài và tẽ nhánh khi bay | vật bay dài ra và tẽ nhánh: trông như mọc, không như bắn | hạt xanh và lá bay quanh vũ khí thường |
| Earth | mass → crush | khối đá, phiến khoáng có trọng lượng | khối lớn khựng lại vì nặng rồi đập xuống, để lại địa hình | khói nâu, pha lê vàng chung chung |
| Wind | pressure → sweep | vỏ áp suất gần như vô hình | thú và mảnh vụn bị đẩy trước khi đòn tới, rồi một vòng áp suất | tia xanh lá, lốc xoáy tràn lan, dải trong mờ khắp nơi |
| Ice | stillness → shatter | lăng trụ, lưỡi băng có mặt cắt | mọi thứ dừng một nhịp rồi vỡ | nước xanh kèm bông tuyết, lấp lánh liên tục, nghìn mảnh vụn |

Bảng màu, 5 pha, phản ứng trên thú và tham chiếu chi tiết từng hệ nằm ở nguồn nghiên cứu.
- **Hỏa:** lõi lửa tránh đúng mã đỏ cảnh báo của địch `#FF4A4A` (D54), đi từ trắng vàng → hổ phách → cam son → bồ hóng tím than.
- **Thủy:** thân chàm đậm gần đen, bọt trắng mép cứng, vân sáng trên đất.

## 3. Hệ thống dùng chung (dựng một lần)

| Hệ thống | Dùng cho | Ở đâu trong mã |
|---|---|---|
| `FlipbookPlayer` | Fire, Thunder, Wind, clip RGBA của Water và các hệ khác | mới; chép từ `games/dragon-hold/src/view/flipbook.ts` (dòng nguồn, `SYNC_DEBT.md`) |
| Element surface master | lưỡi, dải, khối của mọi hệ: đục hoặc cắt, phát sáng, trong mờ; dải màu và mép, lõi | mở rộng `src/view/skills/sword-material.ts` |
| Ground decal pool | dấu cháy, vũng nước, vết nứt, rễ, băng trên đất | mới; thay `GroundSigil` ở pha dư âm |
| Foe status | cháy, ướt, bị rễ giữ, bị đè, bị điện, bị cuốn, đóng băng, bị cắt | mở rộng `src/lab/victims.ts` và kiểu chết |
| Instanced matter | mảnh kim loại, đá, cành, pha lê | mới, `InstancedMesh` |
| Distortion mask | hơi nóng (Fire), khúc xạ (Water), áp suất (Wind); một RT 480×270 dùng chung, một lần ghép | mới, trong chuỗi hậu kỳ |
| Screen accent | chớp, viền tối, giảm bão hòa, tia hướng tâm | `src/view/screen-fx.ts` đã có |
| Element ramp atlas | dải màu theo hệ, một hàng mỗi hệ | thay bảng màu trong `skillGlow()` |
| Impact frame | khung đảo màu kiểu manga | đã có, chỉ đổi bảng màu |

**Cách cắm vào mã Kiếm:**
- `kiem.ts` đã chia theo lớp hiệu ứng: `releaseFlash`, `impact`, `hitSparks`, `slashAt`, `death`, `riseMote`, các dải và vòng xung kích. Mỗi hàm sẽ hỏi bộ chất của hệ đang chọn "vẽ lớp này bằng gì".
- `KiemTextures` (14 kết cấu) thành bộ kết cấu theo hệ.
- Tiếng theo hệ tìm `release-k1-fire` trước, không có thì về `release-k1`.
- Lab chọn hệ bằng `?element=` và một ô trong bảng điều khiển; mặc định là Metal.
- **Đổi tên trong lần sửa này:** `kiem.ts` thành `sword-skills.ts`, `van-kiem.ts` thành `myriad-swords.ts` (tên tiếng Anh, anh nhắc 03/11).

## 4. Nguồn chất và kênh trong suốt

| Loại | Kênh trong suốt |
|---|---|
| Lửa, sét (tự phát sáng) | cộng sáng trên nền đen; đen là không có năng lượng |
| Vệt gió | độ sáng làm mặt nạ, shader tô màu và làm méo |
| Bọt và bụi nước trắng | được dùng độ sáng làm alpha |
| Thân nước, đá, cành, băng | **chỉ alpha thật**, không bao giờ lấy từ độ sáng |

- **Firefly Video có "Transparent background"** (đã kiểm trong giao diện 03/11):
  - chỉ có khi chọn model **Firefly Video** của Adobe; trang mặc định chọn Veo 3.1 là model đối tác, phải đổi trước khi tạo;
  - 540p, 5 giây, có kiểu Anime, Fantasy, 3D và camera Static.
  - Thử nó trước cho bọt, sóng, đá, cành. Không đạt thì dựng trong Blender (mô phỏng chất lỏng, shader toon, xuất RGBA ở đúng góc 55°), chỉ cho 3–4 cú va chạm lớn.
- **Prompt Firefly Video:**
  - camera Static, nền đen phẳng (khi không dùng nền trong suốt), hiệu ứng nằm giữa và chiếm ≤ 65–75 % khung, một hành động;
  - không sàn, không cảnh, không khói mù, không lóe ống kính;
  - clip lặp thì khung đầu và khung cuối giống nhau.
- **Dùng lại trước khi tạo mới:** Dragonhold có 12 flipbook lửa Firefly (lốc cầu lửa, dải lửa, nổ hình sao, lửa trên đất, tàn lửa, cầu lửa nổ, khói). Lửa dùng chúng ở chế độ cộng sáng; làm thân lửa đè trên nền sáng thì không được.
- **Tiếng Hỏa đã tạo** (03/11, Firefly, model Adobe): `tt-sfx-fire-implode`, `-ignite`, `-swing`, `-flyby`, `-impact`, `-burst`, `-roar`, `-crackle-tail`. Mỗi id 2 lượt × 4 bản, riêng `roar` 1 lượt.

## 5. Ngân sách (High, 1080p, p95)

Trần khung hình là 11,5 ms. Phím 7 hiện ở 10,2–10,9 ms, nên mỗi hệ chỉ được thêm tối đa **0,85 ms** so với Metal:

| Phần | Trần |
|---|---|
| thân và vật bay | 0,20 ms |
| va chạm và hạt | 0,20 ms |
| pass méo dùng chung | 0,15 ms |
| dấu trên đất, dư âm | 0,10 ms |
| điểm nhấn màn hình | 0,10 ms |
| khác | 0,10 ms |

- **Chồng lớp:** tối đa 2 lớp trong mờ chồng nhau ở một điểm ảnh. Thân chính ưu tiên lưới đục hoặc cắt (alpha-test). Cấm tấm sprite phủ cả sân trừ tuyệt kỹ chớp nhoáng.
- **Flipbook:** 8–16 khung, ô 256 px; va chạm lớn ô 512 px; không đưa cả clip 5 giây vào game.
- **Bậc đồ họa:** Medium nửa số mảnh vụn và pass méo yếu hơn; Low tắt pass méo, chỉ còn dấu trên đất.

## 6. Thứ tự (anh: "cứ làm lần lượt theo như plan")

1. Hệ thống dùng chung, và chuyển bộ Metal hiện tại vào cùng giao diện (hình không đổi).
2. **Sword × Fire** trên hai chiêu: phím 1 (Threefold Sword Command, nhiều vật bay cùng lúc) và phím 7 (Myriad Swords, chiêu tự săn cả sân, phép thử nặng nhất). Không thử tuyệt kỹ trước: một tuyệt kỹ dựng riêng có thể che một hệ thống hỏng.
3. **Sword × Water** với **đúng** dữ liệu hình và nhịp của hai chiêu đó, chỉ đổi bộ chất. Đây là phép thử mạnh nhất cho kiến trúc.
4. Wind, Ice, Earth, Wood, Thunder.
5. Áp vào Sabre và Spear khi hai phái đó có trong lab.
6. Tuyệt kỹ và cut-in theo hệ, đánh bóng sau cùng.

## 7. Cổng đạt

Chung cho mọi hệ: hai giám khảo mù đều chấm ≥ 8,5 ở bản build chơi, theo cài đặt của người chơi, không cờ URL.

**Fire:**
- cả hai giám khảo gọi ra "lửa" ngay, không cần tên;
- xem ảnh xám vẫn thấy nén rồi bùng;
- ở 40–100 px vẫn nhận ra hình vũ khí lẫn lửa;
- trên nền đá sáng không có lớp màn cam; trên nền tối không có viền đen hay khung tách nền;
- thân cam vẫn cam, chỉ lõi gần trắng vàng;
- phím đúng cuối tới lúc thấy phát chiêu ≤ 50 ms; không chữ gõ nào bị khó đọc;
- chiêu cả sân vẫn tách được từng đường, không thành nồi lửa;
- thêm ≤ 0,85 ms p95; cận cảnh không lộ tấm phẳng.

**Water:**
- giữ nguyên đường bay, số lượng, nhịp;
- đọc ra nước, không phải năng lượng lam;
- ảnh xám vẫn thấy khối chảy liền;
- dòng chảy tiếp qua va chạm;
- trên nền sáng thân vẫn có hình; trên nền tối không thành miếng dán xanh đục;
- không ai thấy giống băng;
- sóng và mép bọt vẫn còn dưới camera 55°;
- chiêu cả sân không thành mớ dải rối;
- cùng trần 0,85 ms.

## 8. Bẫy đã gặp (lửa rồng Dragonhold, `docs/games/vfx/DRAGON_FIRE_DIAGNOSIS_2026-10-31.md`)

- **Chuỗi hỏng:**
  - độ sáng của clip làm alpha, nên lửa mờ hay đang nguội thành nửa trong suốt;
  - nền đá sáng lộ qua, ra lớp màn cam;
  - tăng sáng để bù, thì tone mapping Neutral nén màu nóng về trắng: cam thành màu da.
- Bốn vòng chỉnh thông số không sửa được, vì cách biểu diễn sai từ gốc.
- **Phòng:**
  - kênh trong suốt luôn tách khỏi màu;
  - thân chính là lưới hoặc khối đục;
  - phần cộng sáng chỉ cho lõi và chi tiết mảnh;
  - kiểm màu cam sau tone mapping bằng số;
  - thử trên cả nền sáng lẫn nền tối trước khi gửi giám khảo.

## 9. Chờ anh chốt (từ D59)

- Hệ đã chọn có thành hệ sát thương khi khắc không. Đề xuất: có, giữ ×1,30 / ×0,80 của D23.
- Ô chiêu lấy từ vũ khí; bộ chiêu riêng của từng hệ trong `SKILL_CATALOG_V2.md` dùng thế nào. Đề xuất: lấy làm khoảnh khắc chữ ký và tuyệt kỹ của hệ đó.
- Những hệ nào có ở MVP.
- Chọn hệ lúc nào: lúc tạo nhân vật, hay trước mỗi trận.
