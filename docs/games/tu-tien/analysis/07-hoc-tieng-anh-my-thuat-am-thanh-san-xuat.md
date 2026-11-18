# Tu Tiên Thủ Ải — 07. Học tiếng Anh, mỹ thuật, âm thanh và phạm vi sản xuất (24/10/2026)

> **Mảng:** học tiếng Anh trong trận và trong tu luyện; trình bày (hình, VFX, âm); phạm vi sản xuất, mốc, lát chơi đầu.
> **Trạng thái:** phân tích đề xuất, chưa có mã. Mọi con số ghi "thử" là số khởi điểm, phải đo lại bằng bot và người chơi.
> **Đã đọc:** Codex V2.2 (`TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md` §0–1, 8–9, 11, 14–19, 21–27); `docs/games/{SPLIT_PLAN,BALANCE,AUDIO_PIPELINE}.md`; `tools/audio-lab/DECISIONS.md` Q6; `docs/games/dragon-lane/{DESIGN,01,05}.md`, `research/art-pipeline.md`; `shared/game-kit/{typing,vocab,learning,speech,balance}`; `shared/voice/README.md`; `shared/vocabulary/index.json`, `topics/index.json`; mã `games/dragon-hold/src`, `games/typing-survival/docs/BUILD_S1.md`; khung hình video QCBH (t004, t068, t120, t160, t184, med_08, med_20, boss_10, boss_20).
> **Ký hiệu nguồn:** [video] khung hình chủ dự án quay; [Codex doc]; [web: url]; [trí nhớ] (chưa kiểm chứng).

## 1. Tóm tắt

- **Chữ nằm trên "Bàn Ấn" (thanh kỹ năng), không nằm trên đầu quái.** Thú triều có thể dày 150–300 con mà số chữ phải đọc vẫn cố định ≤ 8. Đây là luật quan trọng nhất để học không bị lấn trong cảnh đông. Chỉ tinh anh và Thú vương mang tối đa 2 "Ấn chữ".
- **Cảnh giới không nâng cấp từ.** Cấp từ lấy từ hồ sơ học (100 cấp, 18.000 mục của `shared/vocabulary`). Cảnh giới chỉ mở thêm *dạng tác vụ học*: nhớ nghĩa, nghe, cụm từ.
- **Công pháp = bài học.** Mỗi công pháp gắn một nhóm từ (một chủ đề 9–16 từ, hoặc một lát cấp từ). Tĩnh Tu đưa từ mới vào, trận luyện từ đó, tham ngộ kiểm nhớ thật. Từ mới không bao giờ nằm trên ô phải dùng gấp.
- **Mini-game tu luyện của Codex (§18) giữ khung, nhưng phải đổi tiêu chí chọn.** Nếu chỉ chọn theo màu nhãn thì chỉ là gõ chép. Bản đề xuất: Tâm ma là từ *không thuộc đạo đề* của công pháp; bậc cao ẩn nhãn để người chơi chọn theo nghĩa; bậc cao nhất hiện nghĩa Việt và bắt gõ từ Anh (nhớ thật).
- **Hình: "nhìn 2D, chạy trên Three.js".** Đề xuất phương án A: camera 3/4 cố định, shader thủy mặc, đất và phông là tranh 2D, sinh vật là GLB Tripo/Meshy vẽ bằng đám đông instanced. Phương án B (dự phòng): sprite nướng từ cùng GLB bằng `bake_impostor.py`. Loại phương án vẽ tay từng khung. Cần chủ dự án duyệt, vì Codex §0 ghi hướng "2D/sprite".
- **Âm theo Q6:** mỗi âm hành động có chuẩn bị, phát, thân, đuôi vang của hẻm núi. Cỡ âm theo cỡ chiêu. Cấm "bụp/thụp", puff, pop, đồ chơi, retro. Tiếng bầy dùng một lớp nền theo mật độ, không mỗi con một tiếng.
- **Lát chơi đầu:** 1 ải, 1 trận triều (6 đợt + Thú vương), 2 trường phái (Kiếm, Hỏa), solo và solo + 1 bot, chỉ Typing. Khoảng 13 GLB, ~100 ảnh 2D, ~55 âm, 3 bản nhạc. Ước 7–9 tuần lịch (hộp xám chơi được sau 2–3 tuần), phụ thuộc giờ Tripo và giờ nghe của chủ dự án.
- **Voice/Hybrid để sau MVP.** `shared/voice` chưa có bộ giải mã chạy thật. Hợp đồng hành động có ID (Codex §1.4) thì làm ngay từ M0 để sau này chỉ cắm kênh mới.

## 2. QCBH làm thế nào (chỉ phần liên quan mảng này)

| Quan sát | Nguồn | Bài học cho ta |
|---|---|---|
| Tu luyện: bóng người thiền trên nền tối, cột sáng. Cầu trắng, cầu lam và cầu đỏ có chữ "魔" bay về thân. Người chơi bấm cầu tốt, tránh cầu đỏ. HUD góc trên trái ghi Ngộ tính 101, tỉ lệ sinh cầu 90 %, tốc độ cầu "Cực chậm", thanh tiến độ | [video 0:14–0:44, med_08, med_20] | Chỉ số nhân vật làm mini-game dễ hơn (sinh nhiều hơn, bay chậm hơn). Đây là phản xạ chuột, không có nội dung để học. Ta giữ ý "chọn lọc dưới áp lực", nhưng thay nội dung bằng từ và nghĩa |
| Học bằng thu cầu "ngộ", phá cầu "ma"; luyện mở dòng hiệu ứng; tham ngộ đổi dòng | [Codex doc §17, R11–R12] | Ba nhu cầu: tiếp nhận, luyện, biến đổi. Ta ghép ba nhu cầu này vào ba bậc của bài từ |
| Tooltip kỹ năng: thân pháp hồi 20 s, tốn 25 Linh lực, mô tả có số. "Kỹ năng tu luyện (1/6)" là 6 dòng khóa. "Tiến độ tu luyện 220/300" | [video t120] | Dòng mở theo tiến độ luyện là móc tốt để gắn với bài từ (mục 4.6). Ta tách tiến độ RPG với độ thuộc từ (Codex §17.1) |
| Trận: nhìn từ trên chéo, tranh mực xám và lục nhạt, rừng trúc, nghĩa địa. Điểm màu đậm chỉ ở đòn: vệt kiếm vàng, nổ đỏ, số đỏ, "Bạo Kích" vàng. Bia đá, tảng đá làm vật che | [video t068, t160, t184] | Nền giảm bão hòa, đòn bão hòa: hợp với luật "bậc nổi" của repo. Ta không dùng máu đỏ (xem 4.8) |
| Mỗi màn hình chỉ có 5–10 quái. Nhãn tên đồ rơi hiện thành chữ trên đất; ở t184 có 6 nhãn "Hạ Phẩm Hồn Thạch" cùng lúc | [video t184] | Cách này không chịu được thú triều 150–300 con. Đồ thường tự hút, không hiện nhãn chữ. Chỉ đồ hiếm có icon |
| HUD đáy: 3 thanh Sinh lực, Linh lực, Niệm lực; 5 ô đan dược có số lượng; 4 ô kỹ năng, võ kỹ hồi 0,1–0,3 s; nút "Trốn" bên trái; chân dung pet bên phải. Bản đồ phòng góc trên phải, đếm quái ở giữa trên | [video t160, t068] | Võ kỹ hồi 0,2 s là nhịp bấm chuột. Gõ một từ tốn 1,4–3 s, nên vai này giao cho đánh nền tự động và ô liên tục, không giao cho kỹ năng |
| Boss lớn (cao ~1/4 màn), tên và thanh máu ở giữa trên, sao choáng, nổ bụi lửa | [video boss_10, boss_20] | Boss cần 180–260 px ở 1080p và vạch báo đòn trên đất |
| Pet nhỏ theo sát nhân vật | [video t160, boss_20] | Pet đọc được nhờ dáng khác hẳn người |
| Có cảnh chiến đấu "兽潮" (thú triều) với nhạc riêng | [web: https://steamcommunity.com/sharedfiles/filedetails/changelog/2815215162] (changelog mod thay nhạc cảnh "兽潮") | Xác nhận có cảnh thú triều trong bản gốc. Luật chi tiết (thành bị tấn công, người chơi giữ thành) chỉ là [trí nhớ] |
| Engine, kỹ thuật làm hình (sprite hay 3D) | Tìm web không ra nguồn đáng tin | Không suy kỹ thuật từ QCBH. Chỉ học cảm giác hình |
| Âm thanh | [video] chỉ có khung hình, không có tiếng | Không rút ra kết luận về âm từ video |

## 3. Codex V2.2 nói gì về mảng này: giữ, sửa, bỏ

| § | Nội dung | Quyết định | Lý do |
|---|---|---|---|
| §1.1–1.3 | Typing, Voice, Hybrid; WASD có trạng thái riêng; mũi tên và click-to-move | **Giữ, sửa thứ tự.** MVP chỉ Typing + click-to-move + mũi tên. Chế độ WASD làm sau | Thủ ải ít cần chạy liên tục. Hai tay ở bàn phím là tốt nhất cho học |
| §1.4 | Hợp đồng hành động: một từ chốt một hành động có ID; partial ASR không cast; kết quả muộn bị bỏ | **Giữ nguyên, làm từ M0** | Là nền để thêm Voice sau mà không phải sửa sim |
| §1.9, §9.2 | 4–6 ô; luôn có ô liên tục và ô tự cứu | **Giữ.** MVP dùng 5 ô, ô thứ 6 mở ở cảnh giới 2 | Tính tải ở mục 4.3: người 25 WPM đã kín giờ với 4 ô có hồi |
| §16.1, §23.2 | T_gõ = 12 × ký tự / WPM; cửa sổ phản ứng gồm đọc + phần dở + từ đáp + đệm | **Giữ**, thêm +1,0 s cho Voice (thử) | Công thức đúng, đã khớp bảng 6,80 s ở 25 WPM |
| §17.1 | Tách 5 tiến trình: tu vi, tư chất, ngộ tính, thành thạo, mức thuộc tiếng Anh | **Giữ, coi là luật cứng** | Không để chỉ số RPG giả làm bằng chứng học |
| §18 | Tu luyện chọn chữ Minh / thường / Tâm ma: deadline, không dừng giờ, luật tiền tố, giữ từ quá hạn, chấm tách | **Giữ khung, sửa tiêu chí chọn** (mục 4.5) | Bản Codex chọn theo nhãn màu, nên giá trị học chỉ là gõ chép. Thêm tiêu chí theo nghĩa và bậc nhớ thật |
| §18.3 | 3–4 điểm đọc cố định, không rải chữ bay chồng | **Giữ** | Khác hẳn cầu bay tự do của QCBH, đúng cho đọc chữ |
| §19 | Sáu hoạt động tu luyện khác | **Bỏ khỏi MVP**, chỉ giữ Tĩnh Tu và Tham Ngộ | Chính Codex §19.2 cảnh báo thành danh sách việc. Mỗi hoạt động là thêm một UI và bộ âm |
| §21.1 | Tu vi không tự nâng mức thuộc từ | **Giữ**, mở rộng: tu vi cũng không nâng cấp từ | Khó lên bằng nhiều trục, không ép gõ nhanh hơn (BALANCE §1.7) |
| §22 | Chi phí từ theo độ dài, preset tách ngôn ngữ và RPG, bot không tạo học | **Giữ**, thêm: mỗi người trong đội có bộ từ riêng | Mục 5 |
| §26.1 | Hình 2D/sprite, không mặc định runtime 3D cho đông quái | **Sửa cách làm, giữ vẻ ngoài** (mục 4.7) | Repo có sẵn Three.js, đám đông instanced (Tuyến Cuối `flood(700)` p95 1,4–1,5 ms), quy trình Tripo/Blender. Không có họa sĩ hoạt hình 2D. Ảnh AI không giữ nhất quán 8 hướng × nhiều khung |
| §26.2–26.4 | Lớp nền, bóng tiếp đất, foreground giảm alpha, HUD tách camera | **Giữ**, thực hiện bằng 3D cố định góc | Nguyên tắc đúng, không phụ thuộc kỹ thuật |
| §26.5–26.6 | Ngữ pháp VFX theo hệ; 7 bước một kỹ năng | **Giữ, bổ sung** màu dành riêng, "chữ thành chiêu", họ âm từng hệ | Mục 4.8 |
| §26.7–26.8 | Ngân sách 2D, đích 60 FPS, test 50/100/200/300 quái | **Sửa số** theo số đo và ngân sách của repo (≤ 8 ms trung bình, p95 ≤ 12 ms ở High) | Repo đã có bậc Low–Ultra và bench |
| §26.9 | Đội đông: VFX đồng đội gọn | **Giữ**, ghi thành hệ số theo bậc (mục 5) | |
| §26.10 | Âm thanh: 3 câu | **Sửa, mở rộng** theo Q6 và hệ bus của Rồng Giữ Ải | Quá mỏng so với luật âm của chủ dự án |
| §27 | Lộ trình P0–P7, Voice ở P2 | **Sửa thứ tự:** lát solo + bot trước, Voice sau Tĩnh Tu, co-op người thật sau nữa | Voice còn phụ thuộc bộ giải mã chưa có |
| §11 | 24 trường phái | **Bỏ khỏi MVP**, chỉ 2 | Mỗi trường phái ≈ 6 chiêu × (VFX + 2–3 âm + icon): cỡ M sản xuất |

## 4. Đề xuất cho game thủ ải thú triều

### 4.1 Luật trình bày chữ

1. **Bàn Ấn** là dải DOM ở giữa đáy màn hình, nằm ngoài canvas: không rung, không hậu kỳ, không bị số sát thương đè (theo luật khung học của Rồng Giữ Ải 05 §4.4).
2. Mỗi ô có từ 28–32 px (Be Vietnam Pro 700), chữ đầu gạch chân, vòng hồi quanh ô, icon chiêu nhỏ. Tên chiêu tách khỏi từ (Codex §1.4).
3. Nghĩa và IPA hiện theo **số lần nhớ đúng**, không theo độ thuộc thô (Rồng Giữ Ải 01 §6.3). Dòng IPA dùng font có đủ glyph IPA (Noto Sans hoặc Charis SIL).
4. Khi ô đang hồi, từ kế tiếp hiện mờ 50 %. Người chơi đọc trước được, nên thời gian nhận từ giảm. Ô hồi xong không tự giành phím đang gõ.
5. Mỗi từ sống có chữ đầu riêng, dùng `Letters` của kit (bậc 1, bậc 2 khi thiếu chữ). Gõ chữ đầu là khóa mềm vào ô đó.
6. Trên chiến trường chỉ có **Ấn chữ**: tối đa 2 cùng lúc, đặt trên tinh anh hoặc Thú vương (phá giáp, ngắt niệm). Quái thường không mang chữ.
7. Trần chữ sống: MVP ≤ 8 (5 ô + 2 Ấn chữ + 1 Từ Khẩn). Sau MVP ≤ 10 (thêm ô 6 và lệnh pet). Vẫn dưới trần 16 của `typing/budget.ts`.

### 4.2 Dữ liệu bài học của một ải

```jsonc
// content/data/lessons/pass-01.json (thử)
{ "passId": "p01-han-coc", "topics": ["nature.animals", "nature.weather"], "levelBand": "profile",
  "newMax": 6, "mix": { "new": 0.12, "due": 0.35, "learning": 0.30, "known": 0.23 },
  "slots": { "flow": "known|learning:3-5", "skillA": "learning|due:4-6", "skillB": "due|learning:4-7",
             "guard": "known:3-5", "ultimate": "due:5-8" },
  "seals": "due|weak:4-7", "urgent": "known:3-5", "filter": ["sensitive", "mature?child"] }
```

- Bộ từ của ải: 70–100 từ, dựng lúc nạp ải qua `typing-game:learning:v1:query`/`lookup` (Rồng Giữ Ải 01 §6.1). Không lặp từ tới khi dùng hết nhóm (`WordPicker`, RNG theo seed).
- `levelBand: "profile"`: cấp từ theo hồ sơ (yếu tố 6 của BALANCE), không theo cảnh giới.
- `shared/vocabulary/topics` có 101 chủ đề (15 nhóm, 835 từ khác nhau). Đủ cho MVP và cho đạo đề của Tĩnh Tu. Khi chủ đề không phủ cấp của người học, bài lấy một lát của danh sách cấp (180 từ mỗi cấp ở các cấp cao).
- Lọc `sensitive` luôn bật. Hồ sơ trẻ em lọc thêm `mature`. Chủ đề thú triều dễ kéo theo từ bạo lực, nên kiểm danh sách chặn (`vocab/content-filter.ts`).

### 4.3 Tải gõ và mật độ quyết định (số thử)

Deck MVP: ô liên tục (không hồi) · Chiêu A hồi 6 s · Chiêu B hồi 10 s · Hộ thân hồi 20 s · Thần thông nạp ~45 s. Nếu dùng mọi ô ngay khi hồi xong thì có tối đa 10 + 6 + 3 + 1,3 ≈ **20 lần cast mỗi phút**.

| Người chơi (từ 5 ký tự) | Giây mỗi từ (nhận + gõ) | Từ mỗi phút | Còn cho ô liên tục | Hệ quả |
|---|---|---|---|---|
| 25 WPM | 0,6 + 2,4 = 3,0 | 20 | ~0 | Kín giờ. Phải thắng được khi đứng trận, có tự ngắm. Nhịp đợt giãn bằng `k` của BALANCE |
| 35 WPM (tham chiếu) | 0,5 + 1,7 = 2,2 | 27 | ~7 | Có một chút thời gian để đi lại hoặc chọn góc |
| 60 WPM | 0,4 + 1,0 = 1,4 | 43 | ~23 | Ô liên tục hút phần dư. Cần trần sức ô liên tục (thử: ≤ 30 % sức gõ) và `k` nén |

- **Thời gian hồi là trần công bằng.** Sức của chiêu không tăng theo tốc độ gõ. Phần dư đi vào ô liên tục, có trần (Codex §22.1).
- Một quyết định cast mỗi 2–3 s. Đây là mật độ đủ căng mà người 25 WPM vẫn theo được.
- Cửa sổ Từ Khẩn (hộ thân trước đòn lớn): ≥ đọc 1 s + phần từ dở + từ đáp + đệm 1 s. Với từ đáp 4 ký tự và 4 ký tự dở ở 25 WPM: 12 × 8 / 25 + 2 = **5,8 s**. Voice thêm 1,0 s. Bot BALANCE kiểm tỉ lệ đỡ kịp.

### 4.4 Cảnh giới mở dạng tác vụ học, không nâng cấp từ

| Cảnh giới (số thứ tự, tên do mảng khác đặt) | Tác vụ học được mở | Ghi chú |
|---|---|---|
| 1 | Từ đơn trên Bàn Ấn; nghĩa hiện cho từ chưa nhớ; Học trước; Sổ Từ | Một trường phái, 5 ô |
| 2 | Ấn chữ trên tinh anh; Thẻ Ôn chọn nghĩa (phím 1/2/3) khi Điều tức; ô thứ 6 | |
| 3 | Tĩnh Tu bậc Tham Ngộ (chọn theo nghĩa); Từ Hỏi Nghĩa trên Ấn chữ boss | Chỉ với từ đã gặp |
| 4 | Ấn Nghe (nghe rồi gõ) trên boss; cụm từ 2 chữ cho thần thông | Cần phụ đề âm khi tắt tiếng |
| 5+ | Chú ngữ: câu ngắn 3–5 từ (entity `sentence`) cho hợp trận, nạp bất đồng bộ | Chỉ khi cấp từ ≥ A2; đội mỗi người một câu riêng |

### 4.5 Tĩnh Tu: bản sửa của Codex §18

Giữ từ Codex: 3–4 điểm đọc cố định quanh bóng thiền; 3 loại chữ; đồng hồ không dừng khi gõ; từ quá hạn giữ ở vùng nhập; luật tiền tố; chấm tách gõ, chọn lọc, đúng hạn; preset ở §18.5; phiên 60–90 s.

**Đạo đề.** Mỗi phiên gắn với một công pháp, và công pháp gắn với một nhóm từ (ví dụ một công pháp lôi gắn chủ đề `nature.weather`). Minh và chữ thường lấy từ nhóm của bài. Tâm ma lấy từ một *nhóm chủ đề khác xa* (khác nhóm trong 15 nhóm), và bỏ các từ đa nghĩa có danh sách loại riêng. Như vậy Tâm ma vẫn là tiếng Anh đúng; người chơi tránh nó vì nó lạc đề (đúng Codex §18.2, §25.3).

| Bậc | Dùng cho từ | Minh hiện | Tâm ma nhận biết bằng | Việc học thật | `activityType` |
|---|---|---|---|---|---|
| Nhập Môn | Mới (≤ 6 mỗi phiên) | Từ + IPA + nghĩa, phát âm khi mảnh vào điểm đọc | Viền khói mực, icon mắt nứt, luôn có nhãn | Tiếp xúc, gõ chép, nghe | `review-card` |
| Tham Ngộ | Đang học | Từ; nghĩa ẩn sau 1,5 s | 2/3 có nhãn; 1/3 không nhãn, phải nhận theo nghĩa | Hiểu nghĩa Anh → Việt | `meaning-recall` (chỉ với mảnh không nhãn) |
| Ngộ Đạo | Đã nhớ ≥ 1 lần | Chỉ nghĩa Việt + chữ đầu + số ô | Nghĩa Việt lạc đạo đề | Nhớ từ Việt → Anh | `meaning-recall` |

- Deadline lấy từ §18.5. Bậc Ngộ Đạo cộng 1,5 s (thử) cho thời gian nhớ.
- Gõ Tâm ma *có nhãn* chỉ tính là lỗi chọn lọc, không ghi sự kiện học sai. Gõ Tâm ma *không nhãn* ghi `meaning-recall` sai cho từ đó.
- **Giá trị học:** bản QCBH là phản xạ chuột. Bản Codex là gõ chép + chọn theo nhãn. Bản này thêm phân loại theo nghĩa và nhớ thật, và là **nơi duy nhất đưa từ mới vào** ngoài trận, không có áp lực máu.
- Phần thưởng RPG: tiến độ công pháp có trần mỗi ngày. Dòng 1–3 của công pháp mở bằng luyện trong trận (số lần cast hợp lệ). Dòng 4–6 cần thêm ≥ 60 % từ của bài đạt "đã nhớ" (≥ 2 lần nhớ đúng, đọc từ `recentSamples`). Phần sức đến từ cửa học có trần (thử ≤ 10 % sức của trường phái), để người học chậm không bị bỏ lại.
- Hình riêng, không giống QCBH: không dùng cầu tròn có chữ "悟/魔". Ta dùng **lá phù giấy dó** bay vào 3–4 điểm đọc trên mặt nước tĩnh. Minh: viền trắng ngà, tia sáng, icon mặt trời. Chữ thường: giấy trơn. Tâm ma: khói mực tím than, icon mắt nứt. Không phân loại chỉ bằng màu.

### 4.6 Vòng một ải

```text
Chuẩn Bị: xem triều, chọn công pháp, Học trước (Tĩnh Tu Nhập Môn 30–45 s, tùy chọn, ≤ 6 từ mới)
→ Bày trận 20 s (chọn trận vị, ô trên Bàn Ấn hiện từ đầu)
→ [ Báo triều 5 s → Đợt 45–70 s → Điều tức 15–20 s (Thẻ Ôn 1–3 câu, đổi ô) ] × 6
→ Lặng 8 s → Thú vương (Ấn chữ, Từ Khẩn) → Kết ải: Sổ Từ Ải, Ôn trận 60 s (tùy chọn)
```

- Nếu bỏ Học trước: từ mới chỉ lên **Chiêu B** ở đợt 1–2 (tải thấp), có nghĩa hiện và Chiêu B không bao giờ là đáp án Từ Khẩn.
- Mỗi từ gửi một sự kiện có chấm mỗi ải (luật D14 của Rồng Giữ Ải). `meaning-recall`, `listening`, `review-card` luôn gửi.

### 4.7 Hướng hình: ba phương án và đề xuất

| | A. Nhìn 2D, chạy Three.js 3D (**đề xuất**) | B. Sprite nướng từ GLB (dự phòng) | C. Sprite vẽ tay, Spine (loại) |
|---|---|---|---|
| Nguồn asset | GLB Tripo/Meshy, rig + clip trong Blender | Cùng GLB, Blender render 5–8 hướng × clip ra atlas | Họa sĩ vẽ từng khung hoặc rig 2D |
| Chuyển động | Trộn clip, quay hướng mượt | Khung rời 10–15 fps, đổi hướng bị giật | Phụ thuộc họa sĩ |
| Mã có sẵn | `dragon-hold/src/view/{crowd,fx,telegraphs,terrain}.ts`, kit `three`, `feedback` | `scripts/models/blender/bake_impostor.py` (16 hướng) + quad instanced | Không có |
| Bộ nhớ | Texture xương ~0,3 MB mỗi loại | Atlas 2048² (RGBA8 16 MiB) mỗi loại quái; anh hùng gấp 2–4 lần | Như B |
| Rủi ro | Đám đông có xương chưa đo (crowd.ts mới có gait thủ tục; khe `bones`, `vat` để trống) | Chuyển động cứng, chủ dự án đã chê chuyển động cứng | AI không làm được; tốn tiền thuê |

Chi tiết của A:
- **Camera** 3/4 cố định: nghiêng 50–55°, FOV 25–30° (gần trực giao), zoom 0,8–1,2. **Không xoay**, khác Rồng Giữ Ải. Nhờ vậy phông, cỏ, mây được vẽ 2D quay về camera mà không lộ tấm.
- **Shader thủy mặc:** ramp 2–3 bậc, viền mực bằng vỏ lật 1,5–2 px cho người và boss, hạt giấy phủ màn hình rẻ, sương theo bán kính, `NeutralToneMapping`. Lọc Kuwahara chỉ ở Ultra, chỉ khi ≤ 1,5 ms (art-pipeline §4).
- **Lớp:** phông xa 3 lớp tranh Codex → đất nướng từ ô 2D → decal mực → bóng tiếp đất → sinh vật GLB → VFX sprite/ribbon → foreground thưa (giảm alpha khi che) → DOM (Bàn Ấn, HUD).
- **Cỡ ở 1080p:** người chơi 90–110 px; quái bầy ≥ 28 px, quái vừa 36–48 px, quái lớn 50–70 px; tinh anh ×1,3; Thú vương 180–260 px. Đo bằng kịch bản kiểu `dh-scale`.
- **Cổng duyệt:** cuối M0a dựng cùng một cảnh bằng A và B. Chụp ảnh tĩnh và đoạn chuyển động 10 s. Chủ dự án chọn. Hai phương án dùng chung GLB, nên đổi hướng không mất asset.

**Bản sắc (đề xuất, chờ duyệt):** "sơn thủy huyền ảo" mang chất Việt. Ải là hẻm núi đá vôi dựng đứng, sương chàm. Bảng màu: mực đen và xám giấy dó, lục rêu, chàm; điểm sáng linh quang trắng ngà. Đỏ son sơn mài chỉ dùng cho dấu triện ở UI. Phe địch là linh thú nhiễm **trọc khí** (mực chàm đen, mắt hổ phách). Trúng đòn thì tà khí tan thành khói mực. **Không có máu.** QCBH dùng nổ máu đỏ [video t160], nhưng máu không hợp game học cho trẻ em và tranh với màu đỏ báo nguy.

### 4.8 Ngữ pháp VFX theo hệ (MVP: Kiếm, Hỏa)

Màu ngữ nghĩa chung của kit không được dùng sai: đỏ `#FF4A4A` chỉ cho nguy hiểm từ địch; cam `#FFB020` cho khẩn; vàng kim `#FFC83A` cho tiền và đồ rơi; xanh ngọc `#7FF5E0` cho sức gõ.

| Hệ | Hình, nhịp | Màu | Lớp mực | Va chạm | Họ âm (Q6) | Hạt High |
|---|---|---|---|---|---|---|
| **Kiếm** | Phi kiếm thẳng, cung sạch, kiếm trận xoay elip quanh người, thu kiếm về sau lưng | Bạc trắng, lõi lam nhạt | Vệt mảnh như nét bút lông, nhọn ở đuôi | Lóe chữ thập nhỏ, vết cắt mực trên đất, quái khựng | Ngân kim loại khi rút → xé gió → whoosh Doppler → cắt và ngân → vang hẻm 0,5–0,8 s | 400 |
| **Hỏa** | Tụ lõi trắng vàng → cuộn lửa → bùng theo đợt, tàn bay; vùng cháy | Cam đào → vàng; không dùng đỏ thuần | Khói mực đen cuộn sau lửa | Nổ có nhịp, đẩy lùi, decal cháy mực 6 s | Hút lửa → bắt lửa áp lực, gầm lửa → whoosh dày đi xa → nổ có thân, than lách tách, vang 0,8–1,2 s | 600 |
| Hộ trận chung | Vòng phù văn quanh trận đài; sáng khi được nạp | Ngà; luồng nạp xanh ngọc | Phù văn vẽ bằng nét mực | Khiên gợn khi đỡ, nứt khi < 30 % | Ngân đồng trầm (không chuông chùa), nứt đá | 150 |
| Quái trọc khí | Dáng thú, mắt hổ phách, khói mực rỉ | Chàm đen, hổ phách | Khói mực | Tan khói khi chết, cụm chết thành một vụ √N | Theo lớp: bầy, xung kích, bay, bắn xa, giáp | 300 |
| Báo đòn địch | Vạch đỏ đầy dần trên đất, có sọc và icon | Đỏ `#FF4A4A` | — | — | Rít báo ngắn, ưu tiên P1 | — |
| Sau MVP: Băng, Lôi, Mộc, Thổ, Phù | Theo Codex §26.5 | Không trùng 4 màu ngữ nghĩa | Mỗi hệ một kiểu nét riêng | | Mỗi hệ một họ âm | |

- **Chữ thành chiêu:** khi chốt từ, chữ trên Bàn Ấn bật lên thành nét thư pháp xanh ngọc, bay vào tay nhân vật trong 0,15 s, rồi chiêu phát. Từ gắn với hành động mà không che vùng chữ.
- Mỗi chiêu theo 7 bước của Codex §26.6, đi qua bậc phản hồi T0–T5 của `kit/feedback` (thêm hồ sơ `tutien`). Dừng hình không nuốt phím.

### 4.9 Âm thanh

- **Bus:** music · ambience · world · enemies · self · allies (đồng đội + bot) · formation · typing · pronunciation · ui · warnings · dialogue → limiter (theo `dragon-hold/src/audio/{mixer,limiter}.ts`).
- **Ưu tiên:** P0 phát âm từ của mình → P1 báo đòn, hộ trận < 30 % → P2 phím → P3 chiêu của mình → P4 chiêu đồng đội, va chạm → P5 bầy, môi trường. Tối đa 32 tiếng cùng lúc (Low 16). Một tiếng ≤ 4 lần mỗi 100 ms.
- **Bầy:** một lớp nền "triều" (vó, gầm gừ lẫn, đá lăn) chia 3 tầng xa/gần/sát trận. Độ to và tầng theo số quái sống. Tiếng chết gộp thành chuỗi "tan khói" đi lên, kiểu Vampire Survivors (AUDIO_PIPELINE §8.5).
- **Luật giọng đọc** (AUDIO_PIPELINE §6.2): năng lượng 1–4 kHz tắt nhanh. Đuôi vang nằm dưới 1 kHz hoặc trên 4 kHz. Âm xong từ là âm nhường, có đuôi thấp để lặp 20 lần không mệt. Đòn lớn (thần thông, Thú vương) có đuôi dài rõ.
- **Nhạc 4 lớp cùng BPM:** Tĩnh (đàn tranh, sáo trúc, pad) → Thủ (trống, cello ostinato) → Triều dâng (trống lớn, dây nhanh, tù và) → Thú vương (bản riêng, mỗi pha một stem). Tĩnh Tu có nền riêng, không nhịp ép. Không chuông chùa, không tụng. Nếu chọn chất Việt thì tránh nhạc cụ Trung, Nhật dán nhãn Việt (AUDIO_PIPELINE §8.2).
- **Nguồn:** bản thu CC0 (Freesound, đọc giấy phép từng trang) và audio-lab Stable Audio 3 (chỉ tạo được trên Mac). Mọi âm qua Bảng Nghe mù của chủ dự án. Âm tổng hợp tạm phải ghi rõ là tạm.

### 4.10 Ngân sách hiệu năng (số thử, đo lại ở bench)

| Mục | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Quái sống (luật sim, mọi bậc) | ≤ 300 | ≤ 300 | ≤ 300 | ≤ 300 |
| Quái vẽ đầy đủ (phần thừa dùng impostor) | 100 | 160 | 300 | 300 |
| `SkinnedMesh` (người chơi, bot, Thú vương) | 4 | 6 | 8 | 10 |
| Hệ số VFX đồng đội | 0,4 | 0,6 | 0,6 | 1,0 |
| Hạt / số sát thương sống | 600 / 50 | 1.500 / 100 | 3.000 / 160 | 4.500 / 200 |
| Draw call | ≤ 80 | ≤ 110 | ≤ 150 | ≤ 190 |
| Khung | ≤ 16 ms | ≤ 12 ms | TB ≤ 8, p95 ≤ 12 ms | như High |

- Phím tới đòn ≤ 50 ms. Bàn Ấn cập nhật ≤ 0,3 ms mỗi khung. Bậc máy chỉ đổi cách vẽ, không đổi luật (Rồng Giữ Ải D10).
- **Bench là việc đầu tiên của M0a:** 300 quái GLB thật, 5 loại, chế độ `bones`, 3 người cùng tung chiêu lớn. Không đạt ở Low thì dùng phương án B cho quái thường, hoặc hạ trần quái sống của luật rồi chạy lại bot.

### 4.11 MVP và sau MVP

| Hạng mục | Lát chơi đầu (M0) | MVP (thêm M1) | Sau MVP |
|---|---|---|---|
| Ải, triều | 1 hẻm ải, 2 cửa tràn + 1 đường bay; 6 đợt + Thú vương, 7–9 phút | 3 ải | Chuỗi ải, biến thể triều |
| Trường phái | Kiếm, Hỏa (5 ô mỗi bên) | + ô 6 | Băng, Lôi, Mộc, Trận, Ngự thú… |
| Hình thức | Solo; solo + 1 bot | như M0 | Co-op online 2–3; Thất Tinh 7 |
| Đầu vào | Typing, click-to-move, mũi tên | + WASD có trạng thái | Voice, Hybrid |
| Học | Bàn Ấn, Ấn chữ, Từ Khẩn, Học trước dạng thẻ, Thẻ Ôn, Sổ Từ, sự kiện học | Tĩnh Tu Nhập Môn + Tham Ngộ; công pháp gắn bài | Ngộ Đạo, Ấn Nghe, chú ngữ |
| Hình | Phương án A + bench + A/B; ~13 GLB, ~100 ảnh | + 2 ải, 3 quái | Theo trường phái |
| Âm | ~55 id, 3 bản nhạc | + Tĩnh Tu, Thẻ Ôn | Theo trường phái |
| Không làm | Pet, cửa hàng sâu, trang bị dòng phụ, đan dược nhiều loại, bản đồ thế giới | | Theo mảng khác |

## 5. Solo và đội: khác biệt và luật công bằng (mảng này)

| Mục | Solo | Solo + bot | Đội 2–3 người (+ bot bù) | Thất Tinh 7 (mở rộng) |
|---|---|---|---|---|
| Từ | Riêng theo hồ sơ | Bot không có chữ hiện; dải bot chỉ có icon và vòng hồi | **Mỗi người một bộ từ riêng.** Không thấy từ của nhau, không giành từ | Như đội |
| Màn hình | Bàn Ấn 5–6 ô | + dải bot | + dải đồng đội (icon, vai, hồi, máu) | Dải nén 6 người, chỉ trạng thái và cảnh báo |
| Hợp trận | Trận nhỏ tự nạp | Bot nạp theo vai | Mỗi người nạp bằng từ của mình, bất đồng bộ (Codex §14.4) | Nạp theo pha, mỗi nhãn một người |
| Phát âm | Từ của mình | Như solo | Chỉ từ của mình, trên máy mình | Như đội |
| Tạm dừng | Được, che Bàn Ấn khi dừng | Được | Không. Thẻ Ôn khi Điều tức không dừng giờ | Không |
| VFX, âm đồng đội | — | Bot ×0,6, −6 dB | ×0,6 (Low ×0,4), −6 dB, đuôi ngắn | ×0,3 + chỉ chiêu lớn, −9 dB, gộp |
| Sự kiện học | Của mình | Bot không tạo | Mỗi người gửi về hồ sơ mình | Như đội |

Luật công bằng:
- Preset ngôn ngữ chốt riêng từng người trước trận. Sức một từ quy đổi theo chi phí ký tự (Codex §22.1), nên người học từ khó không thiệt.
- Thời gian hồi là trần chung. Ô liên tục có trần. Người 60 WPM không "gánh" hết phần của người 25 WPM. Triều của đội đặt theo tổng sức gõ quy đổi (nhịp `k` của BALANCE cho cả đội; mảng cân bằng chốt công thức).
- Bảng xếp hạng tách solo, đội có bot, đội người, theo kênh (Typing/Voice) và preset.
- Hồ sơ trẻ em trong đội công khai: MVP không có chat chữ, chỉ có ping và câu soạn sẵn.

## 6. Gắn với học tiếng Anh (Typing, Voice, Hybrid)

### 6.1 Từ nào, lúc nào

| Lúc | Tác vụ | Nhóm từ, độ dài | Nghĩa, IPA | Phát âm | `activityType` |
|---|---|---|---|---|---|
| Học trước, Tĩnh Tu Nhập Môn | Gõ chép có nghĩa | Mới, ≤ 6 | Luôn hiện | Có | `review-card` |
| Ô liên tục | Gõ nhanh lặp | Đã thuộc + đang học, 3–5 ký tự, xoay vòng 20–30 từ | Theo số lần nhớ | Không | `typing-skill` |
| Chiêu A, B | Gõ để tung chiêu | Đang học, đến hạn; 4–7 ký tự | Theo số lần nhớ | Từ < 40 độ thuộc, sau khi cast | `typing-skill` |
| Hộ thân, Từ Khẩn | Phản ứng | Đã thuộc, 3–5 ký tự | Không cần | Không | `typing-skill` |
| Thần thông | Gõ sau pha nạp dài | Đến hạn, yếu; 5–8 ký tự; cụm 2 chữ từ cảnh giới 4 | Theo số lần nhớ | Có | `typing-skill` |
| Ấn chữ tinh anh, boss | Phá giáp, ngắt | Đến hạn, yếu; Hỏi Nghĩa từ cảnh giới 3; Nghe từ cảnh giới 4 | Theo luật Hỏi Nghĩa | Ấn Nghe phát khi hiện | `typing-elite`, `typing-boss`, `meaning-recall`, `listening` |
| Điều tức | Thẻ Ôn 1–3 câu | Từ gõ ẩu, từ có gợi ý, từ mới | Sau khi trả lời | Có | `meaning-recall`, `review-card` |
| Kết ải | Sổ Từ, Ôn trận | Từ đã gặp, từ sai | Có | Bấm để nghe | `review-card` |
| Tĩnh Tu Tham Ngộ, Ngộ Đạo | Chọn theo nghĩa, nhớ | Đang học, đã nhớ | Bảng 4.5 | Bậc Nhập Môn | `meaning-recall` |

### 6.2 Tránh quá tải trong triều dày

- Số quái không làm tăng số chữ: chữ chỉ ở Bàn Ấn và Ấn chữ (mục 4.1).
- Từ mới không xuất hiện trên ô hộ thân, Từ Khẩn, Ấn chữ, và không vào đợt có tải > 1,0.
- Mỗi lúc chỉ một loại chữ mới được dạy (một ý mới mỗi ải, như lịch dạy của Rồng Giữ Ải 04 §6).
- Tối đa 1 Từ Khẩn cùng lúc. Trong đội, không giao hai đáp án bắt buộc cho một người cùng lúc (Codex §16.1).
- Dòng nghĩa trên màn ≤ 3. Đồ thường tự hút, không có nhãn chữ trên đất.
- Số đo: Ngộp O ≤ 8 % ở chế độ Cân bằng (BALANCE §3). Thời gian nhận từ mới > 1,5 s thì giảm tỉ lệ từ mới ở ải sau.
- Cổng học riêng (giống B8): từ mới không lên độ thuộc ≥ 70 trong ải đầu gặp nó; ≥ 90 % sự kiện học đúng luật; không lượt nào có từ mới trên ô gấp.

### 6.3 Voice và Hybrid

- **Trạng thái thật:** `shared/voice/README.md` ghi bộ giải mã chạy thật chưa có, chưa có bộ chọn Voice. Ngữ pháp dự kiến là Vosk + `[unk]`. Vì vậy MVP chỉ có Typing.
- Ngữ pháp nhận dạng chỉ gồm các từ đang sống trên Bàn Ấn và Ấn chữ (≤ 8–10 từ). Ngữ pháp nhỏ thì nhận đúng hơn. Ngữ pháp đổi khi từ đổi, ở biên hành động.
- Giữ nguyên luật Codex §1.4: kết quả tạm không cast; kết quả muộn không bắn vào ô đã đổi từ; hai kênh cùng xong chỉ chốt một lần; nhận sai không trừ độ chính xác gõ.
- Khi máy đang phát âm (TTS) thì khóa nhận giọng nói (đã có rào thế hệ TTS trong `host.mjs`). Khuyên đeo tai nghe. Chỉ nhận mic của chính người chơi.
- Cửa sổ phản ứng của Voice cộng 1,0 s (thử, đo độ trễ thật). Voice và Typing có cùng hồi chiêu, cùng sức. Không xếp chung bảng tốc độ.
- Tĩnh Tu bằng Voice là profile riêng (thời hạn dài hơn, không phạt Tâm ma theo kết quả chưa chắc), làm sau cùng.
- Hybrid: mỗi từ có một kênh sở hữu từ phím hoặc tiếng đầu tiên. Không ghép nửa gõ nửa nói.

## 7. Tái sử dụng và chi phí sản xuất

### 7.1 Mã và tài liệu dùng lại

| Cần | Có sẵn | Đường dẫn | Việc | Cỡ |
|---|---|---|---|---|
| Khóa chữ đầu, ngân sách chữ, chấm từ, phiên gõ | Kit `typing` | `shared/game-kit/typing/{letters,budget,router,session,scorer}.ts` | Dùng nguyên; thêm nguồn "ô" vào `BudgetLedger` | S |
| Nạp từ, cấp, chủ đề, lọc | Kit `vocab` + dữ liệu | `shared/game-kit/vocab/*`, `shared/vocabulary/{levels,topics}` | Thêm bộ dựng bài theo công pháp và đạo đề | S |
| Sự kiện học, bridge portal | Kit `learning` | `shared/game-kit/learning/{events,bridge}.ts` | Dùng; đăng ký `gameId` mới trong `portal/public/games.json` | S |
| Phát âm | Kit `speech` | `shared/game-kit/speech/speech.ts` | Dùng | S |
| Luật học trong trận | Tài liệu Rồng Giữ Ải | `docs/games/dragon-lane/01-core-combat-learning.md` §6 | Chép luật, đổi "quái" thành "ô" | S |
| Hồ sơ năng lực, FlowMeter, bộ điều nhịp, bot gõ giống người | Kit `balance` | `shared/game-kit/balance/{profile,flow,director,typist,gates}.ts` | Dùng; bot đồng minh dùng `typist` | M |
| Phản hồi T0–T5 | Kit `feedback` | `shared/game-kit/feedback/*` | Thêm hồ sơ `tutien` | S |
| Khung học, HUD | Rồng Giữ Ải | `games/dragon-hold/src/ui/{learning-frame,hud,tags}.ts` | Chép, đổi thành Bàn Ấn | M |
| Đám đông, VFX, báo đòn, đất, bench | Rồng Giữ Ải | `games/dragon-hold/src/view/{crowd,fx,telegraphs,terrain,bench}.ts` | Chép; làm khe `bones` trước. Khi 2 game cùng dùng thì đưa vào kit `three` | M |
| Sim tất định, đợt, spawn, trạng thái | Rồng Giữ Ải, Tuyến Cuối | `games/dragon-hold/src/sim/{world,waves,spawn,director,status}.ts`, `games/typing-survival/src/sim/{move,projectiles,spawn}.ts` | Chép một phần; di chuyển tự do là mới | L |
| Bộ trộn âm, limiter, catalog | Rồng Giữ Ải + kit | `games/dragon-hold/src/audio/{mixer,limiter,catalog,bank}.ts`, `shared/game-kit/audio` | Chép, thêm bus `allies`, `formation` | M |
| Model: chuẩn bị, rig, clip, impostor | Space | `games/space-typing/scripts/models/prepare-models.ts`, `scripts/models/blender/{space_typing_model_tools,bake_impostor}.py`, `docs/games/MEDIA_AND_MODELS.md` | Dùng; thêm shader thủy mặc | S |
| Âm: tạo, chấm, giấy phép | Audio-lab | `tools/audio-lab`, `docs/games/AUDIO_PIPELINE.md`, `DECISIONS.md` Q6 | Dùng; cần giờ của chủ dự án | M |
| Voice | Nền voice | `shared/voice/*`, `games/space-typing/src/input/{mode,voice-session}.ts` | Chờ bộ giải mã | L (sau) |

### 7.2 Danh sách asset lát chơi đầu (ước lượng)

| Nhóm | Số | Ghi chú |
|---|---|---|
| Nhân vật chính (Tripo/Meshy, rig biped) | 2 (Kiếm tu, Hỏa tu) | Clip: Idle, Run, Cast_Short, Cast_Heavy, Hit, Down, Victory (+ Throw cho Kiếm). Bot dùng model của trường phái còn lại, đổi màu áo |
| Linh thú thường | 5 (bầy nhỏ 4 chân, bầy sói, xung kích, bay, bắn xa) | 4 clip mỗi con: Idle, Move, Attack, Death. Tinh anh = scale 1,3 + vật liệu + hào quang, không model mới |
| Thú vương | 1 | 8–10 clip, `SkinnedMesh` |
| Prop lớn Tripo (không rig) | 5 (cổng ải, trận đài, 2 đá vôi, tùng cổ) | |
| Ảnh Codex | ~100 | 26 ảnh nguồn cho GLB (2 góc); 6 ô đất; 8 decal; 3 phông; 6 cỏ bụi; ~16 texture VFX; ~24 icon; ~8 khung UI; ~5 Tĩnh Tu |
| Âm | ~55 id | Phím 4; Kiếm 8; Hỏa 8; quái theo lớp 14; Thú vương 6; triều 2; hộ trận 4; UI 4; Tĩnh Tu 5 |
| Nhạc | 3 | Thủ trận 4 lớp; Thú vương; nền Tĩnh Tu |

Tổng **~13 GLB** (Rồng Giữ Ải M0: ~24). Tripo khoảng 75 credit mỗi sinh vật theo giá API (dragon-lane DESIGN §7.2): ~1.000 credit. Chủ dự án mất ~13–20 giờ tạo, rig, chọn clip; ~2–3 giờ Bảng Nghe; ~2 giờ chơi thử mỗi mốc.

### 7.3 Mốc và thời gian (giả định 4–6 làn agent song song, chủ dự án 6–8 giờ Tripo mỗi tuần)

| Mốc | Nội dung | Cổng | Lịch | Cỡ |
|---|---|---|---|---|
| **M0a Hộp xám** | Bench đám đông `bones` trước; sim tất định 60 Hz; di chuyển tự do + click; đánh nền; 2 kit × 5 ô qua kit `typing`; triều 6 đợt; hộ trận; bot đồng minh; Bàn Ấn DOM; sự kiện học; bot cân bằng 25/35/60 | Golden hash; B1–B9; chữ không chồng, không bị che; 0 lỗi console | 2–3 tuần | L |
| **M0b Hình** | 3 model mẫu duyệt trước (1 người, 1 quái, Thú vương); A/B hình; rồi phần còn lại; shader thủy mặc; ảnh Codex | Chủ dự án duyệt chuyển động và ảnh A/B; đạt cỡ px | 3–4 tuần (bị giới hạn bởi giờ Tripo) | L |
| **M0c Âm, VFX, đánh bóng** | Lô âm ~55 id qua Bảng Nghe; VFX Kiếm, Hỏa; nhạc 4 lớp | Bài nghe trong trận; ngân sách khung | 2 tuần, chồng với M0b | M |
| **M1 Tĩnh Tu + meta** | Tĩnh Tu 2 bậc; công pháp gắn bài; Học trước, Thẻ Ôn, Sổ Từ, lưu, kết ải; 2 ải nữa | Cổng học; lịch Minh khả thi (Codex §23.3) | 2–3 tuần | M |
| M2 Co-op online 2–3 | Gửi lệnh (từ đã chốt, điểm đến) 2–5 tin/s/người qua Worker + Durable Objects; bot thay người rớt | Kiểm hạn mức Cloudflare Free trước khi làm | 3–5 tuần | L |
| M3 Voice, Hybrid | Khi `shared/voice` có bộ giải mã | Không double cast; TTS không lọt mic; đo độ trễ | 2–3 tuần sau khi có bộ giải mã | M |
| M4+ Nội dung | Mỗi trường phái mới ~1,5–2 tuần; pet, buff; Thất Tinh sau số đo M2 | | | M mỗi phần |

Lát chơi đầu (M0a–M0c): **7–9 tuần lịch**, hộp xám chơi được sau 2–3 tuần.

## 8. Rủi ro và câu hỏi cho chủ dự án

### 8.1 Rủi ro

| Rủi ro | Giảm bằng |
|---|---|
| Triều dày làm người học không kịp đọc | Chữ chỉ ở Bàn Ấn; trần 8 chữ sống; cổng Ngộp O; từ mới chỉ ở chỗ không gấp |
| Học thành gõ chép (ô liên tục, Tĩnh Tu) | Nghĩa ẩn theo số lần nhớ đúng; đạo đề; bậc Ngộ Đạo; cửa học cho dòng 4–6 |
| Đám đông có xương chưa đo, có thể không đạt Low | Bench là việc đầu tiên; phương án B dùng chung GLB; hạ trần quái sống của luật |
| Chuyển động bị chê cứng | Duyệt 3 model mẫu trước lô lớn; trộn clip; đo kéo giãn lưới theo xương (quy trình Draconis) |
| Hình giống QCBH | Không cầu "悟/魔", không cuộn giấy nhân vật, không máu; bản sắc sơn thủy riêng; quy trình 6 câu Codex §20 |
| Âm chỉ tạo được trên Mac; tai chủ dự án là cổng cuối | Gom lô, lên lịch phiên nghe; âm tạm ghi rõ là tạm |
| Voice phụ thuộc bộ giải mã chưa có | MVP chỉ Typing; hợp đồng hành động có ID làm từ M0 |
| Phình phạm vi theo QCBH (24 trường phái, chế tạo, bản đồ thế giới) | Danh sách "Không làm" ở 4.11; mỗi trường phái mới phải qua cổng riêng |
| Co-op vượt hạn mức Cloudflare Free | Chỉ gửi lệnh, không gửi trạng thái; đo số tin trước M2 |

### 8.2 Câu hỏi (mỗi câu có đề xuất)

| # | Câu hỏi | Đề xuất |
|---|---|---|
| 1 | Hình làm theo A (nhìn 2D, Three.js 3D, GLB), B (sprite nướng từ GLB) hay C (vẽ tay)? | **A**, có buổi A/B cuối M0a; B làm dự phòng cho quái thường |
| 2 | Chữ chỉ ở Bàn Ấn và tối đa 2 Ấn chữ, quái thường không mang chữ? | **Có** |
| 3 | Từ mới chỉ vào qua Tĩnh Tu, Học trước và Chiêu B ở đợt đầu? | **Có** |
| 4 | Công pháp gắn với một bài từ (chủ đề hoặc lát cấp), dòng 4–6 cần từ đạt "đã nhớ"? | **Có**, sức từ cửa học có trần ~10 % |
| 5 | Tâm ma là từ lạc đạo đề, bậc cao ẩn nhãn? | **Có**; bậc Nhập Môn luôn có nhãn |
| 6 | Voice, Hybrid có trong MVP không? | **Không**; làm ở M3 khi có bộ giải mã |
| 7 | Bản sắc "sơn thủy huyền ảo" chất Việt, không máu? | **Có**; chủ dự án duyệt 2 ảnh thử trước khi làm hàng loạt |
| 8 | Nhạc: đàn tranh, sáo trúc, trống, cello; không chuông chùa, không tụng? | **Có** |
| 9 | Hai trường phái đầu là Kiếm (diệt mạnh, xuyên tuyến) và Hỏa (dọn bầy)? | **Có**; hỗ trợ và pet ở M4 |
| 10 | Hai nhân vật riêng cho hai trường phái, hay một thân đổi vũ khí? | **Hai nhân vật**, để đội dễ nhận ra nhau |
| 11 | Mỗi tuần anh có bao nhiêu giờ Tripo/Meshy và nghe âm? | Giả định 6–8 giờ Tripo, 1 giờ nghe |
| 12 | Trong đội chỉ phát âm từ của mình, không chat chữ ở MVP? | **Có** |
