# Báo cáo phiếu 280 · Làm ấm texture Hỏa lúc nạp

Đã làm phần mã, test mới và build trong phạm vi phiếu. **Chưa đạt toàn bộ kiểm bắt buộc:** kiểm kiểu qua, 5/5 test mới qua, toàn suite 998/1000 test qua; hai test prewarm cũ cần cập nhật nhưng nằm ngoài các đường được phép ghi. Chưa commit hoặc gộp; chưa đo lại ngưỡng GPU 11,5 ms.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD `ee3ee974ad749b20e78afc065fb0b44ff9e0fac4`. Đã đọc báo cáo 277 và 278; tiếp tục nguyên các thay đổi chưa commit. Hai link `?? art-src`, `?? node_modules` có sẵn lúc nhận, không đụng.

## Tệp đã ghi

Tính từ worktree, trừ báo cáo này ở repo cha:

| Tệp | Thay đổi của 280 |
| --- | --- |
| `src/view/skills/element-fire.ts` | Tải texture lên GPU khi thư viện hoặc dải nạp xong; tải cả sampler sprite/đất; loại lặp theo texture và phiên bản trên mỗi renderer. Biên dịch cả scene một lần, khôi phục visibility/target. Thêm trạng thái làm ấm và danh sách ID. |
| `src/lab/skills-main.ts` | Chỉ sửa import, chỗ gọi prewarm và kiểu/trường trả về của `fireImpact()`: truyền scene thật, chọn target theo pipeline đang chạy; thêm `prewarmed` và `textureIds`. |
| `tests/view/fire-prewarm.test.ts` | 5 test bằng renderer giả và texture trong bộ nhớ; không đọc media hoặc mở mạng. |
| `docs/changelog/2026-11-05-fire-lot1-art.md` | Bổ sung 280 và ghi rõ kết quả kiểm còn thiếu. |
| `docs/codex-queue/280-report.md` ở repo cha | Báo cáo này. |

Không cần sửa `element-stage.ts`. Không sửa `fxkit.ts` hoặc các test của 277–278 trong phiếu này; các thay đổi cũ vẫn giữ nguyên. Không đổi shader, kit, sim, nội dung, hình, thông số hoặc nhịp.

## Cách làm ấm

- Đợi riêng `ready("fire")`, `ready(BRUSH.folder)` và Promise nạp dải. Mỗi nhánh hoàn tất gọi `initTexture` cho atlas đang dùng và mask A/B của nó; nhánh dải chạy tiếp khi ảnh riêng xong. Không tải clip không dùng chỉ vì có trong thư viện.
- Quét texture trong uniform của các mesh Hỏa sau khi media xong: có các `SpritePool`, vật liệu đất và sampler rỗng. Texture dùng chung chỉ gọi một lần trên mỗi renderer; phiên bản ảnh mới được tải lại.
- Tạm hiện tất cả mesh Hỏa, gọi `renderer.compile(view.scene, camera)` một lần trong target thật: buffer bloom khi bloom bật, màn hình khi tắt. Giữ ánh sáng/sương của scene; không render ra màn. Khôi phục mọi visibility và target bằng `finally`.
- `__lab.fireImpact()` thêm `prewarmed: boolean`, chỉ đúng sau khi compile thành công, và `textureIds: number[]`, là ID Three.js của texture đã gọi `initTexture` thành công trên renderer này. Đọc trạng thái không làm đổi hiệu ứng.

## Kiểm bắt buộc

1. **PASS**, thoát 0: `node node_modules/typescript/bin/tsc --noEmit -p .`.
2. **CHƯA ĐẠT**, thoát 1: `VITEST_MAX_THREADS=4 /Volumes/SS990TPRO/htdocs/typing-game/.local/bin/heavy.sh node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`. Kết quả **998 qua / 2 lỗi / 1000 test**, **91 tệp qua / 1 tệp lỗi / 92 tệp**, 15,39 giây. Mốc 995 + đúng 5 test mới.
3. **PASS 5/5 test mới**, gồm: 19 texture riêng có đúng 19 lần `initTexture` trong bộ giả đầy đủ (có atlas, hai mask riêng, texture sprite, texture đất giả và sampler rỗng); compile scene đúng một lần sau tải; không render; không phát thẻ hoặc tăng tuổi; chờ brush/dải muộn; trả target bị đổi trong lúc chờ; khôi phục visibility khi compile lỗi; renderer riêng; thử lại khi upload lỗi. Lần chạy riêng cuối: thoát 0, 394 ms.
4. **PASS build**, Vite 7.3.7, 183 module, 859 ms, thoát 0. Dùng đúng wrapper 274 như báo cáo 278, chỉ thay chuỗi `/private/tmp/codex-274-dist` thành `/private/tmp/codex-280-dist` trong bộ nhớ. Giữ nguyên cờ `--no-cache --configLoader runner --outDir`, cache riêng và điều kiện thư mục chưa tồn tại. `grep -rl 'fxcode' /private/tmp/codex-280-dist`: không in gì, thoát 1. Đã xóa đúng thư mục build và xác nhận không còn.
5. **PASS phạm vi/diff:** `git diff --check` sạch. Trạng thái worktree chỉ có các tệp 277, 278, 280 và hai link có sẵn:

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

## Hai test cũ cần mở phạm vi

Trong `tests/view/fire-lot1-art.test.ts`:

- `loads the v2 strip through the fire library from the existing art URL`.
- `prewarms the final masked brush, flash and lot-1 programs without changing live effects`.

Cả hai hiện dừng ở `TypeError: renderer.initTexture is not a function`. Sau khi bổ sung mock này, phép kiểm `compile(pool.mesh, camera)` và callback nhận một mesh cũng phải chuyển sang scene: gọi compile một lần, duyệt các mesh con để giữ kiểm shader, mask, đặt dải, visibility, target và dữ liệu thẻ đang sống. Đây là thay đổi hợp đồng prewarm, không phải nới hoặc bỏ phép kiểm.

Đã hỏi chủ cho phép sửa đúng hai ca này, chưa có câu trả lời tại lúc viết báo cáo. Không sửa ngoài phạm vi và không thêm nhánh runtime để chiều renderer giả cũ. Cần cập nhật hai ca, chạy lại toàn suite rồi mới coi cổng test đạt.

## Bàn giao

Không chạy game chính, mở cổng mạng, tạo media/capture, sửa `art-src` hay dùng lệnh Git ghi. GPU và video giao Claude theo phiếu: kiểm `__lab.fireImpact().prewarmed === true`, đối chiếu `textureIds`, rồi đo lại cả khung bấm và khung trúng đầu ≤ 11,5 ms. Báo cáo CPU/test không chứng minh ngưỡng GPU đã đạt.

Không gặp hạn mức công cụ hoặc mốc giờ phải đợi. Phần còn thiếu là quyền cập nhật hai test prewarm cũ và phép đo GPU của Claude.
