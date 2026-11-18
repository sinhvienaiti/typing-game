# Tuyệt kỹ Tinh Tú: kế hoạch (chưa dựng code)

**Mục tiêu (≤ 3 dòng):** Tuyệt kỹ Tinh Tú theo dòng Tinh Tú của `docs/games/tu-tien/ULT_CHOREOGRAPHY.md`. Người tung giơ tay, chòm Bắc Đẩu Thất Tinh hiện trên trời. Bảy sao băng lần lượt rơi **chéo**, mỗi viên bắn tỉa một con quái. Viên thứ bảy nổ ánh kim cương và là điểm nhấn duy nhất.
**Cách đã chốt:** Làm theo quy trình đã dùng cho Kim, Lôi, Quang và Hư Không (DECISIONS 17–18/11). Thứ tự: phân cảnh → liệt kê thành phần → dùng lại art có sẵn → vẽ ảnh tĩnh còn thiếu từ ảnh tham chiếu của dự án → owner chọn → video Firefly (chỉ cho phần bên trong có chuyển động) → dựng trong lab, xem ở camera chơi → owner duyệt → hai giám khảo mù ≥ 8,5.
**Nghiệm thu (số):** lõi trắng ≤ 25–30 % bề ngang; mọi lớp phụ ≤ 0,9 mỗi kênh, riêng ánh kim cương được vượt; không quá 2 lớp cộng sáng chồng tại một chỗ; p95 ≤ 16,7 ms; 0 lớp vẽ bằng code (mọi lớp có tệp nguồn); hai giám khảo mù ≥ 8,5 trong host chơi.
**Phiếu, báo cáo, ảnh:** `docs/codex-queue/452-tt-star-constellation.md`, `452-tt-star-meteor.md`, `452-tt-star-diamond.md` (báo cáo `452a/452b/452c-report.md`). Phân cảnh: `games/immortality-cultivation/art-src/concept/ult-storyboards/star-storyboard.v1-try1.png`.

## Bài học 17–18/11 áp vào kế hoạch này
- Không có hình nào do code vẽ. Làm mờ, kéo giãn, che mặt nạ hay lọc kênh trên art cũng bị tính là vẽ code (các lớp vùng xám K5–K7, L4, Q4 trong `vfx-code-drawn-audit.md`). Code chỉ được đặt, xoay, phóng **đều**, nhuộm, mờ dần, phát flipbook.
- Mảng phẳng trên trời hoặc dưới đất là mặt phẳng 3D thật, dán texture nhìn thẳng từ trên xuống 90°. Kim đã làm vậy: trận pháp `formation-simple-a` dán trên mặt phẳng ngang. Không dùng ảnh vẽ sẵn góc 55° cho mặt phẳng, nên **không dùng `star-ring-burst-v2`**, `star-ground-mark`, `star-caster-seal`.
- Dải nối giữa các sao là dải năng lượng có độ dày, không phải nét mảnh. Lôi bị chê "như que", owner cấm sợi mảnh trong đòn kết.
- Mảng trên trời chỉ một lớp, đơn giản, độ đục khoảng 0,45, đặt **sau và cao hơn đàn quái** để không che góc sau lưng (Kim 433, 18/11).
- Hiệu ứng phải đủ lớn ở camera chơi, không thành đồ chơi. Camera đẩy vào 1–2 s lúc cao trào, như Kim.
- Owner xem trong lab ở camera chơi (Alt+1) và sau lưng (Alt+2), không xem tranh. Ảnh và video gửi thẳng vào chat, có nhãn và lựa chọn.
- Codex còn dưới 15 % tới 24/11 09:48 nên chỉ được làm ảnh. Phần dựng lab do Claude Opus tự làm, có nhìn. Mỗi phiếu code VFX sau này phải có dòng `Nguồn hình:` (cổng G5).

## 1. Thời gian các pha (tổng 8,4 s)

| Pha | Giây | Việc trên màn | Âm |
|---|---|---|---|
| Tụ lực | 0,00–1,20 | Người tung giơ tay. Xoáy sao `star-charge` (1,4 m) nở ở tay. Hạt `star-sparkle` hút về tay. | `gather` |
| Phát (tại người tung) | 1,10–1,40 | `star-release` bùng ở tay, 1 lần. | `release` |
| Phát (trên trời) | 1,20–2,60 | Chòm sao hiện trên mặt phẳng trời: flipbook vẽ nét 1,2 s (từ video của ảnh owner chọn), sau đó giữ ảnh tĩnh. Bảy nút sao lần lượt lóe `glint-starburst-set`, mỗi nút cách nhau 0,16 s. | `draw`, `node` ×7 (cao độ tăng dần 0,94→1,10) |
| Bay (6 viên bắn tỉa) | 2,60–4,90 | Viên *k* (k = 1..6) rời nút *k* lúc 2,60 + 0,38·(k−1) s và rơi 0,42 s theo đường chéo 35–45° so với phương đứng, từ sau-trái tới trước-phải. Đầu sao băng là billboard 1,6 m. Đuôi gắn sau đầu, dài 7 m, phóng đều, xoay theo hướng bay trên màn, hiện dần trong 0,08 s. Dấu ngắm: một lóe nhỏ trên đầu quái, 0,20 s trước cú chạm. | `launch` mỗi viên |
| Chạm (6 viên) | 3,02–5,32 | Tại quái: `star-impact` 1,8 m. Đất: `star-crack-star` 1,4 m dán trên mặt phẳng nằm, mờ dần trong 1,5 s. Quái bị đẩy nhẹ. | `hit` |
| Cao trào (viên 7) | 5,40–6,30 | Lặng 0,3 s. Viên 7 to 1,6 lần (đầu 2,6 m, đuôi 10 m) rơi từ nút đuôi chòm (Dao Quang) vào chỗ quái đông nhất hoặc tinh anh. Chạm lúc 5,82 s: **ánh kim cương** (flipbook từ ảnh owner chọn, là điểm nhấn duy nhất, HDR chỉ ở lõi). Kèm `star-big-burst` (≤ 0,9) và `star-crack-star` 3 m. Khựng hình 0,06 s, camera đẩy vào 1,2 s. | `climax` |
| Dư âm | 6,30–8,40 | `star-hit-affliction` lặp 1,5 s trên quái còn sống. Bụi sao `star-sparkle` và `glint-gold-twinkle-set` rơi lắng. Chòm sao mờ dần 6,3–7,3 s. Vết đất tan hết lúc 8,0 s. | `tail` |

Vị trí trên trời: mặt phẳng ngang cao 14 m, rộng khoảng 22 m. Tâm nằm 8 m sau tâm đàn quái và lệch trái 6 m, để đường rơi đọc thành đường chéo từ trên-trái xuống dưới-phải như phân cảnh. Ở camera chơi, chòm sao chiếm 40–55 % bề ngang khung và không chạm mép trên. Độ đục 0,45. Góc 35–45° nghiêng hơn mức 15–25° của canon D62. Phân cảnh owner đã thấy chọn góc này, nhưng vẫn ghi lại để owner xác nhận.

## 2. Thành phần (12 hình: 8 dùng lại, 4 ảnh tĩnh mới; 2 trong 4 ảnh mới thành video sau khi owner chọn)

`B = games/immortality-cultivation/art-src/lab/vfx/`, `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`, `N = games/immortality-cultivation/art-src/lab/vfx/star-ult/stills/` (thư mục mới).

| # | Thành phần | Pha | Nguồn | Cách đặt (chỉ thao tác được phép) |
|---|---|---|---|---|
| 1 | **Chòm sao Bắc Đẩu** | phát, bay | **MỚI**: phiếu 452-constellation, `N/star-constellation.v1-try<k>.png`. Khổ 1536×1024, **nhìn thẳng từ trên xuống 90°**, lề ≥ 10 %. Gồm 7 nút sao và dải nối vàng có độ dày, không vòng tròn. Sau khi owner chọn: Firefly image-to-video "nét vẽ nối từng sao", ảnh chọn làm khung cuối, đóng thành flipbook `B/star-ult/star-constellation-draw` | Mặt phẳng 3D nằm ngang trên trời, cộng sáng, độ đục 0,45; flipbook rồi giữ ảnh tĩnh; xoay rất chậm (≤ 3°/s); mờ dần lúc kết |
| 2 | Lóe nút sao và dấu ngắm | phát, bay | DÙNG LẠI `B/aura/glint-starburst-set` (16 khung × 8 biến thể, ô 128) | Billboard tại 7 toạ độ nút (Claude đo trên ảnh chọn, ghi vào `N/../constellation.nodes.json`) và trên đầu quái bị ngắm; nhuộm vàng trắng |
| 3 | Xoáy tụ lực ở tay | tụ lực | DÙNG LẠI `B/star/star-charge` (32 khung, 12 fps) | Billboard 1,4 m ở tay |
| 4 | Hạt sao (tụ lực, dư âm) | tụ lực, dư âm | DÙNG LẠI `B/star/star-sparkle` (48 khung, lặp) và `B/aura/glint-gold-twinkle-set` | Nhân bản; bay về tay, sau đó rơi lắng |
| 5 | Bùng phát ở tay | phát | DÙNG LẠI `B/star/star-release` | Billboard 1,2 m, 1 lần |
| 6 | **Đầu sao băng** | bay | **MỚI**: phiếu 452-meteor, `N/star-meteor-head.v1-try<k>.png`, 1024×1024, nhìn ngang (billboard nên không phụ thuộc góc), một lõi sao, không đuôi dài, lề ≥ 12 %. Tờ chọn kèm phương án E dùng lại `B/star/star-comet` (đầu và đuôi liền trong flipbook) | Billboard 1,6 m (viên 7: 2,6 m), xoay theo hướng bay; có thể làm video lấp lánh lặp nếu owner muốn |
| 7 | **Đuôi sao băng** | bay | **MỚI**: phiếu 452-meteor, `N/star-meteor-trail.v1-try<k>.png`, 1536×1024, dải nằm ngang, đầu sáng ở phải và tan dần về trái, kiểu chuỗi hạt sáng như mẫu D owner chọn cho Kim | Billboard gắn sau đầu, **phóng đều** (dài 7 m / 10 m), xoay theo hướng bay; không kéo giãn, không cắt dần |
| 8 | Cú chạm bắn tỉa | chạm | DÙNG LẠI `B/star/star-impact` (32 khung, 12 fps) | Billboard 1,8 m tại ngực quái |
| 9 | Vết sao trên đất | chạm, dư âm | DÙNG LẠI `S/star-crack-star.v1-try1.png` (toả hình sao, nhìn từ trên) | Mặt phẳng nằm sát đất, 1,4 m (viên 7: 3 m), độ đục ≤ 0,6, mờ trong 1,5 s; không thành vòng tròn lớn |
| 10 | **Ánh kim cương** (điểm nhấn) | cao trào | **MỚI**: phiếu 452-diamond, `N/star-diamond-glint.v1-try<k>.png`, 1024×1024, nhìn thẳng mặt (billboard nổi giữa không trung), lõi trắng ≤ 30 %, lề ≥ 12 %. Sau khi owner chọn: Firefly image-to-video bung nở rồi tắt, đóng thành `B/star-ult/star-diamond-burst` | Billboard 4–5 m tại điểm chạm viên 7; chỉ lớp này được HDR |
| 11 | Thân nổ cao trào | cao trào | DÙNG LẠI `B/star/star-big-burst` (32 khung) | Billboard 3,5 m dưới ánh kim cương, ≤ 0,9 |
| 12 | Dư âm trên quái | dư âm | DÙNG LẠI `B/star/star-hit-affliction` (lặp) | Billboard bám quái còn sống, 1,5 s |

Không dùng: `star-ring-burst-v2`, `star-ground-mark` và `star-caster-seal`, vì chúng là ảnh vẽ sẵn góc 55° cho mặt phẳng. Không dùng `star-pillar`: phóng đều lên 14 m thì cột quá bè. Bảng thành phần 398 (`games/immortality-cultivation/art-src/concept/ult-star/ult-star-components.v1-try1.png`) chỉ làm ảnh tham chiếu vì ô quá nhỏ để dùng trực tiếp.

**Âm** (dùng lại nguyên liệu Firefly trong `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/sound/`, 3–4 bản mỗi việc, cao độ 0,96–1,04, đo bằng ebur128 như `void-ult-sound.ts`):

| Sự kiện | Nguồn | Nhóm |
|---|---|---|
| `gather` | `tt-sfx-star-charge-long` | impact |
| `release` | `tt-sfx-star-cast` | impact |
| `draw` | `tt-sfx-el-star-seal` | world |
| `node` | `tt-sfx-twin-glint-shimmer` (thang cao độ) | impact, tối thiểu cách nhau 0,12 s |
| `launch` | `tt-sfx-el-star-comet` | impact |
| `hit` | `tt-sfx-star-hit-light` | impact, gom 0,05 s |
| `climax` | `tt-sfx-star-big-burst` + `tt-sfx-star-hit-heavy` | big |
| `tail` | `tt-sfx-star-tail` | world, send 0,15 |

Dự phòng: các thư mục `.ogg` trong `games/immortality-cultivation/art-src/lab/audio/` (`cast-star`, `flyby-star`, `impact-spirit-star`, `world-climax-star`, `world-close-star`). Thêm 8 sự kiện này vào `docs/work/tasks/audio-backlog.md` khi dựng.

## 3. Phiếu ảnh Codex (chạy lần lượt, một làn; đều ở trạng thái `Phản biện: (chờ)`)
- `docs/codex-queue/452-tt-star-constellation.md`: chòm sao A/B, đúng 2 lần.
- `docs/codex-queue/452-tt-star-meteor.md`: đầu sao băng A/B/C và đuôi A/B, đúng 5 lần.
- `docs/codex-queue/452-tt-star-diamond.md`: ánh kim cương A/B/C, đúng 3 lần.

Trước khi chạy:
1. Một critic Claude mới phản biện từng phiếu và ghi `Phản biện: PASS` (cổng G1).
2. Đọc `rate_limits`. Dưới 15 % vẫn chạy được vì đây là phiếu ảnh.
3. Chạy bằng `tools/codex-run/run.sh`, một phiếu một lúc (G2).

## 4. Các bước sau khi owner chọn
1. Gửi ba tờ ghép vào chat, có nhãn A/B/C và phương án E (`star-comet`). Owner chọn từng thành phần. Chưa chọn thì không gắn, không làm video.
2. Ghi lựa chọn vào `DECISIONS.md`. Liệt kê các biến thể không chọn vào `docs/games/tu-tien/skills/VFX_LIBRARY.md`, không xoá file nào.
3. Firefly image-to-video chỉ cho hai phần có chuyển động bên trong:
   - chòm sao vẽ nét: ảnh chọn làm khung cuối, camera khoá nhìn từ trên, không thêm vật;
   - ánh kim cương bung nở rồi tắt: ảnh chọn làm khung đầu.

   Đầu sao băng chỉ làm video lấp lánh lặp nếu owner yêu cầu. Mỗi video qua cổng nguồn của `game-video-vfx-usage`: nằm trong khung với lề ≥ 10 %, nền sạch, không có vật lạ, đoạn cuối tan được. Đóng thành atlas, JSON và KTX2 theo phiếu 419/420, kiểm lề trên cả PNG và KTX2.
4. Claude đo 7 toạ độ nút sao trên ảnh chòm sao đã chọn và ghi `games/immortality-cultivation/art-src/lab/vfx/star-ult/constellation.nodes.json`, theo thứ tự Thiên Khu → Dao Quang.
5. Dựng lab trong `games/.wt-ic-lab-all/src/lab/star-ult-*.ts`. Bật bằng phím hoặc `?ult=star`, cùng host với Kim (`MetalUltHost`: `strike`, `sound`).
   - Mỗi lớp trong bảng §2 gắn đúng tệp nguồn, chỉ đặt, xoay, phóng đều, nhuộm, mờ, phát flipbook.
   - Không shader tạo hình, không mặt nạ, không làm mờ.
   - Claude Opus tự dựng khi Codex còn dưới 15 %. Nếu giao Codex thì phiếu phải có `Nguồn hình:` (G5) và một critic PASS.
6. Viết `star-ult-sound.ts` theo mẫu `void-ult-sound.ts` và nối vào bus world.
7. Tự kiểm trước khi gửi:
   - lập bảng "lớp → tệp nguồn" cho mọi lớp và so với các mục vi phạm trong `vfx-code-drawn-audit.md`;
   - đo kênh màu từng lớp phụ (≤ 0,9) và p95 ở 100 quái.
8. Chụp ở camera chơi (Alt+1) và sau lưng (Alt+2), nền `?ground=%23353a40`, tại 1,0 / 2,2 / 3,4 / 5,9 / 7,0 s. Quay video có tiếng, lưu vào `typing-game-review/owner-review/<ngày>/tu-tien/star-ult/`, kèm `ABOUT.md`, rồi chạy `node scripts/review-index.mjs`. Gửi khung và video vào chat. Xoá khung thô bằng `tools/capture-prune/prune.mjs`.
9. Sửa theo nhận xét của owner, mỗi vòng một bảng điểm và không lùi chất lượng. Sau khi owner duyệt, hai giám khảo mù chấm ≥ 8,5 trong host chơi, không cờ URL.

## Nhật ký (mỗi dòng một sự kiện: ngày giờ · ai · việc · kết quả)
- 18/11 · Claude (agent) · lập kế hoạch và ba phiếu ảnh 452 · chưa chạy Codex, chưa sửa code, chưa commit
