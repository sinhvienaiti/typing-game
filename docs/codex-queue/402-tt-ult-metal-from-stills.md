# Phiếu 402: Dựng tuyệt kỹ Kim trong lab theo ảnh 396


Phản biện: PASS (Sonnet, 16/11; 402 sau khi sửa hai chỗ critic chỉ ra)

## Bối cảnh
Chiêu băng v3 (389, 390) được owner khen "tạm đẹp" nhưng chê vỏ bọc che quái; bản 390 đã thay bằng trói chuyển động. Làm chiêu Kim theo cùng cách. Ảnh chọn (theo miễn trừ ảnh của owner 15/11; owner chưa phản đối): `games/immortality-cultivation/art-src/concept/ult-metal/ult-metal-moment-b.v1-try1.png` (bố cục), `ult-metal-components.v1-try2.png` (thành phần), ô mặt đất vết chém trong bảng thành phần (mặt đất).

## Việc (worktree `games/.wt-ic-lab-all`)
1. Script cắt thành phần từ ảnh (nền đen → alpha), xuất vào `art-src/lab/vfx/metal-ult/`. Không vẽ lại, không tạo hình bằng code.
2. File mới `src/lab/metal-ult-*.ts`, theo cấu trúc `ice-ult-sprites.ts`/`ice-ult-frost.ts`: cụm kiếm/lưỡi khí vàng kim billboard trục Y mọc theo vòng sóng 30 m, dày ở vành; decal vết chém trên đất lan rồi tan 2,5 s; một điểm nhấn kiếm sáng ở tâm là điểm nhấn HDR duy nhất; tia kim loại và bụi vàng nhạt (mỗi kênh ≤ 0,9).
3. Quái: **không bọc thân**. Vòng kiếm xoay dưới chân (decal), vài lưỡi kiếm nhỏ bay quanh hông, tông vàng kim nhẹ trên vật liệu clone; trói 3 s rồi kiếm vỡ thành mảnh kim loại và tia lửa. Instancing chung.
4. Nối vào lab cạnh chiêu băng (phím 8, mục kế tiếp), giữ clip video cũ `ult-metal-geng` bật được bằng một phím để so sánh. Âm thanh: dùng thư viện âm Kim có sẵn (kiếm ngân, chém, vỡ kim loại); nếu thiếu, ghi trong báo cáo.

## Nghiệm thu
- Kiểm kiểu sạch; probe CPU 100 quái như phiếu 390. Ảnh lab góc trên và sau lưng cạnh `ult-metal-moment-b` trong `typing-game-review/owner-review/2026-11-16/tu-tien/ult-metal/` có `ABOUT.md`; nếu sandbox chặn, ghi rõ.
- Ghi thành phần mới vào `docs/games/tu-tien/skills/VFX_LIBRARY.md`.
- Ngoài worktree chỉ được sửa thêm đúng một file: `docs/games/tu-tien/skills/VFX_LIBRARY.md` (repo chính). Trong worktree chỉ sửa: `src/lab/` (file mới + chỗ nối trong `skills-main.ts`), `art-src/lab/vfx/metal-ult/`. Không đụng file `ice-ult-*`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/402-report.md`.

## Bài học từ 395
Phiếu 395 (tuyệt kỹ Mộc) lần đầu bị trượt vì vành quá thưa, tâm không đọc được và một thẻ quá to che người tung chiêu. Ngay từ đầu: vành dày và chồng lấn như ảnh đích, điểm nhấn tâm đọc rõ từ góc trên, không thẻ nào che nhân vật hay quá 15 % khung. Ảnh chọn là `ult-metal-moment-b.v1-try1.png` (gợi ý của Codex, theo miễn trừ ảnh 15/11; owner chưa chọn, nếu owner chọn A thì phiếu sau chỉnh).
