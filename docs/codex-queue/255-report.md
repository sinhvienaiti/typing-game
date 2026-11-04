# Phiếu 255 · Tu Tiên · Chuyển camera O và cut-in C3 vào mã lab

> **Claude duyệt (04/11/2026, khoảng 09:45).**
> - Tự chạy lại: tsc sạch; 766/766 test; build không chứa mã lab (grep `LabOrbit|cutinShout|freeOrbit|CUTIN_SHOUT` không ra gì).
> - Một sửa: dời `freeOrbit.apply` về ngay sau `zoom.update`, trước `camBase.copy`, như bản xem. Câu chữ của phiếu ("sau rung và giật") là lỗi của Claude; đặt sau thì `apply` tính lại vị trí và nuốt độ giật. Changelog đã sửa theo.
> - Commit `a900186` trên nhánh `codex/lab-orbit-cutin-port`. Gộp vào `main` và thử trên trình duyệt sau khi hộp xám Song Long (đang sửa `skills-main.ts`) commit xong.

**Trạng thái: đã hoàn tất mã, test và các kiểm tra bắt buộc; chưa commit. Chờ Claude duyệt diff và thử O/C3 trong trình duyệt trước khi gộp.**

Thực hiện ngày 04/11/2026 trên Mac, ghi qua `/Volumes/SS990TPRO/htdocs/typing-game`. Worktree: `games/.wt-immortality-cultivation-codex`, nhánh `codex/lab-orbit-cutin-port`, HEAD giữ nguyên `1a78a82`. Bản vá tham chiếu: `docs/codex-queue/255/owner-preview-port.diff`; ba file nguồn trong `games/immortality-cultivation/tmp/owner-preview/src/lab/` chỉ được đọc.

## 1. File giao

Các đường dẫn dưới đây tính từ gốc worktree, trừ báo cáo:

| File | Thay đổi |
|---|---|
| `src/lab/orbit.ts` | Tạo mới, 94 dòng, chép nguyên từng byte từ bản xem |
| `src/lab/cutin.ts` | Điểm neo/hộp giữ của B, `C_SHOUT_KEEP`, `B_HAND_KEEP`, bảy mặt hô |
| `src/lab/skills-main.ts` | Nối camera O và lựa chọn tranh/mặt hô, mặc định C3 |
| `tests/lab/orbit-cutin.test.ts` | Tạo mới, 173 dòng, 13 test chạy bằng Node |
| `docs/changelog/2026-11-04-lab-orbit-cutin-c3.md` | Tạo mới, 28 dòng, mô tả phím, cờ và cách thử |
| `docs/codex-queue/255-report.md` trong repo cha | Báo cáo này |

Không sửa file nào trong `games/immortality-cultivation/`, không cài gói, không sửa symlink `node_modules`, không sửa `src/kit`, `src/sim`, `src/view` hay các test hiện có. Không dùng lệnh Git ngoài nhóm được phép.

## 2. Đối chiếu đủ 10 khối của bản vá

Số dòng là của kết quả cuối trong worktree, không dùng số dòng cũ để dán bản vá.

| Khối | Vị trí áp | Nội dung |
|---|---|---|
| 1 | `src/lab/cutin.ts:101`, `CUTIN_ART.b` | Chép nguyên điểm neo mắt và hai hộp giữ cho mỗi khung tụ lực/hô B |
| 2 | `src/lab/cutin.ts:127`, bảng mặt hô | Chép nguyên chú thích, `C_SHOUT_KEEP`, `B_HAND_KEEP`, `CUTIN_SHOUT_CANDIDATES` c1–c4 và b1–b3, tên file, kích thước và tọa độ |
| 3 | `src/lab/orbit.ts:1`, lớp `LabOrbit` | Chép nguyên toàn bộ file mới; ba vector được tạo một lần, `apply` không tạo đối tượng mỗi khung |
| 4 | `src/lab/skills-main.ts:42`, vùng import | Thêm `LabOrbit` |
| 5 | `src/lab/skills-main.ts:57`, vùng import | Thêm `CUTIN_SHOUT_CANDIDATES` |
| 6 | `src/lab/skills-main.ts:196`, khởi tạo camera | Tạo `freeOrbit` trên `view.stage.renderer.domElement`, bên cạnh `zoom` |
| 7 | `src/lab/skills-main.ts:673`, cấu hình `ULT_ART` | Đọc `cutinArt`, `cutinShout`, chọn phong cách/khung hô; mặc định C3, giữ ngưỡng thời lượng 0,6 giây |
| 8 | `src/lab/skills-main.ts:1082`, listener `keydown` | O/o gọi `freeOrbit.toggle()`, giữ bộ lọc input/select và các phím hiện tại, gồm A điều khiển hào quang |
| 9 | `src/lab/skills-main.ts:1114`, bảng nút `names` | Thêm nút O và hướng dẫn kéo xoay, giữ các nút hiện tại |
| 10 | `src/lab/skills-main.ts:1269`, hàm `frame(dt)` | Áp xoay sau khi đặt vị trí zoom/rung/giật, trước `screen.applyCamera`; giữ điều kiện bỏ qua camera tùy chỉnh/góc kiểm tra |

Đã so sánh byte của `orbit.ts` với bản xem: **trùng hoàn toàn**. SHA-256: `167fe190183010c010e7364d310d81e8870da7acd96736e581e6f14b9f8c9072`.

## 3. Chỗ điều chỉnh so với bản xem và lý do

- **Vị trí gọi `apply`:** bản diff/bản xem thực tế gọi ngay sau `zoom.update`, trước `camBase.copy`, tức trước phần cộng rung/giật. Phiếu yêu cầu gọi sau chỗ zoom, rung và độ giật đặt camera, nên bản chuyển đặt ngay sau `view.camera.position.set(...)`. Giữ điều kiện `!customCamera && !followShown` của khối gốc. Gọi trước `screen.applyCamera` để phần lắc nghiêng và FOV của hiệu ứng màn hình vẫn được áp sau khi `LabOrbit` căn lại hướng nhìn. Khi O tắt, `apply` trả về ngay, toàn bộ đường camera hiện tại giữ nguyên.
- **`cutinShout` không hợp lệ:** bản xem dùng `undefined`, từ đó trở về khung hô C gốc. Mục 2 của phiếu yêu cầu vẫn dùng mặc định C3, nên bản chuyển dùng khóa dự phòng `"c3"`, vẫn kiểm `Object.hasOwn` để chặn cả khóa kế thừa như `constructor`, `__proto__`. Nếu `cutinArt` hợp lệ chỉ định phong cách khác, vẫn giữ luật của bản xem: phong cách được chỉ định giữ khung hô riêng và ghi cảnh báo.
- **Chữ ký `frame(...)` của cut-in:** mã hiện tại đã nhận `keep?: readonly Box[]` giống bản xem, nên không cần sửa chữ ký. Các lời gọi năm tham số hiện có vẫn tương thích. Hai khung A và khung tụ lực C không đổi; khung hô C gốc được giữ để dùng khi chọn mặt hô hợp lệ nhưng khác phong cách C.
- Các vị trí tương ứng đều còn trong mã mới. Không thay toàn bộ `skills-main.ts` bằng bản cũ; giữ các thay đổi hào quang vòng 1, các hook và góc kiểm tra hiện có.

## 4. Kết quả kiểm tra bắt buộc

Các lệnh TypeScript, Vitest và Vite chạy trong `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-immortality-cultivation-codex`.

**Lưu ý về lệnh thực chạy:** thêm `--configLoader runner` cho Vitest/Vite để không tạo file bundle cấu hình trong `node_modules/.vite-temp` thông qua symlink sang game đang có agent khác làm. Vitest thêm `--no-cache` để không ghi bộ nhớ đệm kết quả vào game, giới hạn bốn worker. Vite nhận `IC_VITE_CACHE_DIR` bên trong thư mục build tạm. Các lựa chọn này chỉ điều khiển cách chạy kiểm tra, không sửa cấu hình hay phạm vi test/build.

| Kiểm | Lệnh thực chạy | Kết quả |
|---|---|---|
| 1 | `node node_modules/typescript/bin/tsc --noEmit -p .` | **Đạt**, exit 0, không lỗi |
| 2, trước sửa | `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4` | **753/753 test**, **82/82 file**, 6,12 giây, exit 0; xác nhận đúng mốc `1a78a82` |
| 2, sau sửa | Cùng lệnh Vitest trên | **766/766 test**, **83/83 file**, 6,09 giây, exit 0; thêm đúng **13 test** |
| 3, build | `IC_VITE_CACHE_DIR=/private/tmp/codex-255-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-255-dist --configLoader runner` | **Đạt**, exit 0, 181 module, build 865 ms |
| 3, kiểm lab | `grep -rl "LabOrbit\|cutinShout" /private/tmp/codex-255-dist` | **Không in đường dẫn nào**, exit 1 đúng nghĩa không tìm thấy; lab không lọt vào build |
| 4 | `git -C games/.wt-immortality-cultivation-codex diff --stat` từ gốc repo cha | Chỉ hai file đã theo dõi được phép sửa; chi tiết dưới đây |

Vite chỉ cảnh báo thư mục output nằm ngoài gốc dự án và sẽ không tự làm trống. Thư mục `/private/tmp/codex-255-dist` chưa tồn tại trước lần build này; đã xóa toàn bộ bằng `shutil.rmtree` sau khi grep và xác nhận không còn tồn tại.

Kết quả `diff --stat`:

```text
 src/lab/cutin.ts       | 33 +++++++++++++++++++++++++++++++--
 src/lab/skills-main.ts | 18 ++++++++++++++++--
 2 files changed, 47 insertions(+), 4 deletions(-)
```

`git diff --stat` không liệt kê file mới chưa được thêm vào index. Đã kiểm thêm `git status --short`: ba file mới là `src/lab/orbit.ts`, `tests/lab/orbit-cutin.test.ts`, changelog nêu trên; đều trong phạm vi cho phép. `?? node_modules` đã có từ lúc bắt đầu, là symlink sẵn của worktree, không phải file do phiếu tạo. `git diff --check` qua, không có lỗi khoảng trắng. Báo cáo nằm ở repo cha nên không xuất hiện trong diff của worktree.

### Test mới và kiểm hồi quy

- 10 test camera: tắt không đổi vị trí/hướng/up/matrix/FOV; bật với yaw 0 và góc cao chưa đặt không đổi camera ở cả `dt=0` và `1/60`; kéo ngang 100 px quay đúng 35° quanh điểm nhìn trên mặt đất, giữ khoảng cách; quay trọn vòng; kẹp góc cao 4° và 89°; kết thúc kéo bằng pointerup/pointercancel; tắt/bật lại trả quyền cho camera thường. Sai số vị trí, góc cao và khoảng cách kiểm ở mức tối đa `1e-6`.
- 3 test cut-in: đủ bảy ID và đúng phong cách; C3 trỏ đúng file `tt-cutin-c-shout-e3-head-skin-up2x.v2-try1.png`; dữ liệu hai khung A giữ nguyên.
- Chạy thêm đoạn chọn tranh thực tế của `skills-main.ts` trong bộ nhớ bằng TypeScript, không dựng DOM: **31 trường hợp URL qua**, gồm mọi ứng viên, mặc định, tham số sai/rỗng/khóa kế thừa, phong cách không khớp và `cutin=0.05`. Không tạo file ngoài danh sách được ghi.
- Không sửa test hoặc dữ liệu golden hiện có. Các kiểm hash/replay hiện có đều qua; các dòng `HASHLINE` của `tests/sim/combat-real-lanes.test.ts` trùng trước/sau. Các mốc chốt:

| Kịch bản | Tick | Hash world/local trước và sau |
|---|---:|---|
| balanced, key/9 | 33403 | `800aabf4:2926feb9` |
| relax, key/9 | 43200 | `e4a969f1:7d6bbcfb` |
| Chuẩn, key/21 | 35672 | `f9f06fd6:18e4b7b6` |

## 5. Phần chưa chạy và việc Claude cần xem

Không mở dev server, không chạy trình duyệt hay chụp hình theo giới hạn phiếu. Không tải gói/ảnh hoặc sao chép media; worktree hiện không có `art-src`. Không có phần mã hoặc kiểm tra bắt buộc nào còn thiếu.

Claude cần đọc kỹ hai điều chỉnh ở mục 3, chạy lại các lệnh kiểm, rồi thử O, xoay 360°, giới hạn góc cao, zoom/rung/giật và trả về camera thường; thử C3 mặc định, tham số sai, A/B và ứng viên khác trên host có đủ media. Các URL thử cụ thể đã ghi trong changelog. Sau bước duyệt đó Claude mới commit và gộp vào `main`.
