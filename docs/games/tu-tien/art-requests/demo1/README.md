# Demo 1 — bộ prompt Firefly Image 5 (01/11/2026)

> **Vai:** prompt nguyên văn cho mọi ảnh của Demo 1 ([`../../ART_AUDIO_VFX_PLAN.md`](../../ART_AUDIO_VFX_PLAN.md) §4.2–4.3), theo chuẩn D52 (painterly-realistic) và D47 (quý phái). Chỉ model Adobe (Firefly Image 5). Mỗi prompt ≤ 1024 ký tự. Ảnh ra lưu `games/immortality-cultivation/art-src/<nhóm>/<id>.v<n>-try<k>.png` kèm `.prompt.txt`; không vào Git.
> **Cổng:** hai giám khảo mù ≥ 8,5 (mức thị trường và, với ảnh nguồn 3D, mức hợp Tripo) trước khi dùng hay dựng. Kết quả chấm ghi ở `JUDGING.md` cùng thư mục.

## 0. Khối chuẩn chung (dán vào cuối mọi prompt ảnh nguồn 3D) — bản 2, 01/11 ~14:00

Bản 1 ("painterly-realistic AAA game concept sheet", nền `#00FF00`) làm Firefly vẽ kiểu truyện tranh và nền xanh loang hắt màu (`JUDGING.md`, Phong Lang v2 try1). Bản 2 dùng câu "photorealistic 3D render" và nền xám phẳng:

```text
Photorealistic 3D render, Unreal Engine 5 look, studio product shot: <CHỦ THỂ>. Not cartoon, not anime. <GÓC: Three-quarter view from 32 degrees above, facing front-left | Front view from 32 degrees above, facing the camera>. One cinematic key light from upper right 45 degrees, soft cool fill, no cast shadow, no ground plane, no platform. Single solid object, centered, 8 percent empty margin on every side, uniform flat medium-grey studio background. No text, no logo, no effects, no particles, no extra objects.
```

Chuẩn chất liệu để prompt "nhìn" theo: ảnh chụp trang lookdev của game (xem `JUDGING.md`, kết luận sau ba vòng), không phải tờ Firefly.

## 1. Tờ chuẩn chất liệu `refs/material-sheet` (bước 1 của §3.1)

Mục đích: một ảnh cho hai giám khảo và cho mọi prompt sau cùng "nhìn" một chuẩn: 8 ô chất liệu của Thanh Thạch Ải dưới cùng ánh sáng. Khổ 2048 × 2048 (Firefly 1:1), chấm trên tờ.

```text
Material study sheet for a AAA xianxia strategy game, 8 square swatches in a 4x2 grid on a neutral dark grey board, each swatch a 3D-rendered material ball with a flat ground tile beneath it, same cinematic key light from upper right 45° and cool fill on all: (1) weathered grey-blue limestone paving flag with moss in the joints, Ninh Binh karst stone; (2) rough karst cliff rock with lichen; (3) dark ironwood beam with carved cloud motif; (4) indigo-grey glazed yin-yang roof tiles; (5) ivory jade with soft inner glow; (6) cold forged steel of a flying sword, faint blue sheen; (7) layered ivory and indigo silk with fine gold-thread crane embroidery; (8) low indigo mist over wet stone. Painterly-realistic, physically correct roughness and specular, high detail, no text, no labels, no numbers.
```

Kiểm sau khi tạo: 8 ô đủ, không chữ, ánh sáng cùng hướng, không ô nào ngả cam hay vàng kim mạnh (màu dành cho tín hiệu).

## 2. Ảnh nguồn 3D cho ba model mẫu (bước 2)

Sửa đúng lỗi của `JUDGING.md` (một chuẩn, lề 8 %, cặp góc cùng khổ và tỉ lệ, chất tiên hiệp, Kiếm tu cầm kiếm, sói chỉ huy và Vương khác sói thường), giữ thiết kế đã duyệt (chân dung A; `../m0b/02-five-families.md`, `../m0b/05-beast-kings.md`). Mỗi prompt = phần chủ thể dưới đây + **khối chuẩn §0**. Đặt `STYLE` sau chủ thể. Cặp góc của một model tạo cùng một phiên, cùng tỉ lệ khung, mô tả y hệt, chỉ đổi câu góc nhìn.

### 2.1 Kiếm tu nữ (`cultivators/kiem-nu.v2`, 3:4, hai góc: `-front`, `-back`)

```text
Full-body FRONT view, A-pose, arms open 30 degrees away from the body, of a noble young female sword cultivator with royal bearing and a tall straight posture: layered ivory silk robe with indigo trim and fine gold-thread cloud-and-crane embroidery, wide sleeves gathered into a few large clean folds, indigo sash with a white jade pendant, small jade crown on a high bun, calm dignified face, soft boots. Her sheathed sword Thanh Phong (cold blue steel hilt, indigo scabbard, jade fittings) hangs at her left hip. Large readable shapes, no loose hair strands, no flowing ribbons.
```

Góc sau: thay câu đầu bằng `Full-body BACK view, same A-pose, same character and outfit seen from behind, head not turned, the sword scabbard visible at the left hip,` rồi giữ nguyên phần còn lại.

### 2.2 Phong Lang (`beasts/phong-lang.v2`, 1:1, hai góc: ba phần tư `-q` và trước `-front`)

```text
A lean corrupted spirit wolf standing with all four paws on the ground, head low and alert, ears back, lips drawn showing teeth: ash-grey fur in large clean clumps, black ink-wash corruption veins spreading over the shoulders and along the spine, faint pale-violet glow in the eyes, slightly larger than a real wolf, deep chest, long tail held low. Menacing, not cute. THREE-QUARTER view from 32 degrees above, the wolf facing front-left.
```

Góc trước: `... FRONT view from 32 degrees above, the wolf facing the camera.`

### 2.3 Thiết Bối Lang Vương (`kings/thiet-boi-lang-vuong.v2`, 1:1, `-q` và `-front`)

```text
A massive ancient beast king wolf, two and a half times a wolf, standing square and heavy, head lowered in threat: dark iron-grey fur, the back and shoulders armoured with jagged black stone-and-iron plates rising like a mountain ridge, a crest of three stone spikes behind the skull, heavy dark-bronze chains with ivory jade seal tags hanging from the neck, old scars glowing faint violet with ink corruption, pale-violet eyes, huge jaw. Royal, menacing, ancient, one solid mass. THREE-QUARTER view from 32 degrees above, facing front-left.
```

Góc trước như 2.2.

### 2.4 Sau khi tạo

Script kiểm khung (lề ≥ 8 %, một khối, không bóng) → nới nền `#00FF00` nếu thiếu lề → hai giám khảo mù (M và T) → chỉ ảnh đạt 8,5 từ cả hai mới `--dry-run` rồi dựng, Phong Lang trước.

## 3. Cách chạy Firefly trong app

- Tab riêng của phiên này; đóng khi xong; không đụng tab của phiên điều phối.
- Model: Firefly Image 5 (không model đối tác). Tỉ lệ: 1:1 cho tờ chuẩn và prop, 3:4 cho vật đứng, 16:9 cho cảnh.
- Nhận ảnh về máy qua bộ nhận cục bộ ở cổng **8775** (bản chép của `recv-img.py`, tên file theo mẫu `tt-<id>.v<n>-try<k>.png`), rồi script kiểm khung (lề, một khối, bóng) trước khi đưa giám khảo.
