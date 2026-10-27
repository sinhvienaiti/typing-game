# Gợi ý ghép GLB Tripo với ảnh nguồn

Phiếu 045 · Node ESM, chỉ dùng thư viện chuẩn và ImageMagick trên máy. Công cụ **chỉ gợi ý**: Claude vẫn xem hình trước khi nhập model. Điểm không phải xác suất đúng.

## Chạy

Chạy từ repo cha, không cần cài gói, mạng, dev server hoặc trình duyệt:

```sh
node tools/tripo-match/match.mjs --upload typing-game-handoff-2026-10-25/tripo-upload
node tools/tripo-match/match.mjs --upload typing-game-handoff-2026-10-25/tripo-upload-dot2
```

Cú pháp đầy đủ:

```text
node tools/tripo-match/match.mjs --upload <thư mục upload> [--glb <thư mục GLB>] [--out <file.json>]
```

- Mặc định tìm `_GLB tải về` ngay dưới upload; nhận cả tên Unicode NFC và NFD trên macOS. Đọc GLB trong các thư mục con của thư mục GLB đã chọn.
- In bảng Markdown ra stdout: tên file, số tam giác, rộng : cao, ba ứng viên gốc cùng điểm tổng/face/hình/chữ và kết quả ghép một-một.
- `--out` ghi JSON mới bằng cờ `wx`, không ghi đè. Thư mục cha phải tồn tại. Cấm đầu ra trong upload, cây GLB, `games/` và toàn bộ `typing-game-handoff-2026-10-25/`; kiểm đường dẫn qua symlink ở thư mục cha. Không tạo cache hoặc file cạnh media.
- JSON có `config`, `candidates`, `rows[].top3`, `rows[].assigned`, `warnings` và `mediaIntegrity`. Mỗi thành phần giữ điểm chưa làm tròn cùng tỉ số face, khoảng cách log hình, từ truy vấn và từ khớp. Bảng Markdown làm tròn hai chữ số; JSON giữ nguyên độ chính xác.
- Thư mục GLB rỗng hoặc chưa tồn tại: in `0 GLB`, thoát 0. Không cần gọi ImageMagick trong trường hợp này.
- GLB hỏng: giữ dòng có lỗi, xử lý tiếp file khác rồi thoát 1. Lỗi đo ảnh: cảnh báo, điểm hình bằng 0. Thiếu bounds: điểm hình bằng 0 và giữ cảnh báo của bộ quét. File media đổi MD5 trong khi chạy: dừng và thoát 1.

ImageMagick được gọi trực tiếp bằng `child_process.execFile`, không qua shell:

```text
/opt/homebrew/bin/magick <ảnh> -fuzz 15% -trim -format '%w %h' info:
```

Mỗi lần đo có giới hạn 30 giây. Công cụ không xuất lại ảnh, không render GLB và không đọc URI mạng.

## Cách đọc và chấm

Mỗi model là một ứng viên, gom các ảnh cùng `<game>_<id>`; bỏ hậu tố `_front`, `_back`, `_left` và `.alpha`/`.flat` khi xác định id. Ưu tiên ảnh front, rồi ảnh đơn, left, back; cùng mức ưu tiên thì lấy theo thứ tự tên file. Không lấy tỉ lệ tốt nhất trong nhiều góc để nâng điểm. Chỉ lấy ảnh PNG ngay trong các thư mục `face <N> - …`; bỏ các thư mục khác như `_cu-khong-gui`. Không đi theo symlink bên trong cây media.

Đếm GLB bằng hàm `inspectGlb` nhập từ `tools/map-factory/registry/scan-assets.mjs` của phiếu 025: tự đọc header GLB 2, chunk JSON/BIN; đếm primitive trong **scene 0**, nhân theo số lần node dùng mesh. TRIANGLES dùng số index/đỉnh chia 3; STRIP/FAN dùng `max(0, count - 2)`. Bounds từ POSITION min/max, áp dụng ma trận/TRS và cây node. Dữ liệu nén thiếu min/max được báo cần giải nén, không suy bounds. Không mở các buffer/texture bên ngoài GLB.

Tổng điểm là `face + hình + chữ`. Các hằng số chung nằm trong `CONFIG`, bảng từ trong `SYNONYMS` và `STOP` của `match.mjs`; không có bảng nối tên file Tripo với mã model.

### Face limit

```text
F = max(face thư mục, minimumFaces)
r = triangles / F
d = abs(log(r / faceTarget))
face = faceReward - faceSlope * d       nếu faceLow <= r <= faceHigh
face = -facePenalty - faceSlope * d     nếu ngoài khoảng
```

| Hằng số | Giá trị | Căn cứ |
|---|---:|---|
| `minimumFaces` | 3000 | 20 GLB đợt 1 thuộc thư mục face 2000 lại có 2748–2966 tam giác. Dùng một ngưỡng sàn chung thay vì phạt cả nhóm. |
| `faceLow`, `faceHigh` | 0,55; 1,02 | Cho phép Tripo giảm nhiều tam giác nhưng phạt mạnh khi vượt bậc; 35 GLB còn lại đo được 0,7265–0,998 lần face. |
| `faceTarget` | 0,95 | Tripo thường xuất sát dưới mức đặt. |
| `faceReward`, `faceSlope`, `facePenalty` | 35; 35; 45 | Phân biệt các bậc dù cùng trong khoảng, với bước trừ 80 điểm khi ra ngoài bậc. |

JSON giữ cả `rawRatio = triangles / face thư mục` và `effectiveLimit`; không thay số face khai báo trong nguồn. Ngưỡng sàn là suy luận từ đợt 1, cần xem lại nếu Tripo đổi cách giảm lưới; đợt 2 vẫn dùng nguyên quy tắc này.

### Tỉ lệ hình

```text
g = max(bounds.size.X, bounds.size.Z) / bounds.size.Y
i = rộng ảnh đã trim / cao ảnh đã trim
logRatio = log(g / i)
hình = shapeWeight * exp(-abs(logRatio) / shapeScale)
```

`shapeWeight = 25`, `shapeScale = 0,4`. Trùng tỉ lệ được 25 điểm; lệch hai lần còn khoảng 4,42 điểm. Lệch rộng/hẹp đối xứng theo log. Ảnh phối cảnh, vật nằm ngang, dáng nghiêng hoặc nền trim chưa sát có thể khiến thành phần này đánh lạc hướng. Không suy hướng từ tên file để sửa riêng từng trường hợp.

### Chữ

- Chuẩn hóa chữ thường, bỏ dấu Việt và đổi `đ` thành `d`; tách dấu `+`, `_`, `-` và các dấu khác. Bỏ số bản tải trùng, `3d`, `model`, hậu tố ảnh và một số từ chung như `stylized`, `fantasy`, `cartoon`.
- So từ tên GLB với phần id bỏ tiền tố game, tên Anh **cùng id và cùng game** trong `docs/games/NAMES_EN.md` nếu có, và nhãn Việt trong `INDEX.md`. INDEX nhận cả danh sách đợt 1 và bảng đường dẫn ảnh đợt 2; bỏ nhãn game ở cuối mô tả. Không tự nối tên của model cha vào phụ kiện.
- Đồng nghĩa dùng chung: wolf↔sói, bridge↔cầu, bamboo↔tre, feather↔lông, scaffold↔giàn, axe↔rìu, hat↔nón/mũ, cliff↔vách, waterfall↔thác; thêm một số từ vật liệu, đồ vật và màu. `băng đô` được gom thành `bandana`; `pinecone` tách thành `pine cone`. Không coi boar và piggy là cùng từ. Các nhóm như hat/helmet hoặc bow/crossbow chỉ là gần nghĩa cho bộ gợi ý và có thể gây nhầm.
- Mỗi từ chỉ tính một lần. Trọng số từ `wood` là 0,3; các từ khác là 1. `chữ = nameWeight × tổng trọng số từ truy vấn khớp / tổng trọng số từ truy vấn`, với `nameWeight = 60`. Không có từ truy vấn thì 0 điểm. Không dùng độ giống chuỗi con để đoán id.

### Ghép một-một

Xếp **tất cả cặp GLB–model** theo tổng điểm giảm dần. Chọn cặp cao nhất còn trống cả dòng GLB lẫn model, rồi khóa cả hai. Hòa điểm thì theo tên file, id, số thứ tự dòng. Không dùng chênh lệch top-1/top-2 làm độ chắc; không dùng thuật toán tối ưu tổng điểm.

Luôn giữ nguyên ba ứng viên trước ghép. `assigned` có thể nằm ngoài top-3, có điểm âm, hoặc là `null` khi hết model. Mỗi id chỉ được gán một lần, kể cả có nhiều ảnh góc. Đây là ràng buộc cứng: hai bản GLB của cùng mũ gatekeeper trong đợt 1 không thể cùng đúng; vẫn tính cả hai trong mẫu đo, không loại để tăng độ đúng.

## Kiểm và đo lại

Node v24.22.0 trên máy này không nhận thư mục test làm điểm vào: `node --test tools/tripo-match/test` báo `MODULE_NOT_FOUND`. Lệnh chạy được bộ test:

```sh
node --test tools/tripo-match/test/*.test.mjs
```

18 test không cần media, ImageMagick hoặc mạng; tạo GLB JSON/BIN và ma trận điểm trong RAM, không ghi file. Có kiểm từng thành phần điểm, parser nhãn/tên, ràng buộc ghép, dữ liệu GLB, CLI và định dạng đầu ra.

Đo lại trên đáp án đợt 1; hàm `evaluate` độc lập với bộ chấm, không đưa đáp án vào xếp hạng:

```sh
node --input-type=module - <<'JS'
import { readFile } from 'node:fs/promises';
import { runMatch, parseAnswers, evaluate } from './tools/tripo-match/match.mjs';
const result = await runMatch({ upload: 'typing-game-handoff-2026-10-25/tripo-upload' });
const answers = parseAnswers(await readFile('docs/games/3D_IMPORT_2026-10-26.md', 'utf8'));
const m = evaluate(result, answers);
for (const [label, key] of [['Top-1', 'top1'], ['Top-3', 'top3'], ['Một-một', 'assigned']]) {
  console.log(`${label}: ${m[key]}/${m.total} (${(100 * m[key] / m.total).toFixed(2)}%)`);
}
console.log('Thiếu GLB:', m.missingFiles, 'Không có đáp án:', m.unlabelledFiles);
console.table(m.details.filter(d => !d.top1Correct || !d.top3Correct || !d.assignedCorrect));
JS
```

Kết quả ngày 28/10/2026: **top-1 38/55 (69,09%), top-3 51/55 (92,73%), một-một 44/55 (80,00%)**. Đạt hai đích của phiếu, chưa thay được duyệt bằng mắt. Đợt 2 có 86 GLB, chạy xong thoát 0; chưa có bảng đáp án để chấm độ đúng. Chi tiết sai và năm kiểm nằm trong [`045-report.md`](../../docs/codex-queue/045-report.md).

Mỗi lần chạy băm MD5 trước/sau mọi GLB và mọi ảnh góc được chọn vào bộ ứng viên, kể cả góc không dùng đo. Không tạo snapshot trên đĩa. Phiếu còn đối chiếu riêng toàn bộ 304 GLB/PNG trong hai cây upload trước/sau phiên; không file nào đổi.
