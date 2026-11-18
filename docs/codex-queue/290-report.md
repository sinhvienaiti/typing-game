# Phiếu 290 · Làm ấm bầy rồng khí trong lab

**Trạng thái:** xong phần code và kiểm tự động, 05/11/2026. Chưa đo GPU lần tung đầu.

## Đã làm

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-dragon-swarm`, nhánh `claude/dragon-swarm-lab`, HEAD giữ nguyên `fc3b3f7`.

- `src/lab/dragon-swarm-energy.ts`: thêm `prewarm(renderer, camera)`, chờ `ready`, thu texture từ thuộc tính vật liệu và uniform, tạo và tải bone texture của từng skeleton. Tạm hiện toàn bộ nhánh và vật liệu, tắt culling, biên dịch lần lượt biến thể màn hình và buffer tuyến tính bằng `compileAsync` (dự phòng `compile`), rồi vẽ một lượt ngoài màn 64×64 và hủy target.
- Ngữ cảnh biên dịch và vẽ giữ sương cùng các đèn đang hiện của scene thật, vì chúng cũng nằm trong khóa chương trình Three.js r170. Scene tạm chỉ mượn tham chiếu bầy rồng và đèn; không chuyển parent, không vẽ nhân vật khác.
- Hoàn trả `visible`, `frustumCulled`, trạng thái hiện vật liệu và render target/cube face/mipmap ngay trước mỗi lần chờ bất đồng bộ, kể cả khi có lỗi. Không đổi opacity, uniform, tư thế, nhịp hay thông số chuyển động; không gọi `cast`/`update`, không phát hạt. Khi nạp xong, `time` vẫn là `-1`; nếu đã có chuyến bay thì giữ nguyên trạng thái của nó.
- `src/lab/skills-main.ts`: thêm đúng một dòng gọi sau `swarmE.ready`, chỉ trong nhánh `?key2=energy`.
- `tests/lab/dragon-swarm-prewarm.test.ts`: thêm 10 ca dùng renderer giả và model giả có chuỗi 40 xương. Kiểm chờ tải, mọi vật liệu hiện lúc compile/render, hai đường compile, đủ texture và chống tải trùng, hoàn trả trạng thái nghỉ/đang bay, không sinh hạt, không đè chuyến bay được kích hoạt lúc chờ, đúng sương/đèn và dọn target khi lỗi.

## Các chương trình được làm ấm

Các nhánh thực sự gắn trong bầy đều được duyệt, với cả đầu ra màn hình và buffer tuyến tính:

| Thành phần | Chương trình/vật liệu |
| --- | --- |
| Thân rồng khí | `VERT_QI` + `FRAG_QI` trên `SkinnedMesh` |
| Lượt ghi độ sâu của rồng khí | `DEPTH_PREPASS` (`MeshBasicMaterial`, skinned, `colorWrite: false`) |
| Ngọc | `PEARL_VERT` + `PEARL_FRAG` |
| Hào quang, vòng, xoáy của ngọc; sáng đầu rồng | `SpriteMaterial` |
| Hai dải râu mỗi rồng (`Trail`) | `MeshBasicMaterial`, texture và vertex color |
| Hạt sao (`Glints`) | `PointsMaterial`, texture và size attenuation |
| Vùng sáng đất khi `?pools=1` | `MeshBasicMaterial`, texture |

Nếu chọn các look sẵn có khác, cùng phép duyệt làm ấm `VERT_TEX` + `FRAG_TEX` (`full`), hoặc `VERT` + `FRAG` và `DEPTH_ONLY` skinned (`shell`). Các look này không bị sửa.

## Các texture được làm ấm

Mỗi đối tượng texture dùng để vẽ đi qua `renderer.initTexture` một lần trong mỗi lần prewarm:

- Map Tripo 4096² trong `/art-src/lab/models/qi-dragon/qi-dragon.rig.glb` (`uMap`; map của model tương ứng nếu chọn look khác).
- `/art-src/lab/models/qi-dragon/qi-scales.png` (`uScale`).
- `/art-src/lab/vfx/aura/strips/strip-fire-sheath-v2.rgba.png` (`uFlame` và râu).
- `/art-src/lab/tex/star_04.png` (glints).
- `/art-src/lab/tex/flare_01.png` (sáng đầu rồng).
- `/art-src/lab/tex/circle_05.png` (hào quang ngọc và vùng sáng đất nếu bật).
- `/art-src/lab/tex/circle_04.png` (vòng ngọc).
- `/art-src/lab/tex/light_01.png` (xoáy ngọc).
- Bone `DataTexture` riêng của từng skeleton; thân và depth prepass dùng chung skeleton nên không tải trùng.

`light_02.png` vẫn được `build()` tải theo mã cũ nhưng không gắn vào vật liệu nào; ngọc hiện dùng `circle_05.png`. Không làm ấm texture không được dùng, không sửa phần tải cũ.

## Kiểm bắt buộc

Chạy tại worktree, dùng công cụ đã cài và khóa CPU chung của Mac:

```sh
../../.local/bin/heavy.sh --cores=1 node node_modules/typescript/bin/tsc --noEmit -p .
../../.local/bin/heavy.sh --cores=4 env VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4 --reporter=dot --silent
git diff --check
```

- TypeScript: **PASS**, mã thoát 0.
- Vitest 3.2.7: **90/90 tệp, 1.095/1.095 test PASS**, 11,75 giây. Bao gồm **106/106 ca chuyển động** và **10/10 ca prewarm**.
- Kiểm khoảng trắng diff: **PASS**.
- Lần gọi đầu bằng `pnpm exec` lỗi SQLite khi pnpm tự kiểm kho phụ thuộc, trước khi chạy TypeScript. Đã dùng trực tiếp binary có sẵn cho các kết quả PASS nêu trên; không cài phụ thuộc.

## Để Claude kiểm sau

- Đo khung bấm phím 2 đầu tiên tại lab `?key2=energy`, mục tiêu **≤ 11,5 ms**. Test renderer giả xác nhận đường làm ấm và trạng thái; chưa chứng minh thời gian GPU thật.
- Không mở cổng mạng, không chạy build hay browser, không tạo ảnh/âm/capture. Không chạy lệnh Git ghi; hai link `art-src`, `node_modules` giữ nguyên. Chỉ sửa ba tệp được phép trong worktree và báo cáo này ở repo cha.
