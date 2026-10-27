# Tu Tiên Thủ Ải — Bộ prompt ảnh M0b và nguồn dựng 3D (25/10/2026)

> **Cập nhật Phiếu 008:** [00-identity.md](00-identity.md) hiện có hai chân dung phục sức hoàng tộc theo D47 và hai cảnh toàn sân theo D48 (50°/55°); cặp Kiếm tu trước/sau ở [01-cultivators-bots.md](01-cultivators-bots.md) dùng thiết kế mới. Phiếu sửa được phép tối đa hai lượt cho mỗi ảnh, độc lập với trần 40 của Phiếu 007 đã xong. Bản cũ và prompt giữ tên `.v1`; xem [giao nhận Phiếu 008](../../../../../games/immortality-cultivation/art-src/README-m0b.md). Các số đếm, thứ tự và việc còn thiếu dưới đây là hồ sơ **Phiếu 007 tại thời điểm giao**, không phải tổng kiểm kê hiện tại.

> **Kết quả lượt này:** 40 đầu ra = 38 ảnh danh mục + 2 bản đầu bị loại. Góc ngang Hỏa Nha sau thử lại vẫn chưa đạt Multiview; nền nguồn chưa khóa đúng #E6E6E6. Sáu ảnh chưa tạo ở §6; xem [nhận xét từng ảnh](../../../../../games/immortality-cultivation/art-src/README-m0b.md).
> **Phiếu 007 · Dành cho:** chủ dự án duyệt bản sắc, tự dựng Tripo; Codex tạo ảnh bằng image_gen tích hợp; Blender dọn model, rig và làm clip sau. Chỉ tạo nguồn 2D, chưa dựng hoặc tích hợp GLB.
> **Nguồn thắng:** [canon](../../00-canon.md) §0, §2, §8–12, §14.5, §20–21, D03, D23, D27, D36; [đánh giá](../../DANH_GIA_2026-10-24.md) cho lý do bản sắc; [3D_REQUESTS.md §1.1](../../../3D_REQUESTS.md#11-quy-tắc-rig-của-lượt-này) cho rig. Cách đóng gói theo bộ Rồng M0; không chép mỹ thuật Rồng hoặc game khác.

```text
Instructions for the image tool (Codex image_gen or ChatGPT)
- This README is an index, not an image prompt.
- Open the named file and paste one complete text prompt per image, verbatim.
- Follow section 2 order. One output per call; never combine views on one sheet.
- Attach the reference image or images named for that output, in their stated roles; inspect local references first.
- Keep all reconstruction plates on uniform #E6E6E6 with no shadows, text or effects.
- Bipeds: front A pose then rear A pose. Quadrupeds: left side then front. Crow: front then left side.
- Keep primary and secondary views geometrically identical.
- For completed ticket 007, all outputs including retries count against its 40-image cap. Ticket 008 allows at most two attempts per requested image.
- Save each PNG and its exact prompt as <id>.prompt.txt in the specified directory.
```

## 1. Mục lục và phạm vi

| File | Nội dung | Ảnh trong bộ | Lượt này |
|---|---|---:|---:|
| [00-identity.md](00-identity.md) | 00. Hai ảnh bản sắc | 2 | 2 |
| [01-cultivators-bots.md](01-cultivators-bots.md) | 01. Người chơi và bot đạo đồng | 6 | 6 |
| [02-five-families.md](02-five-families.md) | 02. Năm họ thú và biến chủng hệ | 14 | 10 |
| [03-elites.md](03-elites.md) | 03. Ba thuộc tính tinh anh | 6 | 6 |
| [04-commanders.md](04-commanders.md) | 04. Thú tướng Lang Đầu Đàn | 2 | 2 |
| [05-beast-kings.md](05-beast-kings.md) | 05. Thú Vương Thiết Bối Lang Vương | 2 | 2 |
| [06-formations-mechanisms-props.md](06-formations-mechanisms-props.md) | 06. Trận pháp, cơ quan và cảnh | 9 | 9 |
| [07-treasures-swords.md](07-treasures-swords.md) | 07. Pháp bảo và phi kiếm của Thiên Hà Kiếm Vũ | 3 | 1 |
| **Cộng** | **19 GLB duy nhất; mẫu bot, tướng, tinh anh, biến chủng dùng lại GLB** | **44** | **38 ảnh danh mục; thêm 2 bản đầu loại = 40 đầu ra** |

- **3D trước, có đo:** người chơi, bot, thú tướng, Thú Vương và chiêu lớn giữ 3D thật. Đám đông 3D nếu HN0 đạt; nếu một phần trượt ngân sách D36, chỉ phần đó xuống impostor nướng từ cùng GLB. Phiếu ảnh không xác nhận HN0 đã đạt.
- Hai ảnh bản sắc hướng dẫn dựng 3D; không phải nền dùng thẳng hoặc đầu vào tái dựng cả cảnh. Các ảnh còn lại là nguồn hình khối hoặc mẫu vật liệu cho 3D. Không có icon, UI, tile, decal hoặc texture VFX trong phiếu.
- Canon §21.3 ước **14 GLB**; giữ đủ 14 và thêm **4 cơ quan §8.3 + Hậu Thổ Ấn §14.5 = 19**. Không cộng bot, tướng, tinh anh, Đằng Thử hoặc Khê Viên thành model mới.
- Dáng, kích thước mét, áo năm thân, dấu vật liệu tinh anh và face limit Tripo là **đề xuất mỹ thuật**, cần anh duyệt; không sửa số gameplay. Không thêm hệ cho Hỏa Nha/Phong Lang vì tên loài. Phù và thú sau MVP chưa có đặc tả hình, chưa mở rộng.

## 2. Thứ tự tạo ảnh và việc anh duyệt

Hai ảnh bản sắc trước; Kiếm tu hai góc; Thú Vương; thú tướng; năm họ thú; phần còn lại theo bảng. **Theo yêu cầu làm trọn phiếu, các ảnh sau vẫn tạo dưới cùng giả định phong cách để anh xem một lượt; chưa coi bản sắc đã duyệt.** Trước khi chi credit dựng hàng loạt, anh duyệt bản sắc rồi ba model mẫu **Kiếm tu, Phong Lang, Thiết Bối Lang Vương** và chuyển động (§21.2). Lịch Tripo của anh sau Rồng qua B9 (D02).

| Lượt | Mã | Ảnh | Prompt |
|---:|---|---|---|
| 1 | BS01 | `identity/thanh-thach-ai.png` | [00-identity.md](00-identity.md) |
| 2 | BS02 | `identity/kiem-tu-portrait.png` | [00-identity.md](00-identity.md) |
| 3 | NV01-F | `cultivators/kiem-tu.png` | [01-cultivators-bots.md](01-cultivators-bots.md) |
| 4 | NV01-B | `cultivators/kiem-tu-back.png` | [01-cultivators-bots.md](01-cultivators-bots.md) |
| 5 | V01-S | `kings/thiet-boi-lang-vuong.png` | [05-beast-kings.md](05-beast-kings.md) |
| 6 | V01-F | `kings/thiet-boi-lang-vuong-front.png` | [05-beast-kings.md](05-beast-kings.md) |
| 7 | TG01-S | `commanders/lang-dau-dan.png` | [04-commanders.md](04-commanders.md) |
| 8 | TG01-F | `commanders/lang-dau-dan-front.png` | [04-commanders.md](04-commanders.md) |
| 9 | T01-S | `beasts/thach-thu.png` | [02-five-families.md](02-five-families.md) |
| 10 | T01-F | `beasts/thach-thu-front.png` | [02-five-families.md](02-five-families.md) |
| 11 | T02-S | `beasts/phong-lang.png` | [02-five-families.md](02-five-families.md) |
| 12 | T02-F | `beasts/phong-lang-front.png` | [02-five-families.md](02-five-families.md) |
| 13 | T03-F | `beasts/hoa-nha.png` | [02-five-families.md](02-five-families.md) |
| 14 | T03-S | `beasts/hoa-nha-side.png` | [02-five-families.md](02-five-families.md) |
| 15 | T04-F | `beasts/nham-vien.png` | [02-five-families.md](02-five-families.md) |
| 16 | T04-B | `beasts/nham-vien-back.png` | [02-five-families.md](02-five-families.md) |
| 17 | T05-S | `beasts/thiet-giap-tru.png` | [02-five-families.md](02-five-families.md) |
| 18 | T05-F | `beasts/thiet-giap-tru-front.png` | [02-five-families.md](02-five-families.md) |
| 19 | NV02-F | `cultivators/tho-the-tu.png` | [01-cultivators-bots.md](01-cultivators-bots.md) |
| 20 | NV02-B | `cultivators/tho-the-tu-back.png` | [01-cultivators-bots.md](01-cultivators-bots.md) |
| 21 | BOT01-F | `bots/bot-dao-dong-tho.png` | [01-cultivators-bots.md](01-cultivators-bots.md) |
| 22 | BOT01-B | `bots/bot-dao-dong-tho-back.png` | [01-cultivators-bots.md](01-cultivators-bots.md) |
| 23 | TA01-S | `elites/phong-lang-cuong.png` | [03-elites.md](03-elites.md) |
| 24 | TA01-F | `elites/phong-lang-cuong-front.png` | [03-elites.md](03-elites.md) |
| 25 | TA02-S | `elites/thiet-giap-tru-thiet-bi.png` | [03-elites.md](03-elites.md) |
| 26 | TA02-F | `elites/thiet-giap-tru-thiet-bi-front.png` | [03-elites.md](03-elites.md) |
| 27 | TA03-S | `elites/phong-lang-hoi-nguyen.png` | [03-elites.md](03-elites.md) |
| 28 | TA03-F | `elites/phong-lang-hoi-nguyen-front.png` | [03-elites.md](03-elites.md) |
| 29 | P01 | `props/tran-tam.png` | [06-formations-mechanisms-props.md](06-formations-mechanisms-props.md) |
| 30 | P02 | `props/tran-tru.png` | [06-formations-mechanisms-props.md](06-formations-mechanisms-props.md) |
| 31 | P03 | `props/cong-ai.png` | [06-formations-mechanisms-props.md](06-formations-mechanisms-props.md) |
| 32 | P04 | `props/da-voi.png` | [06-formations-mechanisms-props.md](06-formations-mechanisms-props.md) |
| 33 | P05 | `props/tung-co.png` | [06-formations-mechanisms-props.md](06-formations-mechanisms-props.md) |
| 34 | CQ01 | `mechanisms/kiem-thung.png` | [06-formations-mechanisms-props.md](06-formations-mechanisms-props.md) |
| 35 | CQ02 | `mechanisms/loi-phu-tru.png` | [06-formations-mechanisms-props.md](06-formations-mechanisms-props.md) |
| 36 | CQ03 | `mechanisms/phong-an-vong.png` | [06-formations-mechanisms-props.md](06-formations-mechanisms-props.md) |
| 37 | CQ04 | `mechanisms/me-vu-tran.png` | [06-formations-mechanisms-props.md](06-formations-mechanisms-props.md) |
| 38 | PB01-F | `treasures/thanh-phong-kiem.png` | [07-treasures-swords.md](07-treasures-swords.md) |
| 39 | PB01-S · để lại | `treasures/thanh-phong-kiem-side.png` | [07-treasures-swords.md](07-treasures-swords.md) |
| 40 | PB02 · để lại | `treasures/hau-tho-an.png` | [07-treasures-swords.md](07-treasures-swords.md) |
| 41 | BT01-S · để lại | `variants/dang-thu.png` | [02-five-families.md](02-five-families.md) |
| 42 | BT01-F · để lại | `variants/dang-thu-front.png` | [02-five-families.md](02-five-families.md) |
| 43 | BT02-F · để lại | `variants/khe-vien.png` | [02-five-families.md](02-five-families.md) |
| 44 | BT02-B · để lại | `variants/khe-vien-back.png` | [02-five-families.md](02-five-families.md) |

**Đã dừng ở 40 đầu ra.** Sáu ảnh cuối chưa tạo: PB01-S, PB02, BT01-S/F và BT02-F/B. Hai lượt tạo lại đẩy PB01-S/PB02 ra khỏi đợt đầu. T03-S sau thử lại vẫn lỗi góc cánh: không dùng Multiview, chỉ gửi T03-F. Nền nguồn đo còn lệch nhẹ #E6E6E6; chuẩn hóa trước Tripo. Cột “Lượt này” đếm ảnh danh mục hiện diện, gồm T03-S còn lỗi; hai bản đầu loại đếm riêng. Hiện vật và nhận xét: [README-m0b.md](../../../../../games/immortality-cultivation/art-src/README-m0b.md).

## 3. Thiết lập Tripo

| Mục | Chọn theo quy ước dự án |
|---|---|
| Chế độ | Hai góc khớp: Multiview to 3D; một góc: Image to 3D |
| Ô ảnh | Hai chân: Front = chính, Back = -back. Bốn chân: Left = chính, Front = -front. Hỏa Nha: Front = chính, Left = -side. Kiếm: Front = mặt rộng, Left = cạnh |
| Tách nền | Bật; nền xám phẳng #E6E6E6 |
| Texture | Bật, HD cao nhất của gói, PBR bật; vật liệu mờ |
| Lưới | Tam giác, Quad tắt, Smart Low Poly tắt |
| Face limit | Bảng §4; mức tạo nguồn, **không phải** ngân sách tam giác runtime |
| Rig Blender | Không bấm rig Tripo, tải GLB không xương. Không dùng Tripo Quadruped cho loạt này |
| Tripo Biped | Chỉ Thổ thể tu: một lần 20 credit rig theo §1.1. Bot dùng lại rig. Chọn clip người đi bộ gần nghĩa; chiêu còn thiếu giao Blender |
| Lỗi rig | Tải bản không xương, không trả phí thử lặp lại |
| Tải | GLB, tên theo id; không tạo model riêng từ ảnh biến thể |

Thiết lập/credit là quy ước dự án; chưa mở Tripo kiểm gói hoặc giao dịch. Không lấy ước “75 credit/sinh vật” làm giá hiện hành. Góc phụ lệch thì bỏ, dùng Image to 3D từ ảnh chính. Mỗi góc một ô; không ghép nhiều góc vào một tấm.

## 4. Face limit, rig và clip

Ảnh tính từ `games/immortality-cultivation/art-src/`. GLB gốc: `games/immortality-cultivation/art-src/3d/<nhóm>/<id>.glb`. Chưa tạo GLB nào. Face limit dưới đây là **đề xuất của phiếu** theo chi tiết cần giữ, không phải số Tripo đã chốt trong canon.

| Mã · id | Face limit | Rig · lý do | Clip cần có |
|---|---:|---|---|
| NV01-F · `kiem-tu` | 20000 | Tự rig Blender. Nhân vật chữ ký; dáng đi bộ, áo xẻ và động tác Kiếm riêng. | Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory |
| V01-S · `thiet-boi-lang-vuong` | 30000 | Tự rig Blender. Thú Vương bốn chân; vồ, húc, chuyển pha và ngã riêng. | Idle, Move, Pounce, Howl_Summon, Charge_Windup, Charge, Hit, Stagger, Phase_Change, Death |
| T01-S · `thach-thu` | 4000 | Tự rig Blender. Bốn chân, cắn; cần chu kỳ bầy ổn định để nướng VAT. | Idle, Move, Attack, Death (Move: chạy; Attack: cắn) |
| T02-S · `phong-lang` | 6000 | Tự rig Blender. Bốn chân, cắn và vồ; chung rig với Lang Đầu Đàn. | Idle, Move, Attack, Death (Move: chạy; Attack: cắn/vồ) |
| T03-F · `hoa-nha` | 5000 | Tự rig Blender. Cánh, bay và bổ nhào; không dùng Biped/Quadruped Tripo. | Idle, Move, Attack, Death (Idle: lơ lửng; Move: bay; Attack: bổ nhào; Death: rơi) |
| T04-F · `nham-vien` | 8000 | Tự rig Blender. Tỉ lệ tay dài của Viên và clip ném riêng; không phải người chuẩn. | Idle, Move, Attack, Death (Move: bước nặng; Attack: ném) |
| T05-S · `thiet-giap-tru` | 8000 | Tự rig Blender. Bốn chân, húc và chiếm nhãn; chuyển trọng lượng phải đúng. | Idle, Move, Attack, Death (Attack: húc; chuẩn bị và lao tách nhịp) |
| NV02-F · `tho-the-tu` | 10000 | Tripo Biped · 20 credit. Người hai chân chuẩn, áo ngắn; rig cơ bản đủ, Blender thêm chiêu Thổ. | Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory |
| P01 · `tran-tam` | 10000 | Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. | — |
| P02 · `tran-tru` | 8000 | Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. | — |
| P03 · `cong-ai` | 10000 | Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. | — |
| P04 · `da-voi` | 6000 | Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. | — |
| P05 · `tung-co` | 10000 | Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. | — |
| CQ01 · `kiem-thung` | 6000 | Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. | — |
| CQ02 · `loi-phu-tru` | 6000 | Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. | — |
| CQ03 · `phong-an-vong` | 6000 | Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. | — |
| CQ04 · `me-vu-tran` | 5000 | Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. | — |
| PB01-F · `thanh-phong-kiem` | 4000 | Không rig. Đạn và pháp bảo gắn cứng; bay bằng runtime, 150/300/500 bản dùng chung mesh. | — |
| PB02 · `hau-tho-an` | 4000 | Không rig. Pháp bảo tĩnh; gắn socket hoặc chuyển động cả vật. | — |

**19 model:** 1 Tripo Biped (20 credit rig), 7 tự rig Blender (Kiếm tu, năm họ thú, Vương), 11 không rig. Không trả rig thêm cho bot/tướng/tinh anh/biến chủng. Nhân vật chữ ký, bốn chân cắn/vồ/húc, Viên tay dài và Điểu có cánh giao Blender; không chuyển sang Biped chỉ vì có tư thế A.

Sau GLB: Blender giảm LOD đám đông Low ≤1.000 / Medium ≤1.800 / High ≤3.000 tam giác; người 8.000–30.000, Vương 12.000–45.000 theo hợp đồng §21.2; phi kiếm 300–800. HN1 đo lại hình thật. “Vạn kiếm” dùng chung một mesh instanced 150/300/500 bản Low/Medium/High theo §20.2.

## 5. Lưu, kiểm và giao nhận

- PNG: `games/immortality-cultivation/art-src/<nhóm>/<id>.png`; đúng prompt cạnh ảnh: `<id>.prompt.txt`. Ảnh chưa tạo chỉ có prompt, không đặt PNG giữ chỗ.
- `art-src/.gitignore` bỏ qua toàn bộ hiện vật tại chỗ; bộ Markdown chia sẻ ở đây. Không sửa ignore/cấu hình media ngoài phạm vi, không chạy git. Anh kiểm cấu hình sao lưu media trước khi đẩy sau.
- Xem từng ảnh: số chi, góc, tư thế A, nền, bóng, chữ, hiệu ứng và đồng nhất hai góc. Prompt không thay cho kiểm; sai mã nền hoặc bóng nhẹ phải xử lý trước khi gửi Tripo.
- Sau dựng: kiểm thang mét, +Y lên, hướng trước, gốc chân, socket và clip tại chỗ; nướng VAT/impostor từ cùng GLB. Các việc này thuộc lượt sau.
- Không tạo âm trong phiếu này. Âm sau theo Q6: hành động quyết định chuẩn bị/phát/thân/đuôi vang, prompt khẳng định và qua Bảng Nghe.

## 6. Việc để lại

PB01-S (cạnh Thanh Phong Kiếm), PB02 (Hậu Thổ Ấn), BT01-S/F (Đằng Thử) và BT02-F/B (Khê Viên, M1) có prompt đầy đủ nhưng chưa có PNG vì hạn mức. Riêng T03-S đã tạo và thử lại một lần, vẫn cần sửa góc cánh ở lượt sau; hiện chỉ dùng T03-F. Phù, pet, Huyễn Hồ, Độc Mãng, Nham Quy, Lôi Điêu và thú đào hang là sau MVP (§10.2, §12.2), chưa chốt hình nên không tự thêm ảnh. Ảnh 2D dùng thẳng trong ước tính ~100 ảnh (UI, nền, VFX…) ngoài phiếu “mọi ảnh cho 3D”.

