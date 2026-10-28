# Phiếu 097 · Lời Gọi · Hai tờ decal mặt đất

**Ngày:** 28/10/2026. **Kết quả:** hoàn thành hai tờ, mỗi tờ 8/8 ô; PNG giao qua các kiểm 2–5. Tự chấm thấp nhất **9/10 ở ô 512 px**, **8,5/10 ở ô thu 128 px**. Đây là điểm của Codex; **Claude phải chấm lại ≥ 8 trước khi chép vào `public/`**.

## 1. Tệp giao và bố cục

Tất cả tài sản mới nằm trong [scenery/meadow/decals/](../../games/typing-defense/art-src/scenery/meadow/decals/), không đưa media vào Git.

| Tờ | Alpha dùng để tích hợp | Bản nền kiểm #FF00FF |
| --- | --- | --- |
| Đất | [ground-decals-a.alpha.png](../../games/typing-defense/art-src/scenery/meadow/decals/ground-decals-a.alpha.png) | [ground-decals-a.png](../../games/typing-defense/art-src/scenery/meadow/decals/ground-decals-a.png) |
| Vật nhỏ | [ground-decals-b.alpha.png](../../games/typing-defense/art-src/scenery/meadow/decals/ground-decals-b.alpha.png) | [ground-decals-b.png](../../games/typing-defense/art-src/scenery/meadow/decals/ground-decals-b.png) |

Hai bản alpha là **2048 × 1024, RGBA, sRGB, 8 bit**, lưới **4 × 2**, ô **512 × 512**. Bản nền hồng là RGB. Mỗi tờ có hai ảnh nguồn `-left`, `-right` vuông; giữ nguyên bốn ảnh thô `.try1.png` cùng prompt chính xác, và lưu bản nguồn chọn thu về 1024 × 1024. Công cụ trả ảnh thô **1254 × 1254**, không sửa hoặc thay thế ảnh thô.

Trong mỗi tờ, đánh số từ trái qua phải, hàng trên trước:

| Ô | Nội dung tờ a | Nội dung tờ b |
| --- | --- | --- |
| 1 | Worn Earth A · đất mòn thứ nhất | White Wildflowers · hoa trắng, điểm son đỏ |
| 2 | Worn Earth B · đất mòn có dấu chân | Yellow Wildflowers · hoa vàng, điểm son đỏ |
| 3 | Y Junction · ngã ba đúng ba nhánh | Fallen Leaves · lá rụng |
| 4 | Straight Trail · đoạn đường thẳng | Tree Stump · gốc cây nhìn thẳng từ trên |
| 5 | Canopy Soil A · đất sẫm, lá kim và lá mục | Pebbles A · sỏi tròn |
| 6 | Canopy Soil B · biến thể đất dưới tán | Pebbles B · sỏi góc cạnh xen cuội |
| 7 | Curved Trail · đoạn đường cong nhẹ | Woodchip Ring · vòng vụn gỗ, tâm trống |
| 8 | Bare Clearing · đất trống | Clover Patch · cỏ ba lá |

Giữ thêm `<tờ>.try1.png` là bản ghép hai nửa nguồn trước sửa, trên nền hồng. Đây **không phải lượt gọi sinh ảnh thứ năm hoặc thứ sáu**. Prompt của tờ ghép chứa nguyên văn hai prompt nguồn, theo thứ tự trái rồi phải; không có một lượt sinh nguyên tờ. Có prompt tương ứng cả cạnh `.alpha.png`.

## 2. Prompt, lượt sinh và sửa bằng công cụ

Dùng skill **imagegen**, công cụ tích hợp **`image_gen`**, bốn lần gọi độc lập, **mỗi nửa chỉ một lượt sinh**. Toàn bộ prompt chính xác lưu trong [prompts.json](../../games/typing-defense/art-src/_review/097/prompts.json) và cạnh ảnh nguồn. Đã xem cỏ A, đường đất, `wildflowers-v2` và `mountain-pine-v2` của meadow để đối chiếu phong cách; không gửi chúng làm ảnh sửa.

| Nửa tờ | Nội dung riêng trong prompt lượt 1 | Thiếu sau sinh; cách sửa | Sửa prompt lượt 2–3 |
| --- | --- | --- | --- |
| `a-left` | Hai mảng mòn, hai mảng đất dưới tán; sắc đất mục tiêu khoảng 37°; góc nhìn thẳng, ánh sáng phẳng, không viền mực | Mép còn cứng; dịch hue từng ô, làm mềm alpha vào trong 24 px | Không cần sinh tiếp |
| `a-right` | Ngã ba Y, đoạn thẳng, đoạn cong và đất trống; nhánh rộng, đầu đường kết thúc trong ô | Một mẩu ngã ba lạc sang ô thẳng; ba ô đường chưa đủ diện tích sau xử lý đầu. Giữ thành phần đất liên thông lớn nhất, nới thân đường có giới hạn, rồi làm mềm | Không cần sinh tiếp |
| `b-left` | Khóm hoa trắng/vàng có điểm son, hai cụm sỏi dày; viền nâu mảnh, góc nhìn thẳng | Một số viên đọc như đá lớn ở thang 128 px/m. Thu cụm sỏi xuống 224/512, ghép bảy cụm xoay khác nhau thành mảng rải bất quy tắc | Không cần sinh tiếp |
| `b-right` | Lá rụng, mặt cắt gốc cây, vòng vụn gỗ tự nhiên không ký tự, cỏ ba lá | Chuẩn hóa kích thước và lề; giữ viền rõ và alpha nguồn | Không cần sinh tiếp |

Các prompt đều khóa nền trong suốt, bốn món tách rời, nhìn thẳng xuống, ánh sáng đều; cấm chữ, số, logo, khung, đường lưới và bóng đổ. Tờ a yêu cầu đất không viền; tờ b yêu cầu viền mực mảnh. Không có chữ trong PNG tài sản; nhãn chỉ ở JPG kiểm.

**Chuỗi xử lý chọn:** ImageMagick 7 thu Lanczos về 1024 × 1024, Node đọc RGBA, chia bốn ô; bỏ pixel alpha rất thấp và màu nền tím cấm; cắt theo vật rồi fit trong giới hạn 456 px, đặt giữa ô. Riêng bốn ô `a-right`, giữ thành phần liên thông lớn nhất trước fit để bỏ mẩu lạc và hạt rời.

Tờ a lấy mặt nạ alpha ≥ 128 làm lõi. Khoảng cách vào trong hình được tính hai lượt, bước ngang/dọc 1 và chéo √2. Alpha mới là `smoothstep(0, 24, khoảng cách)`, lượng tử hóa 8 bit. Vì vậy phần chuyển tiếp **nằm vào trong**, không đổ bóng hoặc làm nhòe ra ngoài. Pixel alpha 0 có RGB 0.

Ở bản xử lý đầu, diện tích ba ô đường A3/A4/A7 lần lượt **34,283% / 27,716% / 32,148%**, chưa đạt. Bản chọn bỏ vật lạc, nới bằng màu của pixel đất gần nhất; bán kính tối đa A3 **8 px**, A4 **32 px**, A7 **12 px**, giảm dần về 0 gần lề bảo vệ 28 px. Sau đó mới feather 24 px. Đầu đường vẫn dừng trong ô; không thêm nền đất hình vuông. Không có lượt sinh lại để sửa lỗi này.

Tờ b giữ alpha và viền nguồn, không áp dụng feather 24 px. Hai mảng sỏi được ghép lại để giảm cỡ viên; vẫn chỉ có hai decal sỏi trong tờ. Cụm sỏi sau ghép có mép hơi múi và một số mô típ viên lặp; ghi rõ trong chấm hình khối và ảnh kiểm.

## 3. KA1 · MD5 toàn bộ scenery

Chạy **`/sbin/md5 -r` mọi file trong `games/typing-defense/art-src/scenery/`**, sắp theo đường dẫn, trước khi ghi prompt hoặc ảnh vào đích, rồi sau khi giao đủ tài sản.

| Số đo | Kết quả |
| --- | ---: |
| Tệp trước | 144 |
| Tệp sau | 172 |
| Tệp cũ đổi nội dung | **0** |
| Tệp cũ mất | **0** |
| Tệp thêm | **28**, đều thuộc `meadow/decals/ground-decals-a.*`, `ground-decals-b.*` và các nửa được phép |
| Dòng nội dung bị bỏ trong `diff -U 0` | **0** |

`diff` chỉ thêm dòng nội dung; không tính tiêu đề `---`, `+++` của công cụ. Bằng chứng: [trước](../../games/typing-defense/art-src/_review/097/md5-before.txt), [sau](../../games/typing-defense/art-src/_review/097/md5-after.txt), [diff](../../games/typing-defense/art-src/_review/097/md5-diff.txt), [đối chiếu](../../games/typing-defense/art-src/_review/097/md5-verification.json).

## 4. Kiểm số trên PNG giao

Đo lại từ **hai `.alpha.png` đã giải mã**, không dùng số của ảnh thô thay cho bản giao. Bbox ghi tọa độ **nội bộ ô, gốc 0, hai đầu tính vào hình**. Diện tích phủ = số pixel **alpha > 0 / 262144**. Cột lõi alpha ≥ 0,5 cung cấp thêm độ đặc, không thay định nghĩa diện tích phủ. Hue theo HSV trên sRGB, trung vị các pixel alpha > 0. Không dùng hue của nền hồng.

| Ô | Bbox x0, y0, x1, y1 | Lề nhỏ nhất ≥ 24 px | Diện tích phủ ≥ 35% | Lõi alpha ≥ 0,5 |
| --- | --- | ---: | ---: | ---: |
| A1 | 30, 40, 481, 471 | 30 | 51,998% | 44,849% |
| A2 | 29, 48, 481, 464 | 29 | 46,657% | 39,621% |
| A3 | 28, 33, 483, 477 | 28 | 38,703% | 31,646% |
| A4 | 125, 28, 386, 482 | 28 | 37,679% | 32,521% |
| A5 | 29, 32, 481, 478 | 29 | 55,411% | 47,620% |
| A6 | 29, 35, 482, 476 | 29 | 50,909% | 43,556% |
| A7 | 33, 28, 478, 483 | 28 | 38,023% | 31,930% |
| A8 | 28, 35, 483, 476 | 28 | 55,637% | 48,746% |
| B1 | 28, 29, 483, 481 | 28 | 56,979% | 53,976% |
| B2 | 28, 35, 483, 476 | 28 | 53,962% | 50,977% |
| B3 | 28, 30, 483, 480 | 28 | 51,190% | 47,141% |
| B4 | 30, 28, 480, 483 | 28 | 49,632% | 48,677% |
| B5 | 63, 48, 449, 469 | 42 | 44,342% | 41,526% |
| B6 | 60, 45, 449, 469 | 42 | 45,480% | 42,664% |
| B7 | 28, 37, 483, 474 | 28 | 46,947% | 42,158% |
| B8 | 28, 33, 483, 478 | 28 | 54,602% | 51,936% |

**Đủ 8/8 ô ở mỗi tờ.** Pixel có **alpha > 0, hue 285–330°, S > 0,5: 0 pixel / 0% trong từng ô**, cả hai bản alpha. Nền #FF00FF của hai bản RGB là nền kiểm được yêu cầu, không phải ảnh đã tách nền dùng trong phép đo này.

Màu chuẩn lấy từ `scenery/meadow/ground/dirt-road.png` của 095: **hue trung vị 37,254902°**. Dịch hue đều trong từng món đất, giữ S/V; độ dịch nằm trong **+3,676920° đến +11,681131°**. Tờ b không bị khóa về hue đất.

| Ô đất | Pixel alpha 0,1–0,9 / pixel alpha > 0, cần ≥ 10% | Hue trung vị | Lệch với đường đất, cần ≤ 12° |
| --- | ---: | ---: | ---: |
| A1 | 15,241% | 37,241379° | 0,013523° |
| A2 | 16,547% | 37,241379° | 0,013523° |
| A3 | 22,316% | 37,263158° | 0,008256° |
| A4 | 16,787% | 37,368421° | 0,113519° |
| A5 | 15,237% | 37,272727° | 0,017825° |
| A6 | 15,881% | 37,215190° | 0,039712° |
| A7 | 19,546% | 37,281553° | 0,026651° |
| A8 | 14,036% | 37,281553° | 0,026651° |

**Tất cả qua kiểm 2–5.** [metrics-decoded.json](../../games/typing-defense/art-src/_review/097/metrics-decoded.json) lưu số đầy đủ; [identify.txt](../../games/typing-defense/art-src/_review/097/identify.txt) ghi định dạng. Đối chiếu bản RGB với phép ghép alpha lên #FF00FF: **0 kênh sai quá 1/255** ở cả hai tờ. Tính lại toàn bộ xử lý v3 từ bốn ảnh thô cho kết quả **trùng từng byte RGBA** với PNG giao; prompt chọn cũng trùng nguyên văn prompt lượt 1: [verification-final.json](../../games/typing-defense/art-src/_review/097/verification-final.json).

Các phép mép liền, chữ thập, độ rối và đốm lặp trong phần luật ô đất dành cho 095/098; không dùng làm cổng cho decal rời của 097.

## 5. Ảnh kiểm và quan sát

Đã mở ảnh kiểm ở cỡ đầy đủ, bản thu **128 px mỗi ô**, và bản ghép đúng thang:

- [097-a-full.jpg](../../games/typing-defense/art-src/_review/097-a-full.jpg), [097-b-full.jpg](../../games/typing-defense/art-src/_review/097-b-full.jpg): **2048 × 1024**, ô nguyên **512 px**, ghép lên caro xám để xem mép.
- [097-on-grass.jpg](../../games/typing-defense/art-src/_review/097-on-grass.jpg): **1280 × 1280**, đủ 16 món. Bản trước thu là [on-grass-full.jpg](../../games/typing-defense/art-src/_review/097/on-grass-full.jpg), **4096 × 4096**: mỗi decal **512 px trên một ô cỏ A 1024 px**, không phóng decal để lấp ô cỏ. Cùng mật độ **128 px/m**; ô decal 4 m, ô nền 8 m. Sau thu, ô cỏ rộng 320 px và vùng decal rộng 160 px. **Không dùng nền màu phẳng dự phòng.**
- [097-128.jpg](../../games/typing-defense/art-src/_review/097-128.jpg): **512 × 600**; từng ô decal đúng **128 × 128**, có dải nhãn riêng. Nền là phần cỏ tương ứng được cắt và thu cùng tỉ lệ với decal.
- [097-reference.jpg](../../games/typing-defense/art-src/_review/097-reference.jpg): đối chiếu bộ cỏ, đường, hoa và cây meadow; [097-a-left-raw.jpg](../../games/typing-defense/art-src/_review/097-a-left-raw.jpg): mép trước feather.

| Nhóm | Quan sát trên cỏ đúng thang |
| --- | --- |
| A1, A2, A8 | Mép chuyển vào cỏ tốt hơn ảnh thô; vẫn nhận rõ mảng vật liệu vàng. A2 có dấu chân giúp nhận đất mòn. Không có viền hồng hoặc mép vuông; **còn cảm giác miếng đất đặt lên cỏ** khi nhìn có chủ ý, nhất là A8 gần tròn. |
| A3, A4, A7 | Dáng Y, thẳng và cong đọc rõ, vùng giữa là đất; mép hòa khá tốt. Đây là đoạn đường rời có đầu dừng trong ô, **chưa phải đường liên tục đã ghép trong map**. A4 có vùng sắc độ kéo nhẹ dọc cạnh do nới thân bằng màu gần nhất. |
| A5, A6 | Đọc đúng đất dưới tán có lá mục/lá kim nhưng tối và đặc hơn nền; **hai món trông như mảng phủ rõ nhất ở tờ a** khi đứng riêng giữa bãi cỏ. Đặt dưới canopy hợp lý hơn. Chi tiết lá nhỏ giảm mạnh ở 128 px. |
| B1, B2 | Hoa trắng/vàng và điểm son đỏ còn rõ; viền mảnh hợp nhóm cây meadow. Cụm dày, lá hơi ôliu so với cỏ A xanh mạnh; còn dáng cụm tròn, hòa bằng khoảng trong suốt giữa lá hơn là feather. |
| B3, B4 | Lá rụng cam và gốc cây đọc rõ từ trên; gốc có vòng năm, vết nứt, không thấy vách thân cao hoặc bóng đổ lệch hướng. Mặt cắt sáng và viền vỏ khiến gốc **trông như vật đặt trên nền**, phù hợp loại vật nhưng chưa thể gọi là chìm vào đất. |
| B5, B6 | Cỡ viên đã giảm; khe cho cỏ lộ ra, không có nền đất đặc. Ở 128 px đọc thành thảm sỏi mịn; **còn dáng múi và nhịp viên lặp do ghép cụm**, cảm giác dán rõ hơn một bãi sỏi phân bố tự nhiên. |
| B7 | Tâm trống cho cỏ đi xuyên, vòng vụn gỗ nhận được ở cả hai cỡ. Gỗ sáng, vòng khá đều nên **còn cảm giác vòng đặt trên cỏ**; cần Claude xem khi đặt vào dấu cây luật đã chặt. |
| B8 | Màu xanh ôliu làm mảng khác mật độ cỏ A; lá đọc rõ, khe ngoài hòa vào nền. Một số cụm lá gần bốn lá, không phải mọi cụm đều là ba lá; đã trừ phần đúng đề. |

Đây là ảnh ghép tĩnh để duyệt tài sản, không phải hình gameplay đã tích hợp hoặc kiểm trình duyệt.

## 6. KA5 tự chấm

Theo `ART_ACCEPTANCE.md` §2.2 và năm tiêu chí ở §1. Thứ tự: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. Chỉ cho Dùng tiếp **2** sau khi các kiểm số của phiếu đạt. Điểm từng ô, không lấy trung bình để che ô thấp.

| Ô | 512 px: năm tiêu chí → tổng | 128 px: năm tiêu chí → tổng | Phần còn thiếu |
| --- | --- | --- | --- |
| A1 | 2 / 2 / 1,5 / 2 / 2 → **9,5** | 2 / 2 / 1,5 / 2 / 2 → **9,5** | Nét đất chi tiết hơn mảng cọ của cỏ A |
| A2 | 2 / 2 / 1,5 / 2 / 2 → **9,5** | 2 / 2 / 1,5 / 2 / 2 → **9,5** | Dấu chân hơi đều; nét đất khá chi tiết |
| A3 | 2 / 2 / 1,5 / 1,5 / 2 → **9** | 2 / 2 / 1,5 / 1,5 / 2 → **9** | Nhánh ngã ba tròn và hơi đều |
| A4 | 2 / 2 / 1,5 / 1,5 / 2 → **9** | 2 / 2 / 1,5 / 1,5 / 2 → **9** | Dải màu kéo nhẹ ở cạnh sau nới |
| A5 | 2 / 1,5 / 1,5 / 2 / 2 → **9** | 2 / 1,5 / 1,5 / 2 / 2 → **9** | Tối, nhiều lá nhỏ; mảng phủ còn rõ |
| A6 | 2 / 1,5 / 1,5 / 2 / 2 → **9** | 2 / 1,5 / 1,5 / 2 / 2 → **9** | Như A5, lá mục khá dày |
| A7 | 2 / 2 / 1,5 / 1,5 / 2 → **9** | 2 / 2 / 1,5 / 1,5 / 2 → **9** | Độ cong nhẹ, đoạn ngắn có đầu bo |
| A8 | 2 / 2 / 1,5 / 2 / 2 → **9,5** | 2 / 2 / 1,5 / 2 / 2 → **9,5** | Dáng khá tròn, còn đọc như miếng đất riêng |
| B1 | 2 / 2 / 1,5 / 2 / 2 → **9,5** | 2 / 2 / 1,5 / 2 / 2 → **9,5** | Lá ôliu, cụm dày |
| B2 | 2 / 2 / 1,5 / 2 / 2 → **9,5** | 2 / 2 / 1,5 / 2 / 2 → **9,5** | Như B1; nhiều hoa vàng |
| B3 | 2 / 2 / 1,5 / 1,5 / 2 → **9** | 2 / 2 / 1,5 / 1,5 / 2 → **9** | Lá lớn và màu thu nổi trên meadow |
| B4 | 2 / 2 / 1,5 / 2 / 2 → **9,5** | 2 / 2 / 1,5 / 2 / 2 → **9,5** | Gốc lớn, mặt cắt sáng |
| B5 | 2 / 2 / 1,5 / 1,5 / 2 → **9** | 2 / 1,5 / 1,5 / 1,5 / 2 → **8,5** | Dáng múi, mô típ lặp; sỏi nhỏ dày khi thu |
| B6 | 2 / 2 / 1,5 / 1,5 / 2 → **9** | 2 / 1,5 / 1,5 / 1,5 / 2 → **8,5** | Như B5; chi tiết dễ nhập thành mảng |
| B7 | 2 / 2 / 1,5 / 1,5 / 2 → **9** | 2 / 2 / 1,5 / 1,5 / 2 → **9** | Vòng khá đều, gỗ sáng |
| B8 | 1,5 / 2 / 1,5 / 2 / 2 → **9** | 1,5 / 2 / 1,5 / 2 / 2 → **9** | Một số cụm gần bốn lá; xanh ôliu |

**Mức: Đạt theo tự chấm**, tờ a thấp nhất 9, tờ b thấp nhất 8,5. B5/B6 là hai món ở mức 8–8,5 khi thu, có thể nâng tiếp độ phân bố khi tiện; không sửa `ART_REPLACE_LATER.md` vì ngoài đường dẫn được phép của phiếu. Ghi ngay trong báo cáo này để Claude tiếp nhận khi duyệt.

## 7. Script, chạy lại và phạm vi

Script và số đo nằm trong [_review/097/](../../games/typing-defense/art-src/_review/097/). Dùng thư viện chuẩn Node và `/opt/homebrew/bin/magick`; không cài gói, không cần NumPy/Pillow.

- `setup.mjs`, `ingest.mjs`: prompt, snapshot và sao chép ảnh thô; ghi độc quyền, từ chối ghi đè.
- `process.mjs`: bản đầu cùng `metrics-plan.json`; giữ lại bằng chứng ba ô chưa đạt.
- `prepare-process-v2.mjs` → `process-v2.mjs`: bỏ thành phần lạc, nới đường; giữ `metrics-plan-v2.json` và hai candidate riêng.
- `prepare-process-v3.mjs` → **`process-v3.mjs`**: bản chọn; bổ sung ghép lại sỏi; số tham số trong `metrics-plan-v3.json`. Hai PNG candidate v3 trùng RGBA với bản giao.
- `prepare-review-v2.mjs` → `make-review-v2.mjs`: bảng kiểm cuối; sửa bản nháp để thumbnail cỏ và decal có cùng mật độ pixel/m. `preview.mjs` và các `make-candidate*.mjs` giữ các lần xem trước chốt.
- `prepare-final.mjs` → **`deliver-selected.mjs`**, **`audit-selected.mjs`**: giao candidate v3, audit định dạng, từng ô, màu, compositing và MD5. Bản audit chọn đọc đúng một dấu cách trong đầu ra `md5 -r` trên macOS.
- `alpha-prompts.mjs`, `verify.mjs`: prompt cạnh alpha, đối chiếu prompt và tính lại RGBA. `deliver.mjs`, `audit.mjs`, `make-review.mjs` và `prepare-deliver-audit-v2.mjs` là các nháp được giữ, không dùng để giao đè lên bản chọn. Mode `finalize` trong các bản `process*` không được chạy.

Các tên v2/v3 là **lượt sửa bằng công cụ**, không phải lượt sinh ảnh. Không ghi đè bản nháp hoặc kết quả cũ của phiên; ảnh thô `.try1` giữ nguyên. Mọi script tạo đầu ra cần chạy trên đích chưa có tệp tương ứng. Chuỗi giao đã chạy từ repo cha:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/typing-defense/art-src/_review/097/process.mjs plan
node games/typing-defense/art-src/_review/097/prepare-process-v2.mjs
node games/typing-defense/art-src/_review/097/process-v2.mjs plan
node games/typing-defense/art-src/_review/097/prepare-review-v2.mjs
node games/typing-defense/art-src/_review/097/preview.mjs
node games/typing-defense/art-src/_review/097/prepare-process-v3.mjs
node games/typing-defense/art-src/_review/097/process-v3.mjs plan
node games/typing-defense/art-src/_review/097/make-candidate-v3-review.mjs
node games/typing-defense/art-src/_review/097/prepare-final.mjs
node games/typing-defense/art-src/_review/097/deliver-selected.mjs
node games/typing-defense/art-src/_review/097/alpha-prompts.mjs
node games/typing-defense/art-src/_review/097/make-review-v2.mjs
node games/typing-defense/art-src/_review/097/audit-selected.mjs
node games/typing-defense/art-src/_review/097/verify.mjs
```

Để **chạy lại phép tính trên ảnh thô, so từng byte với bản giao mà không ghi file**, dùng:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/typing-defense/art-src/_review/097/process-v3.mjs replay
```

**Khác phiếu:** ảnh sinh có alpha thật thay vì phải key nền hồng; bản ghép RGB vẫn đúng #FF00FF theo yêu cầu. Công cụ sinh trả 1254 px, nên chuẩn hóa hai nửa chọn về 1024 px trước ghép. Có thêm sửa hình đường và ghép lại sỏi như mục 2. Giữ các candidate, bảng so trước/sau và số đo trong vùng review để có thể kiểm lại. Không thay loại hoặc số món.

**Bỏ qua:** lượt sinh 2–3 vì công cụ đã sửa lên ngưỡng; chưa chép `public/` vì Claude là người chấm lại và tích hợp. Không làm âm thanh. Không chạy lệnh Git, build/test game, dev server, trình duyệt hay mạng ngoài `image_gen`; không sửa mã game, tài liệu khác hoặc đọc/ghi vùng Tu Tiên. JPG kiểm là dẫn xuất tĩnh được báo cáo sử dụng, không có bộ frame chụp thô cần dọn.

**Claude/chủ dự án cần xem:** trước hết `097-on-grass.jpg` và `097-128.jpg`; xem kỹ cảm giác mảng dán của A5/A6, cạnh kéo màu A4, độ rải và mô típ lặp của B5/B6, vòng vụn gỗ B7 và vài cụm bốn lá B8. Chỉ dùng hai `.alpha.png` đã xử lý khi tích hợp; các nửa chọn và `.try1` là nguồn đối chiếu.
