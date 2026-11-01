# Demo 1 — bộ prompt Firefly Image 5 (01/11/2026)

> **Vai:** prompt nguyên văn cho mọi ảnh của Demo 1 ([`../../ART_AUDIO_VFX_PLAN.md`](../../ART_AUDIO_VFX_PLAN.md) §4.2–4.3), theo chuẩn D52 (painterly-realistic) và D47 (quý phái). Chỉ model Adobe (Firefly Image 5). Mỗi prompt ≤ 1024 ký tự. Ảnh ra lưu `games/immortality-cultivation/art-src/<nhóm>/<id>.v<n>-try<k>.png` kèm `.prompt.txt`; không vào Git.
> **Cổng:** hai giám khảo mù ≥ 8,5 (mức thị trường và, với ảnh nguồn 3D, mức hợp Tripo) trước khi dùng hay dựng. Kết quả chấm ghi ở `JUDGING.md` cùng thư mục.

## 0. Khối chuẩn chung (dán vào cuối mọi prompt ảnh nguồn 3D)

```text
STYLE: painterly-realistic AAA game concept sheet, physically correct materials (weathered grey-blue limestone with lichen, dark ironwood grain, indigo-grey glazed tile, ivory jade, cold forged steel, layered silk with fine embroidery), cinematic key light from upper right 45°, soft cool fill, no cast shadow on the background, no ground plane. FRAMING: single solid object, flat base, three-quarter view from 32° above, centered, 8% margin on every side, uniform flat #00FF00 background. NO text, no logo, no effects, no particles, no extra objects, no duplicate views.
```

Ảnh cảnh và tờ chuẩn không dùng nền `#00FF00` (xem từng prompt).

## 1. Tờ chuẩn chất liệu `refs/material-sheet` (bước 1 của §3.1)

Mục đích: một ảnh cho hai giám khảo và cho mọi prompt sau cùng "nhìn" một chuẩn: 8 ô chất liệu của Thanh Thạch Ải dưới cùng ánh sáng. Khổ 2048 × 2048 (Firefly 1:1), chấm trên tờ.

```text
Material study sheet for a AAA xianxia strategy game, 8 square swatches in a 4x2 grid on a neutral dark grey board, each swatch a 3D-rendered material ball with a flat ground tile beneath it, same cinematic key light from upper right 45° and cool fill on all: (1) weathered grey-blue limestone paving flag with moss in the joints, Ninh Binh karst stone; (2) rough karst cliff rock with lichen; (3) dark ironwood beam with carved cloud motif; (4) indigo-grey glazed yin-yang roof tiles; (5) ivory jade with soft inner glow; (6) cold forged steel of a flying sword, faint blue sheen; (7) layered ivory and indigo silk with fine gold-thread crane embroidery; (8) low indigo mist over wet stone. Painterly-realistic, physically correct roughness and specular, high detail, no text, no labels, no numbers.
```

Kiểm sau khi tạo: 8 ô đủ, không chữ, ánh sáng cùng hướng, không ô nào ngả cam hay vàng kim mạnh (màu dành cho tín hiệu).

## 2. Ảnh nguồn 3D cho ba model mẫu (bước 2)

Viết sau khi có kết quả chấm 26 ảnh Codex (`JUDGING.md`): prompt sửa đúng lỗi giám khảo nêu, giữ thiết kế đã duyệt (chân dung A cho Kiếm tu; Phong Lang và Thiết Bối Lang Vương theo `../m0b/02-five-families.md`, `../m0b/05-beast-kings.md`).

## 3. Cách chạy Firefly trong app

- Tab riêng của phiên này; đóng khi xong; không đụng tab của phiên điều phối.
- Model: Firefly Image 5 (không model đối tác). Tỉ lệ: 1:1 cho tờ chuẩn và prop, 3:4 cho vật đứng, 16:9 cho cảnh.
- Nhận ảnh về máy qua bộ nhận cục bộ ở cổng **8775** (bản chép của `recv-img.py`, tên file theo mẫu `tt-<id>.v<n>-try<k>.png`), rồi script kiểm khung (lề, một khối, bóng) trước khi đưa giám khảo.
