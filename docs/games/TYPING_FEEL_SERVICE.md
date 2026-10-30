# Typing Feel: âm phím và hiệu ứng gõ dùng chung cho mọi game (30/10/2026)

> **Trạng thái:** bản thiết kế, **chờ chủ dự án duyệt** (mục 10). Chưa sửa code nào.
>
> **Chủ dự án yêu cầu (30/10):**
> - Thêm bộ âm phím không cần code: upload một file âm gốc đúng định dạng, bấm nút xử lý, bộ âm vào danh sách trong trang quản trị, mọi game nhận.
> - Âm phím và hiệu ứng gõ thành **một hệ thống chung**, game gọi tới, không mỗi game giữ một bản (luật sửa ở đầu `docs/games/DEPLOY_INDEPENDENCE.md`).
> - "Về trang quản trị, chúng ta đã có sẵn rồi, bạn chỉ cần dựa vào nó, xử lý lại để gom các setting chung và cấu trúc lại nó cho phù hợp." Vì vậy **không làm admin mới**: sửa Portal Admin V2.
> - Cách xử lý âm chủ dự án chọn ngày 30/10 (bản A, "natural"): giữ đuôi tự nhiên của mỗi cú gõ.
>
> **Nguồn:** ba đề xuất độc lập (nạp lúc chạy; cấu trúc lại Admin; vận hành và chuyển đổi) và hai giám khảo chấm theo mã hiện tại. Tài liệu này lấy các lựa chọn giám khảo chấm tốt nhất. Chỗ các đề xuất khác nhau được chốt ở mục 2.3. Mọi dòng mã trích dưới đây đã đọc lại ngày 30/10.
>
> **Phản biện độc lập (30/10, tối):** đã đối chiếu từng chỗ với mã. Các chỗ sai hoặc thiếu đã sửa thẳng trong bài. Chỗ lớn nhất:
> - Dragonhold, Wordwoven và Monkeytype **không** lưu `typingFx`. Chỉ Last Line dùng dải chữ và hiệu ứng chữ của kit (mục 4.5).
> - Bỏ module `feedback` khỏi game sẽ làm hỏng Dragonhold và Last Line. Chỉ bỏ `feedback/typing-fx` (B8).
> - Route xem trước không token không đặt được dưới `/api/admin/`, vì server chặn token trước mọi handler (mục 3.12).
> - Luật cũ "đỉnh phải dưới −0,1 dBFS, không thì chặn" sẽ chặn chính file Hail Stone chủ dự án đã chọn (mục 3.8).
> - OGG ghi lại không ra đúng byte (mục 3.9).
> - Từ 17:30 ngày 30/10 có bộ thứ 34, Hail Stone, được chép tay vào cả bốn nơi; Monkeytype còn chưa commit (mục 7, B0).
> - Có ba câu hỏi mới cho chủ dự án (mục 10, câu 15–17).

---

## 1. Tóm tắt một trang

### Cái gì đổi với chủ dự án

- **Một chỗ duy nhất để quản lý âm phím và hiệu ứng gõ:** Admin, khu **All games → Typing Feel**. Đây là trang Admin đang có. Hôm nay nó ở `https://typing-game.local/admin/space-typing`; sau khi sửa, nó ở `https://typing-game.local/admin`. Trang được chia lại thành hai khu: **All games** (dùng chung) và **Space Typing** (giữ nguyên như hôm nay).
  - Dịch vụ Admin chạy bằng `pnpm dev:admin` (hoặc `pnpm dev`). `pnpm play` không bật nó; game vẫn chơi được khi Admin tắt.
- **Thêm một bộ âm, không cần code:**
  1. Vào **All games → Keyboard Sounds → Add sound set**.
  2. Upload file WAV từ Adobe Firefly (định dạng ở mục 3.8). Admin kiểm ngay và báo lỗi rõ nếu file không đạt.
  3. Bấm **Format**. Admin chạy đúng cách xử lý bản A chủ dự án đã chọn.
  4. Nghe **A/B**: bản cắt thô và bản đã xử lý, ở 70 WPM. Chấm điểm.
  5. Đặt tên, chọn họ (family), bấm **Add to draft**.
  6. Bấm **Review**, xem "affects all games", rồi **Publish to all games**.
- **Sau Publish:** mọi game trên máy nhà nhận bộ mới **ở lần tải trang sau**, không build lại game nào. Bản online nhận sau khi chủ dự án chạy `pnpm feel:deploy` (khi đã có Cloudflare).
- **Sửa được trong thư viện:** đổi tên, đổi họ, đổi thứ tự, ẩn, chọn bộ mặc định, xử lý lại, cho nghỉ hẳn (retire). Mọi sửa đều vào bản nháp (Draft), chỉ có hiệu lực khi Publish, và lùi lại được (Rollback).
- **Mặc định hiệu ứng gõ** (kiểu chữ, cường độ, cỡ, âm lượng phím) cũng đặt ở cùng khu. Nó chỉ áp cho người chơi mở game lần đầu, khi save của game chưa có phần cài đặt này.
  - Hôm nay chỉ hai nơi có hiệu ứng chữ: Last Line (dải chữ của kit) và Monkeytype (lớp hiệu ứng riêng `fx-layer.ts`).
  - Dragonhold và Wordwoven chỉ dùng âm phím của kit, chưa có hiệu ứng chữ. Có đưa hiệu ứng chữ vào hai game này không là câu 15 ở mục 10.

### Mỗi game làm gì

- Đọc danh mục bộ âm từ **một chỗ**: `https://feel.typing-game.local/v1/keys/` trên máy nhà, sau này `https://feel.<tên-miền>/v1/keys/`.
- Không còn chép âm vào game. Hôm nay có **bốn bản sao** của bộ âm, cộng bản gốc ở `~/AudioLab/review/staging/keys-firefly/` (khoảng 27 MB, khoảng 2.780 file):
  - ba nhánh game chưa merge, mỗi nhánh 2.744 dòng `audio/keys` trong `media.md5`;
  - 22 MB trong Monkeytype.
- Ngày 30/10, 17:30, có thêm bộ thứ 34 là **Hail Stone**. Thêm một bộ đã phải sửa tay và commit riêng ở bốn repo (ba nhánh game đã xong tối 30/10, Monkeytype còn dở). Đây đúng là việc thiết kế này bỏ đi. Sau khi chuyển: **một bản**.
- Lựa chọn của người chơi vẫn lưu trong save của từng game (mỗi nguồn web một bộ nhớ riêng). Mỗi game lưu theo trường riêng (mục 4.5).
- **Không tải được Typing Feel thì game vẫn chơi** (luật 6): danh sách chỉ còn Off và âm gốc của game (Relay, Dragonhold, Bamboo, click của Monkeytype), kèm dòng "Keyboard sounds unavailable". Bộ người chơi đã chọn **không bị xoá**.

### Hai bước lớn

1. **Dữ liệu trước (bây giờ):** Typing Feel phục vụ danh mục và file âm. Mỗi game chỉ đổi chỗ đọc. Kit gần như không đổi. Trong bước này code âm phím và hiệu ứng gõ **vẫn được chép vào từng game** qua `kit:sync`. Điều 8 mới (không chép kit âm và hiệu ứng gõ) chỉ đủ sau bước 2.
2. **Code sau (sau bản demo):** code hiệu ứng gõ và âm phím chuyển thành **một module chạy chung** trên cùng host. Game chỉ giữ một bộ nạp nhỏ. Sửa hiệu ứng thì deploy Typing Feel một lần, mọi game nhận.

### Không đổi

- Space Typing không dùng kit, giữ Admin và âm của riêng nó. Nó chưa có bộ âm phím; tham gia sau hay không là câu 16 ở mục 10.
- Admin vẫn chỉ chạy trên máy nhà (D1). Admin chỉ publish **dữ liệu**, không bao giờ publish code.
- Media không vào Git: OGG và WAV lên Drive qua `media.md5`.

---

## 2. Kiến trúc

### 2.1 Bước dữ liệu

```
 MÁY NHÀ CHỦ DỰ ÁN (Admin chỉ chạy ở đây)
 ┌────────────────────────────────────────────────────────────────────────┐
 │  WAV Firefly ──upload──▶ Portal Admin V2  https://typing-game.local/admin │
 │                          All games → Typing Feel                       │
 │                           │  Format: bash tools/audio-lab/run.sh keys natural │
 │                           │  Media V2: bản bất biến, blob theo sha256      │
 │                           │  TypingFeelRevisionStore: Draft → Publish → Rollback │
 │                           ▼  Publish = xuất file tĩnh                     │
 │   typing-feel/public/v1/keys/                                          │
 │     keys-manifest.json                (Git)                            │
 │     sets/<id>/<fp12>/keys-manifest.json (Git)                          │
 │     sets/<id>/<fp12>/*.ogg            (media.md5 + Drive, không Git)    │
 └──────────────┬─────────────────────────────────┬──────────────────────┘
                │ nginx alias (máy nhà)           │ pnpm feel:deploy (online, sau)
                ▼                                 ▼
   https://feel.typing-game.local/v1/     https://feel.<tên-miền>/v1/
     danh mục: no-cache · sets/<id>/<fp12>/: immutable · CORS *
        │             │              │              │
        ▼             ▼              ▼              ▼
    Last Line     Dragonhold     Wordwoven      Monkeytype     (game sau này)
    survival.     dragon.        td.            monkeytype.
    Mỗi game: VITE_TYPING_FEEL_ORIGIN lúc build · lưu lựa chọn trong save riêng
    Hỏng → Off + âm gốc, game vẫn chơi
```

### 2.2 Bước code (sau demo)

```
   feel.<host>/v1/typing-feel.js   (no-cache, ETag → 304)     một file ES module, build từ Git
   feel.<host>/r/<build>/typing-feel.js  (immutable)          để ghim và lùi
   feel.<host>/v1/next/typing-feel.js                         bản ứng viên, chỉ để duyệt
          ▲ import() lúc chạy, cùng JS realm, không iframe, không postMessage
          │
   game: src/kit/typing-feel-client/  (index.ts, load-feel.ts, v1.d.ts, fake.ts)  ← chép bằng kit:sync
         từ shared/game-kit/typing-feel-client/; chỉ đổi khi hợp đồng đổi
   Monkeytype: chép tay 4 file đó, có PROVENANCE.md, như cách chép kit hôm nay
```

### 2.3 Chỗ các đề xuất khác nhau và cách chốt

| # | Chỗ khác nhau | Chốt | Vì sao |
|---|---|---|---|
| 1 | Máy nhà đọc âm từ route của admin server (`/api/runtime/typing-feel/`) hay file tĩnh | **File tĩnh qua nginx** | `scripts/play.sh` không chạy admin. Admin tắt thì local Play mất âm phím. Admin không được nằm trên đường của người chơi. Route `/api/runtime/typing-feel/` chỉ dùng để xem trước nháp trong chính Admin (mục 3.12). |
| 2 | Kết quả Publish nằm ở `.deploy/typing-feel`, `.local/admin/shared/.../export` hay `typing-feel/public/v1/keys/` | **`typing-feel/public/v1/keys/`**: JSON vào Git, OGG lên Drive | Clone mới dựng lại được. Có tiền lệ: `admin/music-assets.mjs` ghi vào `games/space-typing/public/assets/audio/music`. Chủ dự án duyệt ở mục 10, câu 4. |
| 3 | Một kho Media V2 hay thêm một kho thứ hai cho khu dùng chung | **Một kho**, lọc theo khu | Gom chứ không tách. Cần dời khoá ghi vào `MediaAssetStore` (mục 3.6). |
| 4 | Chuyển code và dữ liệu cùng lúc, hay dữ liệu trước | **Dữ liệu trước**, code sau demo | `loadKeyboardCatalog(base)` đã nhận URL khác host. Rủi ro thấp, đang giai đoạn ổn định demo. |
| 5 | Thời gian chờ 5 s hay 3 s cộng 4 s | **3 s** cho danh mục và module. Cổng vào trận chờ âm tối đa **1,5 s**. Khởi động **không bao giờ** chờ Typing Feel. | Mở game một mình phải nhanh (luật 6). |
| 6 | Dấu vân tay thư mục bộ âm dài 8 hay 12 ký tự hex | **12** | Đường dẫn dài hơn 4 ký tự, gần như không trùng. |
| 7 | Bản online giữ thư mục bộ âm của 5 hay 10 bản Publish gần nhất | **10** | Thư mục theo nội dung, bộ không đổi thì dùng chung, nên rẻ. |
| 8 | Quyền `typing-feel.publish` hay `shared.publish` | **`shared.publish`** | Một quyền cho cả khu All games, dùng lại cho hệ chung sau này. Mục 10, câu 9. |
| 9 | Kiểu chữ hiệu ứng là dữ liệu Admin hay code | **Code** (trong module chung) | Kiểu chữ mới cần code vẽ, dữ liệu không tạo được. Khi code đã chung thì vẫn chỉ deploy một lần. |
| 10 | Mặc định riêng theo game | **Chưa làm** | Chưa ai cần. Âm riêng của game (Relay, Bamboo…) vẫn ở code game qua `extra`. |
| 11 | Overlay 1.162 dòng của Monkeytype (`fx-layer.ts`) chuyển vào module ngay | **Thêm sau, trong v1** (thêm, không phá) | Giảm cỡ hợp đồng đầu tiên. |

---

## 3. Trang quản trị: cấu trúc lại Portal Admin V2

### 3.1 Hôm nay (đọc mã 30/10)

- **Vỏ (shell)** là một file, `portal/src/admin/space-typing.ts` (412 dòng): `ADMIN_BASE = "/admin/space-typing"` ở dòng 36, `NAV_GROUPS` ở dòng 40, chữ "Command Center" ở dòng 269, breadcrumb ở dòng 360.
  - `normalizedAdminPath` (dòng 183) là chỗ duy nhất **đổi đường** (hôm nay chỉ `/flags` → `/feature-gates`).
  - `NAV_ALIASES` (dòng 124) **chỉ làm sáng** mục điều hướng cho trang con, không đổi đường. `renderPage` (dòng 391) chọn trang theo đúng đường.
  - Roles & Permissions hôm nay nằm trong nhóm System (dòng 108).
- Portal chỉ định tuyến `/admin/space-typing/*` (`portal/src/main.ts:664`). Nút "Space Admin" ở `main.ts:450`.
- **Server** `admin/server.mjs` nghe `127.0.0.1:3199`. Nó đọc 13 file hợp đồng Space ngay khi khởi động (dòng 48–60), nên thiếu submodule Space thì server không chạy. Thư mục dữ liệu `.local/admin/space-typing` (dòng 61), hiện 136 KB, không có bản sao lưu.
- **Mọi đường `/api/admin/*` phải có token** (`x-typing-game-admin-token`, kiểm ở dòng 184–187), và kiểm này chạy **trước** mọi handler. Chỉ `/api/runtime/space-typing/*` chạy trước bước kiểm token (dòng 160–177).
- Rollback của Space dùng quyền riêng `config.rollback` (`server.mjs:454`), không dùng `config.publish`.
- **Không có trang Audit riêng.** Nhật ký hiện trong History & Publish (`space-typing-history-phase-b.ts`) và Dashboard. API là `GET /api/admin/space-typing/audit`.
- **Typing Content** (`admin/typing-content-catalog.mjs`) đã đọc dữ liệu dùng chung của mọi game, chỉ đọc: `shared/vocabulary` và `shared/typing-texts`.
- **11 script kiểm** đọc thẳng `portal/src/admin/space-typing.ts` (ví dụ `scripts/validate-space-admin-v2-shell.mjs`). `scripts/validate-play-mode.mjs:311` đòi đúng chuỗi `location /api/admin/space-typing/`. Đổi tên vỏ hay đổi location nginx thì phải sửa các script này cùng lúc.
- **Vòng đời bản sửa:** `RevisionStore` (`admin/store.mjs:201`) có `createRevision` (339), `validateRevision` (321), `publish` kiểm `expectedActiveRevision` (362–366), `rollback` (386). Lời ghi seed cứng "Initial Space Typing Admin seed" (dòng 248).
- **Media V2** (`admin/media-assets-v2.mjs`): bản bất biến, blob theo sha256 (`blobs/`, dòng 237), `addReference` (459), `createUploadVersion` chỉ ghi một thành phần (332). Khoá ghi chỉ nằm trong closure của `createMediaV2HttpHandler` (`admin/media-http.mjs:101–106`).
- **Quyền** (`admin/admin-security.mjs`): `ADMIN_PERMISSIONS` (dòng 13), mẫu vai trò Super Admin và Publisher (53–54). Vai trò đặt cho cả server bằng `TYPING_GAME_ADMIN_ROLE` (dòng 132), nên vốn đã dùng chung cho mọi game. Nút bấm được chặn theo regex nhãn (`portal/src/admin/v2/security/permission-gates.ts:16–17`), trừ khi có `data-admin-permission` (dòng 22–34: thuộc tính thắng regex; dòng 90–121: thiếu quyền thì ẩn nút). Nhãn không khớp regex nào (ví dụ "Format", "Add to draft") thì nút không bị chặn ở giao diện.
- nginx của portal chỉ chuyển `/api/admin/space-typing/` sang 3199 (`infra/nginx/typing-game.local.play.conf:28`). `dev.conf` **không có** block này: ở chế độ dev, nginx chuyển hết sang Vite của portal (cổng 3100), và Vite chuyển cả `/api/admin` sang 3199 (`portal/vite.config.ts:17`).

### 3.2 Cấu trúc mới: một Admin, nhiều khu

Giữ vỏ và mọi thành phần V2. Chỉ đổi cách tổ chức:

- `NAV_GROUPS` chuyển vào `portal/src/admin/areas/space-typing.ts`, giữ nguyên mọi nhóm, trừ hai mục chuyển xuống Administration: Media Library (nhóm Media) và Roles & Permissions (nhóm System).
- Thêm `portal/src/admin/areas/shared.ts` và một danh sách khu `areas/registry.ts`. Mỗi khu khai `{ id, label, base, navGroups, renderPage }`.
- Phần vỏ của `space-typing.ts` đổi tên thành `portal/src/admin/admin-shell.ts` (cùng mã). Tên hiện: **Typing Game Admin**.
- Đầu thanh bên có **nút chọn khu**: `All games | Space Typing`. Chỉ liệt kê khu có thật (luật P12 của master plan: không route chết).
- Breadcrumb lấy tên khu: "All games / Keyboard Sounds", "Space Typing / Ships".
- `main.ts` định tuyến `/admin` và `/admin/*`. `/admin` mở **All games**. Nút portal "Space Admin" thành **"Admin"**.
- Mọi URL `/admin/space-typing/*` cũ vẫn chạy. Các trang Space giữ nguyên đường. Hai đường chuyển (`/admin/space-typing/media` → `/admin/media`, `/admin/space-typing/roles` → `/admin/roles`) đi qua một bảng chuyển đường trong `normalizedAdminPath`. Không dùng `NAV_ALIASES` cho việc này, vì nó chỉ làm sáng mục điều hướng.
- Bảng lệnh nhanh (`space-typing-command.ts`) thêm các mục của khu dùng chung.
- Cùng lần sửa này: cập nhật 11 script kiểm đang đọc `space-typing.ts` và kiểm location của `validate-play-mode.mjs` (mục 3.1). Xong khi mọi script đó xanh.
- Giữ nhận diện của P10 (giao diện tối kiểu chỉ huy, Exo 2 / Be Vietnam Pro) cho cả khu All games.

```
Typing Game Admin            LOCAL · CONNECTED          [ All games ▾ | Space Typing ]

ALL GAMES                    /admin/shared
  Overview                   /admin/shared                       bản Published đang chạy, máy nhà và online,
                                                                 nháp đang chờ, nhật ký gần đây, các game đang đọc Typing Feel
  TYPING FEEL
    Keyboard Sounds          /admin/shared/keyboard-sounds       (+ /new, /jobs/:id)
    Typing Effects           /admin/shared/typing-effects
    Release & History        /admin/shared/release
  (sau này, cùng kiểu nhóm: Character Animation, …)

SPACE TYPING                 /admin/space-typing                 giữ nguyên các nhóm hôm nay:
  Dashboard, Content, Gameplay, Economy, Players & Live Ops,
  Media (Music Library, SFX, World / Stage Music),
  System (Audio Defaults, General Settings, History & Publish), Developer Tools

ADMINISTRATION               hiện ở mọi khu, cuối thanh bên
  Media Library              /admin/media     một kho; chip lọc: All · Shared · Space Typing
  Roles & Permissions        /admin/roles
  Audit                      /admin/audit     trang mới; chỉ hiện khi đã làm xong (P12)
```

- **Audit** hôm nay chưa có trang riêng. Trang mới dùng `GET …/audit` có sẵn, lọc theo `domain` (`config`, `media`, `typing-feel`). Chưa làm xong thì không hiện trong điều hướng; nhật ký của khu dùng chung nằm trong Release & History.
- **Typing Content** (bảng từ vựng và bài gõ, chỉ đọc) đọc `shared/vocabulary` và `shared/typing-texts`, là dữ liệu chung của mọi game. Có thể chuyển sang All games với tên "Learning Content", đường cũ vẫn chạy. Chủ dự án quyết ở mục 10, câu 17.

**Cái gì chuyển, cái gì giữ:**

| Mục | Hôm nay | Sau |
|---|---|---|
| Âm phím, hiệu ứng gõ | không có trong Admin, nằm trong 4 game | All games → Typing Feel |
| Media Library | `/admin/space-typing/media` | Administration `/admin/media` (alias đường cũ) |
| Roles & Permissions | `/admin/space-typing/roles` | Administration `/admin/roles` (alias đường cũ) |
| Audio Defaults của Space (giọng đọc, announcer…) | System | **Giữ ở Space Typing**. Đây không phải Typing Feel. |
| Players, Live Ops, Developer Tools | Space | Giữ ở Space Typing |

**Khu từng game:**
- Space Typing là khu đầy đủ duy nhất, vì chỉ nó có cấu hình do Admin quản.
- Dragonhold, Wordwoven, Last Line, Monkeytype **chưa có khu riêng** (P12). Trang Overview của All games có một bảng "Games using Typing Feel": tên game, host, đã chuyển sang Typing Feel chưa, nút mở game. Chỉ đọc. Danh sách lấy từ `admin/typing-feel/consumers.json`.
- Khi một game có cấu hình riêng do Admin quản, nó thêm một khu vào `areas/registry.ts`, cùng khuôn.

### 3.3 Typing Feel có kho bản sửa riêng

- Thêm `admin/typing-feel/store.mjs`: `TypingFeelRevisionStore extends RevisionStore`.
  - Ghi đè `validateConfig` hoàn toàn, không gọi kiểm tra của Space.
  - Thêm tuỳ chọn `seedMessage` cho `RevisionStore` (thay chữ cứng ở `store.mjs:248`).
- Thư mục dữ liệu: `TYPING_GAME_ADMIN_SHARED_DIR`, mặc định `.local/admin/shared/typing-feel/` (`state.json`, `revisions/`, `jobs/`).
- Kế thừa nguyên Draft, Validate, Publish (`expectedActiveRevision`, cha phải là bản đang chạy) và Rollback.

**Vì sao không gộp vào cấu hình Space:** bản sửa Space là cả cấu hình, và chỉ Publish được khi cha là bản đang chạy. Gộp vào thì một bản nháp Space chặn việc Publish âm phím, và Rollback Space lùi luôn âm phím của mọi game. Như vậy phá luật 7 ("sửa Typing Feel chỉ deploy lại Typing Feel").

**Server không còn phụ thuộc Space để chạy khu dùng chung:** bọc mọi phần khởi động cần Space trong một khối có bắt lỗi:
- 13 hợp đồng (`server.mjs:48–60`);
- `SpaceTypingRevisionStore` và `store.initialize` (dòng 62, 66);
- `bootstrapMediaReferences` (dòng 68, đọc file trong `games/space-typing`);
- `MusicAssetService` (ghi vào `games/space-typing/public/assets/audio/music`).

Thiếu submodule Space thì các route cấu hình Space (`/api/admin/space-typing/*`, `/api/runtime/space-typing/*`) trả 503 và khu Space hiện "Space Typing is not checked out". **Trừ** Media V2: nó vẫn ở đường cũ `/api/admin/space-typing/media/*` (`media-http.mjs:7`) và `/api/runtime/space-typing/media/*`, và vẫn chạy. Khu All games cũng vẫn chạy.

**Mọi việc ghi của Typing Feel đi qua một hàng đợi** (Save draft, Accept, Publish, Rollback, xuất lại khi khởi động). `RevisionStore` không có khoá: hai lần Publish cùng lúc có thể cùng qua bước kiểm `expectedActiveRevision`.

### 3.4 Cấu hình một bản sửa (schema `typing-feel-admin/1`)

```json
{
  "schema": "typing-feel-admin/1",
  "contract": 1,
  "keyboard": {
    "defaultSet": "bright-clack",
    "families": [{ "id": "deep", "name": "Deep", "order": 0 }, { "id": "crisp", "name": "Crisp", "order": 4 }],
    "sets": [
      { "id": "raindrop-tile", "name": "Raindrop Tile", "family": "crisp", "order": 6, "enabled": true,
        "status": "published", "assetVersionId": "media-version.<uuid>", "ownerPick": true, "ownerScore": null,
        "recipe": "natural-v1", "note": "Owner pick 30/10, natural" }
    ],
    "retiredIds": []
  },
  "effects": { "defaults": { "style": "stamp", "intensity": "normal", "size": "large", "volume": 1 } }
}
```

- `ownerScore` chỉ ghi khi chủ dự án đã cho điểm. Không bịa điểm: Raindrop Tile và Hail Stone hôm nay có `ownerPick: true`, `score: null` (danh mục staging ghi rõ không chấm bằng điểm 218).
- `volume: 1` giữ đúng mặc định hôm nay của các game (Last Line `FX_DEFAULTS.volume` 1, Dragonhold 1, Wordwoven và Monkeytype 100 trên thang 100). Mức 0,7 của `DEFAULT_TYPING_FX` trong kit không game nào dùng.

**Luật kiểm (`admin/typing-feel/policy.mjs`):**
- `id` khớp regex của kit `^[a-z0-9][a-z0-9-]{0,31}$` (`audio.ts:546`), không trùng. **Đã Publish thì không đổi id**, vì save của người chơi ghi id. Đổi tên chỉ đổi `name`.
- Id trong `retiredIds` **không bao giờ dùng lại**, để save cũ không trỏ sang một âm khác.
- `defaultSet` phải đang bật và không phải `provisional`.
- Mọi `family` dùng tới phải có trong `families`.
- `assetVersionId` phải có trong Media V2, mang tag `typing-feel` và `keyboard-set`, và đủ thành phần: `manifest`, `preview`, **ít nhất 10** `key-NN` và **ít nhất 3** `space-NN` (mức `want` của `TYPING_SOUND_SET`, `audio.ts:44–47`). Bản mới thêm không được đến từ asset đã lưu trữ (archived).
- `effects.defaults` kiểm theo `typing-feel/contract/typing-feel.v1.json`. Một test của kit so file này với `TYPING_FX_STYLES`, `TYPING_FX_INTENSITIES`, `TYPING_FX_SIZES` (`settings.ts:7–15`), để hai nơi không lệch nhau.

**Phạm vi thay đổi (`change-scope.mjs`):** liệt kê bộ thêm, ẩn, retire, xử lý lại (đổi `assetVersionId`), đổi tên, đổi thứ tự, đổi họ, đổi mặc định, đổi mặc định hiệu ứng. Luôn ghi **affects: all games**. Bước Review hiện tóm tắt này với chip "Affects all games".

### 3.5 Seed ban đầu

- Lệnh một lần: `node admin/typing-feel/import-staging.mjs ~/AudioLab/review/staging/keys-firefly`.
- Nhập mọi bộ đang có ở staging thành bản Media V2 (tối 30/10 là 34 bộ). 32 bộ ticket 218 mang ghi chú nguồn "legacy-218, owner-kept 30/10". `raindrop-tile` và `hail-stone` giữ `ownerPick` và `note` của chúng.
- Mọi bộ nhập vào là `published`, vì game đang phát chúng. Cổng "từ 9 điểm" (mục 8.3) chỉ áp cho bộ mới thêm qua Admin.
- Ghi bản sửa `seed-v1`: họ và thứ tự như danh mục hôm nay, `defaultSet: "bright-clack"`, `effects.defaults` như mặc định hôm nay của game.
- **Tiêu chí:** danh mục xuất lần đầu trùng danh mục staging lúc nhập (`schema typing-keys-firefly/catalogue-2`, tối 30/10 là 34 dòng) về id, tên, họ, thứ tự. Chỉ khác đường dẫn.

### 3.6 Dùng lại Media V2

- **File gốc:** upload qua route có sẵn `POST /api/admin/space-typing/media/assets` với `x-media-kind: audio`, `x-media-tags: typing-feel,keyboard-source`. Không thêm route upload.
- **Bộ đã xử lý:** mỗi bộ là một asset (`kind audio`, tag `typing-feel,keyboard-set`). Mỗi lần Format được chấp nhận là **một bản bất biến** gồm nhiều thành phần: `key-01…`, `space-01…`, `preview`, `manifest`, `ab-raw`, `ab-natural`, `report`.
  - Thêm `createUploadBundleVersion({ assetId, components: [{ role, filename, mimeType, buffer, durationSeconds }], source })`. Hôm nay `createUploadVersion` chỉ ghi một thành phần.
  - Tên thành phần hợp `ROLE_PATTERN` có sẵn (`media-assets-v2.mjs:14`).
  - Nguồn gốc ghi vào trường `source` có sẵn (`normalizeSource`, dòng 86), không đổi schema: `generator: "typing-feel natural-v1 (tools/audio-lab keys natural @<git sha>)"`, `sourcePath: <assetVersionId của WAV gốc>`, `license: "Adobe Firefly Generate Sound Effects, generated by the project owner (Adobe model)"` (nhãn của ticket 217), `note`: tham số dạng JSON.
- **Tham chiếu:** mỗi lần Publish gọi `addReference` với `domain "typing-feel.keyboard"`, `entityType "keyboard-set"`, `entityId <setId>`, `field "assetVersionId"`, `revisionId`. Trường `field` là bắt buộc (`media-assets-v2.mjs:470`); thiếu thì `addReference` ném lỗi. Mỗi bộ có thêm tham chiếu `typing-feel.source` tới WAV gốc. Nhờ vậy xoá cứng bị từ chối, Rollback luôn tìm thấy file, Media Library hiện "used by".
- **Việc phải sửa trước:** dời khoá ghi từ closure `serializeMutation` (`media-http.mjs:101–106`) vào chính `MediaAssetStore`. Nếu không, một lần "Accept" của Typing Feel chạy cùng lúc với một upload sẽ làm mất một cập nhật của `registry.json`.
- **Cỡ:** 34 bộ, khoảng 83 thành phần mỗi bộ, tức khoảng 2.800 dòng, chừng 1 MB `registry.json`. Mỗi lần ghi, registry được đọc, kiểm và ghi lại cả file. Chấp nhận được trên máy nhà.
- Giữ đường Media V2 hiện tại (`.local/admin/space-typing/media-v2`). Đổi tên thư mục là việc riêng, sau.

### 3.7 Thư viện bộ âm (Keyboard Sounds)

- Thẻ xếp theo họ, theo thứ tự họ. Mỗi thẻ: tên, họ, nút ▶ nghe preview 1 s, số phím và số space, chip `Published`, `Draft change`, `Hidden`, `Default`, `Provisional`, `legacy-218`.
- Thao tác, tất cả chỉ sửa bản nháp:
  - **Rename** (đổi `name`, id giữ nguyên);
  - **Family** (đổi họ); thêm, đổi tên, sắp xếp họ;
  - **Move up / Move down** trong họ;
  - **Hide / Show** (`enabled`): bộ ẩn không có trong danh mục xuất; người chơi đang dùng nó được chuyển về bộ mặc định ở lần tải sau;
  - **Set as default** (một nút chọn);
  - **Retire** (ẩn vĩnh viễn, id vào `retiredIds`);
  - **Re-format** (xử lý lại từ cùng WAV gốc, ra bản mới).
- Thanh dưới: **Save draft → Review → Publish to all games**, như luật P05 (Edit → Save Draft → Validate → Preview → Review Change Scope → Publish).

### 3.8 Thêm bộ âm (`/admin/shared/keyboard-sounds/new`)

**Bước 1, Upload.** Trang ghi rõ định dạng yêu cầu (đề xuất, chủ dự án duyệt ở mục 10, câu 7):

| Mục | Yêu cầu | Không đạt thì |
|---|---|---|
| Tệp | WAV, PCM 16-bit, 24-bit hoặc float 32-bit | chặn |
| Tần số mẫu | 44,1 kHz hoặc 48 kHz | chặn |
| Kênh | mono hoặc stereo | chặn |
| Độ dài | 4–30 s | chặn |
| Cỡ | tối đa 50 MB | chặn |
| Đỉnh sát 0 dBFS, cú có mẫu vượt 0,99 | báo từng cú | **cảnh báo**, không bỏ cú nào (bản A giữ mọi cú chính) |
| Số cú dùng được | **ít nhất 12** cú chính (to trong vòng 25 dB so với cú to nhất), mỗi cú cách cú sau ít nhất 150 ms | chặn |
| Nền ồn | dưới −50 dBFS | cảnh báo |
| Nhịp gõ, cách thu | khoảng 2 cú mỗi giây; khô, gần mic, không nhạc nền (KEYS_FIREFLY_HANDOFF §5) | ghi chú |

- **Vì sao không chặn theo đỉnh:** bản thu Hail Stone v4 mà chủ dự án đã chọn có đỉnh −0,07 dBFS, và `hits-v4.json` đánh dấu một cú `clipped` (cờ này của `analyse.py` chỉ nghĩa là có mẫu vượt 0,99). Chặn ở −0,1 dBFS sẽ chặn chính file đó. Công thức đã chuẩn cả bộ về đỉnh −2 dBFS, nên đỉnh nguồn cao không hại.
- Upload tạo asset gốc. **Không đổi gì trong game.**
- Kiểm nhanh chạy ngay sau upload (`natural.py --check`), báo bằng câu rõ ràng, ví dụ: "Found 7 usable taps; need at least 12, each at least 150 ms before the next.", "Tap at 2.4 s reaches full scale; check it in the A/B.", "Sample rate 22.05 kHz; use 44.1 or 48 kHz."
- **Số đo trên file thật ngày 30/10** (WAV PCM 16-bit, 48 kHz, stereo, 8 s; cả ba đạt):

| File | Cú tìm được | Cú dùng được | Đỉnh | Nền ồn |
|---|---:|---:|---:|---:|
| `raindrop/src/raindrop.wav` | 22 | 17 | −1,76 dBFS | −90 dB |
| `hail/src/hail-v1.wav` | 52 | 22 | −0,03 dBFS, 1 cú vượt 0,99 | −66 dB |
| `hail/src/hail-v4.wav` (chủ dự án chọn) | 37 | 17 | −0,07 dBFS, 1 cú vượt 0,99 | −73 dB |

Đường dẫn trong bảng tính từ `tmp/keys-firefly/`. Cú tìm được và nền ồn lấy từ `hits*.json`; đỉnh đo bằng `ffmpeg astats`.

- **So nhiều bản thu** (như Hail Stone v1 và v4 ngày 30/10): upload từng file, Format từng file, nghe cạnh nhau, Accept bản được chọn, Discard bản kia.

**Bước 2, Format.** Công thức **Natural (owner pick, 30/10)**, tham số cố định (mục 3.9). Chưa cho sửa tham số. Trang hỏi trạng thái và hiện đuôi log.

**Bước 3, Listen A/B.**
- Ba trình phát: **Raw cut 70 WPM**, **Natural 70 WPM**, và **Currently published** khi đang thay một bộ.
  - "Raw cut" theo đúng bản cắt thô chủ dự án đã nghe: mỗi cú cắt 120 ms, chỉ cân độ to, không xử lý (`tmp/keys-firefly/raindrop/build.py`).
- Cân độ to giữa các bản. Nút lặp 20 lần (bài mỏi tai, SHARED_SYSTEMS_BAR §3).
- Nút **Blind**: ẩn nhãn và xáo thứ tự, để chủ dự án nghe mù như SHARED_SYSTEMS_BAR §2 yêu cầu.
- Preview 1 s. Lưới mọi phím và space, kèm độ dài.
- Cảnh báo từ `report.json`. Dưới mức tối thiểu (10 phím, 3 space) thì nút Accept bị khoá.
- Ô **Owner score** (0–10).
- Âm tải theo kiểu có sẵn: fetch có token rồi tạo object URL (`portal/src/admin/v2/media-api.ts`).

**Bước 4, Name it.** Id (cố định sau khi Publish), tên tiếng Anh, họ, giấy phép (điền sẵn). **Add to draft**: tạo bản Media V2, thêm dòng bộ vào nháp, quay về thư viện với chip "Draft change".

**Thay một bộ:** Re-format chạy job mới trên cùng WAV, ra bản mới. A/B so với bản đang Published. Trong nháp chỉ `assetVersionId` đổi. Đúng luật Media V2: thay là tạo bản mới và đổi tham chiếu rõ ràng.

### 3.9 Công thức Format `natural-v1`

Nâng `tmp/keys-firefly/raindrop/build2.py` **bản A** và `analyse.py` thành công cụ có test: `tools/audio-lab/keys/natural.py` và `tools/audio-lab/keys/onsets.py`. Lệnh là một nhánh mới `natural` trong `keys/pipeline.py` (các nhánh ở dòng 781 trở đi), chạy bằng `bash tools/audio-lab/run.sh keys natural …`. Bỏ bản B và C. `tmp/keys-firefly/hail/hail.py` (Hail Stone, 30/10) đã dùng đúng công thức này cho một nguồn khác, nên tham số cố định là hợp lý.

Đúng cách chủ dự án chọn ngày 30/10:
- Mỗi cú gõ lấy từ lúc chạm tới ngay trước cú sau, **tối đa 450 ms**: giữ đuôi tự nhiên và giọt nước rơi theo sau. Chỉ làm mờ 0,6 ms đầu và 25 ms cuối.
- **Giữ tiếng cao. Không EQ.**
- Thu hẹp chênh lệch độ to **một phần: 60%, tối đa 9 dB** (`even_out(amount=0.6, limit=9.0)`).
- Biến thể đến từ **các cú gõ thật**, không chép rồi đổi cao độ.
- **Space:** 8 cú chính có khoảng lặng phía sau dài nhất (đuôi dài nhất, `gapToNextMs`), **hạ 3 nửa cung**, nâng 1,5 dB.
- Ghi OGG Vorbis 48 kHz, cả bộ chuẩn đỉnh −2 dBFS. Preview 1 s: một đoạn gõ dựng từ chính bộ đó, **10 ms cuối mờ dần** (preview của Hail Stone dừng ở −51 dBFS không mờ, có thể kêu tách).
- **Không tự cắt phần dạo đầu.** Khi một cú gõ mở bằng tiếng tách nhỏ rồi tiếng chính mới tới, `report.json` liệt kê phím đó và độ trễ của tiếng chính, chủ dự án quyết. Ngày 31/10 chủ dự án giữ nguyên Hail Stone, dù 7/25 phím (04, 06, 12, 16, 20, 23, 25) và 4 space có tiếng chính tới sau 35–205 ms.
- Hạt ngẫu nhiên cố định (7 và 11, như build2) cho nhịp của bản nghe 70 WPM và preview.
- **Chạy lại ra cùng mẫu âm, không cùng byte OGG.** Đã thử ngày 30/10 trong venv Audio Lab: ghi cùng một mảng hai lần bằng `soundfile` (libsndfile) ra hai OGG khác md5, vì số serial của luồng Ogg là ngẫu nhiên. Vì vậy:
  - test so mẫu PCM (WAV trung gian hoặc OGG đã giải mã), không so md5 của OGG;
  - mỗi lần Format ra `<fp12>` mới, kể cả khi tham số không đổi. Không sao, vì thư mục theo nội dung và không bao giờ ghi đè;
  - `import-staging` lấy nguyên byte OGG ở staging, không mã hoá lại.
- **Không dùng** điểm của ticket 218 (`keys/firefly_v2*.py`): nó cắt và chuẩn hoá mạnh, và phạt đuôi dài. Chủ dự án thấy 32 bộ của nó nghe giống nhau.

Đầu ra mỗi job:
```
key-NN.ogg (tối đa 80) · space-NN.ogg · preview.ogg · keys-manifest.json (schema typing-feel/set-1)
ab/raw-cut.mp3 · ab/natural.mp3 · report.json
```
`report.json` gồm: số cú gõ, độ dài từng file, độ to, đỉnh thật, LUFS-M max, thời gian lên, năng lượng còn lại sau 120 ms, kết quả cổng cứng của bộ phê bình, cảnh báo.

**Chạy job (`admin/typing-feel/jobs.mjs`):**
- Một job một lúc, trên máy nhà.
- Trước khi chạy, kiểm venv Audio Lab (`~/AudioLab/.venv`) và ffmpeg. Thiếu thì báo: "Run `bash tools/audio-lab/common/setup.sh` on this machine." Đây là cùng lệnh `run.sh` đang chỉ (nó báo bằng tiếng Việt, mã thoát 2).
- Chép blob gốc ra `jobs/<id>/in/source.wav`. Python không chạm vào registry.
- `spawn("bash", ["tools/audio-lab/run.sh", "keys", "natural", "--src", src, "--out", out, …])`: tham số dạng mảng, không qua shell. `run.sh` đã chạy Python với `-I`.
- Hết giờ sau 180 s thì dừng. Job đang chạy khi server khởi động lại được đánh dấu `interrupted`.
- Trạng thái `queued | running | succeeded | failed | accepted | discarded` trong `jobs/<id>/job.json`.
- Dọn: job đã Accept xoá thư mục làm việc khi byte đã vào blob. Job lỗi hoặc bỏ được xoá sau 7 ngày.

### 3.10 Typing Effects (mặc định hiệu ứng)

- Mặc định kiểu chữ (`stamp`, `flare`, `smash`, `shatter`, `rune`, `minimal`), cường độ, cỡ, âm lượng phím. Bộ mặc định chỉ hiện và dẫn sang Keyboard Sounds, để nó ở một chỗ.
- Chỉ áp cho người chơi **chưa có save cài đặt** của game đó. Lựa chọn đã lưu luôn thắng.
  - Game lưu cả object cài đặt mỗi khi người chơi đổi bất kỳ mục nào (ví dụ Last Line lưu `typingFx` đầy đủ). Vì vậy người đã mở Settings một lần sẽ giữ mặc định của lúc đó, kể cả mục họ chưa tự đổi. Trang ghi rõ điều này.
  - Muốn mặc định mới đến cả người cũ chưa tự đổi thì game phải lưu thêm "mục nào người chơi đã chạm". Chưa làm.
- Hôm nay mặc định hiệu ứng chỉ có tác dụng ở **Last Line** (`typingFx`) và **Monkeytype** (`letterEffect`, `effectStrength`, `keyboardVolume` 0–100; không có cỡ chữ). Dragonhold và Wordwoven chỉ nhận bộ âm mặc định và âm lượng phím (mục 4.5).
- Xem trước: iframe của Typing Feedback Lab (`tools/typing-feedback-lab`), đã dùng dải chữ và bộ chọn âm của kit. Lab **đã nhận** `?keysBase=` (`src/profiles.ts:3`); thêm `&style=&intensity=&size=`.
  - Hôm nay Lab chỉ chạy bằng Vite dev, không cổng cố định, không có ở chế độ Play. Admin cần một bản build tĩnh của Lab, do admin server phục vụ ở `/api/runtime/typing-feel/lab/` (cùng nhóm route xem trước, mục 3.12).
  - Ở bước code, thay iframe bằng `mountEffectsPreview` của module thật.

### 3.11 Release & History

- Nháp, kết quả kiểm, phạm vi thay đổi, Publish, Rollback.
- Nhật ký của khu dùng chung.
- **Trạng thái triển khai**, bốn dòng:
  - Máy nhà đang chạy bản nào (đọc `typing-feel/public/v1/keys/keys-manifest.json`).
  - Danh mục đã commit chưa (so với `git status` của đúng thư mục đó, chỉ đọc).
  - OGG và WAV đã lên Drive chưa (`media:status` của nhóm typing-feel). Nút **Back up** đẩy hai nhóm runtime và originals của riêng `typing-feel`, chỉ file mới.
    - Hôm nay `media:push` **không có tuỳ chọn chọn game**: nó chạy cho mọi game đang có trên máy (`scripts/media/commands/push.mjs:406`). Chạy từ Admin như vậy sẽ đẩy cả media mới của game khác. Cần thêm `--game <id>` vào `scripts/media` trước. Khi chưa có, nút chỉ hiện lệnh để chủ dự án tự chạy.
    - Lệnh đích: `pnpm media:push --game typing-feel --only runtime,originals --new-only --yes`.
  - Online đang chạy bản nào (đọc `https://feel.<tên-miền>/v1/health.json` khi đã cấu hình).
- Admin **không bao giờ** chạy git commit hay push.

### 3.12 Server

Thư mục mới `admin/typing-feel/`: `store.mjs`, `policy.mjs`, `change-scope.mjs`, `jobs.mjs`, `export.mjs`, `http.mjs` (`createTypingFeelHttpHandler`, trả true hoặc false như `createMediaV2HttpHandler`), `consumers.json`, và test cùng kiểu `store.test.mjs`, `media-http.test.mjs`, `media-http-server-smoke.test.mjs`. `server.mjs` thêm hai dòng:
- `handleTypingFeelRuntimeRequest` **trước** bước kiểm token, cạnh `handleMediaRuntimeRequest` (dòng 160), cho các route xem trước `/api/runtime/typing-feel/…`;
- `handleTypingFeelRequest` sau `handleMediaV2Request`, cho các route `/api/admin/shared/typing-feel/…`.

Mọi route `/api/admin/…` cần token admin. Mọi thay đổi đi qua `runAuthorizedAdminMutation`, nên có nhật ký. Nhật ký dùng chung `LocalAdminAuditLog` có sẵn (`.local/admin/space-typing/`), `domain "typing-feel"`, tên hành động riêng (`typing-feel.publish`, `typing-feel.rollback`…), để Dashboard của Space không gộp nhầm với "Published changes".

| Route (`/api/admin/shared/typing-feel/…`) | Việc | Quyền |
|---|---|---|
| `GET state` | trạng thái, bản đang chạy, lịch sử | đọc |
| `GET capabilities` | có venv và ffmpeg chưa, công thức `["natural-v1"]`, giới hạn upload, đã cấu hình online chưa | đọc |
| `POST jobs` `{ sourceAssetVersionId, recipe, setId? }` | chạy Format, trả 202 `{ jobId }` | `media.upload` |
| `GET jobs/:id`, `GET jobs/:id/files/:name` | trạng thái, report, log, file để nghe | đọc |
| `POST jobs/:id/accept` `{ assetId?, title, licence, ownerScore }` | tạo bản Media V2; không đổi cấu hình | `media.upload` |
| `POST jobs/:id/discard` | bỏ job | `media.upload` |
| `POST revisions` | lưu nháp | `config.draft` |
| `POST validate-revision` | kiểm, phạm vi thay đổi, dựng bản xem trước | đọc |
| `POST publish` `{ revision, expectedActiveRevision }` | Publish | `shared.publish` |
| `POST rollback` `{ targetRevision, expectedActiveRevision }` | Rollback | `shared.publish` |
| `GET export/status` | máy nhà, commit, Drive, online | đọc |

| Route không token (`/api/runtime/typing-feel/…`) | Việc |
|---|---|
| `GET preview/<revision>/keys/…` | danh mục và file của một nháp **đã kiểm**, để xem trước. Chỉ đọc. |
| `GET lab/…` | bản build tĩnh của Typing Feedback Lab cho trang Typing Effects |

- Vì sao không token: `<audio>`, `fetch` của kit và iframe của Lab không gửi được header token. Route này không thể nằm dưới `/api/admin/`, vì server kiểm token cho mọi đường `/api/admin/` trước khi gọi handler (mục 3.1).
- Không cần lọc theo `127.0.0.1`: admin server vốn chỉ nghe `127.0.0.1`, và qua nginx mọi yêu cầu đều đến từ `127.0.0.1`. Âm của nháp không phải dữ liệu bí mật.

nginx và Vite:
- `play.conf`, server `typing-game.local`: đổi `location /api/admin/space-typing/` thành `location /api/admin/` (dòng 28), thêm `location /api/runtime/typing-feel/` cùng `proxy_pass http://127.0.0.1:3199`. Cả hai đặt trước fallback SPA. Sửa kiểm tương ứng ở `validate-play-mode.mjs:311`.
- `dev.conf`: không sửa, vì nó chuyển hết sang Vite của portal.
- `portal/vite.config.ts`: thêm proxy `/api/runtime/typing-feel` cạnh `/api/admin`.

**Publish làm theo thứ tự (`export.mjs`):**
1. Kiểm bản sửa.
2. Ghi **thư mục bộ âm mới** vào `typing-feel/public/v1/keys/sets/<id>/<fp12>/`. Không bao giờ ghi đè. Thư mục đã có thì so sha256 từng file, khác là lỗi.
3. So sha256 từng file với thành phần Media V2.
4. Ghi danh mục ra file tạm cạnh `keys-manifest.json`.
5. `store.publish({ revision, expectedActiveRevision })`. Lỗi thì xoá file tạm: không gì trong game đổi.
6. Đổi tên file tạm thành `keys-manifest.json` (nguyên tử), ghi `health.json`.
7. Thêm tham chiếu Media V2.

Khi server khởi động, nếu `revision` trong danh mục khác bản đang chạy thì xuất lại, và thêm lại tham chiếu Media V2 còn thiếu (trường hợp server dừng giữa bước 6 và 7). Rollback đi đúng đường này với cấu hình của bản đích. Publish lỗi ở bước 5 có thể để lại thư mục bộ âm mới chưa ai dùng; không sao, vì thư mục theo nội dung.

### 3.13 Quyền và bảo vệ

- **Thêm đúng một quyền:** `shared.publish`, nhãn "Publish shared settings to all games", **nguy hiểm**. Gồm Publish và Rollback của khu All games.
  - Thêm vào cả `ADMIN_PERMISSIONS` và `ADMIN_PERMISSION_CATALOG` (để trang Roles hiện nó).
  - Super Admin tự có (nhận mọi quyền, `admin-security.mjs:49`). Thêm vào mẫu Publisher.
  - Quyền `config.publish` của Space **không** đủ để Publish cho mọi game.
  - Space tách Publish (`config.publish`) và Rollback (`config.rollback`). Ở khu dùng chung đề xuất gộp: ai được đẩy ra mọi game thì cũng lùi được ngay khi hỏng (mục 10, câu 9).
- Nháp dùng lại `config.draft`. Upload, Format, Accept dùng lại `media.upload`: các bước này chỉ tạo media trong thư viện, không đổi gì trong game. Lưu trữ media dùng `media.delete` như hôm nay.
- **Mọi nút** của khu dùng chung mang `data-admin-permission` rõ ràng, không dựa vào regex nhãn:
  - Publish và Rollback: `shared.publish`. Thuộc tính này thắng regex `/^publish\b/` → `config.publish` và `/^roll back\b/` → `config.rollback` của `permission-gates.ts`.
  - Format, Accept, Discard: `media.upload`. "Add to draft", "Save draft": `config.draft`. Nhãn như "Format" không khớp regex nào, nên không có thuộc tính thì giao diện không chặn.
  - Thiếu quyền thì nút bị ẩn (cách `permission-gates.ts` xử lý thuộc tính này). Server vẫn kiểm lại mọi quyền (P09).
- Thêm nhãn nhật ký vào `humanAction` của `portal/src/admin/v2/dashboard.ts`.
- **Bảo vệ dữ liệu người chơi:** id cố định, `retiredIds` không dùng lại, bộ mặc định phải bật.
- **Bảo vệ file:** bản Media V2 bất biến, có tham chiếu thì không xoá cứng được, thư mục bộ âm không bao giờ bị ghi đè.
- **Bảo vệ game:** Admin chỉ publish dữ liệu đã kiểm (đường dẫn tương đối, id hợp lệ). Code chỉ đến từ Git (mục 5.6).

---

## 4. Hợp đồng v1

### 4.1 Luật phiên bản

- v1 gồm: URL, schema danh mục, schema bộ âm, trường save `typingFx`, và (từ bước code) các export của module.
- **Trong v1 chỉ được thêm**, không đổi tên, không bỏ. Game đọc v1 bỏ qua trường lạ (kit đã làm vậy).
- Thay đổi phá hợp đồng đi vào `/v2/`, phục vụ song song. `/v1/` giữ tới khi cả bốn game đã chuyển.

### 4.2 URL

| URL | Nội dung | Cache |
|---|---|---|
| `/v1/keys/keys-manifest.json` | danh mục (`typing-feel/catalogue-3`) | `no-cache` (ETag → 304) |
| `/v1/keys/sets/<id>/<fp12>/keys-manifest.json` | bộ âm (`typing-feel/set-1`) | `public, max-age=31536000, immutable` |
| `/v1/keys/sets/<id>/<fp12>/key-NN.ogg`, `space-NN.ogg`, `preview.ogg` | âm | immutable |
| `/v1/health.json` | `{ contract: 1, revision, build, builtAt }` | `no-cache` |
| `/v1/typing-feel.js` (bước code) | module ES một file, bản đang dùng | `no-cache` |
| `/v1/next/typing-feel.js` (bước code) | bản ứng viên, chỉ để duyệt | `no-cache` |
| `/r/<build>/typing-feel.js` (bước code) | bản cố định, để ghim và lùi | immutable |

- `<fp12>`: 12 ký tự hex đầu của `contentFingerprint` của bản Media V2 (`versionFingerprint`, `media-assets-v2.mjs:149`: băm nguồn gốc, sha256 từng thành phần và `source`). Byte đổi thì URL đổi.
- Không có fallback kiểu SPA: file thiếu trả **404**. Trả `index.html` mã 200 sẽ làm hỏng giải mã âm ("Unexpected token '<'", DEPLOY_INDEPENDENCE §3).
- Mọi đường gửi `Access-Control-Allow-Origin: *`, `Cross-Origin-Resource-Policy: cross-origin`, `X-Content-Type-Options: nosniff`. Không cookie.
- Bộ phân giải của kit nhận đúng các đường này: tương đối, không `/` đầu, không `..`, `:`, `?`, `#`, `%` (`audio.ts:531–535`).

### 4.3 Danh mục `typing-feel/catalogue-3`

Là **tập mở rộng chặt** của `catalogue-2` hôm nay, nên `loadKeyboardCatalog` hiện tại đọc được nguyên vẹn.

```json
{
  "schema": "typing-feel/catalogue-3",
  "contract": 1,
  "revision": "<id bản Published>",
  "publishedAt": "2026-11-02T09:00:00Z",
  "default": "bright-clack",
  "effects": { "style": "stamp", "intensity": "normal", "size": "large", "volume": 1 },
  "families": [{ "id": "crisp", "name": "Crisp", "order": 4 }],
  "profiles": [
    {
      "id": "raindrop-tile", "name": "Raindrop Tile",
      "family": "Crisp", "familyId": "crisp", "order": 19, "score": null, "ownerPick": true,
      "status": "published", "keys": 17, "spaces": 8,
      "manifest": "sets/raindrop-tile/3f2a9c1e7b44/keys-manifest.json",
      "preview": "sets/raindrop-tile/3f2a9c1e7b44/preview.ogg"
    }
  ]
}
```

- Trường kit đọc hôm nay: `id`, `name`, `family` (tên hiện làm tiêu đề họ), `score` (chỉ khi là số), `manifest`, `preview`, `order` (`audio.ts:546–553`). `manifest`, `preview` và `order` là **bắt buộc**: thiếu một trường thì kit bỏ dòng đó. `score` hôm nay là điểm máy của ticket 218 (khoảng 6), không phải điểm chủ dự án; không bộ chọn nào hiện nó.
- Bản xuất sắp theo thứ tự họ rồi thứ tự bộ, và ghi `order` liền nhau từ 0. Bộ cùng họ đứng liền nhau, nên bộ chọn của kit vẽ đúng một tiêu đề mỗi họ.
- Bộ ẩn và bộ đã retire **không có** trong danh mục.
- `status: "provisional"` chỉ để Admin và bộ chọn hiện nhãn. Game cũ bỏ qua.

### 4.4 Bộ âm `typing-feel/set-1` (bản rút gọn cho game)

```json
{
  "schema": "typing-feel/set-1",
  "id": "raindrop-tile", "name": "Raindrop Tile",
  "licence": "Adobe Firefly Generate Sound Effects, generated by the project owner (Adobe model)",
  "recipe": "natural-v1",
  "files": [
    { "file": "key-01.ogg", "set": "key", "durationMs": 450 },
    { "file": "space-01.ogg", "set": "space", "durationMs": 535 }
  ],
  "preview": "preview.ogg"
}
```

- `keyboardFiles` của kit lấy mọi chuỗi dạng `key-NN.<ext>` và `space-NN.<ext>` trong JSON (`audio.ts:75–102`), nên đọc được ngay.
- Số đo chi tiết ở lại `report.json` trong Admin, **không** lên game. Hôm nay ba game dùng kit tải bản đầy đủ của Audio Lab trước cú gõ đầu: `deep/keys-manifest.json` nặng **162.359 B**. Bản rút gọn khoảng 2 KB (`raindrop-tile` hôm nay 2,2 KB). Monkeytype đã dùng bản rút gọn (`deep` 1.664 B).

### 4.5 Save của người chơi

Không đổi chỗ lưu và tên trường. **Mỗi game lưu theo cách riêng** (đọc mã 30/10):

| Game | Trường trong save | Hiệu ứng chữ | Âm lượng phím | Mặc định bộ âm cứng ở đâu |
|---|---|---|---|---|
| Last Line | `typingFx` (`style`, `intensity`, `size`, `soundProfile`, `volume`), làm sạch bằng `sanitizeTypingFx(raw, FX_DEFAULTS)` | có (dải chữ của kit) | 0–1 | `src/app/settings.ts:16`, `FX_DEFAULTS` dòng 19 |
| Dragonhold | `keyboard`, `keyboardVolume` | không | 0–1 | `src/app/settings.ts:8` |
| Wordwoven | `keyboard`, `keyboardVolume` (`prefs.ts:13`) | không | 0–100 | `src/app/prefs.ts:19` |
| Monkeytype | `personalTypingFeelSettings`: `keyboardSound`, `keyboardVolume`, `letterEffect`, `effectStrength` (zod, `store.ts`) | có (`fx-layer.ts`), không có cỡ chữ | 0–100 | `store.ts:8` |

- `default` của danh mục thay mặc định bộ âm cứng của từng game (hôm nay cả bốn đều là `bright-clack`). `soundProfile: "creamy"` của `DEFAULT_TYPING_FX` trong kit (`settings.ts:31`) không game nào dùng.
- `effects` của danh mục chỉ dùng ở game có hiệu ứng chữ. Mỗi game tự đổi sang thang của nó (ví dụ `volume` 1 → 100 ở Wordwoven và Monkeytype).
- Danh mục về **sau** khi game đã đọc save. Game chỉ dùng mặc định của danh mục khi save chưa có trường đó, và chỉ ghi vào save khi `repaired` hoặc khi người chơi đổi (mục 3.10).

### 4.6 API bước dữ liệu (thêm vào kit, không phá)

```ts
// shared/game-kit/feedback/typing-fx/audio.ts: trường mới, đều tuỳ chọn
export type KeyboardCatalog = {
  readonly options: readonly KeyboardSoundChoice[];
  readonly state: "ready" | "missing" | "invalid";
  readonly revision?: string;
  readonly defaultId?: string;                          // catalogue.default
  readonly effects?: Partial<TypingFxSettings>;         // catalogue.effects
};

/** fetchJson có hạn giờ, truyền vào loadKeyboardCatalog(base, { fetchJson }). */
export function timedJson(timeoutMs?: number /* 3000 */): (url: string) => Promise<unknown>;

/**
 * Luật Wordwoven cho mọi game: danh mục không tải được thì GIỮ id đã lưu (hiện thành
 * "Saved sound · unavailable", disabled). Tải được mà thiếu id thì chuyển sang defaultId,
 * rồi bộ đầu tiên, rồi âm gốc của game; chỉ khi đó mới trả repaired: true để game lưu.
 */
export function settleKeyboardChoice(
  savedId: string,
  catalog: KeyboardCatalog,
  builtIn: KeyboardSoundChoice,
  fallbackDefault?: string,
): { readonly id: string; readonly options: readonly KeyboardSoundChoice[]; readonly repaired: boolean };

/** URL gốc từ biến build; thiếu biến thì null (tắt Typing Feel, game vẫn chơi). */
export function typingFeelKeysBase(origin: string | undefined): string | null;   // → `${origin}/v1/keys/`
```

Thêm vào `TypingSounds.load` (`audio.ts:297`): đợt giải mã đầu trộn **12 phím và 4 space**, thay vì mọi phím trước. Mỗi đợt 16 file (`KEYBOARD_DECODE_BATCH_SIZE`, `audio.ts:220`). Bộ của ticket 218 có 72–80 phím, nên hôm nay 4–5 đợt đầu chỉ có phím. Khi bộ chưa có space, `play()` phát tiếng phím thay tiếng space, nên hết từ đầu tiên nghe tiếng phím.

Muốn Admin sửa `default` và `effects` được, game phải đọc chúng từ danh mục. Đây là lý do `KeyboardCatalog` có thêm `defaultId` và `effects`.

### 4.7 API module chung (bước code)

Game chép `src/kit/typing-feel-client/` qua `scripts/sync-game-kit.mjs` (khai `"typing-feel-client"` trong `kit.config.json`).
- `sync-game-kit` chỉ chép thư mục cấp một của `shared/game-kit/` có `index.ts` (`hasModule`). Vì vậy mã nguồn của phần game giữ nằm ở **`shared/game-kit/typing-feel-client/`**: `index.ts`, `load-feel.ts`, `v1.d.ts` và `fake.ts` cho test không mạng.
- `v1.d.ts` sinh từ `typing-feel/src/contract.ts`. Một test chụp nhanh so bản trong kit với bản sinh ra.
- Monkeytype không có `kit.config.json`, nên chép tay bốn file này vào `custom/typing-feel/`, ghi nguồn trong `PROVENANCE.md` như hôm nay.

```ts
// load-feel.ts (game giữ, khoảng 80 dòng)
export async function loadTypingFeel(
  origin: string | undefined,                 // VITE_TYPING_FEEL_ORIGIN
  host: FeelHostOptions,
  options?: { timeoutMs?: number /* 3000 */; channel?: "v1" | "next" | `r/${string}` },
): Promise<TypingFeel | null>;                // null: không URL, 404, CORS, hết giờ, lệch hợp đồng, create ném lỗi

// v1.d.ts (module typing-feel.js export)
export const CONTRACT: 1;
export const VERSION: string;
export function createTypingFeel(options: FeelHostOptions & { base: string; catalogue: unknown }): TypingFeel;

export type FeelHostOptions = {
  game: "dragon-hold" | "typing-survival" | "typing-defense" | "monkeytype" | "admin-preview" | (string & {});
  audio: { context: () => AudioContext; destination?: () => AudioNode };   // context của game (có thể đang suspended), bus sfx
  settings: () => unknown;                                                 // object typingFx đã lưu; làm sạch bên trong
  save: (next: TypingFxSettings) => void;                                  // Typing Feel lưu qua game khi sửa id hoặc người chơi chọn
  levels: () => { master: number; keyboard: number; muted: boolean };      // 0..1
  extras?: readonly KeyboardSoundChoice[];                                 // âm của game: Relay, Dragonhold, Bamboo
  onStatus?: (status: FeelStatus) => void;
};
export type FeelStatus = {
  state: "loading" | "ready" | "partial" | "silent" | "failed";
  set: string; keys: number; spaces: number;
};

export interface TypingFeel {
  readonly version: string;
  readonly revision: string;
  readonly choices: readonly KeyboardSoundChoice[];          // Off, extras, rồi các bộ theo họ và thứ tự
  readonly styles: readonly { id: TypingFxStyle; name: string }[];
  sound(event: TypingSoundEvent, step?: number): boolean;     // false: Off, extra đang chọn, hoặc chưa giải mã; không bao giờ chờ
  owns(): boolean;                                            // đang có bộ Typing Feel phát được
  ready(maxWaitMs?: number /* 1500 */): Promise<void>;        // đợt đầu của bộ đã lưu, hoặc hết maxWait; không bao giờ reject
  unlock(): void;                                             // tự gắn một lần vào pointerdown/keydown đầu tiên
  refresh(): void;                                            // settings hoặc levels vừa đổi
  preview(id: string, delayMs?: number): void;
  stopPreview(): void;
  select(id: string): void;
  driver(options?: { sounds?: readonly TypingSoundEvent[]; strip?: FeelStrip | null }): {
    progress(p: TypingFxProgress, now?: number): void;
  };
  mountStrip(options: FocusStripOptions): FeelStrip;          // API FocusStrip hôm nay (strip.ts)
  mountKeyboardPicker(host: HTMLElement): () => void;          // KeyboardSoundChoices + preview, tiêu đề họ
  mountEffectsPreview(host: HTMLElement, options?: { words?: readonly { text: string; meaning: string }[] }): () => void;
  setTheme(theme: { palette?: Partial<TypingFxPalette>; font?: { family: string; weight?: number }; textures?: TypingFxTextures }): void;
  dispose(): void;
}
// Thêm sau trong v1: mountOverlay(options) cho lớp hiệu ứng của Monkeytype (fx-layer.ts, 1.162 dòng),
// phần đọc DOM riêng của Monkeytype (#wordsWrapper, #words, .word[data-wordindex]) ở lại fork qua một adapter locate.
```

- `v1.d.ts` xuất lại kiểu có sẵn của kit: `TypingFxSettings`, `TypingFxProgress`, `TypingSoundEvent`, `TypingFxPalette`, `TypingFxTextures`, `KeyboardSoundChoice`, `FocusStripOptions` (đều có trong `feedback/typing-fx/index.ts` hôm nay).
- `settings` và `save` nói bằng `TypingFxSettings`. Game không lưu `typingFx` (Dragonhold, Wordwoven, Monkeytype, mục 4.5) tự đổi qua lại trong hai hàm này, ví dụ Wordwoven `keyboard` ↔ `soundProfile`, `keyboardVolume / 100` ↔ `volume`. Không đổi chỗ lưu của game nào.
- Module không có tác dụng phụ khi nạp: không chèn CSS, không tạo AudioContext cho tới `createTypingFeel`.
- Font là font của game (`@fontsource`), texture là atlas của game, tải từ nguồn của game, nên canvas không bị "tainted".

---

## 5. Nạp lúc chạy, lỗi và dự phòng

### 5.1 Bước dữ liệu: một game làm gì

1. Lúc build: `VITE_TYPING_FEEL_ORIGIN`. **Mã không có giá trị mặc định**; script build đặt nó, cùng cách với `VITE_PORTAL_ORIGIN` của HOSTING_PLAN bước 1:
   - `pnpm build:local` ở repo cha và `pnpm dev` của game: `https://feel.typing-game.local`;
   - `deploy:pack` cho bản online: `https://feel.<tên-miền>`;
   - clone riêng hay CI không đặt gì: Typing Feel tắt, game vẫn chơi (mục 5.3).
   - Không ghi giá trị máy nhà vào `.env.production` đã commit: bản online sẽ mang `typing-game.local`, và `check-pack` báo `local-host`.
2. `index.html` thêm `<link rel="preconnect" href="https://feel.<host>" crossorigin>`.
3. Khởi động **không chờ** danh mục. Gọi `loadKeyboardCatalog(typingFeelKeysBase(origin), { extra: [builtIn], fallback: [], fetchJson: timedJson(3000) })` song song với phần còn lại.
4. Khi có danh mục: `settleKeyboardChoice(...)`. Chỉ lưu khi `repaired`.
5. Dựng bảng Sound với danh sách đó. Danh mục chưa về thì hàng âm phím hiện "Loading…".
6. Cổng vào trận chờ đợt âm đầu **tối đa 1,5 s**, rồi vào trận dù chưa có âm.

### 5.2 Lỗi hôm nay phải sửa trước khi đọc từ host khác

Cùng nguồn thì các lỗi này bị che. Khác host thì chúng phá luật 6.

| Game | Lỗi | Ở đâu | Sửa |
|---|---|---|---|
| Last Line | Khởi động `await` danh mục ở cấp cao nhất, không hạn giờ | `games/.wt-ts-typefx/src/app/main.ts:109` | bỏ khỏi `await`, chạy song song |
| Last Line | Danh mục hỏng thì ghi đè và lưu bộ của người chơi | `src/app/keyboard.ts:26` (`restoreKeyboardChoice`), `main.ts:110` | `settleKeyboardChoice` |
| Last Line | Cổng vào trận chờ `keyboardReady` không hạn giờ | `main.ts:223–224`, `:731`, `:825` | hạn 1,5 s |
| Dragonhold | Bảng Settings chỉ dựng sau khi danh mục về | `games/.wt-dh-keys/src/app/app.ts:950` | dựng ngay, nạp danh sách sau |
| Dragonhold | Danh mục hỏng thì ghi đè và lưu bộ của người chơi | `app.ts:952–953`, `src/app/settings.ts:54` (`keyboardChoice`) | `settleKeyboardChoice` |
| Wordwoven | Đã đúng: giữ id, hiện "unavailable" | `games/.wt-td-keys/src/app/quick.ts:42–48` (`keyboardChoices`) | thành luật chung trong kit |
| Wordwoven | `mountQuick` chờ danh mục không hạn giờ trước khi dựng bảng Settings (chunk lười, `src/main.ts:169`) | `src/app/quick.ts:58` | `timedJson(3000)` |
| Monkeytype | Danh sách phụ thuộc `installed.json` do `pnpm sync-keys` ghi | `frontend/src/ts/custom/typing-feel/catalog.ts:9–15` | đọc thẳng Typing Feel |

### 5.3 Hỏng thì game làm gì

| Tình huống | Game làm gì |
|---|---|
| Không có biến `VITE_TYPING_FEEL_ORIGIN` (clone riêng, CI) | Không gọi mạng. Off và âm gốc. |
| Host không trả lời, 404, CORS, HTML mã 200, treo 10 s | Sau tối đa 3 s: Off, âm gốc, và "Keyboard sounds unavailable". Bộ đã lưu giữ nguyên. Không lỗi chưa bắt. |
| Danh mục về, một bộ không tải được | Bộ đó không được tải lại trong phiên tới khi người chơi chọn lại (luật của Dragonhold). Phát âm gốc. |
| Danh mục về, bộ đã lưu đã bị ẩn hoặc retire | Chuyển về `default` của danh mục, lưu. |
| (Bước code) module không nạp được hoặc ném lỗi khi tạo | `loadTypingFeel` trả `null`. Hàng âm phím thành hàng chọn đơn giản. Hàng hiệu ứng bị khoá. Last Line giữ dải chữ của nó (bỏ `hud.strip.attach(typeFx)`, `main.ts:225`). |
| (Bước code) module ném lỗi khi đang chạy | Mỗi hàm public có try/catch riêng. Sau 3 lỗi: tự gỡ dải chữ, tắt tiếng, báo `failed` một lần. Game gắn lại dải chữ của nó. Không nạp lại trong phiên. |

Một phím không bao giờ chờ: `sound()` trả `false` ngay khi chưa có gì giải mã.

### 5.4 Độ trễ cú gõ đầu

- Mỗi phím là một lời gọi hàm trên AudioContext chung của game. Không thêm trễ so với hôm nay.
- **Tải lạnh:** preconnect → danh mục (vài KB) → manifest bộ (khoảng 2 KB, thay 162 KB) → đợt đầu 16 file (khoảng 100 KB, song song qua HTTP/2) → giải mã trên context của game, có thể đang suspended (`decodeAudioData` không cần thao tác người dùng).
  - nginx máy nhà hôm nay **chưa bật HTTP/2** (không block nào có `http2`). Block feel phải có `http2 on;` (nginx 1.31 trên máy nhà hỗ trợ). Không có thì HTTP/1.1 chỉ mở khoảng 6 kết nối, đợt đầu 16 file chậm hơn. Cloudflare có sẵn HTTP/2 và HTTP/3.
- **Tải ấm:** một lần 304 cho danh mục, rồi mọi file bộ âm lấy từ cache đĩa.
- **Cache chung giữa các game:** trình duyệt chia cache HTTP theo site (scheme cộng tên miền gốc). `dragon.`, `td.`, `survival.`, `monkeytype.` và portal cùng site với `feel.`, nên bộ đã tải ở một game là cache hit ở game khác.
  - Bản online cần **tên miền riêng**. `*.workers.dev` nằm trong danh sách hậu tố công cộng, nên mỗi subdomain ở đó là một site riêng, không dùng chung cache.
- Preview vẫn lười: dừng 150 ms rồi mới tải clip 1 s (`KEYBOARD_PREVIEW_DELAY_MS`, `audio.ts:574`).

### 5.5 Bước code: nạp module

- Game gọi `loadTypingFeel` ở dòng đầu `main.ts`, trước màn tiêu đề. Chỉ `await` ở chỗ cần: dựng bảng Sound và cổng vào trận (`feel ? feel.ready(1500) : undefined`).
- Danh mục và `typing-feel.js` tải song song. Tổng hạn 3 s.
- `?feel=next` chỉ được nhận khi build có cờ `VITE_TYPING_FEEL_NEXT=1` (chỉ `build:local` và `dev` đặt), để duyệt bản ứng viên. Không kiểm bằng tên host trong mã: chuỗi `typing-game.local` trong gói online sẽ bị `check-pack` báo `local-host` (`check-pack.mjs:89–92`).

### 5.6 CORS, CSP và độ tin cậy

- Mọi yêu cầu là GET ẩn danh: `Access-Control-Allow-Origin: *` là đủ, không preflight, không cookie. `decodeAudioData` chạy được trên byte tải có CORS. CORP `cross-origin` để sau này bật COEP vẫn được.
- Hôm nay không game nào đặt CSP (nginx không đặt; `firebase.json` của Monkeytype chỉ có `frame-ancestors 'none'`). Nếu sau này thêm CSP: `script-src` và `connect-src` phải có host Typing Feel, và chính sách style phải cho phép sheet được chèn.
- Iframe của portal không sandbox (`portal/src/main.ts:566–569`), nên import chạy được trong đó.
- **Module chạy với quyền của nguồn từng game** (save, localStorage). Vì vậy code chỉ đến từ Git qua build của gói `typing-feel`. Admin chỉ publish dữ liệu đã kiểm. Token deploy Cloudflare là của chủ dự án.

---

## 6. Lưu trữ và hosting

### 6.1 Cái gì ở đâu

| Thứ | Ở đâu | Sao lưu |
|---|---|---|
| Danh mục, manifest bộ âm | `typing-feel/public/v1/keys/` | **Git** (commit theo yêu cầu, Admin không commit) |
| `health.json` | `typing-feel/public/v1/health.json` | Git |
| OGG của bộ âm | `typing-feel/public/v1/keys/sets/**` | `typing-feel/media.md5` + **Drive** |
| WAV gốc chủ dự án upload | blob Media V2, và bản chép `typing-feel/art-src/raw/<sha256>.wav` | Drive (nhóm originals) |
| Bản sửa, nháp, nhật ký, job | `.local/admin/shared/typing-feel/` | chỉ máy nhà; mất thì dựng lại từ Git (mục 6.3) |
| Registry và blob Media V2 | `.local/admin/space-typing/media-v2/` | chỉ máy nhà; blob của bộ đã Publish có bản ở Drive |
| Nhật ký Admin | `LocalAdminAuditLog` có sẵn, trong `.local/admin/space-typing/` | chỉ máy nhà |
| Code Typing Feel (bước code) | `typing-feel/src/`, build ra `typing-feel/dist/` (không commit `dist`) | Git (`src`) |
| Hợp đồng | `typing-feel/contract/typing-feel.v1.json` và bộ sinh `v1.d.ts` | Git |
| Phần game giữ (bước code) | `shared/game-kit/typing-feel-client/` (`index.ts`, `load-feel.ts`, `v1.d.ts`, `fake.ts`), vì `kit:sync` chỉ chép từ `shared/game-kit/` | Git |

- Thêm một mục `typing-feel` vào `games[]` của `media/media.config.json` (`id`, `dir: "typing-feel"`, `lock: "media.md5"`, `pulledStamp`). **Không cần sửa `scripts/media/lib/sets.mjs`:** `games[]` chỉ bắt buộc `id`, `dir`, `lock` (`normalizeGames`, dòng 21–37); `sources` và `modelsDir` là tuỳ chọn (`readSources` trả rỗng khi thiếu, dòng 156 của bản đang sửa).
  - OGG dưới `typing-feel/public/` vào nhóm runtime; WAV dưới `typing-feel/art-src/` vào nhóm originals (gốc `art-src`). Trên Drive là thư mục `repo/typing-feel/`.
  - `sets.mjs`, `plan.mjs` và `media.config.json` đang có thay đổi chưa commit (nhận JSON runtime dưới `public/assets/<id>/`). Đó là việc khác; cho vào trước để hai thay đổi không chồng nhau.
- Không Git LFS. Không bao giờ xoá trên Drive.
- `typing-feel/` là thư mục cấp cao ở repo cha, cạnh `portal/` và `admin/`, vì Admin và Audio Lab ghi vào nó. Nó tự đủ: `package.json` riêng, test ranh giới chặn import ra ngoài thư mục (như `tests/boundary.test.ts` của game). Tách thành repo riêng sau này chỉ là dời thư mục (mục 10, câu 3).

### 6.2 Máy nhà bây giờ

Thêm một block vào **cả hai** `infra/nginx/typing-game.local.play.conf` và `typing-game.local.dev.conf`:

```nginx
server {
    listen 443 ssl;
    http2 on;
    server_name feel.typing-game.local;
    ssl_certificate __SSL_CERT__;
    ssl_certificate_key __SSL_KEY__;
    root __ROOT_DIR__/typing-feel/dist;          # bước code; trước đó thư mục chưa có, mọi đường ngoài /v1/keys/ trả 404
    location /v1/keys/sets/ {
        alias __ROOT_DIR__/typing-feel/public/v1/keys/sets/;   # alias tự trả 404 khi thiếu file
        add_header Cache-Control "public, max-age=31536000, immutable" always;
        add_header Access-Control-Allow-Origin "*" always;
        add_header Cross-Origin-Resource-Policy "cross-origin" always;
        add_header X-Content-Type-Options "nosniff" always;
    }
    location = /v1/health.json {
        alias __ROOT_DIR__/typing-feel/public/v1/health.json;
        add_header Cache-Control "no-cache" always;
        add_header Access-Control-Allow-Origin "*" always;
        add_header Cross-Origin-Resource-Policy "cross-origin" always;
        add_header X-Content-Type-Options "nosniff" always;
    }
    location /v1/keys/ {
        alias __ROOT_DIR__/typing-feel/public/v1/keys/;
        add_header Cache-Control "no-cache" always;
        add_header Access-Control-Allow-Origin "*" always;
        add_header Cross-Origin-Resource-Policy "cross-origin" always;
        add_header X-Content-Type-Options "nosniff" always;
    }
    location / {
        try_files $uri =404;                      # không fallback SPA
        add_header Cache-Control "no-cache" always;
        add_header Access-Control-Allow-Origin "*" always;
        add_header Cross-Origin-Resource-Policy "cross-origin" always;
    }
}
```

- `add_header` phải lặp lại trong mỗi `location`: location có `add_header` riêng thì bỏ hết header cấp server.
- Location dùng `alias` không thêm `try_files`: `alias` tự trả 404 khi thiếu file (như `/vocabulary/` của portal hôm nay), còn `alias` đi cùng `try_files $uri` là chỗ nginx hay ghép sai đường.
- `http2 on;` để đợt đầu 16 file tải song song (mục 5.4).
- Thêm `feel.typing-game.local` vào `HOSTS` của `scripts/setup-nginx.sh` (dòng 38) để `/etc/hosts` và chứng chỉ mkcert có tên này, và vào `server_name` của block chuyển cổng 80 (`play.conf:3`, `dev.conf:3`).
- `scripts/validate-play-mode.mjs` thêm kiểm: host feel có CORS ở mọi location, không fallback SPA. Host game vẫn không được alias dữ liệu chung (luật của Codex 216).
- Publish ghi thẳng vào thư mục nginx phục vụ: **có hiệu lực ở lần tải sau, admin tắt cũng được**.

### 6.3 Clone mới hoặc mất `.local`

1. `git clone --recursive`, `pnpm install`, `pnpm media:pull`.
2. `pnpm build:local` (thêm `build:feel` ở bước code). `scripts/play.sh` kiểm thêm `typing-feel/public/v1/keys/keys-manifest.json`.
3. `pnpm setup:play` (sudo, một lần), `pnpm play`.
4. Admin thấy `.local/admin/shared/typing-feel` trống: dựng lại registry từ danh mục đã commit và file đã pull, thành bản `runtime-reference` (cùng kiểu `admin/media-bootstrap.mjs`), và một bản sửa `restored-<revision>`. Nháp chưa Publish thì mất; ghi rõ điều này ở Release & History.
   - Bộ dựng lại là bản tham chiếu, không phải blob của Admin. Re-format một bộ như vậy cần WAV gốc (pull từ nhóm originals) và ra một bản `admin-upload` mới.
5. Format bộ mới cần venv Audio Lab và ffmpeg.

### 6.4 Cloudflare sau này (cùng HOSTING_PLAN bước 0–3)

- `feel.<tên-miền>`: **một Worker chỉ có file tĩnh, không mã**. Lượt tải miễn phí (HOSTING_PLAN §2), dùng 1 trong 100 Worker.
- Không đặt trên portal (phá luật 7; fallback SPA của portal che 404; `/assets/` của portal immutable), không trên admin (chỉ chạy ở nhà), không R2 (tính lượt đọc khi vượt mức miễn phí, và phải tự đặt CORS; Workers Static Assets thì lượt tải miễn phí).
- `_headers` (Cloudflare gộp mọi luật khớp, nên đặt Cache-Control theo đường cụ thể, không chồng nhau):

```
/*
  Access-Control-Allow-Origin: *
  Cross-Origin-Resource-Policy: cross-origin
  X-Content-Type-Options: nosniff
/v1/keys/keys-manifest.json
  Cache-Control: no-cache
/v1/health.json
  Cache-Control: no-cache
/v1/typing-feel.js
  Cache-Control: no-cache
/v1/next/*
  Cache-Control: no-cache
/v1/keys/sets/*
  Cache-Control: public, max-age=31536000, immutable
/r/*
  Cache-Control: public, max-age=31536000, immutable
```

- `pnpm feel:pack` dựng `.deploy/typing-feel/`: danh mục hiện tại, thư mục bộ âm của **10 bản Publish gần nhất**, `_headers`, `health.json`. Kiểm: sha256 khớp, số file (cảnh báo ở 15.000, dừng ở 19.000; giới hạn 20.000 mỗi deploy), không file nào quá 25 MiB, không còn `typing-game.local`.
  - Tối 30/10, 34 bộ ở staging là khoảng 2.780 file, 27 MB.
  - Từ bước code, gói có thêm `v1/typing-feel.js` và `r/<build>/typing-feel.js`. Zip cho máy công ty (mục 6.5) là đúng gói này, nên Monkeytype ở đó nhận cả module.
- `pnpm feel:deploy`: chủ dự án chạy bằng token của mình. **Từ chối** khi danh mục chưa commit hoặc thiếu media, để bản online luôn dựng lại được từ một clone sạch.
- Game online build với `VITE_TYPING_FEEL_ORIGIN=https://feel.<tên-miền>`. `check-pack.mjs` đã báo `local-host` khi gói còn `typing-game.local` (`shared/game-kit/tools/deploy/check-pack.mjs:92`).

### 6.5 Máy công ty (chỉ GitLab, chỉ Monkeytype)

- Không có repo cha, Drive hay Audio Lab. Không bao giờ làm bộ âm ở đó.
- Trước khi có Cloudflare: `pnpm feel:mirror <typing-feel-v1-rN.zip>` giải nén gói của `feel:pack` vào `frontend/static/typing-feel/` (Git bỏ qua), dùng cùng nguồn, `TYPING_FEEL_URL=/typing-feel/v1/`. Chủ dự án tải zip từ Drive bằng trình duyệt. Hôm nay máy đó cũng làm gần như vậy với zip 32 bộ (`tmp/keys-firefly/zip/keys-firefly-32-monkeytype.zip` rồi `pnpm sync-keys`), nên thói quen không đổi.
- Nhánh máy công ty kéo từ GitLab là `feature/en-vn-translation` (HANDOFF_CURRENT, 30/10). Mọi thay đổi của B6 phải lên nhánh đó.
- Sau khi có Cloudflare: không cần làm gì.

### 6.6 Lùi lại

- **Dữ liệu:** Release & History → Rollback to N. Danh mục được ghi lại theo bản N. Thư mục bộ âm vẫn còn, vì không bao giờ bị ghi đè hay tự xoá ở máy nhà. Máy nhà có hiệu lực ở lần tải sau. Online cần deploy lại; gói đã có bộ âm của 10 bản gần nhất.
- **Code (bước code):** `pnpm feel:promote` chép `/v1/next/` vào `/v1/` và `/r/<build>/`. Lùi là promote bản trước; giữ 5 bản gần nhất trong `typing-feel/releases/`. Trên Cloudflare có thể dùng rollback phiên bản Worker (lần deploy đầu kiểm xem file tĩnh có lùi theo không).
- **Một game:** revert đúng commit chuyển đổi của game đó. Tệ nhất là âm phím Off (luật 6).

---

## 7. Chuyển ba game và Monkeytype, từng bước

Mỗi bước giữ mọi game chơi được và chỉ động tới một nơi. Ba nhánh game (`ts-typefx`, `dh-keys`, `td-keys`) **chưa merge vào main**, và main của ba game có **0** file âm phím. Bỏ bản sao trên nhánh trước khi merge thì main không bao giờ giữ chúng.

**B0. Chuẩn bị (chủ dự án và điều phối)**
- Chủ dự án duyệt tài liệu này.
- Chủ dự án chạy `pnpm setup:play` một lần (sudo) và `pnpm media:setup --reconnect` (token rclone hết hạn 30/10).
- Cho vào các thay đổi đang dở: `shared/game-kit/feedback/typing-fx/css.ts`, `draw.ts`, `shared/game-kit/ui/quick-settings/css.ts`, `scripts/media/lib/plan.mjs`, `sets.mjs`, `media/media.config.json`.
- **Hail Stone (bộ 34)**, đọc Git tối 30/10 lúc phản biện:
  - đã commit ở ba nhánh game: `ts-typefx` `22d22dc`, `dh-keys` `10bf889`, `td-keys` `0cff05e` (mỗi nhánh 2.744 dòng `audio/keys` trong `media.md5`);
  - Monkeytype `feature/typing-feel-32` còn dở: `hail-stone/` chưa theo dõi, `keys-manifest.json`, `keys.sha256`, test, `PROVENANCE.md`.

  Đề xuất: làm xong Monkeytype theo cách cũ, để cả bốn nơi cùng 34 bộ. Đó là lần chép tay cuối cùng; B3–B6 bỏ hết bản sao.

**B1. Host Typing Feel, chỉ dữ liệu (không game nào đổi)**
- Tạo `typing-feel/` (package, `contract/typing-feel.v1.json`, `.gitignore` cho OGG và WAV).
- `pnpm feel:import ~/AudioLab/review/staging/keys-firefly`: dựng `sets/<id>/<fp12>/`, manifest rút gọn, danh mục `catalogue-3` bản `r1` (mọi bộ ở staging, tối 30/10 là 34). Lấy nguyên byte OGG, không mã hoá lại (mục 3.9). Bỏ qua `keys-manifest.*.bak.json`.
- Block nginx, `HOSTS`, `validate-play-mode`, mục `typing-feel` trong `media.config.json`, `pnpm media:push`.
- Kiểm bằng `curl -H "Origin: https://survival.typing-game.local"`: 200, có header CORS, `audio/ogg`; file thiếu trả 404.

**B2. Kit (thêm, không phá)**
- `timedJson`, `settleKeyboardChoice`, `typingFeelKeysBase`, trường mới của `KeyboardCatalog`, đợt giải mã đầu trộn phím và space.
- Test kit. `pnpm kit:sync --target games/.wt-ts-typefx` (và `.wt-dh-keys`, `.wt-td-keys`).
- Monkeytype không nhận `kit:sync`: chép tay `audio.ts` mới vào `custom/typing-feel/kit/`, cập nhật `PROVENANCE.md` và `kit-manifest.json`, như hôm nay (làm ở B6).

**B3. Last Line (nhánh `ts-typefx`)**
- `KEYS_BASE` (`src/app/keyboard.ts:5`) thành `typingFeelKeysBase(import.meta.env.VITE_TYPING_FEEL_ORIGIN)`.
- Sửa ba lỗi ở mục 5.2. Mặc định lấy từ danh mục.
- Xoá `public/assets/typing-survival/audio/keys/**` (gồm các `keys-manifest.json` đang theo dõi) và mọi dòng `audio/keys` của `media.md5` trên nhánh (2.744 dòng từ khi có Hail Stone).
- Test đang ghim danh mục thật (`tests/keyboard-sounds.test.ts` hỏng khi danh mục không đủ bộ) chuyển sang danh mục mẫu trong test, vì danh mục thật không còn nằm trong repo game (luật 2: test chạy được trên clone riêng).
- `pnpm check`, test, kiểm trình duyệt trên host play, có một lần chặn `feel.*`. Rồi merge.

**B4. Dragonhold (nhánh `dh-keys`)**
- `src/app/keyboard.ts:4`, `app.ts:950–953`, `settings.ts:54`. Cùng cách như B3.

**B5. Wordwoven (nhánh `td-keys`)**
- `src/app/quick.ts:14`, hạn giờ, chuyển `keyboardChoices` sang `settleKeyboardChoice` của kit.

**B6. Monkeytype**
- Thêm `TYPING_FEEL_URL` vào `frontend/vite-plugins/env-config.ts` (cả `devConfig`, `prodConfig` và kiểu `EnvConfig`). Không đặt (GitHub `monkey-ci`, GitLab) thì tắt: click của Monkeytype vẫn phát, CI xanh, không cần secret.
- `catalog.ts:9` đọc Typing Feel. Bỏ `loadInstalledSets`, `INSTALLED_URL`.
- Xoá (cần chủ dự án duyệt, mục 10, câu 14): `frontend/scripts/sync-keyboard-sounds.ts`, script `sync-keys` (`frontend/package.json:27`), **35 file** đang theo dõi dưới `frontend/static/sounds/keys/` (33 manifest bộ, danh mục gốc, `keys.sha256`; thêm một khi Hail Stone được commit), các dòng `.gitignore` 141–145, mệnh đề `sync-keys` trong `build:monkeytype` của repo cha (`package.json:22`).
- Thêm `pnpm feel:mirror`.
- Đẩy tay lên GitHub và GitLab, nhánh `feature/en-vn-translation` (workflow mirror trên GitHub chết từ 08/10, theo HANDOFF_CURRENT), rồi nâng con trỏ submodule ở repo cha. Đẩy lên remote cần chủ dự án bảo.

**B7. Admin (song song với B3–B6 được, khác repo)**
- Cấu trúc lại IA (mục 3.2), kho bản sửa, Media V2, thư viện, Publish, Rollback, Format, A/B.
- **Tiêu chí chấp nhận:** chủ dự án upload `raindrop.wav`, Format, nghe A/B với bản cắt thô, chấm, Publish. Bộ hiện trong cả bốn game sau khi tải lại, không build, không code. Rollback thì bộ biến mất.

**B8. Chuyển code (sau demo)**
- `typing-feel/src` nhận `shared/game-kit/feedback/typing-fx/**` và `ui/quick-settings/keyboard-choices.ts`, kèm test.
- QuickSettings của kit bỏ tuỳ chọn `keyboardSounds` và import typing-fx (`quick-settings.ts:15–16`), nhận một chỗ cắm `keyboardPicker`. Danh sách kiểu chữ do nơi gọi truyền vào (thay `LETTER_STYLES` cứng của `rows.ts`).
- Mỗi lần một game, sau `load-feel.ts`, có test so khớp trước (cùng sự kiện, cùng khung hình).
- Cuối cùng: xoá `shared/game-kit/feedback/typing-fx/`, rồi `kit:sync`; công cụ tự xoá `src/kit/feedback/typing-fx/**` ở từng game (`sync-game-kit.mjs`, dòng 279–286).
  - **Không bỏ module `feedback`** khỏi `kit.config.json`. Dragonhold và Last Line còn dùng phần khác của nó: `DRAGON`, `Reactions`, `Debris`, `HitStop`, `Trauma`, `NumberField`… (ví dụ `src/view/fx.ts:20` của Dragonhold). `feedback/index.ts` không xuất typing-fx, nên bỏ thư mục con là đủ.
  - Wordwoven chỉ dùng phần typing-fx của `feedback` (`src/app/quick.ts:7` và qua `ui/quick-settings`), nên bỏ được `feedback` khi cả hai chỗ đã chuyển sang module.
- Cập nhật `docs/games/IN_GAME_SETTINGS.md`: hàng "Keyboard sound" hôm nay còn ghi năm hồ sơ cũ; từ nay danh sách lấy từ Typing Feel.
- Monkeytype: `sounds.ts` dùng `feel.select/sound/owns/ready`, giữ `KeySoundRouter`. Trong `store.ts`, `keyboardSound` đã là chuỗi id; đổi `letterEffect` và `effectStrength` từ `z.enum(...)` (lấy từ kit chép) thành chuỗi, kiểm theo danh sách của module lúc chạy, để kiểu chữ mới từ module không bị save từ chối. `fx-layer.ts` chuyển vào `mountOverlay` khi hàm đó được thêm.

**B9. Cloudflare** (cùng HOSTING_PLAN): Worker `typing-feel`, `_headers`, biến origin của bản online, `feel:deploy`.

**Xoá sau khi xong:**
- Sau B3–B6: bản sao âm trong ba nhánh và Monkeytype (như trên); viết lại KEYS_FIREFLY_HANDOFF §3; `~/AudioLab/review/staging/keys-firefly` thành kho lưu chỉ đọc.
- Sau B8: `shared/game-kit/feedback/typing-fx/**`, `ui/quick-settings/keyboard-choices.ts`, `src/kit/feedback/typing-fx/**` và `src/kit/ui/quick-settings/keyboard-choices.ts` của từng game (qua `kit:sync`), `custom/typing-feel/kit/**` của Monkeytype (7 file, `PROVENANCE.md`, `kit-manifest.json`). `scripts/sync-game-kit.mjs` có danh sách `MOVED` (`feedback/typing-fx`, `ui/quick-settings/keyboard-choices.ts`) để hai phần đó không bị chép lại.
- **Không bao giờ xoá:** file trên Drive, WAV gốc, bản Media V2 còn được một bản sửa tham chiếu.

**Một game mới tham gia Typing Feel** (game sau này, hoặc Space Typing nếu chủ dự án muốn, mục 10, câu 16):
1. Thêm `typing-feel-client` vào `kit.config.json`, chạy `kit:sync`. Game không theo kit (như Monkeytype) thì chép tay bốn file, có `PROVENANCE.md`.
2. Script build đặt `VITE_TYPING_FEEL_ORIGIN`; `index.html` có `preconnect`.
3. Gọi `loadTypingFeel` lúc khởi động, không chờ. Truyền `AudioContext` và bus sfx của game, hàm đọc và lưu save, âm gốc của game qua `extras`.
4. Bảng Sound dùng `mountKeyboardPicker`. Game có hiệu ứng chữ thì dùng `mountStrip` và `driver`.
5. Test khi Typing Feel hỏng (mục 8.1) và kiểm trình duyệt có chặn `feel.*`.
6. Thêm một dòng vào `admin/typing-feel/consumers.json`. Không cần sửa Admin hay Typing Feel.
- Trước bước code, game mới dùng đường dữ liệu: `loadKeyboardCatalog(typingFeelKeysBase(origin), …)` như mục 5.1.

---

## 8. Kiểm thử và chuẩn chất lượng

### 8.1 Tự động

- **typing-feel:**
  - test kit đã chuyển sang;
  - test chụp nhanh hợp đồng: `v1.d.ts` sinh ra phải bằng bản đã commit; bỏ hoặc đổi tên là lỗi, trừ khi vào `/v2`;
  - `contract/typing-feel.v1.json` khớp `TYPING_FX_STYLES`, `TYPING_FX_INTENSITIES`, `TYPING_FX_SIZES` và regex id;
  - `feel:pack` **chặn** khi: một dòng danh mục không phân giải được, sha256 lệch, file không giải mã được, đỉnh thật trên −1 dBTP (AUDIO_PIPELINE §4.3), vượt ngân sách số file hay cỡ, `_headers` thiếu CORS, còn `typing-game.local`.
  - `feel:pack` chỉ **báo** (không chặn) các số độ to và thời gian lên (LUFS-M max −27, đầu tiếng ≤ 2 ms, tiếng chính tới trong 15 ms, SHARED_SYSTEMS_BAR §2). Lý do:
    - các cổng này thuộc bước Format và bộ phê bình, không thuộc bước đóng gói;
    - công thức natural chuẩn theo đỉnh −2 dBFS, không chuẩn theo LUFS;
    - đo LUFS-M (cửa sổ 400 ms) trên file 0,45–0,54 s không chắc. Ví dụ `raindrop-tile/space-01.ogg` đo bằng `ffmpeg ebur128` ra −26,5 LUFS-M max. Chặn cứng ở −27 sẽ chặn bộ chủ dự án đã chọn.
- **Mỗi game, khi Typing Feel hỏng** (fetch giả trả 404, HTML mã 200, lỗi CORS, treo 10 s): khởi động không chờ; trận bắt đầu trong 1,5 s; có Off và âm gốc; id đã lưu không đổi trong storage; không promise bị bỏ rơi.
- **Chặn bản sao quay lại:**
  - `check-pack.mjs` thêm lỗi `keyboard-copy` khi gói game có `audio/keys/*.ogg`;
  - `validate-play-mode.mjs` kiểm host feel (CORS mọi location, không fallback SPA);
  - danh sách `MOVED` trong `sync-game-kit.mjs`.
- **Admin:** `admin/typing-feel/*.test.mjs`: kiểm upload, Format giả, thứ tự Publish, Rollback, từ chối xoá bản đang được tham chiếu, khoá ghi Media V2 khi hai việc ghi cùng lúc, hai lần Publish cùng lúc (chỉ một qua), quyền (`shared.publish`, `data-admin-permission`), id cố định và `retiredIds`, route xem trước chạy không token còn route `/api/admin/shared/…` thì trả 401 khi thiếu token, server khởi động khi thiếu `games/space-typing`. Thêm các file test này vào `admin:test` của `package.json`.
- `scripts/validate-admin-shared-ia.mjs`: mọi mục điều hướng có trang thật, mọi alias cũ còn chạy. 11 script `validate-space-admin-*` đang đọc `space-typing.ts` và kiểm `validate-play-mode` được sửa theo vỏ mới và vẫn xanh.
- **Audio Lab:** pytest cho `natural.py` và `onsets.py` trên một WAV mẫu tổng hợp: số cú, độ dài ≤ 450 ms, chạy lại ra **cùng mẫu PCM** (không so md5 của OGG, mục 3.9), báo lỗi đúng câu. Thêm một test trên ba nguồn thật (raindrop, hail v1, hail v4) khi có file trên máy: cả ba đạt bước kiểm nhanh.

### 8.2 Trình duyệt

- Tối đa 3 người kiểm, mỗi làn một lần (luật kiểm song song).
- Mỗi game: chọn bộ, nghe preview khi rê chuột, gõ, chặn `feel.*` trong DevTools, tải lại.
- Admin: đi hết luồng ở 1280 và 1920 px: thêm bộ, đổi thứ tự, ẩn, đổi mặc định, Publish, Rollback.
- Ảnh chụp để trong `tmp/` của đúng game hoặc worktree, rồi dọn bằng `node tools/capture-prune/prune.mjs <thư mục> --apply` (chạy không `--apply` trước).

### 8.3 Chuẩn chất lượng

- **Một bộ âm mới** (SHARED_SYSTEMS_BAR §2, hai "giám khảo" của tiếng phím):
  1. Cổng cứng của bộ phê bình Audio Lab (AUDIO_PIPELINE §4) xanh. **Không** áp phần phạt đuôi dài của điểm 218, vì công thức natural cố ý giữ đuôi.
  2. Chủ dự án nghe trong bảng A/B của Admin (cân độ to, lặp 20 lần, so với bản cắt thô, có chế độ nghe mù) và chấm **từ 9**.
  - Dưới 9: chỉ Publish được dưới nhãn **Provisional**, có lý do, ghi nhật ký, không được làm bộ mặc định (mục 10, câu 5).
  - Cổng này chỉ áp cho bộ thêm qua Admin. 34 bộ đang có vào seed như hiện trạng (mục 3.5).
- **Thay đổi code hiệu ứng hoặc âm** (bước code trở đi): hai giám khảo độc lập từ 9 và chủ dự án ký trước khi `feel:promote`. B8 là chuyển nguyên trạng: chỉ cần so khớp.

### 8.4 Số phải đạt

| Đo | Mức |
|---|---|
| Đợt âm đầu giải mã xong, tải lạnh | < 1,5 s |
| Đợt âm đầu giải mã xong, tải ấm | < 300 ms |
| Cú gõ đầu tiên có tiếng | ≥ 19/20 lần |
| Game thứ hai lấy bộ âm từ cache đĩa | có |
| Trận bắt đầu khi Typing Feel chậm hoặc hỏng | ≤ 1,5 s sau khi sẵn sàng |
| Manifest bộ âm game tải | ≤ 4 KB |
| Publish tới khi máy nhà thấy | lần tải sau, không build |

---

## 9. Kế hoạch theo giai đoạn

Cỡ việc (việc của agent, chưa tính thời gian chủ dự án nghe): **S** ≤ nửa ngày, **M** 1–2 ngày, **L** 3–5 ngày.

| Giai đoạn | Việc | Xong khi | Cỡ |
|---|---|---|---|
| G0 | B0: duyệt, `setup:play`, nối lại rclone, cho vào thay đổi dở, chốt Hail Stone | chủ dự án đã trả lời mục 10; `git status` của các file ở B0 sạch; bốn nơi cùng một danh sách bộ | S |
| G1 | B1: `typing-feel/`, `feel:import`, nginx, media | curl đạt mục 4.2; mọi bộ ở staging (34) có trên Drive; không game nào đổi | M |
| G2 | B2: thêm vào kit | test kit xanh; `kit:sync --check` xanh ở ba nhánh | S |
| G3 | B3–B5: Last Line, Dragonhold, Wordwoven, lần lượt | mỗi game: đọc từ host feel, bỏ mọi dòng `audio/keys` của md5, test dùng danh mục mẫu, đạt mục 5.3 khi chặn `feel.*`, merge | M mỗi game |
| G4 | B6: Monkeytype | CI xanh khi không có biến; local đọc Typing Feel; đã đẩy GitHub và GitLab | M |
| G5 | Admin IA: vùng, nút chọn khu, Administration, chuyển đường cũ, `/admin`, nginx `/api/admin/` và `/api/runtime/typing-feel/`, server chạy khi thiếu Space | mọi URL cũ chạy; `validate-admin-shared-ia`, 11 script `validate-space-admin-*` và `validate-play-mode` xanh; đi trình duyệt 1280 và 1920 | M |
| G6 | Kho Typing Feel, policy, phạm vi thay đổi, xuất, Publish, Rollback; khoá ghi Media V2; `createUploadBundleVersion`; `import-staging`; Keyboard Sounds, Typing Effects, Release & History; `shared.publish` | test Node xanh; bản xuất seed trùng danh mục staging; đổi thứ tự, ẩn, đổi mặc định, Publish, Rollback chạy trong trình duyệt | L |
| G7 | `natural.py`, `onsets.py`, job, trang Add sound set, A/B | tiêu chí B7: raindrop từ upload tới bốn game, không code; Rollback gỡ được | L |
| G8 | B8: chuyển code thành module chung, từng game | so khớp xanh ở mỗi game; `feedback/typing-fx` không còn trong kit của game nào (phần còn lại của `feedback` giữ nguyên); đạt mục 8.4 | L, cộng M mỗi game |
| G9 | B9: Cloudflare | `feel.<tên-miền>` trả đúng header; game online đọc được; `feel:deploy` từ chối khi chưa commit | M |

- Thứ tự: G0 → G1 → G2 → G3 → G4. G5 → G6 → G7 chạy song song với G3–G4 được, vì khác repo. G8 sau demo. G9 theo HOSTING_PLAN.
- Nếu giữ một làn Codex (luật 30/10): G1–G4 trước (gỡ bản sao, sửa luật 6), rồi G5–G7.

---

## 10. Quyết định cần chủ dự án duyệt

Mỗi câu có đề xuất. Chủ dự án chỉ cần trả lời "đồng ý" hoặc ghi lựa chọn khác.

1. **Tên host:** `feel.typing-game.local` bây giờ, `feel.<tên-miền>` khi lên Cloudflare.
   **Đề xuất:** đồng ý.

2. **Monkeytype bản online có ở cùng tên miền gốc với các game không** (ví dụ `monkeytype.<tên-miền>`)? Cùng tên miền thì bộ âm tải một lần, dùng chung cache với mọi game. Khác tên miền thì Monkeytype tải riêng một lần.
   **Đề xuất:** cùng tên miền gốc, và là tên miền riêng của dự án, không dùng `*.workers.dev` (mỗi subdomain ở đó là một site riêng, mất cache chung).

3. **Mã và dữ liệu Typing Feel đặt ở đâu:** thư mục `typing-feel/` ở repo cha, hay repo riêng ngay từ đầu.
   **Đề xuất:** `typing-feel/` ở repo cha bây giờ, tự đủ và có test ranh giới. Tách repo sau nếu cần, chỉ là dời thư mục.

4. **Nguồn để khôi phục bản Published:** danh mục và manifest vào Git, OGG và WAV lên Drive (Admin không chạy git; agent commit khi chủ dự án bảo), hay chỉ sao lưu `.local/admin/shared` lên Drive.
   **Đề xuất:** Git cộng Drive. Release & History luôn hiện "chưa commit" hoặc "chưa lên Drive" để không lệch.

5. **Cổng nhận một bộ âm mới làm bằng công thức natural:** cổng cứng của bộ phê bình (bỏ phần phạt đuôi của điểm 218) cộng điểm nghe của chủ dự án.
   **Đề xuất:** từ 9 thì Published. Dưới 9 chỉ được Publish dưới nhãn Provisional, có lý do, không được làm bộ mặc định. Chỉ áp cho bộ thêm qua Admin. 34 bộ đang có, kể cả Raindrop Tile và Hail Stone (chủ dự án chọn, chưa có điểm số), vào như hiện trạng. Chủ dự án có thể chấm điểm hai bộ đó trong Admin bất cứ lúc nào.

6. **32 bộ của ticket 218:** giữ trong danh sách hay cất đi.
   **Đề xuất:** giữ, nhãn `legacy-218`. Khi đã có bộ làm bằng Admin, chủ dự án ẩn hoặc retire từng bộ ngay trong thư viện. Id đã retire không bao giờ dùng lại.

7. **Định dạng upload:** WAV (PCM 16/24-bit hoặc float), 44,1 hoặc 48 kHz, mono hoặc stereo, 4–30 s, tối đa 50 MB, ít nhất 12 cú dùng được (to trong vòng 25 dB so với cú to nhất, cách cú sau ít nhất 150 ms). Đỉnh sát 0 dBFS chỉ cảnh báo, không chặn.
   **Đề xuất:** đồng ý, chỉ WAV (Firefly xuất WAV). Thêm FLAC sau nếu cần. Ba bản thu của chủ dự án ngày 30/10 (raindrop, hail v1, hail v4) đều đạt luật này. Luật cũ "chặn khi đỉnh trên −0,1 dBFS" sẽ chặn Hail Stone v4, nên đã bỏ.

8. **Khi nào chuyển code hiệu ứng gõ vào module chung:** ngay sau khi âm đã đọc từ Typing Feel, hay sau demo.
   **Đề xuất:** sau demo, chuyển nguyên trạng có test so khớp. Mọi thay đổi code sau đó qua cổng hai giám khảo từ 9 và chủ dự án ký.

9. **Quyền:** một quyền `shared.publish` cho cả khu All games (âm phím hôm nay, hệ chung khác sau này), hay mỗi hệ một quyền. Space đang tách Publish (`config.publish`) và Rollback (`config.rollback`).
   **Đề xuất:** một quyền `shared.publish`, đánh dấu nguy hiểm, gồm cả Publish và Rollback của khu All games: người đẩy thay đổi ra mọi game phải lùi được ngay khi hỏng. Hôm nay vai trò đặt cho cả server (Super Admin), nên chọn cách nào cũng không đổi gì cho chủ dự án.

10. **Điều hướng:** tên "Typing Game Admin"; `/admin` mở All games; nút portal "Space Admin" thành "Admin"; Media Library và Roles chuyển xuống mục Administration chung, URL cũ vẫn chạy; trang Audit chỉ hiện khi đã làm xong.
    **Đề xuất:** đồng ý.

11. **Deploy online sau Publish:** chủ dự án chạy tay `pnpm feel:deploy` bằng token Cloudflare của mình, hay một nút trong Admin.
    **Đề xuất:** chạy tay trước. Nút trong Admin để sau, khi đã có Cloudflare và chạy ổn.

12. **Mặc định riêng theo game** (ví dụ Last Line mặc định bộ Deep): có cần không.
    **Đề xuất:** chưa. Mọi game cùng một mặc định. Âm riêng của game (Relay, Dragonhold, Bamboo) vẫn có trong danh sách.

13. **Kiểu chữ hiệu ứng:** dữ liệu do Admin bật tắt, hay ở trong code.
    **Đề xuất:** ở trong code của module chung. Admin chỉ chọn mặc định. Kiểu mới vẫn đến mọi game bằng một lần deploy Typing Feel.

14. **Xoá phần âm phím đang theo dõi trong Monkeytype** (manifest, `keys.sha256`, `sync-keys`, 35 file, 36 khi Hail Stone vào) và đẩy lên cả GitHub và GitLab, nhánh `feature/en-vn-translation`.
    **Đề xuất:** đồng ý, làm ở bước B6, sau khi Monkeytype đọc Typing Feel đã kiểm xong.

15. **Hiệu ứng chữ cho Dragonhold và Wordwoven.** Chủ dự án muốn âm và hiệu ứng gõ "áp cho mọi game như nhau". Hôm nay hai game này chỉ dùng âm phím của kit; chữ khi gõ do mã riêng của từng game vẽ, không dùng dải chữ và sáu kiểu chữ của kit. Typing Feel đưa được âm phím tới cả bốn game ngay, nhưng hiệu ứng chữ chỉ tới Last Line và Monkeytype.
    **Đề xuất:** chưa đưa vào khi còn giai đoạn ổn định demo (đang dừng tính năng mới). Sau demo, khi module chung đã chạy (B8), làm từng game: ghép `mountStrip` vào cách hiện chữ của game, qua cổng hai giám khảo từ 9.

16. **Space Typing và các game khác của portal** (Vocab Shooter, Recall, Karaoke, Tu Tiên) có tham gia Typing Feel không. Tài liệu này để Space ngoài: nó không dùng kit và chưa có bộ âm phím.
    **Đề xuất:** chưa. Game nào cần thì đi theo các bước "Một game mới tham gia Typing Feel" ở mục 7. Không phải sửa Admin hay Typing Feel.

17. **Typing Content vào khu All games.** Trang này hôm nay nằm trong Space Typing, nhưng đọc dữ liệu chung của mọi game (`shared/vocabulary`, `shared/typing-texts`), chỉ đọc.
    **Đề xuất:** chuyển sang All games với tên "Learning Content", đường cũ vẫn chạy. Đây đúng là "gom các setting chung". Làm cùng G5, không thêm tính năng mới.
