# Phiếu 057 · Thư viện tài sản · AL-06: nối sổ, lock, bản sao, tuyển chọn

Ngày 28/10/2026, repo cha trên Mac mini M4, Node **v24.22.0**. Lượt đo cuối lúc **13:17:54 ICT**. Đã đọc thiết kế `docs/tools/ASSET_LIBRARY.md` §3.3–3.6, §4.1–4.5 và AL-05/AL-06 trong danh sách phiếu; dùng lại bộ quét, ngữ pháp, cache và bộ đọc Map Factory hiện có.

**Chưa đủ điều kiện đóng phiếu.** Mã và **9/9 test AL-06 đạt**; **5/6 kiểm riêng đạt**. Kiểm 6 chỉ đạt **1.932/2.936 uid = 65,8038%**, dưới ngưỡng 90%. Có thêm **4 test AL-05 cần cập nhật đường dẫn cache**; chúng nằm ngoài phạm vi được sửa của phiếu.

## File đã tạo hoặc sửa

| Đường dẫn | Việc đã làm |
|---|---|
| `tools/asset-library/scan.mjs` | Nối dữ liệu vào lượt quét; thêm `--locks-only`, chế độ trong catalog và thống kê bản sao/file ẩn. Cache mới ghi vào `library/out/hash.json`. |
| `tools/asset-library/lib/joins.mjs` | Đọc lock, SOURCES, preset, manifest và JSONL tuyển chọn; gom bản sao; tính Drive, canonical, pipeline, trạng thái và `formerUids`. |
| `tools/asset-library/test/scan-joins.test.mjs` | 9 test, cây mẫu tự sinh dưới `os.tmpdir()` và tự dọn; gồm lớp bọc fs toàn cục. Không thêm fixture cố định. |
| `library/out/catalog.json` | Catalog đầy đủ cuối lượt: **2.936 thẻ, 5.838 file**, `mode: full`. |
| `library/out/scan-report.md` | Thống kê vai trò, file ẩn, bản sao và cảnh báo. |
| `library/out/hash.json` | Cache của lượt AL-06; cache AL-05 chỉ được đọc làm mồi. |
| `library/out/al06-checks.json` | Số đo, 9 dòng đối chiếu grep, 6 liên kết Draconis, băm bảo vệ cache và nhật ký ghi. |
| `library/out/al06-missing-lock-uids.json` | **1.004 uid** chưa tái dựng được từ bộ metadata Git, kèm file và md5 để duyệt. |
| `docs/codex-queue/057-report.md` | Báo cáo này. |

Preset thắng liên kết `usedBy` cũ; trường `image` vẫn thắng luật gương. `downloadedAs` và `notMadeYet` được giữ trong provenance. File chưa có trên máy vẫn dựng được từ lock/SOURCES với `local: false`. Chế độ `--locks-only` dùng `git ls-files` riêng cho repo cha và bốn game, bỏ manifest/preset/SOURCES/lock chưa được Git theo dõi, không đọc media hoặc cache để lấy danh tính.

Bản sao trong handoff trỏ về thẻ cùng md5; bản không trùng thành thẻ nháp. Bản handoff trùng file loại cũng được nối vào thẻ gốc, giữ `rejectedMd5`. Preset/manifest, handoff và tuyển chọn đều đi qua kiểm đường dẫn và symlink. Tuyển chọn được áp sau trường tự sinh; uid hiện tại được giữ khi khớp bằng md5. Quyền riêng tư và danh sách md5 bị loại không bị dòng tuyển chọn xóa mất.

## K1–K4

| Kiểm | Kết quả và số đo |
|---|---|
| **K1 · Chỉ ghi phạm vi cho phép** | **ĐẠT.** Test bọc fs toàn cục, kể cả import Map Factory: **8 lời gọi ghi**, tất cả dưới `library/out`, **0 ngoài phạm vi**. Kiểm thật full + locks-only + khôi phục catalog full + ghi bằng chứng: **12 lời gọi ghi**, **0 ngoài phạm vi**. Bao phủ write/append/mkdir/rename/copy/symlink/unlink/rm và chặn open có cờ ghi. |
| **K2 · Cây Git** | **ĐẠT đối với công việc của phiếu.** Chỉ sửa/thêm ba file mã/test và báo cáo được phép; sản phẩm dưới `library/out` bị Git bỏ qua. Thay đổi `games/typing-survival` đã có trước lượt này, còn nguyên dòng status cuối. Những thay đổi khác của làn đồng thời được ghi bên dưới. |
| **K3 · Chặn Tu Tiên** | **ĐẠT.** Grep tên cấm trong `library/out`: **0 file khớp**, stdout rỗng, exit **1** nghĩa là không khớp. `library/.thumbs` chưa tồn tại và không được tạo. Test đọc vùng cấm/symlink: **0 lần đọc**, **0 tên rò trong toàn bộ out**. |
| **K4 · Test phiếu** | **ĐẠT.** `node --test tools/asset-library/test/scan-joins.test.mjs`: **9 pass, 0 fail, 0 skip**, exit **0**, khoảng **0,98 giây**. |

Hai file được bảo vệ có SHA-256 trước/sau giữ nguyên (**2/2**): `library/.cache/hash.json` và `.cache/media-hash.json`. Băm cụ thể nằm trong `al06-checks.json`. Không ghi tên từ lock riêng tư ra ngoài `library/out`.

## Sáu kiểm riêng

| Kiểm | Kết quả |
|---|---|
| **1 · Herb Hut** | **ĐẠT.** **9 file hiện**, đúng 9 vai trò; `hiddenFiles`: **rejected 9, prompt 14, report 2**. **9/9** md5 trùng dòng grep trong lock và `onDrive: yes`. `status: shipped`, `pipeline: runtime`. |
| **2 · Wooden Jetty** | **ĐẠT.** `wooden-jetty.try1.png`: **same-folder**; ảnh `rong_wooden-jetty.png` của dot3: **handoff**; cùng md5 **805afcb508b3dbda47baff8aecb8fd19**. Pipeline **tripo-requested**. |
| **3 · Raw Space** | **ĐẠT.** File chính dưới `art-src/models/raw`: **0**. **172** file raw được ghi thành bản sao. Không xóa hoặc dời file gốc. |
| **4 · Draconis** | **ĐẠT.** **6/6** file runtime ở Rồng có `copyOf` trỏ Space; bảng bên dưới. |
| **5 · Tuyển chọn sau đổi tên** | **ĐẠT.** Test thực hiện `rename` trong cây tạm. Dòng cũ gắn lại bằng md5, uid mới `dragon-hold:houses/renamed`, `formerUids: ["dragon-hold:houses/old-name"]`; **5 trường** thủ công giữ đúng. Có kiểm riêng uid chính xác, md5 mơ hồ và canonical tuyển chọn. |
| **6 · Độ phủ locks-only** | **CHƯA ĐẠT.** Full **2.936 uid**; locks-only **1.932 uid**; giao **1.932 uid**, tỷ lệ **65,8038%**. Thiếu **1.004 uid**, toàn bộ thuộc Space. |

Đối chiếu Herb Hut, in cả đầu ra scan và dòng grep thật. Đường dẫn sau md5 là đường dẫn tương đối từ `games/dragon-hold/`:

```text
SCAN glb-original | yes | b2ade5601998050f7e12beb3ba7e6459
GREP b2ade5601998050f7e12beb3ba7e6459  art-src/3d/houses/herb-hut.glb
SCAN concept | yes | 9907b30aabab57040e88be86ac89ec2b
GREP 9907b30aabab57040e88be86ac89ec2b  art-src/houses/herb-hut.png
SCAN tripo-source | yes | a61413b7274a3c61e6490b82b5debd06
GREP a61413b7274a3c61e6490b82b5debd06  art-src/houses/herb-hut.tripo.png
SCAN icon-256 | yes | f89feb3357dd70c2f8fd761f4f303279
GREP f89feb3357dd70c2f8fd761f4f303279  art-src/icons/normalized/herb-hut.256.png
SCAN icon-64 | yes | 1644c8b50f75c8513053306782411fb7
GREP 1644c8b50f75c8513053306782411fb7  art-src/icons/normalized/herb-hut.64.png
SCAN glb-processed | yes | 08267409632cf407eafe60c2c2bfd989
GREP 08267409632cf407eafe60c2c2bfd989  art-src/models/props/herb-hut.glb
SCAN icon | yes | cc737bc005e37a54e8645b814a4158ef
GREP cc737bc005e37a54e8645b814a4158ef  art-src/ui/icons/herb-hut.png
SCAN runtime-high | yes | e6b8b309ea47c2ce140fbeaf511cffe6
GREP e6b8b309ea47c2ce140fbeaf511cffe6  public/assets/dragon-hold/models/m0b/props/herb-hut/herb-hut.high.glb
SCAN runtime-medium | yes | 7241e7200487086415c0e436cb68b29e
GREP 7241e7200487086415c0e436cb68b29e  public/assets/dragon-hold/models/m0b/props/herb-hut/herb-hut.medium.glb
```

Draconis; tiền tố đường dẫn chung là `games/dragon-hold/public/assets/dragon-hold/models/`:

| File | `copyOf` |
|---|---|
| `guides/draconis-v4/draconis-v4.high.glb` | `space-typing:guides/draconis-v4` |
| `guides/draconis-v4/draconis-v4.medium.glb` | `space-typing:guides/draconis-v4` |
| `heroes/draconis-v2/draconis-v2.high.glb` | `space-typing:heroes/draconis-v2` |
| `heroes/draconis-v2/draconis-v2.medium.glb` | `space-typing:heroes/draconis-v2` |
| `heroes/draconis-v3/draconis-v3.high.glb` | `space-typing:heroes/draconis-v3` |
| `heroes/draconis-v3/draconis-v3.medium.glb` | `space-typing:heroes/draconis-v3` |

## Phần cần duyệt hoặc làm tiếp

**Độ phủ chưa đạt do bộ metadata đầu vào.** Trong 1.004 uid Space thiếu, các nhóm lớn gồm `public/assets/space-typing/backgrounds` **384**, `fx` **43**, `src/assets/icons/equipment` **42**, `skills` **26**, `public/assets/space-typing/ships` **25**. Danh sách đầy đủ nằm trong `library/out/al06-missing-lock-uids.json`. Cần bổ sung sổ cho các uid này, hoặc chủ dự án quyết định mở rộng đầu vào của `--locks-only` sang danh sách media Git. Phiếu hiện tại yêu cầu chỉ dùng lock, SOURCES, preset và manifest có trong Git, đồng thời cấm ghi các sổ game; tôi giữ đúng giới hạn đó.

**Test AL-05 chưa tương thích đường dẫn cache.** Lệnh bổ sung `node --test tools/asset-library/test/scan-core.test.mjs` cho **4 pass, 4 fail**, exit **1**. Ba ca dừng ở lớp bọc ghi vì chỉ cho phép `library/.cache/hash.json`; một ca đọc cache tại đường dẫn cũ và gặp ENOENT. Không sửa file test này vì ngoài danh sách được ghi. Cần đổi các kỳ vọng sang `library/out/hash.json` trong lượt được phép sửa test AL-05. Các ca đọc header, biến mất giữa lượt, mồi cache media và dùng sổ GLB vẫn đạt.

Lượt thật cuối: full **3.064,617 ms**, locks-only **588,903 ms**; lượt locks-only **0 băm, 0 đọc GLB, 0 file local=true, 0 cảnh báo**. Full có **285 cảnh báo**: 267 cảnh báo trục sinh vật, 16 `original-not-found` từ số đo GLB, 1 header ảnh chưa hỗ trợ và 1 cảnh báo unknown **353/5.838 = 6,0466%**. Không nới ngữ pháp hoặc xóa cảnh báo để làm số đẹp.

Không sửa sổ game, không cập nhật lock Drive, không sửa ngữ pháp hay test của AL-05, không chạy build/test game, không dùng mạng hoặc server, không sinh ảnh/âm thanh. Không có thao tác Git ghi. Chỉ xóa hoặc đổi tên fixture do chính test tạo trong thư mục tạm.

## Cây Git trước và sau

`git status --porcelain` đầu lượt:

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

`git status --porcelain games/` đầu lượt:

```text
 M games/typing-survival
```

`git status --porcelain` cuối lượt:

```text
 M games/typing-survival
 M tools/asset-library/scan.mjs
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/057-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
?? tools/asset-library/lib/joins.mjs
?? tools/asset-library/test/scan-joins.test.mjs
```

`git status --porcelain games/` cuối lượt:

```text
 M games/typing-survival
```

Dòng game đã có từ đầu; công cụ không ghi game, được lớp bọc fs xác nhận. Báo cáo 052 không còn hiện untracked và thư mục Map Factory hiện thành đường dẫn file do công việc đồng thời; tôi không chỉnh hoặc dọn các đường dẫn đó. Tệp Tu Tiên ở status chỉ được liệt kê tên bởi Git, không được mở.
