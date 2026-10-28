# Phiếu 053 · AL-02: Từ vựng, từ đồng nghĩa, danh sách quét

Ngày làm: 28/10/2026. **Hoàn thành 6/6 kiểm nghiệm thu; 9/9 test đạt.**

## File tạo

- `library/.gitignore`: đúng sáu thư mục sinh ra hoặc riêng tư cần bỏ qua.
- `library/taxonomy.json`: 16 loại hình/3D, 14 loại âm và nhãn menu tiếng Việt; 254 nhãn tiếng Anh; 51 nhóm đồng nghĩa với 183 từ duy nhất; vùng, phong cách, trạng thái, bước làm; 134 dòng ánh xạ thư mục, 9 họ và 16 nhóm âm AudioLab.
- `library/sources.json`: 16 gốc quét (12 gốc của bốn game và bốn gốc ngoài game); chế độ nháp, riêng tư, chỉ tìm bản sao; danh sách cấm và bỏ qua áp cả tại gốc thư mục lẫn bên dưới.
- `library/licences.json`: đủ 9 khóa giấy phép và năm trường quyền yêu cầu.
- `tools/asset-library/lib/taxonomy.mjs`: `load()`, `resolve()`, `related()`, `kindFor()`, `styleFor()`; chỉ đọc, dữ liệu bất biến.
- `tools/asset-library/test/taxonomy.test.mjs`: kiểm trên cây thật và lớp bọc `fs`.
- `docs/codex-queue/053-report.md`: báo cáo này.

## Kết quả kiểm

Lệnh: `node --test tools/asset-library/test/taxonomy.test.mjs` (Node v24.22.0).

| Kiểm | Kết quả |
| --- | --- |
| K1 · Chỉ ghi nơi được phép | Đạt. Test chạy toàn bộ API trong tiến trình con với lớp bọc các hàm ghi `fs`, bản đồng bộ, `fs.promises`, luồng ghi và `open` có cờ ghi. In **Lời gọi ghi: 0**. |
| K2 · Cây Git | Đạt. Sáu file triển khai và báo cáo là toàn bộ phần thêm của phiếu; không sửa file đã có. Hai ảnh chụp `games/` giống nhau, có bên dưới. |
| K3 · Không lọt vùng cấm vào sản phẩm | Không áp dụng bước grep: phiếu không sinh `library/out` hay `library/.thumbs`; cả hai không tồn tại tại lúc kiểm. Tên vùng cấm chỉ khai trong bảng cấm nguồn. Không truy cập vùng cấm. |
| K4 · Test | **9 đạt, 0 hỏng, 0 test bị bỏ qua**, mã thoát 0. |
| 1 · Đi thật thư mục | **157 thư mục**, chỉ dùng `readdirSync(..., {withFileTypes:true})`, không đọc media. Test in từng đường đã đi; tất cả có dòng ánh xạ riêng, không dùng mặc định để che thư mục thiếu. |
| 2 · Đồng nghĩa | **51 nhóm, 183 từ duy nhất**, không trùng sau chuẩn hóa Unicode, hoa/thường và dấu nối/khoảng trắng. Mọi alias gốc tripo-match còn được giữ hoặc đưa sang bảng có phạm vi. |
| 3 · Tra từ và liên quan | `hut/chòi/choi/lều/leu → hut`; `nhà/nha → house`; `related('hut','house') → true`. Có kiểm quan hệ đối xứng và `gõ → click`, `gỗ/go → wood`. |
| 4 · Từ Việt theo thư mục | `cau` chỉ ra `bridge` trong `typing-defense:landmarks` và con của nó, kể cả đường gương 3D; không thư mục ra `null`. `da → stone` chỉ trong thành phần thư mục `scenery/` hoặc `landmarks/`. Có ca sai game, sai biên thư mục và `..`. |
| 5 · AudioLab | **FAMILIES: 9/9**, **CATEGORIES: 16/16** có ánh xạ. Chỉ đọc Python như văn bản, không chạy Python hay AudioLab. |
| 6 · Dung lượng và ổn định | **38.420 byte < 60.000 byte**; **254 nhãn**, đủ **30/30 inferTags**. JSON ghi với khóa sắp đệ quy; tuần tự hóa lại hai lần giống từng byte trong bộ nhớ, không ghi lại file khi test. |

Số thư mục thật theo game: `dragon-hold`: **28**; `typing-defense`: **53**; `typing-survival`: **1**; `space-typing`: **75**.

## Quy ước cho phiếu sau

- `folderMap[game]` dùng đường tương đối dưới `art-src`; ảnh và `art-src/3d` dùng chung luật gương. Đường âm `public/...`, `src/...` giữ tương đối từ gốc game. `kindFor` trả chuỗi loại hoặc `null`, ưu tiên dòng thư mục sâu nhất rồi từng món.
- `styleFor(game)` trả phong cách của game. Ảnh Lời Gọi cũ trong `space-typing:td/` có trường ghi đè `style: viet-village` trong bảng thư mục.
- Hai nhóm `hut` và `house` đã tách theo thiết kế §3.6, dù bảng tripo-match cũ gộp chung. `cau` và `da` chuyển sang `viTokens`, không còn là alias toàn cục.
- `Dota-Sounds` có `private`, `notForRelease`, giấy phép `private-valve`. Các thư mục hỗn hợp phụ như `refs`, `2d-prompts`, `tripo-spares` có loại mặc định `prop`; việc tuyển chọn từng tài sản thuộc phiếu sau.
- Gốc handoff giữ chế độ `copies-only` đúng yêu cầu AL-02; phiếu này không quét handoff.

## Bỏ qua và phần cần chủ dự án xem

- `games/typing-survival/art-src/3d` chưa tồn tại. Test in rõ **Bỏ qua gốc chưa tồn tại**; các thư mục đang có vẫn được kiểm đủ. Không tạo thư mục trong game.
- Không cần ffprobe, magick, Blender hay quyền đọc AudioLab cho AL-02. Không thử quét AudioLab, không gọi mạng, trình duyệt, server, build hay test của game; không chạy media pull/push hoặc Git có ghi.
- Cần xem mặc định `stability-community`: đang khóa thương mại/đầu vào AI/phát hành cho đến khi dòng nguồn có bằng chứng đáp ứng điều kiện dự án theo AUDIO_PIPELINE §10.1; chưa suy đoán rằng đăng ký đã hoàn tất. CC0 cho phép đầu vào AI theo mặc định, nhưng dòng nguồn có yêu cầu từ chối AI phải ghi đè thành `false`.
- Không sinh hình hay âm vì phiếu chỉ yêu cầu dữ liệu chữ và API; không còn hạng mục AL-02 chưa làm.

## Ảnh chụp Git

`git status --porcelain` lúc đầu:

```text
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/052-report.md
?? docs/tools/map-factory/
?? shared/shared
```

`git status --porcelain` lúc cuối (bổ sung dòng báo cáo sau khi tạo file):

```text
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/052-report.md
?? docs/codex-queue/053-report.md
?? docs/tools/map-factory/
?? library/
?? shared/shared
?? tools/asset-library/
```

`git status --porcelain games/` lúc đầu:

```text
 M games/typing-survival
```

`git status --porcelain games/` lúc cuối:

```text
 M games/typing-survival
```

Dòng `M games/typing-survival` đã có từ đầu và thuộc làn khác; phiếu này không ghi dưới `games/`. Các dòng ngoài phạm vi khác cũng giữ nguyên.
