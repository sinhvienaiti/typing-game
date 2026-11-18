# Phiếu 198 · Kho âm từ file theo manifest v2

Hoàn tất ở repo cha, nhánh `feat/space-typing-admin-uiux`, ngày 30/10/2026.
Chỉ sửa nguồn kit và tài liệu được cho phép. Chưa commit hoặc đồng bộ game.

## Đã làm

- Mã mới: `shared/game-kit/audio/manifest.ts`, `variants.ts`, `file-bank.ts`.
- Nối kho file vào `audio/scene-audio.ts`; xuất API/kiểu qua `audio/index.ts`.
- Test mới: `manifest.test.ts`, `variants.test.ts`, `file-bank.test.ts`,
  `scene-audio-files.test.ts`; đồ giả `fake-audio.test-helper.ts` được lệnh
  đồng bộ bỏ qua theo đuôi `.test-helper.ts`.
- Một mục `### audio/: file theo manifest` trong README, một dòng DRIFT,
  changelog riêng `docs/changelog/2026-10-30-kit-audio-file-bank.md`.
- Bằng chứng, log đỏ/xanh và ảnh chụp trạng thái Git dạng chữ trong `198/`.
  Không tạo ảnh hoặc âm vì phiếu chỉ yêu cầu mã tải/phát file.

## API mới

Chữ ký đầy đủ và kiểu xuất nằm trong `audio/index.ts` cùng các module trên.

| API | Chữ ký, mặc định |
|---|---|
| Chuẩn hóa | `parseAudioManifest(json: unknown): AudioManifest`; dạng chung `{ sounds, music, errors }`, nhận v1/v2, bỏ từng mục hỏng. Mảng file rỗng, đường dẫn rỗng, duration sai độ dài/giá trị, metadata không hợp lệ đều có lỗi riêng |
| Tải metadata | `loadAudioManifest(url: string): Promise<AudioManifest>`; HTTP/mạng/JSON lỗi trả rỗng có lỗi, không ném |
| Kiểu manifest | `AudioManifestV1`, `AudioManifestV2`, `AudioManifestSource`, `AudioManifest`, `ManifestSound`, `ManifestTrack`; nguồn là URL hoặc object |
| Chọn biến thể | `new VariantPicker<S>(options?: VariantOptions<S>)`; `pick(id, readyIndices, variant?): number \| undefined`. `random = Math.random`, `avoidLast = 1`, số hoặc bảng theo id, kẹp tới số bản sẵn trừ 1 |
| Kho file | `new FileBank<S>(options?: FileBankOptions<S>)`; `audioBase = "/assets/audio/"`, `preload = []`, `decodeConcurrency = 4`, `legacy` là bảng URL cũ, `manifest` mặc định không có |
| Mở kho | `unlock(context: BaseAudioContext, eagerFiles: readonly string[] = []): Promise<void>`; metadata, ưu tiên theo thứ tự, rồi URL cũ/bản ghi bổ sung; gọi lại dùng cùng promise |
| Nạp id | `ensure(id: S): Promise<void>` nạp cả họ biến thể, không tự phát; `entry(id): ManifestSound \| undefined`, `url(id): string \| undefined`, `has(id): boolean` |
| Lấy file | `select(id, variant?): FileSelection \| null` gồm buffer/chỉ số/URL; `file(path): Promise<AudioBuffer \| null>`, `cached(path): AudioBuffer \| undefined`; cache và giới hạn chung |
| Độ dài, loop, nhạc | `duration(id, variant = 0): number` (giây); `loopBuffer(id): AudioBuffer \| null`; `track(name): Promise<{ url, buffer } \| null>` chỉ nạp nhạc khi gọi |
| Kho ghép | `new LayeredBank<S>(files, missing = {})`; `select(id, variant?): LayeredSelection`, chọn file/móc/im, không dựng công thức âm |
| Móc | `MissingHook = (context: AudioContext, out: AudioNode, noise: AudioBuffer, now: number) => number \| void`; tùy chọn `missing: Partial<Record<S, MissingHook>>`, mặc định rỗng |
| Scene cấu hình | `manifest?`, `preload?: readonly S[]`, `decodeConcurrency?`, `random?`, `avoidLast?`, `missing?`, `musicBus?: B`; `SoundSpec` object được bỏ `url` |
| Scene phát | `play(id, gain = 1, options = {}): number`, `PlayOptions.variant?: number` (chỉ số từ 0); trả giây đo từ buffer chia tốc độ thực, 0 khi im. `playFile` cũng trả số giây; người gọi bỏ giá trị trả về vẫn tương thích |
| Scene bổ sung | `ready(): Promise<void>`, `loopBuffer(id): AudioBuffer \| null`, `playTrack(name: string \| null): Promise<void>`; `playMusic(path \| null)` giữ API cũ |
| Thống kê | `FileBank.stats(): FileBankStats` gồm `errors`, `durationMismatches`; `SceneAudio.stats(): SceneAudioStats<S>` thêm `plays[id]: { file, hook, silent }`. Trả bản sao, id xuất hiện khi có lượt gọi `play` |

Các kiểu `FileSelection`, `LayeredSelection`, `DurationMismatch`, `PlayCounts`,
`FileBankOptions`, `FileBankStats`, `SceneAudioStats`, `VariantOptions` cũng
được xuất. `ready()` đợi metadata, id ưu tiên, file bảng cũ và bản ghi rồng;
không chờ các id lười hoặc nhạc. Trước `unlock()` không mở mạng hay context.

## Quyết định

1. **Bảng và manifest:** mục manifest hợp lệ thắng URL bảng; bỏ tải URL cũ.
   Bus/gain/gap lấy từ bảng âm game. Mục manifest hỏng bị bỏ riêng thì dùng
   URL cũ nếu có. Metadata không mang gain, bus hoặc ưu tiên.
2. **Giải mã:** id ưu tiên giải mã hết biến thể theo đúng thứ tự trước phần
   còn lại; yêu cầu phát sớm không chen trước ưu tiên. Các file bảng cũ và
   `dragonSamples` vẫn nạp tại mở khóa, qua hàng đợi chung mặc định 4 việc.
   Các biến thể sẵn được chọn ngay, giữ chỉ số gốc nếu bản khác lỗi.
3. **Id đang giải mã:** lượt `play` hiện tại gọi móc hoặc im. Khi buffer về,
   không phát muộn. Gap chỉ ghi khi thực sự chọn file/móc; hai nguồn dùng
   cùng gap theo id. Loop không phát một lần và không gọi móc.
4. **Độ dài:** `durationMs` chỉ là gợi ý trước giải mã; đo từ từng buffer
   thay thế ngay. Chênh lớn hơn 20 ms đi vào thống kê, đúng 20 ms không ghi.
   Giữ tốc độ ngẫu nhiên ±5 % của SceneAudio cũ; trả độ dài theo tốc độ
   thật đã gán cho source.
5. **Bus nhạc:** bus được chỉ định nối thẳng destination, còn bus hiệu ứng
   qua master SFX. Cả `playMusic` lẫn `playTrack` chịu `musicVolume` và
   gain/duck nhạc, không nhân SFX. Không chỉ định thì nhạc nối loa như cũ.
   Crossfade giữ hằng số giảm 0,4 giây, tăng 0,6 giây, dừng cũ sau 2 giây.
   Lượt nhạc tải chậm được hủy khi dừng hoặc chọn lượt mới.
6. **Biến thể:** `variant` đích danh ghi vào lịch sử, được phép ghi đè
   tránh lặp. Chỉ số chưa sẵn thì im; có bất kỳ file sẵn nào cũng không gọi
   móc để thay một chỉ số chưa sẵn. Một bản không tiêu thụ RNG chọn biến thể.

## Móc khi thiếu file

**Cờ theo luật chủ dự án 28/10: âm thanh phải là file thật.** `missing` là
đường chuyển tiếp để giữ mã âm game đang có trong thời gian nhận file;
không phải công thức tổng hợp tạm mới. Kit không thêm công thức, file âm,
oscillator hoặc filter nào. Duy nhất dòng mới cấp noise là mẫu đã có của
`synth()`: `this.noise ??= noiseBuffer(context)` tại `scene-audio.ts:201`.

Last Line sẽ dùng móc cho mã đang đi qua `scene.synth`/các hàm dựng hiện có
khi mở phiếu nối. Wordwoven có thể dùng móc của `TypingAudio` khi chuyển
sang kit. Dragonhold tiếp tục dùng bank riêng tới phiếu chuyển riêng; khi
đó mới cân nhắc đưa các recipe hiện có vào tùy chọn này. Phiếu 198 chưa
nối móc vào game nào.

Xóa **từng id** khỏi `missing` sau khi file Firefly/file được duyệt đã có,
đã kiểm mức trong bản trộn, thời điểm và các ca chơi đại diện, và thống kê
không còn phát bằng móc. Không giữ móc như nguồn âm mặc định lâu dài. Id
chưa có file hiện rõ qua `hook`/`silent`; lượt bị gap, tắt âm, chưa mở khóa,
loop hoặc thiếu file đều tính vào `silent`.

## Kiểm và số liệu

Test viết trước mã; `198/tests-red.txt` lưu lần đỏ đầu. Rà soát tiếp thêm
các ca đỏ về yêu cầu phát chen ưu tiên, bản ghi rồng và thời điểm crossfade
trong `tests-edge-red.txt`, sau đó sửa để xanh. Fetch có promise giữ/nhả
chủ động và AudioContext giả; không gọi mạng thật.

| Kiểm | Kết quả | Log |
|---|---|---|
| `pnpm kit:test` trước | 56 file, 867 test qua, 0 đỏ | `198/tests-before.txt` |
| `pnpm kit:test` sau | 60 file, 898 test qua, 0 đỏ | `198/tests-after.txt` |
| Test riêng `audio/` | 6 file, 41 test qua, gồm 31 test mới và 10 test cũ | `198/tests-audio.txt` |
| `pnpm --dir shared/game-kit typecheck` | 0 lỗi | `198/typecheck.txt` |
| Diff test SceneAudio cũ | Mã thoát 0; bốn test cũ qua, không sửa | `198/checks.txt` |
| Import từ `../` trong audio | 0 dòng (grep thoát 1 vì không khớp) | `198/checks.txt` |
| Tổng hợp mới trong ba module mới | 0 dòng | `198/checks.txt` |
| Tổng hợp trên các dòng thêm của SceneAudio | Đúng 1 dòng ngoại lệ cấp noise cho móc, không có công thức mới | `198/checks.txt` |
| Whitespace | `git diff --check` thoát 0 | `198/checks.txt` |

Bảng nhóm test mới (mỗi test chỉ đếm một lần; vài test kiểm nhiều yêu cầu):

| Nhóm trong phiếu | Số test | Phân bố |
|---|---:|---|
| Parse, tải manifest và lỗi | 9 | v1/v2, mục hỏng, phiên bản 3, root/collection hỏng, tải tốt, 404/mạng/JSON hỏng |
| Biến thể | 4 | 1.000 lượt/3 bản/seed cố định, không lặp liền và mỗi bản 20–47 %; tránh hai/4 bản; một/không bản và kẹp cửa sổ; chỉ định bản |
| Giải mã | 7 | 5 test FileBank về thứ tự, chờ ưu tiên, trần 2/4, cache và lỗi; 2 test Scene về im khi tải/không phát muộn và bản ghi rồng |
| Độ dài | 2 | Hints được thay bằng số đo, ngưỡng 20 ms; độ dài biến thể chia tốc độ trong Scene và không phát muộn khi có móc |
| Móc | 4 | LayeredBank ưu tiên file; Scene gain/pan/bus/gap; URL manifest thắng bảng và không gọi móc khi sẵn; loop/chỉ số chưa sẵn/im |
| Manifest rỗng giữ lịch | 1 | Ba cấu hình cho cùng bốn sự kiện và 16 nút: hook@0, file@0, file@0,1, hook@0,2; hook@0,05 bị gap |
| Nhạc | 4 | FileBank loop và nhạc lười; hai API qua bus/duck/độc lập SFX/crossfade; đường cũ trực tiếp; hủy lượt tải chậm |
| **Tổng** | **31** | Bốn file test mới: 9 + 4 + 8 + 10 |

Không có test đỏ từ TF2 trong lần kiểm cuối; không cần dùng ngoại lệ bỏ
các module khác. Không chạy `kit:check`: các game chờ đồng bộ là đúng.

## Phạm vi và trạng thái các làn

`198/status-before.txt` và `198/status-after.txt` lưu nguyên
`git status --short -uall` cùng `git diff --stat`. `numstat-before.txt`,
`numstat-after.txt`, `scope.json` đối chiếu số dòng và đường dẫn. Các file
TF2 trong `feedback/typing-fx/` và `ui/quick-settings/` được đối chiếu riêng;
không sửa file nào ở đó. Đối chiếu cuối: **0 đường dẫn thay đổi ngoài
phạm vi phiếu**, không có dòng lạ mới do làn khác. Cả bảy file TF2 đang
bẩn giữ nguyên số dòng thêm/xóa; ba file chính:

| File TF2 | Trước (thêm/xóa) | Sau (thêm/xóa) |
|---|---:|---:|
| `feedback/typing-fx/audio.ts` | 136/77 | 136/77 |
| `feedback/typing-fx/css.ts` | 1/1 | 1/1 |
| `feedback/typing-fx/draw.ts` | 11/1 | 11/1 |

Bốn file TF2 còn lại và đối chiếu đầy đủ nằm trong `scope.json`.

## Đã bỏ qua và việc kế cho Claude

- Không sửa game, `src/kit`, media, script media, `.gitignore`, các vùng TF2
  hay Tu Tiên. Không chạy dev server, trình duyệt, mạng, build/test game,
  `kit:sync`, `kit:check` hoặc lệnh Git ghi. Chưa có file Firefly trong kit.
- Claude duyệt API, test và cờ chuyển tiếp; commit rồi đồng bộ kit vào
  Last Line (`main`) và Dragonhold. Dragonhold giữ bank riêng cho đến phiếu
  chuyển, kể cả khi module kit đã được đồng bộ.
- Wordwoven: `audio` đã có trong `kit.config.json` ở `td-keys` (`81baf46`),
  chưa gộp vào `a2-days`; đồng bộ sau khi gộp.
- Khi có file Firefly, mở phiếu gắn Last Line `hit.sub`, `hit.tail`
  (`AUDIO_PIPELINE.md` §6.3 mục 3), giữ logic ghép lớp/độ to/độ dài theo bậc.
- Mở phiếu chuyển Dragonhold sang kho file của kit.
- Chủ dự án xem cờ móc và quyết định nhận file theo từng id. Chưa có bằng
  chứng nghe hoặc kiểm trình duyệt ở phiếu mã này; phần đó thuộc phiếu
  ghép game sau đồng bộ.
