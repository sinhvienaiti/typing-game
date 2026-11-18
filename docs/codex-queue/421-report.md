# Phiếu 421 — nối 17 flipbook bùng nổ -v2 vào lab

Ngày 16/11/2026. **Hoàn tất phần nối và nghiệm thu CPU: 17/17 bộ nạp được, strict 0 lỗi.** Chưa chạy GPU/chụp hình; phía dưới có lệnh để Claude chụp lưới trên sân lab ở camera chơi 55° và ghép **cũ | mới**.

## Tệp đã làm

- `games/.wt-ic-lab-all/src/lab/burst-v2.ts`: bảng ánh xạ 17 bộ, đọc JSON riêng, bộ đặt thẻ/pivot, điều khiển so sánh và hàm dựng lưới.
- `games/.wt-ic-lab-all/src/lab/pilot-overrides.ts`: **đổi đúng một dòng**, gọi động sang `burst-v2.ts` sau bộ biến đổi pilot hiện có; giữ trace/status và `?pilot=1`.
- Báo cáo này: `docs/codex-queue/421-report.md`.

**Bật mặc định.** `?burst=old` giữ nguyên nguồn cũ; **Alt+B** đổi giữa hai chế độ bằng tải lại URL, giữ các tham số và hash khác. Phím không chạy khi đang nhập vào input/select/textarea/contenteditable hoặc đang composition. Tải lại để bỏ toàn bộ thẻ cũ, không trộn hai nguồn đang sống.

Tên pool/role cũ được giữ để caller tiếp tục hoạt động; đường dẫn atlas đổi sang `-v2`. Riêng **`style-w2-fire-qi-burst` → `fire-big-burst-v2`** vì manifest Hỏa hiện dùng tên W2 cho vai trò burst. Không thay `fire-burst` dùng cho release/impact hiện tại. Hai tên mới `fire-impact`, `metal-impact` được thêm khi bật v2; ở chế độ old chúng tiếp tục không tồn tại, không lấy clip khác để giả làm bản cũ.

| Nguồn -v2 | Khóa pool hiện tại | Khung / fps | Thời lượng |
| --- | --- | --- | --- |
| fire-impact-v2 | fire-impact, mới | 32 / 12 | 2,667 s |
| fire-big-burst-v2 | style-w2-fire-qi-burst | 32 / 24 | 1,333 s |
| earth-ring-burst-v2 | earth-ring-burst | 32 / 12 | 2,667 s |
| metal-impact-v2 | metal-impact, mới | 32 / 12 | 2,667 s |
| metal-big-burst-v2 | metal-big-burst | 32 / 24 | 1,333 s |
| void-big-burst-v2 | void-big-burst | 32 / 24 | 1,333 s |
| wind-ring-burst-v2 | wind-ring-burst | 32 / 24 | 1,333 s |
| dark-ring-burst-v2 | dark-ring-burst | 32 / 12 | 2,667 s |
| water-ring-burst-v2 | water-ring-burst | 28 / 24 | 1,167 s |
| poison-big-burst-v2 | poison-big-burst | 32 / 12 | 2,667 s |
| poison-ring-burst-v2 | poison-ring-burst | 32 / 12 | 2,667 s |
| blood-big-burst-v2 | blood-big-burst | 32 / 12 | 2,667 s |
| wood-big-burst-v2 | wood-big-burst | 32 / 24 | 1,333 s |
| dark-big-burst-white-v2 | dark-big-burst-white | 32 / 24 | 1,333 s |
| dark-ground-impact-white-v2 | dark-ground-impact-white | 32 / 12 | 2,667 s |
| thunder-impact-v2 | thunder-impact | 32 / 24 | 1,333 s |
| star-ring-burst-v2 | star-ring-burst | 32 / 12 | 2,667 s |

## Đặt thẻ và thời gian

- Đọc `frames`, `fps`, `cell`, `pivot`, `channels`, `blend`, `role`, `trim.tailFade` trực tiếp từ JSON mới. Không mang hash, motion map, video hoặc timing cũ sang nguồn mới. Có đường KTX2 UASTC mới và PNG dự phòng.
- Cả 17 atlas đã được bake tail fade **10 khung** theo JSON của phiếu 419/420. Playback giữ alpha 1 và erosion 0 để không fade hai lần; one-shot phát đủ đoạn ở fps mới, không bị `life`, tốc độ hoặc fade cũ cắt mất đuôi. Giữ đường scrub `ONE_FRAME` và khung do caller chọn.
- Mười bộ 55° của phiếu 420, cộng hai vòng Thổ/Gió, dùng thẻ quay theo trục Y. Pivot nằm ở mặt đất; phần trên dựng đứng, phần dưới pivot trải trên đất. Có hàng đỉnh đúng tại pivot để điểm chạm không bị nội suy nâng lên. Bù phép chiếu giữ tỷ lệ ảnh và hình bầu dục gốc; không chuẩn hóa vòng thành tròn, không áp `layFlat` lần nữa. Bỏ vận tốc/quay của caller cũ đối với các thẻ chạm đất này.
- Hai bộ khói trắng dùng đúng shader RGBA và màu nguồn, thay cho shader/tint density khói tối cũ. Atlas additive có occlude 0. Không sửa màu art.
- Không tạo thêm pool trong phần thay nguồn; constructor, capacity, giới hạn thẻ sống và cơ chế drop khi đầy giữ nguyên. Hàm chụp dùng API `__lab.clip` sẵn có.

## Kết quả kiểm

**PASS:** TypeScript Compiler API với cấu hình strict của worktree, hai root là file thêm/sửa, 425 tệp trong đồ thị phụ thuộc, **0 chẩn đoán**. Có `noUncheckedIndexedAccess`; không chạy build hoặc test suite game.

**PASS:** probe CPU dùng `FlipbookLibrary`, watch, loader và `FlipbookPool` thật. Chỉ thay lớp giải mã ảnh bằng texture rỗng trong bộ probe; mỗi đường ảnh phải tồn tại trên đĩa. Không mở HTTP server hoặc dùng GPU.

- Nạp đủ **17 JSON + 17 PNG** qua luồng library; kiểm thêm **17 đường KTX2** tồn tại. Không có đường thiếu/cảnh báo; mỗi JSON v2 chỉ được yêu cầu một lần dù biến đổi nhiều lượt.
- Khung/fps/pivot/aspect/thời lượng khớp JSON cả 17 bộ; kiểm riêng Thủy 28 khung. Giữ nguyên metadata của các clip ngoài danh sách.
- Thẻ đất có hàng UV tại pivot, anchor y=0, không quay/spin; phép đặt đỉnh CPU tại 55° giữ hình chiếu và không có đỉnh dưới đất. Kiểm hook được khôi phục nếu caller gọi `layFlat` sau attach.
- Life ngắn/tốc độ cũ không cắt tail. Kiểm khung cuối, scrub `ONE_FRAME`, shader RGBA/màu khói trắng và không sửa object options của caller.
- Thử capacity 3: ba thẻ sống, thẻ thứ tư bị drop; không cắt thẻ đang sống. Pool ngoài danh sách vẫn giữ life cũ.
- Probe tích hợp qua **dòng nối thật**: `?burst=old` trả đúng metadata cũ hoặc trạng thái thiếu cũ của cả 17 khóa, **0 request JSON v2**. Chạy riêng `?pilot=1`: đủ 17 v2 và vẫn nạp nguồn pilot Hỏa/Huyết, 0 cảnh báo.
- URL đổi qua lại giữ tham số khác; lưới có 17 vị trí riêng. Kiểm whitespace sạch.

Các script kiểm cục bộ và JSON kết quả nằm tại `/private/tmp/421-burst-{strict.mjs,v2-probe.mjs,v2-probe.json,integration.mjs}`. Chạy lại:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
node /private/tmp/421-burst-strict.mjs
node --import ./games/.wt-ic-lab-all/node_modules/tsx/dist/loader.mjs /private/tmp/421-burst-v2-probe.mjs
node --import ./games/.wt-ic-lab-all/node_modules/tsx/dist/loader.mjs /private/tmp/421-burst-integration.mjs '?burst=old'
node --import ./games/.wt-ic-lab-all/node_modules/tsx/dist/loader.mjs /private/tmp/421-burst-integration.mjs '?pilot=1'
```

## Lệnh chụp cho Claude

Chạy ngoài sandbox, với dev host của **worktree `games/.wt-ic-lab-all`** đã mở. Đổi `BASE` nếu cổng khác 3068; không trỏ vào host game chính. Scenario dưới giữ camera chơi 55°, dùng thời gian fixed, giữ 10 ảnh mốc cần cho báo cáo mỗi chế độ, không tạo chuỗi khung thô. Đầu ra là thư mục owner-review; `ABOUT.md` có sẵn trong script.

```sh
cat > /private/tmp/421-burst-capture.mjs <<'JS'
import { mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
export default async function (page) {
  const out = process.env.OUT_DIR;
  if (!out) throw new Error('OUT_DIR is required');
  mkdirSync(out, { recursive: true });
  writeFileSync(join(out, 'ABOUT.md'), 'purpose: So sánh lưới 17 burst cũ và v2 ở 55°\nmade-by: Claude, lệnh phiếu 421\ndoc: docs/codex-queue/421-report.md\ndelete-when: Owner đã xem và chấm xong\n');
  const checked = async code => {
    const value = await page.eval(code);
    if (value?.evalError) throw new Error(value.evalError);
    return value;
  };
  for (const mode of ['old', 'v2']) {
    const url = new URL(process.env.BASE ?? 'http://127.0.0.1:3068/skills-lab.html');
    for (const [k, v] of Object.entries({ fixed: '1', ui: '0', dpr: '1', video: '0' })) url.searchParams.set(k, v);
    if (mode === 'old') url.searchParams.set('burst', 'old');
    else url.searchParams.delete('burst');
    await page.goto(url.href);
    let ready = false;
    for (let i = 0; i < 240; i++) {
      if (await checked('!!(window.__lab?.ready && window.__burstV2)')) { ready = true; break; }
      await page.sleep(250);
    }
    if (!ready) throw new Error('Lab did not become ready');
    await checked("window.__lab.reset(); window.__lab.camera('play')");
    await checked('window.__burstV2.grid()');
    await checked('window.__lab.tick(0)');
    await checked('window.__lab.reset()');
    const rows = await checked('window.__burstV2.grid()');
    const missing = rows.filter(row => !row.played).map(row => row.key);
    const expected = mode === 'old' ? ['fire-impact', 'metal-impact'] : [];
    if (JSON.stringify(missing) !== JSON.stringify(expected)) throw new Error('Unexpected missing clips: ' + missing);
    writeFileSync(join(out, mode + '-rows.json'), JSON.stringify(rows, null, 2));
    await checked('window.__lab.tick(0)');
    let previous = 0;
    for (const tick of [0, 6, 12, 24, 48, 72, 96, 120, 144, 160]) {
      await checked(`window.__lab.step(${tick - previous})`);
      await page.shot(join(out, mode + '-' + String(tick).padStart(3, '0') + '.jpg'));
      previous = tick;
    }
  }
  if (page.exceptions.length) throw new Error(JSON.stringify(page.exceptions));
  return { out, clips: 17, layout: '5x4, BURST_V2 order, three empty cells' };
}
JS

cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3068/skills-lab.html \
OUT_DIR=/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/burst-v2-lab \
/Volumes/SS990TPRO/htdocs/typing-game/.local/bin/heavy.sh --gpu \
node src/kit/tools/cdp-run.mjs /private/tmp/421-burst-capture.mjs --width=1920 --height=1080 --dpr=1

cd /Volumes/SS990TPRO/htdocs/typing-game
BURST_OUT=/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/burst-v2-lab
for tick in 000 006 012 024 048 072 096 120 144 160; do
  /opt/homebrew/bin/magick "$BURST_OUT/old-$tick.jpg" "$BURST_OUT/v2-$tick.jpg" +append "$BURST_OUT/old-v2-$tick.jpg"
done
node scripts/review-index.mjs
```

Lưới 5 cột × 4 hàng theo đúng thứ tự bảng ánh xạ; ba ô cuối rỗng. File `*-rows.json` ghi tên và tọa độ từng ô. Các ảnh ghép luôn cũ bên trái, mới bên phải. Có thể gọi trực tiếp `await window.__burstV2.grid()` trong console sau `__lab.ready`; `window.__burstV2.rows` là chú giải.

## Bỏ qua và phần owner cần xem

Không bỏ bộ nào. Không tạo media, không sửa manifest/art, không sửa `src/view/`, `skills-main.ts`, game chính, `*-ult-*` hoặc `anim-*`; không chạy build/test suite, không đổi nhánh, không stage/commit/push/reset/clean/stash. Giữ các thay đổi đang có của tác nhân khác. Quota lúc nhận phiếu còn **23%**, trên ngưỡng 15%; làm một luồng, không gọi subagent/dịch vụ AI.

Chưa chạy lệnh chụp/GPU và chưa chấm hình tổng hợp 8,5: phiếu yêu cầu để lệnh chụp cho Claude. Owner/coordinator cần xem điểm chạm và kích thước ở camera thật, hai lớp khói trắng, các đoạn 24 fps ngắn hơn, và độ rõ của vòng Thổ/Gió khi bỏ cách đặt phẳng cũ. Kiểm thêm orbit để thấy thẻ chỉ quay theo trục đứng. Hai impact mới để trống trong nửa cũ là đúng dữ liệu, không phải lỗi nạp.
