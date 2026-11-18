# Phiếu 433j — Kiếm nhỏ to hơn, trận pháp lùi lại

18/11/2026. **Đã hết 3 vòng; chưa đạt toàn bộ phiếu.** A/D đã phóng đều 1,8 lần; trận đã lùi và không che người tung chiêu; kiếm lớn đã bỏ hào quang và giữ vật liệu gốc. Còn thiếu tỷ lệ chiều cao lớn/nhỏ ≥3 khi đối chiếu với kiếm nhỏ lớn nhất: tỷ lệ bảo thủ **2,778×**, tỷ lệ đỉnh **2,957×**. Không sửa hình sau vòng 3 và không ghi PASS cho phần này.

## Bản cuối

- `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`: kiếm nhỏ từ 3,2–3,8 lên **5,76–6,84 m**, cùng hệ số 1,8 cho ảnh A và chiều dài cơ sở của D; giữ thu phóng đều, nguyên hình nguồn và neo chuôi. Kiếm lớn thu phóng đều lên **24 m** để giữ phân cấp, nhưng tỷ lệ màn hình vẫn thiếu cổng nêu trên.
- Trận **A**, đường kính **22 m**, cao **12 m**, tâm cố định **10 m sau tâm đàn quái**, theo hướng rời người tung chiêu; trong cảnh đo là khoảng (−0,637; 12; −18,939). Không dời theo camera. Kiếm nhỏ và kiếm lớn bắt đầu tại mặt trận, rơi chéo về đàn quái; bỏ khoảng xuất phát 8 m trên trận để không mọc thành bó ở ngoài khung.
- Camera chơi giữ góc hạ 6°, khoảng cách 0,95 lần và FOV **40°**, ngắm về phía trận nhưng giữ người tung chiêu trong khung. Góc sau lưng giữ vị trí mắt sau người chơi, FOV 66°, hạ điểm ngắm để thấy người và đàn quái. Trận hiện bằng opacity từ **0,50–0,60 s**, sau khi camera vào vị trí; đợt kiếm đầu vẫn ở 0,60 s. Toàn bộ thời gian trận có opacity >0,001 đều đủ lề 4% ở camera chơi.
- Kiếm nhỏ cắm nghiêng ra xa camera, cùng độ nghiêng cũ 0,06–0,16 rad, mũi ngập 15%; phần thân nổi trên đất dễ đọc hơn. D vẫn neo chuôi, giữ tỉ lệ ảnh và tan 0,20 s, xoay cùng trục kiếm khi cắm.
- `metal-ult-energy-a.ts`: gỡ hoàn toàn card/texture/flipbook hào quang, bỏ ghi đè emissive vàng; chỉ clone vật liệu GLB và đổi opacity khi tan. Bỏ luôn motes bám quanh thân kiếm lớn trong recipe. Không thêm lớp thay thế; vị trí hào quang mới để trống chờ **448**. Vệt D và các lớp va chạm/đất có sẵn giữ lại.
- `metal-sword-look.ts`: nhánh so sánh cũ cũng loại kiếm lớn khỏi nhánh nhuộm phẳng; bỏ ghi đè emissive trên base. Recipe hiện tại chỉ dựng `EnergyASwordLayer`; không gọi lớp so sánh cũ.
- Thêm `metal-ult-rain-j-review.mjs`: dùng server 3148 có sẵn, chụp/đo hai góc, xuất media và báo cáo. Không thêm tài nguyên art, không sửa game chính, `src/kit`, scripts/tests game hoặc tài liệu Tu Tiên.

## Ba vòng đã mở ảnh

1280×720, DPR 1, High mặc định, Chrome headless / ANGLE Metal Apple M4, 100 quái (87 TargetField + 13 walker), nền `?ground=%23353a40`. Đã mở tấm vòng 1, 2, 3, tấm chi tiết/chuyển động và đối chiếu ảnh 433i. Mỗi vòng chụp Alt+1/Alt+2 tại 1,05 / 2,35 / 3,90 / 4,916667 / 5,90 s.

| Số đo | Vòng 1 | Vòng 2 | Vòng 3 cuối |
| --- | ---: | ---: | ---: |
| Hệ số A/D | 1,8× | 1,8× | 1,8× |
| Thân kiếm nhỏ đang rơi, cao dọc khung | 74,90–138,82 px | 74,71–128,31 px | **69,76–149,51 px** |
| Kiếm đã cắm nhỏ nhất, tính cả phần ngập | 31,05 px | 31,05 px | 69,34 px |
| Thân nhỏ còn nổi trên đất, nhỏ nhất | chưa đo riêng | chưa đo riêng | **60,33 px** |
| Kiếm lớn tại 4,916667 s, không tính D | 428,89 px | 349,76 px | **416,24 px** |
| Tỷ số sáng lớn/nhỏ, tối thiểu, chỉ để biết | 0,918× | 2,589× | **1,499×** |
| Chiều cao trận Alt+2 | 13,17% | 13,17% | **22,73%** |
| Trung vị thời gian thấy mũi rơi | 0,950 s | 0,950 s | **0,950 s** |
| Trung vị quãng rơi / chiều cao khung | 68,57% | 40,57% | **30,79%** |
| Đạt đồng thời ≥0,45 s và ≥18% | 103/103 | 103/103 | **103/103** |
| Vùng trắng tối đa | 0,01769% | 0,04568% | **0%** |
| p95 mưa dày | 5,70 ms | 6,00 ms | **5,80 ms** |

Vòng 1 còn cắt trận khi camera vào chiêu; vòng 2 đã sửa phần đó nhưng kiểm rộng hơn thấy kiếm cắm 31 px và người tung chiêu bị cắt ở Alt+1. Vòng 3 sửa khung chơi và góc kiếm cắm. Không giữ kết luận PASS ban đầu của vòng 2.

## Cổng cuối và giới hạn phép đo

- **Kiếm nhỏ đạt:** 6.686 mẫu thân trọn khung, material opacity ≥0,5, gồm bay và cắm. Chiều cao mũi–chuôi 69,34–149,51 px; khi bỏ phần ngập đất, còn **60,33–149,51 px**, trung vị 107,04 px. Mũi/chuôi là neo trong JSON nguồn A, không tính vệt D hoặc bloom. Mọi scale x/y/z bằng nhau, sai số neo tối đa 1,78e−15 m; 0 mô hình kiếm nhỏ và 0 lớp qi-streak được vẽ.
- **Kiếm lớn chưa đạt tỷ lệ 3×:** 56 mẫu trọn thân trong khung cho chiều cao **415,31–442,07 px**, trung vị **427,19 px**. So với kiếm nhỏ lớn nhất 149,506 px: thấp nhất **2,7779×**, đỉnh **2,9569×**. Không dùng trung vị kiếm nhỏ để nhận PASS. Trong chuỗi 60 Hz không có mẫu cả kiếm lớn trọn thân lẫn kiếm nhỏ opacity ≥0,5 cùng khung; phép kiểm đã được sửa để mảng rỗng không biến thành Infinity rồi nhận PASS. JSON vòng 3 đã tính lại từ chính dữ liệu lưu, `passed: false`; không chụp vòng 4.
- **Trận đạt:** Alt+2 cao 163,67 px = **22,732%**, đáy ở 238,58 px, đầu người tung chiêu ở 358,02 px, không giao nhau. Người tung chiêu nằm trọn ở cả hai góc. Alt+1 lề nhỏ nhất bốn phía khi trận hiện là **6,563%**, vượt 4%. Trận đã tan hoàn toàn khi camera trở về; hộp hình học lúc ấy có thể ra ngoài khung, không phải hình đang hiện.
- **Quãng rơi đạt:** đúng cách 433f/433i: lấy mẫu 1/60 s, chiếu mũi local y=0, cộng thời gian trước va chạm khi mũi trong clip/khung và alpha bay ≥0,5; lấy chênh y mũi đầu/cuối chia 720. Đây là phép đo hình học/material alpha, không xét occlusion theo depth buffer hay alpha từng texel của ảnh. Trung vị **0,950 s / 30,788%**, nhỏ nhất **0,800 s / 22,975%**; **100%** đạt cả hai. Riêng kiếm lớn **0,800 s / 23,824%**.
- Giữ sáu đợt **12/14/16/18/20/22**, thời điểm **0,60/1,28/1,90/2,46/2,96/3,40 s**; mưa **4,088344 s**, kiếm lớn sinh 4,10 s, cắm 4,90 s; tối đa 60 kiếm sống, trả đủ 103 ô ở cuối 6,80 s. Bề ngang kiếm cắm trong khung 54,967%; không đổi tọa độ đích/rải quân để làm đẹp số này.
- **Sáng chỉ để biết:** HDR tuyến tính trước bloom/tone mapping đầu ra, render riêng thân A và thân Tripo, không cộng D hoặc cảnh; tỷ số nhỏ nhất **1,499228×**, không áp cổng ≥1,5. Vật liệu lớn vẫn chịu tone mapping gốc của GLB trong cảnh, không nâng emissive để đạt số.
- **Trắng đạt:** cả ba kênh sRGB ≥242/255, đo ảnh pha hai góc và toàn bộ 165 khung clip Alt+1, tối đa **0%**.
- **Hiệu năng đạt:** 42 mẫu lúc có kiếm rơi và số sống ≥80% đỉnh, CPU rồi readPixels một pixel chờ GPU như driver cũ: p95 **5,80 ms**, CPU p95 **2,00 ms**; toàn chiêu **5,60 ms**. Tối đa 302 draw calls / 1.481.537 tam giác. Không đồng nhất với khoảng cách rAF.
- **Kiểm kiểu đạt:** `node node_modules/typescript/bin/tsc --noEmit` tại worktree lab, **0 lỗi**; `node --check` driver mới đạt. Không chạy build hoặc bộ test game. Không có runtime exception. Còn cảnh báo sẵn có KTX2Loader và drawImage metal-crescent-sym/metal-slash-arc ngoài phạm vi; A/D và GLB tải thành công.

## Vật liệu gốc và kết quả grep

GLB có baseColorFactor trắng [1,1,1,1], metallic/roughness factor đều 1, texture màu, metallicRoughness và normal; không có emissive map trong nguồn. Snapshot thực tế khớp toàn bộ clone gốc: màu [1,1,1], metalness/roughness 1, emissive [0,0,0], emissiveIntensity 1, normalScale [1,−1] do GLTFLoader, toneMapped true, FrontSide; map/normal/roughness/metalness cùng UUID nguồn, emissiveMap null. Không tự gỡ một map vốn tồn tại; không tự thêm màu vàng. Chỉ transparent/opacity thay đổi để tan theo lịch cũ.

```sh
grep -nE 'aura-metal-feather-mantle|giant\.material\.(emissive|color)\.(set|copy)|base\.material\.emissive\.(set|copy)' games/.wt-ic-lab-all/src/lab/metal-*
# exit 1; không có dòng khớp

grep -nE 'material\.(color|emissive)\.set|material\.(emissiveMap|metalness|roughness)\s*=' games/.wt-ic-lab-all/src/lab/metal-ult-energy-a.ts games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts
# exit 1; không có dòng khớp

grep -n -A9 'energy = !giant' games/.wt-ic-lab-all/src/lab/metal-sword-look.ts
150:      const giant = i === capacity - 1, energy = !giant && look !== "aura";
151-      const material = base.material.clone();
152-      material.transparent = true;
153-      if (energy) {
154-        material.emissiveMap = null; material.vertexColors = false;
155-        material.depthWrite = true; material.toneMapped = false;
156-        material.map = null; material.normalMap = null; material.roughnessMap = null; material.metalnessMap = null;
157-        material.color.setRGB(0.025, 0.012, 0.002); material.metalness = 0; material.roughness = 1;
158-        material.emissive.setRGB(1, 0.7, 0.15); material.emissiveIntensity = 0.55;
159-      }
```

Nhánh emissive còn lại ở lớp cũ chỉ dành cho `!giant`, không được recipe gọi. Nhật ký grep đầy đủ: [grep-audit.json](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433j/grep-audit.json).

## Giao nộp và dọn dẹp

- [metal-rain-j.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-j.jpg): 10 ô, hai góc, bản vòng 3.
- [metal-rain-j.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-j.mp4): H.264 + AAC, **1280×720, 24 fps, 165 khung, 6,875 s, 5.631.993 byte**, Alt+1; âm Kim có sẵn, 54 sự kiện. ffprobe đúng stream/thời lượng; ffmpeg giải mã hết không lỗi. Không tạo âm hoặc ảnh AI mới.
- [So sánh i/j](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433j/i-j-compare.jpg), [chi tiết hai góc](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433j/round-3-trail-detail.jpg), [chuyển động](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433j/motion-contact.jpg), [số đo cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433j/round-3-metrics.json). Giữ tấm và số đo hai vòng trước.
- Đã ghi ABOUT cho chủ đề/lượt và một dòng kết quả cuối vào ABOUT owner. Đã xem trước rồi prune **378/378 khung thô của phiên, 497.438.642 byte**; không còn PNG thô. Không xóa ảnh hoặc profile của phiên khác.
- Driver đóng Chrome và xóa profile của mọi lượt; không còn tiến trình Chrome st-cdp của phiên, không còn profile tạo ngày 18/11. Các profile cũ ngày 16–17/11 giữ nguyên. Server 3148 **PID 243** vẫn chạy.
- Không commit/push/reset/clean/stash. Không chạy review-index vì file chỉ mục nằm ngoài phạm vi ghi; điều phối cập nhật sau.

**Owner cần xem:** tỷ lệ kiếm lớn so với kiếm nhỏ và phần kiếm lớn vươn khỏi mép trên ở Alt+2 sau khi cắm. Hào quang 448 cố ý để trống. Không nhận phiếu hoàn thành toàn bộ hoặc đã qua chấm mù 8,5; dừng đúng giới hạn ba vòng.
