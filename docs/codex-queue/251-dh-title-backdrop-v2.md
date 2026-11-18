# Phiếu 251 · Dragonhold · Nền màn tựa v2 và logo r2

**Nguồn:**
- Phiếu `119-dh-title-keyart.md`: khối STYLE, STYLE-UI và LOGO, luật hậu kỳ, thang M và Q, kiểm 2–9. Phiếu này chỉ ghi chỗ khác.
- Lượt chấm 01/11 khoảng 02:40: hai giám khảo mù chấm màn tựa thật (workflow `dh-title-119`). Cả màn 6,5 và 6,5; nền 7,5 và 7,5; logo 7,5 và 7,5; huy hiệu 4 và 4 (huy hiệu bỏ khỏi màn tựa).
- Ảnh tham chiếu của chủ dự án (mốc 9): `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp`.

**Báo cáo:** `docs/codex-queue/251-report.md` (tiếng Việt) và thư mục `docs/codex-queue/251/`.

## Vì sao làm lại

Nền 119 (`title-backdrop`) và logo 119 đang gắn tạm trên màn tựa. Giám khảo nêu các lỗi sau ở nền:
- **quá nhiều tâm điểm:** hai tượng rồng đá, rồng bay, đầu thú đá, chậu lửa, cổng, cầu, thác;
- **rồng lửa nhỏ:** chỉ chiếm khoảng 20 % bề ngang, bị đẩy vào góc trên phải, chóp cánh bị cắt ở mép trên;
- **không có bầy Héo:** chỉ có sương tím như trang trí, nên không đọc ra câu chuyện "rồng giữ đèo trước bầy dịch";
- **không có hình người** để thấy tầm vóc;
- **nhòe ở 1080p:** ảnh 1536 px bị phóng 1,25 lần, kiến trúc thành mềm kiểu AI;
- **góc trên phải chói:** đúng chỗ đặt bánh răng và loa.

Logo đọc đúng nhưng:
- mặt chữ tối (đá than vân đỏ, tương phản trong chữ thấp);
- nét "gon" dày mỏng không đều, vân nứt rối;
- con rồng trên chữ D quá nhỏ;
- có một mảng hồng cá hồi ở mép dưới màng cánh.

## Việc

### `title-backdrop.v2`

- **Khổ:** lớn nhất công cụ cho được, tỉ lệ 3:2 hay 16:9. Bản giao tối thiểu 2560 px bề ngang.
  - Nếu công cụ chỉ cho 1536, giao thêm bản phóng `title-backdrop.v2.2x.png` bằng một bộ phóng ảnh có tên. Ghi tên và lệnh; không tô thêm chi tiết bằng tay.
- **Prompt:** STYLE của 119, rồi khối TITLE-V2 dưới đây.

**TITLE-V2**
```text
Scene: the pass at dawn, one clear focal point. The ancient fortress gate spans the pass in the centre-right; on top of the gate a huge red-orange fire dragon with a warm cream belly and dark horns rears with wings spread wide, fully inside the frame, breathing a bright stream of fire down into the valley. Below, a horde of moss creatures and blight wolves with violet rags and glowing yellow-green eyes pours out of the dark pine forest along the river road toward the gate, a violet blight creeping behind them; tiny armoured defenders on the rampart give the scale. Colossal granite cliffs frame the pass, snow peaks fade into blue haze behind, long gold dawn light from the left, god rays through the mist. Only one dragon. Keep the carved cliff statues subtle so they do not compete with the dragon. The top centre is calm sky for the logo; the lower left third is calmer and darker for the menu; the top right corner is not the brightest part of the sky.
```

### `logo.r2`

- STYLE-UI và khối LOGO của 119, thêm câu này:
```text
Bold, heavy, evenly weighted letters with a bright hammered-gold face and a dark iron bevel, so the word reads at once on a bright sky; clean simple shapes, few cracks; the small dragon on the D is clearly a dragon with spread wings. No pink or salmon anywhere.
```
- Hậu kỳ như 119: `logo.r2.alpha.png` và `logo.r2.512.png`. Cạnh dài nguồn ≥ 2048 nếu được.

## Kiểm riêng

- Mọi kiểm 2–9 của 119 áp cho hai ảnh này. Chỗ cho logo và menu đo trên bản cắt 16:9 ở giữa.
- **Tâm điểm:** rồng chiếm ≥ 35 % bề ngang khung 16:9, trọn trong khung (cả chóp cánh), cách mép trên ≥ 4 %. Có đúng một con rồng.
- **Bầy Héo:** đọc ra ở bản thu 960 px. Ghi "đọc ra" hoặc "chưa".
- **Góc trên phải** (x 88–100 %, y 0–10 %): luma trung bình ≤ 0,75, để bánh răng và loa nổi.
- **Logo:** chính tả 10 chữ cái như 119; 0 điểm alpha > 0 có hue 285–345° và S > 0,35 ở dải 4 px quanh mép; tương phản mặt chữ với trời sáng nhất của `title-backdrop.v2` ≥ 3:1.
- **Mock màn tựa** `_review/251-title-mock.jpg`: nền v2 cắt 16:9, logo r2 rộng 45 % ở giữa trên, chỗ menu ở dưới trái. Đặt cạnh mock 119.

## Chỉ được ghi

- `games/dragon-hold/art-src/ui/title-epic/title-backdrop.v2*`, `logo.r2*` (mới, không ghi đè).
- `games/dragon-hold/art-src/_review/251*`.
- `docs/codex-queue/251-report.md`, `docs/codex-queue/251/`.

## Nhận

Claude chấm trên màn tựa thật ở 1280×720 và 1920×1080, cùng hai giám khảo mù. Nhận khi nền và logo đều đạt M ≥ 8, Q ≥ 8.
