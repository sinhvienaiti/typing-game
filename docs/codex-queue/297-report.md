# Báo cáo phiếu 297 · Làm ấm vật liệu số sát thương

**Hoàn tất mã và ba kiểm bắt buộc.** TypeScript qua; **1037/1037 test, 94/94 tệp** qua; build wrapper 274 qua, grep sạch và đã xóa đầu ra. Chưa đo thời gian GPU; Claude kiểm lại khung 13 Hỏa/Kim khi máy rảnh.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD giữ `c15af6f`. Không dùng lệnh Git ghi; giữ nguyên hai link `art-src`, `node_modules`.

## Nguyên nhân và khóa lúc chơi

Đối chiếu ghi nhận khung 13 trong `docs/work/tasks/key1-fire.md`, nguồn `hitfx.ts` và `WebGLPrograms.js`/`WebGLRenderer.js` của Three **0.170.0** đang cài. `IcNumberSprites.render()` vẽ scene số riêng sau hậu kỳ; lượt prewarm cũ ghép scene đó vào scene chiến đấu. Số đèn, cờ sương và bóng vẫn thuộc khóa dù vật liệu không dùng đèn/sương. Đích hậu kỳ còn khác màn hình ở không gian màu và tone mapping.

| Thành phần khóa/trạng thái | Overlay lúc chơi, được làm ấm thêm |
| --- | --- |
| Vật liệu/nguồn | Chính `ShaderMaterial`, `NUMBER_VERTEX`/`NUMBER_FRAGMENT`; không thay nguồn hoặc hook |
| Define | `{}`; không define riêng |
| Blend/alpha | `NormalBlending`, transparent; `opaque = false`, `premultipliedAlpha = false`, không alpha test/hash/coverage. Blend không là một trường số riêng trong khóa r170; transparency/blending quyết định cờ `opaque`. |
| Mặt/độ sâu | `DoubleSide`, không đảo mặt; depth test/write tắt |
| Sương | `fog = false`, `useFog = false`, `fogExp2 = false` |
| Đèn/bóng | Mọi số đèn, bóng, light probe bằng 0; `shadowMapEnabled = false`. `shadowMapType = PCFSoftShadowMap` (2) vẫn có trong khóa khi renderer ở High. |
| Đích/màu | Target `null`, đầu ra sRGB, `NeutralToneMapping` (7) |
| Geometry | Mesh thường với `InstancedBufferGeometry` và `iRect/iUv/iColor/iTint`; `instancing = false` vì không phải `InstancedMesh`. Không skin, morph hoặc màu đỉnh. |
| Phần còn lại | `highp`, hỗ trợ vertex texture; không clipping, log/reverse depth. Uniform `uAtlas/uScreen/uRowY`; atlas thật được dùng lại. |

Khóa đầy đủ dựng bằng `WebGLPrograms.getProgramCacheKey()` trong một tiến trình sạch, cùng vật liệu và cấu hình renderer ở trên:

```text
0,1,highp,srgb,false,,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,,false,false,0,,0,0,0,0,0,0,0,0,0,0,0,2,7,0,0,0,1,2048,srgb,onBeforeCompile( /* shaderobject, renderer */ ) {}
```

Hai số đầu `0,1` là ID nguồn shader do bộ nhớ đệm cấp theo thứ tự trong tiến trình, không phải ID cố định ở phiên chơi. Test so khóa đầy đủ trong cùng bộ nhớ đệm, giữa prewarm và đường vẽ overlay thật. Đây là khóa dựng lại từ thuật toán Three và nguồn hiện tại, chưa phải log lấy từ GPU sau sửa.

Đối chứng trong test: ghép vật liệu vào scene chiến đấu cho `fog = true`, 3 đèn hướng, 4 đèn điểm, 1 bán cầu và bóng hướng, tạo khóa khác; scene overlay đúng nhưng target hậu kỳ cũng tạo khóa khác.

## Tệp đã ghi

Các đường sau tính từ worktree, trừ báo cáo này ở repo cha:

- `src/view/hitfx.ts`: truyền renderer vào điểm vào prewarm; compile scene/camera/vật liệu số thật ở target màn hình trước khi ghép mẫu vào lượt vẽ chung. `finally` trả target, count, bốn buffer glyph và `uScreen`; gỡ scene mẫu. Giữ nguyên field số sống và vật liệu/atlas.
- `src/lab/skills-main.ts`: vòng làm ấm Hỏa/Kim truyền renderer đang dùng cho `numbers.prewarm()`, chỉ một dòng.
- `tests/view/skill-prewarm-shared.test.ts`: cập nhật lời gọi và phân biệt lượt compile overlay với compile scene chiến đấu; giữ các kiểm tra cũ, thêm 6 ca về khóa đầy đủ và khôi phục số sống.
- `docs/changelog/2026-11-05-fire-lot1-art.md`: ghi nguyên nhân, sửa và kiểm.
- `docs/codex-queue/297-report.md` ở repo cha: báo cáo này.

Không cần sửa `renderer.ts` hoặc `element-stage.ts`: một lượt render scene 64×64 hiện có đã upload atlas/buffer; chỉ thiếu lượt compile đúng khóa overlay. Không thêm render, không vẽ mẫu lên màn hình, không đổi thứ tự mask/bóng của 291 hoặc đường vẽ khi chơi.

## Kiểm bắt buộc

Tất cả chỉ chạy trong worktree được giao, qua `.local/bin/heavy.sh` ở repo cha; không chạy game chính hoặc game khác:

1. **PASS**, thoát 0: `node node_modules/typescript/bin/tsc --noEmit -p .`.
2. **PASS**, thoát 0: `VITEST_MAX_THREADS=4 …/heavy.sh node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: **1037/1037 test, 94/94 tệp**. Tệp prewarm **23/23**, tăng 6 ca so với mốc 1031.
3. Test khóa dùng `WebGLPrograms.getParameters/getProgramCacheKey` và `WebGLLights` thật của Three r170; thay adapter GPU bằng mock để chạy Node. Hỏa/Kim đều đi từ `createSkillNumbers()` qua prewarm và `Overlay.draw()` thật. Kiểm trạng thái ngay sau prewarm: không còn glyph mẫu, scene không còn parent, target và kích thước trả lại; các ca có số sống giữ count, buffer, uniform và field sau thành công/lỗi compile riêng/lỗi compile chung/lỗi render. Giữ một lượt render ngoài màn hình và các test bóng của 291.
4. **PASS build**, thoát 0: dùng `.local/codex-runs/274-out/build-no-cache.mjs`, chỉ thay chuỗi `/private/tmp/codex-274-dist` thành `/private/tmp/codex-297-dist` trong bộ nhớ; đủ `--no-cache --configLoader runner --outDir /private/tmp/codex-297-dist`. Cache riêng `/private/tmp/codex-297-dist/.vite-cache`, đầu ra mới, không sửa wrapper.
5. **PASS grep**: `grep -rlE 'fxcode|stripK|prewarmReport' /private/tmp/codex-297-dist` không in gì, thoát 1 đúng nghĩa không tìm thấy. **Đã xóa** `/private/tmp/codex-297-dist`.
6. `git diff --check` sạch; chỉ các đường được phép thay đổi.

Log: `/private/tmp/codex-297-tsc.log`, `codex-297-prewarm.log`, `codex-297-vitest.log`, `codex-297-build.log`, `codex-297-bundle-scan.log`, `codex-297-number-key.log`.

## Bàn giao và phần chưa đo

Claude đo lại Hỏa/Kim đến ít nhất khung 13, kiểm không còn lượt link muộn của vật liệu số và đo cổng 7 ≤ 11,5 ms trên máy rảnh. Test chứng minh khóa khớp và trạng thái được trả lại; chưa chứng minh thời gian GPU thực tế. Không mở cổng mạng, chạy trình duyệt hoặc tạo capture trong phiếu này. Không còn phần mã bỏ dở; không gặp hạn mức hoặc mốc giờ phải đợi.
