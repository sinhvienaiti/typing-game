# Danh sách ảnh còn phải làm · Tu Tiên Thủ Ải (2D và 3D) · 11/11/2026

**Mục tiêu:** một danh sách duy nhất các ảnh 2D và model 3D còn mở, gom từ các tài liệu rải rác, đã đối chiếu với file trên đĩa.
**Cách đối chiếu:** chỉ `ls`/`find`/`grep`, không mở ảnh. "Có file" chưa có nghĩa là anh đã duyệt hay đã đạt 8,5.
**Viết tắt:** `S` = `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`; `A` = `games/immortality-cultivation/art-src`; `T` = `docs/games/tu-tien`; PLAN = `T/ART_AUDIO_VFX_PLAN.md`.

**Ghi chú của phiên điều phối (11/11 23:5x):** mục "Không chắc" về 40 ảnh vẽ lại nhìn từ trên đã được trả lời ở `DECISIONS.md` 11/11 16:00: engine chỉ đặt phẳng các vai trò dấu đất, vành nổ và va chạm đất; mọi vai trò khác là thẻ quay về camera, nên **không vẽ lại** ấn và vòng tụ lực.

## 1. Tóm tắt
- **2D còn mở: 28 dòng, khoảng 145 ảnh.** Trong đó 7 dòng đang đỗ (cut-in, mặt nạ A5/A6/A8), 3 dòng "sau demo" (khoảng 66 ảnh).
- **3D còn mở: 14 dòng, khoảng 22 model.** Trên đĩa mới có kiếm Clear Wind, hai rồng kỹ năng và 5 model mượn cho lab.
- **Phần kỹ năng gần như đủ ảnh:** 14 hệ đều có lưỡi liềm, sao băng, dấu đất, ấn, vòng tụ lực, hiệu ứng bám, 5 sigil, 3 vệt chém; 14 tuyệt kỹ, 4 cột trụ, 11 ảnh vũ khí, 30 kỹ năng mở rộng, bộ Ngũ Lôi, A9 đều có file.
- **Chỗ trống lớn là nền của bản chơi** (PLAN 01/11, chưa làm): nhân vật chính, quái, map 1, UI. Em chưa kiểm bản chơi hôm nay còn hộp xám hay không; PLAN §1 đo ngày 01/11.
- **5 việc giá trị nhất với người chơi:** (1) ảnh nguồn và model Kiếm tu nữ, lab đang dùng `lam.glb` mượn; (2) ý tưởng map 1 theo camera thật rồi đất, decal, viền; (3) quái: Phong Lang đổi texture từ `blight-wolf`, ảnh nguồn Thú Vương; (4) tranh màn tựa và 8 khung UI; (5) tách lớp dấu đất Hỏa (P1 của luồng làm lại ảnh).
- Ảnh Codex 331–338 hôm nay đã loại khỏi danh sách. Video Firefly còn thiếu (83 việc, cả bộ Ngũ Lôi) không tính ở đây vì không phải ảnh.

## 2. 2D còn thiếu

| id | Tên | Dùng ở đâu | Nguồn | Ảnh tham chiếu có sẵn | Công cụ | Ưu tiên | Ghi chú |
|---|---|---|---|---|---|---|---|
| | **VFX kỹ năng** | | | | | | |
| D01 | Dấu đất Hỏa tách lớp: nền đá RGBA/mặt nạ và lớp lửa phát sáng | kỹ năng (Hỏa, groundMark) | `docs/work/tasks/vfx-streams/stream-2-image.md` dòng S1-T0-fire-mark (P1, todo) | `S/fire-ground-mark.v1-try1.jpg` | Codex image_gen | 1 | Trên đĩa chỉ có try1; chưa có bản tách |
| D02 | Dấu đất Thủy tách lớp đá và năng lượng | kỹ năng (Thủy) | cùng file, dòng S1-17 (P4, todo) | `S/water-ground-mark-clean.v1-try1.jpg` | Codex image_gen | 2 | |
| D03 | Tuyệt kỹ Băng: sửa nhũ băng chạm mép dưới, thêm mặt nạ nền | kỹ năng (tuyệt kỹ Băng) | cùng file, dòng S1-18 (P4, todo) | `S/ult-ice-cold-silence-clean.v1-try1.jpg` | Codex image_gen | 2 | Chưa có bản v2 trên đĩa |
| D04 | Tuyệt kỹ Lôi: sửa mây cắt mép trên, thêm lớp mây tối | kỹ năng (tuyệt kỹ Lôi) | cùng file, dòng S1-19 (P4, todo) | `S/ult-thunder-nine-heavens-clean.v1-try1.jpg` | Codex image_gen | 2 | Xem mục 4.3: đã có bản v2 ngày 05/11 |
| D05 | B7 vạch nứt sáng Metal 2048×128, lặp theo x | kỹ năng (phím 7, vết cắt đất) | `T/skills/CODE_DRAWN_AUDIT_2026-11-05.md` §2 B7, bảng hàng 9 | `S/metal-rift-groove.v1-try1.*`, `S/metal-crack-star.v1-try1.*` | Codex image_gen | 2 | Không tìm thấy file dải nào trên đĩa |
| D06 | A5 mặt nạ áo khí Metal 2048×512, 2 bản | kỹ năng (hào quang kiếm) | `T/skills/INTEGRATION_PLAN_2026-11-04.md` hàng A5 | `A/lab/vfx/aura/strips/strip-metal-windsilk-v2.png` | Codex image_gen | 3 | **Đỗ** (`docs/work/BOARD.md` "Đỗ lại", bảng ngày 06/11) |
| D07 | A6 mặt nạ lửa bọc lưỡi 2048×512, 2 bản | kỹ năng (hào quang kiếm Hỏa) | cùng file, hàng A6 | `A/lab/vfx/aura/strips/strip-fire-sheath-v2.png` | Codex image_gen | 3 | **Đỗ** (BOARD) |
| | **Dấu đất và ấn** | | | | | | |
| D08 | B1 sáu mặt nạ glyph 256 px theo chiêu | kỹ năng (ấn chân, mọi phím) | `CODE_DRAWN_AUDIT` §2 B1, Lô 3 | `S/metal-caster-seal.v1-try1.*`, `A/lab/vfx/sigils/` | Codex image_gen | 3 | Ấn chân 14 hệ đã có; riêng 6 glyph không thấy file. Xem mục 4.5 |
| | **Sprite hạt** | | | | | | |
| D09 | A8 tấm sao B: 3 hàng cỡ cho 32, 20, 12 px, 3 bản | kỹ năng (sao mũi kiếm, lấp lánh) | `INTEGRATION_PLAN` hàng A8 | `A/lab/vfx/aura/glint-starburst-set.atlas.png`, `tip-star-glint.atlas.png` | Codex image_gen | 3 | **Đỗ** (BOARD). A9 đã xong hôm nay (337), chờ anh duyệt |
| | **Cut-in** | | | | | | |
| D10 | Tấm nền chữ gọi chiêu (nét bút lót dưới tên chiêu) | cut-in tuyệt kỹ | `T/skills/CUTIN_AUDIT_2026-11-04.md` §4 G5, §5 ý 5 | `A/skills/cutin/tt-cutin-c-*.png` | Codex image_gen | 3 | **Đỗ** (BOARD: "Sửa cut-in, phiếu 268"). Mới là đề xuất, chưa qua vòng duyệt |
| D11 | Khung mực sáng của dải cut-in (mép bút mực, viền trong sáng) | cut-in | cùng file §4 G3, §5 ý 2 | như trên; `A/lab/vfx/cutin/cutin-band-edge-light-loop-w2.*` | Codex image_gen | 3 | **Đỗ**. Dải sáng chạy viền đã có; mép vẽ thì chưa |
| D12 | Tách lớp tóc, ruy băng, tay áo từ 2 tranh cut-in C | cut-in | cùng file §4 G8, §5 ý 7 | `A/skills/cutin/tt-cutin-c-gather.v1-try1.png`, `tt-cutin-c-shout-e1.v2-try1.png` | Gemini (sửa ảnh) | 3 | **Đỗ**. Không được đổi mặt C3 |
| | **UI và icon** | | | | | | |
| D13 | Icon tuyệt kỹ Ám `ult-dark`, 2 hướng ink-gold và jewel-crest | UI (thanh chiêu) | `docs/codex-queue/316-report.md` ("Manifest không có `ult-dark`, nên không tự thêm") | `S/ult-dark-a.*`, `A/lab/ui/skill-icons/ink-gold-*.png` | Codex image_gen | 2 | Không có file `*ult-dark*` trong `A/lab/ui/skill-icons` |
| D14 | Tranh màn tựa `ui/title-key-art` 1920×1080 | UI (màn tựa) | PLAN §4.2, §3.1 bước 7 | `A/identity/kiem-tu-portrait.png`, `A/identity/thanh-thach-ai-55.png` | Gemini, cho anh chọn hướng | 2 | Chưa có file; tên game tiếng Anh (Q3) phải chốt trước |
| D15 | 8 khung 9-slice: Bàn Quyết, thanh HUD, thẻ đợt, cửa hàng, Thu Hoạch, menu, bảng Settings, bảng Sound | UI | PLAN §4.2 `ui/frames/*` | chưa có | Codex image_gen | 2 | Phải vẽ 1 ảnh mẫu cho anh chọn trước |
| D16 | 12 icon: đan phù ×3, cơ quan ×3, tiền ×3, settings, sound, sound-muted | UI (HUD) | PLAN §4.2 `ui/icons/*` | `A/lab/ui/skill-icons/` (hai hướng anh đã khen 06/11) | Codex image_gen | 3 | |
| D17 | Nhóm cũ: icon Thổ thể 7, Đạo Quả 6, cảnh giới 2; Sơn Môn 5 tranh, màn chờ 1; Tĩnh Tu 10 | UI | `T/art-requests/IMAGE_LIST.md` mục I, U, T; PLAN §4.4 | chưa có | Codex image_gen | 3 | "Sau demo". Danh sách từ 25/10, trước khi có 3 phái và 14 hệ; cần rà lại trước khi vẽ |
| | **Bản đồ và nền** | | | | | | |
| D18 | Ý tưởng map 1 vẽ đè ảnh nền có lưới, đúng camera chơi | bản đồ | PLAN §4.2 `concept/map1-camera`; `T/MAP1_CONCEPT.md` | `A/identity/thanh-thach-ai-55.png`; ảnh legend trong `tmp/plan-2026-11-01/` | Gemini (vẽ đè) | 1 | Không có `MAP1_CHATGPT_REVIEW.md`, không có file map1 trong `A` |
| D19 | 6 ô đất lặp (lớp phủ vết trận và rêu trên nền ambientCG) | bản đồ | PLAN §4.2 `ground/thanh-thach/*` | `A/lab/lookdev/PavingStones128`, `Rock035`, `Moss001` | Firefly Image | 2 | Sau D18 |
| D20 | 8 decal nền trong suốt | bản đồ | PLAN §4.2 `decals/thanh-thach/*` | chưa có | Codex image_gen | 2 | Sau D18 |
| D21 | 3 lớp viền ngoài sân nhìn từ trên 4096×1024 | bản đồ | PLAN §4.2 `backdrops/rim-*` | chưa có | Firefly Image | 2 | Sau D18 |
| D22 | 6 thẻ cỏ bụi nền trong suốt | bản đồ | PLAN §4.2 `foliage/*` | chưa có | Codex image_gen | 3 | |
| | **Nhân vật và quái (ảnh nguồn 3D)** | | | | | | |
| D23 | Kiếm tu nữ: ảnh nguồn trước và sau, tay mở 30° | nhân vật chính | PLAN §7 hàng 1; `T/art-requests/demo1/JUDGING.md` ("Không ảnh nào đạt", cao nhất 7,8/8,1) | `A/identity/kiem-tu-portrait.png`, `A/roster/kiem-nu.png` | Gemini, theo `game-character-design` | 1 | `A/cultivators/kiem-tu*.png` là bản Codex 25/10 đã trượt |
| D24 | Thiết Bối Lang Vương: ảnh nguồn ngang và trước | quái (Thú Vương) | PLAN §7 hàng 3; `demo1/JUDGING.md` | `A/kings/thiet-boi-lang-vuong*.png` (đã trượt, giữ thiết kế) | Codex image_gen | 1 | |
| D25 | Thạch Thử, Hỏa Nha, Nham Viên, Thiết Giáp Trư: ảnh nguồn 2 góc mỗi con | quái | PLAN §7 hàng 4–7; `demo1/JUDGING.md` | `A/beasts/*.png` (đã trượt) | Codex image_gen | 2 | Chỉ vẽ con nào không tái dùng được model (bảng 3) |
| D26 | Cổng ải vẽ lại: rộng, thấp, mái đẹp từ trên | bản đồ (công trình) | PLAN §7 hàng 9, §0.1 #2 | `A/props/cong-ai.png` (cao, sẽ bị cắt) | Codex image_gen | 2 | Phụ thuộc D18 |
| D27 | Khê Viên (biến chủng): 2 góc | quái | `IMAGE_LIST.md` mục A (`beasts/khe-vien`, "chờ 007b") | `A/variants/dang-thu.png` | Codex image_gen | 3 | Trên đĩa chỉ có 2 file `.prompt.txt`, không có ảnh |
| D28 | Ảnh nguồn 3D của danh sách nhân vật: phiếu 013 (11 ảnh), 013b (khoảng 22 ảnh) | nhân vật | `IMAGE_LIST.md` lô A2, A3 ("Đã có: 0") | `A/roster/*.png` (anh duyệt 25/10) | Gemini | 3 | "Sau demo" (PLAN §7 hàng 18–21) |

## 3. 3D còn thiếu

`docs/games/MONSTER_MODEL_INVENTORY.md` không tính Tu Tiên (dòng 5); ứng viên tái dùng lấy từ PLAN §0.1 #5 và §7. `docs/games/TRIPO_TODO.md` chỉ có một dòng Tu Tiên (kiếm Clear Wind, đã dựng).

| id | Tên | Nguồn | Ảnh nguồn 2D đã có chưa | Tái dùng model nào | Ưu tiên | Ghi chú |
|---|---|---|---|---|---|---|
| M01 | Kiếm tu nữ (rig người, 6 clip) | PLAN §7 hàng 1 | Chưa đạt (D23) | Không; lab mượn `A/lab/models/lam.glb` | 1 | 50.000 mặt |
| M02 | Phong Lang (sói, nhỏ) | PLAN §7 hàng 2; `demo1/JUDGING.md` (trượt 3 vòng, dừng vẽ) | Không cần nếu tái dùng | `blight-wolf` (Dragonhold), đã chép vào `A/lab/models/` | 1 | Đổi texture; tinh anh và Lang Đầu Đàn dùng chung |
| M03 | Thiết Bối Lang Vương (boss, 8–10 clip) | PLAN §7 hàng 3 | Chưa đạt (D24) | Không có boss sói | 1 | Đặt 45.000 mặt |
| M04 | Thạch Thử (bầy) | PLAN §7 hàng 4 | Có, chưa đạt | `kamaitachi` (Wordwoven), đã ở `A/lab/models/` | 2 | |
| M05 | Hỏa Nha (quạ bay) | PLAN §7 hàng 5 | Góc ngang chưa đạt | Không (`dai-bang-tinh` không hợp) | 2 | Cần D25 |
| M06 | Nham Viên (vượn đá) | PLAN §7 hàng 6 | Có, chưa đạt | Không | 2 | Cần D25 |
| M07 | Thiết Giáp Trư | PLAN §7 hàng 7 | Có, chưa đạt | `tusk-boar` (Dragonhold), đã ở `A/lab/models/` | 2 | Giáp bằng texture |
| M08 | Cổng ải (dùng 2 lần) | PLAN §7 hàng 9 | Phải vẽ lại (D26) | Không | 2 | |
| M09 | Trận Tâm | PLAN §7 hàng 10 | `A/props/tran-tam.png` (8,0/7,9, sát ngưỡng) | Không | 2 | |
| M10 | Trận Trụ | PLAN §7 hàng 11 | `A/props/tran-tru.png`, chưa đạt | Không | 2 | |
| M11 | Kiếm Thung, Lôi Phù Trụ, Phong Ấn Võng | PLAN §7 hàng 12–14 | `A/mechanisms/*.png`, chưa đạt | Không | 2 | 3 model |
| M12 | Đá vôi, Tùng cổ | PLAN §7 hàng 16–17 | Có, chưa đạt | Poly Haven, Quaternius (CC0) thử trước | 3 | Tùng cổ: sau demo |
| M13 | Thổ thể nam và nữ, trượng đá, bot Đạo Đồng | PLAN §7 hàng 18–21 | Chưa (D28) | Không | 3 | Sau demo |
| M14 | Mê Vụ Trận, Hậu Thổ Ấn | PLAN §7 hàng 22–24 | `A/mechanisms/me-vu-tran.png`, `A/treasures/hau-tho-an.png` | Không | 3 | Sau demo |

Không tính: Lang Đầu Đàn và các tinh anh (dùng GLB sói và lợn, PLAN §7 hàng 8); đầu rồng sạch `qi-dragon.v2-try1/2` (**đỗ**, BOARD: anh không muốn vẽ lại, 05/11 15:35).

## 4. Không chắc

1. **Dấu đất, ấn chân, vòng tụ lực của các hệ còn lại có cần bản nhìn thẳng từ trên không.** `docs/work/DECISIONS.md` 11/11 16:00 chỉ kiểm 131 việc làm lại và thấy 4 ảnh phải vẽ lại (đã xong ở 331, 334). Trên đĩa chỉ Ám, Quang, 2 dấu quái và vết sét có đuôi `-top`. 12 dấu đất, 14 ấn chân và 14 vòng tụ lực còn lại vẽ theo đuôi prompt "camera 55°" (`docs/work/tasks/images-0611.md`). Nếu engine đặt phẳng chúng thì sẽ bẹp hai lần: tối đa 40 ảnh vẽ lại. Đây là điểm chưa chắc lớn nhất.
2. **7 sao băng vẽ lại (312):** file `*-comet.v1-try2.png` đã có, nhưng báo cáo ghi "chưa kết luận đạt trên 8" và cổng chấm đã dừng (anh, 06/11 12:35).
3. **Tuyệt kỹ Thủy và Lôi:** anh đã loại hai video (đôi mắt, cuộn giấy; `docs/work/tasks/lab-flipbooks.md`). Bản `ult-*-v2` có trên đĩa từ 05/11, nhưng luồng 2 vẫn ghi sửa bản v1 của Lôi (D04). Không rõ bản nào là chuẩn.
4. **A5, A6, A10:** BOARD ghi đỗ, nhưng dải `strip-*-v2` (04/11) và `S/fire-caster-seal*`, bộ sigil Hỏa đã có. Có thể đã thay được; em không tìm thấy dòng nào nói đã thay.
5. **B1 glyph, B3, B5, B6 của bản rà hình vẽ bằng mã:** B3 (nứt, rãnh) và B6 (vết cháy) có file `*-crack-star`, `*-rift-groove`, `fire-scorch-erosion`; B5 (cột sáng) chỉ có video chữ → video `light-column-strike`, đang nằm ở `vfx-streams/evidence-missing.md`. Chưa thấy ghi anh đã chọn mẫu nào.
6. **Lớp bộ đếm chuỗi:** báo cáo 304 ghi chưa tách lớp sạch, nhưng `A/lab/ui/streak-counter/cut-*.png` và `manifest.json` có từ 06/11. Không rõ đã đủ dùng hay cần vẽ lại.
7. **A9 (337):** đã có 3 tấm, chờ anh duyệt; khổ 1254 không chia hết cho 4.
8. **Icon và tư thế cut-in cho Đao và Thương, model 3D Đao và Thương:** `T/skills/PRODUCTION_LIST_2026-11-05.md` §1 có 3 phái, nhưng không tài liệu nào đặt các ảnh này. Trên đĩa chỉ có tấm `A/weapons/sheet-dao*`, `sheet-spear*`, không có icon `dao-*`, `thuong-*`, không có GLB ngoài Clear Wind.
9. **9 thanh kiếm còn lại** (`T/art-requests/weapons/WEAPON_PROMPTS_9.md`, "Chưa vẽ: Clear Wind phải đạt trước"): đĩa có 5 ảnh `showcase-*` lẻ. Clear Wind còn nợ vòng ngọc (`docs/work/tasks/jade-ring.md`, dừng).
10. **Nhóm V của `IMAGE_LIST.md`** (18 kết cấu VFX) và 14 kết cấu ở PLAN §4.2: em coi là đã bị đợt Firefly 05/11 thay thế nên không liệt kê.
11. **BOARD.md ghi ngày 06/11**, cũ hơn các việc 07–11/11. `docs/games/QUALITY_RESCUE_2026-11-01.md` không có dòng Tu Tiên nào.

## Nhật ký
- 11/11 · Claude (agent) · lập danh sách từ các nguồn nêu trong cột "Nguồn", đối chiếu đĩa bằng `ls`/`find`/`grep`.

## Nợ theo D64 (12/11 09:2x): rà lại mọi trận pháp, ấn chân, sigil, dấu đất dạng trận theo chuẩn huyền bí tu tiên (vành chữ triện, bát quái, cánh sen, mây cuộn, lôi văn, nhiều vòng lồng); hình học cơ bản phải vẽ lại. Danh sách: 14 ấn tụ lực/caster seal các hệ, 5 sigil chiêu, dấu đất 14 hệ (các bản đã nhìn từ trên), ấn triệu hồi Thú Vương, vòng hú sói tướng.

## Anh duyệt (12/11 20:0x)
- **Bộ quái v3/v4 đạt** ("ảnh quái đạt r"): `art-src/kings/thiet-boi-lang-vuong.v3-{q,front}-final.png`, `art-src/beasts/{nham-vien,thiet-giap-tru}.v3-{q,front}-final.png`, `art-src/beasts/{hoa-nha,thach-thu}.v4-{q,front}-final.png`. Bước sau: hai giám khảo mù 8,5, rồi Tripo (vẫn chạy thử, chưa tiêu credit tới khi anh cho).
- **Màn tựa: bản bên phải** = tựa B, cổng ải hùng vĩ, nhân vật nhỏ trên tường thành: `art-src/ui/title-key-art.v1-try2.png`.
- **UI: jewel-crest** (anh, 12/11 20:2x, sau tấm so sánh `owner-review/2026-11-12/tu-tien/codex-images/ui-two-styles.jpg`): mẫu `art-src/ui/frames/ban-quyet-jewel-crest.v1-try1.png`, `art-src/lab/ui/skill-icons/ult-dark-jewel-crest.v1-try1.png`.
- **Bộ giao diện jewel-crest đạt** (anh, 12/11 21:0x): 7 khung `art-src/ui/frames/*-jewel-crest.v1-try*.png` + Bàn Quyết, 12 icon `art-src/ui/icons/hud-*-jewel-crest.v1-try*.png` (phiếu 369).
- **Bộ quái: anh bảo sửa lại** theo bốn lỗi giám khảo 368/368b (7,0 và 7,3).
- **Boss bản 7 đạt** (anh, 12/11 22:5x: "được r, dùng ảnh này đi"): `art-src/kings/thiet-boi-lang-vuong.v7-{q,front}-final.png` (hướng A "Sói Núi Đá", phiếu 370b). Bộ quái dùng: boss v7, `nham-vien`/`thiet-giap-tru` v3, `hoa-nha`/`thach-thu` v4.
