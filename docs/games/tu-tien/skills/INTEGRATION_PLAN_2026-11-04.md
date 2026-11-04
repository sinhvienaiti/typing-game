# Kế hoạch lắp lab chiêu: đưa ứng viên Firefly 6,5–7 lên 8,5 (04/11/2026)

**Trạng thái:** kế hoạch, Claude chốt. Chưa có mã game, chưa sinh ảnh hay video mới. Tài liệu này thay phần thiết kế khung đầu của phiếu 252 (đã dừng) và thay phiếu 253, 254 (đang giữ; xem §8).

**Mục tiêu:** đưa các lớp chiêu Kiếm × Kim và Kiếm × Hỏa từ 6,5–7 (hai giám khảo mù đêm 04/11) lên 8,5, và sửa các chỗ còn mở. Có 10 lớp:
1. áo khí Metal;
2. lửa bọc lưỡi Fire;
3. sao mũi;
4. thân lửa va chạm phím 1, cùng khung đầu và khung cuối;
5. tia lửa;
6. vòng ấn;
7. lót tối trên đá sáng;
8. vòng lặp không bóng chồng;
9. pha bùng cho hình đủ ngay khung 0;
10. tắt chậm.

> **Claude chốt (04/11/2026, khoảng 11:45).**
> - ChatGPT không qua quy trình, nên tài liệu này là **bản nháp lộ trình**. Mỗi gói sẽ có một lượt duyệt hai lần riêng, ngắn, ngay trước khi làm.
> - Luật PASS đã sửa theo đúng lời anh: "đúng, chính xác" (skill `agent-orchestration`). Câu hỏi 7 ở §9 vì vậy không còn phải hỏi anh.
> - Số phiếu Codex dời lên một bậc, vì 256 đã dùng cho `capture-prune`: CX-A → 257, …, CX-J → 266.
> - Ảnh chụp và video vào `typing-game-review/` (skill `review-folder`), không vào `captures/tu-tien/integration-r2` trong repo.

## Đầu vào và quy trình

**Đã đọc:**
- `AGENTS.md`; skill `game-vfx-production` cùng ba tệp tham chiếu; `agent-orchestration` cùng `references/double-review.md`.
- [`VFX_PRODUCTION_PIPELINE.md`](../../VFX_PRODUCTION_PIPELINE.md), nhất là §0, §2, §4, §5, §6 và §10.
- [`FIREFLY_OVERNIGHT_2026-11-04.md`](FIREFLY_OVERNIGHT_2026-11-04.md) và [`BLENDER_FIRE.md`](BLENDER_FIRE.md).
- Hai bài chấm mù: `games/immortality-cultivation/tmp/shots/overnight/judge-1.md` và `judge-2.md`.
- Quyết định của anh:
  - [`SWORD_AURA.md`](SWORD_AURA.md) §3.A và §7;
  - [`FIRE_STYLE.md`](FIRE_STYLE.md), khối "Quyết định của anh";
  - [`SWORD_READABILITY.md`](SWORD_READABILITY.md), khối "Quyết định của anh" và §9.
- Khối Tu Tiên đầu `docs/HANDOFF_CURRENT.md`; các phiếu 252–255 trong `docs/codex-queue/`; ba ảnh thử của 252.
- Mã game ở `1a78a82`, chỉ đọc. Tên module, lớp và hàm trong tài liệu này lấy từ mã đó.

**Duyệt hai lần** (skill `agent-orchestration`):

| Trợ lý | Kết quả | Bản lưu |
|---|---|---|
| ChatGPT (Chat, thinking High) | Lượt chạy 1: FAIL, FAIL, FAIL, dừng. Lượt chạy 2, với brief đã sửa: FAIL, FAIL, FAIL, dừng. **Không đạt** hai PASS liên tiếp | [`source/integration-plan-chatgpt-2026-11-04.md`](source/integration-plan-chatgpt-2026-11-04.md) |
| Gemini (4 Argon, Cao) | Rà soát bản sửa cuối của ChatGPT: FAIL, FAIL, PASS, PASS. **Đạt** | [`source/integration-plan-gemini-2026-11-04.md`](source/integration-plan-gemini-2026-11-04.md) |

- **Chỗ lệch khỏi quy trình.** Bước 3 chỉ cho Gemini lời giải đã qua. Vì ChatGPT trượt luật dừng hai lần, Claude đổi cách theo bước 7: đưa Gemini bản sửa cuối của ChatGPT, nói rõ bản này chưa đạt, và vẫn áp luật hai PASS cho Gemini.
- **Vì sao ChatGPT trượt.** Lời nhắc "chỉ PASS khi không cần đổi gì" đặt lên một tài liệu 30.000–85.000 ký tự thì lượt nào cũng còn chỗ để thêm. Mỗi lượt FAIL viết lại toàn bộ, dài hơn, mà không đổi hướng. Đề xuất sửa quy trình nằm ở §9.
- Hai trợ lý chỉ là tham chiếu. Mọi điểm dưới đây do Claude chốt, sau khi kiểm nguồn: trang Adobe helpx, mã three.js r170 trong `node_modules` của game, trang Khronos, tài liệu và commit của dự án. Bảng kiểm nằm trong hai tệp nguồn.

## 0. Tóm tắt các điểm đã chốt

1. **Mỗi hiệu ứng có ba nguồn.**
   - Hình do tranh vẽ quyết định.
   - Chuyển động bên trong lấy từ Firefly Video (clip gốc 24 fps còn đủ ở `~/VFXLab/inbox/firefly/immortality-cultivation/overnight/`).
   - Màu, lót tối, lõi nóng, thời điểm và độ xói do shader và code lo.
   - Code không vẽ hình chính. Blender theo cách tô bậc phẳng đã dừng.
2. **Mỗi lớp vẽ bằng một cách:**
   - áo khí và lửa bọc lưỡi: chính lưới `MantleSheath` sẵn có, đổi phần "nhìn" bên trong;
   - va chạm: thẻ một lần của `FlipbookPool`;
   - sao, tia lửa, bụi: sprite vẽ tay trên hạt instanced;
   - vòng ấn: ảnh alpha vẽ tay, chỉ dùng SDF khi đo thấy hơn.
3. **Lót tối và lõi sáng nằm trong cùng một fragment,** trộn premultiplied `ONE, ONE_MINUS_SRC_ALPHA` (công thức ở §2.3). Không thêm lớp nền, nên không vượt trần 2 lớp.
4. **Bỏ kiểu bọc vòng bằng hòa chéo.**
   - Áo và lửa bọc lưỡi dùng dải chuyển động lặp theo không gian và cuộn theo trục lưỡi.
   - Một vòng lặp theo khung chỉ được dùng khi đo đạt và mắt thấy liền. Không đạt thì chạy một lần.
5. **Bùng nhanh theo đúng chuẩn chung.** Chớp va chạm và đèn va chạm sáng ≥ 95 % đỉnh ngay ở tuổi 0 (`VFX_STANDARD.md` §3.1 luật 5, bảng L10 và đèn chớp). Thân lửa hiện dần theo thứ tự nét trong 2–4 khung.
6. **Tắt chậm.** Các nét xói theo một trường "sống sót" vẽ sẵn: đầu nhọn chết trước, gốc chết sau. Pha tắt dài ít nhất gấp ba pha bùng. Ở phím 1, lửa của đòn trước phải tan gần hết trước đòn sau (§2.6).
7. **Cổng C1** là ΔE OKLab ≥ 0,25 trong ảnh cuối, cách gộp ở §2.8. Weber không còn là cổng (đã chứng minh không đạt được với thép tối trên đá sáng).
8. **Thứ tự làm:**
   - làm ảnh và đo ngay, không đụng mã game;
   - mã Codex trên các tệp hộp xám chiêu rồng không đụng tới;
   - phần đụng `element-fire.ts`, `sword-skills.ts`, `src/sim`, `src/content` và `skills-main.ts` chờ hộp xám chiêu rồng và phiếu 255 vào xong;
   - sửa độ rõ T3, T1, T4, C1, C2, R1 làm sau cùng, sau khi hào quang vòng 2 vào.

## 1. Mỗi trợ lý góp gì, Claude không đồng ý chỗ nào

**ChatGPT góp** (qua hai lượt chạy):
- Tách ba lớp: hình vẽ là gốc, Firefly là chuyển động bên trong, runtime lo phần còn lại. Giữ `ff-f1-c4` làm chuyển động lửa và phiếu 252 v1/v3 làm hình va chạm.
- Hợp đồng shader "ink dưới, thân giữa, lõi trên" ở dạng phép over ba lớp (công thức của §2.3). Hai mặt nạ điều khiển tách nhau: một cho hình, ink, lõi và thứ tự sống sót; một cho thứ tự hiện.
- Không bọc vòng bằng hòa chéo. Dải lặp theo không gian `u' = fract(k·u − v·t + φ)` có pha riêng từng kiếm.
- Phát hiện cổng Weber ≥ 2 không thể đạt với thép tối trên đá sáng.
- Kiểm r170: `SMAAPass(width, height)`, không có `FXAAPass`, composer mặc định HalfFloat.
- Tách dữ liệu ra khỏi màu (`NoColorSpace`). Không lấy alpha từ nền đen như alpha thật.
- Ngưỡng R_seam ≤ 1,2. Bảng rủi ro. Danh sách lớp cũ phải tắt (hoa sen, tia nan bánh xe, vòng nhiệt, ấn đất, vết cháy code).
- Lời nhắc ảnh và Firefly cho mọi món.

**Gemini góp** (rà soát, đạt hai PASS):
- **Rủi ro C1 trên đá tối.** Thép tối trên `#2a2c30` chỉ đạt ΔE khoảng 0,05–0,10; Claude tính lại OKLab và thấy đúng. Nên mép nóng của lưỡi Fire phải đủ rộng và đủ sắc.
- Ink chỉ ở mép trong (khe 1 px), dưới gốc nét và trong lòng đường cong; 35–50 % ngoài cùng của mỗi lưỡi lửa không có ink. Đây là cách tránh viền "miếng dán".
- Bảng 10 lớp × 6 mặt (hình, chuyển động, ánh, lấp lánh, lót, nhịp). Số ứng viên cho từng món.
- Nhịp va chạm cụ thể: ngưỡng hiện `(tick + 1)/4`, hiện xong ở khung 3, giữ 5 khung, xói 24 khung.
- Công thức tách alpha từ clip nền đen cho `tools/vfx-flipbook`.
- Ý dùng chính mặt nạ áo hoặc lửa đã vẽ làm khung đầu cho Firefly Video, để chuyển động bị ép trong hình (giống cách của `ff-a1-c5`).
- Ý dùng stencil làm lưới an toàn cho C2.
- Lấy đường cắt sai số nhỏ nhất cho dải lặp.

**Claude không đồng ý:**

| Ý | Ai | Vì sao Claude không theo |
|---|---|---|
| Tắt hẳn `MantleHull` vì đang chồng 3–4 lớp lên lưỡi | Gemini | Sai theo repo: commit `6922420` đã sửa để vỏ không vẽ lên lưỡi, và cổng blade-keep đo được điều đó. Vỏ là lớp A2 anh duyệt, cần khi kiếm chĩa vào camera. Giữ nó và đo lại bằng cổng chồng lớp |
| `SMAAPass` r170 dùng target 8 bit nên phải đặt sau `OutputPass` | Gemini | Lý do sai: r170 dùng target `HalfFloatType`. Kết luận có cơ sở một phần, vì shader SMAA r170 có bước `pow(2.2)` rồi `pow(1/2.2)`, tức giả định đầu vào đã mã hóa gamma. Chốt: thử cả hai thứ tự trên r170; mặc định sau `OutputPass`; FXAA (`ShaderPass(FXAAShader)`) luôn sau `OutputPass` |
| Stencil là cơ chế chính cho C2 | Gemini | r170 mặc định `stencil = false` cho renderer và `stencilBuffer: false` cho render target, và scene vẽ vào target của `EffectComposer`; Gemini bỏ sót bước này. Hình học ngoài viền cộng `discard` trong hành lang lưỡi là đủ cho lớp áo. Stencil chỉ làm dự phòng nếu C2 vẫn > 5 % |
| Đặt thanh kiếm 1 xuất phát cách đích 110–132 px để có 12 khung bay chậm | Gemini | Tầm phím 1 là 12 m (canon §12.1), tức tới khoảng 456 px ở camera chơi; kiếm treo ở vai, không ở cạnh đích. T4 của anh đếm "giữa lúc hiện và lúc trúng", nên khung treo được tính (§6) |
| Ngưỡng C1: phân vị 10 % theo **điểm ảnh** | ChatGPT, Gemini | Quá chặt và khác cách §9 đã đo Metal (trung vị theo khung). Chốt cách gộp ở §2.8 |
| Lời nhắc J-RING "ba chi tiết ngọc xanh, đốc sen" | ChatGPT | Sai với thiết kế Clear Wind (`WEAPON_DESIGN.md`: vòng ngọc rỗng có hai khuyết mây, đốc giọt ngọc). Vòng ngọc đi đường shader trước (§3, gói G1) |
| "Camera nghiêng khoảng 55°" | ChatGPT | Không có nguồn, không dùng |
| Lúc nào cũng vẽ một mặt nạ ink riêng | ChatGPT, Gemini | Vẽ màu tối trên nền đen thì không thấy được. Chốt: ink lấy từ hình nét đã vẽ (đẩy lệch về mặt trong và dưới gốc, đứt đoạn theo chính khe hở của nét). Nếu giám khảo chê "miếng dán" thì mới nhờ ChatGPT vẽ mặt nạ ink trắng trên đen khớp đúng khung |
| Bỏ hẳn `ff-g1-c2` cho sao mũi | ChatGPT | Đây là bản 7/7 tốt nhất đêm qua. Làm hai bản và chấm mù A/B: bản `ff-g1-c2` đã gọt (bỏ khung rung, ép lõi, cắt còn 12 khung) và bản vẽ mới |

## 2. Chốt kỹ thuật chung

### 2.1 Mỗi lớp vẽ bằng gì, nằm ở đâu trong mã

| Lớp | Cách vẽ | Nguồn | Mã chạm (đường dẫn trong `games/immortality-cultivation/`) |
|---|---|---|---|
| 1 Áo khí Metal | `MantleSheath` (thẻ instanced dọc trục lưỡi, đọc bảng bề ngang 96×1) với mặt nạ áo vẽ tay và dải chuyển động cuộn; `MantleHull` giữ; `SilkTail` giữ; `MantleHalo` ở kiếm xa giữ dạng vạch mảnh | Mặt nạ: ChatGPT/Gemini vẽ. Chuyển động: `ff-m1-c3`, `ff-m1-c4` | `src/view/skills/aura-mantle.ts` (`WindSilkMantle`, `CARD_FRAGMENT`, `HULL_FRAGMENT`), `sword-aura.ts` (`SWORD_AURA_LOOK`, `applySwordAuraLook`), `element-kit.ts` (`SwordAuraLook`), `element-metal.ts` (`METAL_AURA`) |
| 2 Lửa bọc lưỡi | Như lớp 1, chế độ `flame`, mặt nạ lửa bất đối xứng; lưỡi lửa vẫn chỉ ở ≤ 14 kiếm (`FLAME_CAP`, `FLAME_MID_CAP`) | Mặt nạ: ChatGPT/Gemini. Chuyển động: `ff-f1-c4` (24 fps gốc), `ff-f1-c2` cho vệt | Như lớp 1, cộng hằng `FIRE_AURA` trong `element-fire.ts` |
| 3 Sao mũi | `TipStar` đổi từ sao giải tích (`STAR_FRAGMENT`, hàm `arm()`) sang đọc atlas sprite ba cỡ | A: `ff-g1-c2` đã gọt. B: tấm sao vẽ tay | `aura-mantle.ts` (`STAR_VERTEX`, `STAR_FRAGMENT`) |
| 4 Va chạm phím 1 | Thẻ một lần trong `FlipbookPool`, đọc atlas màu cộng hai mặt nạ điều khiển | Khung đầu và khung cuối sửa từ 252 v1/v3; chuyển động từ Firefly Video | `flipbook.ts` (`FlipbookPool`, `FlipbookMeta`, `parseFlipbookManifest`); `element-fire.ts` (`impact()`, thay `lotus()` ở đòn phím 1) |
| 5 Tia lửa, sao đòn, bụi | Pool sprite instanced mới: quỹ đạo đạn đạo tính trong vertex shader, kéo dài theo vận tốc, kẹp cỡ theo px | Tấm tia lửa và tấm bụi vẽ tay | Tệp mới `src/view/skills/spark-sprites.ts`, `glint-pool.ts`; đăng ký trong `element-stage.ts`; gọi từ `element-fire.ts` (`impact()`, `release()`), thay `sparkRays()`, `ember()`, `dot()` ở đòn phím 1 |
| 6 Vòng ấn | Ảnh alpha vẽ tay trên quad; hiện theo thứ tự đoạn, xói; chỉ đòn lớn | Hai mẫu ấn vẽ tay | Tệp mới `src/view/skills/painted-seal.ts`; gọi từ `release()` (phát chiêu từ ấn), `finisherSlash()`, `plant()` và kiếm dẫn đầu phím 7 khi bổ (`myriad-swords.ts`) |
| 7 Lót tối | Trong cùng shader của lớp 1, 2, 4, 6 (§2.3) | Lấy từ hình nét (§1) | Các shader trên |
| 8, 9, 10 | Hạ tầng chung trong `flipbook.ts` và shader áo | — | `flipbook.ts`, `aura-mantle.ts` |

### 2.2 Ảnh và mặt nạ

- **Atlas màu** lưu alpha thẳng; shader premultiply đúng một lần (như `FlipbookPool` hiện nay).
- **Mặt nạ điều khiển A (RGBA, dữ liệu, `NoColorSpace`):**
  - R = bao hình (độ phủ tối đa) vẽ tay;
  - G = ink;
  - B = vạch nóng;
  - A = thứ tự sống sót: đầu nhọn và mẩu rời thấp, gốc cao, mỗi nét lệch một chút để không tan đều nhau.
- **Mặt nạ điều khiển B (nửa độ phân giải, dữ liệu):**
  - R = thứ tự hiện: 0 ở gốc điểm chém, 1 ở mũi kim, các nét phụ 0,35–0,85;
  - G = ảnh hưởng của chuyển động.
- **Cách làm thứ tự hiện và thứ tự sống sót:** Claude tính từ hình nét đã vẽ, bằng khoảng cách dọc nét từ gốc. Đây là "đặt và nhịp" của hình vẽ, không phải code vẽ hình.
- **Áo và lửa bọc lưỡi:**
  - mặt nạ áo vẽ ngang 2048×512, mũi bên phải, có hành lang lưỡi trống ở giữa;
  - shader ánh xạ trục dọc của ảnh theo khoảng cách tới mép lưỡi (lấy từ `tProfile`), nên hành lang luôn ôm đúng viền thật;
  - dải chuyển động 512×128 (hoặc 1024×128), lặp theo u.
- **Manifest** thêm trường, giữ tương thích ngược: `rows/variants`, `frameRange`, `controlA`, `controlB`, `anchor`, `sourceFps`, `loopMode`, `timingProfile`. Tệp cũ thiếu trường mới chạy y như cũ.

### 2.3 Hợp đồng shader: ink, thân, lõi trong một fragment

Gọi độ phủ của ink, thân và lõi là `a_i`, `a_b`, `a_h`; màu tuyến tính là `C_i`, `C_b`, `C_h` (`C_h` HDR, chỉ ở vạch nóng):

```
α   = 1 − (1 − a_i)(1 − a_b)(1 − a_h)
RGB = C_i·a_i·(1 − a_b)(1 − a_h) + C_b·a_b·(1 − a_h) + C_h·a_h
trộn: ONE, ONE_MINUS_SRC_ALPHA (đã premultiply, không nhân alpha lần nữa)
```

- Đây là phép over ba lớp: lõi trên, thân giữa, ink dưới. Claude kiểm bằng toán.
- **Trần:**
  - thân ≤ 0,85–0,9 mỗi kênh;
  - lõi ≤ 5 % diện tích sáng;
  - ink alpha: Metal 0,35 (đã có trong `METAL_AURA`), Fire bắt đầu 0,45–0,7 (thấp hơn soot 0,85 hiện nay, theo cả hai trợ lý), đứt đoạn 20–35 %.
- **Kiểm:** Codex dựng ô mẫu (không phủ, phủ một phần, phủ đủ) trên đá sáng và đá tối, so GPU với bản CPU, sai số ≤ 1/255.
- **HDR đã được kiểm:** `EffectComposer` r170 dùng target HalfFloat, và `UnrealBloomPass` có ngưỡng 1,0, nên lõi > 1 tới được bloom.

### 2.4 Vòng lặp không bóng chồng

- **Áo và lửa bọc lưỡi.**
  - Viền áo đứng yên trong hệ tọa độ lưỡi; chỉ chi tiết bên trong chạy.
  - Claude dựng dải lặp từ clip gốc 24 fps: chọn vùng có sợi hoặc lưỡi lửa chạy đều, nắn theo trục, nối hai mép trái và phải bằng đường cắt sai số nhỏ nhất (cách đêm 04/11 đã dùng cho `aura-fire-ribbon`, `aura-metal-windsilk`). Không hòa chéo cả khung.
  - Shader dùng `u' = fract(k·u − v·t + φ)`: `RepeatWrapping` theo u, `ClampToEdgeWrapping` theo v. Tốc độ theo vận tốc kiếm, chiều luôn bạt về sau. Mỗi kiếm có pha φ riêng.
  - Có thể lấy hai mẫu với hai tốc độ trong cùng shader để bớt cảm giác "giấy dán tường".
  - Nếu sau ba lượt dải cuộn vẫn đọc như đứng im, đổi sang atlas độ phủ có chuyển động trên cùng lưới.
- **Vòng lặp theo khung** (chỉ khi thật cần):
  - chọn đoạn có R_seam = D(khung cuối, khung đầu) / trung vị D(hai khung liền nhau) ≤ 1,2;
  - phát `stepped` hoặc "hold and erode", không hòa chéo bọc vòng;
  - xem 20 vòng ở tốc độ thật và 0,25×;
  - không đạt thì chạy một lần.
- **Va chạm, sao, tia lửa, ấn:** không lặp.

### 2.5 Bùng nhanh

- **Tuổi 0:** chớp va chạm (sprite nhỏ) và đèn va chạm ở ≥ 95 % đỉnh của chính chúng, đúng luật "khung đầu đủ sáng" (`VFX_STANDARD.md` §3.1 luật 5). Sao lớn của đòn cũng lóe ở tuổi 0.
- **Thân lửa** hiện theo mặt nạ B.R với ngưỡng `T(tick) = clamp((tick + 1)/4, 0, 1)` (TRIAL, của Gemini):
  - tuổi 0: gốc nét 25 %, nằm trong chớp;
  - tuổi 1: 50 %;
  - tuổi 2: 75 % và các nét phụ;
  - tuổi 3: đủ quạt.
- Nét hiện ra đã giữ đủ màu và độ sáng, không mờ dần lên.
- Sáu chỗ hình "bật ra" mà giám khảo chê (`fire-crescent-sweep`, `fire-brush-slash`, …) đều qua cùng cơ chế này.

### 2.6 Tắt chậm

- Mỗi điểm ảnh còn sống khi `smoothstep(e(t), e(t) + w, A)` với `A` là thứ tự sống sót, `w` = 0,06–0,12 (TRIAL).
- Phần còn sống được tô lại theo dải màu bậc (`r = clamp((A − e)/(1 − e))`): từ trắng vàng tới cam, đỏ thẫm, rồi bồ hóng. Không mờ đều cả thẻ. Đây là `cool` và `erode` sẵn có của `FlipbookPool`, mở rộng theo trường A.
- **Nhịp va chạm phím 1** (TRIAL, khung 60 Hz):

  | Tuổi | Pha |
  |---|---|
  | 0 | chớp, đèn, sao lớn; gốc nét |
  | 1–3 | thân hiện |
  | 4–9 | giữ hình, lửa vẫn cuộn bên trong, vạch nóng lấp lánh |
  | 10–20 | đầu nhọn và nét phụ xé trước, phần sáng lớn tan gần hết |
  | 20–42 | chỉ còn mẩu than và bụi vàng thưa |

- **Đòn sau tới khi đòn trước mới 18 khung tuổi** (+18, rồi +36). Cổng TRIAL: ở tuổi 18, phần thân sáng còn ≤ 15 % đỉnh. Than hồng thưa được ở lại lâu hơn.
- Pha tắt dài ít nhất ba lần pha bùng.
- **Áo và lửa bọc lưỡi:** hiện trong 3–6 khung, tan khi về hoặc tan trong 9–21 khung, theo cùng ngưỡng nhiễu với lưỡi (như `iFx.z` hiện nay).

### 2.7 Lấp lánh có định mức (không sao clip-art)

| Hình | Lấp lánh | Trần |
|---|---|---|
| Áo Metal | hạt sáng chạy dọc hai đường may, lõi ≤ 1 px, mỗi điểm ảnh sáng đỉnh ≤ 2 khung (luật của `SWORD_AURA.md` §7) | kiếm chủ và kiếm giữa |
| Lửa bọc lưỡi | vài điểm nóng ở đầu lưỡi lửa | ≤ 2 mỗi kiếm |
| Sao mũi | một sao mỗi kiếm chủ, lóe theo chu kỳ 1,4–2,2 s, nền 0,6 | kiếm chủ phím 7 và kiếm phím 1 |
| Đòn phím 1 | sao lớn ở tuổi 0, hai sao nhỏ ở +4 và +9; 10–18 tia lửa trong 2–3 chùm, ba độ dài, rơi theo trọng lực, 10–20 % nảy một lần; 4–10 hạt bụi vàng | mỗi đòn |
| Dòng sông phím 7 | ánh viền chạy; sao chỉ trên ngọn sóng sáng | trần chung 48 sao sống (`FIRE_STYLE.md` §5.3) |
| Vòng ấn | 3–5 điểm sáng chạy trên vòng | chỉ đòn lớn |

Mọi màu tránh `#FF4A4A`, `#7FF5E0`, `#FFC83A`. Trên đá sáng, sao có viền tối mảnh và đứt đoạn.

### 2.8 Số đo và cổng

| Đo | Cách đo | Ngưỡng |
|---|---|---|
| Khung đầu ≥ 95 % đỉnh | Độ sáng vùng chớp và đèn va chạm ở tuổi 0 so với đỉnh của chính chúng | ≥ 0,95 (REQUIRED) |
| Trắng xóa | Điểm ảnh có độ sáng ≥ 0,95 trên vùng sân, mọi khung; vùng của hiệu ứng ghi riêng để chẩn đoán | ≤ 6 %; tuyệt kỹ ≤ 15 % trong tối đa 3 khung (`VFX_STANDARD.md` §4.2) |
| ΔE trên đá sáng và đá tối | OKLab (Ottosson) trên ảnh cuối đổi về tuyến tính, so cùng khung tắt lớp đó; trung vị trên vùng phủ của lớp | thân ≥ 0,12, điểm nhấn ≥ 0,18 (TRIAL, chỉnh theo giám khảo) |
| C1 (lưỡi Fire) | Mỗi khung: trung vị ΔE của điểm ảnh lõi lưỡi (bỏ 1 px mép răng cưa) so với cùng khung chỉ có nền thật; gộp: phân vị 10 % của các trung vị theo khung, tách lúc chờ và lúc bay, trên cả hai nền | ≥ 0,25. Cách gộp này là Claude chốt (khớp cách đo Metal ở `SWORD_READABILITY.md` §9.3); phân vị 10 % theo điểm ảnh ghi để chẩn đoán |
| C2 | Phần lưỡi bị VFX phủ khi bay, tính cả quạt lửa sau vai và vệt; dùng mặt nạ lớp cộng chênh lệch bật/tắt để bắt bloom tràn | ≤ 5 % |
| Blade-keep, vòng ngọc | Cổng sẵn có (`src/lab/aura-gates.ts`, `tmp/shots/sword-aura/tools/gates.py`) | ≥ 90 % kiếm chủ và giữa, ≥ 85 % kiếm xa; vòng ngọc và chắn ≥ 95 % mọi khung |
| Chồng lớp | `partsCoverage` sẵn có, thêm hạt và vệt | ≤ 2 lớp trong vùng mỗi kiếm |
| Thời gian GPU mỗi lớp | Không có truy vấn thời gian GPU trên ANGLE/Metal (`AuraGpuTimer` không chạy). Dùng `__lab.perf` (CPU cộng đọc 1 điểm ảnh, là cận trên), bật và tắt từng lớp, xen kẽ A/B/B/A; cửa sổ như `lab-element-perf.mjs` | Metal: hào quang ≤ +0,6 ms p95 lúc săn phím 7. Fire hơn Metal ≤ 0,85 ms p95. Mọi cửa sổ p95 ≤ 11,5 ms. Định mức tạm ở §2.9 |
| Mối nối vòng | Theo khung: R_seam ≤ 1,2. Dải theo x: chênh mép trái-phải ≤ 1,2 lần trung vị chênh hai cột trong liền nhau (cách đo đêm 04/11). Cả hai: xem 20 vòng ở 0,25× không thấy vạch, bóng hay giật | |
| Khung đầu và khung cuối (va chạm) | Đo trên ảnh vuông: 3 nét chính; cung mỗi nét 120–180°, đo bằng khớp đường tròn Kåsa trên đường tâm; dày ở 20 % chiều dài ≥ 3 lần dày ở 80 %; vạch nóng 2–6 % diện tích sáng; lề 8 %. Khung cuối: diện tích sáng 15–35 % khung đầu, ≥ 70 % nằm trong mặt nạ khung đầu nở 12 px, lệch ≤ 4 px | Lấy nguyên các ngưỡng của phiếu 252 |
| Thân sáng còn lại | ở tuổi 18 (đòn kế tiếp) | ≤ 15 % đỉnh (TRIAL) |

### 2.9 Định mức thời gian khung (TRIAL)

| Lớp | Phím 7 High, p95 |
|---|---|
| Áo Metal (thẻ, vỏ, đuôi, viền kiếm xa) | ≤ 0,45 ms |
| Sao mũi | ≤ 0,08 ms |
| Dự trữ Metal | 0,07 ms |
| **Tổng Metal** | **≤ 0,60 ms** (REQUIRED) |
| Lửa bọc lưỡi hơn áo Metal | ≤ 0,45 ms |
| Tia lửa, bụi, sao đòn | ≤ 0,20 ms |
| Ấn (khi có) | ≤ 0,10 ms |
| Dự trữ Fire | 0,10 ms |
| **Fire hơn Metal** | **≤ 0,85 ms** (REQUIRED) |
| R1 khử răng cưa | đo riêng, nằm trong 11,5 ms của mọi cửa sổ |

Từng con số không cộng thẳng được; số đo lúc bật cả bộ là số quyết định.

### 2.10 Chụp và chấm

- **Bản để chấm:**
  - bản cố định của lab, xuất bằng `git archive` (như `tmp/owner-preview`), chạy server riêng không HMR;
  - High, 1920×1080, DPR 1, camera chơi, cờ mặc định, không cờ URL;
  - tốc độ thật và 0,25×.
- **Ảnh chẩn đoán** (không dùng để chấm đạt): đá sáng `#d6d0c2` và đá tối `#2a2c30` qua cờ `ground` của lab; cận cảnh 400–500 px; từng lớp riêng.
- **Kịch bản chụp:**
  - `scripts/visual/scenarios/lab-sword-aura.mjs` (`PLAN=owner|gates|perf|smooth`);
  - `lab-element-fire.mjs`;
  - `lab-element-perf.mjs` (`QS=`);
  - kịch bản mới `lab-vfx-gates.mjs` (gói CX-A);
  - chạy qua `.local/bin/heavy.sh --gpu`.
- **Nơi lưu** (skill `review-folder`): ảnh làm việc ở `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/integration-r2/<gói>/`, mỗi thư mục có `ABOUT.md`; video gửi anh ở `owner-review/<ngày>/tu-tien/integration-r2/`. Xong mỗi bước, xóa khung thô của mình.
- **Chấm mù:**
  - hai giám khảo độc lập (agent con), không biết mã ứng viên, prompt hay bản nào mới;
  - mỗi người xem video tốc độ thật và 0,25× cùng dải khung ở camera chơi, rồi một bộ cận cảnh riêng;
  - mỗi người ghi điều thấy trước khi cho điểm, theo `quality-rubric.md`.
- **Đạt** khi cả hai ≥ 8,5, không lấy trung bình, và mọi cổng số đều qua. Món nào ≥ 7 thì gửi anh video demo, rồi làm tiếp.
- Ba lượt không lên điểm theo cùng một cách thì dừng cách đó và bàn lại.

## 3. Gói việc theo thứ tự

**Ký hiệu người làm:**
- **AI-vẽ** = ChatGPT (Chat, thinking High), rồi Gemini khi ChatGPT chạm giới hạn ảnh, Codex chỉ khi cả hai đã chạm giới hạn;
- **FF** = Claude chạy Firefly (chỉ model Adobe);
- **CX** = Codex, model `gpt-6.1-sol`;
- **CL** = Claude.

Anh xem mọi mẫu trước khi nối vào lab.

### Giai đoạn A: làm ngay, không đụng mã game (song song với hộp xám chiêu rồng và phiếu 255)

| Gói | Lớp | Nguồn | Công cụ, người làm | Ra gì | Kiểm |
|---|---|---|---|---|---|
| A1 Đo nền | tất cả | bản lab hiện tại (`1a78a82`) | CL, kịch bản sẵn có | ảnh và số nền: hoa sen, hào quang vòng 1, sao giải tích; đo trắng xóa, ΔE, khung đầu, chồng lớp, thời gian khung | số nền ghi ở `captures/tu-tien/integration-r2/baseline/` |
| A2 Khung đầu va chạm | 4 | `fire-impact-k1-v1.try1.png`, `v3.try1.png` | AI-vẽ (sửa ảnh, 2 bản v1, 1 bản v3), CL đo | ảnh vuông 1080 nền đen đục | các ngưỡng khung đầu ở §2.8; anh chọn v1 hoặc v3 |
| A3 Khung cuối va chạm | 4, 10 | khung đầu đã chọn | AI-vẽ (sửa ảnh, 2 bản), CL đo | khung cuối khớp vị trí | các ngưỡng khung cuối ở §2.8 |
| A4 Video va chạm | 4, 9, 10 | A2 + A3 | FF: Firefly Video, khung đầu và khung cuối, 1:1 1080p nền đen, tắt trong suốt, 24 fps 5 s; 3 lượt (2 cho bản chọn, 1 cho bản kia nếu anh muốn so) | clip gốc; CL chọn đoạn 12–24 khung có chuyển động tốt; atlas màu 24 khung 24 fps ô 384 (256 cho bậc thấp); mặt nạ A và B | đo hình trên mọi khung của đoạn (3 nét, cung, độ thuôn); bỏ lượt nào khép thành chữ C; ba lượt hỏng thì giữ hình vẽ làm bao và chỉ lấy chuyển động bên trong (dự phòng của cả hai trợ lý) |
| A5 Mặt nạ áo Metal | 1 | thiết kế A của anh | AI-vẽ, 2 bản (mảnh góc cạnh / sợi lụa) | 2048×512, hành lang lưỡi trống | hành lang trống (độ sáng < 0,05); ≥ 60 % khoảng trống trong bao; không có khối trắng; sắc 185–225°, không vàng, không xanh lục; anh chọn |
| A6 Mặt nạ lửa bọc lưỡi | 2 | — | AI-vẽ, 2 bản (lưỡi dài / lớp ngắn) | 2048×512 | bạt về sau: diện tích nửa trái ≥ 1,2 lần nửa phải; không có cục ở 15 % bên trái; mũi kim ở 5 % bên phải ≤ 25 % bề cao (Kiểm 8, 9 của phiếu 253); anh chọn |
| A7 Dải chuyển động | 1, 2, 8 | clip gốc `ff-m1-c3`, `ff-m1-c4`, `ff-f1-c4`, `ff-f1-c2` | CL (numpy/scipy/Pillow, ffmpeg, `tools/vfx-flipbook`) | dải lặp 512×128 hoặc 1024×128, Metal và Fire | mối nối dải theo x như §2.8; xem 20 vòng; nếu không cứu được thì FF chạy 2 lượt mới, lấy mặt nạ A5/A6 làm khung đầu (ý của Gemini) |
| A8 Sao | 3, 5 | `ff-g1-c2`, `ff-g1-c3` (biến thể 1, 2, 3, 4, 6) | CL gọt bản A; AI-vẽ tấm B (3 bản, 3 hàng cỡ cho 32, 20 và 12 px) | atlas sao A và B | lõi trắng ≤ 6 % vùng sao; tâm không nhảy > 1 px ở cỡ 24 px; ở 12 px vẫn ra bốn cánh; tỉ lệ cánh/lõi ≥ 3,5 |
| A9 Tia lửa và bụi | 5 | (bản cũ chỉ để so) | AI-vẽ: 2 tấm tia lửa, 1 tấm bụi | atlas sprite | ba độ dài rõ; không đốm tròn; khoảng trống giữa các ô |
| A10 Ấn | 6 | (`ff-c3-c3` chỉ để so) | AI-vẽ, 2 mẫu | 1024 vuông | tròn đều (sai lệch bán kính ≤ 1,5 %); lòng trống; ở 100 px vẫn tách ≥ 2 vòng với rãnh tối hơn đỉnh ≥ 35 % (Kiểm 8–10 của phiếu 254); anh chọn |
| A11 Mặt cut-in C3 | cut-in | `art-src/skills/cutin/tt-cutin-c-shout-e3-head-skin-up2x.v2-try1.png` (3671×1713) | FF: Firefly Upscaler (model Adobe, không dùng Topaz) | bản nâng cỡ để so | chỉ thay khi cận cảnh sắc hơn mà không đổi mặt hay màu da (skin match đã nướng sẵn); anh xem mẫu |
| A12 Cập nhật skill | — | `VFX_PRODUCTION_PIPELINE.md` §10 mục 4, cộng bài học của kế hoạch này | CL, sửa `.agents/skills/game-vfx-production/references/*` rồi `scripts/sync-agent-skills.sh` | skill mới | gồm: Firefly là tài sản cuối khi đạt; khung đầu đục nền đen 1:1 1080p; cấm nâng cỡ video; không bọc vòng bằng hòa chéo; hợp đồng ink, thân, lõi; ngưỡng khung đầu |

**Mốc A:** gửi anh một tấm mẫu và video ngắn cho mỗi món, chờ anh chọn. Chỉ bản anh chọn mới sang giai đoạn B và C.

### Giai đoạn B: Codex, chỉ những tệp hộp xám chiêu rồng và phiếu 255 không đụng

Mỗi gói là một phiếu Codex có lời giải đầy đủ (§7). Codex làm trong worktree riêng `games/.wt-immortality-cultivation-codex`; Claude đọc diff, chạy lại phép kiểm, rồi mới gộp.

| Gói | Lớp | Mã chạm | Kiểm bắt buộc |
|---|---|---|---|
| CX-A Đo cổng VFX | đo | `tools/vfx-flipbook/` (repo cha: R_seam, mối nối dải x, đo cung, độ thuôn, vạch nóng trên ảnh tĩnh); kịch bản mới `scripts/visual/scenarios/lab-vfx-gates.mjs` (khung đầu, trắng xóa sân và vùng, ΔE hai nền, thân sáng ở tuổi 18, chồng lớp, C1 và C2 theo §2.8) | chạy lại trên số nền A1 cho đúng số |
| CX-B `FlipbookPool` bản 2 | 4, 7, 8, 9, 10 | `src/view/skills/flipbook.ts`; test mới `tests/view/flipbook-v2.test.ts` | `loopMode` none/stepped/holderode, không còn hòa chéo bọc vòng; manifest tương thích ngược (atlas cũ y nguyên từng điểm ảnh); mặt nạ A và B; công thức §2.3 khớp bản CPU ±1/255; ngưỡng hiện và xói theo tick; `tsc`, `vitest` đều qua |
| CX-C Vòng ngọc | lưỡi | `src/view/skills/sword-material.ts` (mặt nạ vòng theo hình học `ring.y ± ring.r` của `AuraAnchors` thay mặt nạ `JADE` theo sắc), `real-swords.ts` (dùng `ringU`, `ringR` vốn đã khai báo mà chưa dùng), `blades.ts` nếu cần anchor | vòng giữ ≥ 95 %; Metal trùng khít ngoài vùng vòng (`lab-element-parity.mjs`); ảnh trước và sau gửi anh |
| CX-D Hào quang vòng 2 | 1, 2, 7, 8 | `aura-mantle.ts` (`CARD_FRAGMENT`, `HULL_FRAGMENT`, `WindSilkMantle`), `sword-aura.ts` (`SWORD_AURA_LOOK`, `applySwordAuraLook`), `element-kit.ts` (trường mới trong `SwordAuraLook`: mặt nạ áo, dải chuyển động, tốc độ, ink), `element-metal.ts` (`METAL_AURA`), riêng hằng `FIRE_AURA` trong `element-fire.ts` | blade-keep và vòng ngọc như §2.8; khe mực 1 px đo trên ảnh cuối; `discard` trong hành lang lưỡi; chồng lớp ≤ 2; thời gian theo §2.9; `?aura=off` trùng khít bản cũ |
| CX-E Sao mũi bằng sprite | 3 | `aura-mantle.ts` (`STAR_VERTEX`, `STAR_FRAGMENT` đọc atlas; 3 cỡ theo px trên màn; nhịp: lên 2 khung, giữ 3, thu 8; lấp lánh chu kỳ 1,4–2,2 s) | như A8 nhưng đo trong lab; A/B giữa sao A và sao B |
| CX-F Tia lửa, sao đòn, bụi | 5 | tệp mới `src/view/skills/spark-sprites.ts` (quỹ đạo đạn đạo trong vertex shader, kéo dài theo vận tốc, nảy một lần ở mặt đất y = 0, ba họ độ dài, kẹp cỡ px) và `glint-pool.ts` (sao vẽ tay, chuỗi 0/+4/+9); test | không cấp phát mỗi khung; một lệnh vẽ mỗi pool; phân bố hướng ±10–25° quanh tiếp tuyến nhát chém; không quá 1 lần nảy |

### Giai đoạn C: sau khi hộp xám chiêu rồng vào và phiếu 255 đã gộp

| Gói | Lớp | Mã chạm | Kiểm bắt buộc |
|---|---|---|---|
| CX-G Nối lab | tất cả | `src/lab/skills-main.ts` (cờ `?aura=a2`, `?impact=brush\|lotus`, `?star=ff\|paint`, `?seal=paint`; nạp atlas và mặt nạ mới, thay khối nạp `qi-streak-*`; nạp thư mục `aura/` qua `FlipbookPlayer`), `src/lab/aura-gates.ts` (đo lớp mới) | lab mở không cờ thì ra bản đã chọn; mọi cờ cũ vẫn chạy |
| CX-H Va chạm phím 1 bản 2 | 4, 5, 9, 10 | `src/view/skills/element-fire.ts`: `impact()` gọi thẻ một lần mới thay `lotus()`; chớp và đèn ở tuổi 0; sao và tia lửa qua CX-F thay `sparkRays()`, `ember()`, `dot()`; tắt vòng nhiệt, ấn đất và vết cháy code ở đòn thường; đăng ký pool trong `element-stage.ts` | khung đầu ≥ 95 %; trắng xóa ≤ 6 %; thân sáng ≤ 15 % ở tuổi 18; Fire hơn Metal ≤ 0,85 ms; không có lớp cũ nào còn vẽ ngầm (kiểm theo tên qua `__lab.fxNamed`) |
| CX-I Ấn vẽ tay | 6 | tệp mới `src/view/skills/painted-seal.ts`; gọi từ `release()`, `finisherSlash()`, `plant()` trong `element-fire.ts` và lúc kiếm dẫn đầu bổ trong `myriad-swords.ts` | chỉ đòn lớn; ở 100 px ra ≥ 2 vòng; nhịp hiện 6–10 khung, giữ 6–10, xói 18–30 |
| CX-J Độ rõ kiếm (§6) | T3, T1, T4, C1, C2, R1 | `src/content/data/school-kiem.ts` (`hitTicks` `[18, 36, 66]`), `src/sim/skills.ts` (thời điểm phóng), `src/view/skills/sword-skills.ts` (`T_K1_HITS`, `castK1`, `k1Launch`, `updateK1`, `BLADE_IN_S`), `docs/games/tu-tien/00-canon.md` §12.1, test sim liên quan, `src/kit/three/stage.ts` (R1) | T4, T1 như §6; C1 ≥ 0,25 trên cả hai nền; C2 ≤ 5 %; R1 nằm trong 11,5 ms; test sim cập nhật có chủ đích (`scripts/balance/golden.ts` còn là TODO, chưa có tệp golden để cập nhật) |

### Giai đoạn D: chấm và trả anh

1. CL dựng bản cố định cho anh (`ic-owner-preview`, xuất bằng `git archive`), mặc định là bản đã chọn.
2. Chụp theo §2.10, hai giám khảo mù chấm, gửi anh video.
3. Món nào dưới 8,5 thì quay lại đúng gói của lớp đó.
4. Khi mọi lớp ≥ 8,5, đưa chiêu vào bản dựng của game. Lúc đó media phải có đường từ `art-src` tới `public` của bản dựng, như hai trợ lý nhắc. Việc này ngoài phạm vi kế hoạch này.

## 4. Ảnh mới và lời nhắc

Lời nhắc dưới đây lấy từ hai trợ lý; Claude sửa chỗ sai và gộp lại. Mọi ảnh vẽ trên nền đen đục, không gửi kèm ảnh nào của game khác. Riêng khung đầu va chạm thì gửi kèm ảnh 252 của chính dự án.

**A2. Khung đầu, sửa từ 252 v1 (bản chính; gửi kèm `fire-impact-k1-v1.try1.png`):**
> Edit the attached artwork into an opaque pure-black 1080x1080 square without stretching. Center the whole fan while keeping the strike origin at lower left, sweeping up-right. Keep three separate OPEN flame crescents, each curving between 120 and 180 degrees, never closing into a ring or a C, with heavy irregular roots tapering to fine needle tips, tip at most a third of the root width. Add four or five small counter-strokes, a few detached licks, a razor-thin white-gold line along each leading outer edge (under 5 percent of the lit area) and two or three pin-point glints. Stepped orange-red anime/donghua flame with soft living interiors. No lotus, bird shape, sticker edge, smoke, ground, sword or text.

**A2. Khung đầu, sửa từ 252 v3 (bản phụ):** như trên. Câu mô tả nét đổi thành: "Keep its two long crescents and the short counter-stroke, resolved into three distinct open strokes".

**A3. Khung cuối (sửa ảnh, chỉ gửi kèm khung đầu đã chọn):**
> Edit the attached image. Keep every stroke exactly where it is; do not move, add or extend anything. Show the same three strokes after they have burned down: needle tips torn into small separated fragments, middle sections split into irregular islands, roots cooled to dark crimson embers, a few dying ember specks along the original paths, almost no white-gold left. Bright area about a quarter of the original. Same opaque pure-black 1080x1080 canvas. No new arcs, rings, smoke or text.

**A4. Firefly Video, va chạm (khung đầu và khung cuối; dưới 600 ký tự):**
> Three open curved brushfire strokes erupt from one lower-left strike point and sweep up-right. Heavy orange-red roots taper to long needles; small counter-strokes and detached licks follow. A hair-thin white-gold line races along each leading edge. Fast fierce attack, a brief strong hold, then the tips tear into curling fragments and cooling embers. Fixed view, pure black background. No closed circle, lotus, bird shape, smoke veil or text.

**A5. Mặt nạ áo Metal (2 bản):**
> Paint a horizontal 2048x512 xianxia sword-qi mantle mask on pure black, point to the right. Do not draw the sword: keep a straight empty black channel through the middle for the real blade, plus a thin dark gap along both of its edges. Outside the channel, two unequal banks of separated silver-blue qi plates with clear black gaps, glass-clear bodies drawn by thin silver-white rims and pale blue veins, faint indigo only under the plate roots. An open collar a quarter of the way from the left, softly cloud-curled. Two seams meet in a fine needle past the right tip; one slender silk ribbon trails off the left end. A few tiny sparkles on the rims. No solid feather, fern, wings, white block, gold, jade green or haze.

Bản 1 thêm "sharper, angular tailored plates"; bản 2 thêm "softer streaming silk filaments".

**A6. Mặt nạ lửa bọc lưỡi (2 bản):**
> Paint a horizontal 2048x512 sword-flame sheath mask on pure black, tip to the right. Do not draw the sword: keep a straight empty black channel through the middle for the dark steel blade. Outside both edges, unequal banks of soft living orange-red flame tongues sweep backward to the left as if the blade flies fast to the right; the upper bank is longer and more curled. A fine white-gold needle past the right tip; the left (hilt) end thins into a few wisps, never a blob or arrowhead. Thin white-gold accents only along the inner edges, dark soot only under the roots. Stepped anime/donghua fire. No symmetry, slab, smoke or text.

Bản 1: "long sweeping tongues"; bản 2: "shorter layered tongues in three soft surges".

**A7. Firefly Video dự phòng cho dải chuyển động** (chỉ khi không cứu được clip cũ; khung đầu là mặt nạ A5 hoặc A6 đã chọn):
> Metal: Separated silver-blue silk energy strands flow lengthwise beside an empty black channel, peeling outward and reconnecting toward a fine needle on the right; small silver highlights race along single strands; wide black gaps stay open. Graceful hand-painted xianxia energy, fixed view, pure black. No sword, feather, fern, solid white plates, smoke or text.

> Fire: Soft living orange-red flame tongues stream backward from right to left along both sides of an empty black channel, curling, splitting and retracting in irregular rhythms; a fine needle at the right, a thin white-gold heat thread now and then. Fixed view, pure black. No sword, hilt blob, fireball, smoke cloud or text.

**A8. Tấm sao (3 bản):**
> Paint a 1024x1024 sprite sheet of isolated xianxia sword-tip glints on pure black, 4x3 grid with wide gutters. Top row for large display: four long needle arms and four hair-thin diagonal arms. Middle row: crisp asymmetric four-point stars with one long forward needle. Bottom row for tiny display: bold four-point cross-needles that never become a round dot. Tiny white-gold centre under 6 percent of each star, warm pale-gold arms, tiny broken dark notches behind the root. No swollen white blob, six-point icon, diamond, lens flare, haze or text.

**A9. Tia lửa (2 bản) và bụi (1 bản):**
> Paint a 1024x1024 sprite sheet of isolated anime fire sparks on pure black with wide gutters: three lengths (short needle, medium curved streak, long whip streak), each with a tiny white-gold head, a slender orange body and a thinning dark-red cooling tail; slightly curved, varied taper; a few small ember chips for ground bounces. No round dots, radial firework, grinder sparks, zigzags, glitter, bokeh, smoke or text.

> Paint a sparse 1024x1024 ember-dust sheet on pure black: separated tiny irregular gold flecks, red-orange cooling specks, micro-streaks and a few miniature four-point glimmers, lots of empty black. No light discs, bokeh, coins, glitter cloud, large stars or text.

**A10. Ấn (2 bản):**
> Paint a 1024x1024 xianxia fire seal on pure black, a perfect circle seen straight on, about 70 percent of the frame. Two or three hair-thin broken golden-orange rings with a wide dark gap between them, each broken by two or three open gaps placed out of step. Between the rings, a band of engraved marks: evenly spaced ticks, small cloud-scroll hooks and tiny jewel points. The centre stays empty. A few needle glints at ring breaks; subtle dark ink only under the engraved marks. No letters or characters of any script, no thick bangle, no solid disc, no haze.

Bản 1: "sword-seal motif"; bản 2: "cloud-and-flame motif".

**Vòng ngọc:** không vẽ lại texture ở bước này. Gói CX-C đổi chất liệu bằng mặt nạ hình học, lấy màu ngọc trắng và vàng nhạt từ "ảnh đã duyệt" (changelog kiếm thật), rồi gửi anh ảnh trước và sau. Chỉ khi anh chê mới nhờ AI-vẽ sửa đúng texture UV, giữ nguyên bố cục UV.

## 5. Thứ tự so với hộp xám chiêu rồng và phiếu 255

**Đang chạy:**
- workflow `w4l4pn0nq` dựng hộp xám "Twin Dragons, One Burning Pearl" (Kiếm ô 2, Fire), sau cờ `key2=twin-pearl`. Lúc đọc, nó đang sửa `src/sim/skills.ts` và đã thêm `src/sim/twin-pearl.ts`, `src/content/data/twin-pearl.ts`. Theo kế hoạch, nó còn sửa `src/lab/skills-main.ts`;
- phiếu Codex 255 đang chạy trong worktree `games/.wt-immortality-cultivation-codex`, nhánh `codex/lab-orbit-cutin-port`, sửa `src/lab/orbit.ts`, `cutin.ts` và `skills-main.ts`.

**Luật:** mỗi tệp chỉ một người ghi mỗi lúc. Trước mỗi phiếu, Claude chạy `git -C games/immortality-cultivation status --short` và `git log`; phiếu nào có tệp đang bẩn hoặc đang thuộc việc khác thì chờ.

| Tệp | Hộp xám rồng | Phiếu 255 | Kế hoạch này |
|---|---|---|---|
| `src/sim/*`, `src/content/*` | đang sửa | — | chỉ CX-J, sau khi rồng vào |
| `src/lab/skills-main.ts` | sẽ sửa | đang sửa | chỉ CX-G, sau cả hai |
| `src/lab/cutin.ts`, `orbit.ts` | — | đang sửa | không đụng |
| `src/view/skills/element-fire.ts` | có thể (chiêu rồng là Fire) | — | CX-D chỉ sửa hằng `FIRE_AURA`; CX-H, CX-I chờ rồng vào |
| `src/view/skills/sword-skills.ts`, `myriad-swords.ts` | có thể (phím 2) | — | CX-I (một chỗ gọi), CX-J chờ rồng vào |
| `flipbook.ts`, `aura-mantle.ts`, `sword-aura.ts`, `sword-material.ts`, `real-swords.ts`, `element-kit.ts`, `element-metal.ts`, tệp mới | — | — | giai đoạn B |
| `element-stage.ts` | có thể | — | chỉ CX-H (đăng ký pool) |

Codex có một làn (luật của anh). Thứ tự trong làn: 255 → CX-A → CX-B → CX-C → CX-D → CX-E → CX-F → (rồng vào) → CX-G → CX-H → CX-I → CX-J.

## 6. Sửa độ rõ kiếm: T3, T1, T4, C1, C2, R1

Theo quyết định của anh, các sửa này làm sau khi hào quang vòng 2 (CX-D) vào. Vì đụng `src/sim` và `sword-skills.ts`, chúng cũng phải sau khi hộp xám rồng vào. Tất cả gom trong CX-J.

| Mã | Làm gì | Cổng |
|---|---|---|
| T3 | Thanh kiếm 1: treo, mũi chỉ đích, từ tuổi 0, rồi bay. Đòn trúng đầu đổi từ +6 sang +18 ở `school-kiem.ts` `hitTicks`, sim (`launchTick`) và view (`T_K1_HITS`, `k1Launch`). Đòn 2 và 3 giữ +36 và +66. Cập nhật canon §12.1 và ghi lý do; sửa test sim có chủ đích | sim và view trúng cùng tick; mỗi đòn chỉ một sự kiện sát thương |
| T1 | Thanh 2 và 3 rời vai 0,25–0,3 s trước đòn (khoảng tick +18 tới +21, và +48 tới +51); đường bay nhanh đầu, chậm cuối. Thanh 1 cũng có pha chậm cuối | 8–10 khung cuối ≤ 12 px/khung ở camera chơi |
| T4 | Kịch bản đo: mỗi kiếm chủ có ≥ 12 khung dài ≥ 40 px và ≤ 12 px/khung **giữa lúc hiện và lúc trúng** (khung treo được tính, đúng chữ của anh). Khung đang bay ghi riêng để xem | ngưỡng chỉnh theo mắt anh (§9 của `SWORD_READABILITY.md`) |
| C1 | Lưỡi Fire thép tối nóng mép (Q3). Chỉnh trong khuôn đó: bề rộng và độ sắc của mép nóng (`heatFrom`, `edge` trong `FIRE_BLADE`), khe mực 1 px của áo. Gemini chỉ ra rủi ro trên đá tối là thật | ΔE ≥ 0,25 theo cách gộp §2.8, lúc chờ và lúc bay, cả hai nền |
| C2 | Áo và lửa nằm ngoài viền; tính cả quạt lửa sau vai và vệt | ≤ 5 % khi bay; nếu vượt thì bật stencil, nhớ tạo target của composer có `stencilBuffer: true` |
| R1 | Khử răng cưa rẻ ở High trong `stage.ts`. Thử `SMAAPass(w, h)` sau `OutputPass` (mặc định trên r170), `SMAAPass` trước `OutputPass`, và `ShaderPass(FXAAShader)` sau `OutputPass` với `resolution` = 1/kích thước buffer | giữ được vạch 1 px của áo và mép nóng ở 60 px; nằm trong 11,5 ms mọi cửa sổ |

## 7. Phiếu Codex

Mọi phiếu dùng model `gpt-6.1-sol`. Mỗi phiếu có:
- lời giải đã chốt ở tài liệu này;
- tệp và hàm được sửa, đường ghi được phép, việc cấm;
- phép kiểm bằng số (`tsc`, `vitest`, kịch bản đo);
- tệp báo cáo.

Codex làm trong worktree riêng, không commit; Claude xem diff và kiểm lại trước khi gộp. Số phiếu đề xuất từ 256 (255 đã dùng).

| Phiếu | Gói | Mức | Vì sao mức đó |
|---|---|---|---|
| 256-tt-vfx-gates | CX-A | `xhigh` | đo lường có số, hai nơi (repo cha và game) |
| 257-tt-flipbook-v2 | CX-B | `xhigh` | shader và manifest, tương thích ngược |
| 258-tt-jade-ring-material | CX-C | `xhigh` | shader lưỡi và impostor |
| 259-tt-aura-r2-look | CX-D | `ultra` | nhiều phần: hai hệ, ba tầng kiếm, ánh xạ theo viền, cổng blade-keep |
| 260-tt-tipstar-sprite | CX-E | `xhigh` | |
| 261-tt-spark-glint-sprites | CX-F | `xhigh` | hai pool mới, vật lý trong vertex shader |
| 262-tt-lab-wiring-r2 | CX-G | `xhigh` | sau rồng và 255 |
| 263-tt-key1-brush-impact | CX-H | `xhigh` | sau rồng |
| 264-tt-painted-seal | CX-I | `xhigh` | sau rồng |
| 265-tt-sword-readability | CX-J | `ultra` | đụng sim, nội dung, view, canon, test và hậu kỳ |

Việc ảnh (A2–A10) không giao Codex, trừ khi ChatGPT và Gemini cùng chạm giới hạn ảnh. Phiếu 253 và 254 không chạy nữa; nội dung của chúng đã vào A5, A6, A9, A10.

## 8. Phiếu cũ

- **252** đã dừng (04/11, 09:30). Ba ảnh `fire-impact-k1-v*.try1.png` là đầu vào của A2. Các ngưỡng đo của 252 (Kiểm 1–9) dùng lại ở §2.8.
- **253, 254** giữ, không chạy. Kế hoạch này thay chúng.
- **255** đang chạy: đưa camera xoay phím O và cut-in C3 vào mã chính. Kế hoạch này không lặp việc đó; chỉ thêm A11 (Firefly Upscaler cho mặt C3) và chờ 255 gộp trước khi sửa `skills-main.ts`.

## 9. Quyết định chỉ anh làm được

1. **Khung đầu va chạm:** v1 (ba vầng trăng lồng nhau) hay v3 (hai nét dài và một nét ngược), sau khi dựng lại vuông và đo. Rồi chọn bản Firefly.
   - **Anh đã chọn v1a (04/11, khoảng 14:50):** khung đầu `art-src/lab/vfx/fire/impact-k1-r2/` v1a.try3 (cung 156/148/144°, độ thuôn 4,34/3,50/2,97, vạch nóng 2,3 %), khung cuối v1a.end-b.try2. A4 (Firefly) chờ anh đăng nhập lại.
2. **Mẫu áo Metal** (mảnh góc cạnh hay sợi lụa) và **mẫu lửa bọc lưỡi** (lưỡi dài hay lớp ngắn).
3. **Sao mũi:** bản Firefly `ff-g1-c2` đã gọt hay bản vẽ mới, sau khi chấm mù A/B.
4. **Ấn:** mẫu ấn kiếm hay mẫu mây lửa.
5. **Nhịp phím 1:** khi đòn đầu lùi về +18, đòn 2 tới chỉ 0,3 s sau. Giữ +36/+66 (lửa của đòn trước phải tan gần hết trong 0,3 s, như §2.6) hay dời đòn 2 và 3 muộn hơn (đổi luật chơi)? Claude đề xuất giữ.
6. **Vòng ngọc:** duyệt ảnh trước và sau của cách đổi chất liệu bằng shader, trước khi nghĩ tới vẽ lại texture.
7. **Quy trình duyệt hai lần:** ChatGPT không qua được luật "hai PASS liên tiếp" trên một kế hoạch dài; Gemini qua ở lượt 3 và 4. Anh có muốn đổi lời nhắc rà soát, ví dụ chỉ FAIL khi có lỗi sai hay thiếu bước làm hỏng việc, hoặc rà soát theo từng phần, cho các kế hoạch lớn sau này không?

## 10. Chưa kiểm, bị chặn

- **ChatGPT không đạt quy trình** ở cả hai lượt chạy. Lượt Gemini là đổi cách theo bước 7, đã ghi rõ.
- **Chưa đo gì trên ảnh thật:**
  - 252 v1/v3 mới được Claude nhìn, chưa đo cung và độ thuôn;
  - chưa biết dải chuyển động cứu được bao nhiêu từ clip cũ;
  - mọi con số TRIAL phải đo khi làm.
- **Hai tài liệu Adobe mâu thuẫn:** trang "Generate videos using images" (16/06/2026) nói thêm khung đầu thì tắt nền trong suốt; trang "transparent backgrounds" (18/08/2026) cho dùng PNG trong suốt làm khung đầu. Kế hoạch dùng cách đã chạy được (khung đầu đục, nền đen, tắt trong suốt), nên không bị chặn.
- **Thứ tự SMAA trên r170** cần thử thật (§6, R1).
- **Ink lấy từ hình nét** là quyết định của Claude, chưa có giám khảo xem.
- **Hộp xám chiêu rồng chưa vào, phiếu 255 chưa gộp.** Giai đoạn C bị chặn tới khi cả hai xong.
- **`scripts/balance/golden.ts` là TODO** (thoát với mã 1). "Cập nhật golden" khi đổi T3 hiện chỉ là cập nhật test sim và canon.
