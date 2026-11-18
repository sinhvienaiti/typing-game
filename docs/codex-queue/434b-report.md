# Phiếu 434b — Sét dây chuyền trong không gian 3D

Ngày 17/11/2026. **Đã sửa và qua kiểm kiểu/probe CPU; chưa nghiệm thu hình, alpha mây và p95 GPU.**

## Phạm vi và cách sửa

Chỉ ghi bốn tệp trong worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all` và báo cáo này:

- `src/lab/thunder-ult-chain.ts`: giữ đường gọi phím 8/showcase hiện có; sửa công thức mây, nhảy sét, cú đánh lớn và dư điện.
- `src/lab/thunder-ult-chain-space.ts`: mesh mây, ánh tím trên đất, decal cháy và pool tia tiết diện tròn trong không gian thật.
- `src/lab/thunder-ult-chain-probe.mjs`: probe CPU chạy riêng, không thuộc bộ test game.
- `src/lab/thunder-ult-chain-capture.mjs`: scenario chụp và đo dành cho Claude trên host worktree có sẵn.

Theo phiếu Sonnet PASS và `VFX_STANDARD`, dùng `game-vfx-production`/`game-vfx-layered`: tái dùng thư viện thành phần, không tạo ảnh, video hoặc âm mới. Mesh răng cưa là phương án được phiếu chỉ định. Đã xem phân cảnh nửa phải `ult-storyboard-samples-431.jpg` và sheet `typing-game-review/owner-review/2026-11-17/tu-tien/thunder-chain-r1.jpg`.

| Thành phần | Thay đổi |
|---|---|
| Mây | Bảy lát mesh cong nhẹ, nằm ngang ở 10,05–13,84 m; một draw instanced. Lấy hình và chuyển động từ `thunder-five-cloud-ink-wg`, các lớp lệch pha; chớp nội bộ và lóe theo các mốc 0,18/0,42/1,12/1,62/2,0 s. Không xoay theo camera. |
| Đặt mây | Fit một lần theo camera chơi 16:9, bao mesh mục tiêu 74%, chừa khoảng 24 px trên đầu. Khi cần, thu chiều sâu xuống 7,5 m và dịch khối về nửa gần của đàn quái. Probe công khai cả `targetCentre` và `centre`, không giấu phép dịch. Các camera khác xem cùng khối này. |
| Ánh xuống đất | Một mặt phẳng ngang y = 0,035 m dùng lại atlas mây, trộn tím theo nhịp; không thêm PointLight làm đổi shader của quái. |
| Dây chuyền | Tối đa 14 bước, 0,6–1,9 s, cách nhau 0,1 s. Tia rộng 0,38 m, giữ 0,22 s rồi mờ 0,14 s; 18 đoạn răng cưa, ba nhánh phụ mỗi bước. Các đoạn là mesh tiết diện tám cạnh, có lõi trắng và thân tím; không dùng hướng ngang màn hình để dựng bề rộng. |
| Sét lớn | Bỏ `thunder-pillar-single-narrow`. Thân mesh rộng 1,3 m từ vùng trong đáy mây y = 10,15 m đến đất y = 0,08 m tại mục tiêu cuối/cụm thay thế. Tám nhánh chính bám đúng đường răng cưa của thân, kết thúc trên đất, mỗi nhánh có thêm một chạc nhỏ. Lóe cục bộ đúng 2/60 s; giữ thân 0,24 s rồi mờ. |
| Điểm đánh | Giữ `thunder-big-burst` và sparkle; thêm `thunder-ground-mark` trên mesh nằm ngang 12 × 10 m, nguội và tan đến 3,5 s. Không còn dùng billboard làm vết cháy. |
| Dư âm | Tối đa tám quái sống, năm nhịp từ 2,45 đến 3,25 s, mỗi nhịp 0,2 s: lingering atlas, sparkle và các tia 3D nhỏ; tổng cửa sổ một giây. Mây tan 2,4–3,5 s, tất cả pool sạch ở 3,5 s. |

Giữ nguyên âm và đường hit/số sát thương có sẵn. Bỏ lời gọi camera zoom 0,68 tại cú chót vì nó cắt mây khỏi khung; không sửa `ult-camera-punch.ts`. Không sửa `skills-main.ts`, mã game chính, sim, content, shader mây của phiếu 438 hay tài liệu game. Không đổi nhánh, stage, commit, push hoặc chạy build/bộ test game.

## Kết quả đã kiểm

Strict và `noUncheckedIndexedAccess`, lấy nguyên options trong `tsconfig.json`:

- Module của phiếu và dependency: **0 diagnostic**.
- Tích hợp `skills-main.ts` cùng `stress.ts`, đúng hai module trang stress tải: **0 diagnostic**.
- Nếu chỉ đưa `skills-main.ts` vào chương trình mà bỏ `stress.ts`, có TS2339 ở `cloud-volume-lab.ts:69` vì thiếu khai báo `window.__stress` của trang stress. Không sửa tệp làn khác; kiểm đủ ngữ cảnh trang thì hết lỗi.
- `node --check` scenario chụp: đạt. Không có lỗi khoảng trắng trong các tệp mới.

Probe dùng `fitCamera` thật: tilt 55°, FOV 28°, khoảng cách 53,5085 m, targetZ −4,1896; fixture lưới **100 mục tiêu CPU**, không giả nhận đó là 100 model đã render. Đọc metadata/kiểm atlas trên đĩa; riêng TextureLoader được thay bằng texture CPU, không upload GPU.

| Phép kiểm | Kết quả |
|---|---|
| Mây, 1280 × 720 | Tâm `(≈0; 11,9; −3,9964)` m; tâm đàn fixture `(≈0; 11,9; −9,8)` m. Rộng 28,144 m, sâu 7,5 m; độ cao 10,05–13,84 m. |
| Bao mesh mây | x = 167,64–1114,84 px; y = 24,21–274,93 px; ngang **74,00%**, nằm trọn khung. Đây là bao hình học, **chưa phải diện tích/độ phủ alpha nhìn thấy**. |
| Tia nhảy | **14** mục tiêu khác nhau; đúng nearest-neighbour từng bước, không lặp; **9,12–10,99 px** đường kính hình học trước bloom/mặt nạ chữ; rộng 0,38 m; giữ **0,22 s**, ba nhánh phụ. |
| Cú lớn | Đúng 2,0 s; rộng **1,3 m ≈ 35,96 px** trong fixture; **tám** nhánh chính, khoảng cách hai đầu **3,28–5,70 m**. |
| Lóe | Thuộc tính flash bật tại 2,000 và 2,01667 s, tắt ở 2,03333 s. Chưa đo vùng trắng bằng pixel GPU. |
| Dư âm | Tám quái, **40** lần phát nhỏ trên cửa sổ 2,45–3,45 s. |
| Vòng đời | Không drop; **live = 0 sau update tổng 4 s**. Năm vòng hủy lúc 2,2 s rồi tung lại đủ 4 s không tăng tài nguyên. |
| Tài nguyên | 14 Object3D, 12 geometry, 12 material ổn định; tám atlas chỉ nạp một lần; dispose đủ tám texture, dispose lặp an toàn. |
| Đổi camera | Matrix instance mây giữ nguyên khi chuyển từ camera chơi sang camera sau lưng; bản probe camera chơi cũng giữ nguyên. Không quay hoặc fit lại hình học sang màn hình mới. |
| Bước thời gian/mục tiêu ít | `update(4)` cho cùng thứ tự mục tiêu; không quái thì không tạo cú trúng giả; ba quái thì đánh ba, không lặp. |

Chạy lại, từ đúng worktree:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
node --import tsx src/lab/thunder-ult-chain-probe.mjs
node --check src/lab/thunder-ult-chain-capture.mjs
node --input-type=module <<'JS'
import ts from './node_modules/typescript/lib/typescript.js';
import assert from 'node:assert/strict';
const config = ts.readConfigFile('tsconfig.json', ts.sys.readFile);
assert.equal(config.error, undefined);
const options = ts.parseJsonConfigFileContent(config.config, ts.sys, process.cwd()).options;
for (const files of [
  ['src/lab/thunder-ult-chain.ts', 'src/lab/thunder-ult-chain-space.ts'],
  ['src/lab/skills-main.ts', 'src/lab/stress.ts'],
]) {
  const ds = ts.getPreEmitDiagnostics(ts.createProgram(files, options));
  console.log(ts.formatDiagnosticsWithColorAndContext(ds, {
    getCanonicalFileName: x => x, getCurrentDirectory: () => process.cwd(), getNewLine: () => '\n',
  }));
  assert.equal(ds.length, 0); console.log('PASS: ' + files.join(', '));
}
JS
```

## Claude cần chụp và đo

**p95 100 quái: CHƯA ĐO.** Phiên này thấy listener 3146 bằng `lsof`, nhưng `curl --max-time 3 http://127.0.0.1:3146/stress.html` trả lỗi 7, không kết nối được từ sandbox. Không khởi động server hoặc tìm cách vượt sandbox. Chưa có ảnh/clip sau sửa, chưa chấm 8,5 và chưa thể xác nhận độ phủ alpha ≥60%, vùng trắng, đọc chữ hoặc biên hình ở camera sau lưng.

Scenario có sẵn chụp 0,4/1,2/2,2/3,0 s ở:

- `play`: camera chơi 55°, đúng fit hiện tại;
- `top`: cùng khung thời gian, redraw orbit 82° từ 100 m, không tiến timeline;
- `behind`: camera sau lưng `viewMode('behind')` thật của lab, đã chờ hết chuyển góc trước khi tung.

Mây được fit theo camera chơi; ở góc sau lưng thấp, phần trên có thể nằm ngoài FOV một cách vật lý. Cần xem ảnh để quyết định có cần thay cách đóng khung camera sau lưng ở phiếu riêng; không dựng mây giả quay về mắt để lấp chỗ này.

Đo 240 frame toàn cảnh bằng `__lab.perf(1)`, có GPU fence qua `readPixels`, High/DPR 1/1280×720. Population đầu lượt là 87 TargetField + 13 walker tạo tải render. Gọi `__lab.showcase('ult-thunder-nine-heavens-v2')`; không gọi `__stress.cast()` vì đó là Ngũ Lôi. `pass` của JSON đòi GPU thật, p95 ≤16,7 ms, pool sạch sau 240 frame và không gặp các lỗi shader/asset được runner ghi nhận; vẫn cần đọc toàn bộ log. Các cổng hình/alpha chưa được `pass` này chứng nhận.

```sh
export TG_ROOT=/Volumes/SS990TPRO/htdocs/typing-game
export REVIEW_ROOT=/Volumes/SS990TPRO/htdocs/typing-game-review
export RUN_DAY=$(date +%Y-%m-%d)
export RUN_ID=$(date +%H%M%S)
export OUT="$REVIEW_ROOT/captures/tu-tien/434b-thunder-chain-$RUN_ID"
export BASE=http://127.0.0.1:3146/stress.html
cd "$TG_ROOT/games/.wt-ic-lab-all"
"$TG_ROOT/.local/bin/heavy.sh" --gpu node src/kit/tools/cdp-run.mjs src/lab/thunder-ult-chain-capture.mjs --width=1280 --height=720 --dpr=1
ffmpeg -y -framerate 30 -i "$OUT/frames/f%04d.jpg" -t 4 -c:v libx264 -pix_fmt yuv420p -crf 18 "$OUT/434b-thunder-chain-4s.mp4"
for ANGLE in play top behind; do
  /opt/homebrew/bin/magick montage -font /System/Library/Fonts/Supplemental/Arial.ttf -pointsize 20 -fill white -background '#11151c' -label '0.4 s' "$OUT/434b-$ANGLE-0.4s.png" -label '1.2 s' "$OUT/434b-$ANGLE-1.2s.png" -label '2.2 s' "$OUT/434b-$ANGLE-2.2s.png" -label '3.0 s' "$OUT/434b-$ANGLE-3.0s.png" -tile 2x2 -geometry 640x360+4+4 "$OUT/434b-$ANGLE-phases.jpg"
done
export OWNER_OUT="$REVIEW_ROOT/owner-review/$RUN_DAY/tu-tien/434b-thunder-chain-$RUN_ID"
mkdir -p "$OWNER_OUT"
cp "$OUT/ABOUT.md" "$OWNER_OUT/ABOUT.md"
ln "$OUT/434b-thunder-chain-4s.mp4" "$OUT/434b-play-phases.jpg" "$OUT/434b-top-phases.jpg" "$OUT/434b-behind-phases.jpg" "$OUT/434b-stress.json" "$OWNER_OUT/"
cd "$TG_ROOT"
node tools/capture-prune/prune.mjs "$OUT/frames" --min-age-min 0
node tools/capture-prune/prune.mjs "$OUT/frames" --min-age-min 0 --apply
node scripts/review-index.mjs
```

Clip từ lệnh trên chưa có âm; nghe âm hiện có trực tiếp trong lab nếu cần đánh giá phối âm. Claude cần xác nhận bằng ảnh/video: mây thực sự nhìn thấy ≥60% ngang, ánh tím dưới mây, từng bước sét đọc được, thân sét nối mây xuống đất, tám nhánh tỏa, vết cháy phẳng và dư điện còn rõ ở 3,0 s. Hai giám khảo ≥8,5 và owner duyệt vẫn còn chờ; không gán PASS hình từ probe CPU.
