# Báo cáo 080 · MF-C24 · `prepare-ground` và `prepare-decals`

Ngày 28/10/2026. Hoàn thành phần mã và ba kiểm riêng của phiếu trên Mac mini M4; không chạy trên media thật.

## Phạm vi

- Worktree: `games/.wt-dh-codex`, nhánh `dh-codex`, HEAD đầu và cuối `02fe9c787886aecd668248fe00b5f2a97a6e45f4`.
- `git status --short -uall` ban đầu trống. Cuối phiên chỉ có năm đường dẫn được phép bên dưới; không có đường dẫn bị xóa. Repo cha chỉ nhận báo cáo này từ phiên 080.
- Không sửa checkout chính, worktree phiếu 076, golden hay media. Không commit, push, cài gói, chạy server hoặc trình duyệt.

## Đã làm

Các đường dẫn sau tính từ worktree:

| Đường dẫn | Nội dung |
| --- | --- |
| `scripts/assets/prepare-ground.mjs` | Bộ đóng gói dùng chung: duyệt kit và tên ảnh theo thứ tự cố định; PNG/JPEG/WebP → WebP; bỏ prompt, bản thử và JSON nguồn. |
| `scripts/assets/prepare-decals.mjs` | Lệnh và hàm đóng gói decal dùng chung bộ xử lý; giữ bố cục tấm, tỉ lệ và alpha. |
| `package.json` | Chỉ thêm hai lệnh `prepare-ground`, `prepare-decals`. |
| `tests/assets/prepare-ground.test.mjs` | Sáu test Node trên ảnh tổng hợp trong `$TMPDIR/dh-080/`; có hai tiến trình CLI độc lập cho mỗi loại. |
| `src/view/ground-manifest.ts` | Kiểu dữ liệu, kiểm tra JSON và bộ nạp hai manifest qua URL production; chưa nối vào phần vẽ. |

Mặc định đầu vào là `art-src/<ground hoặc decals>/<kit>/<name>.*`, đầu ra là `public/assets/dragon-hold/<ground hoặc decals>/<kit>/<name>.webp`. Thư mục mặc định được tính từ gốc game. Có `--input`, `--out`, `--size`, `--quality`; đường dẫn truyền vào tính từ thư mục gọi lệnh. `ART_MAGICK` chọn ImageMagick 7.

Mỗi loại có một `manifest.json` tại gốc thư mục đầu ra, dạng `{version: 1, kind, textures}`. Khóa ảnh là `<kit>/<name>`; mỗi mục chứa `name`, `kit`, `width`, `height`, `url`, `md5`, `bytes`. URL là `/assets/dragon-hold/<kind>/<kit>/<name>.webp?v=<md5>`. Không ghi thời gian hoặc đường dẫn máy vào manifest.

Cạnh dài tối đa mặc định 1024 px, chất lượng 90, không phóng lớn ảnh nhỏ. Chuyển sRGB, bỏ metadata, alpha WebP chất lượng 100. Test xác nhận ảnh 1536×768 ra 1024×512, ảnh 16×8 giữ nguyên; alpha 0/64/128/255 giữ đúng từng điểm ảnh khi không đổi cỡ. Trùng tên, nguồn thiếu/rỗng hoặc ảnh hỏng báo lỗi; mọi phép chuyển hoàn tất trước khi thay đầu ra, manifest được thay bằng rename.

## Kết quả kiểm

Môi trường: Node `v24.22.0`, pnpm `11.21.0`, ImageMagick `7.1.2-34 Q16-HDRI aarch64`. Các lệnh dưới chạy trong worktree.

| Kiểm | Kết quả |
| --- | --- |
| KR1 / KC1 | Đạt: ` M package.json` và đúng bốn file mới trong danh sách trên; `git diff --check` không có lỗi. |
| KR2 | Đạt: `pnpm test` được chạy trong `pnpm check`, 51 file / 453 test đạt ở lần chạy một worker; 10 test golden đạt. MD5 hai file golden trước/sau giống hệt. |
| KR3 | Đạt: `VITEST_MAX_FORKS=1 VITEST_MIN_FORKS=1 pnpm check` thoát 0; 73 file kit khớp SHA, test đạt, `tsc --noEmit` đạt, Vite build 175 module đạt. |
| KR4 và manifest tất định | Đạt: hai tiến trình Node cho từng loại xuất manifest và toàn bộ WebP giống từng byte, kể cả khi thư mục đầu ra khác nhau; chạy lại cùng thư mục cũng giữ nguyên manifest. Băm ở bảng dưới. |
| Media được Git bỏ qua | Đạt trong cây thư mục tạm dùng nguyên `.gitignore` của worktree và metadata Git chỉ đọc: `git --work-tree=<thư mục tạm> check-ignore --no-index -- <các đường dẫn>` trả đủ bốn đường dẫn bên dưới. |
| Không dùng nguồn ảnh trong runtime | `grep -rn "/art-src/" src/` không in dòng nào, mã thoát 1 theo quy ước của grep. |
| Test ảnh riêng | `ART_MAGICK=/opt/homebrew/bin/magick node --test tests/assets/prepare-ground.test.mjs`: 6/6 đạt, 0 bỏ qua, khoảng 5,83 giây. Có kiểm MD5/byte theo file thực, giải mã WebP, alpha, nguồn không đổi, lỗi không thay đầu ra, bộ đọc HTTP/JSON và ignore. |

Vitest hiện chỉ nhận `tests/**/*.test.ts`, nên sáu test `.mjs` được chạy riêng bằng Node; không sửa cấu hình hoặc lệnh test ngoài phạm vi. Lần chạy `pnpm check` mặc định đầu tiên đạt 452/453 test nhưng test hiệu năng HUD `tests/ui/tags-bodies.test.ts:330` đo 2,1519 ms so với ngưỡng < 1 ms, làm chuỗi kiểm dừng trước build. Chạy riêng file đó đạt 21/21; chạy lại toàn bộ với một worker đạt 453/453, thời gian Vitest 41,00 giây và Vite build 1,54 giây. Không sửa mã HUD, test hay ngưỡng hiệu năng.

MD5 golden trước và sau:

```text
35138e2875761e7c42f8cec0534ca820 tests/golden/golden.test.ts
75f74947dac170d05fd659f99417940e tests/golden/m0.json
```

SHA-256 manifest của hai tiến trình độc lập:

| Loại | SHA-256 (hai lần giống nhau) |
| --- | --- |
| ground | `8b6eefdaeb2441143b0ea70548a59a3d0017e0877384bfb59e13c8dc6c3f3414` |
| decals | `ab9dff823ac2b5290ad1c69c7e8a93e45964019b6f82596b617f0ee3a280aa40` |

Các đường dẫn do `git check-ignore` trả về:

```text
public/assets/dragon-hold/ground/pine-river/moss.webp
public/assets/dragon-hold/ground/manifest.json
public/assets/dragon-hold/decals/pine-river/edge.webp
public/assets/dragon-hold/decals/manifest.json
```

Chạy trực tiếp `git check-ignore` với đường dẫn dưới `public/assets` trong worktree trả lỗi `is beyond a symbolic link`, kể cả khi có `--no-index`. Vì vậy test dùng cây tạm không có symlink, sao chép đúng nội dung `.gitignore`; không tháo hay ghi vào symlink thật.

## Phần để Claude và chủ dự án xem

- Claude chạy hai script trên media thật, kiểm tra hình xuất và tích hợp bộ đọc vào phần vẽ. Ví dụ cú pháp: `ART_MAGICK=/opt/homebrew/bin/magick pnpm prepare-ground --input <thư mục ground nguồn> --out <thư mục ground đích>`; decal thay lệnh thành `prepare-decals`. Phiên này mọi lần đóng gói đều truyền đường dẫn tạm.
- Chưa xác nhận G7 toàn cảnh production: phiếu chỉ cho làm bộ đọc, chưa nối renderer, và cấm xử lý media thật. Không tạo ảnh nghệ thuật, chạy trình duyệt hoặc thay đổi thuật toán sửa mép/màu. JSON nguồn của tấm decal không được công bố qua bộ đóng gói ảnh này.
- Ảnh tổng hợp được test tự xóa; thư mục `$TMPDIR/dh-080` đã được xóa sau kiểm. Chỉ còn mã, báo cáo, `dist/` và cache được phép của lần build.
