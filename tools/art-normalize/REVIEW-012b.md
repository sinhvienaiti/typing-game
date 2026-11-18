# Đối chiếu phản biện Phiếu 012b

> **Hồ sơ lịch sử đã bị phản biện lần 2.** Các kết luận đạt về despill, độ chi tiết mép, test và chín ảnh Tripo bên dưới không còn là kết luận hiện hành. Xem [REVIEW-012c.md](REVIEW-012c.md) và README-normalize mới. Không dùng tài liệu này để mô tả mã 012c.

Ngày 25/10/2026. Đọc đủ 33 phát hiện trong `.local/codex-runs/012-review.json` (13 mã, 12 an toàn, 8 chất lượng ảnh). Số thứ tự dưới đây theo từng mảng của JSON. Báo cáo ảnh thực tế ở `games/dragon-hold/art-src/2d/README-normalize.md` trên Drive.

## Mã (`code`)

| Mục | Xử lý và bằng chứng |
|---|---|
| 1 · seamless gập gương | Chồng dải cuối–đầu cùng chiều, smoothstep, bỏ overlap, trả lại khổ nguồn; xử lý x/xy. Đo mép/trung vị, mirror đối chứng và nguồn; chốt chi tiết dải ≥90% phần trong; test ảnh bất đối xứng và ảnh gương đối chứng. Không còn chốt MAE bằng 0. |
| 2 · tên bàn giao sai/manifest không tái tạo | Runner 012b lưu bản cũ `.rejected-012`, xuất tên chuẩn; ghi argv thực tế, replay và hash công cụ. Manifest 012 cũ lưu riêng với chú thích thuật toán đã loại. |
| 3 · alpha 254 bỏ qua khóa nền | Chỉ giữ tự động khi bốn góc 0 hoặc ≥1% pixel alpha <128; có thông báo và `--keep-alpha`. Test cả hai nhánh. |
| 4 · mất nét 1–2 px, spill pixel đục | Không ăn mòn mặc định; alpha mềm, tách màu nền và matte chênh màu bão hòa; `--shrink` tùy chọn. Test nét 1/2 px và pixel trộn nền; kiểm màu sau resize. |
| 5 · túi nền kín/chi tiết nhạt | `connected` thêm thành phần kín đủ lớn và trung tính; có `global` rõ ràng. Test lỗ kín và chi tiết kem. Lô đếm màu dư ở từng ảnh. Mép vật cùng màu nền vẫn cần chỉnh tham số/alpha thủ công; không khẳng định phân biệt được từ RGB. |
| 6 · page offset, cắt atlas, đốm alpha | `+repage` ngay sau đọc trong fit/crop 2×2; từ chối vật trên đường chia; bbox alpha >8. Test ba trường hợp. Không xóa thành phần nhỏ vì có thể là nét thật. |
| 7 · icon lỗi để lại một phần bộ cỡ | Kiểm toàn bộ khổ trước, dựng đủ cỡ tạm rồi công bố. Test `256,4` không tạo thư mục đầu ra. Công bố nhiều file không phải giao dịch nguyên tử khi ngắt/xung đột; README nêu đúng giới hạn. |
| 8 · lỗi đầu vào và đầu ra rỗng | Kiểm file/frame trước thư mục đích; lỗi rõ ràng; kiểm mask rỗng sau co; tài liệu và test tên bắt đầu `-` với `--`. |
| 9 · nhãn ImageMagick/font cứng | Từ chối tên chứa `%`/`[` theo chốt an toàn; escape bổ sung và thêm tiền tố nhãn chống `@file`. Trên Mac dùng Arial theo đường dẫn hệ thống; chọn font đã cài trên máy khác. Test bỏ DejaVu-Sans và danh sách font rỗng trên macOS. |
| 10 · file tạm chưa ignore/clone mới | `.gitignore` cục bộ chặn `.tmp/`, cache, ảnh. Tạo `.tmp` trước dùng; script cũ đã khóa điểm vào. Giữ file tạm trong đường dẫn được phiếu cho phép. |
| 11 · giả định bit/profile/mode/góc/erosion | README nêu sRGB 8-bit, ICC và trường hợp seam-check có thể giữ 16-bit; trung vị mảng góc; chế độ kết nối/toàn cục chọn rõ; erosion dùng virtual-pixel edge. Không tuyên bố giữ độ sâu hay chuyển profile bất kỳ. |
| 12 · test yếu/assert bị tắt | Test hồi quy các đầu vào phản biện, kiểm ghi đồng thời và O_EXCL. Chốt dùng ngoại lệ rõ ràng; `assert` lịch sử đã đổi thành điều kiện/ngoại lệ, điểm vào khóa. |
| 13 · script riêng/trộn prompt | Di chuyển vào `jobs/dragon-hold-012/`; bỏ fallback prompt v1 sai nguồn; sidecar 012b có đầu đề dẫn xuất/nguồn/lệnh/hash, prompt nguồn ở phần riêng. |

## An toàn (`safety`)

| Mục | Xử lý và bằng chứng |
|---|---|
| 1 · **chặn: cú pháp tên file và race** | Chặn `%`, `[`, coder prefix trên mọi đầu vào/đầu ra/thư mục icon. ImageMagick chỉ ghi tạm; `open(dst, 'xb')` ở công bố. Test mọi lệnh với `%d`, `[0]`, `png:`, `PNG32:`, hash nguồn, symlink, đích xuất hiện sau guard và hai tiến trình cùng tên. |
| 2 · ảnh tạm có thể vào Git | `.gitignore` cục bộ cho ảnh/cache/tmp; không dùng Git trong phiếu. |
| 3 · bản lỗi ở tên chuẩn/hash công cụ | Runner chỉ lưu các file dẫn xuất trong snapshot 012, kiểm hash rồi công bố tên chuẩn; kiểm nguyên trạng 164 file gốc. Chốt hash công cụ từ đầu lô. |
| 4 · D3 vẫn xanh | Matte và despill trên cả pixel đục, Triangle khi resize để tránh tái tạo màu khóa; chốt 0 pixel chênh màu khóa >25 trên cả 8 atlas ở đầu ra cuối. |
| 5 · `$WORK` không thay thế | Replay dựng token `$WORK/...` trước quote; argv thực tế được lưu riêng. Không dùng thay thế một đường dẫn tuyệt đối trong chuỗi đã tương đối hóa. Hồ sơ cũ cũng sửa phép thay bằng đường dẫn tương đối. |
| 6 · lô chạy một lần nằm trong công cụ chung | Đã chuyển đúng `jobs/dragon-hold-012/`; README gốc chỉ trỏ hồ sơ. Runner mới tiếp tục theo biên bản, không quét glob ảnh dẫn xuất làm nguồn. |
| 7 · assert/ghi sidecar không độc quyền | Không còn `assert` làm chốt; sidecar dùng `open(..., 'x')` trong vùng dựng, công bố bằng `xb`. Lô cũ khóa chạy; ảnh và sidecar dựng xong mới công bố. |
| 8 · mkdir trước kiểm đầu vào | Thư mục đích chỉ tạo ở publish sau khi xử lý hoàn tất; test nguồn thiếu không tạo thư mục. |
| 9 · sidecar không thống nhất | Mọi ảnh mới có định dạng sidecar thống nhất; prompt nguồn nguyên văn ở phần riêng. Sidecar cũ giữ cạnh bản `.rejected-012` để bảo tồn bằng chứng. |
| 10 · README lệch mã/Drive | README viết lại theo mã; nêu art-src trên Drive không có trong clone chỉ lấy mã. Không hướng dẫn chạy lại lô 012 đã khóa. |
| 11 · mode executable | **Để chủ dự án xử lý khi staging.** Phiếu cấm chạy Git nên không thay index mode. Tài liệu dùng `bash script.sh`; cần đặt executable cho `.sh` khi commit nếu muốn gọi trực tiếp trên macOS. |
| 12 · định dạng/import | Mã dùng chung và runner mới viết rõ khoảng trắng, import cấp mô-đun; hồ sơ cũ đã định dạng lại bằng AST khi thay chốt, thay import động trong mã thực thi và sửa f-string để đọc được bằng Python 3.9 trên Mac. Không cài formatter ngoài. |

## Chất lượng ảnh (`output`)

| Mục | Xử lý và bằng chứng |
|---|---|
| 1 · đốm xanh/xanh lam trong decal | Matte chênh màu và unmix, chốt residue ở file sau pad. Tạo sheet trắng/caro/tối 1:1, không dựa vào bản thu 512. |
| 2 · dải cây gương/phông nhòe | Thuật toán overlap không gương; kiểm mirror và tỷ lệ chi tiết, xem crop ghép nguyên cỡ. Không coi chỉ số thay duyệt bố cục mỹ thuật. |
| 3 · tên chuẩn chứa bản bị loại | `.alpha.png`, `pine-river-far.seamless.png`, `_review/pine-river-far.seam.png` dành cho lô sửa; tất cả bản dẫn xuất 012 cũ lưu `.rejected-012`. |
| 4 · nền xám trong lỗ kín Tripo | Tách túi trung tính đủ lớn; kiểm từng file bằng số pixel gần nền chưa đúng E6 và thành phần kín ≥64. Báo cáo liệt kê rõ mọi file chưa qua chốt, không chỉ đo bốn góc. |
| 5 · prompt nguồn bị hiểu là prompt ảnh dẫn xuất | Sidecar ghi rõ nguồn/lệnh/hash và phần prompt nguồn riêng. |
| 6 · thiếu decal trắng/caro 1:1, nhãn 32 sai | Sheet decal tile 1024 trên trắng/caro/tối cho cả bản hiện tại/v1. Nhãn icon ghi cả tên nguồn lẫn cỡ hiển thị, ví dụ `.64 · 32 px`. |
| 7 · alpha 255 thừa trên phông RGB | `save_rgba` xuất PNG24 nếu alpha toàn 255; phông và ảnh ghép giữ đục. |
| 8 · danh sách icon cần duyệt thiếu | Báo cáo bổ sung I14, I17, I18/I19 cùng I03/I12 ở 32 px; giữ nhận xét nguồn moss-warden đã sát/cụt khung. Không sửa thiết kế nguồn trong phiếu hậu kỳ. |

## Giới hạn phạm vi

Không chạy Git, không đổi ảnh gốc, không sinh hình mới bằng AI, không đổi dáng/rig, âm thanh, model, runtime hoặc ô đất ngoài danh sách 012. Các thay đổi bitmap ở đây là đầu ra xác định của công cụ chuẩn hóa mà phiếu yêu cầu sửa và chạy lại. Việc duyệt thiết kế nguồn và quyền executable trong index thuộc bước chủ dự án/Claude phản biện trước commit.

## Kết quả dựng lại trên Mac mini M4

`test.sh` và kiểm cú pháp Python 3.9/bash đã đạt. Lô 012b dựng lại đủ 81 ảnh cùng các sheet, dùng Arial hệ thống; 8/8 decal có 0 pixel trội màu khóa >25. Phông qua chốt mép, mirror và chi tiết. Lưu 250 file dẫn xuất cũ bằng hậu tố `.rejected-012`; giữ nguyên hash của 164 file gốc.

**Giới hạn còn ghi nhận ở lỗi lớn code-5/output-4:** 23/32 ảnh Tripo qua chốt túi nền tự động; 9 ảnh còn bị gắn cờ quanh viền lỗ nhỏ: blight-wolf-front, thorn-ant, thorn-wasp-side, tusk-boar-front, moss-banner, moss-banner-back, bridge-old, pine-round, tree-violet. Crop nguyên cỡ cho thấy lõi lỗ đã đúng E6, phần gần nền còn khác E6 chủ yếu ở mép khử răng cưa. Giữ trạng thái chưa đạt chốt và số đo từng file trong README-normalize, không ép màu toàn bộ vì sẽ có nguy cơ xóa mép vật nhạt. Claude cần duyệt các vùng này trước khi công nhận chất lượng ảnh; đây là giới hạn khóa màu tự động còn chưa giải quyết hoàn toàn.

Không thay quyền executable trong Git index vì phiếu cấm Git. Tất cả lệnh kiểm tra/chạy lô dùng `bash`; chủ dự án xử lý index khi staging.
