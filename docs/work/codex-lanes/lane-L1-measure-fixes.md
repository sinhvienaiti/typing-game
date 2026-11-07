# Làn 1 · Sửa phép đo của 3 hiệu ứng làm thử (cổng boss, vòng Huyết, tia trúng đòn)

Nguồn: `docs/work/consult/codex-pilot-verdict.md` §5 (các mục "Sửa cỡ cổng P1", "Nối P2 vòng Huyết", "Kích P4 không bị channel che").
- Cổng boss chỉ chiếm 0,0017 % khung ở cả bản cũ lẫn bản mới.
- Vòng Huyết chưa có chiêu nào gọi tới.
- Tia trúng đòn bị luồng trắng của `channel` che.

**Mức `high`.** Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`. Ngân sách: `path-to-8.md` §7.

## Việc
1. **Cổng boss (P1):** tìm vì sao cổng vẽ quá nhỏ hoặc nằm ngoài khung ở camera chơi (cỡ theo thân boss, pivot, độ cao). Sửa cho cổng rộng khoảng 1,5–2 lần thân boss, đặt ở chỗ boss sinh ra. Bản cũ và bản làm thử dùng chung cách đặt.
2. **Vòng Huyết (P2):** nối vai trò `ringBurst` vào `CLIP_ROLES` và cho một chiêu Huyết đang có trong lab dùng nó, ví dụ chiêu Huyết đang gọi `release` hay `impact`, đặt dưới chân hoặc tại điểm chạm. Thêm hàm `__lab` để kích riêng vòng này khi quay.
3. **Tia trúng đòn (P4):** thêm cách kích một cú trúng nhẹ đơn lẻ không có luồng `channel`, ví dụ `__lab.hit({ power: "light", directional: false })` hoặc tương đương, để quay riêng `beast-hit-spark-burst`.
4. Sửa `scripts/visual/scenarios/lab-pilot-ab.mjs`: P1, P2, P4 dùng cách kích và khung mới, giữ ngưỡng ≥ 0,5 % điểm ảnh hiệu ứng.

## Ranh giới
- **Được ghi:**
  - `src/lab/foe-flipbook-fx.ts`, `src/lab/clip-skills.ts`, `src/lab/skills-main.ts`;
  - kịch bản trên;
  - test trong `tests/lab/`;
  - báo cáo.
- **Không:** sửa media hay manifest.

## Đạt khi
- Có test node.
- `npx --no-install tsc --noEmit` sạch.
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ.
- `node --check` kịch bản qua.

## Chốt của Claude (07/11 12:35)
Được sửa **tối thiểu** 2 file trong `src/view/skills/` cần cho vai trò `ringBurst`, ghi lý do trong báo cáo. Không đổi hình hay nhịp của chiêu khác. Tự chạy `npx --no-install vitest run --maxWorkers=4` toàn bộ.
