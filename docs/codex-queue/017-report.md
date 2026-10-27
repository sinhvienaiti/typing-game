# Phiếu 017 · Sửa 14 ảnh 2D bằng công cụ

Ngày 27/10/2026. Đã đọc tools/art-normalize/README §1, key-alpha, pad-margin, flat-bg, icon; ART_ACCEPTANCE; các dòng tương ứng ART_FIX_QUEUE §2, §5.1, §5.2. Không AI, không mạng, không Git, không build/test game, không sửa mã game/model hoặc danh sách duyệt.

Đã xuất đủ **23 file theo cột “Ra file” cho 14 mục**, thêm **5 file lượt 2** trong review cho C21, V37, I08. **Không coi toàn bộ phiếu đạt**: V37 không đạt sau hai lượt; T2 chưa đạt chốt seam tổng. C21/I08 nên duyệt lượt 2 trong review. V18 cần xem phần viền xanh còn/mất trước Tripo. Không ghi đè bản lượt 1.

Kiểm 1 sạch: 14 MD5 nguồn giữ nguyên, đã đối chiếu lại ngay khi viết báo cáo. Kiểm 2 của phiếu 017 sạch ở bản kê ban đầu: 154/154 file đúng phạm vi. Khi chạy lại lệnh find để chốt, file của lượt công việc đồng thời khác xuất hiện; xem bản kê nguyên vẹn và phân biệt ở cuối báo cáo. **Không xóa file của người/agent khác để làm sạch danh sách toàn repo.**

## Ảnh xem nhanh đã tự xem

- [Rồng Giữ Ải · 8 hàng](../../games/dragon-hold/art-src/_review/017-dh.jpg).
- [Lời Gọi · 6 hàng](../../games/typing-defense/art-src/_review/017-td.jpg).
- [Vùng nối tile 1:1, trái sang phải T2/T3/T7](../../games/dragon-hold/art-src/_review/017/tile-seams-1to1.jpg).
- [V18 viền bó lúa](../../games/dragon-hold/art-src/_review/017/V18-wheat.compare.jpg), [cỏ trước phải](../../games/dragon-hold/art-src/_review/017/V18-grass.compare.jpg), nguồn trái/kết quả phải.

Đã xem kỹ cả hai tờ, vùng nối, icon 64/32 px và decal trên grass-a. Các tờ dùng Arial `/System/Library/Fonts/Supplemental/Arial.ttf`. Hàng C21/I08/V37 hiển thị lượt 2; V37 ghi CHƯA ĐẠT. Icon đặt đúng số pixel trước khi lưu JPEG.

## Lệnh và kết quả

Mọi lệnh chạy với `ART_MAGICK=/opt/homebrew/bin/magick`, `PYTHONDONTWRITEBYTECODE=1`. Các argv ImageMagick/CLI được chép đủ bên dưới từ standard-log.json. Các lệnh Python không nhận thêm tham số; mọi tọa độ và tham số cố định nằm nguyên trong script được giữ tại `_review/017/`.

[normalizer.py](../../games/dragon-hold/art-src/_review/017/normalizer.py) gọi nguyên normalize.main(), chỉ chuyển WORK, TMPDIR, MAGICK_TEMPORARY_PATH vào `_review/017/work` để không ghi `.tmp` của công cụ ngoài phạm vi. Không sửa công cụ. Các script và writer từ chối ghi đè; không chạy lại vào tên đã có.

Điểm theo năm tiêu chí ART_ACCEPTANCE: đúng đề, đọc ở cỡ game, hợp bộ, hình khối, dùng được bước sau. Điểm không thay điều kiện kỹ thuật: không nhận V37 chỉ vì trung bình màu đạt.

| # | Mã | Lệnh đã chạy (đủ tham số) | Ra file | Số kiểm (mục 3–5) | Tự chấm /10 theo ART_ACCEPTANCE.md | Còn thiếu gì |
|---|---|---|---|---|---|---|
| 1 | C21 Chân dung Mộc Tinh | `/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py key-alpha games/typing-defense/art-src/portraits/moc-tinh.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/moc-tinh.key.png --bg '#0000FF' --despill protect-interior`<br>`/opt/homebrew/bin/magick /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/moc-tinh.key.png -crop 760x760+280+0 +repage -resize 1024x1024 -strip /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/moc-tinh.bust.png`<br>`python3 games/dragon-hold/art-src/_review/017/portrait.py`<br>Lượt 2: `python3 games/dragon-hold/art-src/_review/017/retry.py` | `games/typing-defense/art-src/portraits/moc-tinh.crop.png`<br>`/Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/moc-tinh.crop.retry.png` | 1024×1024 RGB. Mực lớp riêng **107.000, 63.000, 160.000**, A=184/255=72,16 %. Nét sau ghép L1 **77.206, 116.459, 115.451**; L2 **141.245, 109.498, 179.490**. Crop 760×760+280+0, viền Disk:3 (3 px) #2B211A. | L1 **6,5 — Sửa**; L2 **8 — Tạm chấp nhận**. | L1 không chọn: mực tím bị nền xanh pha xỉn. L2 lót #E6E6E6 đúng hình nét cọ rồi phủ #6B3FA0 ở 72 %. Mặt đọc được ở 64 px, 32 px còn nhỏ; nét cọ hơi thẳng. Claude duyệt bản retry, không nhập bản L1 chỉ vì đúng tên. |
| 2 | V37 Mỏ Vàng, Lò Đúc Tiền | `python3 games/dragon-hold/art-src/_review/017/manual.py` (nhánh V37, đã xuất trước lỗi D4)<br>Lượt 2: `python3 games/dragon-hold/art-src/_review/017/retry.py` | `games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.coal.png`<br>`/Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/gold-mine-lo-duc-tien.coal.retry.png` | 1024×1024 RGB. Hộp bao x=**300..470**, y=**496..643**, tính cả hai đầu. L1 đổi **9094 px**, RGB **105.151, 35.683, 21.904**, sáng **19,3964 %**. L2 đổi **9626 px**, RGB **106.388, 36.792, 21.996**, sáng **19,8135 %**. Cả hai ≤35 %; **0 px đổi ngoài hộp**. | L1/L2 **6,5 — Sửa; KHÔNG ĐẠT Tripo**. | Vẫn còn viền vàng/cam sáng sát đáy lòng lò và máng; L2 phủ lòng lò hơi phẳng. Không nhận chỉ vì trung bình màu đạt. Đã đủ hai lượt, không thử lần ba. Vàng mái/đồ trang trí giữ nguyên. |
| 3 | V18 Bộ cấp Ruộng Lúa L2 | `/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py key-alpha games/typing-defense/art-src/kits/farm-kit-l2.png games/typing-defense/art-src/kits/farm-kit-l2.alpha.png --bg '#00FF00' --mode global --fuzz 25%` | `games/typing-defense/art-src/kits/farm-kit-l2.alpha.png` | 1024×1024 RGBA, góc A=**0,0,0,0**. Cỏ trước phải: **2297/2391** px xanh nguồn còn A>8, **2252** px A≥230. Viền bó lúa: **227/545** px xanh còn A>8, **18** px A≥230. | **8,5 — Tạm chấp nhận**. | Cỏ trước phải còn rõ. Despill mặc định giảm phần lớn viền xanh bó lúa. Phiếu nói giữ viền, ART_FIX_QUEUE mô tả despill xóa viền; giữ đúng lệnh hàng việc ưu tiên, không thêm despill off. Claude xem crop trước Tripo. Giá phơi nâu còn. |
| 4 | V69 Hạt Mộc Tinh | `/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py flat-bg games/typing-defense/art-src/projectiles/seed-drop.png games/typing-defense/art-src/projectiles/seed-drop.flat.png --src-bg auto --bg '#00FF00' --size 1024x1024` | `games/typing-defense/art-src/projectiles/seed-drop.flat.png` | 1024×1024 RGB, bốn góc #00FF00; flat-bg không yêu cầu alpha. Cuống và hõm đáy còn. | **8,5 — Tạm chấp nhận**. | Vân múi gắt còn; làm trơn sau Tripo thuộc công việc khác. |
| 5 | T2 Cỏ xuân B | `/opt/homebrew/bin/magick games/dragon-hold/art-src/ground/pine-river/grass-b.png -modulate 100,115,85 -strip games/dragon-hold/art-src/ground/pine-river/grass-b.hue.png`<br>`/opt/homebrew/bin/magick games/dragon-hold/art-src/ground/pine-river/grass-b.hue.png -virtual-pixel tile -filter Lanczos -distort Resize 1024x1024 -strip games/dragon-hold/art-src/ground/pine-river/grass-b.1024.png`<br>`/opt/homebrew/bin/magick games/dragon-hold/art-src/ground/pine-river/grass-a.png -virtual-pixel tile -filter Lanczos -distort Resize 1024x1024 -strip /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/grass-a.1024.png`<br>`python3 games/dragon-hold/art-src/_review/017/seams-v2.py` (lệnh từng lần ở mục kiểm 4) | `games/dragon-hold/art-src/ground/pine-river/grass-b.hue.png`<br>`games/dragon-hold/art-src/ground/pine-river/grass-b.1024.png` | Hue 1254×1254 RGB; tile **1024×1024 RGB**. MAE X **7,412812→8,529948**; Y **6,688464→8,055339**. Reference gốc IndexError. Bổ sung cùng khổ: **pass=false**, row_streak=false cả X/Y. | **8,5 — Tạm chấp nhận về hình; CHƯA ĐẠT kiểm seam tổng**. | Ghép xen A/B còn thấy ranh mảng màu; hoa tím ngả lam như hàng việc đã dự báo. Không hạ ngưỡng hoặc làm seamless ngoài phạm vi. |
| 6 | T3 Rêu dưới tán | `/opt/homebrew/bin/magick games/dragon-hold/art-src/ground/pine-river/moss.png -virtual-pixel tile -filter Lanczos -distort Resize 1024x1024 -strip games/dragon-hold/art-src/ground/pine-river/moss.1024.png`<br>`python3 games/dragon-hold/art-src/_review/017/seams-v2.py` | `games/dragon-hold/art-src/ground/pine-river/moss.1024.png` | **1024×1024 RGB**. MAE X **6,538543→6,379557**; Y **6,555290→6,505859**. Reference gốc lỗi; bổ sung cùng khổ **pass=true X/Y**. | **7,5 — Tạm chấp nhận**. | Gò rêu và bóng khối còn; không chỉnh tương phản. Pass cùng khổ không thay kết quả lỗi với nguồn gốc. |
| 7 | T7 Đá rêu dốc | `/opt/homebrew/bin/magick games/dragon-hold/art-src/ground/pine-river/rock.png -virtual-pixel tile -filter Lanczos -distort Resize 1024x1024 -strip games/dragon-hold/art-src/ground/pine-river/rock.1024.png`<br>`python3 games/dragon-hold/art-src/_review/017/seams-v2.py` | `games/dragon-hold/art-src/ground/pine-river/rock.1024.png` | **1024×1024 RGB**. MAE X **5,681818→5,579753**; Y **7,016215→6,900716**. Reference gốc lỗi; bổ sung cùng khổ **pass=true X/Y**. | **8,5 — Tạm chấp nhận**. | Viền tối mép phiến còn. Không chỉnh màu/tương phản. Giới hạn kiểm như T3. |
| 8 | D4 Decal rêu, vũng nước | `python3 games/dragon-hold/art-src/_review/017/manual-v2.py` (nhánh D4) | `games/dragon-hold/art-src/decals/pine-river/moss-puddles.v1.tone.png` | 1024×1024 RGBA; góc **0,0,0,0**. **186217 px rêu** đổi, RGB TB **73,844;94,888;38,252 → 56,273;85,408;34,434**. **808 px tím hồng**: 802 đặt A=0, 6 tô màu kề; **0 thay đổi alpha khác**. | **8,5 — Tạm chấp nhận**. | Giữ hình khối rêu/đá/lá/nước. Lần dựng mặt nạ đầu dừng tại (697,110) trước khi xuất D4; mở chọn màu kề sang màu đá không tím rồi mới xuất duy nhất một ảnh. |
| 9 | D2 Decal cụm hoa | `/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py key-alpha games/dragon-hold/art-src/_review/015-flower-clusters.png games/dragon-hold/art-src/decals/pine-river/flower-clusters.015.alpha.png --bg '#0000FF' --despill protect-interior`<br>`/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py pad-margin games/dragon-hold/art-src/decals/pine-river/flower-clusters.015.alpha.png games/dragon-hold/art-src/decals/pine-river/flower-clusters.015.1024.png --size 1024 --margin 9.375% --grid 2x2` | `games/dragon-hold/art-src/decals/pine-river/flower-clusters.015.alpha.png`<br>`games/dragon-hold/art-src/decals/pine-river/flower-clusters.015.1024.png` | 1254×1254 và **1024×1024 RGBA**, góc cả hai **0,0,0,0**. Max A đường chia x=511/512 và y=511/512: **0/0**. Tím nguồn **47427 px**: **47240** còn A≥230; **47211** giữ nguyên RGB. | **9 — Đạt**. | Hoa chuông nghiêng còn. Không dùng no-key-hue. Nguồn bản 015 được ghi ở báo cáo này thay vì README ngoài phạm vi. |
| 10 | D3 Decal sỏi, lá, kim thông | `python3 games/dragon-hold/art-src/_review/017/manual-v2.py` (nhánh D3) | `games/dragon-hold/art-src/decals/pine-river/forest-litter.clean.png` | 1024×1024 RGBA; góc **0,0,0,0**. Đổi đúng **33 px**, gần ước tính 34. RGB TB **124,212;151,636;119,212 → 119,818;121,212;120,242**. Giữ nguyên alpha. | **8,5 — Tạm chấp nhận**. | Bóng khối/điểm sáng còn. Chỉ ô sỏi trên trái; không đụng ô lá/kim thông/cành. Tọa độ từng px trong manual-log.json. |
| 11 | I08 Icon Vảy Cứng | `python3 games/dragon-hold/art-src/_review/017/manual-v2.py` (nhánh I08; -modulate 115,105,104)<br>`python3 games/dragon-hold/art-src/_review/017/normalizer.py icon games/dragon-hold/art-src/ui/icons/hard-scale.warm.png games/dragon-hold/art-src/icons/normalized --sizes 256,64`<br>Lượt 2: `python3 games/dragon-hold/art-src/_review/017/retry.py`<br>`python3 games/dragon-hold/art-src/_review/017/normalizer.py icon games/dragon-hold/art-src/_review/017/hard-scale.warm.retry.png games/dragon-hold/art-src/_review/017 --sizes 256,64` | `games/dragon-hold/art-src/ui/icons/hard-scale.warm.png`<br>`games/dragon-hold/art-src/icons/normalized/hard-scale.warm.256.png`<br>`games/dragon-hold/art-src/icons/normalized/hard-scale.warm.64.png`<br>`/Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/hard-scale.warm.retry.png`<br>`/Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/hard-scale.warm.retry.256.png`<br>`/Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/hard-scale.warm.retry.64.png` | 1254×1254 RGB; hai bộ icon 256×256/64×64 RGBA, góc **0,0,0,0**. L1 mean cam **239.257, 166.033, 115.928**; L2 **232.544, 147.633, 99.172**. So #E58A5F=(229,138,95): L2 Δ(**+3,544;+9,633;+4,172**). L1 đổi 536409 px; L2 681827 px với mask mềm. | L1 **7,5**, không chọn do ranh gắt; L2 **8,5 — Tạm chấp nhận**. | Nên duyệt bộ retry. Viền nâu tối giữ nguyên; dáng vảy hơi méo ở 32 px còn. Bộ tên chính vẫn là L1 vì cấm ghi đè. |
| 12 | I11 Icon Long Hống | `/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py icon games/dragon-hold/art-src/_review/015-skill-roar.png games/dragon-hold/art-src/icons/normalized --sizes 256,64` | `games/dragon-hold/art-src/icons/normalized/015-skill-roar.256.png`<br>`games/dragon-hold/art-src/icons/normalized/015-skill-roar.64.png` | 256×256/64×64 RGBA, góc cả hai **0,0,0,0**. Đã xem 64/32 px. | **8,5 — Tạm chấp nhận**. | Đầu rồng khó nhận ở 32 px như hàng việc đã ghi. |
| 13 | U2 Icon Tháp Cung | `/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py key-alpha games/typing-defense/art-src/ui/buildings/archer.png games/typing-defense/art-src/ui/buildings/archer.alpha.png --bg auto`<br>`/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py pad-margin games/typing-defense/art-src/ui/buildings/archer.alpha.png games/typing-defense/art-src/ui/buildings/archer.1024.png --size 1024 --margin 10%`<br>`python3 games/dragon-hold/art-src/_review/017/manual-v2.py` (nhánh U2) | `games/typing-defense/art-src/ui/buildings/archer.alpha.png`<br>`games/typing-defense/art-src/ui/buildings/archer.1024.png`<br>`games/typing-defense/art-src/ui/buildings/archer.flag.png` | 1241×1268 RGBA; hai bản sau **1024×1024 RGBA**, góc cả ba **0,0,0,0**. Mask cờ bbox [292,134,398,206], **4281 px**. Mean **213.841, 70.992, 154.964**; so #D9479B=(217,71,155): Δ(**−3,159;−0,008;−0,036**). | **8,5 — Tạm chấp nhận**. | R giảm nhẹ do chặn highlight ở 255 khi giữ nếp vải. Cung chìm ở 32 px còn. |
| 14 | U4 Icon nhà Trại Lính | `/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py key-alpha games/typing-defense/art-src/ui/buildings/barracks.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/barracks.key.png --bg auto`<br>`/opt/homebrew/bin/magick /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/barracks.key.png -trim +repage -strip games/typing-defense/art-src/ui/buildings/barracks.trim.png`<br>`/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py icon games/typing-defense/art-src/ui/buildings/barracks.trim.png games/typing-defense/art-src/ui/buildings/normalized --sizes 256,64` | `games/typing-defense/art-src/ui/buildings/barracks.trim.png`<br>`games/typing-defense/art-src/ui/buildings/normalized/barracks.trim.256.png`<br>`games/typing-defense/art-src/ui/buildings/normalized/barracks.trim.64.png` | Trim **1439×973 RGBA**; icon **256×256/64×64 RGBA**, góc cả ba **0,0,0,0**. Giữ đủ chân và rào, không cắt thân. | **8,5 — Tạm chấp nhận**. | Dáng nhà dài thấp cũ vẫn khác barracks-v2. Không đổi thiết kế hoặc model. |

## Tham số mặt nạ, số lượt, chỗ lệch

- **C21:** key-alpha `--bg '#0000FF' --despill protect-interior`, crop `760x760+280+0`, resize `1024x1024`; alpha morphology `Dilate Disk:3` cho viền #2B211A. Nét cọ #6B3FA0 ở 72 %, path Bézier ghi đủ trong portrait.py, sau vai, không đè mặt. Nền #00FF00 sau khi xem draconis.png và dai-bang-tinh.png. Lượt 2 thêm lót #E6E6E6 đúng hình nét cọ; màu nét sau ghép khác RGB lớp mực, không đánh tráo số.
- **V37 L1:** hộp x=300..470, y=496..643; H=0..65°, S>0,55, R≥150, G≥65. Ánh xạ sáng t về RGB (90+32t,30+12t,20+4t). **L2:** chỉ hai polygon ghi đủ trong retry.py, H<80°, R>70, S>0,22 hoặc V>0,65; `Close Disk:1`, `-blur 0x0.5`. Toàn bộ thay đổi nằm trong hộp. Cả hai còn lỗi nhìn thấy; không có lượt ba.
- **D4:** A>8, H=55..105°, S>0,22; H+12°, V×0,90, giữ S. Tím hồng: R>1,3G, B>1,3G, R>0,75B; A≤230 đặt 0, còn lại lấy màu kề không tím trong bán kính ≤24 px. Dựng mask đầu trong manual.py dừng trước khi xuất D4 tại (697,110), vì chỉ tìm lá xanh. manual-v2.py cho phép màu đá không tím; chỉ một ảnh D4 được xuất. Hai script đều giữ làm bằng chứng, không sửa đè script cũ.
- **D3:** chỉ ô sỏi x<512,y<512; A>8, G>max(R,B)+20. Lấy màu sỏi kề A>240, abs(G−R)<9, B≥G−5, bán kính ≤16 px; giữ alpha. Đổi 33 px thay ước tính khoảng 34, tọa độ đủ trong manual-log.json.
- **I08 L1:** `-modulate 115,105,104` chỉ H=0..45°, S≥0,35, R≥140, G≥60, R>1,2G, G>1,05B. **L2:** vẫn lấy ảnh đã modulate cùng tham số, trộn bằng mask mềm `(1−smoothstep(30,48,H)) × smoothstep(0.28,0.55,S) × smoothstep(110,170,R)`, chỉ R>G>B. Giữ viền nâu tối. RGB đo L2 là trung bình có trọng số mask mềm.
- **U2:** vùng cờ y<350,x<650,A>8,R>1,5G,B>1,4G,R>80. RGB đích (217,71,155) nhân sáng tương đối `(.2126R+.7152G+.0722B)/mean_l`, chặn 255; giữ nếp vải, gây lệch nhỏ kênh R so đích.
- **V18:** câu “viền xanh ... còn” của phiếu khác mô tả “khử loang mặc định xóa viền xanh” trong ART_FIX_QUEUE. Đã chạy đúng lệnh ưu tiên ở hàng việc, không thêm `--despill off`. Giữ được cỏ; viền xanh bó lúa giảm mạnh, cần Claude xác nhận qua số và crop.
- **D2:** nguồn duy nhất `_review/015-flower-clusters.png`, MD5 `17b731314e8c162376ce73dc19fb096d`; không nhầm bản cũ. Ghi nguồn tại báo cáo thay README ngoài danh sách được phép. Không `--no-key-hue`.
- C21/V37/I08 có đúng hai lượt chỉnh ảnh; lượt 2 giữ ở review vì cấm ghi đè tên lượt 1. Các ảnh khác chỉ xuất một lượt. Ảnh đo, mặt nạ, contact sheet không phải lượt tạo lại art.
- Không tạo prompt.txt cạnh ảnh: không sinh AI và tên sidecar không nằm trong cột đầu ra; lệnh công cụ đã lưu trong script và báo cáo.

## Kiểm 3 · Khổ và kênh

Đầu ra `magick identify -format '%f %wx%h %[channels]\n'` cho 23 file yêu cầu và 5 ứng viên lượt 2:

```text
moc-tinh.crop.png 1024x1024 srgb  3.0
gold-mine-lo-duc-tien.coal.png 1024x1024 srgb  3.0
farm-kit-l2.alpha.png 1024x1024 srgba 4.0
seed-drop.flat.png 1024x1024 srgb  3.0
grass-b.hue.png 1254x1254 srgb  3.0
grass-b.1024.png 1024x1024 srgb  3.0
moss.1024.png 1024x1024 srgb  3.0
rock.1024.png 1024x1024 srgb  3.0
moss-puddles.v1.tone.png 1024x1024 srgba 4.0
flower-clusters.015.alpha.png 1254x1254 srgba 4.0
flower-clusters.015.1024.png 1024x1024 srgba 4.0
forest-litter.clean.png 1024x1024 srgba 4.0
hard-scale.warm.png 1254x1254 srgb  3.0
hard-scale.warm.256.png 256x256 srgba 4.0
hard-scale.warm.64.png 64x64 srgba 4.0
015-skill-roar.256.png 256x256 srgba 4.0
015-skill-roar.64.png 64x64 srgba 4.0
archer.alpha.png 1241x1268 srgba 4.0
archer.1024.png 1024x1024 srgba 4.0
archer.flag.png 1024x1024 srgba 4.0
barracks.trim.png 1439x973 srgba 4.0
barracks.trim.256.png 256x256 srgba 4.0
barracks.trim.64.png 64x64 srgba 4.0
moc-tinh.crop.retry.png 1024x1024 srgb  3.0
gold-mine-lo-duc-tien.coal.retry.png 1024x1024 srgb  3.0
hard-scale.warm.retry.png 1254x1254 srgb  3.0
hard-scale.warm.retry.256.png 256x256 srgba 4.0
hard-scale.warm.retry.64.png 64x64 srgba 4.0
```

Ảnh tách nền V18, cả hai D2, ba U2, ba U4 đều có alpha và bốn góc A=0. D4/D3 và mọi bộ icon cũng có bốn góc A=0. Chi tiết từng file trong [verification.json](../../games/dragon-hold/art-src/_review/017/verification.json). [identify-review.txt](../../games/dragon-hold/art-src/_review/017/identify-review.txt) ghi thêm toàn bộ ảnh kiểm/mặt nạ/xem nhanh.

## Kiểm 4 · Mép tile

Đã chạy CLI thuật toán seam-check với `--axis xy --reference` đúng nguồn gốc cho cả ba. Thay wrapper .sh bằng normalizer.py chỉ để đặt WORK trong phạm vi. Đích kiểm đặt trong review thay tên cạnh tile vì cột đầu ra không cho ghi thêm file cạnh tile:

```bash
/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py seam-check games/dragon-hold/art-src/ground/pine-river/grass-b.1024.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/T2.nguon-goc.seam.png --axis xy --reference games/dragon-hold/art-src/ground/pine-river/grass-b.png
/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py seam-check games/dragon-hold/art-src/ground/pine-river/moss.1024.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/T3.nguon-goc.seam.png --axis xy --reference games/dragon-hold/art-src/ground/pine-river/moss.png
/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py seam-check games/dragon-hold/art-src/ground/pine-river/rock.1024.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/T7.nguon-goc.seam.png --axis xy --reference games/dragon-hold/art-src/ground/pine-river/rock.png
```

Cả ba exit 1, chưa tạo được các file `.nguon-goc.seam.png`:

```text
normalize.py, reference_metrics, line 579:
    q = k+length if has_overlap and k<path[y] else k
IndexError: list index out of range
```

Đối chiếu nguồn 1254×1254 với bản 1024×1024 đi vào nhánh overlap không xử lý được chênh khổ này. Không sửa công cụ trong phiếu. seams.py gặp lỗi T2 trước khi xuất; seams-v2.py ghi đủ lỗi cho cả ba. [Log/argv/stdout/stderr nguyên vẹn](../../games/dragon-hold/art-src/_review/017/seam-check-log-v2.json).

MAE đo độc lập trên RGB 0–255: X là cột đầu/cuối, Y là hàng đầu/cuối. Trước là nguồn gốc trong bảng, sau là bản 1024:

| Mã | X trước | X sau | Y trước | Y sau | Kiểm bổ sung cùng khổ |
|---|---:|---:|---:|---:|---|
| T2 | 7.412812 | 8.529948 | 6.688464 | 8.055339 | pass=false, row_streak=false X/Y |
| T3 | 6.538543 | 6.379557 | 6.555290 | 6.505859 | pass=true X/Y |
| T7 | 5.681818 | 5.579753 | 7.016215 | 6.900716 | pass=true X/Y |

Kiểm bổ sung: đổi khổ nguồn bằng `-virtual-pixel tile -filter Lanczos -distort Resize 1024x1024` vào `<mã>.reference-1024.png` trong review; giữ nguyên màu nguồn T2; chạy các lệnh sau:

```bash
/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py seam-check games/dragon-hold/art-src/ground/pine-river/grass-b.1024.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/T2.nguon-cung-kho.seam.png --axis xy --reference /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/T2.reference-1024.png
/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py seam-check games/dragon-hold/art-src/ground/pine-river/moss.1024.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/T3.nguon-cung-kho.seam.png --axis xy --reference /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/T3.reference-1024.png
/Library/Developer/CommandLineTools/usr/bin/python3 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/normalizer.py seam-check games/dragon-hold/art-src/ground/pine-river/rock.1024.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/T7.nguon-cung-kho.seam.png --axis xy --reference /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/T7.reference-1024.png
```

T2 **pass=false dù exit=0**; T3/T7 chỉ pass phép kiểm bổ sung, không được coi là pass với nguồn gốc 1254. Không chạy seamless, không hạ ngưỡng, không chỉnh tương phản ngoài yêu cầu. Đã tự xem vùng nối 1:1 và ghép A/B 2×2.

## Kiểm 5 · Màu đích

Đo bằng ImageMagick trên vùng mask chọn: tắt alpha, nhân mask, lấy mean.r/g/b rồi chia mean mask. Với mask mềm, đây là trung bình có trọng số. Ví dụ nguyên argv V37 L1:

```bash
/opt/homebrew/bin/magick games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.coal.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/V37.mask.png -alpha off -compose Multiply -composite -format '%[fx:mean.r*255/0.00867271000000],%[fx:mean.g*255/0.00867271000000],%[fx:mean.b*255/0.00867271000000]' info:
/opt/homebrew/bin/magick games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.coal.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/017/V37.mask.png -alpha off -compose Multiply -composite -colorspace Gray -format '%[fx:mean*100/0.00867271000000]' info:
```

Độ sáng là `-colorspace Gray` và mean×100/mean_mask; không dùng HSV V (khoảng than chỉ định tự có HSV V khoảng 35–48 %). Mọi argv và số đo nằm trong verification.json mục colors.

| Vùng | RGB trung bình magick | Điều kiện / đối chiếu |
|---|---|---|
| C21-lop-muc | 107.000, 63.000, 160.000 | Đúng #6B3FA0; alpha 72,16 % |
| C21-lan1 | 77.206, 116.459, 115.451 | Nền xanh pha xỉn, không chọn |
| C21-lan2 | 141.245, 109.498, 179.490 | Sau lót giấy, thấy tím; khác RGB lớp mực |
| V37-lan1 | 105.151, 35.683, 21.904 | Sáng 19,3964 % ≤35 %, vẫn không đạt thị giác |
| V37-lan2 | 106.388, 36.792, 21.996 | Sáng 19,8135 % ≤35 %, còn viền sáng |
| I08-lan1 | 239.257, 166.033, 115.928 | So #E58A5F, quá sáng và ranh gắt |
| I08-lan2 | 232.544, 147.633, 99.172 | So #E58A5F: Δ(+3,544;+9,633;+4,172) |
| U2 | 213.841, 70.992, 154.964 | So #D9479B: Δ(−3,159;−0,008;−0,036) |

## Kiểm 1 · Nguồn không đổi

`md5 -r` ghi đủ 14 ảnh trước/sau trong [md5-before.txt](../../games/dragon-hold/art-src/_review/017/md5-before.txt), [md5-after.txt](../../games/dragon-hold/art-src/_review/017/md5-after.txt). Đã đọc và đo lại nguồn ngay lúc viết báo cáo: cùng kết quả. Đầu ra trước (sau giống từng byte):

```text
d21762eca5d8089a4a3d05d158d72a8e games/typing-defense/art-src/portraits/moc-tinh.png
7049d4ca821e9b4b7f7127461a9baf4d games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.png
8c376731c3103bf63d2f240f88c93d7e games/typing-defense/art-src/kits/farm-kit-l2.png
877f19f55b618bc8f32d8be9d29c3955 games/typing-defense/art-src/projectiles/seed-drop.png
a8ebe47d53af7a58f51052b60bf7b0f5 games/dragon-hold/art-src/ground/pine-river/grass-b.png
0c053f350973d4955312b2541a7533fa games/dragon-hold/art-src/ground/pine-river/moss.png
77dbf8d6af2f7538c58ff2c7837d0543 games/dragon-hold/art-src/ground/pine-river/rock.png
36d4be0444f1aaa1f4f2adcd2b53fcf0 games/dragon-hold/art-src/decals/pine-river/moss-puddles.v1.alpha.png
17b731314e8c162376ce73dc19fb096d games/dragon-hold/art-src/_review/015-flower-clusters.png
995b00a9e70d619dee7bdb42b981f3fb games/dragon-hold/art-src/decals/pine-river/forest-litter.alpha.png
d3c43fbc0c0cb7edc72983974815de2d games/dragon-hold/art-src/ui/icons/hard-scale.png
81208b384a9cd0c3382cecffe9c38202 games/dragon-hold/art-src/_review/015-skill-roar.png
86252fa2175a2b2a1a54ff51cc0b42d5 games/typing-defense/art-src/ui/buildings/archer.png
3211b6f44325c4f021873a1a29cd3e6e games/typing-defense/art-src/ui/buildings/barracks.png
```

```text
$ diff games/dragon-hold/art-src/_review/017/md5-before.txt games/dragon-hold/art-src/_review/017/md5-after.txt
[stdout rỗng, stderr rỗng, exit 0]
```

## Kiểm 2 · Phạm vi file mới, không ghi đè

Các writer art-normalize có output_guard và công bố độc quyền. Đích magick được kiểm chưa tồn tại; text mở exclusive `open(..., 'x')`. Tên lượt sau khác lượt trước; không thay/xóa ảnh đã có. Thư mục 017 và hai tờ tổng chưa tồn tại khi bắt đầu.

**Bản kê phiếu 017 đầu tiên: 154/154 hợp lệ, unexpected=[]**, được lưu tại [find-new.txt](../../games/dragon-hold/art-src/_review/017/find-new.txt), [boundary-check.json](../../games/dragon-hold/art-src/_review/017/boundary-check.json). Không có file lạ do phiếu 017 tạo.

Lệnh find nguyên văn chạy lại lúc chốt báo cáo trả cả file công việc đồng thời mới xuất hiện. Bản kê sau đây là đầu ra thực tế, không lọc:

```text
$ find games/*/art-src -newer games/dragon-hold/art-src/_review/017/md5-before.txt -type f
games/dragon-hold/art-src/ui/icons/hard-scale.warm.png
games/dragon-hold/art-src/ground/pine-river/moss.try1.png
games/dragon-hold/art-src/ground/pine-river/moss.1024.png
games/dragon-hold/art-src/ground/pine-river/grass-b.hue.png
games/dragon-hold/art-src/ground/pine-river/grass-b.1024.png
games/dragon-hold/art-src/ground/pine-river/rock.1024.png
games/dragon-hold/art-src/ground/pine-river/moss.try1.prompt.txt
games/dragon-hold/art-src/_review/017-dh.jpg
games/dragon-hold/art-src/_review/017/T2.cell-2.png
games/dragon-hold/art-src/_review/017/identify-review.txt
games/dragon-hold/art-src/_review/017/V18-grass.compare.jpg
games/dragon-hold/art-src/_review/017/I08.row.png
games/dragon-hold/art-src/_review/017/sources.json
games/dragon-hold/art-src/_review/017/T2.nguon-goc.log.txt
games/dragon-hold/art-src/_review/017/hard-scale.warm.retry.png
games/dragon-hold/art-src/_review/017/U2.mask.png
games/dragon-hold/art-src/_review/017/T2.cell-1.png
games/dragon-hold/art-src/_review/017/T7.reference-1024.png
games/dragon-hold/art-src/_review/017/T7.nguon-cung-kho.seam.png
games/dragon-hold/art-src/_review/017/I08.mask.png
games/dragon-hold/art-src/_review/017/T2.cell-0.png
games/dragon-hold/art-src/_review/017/U4.row.png
games/dragon-hold/art-src/_review/017/I11.row.png
games/dragon-hold/art-src/_review/017/T7.nguon-goc.log.txt
games/dragon-hold/art-src/_review/017/I08-retry.mask.png
games/dragon-hold/art-src/_review/017/seams-v2.py
games/dragon-hold/art-src/_review/017/gold-mine-lo-duc-tien.coal.retry.png
games/dragon-hold/art-src/_review/017/sources.jpg
games/dragon-hold/art-src/_review/017/T2.nguon-cung-kho.log.txt
games/dragon-hold/art-src/_review/017/T7.cell-1.png
games/dragon-hold/art-src/_review/017/seam-check-log-v2.json
games/dragon-hold/art-src/_review/017/T7.cell-0.png
games/dragon-hold/art-src/_review/017/T3.nguon-goc.log.txt
games/dragon-hold/art-src/_review/017/V69.row.png
games/dragon-hold/art-src/_review/017/grass-a.1024.png
games/dragon-hold/art-src/_review/017/find-new.txt
games/dragon-hold/art-src/_review/017/sheets.py
games/dragon-hold/art-src/_review/017/T7.cell-2.png
games/dragon-hold/art-src/_review/017/D4-pink.mask.png
games/dragon-hold/art-src/_review/017/C21-underpaint.png
games/dragon-hold/art-src/_review/017/T3.nguon-cung-kho.seam.png
games/dragon-hold/art-src/_review/017/portrait.py
games/dragon-hold/art-src/_review/017/D2.cell-1.png
games/dragon-hold/art-src/_review/017/T3.tile-2x2.png
games/dragon-hold/art-src/_review/017/V37.cell-2.png
games/dragon-hold/art-src/_review/017/T7.row.png
games/dragon-hold/art-src/_review/017/standard.py
games/dragon-hold/art-src/_review/017/I11.cell-2.png
games/dragon-hold/art-src/_review/017/C21.cell-2.png
games/dragon-hold/art-src/_review/017/D2.row.png
games/dragon-hold/art-src/_review/017/D2.cell-0.png
games/dragon-hold/art-src/_review/017/D2.cell-2.png
games/dragon-hold/art-src/_review/017/C21.cell-0.png
games/dragon-hold/art-src/_review/017/V37.cell-1.png
games/dragon-hold/art-src/_review/017/output-manifest.json
games/dragon-hold/art-src/_review/017/I11.cell-0.png
games/dragon-hold/art-src/_review/017/hard-scale.modulated.png
games/dragon-hold/art-src/_review/017/T7.seam-center.png
games/dragon-hold/art-src/_review/017/T3.nguon-cung-kho.log.txt
games/dragon-hold/art-src/_review/017/T2.reference-1024.png
games/dragon-hold/art-src/_review/017/I11.cell-1.png
games/dragon-hold/art-src/_review/017/C21.mask.png
games/dragon-hold/art-src/_review/017/V37.cell-0.png
games/dragon-hold/art-src/_review/017/C21.cell-1.png
games/dragon-hold/art-src/_review/017/U4.cell-2.png
games/dragon-hold/art-src/_review/017/I08.cell-1.png
games/dragon-hold/art-src/_review/017/I08.cell-0.png
games/dragon-hold/art-src/_review/017/T2.tile-2x2.png
games/dragon-hold/art-src/_review/017/boundary-check.json
games/dragon-hold/art-src/_review/017/U4.cell-1.png
games/dragon-hold/art-src/_review/017/V37.row.png
games/dragon-hold/art-src/_review/017/manual.py
games/dragon-hold/art-src/_review/017/I08.cell-2.png
games/dragon-hold/art-src/_review/017/barracks.key.png
games/dragon-hold/art-src/_review/017/retry-log.json
games/dragon-hold/art-src/_review/017/U4.cell-0.png
games/dragon-hold/art-src/_review/017/V18.row.png
games/dragon-hold/art-src/_review/017/hard-scale.warm.retry.64.png
games/dragon-hold/art-src/_review/017/D3.row.png
games/dragon-hold/art-src/_review/017/T7.nguon-cung-kho.log.txt
games/dragon-hold/art-src/_review/017/C21-outline.png
games/dragon-hold/art-src/_review/017/D2.on-grass.png
games/dragon-hold/art-src/_review/017/V37-retry.mask.png
games/dragon-hold/art-src/_review/017/T2.nguon-cung-kho.seam.png
games/dragon-hold/art-src/_review/017/T3.row.png
games/dragon-hold/art-src/_review/017/retry.py
games/dragon-hold/art-src/_review/017/manual-v2.py
games/dragon-hold/art-src/_review/017/D4.cell-2.png
games/dragon-hold/art-src/_review/017/D4-moss.mask.png
games/dragon-hold/art-src/_review/017/manual-log.json
games/dragon-hold/art-src/_review/017/V69.cell-2.png
games/dragon-hold/art-src/_review/017/T7.tile-2x2.png
games/dragon-hold/art-src/_review/017/V69.cell-0.png
games/dragon-hold/art-src/_review/017/md5-after.txt
games/dragon-hold/art-src/_review/017/D4.cell-0.png
games/dragon-hold/art-src/_review/017/D4.cell-1.png
games/dragon-hold/art-src/_review/017/tile-seams-1to1.jpg
games/dragon-hold/art-src/_review/017/V69.cell-1.png
games/dragon-hold/art-src/_review/017/seams.py
games/dragon-hold/art-src/_review/017/U2.cell-0.png
games/dragon-hold/art-src/_review/017/T3.cell-2.png
games/dragon-hold/art-src/_review/017/moc-tinh.crop.retry.png
games/dragon-hold/art-src/_review/017/moc-tinh.bust.png
games/dragon-hold/art-src/_review/017/identify-outputs.txt
games/dragon-hold/art-src/_review/017/D4.on-grass.png
games/dragon-hold/art-src/_review/017/U2.cell-1.png
games/dragon-hold/art-src/_review/017/D3.on-grass.png
games/dragon-hold/art-src/_review/017/moc-tinh.key.png
games/dragon-hold/art-src/_review/017/standard-log.json
games/dragon-hold/art-src/_review/017/T2.seam-center.png
games/dragon-hold/art-src/_review/017/T3.reference-1024.png
games/dragon-hold/art-src/_review/017/U2.row.png
games/dragon-hold/art-src/_review/017/T2.row.png
games/dragon-hold/art-src/_review/017/C21-brush.png
games/dragon-hold/art-src/_review/017/T3.cell-1.png
games/dragon-hold/art-src/_review/017/V18-wheat.compare.jpg
games/dragon-hold/art-src/_review/017/D3.mask.png
games/dragon-hold/art-src/_review/017/V37.mask.png
games/dragon-hold/art-src/_review/017/T3.cell-0.png
games/dragon-hold/art-src/_review/017/U2.cell-2.png
games/dragon-hold/art-src/_review/017/hard-scale.warm.retry.256.png
games/dragon-hold/art-src/_review/017/verification.json
games/dragon-hold/art-src/_review/017/V18.cell-0.png
games/dragon-hold/art-src/_review/017/T3.seam-center.png
games/dragon-hold/art-src/_review/017/V18.cell-1.png
games/dragon-hold/art-src/_review/017/verify.py
games/dragon-hold/art-src/_review/017/normalizer.py
games/dragon-hold/art-src/_review/017/C21.row.png
games/dragon-hold/art-src/_review/017/V18.cell-2.png
games/dragon-hold/art-src/_review/017/V37-retry.mask.raw.png
games/dragon-hold/art-src/_review/017/diff-md5.txt
games/dragon-hold/art-src/_review/017/C21-dilated.png
games/dragon-hold/art-src/_review/017/D4.row.png
games/dragon-hold/art-src/_review/017/portrait-log.json
games/dragon-hold/art-src/_review/017/D3.cell-1.png
games/dragon-hold/art-src/_review/017/D3.cell-0.png
games/dragon-hold/art-src/_review/017/D3.cell-2.png
games/dragon-hold/art-src/icons/normalized/015-skill-roar.64.png
games/dragon-hold/art-src/icons/normalized/hard-scale.warm.256.png
games/dragon-hold/art-src/icons/normalized/hard-scale.warm.64.png
games/dragon-hold/art-src/icons/normalized/015-skill-roar.256.png
games/dragon-hold/art-src/decals/pine-river/moss-puddles.v1.tone.png
games/dragon-hold/art-src/decals/pine-river/flower-clusters.015.alpha.png
games/dragon-hold/art-src/decals/pine-river/flower-clusters.015.1024.png
games/dragon-hold/art-src/decals/pine-river/forest-litter.clean.png
games/typing-defense/art-src/ui/buildings/barracks.trim.png
games/typing-defense/art-src/ui/buildings/normalized/barracks.trim.64.png
games/typing-defense/art-src/ui/buildings/normalized/barracks.trim.256.png
games/typing-defense/art-src/ui/buildings/archer.alpha.png
games/typing-defense/art-src/ui/buildings/archer.1024.png
games/typing-defense/art-src/ui/buildings/archer.flag.png
games/typing-defense/art-src/scenery/coast/olive-tree-v2.try1.prompt.txt
games/typing-defense/art-src/scenery/coast/casuarina-v2.try1.prompt.txt
games/typing-defense/art-src/kits/farm-kit-l2.alpha.png
games/typing-defense/art-src/_review/017-td.jpg
games/typing-defense/art-src/_review/020/generation-plan.json
games/typing-defense/art-src/_review/020/ground-reference.jpg
games/typing-defense/art-src/_review/020/md5-before.txt
games/typing-defense/art-src/_review/020/coast-reference.jpg
games/typing-defense/art-src/_review/020/portraits-reference.jpg
games/typing-defense/art-src/_review/020/barracks-reference.jpg
games/typing-defense/art-src/_review/020/inventory-before.json
games/typing-defense/art-src/portraits/lam.try1.prompt.txt
games/typing-defense/art-src/portraits/draconis-ult.try1.prompt.txt
games/typing-defense/art-src/portraits/tre-ult.try1.prompt.txt
games/typing-defense/art-src/portraits/tre.try1.prompt.txt
games/typing-defense/art-src/portraits/moc-tinh.crop.png
games/typing-defense/art-src/portraits/lam.try1.png
games/typing-defense/art-src/portraits/draconis-ult.try1.png
games/typing-defense/art-src/branches/barracks-giao-dai.try1.prompt.txt
games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.coal.png
games/typing-defense/art-src/projectiles/seed-drop.flat.png
```

```text
file_017_trong_ban_ke_goc=154
file_017_ngoai_pham_vi=0
tong_find_luc_chot=172
file_phat_sinh_dong_thoi_ngoai_017=18
source_hash_diff_empty=true
```

Các file phát sinh sau bản kê sạch 017, **không do phiếu này tạo, không xóa** vì chủ dự án đã báo có agent khác làm đồng thời và cấm sửa ngoài phạm vi:

```text
games/dragon-hold/art-src/ground/pine-river/moss.try1.png
games/dragon-hold/art-src/ground/pine-river/moss.try1.prompt.txt
games/typing-defense/art-src/_review/020/barracks-reference.jpg
games/typing-defense/art-src/_review/020/coast-reference.jpg
games/typing-defense/art-src/_review/020/generation-plan.json
games/typing-defense/art-src/_review/020/ground-reference.jpg
games/typing-defense/art-src/_review/020/inventory-before.json
games/typing-defense/art-src/_review/020/md5-before.txt
games/typing-defense/art-src/_review/020/portraits-reference.jpg
games/typing-defense/art-src/branches/barracks-giao-dai.try1.prompt.txt
games/typing-defense/art-src/portraits/draconis-ult.try1.png
games/typing-defense/art-src/portraits/draconis-ult.try1.prompt.txt
games/typing-defense/art-src/portraits/lam.try1.png
games/typing-defense/art-src/portraits/lam.try1.prompt.txt
games/typing-defense/art-src/portraits/tre-ult.try1.prompt.txt
games/typing-defense/art-src/portraits/tre.try1.prompt.txt
games/typing-defense/art-src/scenery/coast/casuarina-v2.try1.prompt.txt
games/typing-defense/art-src/scenery/coast/olive-tree-v2.try1.prompt.txt
```

Vì vậy **kiểm 2 riêng phiếu 017 sạch; đầu ra find toàn repo lúc chốt không chỉ còn file 017**. Không tuyên bố đã xóa các file đó hoặc toàn cây chỉ chứa đầu ra phiếu. Báo cáo này là file docs được phép riêng, không nằm trong cây find art-src. Lệnh find chỉ đọc danh sách, không chỉnh game khác.

## Cần chủ dự án/Claude xem

V37 chưa dùng gửi Tripo. Xem T2 vì chốt seam tổng chưa đạt và ba lỗi reference khác khổ; sửa công cụ thuộc phiếu riêng. Duyệt bản retry của C21/I08 trước khi nhập tên dùng trong game. Xem crop V18 để chốt giữ/xóa viền xanh. Kiểm 1 sạch; kiểm 2 toàn cây cần xét riêng các file đồng thời liệt kê trên. Không thay ảnh runtime, cập nhật danh sách hoặc đụng model 3D trong phiếu này.
