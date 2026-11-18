# Phiếu 434d — Lôi: mây lên cao mép trên, sét dày sáng (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
434c (`typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-c.jpg`): Codex tự chấm 7,4, Claude ~4,5 — ở camera chơi mây đen nằm thấp, che kín giữa sân và đè lên đàn quái; sét dây chuyền mảnh. Owner 17/11 chọn "Mây lên cao, mép trên": đẩy mây lên cao và ra xa như phân cảnh, chỉ chiếm dải trên khung, quái luôn lộ rõ; sét dày và sáng hơn. Đích: nửa phải `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`. Quyền, server 3148, ffmpeg, prune, cách đo p95 và phạm vi sửa (`games/.wt-ic-lab-all/src/lab/thunder-ult-*`, `cloud-volume*`) giữ như `docs/codex-queue/434c-tt-thunder-zigzag-trunk.md`; được ghi `ABOUT.md` trong thư mục review và `docs/codex-queue/434d-report.md`.

## Việc
1. **Mây cao và xa:** ở camera chơi 1280×720, khối mây nằm trong dải trên cùng: mép dưới mây ≤ 28 % chiều cao khung tính từ trên; không phủ lên bất kỳ quái nào (đo: số quái có tâm màn hình nằm dưới mây phủ đặc (alpha ≥ 0,5) = 0). Đặt mây trong thế giới ở độ cao và khoảng cách lớn hơn phía sau đàn quái (không ép bằng màn hình); góc sau lưng vẫn thấy mây ≥ 30 % chiều cao khung.
2. **Ánh tím từ mây xuống:** khi chớp, ánh tím mờ hắt xuống đất và quái (đèn/decal mềm, kênh ≤ 0,9), không vòng tròn.
3. **Sét dày sáng hơn:** dây chuyền ở camera chơi rộng (lõi + quầng) ≥ 6 px, lõi trắng tím, quầng tím ≥ 3 lần lõi, nhánh phụ 2–4/bước; giữ zíc zắc của 434c. Sét lớn từ đáy mây xuống cụm quái: thân ≥ 10 px ở camera chơi, vẫn là điểm nhấn duy nhất, vùng trắng ≤ 6 %.
4. Giữ dư điện trên quái và mây tan.

## Vòng lặp và đo
Tối đa 4 vòng sửa → chụp → mở ảnh → so phân cảnh → sửa; 0,4/1,2/2,2/3,0 s, camera chơi (Alt+1) và sau lưng (Alt+2), nền `?ground=%23353a40`. In: mép dưới mây (%), số quái bị mây phủ, độ rộng sét (probe cắt ngang như `light-ult-glow-probe.mjs`; vị trí màn hình của quái và camera lấy như `thunder-ult-chain-probe.mjs`), vùng trắng.

## Nghiệm thu
Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms. Lưu `thunder-codex-d.jpg/.mp4` mới (giữ file cũ), dòng `ABOUT.md`. Xoá khung thô. Không commit.

## Giao nộp
`docs/codex-queue/434d-report.md`.
