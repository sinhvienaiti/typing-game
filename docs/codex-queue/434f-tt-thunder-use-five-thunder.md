# Phiếu 434f: Lôi, dùng lại sét dày của Ngũ Lôi (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Owner nói ngày 17/11: "tôi rất ghét bạn dùng kiểu sét mỏng này, bạn còn nhớ dạng sét ngũ lôi của chúng ta chứ, nó rất dày và uy lực, sao không lấy từ đó hoặc làm theo".

Ngũ Lôi Oanh Đỉnh đã được owner duyệt và đang nằm trong `games/.wt-ic-lab-all/src/lab/five-thunder.ts`. Nó dùng các flipbook cột sét dày:
- `COLUMN_MIX = "thunder-columns-mix"`;
- `thunder-column-*-i2v5`;
- các lớp `columnA`, `columnCoreA`, `boltA`–`boltD`, `boltCentre`, `burst`, `lichtenberg`, `scarHot`/`scarCold`, `crawlA`–`crawlD`.

Bản tuyệt kỹ Lôi hiện tại là 434e (`typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-e.jpg`). Sét lớn và sét dây chuyền trong đó đều là dải mảnh vẽ bằng code.

Owner cho chạy full-access để Codex tự chụp ("Cho full-access", 17/11). Giữ nguyên như `docs/codex-queue/434e-tt-thunder-cloud-visible.md`:
- quyền chạy, server 3148, ffmpeg, prune, cách đo p95;
- phạm vi sửa: `games/.wt-ic-lab-all/src/lab/thunder-ult-*` và `cloud-volume*`.

Chỉ **import** từ `five-thunder.ts` và đọc các flipbook của nó. Không sửa `five-thunder.ts`, không sửa flipbook. Được ghi `docs/codex-queue/434f-report.md` và `ABOUT.md`.

## Việc
1. **Sét lớn từ mây.** Thay thân sét vẽ bằng code bằng cột sét dày của Ngũ Lôi: `COLUMN_MIX` hoặc `columnA` + `columnCoreA`. Cách nạp và đặt theo đúng `five-thunder.ts`, kèm `burst`, `lichtenberg` và vết `scarHot`/`scarCold` ở chân. Cột đi từ đáy mây xuống điểm đánh. Ở camera chơi, bề ngang thân cột ≥ 40 px.
2. **Sét dây chuyền.** Thay dải mảnh bằng các tia đơn dày của Ngũ Lôi (`boltA`–`boltD`). Mỗi bước nhảy là một tia dày nối quái này sang quái kia, xoay và kéo giãn theo đoạn nối. Giữ nhịp zíc zắc của 434c. Ở camera chơi, thân tia ≥ 14 px.
3. **Vết đất.** Dùng `crawlA`–`crawlD` và `scar*` của Ngũ Lôi thay cho nhánh sét vẽ bằng code. Không vết hình sao, không vòng.
4. **Màu.** Giữ tím–trắng điện của tuyệt kỹ Lôi bằng cách nhuộm (tint). Không đổi màu file nguồn.
5. **Giữ nguyên:** mây ở dải trên khung (434e), ánh tím hắt xuống, dư điện trên quái. Sét lớn là điểm nhấn duy nhất. Vùng trắng ≤ 6 %.

## Vòng lặp
- Tối đa 4 vòng: sửa → chụp → mở ảnh → so với nửa phải phân cảnh `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg` và với Ngũ Lôi trong lab → sửa.
- Chụp ở camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- Mỗi vòng in ra: bề ngang thân cột và thân tia (probe cắt ngang), vùng trắng, p95.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `thunder-codex-f.jpg` và `.mp4` mới, giữ file cũ, thêm dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.

## Giao nộp
`docs/codex-queue/434f-report.md`.
