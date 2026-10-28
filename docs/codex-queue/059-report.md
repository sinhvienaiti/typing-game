# Phiếu 059 · Thư viện tài sản · AL-08: quét âm thanh

Ngày 28/10/2026, repo cha trên Mac mini M4. Đã đọc thiết kế §3.3–3.4, phần họ âm §3.6–3.7, §4.1–4.2, §4.6, §7 và phiếu AL-04/AL-08; dùng bộ đọc đầu file AL-04 và bước nối AL-06/AL-07 đang có. **Hoàn tất: K1–K4 và cả sáu kiểm riêng đều đạt.**

## File tạo hoặc sửa

| Đường dẫn | Nội dung |
|---|---|
| `tools/asset-library/scan-audio.mjs` | Quét Space, index/ledger AudioLab, lượt work đủ hai hồ sơ, Dota và lock nhạc riêng; nối sha256, gom biến thể, giấy phép và usedBy; CLI sinh JSON. |
| `tools/asset-library/scan.mjs` | Chỉ thêm import, bước gọi/gộp scan-audio, thống kê/cảnh báo âm trùng và truyền cờ `--all`; giữ các thay đổi AL-06/AL-07 đã có từ đầu. |
| `tools/asset-library/test/scan-audio.test.mjs` | 6 test, gồm cây mẫu tự sinh dưới os.tmpdir(), lớp bọc fs, kiểm tích hợp scan trong cây tạm và kiểm nguồn thật. |
| `library/out/audio-catalog.json` | Đầu ra riêng AL-08, schema `asset-library-audio/1`; 1.849 thẻ hiện mặc định, gồm nguồn riêng tư chỉ lưu trong out. |
| `docs/codex-queue/059-report.md` | Báo cáo này. |

Không cần fixture cố định dưới repo. Test tự sinh WAV nhỏ, index và hồ sơ trong cây tạm của chính nó rồi dọn đúng cây đó. Trên macOS, cây tạm được realpath trước khi kiểm symlink vì `/var` trỏ sang `/private/var`.

`scanAudio()` chỉ đọc, trả `{cards, stats, duplicates, warnings}`. CLI riêng ghi `library/out/audio-catalog.json`; `scan.mjs` gọi trực tiếp hàm này để gộp vào catalog chung ở những lượt quét tiếp theo. Bản sao Space vẫn nằm trong `files[]` với role `copy`, đồng thời có trong `copies[]`, giữ đường dẫn file chính và số biến thể. Media thư viện AudioLab không được mở hoặc băm lại: dùng sha256, kích thước và số đo từ index. Dòng ledger đầy đủ nằm trong provenance; dòng nguồn work giữ theo từng file. Quyền AI trong ledger thắng mặc định giấy phép.

Đầu ra mặc định có 2.183 file, trong đó 1.555 thẻ thư viện ngoài và 65 thẻ có usedBy. Tham chiếu chuỗi đường dẫn có confidence `path`; tham chiếu import.meta.glob có confidence `folder`. Dòng bình luận được bỏ khỏi việc tìm tham chiếu. Dòng uiFile dùng tên ngắn được nối với glob UI trong cùng module.

## K1–K4

| Kiểm | Kết quả |
|---|---|
| K1 · Giới hạn ghi | **ĐẠT.** Bọc fs callback, sync, promises, open có cờ ghi và createWriteStream; CLI/tích hợp dùng cùng lớp bọc promises. Quét repo thật: **0** lời gọi ghi. CLI thật: **2** lời gọi ghi, mkdir out và writeFile audio-catalog.json, **0** ngoài library/out. CLI cây mẫu: **2** lời gọi; tích hợp scan cây mẫu: **5** lời gọi, tất cả dưới out của cây tạm. |
| K2 · Cây Git | **ĐẠT đối với phiếu.** So đầu/cuối chỉ thêm scan-audio.mjs, test và báo cáo, sửa bước gọi âm trong scan.mjs đã bẩn sẵn. Output bị Git bỏ qua. Dòng games/typing-survival có sẵn và giống lúc cuối; không ghi vào game. Hai bản Git đầy đủ và hai bản games/ ở dưới. |
| K3 · Vùng cấm | **ĐẠT.** grep -rlE trên library/out: **0** file khớp, stdout rỗng, exit **1**. library/.thumbs chưa tồn tại. Test chặn đọc vùng cấm trước lstat/readdir/readFile/open, loại đường index thoát gốc và không đi theo symlink. JSON không có chuỗi vùng cấm. |
| K4 · Test | **ĐẠT.** `node --test tools/asset-library/test/scan-audio.test.mjs`: **6 pass, 0 fail, 0 skip**, exit **0**, **23.594 ms**. `node --check` scanner âm, test và scan.mjs đạt; `git diff --check` trên các file mã được phép đạt, exit **0**. |

Test còn xác nhận output symlink bị từ chối, thư mục ngoài không nhận file mới; các dòng nguồn chứa vùng cấm không vào JSON; thư viện ngoài chỉ cần index/ledger ngay cả khi không có media trong cây mẫu. Mọi thao tác xóa chỉ dọn cây tạm do test này tạo.

## Sáu kiểm riêng

| Kiểm | Số đo và kết quả |
|---|---|
| 1 · Đủ âm Space | **116/116** đường dẫn duy nhất trong thẻ; đủ audio header, không lỗi đọc. |
| 2 · Bản sao Kenney | **29** file Space trùng sha256 Kenney. `games/space-typing/src/assets/audio/ui/click.ogg` là bản sao trên **kenney:interface-sounds/Audio/click**, biến thể **002**, file chính click_002.ogg. Thẻ click có **5** biến thể nguồn. |
| 3 · Hai cặp trùng byte | **2** nhóm, mỗi nhóm hai đường dẫn: public/assets/audio/sfx/kenney/confirm.ogg = src/assets/audio/ui/confirm.ogg; public/assets/audio/sfx/kenney/force-field.ogg = src/assets/audio/ui/deploy.ogg. Tất cả thuộc games/space-typing. |
| 4 · Riêng tư | **15** file Dota có licence.private=true và licence.notForRelease=true; **193** file nhạc có licence.private=true. Tất cả onDrive=private; giấy phép lần lượt private-valve/private-producer và đều có audio header. |
| 5 · Ẩn work mặc định | **91** lượt có cả manifest.fragment.json và SOURCES.json, tạo **91** thẻ draft, **0** thẻ work hiện mặc định. Cây mẫu xác nhận `--all` cho thấy draft và giữ cờ hidden; lượt thiếu hồ sơ và master rời không tạo thẻ. |
| 6 · Click usedBy | Có chính xác ref **games/space-typing/src/audio/Sfx.ts:36**, confidence=folder, glob ../assets/audio/ui/*.ogg; và ref **games/space-typing/src/audio/Sfx.ts:672**, confidence=path. Cả hai gắn copyPath của click.ogg, variant=002. |

Đã đọc đủ **1.859** dòng file trong index AudioLab; **0** lần đọc media libraries, **0** cảnh báo lượt quét thật. Đọc **959** file mã nguồn thuộc bốn game cho phép. Bảng ATTRIBUTION tạo **41** dòng nguồn (18 Kenney, 23 Freesound), giữ số Freesound, tác giả, URL và dòng chứng cứ. Bộ quét dùng audioFamilyMap; test phim-ui → ui đồng thời giữ alias cũ. Có chế độ locks-only, được kiểm trên cây mẫu với file Space chưa có tại máy.

## Phần bỏ qua và việc cần chủ dự án xem

- Chưa chạy lại toàn bộ quét hình/GLB của repo thật: phạm vi phiếu là âm thanh. Đã sinh đầu ra âm thật và kiểm bước gộp scan.mjs bằng cây tạm; catalog chung hiện có sẽ nhận âm khi chạy lượt scan toàn bộ tiếp theo.
- **30 file Space** vẫn giữ giấy phép unknown do chưa nối được nguồn từng file qua bảng hoặc sha256. Không tự nâng quyền sao chép; chủ dự án/Claude cần bổ sung bằng chứng nguồn ở lượt giấy phép/tuyển chọn.
- **91 thẻ work** vẫn là draft; `--all` chỉ cho xem, không duyệt hay phát hành. Không đổi trạng thái dựa vào việc có file render.
- Không có phần bỏ qua vì thiếu quyền AudioLab: nguồn ngoài đọc được. Không cần ffprobe, magick, Blender, sinh hình hay sinh âm; dùng bộ đọc đầu file Node của AL-04. Không dùng mạng, trình duyệt, server, build/test game, lệnh media hoặc lệnh Git ghi.

## Git status lúc đầu

```text
 M games/typing-survival
 M tools/asset-library/scan.mjs
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/057-report.md
?? docs/codex-queue/058-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
?? tools/asset-library/doc-facts.mjs
?? tools/asset-library/lib/joins.mjs
?? tools/asset-library/test/doc-facts.test.mjs
?? tools/asset-library/test/scan-joins.test.mjs
```

## Git status lúc cuối

```text
 M games/typing-survival
 M tools/asset-library/scan.mjs
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/057-report.md
?? docs/codex-queue/058-report.md
?? docs/codex-queue/059-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
?? tools/asset-library/doc-facts.mjs
?? tools/asset-library/lib/joins.mjs
?? tools/asset-library/scan-audio.mjs
?? tools/asset-library/test/doc-facts.test.mjs
?? tools/asset-library/test/scan-audio.test.mjs
?? tools/asset-library/test/scan-joins.test.mjs
```

## git status --porcelain games/ · lúc đầu

```text
 M games/typing-survival
```

## git status --porcelain games/ · lúc cuối

```text
 M games/typing-survival
```
