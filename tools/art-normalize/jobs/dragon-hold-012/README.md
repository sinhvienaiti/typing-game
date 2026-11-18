# Hồ sơ chuẩn hóa Rồng Giữ Ải · Phiếu 012–012d

012–012c là hồ sơ lịch sử, cần giữ để so sánh. 012c chưa qua phản biện lần 3; dùng REVIEW-012d.md và README-normalize của lô mới. Wrapper 012 bị khóa trỏ về rebuild-012d.sh.

```bash
export ART_MAGICK=/opt/homebrew/bin/magick
bash tools/art-normalize/test.sh
bash tools/art-normalize/jobs/dragon-hold-012/verify-code.sh
bash tools/art-normalize/jobs/dragon-hold-012/rebuild-012d.sh build
# Duyệt ảnh dẫn xuất và crop 1:1 trong WORK/dragon-hold-012d/images/.
bash tools/art-normalize/jobs/dragon-hold-012/rebuild-012d.sh publish
bash tools/art-normalize/jobs/dragon-hold-012/report-012d.sh
```

Đây là chuyển lô một lần từ trạng thái 012c đã xác nhận. Sau công bố, không xóa WORK rồi chạy build lại: snapshot mới từ lô 012d bị từ chối. Giữ snapshot/manifest để tiếp tục sau ngắt. Mục có ảnh mà thiếu biên bản cần kiểm vùng dựng trước khi tiếp tục; không tự xóa ảnh đó. build-parallel là bí danh tuần tự; đã bỏ --shard vì CLI trước nhận nhưng không dùng.

build kiểm hash nguồn/lịch sử và công cụ, dựng 8 decal, B1, 40 icon và 32 Tripo; chạy test.sh và verify-code.sh thật, ghi mã thoát/stdout/stderr/hash. Không sửa mã giữa lô. Lô 012d có ngoại lệ đã ghi trong manifest: sau khi dựng, chỉ test/harness, hàm quét `tool_hashes` và verify-code.sh được ghim lại (`validation_revision`, `scan_revision`, `final_test_revision`), không PNG nào đổi. `tool_sha256` của manifest công bố khớp mã Codex 012d trong commit đầu; các sửa sau phản biện lần 4 của Claude làm hash hiện hành khác manifest. Đó là chủ đích: không viết lại manifest, không dựng lại lô. Tripo chọn canvas theo khoảng cách log tỉ lệ vật, không theo độ phân giải; fit chặn scale >1. D1/D3 bật no-key-hue, đếm các thay đổi màu được phép; nguồn thiếu prompt riêng được ghi rõ.

Runner/report giữ cùng flock; biến ART_NORMALIZE_LOCK/ART_NORMALIZE_ART/ART_NORMALIZE_STAGE phục vụ test trong thư mục tạm. Test luôn đặt đủ ba biến và giữ khóa riêng, kể cả khi kiểm lỗi bỏ khóa. Không phụ thuộc runner thật hoặc khóa của tiến trình cha.

publish có hai pha: kiểm toàn bộ hash và tên trước; từ chối cả symlink treo ở đích/bản lưu và đường dẫn thoát ART. Sau đó sao chép dẫn xuất 012c sang .rejected-012c, kiểm hash rồi bỏ tên cũ và công bố file mới. Từng file dùng os.link nguyên tử/không ghi đè; cả lô không phải giao dịch nguyên tử. Có thể tiếp tục dựa vào hash sau ngắt. Giữ nguyên nội dung nguồn, .rejected-012 và .rejected-012b; không chạm art-src/3d hay các file phiếu khác.

report-012d kiểm lại hash trên đĩa, ghi README-normalize và normalize-verification từ số đo, không ghi sẵn kết luận mỹ thuật. Bảng Tripo chỉ rõ file giống byte lịch sử. Mỗi ảnh có sidecar prompt/lệnh/hash. Các crop B1 hàng 0–600 và ảnh ghép được bàn giao cùng art-src; không phụ thuộc ảnh trong WORK sau commit.

verify-code chỉ kiểm cú pháp Python/bash của công cụ/job. inspect-pockets là tiện ích lịch sử cho Tripo, chỉ ghi WORK; không thay duyệt ảnh. probe/audit/normalize/finalize/refine/review_labels/maintain-history cũ bị khóa. Script 012b/012c giữ để kiểm hồi quy và đọc lịch sử, không phải quy trình dựng lô hiện hành.

Ảnh và manifest ở art-src trên Drive; clone chỉ lấy mã không có chúng. Không source common.sh trong shell tương tác. Không chạy Git hay build/test game. Claude đã phản biện lần 4; phần sửa và các mục hoãn nằm cuối REVIEW-012d.md.
