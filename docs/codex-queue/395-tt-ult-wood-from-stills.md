# Phiếu 395: Dựng tuyệt kỹ Mộc trong lab theo ảnh 391


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Chiêu băng v3 (389, 390) được owner khen "tạm đẹp" nhưng chê vỏ bọc che quái; bản 390 đã thay bằng trói chuyển động. Làm chiêu Mộc theo cùng cách. Ảnh chọn (theo miễn trừ ảnh của owner 15/11; owner chưa phản đối): `games/immortality-cultivation/art-src/concept/ult-wood/ult-wood-moment-b.v1-try1.png` (bố cục), `ult-wood-components.v1-try3.png` (thành phần), `ult-wood-root-ground.v1-try1.png` (mặt đất).

## Việc (worktree `games/.wt-ic-lab-all`)
1. Script cắt thành phần từ ảnh (nền đen → alpha), xuất vào `art-src/lab/vfx/wood-ult/`. Không vẽ lại, không tạo hình bằng code.
2. File mới `src/lab/wood-ult-*.ts`, theo cấu trúc `ice-ult-sprites.ts`/`ice-ult-frost.ts`: cụm rễ/gai gỗ billboard trục Y mọc theo vòng sóng 30 m, dày ở vành; decal rễ phủ đất lan rồi tan 2,5 s; một mầm sáng ở tâm là điểm nhấn HDR duy nhất; lá và bào tử sáng nhạt (mỗi kênh ≤ 0,9).
3. Quái: **không bọc thân**. Vòng dây leo xoay dưới chân (decal), vài lá/bào tử bay quanh hông, tông xanh lục nhẹ trên vật liệu clone; trói 3 s rồi rễ vỡ thành mảnh gỗ và bụi sáng. Instancing chung.
4. Nối vào lab cạnh chiêu băng (phím 8, mục kế tiếp), giữ clip video cũ `ult-wood-primordial-tree` bật được bằng một phím để so sánh. Âm thanh: dùng thư viện âm mộc có sẵn (mọc, nứt, vỡ); nếu thiếu, ghi trong báo cáo.

## Nghiệm thu
- Kiểm kiểu sạch; probe CPU 100 quái như phiếu 390. Ảnh lab góc trên và sau lưng cạnh `ult-wood-moment-b` trong `typing-game-review/owner-review/2026-11-16/tu-tien/ult-wood/` có `ABOUT.md`; nếu sandbox chặn, ghi rõ.
- Ghi thành phần mới vào `docs/games/tu-tien/skills/VFX_LIBRARY.md`.
- Ngoài worktree chỉ được sửa thêm đúng một file: `docs/games/tu-tien/skills/VFX_LIBRARY.md` (repo chính). Trong worktree chỉ sửa: `src/lab/` (file mới + chỗ nối trong `skills-main.ts`), `art-src/lab/vfx/wood-ult/`. Không đụng file `ice-ult-*`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/395-report.md`.
