# Process chung: Mac mini M4 ⇄ Dell (từ 24/10/2026)

> File sống. Ghi việc đã xong, đang làm, còn lại cho **cả repo cha và 4 game**, để một AI không có bối cảnh hội thoại (Claude, Codex) làm tiếp được trên máy Dell hay máy Mac mini M4.
> Cập nhật sau mỗi phần việc đã commit: sửa mục 4–6 và thêm một dòng vào nhật ký (mục 9).
> File cũ hơn, chỉ cho Space Typing: [`games/space-typing/docs/CLAUDE_PROCESS_2026-10-17.md`](../games/space-typing/docs/CLAUDE_PROCESS_2026-10-17.md) (dừng ở 21/10, nhiều chỗ đã cũ).

## 1. Hai máy

| | Mac mini M4 | Dell (laptop Windows 11) |
|---|---|---|
| Thư mục repo | `/Users/toandx/htdocs/typing-game` | `D:\typing-game` = `/mnt/d/typing-game` trong WSL |
| Công cụ | Homebrew, node 24, pnpm 11.21 | **Chỉ trong WSL Ubuntu-24.04**: git, nvm node 24.11.0, pnpm 11.21.0. Windows không có git/node |
| Chạy lệnh | Terminal | `wsl -e bash <file.sh>`; script nên `source scripts/local-env.sh` (nạp nvm, `CHROME_PATH`, `BLENDER_BIN`) |
| Trình duyệt cho `cdp-run` | Chrome của macOS | Chrome for Testing trong WSL: `~/.cache/chrome-for-testing/chrome/linux-*/chrome-linux64/chrome` (tự đặt `CHROME_PATH` qua `local-env.sh`) |
| Blender | `/Applications/Blender.app` | Bản Linux `~/.local/blender/blender-5.2.*-linux-x64/blender` (tự đặt `BLENDER_BIN`). `D:\Blender\blender.exe` không nhận đường dẫn `/mnt/...` |
| audio-lab | Chạy được: `~/AudioLab` (venv, Stable Audio 3 bản MLX, thư viện CC0, work, review) | **Không chạy được phần sinh âm**: MLX chỉ có trên Apple Silicon, `say` chỉ có trên macOS, `~/AudioLab` không chép sang |
| Media (Google Drive qua rclone) | Đã cấu hình `tgmedia` | rclone 1.75 đã cài, **chưa có `~/.config/rclone`**: chủ dự án chạy `pnpm media:setup` (đăng nhập Google) trước mọi `media:*` |
| nginx Play mode | Đã dựng 9 host | nginx trong WSL còn cấu hình 16/10 (6 host cũ). Xem mục 7.3 |
| GitHub | SSH + HTTPS | SSH qua `~/.ssh/id_ed25519_github` (đã thêm `~/.ssh/config`). Remote của `games/space-typing` trên Dell đã đổi sang SSH; các submodule cũ (monkeytype, karaoke, recall, vocab) vẫn HTTPS, chưa có credential |
| RAM cho WSL | — | 7 GB: đừng chạy song song nhiều trình duyệt hay bộ cân bằng nhiều luồng |

Thiết lập đã làm trên Dell ngày 24/10 (log: `.local/dell-setup-2026-10-24.log`, gitignored):
- `core.filemode=false` trong mọi repo (bản chép từ Mac làm ~1.278 file hiện "đổi quyền"). `~/.gitconfig`: `user.name=toandx`, `user.email=toandx@192.168.52.5` (giống commit trên Mac), `pull.ff=only`, `core.autocrlf=false`.
- `node_modules` chép từ Mac hỏng hết (mất symlink, store trỏ `/Users/toandx/Library/pnpm/store`, binary darwin-arm64). Đã **chuyển** (không xoá) sang `D:\_mac-leftovers-2026-10-24\node_modules\` rồi `pnpm install --frozen-lockfile` cho: gốc, `portal`, `shared/game-kit`, 4 game.
- 4 worktree cũ của space-typing (`games/.wt-survival`, `.wt-td-1a`, `.wt-td-1a6`, `.wt-td-1a6-r3`) trỏ vào đường dẫn Mac, đã kiểm: không có thay đổi chưa commit, nhánh đã gộp hoặc đã push, nội dung có trong `typing-defense`/`typing-survival`. Đã **chuyển** 3 cái sang `D:\_mac-leftovers-2026-10-24\worktrees\`; `games/.wt-td-1a` chưa chuyển được (Windows đang giữ file, "Permission denied"), parent repo bỏ qua nó. Metadata `git worktree` vẫn còn (đánh dấu prunable), không ảnh hưởng.
- apt: jq, zip, ffmpeg, sqlite3, python3-venv, python3-pip, thư viện cho Chrome và Blender; rclone 1.75 (.deb chính thức); Chrome for Testing 156 (headless, sandbox chạy được); Blender 5.2.3 LTS bản Linux ở `~/.local/blender`.
- `scripts/local-env.sh` có thêm khối Linux: nạp nvm nếu thiếu node, đặt `CHROME_PATH`, `BLENDER_BIN`. Các script `cdp-run.mjs` đọc `CHROME_PATH`; `scripts/models/prepare-3d-models.mjs` đọc `BLENDER_BIN`.
- **Đừng chạy `pnpm bootstrap`** khi còn việc chưa commit: nó `submodule sync/update` (đổi remote 3 game mới sang HTTPS, checkout gitlink cũ).

## 2. Luật của chủ dự án (giữ nguyên trên cả hai máy)

- Việc nào tài liệu ghi "chủ dự án cần chọn": làm theo phương án đề xuất, ghi "đã chọn theo đề xuất" vào tài liệu, liệt kê trong báo cáo để chủ dự án đổi sau.
- Backend online chỉ dùng Cloudflare Free (Workers/D1/DO).
- Mô hình 3D: Claude viết prompt, chủ dự án tạo ở Tripo3D/Meshy, Claude dọn và rig trong Blender. Chủ dự án chê chuyển động cứng.
- Âm thanh: ghi nhớ cũ (18/10) nói "chỉ âm thu thật CC0". Từ 23/10, `tools/audio-lab/DECISIONS.md` Q1 cho phép Stable Audio 3 là nguồn chính cho lửa, nổ, nền, sinh vật (chủ dự án đã đăng ký giấy phép Stability). Theo `DECISIONS.md`.
- **Âm theo hình dạng hành động** (chủ dự án, 24/10, [`tools/audio-lab/DECISIONS.md`](../tools/audio-lab/DECISIONS.md) Q6). Mỗi âm phải đúng loại và cỡ của hành động: tụ lực, phát có lực, thân, đuôi vang trong không gian bản đồ. Rồng khạc cầu lửa phải nghe mạnh mẽ, vang vọng. Cấm âm quê mùa, lỗi thời kiểu "bụp", "thụp", puff, pop, bóng bay, đồ chơi, retro.
- Mỗi game có `AGENTS.md` riêng; repo cha có [`AGENTS.md`](../AGENTS.md) và [`docs/games/SPLIT_PLAN.md`](games/SPLIT_PLAN.md).
- Mỗi phần việc xong: commit, push, cập nhật file này.

## 3. Trạng thái Git lúc nhận từ Mac (24/10 ~09:08, chép sang Dell ~12:00)

Mọi commit trên Mac **đã có trên GitHub** (kiểm bằng `git ls-remote`). Phần chỉ có trên đĩa là việc chưa commit:

| Repo | Nhánh / HEAD | Chưa commit lúc nhận |
|---|---|---|
| cha `typing-game` | `feat/space-typing-admin-uiux` `f1ab34f2` | 34 file sửa + 64 file mới trong `tools/audio-lab` (lô 1: `BATCH1_BRIEF.md`, `SESSION_1_*.md`, `common/batch1_*.py`, gói `context/`, `build/recipes/**`); gitlink của dragon-hold, typing-defense, typing-survival chậm 1 commit |
| `games/space-typing` | `feat/space-typing-2026-10-18` `36249a35` (tag `td-1a6-final`, `survival-s0` đã push) | `media.md5` (+70 dòng art-src/td, đã đẩy lên Drive từ Mac 09:08). 409 file model/hull chưa track là **media của Drive theo thiết kế**: không `git add`, không `git clean` |
| `games/dragon-hold` | `main` `a011b96` | `media.md5` (6 GLB Rồng) chưa track |
| `games/typing-defense` | `main` `74628a4` | 45 file sửa + 10 file mới: lượt sửa sau phản biện 1B R1 và lượt rig sinh vật; `media.md5` (288 dòng) chưa track |
| `games/typing-survival` | `main` `c140039` | 15 file sửa: lượt sửa sau phản biện S1 R1 (đang dở: `COUNTER_SEEDS`/`countersMatch` thêm nhưng chưa dùng) |

Bản chụp nguyên trạng việc chưa commit của typing-defense và typing-survival: nhánh **`wip/mac-2026-10-24`** (đã push, chỉ để phòng hờ).

## 4. Đã xong trên Dell

- 24/10: audit toàn bộ, kiểm chứng chéo (6 agent), dựng môi trường (mục 1), bản chụp `wip/mac-2026-10-24`.
- 24/10, **bước A (chốt việc dở từ Mac) xong và đã push**. Mỗi game có một agent làm, một agent khác kiểm tra độc lập.

| Repo | Commit (đã push) | Nội dung | Kiểm tra độc lập |
|---|---|---|---|
| `games/typing-defense` | `b2533df`, `eb410e2`, `951c298`, `702eaf1`, `73019dc` | Sửa sau phản biện 1B R1; `BUILD_1B` khớp mã; `BUILD_NOTES` §7.2; changelog `2026-10-24-td-1b-r1-fix.md`; rig sinh vật (changelog `2026-10-24-models-creature-rigs.md`); `media.md5`; `scripts/td/tsx-worker.mjs` để `td:balance` chạy được trên Node 24.11 Linux | Đạt, có lỗi nhỏ (mục 6.A) |
| `games/typing-survival` | `17710ae`, `dc5a4db`, `a789a7b` | Sửa sau phản biện S1 R1: G3c bỏ bộ bẫy, báo cáo 100 seed chạy được, G3m 16 seed; changelog `2026-10-24-s1-r1-fix.md`; `BUILD_NOTES` 9.1 | **Chưa đạt**: một ô `COUNTERS` sai (mục 6.A) |
| `games/dragon-hold` | `09d7c7d`, `c105897`, `8fd646b`, `58b5ade`, `767d69a`, `8231629`, `7c28c45` | Ghi review 2; hỏi tốc độ gõ trước ván đầu, không ngầm 35 WPM (canon D26); cờ tướng G01; menu ô tránh Hỏa Long; golden Khó tắt điều nhịp + Esc; import kit; `media.md5` | Đạt, có lỗi nhỏ |
| `games/space-typing` | `9445341b`, `27a987b1`, `fe048d6a`, `63f63cf6` | `media.md5`; `.gitignore` chặn media runtime (mục review #74); `td.html` báo Lời Gọi đã chuyển; file process 17/10 trỏ về file này | Đạt |
| cha | (commit này) | Canon Rồng Giữ Ải D24–D26, §4.4, §4.10, §7; `DESIGN.md:4`; gitlink 4 game; `*.mp4` vào `.gitignore` | — |

Chưa đo được trên Dell: Chrome trong WSL vẽ WebGL bằng phần mềm (SwiftShader), nên các kịch bản hiệu năng và gõ phím thời gian thực trượt hoặc không chạy được:
- Lời Gọi: kiểm luồng chính của `td-1b-perf` và `td-1a6-perf`.
- Tuyến Cuối: `s0-keys`, `s0-perf`, `s1-perf`.
- Rồng Giữ Ải: `dh-hitstop-keys` và 10 kịch bản `dh-*`.

Chạy lại các kịch bản này trên Mac, hoặc trên Dell bằng Chrome của Windows (có GPU) qua node Windows (mục 6.C).

- 24/10, **lượt sửa sau kiểm tra độc lập xong và đã push**. Kèm theo, đo lại bằng GPU qua Chrome Windows các kịch bản trước đó trượt vì vẽ phần mềm.

| Repo | Commit | Kết quả |
|---|---|---|
| typing-survival | `015e454`, `e4c7db7` | Ô Xung/swarmNear = ○ như hai bộ seed đo được. G3m báo **trượt** một cách trung thực, test ghim `KNOWN_MISSES`; chờ lượt làm lại sức súng. Báo cáo 100 seed chạy lại (`tmp/dell-2026-10-24/bal100d.md`). GPU: hiệu năng đạt rộng. Kiểm tra: đạt |
| typing-defense | `0f7aa72`, `37c2ec1` | Thẻ Thành Lũy xếp lại nút bán; B1/B7 gộp chấm theo dải chặt (vẫn trượt như đã biết); đủ kịch bản ở 1920; GPU đạt; "đã chọn theo đề xuất (b)". Kiểm tra: đạt |
| dragon-hold | `02a0833`, `dc08714` | Phím tốc độ cố định; toast; ô số đo theo nét vẽ (`dh-numbers-drawn`); đo lại GPU. Kiểm tra: **chưa đạt**, vì tài liệu nói quá về bằng chứng hit-stop (mục 6.A) |
| space-typing | `4061ae02` | `.gitignore` chừa `*.md`, `*.txt` cạnh model. Kiểm tra: đạt |

- 24/10 tối, **bước B, đợt 1 (đã push)**. Workflow bị ngắt vì giới hạn phiên lúc khoảng 21:30. Phần đã xong:

| Repo | Commit | Nội dung |
|---|---|---|
| dragon-hold | `68e51ea`, `24c8591`, `8ccefbc`, `0211249`, `a4d00e7` | Vòng 3: 9 quyết định theo đề xuất (canon D27–D29: dải nhàn Cân bằng ≤ 20 %, G8 theo 03 §0, trần k 1,50). Atlas số sát thương từ kit. Hit-stop đo trên GPU: 0/2.848 khung có số chạm nhau. `dh-crowd` đủ 3 lần đo (seed 5, 6). B1/B7 vẫn trượt sau 6 vòng chỉnh. **Kiểm tra độc lập: đang chạy lại** |
| typing-survival | `f975d02`, `49ba852`, `0f0748d` | Làm lại sức súng (Xung chương 27 viên, Tán 2,3 s, Ray 95…), G3m đo trên cả seed 1–16 và 17–32, đồng bộ kit. Báo cáo 100 seed, tài liệu và kịch bản: **đang làm** |
| typing-defense | `8f5ae21` | Chỉ có phần âm Q6. R2 **đang dở trong cây làm việc** (khoảng 63 file), lượt chạy lại sẽ chụp vào nhánh `wip/r2-partial-2026-10-24` rồi làm tiếp |
| cha | `bfdf2177`, `512033e9` | Viết lại 54/66 thẻ âm hành động theo Q6 (`tools/audio-lab/Q6_REWRITE_2026-10-24.md`). Kit: atlas chữ số đo theo nét mực, nhãn ở hàng riêng; canon và BALANCE. Kiểm tra làn âm: **chưa đạt** (`hit.t1`/`t2` của Tuyến Cuối giữ nguyên với lý do sai; 4 thẻ còn "thump/thud"), đang sửa |

- 25/10 (rạng sáng), **bước B, đợt 2 (đã push)**:

| Repo | Commit | Nội dung | Kiểm tra độc lập |
|---|---|---|---|
| typing-defense | `66a2888`, `a6309e4`, `dd4534c`, `a9d855e`, `f9d4667`, `1da07bc` | 1B R2: Tối Thượng, Chữ Chiêu, Mảnh Chữ, Ngắt, Tanuki, Nuppeppō, chế độ hoảng; thẻ nhà tự xuống dòng; kịch bản `td-1b-ult`, `td-1b-direct`; `BUILD_NOTES` §7.3. Phần dở cũ chỉ còn ở nhánh cục bộ `wip/r2-partial-2026-10-24` (`c7db97d`, chưa push). Âm Q6: prompt pack `04-audio*.md` | **Chưa đạt**: G5 chỉ đạt với bot Chuẩn; cân bằng R2 tệ hơn R1 (B3 trượt, B1 trượt cả hai bộ); cần chỉnh cân bằng bị để chủ dự án chọn, trái luật chọn theo đề xuất; JS gzip 87,16 kB, vượt 85 kB |
| typing-survival | `9e6d91c`, `0e36f7c`, `4490077` | Báo cáo 100 seed trên `49ba852`: lần đầu **G3m, B3, B4 đạt**. Còn trượt B1, B7 và vế "tốt nhất ≤ 97 %" của G3c. 9 vòng chỉnh sau đó không giữ được vòng nào. Âm Q6: `hit.t1`/`t2`/`t4` | Đạt (lỗi nhỏ) |
| dragon-hold | `61d372f` | Bảng giọng giữ đúng độ dài âm đang phát (`synthMs`) cho các đích Q6 dài hơn | Lượt kiểm tra vòng 3: **chưa đạt**. Dải nhàn ≤ 20 % riêng của game (D27) che việc B1 trượt theo dải chung ≤ 10 % cho cả 6 bot; không tài liệu nào đề xuất D27. D29 hạ sàn đọc được (stagger khoảng 0,34 s so với canon 0,6 s) |
| cha | `3bc8322a` | Q6 sửa sau review: TS hit, gỡ thump/thud, `gen.sa3` chặn từ Q6, `test_sa3_q6.py` | Đạt (lỗi nhỏ) |

Test audio-lab trên Dell:
- Lệnh: `AUDIOLAB_HOME=$HOME/AudioLab ~/.venvs/audiolab-tests/bin/python -m pytest -q specs/tests gen/tests`, chạy trong `tools/audio-lab`. Venv chỉ phục vụ test (numpy, scipy, soundfile, soxr, librosa, pyloudnorm, pyyaml, jsonschema, pytest, ghim theo `requirements.txt`); không có mô hình.
- Kết quả: 206 đạt, 2 trượt. Hai test trượt vì 14 thẻ S1 của Tuyến Cuối chưa có bộ đọc trong `specs/readers/typing_survival.py`.
- Phải đặt `AUDIOLAB_HOME`. Nếu không, `pytest.ini` tạo một thư mục tên đúng nguyên chữ `$AUDIOLAB_HOME` ngay trong `tools/audio-lab` (đã bị gitignore).

- 25/10 (sáng), **bước C: sửa sau kiểm tra (đã push)**. Phần làm xong ở cả 4 làn. Kiểm tra độc lập của 3 game bị ngắt vì giới hạn phiên, đang chạy lại; làn âm đã đạt.

| Repo | Commit | Nội dung |
|---|---|---|
| dragon-hold | `915a888`, `d5fd0fb`, `212167f`, `06cd4e6` | B1/B7 chấm theo **dải chung** BALANCE §3 và in thêm dải D27. Cả hai vẫn trượt: nhàn I của 6 bot 16,4–30,6 %. D27 thành "đề xuất của vòng 3, chờ chủ dự án xác nhận". Luật cổng giữ sàn canon (1,5 s mỗi cổng, 0,6 s giữa làn); khi cổng giữ một nhóm, cả đợt chờ; G9 1,40. Đọc được ở 70 và 100 WPM (GPU). Thử 4 vòng B1/B7, không giữ vòng nào |
| typing-defense | `e2757fd`…`0fc83a8` (7) | Gói JS khởi động 77,2 kB < 85 kB, `pnpm build` tự kiểm. G5 chấm mọi bot, đạt (cao nhất 12,4 %). `PACE.speedK` 0,3 (chờ chủ dự án xác nhận). B3 đạt; đích chặt 4/6 bot như R1. Còn trượt: B1 (Ẩu, Chậm chắc ở bộ 2), G3 bộ 2. `BUILD_NOTES` §7.4 |
| typing-survival | `ce953b8`…`5766ea4` (7) | Tách `aim.ts` cho ngân sách dòng; băng Xung chương không lẫn sang Trận thử; định nghĩa B4 vào `BUILD_S1` §11.3; kịch bản `survival-s1-latency` (phím tới khung/tới đạn trên GPU); cần `drainRate` cho từng ải. 6 vòng thử mỗi họ cổng, không vòng nào giữ. Báo cáo 100 seed: **cổng R1 vẫn chưa đạt** (B1, B7, G3c vế "tốt nhất") |
| cha | `c18f1a2c`, `559bc106`, `b88cb0ca` | Âm Q6: thẻ cho 14 id S1, bộ chấm đọc `loop_eval`, thêm từ cấm cho `gen.sa3` (kiểm tra: đạt). Canon D27/D29. Changelog ngày |

## 5. Đang làm

- Chạy lại kiểm tra độc lập của bước C cho dragon-hold, typing-defense, typing-survival (workflow `phase-c-review-fixes`, chạy tiếp bằng cache).
- Nếu phiên bị ngắt: đọc `git log` và `git status` của từng repo rồi chạy tiếp từ trạng thái đó. Kết quả chạy nằm ở `games/<game>/tmp/dell-2026-10-2x/`. Script workflow để chạy tiếp được chép vào `.local/workflows/` (gitignored).

## 6. Còn lại, theo thứ tự

### A. Còn sót sau kiểm tra độc lập (gộp vào lượt B của từng game)
- **dragon-hold** (lớn):
  - `docs/changelog/2026-10-24-m0a-review2.md` (hàng GPU của `dh-hitstop-keys`) nói số trong bão "chạm 0 lần, theo box và theo nét vẽ". Tài liệu cũng ghi sai nguyên nhân của mẫu "touching 1" ở lần chạy GPU đầu. Phải viết lại cho đúng những gì lần chạy chứng minh.
  - Phụ: `dh-crowd` ở 1920 chỉ lấy được 1/3 lần đo, vì Rồng gục. Thử seed khác.
  - Phụ: kit `feedback/numbers.ts`: chữ số nghiêng tràn ô atlas 48 px; dấu của nhãn lấn sang ô số "3".
- **typing-defense** (nhỏ): thẻ tháp, trại lính, mỏ vàng và ruộng vẫn tràn chữ ở nút bán và "Gửi Draconis" khi ở 1280×720. Check `typedInTheWindow` của `td-1a6-perf` dễ chập chờn (29–35 phím, cần ≥ 30).
- **typing-survival** (nhỏ): G3m chỉ đo seed 1–16 trong test; seed 17–32 là bước tay. Thời gian chạy báo cáo trong `AGENTS.md` cần sửa thành 18–30 phút.

### A0. Lỗi kiểm tra lượt 1 (đã sửa ở lượt sửa, giữ để tra)
1. **typing-survival** (lớn): ô `COUNTERS` của Xung trên "Bầy sát vạch" được commit là ● (2). Đo seed 1–16 ra ○ (tỷ lệ 1,30); seed 17–32 cũng ra ○ (1,41). G3m chỉ đạt nhờ ô này, và changelog ghi sai lý do. Phải sửa bảng hoặc sức súng, chạy lại G3m, rồi sửa changelog.
   Lỗi nhỏ:
   - Bảng 100 seed lệch báo cáo 1 điểm ở khoảng 8 ô.
   - "14 400 trận" phải là 18 400 (có cả G3c).
   - Đếm cặp của hàng Trâu sai.
2. **typing-defense** (nhỏ):
   - Nút "Bán 10 Gỗ" và "Bán 10 Lúa" tràn chữ ở 1280×720.
   - Ghi "đã chọn theo đề xuất (b)" cho quyết định thiết kế ở §7.2.
   - Comment `heroMul` còn ghi 0,5 (số đúng là 0,35).
   - Báo cáo `td:balance` vẫn chấm B7 gộp theo dải cũ.
3. **dragon-hold** (nhỏ):
   - Bước B9 chưa cảnh báo phím tốc độ lùi một số khi đã có "Số đo".
   - Selector toast trong `dh-pace` sai.
   - Ví dụ "85 %, CV 0,35 → × 1,88" ở canon §4.4 chỉ đúng với E ≥ 45.
   - `dh-hitstop-keys` bị kể là bằng chứng cho phần sửa số chồng nhau, dù chưa chứng minh được gì.
4. **space-typing** (nhỏ): `.gitignore` chặn cả README/LICENSE mới đặt cạnh model; changelog repo cha chưa có dòng trỏ sang.

### B. Việc tiếp theo của từng game
- **typing-defense**:
  - Chủ dự án chơi bản đồ 1 tới boss ở 1280×720 (`BUILD_1B.md:627`, kịch bản §22) và bấm "Chép số chơi thử" để có số cho B9.
  - Cổng cân bằng R1 còn trượt (`BUILD_NOTES.md:886-893`): B1 bộ 1 (Chậm chắc 92 %, Ẩu 73 %); B7 bộ 1 (91 %); đích chặt gộp. Khoảng 15 bộ số thử đều không gỡ được.
  - Đề xuất (b): sang R2, nâng "Bắn mạnh nối" cùng lúc làm Đêm 1–4 khó hơn.
  - Sau đó làm R2, R3 (`BUILD_1B` §17).
- **typing-survival**:
  - Cổng R1 chưa đạt: B1, B3 (Trẻ em ở Thư giãn), B4, B7, và vế "tốt nhất ≤ 97 %" của G3c.
  - Bước kế theo `docs/changelog/2026-10-24-s1-r1-fix.md:213`: làm lại sức các súng mạnh (Tán, Tia trực tuyến, Pháo Sao) cùng nhịp ải 1–4; đo bằng `tmp/dell-2026-10-24/scripts/g3c-all.sh` và `b1-all.sh`; rồi chạy lại báo cáo 100 seed.
  - Sau đó làm R2 (`docs/BUILD_S1.md:531-538`).
- **dragon-hold**:
  - Làm 9 mục "Cần anh quyết" theo đề xuất. Bảng đề xuất ở `docs/changelog/2026-10-24-m0a-review2.md:132-144`, bắt đầu với Nhàn I (B1, B7), rồi chạy lại `pnpm dh:balance`.
  - Chủ dự án chơi thử B9 với tốc độ đã chọn.
  - Sửa `box()` ở `shared/game-kit` feedback/numbers.ts (kit drift), rồi chép lại vào game.
  - Sau đó sang M0b.
- **space-typing**: lõi Space chưa có bước kế được ghi sau 21/10. Ứng viên: phần "Còn lại" của `docs/changelog/2026-10-21-fix-batch-1.md:44-55`, lộ trình §5 của `docs/changelog/2026-10-21-code-review.md`, mục 5 của file process 17/10. Bước S8 "Dọn Space" của `SPLIT_PLAN.md` chờ 2 tuần ổn định hoặc chủ dự án đồng ý.
- **audio-lab**: lô 1 đã sinh và dựng 6 phiên nghe trên Mac (`tools/audio-lab/SESSION_1_*.md`), chủ dự án chưa chấm. Chỉ sinh âm được trên Mac.
  - Theo Q6 (24/10), họ lửa của Rồng Giữ Ải phải sinh lại ở lô 1c, vì hướng "phụt tròn" đã bị bỏ.
  - Trước đó, trên Dell, phải viết lại thẻ spec (`tools/audio-lab/specs/**`), `docs/audio/*` và `src/audio/catalog.ts` của ba game theo Q6. Bước A đã xong, nên giờ làm được.

### C. Môi trường Dell
- **Đã có (24/10): đo bằng GPU qua Chrome Windows.** Chrome Windows 155 dùng RTX 3050 Ti qua ANGLE D3D11, đo được khoảng 238 khung/giây với Rồng Giữ Ải.
  - Node portable Windows: `D:\_tools\node-v24.11.0-win-x64\node.exe` (đã kiểm sha256).
  - Cách chạy:
    1. Chạy Vite của game trong WSL.
    2. Từ PowerShell đặt `$env:URL` và `$env:OUT_DIR`.
    3. `& D:\_tools\node-v24.11.0-win-x64\node.exe <game>\src\kit\tools\cdp-run.mjs <kịch bản> --width= --height=`.
  - Phần cần tsx/esbuild (replay, so mã băm) chạy trong WSL, vì `node_modules` là bản Linux.
  - Chrome trong WSL chỉ có SwiftShader: dùng cho kiểm chức năng, không dùng để đo hiệu năng.
- ImageMagick 7.1.2-34 (`magick`): đã cài 24/10 từ bản phát hành chính thức trên GitHub (AppImage, giải nén sẵn), ở `~/.local/bin/magick`. `local-env.sh` đưa `~/.local/bin` vào `PATH`. `td_rig_review.py` dùng nó để ghép bảng ảnh duyệt rig.

### D0. Trạng thái 25/10 sáng (đọc mục này trước mục D)
- **Tu Tiên Thủ Ải = repo `immortality-cultivation`.** Chủ dự án tạo repo `sinhvienaiti/immortality-cultivation`; đã gắn làm submodule `games/immortality-cultivation` (commit `6ab88f87`).
- **Hướng hình (chủ dự án, 25/10):** 3D trước, có đo bằng bench HN0. Chỉ phần nào trượt ngân sách mới lùi xuống bản nhẹ hơn.
- **M0 Canon xong:** `docs/games/tu-tien/00-canon.md` (D01–D46) và `M0A_PLAN.md` (bước 0 + 8 làn), đã qua phản biện `analysis/09`, commit `07b31720`.
- **Menu portal và nginx có game thứ 9:** commit `6c44135b`, do Codex làm ở phiếu 004. Play mode trong WSL phục vụ 10 host. Chủ dự án chạy `scripts/windows/add-hosts.ps1` (quyền Administrator) để thêm host vào Windows.
- **Đang chạy:**
  - M0a đợt A (workflow `tu-tien-m0a-part-a`, script chép ở `.local/workflows/tu-tien-m0a-part-a.js` để chạy tiếp): bước 0 khung repo, rồi làn 1a, 2, 3, 5, 8, rồi kiểm tra độc lập.
  - Đợt B: làn 1b bench HN0 đầy đủ, làn 4 Kiếm/combat, làn 6 view, làn 7 bot/cổng.
- **Codex** (hàng việc `docs/CODEX_QUEUE.md`, bộ chạy `tools/codex-run`, model `gpt-6.1-sol`):
  - Ảnh Rồng Giữ Ải M0 đã xong 67/67; phiếu 006 làm lại các ảnh lỗi.
  - Ảnh 2D bậc VS của Lời Gọi (005a, 005b).
  - Bộ prompt và ảnh của Tu Tiên (007).
  - Danh sách 3D của mọi game: `docs/games/3D_REQUESTS.md`.
- **Lời Gọi R2:** lượt sửa 2 xong và đã push (`c9a8edd`…`266e39d`):
  - G3, G8 chấm theo từng bộ seed; chunk tải lười có đường lùi; gói khởi động ở `/` 82,56 kB; perf đo ở 60 Hz.
  - B1 vẫn tệ hơn R1 và G3 bộ 2 vẫn trượt sau khi thử đủ các bước §6.5. Hướng chỉnh kế tiếp ghi cho R3.
  - Bước kiểm tra độc lập của lượt này chưa chạy, vì bị giới hạn phiên. Chạy lại khi rảnh.
- **Chủ dự án duyệt ảnh bản sắc Tu Tiên (25/10):** ảnh nữ kiếm tu chưa đủ quý phái và hoàng tộc (D47); ảnh cảnh ải phóng to quá, phải thấy trọn sân (D48).
  - Chủ dự án muốn nhiều nhân vật, nên có thêm D49 (đề xuất): mỗi trường phái có 1 nam, 1 nữ.
  - Codex phiếu 008 (vẽ lại) và 009 (chân dung cả danh sách) chạy sau khi hạn mức ChatGPT mở lại lúc 08:56.
  - **008 xong, chủ dự án duyệt** ("khá đẹp… pass"): chân dung A (miện ngọc) là chuẩn phong cách; cảnh 55° là góc camera mặc định (canon D47, D48).
- **Danh sách toàn bộ ảnh Tu Tiên (25/10, 09:40):** `docs/games/tu-tien/art-requests/IMAGE_LIST.md`.
  - 159 ảnh chia 7 lô (A nguồn 3D, R nhân vật, E môi trường, V VFX, I biểu tượng, U giao diện và Sơn Môn, T Tĩnh Tu); 46 ảnh đã có.
  - Phiếu Codex 010a (E + V), 010b (I), 010c (U + T) sinh phần còn lại.
- **Codex nhận thêm việc ngoài ảnh** (chạy được lệnh WSL nhờ `-Sandbox danger-full-access`):
  - 012: công cụ hậu kỳ ảnh `tools/art-normalize` (alpha, lề, nền phẳng, liền mép, icon, ảnh xem nhanh), chạy trên ảnh Rồng Giữ Ải còn lỗi;
  - 011: phản biện độc lập lượt sửa 2 của Lời Gọi R2. Báo cáo ở `games/typing-defense/tmp/dell-2026-10-25/review3/REPORT.md`; Claude đọc rồi sửa nếu cần.
- **Hai làn Codex chạy song song** (`tools/codex-run/queue.ps1`, tự chờ khi gặp hạn mức ChatGPT):
  - làn A (ảnh): 009 → 007b → 005a → 005b, rồi 010a → 010b → 010c;
  - làn B (việc khác): 012 → 011.
  - Xem trạng thái ở `docs/CODEX_QUEUE.md`, log ở `.local/codex-runs/`.
  - **Nếu máy tắt giữa chừng:** chạy lại `queue.ps1` với cùng file danh sách. Bỏ dòng của phiếu đã xong; phiếu ảnh tự bỏ qua ảnh đã có.
- **Luật mới (chủ dự án, 25/10):** Claude duyệt kỹ mọi đầu ra của Codex trước khi commit: đọc diff, chạy test, phản biện nhiều góc. Ghi ở `docs/CODEX_QUEUE.md`.
- **Phiếu 009 xong:** 10 chân dung cộng ảnh đội hình. Ảnh xem nhanh ở `games/immortality-cultivation/art-src/_review/009-roster-sheet.jpg`. **Chờ chủ dự án chọn hoặc sửa** trước khi làm ảnh nguồn 3D.
- **M0a đợt A của Tu Tiên xong và đã push** (game `947bc5a`; repo cha nâng gitlink ở `2eccea5c`).
  - Gồm bước 0 và các làn 1a, 2, 3, 5, 8. Phản biện độc lập: đạt.
  - Phản biện nêu 3 lỗi lớn:
    - test ranh giới quá chậm trên `/mnt/d`;
    - camera 52° thay vì 55° (D48);
    - thiếu 11 dòng SYNC_DEBT.
  - Thêm 10 lỗi nhỏ. Kết quả đầy đủ ở `games/immortality-cultivation/tmp/part-a/result.json` (không vào Git).
- **M0a đợt B đang chạy:** workflow `tu-tien-m0a-part-b`, script `.local/workflows/tu-tien-m0a-part-b.js`.
  - Thứ tự: sửa lỗi phản biện đợt A → làn 1b (bench HN0 và phán quyết GPU), làn 4 (Kiếm, combat), làn 6 (view, HUD) → tích hợp `startApp` → làn 7 (bot, cổng, golden, kịch bản, gồm `ic-camera-frame`) → phản biện → sửa.
  - Bị ngắt thì chạy tiếp bằng `resumeFromRunId`.
- **Kế hoạch đưa game lên mạng:** `docs/HOSTING_PLAN_2026-10-25.md`.
  - Chủ dự án hỏi gói Free hay 5 USD có đủ không. Kết luận: đủ cho phần file (≈ 680 MiB phục vụ, không có giới hạn tổng); gói 5 USD chỉ cho backend.
  - Việc khó là mã: mọi game ghi cứng nguồn portal `https://typing-game.local`; API runtime của Admin và Duel chưa có chỗ chạy.
  - Đã qua 2 phản biện độc lập. Chưa làm bước nào; bước 0 là việc của chủ dự án (tên miền, thanh toán, nhạc riêng, 4 game luyện gõ).
- **M0a đợt A bị giới hạn phiên ngắt lúc khoảng 07:00.**
  - Bước 0 đã commit và push (`4ee8658`, `2443db6`).
  - 5 làn bỏ lại khoảng 71 file chưa commit. Workflow chạy tiếp từ cache; các làn được dặn làm tiếp phần dở trong đường dẫn của mình.

### D. Game tu tiên chống thú triều (mới, 24/10)
- **Đã xong: đánh giá** `docs/games/tu-tien/DANH_GIA_2026-10-24.md` (đọc trước), gồm 7 bản phân tích và 1 bản phản biện ở `analysis/`. Bản chụp đề xuất Codex nằm ở `source/`. Video QCBH ở gốc repo, không vào Git.
- **Kết luận:** nên làm, dưới dạng **game mới** `games/tu-tien` (cổng 3008), không phải mode của Rồng Giữ Ải.
  - Ba điểm mới so với các game hiện có: nhân vật tự đi trên sân, gõ vào thanh kỹ năng "Bàn Quyết" chứ không gõ lên từng con quái, và chơi đội 2–3 người.
  - Ngoài trận chỉ có 4 hệ lâu dài: cảnh giới, công pháp, pháp bảo, Thư Lâu.
  - Dùng 3 loại tiền. Sơn Môn là một màn tĩnh 4 điểm.
- **MVP** (khoảng 10–14 tuần):
  - Solo, có thể thêm 2 bot.
  - 1 chương = 1 ải.
  - 2 trường phái (Kiếm, Thổ thể), 2 cảnh giới.
  - Có Tĩnh Tu; chỉ Typing.
- **Chờ chủ dự án:**
  - Đồng ý bắt đầu.
  - Chọn hướng hình (lai GLB và sprite) sau buổi A/B có số đo. Đây là điểm duy nhất không tự làm theo đề xuất.
  - Các câu khác ở mục 8 của file đánh giá đã có đề xuất.
- **Bước kế khi được đồng ý:** M0 Canon (viết `docs/games/tu-tien/00-canon.md`, 2–3 ngày), rồi M0a hộp xám, song song với bản thử Tĩnh Tu.

## 7. Quay về Mac mini M4

### 7.1 Lấy việc của Dell về
Trên Mac, thư mục cũ vẫn còn **chính những thay đổi chưa commit** mà Dell đã commit. Làm theo thứ tự:
```bash
cd ~/htdocs/typing-game
# 1. Xem thay đổi còn trên Mac có khác bản đã push không (bình thường là giống).
for r in games/typing-defense games/typing-survival games/dragon-hold games/space-typing .; do
  git -C "$r" fetch origin && git -C "$r" status -sb | head -3
done
# 2. Ở mỗi repo con còn việc dở: cất đi rồi kéo bản của Dell.
git -C games/typing-defense stash push -u -m mac-before-dell-sync && git -C games/typing-defense pull --ff-only
git -C games/typing-survival stash push -u -m mac-before-dell-sync && git -C games/typing-survival pull --ff-only
git -C games/dragon-hold stash push -u -m mac-before-dell-sync && git -C games/dragon-hold pull --ff-only
git -C games/space-typing stash push -m mac-before-dell-sync -- media.md5 && git -C games/space-typing pull --ff-only
git stash push -u -m mac-before-dell-sync -- tools && git pull --ff-only
git submodule status
```
Khi đã chắc bản kéo về đủ, các stash `mac-before-dell-sync` có thể bỏ.

### 7.2 Những thứ trên Mac vẫn đúng
`~/AudioLab`, `~/.config/rclone`, node_modules của Mac, nginx 9 host vẫn dùng được, không cần cài lại.

### 7.3 Việc chủ dự án tự làm trên Dell (cần quyền quản trị, Claude không tự sửa cài đặt hệ thống)
- **Play mode trong WSL đã dựng lại (25/10).**
  - nginx có 10 host: thêm `dragon.`, `td.`, `survival.`, `tutien.typing-game.local`.
  - Chứng chỉ mkcert có đủ 10 tên.
  - Portal và 3 game đã build lại.
  - Trong WSL cả 10 host trả về 200.
  - `tutien` tạm là trang chờ (`games/immortality-cultivation/dist/index.html`, không commit) tới khi M0a có bản build.
- **Còn việc của chủ dự án:** thêm host vào hosts của Windows. Mở PowerShell bằng "Run as administrator" rồi chạy `powershell -ExecutionPolicy Bypass -File D:\typing-game\scripts\windows\add-hosts.ps1`.
  - Script đọc `HOSTS` của `scripts/setup-nginx.sh`, chỉ thêm host còn thiếu, sao lưu file hosts trước, chạy lại được nhiều lần.
- Nếu Chrome trên Windows báo chứng chỉ không tin: nhập `rootCA.pem` của mkcert trong WSL (`mkcert -CAROOT`) vào Windows.
- `pnpm media:setup` (đăng nhập Google) trước khi dùng `media:pull/push`.
- Chạy game không cần nginx: `pnpm --dir games/<game> dev` (dragon 3005, td 3006, survival 3007), mở `http://127.0.0.1:<port>`.

## 8. Dữ liệu ngoài Git (đừng xoá khi dọn)

- `games/*/tmp/`: bằng chứng cổng, ảnh phản biện, báo cáo cân bằng (dragon-hold 1,6 GB; typing-defense `tmp/review-r1`, `tmp/fix-r1`; typing-survival `tmp/review-r1`, `tmp/fix`). Là bản duy nhất của các lượt phản biện.
- `D:\typing-gamev2` (bản Windows trước thời Mac, 18/10): còn **bản gốc Meshy** mà `games/space-typing/art-src/3d/SOURCES.json` ghi là đã mất (`draconis-v2/v3/v4.meshy.glb`, `rainbow-scout-3d`, `dragon-fireball`, `auriel-hero.glb`, `draconis.blend`). `C:\Users\Admin\Downloads\dragon` cũng có bản tải Meshy. Cần chép về `art-src/3d/...` rồi `pnpm media:push --new-only --only originals`.
- `D:\typing-game2410.zip` (19 GB, chép từ Mac): giữ tới khi mọi thứ đã khớp.
- `D:\_mac-leftovers-2026-10-24`: node_modules và worktree cũ của Mac, xoá được khi đã chạy ổn.
- `~/AudioLab` chỉ có trên Mac. `tools/audio-lab/owner-data/` chỉ giữ điểm chấm lô 0a, 0b và giấy phép.
- `.local/admin/space-typing/*`, `games/space-typing/.account-local/`, `cloud/.dev.vars`: trạng thái local, gitignored.

## 9. Nhật ký cập nhật

- 24/10/2026 (Dell): tạo file. Audit, kiểm chứng, dựng môi trường WSL, bản chụp `wip/mac-2026-10-24` cho typing-defense và typing-survival.
- 24/10/2026 (Dell): repo cha commit `f3de2980` (khối Linux trong `local-env.sh`, file này) và `47faf42b` (lô 1 audio-lab từ Mac). Đã push.
- 24/10/2026 (Dell): chủ dự án chốt luật âm theo hình dạng hành động. Ghi vào `tools/audio-lab/DECISIONS.md` Q6 và `SESSION_1_DH.md` S2.
- 24/10/2026 (Dell): bước A xong.
  - Đã push 19 commit của 4 game (bảng ở mục 4).
  - Repo cha: nâng gitlink, commit canon Rồng Giữ Ải, chặn `*.mp4`.
  - Kiểm tra độc lập tìm ra lỗi; việc sửa ghi ở mục 6.A.
  - Mở việc đánh giá mode tu tiên (6.D).
- 24/10/2026 (Dell): lượt sửa sau kiểm tra độc lập xong.
  - 4 game push 7 commit; repo cha nâng gitlink.
  - Có đường đo hiệu năng bằng GPU qua Chrome Windows.
  - Changelog ngày `docs/changelog/2026-10-24.md` nay ghi đủ việc trong ngày.
  - Bản đánh giá Tu Tiên Thủ Ải đã commit (`707349e0`), chờ chủ dự án đồng ý mốc M0.
- 24/10/2026 (Dell, tối): bước B đợt 1, một phần, đã push.
  - Rồng Giữ Ải vòng 3.
  - Tuyến Cuối làm lại sức súng.
  - Âm Q6: 54 thẻ.
  - Kit: atlas chữ số.
  - Bị ngắt vì giới hạn phiên; chạy tiếp ở đợt 2.
- 25/10/2026 (Dell, 09:40): danh sách toàn bộ ảnh Tu Tiên (`IMAGE_LIST.md`).
  - Codex có phiếu 010a, 010b, 010c (ảnh), 011 (phản biện Lời Gọi R2 lượt sửa 2), 012 (công cụ hậu kỳ ảnh).
  - Thêm `tools/codex-run/queue.ps1`: hai làn Codex chạy song song, tự chờ khi gặp hạn mức.
- 25/10/2026 (Dell, trưa):
  - Luật duyệt kỹ đầu ra Codex.
  - Phiếu 009 xong: chờ chủ dự án chọn nhân vật.
  - M0a đợt A của Tu Tiên push xong, đợt B đang chạy.
  - Kế hoạch đưa game lên mạng `docs/HOSTING_PLAN_2026-10-25.md`.
