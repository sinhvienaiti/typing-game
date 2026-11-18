## TÓM TẮT (≤ 300 từ)

Nên giữ hướng chấm hai tầng của Claude, nhưng phải sửa ba điểm: **8 là mốc tiến bộ, nghiệm thu vẫn là hai giám khảo mù đều ≥ 8,5 trong bản chơi**; đạt kỹ thuật chưa đủ nếu lớp sai công dụng; engine sửa nhịp tổng thể nhưng không cứu được hình sai, mất bộ phận, khói nhựa hoặc chuyển động nội tại hỏng.

Đã đọc 467 kết quả của 372 job: không clip nào đạt 8 theo thước cũ. Thử sửa prompt trên cùng 10 việc chỉ tăng 5,60 → 5,95. Đây là bằng chứng để ngừng làm lại hàng loạt bằng prompt, không phải bằng chứng mọi clip đều bỏ. Có 20 ứng viên giữ để trích lớp nguồn trong §4; mốc cắt là đề xuất, chưa được chứng nhận qua từng khung và phát thực.

Ưu tiên giữ thân sao băng, lưỡi băng, ấn và chất liệu ultimate khá tốt; bổ sung nhịp, tương tác, lớp sáng/tối đúng vai trò. Hình sai thì sửa ảnh; chất liệu không có chuyển động hữu cơ thì thử Blender. Mẫu D1 kiểm soát alpha và thời gian tốt nhưng chỉ tự chấm 6,5: chưa đáng chạy lô, cũng chưa chứng minh Blender chỉ nên làm lớp phụ.

Đề xuất ba luồng tách đầu ra: giữ–chỉnh; ảnh có hình rồi I2V; chất liệu Blender. Mỗi việc có nguồn, vai trò, đoạn dùng, phép kiểm, phạm vi ghi và điều kiện chuyển luồng; làm thứ đang dùng trong lab trước. Thử hai mẫu trước mỗi lô, trình anh xem; hoàn thành một hiệu ứng năm pha trong lab rồi mới nhân rộng. Cách lai vẫn chờ demo để anh chốt.

## Phạm vi và bằng chứng

Ngày 07/11/2026 · A7 · Codex phản biện bản nháp của Claude theo yêu cầu trực tiếp của anh. Đây là tư vấn; chưa đổi quy trình chính thức, hàng việc, media hoặc mã. Không gọi trợ lý khác, tạo agent, mở trình duyệt, mở cổng, chạy build/test hoặc tạo media.

Đã đọc toàn bộ JSON trong [results](../../../.local/video-review/results/), [báo cáo C](../../codex-queue/laneC-report.md), [báo cáo D1](../../codex-queue/laneD1-report.md), [chuẩn VFX](../../games/VFX_STANDARD.md), [skill sản xuất](../../../.agents/skills/game-vfx-production/SKILL.md), [đóng gói runtime](../../../.agents/skills/game-vfx-production/references/runtime-packaging.md), luật AGENTS và điều phối. Đã xem lại sheet có sẵn của 20 clip ở §4 cùng hai mẫu D1; đọc `render.json`, `validation.json` D1; dùng ffprobe chỉ đọc thông tin 20 video. Không phát video trong host hoặc đo từng khung của 20 clip ở lần tư vấn này.

| Phạm vi dữ liệu đọc tại lần này | Kết quả |
| --- | --- |
| `batch-01`…`batch-09` | 450 lượt chấm |
| `redo-01` | 17 lượt chấm, trong đó 10 cặp việc có điểm trước/sau |
| Tổng | 467 key riêng, 372 job; 364 REDO, 103 DROP, 0 PASS; cao nhất 7,5 |
| Nối với `clips.json` hiện có | 466/467 key; thiếu metadata của `fire-ground-impact__take2` |
| Theo `mode` của metadata, trên các key nối được | I2V: 266 clip, TB 5,32, 25 clip ≥ 7; T2V: 200 clip, TB 4,90, 5 clip ≥ 7 |

Số anh đưa (I2V 184, T2V 129) là lát cắt khác với toàn bộ JSON đọc ở đây; không thay nó bằng một mẫu rồi so như cùng đợt. `mode` trong `clips.json` được công cụ suy từ trường ảnh của hàng việc, không phải kiểm chứng lịch sử tạo của nhà cung cấp. Trung bình theo mode chỉ mô tả mẫu, **không phải xác suất nhân quả**: nhóm chiêu, still, take và thời điểm khác nhau. Chưa có thử đối chứng để hứa công cụ nào có bao nhiêu phần trăm lên 8.

`clips.json` có 640 mục, nên cũng không được gọi 467 là toàn bộ kho video. Bản chấm cũ vẫn có giá trị làm chỉ mục lỗi và ưu tiên; không viết lại lịch sử REDO thành PASS.

## 1. Phản biện bản nháp của Claude

### 1.1 Chấm hai tầng là đúng, nhưng tầng nguồn cần xét đúng vai trò

Một dải khói không cần mang toàn bộ sức nặng của một chiêu cuối. Chấm tổng thể nó như chiêu hoàn chỉnh dễ khiến làm lại thứ dùng được. Tuy vậy, câu “lớp riêng cũng không đạt 8” quá tuyệt đối: một lớp độc lập vẫn có thể rất đẹp; lớp chính phô lớn vẫn phải có sức hấp dẫn riêng. Không dùng lập luận chồng lớp để hợp thức hóa vật liệu xấu.

Tầng A phải là **đủ tốt để làm đúng vai trò đã khai báo**, gồm hình, chất liệu, chuyển động cần thiết, khả năng tách nền và đóng gói. Tầng B mới là tổng thể năm pha trong cảnh chơi. Mọi thay đổi vai trò, như lấy video chém làm texture cung, phải ghi rõ và chấm A lại theo vai trò mới.

Bằng chứng: `i2v-blood-charge-fill__take1` có technical 8 nhưng fit 3, tổng 4; `i2v-light-charge-fill__take1` có technical 8 nhưng fit 2. Cung sáng chạy rồi tắt ô cũ, không thể biểu diễn lượng gõ tích lũy. Chỉ lấy technical ≥ 7 hoặc ≥ 8 làm GIỮ là sai. Ngược lại, `i2v-ult-ice-cold-silence__take2` có fit 9, motion 7: vẻ tĩnh là chủ ý, không cần thêm một cú nổ chỉ để trông nhiều chuyển động hơn. [batch-04](../../../.local/video-review/results/batch-04.json), [batch-06](../../../.local/video-review/results/batch-06.json), [batch-08](../../../.local/video-review/results/batch-08.json).

### 1.2 Engine sửa được đường bao thời gian, không thay được mọi chuyển động

Đúng: engine nên quyết định lúc bắt đầu, hướng, đường bay, tuổi, nhịp sáng, reveal và erosion. Không nên buộc một video năm giây tự đóng vai toàn bộ chiêu.

Thiếu: scale/alpha chỉ làm **cả tấm** to, nhỏ, mờ đi. Nó không tạo được đầu lưỡi chém dẫn đường, sợi khói cuộn, đỉnh sóng đổ xuống, chân thú đúng hay đá giữ nguyên khi năng lượng tắt. Ép scale mạnh dễ làm cảm giác “chiếu video” rõ hơn. Tua nhanh đoạn gần tĩnh vẫn là ảnh nhấp sáng; tua quá nhanh chất liệu có thể rung giật.

Vòng lặp lệch pha giữa nhiều instance chỉ giảm sự đồng bộ; **không chữa được đường nối trong từng instance**. Cross-fade hai hình khác dáng sinh hai viền; phát ping-pong khói làm vật chất hút ngược. Với `i2v-star-caster-seal__take1`, MAE nối/khung kề 1,20× là tín hiệu để kiểm tiếp, chưa phải chứng nhận loop. Với `i2v-wind-crescent-sym__take1`, tỷ số 3,45× cảnh báo rõ hơn nhưng vẫn không phải thước đẹp. [batch-07](../../../.local/video-review/results/batch-07.json), [batch-09](../../../.local/video-review/results/batch-09.json).

Các lớp điều khiển tiến độ phải thật sự do engine sở hữu: vòng nạp dùng ảnh nền cùng mask reveal theo tiến độ, lớp chất liệu riêng chạy bên trong; không lấy độ sáng thất thường của clip làm dữ liệu tiến độ. Sửa mask vẫn thuộc GIỮ-CHỈNH nếu ảnh gốc đúng, không mặc định vẽ lại ảnh vì video sai nhịp.

### 1.3 Lề và nền đúng là cần, nhưng không đủ để giữ hình

`redo-01` có `i2v-yin-yang-void-mirror-manifest-r3__take2` vẫn 6: thu nhỏ still 85% chưa giải quyết được đổi hình/phình và tan. Batch-08 ghi Void affliction bị crop ngay khung đầu dù still có đủ ôvan. Cần phân biệt **still sai**, **cách fit ảnh vào khung tạo sai**, và **model làm sai sau khung đầu**; chỉ trường hợp đầu mới buộc làm lại ảnh. [redo-01](../../../.local/video-review/results/redo-01.json), [báo cáo C](../../codex-queue/laneC-report.md).

Crop không khôi phục phần bị cắt; lọc nền không tách được sàn dính cùng ánh sáng với vật chính mà luôn giữ đẹp. Nếu biến hình xảy ra muộn, giữ đoạn trước lỗi; nếu ngay khung đầu đã mất mũi/chi, cần nguồn khác. Không hứa tạo 3–4 take chắc chắn chữa được.

### 1.4 Không đóng mọi thứ vào một ảnh nhiều lớp rồi kỳ vọng sửa riêng

Ảnh nhiều lớp tốt về bố cục, nhưng khi nền đá, khói tối, lửa, tia và vòng cùng bị bake vào một video, chúng cùng đổi hình và cùng mất khi key/fade. Cần thiết kế **khả năng tách lớp**, không chỉ tăng số lớp trong still. Ví dụ: đá tối là ảnh/alpha cố định; khe sáng là mask riêng; hạt là sprite riêng. Mỗi lớp có quyền điều khiển khác nhau.

Radiance thuộc từng pha của **hiệu ứng ghép**, không phải mọi mặt nạ nguồn. Prompt sửa `beast-dissolve-edge-noise` yêu cầu mask đen → trắng nhưng còn thêm sao, motes, halos theo đoạn văn dùng chung; các chấm sáng có thể làm mask sai. Prompt sửa khói mực cũng mang đoạn sparkle chung. Nên tách nhiệm vụ mặt nạ khỏi trang trí; không áp “glowing, rich layered detail” đồng loạt lên mọi nguồn. [batch-01](../../../.local/video-review/results/batch-01.json).

Lõi HDR mảnh và bloom chỉ hỗ trợ phân cấp sáng. MP4 đã cháy trắng không có chi tiết để phục hồi bằng tăng HDR; tăng bloom toàn thân làm mất màu và che chữ. Tia, sao, crack, scorch phải dùng art/render được duyệt, đúng luật cấm hình thô tự vẽ bằng mã.

### 1.5 Đổi giới hạn “ba vòng” thành giới hạn thử có chẩn đoán

Nên dừng ba lần cùng phương pháp không tiến bộ; không có “hết ba vòng thì chấp nhận bản tốt nhất”. `redo-01` tăng TB 0,35, một số việc không tăng hoặc giảm: đã đủ lý do không mở tiếp một lô chỉ thay tính từ trong prompt. Một thử nghiệm phải ghi giả thuyết, một thay đổi chính, bằng chứng và thời gian người làm. Sau tối đa ba lần không giải được lỗi chặn, đổi biểu diễn/phương pháp hoặc đưa anh quyết; trạng thái vẫn chưa đạt.

Chuẩn cũ có những đoạn cho mã tự vẽ hình và nhận từ 8; luật AGENTS ngày sau cùng skill sản xuất đã thay thế chúng. Nghiệm thu hiện hành là **hai giám khảo mù đều ≥ 8,5**, trong built play host, đúng settings người chơi, không URL flag; hệ dùng chung ≥ 9. Bản lab là cổng thử của anh, chưa thay nghiệm thu cuối. Việc skill có ghi “owner approved” ở phần cách lai cũng phải đọc kèm trạng thái chi tiết: **hướng đang thử, chờ demo A/B, chưa chuyển hàng loạt video đang có**.

## 2. Quy trình đề xuất sau khi Claude chốt

1. **Khóa một hiệu ứng và kịch bản thật.** Tên/action class, kích thước tại camera chơi, nguồn tham chiếu nội bộ đã duyệt, số lần đồng thời, input/release/hit đang có, nền sáng/tối, settings và ngân sách. Liệt kê năm pha A/R/T/I/F, radiance mỗi pha và lý do nếu pha không áp dụng. Làm phía người tung trước. Không kéo dài tick trúng chỉ để vừa video.
2. **Lập bản đồ lớp và quyền điều khiển.** Mỗi lớp ghi vai trò, source/still, blend/alpha, góc nhìn, phần engine điều khiển, đoạn video hữu ích, dạng đóng gói dự kiến. Tách hình định danh khỏi chất liệu, ánh sáng khỏi nền đá. Dùng nguồn đang có trước.
3. **Triage trước khi tạo mới.** Áp §6 cho mọi take và ảnh phụ thuộc. Chốt một take chính theo từng vai trò, không chỉ theo `best` cục bộ; giữ bản thay thế nếu nó có đoạn riêng tốt hơn. Nguồn không đủ bằng chứng được đánh dấu chờ kiểm, không tự động cho PASS hoặc BỎ.
4. **Kiểm nguồn A theo vai trò (§5).** Với đoạn giữ: kiểm mọi khung của đoạn, matte trên nền sáng/tối, kích thước thật và tốc độ dự kiến. Với nguồn mới: hai mẫu đại diện trước lô, xem và gửi anh; hình mới cho anh chọn. Chỉ sau đó mới mở số take hoặc biến thể. Prompt/script giữ nguyên đường dẫn tham chiếu nội bộ và ý đồ từng lớp.
5. **Ghép một mẫu năm pha trong lab.** Nhịp macro do engine; chuyển động nội tại do nguồn. Release, ánh sáng, phản ứng mục tiêu và âm gặp nhau đúng sự kiện; one-shot, sustain và progress có cách phát khác nhau. Nghe âm đã có theo Q6: âm được tạo hình bởi hành động, không bù lực bằng tiếng puff/pop/thump rẻ. Không đổi sim/canon để che sai timing.
6. **Tìm lớp yếu bằng phép bật/tắt có kiểm soát.** So cùng camera, seed, clock, ground và âm lượng; xem cả bản tắt âm để tránh âm cứu hình giả. Tắt riêng thân, quầng, hạt, impact để biết hình nào đang gây phẳng/rối. Không mặc định thêm lớp; thay hoặc giảm lớp che hình chính.
7. **Chấm B và đo trong cảnh có tải.** Chạy một lần, rồi nhiều instance; thử cold load/warm load, nền sáng/tối, đọc chữ, báo trước địch, giảm chuyển động. Số đo và video cùng cấu hình. Dùng mặc định host cho nghiệm thu; flag chỉ phục vụ chẩn đoán A/B.
8. **Sửa đúng nơi, hoàn tất mẫu rồi nhân rộng.** Lỗi timing → engine; mask → xử lý/mask; vật liệu hỏng → nguồn; hình sai → ảnh. Mỗi vòng giải một lỗi chặn có bằng chứng. Anh xem before/after mẫu, sau đó hai giám khảo mù chấm bản dựng cuối ≥ 8,5 từng người. Chưa tới bar thì vẫn mở việc, dù đã vượt 8.

Trong giai đoạn thử cách lai, so video hiện tại với lớp đóng gói mới **cùng một nguồn** trước; nếu đồng thời thay art và runtime thì không biết yếu tố nào tạo khác biệt. Kiểm nét, màu, alpha, nhịp, bộ nhớ và khựng lần đầu. Không tăng số video vượt giới hạn hiện ghi (3); không tự chuyển tất cả sang atlas. Kích thước ô lấy từ kích thước lên màn, không dùng một độ phân giải cho mọi loại.

## 3. Hướng có triển vọng nhất theo nhóm

Đây là thứ tự thử dựa trên lỗi quan sát và độ kiểm soát, chưa phải tỷ lệ thành công đo được. Mọi hướng mới đều phải qua hai mẫu và bản ghép.

| Nhóm | Hướng thử trước | Lý do và giới hạn |
| --- | --- | --- |
| Chiêu từ trời: cột, sao băng | Giữ thân comet I2V khá tốt; engine giữ trục và bay theo đường thật; release từ người tung, điểm rơi/impact/dư âm riêng. Cột dùng thân chất liệu theo trục, đầu/chân và xung sét tách lớp; Blender nếu thiếu motion nội tại. | Nhiều comet đạt 7, giữ hình/nền tốt; lực thấp chủ yếu vì clip đứng yên được chấm như hành động. Cột sáng đều hoặc mưa sao thành tia treo cần cấu trúc xung và điểm chạm; kéo scale cả cảnh không tạo trận mưa thật. Cột có hình định danh vẫn cần still trước I2V. |
| Dải và lưỡi chém | Ảnh/đoạn I2V đúng cung làm texture trên strip/mesh theo mặt phẳng chém; reveal theo hướng, erosion đuôi, sprite phụ ở mũi và điểm chạm. | Ice crescent giữ hình; nhiều slash giữ ảnh tới 70–90%. Giữ hình là lợi thế khi engine sở hữu quét, nhưng chỉ thêm alpha lên billboard đứng yên thì vẫn là hình dán. Không kéo méo các tinh thể đặc quá mức. |
| Hào quang lặp | Ảnh vòng/sheath đúng dáng cùng dòng chất liệu lặp riêng; chuyển động các lớp độc lập, mật độ ổn định, hạt sinh–tắt rải thời gian. Blender tuần hoàn nếu I2V đổi topology. | Các loop đang đổi kích thước, lõi và sáng. Cần ổn định thể tích trước khi thêm sparkle; phase offset không sửa seam. Không bắt aura sustain bung–tan mỗi chu kỳ. |
| Khói và nổ | Với take có chất liệu đẹp, giữ đoạn hữu ích; khói tối xuất alpha thật, lõi/tia/khói/đá tách. Thử Blender làm **thân** khói hoặc nổ nếu Firefly phình/crop dai dẳng. | Death ink và blood impact không tăng qua redo; D1 cho thấy kiểm soát lề/alpha được. Nhưng D1 còn cụm tròn, nên chưa khẳng định sim/render đẹp hơn Firefly. Nổ cần hướng lực, tương phản và thời gian, không chỉ có khói. |
| Ấn và vòng đất | Still/decal giữ hình; base đá, emissive khe và hạt tách; engine reveal/erosion trên mask art. I2V chỉ làm dòng sáng bên trong khi giữ cấu trúc. | Charge không tích lũy; nhiều ground mark làm mất cả đá. `water-ground-mark` take2 là ngoại lệ hữu ích có đá tối cuối. Không để chữ/rune quan trọng tự đổi nét; phép chiếu xuống đất phải tránh nghiêng hai lần. |
| Hiện hình thần thú | Still nội bộ dạng năng lượng, mức chi tiết đồng nhất đầu/thân; mask hiện hình theo tiến độ độc lập. Clip in-place chỉ cung cấp nội khí; đầu dẫn và thân strip theo đường/S-wave nếu cần bay. | Fox thành thú đặc, tiger co duỗi chân, nhiều manifest tan dồn cuối. Không đảo clip tàn hỏng để làm progress; không buộc video tự diễn cả hiện hình, tấn công, tan. Close-up có hành động/phối cảnh phức tạp cần mẫu CGI riêng. |
| UI và thẻ | Giữ ảnh sắc nét có bố cục, chữ do UI thật dựng; frame/aura/sweep/glint art tách; animation theo trạng thái hover/ready/select/reward. | UI được nhìn lâu, chi tiết sai khó giấu bằng bloom. Video nền không được làm nhòe nội dung hoặc thay chữ. Làn C có cut-in material nhưng không có mẫu đối chứng đủ để suy ra hiệu quả của toàn bộ UI/thẻ. |

## 4. Hai mươi clip nên giữ để thử làm lớp nguồn

**Giới hạn kết luận:** hiện không thể ký “20 clip đã đạt A đầy đủ” từ JSON và sáu khung. Làn C chưa chứng nhận phát thực; A mới còn cần matte, fit vai trò, đoạn trích và loop đúng cách. Danh sách dưới là **ưu tiên GIỮ-CHỈNH để kiểm A**, chưa có lý do buộc tạo lại ảnh ngay. Không gọi chúng PASS xuất xưởng. Đây là cách trả lời phần “dùng ngay” mà không bịa chứng nhận.

Đường dẫn video của mỗi dòng: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video/<job>/take<N>.mp4`. Key `<job>__take<N>` nối thẳng tới JSON và sheet trong `.local/video-review/sheets/`. Cả 20 file được ffprobe xác nhận 1920×1080, 24 fps, 5,041667 s. Sheet lấy tại 10/25/40/55/70/90% thời lượng, **không phải đầu/cuối**.

Mốc cắt dùng thời gian nguồn, khoảng nửa mở `[in, out)`, đã chọn theo khung 24 fps: 0,50–3,50 s tương ứng khung 12…83. Đó là cửa sổ **đề xuất để soi từng khung**, không phải EDL đã kiểm. Với still/texture có thể chỉ lấy một khung tốt; với one-shot phải thêm envelope/erosion, không giữ nguyên 3 giây trên sân. Những đoạn này không được coi là loop tự nhiên.

| # | Key / đợt / điểm cũ | Đoạn đề xuất (giây nguồn) và vai trò giữ | Chỉnh cụ thể trước khi dùng |
| --- | --- | --- | --- |
| 1 | `i2v-fire-comet__take1` · 05 · 7 | 0,50–3,50; thân sao băng | Giữ nội hỏa, bay bằng engine; thêm sheath/glint thật và impact riêng, không đòi thân tự nổ. |
| 2 | `i2v-ice-comet__take1` · 05 · 7 | 0,50–3,50; đầu/đuôi băng | Giữ mạng băng; lớp sương lạnh, mảnh và lõi mảnh riêng; kiểm nhấp sáng khi tăng tốc. |
| 3 | `i2v-earth-comet-v2__take1` · 05 · 7 | 0,50–3,50; thân Thổ | Giữ hướng và cấu trúc v2; bụi có alpha, tia và impact tách. Không phục hồi v1 đã bị thay thế. |
| 4 | `i2v-metal-comet-v2__take1` · 06 · 7 | 0,50–3,50; thân Kim | Giữ sợi bạc; dòng đuôi và glint lệch nhịp, xung đầu khi release riêng. |
| 5 | `i2v-poison-comet-v2__take1` · 07 · 7 | 0,50–2,75; thân Độc | Tránh phần đầu mềm dần về cuối; giọt/tia tím từ art riêng; kiểm độ giữ thể tích. |
| 6 | `i2v-star-comet__take1` · 07 · 7 | 0,50–3,50; thân Tinh | Giữ mạng sao và vị trí; thêm hạt đuôi đa cỡ có nhịp, đường bay thật. |
| 7 | `i2v-thunder-comet__take1` · 07 · 6,5 | 0,50–2,75; lớp thân Lôi | Giữ sét nội bộ; bổ sung lõi/sheath mảnh và xung, không đẩy cả đầu mềm thành trắng. |
| 8 | `i2v-water-comet__take1` · 08 · 6,5 | 0,50–3,50; lớp thân Thủy | Giữ vân chảy; bọt/giọt riêng, nhịp di chuyển và chạm đất; kiểm đầu dạng lưới ở cỡ chơi. |
| 9 | `i2v-blood-crescent-sym__take1` · 04 · 6 | 0,50–3,50; hình kiếm khí cân | Dùng làm thân/texture có reveal hướng tâm–mũi; thêm radiance, erosion cuối; chưa duyệt loop. |
| 10 | `i2v-ice-crescent-sym__take1` · 06 · 7 | 0,50–3,50; hình kiếm khí băng | Giữ mặt tinh thể và hai sừng; chuyển động quét/bay và đuôi do engine, hạt từ art. |
| 11 | `i2v-dark-slash-arc__take1` · 05 · 6 | 0,50–2,75; texture cung đỏ | Bỏ yêu cầu clip diễn toàn nhát; reveal theo cung, xói đuôi, tàn bằng mask. Nếu cần khối đen phải có alpha/lớp tối riêng. |
| 12 | `i2v-ice-slash-arc__take1` · 06 · 6 | 0,50–3,50; texture cung tinh thể | Giữ chi tiết đang gần tĩnh; đặt vào mặt phẳng chém, thêm quét sáng và erosion. Không chỉ tua nhanh đoạn giữ hình. |
| 13 | `i2v-water-slash-arc__take1` · 08 · 6,5 | 0,50–2,75; thân cung nước | Giữ hình trước co/tan muộn; trích chất liệu, nhịp chém/đuôi và giọt riêng. Đoạn cuối đen chỉ là tài liệu tham khảo, chưa chọn cho timing thật. |
| 14 | `i2v-star-caster-seal__take1` · 07 · 7 | 0,50–2,75; ấn sustain ngắn | Giữ tâm rỗng; reveal và xung tâm–vành riêng. MAE 1,20× của toàn clip không chứng nhận cửa sổ này loop. |
| 15 | `i2v-thunder-caster-seal__take1` · 07 · 6,5 | 0,50–2,75; ấn sustain ngắn | Giữ rune, thêm nhánh sét bò/hạt nâng riêng; kiểm mối nối mới dù MAE toàn clip 1,09×. |
| 16 | `i2v-metal-caster-seal__take1` · 06 · 7 | 0,50–2,75; lớp ấn Kim | Giữ đường bạc và tâm rỗng; thêm chiều sâu sáng/tối, pulse riêng; tránh chồng thêm một đĩa trắng. |
| 17 | `i2v-water-ground-mark__take2` · 08 · 6,5 | 0,50–2,75: lớp năng lượng; 4,50–5,00: khảo sát base đá | Giữ hai phần thành hai lớp nếu matte tách sạch; nếu không, dùng still đá gốc. Erosion năng lượng riêng để đá còn lại; không luma-key mất đá. |
| 18 | `i2v-ult-ice-cold-silence__take2` · 08 · 7,5 | 0,50–3,50; nền/lớp cảnh băng tĩnh | Giữ ý tĩnh lặng; thêm sương bò tinh thể và chuyển tiếp đầu/cuối riêng. Không hứa nâng điểm bằng rung/nổ. |
| 19 | `i2v-ult-thunder-nine-heavens__take2` · 08 · 7,5 | 0,50–3,50; lớp mây/cuộn thư/sét | Dùng lớp sân khấu; xung giáng và chạm chân ấn riêng. Bản v2 đang nối ở lab: không thay ngược v2 bằng v1 chỉ vì v1 điểm cao hơn. |
| 20 | `i2v-ult-water-profound-sea-v2__take3` · 08 · 7,5 | 0,50–3,50; mặt xoáy nền | Giữ màu, bọt và lòng xoáy; nếu chiêu cần sóng đổ thật, làm lớp sóng chủ lực riêng, không gọi mặt xoáy lay nhẹ là đã đủ. |

Các đoạn bảng trên có thể rút ngắn thêm hoặc trượt A sau kiểm từng khung. Không điền thời điểm “bung đẹp nhất” chính xác tới một khung khi chỉ có sheet. Nếu cần loop dài hơn, tìm cặp nối bằng toàn bộ clip rồi phát kiểm; không lặp nguyên cửa sổ bảng một cách mặc định.

Không chọn một số “điểm kỹ thuật cao” vào bảng: charge-fill sai logic; Dark ground mark take2 tổng 4 dù technical 8 vì đá biến đĩa và cuối sáng hơn; `i2v-wood-comet-v2` có hình thoi xám sẵn ở still; `beast-hit-ink-streak` technical 8 nhưng chất liệu/hình vệt sai. Chúng cần chẩn đoán khác, không chỉ thêm bloom.

## 5. Thước chấm hai tầng gọn và đo được

### A — Lớp nguồn, PASS/FAIL/CHƯA ĐỦ BẰNG CHỨNG

Năm ô, mỗi ô phải có chứng cứ: **đúng vai trò; giữ hình/motion cần thiết; matte/nền; thời gian/loop; đủ nét và đóng gói**. Một ô FAIL làm A FAIL cho vai trò đó. Thiếu chứng cứ thì chờ kiểm, không gán PASS. Điểm đẹp cũ giữ nguyên để ưu tiên, không lấy trung bình thành A.

Các số dưới là **ngưỡng thử đề xuất**, cần Claude kiểm trên hai mẫu trước khi áp lô; chưa phải luật đã được anh duyệt. Đo trên miền foreground/ROI, không để nền đen lớn làm đẹp giả số đo.

| Ô A | Phép kiểm ngắn |
| --- | --- |
| Vai trò/hình | Ghi silhouette, màu, hướng, các mốc định danh bắt buộc; 0 lần mọc/mất chi, đổi số cánh, rune quan trọng hoặc vật thừa trong đoạn dùng. Texture thuần không bắt có hình nhân vật. Progress phải đơn điệu theo trạng thái gõ, không theo video. |
| Lề/ổn định | Nguồn in-place: lõi hình cách mép ≥ 5% kích thước tương ứng ở mọi khung; vành ngoài ≥ 4 px sạch ở bản đóng gói. Drift tâm ≤ 2% cạnh ngắn, đổi kích thước bao ≤ 5% trong đoạn sustain, trừ chuyển động được thiết kế. Không áp máy móc cho tia toàn màn hoặc strip chủ ý tile qua mép; chúng kiểm seam/endpoint riêng. |
| Nền/matte | RGBA: alpha mép ≤ 2/255, không viền đen/trắng trên hai nền. Video additive nền đen: nền ROI ngoài hiệu ứng có p99 mỗi kênh ≤ 4/255 sau giải mã; xem cả rìa glow. Khói/đá đen dùng alpha thật hoặc mask riêng; không bắt additive hiển thị màu đen. Không lọc nền bằng ngưỡng mạnh tới mức mất sợi mảnh. |
| Thời gian | One-shot sau envelope/erosion: cuối alpha/mask max ≤ 2/255; additive cuối không còn hình thấy được trên hai nền. Sustain không buộc tan; ground base có thể tồn tại. Loop: so frame cuối–đầu với phân bố chênh khung kề, ngưỡng cảnh báo tỷ số > 2×, đồng thời kiểm màu, tâm, dáng và phát ≥ 10 chu kỳ ở tốc độ thật. Tỷ số nhỏ không tự PASS; mẫu gần tĩnh cần ngưỡng tuyệt đối và kiểm mắt. |
| Nét/đóng gói | Kiểm ở cỡ pixel thật và tốc độ thật; không bậc frame, ghost, ô atlas rò hoặc nhòe do nén. Với burst, skill hiện ghi ≥ 24 khung; không nhân bản khung cho đủ hoặc kéo dài đòn chỉ để đủ số. Lớp loop phải có chu kỳ thực được kiểm. So source và bản runtime cùng điều kiện. |

Mặt nạ soft không dùng bounding box của mọi pixel nén lẻ; khai báo threshold dùng đo (ví dụ > 8/255 cho lõi, > 2/255 cho matte) và giữ nhất quán. Sai số lề, màu và drift được đo ở đoạn thực dùng sau xử lý; report cũng giữ số nguồn thô để biết đã sửa gì. Các phép kiểm này không thay chấm đẹp.

### B — Hiệu ứng ghép, chấm 1–10 trong bản chơi

Giữ năm cột: **cuốn hút/phong cách; hình–chất liệu–ánh sáng; nhịp/lực; tương tác/đúng việc; dễ đọc**. Điểm tổng là nhận định có lý do, không lấy trung bình che một lỗi chặn. Mỗi giám khảo nêu một lỗi lớn nhất, pha và thời điểm nó xảy ra. Kỹ thuật/hiệu năng là cổng riêng, không cộng điểm render nhanh vào vẻ đẹp.

Chấm bản chơi tại 720p và 1080p, camera/settings người chơi, nền sáng và tối, một đòn và tải thật. Mẫu lab được anh duyệt trước khi tích hợp; hai người chấm mù độc lập cho bản dựng cuối, không xem điểm cũ, tên công cụ hoặc nhận xét của nhau. Cả hai ≥ 8,5 mới đạt; dùng chung ≥ 9. Một người dưới bar thì FAIL, không bình quân hai người. Anh xem cuối theo luật dự án.

Cổng bắt buộc từ VFX_STANDARD/AGENTS: đủ pha có áp dụng, release ở nguồn; không đổi sim; ánh lóe/đèn khung đầu ≥ 95% đỉnh; vùng trúng sai số ≤ 10%; phím cuối tới release ≤ 50 ms theo hợp đồng đòn; chữ tương phản ≥ 7:1 theo phép đo của game; trắng xóa ≤ 6% sân, ultimate ≤ 15% trong tối đa 3 khung; chớp toàn màn ≤ 2/s. Ngân sách frame time và số đèn lấy của game/cảnh hiện hành, không bê số Dragonhold sang Tu Tien. Không dùng mọi hàng timing như một delay mới cho mọi loại hành động.

### Có chấm lại toàn làn C không?

**Có, nhưng theo hai lượt, ưu tiên nguồn đang dùng.** Lượt 1 dùng JSON để định tuyến, gắn ảnh nguồn và role, đánh dấu lỗi rõ; không dựng lại 467 bộ nhận xét dài. Lượt 2 chỉ soi từng khung/phát thực các đoạn có triển vọng hoặc đang chạy trong lab, ghi năm ô A và một dòng việc sửa. Clip FAIL hình/sai công dụng rõ không cần xem mười vòng để xác nhận lại.

Phiếu ngắn cho một vai trò: `key; source-hash; still+approval; role; A[5 ô]; in/out/frame/fps; blend; motion-mode; lỗi chặn; nhóm; việc sửa; owner-lane; phụ thuộc; bằng chứng; B[chưa chấm hoặc capture+hai điểm]`. Đánh giá nguồn gốc và khả năng áp dụng sau xử lý tách biệt; không tự ghi A PASS cho video thô vì kế hoạch sửa nghe hợp lý.

## 6. Phân loại toàn kho và chia ba luồng

### 6.1 Quy tắc phân loại clip và ảnh nguồn

Đơn vị quyết định là **job + vai trò + đoạn dùng**, có danh sách take/still phụ thuộc. Một clip có thể giữ cho vai trò vật liệu nhưng trượt vai trò chiêu hoàn chỉnh; không tạo hai worker cùng sửa nó. Mỗi ảnh nguồn có quyết định riêng, không kết tội ảnh chỉ vì video đổi hình.

Thứ tự xét để mọi mục đều có lối xử lý:

1. Nối key → video/sidecar → still thật → nơi dùng thật. Thiếu use/prompt/still hoặc hash thì ghi CHƯA ĐỦ BẰNG CHỨNG trong trạng thái kiểm và giao việc truy vết; đây không phải nhóm sản xuất thứ năm. Không tự gán T2V, BỎ hay LÀM-LẠI-ẢNH vì thiếu metadata.
2. Gộp bản trùng nội dung, bản bị thay thế và best theo **toàn kho**. `i2v-dark-ground-mark` có best take1 ở batch-04 và take2 ở batch-05; lời giải thích ở batch-05 thay lựa chọn cũ. `best:true` không phải quyền tự động đưa vào game. DROP cũ phần lớn là take thừa, không có nghĩa cả job phải bỏ. Giữ quan hệ v1→v2 và q1→bản gốc.
3. So still và khung đầu: sai silhouette/màu/vật thừa/lề ở ảnh → ảnh cần sửa; still đúng nhưng fit bị crop → GIỮ-CHỈNH cách fit, thử lại cùng ảnh; chỉ video drift/hỏng muộn → thử đoạn sạch hoặc I2V lại từ ảnh giữ. Không buộc tạo ảnh mới cho lỗi video đơn thuần.
4. Áp cổng A theo vai trò. Chỉ sau kiểm mới khóa một trong bốn nhãn dưới; nếu FAIL sửa nhỏ thì ghi nhãn dự kiến cùng trạng thái A hiện tại, không gọi nó “đã đạt”. Bốn tên anh nêu còn thiếu trường hợp **ảnh đúng nhưng video hỏng toàn đoạn**: đề xuất để trong luồng 2 với trạng thái `I2V-lại/ảnh-giữ`, ghi rõ đây là mở rộng route của LÀM-LẠI-ẢNH, không yêu cầu tạo ảnh mới vô ích. Claude chốt cách ghi này trước khi xuất danh sách triển khai.

| Nhãn sau kiểm | Điều kiện đo được và việc tiếp theo |
| --- | --- |
| **GIỮ-CHỈNH** | Có đoạn/khung đúng dáng, đúng vai, matte xử lý sạch; qua A cho lớp sẽ giữ. Lỗi còn lại xác định được bằng trim/retime/envelope/reveal/erosion, grade, fit, alpha hoặc một lớp phụ độc lập. Ghi chính xác in/out, phép xử lý và phần giữ; không thay toàn thân bằng lớp mới rồi vẫn gọi là giữ. Nếu cả đoạn thô chưa qua A thì chỉ là ứng viên GIỮ, chưa khóa nhãn. |
| **LÀM-LẠI-ẢNH** | Có hình định danh nhưng không có đoạn đạt A vì hình/lề/góc/vật thừa; hoặc I2V làm sai hình trong suốt đoạn cần dùng. Ghi `ảnh=giữ/sửa/mới`: ảnh đúng thì giữ và thử I2V lại, không phí vẽ; ảnh sai phải sửa đúng lỗi đo được và cho anh duyệt trước. Nhãn này là luồng có hình; không khẳng định mọi việc đều cần ảnh mới. |
| **LÀM-LẠI-BLENDER** | Vai trò chất liệu thuần; không có đoạn đạt A và lỗi nằm ở chuyển động/thể tích/tan/alpha cần kiểm soát. Ảnh đúng không cứu được motion; thử render có điều khiển, chứng minh hai mẫu trước lô. Hình có dáng không bị chuyển sang T2V; Blender lớp phụ có thể là phụ thuộc của việc GIỮ. |
| **BỎ** | Trùng hash/nội dung đã có bản chính, bị thay thế có bằng chứng nơi dùng, sai hoàn toàn công dụng và không có lớp/đoạn khác hữu ích sau kiểm. BỎ là rút khỏi kế hoạch sản xuất, giữ file và lý do; không tự xóa media. Điểm dưới 8 không phải điều kiện BỎ. |

Với ảnh: giữ nếu định danh, camera, màu, lề, mức sáng và quyền dùng đáp ứng brief; chỉ cần tách mask/reframe thì GIỮ-CHỈNH; sai cấu trúc thì LÀM-LẠI-ẢNH. Ảnh chất liệu làm tham chiếu Blender được giữ kèm nhãn route của job, không gọi một ảnh xấu là “đã sửa bởi Blender” khi chưa render. Ảnh trùng/không còn nơi dùng mới xét BỎ. Một still chung nhiều video chỉ có **một** việc sửa ảnh; các job khác phụ thuộc đầu ra đó.

### 6.2 Ưu tiên theo thứ đang dùng trong lab

Thứ tự: **đang có đường gọi trong lab và lỗi nhìn thấy rõ → asset đang dùng lại nhiều lần → chiêu mẫu năm pha cần anh chấm → nguồn mới chưa nối**. Trong cùng mức, ưu tiên sửa hình sai/crop/thiếu caster trước, rồi timing, matte, cuối cùng radiance. Không chọn chỉ theo tổng điểm thấp nhất hay số clip làm được mỗi giờ.

Đã đọc chỉ để xác định ưu tiên: `games/.wt-ic-lab-all/src/lab/clip-skills.ts` có `pillar-thunder-single`, `pillar-thunder-field`, `pillar-fire-meteor`, `ult-thunder-nine-heavens-v2`; `five-phase.ts` và `skills-main.ts` có mẫu M/sao băng và key 2/lưỡi liềm. [Phiếu B8](../codex-lanes/lane-B8-thunder-pillar-five-phase.md) cũng nhắm mẫu Cột Lôi. Đây là bằng chứng nối mã, **không phải xác nhận tab đang mở dùng đúng worktree hoặc tất cả đường gọi đã render đúng**. Trước khi xếp hàng thật, Claude chốt host/worktree đang phục vụ và đối chiếu manifest/trace runtime; trường `use` chỉ là ý định, chưa đủ.

Mẫu đầu nên chọn từ Cột Lôi đang nối hoặc Hỏa M/key 2 đang có năm pha: giải một vòng A→ghép→B rồi mới nhân rộng. Không đưa v1 Thunder ultimate 7,5 thay v2 đang nối chỉ vì v2 có điểm 7; hai bản có ý đồ khác nhau.

### 6.3 Ba luồng và danh sách việc sau khi chốt

Đây là **đề xuất nội dung ba file làn**, chưa tạo file hoặc giao worker. Mỗi làn nhận danh sách toàn bộ job của mình sau bước triage; không ghi kiểu “làm các clip còn lại”. Danh sách khóa trước khi chạy, mỗi dòng có source-hash, role, đoạn dùng, ảnh, phép kiểm A/B, phụ thuộc, đường dẫn ghi và trạng thái. Không chạy thêm agent trong A7.

| Luồng | Danh sách việc có thứ tự trong file làn | Phạm vi ghi đề xuất, tách biệt |
| --- | --- | --- |
| **1 · GIỮ-CHỈNH** | 1) Chốt map asset→role→đường gọi lab của các việc được giao. 2) Kiểm A và thử trim 20 ứng viên §4 theo ưu tiên lab, rồi toàn bộ ứng viên GIỮ còn lại đã liệt kê. 3) Làm trim/matte/grade/mask/fit cần thiết vào bản dẫn xuất, giữ nguồn bất biến. 4) Viết recipe nhịp và các lớp thiếu cho từng job, yêu cầu lớp phụ ở luồng 3 nếu cần. 5) So nguồn–dẫn xuất và kiểm đóng gói; giao gói cùng bằng chứng cho Claude ghép mẫu. 6) Nhận lỗi B, sửa đúng lớp, PASS việc hiện tại rồi chuyển việc kế. | Thư mục đầu ra mới `<đợt>/keep/<job>/<version>/`, báo cáo/recipe riêng của làn 1; không sửa still/video gốc, manifest chung hoặc mã game. |
| **2 · HÌNH/ẢNH → I2V** | 1) Liệt kê từng job/still sai hình hoặc video giữ hình thất bại, đối chiếu nơi dùng. 2) Reuse ảnh đúng; sửa fit trước nếu lỗi từ khung. 3) Ảnh thật sự sai: chuẩn hóa brief, tham chiếu nội bộ, ảnh sửa/mới và prompt bên cạnh; cho anh chọn. 4) Kiểm hai mẫu trước lô. 5) Từng job I2V một lần thử có giả thuyết, mở thêm take khi có lý do, không chạy 3–4 take mù cho mọi ảnh. 6) Kiểm A, khóa đoạn và tệp đầu ra, giao luồng 1/Claude; tối đa ba lần cùng phương pháp không giải lỗi thì đổi cách, không tự PASS. | `<đợt>/image/<still-id>/<version>/` và `<đợt>/image-video/<job>/<version>/`; chỉ làn 2 sở hữu ảnh dùng chung. Luồng 1 đọc bản đã khóa, không ghi vào đây. |
| **3 · CHẤT LIỆU BLENDER** | 1) Nhận danh sách chất liệu FAIL A và phụ thuộc lớp phụ của luồng 1, ưu tiên death/hit/caster đang dùng. 2) Hai mẫu có reference/alpha/camera/timing đúng; sửa D1 về hình tia có hướng và khói có sợi trước khi chạy lô. 3) So chủ lực Blender với Firefly giữ lại ở cùng cỡ, rồi so lớp phụ bật/tắt. 4) Chỉ khi mẫu ghép đạt mới render lần lượt từng job đã liệt kê; kiểm frame, lề, alpha, tail/loop, độ nét. 5) Giao RGBA/mask, recipe và thông số tái lập; luồng 1/Claude dùng bản khóa. 6) Thu lỗi B, sửa nguồn hoặc đổi phương pháp, kiểm xong rồi sang việc tiếp. | `<đợt>/blender/<job>/<version>/`, recipe/script snapshot và báo cáo làn 3; không sửa `tools/blender-vfx` chung hoặc file của luồng 1/2 trong cùng đợt. |

`<đợt>` là thư mục mới **sẽ được phiếu sau chỉ định và cho phép ghi**; các đường trên là cách chia quyền, không phải quyền ghi được cấp trong A7. Captures/owner-review đặt trong review folder theo AGENTS bằng worker có quyền tương ứng. Chỉ Claude/integrator cập nhật manifest/đường gọi lab sau kiểm; tránh cả ba cùng sửa `five-phase.ts`, `clip-skills.ts`, `manifest.json` hoặc hàng việc chung.

Phụ thuộc không làm trùng việc: luồng 1 có job chính và yêu cầu “bụi phụ”; luồng 3 có ID lớp phụ riêng cùng owner. Luồng 2 sửa một still dùng chung một lần. Mọi chuyển nhóm phải bàn giao hash/version, lý do và đổi người sở hữu trước khi người sau ghi; không chuyển rồi hai bên cùng tiếp tục. Ba luồng có thể làm đồng thời ba job độc lập; không cần cả ba cùng sửa một chiêu.

Tôi chưa lập danh sách phân loại cuối cho 640 mục: thiếu kiểm A mới và xác minh host thật. Phạm vi A7 chỉ cho tư vấn một file; tự điền hàng trăm PASS/route chắc chắn lúc này sẽ tạo độ chính xác giả. Quy tắc ở trên bao phủ mọi mục, còn việc kiểm và xuất ba danh sách đầy đủ là bước đầu bắt buộc của đợt triển khai được chốt sau này.

## 7. Ảnh đầu cho I2V: giữ hình, giữ lề, tan đúng

Không có bố cục nào bảo đảm model không phình hoặc tan đúng. Ảnh khóa **hình và vật liệu**; motion brief, cách fit, giới hạn take và lớp runtime khóa **cách dùng**. Trước khi vẽ ảnh mới, thử ảnh hiện có với khung đúng.

- **Khung/lề:** đúng tỷ lệ video đích và cách contain; xem preview khung 0 trước tạo. Với hình cô lập dễ nở, bắt đầu khoảng 60–70% chiều rộng/cao khả dụng, tính cả halo; nở mạnh dùng ít hơn. Đây là điểm thử, không luật phải thu nhỏ mọi asset. Với chiều khung `W`, bề rộng nguồn `w`, hệ số nở tối đa dự kiến `g`, drift `d` và lề an toàn `m`, cần `g*w + 2*d + 2*m ≤ W`; tính tương tự theo cao. Clip hiện có không phải bỏ chỉ vì khác tỷ lệ này, nếu đoạn dùng qua A.
- **Nền/matte:** lớp sáng cô lập trên đen đồng nhất; lớp tối cần alpha/mask hoặc nguồn riêng phù hợp. Nền trắng để tạo mask khói có thể đúng brief, không mặc định coi nền trắng là lỗi. Bỏ sàn/bóng/cảnh vật ngoài chủ đích trước tạo; giữ provenance ảnh nội bộ, không dùng ảnh bên thứ ba.
- **Tư thế:** dáng rõ ở camera chơi, nhìn ra trục và tâm, không sát mép, không mất mũi/chi. Vật thể bay ở giữa và đứng tại chỗ trong nguồn; engine di chuyển. Thần thú là năng lượng, chi tiết đầu/thân cùng cấp, không tư thế chân chạy nếu mục đích bay. Seal/đất giữ mặt phẳng phù hợp; ảnh đã phối cảnh không lại ép nghiêng như texture top-down.
- **Độ sáng:** thân có màu và khoảng tối bên trong, lõi sáng mảnh; không bake một khối trắng kín, bloom dày hay flare che bộ phận định danh. Không coi LDR nguồn là HDR thật; chốt màu trong color pipeline của host. Lớp màu/quầng runtime giữ ≤ 0,9 mỗi kênh theo luật; boost chỉ lõi mảnh sau thử.
- **Số lớp:** trong mỗi nguồn chỉ một nhiệm vụ chuyển động chính; có thể giàu lớp nội hỏa, nhưng đá, năng lượng, tia và progress cần điều khiển riêng thì tách nguồn/mask. Không đặt số lớp bắt buộc; chọn ít lớp đủ đọc và đủ đẹp, không tấm ảnh rối mà model phải tự hiểu mọi pha.
- **Tan:** ảnh không thể chỉ huy thời điểm tan. One-shot dùng ảnh đỉnh đúng dáng, clip cho nội động, tail riêng hoặc erosion mask theo hướng vật liệu; kiểm đoạn tan thực. Đừng dùng cùng still đầu/cuối cho one-shot cần về đen. Với loop in-place có thể thử cùng ảnh ở hai đầu để giảm drift, nhưng phải kiểm model có đóng băng và seam có giật vận tốc không. Progress/manifest gắn gõ dùng mask reveal riêng; không đảo tự động một clip biến hình hỏng.

Prompt viết khẳng định nhiệm vụ: chủ thể/kiểu vật liệu, trục, phần chuyển động, nhịp hoặc sustain, envelope, camera và nền. Ví dụ mô tả nội hỏa chảy trong dáng cố định, thay vì yêu cầu vật chạy tiến khi engine sẽ bay nó. Mask thuần chỉ mô tả mask; sparkle được giao lớp art riêng.

## 8. Kết luận riêng về Blender D1

**Chưa chạy lô bằng hai recipe hiện tại.** Giữ chúng như mẫu kỹ thuật và điểm khởi đầu để nâng chất liệu, không gắn nhãn đã đạt vì alpha sạch. Đã xem sheet tia nền đen và khói trên nền sáng; kết luận kỹ thuật đối chiếu từ JSON, không giả nhận đã xem MP4 realtime.

| Bằng chứng D1 | Điều rút ra |
| --- | --- |
| Hai mẫu tự chấm 6,5; technical 9, fit 8 | Kỹ thuật tốt vẫn chưa đạt vẻ đẹp 8; tự chấm ngoài game không phải hai giám khảo mù. |
| Spark 16 khung, 512², 24 fps, 0,667 s; render 3,605 s; lề tối thiểu 174 px | Có quyền điều khiển timing/alpha; sheet cho tia quá nhỏ trong khung và khá hướng tâm. 16 khung cũng chưa đủ yêu cầu burst ≥ 24 của skill hiện tại: nếu cần thêm mẫu motion, render đủ mật độ ở cùng thời lượng, không kéo dài cú hit hoặc nhân đôi khung cho đủ. |
| Smoke 36 khung, 512², 24 fps, 1,5 s; render 30,004 s; lề 117 px | Thân tối tồn tại trên nền sáng, cuối sạch; nhưng các cụm tròn còn giống bông. Đây là volume nhiễu có giới hạn, **không phải** Mantaflow nên không suy ra chất lượng mô phỏng khói thật. |
| Alpha bốn mép và khung cuối đều 0; 10/10 khung render lại trùng RGBA | Pipeline có tính tái lập; chưa nói lên silhouette đẹp, motion mượt hay khớp cỡ hit/death. |
| Cycles CPU 3 khung/84,5 s, báo cáo không thấy cải thiện đáng thời gian | Nút thắt hiện là thiết kế hình/chuyển động/phân lớp, chưa có căn cứ tăng chất lượng bằng đổi engine render. |

Tia: thử phân hướng theo lực đánh, tách một vài tia chính khỏi hạt rất mịn, sửa tỷ lệ chủ thể trong khung và chiều dài tail, quầng có màu tiết chế. Khói: thử một mẫu kéo sợi và khe rỗng có hướng, một mẫu mô phỏng dòng nếu công cụ sẵn; đánh giá ở cỡ death thật, không chọn theo độ nhiễu cận cảnh. Tránh bù thiếu hấp dẫn bằng tăng mật độ thành một quả cầu khói lớn.

Ưu tiên **Blender lớp phụ** khi clip Firefly đã có hình/chất liệu đẹp, chỉ thiếu tia, bụi, áp lực hoặc tail. Ưu tiên **Blender lớp chủ lực** cho chất liệu mà Firefly liên tục crop, không tắt hoặc không có motion hữu cơ, sau khi hai mẫu chứng minh đẹp hơn trong bản ghép. D1 chưa đủ bằng chứng chọn một trong hai làm quy tắc cho mọi nhóm. Blender toàn thân tốt hơn một clip hỏng là hợp lý; chồng lớp phụ lên một hình sai không hợp lý.

## 9. Điều cần anh xem trước khi mở lô

Một mẫu năm pha đang dùng trong lab, trước/sau giữ cùng camera/clock/settings; hai mẫu nguồn đại diện; và demo video so cách đang phát với cách lai ở độ nét anh sẽ chơi. Các file media/capture đó do đợt sau làm trong đúng thư mục review, không tạo ở A7. Anh chọn hướng; Claude chốt recipe, phạm vi ba file làn và kiểm độc lập cuối. Không cần quyết lại mọi tham số nhỏ hoặc duyệt lại ảnh đã đúng chỉ vì clip sai nhịp.

## Tự kiểm

| Lượt | Kết quả | Phản biện và xử lý |
| --- | --- | --- |
| 1 | **FAIL → đã sửa** | Đối chiếu key trong JSON phát hiện bản nháp ghi sai ID gương; sửa đúng `i2v-yin-yang-void-mirror-manifest-r3__take2`, 6 điểm, still thu 85%. Làm rõ trường hợp ảnh đúng/video hỏng cần I2V lại, tránh ép vẽ ảnh mới và tránh âm thầm đổi nghĩa bốn nhóm. Kiểm tự động xác nhận tóm tắt 278 từ, 20/20 key/điểm/đường dẫn khớp và không có liên kết nội bộ hỏng. Bộ đếm PASS liên tiếp về 0. |
| 2 | **PASS (1/2 liên tiếp)** | Rà tính đúng: đối chiếu lại 467 kết quả/372 job, 364 REDO/103 DROP, điểm tối đa 7,5, 10 cặp trước/sau, mọi take nêu tên và số D1. Phân biệt thống kê mode với quan hệ nhân quả; mốc trích với EDL đã kiểm; technical với fit; nguồn có triển vọng với A PASS; 8 với bar 8,5. Không còn lỗi nội dung cần sửa. |
| 3 | **PASS (2/2 liên tiếp)** | Phản biện khả năng thực hiện và đủ đề: đủ bảy câu hỏi, không hứa xác suất hay tự cấp chứng nhận A từ sheet; không coi crop/alpha/phase offset cứu được hình/motion sai; giữ cả nguồn và ảnh tốt; tách ba vùng ghi và người tích hợp, ưu tiên đường gọi lab có bằng chứng. Demo cách lai vẫn chờ anh, D1 không mở lô ở 6,5; bar cuối và luật tham chiếu được giữ. Kiểm lại thống kê mode, 20 ứng viên, tóm tắt 278 từ và hash thân bài không đổi từ lượt PASS trước. Hai lần PASS là tự kiểm tư vấn, không thay hai giám khảo mù của media. |
