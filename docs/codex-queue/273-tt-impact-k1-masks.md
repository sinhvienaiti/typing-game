# Phiếu 273 · Tu Tiên · Công cụ: atlas RGBA và mặt nạ A/B cho đòn lửa phím 1 (lượt 2 đã duyệt)

**Loại việc:** code công cụ và xử lý ảnh bằng số (`gpt-6.1-sol`, mức `xhigh`). Không vẽ ảnh, không dùng AI tạo ảnh. Lời giải đã chốt trong phiếu. Chỗ nào không làm được đúng như viết thì dừng ở đó và ghi vào báo cáo.

**Báo cáo:** `docs/codex-queue/273-report.md` (tiếng Việt).

**Đường duyệt:**
- Claude viết lúc 20:50 ngày 04/11 khi làn Codex trống.
- Anh đã duyệt đoạn lửa lượt 2 (khung f053–f076) lúc 19:40.
- Ý nghĩa các kênh mặt nạ đã chốt và đã gộp ở phiếu 258: `docs/codex-queue/258-tt-flipbook-v2.md` §2–§3; `games/immortality-cultivation/src/view/skills/flipbook.ts` `FB_COMPOSE_GLSL`, `composeFlipbookMasked`.
- Kết quả là **ứng viên để anh xem**, chưa nối vào lab. Việc nối là phiếu 264, sau khi anh duyệt tấm xem trước.

## Bối cảnh
- Atlas màu: `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.a4.atlas.png`. Kích thước 2304×1536, 6 cột × 4 hàng, ô 384 px, viền 2 px để 0. Lửa RGB trên nền đen, không có alpha. Khung nguồn: lượt 2, f053–f076, 24 fps (`/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/impact-k1-r2/a4/cells/atlas.meta.json`).
- Clip gốc lượt 2: `…/impact-k1-r2/fire-impact-k1-r2-v1a.a4-run2.mp4` (121 khung, 1080×1080, 24 fps), cùng thư mục art-src.
- Đường tâm ba nét của khung đầu: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/impact-k1-r2/measure/v1a.try3.strokes.json` (`strokes[].pts`, tọa độ 1080×1080; điểm đầu mỗi nét là gốc (331, 797), phía dưới trái).
- **Ý nghĩa kênh** (phiếu 258):
  - mặt nạ A: R vỏ (hull), G mực, B vạch nóng, A thứ tự sống sót;
  - mặt nạ B: R thứ tự hiện, G ảnh hưởng chuyển động (shader chưa đọc, đặt 0);
  - cả hai là dữ liệu tuyến tính (NoColorSpace), alpha thẳng, cùng lưới ô với atlas.
- Shader:
  - hiện khi `B.R ≤ T` (T tăng 0→1 trong tick 0–3);
  - thân sống khi `A.A > e` (e tăng theo lịch `impact-key1`), nên A.A cao thì sống lâu;
  - lõi nóng tắt sớm hơn thân một khoảng `uHotLead · rampMix`.

## Làm ở đâu (cwd là gốc repo cha)
### Được ghi
- `tools/vfx-masks/impact_masks.py` (tạo mới) và `tools/vfx-masks/README.md` (tạo mới);
- `tools/vfx-masks/preview-masked.ts` (tạo mới);
- trong `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/`, chỉ ba file mới:
  - `fire-impact-k1-r2-v1a.a4.rgba.png`;
  - `fire-impact-k1-r2-v1a.a4.maskA.png`;
  - `fire-impact-k1-r2-v1a.a4.maskB.png`;
  - cùng `fire-impact-k1-r2-v1a.a4.masks.json`;
- `.local/codex-runs/273-out/` (tấm xem trước và số đo; Claude chuyển sang thư mục review);
- `docs/codex-queue/273-report.md`.

### Cấm
- Sửa hay xóa file đang có trong art-src, hay sửa mã game.
- Mọi lệnh git trừ `status`, `diff`, `log`, `show`.
- Mở cổng mạng, trình duyệt, dev server; sinh ảnh bằng AI.

### Chạy Python
Dùng `uv run --offline --no-project --with numpy --with scipy --with pillow python3 tools/vfx-masks/impact_masks.py …`. Claude đã thử: chạy được offline với numpy 2.0.2, scipy 1.13.1, Pillow 11.3.0. Không cài gì khác.

## Việc (lời giải đã chốt)
Mọi phép tính làm **trên từng ô 384×384** (k = 0…23, theo thứ tự hàng trước). Viền 2 px của ô giữ bằng 0 ở mọi file ra.

### 1. Atlas RGBA (alpha thẳng, tách từ nền đen)
- Với mỗi điểm ảnh, trên giá trị sRGB 0–1: `a = max(r, g, b)`. Nếu `a > 0` thì `rgb' = rgb / a` (vẫn là sRGB), nếu không thì `rgb' = 0`.
- **Loang màu vào điểm trống**: điểm có `a < 1/255` lấy rgb' của điểm có alpha gần nhất (`scipy.ndimage.distance_transform_edt` với `return_indices`), để lọc mipmap không kéo màu đen vào mép. Alpha của các điểm đó giữ bằng 0.
- Ghi PNG RGBA 8 bit, **không premultiply** (Pillow lưu thẳng).
- Kiểm ngược: `round(rgb'·a·255)` khác atlas gốc tối đa 1 mức, ở mọi điểm có `a ≥ 1/255`.

### 2. Mặt nạ A
- **A.R vỏ:** `cov = smoothstep(0.03, 0.12, a)`. Giãn 2 px (`maximum_filter` 5×5), rồi Gauss σ = 1 px. Kẹp [0, 1].
- **A.G mực:** vành ngoài vỏ, bằng `dilate(cov > 0.5, 4 px) − (cov > 0.5)`, làm mềm σ = 0,8 px.
  - Nhân với mẫu đứt đoạn: nhiễu giá trị hạt giống cố định (`numpy.random.default_rng(273)`, lưới 24 px, nội suy song tuyến tính). Ngưỡng chọn sao cho **25 % ± 3 %** số điểm của vành thành khe (giá trị 0).
  - Mẫu cố định theo vị trí ảnh (không đổi theo khung), để mực không nhấp nháy.
- **A.B vạch nóng:** dải 0–3 px phía trong mép vỏ, **chỉ ở phía lồi (phía ngoài) của mỗi nét**.
  - Đường tâm ở khung đầu, đổi tỉ lệ 1080 → 384 (chia 2,8125).
  - Mỗi điểm mép lấy điểm gần nhất trên đường tâm gần nhất và pháp tuyến ở đó. Điểm thuộc phía lồi khi tích vô hướng (điểm − điểm đường tâm) · (điểm đường tâm − tâm cong cục bộ) > 0. Tâm cong cục bộ tính bằng đường tròn qua 3 điểm đường tâm liền nhau.
  - Trong dải đó, giữ những điểm sáng nhất, theo `a` của atlas, cho tới khi diện tích vạch nóng bằng **4 %** diện tích sáng (`a > 0,1`) của ô.
  - Làm mềm σ = 0,6 px.
  - Đường tâm chỉ có cho khung đầu. Các khung sau dùng cùng đường tâm, vì nét không di chuyển (khung cuối "giữ đúng chỗ"). Ghi trong báo cáo độ lệch trung bình giữa mép vỏ khung k và đường tâm.
- **A.A thứ tự sống sót:**
  - Giải mã clip lượt 2, khung f053–f120, về 384×384, cùng cách đổi cỡ như atlas (Lanczos, không kẹp lại), tính `a_t` như mục 1.
  - Với ô k (khung nguồn f053+k) và điểm p: `life(p) = số khung t ≥ 53+k cho tới khung đầu tiên có a_t(p) < 0,08`, đếm tới f120. Không bao giờ tắt thì `life` = 120 − (53+k) + 1.
  - Chuẩn hóa: `A.A = clamp(life / maxLife_k, 0, 1)`, với `maxLife_k` là phân vị 99 của life trong vỏ của ô k.
  - Trộn thêm độ dày: `A.A = 0,75·A.A + 0,25·edt_norm`, với `edt_norm` là khoảng cách tới mép vỏ chia phân vị 99 của nó. Điểm dày ở gốc sống lâu; mũi kim chết trước.
  - Ngoài vỏ: A.A = 0.

### 3. Mặt nạ B
- **B.R thứ tự hiện:** quãng đường dọc đường tâm, từ gốc (331, 797) tới điểm gần nhất trên nét gần nhất, chia cho độ dài nét đó. Kết quả 0 ở gốc, 1 ở mũi.
  - Điểm trong vỏ mà cách đường tâm hơn 40 px (ở 384) lấy giá trị của nét gần nhất.
  - Làm mềm σ = 1 px. Ngoài vỏ: 1 (hiện sau cùng, vô hại).
  - Mọi ô dùng cùng một B.R, vì thứ tự hiện là của hình nét.
- **B.G:** 0. **B.B:** 0. **B.A:** 255.

### 4. Ghi file
- maskA RGBA 8 bit, maskB RGBA 8 bit, cùng kích thước 2304×1536 và cùng viền 0 với atlas.
- `masks.json` ghi:
  - mọi tham số ở trên, hạt giống, đường dẫn nguồn và md5 của chúng;
  - số đo theo ô: diện tích sáng, vỏ, mực, tỉ lệ khe mực, vạch nóng / diện tích sáng, A.A trung bình ở vùng gốc so với vùng mũi (20 % đầu và 20 % cuối dọc đường tâm).

### 5. Xem trước bằng bộ tính CPU của game (`tools/vfx-masks/preview-masked.ts`)
- Chạy bằng `node --import tsx tools/vfx-masks/preview-masked.ts` (nếu sandbox chặn IPC của `tsx` CLI thì dùng loader như báo cáo 259).
- Nhập từ `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/view/skills/flipbook.ts`: `composeFlipbookMasked`, `blendPremultiplied`, `flipbookControl`, `FLIPBOOK_TIMING`, `FLIPBOOK_MASKED_LOOK`, `srgbToLinear`.
- Với tick ∈ {0, 1, 3, 6, 9, 12, 18, 24, 30, 36, 42}:
  - khung `vFrame = tick·24/60`, loopMode `none`, `f0 = floor`, `w = phần lẻ`;
  - `ctl` từ `flipbookControl(tick/60, 43/60, 0, 0, FLIPBOOK_TIMING["impact-key1"], out)`;
  - lấy mẫu atlas RGBA (đổi sRGB sang tuyến tính) và hai mặt nạ (`byte/255`) ở f0 và f1;
  - ghép bằng `composeFlipbookMasked` (look mặc định, tint 1, soft 1), rồi `blendPremultiplied` lên nền đá tối `#2a2c30` tuyến tính;
  - đổi sang sRGB 8 bit, có kẹp. Lõi HDR > 1 bị kẹp, chỉ dùng để xem.
- Ra `.local/codex-runs/273-out/preview-ticks.png`: 11 ô liền nhau, nhãn tick tiếng Anh.
- Thêm tấm từng kênh `channels-k00-k23.png`: hàng atlas RGBA, A.R, A.G, A.B, A.A, B.R; 6 cột chọn k = 0, 4, 8, 12, 16, 20.

## Kiểm bắt buộc
1. Mục 1: sai số dựng ngược ≤ 1 mức trên mọi điểm có alpha. In số điểm vượt (phải là 0).
2. Mục 2 trên mọi ô:
   - vạch nóng / diện tích sáng nằm trong 3,5–4,5 %;
   - tỉ lệ khe mực 22–28 %;
   - A.A trung bình vùng gốc > vùng mũi.

   In bảng 24 ô.
3. Mục 3: B.R ở gốc ≤ 0,05 và ở mũi ba nét ≥ 0,95.
4. Viền 2 px của mọi ô bằng 0 trong cả bốn file ra.
5. `preview-ticks.png`: điểm sáng (độ sáng > 0,1) ở tick 42 ít hơn 2 % so với tick 9. In hai số.
6. `git status --short`: không có thay đổi nào ngoài các file được ghi. `art-src` không theo Git; liệt kê bằng `ls -la` bốn file mới.

## Claude làm sau
- Xem tấm xem trước và tấm kênh, chuyển sang `typing-game-review/captures/tu-tien/impact-k1-r2/masks/` và gửi anh.
- Nếu anh duyệt: phiếu 264 nối clip v2 vào lab (manifest với `controlA`, `controlB`, `timingProfile: "impact-key1"`, `loopMode: "none"`), rồi quay video.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
