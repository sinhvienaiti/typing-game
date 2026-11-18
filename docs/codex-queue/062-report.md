# Phiếu 062 · Thư viện tài sản · AL-11: dòng tuyển chọn mồi

Ngày 28/10/2026, repo cha trên Mac mini M4. Đã đọc thiết kế §3.3, §3.6, §4.1–4.3, AL-10/11 và báo cáo 060/061; dùng lại dữ kiện AL-07/08, bộ đọc bảng và bộ nối tài liệu đã có. Hoàn tất K1–K4 và bảy kiểm riêng trên ảnh chụp cuối phiên.

## File tạo

| Đường dẫn | Nội dung |
|---|---|
| `tools/asset-library/seed-curated.mjs` | CLI Node; mặc định thêm dòng mới, có `--dry-run`; chỉ ghi năm file cố định. |
| `tools/asset-library/test/seed-curated.test.mjs` | 9 test, lớp bọc fs, cây mẫu tạm, kiểm rò thật và chạy pnpm lib:scan thật với đầu ra chuyển sang cây tạm. |
| `library/curated/dragon-hold.jsonl` | 115 dòng, sắp theo uid. |
| `library/curated/typing-defense.jsonl` | 293 dòng, sắp theo uid. |
| `library/curated/typing-survival.jsonl` | 7 dòng, sắp theo uid. |
| `library/curated/space-typing.jsonl` | 1.416 dòng, sắp theo uid. |
| `library/curated/audio-libraries.jsonl` | 1.555 dòng, sắp theo uid. |
| `docs/codex-queue/062-report.md` | Báo cáo này và danh sách 50 tên cần xem. |

Tổng **3.386 dòng**, uid không trùng trong từng file. Không có file tuyển chọn từ trước phiên; các bản mồi do phiên này tạo đã được sửa trước nghiệm thu. Công cụ cuối cùng chỉ thêm uid mới, giữ nguyên dòng có sẵn dù chưa duyệt; không tự sửa dòng cũ để cập nhật thuật toán.

## Hành vi

- Tên: NAMES_EN → phần Anh của 3D_IMPORT → dịch mồi từ id. Số dòng: **15 NAMES_EN**, **26 3D_IMPORT**, **3.345 seed-translation**. Tên bỏ dấu; alias giữ Việt có dấu/không dấu, id và chú thích Tripo.
- Loại/con lấy folderMap và perItem. Đường runtime và src/assets được bỏ tiền tố để dùng cùng ánh xạ art-src; các nhóm guides/heroes, skills, backgrounds và icons dùng loại theo thiết kế. Không suy loại con từ chú thích Tripo, vì chú thích có thể gọi bộ Barracks là hut.
- Nhãn lấy tên, alias và ghi chú ở các dòng 3D_IMPORT đã nối bằng AL-07. Chỉ nhận từ trong taxonomy; giữ phân biệt gõ/gỗ và sách/sạch. Không mở hay chép nội dung prompt. Không thêm nhãn vật liệu để bù tỷ lệ.
- canonical là {}, reuseNotes/quality/reviewed là null. Dữ kiện điểm tài liệu vẫn do scanner AL-07 nối; Claude sẽ ghi điểm còn thiếu ở AL-12. Âm ngoài có sha256 từ AL-08; md5s để [] khi nguồn không có md5, không đọc/băm lại media AudioLab.
- Chặn private/notForRelease tại thẻ, licence, file, bản sao, đường dẫn và md5 riêng tư; kiểm thêm tên file riêng tư trước khi ghi. Gặp symlink, uid trùng, JSON hỏng hoặc file vừa bị làn khác sửa thì dừng. Dòng cũ giữ nguyên cả khoảng trắng và CRLF.

Lệnh: `node tools/asset-library/seed-curated.mjs`; xem dự kiến bằng `node tools/asset-library/seed-curated.mjs --dry-run`. Không thêm script vào package.json vì phiếu không cho phép.

## K1–K4

| Kiểm | Kết quả |
|---|---|
| K1 · Chỗ ghi | **ĐẠT.** Test bọc fs callback/sync/promises, stream và open có cờ ghi: **20 lời gọi ghi** trước dọn, đều dưới cây tạm test; dọn đúng cây đó. Tiến trình pnpm: **0 ghi**; tiến trình scan: **5 ghi**, đều được chuyển sang cây tạm. Các lượt sinh thật cũng dùng io giới hạn mkdir tại curated và writeFile đúng năm file. Không ghi repo game, cache media, taxonomy/sources hay out thật. |
| K2 · Git | **ĐẠT.** Phiên này chỉ thêm 8 file được phép ở trên. Các thay đổi có sẵn, gồm package.json và games/typing-survival, không do phiên này sửa. Trong lúc chạy xuất hiện thêm docs/codex-queue/068-report.md của làn khác; không công cụ nào của phiên này ghi đường đó. Hai bản status games/ giống nhau; xem cuối báo cáo. |
| K3 · Vùng cấm | **ĐẠT.** Không sinh out/thumbs trong repo. Kiểm bổ sung grep trên out: **0 file khớp**, stdout rỗng, exit **1**; .thumbs chưa có. Catalog quét mới trong cây tạm cũng không có chuỗi cấm. Không đọc/ghi các thư mục bị cấm. |
| K4 · Test | **ĐẠT.** `node --test tools/asset-library/test/seed-curated.test.mjs`: **9 pass, 0 fail, 0 skip**, exit **0**, **12.679,77 ms**. Hai file mjs qua node --check; kiểm khoảng trắng trên mã và năm JSONL đạt. |

## Bảy kiểm riêng

| Kiểm | Kết quả và số đo |
|---|---|
| 1 · Độ phủ | **ĐẠT.** Bản quét cuối: **3.386/3.386 thẻ hiện công khai có dòng, tên và kind (100%)**. **341/411 model3d có ít nhất hai nhãn (82,97%)**. |
| 2 · Quét và câu vàng | **ĐẠT.** Chạy đúng `pnpm lib:scan` bằng tiến trình con, đọc nguồn thật; fs chuyển mọi đầu ra out sang os.tmpdir(). Quét **4.802 thẻ, 8.080 file**, **9,501 giây**; **7/7 câu vàng đạt** với đúng topN và uid của queries.json. Không sửa câu tìm hay lõi xếp hạng. |
| 3 · Lượt hai | **ĐẠT.** Trên đầu vào quét mới và đầu vào catalog cũ: **0 dòng thêm, 0 file đổi**. Lượt CLI cuối cũng trả 0/0. |
| 4 · reviewed | **ĐẠT.** Mẫu có tên tự đặt, khoảng trắng và CRLF giữ từng byte sau khi thêm dòng/sắp. Dòng chưa reviewed cũng giữ nguyên. Ca làn khác vừa ghi reviewed sau đọc kế hoạch: dừng, giữ nguyên byte mới. |
| 5 · Tên không dấu Việt | **ĐẠT.** **0/3.386 tên** có dấu Việt; **0 trường prompt**. |
| 6 · Chặn rò | **ĐẠT, không bỏ qua.** Có private.md5 trên máy; đọc tên file Dota chỉ để đối chiếu. **208 tên riêng tư**, **3.389 khối văn bản** gồm năm JSONL thật, taxonomy, sources và ứng viên; **0 khớp**. Không in tên riêng tư trong báo cáo/log. |
| 7 · 50 tên độ tin thấp | **ĐẠT.** Bảng dưới gồm đúng 50 dòng theo điểm tăng dần rồi uid; điểm chỉ là mức ưu tiên rà, không phải xác suất đã hiệu chuẩn. |

Các câu vàng: hut/chòi/choi đều đủ **4 uid trong top 6**; jetty **1 trong top 3**; bridge **2 trong top 5**; rock/pine-forest **3 trong top 20**; wood click/audio **1 trong top 3**.

## Giới hạn và việc Claude cần xem

- **Không cập nhật catalog/out thật:** danh sách ghi của phiếu không có library/out. Lệnh pnpm lib:scan bắt buộc đã chạy thật trong test, chỉ chuyển nơi ghi. Claude cần quét lại ra out thật bằng quyền của AL-12 khi duyệt. Các file sinh tạm đã được dọn; không sửa scanner để lách phạm vi.
- **Scanner hiện có 1.899 cảnh báo**, trong đó **1.612 dòng “tuyển chọn không còn thẻ”**. Đây là các dòng âm thanh: AL-06 đọc curated trước khi thêm thẻ từ scanAudio; do đó metadata tuyển chọn âm chưa được áp vào catalog âm. Bảy câu vàng vẫn đạt. Cần nối phần này trong phiếu được phép sửa scanner; phiên AL-11 giữ nguyên mã của làn trước.
- Media của làn khác tăng trong lúc làm. Bản đầu có 3.382 ứng viên; đã bổ sung **4 uid mới** từ ảnh chụp quét mới, thành 3.386. Test kiểm tuyệt đối một-thẻ-một-dòng trên ảnh chụp tạm và kiểm ngưỡng 95% trên bộ thật, tránh đòi cây nguồn đang thay đổi phải đứng yên. Số đo cuối đạt 100% trên cả hai.
- Mồi chưa phải duyệt bằng mắt: **0 dòng reviewed**. Claude xem 50 tên dưới, nhất là tên riêng và bộ phận chỉ có id Việt; tiếp tục AL-12 để chấm tên, nhãn, chất lượng và khả năng dùng lại.
- Bỏ qua thẻ ẩn và thẻ bị chặn theo quyền riêng tư/phát hành; không sinh ảnh/âm, không cần ffprobe, magick hay Blender. AudioLab đọc được qua scanner, **1.859 dòng file ngoài, 0 lần đọc media ngoài**; không có phần bắt buộc nào bị bỏ qua.
- Không dùng mạng, trình duyệt, server, build/test game, lệnh media hay lệnh Git có ghi.

## 50 tên cần Claude duyệt trước

Tất cả các tên dưới có nameSource là seed-translation. Điểm 0,25 đánh dấu id còn chữ Việt/tên riêng khó suy; 0,40 là tên dịch từ id có tài liệu Việt nhưng chưa có tên Anh chính thức. Các tên đồng điểm được xếp theo uid.

| # | uid | Tên mồi | Độ tin |
|---|---|---|---:|
| 1 | `space-typing:td/helpers/helper-gach-ref` | Helper Gach Ref | 0.25 |
| 2 | `space-typing:td/helpers/helper-gach-strap` | Helper Gach Strap | 0.25 |
| 3 | `space-typing:td/helpers/helper-phay-ref` | Helper Phay Ref | 0.25 |
| 4 | `space-typing:td/helpers/helper-phay-strap` | Helper Phay Strap | 0.25 |
| 5 | `typing-defense:bosses/dai-bang-tinh-front` | Eagle Spirit Front | 0.25 |
| 6 | `typing-defense:bosses/moc-tinh` | Moc Tinh | 0.25 |
| 7 | `typing-defense:bosses/moc-tinh-back` | Moc Tinh Back | 0.25 |
| 8 | `typing-defense:bosses/moc-tinh-side` | Moc Tinh Side | 0.25 |
| 9 | `typing-defense:helpers/helper-gach-strap` | Helper Gach Strap | 0.25 |
| 10 | `typing-defense:helpers/helper-gach-wingband` | Helper Gach Wingband | 0.25 |
| 11 | `typing-defense:helpers/helper-phay-strap` | Helper Phay Strap | 0.25 |
| 12 | `typing-defense:helpers/helper-phay-tail` | Helper Phay Tail | 0.25 |
| 13 | `typing-defense:heroes/lam` | Lam | 0.25 |
| 14 | `typing-defense:heroes/lam-back` | Lam Back | 0.25 |
| 15 | `typing-defense:heroes/lam-side` | Lam Side | 0.25 |
| 16 | `typing-defense:models/heroes/lam` | Lam | 0.25 |
| 17 | `typing-defense:portraits/helper-gach-happy` | Helper Gach Happy | 0.25 |
| 18 | `typing-defense:portraits/helper-gach-scared` | Helper Gach Scared | 0.25 |
| 19 | `typing-defense:portraits/helper-phay-happy` | Helper Phay Happy | 0.25 |
| 20 | `typing-defense:portraits/helper-phay-scared` | Helper Phay Scared | 0.25 |
| 21 | `typing-defense:portraits/lam` | Lam | 0.25 |
| 22 | `typing-defense:portraits/lam-ult` | Lam Ult | 0.25 |
| 23 | `typing-defense:portraits/moc-tinh` | Moc Tinh | 0.25 |
| 24 | `typing-defense:workers/worker-kit-dong-head` | Worker Kit Dong Head | 0.25 |
| 25 | `typing-defense:workers/worker-kit-dong-rammer` | Worker Kit Dong Rammer | 0.25 |
| 26 | `typing-defense:workers/worker-kit-sam-drumstick` | Worker Kit Sam Drumstick | 0.25 |
| 27 | `typing-defense:workers/worker-kit-sam-head` | Worker Kit Sam Head | 0.25 |
| 28 | `typing-defense:workers/worker-kit-sam-vest` | Worker Kit Sam Vest | 0.25 |
| 29 | `typing-defense:workers/worker-kit-se-head` | Worker Kit Se Head | 0.25 |
| 30 | `typing-defense:workers/worker-kit-se-quiver` | Worker Kit Se Quiver | 0.25 |
| 31 | `typing-defense:workers/worker-kit-tieu-axe` | Worker Kit Tieu Axe | 0.25 |
| 32 | `typing-defense:workers/worker-kit-tieu-head` | Worker Kit Tieu Head | 0.25 |
| 33 | `typing-defense:workers/worker-kit-tro-head` | Worker Kit Tro Head | 0.25 |
| 34 | `typing-defense:workers/worker-kit-tro-scroll` | Worker Kit Tro Scroll | 0.25 |
| 35 | `dragon-hold:2d/samples/blight-wolf-front` | Blight Wolf Front | 0.40 |
| 36 | `dragon-hold:2d/samples/heo-test-a` | Pig Test A | 0.40 |
| 37 | `dragon-hold:2d/samples/heo-test-b` | Pig Test B | 0.40 |
| 38 | `dragon-hold:backdrops/pine-river-far` | Pine River Far | 0.40 |
| 39 | `dragon-hold:backdrops/pine-river-far-015` | Pine River Far 015 | 0.40 |
| 40 | `dragon-hold:decals/pine-river/dirt-patches` | Dirt Patches | 0.40 |
| 41 | `dragon-hold:decals/pine-river/dirt-patches-015` | Dirt Patches 015 | 0.40 |
| 42 | `dragon-hold:decals/pine-river/flower-clusters` | Flower Clusters | 0.40 |
| 43 | `dragon-hold:decals/pine-river/flower-clusters-015` | Flower Clusters 015 | 0.40 |
| 44 | `dragon-hold:decals/pine-river/forest-litter` | Forest Litter | 0.40 |
| 45 | `dragon-hold:decals/pine-river/forest-litter-015` | Forest Litter 015 | 0.40 |
| 46 | `dragon-hold:decals/pine-river/moss-puddles` | Moss Puddles | 0.40 |
| 47 | `dragon-hold:decals/pine-river/moss-puddles-015` | Moss Puddles 015 | 0.40 |
| 48 | `dragon-hold:enemies/blight-wolf` | Blight Wolf | 0.40 |
| 49 | `dragon-hold:enemies/blight-wolf-front` | Blight Wolf Front | 0.40 |
| 50 | `dragon-hold:enemies/moss-archer-back` | Moss Archer Back | 0.40 |

## git status --porcelain · lúc đầu

```text
 M docs/CODEX_QUEUE.md
 M games/typing-survival
 M package.json
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/061-report.md
?? docs/codex-queue/066-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
?? tools/asset-library/find.mjs
?? tools/asset-library/play.mjs
?? tools/asset-library/show.mjs
?? tools/asset-library/test/cli.test.mjs
```

## git status --porcelain · lúc cuối

```text
 M docs/CODEX_QUEUE.md
 M games/typing-survival
 M package.json
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/061-report.md
?? docs/codex-queue/062-report.md
?? docs/codex-queue/066-report.md
?? docs/codex-queue/068-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? library/curated/
?? shared/shared
?? tools/asset-library/find.mjs
?? tools/asset-library/play.mjs
?? tools/asset-library/seed-curated.mjs
?? tools/asset-library/show.mjs
?? tools/asset-library/test/cli.test.mjs
?? tools/asset-library/test/seed-curated.test.mjs
```

## git status --porcelain games/ · lúc đầu

```text
 M games/typing-survival
```

## git status --porcelain games/ · lúc cuối

```text
 M games/typing-survival
```
