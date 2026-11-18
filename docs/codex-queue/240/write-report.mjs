import fs from 'node:fs';
const root='games/typing-survival/art-src',rev=root+'/_review/240';
const jobs=JSON.parse(fs.readFileSync('docs/codex-queue/240/selection.json')),v=JSON.parse(fs.readFileSync(rev+'/validation-delivery.json')),comparison=v.comparison;
const fmt=(x,n=4)=>Number(x).toFixed(n).replace('.',',');
const final=j=>`${root}/ui/${j.dir}/${j.nameFinal}`;
const link=(p,label)=>`[${label}](../../${p})`;
const choices=jobs.map(j=>`| \`${j.nameFinal}\` | ${link(final(j)+'.png',j.name)} | ${link(rev+'/'+j.nameFinal+'-before-after.jpg','Sinh / chốt')} |`).join('\n');
const small=jobs.map(j=>{const sizes=j.dir==='parts'?[10,15,20,30]:[20,24,30,36];return sizes.map(n=>{const m=j.metrics.find(x=>x.n===n);return `| ${j.nameFinal} | ${n} | ${fmt(m.deltaDark,6)} | ${fmt(m.deltaLight,6)} |`;}).join('\n');}).join('\n');
const geometry=jobs.map(j=>{const m=v.files.find(f=>f.file===final(j)+'.png').metrics;return `| ${j.nameFinal} | ${m.bbox.w} × ${m.bbox.h} | ${fmt(m.longestPct,3)}% | ${fmt(Math.max(...m.offsetPct),3)}% | ${fmt(m.keyLeakPct,5)}% |`;}).join('\n');
const alpha=jobs.map(j=>{const ff=[1024,256,128,64].map(n=>v.files.find(f=>f.file===final(j)+(n===1024?'':'.'+n)+'.png'));return `| ${j.nameFinal} | ${ff.map(x=>`${x.metrics.semi16} / ${x.metrics.semi127}`).join(' | ')} |`;}).join('\n');
const iou=jobs.map(j=>{const group=j.dir==='parts'?'parts':j.nameFinal==='station-crest'?'stage':'settings';const pairs=comparison.ious[group].filter(x=>x.a===j.nameFinal||x.b===j.nameFinal);const maxima=[16,127].map(t=>pairs.reduce((best,x)=>x['iou'+t]>best['iou'+t]?x:best));return `| ${j.nameFinal} | ${maxima.map((x,i)=>`${fmt(x['iou'+[16,127][i]],6)} · ${x.a===j.nameFinal?x.b:x.a}`).join(' | ')} |`;}).join('\n');
const report=`# Phiếu 240 · Last Line · Đã giao năm bản sửa, còn ngoại lệ trước nghiệm thu

Ngày 31/10/2026, Codex. Đã sinh **chín ảnh**, chọn năm bản, giao **20 PNG** (1024², 256², 128², 64²), đủ prompt nguyên văn cạnh từng ảnh. Đã sao lưu 31 file chốt cũ trước khi ghi đè. Không gặp HTTP 429 hoặc thông báo phải đợi.

**Chưa đóng phiếu:** cần Claude chấm lại từ 8. Kiểm khổ, sRGBA/sRGB, lề, tâm, màu khóa, tương phản ở cỡ dùng chính, cặp ô đạn và bảo toàn file đạt. **Còn alpha trung gian ngoài mép ở bản thu Lanczos; Station Crest–Hazard có IoU 0,816092 theo alpha ≥128, vượt 0,80.** Giữ tranh và ghi số thật; không tuyên bố mọi kiểm số đã đạt. Giới hạn ba lượt ý tưởng mới của Station Crest đã dùng hết.

## 1. Bộ giao và lượt chọn

Đường dẫn dưới trỏ master 1024². Mỗi bộ có ba bản thu trực tiếp từ master và prompt cạnh cả bốn PNG.

| Tên | Bản chọn | Tờ đối chiếu |
| --- | --- | --- |
${choices}

- **Shake c2-try1:** đổi khung rỗng sang thiết bị đặc, lõi tinh thể lam lớn, hai bóng lệch hai bên và vạch rung dày. Dáng trung tâm là khối vuông xoay chéo; không còn màn hình rỗng. Chọn lượt đầu, không dùng thêm hai lượt còn lại.
- **Reduced Motion c2-try1 → c2-try2:** quả cầu đặc có vòng kẹp và ba vệt. Lượt đầu có quầng alpha phải sửa mạnh (4.826 pixel, tối đa 127/255 trong bước matte master), nên không chọn. Lượt 2 yêu cầu mặt vật hoàn toàn đặc, vệt lam tối hơn và giảm sắc về đầu trái, vòng kẹp chặn vệt; bước matte master còn 867 pixel, tối đa 29/255, RGB không đổi. Các vệt còn giống cánh kim loại ở bản lớn; ở 20 px đọc rõ quả cầu, còn ý “dịu lại” cần Claude xét.
- **Stat Evenness try2:** thay thanh ngang bằng ba cột cao bằng nhau, cùng lõi lam trên một bệ; thân tổng gần vuông, khoảng tối tách ba cột vẫn rõ ở 20/24 px. Không cần dùng try3.
- **Station Crest c2-try1 → c2-try2 → c2-try3:** lượt 1 là lục giác đặc, khác Chapter Crest nhưng gần Hazard (IoU alpha ≥128: 0,875354). Lượt 2 đổi sang khiên, còn 0,816092. Lượt 3 yêu cầu đỉnh phẳng, thân hẹp hơn và đáy nhọn sâu; công cụ giữ phần lớn dáng lượt 2, số IoU vẫn 0,816092. Chọn lượt 3 vì mép nguồn sạch hơn (484 pixel matte master, tối đa 10/255), vẫn giữ toàn bộ các lượt. Không bóp hình để ép qua số. Khiên chứa một trạm, không còn tháp mảnh đứng riêng.
- **Mag Empty try2 → try3:** lượt 2 tăng viền nhưng chênh với Mag Full chỉ 0,256744 ở 10 px. Lượt 3 làm tối lòng và hai đầu, tập trung vàng sáng lên viền. Hậu kỳ căn hộp bao 237×717 thành 233×716 theo vỏ Mag Full, giảm RGB toàn ảnh **5,6%**, trong giới hạn ±10%. Giữ vật liệu, lòng tối và phản lam rất nhẹ; không sửa Mag Full. Chênh đạt 0,301323 ở 10 px, IoU hai ngưỡng đều 1,00 ở 32 px.

Mọi prompt dùng nguyên văn STYLE-UI Lightbearer §4.3, khối KIND của 152/153, phần vật riêng và dòng alpha. Phần KIND của crest cho phép chính chiếc huy hiệu là vật thể, không thêm khung trình bày. Prompt tiếng Anh, báo cáo tiếng Việt. Công cụ: **image_gen.imagegen tích hợp**, không dùng CLI/API thay thế. [Nhật ký nguồn và prompt](240/generated-files.json).

Đã xem tham chiếu HUD chủ dự án, tờ 152/153, Pulse Gun chuẩn cỡ, ảnh 121 và khung 127; thêm các ảnh được nhận để đối chiếu vật liệu. Khung 127 nguồn có nền khóa; tờ xem dùng bản alpha sẵn có, không sửa nguồn.

## 2. Hậu kỳ, khổ và alpha

Nguồn sinh 1254², alpha thật. Đưa hai đầu alpha ≤16 / ≥250 về 0/255, cắt phần rỗng và căn vật có cạnh dài 717 px trên canvas 1024². Chỉ sửa matte, không phủ hay vẽ lại nội dung; bốn icon không đổi sáng RGB. Ô đạn có căn kích thước và giảm sáng toàn ảnh như trên. Bước matte ban đầu chỉ dùng ở master; không dùng bản thu đã ép matte của ứng viên trung gian để giao.

**20/20 PNG giao** đúng khổ và sRGBA/sRGB. **15/15 bản thu** giống pixel phép Lanczos trực tiếp từ master, không làm nét bản 64. Tái lập lại từ cả năm nguồn sinh trong một thư mục mới, **20/20 bản khớp pixel với bộ giao**: [kết quả replay](../../${rev}/replay-verify-final/comparison.json). [Identify](../../${rev}/identify-delivery.txt).

| Tên | Hộp bao master | Cạnh dài / canvas | Lệch tâm lớn nhất | Hue gần magenta trên pixel alpha >0 |
| --- | --- | --- | --- | --- |
${geometry}

Cạnh dài 68–72%, tâm ≤2% đều đạt. Màu gần khóa tối đa cả 20 PNG **${fmt(Math.max(...v.files.map(x=>x.metrics.keyLeakPct)),6)}%**, dưới 0,2%; nguồn alpha thật, không dùng nền khóa. Số trên vẫn ghi theo cách đo bảo thủ H=285…315°, S>0,5.

**Ngoại lệ alpha:** dưới đây là số pixel alpha 1…254 nằm ngoài dải Euclid 3 px quanh đường bao; mỗi ô là **ngưỡng >16 / ngưỡng ≥128**. Giữ cả hai định nghĩa, không chỉ báo cách có lợi.

| Tên | 1024² | 256² | 128² | 64² |
| --- | --- | --- | --- | --- |
${alpha}

Bốn master icon đạt cả hai cách đo. Master Mag Empty sau căn kích thước đạt theo đường bao 50%, còn 354 pixel theo >16. Bản thu có đuôi alpha do Lanczos. Cách ép matte cũ xử lý được số nhưng ở Reduced Motion 64² đổi tới 112/255 tại vài pixel chi tiết; đã giữ ứng viên đó trong hồ sơ, **bản giao giữ nét Lanczos trực tiếp**. Vì [ART_ACCEPTANCE §5](../games/ART_ACCEPTANCE.md#5-hậu-kỳ-không-được-phá-tranh-29102026) yêu cầu “Khi một ngưỡng số mâu thuẫn với tranh … dừng lại, giữ tranh đẹp, ghi mâu thuẫn trong báo cáo để Claude quyết”, dừng sửa để ép số, chờ Claude chốt alpha. Không ghi “alpha sạch hoàn toàn” hoặc cho 2 điểm Dùng tiếp.

## 3. Cỡ nhỏ, tương phản và dáng

Tờ chính có ô icon **20/24 px**, thêm 30/36 px; ô đạn **10/15 px**, trên **#14181f** và **#8c96a3**. Đủ ba cặp Shake–Reduced Motion, Mag Empty–Mag Full, Station Crest–Chapter Crest ở **20/30 px** trên cả hai nền. Có cỡ 720p và 1080p theo 152/153, bốn icon cũ và mảnh HUD thương mại cùng cao, khung 127 và cảnh 121.

Luma sRGB Y′ = 0,2126R′ + 0,7152G′ + 0,0722B′, trung bình màu vật theo trọng số alpha; chênh với luma nền, không phải tỷ lệ WCAG.

| Tên | Cỡ canvas px | Chênh than chì | Chênh thép sáng |
| --- | ---: | ---: | ---: |
${small}

Tất cả icon vượt 0,25 trên than chì. **Mag Empty đạt 0,25 tại cỡ dùng 10/15 px**; không tuyên bố đạt tại master, 20 hoặc 30 px (đó là ô so cặp bổ sung). Ô đạn có biên khá sát, nên cách thu khi tích hợp cần giữ nguyên.

| Cỡ | Luma rỗng | Luma đầy đã nhận | Chênh |
| --- | ---: | ---: | ---: |
${Object.entries(comparison.pair).map(([n,x])=>`| ${n} px | ${fmt(x.empty,6)} | ${fmt(x.full,6)} | ${fmt(x.delta,6)} |`).join('\n')}

IoU thu toàn canvas 32², Lanczos, hai ngưỡng alpha:

| Ảnh | IoU lớn nhất >16 · cặp | IoU lớn nhất ≥128 · cặp |
| --- | --- | --- |
${iou}

Cực đại đã tính đủ 55 cặp của 152, 21 cặp của 153 và 55 cặp của bộ icon ải. Cặp trạng thái ô đạn phải ≥0,95, các tên khác ≤0,80. Shake–Reduced Motion **0,673716 / 0,587031**; Station Crest–Chapter Crest **0,597052 / 0,564384**; Mag Empty–Mag Full **1,00 / 1,00**. Bộ 152 đạt theo cả hai ngưỡng; bộ 153 đạt cả hai. Bộ ải đạt theo >16, **chưa đạt theo ≥128 do Station Crest–Hazard**. Không sửa Hazard, Chapter Crest hoặc bất kỳ ảnh đã nhận nào. [Toàn bộ cặp và số đo](../../${rev}/comparison.json).

## 4. Tờ xem và KA5

- [Tờ chính · cỡ thật](../../${root}/_review/240-sheet-small.jpg).
- [Tờ phụ · nearest để soi mất nét](../../${root}/_review/240-sheet-nearest.jpg): vùng icon phóng 4×, vùng cặp 2×, riêng ô đạn 10/15 phóng 8×; không dùng tờ phóng để thay kiểm cỡ thật.
- Năm tờ sinh/chốt ở bảng §1, đã xem; các lượt không chọn vẫn có tờ riêng trong hồ sơ.

Tự chấm **trên bản giao**, so mức hoàn thiện HUD thương mại, thứ tự **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi mục 0–2. Các ngoại lệ kỹ thuật còn mở nên Dùng tiếp chỉ 1 ở cả năm ảnh. Điểm tự chấm không thay Claude.

| Tên | 1024² | Cỡ dùng 720p | Còn phải xem |
| --- | --- | --- | --- |
| shake | 2/2/2/2/1 → 9 | 2/1,5/2/1,5/1 → 8 | 20 px còn lõi và bóng hai bên; vạch rung mất một phần chi tiết. |
| reduced-motion | 1,5/2/2/2/1 → 8,5 | 1,5/1,5/2/2/1 → 8 | Vòng kẹp và quả cầu rõ; ba vệt vẫn có thể gợi tăng tốc thay vì dịu lại. |
| stat-evenness | 2/2/2/2/1 → 9 | 2/2/2/2/1 → 9 | Ba cột bằng nhau rõ, vân tinh thể nhỏ hòa lại. |
| station-crest | 2/2/2/2/1 → 9 | 2/1,5/2/1,5/1 → 8 | Khiên đặc còn khối ở 20 px; trạm giữa mất chi tiết; IoU với Hazard còn quá ngưỡng ≥128. |
| mag-empty | 2/2/2/2/1 → 9 | 2/1/2/2/1 → 8 | 10 px rất hẹp; rỗng/đầy tách màu rõ, nhưng lòng ô rỗng cần Claude xét trực tiếp trên nền tối. |

## 5. Bảo toàn, phạm vi và phần để lại

| KA1 · ui/icons + ui/parts | Kết quả |
| --- | ---: |
| File trước / sau | ${v.beforeCount} / ${v.afterCount} |
| Thêm | ${v.added.length} |
| File cũ đổi theo quyền ghi đè đúng năm tên | ${v.modified.length} |
| Bản sao cũ khớp MD5 | ${v.backups.filter(x=>x.pass).length}/${v.backups.length} |
| File mất / đổi ngoài danh sách cho phép | ${v.missing.length} / ${v.unauthorized.length} |
| File cũ được bảo vệ giữ nguyên | ${v.protectedCount}/${v.protectedCount} |

Khác luật diff chỉ thêm của 152/153: phiếu 240 cho ghi đè đúng năm bản chốt, nên có 31 thay đổi chủ động và đủ bản sao cũ trong [prev](../../${rev}/prev/). Cập nhật cả prompt cỡ thu để mỗi PNG giao có prompt đúng lượt chọn bên cạnh. Mọi try cũ và ảnh đã nhận giữ nguyên byte. [MD5 trước](../../${rev}/md5-before.txt), [sau](../../${rev}/md5-after.txt), [diff](../../${rev}/md5-diff.txt), [kiểm giao](../../${rev}/validation-delivery.json).

Chỉ ghi đúng các tên/lượt được phép, _review/240* và hồ sơ phiếu 240. Không lệnh Git, build/test game, dev server, trình duyệt, âm thanh, public/, Tu Tiên hoặc .wt-*. Không có capture game/raw frame phải prune. Các tờ xem là hậu kỳ ảnh tài sản theo phạm vi phiếu.

**Không làm tiếp:** không sinh vượt ba lượt Station Crest hoặc tổng ba lượt Mag Empty; không chỉnh ảnh đã nhận; không ép các số alpha bằng thao tác làm hỏng nét thu. Chưa tích hợp public/ và chưa có điểm Claude. Giữ mọi nguồn, prompt, ứng viên và script để tiếp tục theo quyết định của chủ dự án. [Hướng dẫn hồ sơ và tái lập](240/README.md).

**Chủ dự án/Claude cần xem:** tờ cỡ thật, nhất là Reduced Motion có đọc đúng “dịu lại”, ô Mag Empty ở 10 px, và Station Crest ở 20 px cạnh Chapter Crest. Chốt cách xử lý ngoại lệ alpha và IoU với Hazard trước khi đóng phiếu; không coi đây là bộ đã đạt đầy đủ chỉ vì tự chấm từ 8. Không có thời điểm chờ công cụ trong lượt này.
`;
fs.writeFileSync('docs/codex-queue/240-report.md',report);
console.log('Wrote report: '+report.split('\n').length+' lines.');
