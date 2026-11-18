# Nữ chính Tu Tiên 3D: phân tích trước khi làm lại (18/11/2026)

Chủ dự án, 18/11/2026, sau ba lần thử: "vẫn quá xấu, thực sự bạn đã làm đúng cách chưa vậy, tìm hiểu và phân tích trước khi làm cho tôi, hướng là dùng tripo, blender". Ràng buộc: chỉ công cụ miễn phí (Tripo ~490 credit sẵn có, Blender, Firefly, ảnh 2D của ta). Tài liệu này chỉ phân tích; chưa dựng, chưa tiêu credit.

## Tóm tắt (250 từ)

Ba lần thử thất bại không phải do thiếu credit mà do sai cách: ta coi Tripo là công cụ làm **nhân vật hoàn chỉnh**, trong khi Tripo chỉ cho ra **một khối liền** (da, tóc, mắt, áo dính nhau), ánh sáng của ảnh 2D bị nướng vào texture, mắt không có nhãn cầu, tóc là vỏ bóng. Không game thương mại nào để mặt và tóc như vậy: họ có đầu tách riêng, topo sạch, nhãn cầu riêng (giác mạc, viền nước mắt), mi và mày dạng card, tóc dạng card với texture sợi có alpha, và shader da. MPFB cho topo và mắt chuẩn nhưng mặt Âu chung chung vì ta chỉ kéo slider, không nắn theo ảnh.

Đề xuất: **kết hợp hai thứ**. Thân lấy từ Tripo v6B (đã đạt hình dáng, giữ). Đầu: lấy MPFB CC0 làm lưới gốc (có nhãn cầu, mi, răng, rig), **nắn tay (sculpt + shrinkwrap) theo đầu Tripo v6B** làm khuôn hình, chiếu texture mặt từ ảnh chính diện độ phân giải cao do Firefly làm lại từ ảnh v6B (ánh sáng phẳng). Tóc: không dùng Tripo; làm bằng Hair Curves của Blender rồi đổi sang card (setup Geometry Nodes miễn phí), texture sợi tự bake trong Blender. Mắt: nhãn cầu MPFB CC0 + giác mạc khúc xạ + viền nước mắt. Da theo mức B của `character-skin-shading.md`.

Chi phí: 0–65 credit (chỉ khi cần dựng lại đầu Tripo với `delight`), khoảng 4–6 ngày làm việc của Claude trong Blender, với 5 cổng chủ dự án duyệt (mặt xám, mặt có texture, mắt, tóc, toàn thân trong game). Trần chất lượng thực tế: khoảng mức nhân vật game web/mobile tầm trung–khá (gần Genshin-ish bán thực / mobile MMO), khó đạt mặt cấp AAA. Rủi ro lớn nhất là tóc card và độ giống ảnh 2D; vì vậy cổng 1 là mặt xám, chưa làm gì khác.

## 1. Vì sao ba lần thử thất bại

| Lần | Thấy gì | Nguyên nhân cụ thể |
|---|---|---|
| Tripo cả người v5B (`tripo-v5b-mirror/`) | Mặt sáp như búp bê, tóc là cục | (a) Mặt chiếm ~3 % diện tích ảnh toàn thân 1536 px → Tripo chỉ có vài chục pixel cho mắt mũi miệng. (b) Ảnh nguồn có bóng đổ và highlight: không bật `delight`, nên ánh sáng 2D bị nướng vào màu, rồi ta lại chiếu sáng lần hai → phẳng, sáp. (c) Tripo tạo một mặt kín liên tục: tóc, da, mắt cùng một lưới, không có lỗ mắt, không có lớp alpha → tóc chắc chắn là vỏ. (d) 50k tam giác chia cho cả người, phần đầu chỉ vài nghìn. |
| MPFB CC0 (`heroine-mpfb/`) | Mặt Âu chung chung, tóc vỏ | (a) Chỉ dùng modifier/macro, không sculpt → mặt là "trung bình" của MakeHuman, không phải mặt v6B. (b) Chiếu ảnh 3/4 lên mặt có mắt/mi là lưới riêng → lệch, ta đã ghi "không cải thiện". (c) Tóc búi CC0 là proxy thấp, không có sợi. Ưu điểm đã chứng minh: có nhãn cầu, mi, răng, rig, giấy phép sạch. |
| Tripo thân + đầu riêng v6B (`heroine-v6b-3d/`) | Mặt tốt hơn, vẫn xấu; tóc vỏ; không nhãn cầu | (a) Đầu nguồn là ảnh mặt **phóng to Lanczos** từ ảnh toàn thân → không thêm chi tiết thật, chỉ mờ to hơn. (b) Vẫn không `delight`. (c) Mắt vẽ trên texture lưới liền → không phản chiếu, không độ sâu, nhìn "chết". (d) Tóc vẫn là vỏ, mép tóc răng cưa (thấy rõ ở 3/4). (e) Topo tam giác tự động, không có vòng cạnh quanh mắt/miệng → không làm biểu cảm hay chớp mắt được. (f) Cổ áo rách mép (ghép đầu). |

Nguyên nhân chung: **ta để một công cụ tạo hình khối làm những phần mà ngành luôn làm riêng** (mắt, mi, tóc, shader da) và **cho nó ảnh nguồn thiếu độ phân giải mặt và có ánh sáng nướng sẵn**. Nhìn sheet v6B: hình dáng thân 3D đã khá giống ảnh 2D; phần hỏng gần như hoàn toàn ở đầu, mắt và tóc.

## 2. Pipeline đề xuất (Tripo + Blender + Firefly)

Nguyên tắc: thân và đầu tách; đầu dùng lưới có topo chuẩn; mắt, mi, mày, tóc là lưới riêng; Tripo chỉ là **khuôn hình** (shape reference) và nguồn texture thân.

| # | Bước | Đầu vào | Công cụ, thiết lập | Đầu ra | Cổng (ai duyệt, đo gì) | Thời gian / credit |
|---|---|---|---|---|---|---|
| 0 | Ảnh mặt nguồn | ảnh v6B, face zoom 436j | Firefly Image 5 (tham chiếu ảnh của ta, Structure + Style reference), xin: mặt chính diện và nghiêng 90°, ánh sáng phẳng đều, không bóng, mắt mở nhìn thẳng, tóc vén gọn khỏi trán/tai, 2048 px+ (Image 5 ra tối đa ~4 MP). Không phóng to Lanczos. | `head-front.flat.png`, `head-side.flat.png` | Chủ dự án: còn giống mặt v6B? Ánh sáng phẳng? Mắt đối xứng? | 1–2 giờ, 0 credit |
| 1 | Thân | Tripo v6B đã có (49k tam giác) | Giữ. Blender: cắt bỏ đầu tại cổ áo, vá viền cổ áo rách. | `body.v6b.clean.glb` | Không đổi hình so với sheet đã xem | 1 giờ, 0 |
| 2 | Khuôn đầu (tuỳ chọn) | ảnh bước 0 | Tripo multiview (front + left), v3.1, `geometry_quality=detailed`, `texture_quality=detailed`, `pbr=true`, **`delight=true`**, `face_limit` 30k. Chỉ làm nếu đầu v6B hiện có không đủ làm khuôn. | `head-shape.tripo.glb` | Hình khối (gò má, cằm, mũi, mí) đúng ảnh ở 3 góc xám, không xét texture | 0 hoặc 1 model (~40–60 credit) |
| 3 | Lưới đầu chuẩn | MPFB CC0 (đã cài), đầu Tripo làm khuôn | MPFB nữ Á (thiết lập v5) → căn đầu vào khuôn Tripo → **Shrinkwrap** (nearest surface, giữ vùng mắt/miệng loại trừ) → **Sculpt** tay ở chế độ Multires theo hai ảnh bước 0 đặt làm ảnh nền ortho (mí phượng, đuôi mắt, môi, mũi, cằm V). Giữ topo MPFB → giữ nhóm đỉnh, mắt, mi, rig. | `head.mpfb-sculpt.blend` | **Cổng 1 (quan trọng nhất): mặt xám**, Workbench + Cycles đèn phẳng, 5 góc đặt cạnh ảnh 2D. Chủ dự án phải nói "giống, đẹp" trước khi làm texture. | 1–2 ngày, 0 |
| 4 | UV và texture mặt | đầu bước 3, ảnh bước 0 | UV MPFB có sẵn. Chiếu ảnh chính diện + nghiêng (Texture Paint, chế độ Project / "Quick Edit" hoặc UV Project từ camera ortho), trộn ở đường mép bằng mask; tô tay vùng tai, gáy. Bake normal/AO từ bản Multires cao xuống bản thấp. Map: màu 2048, normal, roughness vùng (masks đã có ở `character-skin-shading.md`). | `head_color/normal/rough.png` | **Cổng 2:** mặt có màu, đèn 3 điểm, so ảnh 2D; không vệt chiếu, không bóng nướng | 1 ngày, 0 |
| 5 | Mắt | nhãn cầu MPFB CC0 | Ba lớp: tròng (iris texture tô lại màu nâu theo ảnh, có bóng sâu), giác mạc lồi trong suốt (IOR ~1,376, roughness thấp → có catchlight thật), lưới viền nước mắt/caruncle ẩm, bóng mí (AO mờ trên tròng trắng). Mi và mày: card alpha của MPFB CC0, chỉnh dày theo ảnh. | `eyes.blend` | **Cổng 3:** cận mặt 3/4, mắt có độ sâu và ánh sáng, không "chết" | 0,5 ngày, 0 |
| 6 | Tóc | ảnh v6B (búi + mái hai bên) | Blender Hair Curves (built-in): mọc từ da đầu, tạo hướng tóc, búi bằng các nhóm curve; texture sợi: render 20–40 sợi curve thành một atlas alpha/màu/độ sâu ngay trong Blender (Cycles bake). Đổi curve → card: setup Geometry Nodes miễn phí của Daniel Bystedt hoặc tự viết node (Curve to Mesh + profile phẳng + UV dọc). Shader: alpha-hashed/clip, anisotropic theo hướng UV, hai vệt highlight. Vài nghìn card, ~15–30k tam giác. | `hair.cards.glb` | **Cổng 4:** tóc trong trình xem three.js (không phải Cycles), đọc ra sợi, không cục, viền tóc mềm; đo FPS | 1–2 ngày, 0 |
| 7 | Ghép, rig | thân, đầu, mắt, tóc | Rig: dùng rig `game_engine` của MPFB cho đầu (có xương hàm, mắt) ghép với thân; hoặc Tripo rig v3.0 (spec tripo, ~25 credit) cho thân rồi gắn đầu vào xương đầu. Shape key chớp mắt từ topo MPFB. Kiểm khớp cổ khi xoay đầu. | `heroine.v7.glb` | Clip thử idle + quay đầu, không rách cổ | 0,5–1 ngày, 0–25 |
| 8 | Trong game | GLB | three.js: MeshPhysicalMaterial da mức B, transmission/clearcoat cho giác mạc, alpha cho tóc/mi; camera chơi 55° và cận mặt | — | **Cổng 5:** hai giám khảo mù ≥ 8,5 trong host chơi, cài đặt người chơi | 0,5 ngày, 0 |

Tổng: khoảng 4–6 ngày làm việc, 0–85 credit. Mỗi cổng dừng nếu chủ dự án không đạt; không đi bước sau trên nền hỏng.

## 3. Hướng thay thế

| Hướng | Cách | Ưu | Nhược |
|---|---|---|---|
| A. Tripo đầu tốt hơn, giữ lưới liền | Bước 0 + bước 2 (delight, ảnh mặt 2K thật), rồi chỉ remesh, khoét hốc mắt, chèn nhãn cầu MPFB, thay tóc card | Giống ảnh 2D nhất về hình; ít sculpt | Topo tam giác, khoét mắt dễ lệch; không biểu cảm; texture mặt Tripo vẫn có thể sáp; tốn 40–60 credit mỗi lần thử |
| B. MPFB thuần + sculpt (không Tripo đầu) | Như bước 3 nhưng sculpt chỉ theo ảnh, không khuôn | 0 credit, topo/rig/mắt sạch nhất | Phụ thuộc tay sculpt của Claude qua script/headless; độ giống ảnh rủi ro cao |
| C. CharMorph (thân Vitruvian CC0) | Thay MPFB bằng CharMorph | Có bộ morph mặt khác | Không có lợi rõ so với MPFB đã cài; MB-Lab gốc là AGPL nên **loại** |
| D. Giảm phạm vi theo camera chơi | Ở camera 55° nhân vật chỉ cao ~100–200 px; dùng bản Tripo v6B + mắt + tóc card, chỉ làm đẹp mặt cho cut-in bằng ảnh 2D | Nhanh nhất | Không có cận mặt 3D đẹp; nếu game cần zoom gần thì lộ |

Đề xuất chính là pipeline mục 2 (lai A và B). Nếu Cổng 1 hỏng hai lần, chuyển D và báo chủ dự án.

## 4. Rủi ro

- **Sculpt headless:** Claude điều khiển Blender bằng script; sculpt tay theo ảnh khó hơn nhiều so với người. Giảm rủi ro: shrinkwrap theo khuôn Tripo làm phần lớn việc, sculpt chỉ sửa vùng mắt/môi bằng modifier định hướng (Hook, Lattice, Warp) đo theo landmark trên ảnh.
- **Tóc card** là phần khó nhất của ngành; bản đầu sẽ thô. Cần atlas sợi tốt và sắp xếp lớp; có thể mất 2 vòng.
- **Firefly đổi mặt:** ảnh chính diện mới có thể không giống v6B. Cổng 0 bắt chủ dự án duyệt.
- **Giấy phép:** chỉ tài sản MPFB gói ghi CC0; tóc búi `.mhclo` ghi AGPL (đã ghi trong `heroine-mpfb-pipeline.md`) thì không dùng. Setup tóc của Bystedt chưa xác minh giấy phép → nếu không rõ, tự viết node.
- **Hiệu năng web:** tóc alpha nhiều lớp gây overdraw; dùng alpha-test + một lớp alpha-blend mỏng, đo FPS ở Cổng 4.
- **`delight`** chỉ là xử lý tự động của Tripo; có thể làm mất màu môi/mắt — đó là lý do texture mặt lấy từ chiếu ảnh, không từ Tripo.
- Trần chất lượng: với công cụ miễn phí và không có người sculpt, mục tiêu thực tế là mặt đẹp, giống 2D ở camera chơi và cận vừa; da lỗ chân lông/biểu cảm AAA là ngoài tầm.

## 5. Nguồn

| Nguồn | Khẳng định | Trạng thái |
|---|---|---|
| https://developers.tripo3d.com/en/docs/generation-image-to-model/standard.md | Model v3.1-20260211; ảnh ≥256 px, nền sạch; `texture_quality` fast/standard/detailed/extreme; `delight` bỏ ánh sáng nướng; `geometry_quality` detailed; face_limit tối đa; quad ≤150k; smart_low_poly 500–20k chỉ cho vật đơn giản; `generate_parts` không texture | Đã mở, đọc 18/11 |
| https://developers.tripo3d.com/en/docs/animations-rig.md | Rig biped, spec tripo/mixamo/unity/unreal/vrm; v3.0-20260909 khuyên cho người; ví dụ 25 credit; xuất GLB/FBX; không nói xương mặt/ngón | Đã mở, đọc 18/11 |
| https://developers.tripo3d.com/en/docs/generation-multiview-to-model/standard.md (qua docs.comfy.org, fal.ai) | Multiview: front bắt buộc + 1–3 view [front, left, back, right]; left = trái của nhân vật | Từ kết quả tìm, chưa mở trang gốc |
| https://www.tripo3d.ai/blog/explore/retopology-pipeline-for-ai-generated-models | Chính Tripo khuyên retopo trước khi dùng cho game/hoạt hình | Từ kết quả tìm (blog của nhà bán) |
| https://www.cgchannel.com/?p=156171 | Setup Geometry Nodes miễn phí của Daniel Bystedt đổi Hair Curves → card (Blender 3.6+) | Từ kết quả tìm; giấy phép chưa xác minh |
| https://superhivemarket.com/products/hair-cards-to-curves/docs | Đa số addon card tóc là trả phí (loại theo ràng buộc) | Từ kết quả tìm |
| https://mb-lab-docs.readthedocs.io/en/latest/license.html | MB-Lab: dữ liệu nhân vật AGPL lan sang model xuất → loại | Từ kết quả tìm |
| https://www.cgchannel.com/2025/03/check-out-new-open-source-3d-character-generator-charmorph/ | CharMorph: nhân vật Vitruvian CC0 | Từ kết quả tìm |
| https://github.com/makehumancommunity/mpfb2 , https://static.makehumancommunity.org/assets/assetpacks.html | MPFB tài sản CC0, gói system assets (mắt, mi, mày, răng) CC0 | Đã kiểm 18/11 (xem `heroine-mpfb-pipeline.md`) |
| https://techcrunch.com/2025/10/28/adobe-firefly-image-5-brings-support-for-layers-will-let-creators-make-custom-models/ | Firefly Image 5 ra tối đa ~4 MP gốc | Từ kết quả tìm |
| https://blog.adobe.com/en/publish/2024/03/26/new-structure-reference-capabilities-adobe-firefly-bring-new-level-creative-control-ideation | Structure Reference + Style Reference | Từ kết quả tìm |
| Sheet nội bộ `typing-game-review/owner-review/2026-11-18/tu-tien/heroine-v6b-3d/heroine-v6b-3d-sheet.png` | Thân giống 2D; đầu, mắt, tóc hỏng; cổ áo rách | Đã xem |

Chưa tìm được nguồn độc lập đáng tin nói riêng về "sửa mặt xấu của Tripo"; phần mắt nhiều lớp, mi/mày card, tóc card là thực hành chuẩn của ngành (Tripo, yelzkizi, Kevuru đều nêu), không phải mẹo riêng của Tripo.
