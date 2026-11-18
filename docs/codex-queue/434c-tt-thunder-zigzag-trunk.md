# Phiếu 434c: Lôi, sét dây chuyền zíc zắc, thân sét lớn bớt trắng, mây ra mây bão (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Agent Claude đã đưa Lôi lên khoảng 6,5/10 và mây lên khoảng B−. Ảnh hiện tại: `typing-game-review/owner-review/2026-11-17/tu-tien/thunder-claude.jpg` và `clouds-claude.jpg`.
Đích là nửa phải của phân cảnh `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`.

Owner cho chạy full-access để tự chụp ("Cho full-access", 17/11). Cách làm giống phiếu 439:
- Chrome chạy headless, chỉ vào localhost:3148. Không dừng server.
- Có thể dùng ffmpeg và `tools/capture-prune/prune.mjs`.
- Cách đo p95 như `docs/codex-queue/439b-tt-light-ult-glow.md`.

Chỉ sửa `games/.wt-ic-lab-all/src/lab/thunder-ult-*` và `cloud-volume*`. Không sửa file khác, không commit.

## Việc
1. **Sét dây chuyền zíc zắc.** Mỗi bước nhảy chọn quái kế tiếp lệch ngang so với hướng trước, góc đổi hướng 35–80°, xen kẽ trái và phải. Như vậy sét quét ngang qua đàn quái chứ không chạy thẳng. In ra góc đổi hướng của từng bước.
2. **Thân sét lớn.**
   - Lõi trắng mảnh, quầng tím xanh. Ở góc sau lưng, bề rộng phần gần trắng (độ sáng ≥ 0,95) ≤ 2 % bề rộng khung.
   - Vùng trắng toàn khung ≤ 6 % ở mọi khung.
   - Đây vẫn là điểm nhấn duy nhất.
3. **Lóe trong mây.** Chỉ sáng cục bộ quanh tia chớp (bán kính 3–5 m trong mây), không làm cả đám mây nhạt sang tím nhạt.
4. **Mây ra mây bão.**
   - Đáy mây tối và dày, có gờ cuộn rõ.
   - Khối mây tầng lớp, dày hơn ở giữa.
   - Ở góc sau lưng, mây phủ ít nhất 30 % chiều cao khung, không chỉ là một dải mỏng ở mép trên.
   - Dùng lại cụm khói CC0 trong `art-src/lab/vfx/cloud-puffs/`.

## Vòng lặp
Tối đa 5 vòng: sửa, chụp, mở ảnh, so phân cảnh, sửa tiếp.
- Chụp lúc 0,4 / 1,2 / 2,2 / 3,0 s ở camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- Chụp riêng mây với `?cloud=thunder`.

Ghi bảng điểm kèm các số đo của mục 1–4.

## Nghiệm thu
- Kiểm kiểu 0 lỗi.
- p95 ≤ 16,7 ms.
- Lưu `thunder-codex-c.jpg` và `.mp4`, cùng `clouds-codex-c.jpg`, vào `owner-review/2026-11-17/tu-tien/`. Giữ file cũ. Thêm dòng vào `ABOUT.md`.
- Xoá khung thô của mình.

## Giao nộp
`docs/codex-queue/434c-report.md`.
