# Tu Tiên Thủ Ải — M0b · 06. Chân dung cả danh sách nhân vật (25/10/2026)

> **Phiếu 009**, chạy sau Phiếu 008. Nguồn: [canon](../../00-canon.md) §3 (D03, D47, D48, D49), §11–12 và bản sắc sơn thủy huyền ảo chất Việt. [Giao nhận và nhận xét](../../../../../games/immortality-cultivation/art-src/README-roster.md). Chỉ tạo concept chân dung để anh duyệt; ảnh nguồn 3D làm sau khi được duyệt.

**Đã giao:** chín chân dung mới 1024×1536, bản sao nguyên nữ Kiếm tu A 1024×1536 và ảnh đội hình 2172×724; mỗi PNG có prompt cạnh ảnh. Đội hình đủ mười người và hai linh thú nhỏ, dùng năm ảnh đại diện do giới hạn công cụ; chi tiết mặt và phụ kiện có lệch so với chân dung riêng. Không tạo lại ảnh nào; xem README giao nhận để chọn hoặc sửa.

## 1. Khóa phong cách và phạm vi

- Mỗi trường phái có một nam và một nữ theo yêu cầu phiếu: Kiếm, Thổ thể thuộc MVP; Phù, Hỏa, Ngự thú sau MVP. Đây là danh sách ngoại hình, không đặt sức mạnh khác nhau giữa nam và nữ. Bot Đạo Đồng ở ngoài danh sách mười nhân vật của phiếu.
- **Chuẩn Phiếu 008:** bản A có miện nhỏ, `identity/kiem-tu-portrait.png`. Chủ dự án **đã duyệt ngày 25/10** (canon D47): đây là chuẩn phong cách chung. Codex viết phiếu này trước khi biết, nên câu hỏi "A hay B" trong README giao nhận đã có lời đáp là A. Nữ Kiếm tu sao chép nguyên PNG và prompt sang `roster/kiem-nu.*`, không tạo lại.
- Tên tạm dùng cách gọi của canon và thêm nam/nữ; chưa đặt tên riêng hoặc thân thế. Kiếm = Kim, Thổ thể = Thổ, Phù = Hỏa đã chốt ở §11. **Hỏa = Hỏa, Ngự thú = Mộc là đề xuất mỹ thuật** cho phiếu này vì canon chưa chốt hệ hai phái ấy; không sửa luật hoặc canon. D49 trong canon còn ghi chờ xác nhận, phiếu hiện tại cho phép tạo đủ concept để duyệt.
- Cùng gia đình phục sức quý phái D47: lụa nhiều lớp lấy cấu trúc áo ngũ thân làm gợi ý, cổ kín, viền thêu, ngọc bội, miện thấp hoặc trâm; nam vương giả, nữ thanh tú quý phái. Tất cả kín đáo, hợp mọi lứa tuổi, nhân vật và phục sức gốc của dự án.
- Giữ khối phong cách của `00-identity.md`: khối hình 3D cách điệu, chuyển sắc thủy mặc, chất giấy dó, đá vôi, sương chàm, tùng thưa; ánh sáng ngày dịu, vàng cổ nhạt chỉ ở thêu và kim loại mờ. Màu hệ nằm ở vật liệu, không giả màu cảnh báo hoặc hiệu ứng gameplay.
- Chân dung là cận nhân vật nên không áp góc toàn sân D48; không dùng các ảnh này để kết luận khung camera hoặc hiệu năng D03 đã đạt.
- Chín ảnh mới, một bản sao nữ Kiếm tu và một ảnh đội hình. Mỗi ảnh hỏng rõ chỉ tạo lại tối đa một lần; bản thử nếu có giữ kèm prompt riêng. Mỗi PNG giữ một prompt nguyên văn `<tên>.prompt.txt` cạnh ảnh. Dùng image_gen tích hợp, mỗi chân dung một lượt gọi riêng.

## 2. Danh mục

Đường dẫn trong bảng tính từ `games/immortality-cultivation/art-src/roster/`. Bảng màu là hướng mỹ thuật, không phải khóa màu dữ liệu runtime.

| Mã | Tên tạm | Trường phái · hệ | Mốc | Bảng màu | PNG |
|---|---|---|---|---|---|
| DS01 | Kiếm tu nam | Kiếm · Kim (canon §11) | M1 | Trắng ngọc, lam sẫm, bạc mờ, vàng cổ nhạt | `kiem-nam.png` |
| DS02 | Kiếm tu nữ | Kiếm · Kim (canon §11) | M0a | Trắng ngọc, lam sẫm, vàng cổ nhạt | `kiem-nu.png` |
| DS03 | Thổ thể tu nam | Thổ thể · Thổ (canon §11) | M1 | Nâu đất, ngọc hoàng thổ, ngà, chàm than | `tho-the-nam.png` |
| DS04 | Thổ thể tu nữ | Thổ thể · Thổ (canon §11) | M1 | Ngà, nâu trà, ngọc hoàng thổ, chàm than | `tho-the-nu.png` |
| DS05 | Phù tu nam | Phù · Hỏa (canon §11) | Sau MVP | Mực chàm, giấy ngà, đồng nâu, hổ phách trầm | `phu-nam.png` |
| DS06 | Phù tu nữ | Phù · Hỏa (canon §11) | Sau MVP | Giấy ngà, chàm mực, nâu mận, hổ phách trầm | `phu-nu.png` |
| DS07 | Hỏa tu nam | Hỏa · Hỏa (đề xuất mỹ thuật; canon chưa chốt) | Sau MVP | Nâu đồng, nâu mận, ngà, than tím | `hoa-nam.png` |
| DS08 | Hỏa tu nữ | Hỏa · Hỏa (đề xuất mỹ thuật; canon chưa chốt) | Sau MVP | Ngà, nâu mận, đồng hồng trầm, ngọc hổ phách | `hoa-nu.png` |
| DS09 | Ngự thú tu nam | Ngự thú · Mộc (đề xuất mỹ thuật; canon chưa chốt) | Sau MVP | Lục rêu, ngà, chàm than, ngọc lục xám | `ngu-thu-nam.png` |
| DS10 | Ngự thú tu nữ | Ngự thú · Mộc (đề xuất mỹ thuật; canon chưa chốt) | Sau MVP | Ngà, lục trà, lam suối xám, ngọc lục xám | `ngu-thu-nu.png` |

## 3. Prompt nguyên văn từng chân dung

Mỗi khối dưới là toàn bộ prompt, không phải ghép thêm khối chung. Với chín ảnh mới, đính kèm bản A của Phiếu 008 làm **tham chiếu phong cách**; không dùng mặt nữ Kiếm tu làm mặt cho mọi người.

### DS01 · Kiếm tu nam

**File:** `roster/kiem-nam.png` · **Prompt cạnh ảnh:** `roster/kiem-nam.prompt.txt`.

**Thiết kế:** Nam khoảng 28 tuổi, mặt dài góc cạnh, tóc búi cao gọn; áo lam khoác trên lụa trắng, miện thấp, ngọc bội dài. Kiếm Thanh Phong trong bao lam.

**Đính kèm:** `identity/kiem-tu-portrait.png` — phong cách, không khóa nhận dạng nhân vật.

```text
Use case: stylized-concept.
Asset type: Kiếm tu nam roster concept portrait for the original Vietnamese fantasy game Tu Tien Thu Ai; visual concept for owner review.
Input image 1: the attached Ticket 008 female sword-cultivator portrait A is a style reference only. Create the new character described below, retaining the shared art family rather than copying her face or sword costume.
Primary request: a handsome Vietnamese man sword cultivator, about 28, with an angular oval face, defined jaw, straight dark brows, warm dark eyes and an upright, calm princely bearing. His face is masculine and distinct from the reference woman.
Costume: deep-indigo layered silk outer robes inspired by the structure of Vietnamese ao ngu than over broad pearl-white inner panels, a fully closed high collar, neat long sleeves, silver-grey woven cloud-and-crane borders and restrained pale antique-gold stitching. A broad dark-indigo belt holds one elongated white-jade pendant. Smooth black hair in a compact high topknot secured by a low white-jade and pale-gold coronet. Regal masculine tailoring, balanced shoulders, graceful practical proportions.
Signature implement: one physical Thanh Phong sword in a deep-indigo lacquer scabbard at his left hip, straight refined guard, white-jade pommel and pale-gold cloud fittings; his left hand rests naturally on the upper scabbard, his right hand relaxed by the belt. The sword is clearly distinct from a staff.
Color palette: pearl white, deep indigo, silver grey, ink charcoal and restrained pale antique gold.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, one sparse old pine and soft indigo mist remain subordinate to the character.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty. Match the attached portrait's finish, face rendering, silk, embroidery, jade, daylight and noble bearing.
Composition: one upright adult character, head to upper thighs, gentle three-quarter body angle, gaze towards viewer, face large enough to judge, complete head ornament with breathing room, both hands and the signature implement readable.
Lighting: soft broad daylight, quiet dignified mood. Opaque natural jade, muted antique-metal embroidery and matte crafted objects. Colors belong to physical fabric and material.
Constraints: original character and original costume for this project; fully clothed in opaque layers with closed collar, covered chest, shoulders and legs, all-ages dignity. One character, one view, clean natural anatomy, five fingers per visible hand. No text, readable letters, numbers, UI, logo, watermark or frame. No cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No copied game character, costume or emblem. No aura, floating ornaments or bright magical effect. Gold is pale antique embroidery, never bright reward-yellow; avoid enemy-warning red #FF4A4A, urgency orange #FFB020 and typing cyan #7FF5E0.
Output: one portrait PNG, 1024x1536.
```

### DS02 · Kiếm tu nữ

**File:** `roster/kiem-nu.png` · **Prompt cạnh ảnh:** `roster/kiem-nu.prompt.txt`.

**Dùng lại:** sao chép nguyên `identity/kiem-tu-portrait.png` và prompt gốc; lụa trắng ngọc, lam sẫm, thêu mây–hạc, miện ngọc thấp, ngọc bội tròn, kiếm Thanh Phong. Không gửi thêm lượt tạo ảnh.

```text
Use case: stylized-concept.
Asset type: royal sword-cultivator identity portrait, option A, for the original Vietnamese fantasy game Tu Tien Thu Ai.
Primary request: a strikingly beautiful young adult Vietnamese woman sword cultivator, about 24, with delicate harmonious facial features, dark almond eyes, luminous natural skin and a calm noble gaze. She stands very upright, shoulders relaxed, head held with the composed dignity of a royal heir.
Costume A: pearl-white layered silk robes inspired by the structure of Vietnamese ao ngu than, a fully closed high inner collar, long fitted inner sleeves, deep-indigo outer shoulder and side panels, a wide indigo silk waist belt, fine pale antique-gold embroidered borders and elegant large cloud-and-crane motifs. A compact low royal diadem of pale gold and white jade sits above a smooth black updo; one substantial white-jade pendant hangs neatly at the waist. Refined royal craftsmanship, restrained and graceful.
Sword: the Thanh Phong sword of a royal cultivator rests vertically at her side in a deep-indigo lacquer scabbard with pale-gold cloud fittings, a white-jade pommel and a dignified straight guard; her relaxed hand rests near its hilt. The sword is a physical crafted object.
Composition: one upright character, head to just below hips, face large enough to judge beauty and nobility, crown, collar, waist pendant and sword hilt all visible, gentle three-quarter body angle, gaze towards viewer.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, a sparse old pine and soft indigo mist stay subordinate to the woman.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty.
Lighting and palette: soft broad daylight, pearl white, deep indigo, ink charcoal, limestone grey, restrained pale antique gold and opaque white jade. Gold is muted embroidery, never bright reward-yellow or emissive.
Constraints: fully clothed, opaque layered silk covering chest, shoulders and legs; dignified all-ages presentation. One original character, one view, no text, letters, numbers, UI, logo, watermark or frame; no cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No aura, floating ornament or bright magical effect.
Output: one portrait PNG, 1024x1536.
```

### DS03 · Thổ thể tu nam

**File:** `roster/tho-the-nam.png` · **Prompt cạnh ảnh:** `roster/tho-the-nam.prompt.txt`.

**Thiết kế:** Nam khoảng 34 tuổi, vai rộng, mặt vuông, da nâu ấm; áo chiến lụa nhiều lớp, giáp ngọc khối vuông, găng đá–ngọc, miện thấp.

**Đính kèm:** `identity/kiem-tu-portrait.png` — phong cách, không khóa nhận dạng nhân vật.

```text
Use case: stylized-concept.
Asset type: Thổ thể tu nam roster concept portrait for the original Vietnamese fantasy game Tu Tien Thu Ai; visual concept for owner review.
Input image 1: the attached Ticket 008 female sword-cultivator portrait A is a style reference only. Create the new character described below, retaining the shared art family rather than copying her face or sword costume.
Primary request: a Vietnamese man earth-body cultivator, about 34, broad-shouldered with believable strong proportions, a square face, warm brown skin, a clean-shaven jaw and steady protective eyes. He carries the composed nobility of a royal guardian.
Costume: layered warm-earth-brown and ivory silk robes inspired by Vietnamese ao ngu than, a closed high collar, fitted inner sleeves and structured outer shoulder panels. Smooth opaque ochre-jade armor plates cover the shoulders and upper chest in a clear square-block rhythm, inset with restrained pale antique-gold mountain-contour engraving; the silk remains visible between plates. A wide charcoal-indigo belt bears one square earth-jade pendant. Black hair in a compact topknot under a low square jade coronet.
Signature implement: two articulated earth-jade and carved-stone gauntlets with readable squared knuckle plates and normal human hands inside. Both closed relaxed fists are held separately near the waist, the left slightly higher, so the gauntlets and armor read as his school identity.
Color palette: warm earth brown, opaque ochre jade, ivory, charcoal indigo and muted antique gold.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, one sparse old pine and soft indigo mist remain subordinate to the character.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty. Match the attached portrait's finish, face rendering, silk, embroidery, jade, daylight and noble bearing.
Composition: one upright adult character, head to upper thighs, gentle three-quarter body angle, gaze towards viewer, face large enough to judge, complete head ornament with breathing room, both hands and the signature implement readable.
Lighting: soft broad daylight, quiet dignified mood. Opaque natural jade, muted antique-metal embroidery and matte crafted objects. Colors belong to physical fabric and material.
Constraints: original character and original costume for this project; fully clothed in opaque layers with closed collar, covered chest, shoulders and legs, all-ages dignity. One character, one view, clean natural anatomy, five fingers per visible hand. No text, readable letters, numbers, UI, logo, watermark or frame. No cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No copied game character, costume or emblem. No aura, floating ornaments or bright magical effect. Gold is pale antique embroidery, never bright reward-yellow; avoid enemy-warning red #FF4A4A, urgency orange #FFB020 and typing cyan #7FF5E0.
Output: one portrait PNG, 1024x1536.
```

### DS04 · Thổ thể tu nữ

**File:** `roster/tho-the-nu.png` · **Prompt cạnh ảnh:** `roster/tho-the-nu.prompt.txt`.

**Thiết kế:** Nữ khoảng 29 tuổi, mặt vuông mềm, dáng vững; lụa ngà viền địa tầng, giáp ngọc thổ, trâm núi, trượng đá vuông.

**Đính kèm:** `identity/kiem-tu-portrait.png` — phong cách, không khóa nhận dạng nhân vật.

```text
Use case: stylized-concept.
Asset type: Thổ thể tu nữ roster concept portrait for the original Vietnamese fantasy game Tu Tien Thu Ai; visual concept for owner review.
Input image 1: the attached Ticket 008 female sword-cultivator portrait A is a style reference only. Create the new character described below, retaining the shared art family rather than copying her face or sword costume.
Primary request: a refined Vietnamese woman earth-body cultivator, about 29, with a softly squared face, warm medium skin, dark steady eyes and a strong upright stance. Elegant noble protector, physically capable with natural adult proportions.
Costume: ivory layered silk robes inspired by Vietnamese ao ngu than with tea-brown overlapping outer panels, a fully closed high collar and neat long sleeves. Opaque ochre-jade shoulder guards and a small fitted earth-jade breastplate over the fully covering silk carry broad square mountain-strata embroidery in muted pale antique gold. A charcoal-indigo sash holds a square earth-jade pendant. Smooth black hair in a low braided bun with one substantial jade mountain-shaped hairpin and a restrained pale-gold mounting.
Signature implement: one upright carved grey-brown stone staff at her right side, its top a compact solid square earth-jade block with engraved mountain strata, visible from the head of the staff down beyond the waist. Her right hand grips the shaft naturally at waist level and her left rests openly against the belt. A short stone-jade bracer reinforces the free wrist.
Color palette: ivory, tea brown, opaque ochre jade, charcoal indigo and pale antique gold.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, one sparse old pine and soft indigo mist remain subordinate to the character.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty. Match the attached portrait's finish, face rendering, silk, embroidery, jade, daylight and noble bearing.
Composition: one upright adult character, head to upper thighs, gentle three-quarter body angle, gaze towards viewer, face large enough to judge, complete head ornament with breathing room, both hands and the signature implement readable.
Lighting: soft broad daylight, quiet dignified mood. Opaque natural jade, muted antique-metal embroidery and matte crafted objects. Colors belong to physical fabric and material.
Constraints: original character and original costume for this project; fully clothed in opaque layers with closed collar, covered chest, shoulders and legs, all-ages dignity. One character, one view, clean natural anatomy, five fingers per visible hand. No text, readable letters, numbers, UI, logo, watermark or frame. No cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No copied game character, costume or emblem. No aura, floating ornaments or bright magical effect. Gold is pale antique embroidery, never bright reward-yellow; avoid enemy-warning red #FF4A4A, urgency orange #FFB020 and typing cyan #7FF5E0.
Output: one portrait PNG, 1024x1536.
```

### DS05 · Phù tu nam

**File:** `roster/phu-nam.png` · **Prompt cạnh ảnh:** `roster/phu-nam.prompt.txt`.

**Thiết kế:** Nam khoảng 31 tuổi, mặt hẹp, mắt trầm; lụa mực–ngà, miện ngọc chữ nhật, bút lớn và phù lục có nét trừu tượng.

**Đính kèm:** `identity/kiem-tu-portrait.png` — phong cách, không khóa nhận dạng nhân vật.

```text
Use case: stylized-concept.
Asset type: Phù tu nam roster concept portrait for the original Vietnamese fantasy game Tu Tien Thu Ai; visual concept for owner review.
Input image 1: the attached Ticket 008 female sword-cultivator portrait A is a style reference only. Create the new character described below, retaining the shared art family rather than copying her face or sword costume.
Primary request: a Vietnamese man talisman cultivator, about 31, with a slender rectangular face, thoughtful dark eyes, clean-shaven features and quiet royal-scholar dignity. His mature face is distinct from the sword man.
Costume: ink-indigo layered silk robes inspired by Vietnamese ao ngu than, broad parchment-ivory overlapping lapels, a closed high inner collar, long neat sleeves with pale-gold embroidered geometric scroll borders and muted amber-brown knotwork. A dark belt holds a rectangular ivory-jade pendant and a neat closed scroll case. Smooth black hair in a high compact scholar's knot secured by a low rectangular white-jade coronet with antique-bronze fittings.
Signature implement: one substantial physical calligraphy brush with an ivory-jade grip, dark wood shaft and pointed black bristles, held diagonally in his right hand at chest level. His left hand supports a small rigid folded ivory-paper talisman booklet at waist height. A few broad abstract burnt-umber marks imply talisman work without readable script, letters or real-world sacred symbols. The brush and paper are clearly separate objects; no sword, fan or flames.
Color palette: ink indigo, parchment ivory, antique bronze, muted amber brown and restrained pale antique gold. The school's canonical Fire element is suggested by warm amber talisman materials, not red UI color.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, one sparse old pine and soft indigo mist remain subordinate to the character.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty. Match the attached portrait's finish, face rendering, silk, embroidery, jade, daylight and noble bearing.
Composition: one upright adult character, head to upper thighs, gentle three-quarter body angle, gaze towards viewer, face large enough to judge, complete head ornament with breathing room, both hands and the signature implement readable.
Lighting: soft broad daylight, quiet dignified mood. Opaque natural jade, muted antique-metal embroidery and matte crafted objects. Colors belong to physical fabric and material.
Constraints: original character and original costume for this project; fully clothed in opaque layers with closed collar, covered chest, shoulders and legs, all-ages dignity. One character, one view, clean natural anatomy, five fingers per visible hand. No text, readable letters, numbers, UI, logo, watermark or frame. No cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No copied game character, costume or emblem. No aura, floating ornaments or bright magical effect. Gold is pale antique embroidery, never bright reward-yellow; avoid enemy-warning red #FF4A4A, urgency orange #FFB020 and typing cyan #7FF5E0.
Output: one portrait PNG, 1024x1536.
```

### DS06 · Phù tu nữ

**File:** `roster/phu-nu.png` · **Prompt cạnh ảnh:** `roster/phu-nu.prompt.txt`.

**Thiết kế:** Nữ khoảng 27 tuổi, mặt trái xoan dài; lụa ngà nẹp chàm, trâm cuộn thư, bút nhỏ và lá phù giấy ngà.

**Đính kèm:** `identity/kiem-tu-portrait.png` — phong cách, không khóa nhận dạng nhân vật.

```text
Use case: stylized-concept.
Asset type: Phù tu nữ roster concept portrait for the original Vietnamese fantasy game Tu Tien Thu Ai; visual concept for owner review.
Input image 1: the attached Ticket 008 female sword-cultivator portrait A is a style reference only. Create the new character described below, retaining the shared art family rather than copying her face or sword costume.
Primary request: a refined Vietnamese woman talisman cultivator, about 27, with an elongated oval face, expressive dark brows, warm dark eyes and a composed noble-scholar gaze. Her face and hairstyle are distinct from the reference sword woman.
Costume: parchment-ivory layered silk robes inspired by Vietnamese ao ngu than, broad ink-indigo front edging, muted plum-brown side panels, a fully closed high collar, long sleeves with close cuffs and fine pale antique-gold embroidered scroll-knot borders. A dark-indigo silk belt holds a rectangular white-jade pendant. Black hair in a smooth low coiled bun, secured with a substantial white-jade rolled-scroll hairpin in an antique-bronze mounting.
Signature implement: one physical dark-wood calligraphy brush with a white-jade grip in her right hand held at a relaxed diagonal, its pointed black bristles clearly visible. Her left hand holds two broad ivory-paper talisman slips separately at chest height, each with a few abstract burnt-umber ink strokes, decorative and nonlinguistic, without readable letters or real-world sacred symbols. Brush, fingers and slips are distinct; no sword, fan or flames.
Color palette: parchment ivory, ink indigo, muted plum brown, warm amber accents and pale antique gold. The canonical Fire element is suggested by warm talisman materials.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, one sparse old pine and soft indigo mist remain subordinate to the character.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty. Match the attached portrait's finish, face rendering, silk, embroidery, jade, daylight and noble bearing.
Composition: one upright adult character, head to upper thighs, gentle three-quarter body angle, gaze towards viewer, face large enough to judge, complete head ornament with breathing room, both hands and the signature implement readable.
Lighting: soft broad daylight, quiet dignified mood. Opaque natural jade, muted antique-metal embroidery and matte crafted objects. Colors belong to physical fabric and material.
Constraints: original character and original costume for this project; fully clothed in opaque layers with closed collar, covered chest, shoulders and legs, all-ages dignity. One character, one view, clean natural anatomy, five fingers per visible hand. No text, readable letters, numbers, UI, logo, watermark or frame. No cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No copied game character, costume or emblem. No aura, floating ornaments or bright magical effect. Gold is pale antique embroidery, never bright reward-yellow; avoid enemy-warning red #FF4A4A, urgency orange #FFB020 and typing cyan #7FF5E0.
Output: one portrait PNG, 1024x1536.
```

### DS07 · Hỏa tu nam

**File:** `roster/hoa-nam.png` · **Prompt cạnh ảnh:** `roster/hoa-nam.prompt.txt`.

**Thiết kế:** Nam khoảng 30 tuổi, gò má rõ; áo nâu đồng–ngà, viền đường lửa, miện thấp; quạt xếp có họa tiết lửa khắc.

**Đính kèm:** `identity/kiem-tu-portrait.png` — phong cách, không khóa nhận dạng nhân vật.

```text
Use case: stylized-concept.
Asset type: Hỏa tu nam roster concept portrait for the original Vietnamese fantasy game Tu Tien Thu Ai; visual concept for owner review.
Input image 1: the attached Ticket 008 female sword-cultivator portrait A is a style reference only. Create the new character described below, retaining the shared art family rather than copying her face or sword costume.
Primary request: a Vietnamese man fire cultivator, about 30, with pronounced cheekbones, warm tan skin, a clean-shaven face and calm confident dark eyes. Upright princely presence, distinct from the sword and earth men.
Costume: layered copper-brown and muted plum-brown silk robes inspired by Vietnamese ao ngu than, ivory inner overlapping front panels, a fully closed high collar, neat long sleeves and broad pale antique-gold embroidery in a clear upward flame-scroll rhythm. A charcoal-plum belt holds a rounded opaque smoky-amber jade pendant. Black hair in a neat high topknot secured by a low ivory-jade coronet with a simple rising-flame silhouette in muted bronze.
Signature implement: one broad half-open folding fan held in his right hand at chest level, ivory silk leaves with muted copper-brown flame-scroll embroidery and sturdy antique-bronze ribs. His left hand rests naturally at the belt. The flame identity is crafted into the fan and collar; the fan is a solid physical object with no emitted fire, sparks or halo.
Color palette: copper brown, muted plum brown, ivory, charcoal plum and pale antique gold. Suggest Fire through physical warm materials and flame-shaped craftsmanship, keeping cloth away from bright red, warning orange and reward yellow.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, one sparse old pine and soft indigo mist remain subordinate to the character.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty. Match the attached portrait's finish, face rendering, silk, embroidery, jade, daylight and noble bearing.
Composition: one upright adult character, head to upper thighs, gentle three-quarter body angle, gaze towards viewer, face large enough to judge, complete head ornament with breathing room, both hands and the signature implement readable.
Lighting: soft broad daylight, quiet dignified mood. Opaque natural jade, muted antique-metal embroidery and matte crafted objects. Colors belong to physical fabric and material.
Constraints: original character and original costume for this project; fully clothed in opaque layers with closed collar, covered chest, shoulders and legs, all-ages dignity. One character, one view, clean natural anatomy, five fingers per visible hand. No text, readable letters, numbers, UI, logo, watermark or frame. No cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No copied game character, costume or emblem. No aura, floating ornaments or bright magical effect. Gold is pale antique embroidery, never bright reward-yellow; avoid enemy-warning red #FF4A4A, urgency orange #FFB020 and typing cyan #7FF5E0.
Output: one portrait PNG, 1024x1536.
```

### DS08 · Hỏa tu nữ

**File:** `roster/hoa-nu.png` · **Prompt cạnh ảnh:** `roster/hoa-nu.prompt.txt`.

**Thiết kế:** Nữ khoảng 28 tuổi, mặt trái tim, mắt kiên định; áo ngà–nâu mận, trâm lửa cách điệu; ấn lửa bằng ngọc hổ phách.

**Đính kèm:** `identity/kiem-tu-portrait.png` — phong cách, không khóa nhận dạng nhân vật.

```text
Use case: stylized-concept.
Asset type: Hỏa tu nữ roster concept portrait for the original Vietnamese fantasy game Tu Tien Thu Ai; visual concept for owner review.
Input image 1: the attached Ticket 008 female sword-cultivator portrait A is a style reference only. Create the new character described below, retaining the shared art family rather than copying her face or sword costume.
Primary request: a beautiful refined Vietnamese woman fire cultivator, about 28, with a heart-shaped face, softly defined cheekbones, warm natural skin and a serene determined gaze. Upright royal dignity, visibly distinct from the sword woman.
Costume: layered ivory and muted plum-brown silk robes inspired by Vietnamese ao ngu than with broad subdued rose-copper outer shoulder panels, a fully closed high collar, fitted long inner sleeves and pale antique-gold embroidered flame-scroll borders. A dark plum silk sash holds a rounded smoky-amber jade pendant. Black hair in a compact swept-back bun secured by a sculpted ivory-jade rising-flame hairpin with muted copper fittings.
Signature implement: one palm-sized physical fire seal made of opaque smoky-amber jade, its solid handle carved as three upward flame petals on a squat square base. She supports its base on her left open palm at waist height while her right hand steadies its side naturally. The seal is an inert crafted object with rounded readable facets, without lettering, emitted flames, sparks or glow.
Color palette: ivory, muted plum brown, subdued rose copper, opaque smoky amber and pale antique gold. Fire is conveyed by shape and material, avoiding bright signal red, orange and yellow.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, one sparse old pine and soft indigo mist remain subordinate to the character.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty. Match the attached portrait's finish, face rendering, silk, embroidery, jade, daylight and noble bearing.
Composition: one upright adult character, head to upper thighs, gentle three-quarter body angle, gaze towards viewer, face large enough to judge, complete head ornament with breathing room, both hands and the signature implement readable.
Lighting: soft broad daylight, quiet dignified mood. Opaque natural jade, muted antique-metal embroidery and matte crafted objects. Colors belong to physical fabric and material.
Constraints: original character and original costume for this project; fully clothed in opaque layers with closed collar, covered chest, shoulders and legs, all-ages dignity. One character, one view, clean natural anatomy, five fingers per visible hand. No text, readable letters, numbers, UI, logo, watermark or frame. No cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No copied game character, costume or emblem. No aura, floating ornaments or bright magical effect. Gold is pale antique embroidery, never bright reward-yellow; avoid enemy-warning red #FF4A4A, urgency orange #FFB020 and typing cyan #7FF5E0.
Output: one portrait PNG, 1024x1536.
```

### DS09 · Ngự thú tu nam

**File:** `roster/ngu-thu-nam.png` · **Prompt cạnh ảnh:** `roster/ngu-thu-nam.prompt.txt`.

**Thiết kế:** Nam khoảng 26 tuổi, nét cởi mở; lụa lục rêu viền lá, miện ngọc; sáo trúc và linh lộc nhỏ.

**Đính kèm:** `identity/kiem-tu-portrait.png` — phong cách, không khóa nhận dạng nhân vật.

```text
Use case: stylized-concept.
Asset type: Ngự thú tu nam roster concept portrait for the original Vietnamese fantasy game Tu Tien Thu Ai; visual concept for owner review.
Input image 1: the attached Ticket 008 female sword-cultivator portrait A is a style reference only. Create the new character described below, retaining the shared art family rather than copying her face or sword costume.
Primary request: a Vietnamese man beast-taming cultivator, about 26, with a broad oval face, warm dark eyes, medium warm skin and a gentle confident smile. Refined princely bearing, adult natural proportions.
Costume: moss-green layered silk robes inspired by Vietnamese ao ngu than over ivory inner panels, a fully closed high collar, long neat sleeves, charcoal-indigo belt and broad pale antique-gold leaf-and-river embroidery. One opaque grey-green jade leaf pendant sits at the waist. Black hair in a low half-tied topknot secured by a compact grey-green jade coronet with muted bronze leaf fittings.
Signature implement: one physical bamboo transverse flute with visible finger holes, held diagonally across his waist in his right hand, clearly separate from his body. A single small friendly spirit deer, knee-high with a soft ivory coat, warm brown eyes and two short unbranched moss-green antler buds, stands beside his left hip on a low limestone ledge. Its whole head, four legs and hooves are visible; his left hand rests gently on its upper back. It is one complete small companion with natural quadruped anatomy and no glow.
Color palette: moss green, ivory, charcoal indigo, opaque grey-green jade and muted pale antique gold. Wood is a proposed art direction rather than a finalized gameplay element.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, one sparse old pine and soft indigo mist remain subordinate to the character.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty. Match the attached portrait's finish, face rendering, silk, embroidery, jade, daylight and noble bearing.
Composition: one upright adult character, head to upper thighs, gentle three-quarter body angle, gaze towards viewer, face large enough to judge, complete head ornament with breathing room, both hands and the signature implement readable.
Lighting: soft broad daylight, quiet dignified mood. Opaque natural jade, muted antique-metal embroidery and matte crafted objects. Colors belong to physical fabric and material.
Constraints: original character and original costume for this project; fully clothed in opaque layers with closed collar, covered chest, shoulders and legs, all-ages dignity. One character, one view, clean natural anatomy, five fingers per visible hand. No text, readable letters, numbers, UI, logo, watermark or frame. No cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No copied game character, costume or emblem. No aura, floating ornaments or bright magical effect. Gold is pale antique embroidery, never bright reward-yellow; avoid enemy-warning red #FF4A4A, urgency orange #FFB020 and typing cyan #7FF5E0.
Output: one portrait PNG, 1024x1536.
```

### DS10 · Ngự thú tu nữ

**File:** `roster/ngu-thu-nu.png` · **Prompt cạnh ảnh:** `roster/ngu-thu-nu.prompt.txt`.

**Thiết kế:** Nữ khoảng 25 tuổi, mặt tròn trái xoan, mắt dịu; lụa ngà–lục trà, trâm lá; sáo ngọc và linh cáo nhỏ.

**Đính kèm:** `identity/kiem-tu-portrait.png` — phong cách, không khóa nhận dạng nhân vật.

```text
Use case: stylized-concept.
Asset type: Ngự thú tu nữ roster concept portrait for the original Vietnamese fantasy game Tu Tien Thu Ai; visual concept for owner review.
Input image 1: the attached Ticket 008 female sword-cultivator portrait A is a style reference only. Create the new character described below, retaining the shared art family rather than copying her face or sword costume.
Primary request: a refined Vietnamese woman beast-taming cultivator, about 25, with a softly rounded oval face, warm medium skin, bright gentle dark eyes and a quiet reassuring smile. Noble graceful bearing, adult natural proportions, distinct from the reference sword woman.
Costume: ivory layered silk robes inspired by Vietnamese ao ngu than with tea-green outer panels, a fully closed high collar, long neat sleeves and subtle grey stream-blue cuffs. Broad pale antique-gold leaf-and-river embroidery follows the panel edges. A deep moss sash holds one opaque grey-green leaf-shaped jade pendant. Black hair in a smooth low braided bun secured by a substantial grey-green jade leaf hairpin with an antique-bronze setting.
Signature implement: one physical opaque pale-green jade transverse flute with visible finger holes, held diagonally across the waist in her right hand. A single small friendly spirit fox with an ivory coat, soft grey-green ear tips, warm brown eyes, four natural legs and exactly one full fluffy tail sits beside her left hip on a low limestone ledge. Its whole head, paws and tail remain visible; her left hand rests gently on its upper back. One complete small companion, no glow or extra limbs.
Color palette: ivory, tea green, grey stream blue, deep moss and opaque grey-green jade with pale antique gold. Wood is a proposed art direction rather than a finalized gameplay element.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, one sparse old pine and soft indigo mist remain subordinate to the character.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty. Match the attached portrait's finish, face rendering, silk, embroidery, jade, daylight and noble bearing.
Composition: one upright adult character, head to upper thighs, gentle three-quarter body angle, gaze towards viewer, face large enough to judge, complete head ornament with breathing room, both hands and the signature implement readable.
Lighting: soft broad daylight, quiet dignified mood. Opaque natural jade, muted antique-metal embroidery and matte crafted objects. Colors belong to physical fabric and material.
Constraints: original character and original costume for this project; fully clothed in opaque layers with closed collar, covered chest, shoulders and legs, all-ages dignity. One character, one view, clean natural anatomy, five fingers per visible hand. No text, readable letters, numbers, UI, logo, watermark or frame. No cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No copied game character, costume or emblem. No aura, floating ornaments or bright magical effect. Gold is pale antique embroidery, never bright reward-yellow; avoid enemy-warning red #FF4A4A, urgency orange #FFB020 and typing cyan #7FF5E0.
Output: one portrait PNG, 1024x1536.
```

## 4. Ảnh đội hình

**File:** `roster/doi-hinh.png` · **Prompt cạnh ảnh:** `roster/doi-hinh.prompt.txt`.

Đính kèm năm ảnh đại diện vì image_gen chỉ nhận tối đa năm đường dẫn: nữ Kiếm, nam Thổ thể, nam Phù, nữ Hỏa, nam Ngự thú. Lượt gọi định đính kèm mười ảnh bị từ chối trước khi tạo, không có PNG phát sinh; prompt dưới đã sửa theo giới hạn thực tế. Năm nhân vật còn lại được mô tả đầy đủ trong prompt, không có ảnh riêng đính kèm ở lượt đội hình. Một hàng từ trái sang phải: Kiếm nam/nữ, Thổ thể nam/nữ, Phù nam/nữ, Hỏa nam/nữ, Ngự thú nam/nữ. Hai linh thú nhỏ nằm cùng chủ, không tính thành nhân vật thứ 11–12. Ảnh chỉ để so phục sức, bảng màu và khả năng nhận ra trường phái; khi xem mặt và tay phải mở chân dung riêng. Không xem đội hình là bản ghép pixel hoặc cam kết giữ đúng nhận dạng cả mười ảnh.

```text
Use case: stylized-concept.
Asset type: wide roster review concept image for the original Vietnamese fantasy game Tu Tien Thu Ai, Ticket 009.
Primary request: exactly ten adult Vietnamese cultivators standing side by side in ONE uninterrupted horizontal row, five adjacent male-female school pairs. Create one coherent group from five school reference portraits and the ten character specifications below. Each attached reference anchors the art, materials and palette of one school pair; create its counterpart according to the specifications, rather than duplicating the reference person. Preserve the attached characters' identities as closely as possible and give every counterpart the specified costume, ornament and implement.
Input images: image 1 = female Sword kiem-nu.png (Ticket 008 style anchor); image 2 = male Earth-body tho-the-nam.png; image 3 = male Talisman phu-nam.png; image 4 = female Fire hoa-nu.png; image 5 = male Beast-tamer ngu-thu-nam.png. These are five school references, not the complete character count. Ten individual roster portraits exist; the remaining five designs are specified in words here because the tool accepts at most five reference files.
Ten character specifications, exact left-to-right order:
1. kiem-nam.png: male Sword, pearl white and deep indigo, low jade coronet, sheathed Thanh Phong sword.
2. kiem-nu.png: female Sword from Ticket 008, pearl white and deep indigo, small pale-gold and white-jade diadem, cloud-and-crane silk, sheathed Thanh Phong sword.
3. tho-the-nam.png: male Earth-body, broad shoulders, brown and ivory silk, ochre-jade square armor, stone-jade gauntlets.
4. tho-the-nu.png: female Earth-body, ivory and tea-brown silk, square ochre-jade armor, mountain-jade hairpin, upright stone staff.
5. phu-nam.png: male Talisman, ink-indigo and ivory scholar robes, rectangular jade coronet, calligraphy brush and ivory talisman booklet.
6. phu-nu.png: female Talisman, ivory and ink-indigo scholar robes, scroll-jade hairpin, calligraphy brush and two ivory talisman slips.
7. hoa-nam.png: male Fire, copper-brown and plum-brown silk with ivory panels, low coronet, half-open embroidered physical fan.
8. hoa-nu.png: female Fire, ivory and muted plum silk with subdued rose-copper shoulders, flame-jade hairpin, solid smoky-amber fire seal supported at the waist.
9. ngu-thu-nam.png: male Beast-tamer, moss-green and ivory silk, low jade coronet, bamboo flute and one small ivory spirit deer with short antler buds.
10. ngu-thu-nu.png: female Beast-tamer, ivory and tea-green silk, leaf-jade hairpin, jade flute and one small ivory spirit fox with exactly one fluffy tail.
Composition: very wide 3:1 panorama, 3840x1280. Exactly ten visible adult heads in one horizontal row at comparable scale and one common standing depth, all faces unobscured. Show each adult from complete head ornament down to knees or below, with generous margin above crowns and at the two outer edges. Keep their separate silhouettes and each school's implement legible. Adjacent school pairs can have a little breathing space. Both small companions stay near their own beast-tamer's lower legs on the far right, with complete heads and bodies visible, and remain much smaller than the humans. There are exactly ten adult characters plus two small animal companions. No other people, background crowds or portraits.
Scene: one quiet Vietnamese limestone pass terrace with distant low-contrast karst silhouettes, sparse old pine and soft indigo mist. Background remains subordinate. All ten share the same soft broad daylight and ground.
Style: match the attached Ticket 008 female Sword portrait and the four other school references: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art, soft ink-wash value steps, subtle do-paper character, readable layered silk, pale antique-gold embroidery and opaque jade. Royal dignity for men and refined nobility for women. Realistic adult proportions and clear natural hands.
Constraints: preserve each attached reference identity and implement, and follow the written specification for all five counterparts. All clothing opaque and fully covering chest, shoulders and legs, closed collars, all-ages dignity. Original project characters and costumes. A single continuous lineup, without panels, grids, inset portraits, duplicated people, merged limbs, text, captions, labels, numbers, UI, logo, watermark or frame. No emitted flames, aura or bright magical effects; the fire fan and seal are crafted physical objects. No sexualized poses, blood or horror. Muted physical material colors; no enemy-warning red, urgency orange, reward-yellow glow or typing-cyan glow.
Output: one wide PNG roster lineup, 3840x1280, aspect ratio 3:1.
```
