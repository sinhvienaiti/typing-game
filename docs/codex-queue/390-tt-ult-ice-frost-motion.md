# Phiếu 390: Bỏ vỏ băng bọc quái, thay bằng hiệu ứng băng chuyển động


Phản biện: PASS (Sonnet, 16/11, vòng 2)
## Bối cảnh
Owner 16/11/2026 xem bản v3 (phiếu 389): "tạm đẹp đó, nhưng vì sao băng lại bọc quanh người nhân vật xấu vậy, nó nên là kiểu hiệu ứng gì đó chuyển động chứ bọc quanh người thì hơi xấu, nó cũng che luôn nhân vật, nên đổi". Rừng tinh thể, mặt băng nứt và bông tinh thể ở tâm giữ nguyên.

## Ảnh tham chiếu và thành phần (chỉ dùng ảnh có sẵn, không tạo ảnh mới)
Tất cả trong `games/.wt-ic-lab-all/art-src/lab/vfx/` (cùng nội dung với `games/immortality-cultivation/art-src/lab/vfx/`):
- mảnh băng bay: `ice-ult/shard-0.png`, `shard-1.png`, `shard-2.png`;
- lấp lánh và bụi: `ice-ult/glint.png`, `ice-ult/sparkles.png`, `ice-ult/dust.png`;
- vòng sương dưới chân: `ice/ice-ground-mark.atlas.png` (hoặc `ice/ice-caster-seal.atlas.png`), ảnh tĩnh do code xoay, co giãn và mờ dần;
- tông bố cục đích: `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png`.
Nếu thiếu file nào, dừng và ghi trong báo cáo, không tự vẽ bằng code.

## Việc
Worktree: `games/.wt-ic-lab-all`. Trong `src/lab/ice-ult-sprites.ts` (và `src/lab/ice-ult-layered.ts` nếu cần; instancing đặt trong các file này hoặc một file mới trong `src/lab/`):
1. Bỏ billboard vỏ băng `round-shell` ôm quái. Theo luật "thay, không chỉ bỏ": giữ asset trong `art-src/lab/vfx/ice-ult/` và ghi vào `docs/games/tu-tien/skills/VFX_LIBRARY.md` là không dùng.
2. Thay bằng hiệu ứng trói chuyển động, **không che mô hình quái** (mô hình phải nhìn rõ trong suốt 3 s):
   - một vòng sương băng mỏng xoáy chậm dưới chân quái (decal mặt đất, quay, nhịp sáng nhẹ);
   - 4–8 mảnh băng nhỏ (từ ảnh `shards-sparkle`) bay quỹ đạo quanh thân, ngang hông, bán kính lớn hơn bán kính quái;
   - hạt lấp lánh và bông tuyết rơi nhẹ quanh quái;
   - mô hình quái đổi tông xanh lạnh nhẹ (tint/fresnel trên vật liệu đã clone, không phủ lớp đục), và đứng hình như bản v1.
   Mọi lớp phụ nhạt, mỗi kênh ≤ 0,9. Điểm nhấn duy nhất vẫn là bông tinh thể ở tâm.
3. Hết 3 s: các mảnh bay rời ra ngoài và tan thành bụi lấp lánh, vòng dưới chân vỡ; số sát thương giữ như cũ.
4. Chi phí: dùng instancing chung cho mọi quái (không tạo mesh riêng mỗi quái).

## Nghiệm thu
- Chụp lab góc trên và góc sau lưng giữa lúc trói: quái nhìn rõ hình dáng, không bị khối trắng che.
- 100 quái trên `stress.html`: p95 ≤ 16,7 ms. Nếu sandbox chặn đo, ghi rõ và để lại lệnh đo để Claude chạy; ít nhất báo số instance và số draw call thêm vào (mục tiêu ≤ 4 draw call cho mọi quái).
- Chỉ sửa trong `games/.wt-ic-lab-all`: `src/lab/ice-ult-*.ts`, file mới trong `src/lab/`, `art-src/lab/vfx/ice-ult/`, `VFX_LIBRARY.md`. Không đụng file bản đồ 387, `view/ground.ts`, `rules.ts`.
- Không commit, không đưa media vào Git, không đổi nhánh.

## Giao nộp
Ảnh chụp trong `typing-game-review/owner-review/2026-11-16/tu-tien/ult-ice-v3/frost-motion/` kèm `ABOUT.md`. Báo cáo `docs/codex-queue/390-report.md`.
