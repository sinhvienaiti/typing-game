# Phiếu 290 · Tu Tiên · Code: làm ấm bầy rồng khí lúc nạp (lab), lần tung đầu không khựng

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/290-report.md`.

**Worktree:** `games/.wt-ic-dragon-swarm`, nhánh `claude/dragon-swarm-lab`, HEAD `fc3b3f7`. `?? art-src`, `?? node_modules` là link của Claude: không đụng. **Không lệnh git ghi.**

## Vì sao
Bài học cổng 7 của chiêu lửa (phiếu 280, 283, 286): chương trình shader và texture biên dịch, tải lên lúc tung chiêu lần đầu làm khung hình khựng 30–235 ms. Bầy rồng khí (`src/lab/dragon-swarm-energy.ts`, `?key2=energy`) có nhiều chương trình chưa từng vẽ trước lần tung đầu: `FRAG_QI` trên mesh skinned, `DEPTH_PREPASS` skinned, ngọc (`PEARL_FRAG`, 3 sprite), dải râu `Trail`, `Glints` (Points). Texture: map Tripo 4096², `qi-scales.png`, dải lửa, sao, Kenney.

## Việc
1. Thêm `DragonSwarmEnergy.prewarm(renderer: THREE.WebGLRenderer, camera: THREE.Camera): Promise<void>`:
   - chờ `ready`;
   - tạm cho mọi rồng, ngọc, dải râu, glints hiện (đặt ngoài màn hoặc độ mờ 0 vẫn được vẽ), gọi `renderer.compileAsync` (hoặc `compile`) trên nhóm, `renderer.initTexture` cho mọi texture dùng tới;
   - một lần vẽ ngoài màn 64×64 nếu cần để skinning và depth prepass được biên dịch đúng biến thể;
   - trả lại đúng trạng thái cũ (visible, opacity, uniform, `time = -1`); không thẻ nào còn sống.
2. Gọi `prewarm` một lần trong `src/lab/skills-main.ts` ngay sau khi `swarmE.ready` xong (chỉ khi `?key2=energy`).
3. Test `tests/lab/dragon-swarm-prewarm.test.ts` với renderer giả: `compile`/`compileAsync` được gọi khi mọi vật liệu của bầy đang hiện; mọi texture qua `initTexture`; sau `prewarm` trạng thái hiện/ẩn và `running` như trước. Dùng lại cách dựng chuỗi xương của `tests/lab/dragon-swarm-motion.test.ts` nếu cần, hoặc mock `loadModel`.

### Được ghi
`src/lab/dragon-swarm-energy.ts` (chỉ thêm `prewarm` và phần cần cho nó), `src/lab/skills-main.ts` (chỉ dòng gọi), `tests/lab/dragon-swarm-prewarm.test.ts`, `docs/codex-queue/290-report.md` ở repo cha.

### Cấm
Mọi lệnh git ghi; đổi hình, số, nhịp, chuyển động; sửa tệp khác; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua, gồm 106 ca chuyển động; ghi tổng số test.
3. Liệt kê trong báo cáo: các chương trình và texture được làm ấm.

## Claude làm sau
Đo khung bấm phím 2 đầu tiên trong lab (≤ 11,5 ms), commit.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
