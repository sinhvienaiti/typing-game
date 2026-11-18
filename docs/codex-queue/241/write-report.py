from pathlib import Path
import json
out=Path('docs/codex-queue/241');base=Path('games/dragon-hold/art-src/ui/quick-settings/sliders');review=Path('games/dragon-hold/art-src/_review/241')
m=json.loads((out/'metrics-tryfinal.json').read_text());v=json.loads((out/'final-verification.json').read_text());posts=[json.loads((out/f'postprocess-try{n}.json').read_text()) for n in range(1,4)];metrics=[json.loads((out/f'metrics-try{n}.json').read_text()) for n in range(1,4)]
def link(p,title=None):return f'[{title or Path(p).name}](../../{p})'
report='''# Phiếu 241 · Dragonhold · Rãnh thanh trượt bảng Sound

**Trạng thái: đã dùng đủ 3/3 lời gọi, giữ lượt 3 là bản tốt nhất; CHƯA ĐẠT điều kiện nhận.** Đầu trái còn 69 px (6,738%), vượt Kiểm 4 là 61 px; đầu phải 46 px (4,492%) đạt. Không gọi thêm, không san phẳng độ sáng hay cắt bỏ phần vẽ để ép qua số. Chờ Claude chấm lại ở 720p và quyết hướng tiếp theo.

## File giao và bản lưu

'''
report+='- Bản tốt nhất chờ duyệt: '+link(base/'slider-track.png')+' (1024×64), '+link(base/'slider-track.512.png')+' (512×32), '+link(base/'slider-track.prompt.txt')+'.\n'
report+='- Ba bản sinh và prompt chính xác: `'+str(base)+'/slider-track.c2-try1..3.png` và `.prompt.txt`; mỗi lượt còn có `.processed.png`, `.512.processed.png` cùng prompt cạnh ảnh. Không đụng các `try*` cũ.\n'
report+='- Bản trước khi thay: `'+str(review)+'/prev/slider-track.png`, `slider-track.512.png`, `slider-track.prompt.txt`; SHA-256 trùng mốc ban đầu. Có thêm bản sao prompt cũ của ảnh 512 để bảo toàn ngữ cảnh.\n'
report+='- Tờ xem: '+link(review/'241-sheet.jpg')+'; đủ 0/50/100%, 720p/1080p, nền tối/sáng, núm đã nhận; bản phóng point ×3, sáu cỡ kéo giãn, icon vol-master 20/28 px, HUD tham chiếu chủ dự án và ô “kit hôm nay”.\n'
report+='- Tờ bản sinh | bản hậu kỳ: '+', '.join(link(review/f'try{n}-compare.jpg') for n in range(1,4))+'. Hai ô cùng cỡ, ảnh giữ tỉ lệ.\n'
report+='- Bằng chứng số: [metrics-tryfinal.json](241/metrics-tryfinal.json), [final-verification.json](241/final-verification.json), [calls.json](241/calls.json), [prompts.json](241/prompts.json).\n'
report+='''
## Preflight, tham chiếu và phạm vi

Thực hiện ngày 31/10/2026, khoảng 05:27–05:33 giờ Việt Nam. ImageMagick 7.1.2-34 trên macOS; font `/System/Library/Fonts/Supplemental/Arial.ttf`. Công cụ tích hợp `image_gen`, không dùng CLI/API sinh ảnh khác. Không gặp 429, lỗi hạn mức hay yêu cầu thử lại sau.

Phiếu 241 thay các điều kiện thư mục rỗng của 225 vì bộ 225 đã có và năm ảnh đã được nhận. Trước sinh chụp SHA-256 toàn bộ 184 file trong `games/dragon-hold/art-src/ui/quick-settings/`; không coi file đã có là lỗi preflight. Các kiểm số, khổ giao, tờ so sánh, giới hạn hậu kỳ và tham chiếu của 225 vẫn áp dụng.

Đã xem mức hoàn thiện HUD trong `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp` nhưng không đính kèm ảnh này khi sinh. Mỗi lời gọi đính kèm ba tham chiếu Dragonhold: `selected/hud-settings.png`, `selected/vol-master.png`, `ui/parts/keycap.png`; thêm `slider-thumb.png` đã nhận để khớp vàng đồng ấm và sắt tối. Lượt 3 thêm bản sinh lượt 1 làm ảnh đích chỉnh sửa. STYLE-UI và PART giữ từ prompt Dragonhold, bỏ câu chiếm 70% cạnh dài như luật cho rãnh.

## Ba lượt và hậu kỳ

| Lượt | Thay đổi trong prompt | Kết quả và lý do chọn/bỏ |
| --- | --- | --- |
| 1 | Ý tưởng mới: thân dài 16:1, mũ vát 1%, lõi sắt tối, viền vàng đồng; xin khung 2048×128 RGBA. | Dáng gần đúng; đầu trái 86 px, phải 50 px. Chưa chọn. |
| 2 | Thu mũ thành nút sắt tối 0,5%, yêu cầu độ sáng đều tới sát đầu. | Công cụ trả vật 11,6718:1; thêm đệm làm vật ngắn trong khung, đầu đo 179/177 px. Bỏ. |
| 3 | Chỉnh trực tiếp lượt 1 để giữ dáng dài, bỏ vùng tối dần gần đầu trái, mũ gọn cùng tỉ lệ sáng/tối với thân. | Vật 16,4731:1; dáng và cỡ nhỏ tốt nhất, đầu 69/46 px. Giữ để Claude xét, chưa nhận. |

Cả ba công cụ trả khung cao hơn khung 16:1 đã xin. Thực hiện đúng quy tắc 241: cắt hộp bao alpha >16, thêm **đệm trong suốt** về khung nguồn nguyên tỉ lệ 16:1, rồi thu Lanczos. Hai bản 1024×64 và 512×32 thu độc lập từ cùng bản đệm. Không co không đều. Không thay RGB, không chỉnh sáng, không tô lại, ghép hay bỏ phần vẽ.

'''
report+='| Lượt | Khổ sinh | Hộp bao (x,y,w,h) | w/h | Khung đệm | Co x / y bản 1024 | Co x / y bản 512 |\n| --- | --- | --- | ---: | --- | --- | --- |\n'
for n,p in enumerate(posts,1):
 scales=[' / '.join(f'{r[k]:.9f}' for k in ['scaleX','scaleY']) for r in p['outputs']]
 report+=f"| {n} | {'×'.join(map(str,p['sourceSize']))} | {p['bboxAlphaGT16']} | {p['bboxRatio']:.6f} | {'×'.join(map(str,p['paddedSize']))} | {scales[0]} | {scales[1]} |\n"
report+='''
Lượt 3 đệm tổng 4 px ngang, 3 px dọc; mọi hệ số x = y. Mức lệch hộp bao so với 16:1 là +2,957%; phần đệm hấp thụ sai lệch, không ép dẹt hai đầu.

Alpha công cụ sinh có phần trong lòng vật gần đục nhưng chưa 255. Sửa alpha theo phép kẹp mép, giữ mọi RGB: lượt 1–2 kẹp ≤2 về 0, ≥253 về 255; lượt 3 kẹp ≤2 về 0, ≥250 về 255 (chênh tối đa 5/255). Alpha lẻ ngoài dải mép Chebyshev 3 px quanh mặt nạ ≥128 về phía 0/255 gần nhất. Lượt 3 không còn pixel phải xử lý theo quy tắc ngoài dải. Không dùng bước tách khóa vì nguồn có RGBA thật; vẫn kiểm sắc magenta như 225. Chi tiết trong `postprocess-try*.json`.

## Kiểm 1 · Bảo toàn file

184 file trước, 202 file sau; thêm 18 file có tiền tố `slider-track.c2-try` trong đúng thư mục được phép. Chỉ ba file được phép thay đổi: `slider-track.png`, `slider-track.512.png`, `slider-track.prompt.txt`; bản lưu trước thay trùng SHA-256. **181 file cũ khác giữ nguyên**, bao gồm toàn bộ núm Dragonhold, bộ 180, selected và mọi lượt thử cũ. Không ghi vào Wordwoven hoặc Last Line. Chi tiết ở [sha256-before.json](241/sha256-before.json), [sha256-after.json](241/sha256-after.json) và [final-verification.json](241/final-verification.json). Kiểm 1 đạt theo ngoại lệ ghi đè của 241.

## Kiểm 2–3 · Khổ và alpha của bản tốt nhất

'''
report+='| File | Khổ / kênh | Alpha lẻ ngoài mép 3 px | Pixel sắc khóa / pixel có alpha | Tỷ lệ khóa | Alpha 255 trong 80% giữa |\n| --- | --- | ---: | --- | ---: | ---: |\n'
for a in m['alpha']:
 report+=f"| `{Path(a['file']).name}` | {'×'.join(map(str,a['size']))} / {a['channels']} | {a['partialOutside3px']} | {a['keyHuePixels']}/{a['visiblePixels']} | {a['keyHuePercent']:.6f}% | {a['centralOpaqueFraction']:.6f} |\n"
report+='\nKiểm 2–3 đạt: đúng 1024×64 / 512×32 sRGBA, tỷ lệ sắc khóa ≤0,2%, không alpha lẻ ngoài mép; alpha 255 giữa bản 1024 là 0,917940 ≥0,90.\n'
report+='''
## Kiểm 4 · Kéo giãn và đầu rãnh

| Cỡ kéo giãn | Độ lệch chuẩn luma cột, 80% giữa | Ngưỡng |
| --- | ---: | --- |
'''
for r in m['stretch']:report+=f"| {'×'.join(map(str,r['size']))} | {r['centralColumnLumaStd']:.9f} | ≤0,05 · đạt |\n"
report+='''
Đầu đo trên 1024×64, nền tối `#2b2118`, trung vị luma giữa **0,336930002**. Dùng đúng phép tìm 16 cột liên tiếp trong ±0,03 của 225: **trái 69 px, phải 46 px**; giới hạn ≤61 px mỗi đầu. Kiểm 4 **CHƯA ĐẠT** vì trái vượt 8 px. Sai lệch độ sáng vẫn trải dài hơn mũ nhìn thấy; không đổi thuật toán, nền hay ngưỡng để cho qua. Tất cả sáu cỡ đều đạt độ ổn định phần giữa.

## Kiểm 5 · Đọc ở cỡ trong game

Đo tại 50%, rãnh 210×10 và ô núm 22 px (720p), 315×15 và ô núm 33 px (1080p); rãnh bỏ vùng bị núm che. Luma đúng công thức 225 trên sRGB 0–1, sau composite nền, chỉ pixel alpha ≥128. Núm dùng file đã nhận, không cắt lại lề.

| Nền | Cỡ | Y rãnh | Y núm | Δ núm−rãnh | Δ rãnh−nền |
| --- | --- | ---: | ---: | ---: | ---: |
'''
for r in m['readability']:
 report+=f"| `{r['background']}` | {'720p' if r['scale']==1 else '1080p'} | {r['trackMeanLuma']:.6f} | {r['thumbMeanLuma']:.6f} | {r['thumbMinusTrack']:.6f} | {r['trackMinusPanel']:.6f} |\n"
report+='''
Kiểm 5 đạt trên nền tối ở cả hai cỡ: Δ núm−rãnh ≥0,25 và Δ rãnh−nền ≥0,12. Trên nền sáng rãnh tối hơn nền; số có dấu âm đúng dự kiến, không dùng `passDark` của các hàng sáng để kết luận thất bại. Đã xem trực tiếp tờ xem và tờ so sánh, không chỉ đọc số.

## KA5 · Tự chấm bản hậu kỳ

| Tiêu chí | Điểm / 2 | Nhận xét ở khổ giao và 720p |
| --- | ---: | --- |
| Đúng đề | 2 | Rãnh sắt tối viền vàng đồng, không mức đầy, không ký tự. |
| Đọc được trong game | 1,5 | Đường vàng và lõi rõ, núm nổi; đoạn tối gần đầu trái còn kéo dài. |
| Hợp bộ | 2 | Cùng màu vàng ấm, chất sắt tối và nét vát với núm đã nhận; đối chiếu HUD thương mại. |
| Hình khối | 1,5 | Thân dài thẳng, không ép dẹt; mũ vát còn đọc như mảnh khung hơn một nút bịt rất nhỏ. |
| Dùng được cho bước sau | 0,5 | Khổ, alpha, tương phản đạt; Kiểm 4 chưa đạt nên không cho 2 điểm. |
| **Tổng** | **7,5/10 · CHƯA ĐẠT** | **Giữ bản tốt nhất sau 3 lượt để Claude quyết; chưa nhận.** |

## Chỗ khác phiếu 225 và việc không làm

- 241 thay co không đều bằng đệm trong suốt và co đều. Nguồn sinh RGBA thật theo yêu cầu nền trong suốt của 241; không dùng nền khóa magenta. Không can thiệp phần vẽ để đạt số.
- Thay ba file rãnh được phép bằng lượt 3 sau khi lưu bản cũ; tên bản chốt chỉ là nơi giữ ứng viên tốt nhất, không có nghĩa đã được nhận. Năm ảnh đã nhận không sửa hay xóa.
- `slider-track.512.prompt.txt` cũ giữ nguyên vì không thuộc danh sách được ghi đè của 241. Prompt đúng của bản 512 mới ở `slider-track.c2-try3.512.processed.prompt.txt` và `slider-track.prompt.txt`; Claude cần lưu ý khi duyệt.
- Không mở game, không chạy build/test, không chỉnh mã, CSS, âm thanh, public, game khác, Tu Tiên hay `.wt-*`; không chạy lệnh Git. Không tạo capture trình duyệt hay raw frames; không có capture cần prune.
- Ba ảnh nguồn, ba tờ so sánh và ảnh cắt/đệm phục vụ tái hiện báo cáo tổng dung lượng nhỏ; giữ dưới các đường dẫn được phép, không ghi ảnh vào docs.

## Việc của Claude

- Xem `241-sheet.jpg`, bản 1024 và 720p; chấm lại lượt 3. Đầu trái 69 px còn vượt ngưỡng; quyết hướng tiếp theo sau giới hạn 3/3, không coi phiếu đã đạt.
- Chỉ chuyển sang gắn khi ảnh được nhận. Phiếu này không chép public, không sửa `skin.sliderTrack`.
- Ô “kit hôm nay” vẫn có màu `#4A505C` dưới rãnh và ô trắng `#F3F4F6` dưới núm, như CSS của 225; phiếu gắn sau xử lý nền kit theo thẩm quyền riêng.
- Sao lưu media theo quy trình của chủ dự án sau khi duyệt; phiếu này không chạy `pnpm media:push`.

## Tái hiện kiểm và prompt đầy đủ

Từ gốc repo, `node docs/codex-queue/241/audit.mjs final`; dựng tờ xem bằng `node docs/codex-queue/241/review.mjs`. Script hậu kỳ: `node docs/codex-queue/241/postprocess.mjs <1|2|3>`, chỉ ghi file của 241, không gọi sinh ảnh. Lệnh ImageMagick ghép ảnh lưu trong [review-commands.json](241/review-commands.json).

'''
for n in range(1,4):report+=f"### Lượt {n}\n\n```text\n"+(base/f'slider-track.c2-try{n}.prompt.txt').read_text().strip()+'\n```\n\n'
Path('docs/codex-queue/241-report.md').write_text(report)
(out/'ka5.json').write_text(json.dumps({'selectedTry':3,'score':7.5,'criteria':[2,1.5,2,1.5,.5],'pass':False,'reason':'Đầu trái 69 px > 61 px; đã dùng đủ 3 lượt, chờ Claude chấm lại.'},ensure_ascii=False,indent=2)+'\n')
print('Đã ghi docs/codex-queue/241-report.md; trạng thái CHƯA ĐẠT Kiểm 4.')
