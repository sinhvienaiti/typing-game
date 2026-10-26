# Đối chiếu phản biện Phiếu 012c

Ngày 26/10/2026. Nguồn: `.local/codex-runs/012b-review.json`, toàn bộ `merged.findings`, `merged.review012_status` và bốn bản từng góc; đối chiếu script/ảnh người phản biện; hồ sơ lịch sử này chưa đạt phản biện lần 3, xem REVIEW-012d.md. Đây là phiếu sửa lần 2, cần Claude phản biện lần 3 trước commit. Kết quả ảnh và số đo thực tế được sinh trong `games/dragon-hold/art-src/2d/README-normalize.md` cùng manifest, không ghi sẵn số đạt trong tài liệu mã.

## Bốn lỗi lớn

| Phát hiện | Sửa và bằng chứng có thể chạy lại |
|---|---|
| Despill làm xám/trong màu vật | `key()` chỉ áp matte chênh màu và kẹp kênh trong nền đã chọn nở 3 px. Thêm `protect-interior`, bảo vệ tương tự mặc định auto. Khóa đậm, kể cả vùng tối có chênh >25% nền và >70% kênh lớn nhất, là ứng viên nền nhưng phải qua chế độ kết nối/toàn cục và ngưỡng túi. Ưu tiên lấy alpha/RGB từ mô hình pha với màu vật lân cận, phục hồi màu viền tối trong dải loang. Test tím nhạt (150,130,200) trên xanh lam và xanh rêu (90,140,60) trên xanh lá ở lòng vật: alpha 255 và RGB nguyên giá trị, cả connected/global. Runner dựng lại decal/icon; kiểm RGB/alpha từng pixel nguồn trong vùng bảo vệ, kiểm khóa đậm xa mép, bỏ chốt `key_dominance_gt_25`. |
| Seamless kéo giãn và nhòe | Mặc định W−B/H−B, không resize. `--keep-size` rõ ràng dùng Lanczos + virtual-pixel tile. Chọn đường cắt thẳng sai số thấp, trộn tối đa 8 px quanh đường cắt thay cho trộn cả overlap. Test khổ sau x/xy và khổ keep-size. Runner dựng lại B1 và ảnh ghép; ghi chi tiết toàn ảnh/cửa sổ so nguồn. |
| Chốt mép có điểm mù | Cửa sổ trượt phủ toàn dải overlap; chi tiết tối thiểu theo cửa sổ, thêm chi tiết toàn ảnh so reference. Kiểm độ lệch hàng hai mép so phần trong, dùng reference để không phạt cấu trúc hàng sẵn có. Cặp gương/đối chứng cùng khoảng cách 2k+1. Chặn cạnh <4 px bằng ValueError. Nguồn không liền mép được miễn tỷ số mirror so nguồn khi tỷ số mirror/đối chứng ngoài [0,75;1,5]; README ghi rõ. Runner đo lại cả phông sọc `.rejected-012` và bản mềm 012b, bắt buộc bản sọc trượt. |
| Test nói quá | Fixture bất đối xứng 320×288. Ca mờ một dải kiểm rõ edge/mirror/row đều đạt rồi chỉ detail trượt; ca mất tương phản toàn ảnh đạt nội ảnh nhưng trượt khi CLI thêm reference. Các ca phải trượt: sọc hàng, bù lệch theo hàng, trộn chéo 50%, gập gương rộng ≥256 không reference. Không phụ thuộc việc trục y tình cờ sát ngưỡng. |

## Lỗi nhỏ trong merged.findings

Thứ tự dưới đây tương ứng 19 mục nhỏ sau bốn mục lớn trong JSON, gồm các nhánh chi tiết được nhắc lại ở từng góc.

| Mục | Xử lý |
|---|---|
| 1 · quyền script | `chmod +x` mọi `.sh` của công cụ/job; README ghi chủ dự án dùng `git add --chmod=+x` khi commit. Phiếu không chạy Git. |
| 2 · hash thiếu seamless.sh | Hash mọi `.sh`, và với runner 012c cả mọi `.py`, loại WORK/cache. Bao gồm wrapper, runner, test và mã report. |
| 3 · alpha giả/khóa sai không báo | Alpha có ý nghĩa cần ≥1% pixel alpha <128; bốn góc riêng lẻ không đủ. Cảnh báo mảng góc còn alpha >8 sau key, trừ keep-alpha rõ ràng. Test alpha rời rạc, một góc, bốn góc, sát dưới/đúng 1%, 2% không góc và màu nền sai. |
| 4 · thiếu màu nguồn flat-bg/icon | Thêm `--src-bg auto\|#RRGGBB`, chuyển vào key; thông báo lỗi lấy tên tùy chọn đúng của từng lệnh. Có test cả hai lệnh. |
| 5 · ảnh 1 px IndexError | `seam_metrics` từ chối một trong hai cạnh <4 trước truy cập pixel; test measure các khổ hẹp/cao và thông báo không traceback; thêm measure/seam-check ảnh 4–8 px để không có cửa sổ rỗng. |
| 6 · API thư viện/WORK không qua guard | Decorator dùng chung cho save_rgba/key/fit/pad/seamless/sheet: guard đích, kiểm nguồn, WORK và tmp, vùng dựng riêng, publish nguyên tử. Test ghi đè, `%d`, `[0]` qua mọi hàm và WORK đặc biệt. |
| 7 · công bố không nguyên tử/tín hiệu | Copy cùng thư mục đích → fsync → os.link, cuối cùng xóa partial. SIGTERM/SIGHUP thành SystemExit; test ngắt ngay khi đang copy chỉ để lại file tạm được dọn, không có tên cuối. Test race tới chính os.link bảo vệ nạn nhân. SIGKILL có thể để lại partial/thư mục tạm, không tạo tên cuối 0 byte; README nêu giới hạn này. |
| 8 · runner chạy đôi/công bố từng phần trước kiểm | 012b khóa trạng thái sau publish; 012b/012c/report chung flock. Cả hai publish có pha kiểm toàn bộ trước pha thay đổi. Test bản lưu sai ở cuối danh sách không được làm đổi file đầu; test runner bị khóa. 012c không đọc manifest bàn giao ở main trước resume, nên tiếp tục được sau ngắt khi tên manifest cũ đã chuyển lưu. |
| 9 · ignore thiếu định dạng/chữ hoa | Danh sách cho phép mã/text, mọi media khác bị chặn không phụ thuộc hoa/thường. WORK/cache chặn riêng. Không dùng Git để kiểm trong phiếu. |
| 10 · coder SVG/MSL/MVG | Kiểm chữ ký PNG/JPEG/WebP trước gọi decoder; forced coder ở identify rồi xác nhận định dạng/frame. Test SVG/MSL giả `.png`/MVG bị chặn. |
| 11 · viền ô liu/tối | Mô hình màu vật lân cận trả cả coverage và RGB; ưu tiên trước excess matte. Phục hồi màu ở viền mềm tối chỉ trong dải loang. Runner ghi tỷ số sáng viền/đục lân cận trước/sau từng decal; không dùng đếm toàn bộ sắc xanh/vàng làm chốt vì D2/D4 có lá/rêu thật. Tỷ số 0,85 là dấu hiệu cần xem, không tự xóa màu vật để đạt số. |
| 12 · herb-hut viền hồng | Bỏ ngoại lệ despill off của job mới; dùng protect-interior, vẫn khử loang quanh nền. Dựng đủ hai cỡ và sheet 256/64/32. |
| 13 · Tripo bị báo nhầm túi | Khi đếm lõi sai E6, bỏ điểm kề vùng vật trong 1 px. Giữ số gần nền ≠E6 riêng để tra cứu; không ép viền mềm. Đo lại nhóm bị cờ và ghi nhãn từ kết quả, có inspect-pockets để xem lỗ lớn. |
| 14 · vật rộng bị co nhiều | **Đã chọn theo đề xuất** của chủ dự án: canvas mong muốn theo hộp vật + lề 8%; chọn khổ chuẩn 012 gần nhất theo khoảng cách log hai chiều, giữ tỉ lệ vật khi fit. Ghi khổ trước/sau và hệ số scale thực; chủ dự án có thể đổi sau. |
| 15 · nhánh test chưa phủ | Túi trung tính và xanh lá 63/64, túi xanh khóa bão hòa tối; alpha một pixel/một góc/bốn góc/2% không góc; file `%d`/`[0]` có thật và kiểm nội dung lỗi; lỗi fit thứ hai sau validation; mock bỏ Arial để chạy DejaVu/font đầu/default, kiểm lựa chọn và kích thước sheet. Nhánh font được mô phỏng khi font tương ứng không có trên Mac, render bằng Arial đã cài sau khi kiểm argv. |
| 16 · cwd test không cô lập | Mọi subprocess kiểm CLI/đối thủ có cwd thư mục test trong WORK; không có cây `png:` ở cwd của người gọi nếu guard hồi quy. |
| 17 · reference phạt nguồn không liền mép | Miễn mirror-source có điều kiện; vẫn giữ edge/mirror đối chứng, đo chi tiết nguồn và hàng. Không yêu cầu cùng khổ vì overlap bỏ cột/hàng. README nêu công thức, miễn trừ và tính kinh nghiệm. |
| 18 · số báo cáo ghi cứng | 012c chạy thật test.sh và verify-code.sh; lưu exit/stdout/stderr/hash. Số ảnh, số đạt, hash nguồn/bản lưu/đầu ra, tỷ số chi tiết và nhãn túi lấy từ dữ liệu. Các xác nhận “đã xem nguyên cỡ” không còn được template tự phát ra. Report 012b lịch sử đã khóa, không dùng phát sinh kết luận mới. |
| 19 · README/source/report/helper/help | Bỏ source common.sh khỏi shell tương tác; quy trình job có test, verify, build, inspect, publish, report. Help tùy chọn bằng tiếng Việt. Khóa probe/audit cũ; inspect mới chỉ viết WORK riêng. README mô tả đúng W−B, source-bg, alpha, API thư viện và giới hạn chất lượng. |

## Đối chiếu trạng thái 012 còn dở

Các mục code-1/2/3/5/7/9/12, safety-1/3/10/11 và output-4 từ `merged.review012_status` được xử lý bằng các thay đổi/test ở trên: tên bàn giao và replay giữ nguyên hợp đồng; thêm chốt thiếu, test độc lập, hash đủ wrapper, alpha/túi đúng ngưỡng, giữ màu vật và nhãn Tripo đúng. Không coi báo cáo 012b “đạt” là bằng chứng cho bản mới. Toàn bộ số trước/sau, kết quả từng chốt và ảnh cần duyệt nằm trong manifest/README-normalize được tạo sau lô.

Không sửa hoặc sinh lại ảnh gốc, không đụng Tu Tiên, game code/docs khác, tools/audio-lab, runtime, model hoặc âm thanh. Không chạy Git/build/test game. Duyệt thiết kế nguồn/rig, độ đọc icon và cảm nhận đường cắt B1 thuộc phản biện ảnh lần 3.

## Bằng chứng kiểm sức bắt lỗi của test

Lần 012c chỉ thử 5 mutant tắt toàn bộ một bước và bắt 5/5. Con số này không đại diện sức bắt lỗi: phản biện lần 3 thử 64 mutant chi tiết, 31 bị bắt và 33 còn sống; bộ code thử 7 mutant, 5 còn sống. Các kết luận “đạt” ở trên là kết luận lịch sử đã bị bác. Xem REVIEW-012d.md cho kết quả chạy lại.

## Kiểm crop bàn giao

Lần 012c đã xem D2 trên trắng/nền cỏ, D3 trên trắng/tối và B1 qua mép lặp; crop B1 bỏ sót vùng đường nối hàng 410–480. Không đủ để xác nhận B1 đạt. Herb-hut 256: pixel alpha 9–199 có min(R,B)−G >25 giảm 547 → 0 (64 px: 2 → 0), theo phép đếm trực tiếp ảnh trước/sau. Đây là số đo lịch sử, không phải phê duyệt thiết kế.
