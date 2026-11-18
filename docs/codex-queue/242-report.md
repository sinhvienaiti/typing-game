# Phiếu 242 · Last Line · Đủ 11 icon mới, chờ Claude duyệt trong game

Ngày 31/10/2026, Mac mini M4. Đã sinh **18 ảnh thử** bằng `image_gen` tích hợp, chọn 11 ảnh và giao **44 PNG**: 1024², 256², 128², 64², sRGB RGBA 8 bit. Mỗi PNG giao và mỗi lượt sinh có prompt nguyên văn cạnh ảnh. Không gặp 429 hay thông báo chờ; không dùng API/CLI tạo ảnh thay thế.

**Đây là bộ giao để chấm lại, chưa đóng nghiệm thu.** Đạt khổ, lề, tâm, alpha master, độ đặc, độ phủ, tương phản và mọi cặp IoU bắt buộc theo alpha >128. Còn ngoại lệ alpha trên các bản thu Lanczos, IoU New-word read–Words theo ngưỡng phụ >16, sắc tím Rift và giới hạn của tự đọc bỏ nhãn; ghi đủ bên dưới. Không gọi các số còn thiếu là đạt.

## Bộ giao và lượt sửa

Gốc ảnh: `games/typing-survival/art-src/ui/icons/`. Mười tên cũ có bản chọn `<tên>.r2.png`, `.r2.256.png`, `.r2.128.png`, `.r2.64.png`; tên mới `stat-words` không có `.r2`. Không ghi đè ảnh, prompt hay try cũ. Claude tự trỏ game sang các bản này khi quyết định nhận.

| Tên | Chọn / tổng lượt | Sửa prompt qua lượt |
|---|---|---|
| next-stage | r2-try2 / 2 | Lượt 1 vòng C còn lớn, đầu tên nhỏ. Lượt 2 làm đầu tên chiếm khoảng 60% chiều ngang, rút thân, mở cổng C, giảm mạch vàng. |
| bay-full | r2-try1 / 1 | Ba viên đạn đầu nhọn dựng trong kẹp dày, không phải ba khối pin bằng đầu. |
| kills | r2-try1 / 1 | X lớn giữa bốn ngàm ngắm, chớp cam nhỏ ở tâm. Không còn mảnh dao/lông vũ. |
| stat-accuracy | r2-try1 / 1 | Bia ba vòng dày, mũi tên cắm tâm, phân biệt với X của Kills. |
| stat-evenness | r2-try2 / 2 | Lượt 1 thấy thanh nhưng bọt quá nhỏ. Lượt 2 yêu cầu cửa tối và một bọt lam lớn; ảnh vẫn dài hơn tỷ lệ 2:1 đã đề nghị, giữ hình vì bọt đọc rõ hơn. |
| stat-new-word | r2-try1 / 1 | Mắt mở phía trên thẻ hai thanh, bỏ viên ngọc đơn. |
| stat-words | try2 / 2 | Lượt 1 hai màn lam còn nhiễu sắc hồng ở mép. Lượt 2 mặt sứ ngà và hai thanh tối lớn, bớt hoa văn. |
| keyboard | r2-try3 / 3 | Lượt 1 giống keycap (IoU 0,991). Lượt 2 thuôn hơn nhưng còn 0,869. Lượt 3 thuôn mạnh, ba hàng phím và phím cách dài. Tăng đều toàn vật tới lề 71,973% để phím lớn hơn, IoU còn 0,738. Không bóp hình. |
| clock | r2-try1 / 1 | Đồng hồ bấm giờ có nút trên, một kim dày; không mũi tên quanh vành. |
| hazard | r2-try1 / 1 | Tam giác sọc cam–đen và nứt giữa, khác tấm lục giác cũ. Còn đường lam phụ, giảm điểm Hợp bộ. |
| rift | r2-try3 / 3 | Lượt 1 như ngọc có khung kim loại. Lượt 2 đổi sang khe rách kính, nhưng ΔY panel chỉ 0,248. Lượt 3 mở lòng khe sáng hơn, tím ngả lam; ΔY panel 0,308. Đã hết ba lượt. |

Mỗi prompt giữ STYLE-UI Lightbearer §4.3, khối KIND lấy từ prompt đã dùng của phiếu gốc (Words dùng khối ICON của nhóm hồ sơ), rồi thêm nguyên văn SMALL-SIZE, ý riêng và dòng nền. Quy tắc nhỏ của 242 được ưu tiên khi mâu thuẫn khối cũ về outline/hoa văn. **Cả 18 lần đều đính kèm ba ảnh tham chiếu đã xem: streak.png, lock.png và ../parts/mag-full.png.** Không sửa các ảnh tham chiếu. Prompt và nguồn sinh nằm cạnh nhau theo đúng hậu tố, nguồn 1254² RGBA thật.

## Hậu kỳ và kiểm 1–2

Dùng ImageMagick 7 trực tiếp trên macOS. Cắt khoảng rỗng theo bbox alpha >16, thu **đều hai trục theo cùng tỷ lệ** về cạnh dài 717 px (Keyboard 737 px), căn giữa và đệm trong suốt 1024². Không thay RGB ở bước matte; chỉ đưa alpha rất gần 0/255 về đầu mút **ngoài dải mép 3 px** theo cả đường bao >16 và 50%. Mức đổi alpha lớn nhất 14/255, không phủ/xóa phần vẽ. Không chỉnh gamma, độ sáng, hue, không làm nét. Ba bản thu dùng Lanczos trực tiếp từ master, không sửa matte riêng của bản thu.

Mười một tờ sinh/hậu kỳ: `art-src/_review/242-<tên>-before-after.jpg`, hai ô cùng canvas 512². Đã xem bản chọn và đối chiếu các tờ; còn đủ nguồn và ứng viên để kiểm lại. Thao tác chỉ đổi lề/cỡ và matte nhẹ, giữ bevel, vật liệu, lõi sáng và khe hở.

44/44 PNG được kiểm khổ/kênh/độ sâu; 33/33 bản thu so pixel với phép Lanczos trực tiếp. Kết quả ở [audit-delivery/identify.txt](242/audit-delivery/identify.txt), [summary.json](242/audit-delivery/summary.json).

| Tên | Cạnh dài/canvas % | Lệch tâm % | Pixel matte đổi | Δ alpha lớn nhất |
|---|---:|---:|---:|---:|
| next-stage | 70.020 | 0.049 | 206082 | 11 |
| bay-full | 70.020 | 0.049 | 364439 | 14 |
| kills | 70.020 | 0.049 | 281927 | 10 |
| stat-accuracy | 70.020 | 0.049 | 375749 | 10 |
| stat-evenness | 70.020 | 0.049 | 167989 | 8 |
| stat-new-word | 70.020 | 0.049 | 365067 | 13 |
| stat-words | 70.020 | 0.049 | 390284 | 12 |
| keyboard | 71.973 | 0.049 | 203321 | 11 |
| clock | 70.020 | 0.049 | 296164 | 11 |
| hazard | 70.020 | 0.049 | 287372 | 10 |
| rift | 70.020 | 0.049 | 127479 | 9 |

## Alpha sạch và sắc gần màu khóa

Số dưới là **pixel alpha 1…254 ngoài dải mép 3 px**: mỗi ô ghi theo đường bao **>16 / ≥128**. Dải mép dùng kernel Disk bán kính 3 trong ImageMagick; giữ cả hai định nghĩa để không chọn cách có lợi. Cột M là phần trăm pixel alpha >0 có H=285…315°, S>0,5, lớn nhất qua bốn khổ.

| Tên | 1024² | 256² | 128² | 64² | M tối đa % |
|---|---:|---:|---:|---:|---:|
| next-stage | 0 / 0 | 111 / 0 | 60 / 0 | 20 / 0 | 0.016846 |
| bay-full | 0 / 0 | 99 / 0 | 47 / 4 | 16 / 0 | 0.070264 |
| kills | 0 / 0 | 137 / 10 | 77 / 3 | 34 / 0 | 0.103539 |
| stat-accuracy | 0 / 0 | 66 / 0 | 21 / 0 | 4 / 1 | 0.021590 |
| stat-evenness | 0 / 0 | 110 / 0 | 31 / 0 | 22 / 0 | 0.026352 |
| stat-new-word | 0 / 0 | 110 / 0 | 87 / 0 | 60 / 0 | 0.053609 |
| stat-words | 0 / 0 | 108 / 0 | 41 / 0 | 26 / 0 | 0.039520 |
| keyboard | 0 / 0 | 48 / 0 | 26 / 0 | 14 / 0 | 0.029025 |
| clock | 0 / 0 | 43 / 1 | 17 / 0 | 14 / 0 | 0.033486 |
| hazard | 0 / 0 | 53 / 0 | 8 / 0 | 2 / 0 | 0.026321 |
| rift | 0 / 0 | 42 / 2 | 18 / 2 | 10 / 1 | 0.201879 |

**11/11 master đạt cả hai cách đo mép. Bản thu chưa đạt đầy đủ kiểm alpha nghiêm ngặt.** Đuôi/ringing Lanczos tạo lại alpha lẻ, nhiều nhất 137 pixel theo >16 và 10 theo ≥128 trong một file. Không ép matte bản thu vì phải giữ phép thu trực tiếp và nét ở cỡ nhỏ. Theo ART_ACCEPTANCE §5, giữ tranh và ghi mâu thuẫn để Claude quyết; mọi ảnh chỉ nhận 1 điểm Dùng tiếp.

**Rift master có M=0,201879%, cao hơn 0,2% đúng 0,001879 điểm phần trăm.** Đây là phép đếm sắc gần magenta, nguồn sinh alpha thật và không dùng nền khóa; tím là màu được yêu cầu của Rift. Không xóa ánh tím hoặc đổi hue để ép số. Giữ nguyên ngoại lệ này cho Claude chốt. Mười ảnh còn lại đều dưới 0,2%. Đã dùng hết ba lượt Rift.

## Cỡ thật, độ đặc, độ phủ và tương phản

Ô PNG trong [proofs-v3](242/proofs-v3/) có hai nền cắt **nguyên pixel từ ảnh UI thật**: button.png `320x64+220+160`, panel-large.png `320x64+230+230`. Hai vùng đều ở lòng khung, không chứa nền khóa ngoài khung. Nền không tô lại, không dùng màu phẳng. Các số tương phản đo ở chính phần đặt icon; vùng cắt rộng hơn của proof v3 giữ nguyên pixel vùng đó.

Font Arial hệ thống; nhãn được render rồi thu đều về **chiều cao bitmap đúng round(0,60 × cỡ icon)**, tránh nhầm point size với chiều cao chữ thật. Bay full không nhãn. Ô 1× giữ nguyên pixel; có nguyên ô phóng 4× bằng point trong proofs-v3. Không dùng ảnh phóng để cho điểm.

Độ đặc = số pixel còn sau opening 2×2 / số pixel mask ban đầu ở 720p. Độ phủ = diện tích alpha >128 / diện tích bbox của mask ấy. Luma sRGB Y′=0,2126R′+0,7152G′+0,0722B′, ΔY là chênh trung bình có trọng số alpha với nền UI dưới vật, không phải tỷ số WCAG.

| Tên | 720p / 1080p px | Opening % ≥80 | Phủ % ≥30 | ΔY button 720 / 1080 | ΔY panel 720 / 1080 |
|---|---|---:|---:|---|---|
| next-stage | 28 / 40 | 99.38 | 60.90 | 0.477 / 0.479 | 0.458 / 0.456 |
| bay-full | 20 / 28 | 98.59 | 84.52 | 0.418 / 0.419 | 0.401 / 0.400 |
| kills | 28 / 40 | 100.00 | 55.25 | 0.413 / 0.413 | 0.393 / 0.390 |
| stat-accuracy | 28 / 40 | 99.65 | 78.61 | 0.462 / 0.466 | 0.442 / 0.443 |
| stat-evenness | 28 / 40 | 100.00 | 78.75 | 0.364 / 0.369 | 0.344 / 0.346 |
| stat-new-word | 28 / 40 | 99.64 | 72.89 | 0.370 / 0.374 | 0.351 / 0.351 |
| stat-words | 28 / 40 | 99.66 | 73.50 | 0.471 / 0.475 | 0.452 / 0.452 |
| keyboard | 28 / 40 | 100.00 | 79.00 | 0.442 / 0.441 | 0.422 / 0.417 |
| clock | 22 / 32 | 98.59 | 73.96 | 0.353 / 0.356 | 0.335 / 0.335 |
| hazard | 28 / 40 | 99.52 | 65.62 | 0.471 / 0.476 | 0.450 / 0.452 |
| rift | 24 / 32 | 98.61 | 60.00 | 0.326 / 0.328 | 0.308 / 0.308 |

Cả 11 đạt ba kiểm này, trên cả hai mảnh nền ở cả hai độ phân giải.

## Khác dáng ở 32 px

Thu toàn canvas về 32² bằng Lanczos; IoU tính theo alpha **>128** đúng phiếu. Ghi thêm >16 như phép kiểm nhạy với mép. Mỗi dòng là một cặp trong cột So với, không bỏ cặp khó.

| Icon | So với | IoU >128 ≤0,80 | IoU >16 phụ |
|---|---|---:|---:|
| next-stage | menu-play | 0.290837 | 0.374150 |
| next-stage | streak | 0.530744 | 0.637168 |
| next-stage | retry | 0.329193 | 0.424802 |
| bay-full | stat-evenness.r2 | 0.345178 | 0.355856 |
| bay-full | ../parts/mag-full | 0.375661 | 0.389671 |
| kills | stat-accuracy.r2 | 0.761905 | 0.773723 |
| kills | objective | 0.445748 | 0.472296 |
| stat-accuracy | kills.r2 | 0.761905 | 0.773723 |
| stat-accuracy | objective | 0.455696 | 0.486047 |
| stat-accuracy | clock.r2 | 0.756614 | 0.759524 |
| stat-evenness | bay-full.r2 | 0.345178 | 0.355856 |
| stat-evenness | stat-wpm.v2 | 0.621849 | 0.614815 |
| stat-new-word | stat-words | 0.788095 | 0.840000 |
| stat-new-word | learning-rule | 0.588384 | 0.620930 |
| stat-words | stat-new-word.r2 | 0.788095 | 0.840000 |
| stat-words | keyboard.r2 | 0.501253 | 0.484018 |
| keyboard | ../parts/keycap | 0.737705 | 0.766667 |
| keyboard | stat-words | 0.501253 | 0.484018 |
| clock | retry | 0.445070 | 0.552764 |
| clock | stat-time | 0.535484 | 0.616477 |
| hazard | warning | 0.780000 | 0.772455 |
| hazard | surge | 0.552632 | 0.645833 |
| rift | surge | 0.331897 | 0.458955 |
| rift | warning | 0.495968 | 0.498258 |

**Mọi cặp bắt buộc đạt theo >128.** Riêng New-word read–Words có IoU phụ >16 = **0,840000**, vượt 0,80; không giấu kết quả này. Theo ngưỡng yêu cầu >128 cặp là 0,788095, khá sát. Claude cần xem mắt phía trên và hai thẻ phía sau ở cỡ thật.

**Cặp Kills–Accuracy:** IoU >128 **0,761905**, >16 **0,773723**. [Cặp 28/40 px trên hai mảnh UI, 1×](../../games/typing-survival/art-src/_review/242-kills-accuracy-v3-1x.png), [bản point 4×](../../games/typing-survival/art-src/_review/242-kills-accuracy-v3-4x.png). Nhìn 28 px: một hình có X lớn, hình kia có vòng bia và mũi tên; tự đọc phân biệt được. Không thay điểm chấm trong game.

[Probe lề Keyboard](242/keyboard-margin-probe.json) giữ mọi số thử. Chọn mức lớn nhất trong dải hợp lệ để phím rõ hơn, không dịch tâm, đổi tỷ lệ ngang/dọc hay sửa mặt nạ.

## Đọc bỏ nhãn và KA5 ở 720p 1×

Đã mở tờ PNG 260×528 ở 100%, icon theo cỡ từng hàng, bỏ nhãn và đảo thứ tự. Ghi câu 3–5 chữ trước khi đối chiếu lại cột Ý mới; [ghi đầu](242/blind-notes-v1.md), [ghi sau sửa](242/blind-notes-final.md), [tờ bản giao](242/final-delivery/blind-1x.png). Bản giao Steadiness được xem lại sau lượt 2: “Thanh ngang bọt lam”.

**Giới hạn:** người tạo đã biết prompt, nên phép này là tự nhận dạng bỏ nhãn, **không phải đọc mù độc lập**. Chưa xác lập Kiểm 8 theo mức độc lập; Claude cần chấm lại. Không cộng 2 điểm Đọc được chỉ dựa vào câu tự đọc.

| Tên | Câu tự đọc 720p | Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp | Q |
|---|---|---|---:|
| next-stage | Mũi tên qua cổng | 2 / 1,5 / 1,5 / 2 / 1 | 8 |
| bay-full | Ba viên đạn đứng | 2 / 1,5 / 2 / 2 / 1 | 8,5 |
| kills | Ngắm chữ X nhỏ | 2 / 1,5 / 2 / 2 / 1 | 8,5 |
| stat-accuracy | Bia tròn cắm tên | 2 / 1,5 / 2 / 2 / 1 | 8,5 |
| stat-evenness | Thanh ngang bọt lam | 2 / 1,5 / 2 / 2 / 1 | 8,5 |
| stat-new-word | Mắt trên thẻ nhỏ | 2 / 1,5 / 2 / 2 / 1 | 8,5 |
| stat-words | Hai thẻ chữ chồng | 2 / 1,5 / 2 / 2 / 1 | 8,5 |
| keyboard | Bàn phím hàng phím | 2 / 1,5 / 2 / 2 / 1 | 8,5 |
| clock | Đồng hồ nút bấm | 2 / 1,5 / 2 / 2 / 1 | 8,5 |
| hazard | Tam giác nứt sáng | 2 / 1,5 / 1,5 / 2 / 1 | 8 |
| rift | Khe cửa tím dọc | 2 / 1,5 / 2 / 2 / 1 | 8,5 |

Các câu không còn trùng cách đọc sai trong phiếu. Điểm là tự chấm trên bản hậu kỳ ở cỡ 720p; không phải xác nhận của hai giám khảo hoặc chủ dự án. Chi tiết sơn tay không dùng để bù cho nghĩa ở cỡ nhỏ.

## Tờ xem cần dùng

- **Bản duyệt cuối:** [242-sheet-v4.jpg](../../games/typing-survival/art-src/_review/242-sheet-v4.jpg).
- Tách trang để mở 100%: [trang 1](../../games/typing-survival/art-src/_review/242-sheet-v4-page-1.jpg), [trang 2](../../games/typing-survival/art-src/_review/242-sheet-v4-page-2.jpg), [trang 3](../../games/typing-survival/art-src/_review/242-sheet-v4-page-3.jpg).
- Hàng 1 master 256; hàng 2 1080p 1× trên button/panel; hàng 3 720p 1× trên button/panel; hàng 4 crop vùng icon của hàng 3 phóng point 4×; hàng 5 đủ icon cột So với ở cùng cỡ 720p; hàng 6 icon đang dùng cạnh bản mới (Words lấy Keyboard cũ).
- Nguyên ô gồm nhãn phóng 4× nằm riêng trong proofs-v3; hàng 4 tờ tổng chỉ lấy vùng icon để tờ vẫn xem được.
- Tờ yêu cầu tên `242-sheet.jpg` vẫn giữ nguyên. Lượt đầu có cắt nhãn dài ở 1080p; v2 sửa chiều rộng; v3 đo lại chiều cao chữ đúng 60% bằng bitmap; v4 cắt vùng phóng theo riêng chiều rộng từng icon để không lọt mảnh nhãn Time/Rift vào hàng 4. Không ghi đè/xóa tờ cũ; **chỉ dùng v4 để duyệt**. Đây là khác biệt tên tờ cuối nhằm giữ luật không ghi đè.

## KA1, phạm vi và bàn giao

Mốc đầu chạy `/sbin/md5 -r` mọi file ui/icons trước khi tạo prompt, **532 file**; lúc ấy chưa có report, file hồ sơ 242 hay _review/242*. [md5-before.txt](242/md5-before.txt). Mốc sau dùng cùng công cụ; [diff](242/audit-delivery/md5-diff.txt) chỉ có dòng thêm của dữ liệu, không có dòng xóa/thay (trừ header diff). [Manifest mọi đường dẫn đích](242/audit-delivery/md5-after-all-targets.txt) gồm ảnh, prompt, report, script và proof; loại chính thư mục audit đang ghi để không tự băm đệ quy. [Tổng kết](242/audit-delivery/summary.json) ghi số thực. **532 → 656 file trong ui/icons: thêm 124, đổi 0, mất 0. Không thay hay mất file cũ.**

Không làm music, menu-profile, menu-armory, repair-pod, reduced-motion và các ảnh đã nhận khác vì ngoài bảng làm lại. Không sửa mã, manifest, công cụ chung, public/, tài liệu khác, Tu Tiên hay .wt-*. Không chạy Git ghi, build/test game, dev server, trình duyệt hoặc mạng ngoài image_gen. Không làm âm thanh. Không có capture game/raw frame mới để prune; ảnh thử và proof là hồ sơ của phiếu, được giữ nguyên.

**Claude/chủ dự án cần xem:** tờ v4 ở 100%, cặp X–bia tại 28 px; bọt Steadiness, đạn ở 20 px, khe Rift và mắt–thẻ so với chồng thẻ. Chốt ngoại lệ alpha bản thu, sắc tím và IoU phụ trước khi đóng phiếu. Sau khi Claude trỏ game sang bản mới, chấm lại ≥8 trong game ở 1280×720 và 1920×1080; phiên này không được phép tích hợp hoặc chạy game. Không có giờ chờ công cụ.
