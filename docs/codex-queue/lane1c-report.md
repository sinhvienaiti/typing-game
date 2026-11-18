# Làn 1c · Gộp Song Long vào lab chung

Đã giải 5 khối xung đột trong đúng hai tệp của `games/.wt-ic-lab-all` (nhánh `codex/lab-all`):

- `src/lab/skills-main.ts`: giữ import SkillBar, cấu hình `cut`/`dark`, thêm presenter/adapter swarm và `skillsLabQuality` cho `tier`; ưu tiên phím 2 swarm trước mẫu Fire, giữ nguyên M và các nhánh còn lại. Giữ cả `lastWorldDt`, dừng theo swarm, cập nhật sim, vẽ swarm và `placeTags` trước render; giữ Reset, tải/làm ấm và API `__lab.qiSwarm`.
- Giữ panel 240 px, `SHORT`, `content`, `togglePanel`/H, thanh chiêu/I, `refreshClipSlots`, A/B/KTX2, âm và phím 8, 9, M, K, C. Khi bật swarm, nút 2 ghi **Twin Dragons (swarm)**; tooltip đầy đủ **Twin Dragons, One Burning Pearl · real swarm sim (<tầng>)**. Thanh chiêu dùng biểu tượng Twin Dragons và cùng tooltip.
- `src/lab/herd.ts`: giữ `slow` và `hit(..., rimS?)` của lab chung; giữ `hitFromSim` để phản ánh máu sim, `autoRespawn` để quái chết nằm ngoài sân tới Reset.
- Sửa thêm ngay trong `skills-main.ts`: panel cũ gọi `localStorage` trực tiếp khiến boundary test lỗi. Chuyển sang `gameStorage` có sẵn; giữ khóa `lab.panel.collapsed` và dữ liệu `1`/`0` tương thích bản cũ. Không sửa storage hay test.

## Kiểm tra

- `git diff --check`: sạch; quét đệ quy `src` không còn `<<<<<<<` hoặc `>>>>>>>`.
- `npx tsc --noEmit`: PASS sau sửa cuối.
- Toàn suite: **113 file / 1.270 test PASS**, 55,49 giây. Lệnh: `VITEST_MAX_THREADS=4 bash ../../.local/bin/heavy.sh --cores=4 npx vitest run --maxWorkers=4 --no-cache --configLoader=runner`; tắt cache và dùng runner để tránh ghi vào `node_modules` dùng chung. Lượt đầu có đúng một lỗi storage nêu trên; lượt cuối không lỗi.
- Đối chiếu HEAD: sáu tệp triển khai thanh chiêu, A/B và ấn vẽ tay (`skill-bar`, `hybrid-ab`, `painted-sigils`, `fxkit`, `sword-rain`, `sword-skills`) giữ nguyên. Test Node còn cảnh báo fixture Fire chưa tải và URL tương đối manifest ấn; các test đều qua.

## URL sau gộp

Đều dùng trang `/skills-lab.html` trong **worktree này**:

| Mục | Tham số |
| --- | --- |
| Song Long | `?key2=swarm&tier=high`; đổi `tier=medium`/`low`. `q=low|medium|high|ultra` vẫn dùng khi không có tier swarm hợp lệ. `key2=twin-pearl` giữ lab khối mô phỏng cũ. |
| Panel/thanh chiêu | Mặc định hiện cả hai; H thu gọn/mở panel, I đổi kiểu. `ui=0` ẩn cả hai; `bar=0` chỉ ẩn thanh; `icons=jewel` chọn jewel-crest. Cảnh `ab` giữ hành vi ẩn panel/thanh. |
| Demo A/B | `?ab=meteor&element=fire` hoặc `?ab=azure-cloud-dragon`; `only=left|right`, `left=crf23|720p`, `ktx2=uastc|etc1s|0`, `mv=0`, `prewarm=0`, `autostart=0`. Ngoài A/B: `cometFlip=1` hoặc `video=0` dùng atlas. |
| Ấn và mẫu chiêu | Mặc định ấn vẽ tay; `sigil=code` để so. Giữ `element`, `weapon`, `typed=1`, `wpm`, `five=0`, `herd=march`, `cut=sabre`, `dark=b`. |
| Quay/kiểm chuyển động | `fixed=1&ui=0&probe=0&dpr=1`; thêm `motion=reduce`. Giữ các núm camera/hình, aura, tag và âm hiện có. |

Không sửa tệp nào khác ngoài hai nguồn trên và báo cáo này; không chạy build, mở trình duyệt hay tạo media. Chưa nghiệm thu hình/âm: Claude cần xem panel/H, thanh chiêu/I, phím 2 trong cả Metal và Fire, Reset và hai cảnh A/B. Không dùng lệnh Git ghi; HEAD `60e4657`, MERGE_HEAD `261bf79` giữ nguyên, index vẫn `UU` ở hai tệp để Claude tự `git add` và commit.
