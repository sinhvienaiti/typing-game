# Vũ khí: ảnh tham khảo và mẫu prompt (02/11/2026, chiều)

Chủ dự án, 02/11: "liệu bạn đã tự review lại prompt chưa, đã nhờ chatgpt review lại prompt, cải thiện prompt chưa, đã lấy 1 số hình ảnh để tham khảo để 2 bạn có hình mẫu tạo ra prompt chưa". ChatGPT (Chat mode, High) đã tra web, xem ảnh chính thức của 13 vũ khí rồi viết lại mẫu prompt. Phần dưới tóm tắt câu trả lời của nó; Claude đã đọc và chốt dùng.

## 1. Bảng tham khảo (ảnh chính thức trên trang game hoặc wiki)

| # | Vũ khí | Nguồn | Học được gì |
|---|---|---|---|
| 1 | Mistsplitter Reforged (Genshin) | HoYoWiki | Phát sáng là một trạng thái sức mạnh, không phải một đường LED nhỏ |
| 2 | Haran Geppaku Futsu (Genshin) | HoYoWiki | Hoa văn, màu và dòng chảy của lưỡi cùng nói một ý ("sóng") |
| 3 | Primordial Jade Cutter (Genshin) | HoYoWiki | Một ý vật liệu đủ mạnh để nhận ra cả khi tắt VFX |
| 4 | Light of Foliar Incision (Genshin) | HoYoWiki | Ba cấp chi tiết: bóng lớn, mảng khảm vừa, khắc nhỏ |
| 5 | Redhorn Stonethresher (Genshin) | HoYoWiki | Mảng lớn và bất đối xứng thắng chi tiết ở cỡ nhỏ |
| 6 | Staff of Homa (Genshin) | HoYoWiki | Đầu cán dài chiếm hết độ phức tạp, cán để nghỉ |
| 7 | Calamity Queller (Genshin) | HoYoWiki | Ánh sáng nằm bên trong cấu trúc, không phủ ngoài |
| 8 | Emerald of Genesis (Wuthering Waves) | Wuthering Waves wiki | Một khối năng lượng lớn được giữ trong vỏ vật chất |
| 9 | Blazing Brilliance (Wuthering Waves) | Wuthering Waves wiki | Năng lượng có hướng: một khung hình đã thấy nhiệt chạy dọc lưỡi |
| 10 | Verdant Summit (Wuthering Waves) | Wuthering Waves wiki | Vũ khí nặng vẫn có tốc độ nhờ các đường chảy dài |
| 11 | Seven Thunders of Retribution: Narukami (Honkai Impact 3rd) | trang hướng dẫn chính thức | Vũ khí có trạng thái "bật sức mạnh" phô trương hơn lúc nghỉ |
| 12 | Kiếm dài huyền thoại của Naraka: Bladepoint | trang cập nhật chính thức | Hoa văn dày vẫn được nếu tâm điểm rõ |
| 13 | Heng Blade (Where Winds Meet) | NetEase | Dáng binh khí lịch sử thật vẫn đẹp nếu cách trình bày đủ cao cấp |

Đây chỉ là mốc chất lượng. Không chép bóng dáng, hộ thủ, hoa văn lưỡi hay cách chia màu của bất kỳ món nào.

## 2. Mười bí quyết

1. Một hình chủ đạo lớn trước mọi thứ. Nếu ở 25–40 px không nhận ra, khắc thêm cũng không cứu được.
2. Một ý lớn về vật liệu hoặc năng lượng, nói được trong một câu.
3. Có thứ bậc: một vùng "ồn" và một vùng nghỉ, không trang trí đều từ đốc tới mũi.
4. Ánh sáng 5 sao có ba lớp: lõi gần trắng, thân màu rõ, quầng mềm. Một rãnh nhỏ thường chưa đủ.
5. Ánh sáng bên trong đẹp hơn đường sáng dán ngoài: dưới pha lê, trong hốc, giữa hai lớp lưỡi, trong vòng rỗng.
6. Vật lơ lửng lặp lại motif của chính món đó, không rải mảnh ngẫu nhiên.
7. Bề mặt có ba cỡ: khối bóng dáng, mảng khảm vừa, khắc nhỏ. Các bản cũ thiếu lớp vừa.
8. Tương phản sáng tối quan trọng hơn độ bão hòa: hốc tối, sứ trắng, lõi sáng.
9. Cách trình bày là một nửa thiết kế: quầng sau, ánh viền, hướng hạt, khoảng tối quanh bóng dáng.
10. Ảnh concept được có hào quang, ánh phản xạ và phần lơ lửng; model trong game sẽ giản lược sau.

## 3. Vì sao prompt cũ cho ảnh "đúng nhưng không ai muốn có"

- Quá nhiều ràng buộc nhỏ (20–40 điều), nên "wow" bị xếp cuối.
- Danh sách cấm quá dài, khiến ảnh dè dặt.
- Luật "chỉ lòng rãnh phát sáng" quá cứng cho ảnh đẹp: nó loại ánh dội bên trong, hốc năng lượng và quầng sáng.
- Số đo chính xác (34 %, 1,6 lần, cách mũi 3 cm) thuộc về tờ dựng model sau khi duyệt, không thuộc ảnh concept.

ChatGPT tự chấm sáu ảnh cũ: Winter Vein khoảng 8–8,3; Ember Crest khoảng 8,2; Thunder Seal khoảng 8 nhưng có nguy cơ thành máy móc; Verdant Branch khoảng 7,5–7,8 (xanh gắt, nhiều lá); Clear Wind cũ khoảng 7,5 (xám); Mountain Verdict khoảng 7,2 (yếu nhất, thiếu sức hút).

## 4. Mẫu prompt (dùng nguyên văn, điền bốn biến)

```text
Premium 5-star xianxia weapon reveal, cinematic anime/donghua game splash art with the visual impact, clarity and desirability of top-tier modern gacha-game weapon presentations, while keeping an entirely original Chinese weapon design.

Show exactly ONE [WEAPON FAMILY] floating diagonally from lower-left to upper-right against a deep charcoal background, fully visible, three-quarter view slightly from above. Its base silhouette must unmistakably come from [CHINESE HISTORICAL WEAPON ANCHOR]. Give it ONE dominant signature shape that remains recognizable at thumbnail size: [HERO SILHOUETTE HOOK].

Make it feel like a divine artifact, not a museum replica and not Western fantasy. Use layered cold brushed silver, bright polished bevels, deep smoke-silver recesses, blue-white glazed porcelain, tiny restrained pale-jade accents and deep-indigo wrapped grip. Break large metal surfaces into clear material zones: structural dark metal, satin blade fields, porcelain or crystal inserts, recessed channels and fine shallow ornament. Use refined cloud/ruyi/lotus-inspired relief only as secondary craftsmanship, never as the main silhouette.

The supernatural focal point is [HERO ENERGY IDEA]. Give it a brilliant near-white energy core with [ELEMENT COLOR] body and a soft surrounding aura. The power should feel visibly contained inside or between parts of the weapon geometry, with controlled reflected light spilling onto nearby metal and porcelain. The weapon may have one larger internal luminous region, energy blade, suspended core or illuminated cavity if that makes the design feel more extraordinary.

Add 2–4 detached supernatural elements that repeat the weapon's own motif—small rings, seals, shards, petals, plates or energy fragments—and one elegant directional energy ribbon or arc that guides the eye from the hilt toward the tip. Keep all floating effects behind or around the silhouette, never covering the weapon.

Lighting and presentation: sharp premium anime-game splash render, strong cinematic key from upper-left, powerful cool rim light, deep shadow cavities, brilliant specular edges, one large soft circular back halo centered behind the main focal point, sparse directional particles, rich contrast and vivid but controlled element color. The weapon should immediately feel rare, regal, supernatural and desirable.

Preserve readability: one hero shape, one hero material/energy idea, one primary focal zone. Do not distribute equal detail over the entire weapon.

Hard exclusions: no gold or bronze, no large central gemstone, no tassels or flying cloth, no text, logos or Chinese characters, no generic Western crossguard, no angel wings, claws or random spikes, no sci-fi mechanical housings unless explicitly requested. Do not copy the silhouette, guard, blade pattern or color layout of any existing Genshin Impact, Honkai, Wuthering Waves or other commercial weapon.
```

Sau mẫu, thêm 4–6 câu về điểm riêng của món đó. Mỗi món một kiểu "cảnh tượng" khác nhau để cả bộ không cùng công thức:

| Món | Cảnh tượng riêng |
|---|---|
| Clear Wind | vòng trăng và dải gió |
| Winter Vein | pha lê khúc xạ và sương rơi |
| Thunder Seal | khung ấn và tia điện vuông |
| Verdant Branch | nhựa sống chảy và vài lá trúc lớn |
| Ember Crest | cung nhiệt lò rèn và tàn lửa |
| Mountain Verdict | quầng địa tầng và phiến đá lơ lửng |
| Tidal Crescent | tấm nước lơ lửng và gợn sáng khúc xạ |
| Sky Thread | xoắn áp suất và sợi gió mảnh |
| Resonant Fang | các vòng cộng hưởng đồng tâm |
| Storm Pin | lưới nút điện ngắn |

## 5. Prompt Clear Wind bản 2 (đã vẽ, `showcase-clear-wind.v2-try1.png`)

```text
Premium 5-star xianxia divine-sword reveal, cinematic anime/donghua game splash art with the visual impact of elite modern gacha-game weapon presentations, but an entirely original Chinese jian.

Show exactly ONE long, slender Han-inspired double-edged jian floating diagonally from lower-left to upper-right, fully visible, three-quarter view slightly from above. Its unmistakable signature is a large flat hollow bi-disc guard in the SAME PLANE as the blade: a refined circular silver-and-blue-white-porcelain ring pierced by the blade through its center, with two broad dark negative spaces visible through the ring. No Western crossguard beneath it.

The sword belongs to a regal female sword cultivator. Make it breathtaking, lunar, noble and supernatural. Use cold brushed silver, polished bright bevels, deep smoke-silver recessed fields, luminous blue-white porcelain, tiny pale-jade accents and a deep-indigo wrapped grip. The blade is very long and narrow with a strong diamond ridge; break up the steel with one elegant porcelain inlay zone and shallow flowing-wind engravings so no large surface feels plain.

Hero energy idea: the bi-disc contains a suspended "clear wind moonlight" field. A brilliant silver-white energy core runs from inside the ring into the center ridge of the blade and becomes increasingly radiant toward the needle tip. The energy is visibly contained inside the sword, but it casts bright reflected light onto nearby silver and porcelain. Let the inner rim of the bi-disc catch a luminous lunar edge, as if the ring is focusing the blade's power.

Around the ring, add two incomplete concentric moonlight arcs and three tiny floating bi-disc fragments, all clearly detached from the weapon. Add one elegant translucent wind ribbon passing through the ring and flowing toward the blade tip, plus sparse silver particles. Strong circular back halo behind the ring, crisp upper-left key light, powerful cool rim light, deep dark cavities and bright premium specular edges.

The overall impression should be "a royal immortal's moonlit flying sword": graceful rather than bulky, dazzling rather than gray, ancient Chinese in silhouette but impossibly refined and divine.

No gold or bronze, no large gemstone, no tassel or flying cloth, no text, logo or Chinese characters, no cross-shaped or T-shaped guard, no wings, claws or random spikes, no Celtic sun-wheel spokes, no jade blade, no generic Western fantasy sword.
```

## 6. Năm câu tự kiểm trước mỗi ảnh

1. Bỏ màu đi, hình chủ đạo là gì? Phải trả lời được trong 3–5 từ.
2. Bỏ hạt sáng đi, vũ khí còn đẹp không? Nếu không, hình khối và vật liệu chưa đủ.
3. Năng lượng chính nằm ở đâu? Chỉ được một câu trả lời.
4. Thu về 25 px, phần nào còn sống? Hình chủ đạo phải còn khác biệt 2–4 px.
5. Có gì khiến người xem nghĩ ngay tới một vũ khí thương mại cụ thể không? Nếu có, đổi bóng dáng hoặc cách chia màu trước khi vẽ.

## 7. Rủi ro ChatGPT tự nêu

- Câu mốc "vũ khí gacha hàng đầu" có thể kéo ảnh về Genshin hoặc Wuthering Waves (katana, hộ thủ Inazuma, viền vàng). Ngay sau câu mốc luôn có câu "entirely original Chinese weapon".
- Các chữ như "divine", "ornate", "crystalline" dễ gọi ra hộ thủ chữ thập, cánh, đá to. Câu neo binh khí Trung Hoa phải đứng sớm, và chỉ cấm 3–5 lỗi lớn.
- Thêm lớp và vật lơ lửng dễ làm ảnh chết ở 25 px: mỗi món chỉ một hình, một tâm điểm, một ý năng lượng.
- Quầng sáng quá mạnh làm mất đường viền: vũ khí phải sắc hơn quầng, có khoảng tối sát viền.
- Ánh sáng bên trong dễ thành sci-fi (lò phản ứng, kiếm laser): luôn gắn với một ẩn dụ tiên hiệp (trăng, mạch băng, nhựa sống, lửa vùi, linh khí núi, ấn sét).
