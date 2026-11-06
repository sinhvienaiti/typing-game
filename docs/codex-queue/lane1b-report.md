# Phiếu 296 · Song Long từ sim thật

## Việc 1 · Presenter — đạt kiểm tra mã

Đã thêm `games/.wt-ic-swarm-sim/src/view/skills/qi-dragon-swarm.ts` và nối ba sự kiện `swarm-*` trong `src/view/fx.ts`. Giải mã/checksum gói, nội suy tick, bám mẫu xoắn 250 mm, rút thân đúng sim, pool hai lần tung theo seat/castId; nổ theo sự kiện và dọn theo tick hết. `createFx` được gọi trong `newMatch`, khởi động tải/làm ấm hai bầy; giảm chuyển động bỏ hạt, dải phụ, chớp và rút ngắn dư âm. Dùng lại shader, vật liệu và cách đặt xương của lab đã duyệt; không tự vạch hay làm trơn đường. Test Node mới đối chiếu mọi tick với `swarmBodyAt`, kiểm giải mã, nội suy, pool và tạm dừng. `tsc` sạch; vitest **92 file / 1.056 test qua**; test băm ghim Twin Pearl qua, không sửa sim hay băm.

Lưu ý nhịp: mã sim phiếu 293 vòng 3 dùng tốc độ 16 m/s, tick lao/nổ/hết tính riêng từng gói; presenter theo gói, không dùng các mốc cố định cũ trong §10.3. Media phiếu 292 đã chép bằng `cp -n` vào `public/assets/immortality-cultivation/{models,vfx}` của worktree đích. Các tranh phụ của lab vẫn dùng URL `/art-src/lab/...`; worktree này chưa có thư mục media `art-src`, nên Claude cần phục vụ bộ media lab đã duyệt khi quay (ngoài phạm vi chép media của phiếu). Chưa có kiểm chứng GPU hoặc chấm hình.

## Việc 2 · Tầng chất lượng — đạt kiểm tra mã

High/Ultra dựng 5 lượt màu + 3 lượt depth; Medium 5 lượt màu, không depth; Low không tải model/manifest model, dựng 5 dải texture trên đường sim, ngọc và vòng nổ phủ sân, không bloom. High/Medium giữ URL có phiên bản từ manifest phiếu 292; mỗi GLB thực tế có một mesh/một primitive, 40 xương. Test Node đếm trực tiếp đối tượng/lượt skinned của cả hai bầy, kiểm chọn tầng, vị trí mọi khớp, ngọc chỉ nổ sau sự kiện, giảm chuyển động và dọn pool. `tsc` sạch; vitest **92 file / 1.063 test qua**; băm ghim giữ nguyên. Ngân sách lượt vẽ đã kiểm cấu trúc; thời gian GPU và độ đẹp chờ video của Claude.

## Việc 3 · Lab từ sim thật — đạt kiểm tra mã

Thêm `src/lab/qi-dragon-swarm.ts`, nối `skills-lab.html` / `src/lab/skills-main.ts`; bổ sung hai móc nhỏ trong `src/lab/herd.ts` để hiển thị đúng máu còn lại từ sim và giữ quái chết tới Reset. Adapter tạo world với header `swordKey2: "swarm"`, dùng nguyên `emitCast`, `stepCasts`, `stepSkills`; bầy quái lab cung cấp vị trí mỗi tick. Gói đường, chạm, quỹ sát thương, nổ và hết đều do mô-đun sim thật phát; số nổi lấy `hit.amount`, không dùng sát thương giả của lab. Sức chứa world riêng của lab đủ bầy đang có; không sửa nội dung hay công thức sát thương. Chỉ nhánh `key2=swarm` dùng adapter; lab mặc định và cách chọn `q` cũ giữ nguyên. Test mới kiểm gói đúng byte, ba kênh sát thương, nhịp nổ/hết, quái di chuyển, hai lần tung chồng, tạm dừng, Reset và bầy trống. Kiểm cuối: `tsc` sạch; vitest **93 file / 1.069 test qua**; `git diff --check` sạch; `src/sim`, `src/content` và `tests/sim/twin-pearl.test.ts` không có diff.

Claude phục vụ **worktree này**, rồi mở `/skills-lab.html?key2=swarm&tier=high` (đổi `medium` / `low` để so tầng). Phím **2** tung ngay, tung hai lần để xem chồng; **R** khôi phục bầy. Thêm `&motion=reduce` để xem giảm chuyển động; `&fixed=1&ui=0&probe=0&dpr=1` dùng bộ quay hiện có. Chờ `window.__lab.ready`; `__lab.qiSwarm.cast()`, `.reports()`, `.active()`, `.tick()` và `.pause(true/false)` phục vụ quay/đọc số. Không tham số vẫn là lab cũ.

## Bàn giao

Mã/test đổi đúng worktree `codex/key2-swarm-sim`: presenter và fx; adapter lab, herd, skills-main, HTML; hai test mới `tests/{view,lab}/qi-dragon-swarm.test.ts`. Media chép tại `public/assets/immortality-cultivation/{models,vfx}`, cả năm tệp giống byte bản gốc. Báo cáo duy nhất là tệp này. Không tạo ảnh/âm thanh mới, không sửa sim/số sát thương/băm, không lệnh Git ghi, không build, không mở cổng hoặc trình duyệt. **Chưa quay/chấm hình và đo GPU** theo ranh giới phiếu; Claude cần nối media `/art-src/lab` đã duyệt, kiểm hình từng tầng, chuyển động, hai bầy chồng và quay video cho anh. Đây là kết quả kiểm mã, chưa phải nghiệm thu hình 8,5.
