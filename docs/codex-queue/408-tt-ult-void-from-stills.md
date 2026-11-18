# Phiếu 408: Dựng tuyệt kỹ Hư Không trong lab theo ảnh 398


Phản biện: PASS (Sonnet, 16/11)


## Bối cảnh
Chiêu băng v3 (389, 390) được owner khen "tạm đẹp" nhưng chê vỏ bọc che quái; bản 390 đã thay bằng trói chuyển động. Làm chiêu Hư Không theo cùng cách. Ảnh chọn (theo miễn trừ ảnh của owner 15/11; owner chưa phản đối): `games/immortality-cultivation/art-src/concept/ult-void/ult-void-moment-b.v1-try1.png` (bố cục), `ult-void-components.v1-try2.png` (thành phần), ô mặt đất vết chém trong bảng thành phần (mặt đất).

## Việc (worktree `games/.wt-ic-lab-all`)
1. Script cắt thành phần từ ảnh (nền đen → alpha), xuất vào `art-src/lab/vfx/void-ult/`. Không vẽ lại, không tạo hình bằng code.
2. File mới `src/lab/void-ult-*.ts`, theo cấu trúc `ice-ult-sprites.ts`/`ice-ult-frost.ts`: khe nứt không gian tím đen và mảnh kính lơ lửng billboard trục Y mọc theo vòng sóng 30 m, dày ở vành; decal vết nứt hư không trên đất lan rồi tan 2,5 s; một xoáy hút sáng ở tâm là điểm nhấn HDR duy nhất; hạt bị hút vào tâm, nhạt (mỗi kênh ≤ 0,9).
3. Quái: **không bọc thân**. Vòng nứt hư không xoay dưới chân (decal), vài mảnh kính bay quanh hông, tông tím lạnh nhẹ trên vật liệu clone; trói 3 s rồi mảnh kính vỡ và tan vào hư không. Instancing chung.
4. Nối vào lab cạnh chiêu băng (phím 8, mục kế tiếp), nếu lab có sẵn cách bật clip video cũ `ult-void` thì giữ, nếu không thì bỏ qua và ghi trong báo cáo. Âm thanh: dùng thư viện âm Hư Không có sẵn (hút, nứt, vỡ kính); nếu thiếu, ghi trong báo cáo.

## Nghiệm thu
- Kiểm kiểu sạch; probe CPU 100 quái như phiếu 390. Ảnh lab góc trên và sau lưng cạnh `ult-void-moment-b` trong `typing-game-review/owner-review/2026-11-16/tu-tien/ult-void/` có `ABOUT.md`; nếu sandbox chặn, ghi rõ.
- Ghi thành phần mới vào `docs/games/tu-tien/skills/VFX_LIBRARY.md`.
- Ngoài worktree chỉ được sửa thêm đúng một file: `docs/games/tu-tien/skills/VFX_LIBRARY.md` (repo chính). Trong worktree chỉ sửa: `src/lab/` (file mới + chỗ nối trong `skills-main.ts`), `art-src/lab/vfx/void-ult/`. Không đụng file `ice-ult-*`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/408-report.md`.

## Bài học từ 395
Phiếu 395 (tuyệt kỹ Mộc) lần đầu bị trượt vì vành quá thưa, tâm không đọc được và một thẻ quá to che người tung chiêu. Ngay từ đầu: vành dày và chồng lấn như ảnh đích, điểm nhấn tâm đọc rõ từ góc trên, không thẻ nào che nhân vật hay quá 15 % khung. Ảnh chọn là `ult-void-moment-b.v1-try1.png` (gợi ý của Codex, theo miễn trừ ảnh 15/11; owner chưa chọn, nếu owner chọn A thì phiếu sau chỉnh).

## Bài học thêm (Mộc, Kim 16/11)
- Vòng đặt theo vùng camera chơi thấy: tâm là trung bình vị trí quái trong tầm, bán kính 7–14 m, không 25–28 m.
- Thẻ phẳng không đọc được ở góc sau lưng; hình chính đứng (mảnh kính, khe nứt) nên có khối hoặc nhiều lớp thẻ giao nhau. Xong phiếu, agent Claude Opus sẽ chụp và chỉnh bằng mắt.
