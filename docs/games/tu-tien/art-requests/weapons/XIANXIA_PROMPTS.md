# 5 kiểu prompt tu tiên, thảo luận với ChatGPT (02/11/2026, tối)

Chủ dự án, sau vòng 15: "chán thật, bạn tạo kiếm xấu thật sự, nhìn nó quá mức đơn giản, rõ ràng 12 ảnh chatgpt gửi nó rất đẹp và khác, ảnh của bạn đang bị tạo style đơn giản và nó k kiểu mấy loại trong tiểu thuyết tu tiên, tôi nghĩ bạn nên thảo luận với chatgpt để đưa ra 5 loại prompt để thử xem có cải thiện được hơn k".

Thảo luận trong chat `6ae888dc` (có 12 mẫu), có đính kèm 5 ảnh vòng 15. Toàn văn trả lời của ChatGPT lưu ở scratchpad phiên (`doc-inbox/tt-xianxia-discussion.v1.txt`).

## Chẩn đoán

Claude nêu 5 nguyên nhân, ChatGPT đồng ý cả 5:
1. Prompt đòi sự đơn giản ("sparse ornament", "restrained", "clean silhouette", "one material", "generous empty space"), ngược hẳn với mẫu: hộ thủ nhiều tầng, đá quý, chạm lộng, kim loại hai tông, khảm phát sáng.
2. Cấm vàng nên mất tương phản kim loại ấm, thứ gần như mẫu nào cũng dùng.
3. Khi kéo prompt xa bản gốc, đã bỏ đúng nét đẹp nhất (lông phượng, ngọn sóng) và thay bằng hình học trơn.
4. Đặt độ rõ ở 25 px lên trên vẻ đẹp của ảnh trình diễn. Ảnh trình diễn phải giàu; model trong game giản lược sau.
5. Model ảnh thiếu từ vựng trang trí cụ thể nên điền bằng hình chung chung.

ChatGPT thêm:
- **Sơ đồ khái niệm, không phải vật khiến người ta thèm.** Mẫu có thứ bậc điểm nhìn nhiều tầng, chỗ chuyển giữa các phần đắt tiền, nhiều nhiệt độ chất liệu, cụm trang trí ở các khớp, một "luận đề" kỳ ảo mạnh.
- **Vẻ đẹp nằm ở mối nối:** gốc lưỡi vào cổ, cổ vào hộ thủ, hộ thủ vào chuôi, chuôi vào núm, núm vào tua hay hạt.
- **Hộ thủ phải là một tiểu cảnh:** vòng lồng nhau, khung lồng nhau, tầng cánh hoa, chạm lộng, vật treo, hạt đá quý, viền trong và viền ngoài.
- **Chất liệu nông:** cần ít nhất ba họ chất liệu (kim loại kết cấu, vật quý khảm, điểm nhấn mềm hay trang trí).
- **Thiếu ngữ pháp tu tiên:** đọc ra kiếm fantasy chung, không ra pháp bảo, bảo vật tông môn, kiếm được nuôi bằng linh khí trăm năm.
- **Nền đẹp nhưng không có linh hồn riêng:** nền phải là "lãnh địa" của vũ khí (trận pháp đáp lại pháp bảo, biển mây rẽ quanh kiếm khí, lò rèn tiên sau đao lửa).

Luật thiết kế mới cho ảnh trình diễn (thay cho "một ý tưởng sạch, dễ đọc"): **một luận đề chính, hai hệ trang trí phụ, ba họ chất liệu, một vùng hào quang có cảm xúc riêng.** Cho phép vàng hay kim loại ấm làm điểm nhấn, cho phép tua kiếm hay dải lụa nếu làm đẹp hơn; vẫn không chữ, không chép thiết kế có sẵn.

## Từ vựng tu tiên (ChatGPT, tóm tắt)

- **Hộ thủ:** đĩa bích và vòng lồng (vòng kim loại ngoài, vòng ngọc trong, móc mây, hạt treo); như ý đôi, mây chạm lộng; sen và hoa (cánh sen nhiều tầng, mai năm cánh có đá giữa); kiến trúc (thanh lanh tô bậc, mái cong, cổng vòm nhỏ); ấn sét (khung bát giác, lôi văn, lõi lơ lửng); cành và dây leo.
- **Núm:** nụ sen, cụm mây, vòng có tua hay chuỗi hạt, đỉnh tháp chồng, ấn có đá, đĩa nhật nguyệt, hồ lô ngọc, hạt trong lồng chạm lộng.
- **Lưỡi:** gân giữa và mặt vát gương, thép nhiều lớp vân nước, thép xanh viền bạc, thân bạch ngọc bọc kim loại, rãnh pha lê trong kim loại, linh mạch dưới mặt thép; khảm dây vàng nhạt ở gốc, phù điêu ngọc, mây bạc, xà cừ, men cloisonné, hạt đá ở bốn hướng. Chi tiết dồn ở gốc lưỡi, hộ thủ và gân, không phủ cả lưỡi.
- **Phối chất liệu:** bạc trăng + bạch ngọc + lụa chàm; thép đen + vàng đỏ + pha lê tím; sứ trắng + vàng sâm panh + ngọc thanh; bạc mờ + pha lê lam trắng + lụa trắng; gỗ sơn mài + ngọc nhạt + dây leo mạ vàng; sắt thiên thạch + đường lửa đồng + lụa đỏ.
- **Hào quang:** trận pháp đồng tâm, linh hoàn quay, biển mây rẽ, dải kiếm khí, mảnh phù không chữ, quầng trăng, cánh mai hay lá trúc, đom đóm than hồng, tinh thể băng và phù băng, sợi sét từ lõi ấn, đất đá lơ lửng.

## 5 chiến lược và prompt

### 1. Bảo vật gia truyền (Clear Wind)

> Official 5-star weapon-card art for a premium anime xianxia game, at the beauty level of top signature gacha weapons: immaculate jewel-like rendering, elegant composition, layered precious materials, refined celestial luxury, and a pristine pale pearl background with a faint moon halo, drifting cloud silk and subtle carved border motifs.
>
> Clear Wind, an original Chinese Han jian, is shown whole on a graceful diagonal. The blade is long, slender and noble, mirror-bright cold silver with a crisp central ridge and a translucent pale-jade spirit channel enclosed inside the steel, glowing softly like mist under ice. Near the forte, delicate silver cloud tracery and tiny pale-gold inlay lines enrich the blade root without cluttering it.
>
> Its signature guard is a luxurious hollow bi-disc: an outer cold-silver ring, an inner white glazed porcelain ring, and layered ruyi-cloud brackets curling partly across the circle, with two small jade cabochons and fine champagne-gold filigree rims. The grip is short indigo silk over a sculpted silver core, finished with stacked collars, a lotus-cloud pommel, one pale-jade bead, and a long pale-blue silk tassel.
>
> Silhouette first, but richly detailed: polished metal, porcelain glaze, jade translucency, crisp rim light, premium depth, no text or letters.

### 2. Thiên lệnh và trận pháp (Thunder Seal)

> Cinematic featured-weapon reveal splash for a premium xianxia action game: monumental, divine, high-contrast and ceremonial, with the grandeur of a heavenly thunder decree. Deep storm-violet skies, concentric formation circles, distant cloud vortices and branching electric light frame the weapon, while the sword itself remains razor-sharp and richly rendered.
>
> Thunder Seal, an original Chinese lightning jian, floats upright with commanding symmetry. Its blade is long and slender, forged from dark blued storm steel with bright silver edges and a narrow translucent violet-white lightning vein imprisoned along the central ridge. Near the blade root, fine electrical branches spread under the metal like awakened spirit meridians before resolving into one brilliant core line toward the short symmetric point.
>
> The signature guard is an ornate open thunder seal: a layered octagonal frame of polished silver and darkened silver, with nested leiwen step forms, small violet crystal tablets, inner hanging ring elements, and a glowing circular core suspended in the open centre. The grip is deep indigo silk braided with silver wire and capped by stacked seal-collars; the pommel is a faceted decree-seal topped with a violet crystal and two narrow storm-silk streamers.
>
> Lavish detail, glossy metal, gemstone accents, divine electricity, Chinese immortal authority. No text or letters.

### 3. Linh vật sống (Verdant Branch)

> Premium painterly-anime weapon splash for a high-end xianxia game: lush, graceful, deeply ornamental and alive with spiritual growth, like a treasured wood-element fabao cultivated for centuries beneath an immortal tree. The presentation is rich and luxurious, with floating leaves, pollen motes, jade-green light and a halo of branching spirit lines behind the weapon.
>
> Verdant Branch, an original Chinese wood jian, is long, elegant and slightly slender, its blade formed from dark polished spiritual wood sleeved in translucent celadon-jade edges, so the weapon reads as both living timber and precious artefact. Fine growth-ring striations, pale sap-gold vein lines and tiny leaf-like inlays run through the blade body; the central ridge glows softly with green qi, as if the sword still carries the pulse of a sacred tree.
>
> Its guard is a layered blossom-and-vine composition: white jade petals, pale gold vine filigree, and curling branch arms that cradle the blade root like an opening flower. The grip is wrapped in moss-green silk over lacquered wood, with elegant gold collars. The pommel is a carved jade seedpod with hanging bead chains, twin leaf pendants and a long green-and-cream silk ribbon.
>
> Luxurious botanical detail, living materials, soft sacred radiance, unmistakable immortal-cultivation beauty. No text or letters.

### 4. Cảnh giới thần thoại (Winter Vein)

> Mythic 5-star weapon reveal splash for a premium anime xianxia game: radiant moonlit spectacle, crystalline precision, luxurious ornament and a vast celestial environment worthy of an immortal ice treasure. A full moon, frozen lake, distant snow peaks, drifting ice motes and a delicate star-array of frost sigils surround the weapon, while the sword remains the brightest focal point.
>
> Winter Vein, an original Chinese ice jian, crosses the frame on a majestic diagonal. The blade is long and slender, built from a luminous frost-crystal core contained within a bright silver lattice frame. Inside the crystal, layered internal facets, snow-vein fractures and branching dendritic patterns catch blue-white light like frozen spirit channels. The edges are clean, sharp and intensely polished.
>
> Its guard is richly mounted rather than minimal: a snow-lotus composition of silver petals, translucent crystal lobes and pale blue gemstones arranged around the blade root, with small projecting crystal leaves and fine frost filigree. The grip is white silk over pale silver with icy-blue braid accents; the pommel is a faceted moon-crystal enclosed in a silver cage, with short white silk cords and crystal bead drops.
>
> Lavish detail, expensive materials, crisp highlights, cold aura, celestial nobility. No text or letters.

### 5. Lò rèn thần (Ember Crest)

> Cinematic featured-weapon banner for a premium xianxia action game: fierce, luxurious and unforgettable, with the splendour of an immortal forge at full awakening. The background is near-black with a blazing furnace halo, heat ripples, sparks, ember smoke and hints of molten bronze architecture, while the weapon remains perfectly readable and richly crafted.
>
> Ember Crest, an original Chinese fire dao, sweeps through the frame in a powerful curve. The blade is broad yet elegant, forged from blackened meteoric steel with polished silver edges and a bright internal fire seam flowing just behind the edge, white-hot at its heart and fading through molten gold, orange and deep crimson into the darker spine. Subtle furnace-crack patterns and flowing flame-cloud engravings enrich the blade without breaking its solid silhouette.
>
> Its guard is a lavish furnace-gate composition: layered red-gold and dark bronze stepped frames, curling flame-ruyi brackets, recessed ember channels and a glowing red gem set at the centre. The grip is wrapped in dark crimson silk with bronze wire crossings. The pommel is a heavy faceted forge-seal with a caged ember jewel, trailing a crimson-black tassel and bead chain.
>
> Expensive metals, hard specular highlights, contained fire, Chinese ornamental authority, premium market-level rendering. No text or letters.

