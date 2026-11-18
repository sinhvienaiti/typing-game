# Báo cáo phiếu 286 · Làm ấm ba chương trình shader còn muộn

**Hoàn tất mã và kiểm tự động.** TypeScript qua; **1014/1014 test, 93/93 tệp** qua; build wrapper 274 qua và đã xóa đầu ra. **Cổng 7 chờ Claude đo lại**, chưa kết luận GPU ≤ 11,5 ms. Không commit hoặc gộp.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD `9434ac2`. Hai link có sẵn `?? art-src`, `?? node_modules` giữ nguyên.

## Đã làm

| Tệp trong worktree | Thay đổi |
| --- | --- |
| `src/view/screen-fx.ts` | `ImpactPass.prewarm()` compile vật liệu thật cho màn hình bằng quad tạm trong scene không ánh sáng/sương; giữ lượt render mask ngoài màn hình; khôi phục sampler/target và dọn quad/geometry khi xong hoặc lỗi. |
| `src/view/renderer.ts` | Trong prewarm chung, tạm bật bóng cho mesh skinned/instanced có map, cho renderer và các đèn đổ bóng cập nhật shadow map; trả lại mọi cờ bằng `finally`. Giữ đúng một lượt render 64×64 mỗi nguyên tố của 283. |
| `tests/view/skill-prewarm-shared.test.ts` | Thêm 8 ca, tổng tệp 14 ca: bóng mapped skinned/instanced, biến thể impact Hỏa/Kim, khôi phục khi thành công và khi lỗi. |
| `docs/changelog/2026-11-05-fire-lot1-art.md` | Ghi thay đổi và kiểm 286. |

Báo cáo này ở repo cha: `docs/codex-queue/286-report.md`.

## Đối chiếu shader

Đã mở hai tệp `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/code-drawn/lot1/recheck-283/stall-ids-fire.json` và `stall-ids-metal.json`. Chúng **không chứa ID chương trình dạng số**, chỉ chứa loại, độ dài nguồn, define và varying; không suy đoán ID.

| Log | Dấu hiệu nhận dạng | Chương trình cần làm ấm |
| --- | --- | --- |
| Hỏa, khung 6 | `ShaderMaterial`, vertex 1652, fragment 11262, varying `vUv` | `ImpactPass`, có `ROLES`, biến thể màn hình. |
| Kim, khung 6 | `ShaderMaterial`, vertex 1637, fragment 11247, varying `vUv` | Cùng `ImpactPass`, không có `ROLES`, biến thể màn hình. |
| Kim, khung 7 | `MeshDepthMaterial`, vertex 14842, fragment 12228; `USE_MAP`, `USE_SKINNING`, `USE_SHADOWMAP`, `DEPTH_PACKING 3201` | Bóng của mesh skinned có map. |
| Kim, khung 7 | `MeshDepthMaterial`, vertex 14844, fragment 12228; `USE_MAP`, `USE_INSTANCING`, `USE_SHADOWMAP`, `DEPTH_PACKING 3201` | Bóng của mesh instanced có map. |

Qi slash dùng varying `vP`, nên không phải shader trong log. Trước sửa, pass impact chỉ prewarm bằng render vào target mask tuyến tính, trong khi lúc trúng nó có thể là pass cuối vẽ ra màn hình. Nay compile thêm đúng đích màn hình, không vẽ warmup lên màn hình. Vật liệu thật còn sống để giữ chương trình; chỉ quad và geometry tạm được dọn.

Không sửa `element-stage.ts` hoặc `skills-main.ts`: vòng nạp Hỏa/Kim của 283 đã gọi `screen.prewarm()` và `stage.prewarm()` trước `ready`. Không đổi hình, thông số, thời gian, RNG, sim hoặc âm thanh. Không gọi cast/emit/update; pool rỗng vẫn rỗng sau prewarm.

## Kiểm bắt buộc

Chạy trong worktree được giao, qua bộ khóa `.local/bin/heavy.sh` của repo cha; không chạy game chính hoặc game khác.

1. **PASS**, thoát 0: `node node_modules/typescript/bin/tsc --noEmit -p .`.
2. **PASS**, thoát 0: `VITEST_MAX_THREADS=4 …/heavy.sh node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`. **1014/1014 test, 93/93 tệp**; giữ toàn bộ mốc 1006, thêm 8 ca. Lượt riêng tệp prewarm cũng qua **14/14**.
3. **PASS:** trong compile/render, test thấy cả mapped `SkinnedMesh` và `InstancedMesh` có `castShadow = true`, có một instance khi pool vốn rỗng và shadow map được cập nhật. Sau thành công hoặc lỗi compile/render, trả lại cả cờ true/false ban đầu, visibility, culling, count, ma trận, target và cờ cập nhật bóng; không còn thẻ sống. Test impact kiểm riêng Hỏa/Kim, sampler, geometry tạm và các lỗi mask/compile/render.
4. **PASS build**, thoát 0: dùng `.local/codex-runs/274-out/build-no-cache.mjs`, chỉ thay chuỗi `/private/tmp/codex-274-dist` thành `/private/tmp/codex-286-dist` trong bộ nhớ. Giữ `--no-cache --configLoader runner --outDir`, cache riêng `IC_VITE_CACHE_DIR=/private/tmp/codex-286-dist/.vite-cache` và điều kiện thư mục mới. Không sửa wrapper. Quét bundle không có `prewarmReport` hoặc `fxcode`; đã xóa `/private/tmp/codex-286-dist`.
5. **PASS phạm vi:** `git diff --check` sạch; worktree chỉ thay bốn tệp trong bảng và còn đúng hai link không theo dõi có sẵn. Repo cha chỉ ghi báo cáo này; không đụng thay đổi của luồng khác.

Log tạm: `/private/tmp/codex-286-tsc.log`, `/private/tmp/codex-286-prewarm.log`, `/private/tmp/codex-286-vitest.log`, `/private/tmp/codex-286-build.log`.

## Bàn giao

Claude đo lại cổng 7 cho cả Hỏa và Kim: khung bấm phím, khung trúng đầu và khung sau trúng; đối chiếu không còn ba chương trình biên dịch muộn, kiểm hình/nhịp rồi mới commit và gộp theo phiếu. Không mở cổng mạng, chạy trình duyệt, tạo capture hoặc sửa media/link. Không có phần bị bỏ vì hạn mức; không gặp mốc giờ phải đợi.
