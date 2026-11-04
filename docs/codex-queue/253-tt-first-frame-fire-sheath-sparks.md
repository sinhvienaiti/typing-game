# Phiếu 253 · Tu Tiên · Khung đầu cho lửa bọc lưỡi kiếm và chùm tia lửa (Sword × Fire)

> **TẠM GIỮ, KHÔNG CHẠY (04/11/2026).** Phiếu này chờ kết quả thí điểm 252 và phải viết lại theo bản phản biện 04/11 (các mục 3, 4, 7, 8, 10, 12, 15). Ngoài ra:
> - Món `fire-sheath` đi ngược kế hoạch đã chốt (`VFX_PRODUCTION_PIPELINE.md` §0.2 và §10.2). Thứ gắn vào lưỡi kiếm là lưới mang texture cuộn, cắt từ clip lửa đã duyệt, không phải thẻ khung đầu. Muốn giữ món này phải có quyết định mới.
> - Món tia lửa đổi tên thành `fire-spark-sheaves`, vì `fire-sparks` trùng atlas đã có.

**Nguồn và luật:**
- **Luật chung của đợt: mục "Luật chung của đợt 252–254" trong `docs/codex-queue/252-tt-first-frame-fire-impact.md`.** Mục đó gồm:
  - đường dẫn được ghi, các điều cấm;
  - tham chiếu được xem, gu của chủ dự án;
  - định dạng ảnh (1536×1024 → `.master.png` 1536×864, `.540.png`, `.alpha.png`);
  - Kiểm 1–7, giới hạn 3 lượt mỗi biến thể, cách báo hết hạn mức.

  Phiếu này chỉ ghi chỗ khác.
- Hai bài chấm đêm 04/11: `games/immortality-cultivation/tmp/shots/overnight/judge-1.md` và `judge-2.md`.

**Báo cáo:** `docs/codex-queue/253-report.md` và `docs/codex-queue/253/`. Model `gpt-6.1-sol`, mức `high`.

## Món 1: `fire-sheath` (lửa liếm quanh lưỡi kiếm khi bay), 3 biến thể

Trong game, ảnh này thành một thẻ nằm dọc lưỡi kiếm thật. Lưỡi kiếm do model 3D vẽ, nên ảnh **không vẽ kiếm**, chỉ vẽ lửa quanh một trục trống.

Bản tốt nhất đêm qua là `aura-fire-flame-sheath` (`ff-f1-c4`), được 7 ở cả hai giám khảo. Nó trượt 8,5 vì bốn chỗ:
- lửa đối xứng, không bạt về sau;
- khối lửa ở phía chuôi làm cả thẻ giống **đầu mũi tên**;
- trên đá sáng thành vệt kem;
- dải quá dày, không có lõi sáng.

**Bố cục chung:**
- Trục kiếm nằm ngang ở giữa khung, dài khoảng 70 % bề ngang khung.
- Mũi kiếm ở **bên phải**, chuôi ở **bên trái**. Kiếm bay về phía phải, nên mọi lưỡi lửa **bạt ngược về bên trái**, như lửa trên vật đang lao đi.
- Gốc lửa sát hai mép của trục trống. Lửa bên trên dài hơn bên dưới một chút (bất đối xứng).
- Phía mũi thu lại thành **mũi kim** sáng. Phía chuôi **tan dần thành vài lưỡi mảnh**, không có cục, không có hình đầu mũi tên.
- Dọc trục có một đường nóng trắng vàng mảnh.
- Cả dải chỉ cao 20–30 % chiều cao khung.

| Biến thể | Ý riêng (EN) |
|---|---|
| `v1` | slender, elegant flame tongues licking back along both edges of an empty horizontal blade line, longer and more curled on the upper edge |
| `v2` | flames that peel off the blade line in a rhythm of three soft surges, each surge curling back and thinning into wisps, like silk ribbons of fire |
| `v3` | a tight, intense sheath of short flickering flame along the blade line that streams back into two long, thin flame ribbons trailing off the left end |

Câu chung ở cuối prompt:

> Everything flows backward to the left as if the blade is flying fast to the right. The right end narrows to a bright needle point of white-gold heat; the left end dissolves into a few thin wisps with no blob or arrowhead shape. Soft, flowing, slightly realistic fire in the style of premium anime xianxia game effects, deep wine-red outer edges through crimson, vermilion and orange to amber, a thin white-gold hot line along the empty blade axis, a few tiny sharp sparkles. No sword or metal drawn, the blade axis is empty. Pure black background, wide empty margins, no text, no frame.

Kiểm thêm:
- **Kiểm 8, bạt về sau.** Chia dải sáng thành nửa trái và nửa phải. Diện tích sáng nửa trái lớn hơn nửa phải 1,2 lần trở lên. Cột sáng cao nhất không nằm trong 15 % bên trái cùng (không có cục ở chuôi).
- **Kiểm 9, mũi kim.** Ở 5 % bên phải cùng của dải sáng, bề cao vệt sáng ≤ 25 % bề cao lớn nhất của dải.

## Món 2: `fire-sparks` (chùm tia lửa văng theo nhát chém), 3 biến thể

Đêm qua `fire-spark-spray` chỉ được 5,5, vì ba chỗ:
- giống tia máy mài: cam đều, thẳng;
- vệt gãy khúc như sét;
- không có đầu trắng vàng.

Bản khác thì tỏa 360°, sai hướng. Bản mới phải theo **một hướng vung**.

**Bố cục chung:**
- 2–3 chùm vệt mảnh xuất phát gần giữa bên trái, bay lên sang phải theo đường vung.
- Mỗi vệt cong mượt, không gãy khúc. Dài ngắn khác nhau, xếp so le.
- Mỗi vệt có **đầu trắng vàng nhỏ sắc**, đuôi nhạt dần qua cam, son, rồi đỏ rượu.
- Một hai đầu vệt có điểm lóe bốn cánh rất nhỏ.

| Biến thể | Ý riêng (EN) |
|---|---|
| `v1` | two dense sheaves of fine, gently curving spark streaks thrown up and to the right along a sword swing |
| `v2` | three loose fans of long and short spark streaks of different lengths, the longest ones arcing slightly downward at their ends as they lose speed |
| `v3` | one main sheaf of long curving streaks with a scatter of short bright flecks and tiny ember dots around its tip |

Câu chung ở cuối prompt:

> Each streak is a smooth curve, never zigzag, with a small sharp white-gold head and a tail fading through orange and vermilion to deep wine-red. Premium anime xianxia game effect, elegant and radiant, not industrial grinder sparks, not fireworks, not lightning. Pure black background, wide empty margins, no text, no frame.

Kiểm thêm:
- **Kiểm 8, một hướng.** Tính hướng chính của các điểm sáng (PCA trên tọa độ điểm có luma > 0,1). Ít nhất 75 % diện tích sáng nằm trong cung ±60° quanh hướng đó, nhìn từ điểm xuất phát.
- **Kiểm 9, đầu vệt nóng.** Đếm các điểm có luma ≥ 0,85: chúng phải nằm thành ≥ 8 cụm nhỏ tách nhau (đầu vệt), không thành một khối.

## Nhận
- Thư mục `fire-sheath/selected/` có 3 biến thể và `fire-sparks/selected/` có 3 biến thể, mỗi biến thể đủ ba file.
- Tấm xem `tmp/shots/codex-first-frames/fire-sheath-sheet.jpg` và `fire-sparks-sheet.jpg`.
- Báo cáo ghi số Kiểm 1–9, prompt từng lượt, điểm tự chấm, và biến thể nên đưa vào Firefly trước.
