# Báo cáo phiếu 387a · 16/11/2026

**Mã và kiểm tự động đã xong; kiểm hình bản build còn chờ do sandbox.** Không ghi Git. Chưa chốt nghiệm thu hình ảnh.

## Đã làm

- Sân 48 × 52 m, lưới 96 × 104 ô; hai cổng ở miệng đường, lối trời mới, hai trụ và sáu ô đúng tọa độ phiếu. Giữ nguyên dữ liệu đợt và `liveCap`.
- Lane 12 m dùng 51 điểm Catmull–Rom ghi cứng, bước 0,1, làm tròn 10 mm, không trùng liền kề. Phép chiếu và khoảng cách trong sim dùng mm nguyên, `mulDivSym`; bằng ngưỡng vẫn mở, đoạn dài 0 được bỏ qua.
- `blockedCells` bắt buộc truyền `{ lane }`: thú bật, người chơi tắt. Mọi ô mở của flow tới được tim; lưới người chơi có 9.940 ô tới được, gồm mọi ô cơ quan và Tâm nhãn.
- Strip 0/2 có `alongPm` tính bằng `unitPm` lúc dựng stage; sim và view dùng cùng hướng. Khoảng cách tâm strip tới polyline đều 2,24 mm. Hướng lần lượt (−265; 965) và (559; 831) ‰. Stage thiếu hướng vẫn dùng ô → tim.
- Tốc độ theo phiếu, gồm Hỏa Nha 3.000 mm/s. `approachMs` 10–16 s, sàn 8 s. Các fixture/test tốc độ và tọa độ cũ được sửa theo thay đổi này; test director tạo áp lực từ đầu để kiểm nhánh giảm nhịp, vì đường mới có đoạn mở đầu chưa có thú gần tim.
- Camera mặc định B: 42°, FOV 28°, 52,8 m, look z −7,55; khung dọc cố định theo mọi aspect. Giữ chữ ký `CameraFit` và tùy chọn góc hiện có, không sửa bốn góc nhìn/lab.
- Vẽ đường và screen zones lấy cùng `stage.field.lane.pointsMm`, nửa rộng 6 m; stage không có lane giữ hành lang cũ. Cổng view gộp ở (0; −43,5).
- `edge-pan.ts`: bước tính thuần và adapter DOM; dải 24 px, đọc rect Bàn Quyết thật; trễ 0,15 s, tăng tốc 0,15 s, dừng 0,12 s bằng tích phân damp mũ; chéo chuẩn hóa, kẹp x ±4 và z −16,8…−7,55; giữ vị trí khi buông. Tốc độ 12 m/s, reduced motion 6 m/s, kể cả khi đổi tùy chọn lúc đang trượt.
- App cập nhật camera trước các presenter chiếu DOM, khóa pan theo menu/Settings/Shop/pause/kết thúc; rời cửa sổ và blur dừng ngay, không đụng focus hay phím. `CameraZoom` chia sẻ gốc pan, công bố mức zoom/framing để khóa pan, `reset()`/toggle về toàn khung trả look về nhà trong 0,35 s. App chơi hiện chưa dùng `CameraZoom` hay cut-in; lớp zoom đang được dùng trong lab, không thêm điều khiển lab trong phiếu này.

## Kiểm

- `npm test -- --maxWorkers=4`: **992/992 test xanh**, gồm boundary, tính nguyên, replay/hash và test mới lane/pan/khung.
- `npm run typecheck`: package hiện **không có script này**. Chạy trực tiếp TypeScript của game: `tsc --noEmit -p games/immortality-cultivation/tsconfig.json`: **xanh**. Không sửa package ngoài phạm vi.
- Vite production build: **xanh**, tại `.local/captures/387a/build/`; dùng `publicDir: false` để không sao chép toàn bộ media hoặc ghi đè `dist` của agent khác. Máy chủ kiểm chuẩn bị sẵn đọc media gốc từ `public` và dữ liệu từ `shared`.
- `git diff --check`: xanh. Không sửa `media.md5` vốn có thay đổi từ trước.
- Test mới kiểm mọi điểm đường/cổng tới tim, mọi ô mở có flow, đường A/B lệch ≤5%, route ±3%, waypoint và hành trình hai thú trong lane, strip ≤2 m, sky route ±1%, thời gian từng loài Nhỏ và cả swarm, clearance/bằng ngưỡng, đoạn trùng, pan/kẹp/trễ/panel/zoom/cut-in/reduced motion, tính nhất quán 30/60/144 Hz, liên kết reset của zoom.

### Số đo từ chính mã game (chưa phải ảnh chụp host)

| Đại lượng | Kết quả |
| --- | --- |
| Route ô cổng A → mép tim r 2 m | 41.308,483 mm |
| Route ô cổng B → mép tim r 2 m | 41.308,483 mm |
| Hằng `routeMm` | 41.308 mm; sai lệch 0,0012%, A/B bằng nhau |
| Lối trời → tâm | 50.119,850 mm; hằng 50.120 mm |
| Thạch Thử A/B → mép Kết Giới | 11.516,7 ms |
| Phong Lang A/B → mép Kết Giới | 13.300 ms |
| Hỏa Nha → mép Kết Giới | 13.716,7 ms; test kiểm cả hai lối trời |
| Tâm nhãn y, 1920 × 1080 / 1280 × 720 | 880,065 / 586,710 px |
| Trận Tâm y, 1920 × 1080 / 1280 × 720 | 771,866 / 514,577 px |
| Quái 1,5 m tại z −31, 1080p / 720p | 41,893 / 27,929 px |
| Mép trên tại kẹp bắc | z −44,0082 m ở cả hai kích thước |

Hai trụ, cả chân lẫn đỉnh, và sáu tâm ô nằm trong khung. Test chiếu dải đường xác nhận không xuống vùng Bàn Quyết y ≥930 tại 1080p. Cần ảnh host để xác nhận HUD/DOM thực tế.

### Hash vàng, cập nhật có chủ ý

Trong `tests/sim/twin-pearl.test.ts`, kịch bản cờ thử nghiệm tắt, lấy mỗi 300 tick; hậu tố là số thú sống:

| Seed | Cũ | Mới |
| --- | --- | --- |
| 5 | `844c012d@22` | `2231db6c@23` |
| 5 | `1cb00f08@36` | `96141749@35` |
| 5 | `527f8f69@58` | `9a5257a5@55` |
| 5 | `7b865d13@35` | `28755f54@43` |
| 9 | `aa8ae3cc@23` | `a82ff7c4@21` |
| 9 | `4ba2160f@38` | `73c2b707@34` |
| 9 | `753240f5@56` | `578f0f34@52` |
| 9 | `29c48d76@34` | `2b8c358d@35` |

Lý do: hình học, vị trí sinh, hướng strip và tốc độ là thay đổi sim đã duyệt. Pan chỉ nằm ở view, không được đưa vào world/hash. Script `ic:golden:update` hiện là stub; cập nhật đúng golden đang được suite sử dụng, không sửa script stub.

## Tệp đã đổi

Trong `games/immortality-cultivation/`:

- `src/content/types.ts`, `src/content/rules.ts`, `src/content/data/{stage-m0a,beasts,boss}.ts`.
- `src/sim/{field,mechanisms}.ts`, `src/local/nav.ts`, `src/ui/screen-zones.ts`.
- `src/view/{edge-pan,renderer,camera-zoom,ground,stage}.ts`, `src/app/app.ts`.
- `tests/content/{rules,stage}.test.ts`; `tests/local/fakes.ts`, `tests/local/map1-lane.test.ts` mới.
- `tests/sim/{beasts-stage,beasts,boss,core-director,core-field,core-heart-distance,elites,formation,mechanisms,pressure,twin-pearl}.test.ts`.
- `tests/ui/screen-zones.test.ts`; `tests/view/{actors,camera-zoom,edge-pan,impostor,renderer,stage}.test.ts`; `edge-pan.test.ts` mới.

Ngoài game: báo cáo này và `.local/captures/387a/{ABOUT.md,checks.json,measurements.json,measure.ts,serve.mjs,build/}`. `measure.ts` chạy bằng `node --import ./games/immortality-cultivation/node_modules/tsx/dist/loader.mjs .local/captures/387a/measure.ts` (CLI tsx tự mở IPC pipe nên bị sandbox từ chối).

## Chưa làm và việc cần chủ dự án/Claude xem

1. **Capture bản build bị chặn:** mở preview `127.0.0.1:3039` trả `listen EPERM`. Không có máy chủ nào của phiếu còn chạy. Nginx hiện trỏ tới `games/immortality-cultivation/dist`, một build khác; không ghi đè build đó hoặc dùng ảnh cũ làm chứng cứ. Môi trường cần cho phép chạy `node .local/captures/387a/serve.mjs`, hoặc Claude phục vụ thư mục build này.
2. Vì vậy chưa có bốn ảnh nhà/bắc ở 1920 × 1080 và 1280 × 720, chưa có ghép `lane-w12.png | ảnh chơi | chồng 50%`, chưa kiểm trực quan focus/overlay trên host. Không có khung thô được tạo, nên không có khung của tôi cần prune. `ABOUT.md` đã có; Claude chuyển chứng cứ sang review folder và dựng lại index khi có ảnh.
3. Impostor dùng `bakeImpostorAtlas` **nướng trong trang lúc tạo crowd**, đọc `CAMERA.defaultTiltDeg`; lần mở trang mới tự nướng ở 42°. Không có atlas bền trên đĩa được crowd hiện tại dùng cần ghi lại. Chưa quan sát lần nướng trên GPU do capture bị chặn.
4. Chưa làm 387b (ảnh/mặt đất/váy đất) hoặc 387c (đợt và liveCap); không sửa Ngũ Lôi, mã lab, script hay docs của game. Chưa chấm đạt thị giác; cần kiểm host và ảnh trước khi đóng 387a.

## Nghiệm thu kỹ thuật của Claude (16/11)

- Chạy lại: `vitest` 992/992 xanh; `tsc --noEmit` sạch.
- Chụp bản build `.local/captures/387a/build` (phục vụ bằng `serve.mjs`, `?prelearn=0&review=0`, 35 WPM) ở 1920 × 1080 và 1280 × 720: `typing-game-review/captures/tu-tien/map1-lane-build/387a/` và tấm ghép `387a-sheet.jpg`. Thấy: đường chữ S sáng hơn nền, hai Trận Trụ, Tâm nhãn ngay trên Bàn Quyết, thú đợt 1 ra ở mép trên; rê chuột lên mép trên trượt camera tới kẹp bắc, buông thì đứng yên.
- Ghi chú (không chặn): thú đi gần thẳng giữa đường (đúng như lời giải sửa); nền ngoài x ±24 còn màu xám trơn (387b làm váy đất).
- **387a nghiệm thu kỹ thuật: ĐẠT.** Hình chưa chấm 8,5 (chờ 387b mặt đất và anh xem). 387b, 387c được chạy tiếp.
