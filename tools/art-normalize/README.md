# Công cụ hậu kỳ ảnh dùng chung · `art-normalize`

Phiếu 012d, ngày 26/10/2026. Python 3 chuẩn và ImageMagick 7; chạy trực tiếp trên macOS/Linux. Hậu kỳ xác định từ nguồn, không gọi dịch vụ sinh ảnh, không sửa runtime.

## 1. Chạy từ gốc repo

```bash
export ART_MAGICK=/opt/homebrew/bin/magick
bash tools/art-normalize/key-alpha.sh input.png output.alpha.png --mode global --despill protect-interior
bash tools/art-normalize/pad-margin.sh output.alpha.png output.padded.png --size 1024 --margin 8%
bash tools/art-normalize/pad-margin.sh atlas.alpha.png atlas.padded.png --size 1024 --margin 9.375% --grid 2x2
bash tools/art-normalize/flat-bg.sh input.png output.tripo.png --src-bg auto --bg '#E6E6E6' --size 1536x1024
bash tools/art-normalize/seamless.sh landscape.png landscape.seamless.png --axis x --blend 12%
bash tools/art-normalize/seam-check.sh landscape.seamless.png landscape.seam.png --axis x --blend 12% --reference landscape.png
bash tools/art-normalize/icon.sh icon.png icons/normalized --sizes 256,64 --src-bg auto
bash tools/art-normalize/sheet.sh review.png icons/normalized/*.256.png --bg checker --tile 256
python3 tools/art-normalize/normalize.py measure output.alpha.png --grid 2x2
```

Ví dụ xy tự kiểm được, dùng thư mục mới trong WORK:

```bash
python3 tools/art-normalize/example_xy.py tools/art-normalize/.tmp/example-xy
bash tools/art-normalize/seamless.sh tools/art-normalize/.tmp/example-xy/ground.png tools/art-normalize/.tmp/example-xy/ground.seamless.png --axis xy
bash tools/art-normalize/seam-check.sh tools/art-normalize/.tmp/example-xy/ground.seamless.png tools/art-normalize/.tmp/example-xy/ground.seam.png --axis xy --reference tools/art-normalize/.tmp/example-xy/ground.png
```

Đọc `pass` trong JSON: mã thoát 0 chỉ xác nhận đo/ghép thành công. Ảnh bất kỳ không bảo đảm có overlap phù hợp; nếu chốt trượt, xem đường nối ở 1:1 và chọn nguồn/overlap khác, không hạ ngưỡng để công bố.

Với art thật phải chạy seam-check có `--reference` là ảnh nguồn trước seamless. Chế độ nội ảnh không có reference chỉ dành cho texture tổng hợp: nó trượt cả phông tự nhiên đạt chuẩn (B1 tốt có row_step_excess 30,68), nên không dùng để duyệt hoặc công bố. Kể cả khi `pass` là true, seam-check không thấy mảnh vỡ ở mức nội dung (mây bị cắt chéo, ngọn thông lơ lửng trong trời): luôn xem đường nối ở 1:1 trước khi công bố.

Wrapper giữ ART_MAGICK, nếu thiếu tìm magick trong PATH rồi ~/.local/bin/magick. Không source common.sh trong shell tương tác. Dùng `--` trước tên bắt đầu bằng dấu `-`; API thư viện chuyển tên nguồn sang đường dẫn tuyệt đối. Chặn `%`, `[`, tiền tố coder trên tên và WORK, kể cả thư mục cha. Chỉ nhận PNG/JPEG/WebP một frame: kiểm chữ ký trước decoder; mỗi lần đọc dùng đúng coder đã kiểm, file bị tráo thành SVG không được đoán lại định dạng.

Mọi đích phải là tên mới, đuôi PNG; chặn ghi đè, symlink và alias nguồn. Các writer thư viện có cùng guard, dựng trong WORK riêng. `tmp` truyền vào phải nằm trong WORK và được thay bằng thư mục riêng của lần gọi. `im()` là primitive nội bộ, không phải writer được bảo vệ.

Công bố: copy vào `.partial` cùng thư mục đích → flush/fsync → os.link độc quyền → xóa partial. File mới là 0644. Chặn SIGTERM/SIGHUP/SIGINT trong lúc tạo tên tạm và lúc dọn; cho phép ngắt copy để dọn qua finally. Chỉ CLI/runner cài handler, giữ SIG_IGN của nohup; import không thay handler. Tín hiệu đến ngay sau link có thể trả lỗi dù đích đã đầy đủ, và có thể để lại một `.normalize-*.partial` là hard link thứ hai của đích hoàn chỉnh (giảm so với 012c, chưa loại hẳn); xóa tay được, media sync bỏ qua *.partial. SIGKILL/mất điện có thể để lại tạm; fsync không thay bảo đảm phần cứng về mất điện. Nhiều đích không phải giao dịch nguyên tử. Filesystem cần hỗ trợ hard link.

WORK là `tools/art-normalize/.tmp/`. Danh sách cho phép trong .gitignore chỉ giữ mã/text; ảnh và hồ sơ lô ở art-src trên Drive. Script .sh có quyền thực thi. Phiếu này không chạy Git hoặc build/test game.

## 2. Lệnh và quy tắc màu

| Lệnh | Mặc định và xử lý |
|---|---|
| `key-alpha IN OUT --bg auto\|#RRGGBB` | Fuzz 12%; màu tự động là trung vị bốn mảng góc 8×8. Góc lệch >45 cần chỉ định nền. Connected: nền nối biên và túi kín ≥64 px; global: mọi ứng viên. Nền trung tính chỉ nhận sắc độ max−min ≤6, kể cả flood bên ngoài, giữ highlight có màu. |
| `--despill auto\|protect-interior\|off` | Auto/protect-interior giống nhau: matte theo mô hình pha khóa với sơn lân cận trong 6 px, chỉ trong nền đã chọn nở Diamond 3 px. Chỉ nhận residual bình phương trung bình ≤9. Sơn tối không khóa và pixel đục không phải ứng viên không bị hạ alpha từ một phép fit gần 1. Không phục hồi sáng bằng trung bình hàng xóm. Off bỏ despill, vẫn tách theo khoảng cách. |
| `--no-key-hue` | Chỉ dùng khi nguồn/quyết định job loại sắc khóa: kẹp kênh khóa ở viền mềm trong dải 3 px và pixel có chênh khóa >50 trong lòng vật. Đây là thay đổi màu có chủ đích, phải đếm riêng. D1/D3 bật; D2/D4 giữ mặc định. |
| Khóa bão hòa | Chênh kênh >50% chênh nền, hoặc >25% nền và >70% kênh lớn nhất: ứng viên khóa, vẫn qua connected/global. Ứng viên bão hòa >70% kênh lớn nhất không giải thích được bằng viền pha được xóa. Vì vậy sơn trùng sắc khóa có thể bị xóa/hạ alpha cả trong lòng vật. Runner đếm tổng/xóa/alpha 9–249 của lớp này cách nền sáng >5 px; không loại khỏi báo cáo. |
| Alpha nguồn | Tự giữ khi ≥1% pixel alpha <128. `--keep-alpha` giữ rõ ràng RGB/alpha; từ chối alpha rỗng. Cảnh báo góc còn alpha >8 khi không keep-alpha. `--shrink N` co Diamond N, mặc định 0. |
| `pad-margin IN OUT --size N\|WxH --margin P%` | Trim alpha >8, +repage, Triangle giữ tỉ lệ, dự trữ lọc 2 px mỗi cạnh. Atlas 2×2 cần khổ chẵn và đường chia trống. Không xóa thành phần nhỏ. Có thể phóng to; flat-bg gọi fit với chặn phóng to. |
| `flat-bg IN OUT --src-bg auto --bg #RRGGBB --size WxH` | Fuzz 6%; màu nền nguồn tách riêng màu đích; lề 8%, PNG24, không phóng to nguồn. Túi trung tính và vành AA cần phân biệt. |
| `icon IN OUTDIR --sizes 256,64` | Fuzz 12%, src-bg auto, lề 8%; dựng đủ bộ trước công bố từng file. Lỗi giữa bước công bố có thể để lại một phần bộ hoàn chỉnh. |
| `seamless IN OUT --axis x\|xy --blend 12%` | B=ceil(L×blend), khổ W−B/H−B. Đường nối quy hoạch động theo từng hàng: sai số RGB bình phương cộng 60×bước nhảy RGB qua 8 cột bình phương, bước ngang tối đa 4 px mỗi hàng, tránh 5 px hai mép overlap. Smoothstep bán kính 3 px (ảnh nhỏ 1–2). Lưu đường nối/bán kính/khổ nguồn trong PNG tEXt art-normalize-seam. Không co giãn mặc định. `--keep-size` bật rõ mới Lanczos + virtual-pixel tile; phải đo lại. |
| `sheet OUT FILES… --bg dark\|light\|white\|checker --tile 256` | Tối đa 5 cột, nhãn tên/cỡ. Arial macOS → DejaVu-Sans → font đầu danh sách → mặc định. Sheet thu nhỏ không thay duyệt 1:1. |

Đầu ra PNG 8-bit sRGB, bỏ profile/metadata nguồn; seamless thêm bản ghi đường nối. Nguồn 16-bit/grayscale được nhận nhưng không giữ độ sâu. Màu thật trùng nền không thể phân biệt chắc chắn từ RGB; xem nguồn trước dùng global/no-key-hue.

## 3. Chốt mép

| Tiêu chí | Phép đo và ngưỡng |
|---|---|
| Mép lặp | MAE đầu–cuối ≤max(1; 2,5×trung vị cặp kề). |
| Gương | Cặp k/L−1−k và đối chứng c−k−1/c+k cùng khoảng cách 2k+1; tỷ số ≥0,5 khi đối chứng >1. Kiểm cả dải 30 px và các dải hẹp 3/5/8/12 px. |
| Chi tiết | Cửa sổ trượt tối đa 30 px, bước nửa cửa sổ phủ cả hai dải overlap; sai phân bậc hai / phần trong ≥0,9. Có reference thì so từng cửa sổ với đúng cột nguồn đã được chọn, thay kiểm nội ảnh; toàn ảnh / nguồn ≥0,9. Không dùng vị trí chuẩn hóa. |
| Sọc hàng | Cửa sổ trượt tối đa 30 px trên toàn hai dải; bước hàng có dấu trừ bước phần trong, dôi ≤5. Có reference: trừ bước ở đúng cột nguồn của từng hàng, kể cả đường nối di chuyển; residual ≤5. Không cộng cực đại nguồn vào ngưỡng. |
| Đường nối | Tìm lại đường nối từ pixel/reference, không tin metadata. Theo dải hàng 64 px: bước qua 2r+2 cột ≤max(1; p99 cặp cùng độ rộng ở phần trong), và ≤max(3; 1,5×cặp nguồn tương ứng+1). Bước độ sáng tuyệt đối trung bình hàng (có ghi riêng bước có dấu) ≤max(1; p99 cùng phép đo ở phần trong) và ≤max(3; 1,5×bước nguồn+1). Overlap <10 px không đủ đo bước 8 cột, không phát tiêu chí này. Dải 64 hàng thô: một đoạn gãy ngắn hơn dải có thể lọt. |
| Liền đường nối | Có overlap thì ghi `inferred_path_max_jump`, bước lớn nhất giữa hai hàng của đường nối suy ra; `path_continuity` đòi ≤8 px. Seamless chỉ đi tối đa 4 px/hàng; B1 công bố đo 5, ví dụ xy 4/4, B1 rách theo từng hàng 174. |
| Gương nguồn | MAE gương / nguồn ≥0,5 khi nguồn có mirror/control trong [0,75;1,5] và MAE >1. Ngoài khoảng đó ghi cờ miễn do nguồn không liền mép. |

Tham chiếu xy áp overlap vuông góc lên nguồn trước khi đối chiếu trục hiện tại. Đây vẫn là phép kiểm kinh nghiệm: cần duyệt đường nối và các cấu trúc cây/núi ở nguyên cỡ. Ảnh có cạnh <4 px bị từ chối rõ ràng. `measure` đo cả hai trục; seam-check chỉ xét trục được yêu cầu.

## 4. Kiểm và dựng lô

```bash
bash tools/art-normalize/test.sh
bash tools/art-normalize/jobs/dragon-hold-012/verify-code.sh
```

Test chỉ dùng ảnh tổng hợp và ART/STAGE/khóa riêng; không thể chạy build game hoặc dựng art thật khi khóa bị bỏ. Kiểm toàn bộ lòng vật/vành 4–10 px/ranh sơn, nét tối, ngưỡng chi tiết 0,9, sọc nhỏ một bên, gương hẹp/reference, cắt cứng/sai cột, bù lệch 30 px, túi Tripo, chữ ký/frame/coder, API, công bố độc quyền/tín hiệu và khóa runner/report. Kết quả mutant và giới hạn nằm ở [REVIEW-012d.md](REVIEW-012d.md); không dùng số 5/5 của 012c làm kết luận chung.

Xem [quy trình job](jobs/dragon-hold-012/README.md). 012–012c là lịch sử; 012d lưu bản 012c thành `.rejected-012c` kèm kiểm từng hash, giữ nguyên nguồn và nội dung `.rejected-012`/`.rejected-012b`. Mỗi PNG dẫn xuất có `.prompt.txt` ghi lệnh thực tế và prompt nguồn nguyên văn khi có. Không sinh ảnh mới và không gán prompt bản khác cho `.v1`.
