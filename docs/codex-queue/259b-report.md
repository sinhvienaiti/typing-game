# Báo cáo phiếu 259b · Tu Tiên · Vòng ngọc Clear Wind (05/11/2026)

**Trạng thái: đã làm đủ phần mã và kiểm được giao; chưa chỉnh ngoại hình.** Tiếp tục từ mã 259 chưa commit trong `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-immortality-cultivation-codex`. Phiếu sửa lúc 01:38 đã bỏ điều kiện phản biện; áp dụng `agent-orchestration`, “Working lean” §6, một luồng. Báo cáo này thay trạng thái chờ của lượt trước.

## Tệp đã sửa

Các đường dẫn sau tính từ worktree:

| Tệp | Kết quả |
| --- | --- |
| `src/view/skills/sword-material.ts` | Trần 0,95 dùng Rec. 709; giữ `swRingDe` ngoài trần; nhánh ghi trọng số khi `uSwRingOn > 1.5`; kẹp mép mềm bằng cạnh ô thật; thêm uniform chỉnh albedo, normal và sheen, dùng lại uniform roughness/glow. |
| `src/view/skills/blades.ts` | Chỉ bổ sung `texel: cell` vào kết quả `jadeRingOf`; thuật toán đo và các số cũ giữ nguyên. |
| `src/lab/skills-main.ts` | Cờ URL, API chỉnh/đọc ngọc, `ringCap()` và kiểu tương ứng; giữ `{ hero, mid }` để so số đo. |
| `scripts/visual/scenarios/lab-element-parity.mjs` | `MASK=1`: ngay sau ảnh màu đọc `bright`, rồi `ringCap`, rồi mặt nạ; ghi cả hai số đo vào shots. |
| `scripts/visual/ring-parity.mjs` | Chép `ringCap` của bản sau, thêm `ok`; tổng số khung lỗi/thiếu, tổng `soft` và `softMax` lớn nhất. |
| `tests/view/jade-ring.test.ts` | Kiểm ba dòng trần theo thứ tự, Rec. 709/mép tan, ca nghiêng 85°, uniform/mặc định, GGX/headroom, API lab, ba lượt HalfFloat và khôi phục khi lỗi. Tổng 16 test. |
| `docs/changelog/2026-11-04-lab-jade-ring.md` | Ghi công thức, tham số, phép đo và kiểm tra 259b bằng tiếng Việt. |

Ở repo cha chỉ cập nhật `docs/codex-queue/259b-report.md`. Không sửa báo cáo 259 hay script `jade-ring-measure.ts` có sẵn.

## Công thức chặn tràn

```text
texel = 2 × 1,25 × guardHalf / 512
swSoftMax = 1,5 × texel
swAr = min(max(fwidth(swD), 1e-5), swSoftMax)
swAz = min(max(fwidth(vSwP.z), 1e-5), swSoftMax)
```

`texel` đi từ `jadeRingOf` qua `JadeRing.texel` vào uniform riêng `uSwRingTexel`, kể cả overlay. Đo lại hai GLB bằng loader `tsx`: đầy đủ `texel = 0,0007119846850400791`, LOD `0,0007151773024816066`; biên mềm tối đa tương ứng `0,0010679770275601187` và `0,0010727659537224099`. Các số tâm, bán kính, mặt phẳng và margin trùng kết quả 259.

Test tổng hợp chiếu footprint một ô ở góc 85°: đạo hàm bán kính `texel / cos(85°)`, độ sâu `texel × tan(85°)`. Ba điểm cách biên bán kính/mặt trước/mặt sau 2 ô có trọng số cũ > 0 và sau kẹp = 0; điểm trong đĩa vẫn = 1. Dải khử răng cưa tối đa 1,5 ô vẫn được giữ.

## Các núm dành cho Claude

| URL | API | Mặc định | Kẹp | Uniform |
| --- | --- | --- | --- | --- |
| `jadeAlbedo` | `albedo` | 1 | 0–2 | `uSwRingTune.x` |
| `jadeRough` | `rough` | 0,34 | 0,04–1 | `uSwRingPbr.y` |
| `jadeNormal` | `normal` | 1 | 0–4 | `uSwRingTune.y` |
| `jadeSheen` | `sheen` | 0 | 0–1 | `uSwRingTune.z` |
| `jadeGlow` | `glow` | 0,06 | 0–0,15 | `uSwRingTone.z` |

Ví dụ `__lab.jadeRing({ albedo: 1, rough: 0.34, normal: 1, sheen: 0, glow: 0.06 })`. Trường thiếu giữ giá trị hiện tại, số không hữu hạn bị bỏ qua; setter vẽ lại với thời gian 0. `__lab.jadeRing()` chỉ đọc, trả năm số cùng `{ hero, mid }`. Tên cũ `jadeRingGlow` vẫn dùng được; `jadeGlow` ưu tiên nếu có cả hai.

Sheen dùng GGX điện môi F0 0,04, nhám 0,12, theo ánh sáng/bóng đèn điểm, spot và hướng. Chỉ nhân trọng số ngọc, cộng vào cả `swJadeE` và tổng emission trước quy tắc headroom có sẵn rồi qua trần vòng. Normal chỉnh normal map tiếp tuyến chỉ trong ngọc. Mặc định albedo/normal = 1 bỏ qua phép nhân mới, sheen = 0 bỏ qua nhánh mới; rough/glow giữ nguyên. Đã giữ đường tính mặc định theo yêu cầu; **chưa có bằng chứng ảnh GPU trùng từng điểm ảnh** ngoài hai thay đổi bắt buộc, vì phiếu cấm trình duyệt/cổng mạng.

## Kiểm tra

Từ worktree, qua khóa CPU có sẵn `../../.local/bin/heavy.sh`:

```sh
../../.local/bin/heavy.sh node node_modules/typescript/bin/tsc --noEmit -p .
VITEST_MAX_THREADS=4 ../../.local/bin/heavy.sh node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4
```

**tsc thoát 0; Vitest 933/933 test, 87/87 tệp, 6,75 s.** Không đổi golden. Test lab thực thi chính các khối cờ/API sau khi xóa kiểu TypeScript với renderer giả: xác nhận ba lượt 0/1/2, phân loại interior/over/soft/nonFinite, khôi phục uniform, sương, nền, target, màu clear, bóng và visibility khi thành công hoặc đọc lỗi. Đây là kiểm logic, không thay kiểm GPU.

CLI Vite với đủ `--no-cache --configLoader runner` **bị từ chối trước build**: `CACError: Unknown option --cache` (Vite 7.3.7). Không chạy lại CLI bằng cách bỏ cờ. Dùng wrapper Node nhận đủ hai cờ, kiểm chúng, bảo đảm output/cache chưa tồn tại, rồi gọi API tương đương:

```js
// node --input-type=module - --no-cache --configLoader runner
// IC_VITE_CACHE_DIR=/private/tmp/codex-259b-dist/.vite-cache
await build({
  configLoader: "runner",
  cacheDir: process.env.IC_VITE_CACHE_DIR,
  build: { outDir: "/private/tmp/codex-259b-dist" },
});
```

**Build thoát 0**, 183 module, 887 ms. Chỉ cảnh báo outDir ở ngoài project. `grep -rl 'jadeRingGlow\|ring-parity\|jadeSheen' /private/tmp/codex-259b-dist` không in gì, thoát 1 đúng yêu cầu. Đã xóa và xác nhận không còn thư mục build/cache.

Kiểm thêm đạt: `node --check` cho hai công cụ; `git diff --check`; đo GLB bằng `node --import ./node_modules/tsx/dist/loader.mjs scripts/visual/jade-ring-measure.ts`. Fixture PNG tổng hợp kiểm `ring-parity`: giữ trường tùy ý của ringCap, ca đạt/lỗi/không hữu hạn/thiếu, tổng `ringCapFailed = 2`, `ringCapMissing = 1`, `soft = 6`, `softMax = 1,3`. Kịch bản giả xác nhận đúng thứ tự `bright → ringCap → mask`, không gọi cả hai khi thiếu `MASK`. Dữ liệu fixture tạm đã xóa.

`git status --short` của worktree cuối lượt:

```text
 M scripts/visual/scenarios/lab-element-parity.mjs
 M src/lab/skills-main.ts
 M src/view/skills/blades.ts
 M src/view/skills/sword-material.ts
?? docs/changelog/2026-11-04-lab-jade-ring.md
?? node_modules
?? scripts/visual/jade-ring-measure.ts
?? scripts/visual/ring-parity.mjs
?? tests/view/jade-ring.test.ts
```

Chỉ tám tệp được phép của 259 và symlink `node_modules` đã có từ đầu. Repo cha có nhiều thay đổi của tác vụ khác; không can thiệp. Không chạy lệnh Git ghi, cài gói, sửa checkout game chính hoặc mở cổng mạng.

## Phần để Claude và anh xem

Không tạo ảnh/âm thanh/capture; không tự chỉnh nét, đổi texture/model hay atlas, chạy browser, đo GPU/màu/thời gian hoặc tuyên bố nghiệm thu hình. Đây là phần Claude làm sau trong phiếu: chỉnh bộ số trong lab so với ảnh đã duyệt ở cận cảnh và camera chơi; đạt Kiểm 9, ghi mặc định được chọn, chạy lại Kiểm 8 và kiểm thời gian rồi gửi anh tấm so. **Anh cần xem tấm so của Claude; hiện chưa có bộ số ngoại hình mới được duyệt.**
