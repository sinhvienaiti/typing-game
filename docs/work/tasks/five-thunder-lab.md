# Ngũ Lôi Oanh Đỉnh trong lab (thay Cột Lôi) · 11/11/2026

**Ai làm:** phiên lab-element-kits, trong `games/.wt-ic-lab-all` (nhánh `codex/lab-all`, lab cổng 3146). **Không commit, không push.** Chỉ đụng tệp của chiêu sét và tệp mới của việc này.

## Anh nói gì
- 07/11: cột sét phải **chỉ là tia sét đánh xuống** (không vỏ trụ, ống sáng); **nhiều tia trong 3–5 giây trên vùng rộng**, không phải một tia mảnh; dư âm là **đất nứt, cháy đen**, không phải vết màu tím.
- 11/11: chọn hướng **Ngũ Lôi Oanh Đỉnh**, tông **trắng xanh**. "hiệu ứng vfx đẹp khi có nhiều hiệu ứng chồng lên nhau… ngũ lôi thì phải dồn dập nhiều tia sét đánh lực mạnh mẽ, chứ tôi sợ bạn dùng 1 video nó k có cái hồn đó được".
- Chuẩn: `docs/games/VFX_STANDARD.md` (5 pha), skill `game-vfx-layered`, `game-vfx-production`. Mã chỉ đặt, định giờ và làm chuyển động; hình lấy từ ảnh và video.

## Nguyên liệu (đã có, anh đã duyệt)
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`, `V = …/firefly-sprint-2026-11-05/video`.
| Lớp | Ảnh trắng xanh (dùng ngay) | Video |
|---|---|---|
| Xoáy mây kiếp (tụ lực, thẻ phẳng trên trời) | `S/thunder-five-cloud-vortex-top.v2-try1.png` | chưa có bản trắng xanh |
| Ấn lôi ở tay (phóng) | `S/thunder-five-caster-seal.v2-try9.png` | chưa có |
| 4 tia đơn A–D (dồn dập) | `S/thunder-single-bolt-{a,c,d}.v2-try1.png`, `S/thunder-single-bolt-b.v2-try9.png` | chưa có |
| Đòn kết năm tia | `S/thunder-five-strike.v2-try9.png` | chưa có |
| Vụ nổ tại điểm giáng | `S/thunder-five-impact-burst.v2-try9.png` | chưa có |
| Vành sốc trên đất | `S/thunder-five-shock-ring-top.v2-try1.png` | chưa có |
| Tia điện còn sót | `S/thunder-five-lingering-arcs.v2-try1.png` | chưa có |
| Vết nứt cháy trên đất | `S/thunder-scorch-crack-top.v1-try9.png` | `V/i2v-thunder-scorch-crack-top-i2v3/take{1,2}.mp4` (đã có) |

Firefly đang bị chặn tới mai, nên **dựng trước bằng ảnh tĩnh**. Mỗi lớp đọc nguồn qua một bảng khai báo, để khi có video (flipbook) chỉ đổi một dòng, không sửa logic.

## Dựng thế nào (khoảng 3–5 giây)
1. **Tụ lực (0–0,6 s):** xoáy mây hiện trên vùng đánh, quay chậm, sáng dần; ấn lôi ở tay; cảnh tối nhẹ.
2. **Dồn dập (0,6–3,4 s):** 12–20 tia đơn, nhịp nhanh dần (khoảng 280 ms xuống 90 ms). Mỗi tia chọn ngẫu nhiên có hạt giống cố định: hình A–D, lật ngang, cỡ 0,8–1,25, điểm rơi trong vùng rộng (không trùng điểm vừa đánh). Tia là **chớp**: sáng đủ ngay khung đầu, sống 3–6 khung, nháy lại 1–2 lần ở độ sáng thấp hơn.
3. **Mỗi tia rơi kéo theo:** chớp sáng toàn cảnh rất ngắn; vụ nổ tại điểm chạm; vành sốc lan; một vết nứt cháy mới (giữ lại tới dư âm); quái trong tầm giật lùi; rung màn hình theo cỡ tia; móc tiếng sét riêng (dùng tiếng sét sẵn có trong lab, đổi cao độ ngẫu nhiên).
4. **Đòn kết (3,4–4,0 s):** năm tia thân dày cùng giáng vào giữa vùng, vụ nổ và vành sốc lớn nhất, rung mạnh nhất.
5. **Dư âm (4,0–5,5 s):** các vết nứt còn rực rồi nguội dần; tia điện sót nhảy trên đất; khói mỏng.

Luật ánh sáng: chỉ lõi mảnh được HDR; quầng và vành ≤ 0,9 mỗi kênh; không hạ bloom chung. Không có trụ, ống hay cột trơn ở bất kỳ khung nào. Có bản giảm chuyển động (bỏ chớp toàn cảnh và rung).

## Xong khi
- Trong lab có nút và phím gọi chiêu trên một nhóm quái giả, đồng hồ bước cố định (cùng hạt giống ra cùng khung).
- Thư mục `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/five-thunder-lab/` có `ABOUT.md`, một clip 1280×720 từ camera chơi, tấm khung hình theo pha, và số đo: khung đầu mỗi tia ≥ 95 % đỉnh; trắng xoá ≤ 6 % khung; phần khung hình chiêu phủ ở đỉnh (mục tiêu ≥ 20 %); thời gian khung so với ngân sách.
- Test của lab chạy qua; `vite build` không kéo trang lab vào bản người chơi.
- Xoá khung thô của mình bằng `tools/capture-prune`. Báo cáo ≤ 300 chữ: đã làm gì, số đo, chỗ chưa đạt. **Không tự chấm điểm đẹp**; Codex chấm mù sau.

## Anh sửa pha tụ lực (12/11 08:5x)
"cái vòng tròn xuất hiện đầu tiên nó k phù hợp tý nào, thả làm kiểu dưới mặt đất xuất hiện 1 vòng tròn trận pháp dạng của lôi hiển thị từ bé rồi to dần 1 cách nhanh chóng, sau đó sấm sét đánh ra như hiện tại sẽ đẹp hơn nhiều".
→ Bỏ xoáy mây trên trời. Tụ lực = **trận pháp lôi trên mặt đất** tại vùng đánh: hiện từ bé, phóng to rất nhanh (≈ 0,25–0,35 s, nhanh dần rồi dội nhẹ), sáng dần, chạy tia điện quanh vành; rồi các tia giáng xuống như hiện tại, tia rơi trong lòng trận. Ảnh trận pháp lôi nhìn từ trên: phiếu Codex 345; tạm dùng `thunder-five-shock-ring-top.v2-try1.png` làm trận cho tới khi có ảnh mới.

## Vòng 21 · đòn kết tám cột lôi từ linh kiện (12/11 16:2x)
Điểm mù bản 20: 7,2 và 7,0 (`docs/codex-queue/361-report.md`, `361b-report.md`); bản 19: 7,2 và 6,7. Anh ra hai luật mới:
- **Linh kiện, không video trọn cảnh.** "tạo 1 tia, rồi tự làm cho từng tia hiển thị theo hướng bạn muốn… tạo 3–4 tia hoặc các thứ phụ rồi tự ghép lại". Bỏ thẻ `fan` (quạt năm tia) và thẻ `gather` khỏi đòn kết; đưa hai thẻ vào `docs/games/tu-tien/skills/VFX_LIBRARY.md` (không xoá tệp). Mọi lớp của đòn kết ghép từ linh kiện đã có: tia A–D (flipbook `-wg-hi`), `burst`, `ring`, ba vết đất (`scarHot`, `thunder-scar-lichtenberg.v1-try9.png`, `scarCold`), mây mực, hạt.
- **Đòn kết = tám cột lôi toả tám hướng chạy hết vùng camera.** "làm khoảng 8 cột lôi toả ra 8 hướng di chuyển đến hết màn".

Dựng đòn kết (thay pha quạt, giữ nghỉ im 180 ms và thu năng lượng 0,4 s nhưng thu bằng 40 hạt bay lên + mây sáng dần, không dùng thẻ gather):
1. Một tia dày giáng đúng tâm trận (tia A hoặc D, cỡ 1,6), vụ nổ + vành sốc lớn nhất, rung mạnh nhất. Khung đầu đủ sáng.
2. Ngay khung sau: 8 cột xuất phát từ tâm, 4 hướng chính trước, 4 hướng chéo lệch **3 khung** sau. Mỗi cột là **một tia đơn A–D** (chọn theo hạt giống, lật ngang ngẫu nhiên, 2 cột cạnh nhau không cùng hình), thân nghiêng 10–15° theo hướng chạy, chạy với tốc độ ra tới mép vùng camera trong ≈ 0,5 s; cứ 3–4 khung tia đổi khung flipbook để thân nhấp nháy, không trượt như một tấm ảnh.
3. Mỗi cột kéo theo phía sau: một vệt sẹo Lichtenberg kéo dài theo hướng chạy (decal, xoay theo hướng, dài dần theo quãng cột đã đi), vài vụ nổ nhỏ `burst` cỡ 0,5 rải cách 2 m, hạt tia văng ra hai bên. Quái trên đường cột bị giật lùi theo hướng cột.
4. Càng xa tâm cột càng mờ (cường độ 1,0 ở tâm → 0,45 ở mép), hai cột phía nam (về phía camera) ngắn hơn 40 % và mờ hơn, để không che nhân vật. Nếu vẫn che, bỏ còn 6 cột (bỏ hai cột nam-đông, nam-tây) và ghi rõ.
5. Dư âm: 8 vệt sẹo hình sao còn rực rồi nguội, thay cho năm vết hàng ngang; sẹo nguội khác nhau về cỡ và hướng nhánh (xoay + cỡ 0,8–1,3 theo hạt giống).

Bốn sửa còn lại cả hai giám khảo nêu, làm cùng vòng:
- **Khe tối giữa tia (Z06/Z10):** tán nhánh và quầng chân mỗi tia hạ còn ≤ 0,7, lõi giữ HDR; hai tia dồn dập không được giáng cách nhau dưới 2,5 m trong cùng 6 khung.
- **Trận nhường tia:** từ tia đầu tiên, vành chữ và năm xoáy xuống 0,45 (đang 0,6); trận bám sân: tăng góc phối cảnh (thẻ phẳng đúng mặt sân, không nâng), mép ngoài mờ 8 %.
- **Bỏ "hoa tinh thể" (Z09/Z03):** vụ nổ tại điểm chạm chuyển sang thẻ `burst` đặt phẳng bám đất (flat), cỡ ngang 1,4 × cao 0,6, hất hạt ra ngang; không thẻ dựng đứng ở điểm chạm ngoài thân tia.
- **Vết đất biến thiên (Z08):** mỗi vết xoay ngẫu nhiên, cỡ 0,8–1,3, chọn 1 trong 3 ảnh; tương phản với gạch: lõi sẹo tối hơn sân ≥ 25 % độ sáng.

Cổng cứng không đổi: trắng xoá zoom cận ≤ 6 %, khung đầu ≥ 95 % đỉnh, bước p95 ≤ 2,0 ms, không lùi cột nào trong SCORECARD. Ghi `measurements-v21.md`, hàng v21 trong SCORECARD, clip `ngu-loi-lab-v21-web.mp4` và tấm pha vào `owner-review/2026-11-12/tu-tien/five-thunder-lab/`. Âm hush vẫn chờ gói âm. Báo cáo ≤ 300 chữ, không tự chấm đẹp.

## Vòng 22 · tám cột phải đọc ra là chạy ngang (12/11 16:3x)
Bản 21 đạt ba cổng cứng (trắng xoá 2,3 %, khung đầu 20/20, p95 1,7 ms) và tám vệt sẹo hình sao đọc rõ. Nhưng trên tấm pha, tám cột ở 3,53–3,93 s đọc như một chùm sét cao quanh trận, không ra là cột chạy tới mép màn: tia vẽ đứng cao gấp đôi quãng chạy, nên mắt thấy chiều cao chứ không thấy chuyển động ngang; khung cao trào vẫn là một mảng sáng giữa, không có khe tối. Chưa chấm mù; chấm ở bản 22. Sửa:
1. Cột = tia đơn cỡ 0,6 (thấp), nghiêng 30° theo hướng chạy; chân tia bám đất, ngọn ngả về phía trước.
2. Quãng chạy tới đúng mép vùng camera chơi (đo từ tâm trận tới mép khung theo từng hướng, không phải một bán kính chung); tốc độ chậm lại: 0,8 s tới mép, tốc độ giảm dần ở 30 % cuối.
3. Dấu chuyển động: vệt sẹo kéo sáng (rực) ngay sau chân cột rồi nguội dần phía sau, dài dần theo quãng; hạt tia văng ngược hướng chạy.
4. Khe tối giữa cột: tám cột không cùng khung; hướng chính và chéo lệch 3 khung giữ; thêm mỗi cột lệch ngẫu nhiên 0–2 khung; quầng cột ≤ 0,5; không chớp toàn màn trong lúc cột chạy (chỉ chớp ở tia tâm).
5. Phủ khung không được lùi dưới 9,9 % (v21); trắng xoá ≤ 6 %, khung đầu ≥ 95 %, p95 ≤ 2,0 ms.
Giao như vòng 21 với hậu tố v22; tấm pha phải có 4 khung liên tiếp của một cột để thấy nó di chuyển.

## Vòng 23 · vệt tám cột bằng dải nứt sét thật (12/11 18:1x)
Anh (sau v22): vệt tám hướng "đang kiểu vệt tự style, nhìn rất xấu, đáng lẽ nên là những vệt dạng sấm sét in dưới, hoặc nứt đất, có rực lửa 1 chút". Nguyên nhân: kéo dãn ảnh vết tròn Lichtenberg. Linh kiện mới (Codex 366, `docs/codex-queue/366-report.md`), trong `S`: `thunder-trail-rock.v1-try*.png` và `thunder-trail-glow.v1-try*.png` (2048×256, lặp liền theo x, chồng khít), `thunder-trail-cap.v1-try*.png` và `thunder-trail-cap-glow.v1-try*.png` (đầu dải, 512×256). Lấy đúng try báo cáo 366 chọn.
1. Thay vệt Lichtenberg kéo dãn bằng dải: mỗi cột đặt nối tiếp các đoạn dải (decal phẳng trên sân, xoay theo hướng cột), **không kéo dãn**: tỉ lệ đoạn giữ 8:1, bề ngang ≈ 1,6 m; đoạn mới hiện ra ngay sau chân cột khi cột đi qua; đặt cap ở điểm cột dừng. Lệch UV ngẫu nhiên mỗi cột để tám vệt không giống nhau.
2. Lớp glow cộng sáng: rực đầy khi cột vừa qua, tắt dần trong 0,8 s theo khoảng cách sau chân cột (gần chân sáng nhất), rồi còn ánh than mờ 0,15 tới hết dư âm; lớp rock giữ tới hết dư âm rồi mờ.
3. Bỏ hẳn vệt Lichtenberg kéo dãn khỏi tám cột (vết tròn dưới tia đơn của pha dồn dập giữ nguyên). Ghi ảnh cũ vào `VFX_LIBRARY.md` nếu chưa có.
Cổng cứng giữ (trắng xoá ≤ 6 %, khung đầu ≥ 95 %, p95 ≤ 2,0 ms). Giao `measurements-v23.md`, hàng v23 SCORECARD, clip `ngu-loi-lab-v23-web.mp4`, tấm pha có khung dư âm 4,5 s ở camera chơi và zoom cận vệt. Không commit. Báo cáo ≤ 300 chữ.

## Vòng 24 · tám cột bằng cột lôi bện (12/11 19:4x)
Anh (sau v23): tám hướng nên dùng "những dạng hình cột", tia đơn "dạng nhành cây, k hợp"; sau khi xem ba cột Codex 367: "tại sao không dùng cả 3, lôi điện thì dùng nhiều hình dạng cũng được". Anh đã duyệt cả ba (luật mới: mọi ảnh anh kiểm trước khi dùng).
Linh kiện, trong `S`: `thunder-column-a.v1-try1.png` (bện chặt), `thunder-column-b.v1-try1.png` (bện thoáng), `thunder-column-c.v1-try1.png` (hai bó quấn nhau); nền đen, khổ 1024×1536, chân cột trên một hàng pixel (báo cáo `docs/codex-queue/367-report.md`). Các ảnh `-core` của Codex **không dùng** (chưa chồng khít).
1. **Lõi:** tách lõi từ chính mỗi ảnh cột bằng script (giữ điểm ảnh sáng nhất, ví dụ độ sáng > 0,8, làm mờ nhẹ 1 px), lưu cạnh nó là `thunder-column-{a,b,c}-core.lab.png`. Đây là mặt nạ lấy từ ảnh đã duyệt, không vẽ hình bằng code.
2. **Tám cột:** thay tia đơn A–D bằng cột a/b/c; hai cột cạnh nhau khác kiểu; lật ngang ngẫu nhiên; chân cột bám mặt sân, thân thẳng đứng (bỏ độ nghiêng 30° của v22, cột không cần nghiêng nữa); cỡ cao khoảng 5 m ở camera chơi.
3. **Nhấp nháy:** thân cột ở mức 0,6–0,8 dao động chậm; lõi chớp ngẫu nhiên 2–4 khung một lần ở mức HDR như tia; mỗi cột lệch pha. Thân cột trôi theo đường chạy, giữ tốc độ và dải nứt sét của v23.
4. Tia đơn A–D vẫn dùng cho pha dồn dập và tia tâm đòn kết.
Cổng cứng giữ (trắng xoá ≤ 6 %, khung đầu ≥ 95 %, p95 ≤ 2,0 ms). Giao `measurements-v24.md`, hàng v24 SCORECARD, clip `ngu-loi-lab-v24-web.mp4`, tấm pha có 4 khung liên tiếp của một cột và zoom cận ba kiểu cột. Không commit. Báo cáo ≤ 300 chữ.

## Vòng 25 · tám hướng dày hơn: nhiều cột mỗi hướng (12/11 20:0x)
Anh (sau v24): "đoạn lôi toả ra vẫn chưa đạt, nó quá mỏng, nên cho nhiều cột lôi để nó dày hơn thì hợp lý hơn".
1. Mỗi hướng là **một chùm 3 cột** thay vì 1: cột giữa và hai cột hai bên lệch ngang 1,0–1,4 m, chạy cùng hướng; hai cột bên xuất phát trễ 2–4 khung và ngắn hơn 15 %; ba cột trong chùm khác kiểu a/b/c; tổng 24 cột. Cao cột giữa 7 m (v24: 5 m), hai bên 5,5–6 m.
2. Dải nứt sét: một dải rộng hơn (≈ 2,4 m) dưới cột giữa, hai dải mảnh (≈ 1,2 m) dưới hai cột bên, cùng một rãnh chính nên đọc là một vệt dày.
3. Giữ khe tối giữa các cột (thân 0,6–0,8, chỉ lõi HDR); không chớp toàn màn khi cột chạy.
4. Nếu bước p95 vượt 2,0 ms: gộp vẽ cột (instancing một lượt cho 24 cột) trước khi bớt số cột; chỉ bớt khi gộp vẫn không đủ, và ghi rõ.
Cổng cứng giữ (trắng xoá ≤ 6 %, khung đầu ≥ 95 %, p95 ≤ 2,0 ms đo khi máy rảnh). Giao measurements-v25.md, hàng v25 SCORECARD, clip `ngu-loi-lab-v25-web.mp4`, tấm pha có khung tám chùm đang chạy ở camera chơi. Không commit. Báo cáo ≤ 300 chữ.

## Vòng 26 · sửa ba lỗi lớn của v25 (12/11 21:1x)
Anh: "bộ ngũ lôi tôi thấy chưa ổn, bạn tự chấm xem". Điều phối tự chấm v25 khoảng 5,5/10 (không phải giám khảo mù) vì:
1. **Vệt dư âm là dải đen thẳng, đều, đặc và chạy ra ngoài mép sân** (tấm pha 4,67 và 5,50 s). Sửa: vệt **dừng ở mép sân** (cắt theo hình chữ nhật sân, không vượt ra ngoài); thuôn nhỏ dần về cuối (bề ngang 100 % ở tâm còn 35 % ở cuối); bề ngang dao động ±20 % dọc chiều dài; lớp rock dùng alpha của ảnh (mép vỡ), độ đậm tối đa 0,75 (không đen đặc); lớp glow còn ánh than 0,2 trong khe tới hết dư âm. Ba chùm cạnh nhau ra ba vệt khác UV.
2. **Cột không đọc ở camera chơi** (55° từ trên làm cột đứng bị ép ngắn; ở zoom cận chùm thành búi trắng). Sửa: (a) thêm **dải sét bò sát đất** dưới chân mỗi chùm: dùng tia đơn A–D đặt **nằm phẳng trên sân**, xoay theo hướng chạy, nối tiếp theo chân chùm, đổi khung mỗi 2–3 khung, sáng hơn thân cột (lõi HDR); (b) thân cột **ngả về phía camera** 25° để không bị ép ngắn; (c) mỗi chùm giữ khe tối: ba cột cách nhau ≥ 1,2 m, thân 0,55–0,7, chỉ lõi HDR.
3. **Trận lấn át nửa đầu** (0,6–3,4 s). Sửa: trận và năm xoáy xuống 0,35 ngay từ tia đầu (v25 0,45), vành chữ ngoài 0,25.
Cổng cứng giữ; p95 đo khi máy rảnh (không có Codex chạy). Giao measurements-v26.md, hàng v26 SCORECARD, clip `ngu-loi-lab-v26-web.mp4`, tấm pha cùng các mốc như v25 (để so). Không commit. Báo cáo ≤ 300 chữ.

## Vòng 27 · tám dải sét bò sát đất, cột bùng ở mép sân (12/11 22:3x)
Anh để điều phối tự quyết ("bạn tự làm theo đề xuất đi"). Điều phối tự chấm v26 khoảng 6/10: cột đứng bị camera 55° ép ngắn, 24 cột chỉ còn vệt trắng xù; sét bò đất của v26 gần như không thấy; vệt dư âm quá mảnh như vết cào. Chọn **hướng 2**: thứ chạy ngang mặt đất mới đọc rõ từ trên cao.
1. **Tám dải sét bò sát đất là vai chính của pha toả:** mỗi hướng một "con rắn điện" chạy từ tâm ra mép sân trong 0,8 s: ghép từ tia đơn A–D **nằm phẳng trên sân**, xoay theo hướng chạy, nối tiếp 3–4 tia một dải, rộng ≈ 1,8 m, uốn lượn nhẹ (lệch ngang ±0,6 m theo sin dọc đường), đổi khung mỗi 2 khung; đầu dải sáng nhất (lõi HDR như tia đơn), thân sau đầu giảm còn 0,5 trong 0,3 s. Dải nứt sét v23 hiện ngay sau đầu dải như cũ.
2. **Cột chỉ bùng ở mép sân:** khi đầu dải chạm mép, một chùm 3 cột (a/b/c) bùng lên tại đó, cao 7 m, ngả 25° về camera, sống 0,35 s rồi tan; vụ nổ phẳng `burst` và vành sốc tại chân. Bỏ 24 cột chạy suốt đường.
3. **Vệt dư âm dày lại vừa phải:** bề ngang 1,6 m ở tâm, thuôn còn 50 % ở mép, độ đậm tối đa 0,6, giữ ánh than 0,2 trong khe; vẫn dừng trong sân.
4. Giữ trận 0,35 từ tia đầu.
Cổng cứng giữ; đo p95 khi không có Codex chạy (có một phiếu Codex đang chạy: chờ nó xong). Giao measurements-v27.md, hàng v27 SCORECARD, clip `ngu-loi-lab-v27-web.mp4`, tấm pha cùng mốc v26 cộng 4 khung liên tiếp của một dải đang chạy. Không commit. Báo cáo ≤ 300 chữ.

## Vòng 28 · dải sét đủ dày ở camera chơi (12/11 23:0x)
Điều phối tự chấm v27 khoảng 6,3/10 (v26: 6). Đã đúng hướng: tám dải chạy ngang mặt đất giờ đọc ra từ camera chơi. Còn: sân rộng nên dải 1,8 m và vệt 1,6 m chỉ thành nét mảnh như kẻ thước; vệt dư âm thẳng tắp; chùm cột ở mép nhỏ, gần như không thấy.
1. **Dải sét dày gấp đôi:** rộng ≈ 3,6 m, gồm 2 lớp tia đơn chồng lệch nhau 0,5 m (một lớp lõi sáng, một lớp nhánh 0,6); thêm **vũng sáng mặt đất** dưới đầu dải (decal mềm tròn dẹt 6 × 3 m, ≤ 0,9 mỗi kênh, trắng ngà ấm) đi theo đầu dải, tắt trong 0,25 s phía sau.
2. **Vệt dư âm rộng 3 m ở tâm, thuôn còn 50 %**, đường đi uốn nhẹ theo đúng đường sin của dải (không thẳng tắp), lớp rock độ đậm 0,6.
3. **Chùm cột ở mép to hơn:** cao 10 m, ngả 30° về camera, sống 0,45 s, vụ nổ phẳng cỡ 1,5 và vành sốc lớn tại chân; rung màn hình nhẹ khi tám chùm cùng bùng.
4. Không đổi các pha trước đòn kết.
Cổng cứng giữ; đo p95 khi không có Codex chạy (hai giám khảo Codex 371/371b đang chạy: chờ xong rồi đo). Giao measurements-v28.md, hàng v28 SCORECARD, clip `ngu-loi-lab-v28-web.mp4`, tấm pha cùng mốc v27. Không commit. Báo cáo ≤ 300 chữ.
**Sửa vòng 28 (anh, 12/11 23:1x: "hãy thử làm cho vệt sấm sét toả ra dày và to xem sao"):** tăng mạnh hơn mục 1–2 ở trên: dải sét rộng ≈ 5,5 m (gấp 3 v27), **3 lớp** tia đơn chồng lệch (lõi sáng giữa, hai lớp nhánh hai bên 0,6), tia của lớp nhánh cỡ 1,3 để nhánh toả ra rộng; vũng sáng mặt đất 8 × 4 m; vệt dư âm rộng 4,5 m ở tâm, thuôn còn 55 %, nhiều nhánh nứt toả hai bên (dùng thêm vết `thunder-scar-lichtenberg` đặt phẳng dọc vệt, mỗi 3 m một vết, cỡ 0,6–1,0, xoay ngẫu nhiên). Trắng xoá vẫn ≤ 6 %: nếu vượt, hạ lớp nhánh trước, giữ lõi.

## Vòng 29 · từ v28b: chùm cột ở mép, vệt sắc, vũng sáng gọn (13/11 00:1x)
Điều phối tự chấm v28b khoảng 7,2/10 (v27: 6,3): tám dải sét to giờ đọc rõ thành ngôi sao toả, vệt dư âm rộng có nhánh. Còn yếu:
1. **Chùm cột ở mép gần như không thấy** (tấm 4,33 và 4,67 chỉ còn vài sợi mảnh ở rìa). Sửa: tại mép, chùm 3 cột cao 10 m với **lõi HDR bằng tia đơn** (không chỉ thân 0,6), cộng vụ nổ phẳng cỡ 2,0 và vành sốc; sống 0,5 s; nếu cột vẫn mảnh ở camera chơi thì nhân 1,5 bề ngang thẻ cột.
2. **Vũng sáng mặt đất làm mờ sương** quanh dải (tấm 4,33). Sửa: vũng sáng hẹp lại 6 × 2,5 m, mép cứng hơn (falloff ngắn), tắt trong 0,15 s phía sau đầu dải.
3. **Vệt dư âm 5,5 s hơi nhoè**: lớp rock dùng đúng độ phân giải ảnh (không mip mờ: bật anisotropy 8 cho decal dải), độ đậm 0,65, viền khe nứt sắc.
4. Giữ mọi thứ khác của v28b.
Cổng cứng giữ. **p95 đo khi máy rảnh**: chờ Codex (phiếu 375 đang chạy) xong, đo ba lần; đo lại luôn v28b trong cùng lượt. Giao measurements-v29.md, hàng v29 (và p95 v28b) trong SCORECARD, clip `ngu-loi-lab-v29-web.mp4`, tấm pha cùng mốc v28b. Không commit. Báo cáo ≤ 300 chữ.

## Vòng 30 (vòng cuối của đêm) · bỏ cục khói xám, làm p95 đạt chắc (13/11 00:4x)
Điều phối tự chấm v29 khoảng 7,4/10 (v28b: 7,2): chùm cột ở mép giờ thấy rõ, vệt dư âm sắc. Còn:
1. **Cục khói xám như bông** ở đầu mỗi dải và quanh tâm (tấm 4,13 và 4,33; zoom 3,93 thành một đám sương xám lớn). Tìm lớp gây ra (khói `smoke` hay quầng `burst` phẳng mở rộng) và **thay** bằng lớp cùng vai trò đẹp hơn (luật anh: không gỡ mà không thay): ở đầu dải là chùm tia lửa nhỏ văng thấp (`sparks`) và một chớp lõi trắng ngà 2 khung; khói chỉ còn mỏng, tối (pha thường, không cộng sáng), ≤ 0,35.
2. **p95 đạt chắc chắn:** đo v29 nhiều lần đều 2,0–2,3 ms nên coi là vượt thật, không đổ cho máy. Gộp vẽ ba lớp tia của mỗi dải và 24 thẻ cột thành một lượt mỗi loại (instancing hoặc gộp hình), giới hạn hạt mỗi dải; mục tiêu ≤ 1,8 ms ở ba lần đo khi máy rảnh. Không đổi hình.
3. Giữ mọi thứ khác của v29.
Giao measurements-v30.md, hàng v30 SCORECARD, clip `ngu-loi-lab-v30-web.mp4`, tấm pha cùng mốc. Không commit. Báo cáo ≤ 300 chữ. Sau vòng này dừng, chờ anh xem.

## Vòng 31 · cột lôi chạy cùng dải từ tâm tới mép (13/11 07:4x)
Anh xem v30: "thấy khá ổn, nhưng vì sao lúc toả ra 8 cột lôi, nó như kiểu đi dưới lòng đất, chỉ khi chạm vào cuối màn thì 8 cột lôi mới xuất hiện… sao k phải là cột xuất hiện ngay từ đầu". Giữ toàn bộ v30, chỉ đổi:
1. **Chùm cột trên đầu dải từ khung đầu:** mỗi hướng một chùm 3 cột (a/b/c, khác kiểu) đứng ngay trên đầu dải sét, xuất hiện ở tâm cùng lúc dải bắt đầu chạy và **đi theo đầu dải suốt quãng** tới mép. Cột giữa cao 8 m, hai cột bên 6 m; ngả 30° về camera; thân 0,6–0,75 dao động, lõi HDR chớp mỗi 2–4 khung (lệch pha từng cột); chân cột gắn đúng chớp lõi trắng ngà ở đầu dải.
2. **Tới mép:** chùm cột phình lên 1,4 lần trong 0,1 s (cột giữa 11 m), vụ nổ phẳng cỡ 2,0, vành sốc, rồi tan trong 0,35 s (thay cho chùm bùng riêng ở mép của v30).
3. Giữ khe tối: ba cột trong chùm cách nhau ≥ 1,2 m; tám chùm không chớp lõi cùng khung.
4. Hiệu năng: 24 cột vẽ một lượt (instancing như v30). Đo p95 khi máy rảnh, kèm đối chứng v30 cùng lượt; v31 không được chậm hơn v30 quá 0,1 ms.
Cổng cứng giữ. Giao measurements-v31.md, hàng v31 SCORECARD, clip `ngu-loi-lab-v31-web.mp4`, tấm pha cùng mốc v30 cộng 4 khung liên tiếp của một chùm đang chạy. Không commit. Báo cáo ≤ 300 chữ.
**Bổ sung vòng 31 (anh, 13/11 07:5x: "vì sao 8 cột nhưng chỉ thấy 4 hướng xuất ra lôi"):** nguyên nhân trong `five-thunder.ts` (khoảng dòng 1874–1906): ba hướng về camera (`dz > 0.3`) bị `colNearK`/`colNearDim` cắt ngắn và làm mờ, hướng nam còn bị `guardM` dừng trước chỗ người chơi; ba hướng bắc chạm mép sân rất sớm vì tâm đòn gần mép bắc và lẫn vào đĩa trận. Sửa:
- Bỏ làm mờ hướng gần camera (độ sáng như các hướng khác); chỉ giữ ngắn hơn ở **đúng hướng nam** đủ để không chạm người chơi; đông nam và tây nam chạy hết như đông, tây.
- Mỗi hướng có **độ dài nhìn thấy trên màn ≥ 60 % hướng dài nhất** (đo bằng pixel ở camera chơi, ghi bảng tám hướng vào measurements-v31.md). Hướng bắc ngắn quá thì cho chùm cột đầu dải to hơn (1,3 lần) và đầu dải chạy chậm lại để vẫn sống đủ 0,8 s, thay vì kéo dải ra ngoài sân.
- Trong 0,3 s đầu, trận dưới tâm hạ còn 0,2 để ba hướng bắc không lẫn vào vành trận.
- Tấm pha thêm một khung ở 4,0 s có đánh số 8 hướng để kiểm đủ tám.

## Vòng 32 · cột bằng video, đặc dày hơn, tám hướng chạy đều (13/11 09:4x)
Anh (sau v31b): duyệt ba video cột lôi Firefly; "phần 8 cột lôi nên đặc và dày hơn nữa, chứ hiện tại vẫn hơi mỏng và không đều ở đoạn di chuyển, cái chạy trước cái chạy sau". Giữ toàn bộ v31b, đổi:
1. **Cột dùng video:** làm flipbook từ `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video/i2v-thunder-column-{a,b,c}-i2v5/take{1,2}.mp4` theo cách các flipbook sét trước (`art-src/lab/vfx/thunder/manifest.json`, mục `-wg`), nền đen cộng sáng. **Chỉ lấy đoạn đầu trước khi mây đỉnh phình thành cục khói xám** (khoảng 0–2 s; kiểm tấm khung `owner-review/2026-11-13/tu-tien/codex-images/column-videos-sheet.jpg`), hoặc che đỉnh bằng mặt nạ dọc mờ dần ở 15 % trên. Sáu bản (3 cột × 2 take) xoay vòng để không cột nào giống cột cạnh nó. Ảnh tĩnh 367 thành dự phòng, ghi vào `VFX_LIBRARY.md`.
2. **Đặc và dày hơn:** mỗi hướng một chùm **5 cột** (giữa + 2 bên sát + 2 bên ngoài), bề ngang thẻ mỗi cột 1,5 lần v31b, cột giữa cao 9 m; khoảng cách giữa các cột trong chùm 0,8–1,0 m để đọc như một bó đặc nhưng vẫn có khe tối mảnh; thân 0,7–0,85.
3. **Tám hướng chạy đều:** cả tám chùm **xuất phát cùng một khung** (bỏ trễ 3 khung của hướng chéo và trễ ngẫu nhiên), **tới mép cùng một lúc** (tốc độ mỗi hướng = quãng của hướng đó / cùng một thời gian 0,8 s, nên hướng ngắn chạy chậm hơn); trong một chùm các cột đi sát nhau, không cột nào vượt lên trước (lệch dọc đường ≤ 0,3 m). Chớp lõi vẫn lệch pha để sống động.
4. Hiệu năng: 40 cột vẽ một lượt (instancing). p95 ≤ 2,0 ms đo khi máy rảnh, kèm đối chứng v31b cùng lượt; nếu vượt, giảm hạt trước, giữ số cột.
Cổng cứng giữ. Giao measurements-v32.md, hàng v32 SCORECARD, clip `ngu-loi-lab-v32-web.mp4`, tấm pha cùng mốc v31b + khung đánh số 8 hướng + 4 khung liên tiếp lúc chạy. Không commit. Báo cáo ≤ 300 chữ.

## Việc riêng · ba góc nhìn trong lab (13/11 10:2x)
Anh: "tạm thời chúng ta sẽ chỉnh để có 3 lựa chọn góc nhìn, 1 là góc nhìn từ trên xuống như hiện tại ở lab, 2 là góc nhìn dạng ngang sau lưng gần như mắt nhìn của nhân vật, 3 là góc nhìn dạng ngang màn hình"; về góc thấp: "nếu góc nhìn gần ngang được thì tốt, còn nếu không chúng ta cần phải xử lý trong code để nó phù hợp thêm". Không có chữ trên đầu quái (người chơi gõ ở Bàn Quyết dưới màn).
1. **Bộ chuyển góc trong lab** (phím 1/2/3 và nút): (1) như hiện nay (55°); (2) sau lưng người chơi, camera cao ~1,8–2,5 m trên đất, sau lưng 6–8 m, nhìn về phía bắc dọc đường quái, FOV 45–55°; kèm biến thể 2b chếch 25° để so; (3) nhìn ngang từ phía đông (trục camera vuông góc đường quái), quái đi từ phải sang trái, FOV 35°. Chuyển góc mượt 0,4 s.
2. **Hồ sơ hiệu ứng theo góc** (chỉ view, không đổi sim): ở góc 2 và 3, vật nằm phẳng (vệt nứt, trận, vũng sáng) được nâng 2 cm và nghiêng một phần về camera (tối đa 35°) để không bị ép dẹt; cột và tia to 1,2 lần; tách bầy quái bằng viền sáng mảnh cho boss và tinh anh.
3. **Chụp:** Ngũ Lôi v32 ở 1, 2, 2b, 3; mỗi góc một tấm pha (tụ lực, dồn dập, đòn kết, tám chùm chạy, dư âm) và clip 1280×720; ghi nhận xét đo: bao nhiêu quái thấy được, quái xa nhất bao nhiêu px, hiệu ứng nào mất.
Không đụng phần chiêu ngoài hồ sơ theo góc. Không commit. Giao `owner-review/<ngày>/tu-tien/five-thunder-lab/camera-modes-*.{jpg,mp4}`, `measurements-camera-modes.md`. Báo cáo ≤ 300 chữ.

## Vòng 33 · tám hướng bằng cột sét đổ thẳng (13/11 11:0x)
Anh duyệt cột sét đổ thẳng (Codex 378, "k cần xử lý thêm") và muốn "test với 8 cột lôi toả ra 8 hướng với dạng cột dày để xem có đẹp hơn hay k". Giữ toàn bộ v32, chỉ thay cột:
1. Cột chùm dùng `S/thunder-stream-{a,b,c}.v1-try1.png` (ảnh tĩnh) và lõi `S/thunder-stream-{a,b,c}-core.v1-try*.png` theo try báo cáo `docs/codex-queue/378-report.md` chọn (lõi B là try3). **Cột giữa mỗi chùm là A**, hai bên B và C xen kẽ. Lõi chớp ngẫu nhiên lệch pha để sét như đang đổ. Video Firefly của ba cột này đang xếp hàng; khi có, đổi sang flipbook như v32.
2. Chùm 5 cột dày như v32; tám hướng xuất phát và tới mép cùng lúc.
3. Cột bện xoắn (367 và video) ghi vào `VFX_LIBRARY.md`, không xoá.
4. Chụp ở **cả bốn góc** (1, 2, 2b, 3) như việc ba góc nhìn, kèm so sánh v32 | v33 ở từng góc tại 4,0 s.
Cổng cứng giữ. Giao measurements-v33.md, hàng v33 SCORECARD, clip `ngu-loi-lab-v33-web.mp4` (góc 1) và `camera-modes-v33-compare.{jpg,mp4}`. Không commit. Báo cáo ≤ 300 chữ.

## Vòng 34 · cột chính hai tia gãy gắt bạch kim (13/11 15:1x)
Anh chọn cột hai tia gãy gắt đã chỉnh màu bạch kim ("thử triển khai với bản gãy gắt đã chỉnh màu xem sao"); điều phối tự chấm 8,0, cao nhất trong các bản. Ảnh: `S/thunder-energy-sharp.v1-try9.png` (= `thunder-energy-column.v5-try2-grade.png`), bốn khung `S/thunder-energy-sharp-frames.v1-try9.png` (2048×768, 4 khung 512×768). Video Firefly đang làm (`i2v-thunder-energy-sharp-i2v5`); khi có, đổi sang flipbook như v32 (cắt đoạn trước khi mây phình nếu có).
Giữ toàn bộ v33 (tám hướng, xuất phát và tới mép cùng lúc, dải sét bò, vệt, góc nhìn), chỉ đổi cột:
1. **Mỗi hướng: 1 cột chính hai tia ở giữa** (cao 9 m, bề ngang thẻ theo tỉ lệ ảnh), **2 cột phụ** hai bên dùng cùng ảnh lật ngang và thu 0,7 lần, lệch 1,0–1,3 m; bỏ chùm 5 cột đổ thẳng (ghi cột 378 vào `VFX_LIBRARY.md`).
2. **Trước khi có video, cho cột sống bằng bốn khung:** đổi khung trong bốn khung mỗi 3–4 khung hình theo thứ tự ngẫu nhiên khác nhau từng cột, lõi chớp lệch pha; không lật cùng lúc mọi cột.
3. **Uy lực:** lõi sáng hơn 15 % so với ảnh (HDR ở lõi như tia đơn), quầng giữ ≤ 0,9.
4. Chụp ở cả bốn góc kèm so sánh v33 | v34 ở 4,0 s.
Cổng cứng giữ. Giao measurements-v34.md, hàng v34 SCORECARD, clip `ngu-loi-lab-v34-web.mp4`, `camera-modes-v34-compare.{jpg,mp4}`. Không commit. Báo cáo ≤ 250 chữ.

## Vòng 35 · một điểm nhấn, chừa khe nhìn quái (13/11 16:3x)
Điều phối tự chấm v34 khoảng 5,5 (lực 8,5, sống động 8,5, đọc ra sét 8,5; nhưng thứ bậc sáng 5,5 và đọc trận đấu 5,5: 24 cột cùng rực, ba chùm thành tường sáng che quái ở góc thấp; V > 0,9 zoom cận 56 %). Anh: "đồng ý, thử triển khai xem". Giữ toàn bộ v34, sửa ba việc:
1. **Một cột chính mỗi chùm:** cột giữa giữ độ sáng và cỡ hiện tại; hai cột phụ hạ còn ~50 % độ sáng thân (lõi ~60 %), bề ngang 0,7 lần, lùi ra sau cột chính 0,6 m theo hướng camera. Mục tiêu: V > 0,9 ở zoom cận ≤ 35 %.
2. **Bớt chồng lấn, luôn có khe nhìn:** tám hướng vẫn xuất phát và tới mép cùng lúc, nhưng **thời điểm bùng sáng đỉnh** của từng chùm lệch nhau 0,06–0,12 s theo vòng (không bùng cùng khung); trong mọi khung, các vùng cột có độ sáng > 0,9 không phủ quá 40 % bề ngang khung hình ở góc 2, 2b, 3 (đo và ghi).
3. **Thấy quái phía sau ở góc thấp:** ở góc 2, 2b, 3, nửa dưới thân cột (0–45 % chiều cao, trừ 10 % chân có vụ chạm đất) giảm độ đặc còn 55 % theo dải mờ dần, để thấy hình quái phía sau; ở góc 1 giữ như v34.
Đo thêm: số quái vẫn thấy rõ (không bị vùng sáng > 0,8 che quá nửa thân) lúc 4,0 s ở từng góc, so v34.
Cổng cứng giữ. Giao measurements-v35.md, hàng v35 SCORECARD, clip `ngu-loi-lab-v35-web.mp4`, `camera-modes-v35-compare.{jpg,mp4}` (v34 | v35). Không commit. Báo cáo ≤ 250 chữ.

## Vòng 36 · năm sửa của giám khảo 380/380b (13/11 17:xx)
Giám khảo mù v35: 5,8 / 6,0 (`docs/codex-queue/380-report.md`, `380b-report.md`); v20: 7,2 / 7,0. Thấp nhất ở cả hai: (e) đọc trận đấu ở mọi góc. Cả hai nêu cùng năm sửa; làm cả năm, giữ chất sét sống:
1. **Khoảng nhìn quái mọi góc (Y07, Y14–Y17):** thân cột chính hẹp 0,8 lần, quầng hẹp 0,7 lần; mạng điện sát đất ở góc thấp hạ 40 %; không chùm nào đứng che trước chùm khác ở góc 2/2b/3 quá 2 khung liền (lệch thời điểm hoặc hạ độ đặc chùm sau).
2. **Tám chùm đọc được, một chính hai phụ (Y07, Y11, Y12, Y17):** hai cột phụ tách khỏi cột chính bằng khe hở ≥ 0,5 bề rộng cột chính, độ sáng phụ 40 %, chân phụ lùi sau chân chính.
3. **Thứ bậc sáng, cứu lõi (Y06, Y10, Y11, Y17):** chỉ tia tâm đòn kết và lõi cột chính có HDR; mọi lớp khác ≤ 0,9; quầng rộng giảm; vùng cháy trắng (RGB > 245) ở Y10/Y11/Y17 không thành mảng (đo: mảng liền lớn nhất ≤ 0,5 % khung).
4. **Bớt lặp (Y07–Y08, Y11, Y14, Y17):** xen kẽ hình cột giữa các chùm: video hai tia take1 và take2, ảnh một tia `S/thunder-energy-column-1bolt.v1-try3.png` và ba tia `S/thunder-energy-column-3bolt.v1-try3.png` (cho sống bằng đổi khung và lõi chớp), lật ngang ngẫu nhiên, chiều cao 0,85–1,15; hai chùm cạnh nhau không cùng hình. Vệt nứt mỗi hướng lệch UV và bề rộng khác nhau.
5. **Tách năm pha (Y01–Y06, Y12–Y13):** thêm dấu phóng ở người thi triển (ấn lôi sáng ở tay 0,25 s cùng lúc trận hiện), tụ lực co về tâm trước đòn kết (vòng hạt hút vào 0,3 s), giữ nghỉ ngắn trước tia tâm.
Cổng cứng giữ. Giao measurements-v36.md, hàng v36 SCORECARD, clip `ngu-loi-lab-v36-web.mp4`, `camera-modes-v36-compare.{jpg,mp4}` (v35 | v36), và **gói chấm mù mới** `captures/tu-tien/judge-packet-381/packet/` cùng mốc như gói v35 (tên X01–X17, không chữ, khoá ở `captures/tu-tien/judge-five-thunder-v36/key/`). Không commit. Báo cáo ≤ 250 chữ.

## Vòng 37 · sửa thêm trước khi chấm (13/11 18:0x)
Anh: "sửa thêm trước r chấm". Giữ toàn bộ v36, sửa:
1. **Trả lực cho pha dồn dập:** tia dồn dập về độ sáng như v35 (v36 hạ ~40 %); tia dồn dập không chồng lên chùm cột nên không ảnh hưởng thứ bậc ở đòn kết. Giữ thứ bậc chỉ trong pha đòn kết.
2. **Cột phụ sắc chứ không nhoè (góc thấp):** thay cách làm phụ "mờ đi" bằng "mảnh và thấp hơn": cột phụ bề ngang 0,55 lần cột chính, cao 0,75 lần, độ sáng thân 0,6 nhưng **giữ lõi sắc** (không mờ dần cả thân, không blur); bỏ dải trong suốt nửa dưới ở cột phụ (chỉ giữ ở cột chính nếu cần thấy quái).
3. **Bề ngang vùng sáng ở góc 2 và 3 ≤ 40 %:** tăng khoảng lệch thời điểm bùng đỉnh giữa các chùm lên 0,10–0,16 s, và ở góc 2/3 các chùm hướng về phía camera (nam, đông nam, tây nam) thấp hơn 0,8 lần.
4. **Hiệu năng:** p95 ≤ 1,8 ms ở ba lần đo khi máy rảnh (v36 chạm 2,0): gộp lượt vẽ cột phụ vào cùng instancing với cột chính nếu chưa.
Cổng cứng giữ. Giao measurements-v37.md, hàng v37 SCORECARD, clip `ngu-loi-lab-v37-web.mp4`, `camera-modes-v37-compare.{jpg,mp4}` (v36 | v37), và **gói chấm mù** `captures/tu-tien/judge-packet-382/packet/` (W01–W17, cùng mốc như gói v35/v36, không chữ; khoá ở `captures/tu-tien/judge-five-thunder-v37/key/`). Không commit. Báo cáo ≤ 250 chữ.

## Vòng 38 · dùng tia sét của Thunder Pillar cho Ngũ Lôi (15/11 19:xx)
Anh (15/11, xem Thunder Pillar phím 8 trong lab): "dạng lôi này rất đẹp… chỉ là do nó tự nhiên được bọc 1 lớp trụ hình tròn xung quanh nên tôi không thích… làm giống kỹ năng Five thunders… diện tích rộng hơn to hơn, bỏ cái cột trụ tròn đi, màu sắc nó đậm hơn để tránh bị nhìn giống video".
Nguồn: flipbook `thunder-pillar` (thư mục `art-src/lab/vfx/thunder/`, video `video/thunder-pillar/take1.mp4`: tia sét tím trắng phân nhánh dày, điện bò sát đất). **Không dùng** lớp trụ sáng tròn (video `i2v-pillar-thunder-single`). Giữ v37 làm mốc, tạo v38:
1. **Tia sét chính của cả chiêu = tia Thunder Pillar** (không lớp trụ): dùng cho pha dồn dập (thay tia đơn A–D), tia tâm đòn kết (to 1,6 lần), và làm cột chính của tám chùm (thay cột video gãy gắt; cột phụ dùng cùng nguồn lật ngang, thu 0,6).
2. **To và rộng hơn:** vùng dồn dập rộng 1,4 lần v37; mỗi tia cao 1,3 lần.
3. **Màu đậm hơn, không như video dán:** đậm sắc (saturation +25 %), lõi trắng giữ HDR, nhánh và quầng đậm màu hơn; thêm vũng sáng và chớp đất đúng màu tia ở chân mỗi tia để gắn tia vào cảnh. Làm **hai biến thể màu bật bằng một nút**: (a) tím trắng như gốc, (b) nhuộm bạch kim trắng ngà vàng nhạt (canon D65 đang chốt bạch kim; anh sẽ chọn).
4. Giữ thứ bậc sáng và khoảng nhìn quái của v37; cổng cứng giữ (trắng xoá ≤ 6 %, p95 ≤ 2,0 ms khi máy rảnh).
Giao: clip `ngu-loi-lab-v38-violet-web.mp4` và `ngu-loi-lab-v38-platinum-web.mp4` (góc 1), `camera-modes-v38-compare.{jpg,mp4}` (v37 | v38 tím | v38 bạch kim ở góc 1 và 2b), measurements-v38.md, hàng v38 SCORECARD. Ghi phím/nút đổi màu để anh tự thử trong `skills-lab.html`. Không commit. Báo cáo ≤ 250 chữ.
**Sửa vòng 38 (anh, 15/11 19:xx, sau khi xem tấm hai hàng):** "hàng trên vẫn đẹp hơn, lượng năng lượng lôi dày hơn, chứ không hề thích hàng dưới cho lắm… tôi chỉ không thích vì nó có trụ bọc xung quanh, và cảm giác hơi mờ nhạt thôi". Đổi nguồn: dùng video **`video/i2v-pillar-thunder-single/take{1,2}.mp4`** (luồng năng lượng dày, nổ chân), **không** dùng `thunder-pillar` (tia tím phân nhánh). Cách bỏ "trụ bọc" và "mờ nhạt" mà giữ năng lượng:
- Kiểm trong lab xem Thunder Pillar có lớp lưới trụ/ống riêng không (ví dụ lớp của mẫu năm pha `fivePhase`): nếu có, không dùng lớp đó.
- Trong chính video, quầng sáng mờ rộng quanh lõi là thứ đọc như trụ: cắt quầng bằng đường cong mức trong shader (nâng điểm đen, ví dụ độ sáng < 0,25 về 0, 0,25–0,5 kéo giãn), giữ lõi và các tia sét dày; đậm sắc (+25–35 %) và tăng tương phản để hết mờ nhạt; mép trái phải mờ dần bằng mặt nạ dọc để không lộ hình chữ nhật.
- Phần còn lại của phiếu vòng 38 giữ nguyên (dùng cho dồn dập, tia tâm, cột chính; to rộng hơn; hai biến thể màu tím trắng gốc và bạch kim; vũng sáng chân tia).
