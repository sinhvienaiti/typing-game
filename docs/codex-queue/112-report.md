# Phiếu 112 · Last Line · Ba hướng ý tưởng

Ngày 29/10/2026, Codex. Đã làm sáu bản chọn bằng công cụ `image_gen` tích hợp, tổng cộng 13 lượt sinh; không ảnh nào quá ba lượt. Tự chấm sáu ảnh đạt M ≥ 8 và Q ≥ 8 ở cả hai cỡ. Đây là kết quả tự kiểm, **chờ Claude chấm lại**, chưa phải quyết định chọn hướng của chủ dự án.

## Ảnh giao và tờ chọn

Thư mục gốc media: `games/typing-survival/art-src/`. Mỗi bản chọn có `.png` và prompt nguyên văn `.prompt.txt`; toàn bộ 13 bản sinh giữ đủ `.tryN.png` và `.tryN.prompt.txt` trong `concepts/`.

| Hướng | FIGHT | KEYART |
| --- | --- | --- |
| A · Iron Warden | [Ảnh trận](../../games/typing-survival/art-src/concepts/a-iron-warden-fight.png), chọn try3 | [Key art](../../games/typing-survival/art-src/concepts/a-iron-warden-keyart.png), chọn try3 |
| B · Lightbearer | [Ảnh trận](../../games/typing-survival/art-src/concepts/b-lightbearer-fight.png), chọn try2 | [Key art](../../games/typing-survival/art-src/concepts/b-lightbearer-keyart.png), chọn try2 |
| C · Rampart | [Ảnh trận](../../games/typing-survival/art-src/concepts/c-rampart-fight.png), chọn try2 | [Key art](../../games/typing-survival/art-src/concepts/c-rampart-keyart.png), chọn try1 |

- [Tờ chọn ba hướng](../../games/typing-survival/art-src/_review/112-directions.jpg): 2591 × 2352; hàng đầu Today và Owner reference, ba hàng sau FIGHT, KEYART và Owner reference. Mỗi ảnh cao đúng 512 px, giữ tỷ lệ.
- [Tờ so từng bản với tham chiếu](../../games/typing-survival/art-src/_review/112-vs-ref.jpg): 2247 × 4512; sáu cặp, mỗi ảnh cao đúng 640 px, có nhận xét ngay dưới cặp.
- [Tờ kiểm cỡ nhỏ](../../games/typing-survival/art-src/_review/112/thumbnails.jpg): sáu ảnh con, mỗi ảnh đúng 384 × 256. Bản nhỏ riêng nằm trong `_review/112/*.384.jpg`.
- [Số đo máy](../../games/typing-survival/art-src/_review/112/measurements.json), [ảnh súng và quái đã đọc](../../games/typing-survival/art-src/_review/112/source-assets.jpg).

Đã đọc ảnh chuẩn của chủ dự án, cảnh nền hôm nay, tờ capture trận, các dáng quái gốc và năm súng. Đã đọc `guns.ts`, `foes.ts`: Pulse Gun, Heat Beam, Scatter Gun, Rail Gun, Star Mortar; Swarm, Scout, Brute, Shield Guard, Splitter, Shard, Pack Leader. Nội dung concept tuân theo ba hướng trong phiếu, không ép hình mới thành sprite cũ.

## Các lượt sinh và sửa prompt

Ba khối CONCEPT STYLE, hướng và cảnh được giữ nguyên văn trong mọi prompt. KEYART luôn đính kèm **bản FIGHT đã chọn của đúng hướng**, kèm đúng câu `Use the attached image only to keep the same hero, weapons, foes, colours and materials. Paint the new shot as described.` Không dùng ảnh chuẩn làm đầu vào để sao chép nội dung.

| Ảnh | Lượt | Kết quả và sửa đúng chỗ thiếu |
| --- | --- | --- |
| A FIGHT | 1 | Chỉ ba khối nguyên văn; công cụ trả 1024 × 1536. Mức chi tiết tốt nhưng khung dọc, cắt giữa sẽ mất nhân vật hoặc hố đen. Giữ nguyên bản sinh. |
| A FIGHT | 2 | Thêm chỉ dẫn kỹ thuật khổ ngang 1536 × 1024 và giữ đủ hố đen, nhân vật, vòng sàn. Đúng khổ nhưng mech lớn, chạm vùng đặt chữ. |
| A FIGHT | 3 | Thêm tọa độ bố cục: nhân vật ở đáy, vùng chữ là sàn tối, bầy ở nửa xa, đạn đi hai mép. Chọn bản này; vẫn lớn hơn tỷ lệ một phần năm, ghi thiếu bên dưới. |
| B FIGHT | 1 | Ba khối nguyên văn; trả 1024 × 1536. Nhận diện nhân vật và leviathan tốt nhưng sai khổ. |
| B FIGHT | 2 | Thêm khổ ngang và tọa độ nhân vật, hai sentinel, vùng sàn tối, bầy ở nửa xa. Chọn; giữ rõ áo choàng, vật liệu trắng vàng và leviathan. |
| C FIGHT | 1 | Ba khối nguyên văn; trả 1024 × 1536. Có hai pháo và chỉ huy nhưng khung dọc. |
| C FIGHT | 2 | Thêm khổ ngang, giải nghĩa hero là cụm tường/pháo/chỉ huy, tọa độ cụm đáy, sàn tối và quái leo tường. Chọn. |
| A KEYART | 1 | Prompt nguyên văn và ảnh trận A; đúng khổ ngang nhưng mech quay mặt về máy, hai súng thiên cyan. |
| A KEYART | 2 | Chỉ rõ nhìn giáp lưng, quay về bầy, hai màu súng, chừa trời tối phía trái. Giáp vẫn gợi mặt trước; chưa chọn. |
| A KEYART | 3 | Chỉ rõ ba lô động cơ, khớp hông sau, gót chân, tư thế đi xa máy; cockpit ở phía bầy. Chọn: giáp lưng rõ, có mảng trời tối phía trên trái. |
| B KEYART | 1 | Prompt nguyên văn và ảnh trận B; leviathan rõ, góc sau đúng, nhưng cả hai sentinel có lõi cyan và nét glyph gần chữ. |
| B KEYART | 2 | Khóa sentinel trái cyan/phải cam; glyph thành hạt, hình thoi, vòng tròn; chừa trời tối phía trên trái. Chọn. |
| C KEYART | 1 | Prompt nguyên văn và ảnh trận C. Chọn ngay: thấy chỉ huy từ sau, đủ hai pháo, tường, bầy và hố đen. |

**Khác phiếu về prompt:** sau những lượt sai bố cục, có thêm đoạn chỉ dẫn kỹ thuật về khổ, tọa độ, góc máy, màu vũ khí và hình học của glyph. Không thêm câu phong cách mới; ba khối bắt buộc vẫn nguyên văn. Công cụ tích hợp không có tham số khổ ảnh riêng, nên cần chỉ rõ trong prompt.

## Khổ, nền, vùng chữ và bố cục

`/opt/homebrew/bin/magick identify` xác nhận cả sáu bản chọn là **PNG 1536 × 1024, 8-bit sRGB, nền đặc**, không alpha. Các bản chọn đã đúng khổ ngay từ công cụ nên không cần cắt giữa hay thu ảnh chính. Ba try1 FIGHT khung dọc được giữ nguyên, không cắt vì mất nội dung bắt buộc. Tờ so và ảnh nhỏ dùng `-filter Lanczos -resize x512`, `x640` và `384x256!`.

Đã xem các bản chọn ở cỡ đầy đủ và cỡ nhỏ: không thấy chữ/số đọc được, logo, chữ ký, HUD, khung hoặc viền. Các vạch sáng trên pháo là chi tiết vật liệu; glyph B là hình học rời, không tạo từ hay dòng chữ. HUD trong ảnh chuẩn chỉ thuộc ảnh tham chiếu trên tờ so, không thuộc sáu concept.

Hộp kiểm dùng x = 537…998, y = 563…696, kích thước 462 × 134; làm tròn ra ngoài để phủ toàn vùng phần trăm. Luma tính trực tiếp trên RGB sRGB 0–1 theo công thức phiếu, không đổi sang ánh sáng tuyến tính.

| FIGHT | Luma TB trước → sau | Luma lớn nhất trước → sau | Px > 0,92 sau | TB ≤ 0,45; max ≤ 0,92 |
| --- | --- | --- | --- | --- |
| A | 0,230167 → **0,207388** | 1,000000 → **0,901961** | **0** | Đạt |
| B | 0,206904 → **0,186386** | 1,000000 → **0,901961** | **0** | Đạt |
| C | 0,134609 → **0,134609** | 0,899805 → **0,899805** | **0** | Đạt |

A/B được giảm RGB cục bộ 10% trong hộp kiểm, viền chuyển 40 px bên ngoài, bằng ImageMagick `-channel RGB -fx 'u*(1-0.10*(mask))' +channel`. Công thức mask và lệnh đầy đủ nằm trong `select-fights.py`. Không sửa bản try; bản chọn C chép nguyên try2. Đây là chỉnh sáng bằng công cụ trước khi cân nhắc sinh lại, không phủ mảng sàn giả lên ảnh.

| Bố cục FIGHT | A | B | C |
| --- | --- | --- | --- |
| Làn thẳng từ đáy lên hố đen phía trên | Có | Có | Có |
| Nhân vật/cụm chủ thể giữa đáy trong vòng sáng | Có | Có | Có |
| Một vũ khí trái, một vũ khí phải | Có | Có | Có |
| Bầy tập trung ở nửa xa, tràn về phía nhân vật | Có | Có | Có |
| Vùng chữ đạt hai ngưỡng số đo | Có | Có | Có |

**Chỗ còn thiếu:** mech A cao khoảng 35% ảnh, Lightbearer B khoảng 28%, lớn hơn mục tiêu khoảng 20%; A đã dùng đủ ba lượt. Đầu mech A và glyph B còn chạm phần thấp hộp chữ, dù số đo đạt; vùng này chưa hoàn toàn là sàn trống. Sentinel B hơi xa vai. KEYART A che phi công do góc lưng, một nòng bị thu ngắn theo phối cảnh và sắc cam ở cánh tay chưa thành tia rộng rõ như FIGHT. KEYART C có mốc lớn nhưng mảng trên trái còn nhiều cấu trúc, đặt logo sau này cần cân nhắc. Đây là ảnh chọn hướng, không coi các phần đó là thiết kế sản xuất đã khóa.

| Đọc ở 384 × 256 | Nhân vật | Hai vũ khí | Bầy | Hố đen |
| --- | --- | --- | --- | --- |
| A FIGHT | Được | Được | Được | Được |
| A KEYART | Được | Được, tay xa ngắn | Được | Được |
| B FIGHT | Được | Được | Được | Được, leviathan che một phần |
| B KEYART | Được | Được | Được | Được, leviathan rõ |
| C FIGHT | Được | Được | Được | Được |
| C KEYART | Được | Được | Được | Được |

## KA5 · Tự chấm mức chợ và chất lượng

Mốc M = 9 là ảnh chủ dự án. Sáu bản đều có mốc lớn làm nhân vật nhỏ lại, lớp gần–giữa–xa và trời, ánh sáng có hướng, sắc cam hố đen đối lập cyan vũ khí, vật liệu hoàn thiện. Điểm dưới mốc tham chiếu do nhiều lửa, sàn phản sáng và đám đông làm phân cấp chi tiết kém thoáng hơn ảnh chuẩn. B có thêm leviathan và vòng trạm, giúp kể quy mô rõ hơn. Không chấm dựa trên việc đẹp hơn bộ cũ.

Q gồm Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp, mỗi mục tối đa 2. Năm tiêu chí nằm ở bảng §1 của `ART_ACCEPTANCE.md`; §2.2 là ngưỡng ảnh 2D. Chấm riêng hai cỡ, không gộp M vào Q.

| Bản chọn | Cỡ | M | Đúng đề | Đọc | Hợp bộ | Khối | Dùng tiếp | Q | Mức |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A FIGHT | 1536 × 1024 | **8,4** | 1,5 | 1,5 | 2 | 2 | 1,5 | **8,5** | Tự đạt |
| A FIGHT | 384 × 256 | **8,2** | 1,5 | 1,5 | 2 | 2 | 1,5 | **8,5** | Tự đạt |
| A KEYART | 1536 × 1024 | **8,4** | 1,5 | 1,5 | 2 | 2 | 1,5 | **8,5** | Tự đạt |
| A KEYART | 384 × 256 | **8,2** | 1,5 | 1,5 | 2 | 1,5 | 1,5 | **8,0** | Tự đạt |
| B FIGHT | 1536 × 1024 | **8,7** | 1,5 | 2 | 2 | 2 | 1,5 | **9,0** | Tự đạt |
| B FIGHT | 384 × 256 | **8,5** | 1,5 | 1,5 | 2 | 2 | 1,5 | **8,5** | Tự đạt |
| B KEYART | 1536 × 1024 | **8,8** | 2 | 2 | 2 | 2 | 1,5 | **9,5** | Tự đạt |
| B KEYART | 384 × 256 | **8,6** | 2 | 1,5 | 2 | 2 | 1,5 | **9,0** | Tự đạt |
| C FIGHT | 1536 × 1024 | **8,5** | 2 | 2 | 2 | 2 | 1,5 | **9,5** | Tự đạt |
| C FIGHT | 384 × 256 | **8,3** | 2 | 1,5 | 2 | 2 | 1,5 | **9,0** | Tự đạt |
| C KEYART | 1536 × 1024 | **8,5** | 2 | 1,5 | 2 | 2 | 1,5 | **9,0** | Tự đạt |
| C KEYART | 384 × 256 | **8,3** | 2 | 1,5 | 2 | 2 | 1,5 | **9,0** | Tự đạt |

## KA1, script và phạm vi

Baseline được lấy **trước khi tạo bất kỳ file nào của phiếu**, bằng `md5 -r` từng file đệ quy trong `games/typing-survival/art-src/`: 267 file. Đối chiếu sau giao yêu cầu cả 267 file còn nguyên; `diff` chỉ thêm nội dung. Nhật ký: [trước](../../games/typing-survival/art-src/_review/112/md5-before.txt), [sau](../../games/typing-survival/art-src/_review/112/md5-after.txt), [diff](../../games/typing-survival/art-src/_review/112/md5-diff.txt), [kết quả](../../games/typing-survival/art-src/_review/112/md5-summary.json). Manifest sau được tính trước khi ghi chính manifest và hai nhật ký kết quả; ba file này không thể tự băm đệ quy.

Script đã dùng hoặc lưu lại để tái hiện nằm trong `_review/112/`: `baseline.py`, `prepare.py`, `replay-fight-prompts.py`, `replay-a-keyart-try2.py`, `refine-keyart.py`, `select-fights.py`, `source-sheet.sh`, `finish-v2.py`, `md5-audit.py`. `finish.py` là bản đầu dừng vì chuỗi channels có khoảng trắng; giữ lại nguyên, dùng `finish-v2.py` đã đổi dấu phân cách. Script giữ file đã có; audit chỉ chạy một lần để không thay mốc giao. Ảnh sinh gốc được ánh xạ chính xác trong `finish-v2.py`; muốn sinh lại phải gọi công cụ tích hợp với prompt lưu cạnh ảnh, không có runner API/mạng thay thế.

Không tìm thấy `docs/games/ART_DIRECTION_2026-10-28.md` trong các thư mục tài liệu được phép đọc; dùng nguyên nội dung chỉ đạo, prompt và thang M trong phiếu. Không sửa tài liệu khác để bù file thiếu. Không dùng mạng ngoài image_gen, không chạy Git, dev server, trình duyệt, build hoặc test game. Không đọc hay ghi Tu Tiên. Không thay mã, runtime, UI, âm thanh hoặc asset đang dùng. Không tạo tiếng vì phiếu chỉ yêu cầu ảnh; không làm phiếu 113. Không có capture trình duyệt hay raw frame cần prune; các try là bản sinh phải giữ theo phiếu.

Chủ dự án xem tờ chọn hướng; Claude cần chấm lại M/Q độc lập. Không chọn thay chủ dự án. Điểm M dưới đây ghi **đầy đủ / nhỏ**.

| Hướng | M FIGHT | M KEYART | Mạnh và yếu |
| --- | --- | --- | --- |
| A · Iron Warden | 8,4 / 8,2 | 8,4 / 8,2 | Mạnh ở sức nặng cơ khí, pilot và hai tay súng; yếu ở mech trận còn lớn và dáng súng key art bị thu ngắn. |
| B · Lightbearer | 8,7 / 8,5 | 8,8 / 8,6 | Mạnh ở cá tính nhân vật, áo choàng và quy mô leviathan; yếu ở glyph gần vùng chữ và sentinel hơi xa vai. |
| C · Rampart | 8,5 / 8,3 | 8,5 / 8,3 | Mạnh ở hai bến súng và tuyến phòng thủ đọc rõ; yếu ở chỉ huy nhỏ và key art ít khoảng yên cho logo. |
