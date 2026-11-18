# Phiếu 245 · Hàng danh sách, nút Close và bóng hình quái nhỏ

Đã làm đủ **13 bản chọn** bằng công cụ tích hợp `image_gen`: bốn hàng danh sách, ba nút Close và sáu bóng hình quái. Bản chọn, các lượt sinh và prompt nguyên văn đều nằm trong đúng đường dẫn phiếu cho phép. Không sửa runtime, manifest, `public/`, mã game hoặc tài liệu game; không chạy Git, máy chủ, trình duyệt, build hay bộ kiểm thử game. Không đọc hoặc ghi Tu Tiên.

Các chốt cỡ thật, độ đặc, độ phủ, tương phản và khác dáng đều đạt. **Chưa coi là nghiệm thu trong game.** Còn cờ hue gần đen của vài ảnh alpha thật, giải thích ở dưới; cần Claude duyệt cùng lượt gắn ảnh tại 1280×720 và 1920×1080.

## 1. File giao

| Game | Thư mục | Bản chọn |
| --- | --- | --- |
| Dragonhold | `games/dragon-hold/art-src/ui/frames/` | `list-row.png`, `list-row-active.png`, `close.png` |
| Wordwoven | `games/typing-defense/art-src/ui/frames-epic/` | `list-row.png`, `list-row-active.png`, `close.png` |
| Last Line | `games/typing-survival/art-src/ui/frames-epic/` | `close.png` |
| Last Line | `games/typing-survival/art-src/ui/foes/` | `brute.small.png`, `pack-leader.small.png`, `scout.small.png`, `swarm.small.png`, `shield-guard.small.png`, `splitter.small.png` |

Bốn hàng có khổ 1536×256, RGBA sRGB, `.json` cùng tên với `size`, bốn `slice`, `fill` và hướng dẫn tỷ lệ hiển thị. `fill` chỉ là màu tham khảo; tờ dựng dùng nguyên vân tranh. Chín ảnh Close/quái có bản 1024² và `.256`, `.128`, `.64`; mỗi bản có `.prompt.txt`. Mọi lượt `tryN` được giữ. Tổng 40 PNG bản chọn và bản thu; 23 PNG lượt sinh.

Tờ xem tại `games/<game>/art-src/_review/245-sheet.jpg`, `245-raw-vs-final.jpg`; ô Close `245-close-{720,1080}.png` và bản `-4x`. Hai game có hàng danh sách thêm `245-list-{720,1080}.png` và `-4x`. Last Line thêm `245-foes-{720,1080}-{1x,4x}.png`.

## 2. Lượt sinh và hậu kỳ

| Ảnh | Lượt chọn | Chỗ đã sửa |
| --- | --- | --- |
| Dragonhold list-row | 2/2 | Lượt 1 sao theo khung cũ, góc và đá kem quá nặng. Lượt 2 giảm còn viền vàng mảnh và hai đầu sắt rèn. |
| Dragonhold list-row-active | 1/1 | Đính kèm hàng lượt 2; giữ dáng, thêm viền than hồng và viên ngọc trái phát sáng. |
| Wordwoven list-row | 2/2 | Lượt 1 có huy hiệu mặt trời chiếm cả chiều cao. Lượt 2 đổi thành mép kem mảnh, góc mây nhỏ và dấu vàng trái. |
| Wordwoven list-row-active | 1/1 | Đính kèm hàng lượt 2; giữ dáng, thêm ánh đèn hổ phách dọc viền và dấu trái. |
| Dragonhold close | 2/2 | Lượt 1 thiếu tương phản khi đo hiệu luma trung bình. Lượt 2 tăng phần vàng sáng trên X và phản sáng sắt rèn. |
| Wordwoven close | 1/1 | X kem lớn, đĩa ngọc và viền kim loại ấm. |
| Last Line close | 1/1 | X trắng vàng, đĩa than chì, đường lam điện. |
| Brute | 2/2 | Vai rộng, nắm đấm dày; lượt 2 tăng mảng bạc thay các vệt tối nhỏ. |
| Pack Leader | 2/2 | Giữ mào vàng cao; lượt 2 tăng mảng sáng rộng, tách dáng với Brute. |
| Scout | 2/2 | Lượt 2 gom cánh và mũi thành các mặt lớn, bỏ điểm lam sáng riêng. |
| Swarm | 2/2 | Lượt 2 tăng phản sáng trên gai và thân, giữ lõi cam lớn. |
| Shield Guard | 2/2 | Lượt 2 kéo dáng thành tấm khiên cao hẹp, tăng mặt khiên lam bạc; sửa cặp IoU với Swarm. |
| Splitter | 3/3 | Lượt 1 còn dáng cua gần Brute; lượt 2 tròn hơn, có khuyết trên/dưới nhưng còn tối. Lượt 3 có hai nửa bạc rộng, khe cam dọc rõ. Không sinh lượt 4. |

Ảnh tham chiếu: khung `button` Dragonhold, `button.v2` Wordwoven; các icon `check`, `lock`, `vol-music`, `streak`, `mag-full` tương ứng; từng quái đính kèm đúng chân dung `.v2` của nó. Đã xem ảnh tham chiếu thương mại của chủ dự án để so mức hoàn thiện.

Công cụ trả khổ khác yêu cầu. Hàng được tách nền, cắt đúng phần alpha, co **đều** về cao 256 rồi co phần giữa bằng chín mảnh về 1536; giữ nguyên hai đầu. Icon/quái được cắt phần alpha, co **đều** cạnh dài về 716 px và đệm giữa canvas 1024². Không kéo méo icon. Bốn hàng cắt trên/dưới 48 px = 18,75% chiều cao, hai đầu 200 px; khi hiển thị mọi đường cắt cùng tỷ lệ 34/256 hoặc 51/256.

Dragonhold/Wordwoven tách nền bằng `tools/art-normalize/key-alpha.sh`, `ART_MAGICK=/opt/homebrew/bin/magick`, `--mode global --despill protect-interior`. Last Line giữ alpha thật. Chuẩn hóa độ kín của alpha nguồn, bỏ sương ngoài vật; khử màu khóa chỉ trong dải mép ngoài 6 px; sửa alpha gần 0/255 và đốm rời do nội suy. Không tô đè lòng, không thay vân, không vẽ thêm chi tiết. Tăng sáng toàn RGB **+10%** ở Close Dragonhold, Brute và Splitter; các ảnh còn lại không tăng sáng.

Các bản thu lấy Lanczos trực tiếp từ bản 1024, sau đó chỉ làm sạch sai số alpha ở mép; không làm nét, kể cả bản 64. Đây là phần hậu kỳ mép có thêm so với cách chỉ chạy một lệnh thu ảnh. Tờ bản sinh | bản hậu kỳ giữ để đối chiếu. Font tờ kiểm: Arial hệ thống, chữ thử tiếng Anh.

## 3. Số đo

Độ đặc: opening ô vuông 2×2 trên alpha >128 tại cỡ 720p. Độ phủ: diện tích alpha >128 chia diện tích hộp bao. Tương phản là **hiệu hai luma trung bình**, không đổi sang trung bình hiệu tuyệt đối để ép qua ngưỡng. Close đo ở góc trong bên phải panel thật; quái đo trên `word-plate` thật. Ô Close để nhãn trống. Quái có thêm ô trên mảnh `button` và `panel`, xem `proofs-final/`.

| Ảnh | Cạnh dài bbox nguồn (%) | Độ đặc (%) | Độ phủ (%) | Δ luma 720p | Δ luma 1080p |
| --- | ---: | ---: | ---: | ---: | ---: |
| dh-close | 69.92 | 100.00 | 73.97 | 0.2989 | 0.2965 |
| ww-close | 69.92 | 100.00 | 80.99 | 0.3155 | 0.3182 |
| ll-close | 69.92 | 100.00 | 80.58 | 0.3438 | 0.3469 |
| ll-brute.small | 69.92 | 97.39 | 71.88 | 0.2581 | 0.2630 |
| ll-pack-leader.small | 69.92 | 97.83 | 57.50 | 0.3288 | 0.3267 |
| ll-scout.small | 69.92 | 97.44 | 39.80 | 0.2680 | 0.2545 |
| ll-swarm.small | 69.92 | 100.00 | 56.25 | 0.2556 | 0.2584 |
| ll-shield-guard.small | 69.92 | 98.92 | 72.66 | 0.2903 | 0.2891 |
| ll-splitter.small | 69.92 | 100.00 | 80.36 | 0.4107 | 0.4123 |

Mọi ảnh có alpha min 0/max 255. Bbox icon/quái nằm trong 68–72%, lệch tâm không quá 0,049%. Mọi bản chọn và 27 bản thu: **0 pixel alpha lửng ngoài dải mép 3 px**. Mọi bản chọn: **0 đốm rời nhỏ hơn 20 px**. Số đo đầy đủ, kể cả từng bản thu: [`audit.json`](245/proofs-final/audit.json), [`metrics.json`](245/final-v2/metrics.json).

| Hàng | Độ lệch luma dọc viền | Tương phản chữ/lòng | Slice trên/dưới |
| --- | ---: | ---: | ---: |
| dh-list-row | 0.0224 | 11.46:1 | 18.75% |
| dh-list-row-active | 0.0317 | 10.07:1 | 18.75% |
| ww-list-row | 0.0097 | 11.30:1 | 18.75% |
| ww-list-row-active | 0.0142 | 8.53:1 | 18.75% |

Độ lệch viền đo trên profile luma trung bình mỗi cột của dải viền 48 px, bỏ hai đầu; ngưỡng 0,05. Đồng thời giữ số cực đại từng đường quét trong JSON để kiểm lại, không giấu dao động do vân/glow. Chữ kem `#f3ead2` so với màu trung vị lòng; các tờ 720p/1080p cho thấy hàng đang chọn ngay ở 1×.

IoU thường/đang chọn, đo đúng toàn ảnh 1536×256: Dragonhold **0.9902**, Wordwoven **0.9979**; vượt 0,95. Ở hàng 300×34: cả hai cặp **0.9997**. Ba nút Close cùng nghĩa, cùng dáng tròn nên không áp yêu cầu khác dáng giữa chúng. Tờ xem đặt Close cạnh Settings/Sound cùng game để so cỡ.

Sáu quái, 15 cặp ở 24 px:

| A | B | IoU |
| --- | --- | ---: |
| brute | pack-leader | 0.3269 |
| brute | scout | 0.3403 |
| brute | swarm | 0.5988 |
| brute | shield-guard | 0.3595 |
| brute | splitter | 0.6209 |
| pack-leader | scout | 0.3077 |
| pack-leader | swarm | 0.5128 |
| pack-leader | shield-guard | 0.6228 |
| pack-leader | splitter | 0.3878 |
| scout | swarm | 0.4051 |
| scout | shield-guard | 0.4370 |
| scout | splitter | 0.3163 |
| swarm | shield-guard | 0.5592 |
| swarm | splitter | 0.6701 |
| shield-guard | splitter | 0.3858 |

Lớn nhất 24 px **0.6701**; 32 px **0.6667**. Lượt đầu có Brute–Splitter 0,7246 và Swarm–Shield Guard 0,7222; đã sửa bằng các lượt sinh sau, không chỉnh mặt nạ để ép IoU.

### Cờ hue và giới hạn phép đo

Hai nút Close dùng nền khóa đều dưới 0,2% hue magenta trong bản nguồn và các bản thu sau khử loang mép; bốn hàng lần lượt có tỷ lệ 0.0123%, 0.0003%, 0.0023%, 0.0000%.

Last Line sinh trên alpha thật, không có màu nền khóa. Nếu vẫn áp phép đếm mọi hue 285–330° với S >0,5 cho cả ảnh alpha, một số số đo vượt 0,2%: ví dụ nguồn Swarm **0,6620%**, Shield Guard **0,3110%**; có bản thu của Brute và Scout cũng vượt. Chủ yếu là RGB gần đen như `(1,0,1)`, sai số màu của nét tối; phần hue đó có giá trị sáng >10/255 rất nhỏ (mọi bản ≤0,1595%). Hai số được ghi riêng trong audit, không đổi công thức hay bỏ pixel khỏi báo cáo.

Theo ART_ACCEPTANCE §5, giữ RGB trong vật, không xóa hoặc phủ màu chỉ để ép con số. **Cờ này chờ Claude duyệt**; không khẳng định trọn bộ qua mọi ngưỡng hue khi áp tuyệt đối cho alpha thật. Các tiêu chí hình, tương phản và sạch alpha không bị hạ ngưỡng.

## 4. Tự đọc và tự chấm ở cỡ thật

[`blind-notes.md`](245/blind-notes.md) ghi 3–5 từ cho từng ô đã ẩn tên ở 1× trước khi mở ánh xạ. Kết quả đọc: Scout là dart/cánh quét, Shield Guard là tấm khiên lam, Splitter là hai nửa nứt, Swarm là mìn có lõi và gai, Brute là khối vai rộng có sừng, Pack Leader là quái cao đội mào. Ba Close đọc thành X đóng bảng. Không còn sáu con cùng thành ngài nâu hay Swarm thành một chấm. Đây là tự đọc của người biết prompt, **không phải** chấm mù độc lập.

Điểm tự chấm trên bản hậu kỳ ở ô 720p 1×. Năm số Q lần lượt: đúng đề / đọc được / hợp bộ / hình khối / dùng tiếp. Giảm điểm hợp bộ của bóng hình nhỏ vì mảng bạc lớn hơn chân dung; giảm dùng tiếp ở các quái còn cờ hue. Điểm M so với giao diện thương mại, không tự coi số đo là bằng chứng đủ cho nghiệm thu.

| Ảnh | M | Năm điểm Q | Q/10 |
| --- | ---: | --- | ---: |
| dh-list-row | 8,2 | 2/2/2/2/2 | 10 |
| dh-list-row-active | 8,3 | 2/2/2/2/2 | 10 |
| ww-list-row | 8,2 | 2/2/2/2/2 | 10 |
| ww-list-row-active | 8,4 | 2/2/2/2/2 | 10 |
| dh-close | 8,2 | 2/2/2/2/2 | 10 |
| ww-close | 8,2 | 2/2/2/2/2 | 10 |
| ll-close | 8,4 | 2/2/2/2/2 | 10 |
| ll-brute.small | 8,0 | 2/2/1/2/1 | 8 |
| ll-pack-leader.small | 8,2 | 2/2/1/2/2 | 9 |
| ll-scout.small | 8,1 | 2/2/1/2/1 | 8 |
| ll-swarm.small | 8,2 | 2/2/1/2/1 | 8 |
| ll-shield-guard.small | 8,2 | 2/2/1/2/1 | 8 |
| ll-splitter.small | 8,0 | 2/2/1/2/2 | 9 |

Cần chủ dự án/Claude nhìn kỹ phần bạc sáng của Splitter so với nhận diện kính đen cũ, và quyết cờ hue tối khi gắn thực tế. Điểm từ 8 là tự đánh giá, không thay quyết định nhận cuối.

## 5. Kiểm toàn vẹn và chạy lại

KA1: **317 file cũ giữ nguyên**, **130 file thêm**, **0 đổi, 0 mất** trong bốn thư mục đích. [`md5-before.txt`](245/md5-before.txt), [`md5-after.txt`](245/md5-after.txt), [`md5-diff.txt`](245/md5-diff.txt). Danh sách giao và hash: [`delivered.json`](245/delivered.json). Chỉ có dòng thêm trong diff. 114 file bản chọn/phụ trợ đã giao; các try là phần thêm riêng.

Chạy lại bằng Python chuẩn và ImageMagick, với thư mục đầu ra **mới** để không ghi đè:

```sh
python3 docs/codex-queue/245/process.py docs/codex-queue/245/recheck-new docs/codex-queue/245/selection-final.json
python3 docs/codex-queue/245/proofs.py docs/codex-queue/245/recheck-new docs/codex-queue/245/recheck-proofs-new
```

`process.py` và `proofs.py` chỉ dựng/đo ảnh trong thư mục báo cáo. `deliver.py` đã chạy một lần; không chạy lại vì nó chủ động từ chối file đích đã có. Các thư mục `candidate-*`, `stage-v1`, `final`, `proofs-v1` là ứng viên và bằng chứng trước khi sửa; **bản giao khớp `final-v2/` và `proofs-final/`**. Không xóa lượt sinh hay file cũ để làm sạch lịch sử.

## 6. Phần không làm

- Không tạo hàng Last Line: phiếu quy định dùng lại `button`/`button-active` của 127.
- Không gắn ảnh, sửa code/manifest hoặc chép `public/`: để Claude làm lượt gắn/chấm trong game.
- Không làm âm thanh: phiếu này chỉ yêu cầu hình ảnh.
- Không chạy game/build/test suite, không tạo capture trình duyệt. Không có raw frame trình duyệt cần prune.
- Không đổi/chạy model qua API riêng; dùng đúng công cụ ảnh tích hợp, không dùng CLI fallback.
