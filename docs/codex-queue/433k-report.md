# Phiếu 433k — Hào quang C phía sau kiếm lớn

18/11/2026. **Đạt các cổng số của 433k sau đúng ba vòng sửa → chụp → mở ảnh.** Tỷ số sáng thấp nhất **1,947238×**, vùng trắng tối đa **0,00043403%**, p95 mưa dày **6,10 ms**, kiểm kiểu **0 lỗi**. Đây là bản lab gửi owner xem, chưa có chấm mù 8,5 hoặc owner duyệt hiệu ứng tổng hợp.

433j đã kết thúc trước khi bắt đầu: hào quang lông nhọn và nhuộm phẳng đã được gỡ, kiếm lớn giữ vật liệu GLB gốc. Giữ nguyên nợ của 433j: tỷ lệ chiều cao lớn/nhỏ bảo thủ **2,777864×**, chưa đạt 3×. Phiếu này không đổi kích thước kiếm, camera, trận, nhịp mưa hoặc âm thanh.

## Tệp và cách gắn

- `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/giant-sword-aura-c.png`, `.json`, `.prompt.txt`: xử lý duy nhất ảnh owner chọn `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/giant-sword-aura.v1-try3.png`. Giữ toàn bộ 1024×1024, không cắt mất chi tiết, không đổi tỉ lệ, làm mờ, mask hoặc vẽ thêm. Alpha thẳng = max RGB sRGB; RGB bù trong ánh sáng tuyến tính, lưu PNG 16 bit. Cộng lại trên nền đen: sai số kênh lớn nhất và trung bình **0/255**.
- JSON ghi tâm khe **(512;500)**, đầu trên **(512;240)**, đầu dưới **(512;760)**, cao **520 px**; hai sao **(512;180)** và **(512;808)**. Hai sao nằm ngoài hai đầu khe. Prompt cạnh PNG ghi đầy đủ nguồn và thao tác; đây là tách ảnh đã có, không phải sinh ảnh AI mới.
- `games/.wt-ic-lab-all/src/lab/metal-ult-aura-c-extract.mjs`: lệnh tái tạo PNG/JSON/prompt và kiểm phép cộng sáng.
- `games/.wt-ic-lab-all/src/lab/metal-ult-energy-a.ts`: thêm đúng **một quad C**, 2 tam giác, vật liệu chuẩn `MeshBasicMaterial`, `AdditiveBlending`, texture sRGB, không shader tạo hình. Trục dọc theo kiếm, chỉ quay quanh trục đó để hướng camera. Quad đặt sau toàn bộ bề dày mô hình theo hộp giới hạn GLB; lùi theo tia camera và bù bằng một hệ số thu phóng đều để khe vẫn khớp mũi–chuôi trên màn hình. Màu nhân đều **3,2**; không sửa màu, emissive hoặc map của GLB.
- C được vẽ thứ tự **8**, kiếm GLB thứ tự **9**: thân kiếm che C phía trước. Tắt depth test/write của riêng C để mặt đất không cắt ngang quầng khi quad được lùi ra sau; không thêm lớp che hoặc lớp sáng khác. Vì vậy phần quầng ngoài thân có thể phủ lên cảnh ở xa, cần owner xem ở góc sau lưng.
- `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`: tải texture C, đặt sRGB/lọc tuyến tính và truyền mốc sinh/chạm cho lớp kiếm; texture đi qua đường upload/dispose hiện có.
- `games/.wt-ic-lab-all/src/lab/metal-ult-rain-k-review.mjs`: driver riêng cho 433k, dùng server 3148 có sẵn, chụp/đo hai góc và xuất media. Chạy bằng `src/kit/tools/cdp-run.mjs` dưới `.local/bin/heavy.sh --perf`, 1280×720, DPR 1. Không chạy build hoặc bộ test game.

## Nhịp của C

Kiếm lớn bắt đầu rơi **4,10 s**; C hiện êm trong **0,08 s** đầu. Opacity tăng từ mức bay 0,72 lên **0,90 khi chạm 4,90 s**. Khi cắm, chỉ opacity nhịp ở **1,4 Hz**, hệ số 0,92–1,00; hình và kích thước không co giãn theo nhịp. C nhân đúng độ tan của kiếm từ **5,35 s**, về 0 ở **6,70 s**; ô kiếm trả về pool ở cuối chiêu **6,80 s**. Mẫu hai góc khớp nhau: 4,12 s = 0,112552; 4,90 s = 0,90; 5,05 s = 0,872953; 5,20 s = 0,832453; 5,90 s = 0,532067; 6,70 s = 0.

## Ba vòng đã mở ảnh

Cùng Chrome headless, High mặc định, ANGLE Metal Apple M4, 100 quái (87 TargetField + 13 walker), nền `?ground=%23353a40`. Mỗi vòng chụp Alt+1 và Alt+2 ở **1,05 / 2,35 / 3,90 / 4,65 / 4,90 / 5,90 s**; có đúng khung chạm đất 4,90 s. Đã mở tấm ghép ba vòng, khung chạm hai góc và tấm chuyển động; đối chiếu hàng ghép C của phiếu 448.

| Số đo | Vòng 1 | Vòng 2 | Vòng 3 cuối | Cổng |
| --- | ---: | ---: | ---: | ---: |
| Sáng lớn / nhỏ thấp nhất | 1,499228× | 1,947238× | **1,947238×** | ≥1,5× |
| Trắng toàn khung tối đa | 0% | 0% | **0,00043403%** | ≤6% |
| p95 mưa dày | 6,00 ms | 5,90 ms | **6,10 ms** | ≤16,7 ms |
| Cách mặt phẳng C sau bề mặt GLB, thấp nhất | −1,653 m | 1,977 m | **1,977 m** | >0 |

Vòng 1 thiếu sáng ở góc sau lưng và quad chưa lùi đủ toàn bộ bề dày kiếm. Vòng 2 sửa hai số đó nhưng khi mở ảnh thấy mặt đất cắt ngang phần dưới của C. Vòng 3 đổi thứ tự vẽ/depth của cùng quad, hết đường cắt đó. Dừng đúng ba vòng, không sửa hình sau vòng 3.

## Số đo cuối và giới hạn

- **Khe khớp:** 32 mẫu C đang hiện ở hai góc, chiều cao khe / mũi–chuôi màn hình **0,9999999999999992–1,0000000000000009**; sai số neo tối đa **3,98e−13 px**; scale x/y/z lệch **0**, hướng mặt dot ≥0,9999999999999999. Vật liệu chuẩn ở mọi mẫu. Vật liệu GLB khớp bản gốc ở mọi snapshot, không nhuộm phẳng lại.
- **Sáng:** đúng phương pháp 433i: render riêng thân A và nhóm kiếm lớn GLB + C vào HDR tuyến tính trước bloom/đầu ra, không cộng D hay cảnh. Tám mẫu hợp lệ, bốn mỗi góc: **4,20 / 4,40 / 4,60 / 4,916667 s**. Thấp nhất Alt+1 **2,558482×**, Alt+2 **1,947238×**. Không nhận mẫu rỗng hoặc Infinity. Đây là cực đại độ chói từng nhóm, không phải độ sáng trung bình hoặc tỉ lệ đã chấm thẩm mỹ.
- **Trắng:** cả ba kênh sRGB ≥242/255; đo 12 ảnh pha hai góc và toàn bộ **165 khung** clip Alt+1. Tối đa **4/921.600 pixel = 0,00043403%**.
- **Hiệu năng:** 42 mẫu lúc có kiếm rơi và số kiếm sống ≥80% đỉnh; CPU + readPixels một pixel chờ GPU như driver kế thừa. p95 **6,10 ms**, CPU p95 **2,20 ms**; p95 riêng đoạn kiếm lớn **5,60 ms**, toàn chiêu **5,90 ms**. Tối đa **302 draw calls / 1.481.543 tam giác**. Không đồng nhất số này với khoảng cách rAF hoặc tốc độ 24 fps của clip xuất.
- **Không đổi quãng rơi:** 103/103 kiếm đạt ≥0,45 s và ≥18% chiều cao khung; trung vị **0,950 s / 30,788%**, nhỏ nhất **0,800 s / 22,975%**. Kiếm lớn **0,800 s / 23,824%**. Đo mũi mỗi 1/60 s với material alpha ≥0,5 như 433j/433i, không xét che khuất theo từng texel/depth. Mưa 6 đợt, 102 kiếm nhỏ + 1 lớn, đỉnh 60 kiếm sống, trả đủ 103 ô cuối chiêu.
- **Kiểm tra:** `node node_modules/typescript/bin/tsc --noEmit` tại worktree lab **0 lỗi**; `node --check` hai driver mới đạt. Không có runtime exception. Còn cảnh báo KTX2Loader và flipbook metal-crescent-sym/metal-slash-arc sẵn có ngoài phạm vi; C/A/D và GLB tải thành công.

## Giao nộp và dọn dẹp

- [metal-rain-k.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-k.jpg): 12 ô, hai góc, bản vòng 3.
- [metal-rain-k.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-k.mp4): H.264 + AAC, **1280×720, 24 fps, 165 khung, 6,875 s, 5.724.212 byte**, Alt+1, trọn từ kích chiêu tới tan; 54 sự kiện âm Kim có sẵn. ffprobe đúng stream/thời lượng; ffmpeg giải mã hết không lỗi.
- [C ghép thử / runtime](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433k/c-runtime-compare.jpg), [tấm vòng 3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433k/round-3-k-sheet.jpg), [chuyển động](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433k/motion-contact.jpg), [số đo cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433k/round-3-metrics.json). Giữ tấm và số đo hai vòng trước.
- Đã xem trước rồi prune đúng **549/549 khung thô** của ba thư mục riêng phiên, **747.582.759 byte**, từ chối 0, không còn PNG thô. Giữ tấm ghép/JPG và JSON. Chrome của ba lượt đã đóng, profile tạm đã xóa; không còn profile st-cdp tạo ngày 18/11. Không đụng profile cũ hoặc Chrome của owner. Server 3148 **PID 243** giữ chạy.
- Đã ghi ABOUT cho chủ đề/từng lượt và thêm dòng vào ABOUT owner. Không chạy review-index vì các tệp chỉ mục nằm ngoài phạm vi ghi của phiếu; điều phối cập nhật sau.
- Không sinh ảnh AI hoặc âm thanh mới; không thêm lớp VFX khác; không sửa game chính, src/kit, scripts/tests game hoặc docs Tu Tiên. Không commit/push/reset/clean/stash.

**Owner cần xem:** độ ôm của C, phần sao dưới phủ trước cảnh/người tung chiêu ở Alt+2 do quầng không bị đất cắt, và phần trên kiếm/hào quang vượt mép trên ở góc sau lưng (camera/kích thước kế thừa 433j). Nợ tỷ lệ chiều cao 3× của 433j vẫn còn, không dùng kết quả 433k để nhận PASS nợ đó. Chưa có nghiệm thu thẩm mỹ 8,5.
