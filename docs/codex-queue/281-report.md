# Báo cáo phiếu 281 · Cập nhật hai test prewarm cũ

Đã hoàn tất: **kiểm kiểu qua; 1000/1000 test, 92/92 tệp qua**. Chỉ sửa đúng hai ca trong `tests/view/fire-lot1-art.test.ts`; không nới hoặc bỏ phép kiểm, không sửa mã chạy. Chưa commit hoặc gộp.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD `ee3ee974ad749b20e78afc065fb0b44ff9e0fac4`. Tiếp tục nguyên các thay đổi chưa commit của 277, 278 và 280.

## Tệp đã ghi

- `games/.wt-ic-fire-lot1/tests/view/fire-lot1-art.test.ts`: chỉ hai ca `loads the v2 strip through the fire library from the existing art URL` và `prewarms the final masked brush, flash and lot-1 programs without changing live effects`.
- `docs/codex-queue/281-report.md`: báo cáo này ở repo cha.

Hai renderer giả có `initTexture`. Mỗi ca gắn layer vào một `THREE.Scene`, truyền scene đó cho `prewarmFire` và kiểm `compile(scene, camera)` đúng một lần. Callback duyệt các mesh con, giữ kiểm shader dải sau `onBeforeCompile`, mask A/B, visibility khi compile và sau khôi phục, kể cả khi compile ném lỗi. Giữ nguyên URL, metadata và wrap/color space của dải, target lúc compile và sau khi tải muộn, dữ liệu thẻ sống, thời gian, audit và luồng ngẫu nhiên. Ca nạp dải còn kiểm texture được chuyển cho `initTexture`.

## Kiểm bắt buộc

1. **PASS**, thoát 0:
   `/Volumes/SS990TPRO/htdocs/typing-game/.local/bin/heavy.sh node node_modules/typescript/bin/tsc --noEmit -p .`
2. **PASS**, thoát 0:
   `VITEST_MAX_THREADS=4 /Volumes/SS990TPRO/htdocs/typing-game/.local/bin/heavy.sh node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`
   Kết quả: **1000/1000 test, 92/92 tệp**, 11,80 giây; riêng `fire-lot1-art.test.ts` **7/7**. Không thêm, bỏ hoặc skip test.
3. **PASS phạm vi:** `git diff --check` sạch; tệp test chưa theo dõi cũng không có khoảng trắng cuối dòng. Đối chiếu nội dung trước/sau xác nhận phần ngoài hai ca không đổi. SHA-256 của mọi tệp có thay đổi sẵn khác đều giữ nguyên. `git status --short` trong worktree giống nguyên trạng lúc nhận, không thêm đường nào:

```text
 M src/lab/skills-main.ts
 M src/view/skills/element-fire.ts
 M src/view/skills/fxkit.ts
 M tests/view/element-layer.test.ts
 M tests/view/key1-brush-impact.test.ts
?? art-src
?? docs/changelog/2026-11-05-fire-lot1-art.md
?? node_modules
?? tests/view/fire-lot1-art.test.ts
?? tests/view/fire-prewarm.test.ts
?? tests/view/key1-flash-age0.test.ts
```

## Không làm và bàn giao

Không chạy build, game, trình duyệt hoặc tạo media/capture vì phiếu chỉ yêu cầu cập nhật test và các kiểm trên. Không đụng hai link `art-src`, `node_modules` có sẵn hoặc các tệp của 277–280 ngoài hai ca được mở phạm vi.

Không còn phần thiếu trong phiếu 281. Claude tiếp tục phần GPU/video đã bàn giao ở 280: kiểm trạng thái prewarm, ID texture và đo khung bấm/khung trúng đầu ≤ 11,5 ms; kết quả test này không thay cho phép đo GPU. Chủ xem video sau bước đó.

Không gặp hạn mức công cụ hoặc mốc giờ phải đợi.
