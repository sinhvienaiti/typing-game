# Phiếu 324b · Tu Tiên · Ảnh 2D: vẽ lại 2 ấn Kim chưa đạt (xoắn ốc, rãnh mưa kiếm)

Phiếu 324 xong 7 ảnh, nhưng tự chấm 2 ảnh còn dưới 8 (`docs/codex-queue/324-report.md`):
- **xoắn ốc** `metal-sigil-spiral.v1-try1.png`: lề trên chỉ 6 px;
- **rãnh** `metal-rift-groove.v1-try2.png`: dải quá dày (khoảng 19 % khung), còn phù văn.

Phiếu này vẽ lại đúng hai hình đó, cùng phong cách và luật như phiếu 324.

**Model `gpt-6.1-sol`, mức `high`. Đúng 2 lần gọi `image_gen`, cộng tối đa 2 lần vẽ lại.** Báo cáo: `docs/codex-queue/324b-report.md` (tiếng Việt, ngắn).

## Đường dẫn và luật
- `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
- **Được ghi:** chỉ thêm file mới vào `S` (`cp -n`) và báo cáo.
- **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo.
- Mốc phong cách gửi kèm mỗi lần gọi `image_gen`: `S/metal-sigil-hex.v1-try2.png`, `S/metal-sigil-line.v1-try1.png`. Thêm bản cũ của chính hình đó, chỉ để Codex thấy lỗi cần tránh.
- Prompt như phiếu 324.

## Hai ảnh
| Tên tệp | Sửa gì |
|---|---|
| `S/metal-sigil-spiral.v1-try2.png` | Giữ dáng trận xoắn ba nhánh như try1, nhưng **cả trận chỉ chiếm khoảng 70 % chiều cao khung**, căn giữa, lề trên và dưới mỗi bên ít nhất 12 % chiều cao. |
| `S/metal-rift-groove.v1-try3.png` | Một **vết chém đất** mảnh nằm ngang: khe sáng ánh thép ở giữa, mép nứt răng cưa, nứt nhánh ngắn hai bên, hai đầu thon nhọn. **Không phù văn, không chữ, không trang trí.** Cả rãnh kể cả quầng sáng và nhánh nứt **cao không quá 10 % khung**, chạy gần hết bề rộng, lề trái và phải ít nhất 3 %. |

## Tự chấm, xong khi
- Tự chấm như phiếu 324. Đo hộp nét ở ngưỡng sáng 5 % và ghi vào báo cáo: lề trên của xoắn ốc và chiều cao của rãnh.
- Dưới 8 thì vẽ lại một lần (spiral `-try3`, groove `-try4`) và chọn bản điểm cao hơn.
- Ghép lại tấm `S/metal-sigils-set-sheet-v2.jpg`: 7 bản đã chọn, thay bằng bản mới của xoắn ốc và rãnh.
- Báo cáo có bảng điểm và hai số đo.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
