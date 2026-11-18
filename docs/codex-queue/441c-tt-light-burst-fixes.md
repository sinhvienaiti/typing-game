# Phiếu 441c: Quang, giữ cỡ nổ và sửa 3 lỗi (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Bản trước là 441b (`typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-f.jpg`). Owner ngày 17/11 chọn "Giữ cỡ, sửa lỗi". Ba lỗi cần sửa:
- ở camera chơi, phần trên cú nổ D bị cắt mép khung;
- các quái lóe thành những đốm trắng lạ;
- cuối chiêu còn hiện một vòng sáng tròn.

Những thứ giữ nguyên như `docs/codex-queue/441b-tt-light-burst-huge.md`:
- quyền, server 3148, ffmpeg, prune, phạm vi sửa (`games/.wt-ic-lab-all/src/lab/light-ult-*`, `light-ult-cut.mjs`), cách đo;
- cỡ nổ: ≥ 45 % bề rộng và ≥ 35 % chiều cao khung;
- tia hội tụ.

Được ghi `docs/codex-queue/441c-report.md`.

## Việc
1. **Không cắt mép.** Ở khung nổ, mọi điểm sáng của cú nổ (độ sáng tăng ≥ 0,15) nằm trong khung với lề ≥ 3 %. Cách làm: hạ tâm hình trên màn hình, hoặc neo flipbook thấp hơn, hoặc nghiêng nhẹ về phía camera. Không được thu nhỏ dưới ngưỡng cỡ nổ.
2. **Bỏ đốm trắng trên quái.** Quái trong vùng nổ chỉ lóe viền vàng nhẹ, kênh ≤ 0,9, không phủ trắng cả thân. In ra độ sáng tối đa trên thân quái.
3. **Không còn vòng tròn sáng ở cuối.** Cắt flipbook trước khung có vòng, hoặc làm mờ nhanh phần đó. Luật cấm vòng của 439 vẫn áp dụng.

## Vòng lặp
- Tối đa 3 vòng.
- Chụp ở camera chơi và góc sau lưng, nền `?ground=%23353a40`.
- Mỗi vòng in: lề nhỏ nhất của cú nổ, cỡ nổ, vùng trắng, độ sáng trên thân quái.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu bản mới `light-ult-codex-g.jpg` và `light-ult-codex-g.mp4`, giữ file cũ, thêm một dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.
