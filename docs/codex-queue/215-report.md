# Phiếu 215 · Cổng game trả lời lookup của shared learning

Ngày 30/10/2026 · Repo cha · Nhánh `feat/space-typing-admin-uiux`.

## Kết quả

Đã hoàn tất chín việc triển khai/tài liệu và các lệnh kiểm của phiếu.
Portal trả `typing-game:learning:v1:query-result` cho lookup hợp lệ từ
game đang mở; từ đã học ở game khác có bản ghi trong kết quả. Lõi lưu
tám mẫu gần đây có loại hoạt động và gợi ý để Dragonhold đếm lần nhớ
đúng. Bộ đọc theo đúng luật Dragonhold nhận **2** lần nhớ đúng cho kịch
bản năm sự kiện yêu cầu. Chưa nghiệm thu trong trình duyệt, đúng phạm vi
bàn giao Claude ở cuối phiếu.

Mốc bắt đầu: `7f0d9e4409c795fcee176d832df06a49a6c141b2`.
HEAD Dragonhold đã đọc: `1f1de484afd5092f5967454fab5f4e6edd3189c9`.
Không đổi nhánh. Trong lúc thực hiện HEAD tiến lên
`da505e4a3712c75b0a95ec2eb8d9928f5bd37570`: hai commit chỉ đổi sáu ghi
chú điều phối trong `docs/codex-queue`, không đổi nguồn hoặc cấu hình
đã kiểm. Xem `215/start.json`, `215/head-advance.txt` và mốc kết thúc
trong `215/verification.json`. Giữ bằng chứng các lượt dừng trước trong
thư mục 215; báo cáo cũ được chép sang `215/previous-report.md`.

## Phần của phiếu 214 và trạng thái ban đầu

Đã đối chiếu `214-report.md`. Bảy đường dẫn chưa commit sau thuộc 214,
được giữ nguyên bởi lượt này:

- `portal/public/games.json`
- `portal/src/main.ts`
- `portal/src/styles.css`
- `portal/src/game-card.ts`
- `portal/tests/fixtures/legacy-games.json`
- `portal/tests/game-card.test.mjs`
- `docs/changelog/2026-10-30-portal-english-names.md`

Không có file dùng chung với 214 cần sửa, nên không phát sinh bản chép
`215/before/`. `shared/learning` và `portal/src/learning/bridge.ts` sạch
ở mốc đầu. Changelog `2026-10-30-audio-lab-firefly-ingest.md` thuộc 217,
là file đã biết theo chỉ dẫn chạy lại lần 3. Không sửa nội dung đó.
Trạng thái toàn repo được lưu đầy đủ, không cắt ngắn, trong
`215/status-before.txt`; trạng thái vùng ghi ở
`215/allowed-status-before.txt` và `215/scoped-status-current.txt`.

## Các đoạn do 215 thay đổi

- `shared/learning/core.mjs:291`: thêm mẫu năm trường bằng
  `boundedAppendChronological`; mặc định `hintUsed` đã được parser sự
  kiện chuyển thành boolean. Mọi loại thực thể đều lưu; đến muộn vẫn
  chen đúng thời gian. Không lưu câu trả lời vào mẫu mới.
- `shared/learning/query.mjs:64`: parser lookup riêng, kiểm 1–200 phần
  tử trước bỏ trùng, tối đa 200 ký tự sau cắt khoảng trắng; từ vựng
  chuẩn hóa NFKC, loại khác chỉ trim. Bỏ trường lạ và giữ thứ tự id.
- `shared/learning/query.mjs:273`: tách cách dựng item cho query và
  lookup dùng chung. Query cũ giữ nguyên hình dạng, kể cả bản ghi cũ
  không có `recentSamples`. Lookup ở dòng 285 dùng `Object.hasOwn`,
  chỉ đọc các id yêu cầu, bỏ khóa nguyên mẫu kể cả khi có own property,
  không quét hồ sơ; luôn trả mảng `recentSamples`.
- `shared/learning/message-contract.mjs:11,61`: thêm loại lookup và
  trả `{ type, requestId, lookup }`; giới hạn 200 được định nghĩa một
  lần ở query rồi xuất lại qua hợp đồng tin, không tạo vòng import.
- `portal/src/learning/bridge.ts:91,107,114,183`: rẽ theo `message.type`,
  thêm handler lookup `flush → load → lookup → query-result`.
  Kiểm cửa sổ/origin ở dòng 80–84 giữ nguyên; game lấy từ iframe đang
  mở, không gắn cứng id. Giữ nhánh lỗi `invalid-request`, thêm xử lý
  đọc lỗi `query-failed`; lookup không ghi kho hoặc gọi `onApplied`.
- `shared/learning/profile-backup.mjs:130`: trường mẫu tùy chọn dùng
  `validateSamples`; bản cũ vẫn nhập được, bản có hơn tám mẫu hay mẫu
  sai dạng bị từ chối. Không cần đổi chữ ký `.d.mts` của sao lưu.
- Các khai báo `core.d.mts`, `query.d.mts`, `message-contract.d.mts`
  bổ sung mẫu, lookup, kết quả và kiểu phân biệt theo tên tin cho TS.
- Hai file test mới: `shared/learning/lookup.test.mjs`,
  `portal/tests/learning-lookup.test.mjs`. Không sửa test cũ.
- `shared/learning/README.md`: bổ sung trường mẫu, hỏi/trả lookup,
  chuẩn hóa, giới hạn, mã lỗi và điều kiện không trả lời.
- Changelog mới: `docs/changelog/2026-10-30-portal-learning-lookup.md`.

Toàn bộ thay đổi trong bridge và các file shared learning nêu trên là
của 215. Không sửa đoạn mã nào của 214. Danh sách file sản phẩm và bằng
chứng cụ thể có trong `215/files.txt`.

## Bảy mục kiểm

Mọi lệnh pnpm dùng `pnpm_config_verify_deps_before_run=false` để dùng
phụ thuộc sẵn có, không cài gói hoặc truy cập mạng. Log `.log` giữ nguyên
trên đĩa; bản `.txt` trong `215/logs/` bỏ khoảng trắng cuối dòng để Claude
có thể theo dõi bằng Git. Không bỏ thông báo hoặc lỗi kiểm tra.

| Mục | Kết quả | Bằng chứng trong `215/` |
|---|---|---|
| 1. Learning | Trước **12 file, 55 test, 55 đạt**; sau **13 file, 84 test, 84 đạt**, 0 lỗi. `pnpm learning:check` mã **0**. Các review-session/mixed-review/adaptive-mix và năm dataset cũ đều xanh, không sửa. | `baseline.json`, `tests-after.json`, `logs/learning-*.txt` |
| 2. Portal | Trước **51/51** trên 2 file; sau **77/77** trên 3 file. 11 test bridge cũ và 40 test thẻ game của 214 đều xanh. | `baseline.json`, `tests-after.json`, `logs/portal-*.txt` |
| 3. Build | `pnpm --dir portal build`: **0 trước, 0 sau**, gồm `tsc --noEmit` và `vite build`. Không đưa đầu ra build vào Git. | `build-baseline.exit`, `build-after.exit`, `logs/build-*.txt`, `bundle-bytes.json` |
| 4. Test trước mã | Shared: **29 mới**, đỏ **28**, xanh sẵn 1; sau **29/29**. Portal: **26 mới**, đỏ **9**, xanh sẵn 17; sau **26/26**. Tổng trước mã **37 lỗi**, sau **0 lỗi**. Các ca malformed vốn đã được nhánh lỗi cũ trả đúng nên xanh ngay. | `tests-before.json`, `tests-after.json`, `logs/*-red.txt` |
| 5. Snapshot | 12 sự kiện cố định, ba từ cùng grammar/sentence, các hoạt động yêu cầu, có/không gợi ý, câu sai và sự kiện đến muộn; bỏ riêng `recentSamples`, **giống hệt từng byte**. | `core-snapshot.mjs`, `core-before.json`, `core-after.json`, `core-hashes.json` |
| 6. Tốc độ | 5.000 từ, 200 id, 5 lần khởi động và **20 lần đo**; trung vị **0,1875 ms < 20 ms**, không cần tối ưu thêm. Mac arm64, Node v24.22.0. | `lookup-timing.mjs`, `lookup-timing.json` |
| 7. Phạm vi | `git diff --check` trên các file của phiếu: mã **0**; kiểm riêng khoảng trắng của file mới cũng đạt. Mọi file do 215 ghi đều nằm trong vùng được phép. Chênh status toàn repo được tách phần 215 và phần việc đồng thời, giữ nguyên file người khác. | `status-after.txt`, `status-delta.json`, `diff-check.txt`, `verification.json` |

SHA-256 của `core-before.json` và `core-after.json` đều là:

```text
f091f364b03c624afd2ab52e7b52113c88fc1e24945a0b73d3a3ac7d46aa182c
```

Tổng JS của các chunk gồm cả worker: **4.977.994 byte trước**, sau
**4.979.637 byte**, tăng **1.643 byte** (`215/bundle-bytes.json`). CSS trước/sau
**127.854 byte**. Cảnh báo chunk hơn 500 kB đã có ở baseline, không đổi
cách chia gói trong phiếu này.

So với status ban đầu, có thêm các file do việc đồng thời, gồm:
`docs/codex-queue/199/preflight-final-run.json` và
`docs/codex-queue/202/bundle-budget.json`, cùng phiếu
`docs/codex-queue/226-td-a2-package-160.md`. Không sửa hoặc xóa chúng.
Vì vậy không tuyên bố chênh status **toàn repo** chỉ gồm đường của 215;
phần do 215 tạo/sửa nằm hoàn toàn trong vùng cho phép. JSON chênh lệch
giữ riêng hai nhóm và danh sách đầy đủ tại mốc kết thúc để Claude kiểm.

Các kiểm bổ sung trong 55 test mới: ba game lấy origin từ registry;
ba origin sai, cửa sổ lạ, chưa mở game; 200/201 id; mọi ca tin hỏng;
id vắng mặt; prototype kể cả own key; thứ tự ghi trước đọc; đọc kho lỗi;
chỉ đọc và không callback; bản ghi cũ; mẫu đến muộn/bị chặn ở tám;
sao lưu và hợp đồng hằng số đọc từ kit dạng văn bản. Bộ đọc Dragonhold
chép luật `parseLookup`, `RECALLS`, `isRightRecall`, với ngưỡng
`weakMastery = 40`; chú thích giữ HEAD game. Không import mã game.

## Danh sách Claude sửa tiếp, kèm dòng

Các đường sau chỉ đọc, không sửa trong phiếu 215:

| Đường dẫn | Dòng | Việc Claude làm |
|---|---:|---|
| `shared/game-kit/learning/contract.ts` | 6 | Bỏ/cập nhật “the portal may not answer it yet”; lookup nay được portal trả lời. |
| `games/dragon-hold/src/app/learning.ts` | 335 | Cập nhật “its lookup may lack recent samples”; hồ sơ cũ còn thiếu mẫu lịch sử, kết quả luôn có mảng. |
| `docs/games/SPLIT_PLAN.md` §9.2 | 224 | Đánh dấu lookup tối đa 200 id, có recentSamples đã xong; dẫn báo cáo này. |
| `docs/games/DEPLOY_INDEPENDENCE.md` §7, hàng 6 | 162 | Bỏ tình trạng portal từ chối lookup; handler dùng game đang mở, không cần thêm nhánh theo id khi thêm game. Giữ phần Smart Review còn lại. |
| `docs/games/dragon-lane/01-core-combat-learning.md` §6.8 | 500 | Đánh dấu phụ thuộc lookup/recentSamples ở repo cha đã xong. |

Claude duyệt rồi commit, bổ sung hàng chỉ mục changelog, sửa các chú
thích/tài liệu trên, build lại portal. Sau đó kiểm một lần qua
`https://typing-game.local`, vào Dragonhold: lookup nhận `query-result`,
không `error`, không đợi timeout 2 s; từ đã học ở game khác có bản ghi
và không bị coi là từ mới. Lượt này không mở trình duyệt/dev server.

## Việc bỏ qua và giới hạn

Không chạy build/test game, không sửa `games/**`, `shared/game-kit/**`,
Smart Review, registry, `docs/games/**`, Tu Tiên, công thức điểm hay phiên
bản hồ sơ. Không media, mạng, kit:sync, lệnh Git ghi hoặc chỉnh chỉ mục
changelog. Các lệnh test/build portal và shared learning bắt buộc đều
đã chạy, không dùng luật chung để bỏ kiểm.

Bản ghi cũ không được dựng lại những mẫu đã không lưu trong quá khứ;
lookup trả `[]`, mẫu mới tích lũy từ sự kiện tiếp theo. Chỉ tám mẫu gần
đây được giữ, đúng hợp đồng. Nghiệm thu trải nghiệm trong trình duyệt
và kiểm G7/DH-04 thuộc bước Claude làm tiếp, chưa tuyên bố đã đạt.
