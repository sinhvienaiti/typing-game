# Phiếu 148 · Dragonhold · Chân dung quái và vải cờ

Ngày tiếp tục và bàn giao: **30/10/2026**, macOS, repo cha. **Đủ bộ ứng viên 8 ảnh + 24 bản thu; chưa đủ điều kiện nhận toàn phiếu.** `thorn-ant` còn thiếu tương phản trên nền tối: **0,202410 < 0,25**. Lệnh sinh sửa bằng `image_gen` tích hợp bị trả **429 / `usage_limit_reached`**; không có ảnh mới từ lệnh này. Giữ tranh theo `ART_ACCEPTANCE.md` §5, không tăng sáng quá giới hạn để ép đạt số.

## 1. Bộ giao và phần giữ nguyên

Đầu lượt này đã có **13 PNG lượt sinh**, các prompt, ba bộ chân dung mang tên bản chọn và nhiều ứng viên hậu kỳ. Đã tiếp tục từ những tệp đó, không sinh lại cả bộ, không ghi đè, đổi tên hay xóa tệp có sẵn.

**Bộ cuối để Claude chấm và chọn khi gắn:** [delivery-final/](../../games/dragon-hold/art-src/_review/148/resume-20261030/delivery-final/). Mỗi tên có `.png`, `.256.png`, `.128.png`, `.64.png` và prompt nguyên văn cạnh từng tệp. Tổng **32 PNG + 32 prompt**. Bảy chân dung gốc 1024 × 1024; vải cờ gốc **1024 × 1536**, theo ngoại lệ riêng của phiếu. Bản thu đều là ô vuông đúng cỡ, giữ tỉ lệ và thêm lề alpha, không kéo méo vải.

| Tên | Lượt chọn | Bản gốc cuối |
|---|---:|---|
| moss-grunt | 1 | [PNG](../../games/dragon-hold/art-src/_review/148/resume-20261030/delivery-final/moss-grunt.png) |
| moss-archer | 2 | [PNG](../../games/dragon-hold/art-src/_review/148/resume-20261030/delivery-final/moss-archer.png) |
| blight-wolf | 1 | [PNG](../../games/dragon-hold/art-src/_review/148/resume-20261030/delivery-final/blight-wolf.png) |
| tusk-boar | 2 | [PNG](../../games/dragon-hold/art-src/_review/148/resume-20261030/delivery-final/tusk-boar.png) |
| thorn-wasp | 1 | [PNG](../../games/dragon-hold/art-src/_review/148/resume-20261030/delivery-final/thorn-wasp.png) |
| thorn-ant | 2 | [PNG](../../games/dragon-hold/art-src/_review/148/resume-20261030/delivery-final/thorn-ant.png) |
| moss-banner | 2 | [PNG](../../games/dragon-hold/art-src/_review/148/resume-20261030/delivery-final/moss-banner.png) |
| banner-cloth | 2 | [PNG](../../games/dragon-hold/art-src/_review/148/resume-20261030/delivery-final/banner-cloth.png) |

Đã bổ sung các tên bản chọn còn thiếu trong `art-src/ui/portraits/`: `tusk-boar`, `thorn-wasp`, `thorn-ant`, `moss-banner`; và `art-src/ui/banners/banner-cloth`, cùng ba bản thu và prompt. **Ba bộ tên cũ `moss-grunt`, `moss-archer`, `blight-wolf` được giữ nguyên**, dù còn lỗi alpha hoặc dùng ứng viên cũ. Các bản thu bổ sung ban đầu cũng được giữ sau khi phát hiện alpha dư do Lanczos. Vì luật cấm ghi đè, bộ đã kiểm sạch thống nhất nằm trong `delivery-final/`; không lấy lẫn tệp từ các bộ trung gian.

## 2. Prompt và các lượt

Prompt dùng khối **STYLE-UI nguyên văn của phiếu 119**, thêm KIND `PORTRAIT` hoặc `PART`, nhận diện từ ảnh nguồn M0b và dòng nền M/G. Đã xem tờ nguồn gồm toàn bộ quái, các góc trước/bên bắt buộc, hai icon `skill-fire-breath`, `gold`, huy hiệu 119 và HUD trong ảnh tham chiếu của chủ dự án. Giữ mặt gỗ, mắt vàng xanh, đá nứt, màu lông/chitin và các nét riêng của từng loài. Không vẽ thêm khung hay vương miện vào chân dung tướng.

| Ảnh | Lượt 1 | Sửa ở lượt 2 | Lượt 3 |
|---|---|---|---|
| moss-grunt | Mặt gỗ vuông, hai lá rộng, nấm kem, vai đá; nền M | Không cần | — |
| moss-archer | Mũ lá nhọn, cung, tên và khăn tím; nền M | Yêu cầu mặt gỗ lớn sáng hơn, bóng trong mũ mở, luma khoảng 0,44 | — |
| blight-wolf | Đầu sói nghiêng trái, mõm kem dài, cổ lông sáng, giáp đá; nền M | Không cần | — |
| tusk-boar | Nhận diện lợn rừng và hai nanh; bố cục còn rộng | Khóa riêng đầu và cổ, bỏ bố cục toàn thân, hai nanh chiếm ưu thế | — |
| thorn-wasp | Cơ thể bay, cánh tím mở chữ V, bụng nhọn và sáu chân; nền G | Không cần | — |
| thorn-ant | Kiến đứng đất, sáu chân, râu gập, bụng giáp; nền M | Mở ánh sáng toàn thân, chitin caramel và giáp tro sáng; vẫn tối hơn yêu cầu | Đã gửi prompt tăng các mảng sáng mật ong và đá tro, mục tiêu luma 0,46. Công cụ từ chối do hạn mức, **không sinh PNG** |
| moss-banner | Mặt gỗ dài, chạc cây, vai rêu và cờ lá; nền M | Mở ánh sáng trên đầu, tay, rêu, giáp, giữ nguyên nhận diện | — |
| banner-cloth | Vải tro, viền vàng úa, ấn mắt tím, mép rách; nền G | Vải tro bạc sáng hơn, nếp nông, ấn mắt có lòng tím nhạt và đồng tử sẫm; sợi vải rõ hơn | — |

Các lượt 1–2 ở trên đã có trước lượt tiếp tục này; đối chiếu bằng prompt cạnh `.tryN.png`. [Prompt kiến lượt 3](../../games/dragon-hold/art-src/ui/portraits/thorn-ant.try3.prompt.txt) được lưu nguyên văn dù lệnh thất bại; [nhật ký lỗi](../../games/dragon-hold/art-src/_review/148/resume-20261030/generation-failure.json) phân biệt rõ lần yêu cầu thất bại với ảnh sinh thành công. Không dùng API/CLI hoặc dịch vụ khác thay công cụ tích hợp.

## 3. Hậu kỳ và bảo toàn tranh

Tách khóa M/G bằng bản `art-normalize` đã lưu trong review; cắt riêng lề trống, giữ sợi/mép có alpha, thu đồng dạng và đặt tâm để cạnh dài hộp bao khoảng 70%. Không cắt bỏ vật, san phẳng, đè màu hoặc làm nét bản 64.

Các bước sáng toàn ảnh đã có trong hồ sơ ứng viên: lợn rừng nhân RGB **1,1**; tướng **1,084186** ở bước chọn, bước cuối không đổi RGB thực tế do làm tròn 8 bit. Những ảnh khác giữ độ sáng. Không dùng gamma hay chỉnh sáng cục bộ. Riêng kiến, tăng tối đa 10% vẫn chỉ cho chênh luma khoảng **0,236**, chưa đủ 0,25; giữ bản đẹp hiện có và ghi thiếu, không tiếp tục ép sáng.

Làm tròn alpha dư ngoài dải mép 3 px ở bản gốc: số pixel của tám ảnh theo thứ tự bảng giao là **91, 65, 123, 229, 28, 69, 91, 302**; gồm bước chọn và hoàn thiện. RGB không đổi ở bước này. Khử sắc khóa còn sót **chỉ ở mép 3 px** của kiến **769 pixel**, vải cờ **1.263 pixel**, giữ nguyên alpha và mọi pixel bên trong; không thay bằng màu lấy từ vùng vẽ khác. [Nhật ký từng pixel](../../games/dragon-hold/art-src/_review/148/resume-20261030/edge-cleaning.json).

Ba bản thu lấy bằng **Lanczos trực tiếp từ bản gốc**, không thu nối tiếp. Sau đó chỉ làm tròn alpha ngoài dải mép 3 px; **RGB và mặt nạ alpha ≥128 giữ nguyên**. [Nhật ký alpha bản thu](../../games/dragon-hold/art-src/_review/148/resume-20261030/reduction-alpha-cleaning.json) lưu tọa độ, alpha trước/sau của từng pixel. Số pixel sửa ở 256/128/64 lần lượt: grunt **35/19/11**, archer **63/26/5**, wolf **63/29/6**, boar **64/22/2**, wasp **26/12/4**, ant **7/5/10**, bannerman **63/22/19**, cloth **68/30/28**.

Đã xem đủ tám PNG hậu kỳ ở khổ đầy đủ, tám tờ trước/sau và tờ cỡ trong game. Vết vẽ, nếp vải, mắt, chân và cánh được giữ; không thấy phần vẽ bị phủ hoặc san phẳng.

## 4. KA1 và số đo

`md5 -r` trên toàn bộ tệp trong hai thư mục đích UI:

- [Trước toàn phiếu](../../games/dragon-hold/art-src/_review/148/md5-before.txt): **32 tệp**; [sau](../../games/dragon-hold/art-src/_review/148/md5-after.txt): **123 tệp**, **91 thêm, 0 sửa, 0 mất**.
- [Trước lượt tiếp tục](../../games/dragon-hold/art-src/_review/148/resume-20261030/md5-before.txt): **82 tệp**; sau **123**, **41 thêm, 0 sửa, 0 mất**. Gồm 40 tệp giao còn thiếu và một prompt kiến lượt 3.
- [Diff toàn phiếu](../../games/dragon-hold/art-src/_review/148/resume-20261030/md5-original-diff.txt), [diff lượt tiếp tục](../../games/dragon-hold/art-src/_review/148/resume-20261030/md5-diff.txt): chỉ có dòng nội dung thêm. [MD5 bộ cuối](../../games/dragon-hold/art-src/_review/148/resume-20261030/md5-delivery-final.txt) ghi riêng media review.

Khổ và kênh: **32/32 đúng**, `srgba`; [kết quả identify nguyên văn](../../games/dragon-hold/art-src/_review/148/resume-20261030/identify-final.txt). Bản gốc alpha min/max **0/255**. Dải mép lấy từ mặt nạ alpha ≥128, giãn/co `Disk:3`; sắc khóa xét hue lệch ≤15°, S >0,5, mẫu số là số pixel alpha >0. Luma dùng hệ số Rec.709 trên RGB sRGB 0–1, trung bình có trọng số alpha. Các số dưới đây là **bộ `delivery-final/`**.

| Ảnh | Cạnh dài bbox % | Lệch tâm x/y % | Alpha lẻ ngoài 3 px, cả 4 cỡ | Sắc khóa gốc % | Sắc khóa lớn nhất cả 4 cỡ % | Δ luma tối / kem |
|---|---:|---:|---:|---:|---:|---:|
| moss-grunt | 70,020 | 0 / 0,049 | 0 | 0,051055 | 0,051055 | 0,277863 / 0,480028 |
| moss-archer | 70,020 | 0 / 0,049 | 0 | 0,051090 | 0,073584 | 0,283060 / 0,474831 |
| blight-wolf | 70,020 | 0 / 0,049 | 0 | 0,082829 | 0,082829 | 0,303465 / 0,454426 |
| tusk-boar | 70,020 | 0 / 0,049 | 0 | 0,058937 | 0,058937 | 0,251038 / 0,506853 |
| thorn-wasp | 70,020 | 0,049 / 0 | 0 | 0,078162 | 0,078162 | 0,319086 / 0,438804 |
| thorn-ant | 70,020 | 0,049 / 0,049 | 0 | 0,001254 | 0,158353 | **0,202410** / 0,555480 |
| moss-banner | 70,020 | 0,049 / 0,049 | 0 | 0,062779 | 0,062779 | 0,253558 / 0,504332 |
| banner-cloth | 69,987 | 0 / 0,033 | 0 | 0,008086 | 0,155340 | 0,369888 / 0,388002 |

Tất cả qua alpha, sắc khóa ≤0,2%, bbox 68–72% và lệch tâm ≤2%. **Chỉ kiến không qua tương phản nền tối**. Nền kem không được dùng để thay điều kiện nền tối. [Số đo gốc và ma trận IoU](../../games/dragon-hold/art-src/_review/148/resume-20261030/measurements.json), [đo sạch cả 32 PNG cuối](../../games/dragon-hold/art-src/_review/148/resume-20261030/all-size-final.json).

| Ảnh | IoU lớn nhất ở 32 px · cặp | IoU lớn nhất ở 22 px · cặp |
|---|---|---|
| moss-grunt | 0,727273 · moss-archer | 0,730570 · moss-archer |
| moss-archer | 0,727273 · moss-grunt | 0,743316 · moss-banner |
| blight-wolf | 0,758621 · tusk-boar | 0,747368 · tusk-boar |
| tusk-boar | 0,758621 · blight-wolf | 0,747368 · blight-wolf |
| thorn-wasp | 0,506234 · tusk-boar | 0,502488 · tusk-boar |
| thorn-ant | 0,641791 · tusk-boar | 0,705584 · tusk-boar |
| moss-banner | 0,714646 · moss-archer | 0,743316 · moss-archer |
| banner-cloth | 0,559271 · blight-wolf | Không áp dụng |

Mặt nạ thu Lanczos trực tiếp từ gốc, alpha >16, giữ vị trí trên ô vuông; mọi cặp đạt ≤0,80. Riêng wasp/ant: **0,478022 ở 32 px**, **0,478723 ở 22 px**; cánh mở và chân đứng đất phân biệt rõ. Không có cặp sáng/tắt trong phiếu.

## 5. Tờ xem và KA5

[Tờ xem đúng tên phiếu](../../games/dragon-hold/art-src/_review/148-sheet.jpg) giữ bản bố cục đầu. [Tờ xem cuối](../../games/dragon-hold/art-src/_review/148-sheet-final.jpg) bổ sung cờ ở **chiều cao vật nhìn thấy 90/60 px** và bốn icon có sẵn cùng mảnh HUD tham chiếu trong ô 256 px. Không ghi đè tờ đầu. Bảy chân dung ở 34/115 và 22/77 px trên cả `#2b2118`, `#f1e3c4`. Tờ này thu trực tiếp từ các bản gốc cuối; các bản gốc giữa `delivery/` và `delivery-final/` giống hệt nhau.

Tám tờ “bản sinh | bản hậu kỳ”, mỗi phía cùng cỡ hiển thị toàn canvas, dùng đúng lượt chọn:
[grunt](../../games/dragon-hold/art-src/_review/148/resume-20261030/moss-grunt-before-after.jpg),
[archer](../../games/dragon-hold/art-src/_review/148/resume-20261030/moss-archer-before-after.jpg),
[wolf](../../games/dragon-hold/art-src/_review/148/resume-20261030/blight-wolf-before-after.jpg),
[boar](../../games/dragon-hold/art-src/_review/148/resume-20261030/tusk-boar-before-after.jpg),
[wasp](../../games/dragon-hold/art-src/_review/148/resume-20261030/thorn-wasp-before-after.jpg),
[ant](../../games/dragon-hold/art-src/_review/148/resume-20261030/thorn-ant-before-after.jpg),
[bannerman](../../games/dragon-hold/art-src/_review/148/resume-20261030/moss-banner-before-after.jpg),
[cloth](../../games/dragon-hold/art-src/_review/148/resume-20261030/banner-cloth-before-after.jpg).

[Cờ trên mảnh cảnh nguồn, 60 và 90 px](../../games/dragon-hold/art-src/_review/148/resume-20261030/banner-cloth-scene-detail.jpg): cắt nguyên tỉ lệ một cảnh từ `sheet-12-heo-lan-hp-loss-1280.jpg`, không phóng đại cảnh, ghép cờ sau trim lề alpha. Ở 60 px còn thấy rõ hình mắt và đồng tử sẫm. Đây là ảnh ghép kiểm đọc, chưa phải texture đã tích hợp vào game. Cũng giữ hai bản ghép trên [toàn tờ nguồn 60 px](../../games/dragon-hold/art-src/_review/148/resume-20261030/banner-scene-60.jpg) và [90 px](../../games/dragon-hold/art-src/_review/148/resume-20261030/banner-scene-90.jpg).

Điểm tự chấm **trên bản hậu kỳ**, so mức hoàn thiện UI game thương mại và ảnh chủ dự án; chưa phải điểm nhận của Claude. Thứ tự năm điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**. Hợp bộ 1,5 vì cách dựng khối còn hơi faceted, chất liệu chưa đạt độ trau chuốt của UI tham chiếu. Ở chip nhỏ, mất chi tiết phụ nhưng nét phân loài còn rõ.

| Ảnh | Cỡ gốc: năm điểm → tổng | Cỡ 720p: năm điểm → tổng | Chỗ cần nhìn khi duyệt |
|---|---|---|---|
| moss-grunt | 2/2/1,5/2/2 → **9,5** | 2/1/1,5/2/2 → **8,5** | Lá và mặt gỗ còn rõ; dao và rêu dày ở 22 px |
| moss-archer | 2/2/1,5/2/2 → **9,5** | 2/1,5/1,5/2/2 → **9** | Mũ nhọn, cung/tên khác dáng grunt |
| blight-wolf | 2/2/1,5/2/2 → **9,5** | 2/2/1,5/2/2 → **9,5** | Mõm nghiêng và cổ kem đọc tốt |
| tusk-boar | 2/2/1,5/2/2 → **9,5** | 2/1,5/1,5/2/2 → **9** | Hai nanh và mũi bẹt; tương phản tối sát ngưỡng |
| thorn-wasp | 2/2/1,5/2/2 → **9,5** | 2/1,5/1,5/2/2 → **9** | Cánh chữ V phân biệt rõ kiến |
| thorn-ant | 2/2/1,5/2/1 → **8,5** | 2/1,5/1,5/2/1 → **8** | Chân và râu rõ hơn trên kem; **tối chưa đạt số**, Dùng tiếp chỉ 1 |
| moss-banner | 2/2/1,5/2/2 → **9,5** | 2/1/1,5/2/2 → **8,5** | Cờ/chạc cây nhận ra; mặt nhỏ ở 22 px |
| banner-cloth | 2/2/1,5/2/2 → **9,5** | 2/1,5/1,5/2/2 → **9** | Mắt còn rõ ở 60 px; sợi vải chỉ đọc ở cỡ lớn |

## 6. Khác phiếu, việc còn lại và chạy lại

1. Bộ cuối thống nhất ở **review**, do không được ghi đè ba bộ tên cũ và các bản trung gian. Đường dẫn từng bản chọn ở mục 1 là nguồn đề nghị cho Claude.
2. Tờ `148-sheet-final.jpg` là bản bổ sung; tờ đúng tên `148-sheet.jpg` vẫn được giữ. Bản bổ sung làm rõ kích thước cờ tính theo **vải nhìn thấy**, thay vì cả canvas có lề.
3. Không thực hiện bước Claude cắt thử, theo chỉ dẫn “chạy ngay”. Không tạo khung vương miện bằng mã; không sửa game, `public/`, tài liệu khác, âm thanh, Tu Tiên hay worktree. Không chạy Git, build, test suite, dev server, trình duyệt hoặc mạng ngoài lệnh `image_gen`.
4. **Còn lại:** khi hạn mức sinh ảnh mở lại, chạy prompt kiến lượt 3 hoặc để Claude quyết cách dùng ảnh hiện tại. Không coi điểm tự chấm ≥8 là thay thế được chỉ tiêu tương phản. Claude cần chấm lại bộ cuối, đặc biệt kiến trên nền tối, mép cờ và các chip 22 px; Claude mới chép vào `public/` khi gắn.

Script mới đều trong [resume-20261030/](../../games/dragon-hold/art-src/_review/148/resume-20261030/), chỉ thêm file và bỏ qua tên đã tồn tại. Các script `process.py`, `finalize.py`, `audit.py`, `normalize-tool/` của lượt trước được giữ để truy nguyên. Chạy từ repo cha, không cần game:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
python3 games/dragon-hold/art-src/_review/148/finalize.py thorn-ant moss-banner banner-cloth
python3 games/dragon-hold/art-src/_review/148/resume-20261030/finish.py
python3 games/dragon-hold/art-src/_review/148/resume-20261030/supplement.py
python3 games/dragon-hold/art-src/_review/148/resume-20261030/clean-reductions.py
```

Font tờ xem: `/System/Library/Fonts/Supplemental/Arial.ttf`. Không có khung hình trình duyệt/render mới cần dọn; các JPEG trong review là chứng cứ bàn giao.
