**Owner miễn luật hạn mức 16/11 (nguyên văn):** "tôi đã nói cứ cho codex làm đi, tôi sẽ reset codex sau".


Phản biện: PASS (Sonnet, 16/11; 427 sửa tiêu đề và số đo theo phản biện)
# Phiếu 427: Tuyệt kỹ Hư Không — thay thẻ phẳng đứng bằng mô hình 3D (GLB Tripo có sẵn)


## Bối cảnh
(Tên file giữ chữ `blender` vì lịch sử phiếu; phiếu này **không** chạy Blender.)
Owner 16/11 duyệt cho tuyệt kỹ Mộc: "Đổi cách: rễ 3D từ Blender" rồi "Giữ 3D, chỉnh vật liệu" — thẻ phẳng không đọc được ở góc sau lưng. Mộc đã làm theo cách này (`games/.wt-ic-lab-all/src/lab/wood-ult-roots3d.ts`, `art-src/lab/vfx/wood-ult/roots3d/`: script Blender, GLB, InstancedMesh mỗi mẫu). Tuyệt kỹ Hư Không hiện khoảng 6,5/10 từ trên, yếu từ sau lưng vì cùng lỗi. Owner 16/11: "cứ giao cho codex việc xử lý code đi".

## Việc (worktree `games/.wt-ic-lab-all`)
1. **Không dựng Blender** (owner 16/11: "phần blender bạn xử lý đi, tránh để giao cho codex"). Dùng mô hình Tripo đã có: `art-src/lab/vfx/void-ult/models3d/tripo/ult-void-clean.tripo.v1.glb` (5.930 tam giác, cụm 5 tinh thể). Vật liệu trong code: kính tím trong (transmission giả hoặc fresnel), viền tím trắng, lõi phát sáng nhẹ ≤ 0,9 mỗi kênh; giữ texture gốc làm màu nền nếu đẹp.
2. File mới `src/lab/void-ult-3d.ts` theo đúng cấu trúc `wood-ult-roots3d.ts`: một InstancedMesh mỗi mẫu, thay các thẻ đứng ở vành, đặt theo vòng hiện có của `void-ult-sprites.ts` (tâm theo quái, bán kính 7–14 m), mọc theo sóng, giữ trong lúc trói, rồi tan/vỡ. Nối bằng một dòng gọi trong `void-ult-sprites.ts`. Lớp phụ mỗi kênh ≤ 0,9; điểm nhấn tâm vẫn là HDR duy nhất.
3. Ghi thành phần mới vào `docs/games/tu-tien/skills/VFX_LIBRARY.md`.

## Nghiệm thu
- Kiểm kiểu strict 0 lỗi; script check của Hư Không (`src/lab/void-ult-check*` nếu có, hoặc probe mới) chạy đạt: số instance, không mesh thừa, xoá/tung lại 5 lần không rò.
- GLB nạp đúng, ~5,9k tam giác mỗi instance; tổng tam giác lúc đỉnh và p95 thời gian khung hình (ms, đo trên `stress.html` với 100 quái, trong lúc trói) ≤ 16,7 ms, nếu sandbox chặn đo thì để lệnh cho Claude. Không có thẻ nào che người tung chiêu (vành tránh vùng 2 m quanh người tung).
- Để lệnh chụp góc trên/sau lưng lúc trúng đòn và lúc trói cho Claude (sandbox chặn trình duyệt).
- Chỉ sửa trong worktree: `src/lab/void-ult-*`, `art-src/lab/vfx/void-ult/`; và `VFX_LIBRARY.md`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/427-report.md`.
