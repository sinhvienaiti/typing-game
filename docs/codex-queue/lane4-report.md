# Báo cáo làn Codex 4

Đã cắt **74 clip**, xem **74 sheet bằng `view_image`**; giữ **70 atlas trong manifest, 257,2 MiB**. Bỏ khỏi đầu ra 4 clip: 2 lỗi và 2 không có mục cũ để thay. Không thiếu video; bỏ mọi file `wrong-dup`, không xử lý hai clip thử Content Credentials.

Đầu ra: `games/immortality-cultivation/art-src/lab/vfx/` theo các thư mục dưới; mỗi atlas kèm JSON, mục manifest có `role`, `job`, `take`, `source`, MD5 nguồn. Thêm 74 cấu hình vào `tools/vfx-flipbook/immortality-cultivation.json`, giữ nguyên cấu hình cũ. Sheet Arial, atlas chẩn đoán, log và trạng thái: `.local/vfxlab-lane4/`.

**1. Thú chết — `beast/`:** 6/6 atlas; **7 → 13 mục**. Xem đủ sheet, hình chính đủ khung, không trống. Crow dùng bản hợp lệ, bỏ `wrong-dup`. Kiểm manifest: 0 problems.

**2. Boss — `boss/`:** 6/6 atlas; **9 → 15 mục**. Hai bản nổ r2 đủ khung; khói trắng dùng `smoke`/`normal`. Hai vòng lặp liền. Kiểm manifest: 0 problems.

**3. Đòn quái — `foe/`:** giữ 1/2 atlas; **14 → 15 mục**. Loại `foe-rock-impact-shatter-r2`: khối đá/vành đá vẫn cụt mép dưới và hai bên nguồn. Lõi đạn lặp liền, vai `projectile`. Kiểm manifest: 0 problems.

**4. Thế giới — `world/`:** 10/10 atlas; **4 → 14 mục**. Tám vòng lặp liền; texture phủ tới biên theo nội dung. Phantom dùng `smoke`/`normal`, nguồn chứa hai cột khói. Kiểm manifest: 0 problems.

**5. Thưởng/UI/anh hùng — `meta/`:** giữ 17/18 atlas; **7 → 24 mục**. Loại `results-victory-rays-loop`: điểm nối 1,054 vượt ngưỡng 1,0. Mười một vòng lặp còn lại đạt; khói tâm ma dùng `smoke`/`normal`. Kiểm manifest: 0 problems.

**6. Cut-in — `cutin-mat/`:** 8/8 atlas; **0 → 8 mục**. Đã xem đủ sheet, texture phủ biên, bốn vòng lặp liền; hai lớp ink dùng `smoke`/`normal`. Kiểm manifest: 0 problems.

**7. Hiện hình r2 — `expansion-phases/`:** đã cắt/xem hai clip trong `.local`, **không đăng ký atlas; 22 → 22 mục**. Hai mục cùng vai đã bị làn 2 gỡ, nên không có đích thay; không tự thêm vì phiếu cấm tăng số mục. Ấn đúng hình và đủ khung; gương r2 còn vành dưới sát/cụt biên lúc nở. Kiểm manifest: 0 problems.

**8. Tụ lực — `charge-fill/`:** 14/14 atlas, đủ cả Wood; **0 → 14 mục**. Vai `charge`, trường `element` đúng từng hệ; xem đủ sheet, hình chính đủ khung. Kiểm manifest: 0 problems.

**9. Cơ chế — `mech/`:** 4/4 atlas; **0 → 4 mục**. Lưới trói đủ hình; sét/dải nối tới biên, cột sáng đi vào từ trên. Hai vòng lặp liền. Kiểm manifest: 0 problems.

**10. Rồng/hoa sen — `spirit/`:** 4/4 atlas; **0 → 4 mục**. Dùng `take2-inplace` cho side, `take1-inplace` cho unified, `take3` cho body-ribbon và lotus. Đầu rồng/hoa sen đủ khung; đuôi dải tới biên trái. Kiểm manifest: 0 problems.

**11. Kiểm 7 job trùng:** không cần cắt lại. `void-wave` đã mới hơn nguồn; crow và wave-clear vừa cắt ở việc 1/5, mới hơn và khớp MD5 nguồn. Không tìm thấy mục có `job` bằng `dark-big-burst`, `style-w3-fire-ribbon` và hai job hiện hình gốc; không đụng các bản `-v2`, `-w2` hay vai `treasure` khác. Số mục không tăng. Chi tiết: `.local/vfxlab-lane4/group11.json`.

**Kiểm cuối:** 70 PNG/JSON khớp kích thước, MD5, dung lượng, take và nguồn; mọi cạnh ≤4096 px. 28 vòng lặp giữ lại đều đạt, điểm nối cao nhất 0,977. Bộ kiểm các thư mục làn này: **133 mục, 0 problems**; toàn cục **417 → 487 mục**, vẫn 1 lỗi có sẵn tại `sigils/manifest.json` ngoài phạm vi. Bằng chứng: `.local/vfxlab-lane4/audit.json` và `validate-11-after*.txt`. Không còn khung thô trên đĩa.

**Anh cần xem:** việc 7 không thể thay mục đã bị gỡ; một số nguồn hero/realm/van-khi/world và cut-in có hình xoắn đỏ cam tương tự nhau, nhất là `cutin-gold-rays` không ra tia vàng. MD5 của 74 nguồn đều khác nhau. Đây là cảnh báo nội dung nguồn, chưa phải duyệt mỹ thuật/tích hợp lab. Không sửa video gốc, mã game/lab hay âm thanh; không build/test game, mở cổng/trình duyệt hoặc Git ghi. README công cụ không tồn tại; dùng quy trình làn 2 và mã công cụ; chạy bộ kiểm bằng `node --import tsx/dist/loader.mjs`.
