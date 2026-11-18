"""Ghi báo cáo và trạng thái của riêng phiếu 221; mọi lệnh Git chỉ đọc."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = ROOT / 'docs/codex-queue/221'
REPORT = ROOT / 'docs/codex-queue/221-report.md'

def command(*args):
    return subprocess.check_output(args, cwd=ROOT, text=True)

def load(path):
    return json.loads((ROOT / path).read_text())

def allowed(line):
    path = line[3:].strip('"')
    return path.startswith('docs/codex-queue/221/') or path in {
        'docs/codex-queue/221-report.md',
        'docs/games/audio/firefly/typing-defense.md',
        'docs/games/audio/firefly/typing-defense.json',
    }

# Tạo tên file đầu ra trước khi chụp status, để bản sau liệt kê đủ các file của phiếu.
for path in [REPORT, HERE / 'status-after.txt', HERE / 'game-after.txt', HERE / 'state-check.json']:
    path.touch(exist_ok=True)
before = (HERE / 'status-before.txt').read_text()
after = command('git', 'status', '--short', '-uall')
game_after = command('git', '-C', 'games/typing-defense', 'branch', '--show-current') + command('git', '-C', 'games/typing-defense', 'status', '--short')
(HERE / 'status-after.txt').write_text(after)
(HERE / 'game-after.txt').write_text(game_after)
added = sorted(set(after.splitlines()) - set(before.splitlines()))
removed = sorted(set(before.splitlines()) - set(after.splitlines()))
concurrent_added = [s for s in added if not allowed(s)]
concurrent_removed = [s for s in removed if not allowed(s)]
protected = [
    'docs/games/audio/firefly/schema.json',
    'docs/codex-queue/212/check.mjs',
    'docs/games/audio/firefly/README.md',
]
md5 = {p: hashlib.md5((ROOT / p).read_bytes()).hexdigest() for p in protected}
expected = ['c37879d9b6b4a85470c10b92f937b538', 'ffbeee75450361fe957bd6d4493cbc7d', 'c0732e449f7e5e087460b796d686bb54']
state = {
    'gameUnchanged': game_after == (HERE / 'game-before.txt').read_text(),
    'gameBefore': (HERE / 'game-before.txt').read_text(),
    'gameAfter': game_after,
    'parentBeforeEntries': len(before.splitlines()),
    'parentAfterEntries': len(after.splitlines()),
    'taskAdded': [s for s in added if allowed(s)],
    'concurrentAddedOrChanged': concurrent_added,
    'concurrentRemovedOrChanged': concurrent_removed,
    'protectedMD5': md5,
    'protectedMD5Unchanged': list(md5.values()) == expected,
    'scopeStatement': 'Phiếu 221 chỉ ghi bốn gốc đường dẫn được cho phép. Status là ảnh chụp trạng thái Git, không chứng minh byte của các file làn khác không đổi giữa hai lần chụp; không sửa/dọn chúng.',
}
(HERE / 'state-check.json').write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')

check = load('docs/codex-queue/221/check.json')
selftest = load('docs/codex-queue/221/check-selftest.json')
data = load('docs/games/audio/firefly/typing-defense.json')
fired = load('docs/codex-queue/221/fired-ids.json')
evidence = load('docs/codex-queue/221/source-evidence.json')
exclusions = {e['id']: e for e in data['excluded']}
group_table = '\n'.join(f"| {g['name']} | {g['rows']} | {g['takes']} |" for g in check['groups'])
fired_table = '\n'.join(f"| `{f['id']}` | {str(f['map1']).lower()} | `{f['trigger']}` | {exclusions[f['id']]['reason'] if f['id'] in exclusions else '—; rows'} |" for f in fired)
gong_table = '\n'.join(f"| `{r['id']}` | {r['eraNote']} |" for r in data['rows'] if r['id'] in check['gongRows'])
without = ', '.join('`' + r['id'] + '`' for r in data['rows'] if r['specCard'] is None)
state_lines = '\n'.join(concurrent_added + concurrent_removed) or '(không có)'
own_lines = '\n'.join(state['taskAdded'])
reason_counts = {
    'Phím đúng thuộc 189–193': 1,
    'Loài chỉ ở hộp cát, chưa có ải truyện': 2,
    'Có khóa registry nhưng chưa có emitter': 1,
    'Giọng người do chủ dự án ghi': 1,
    'Nền chỉ có thẻ, chưa có mã phát': 1,
    'Nhạc theo đường riêng': 4,
}
reason_table = '\n'.join(f'| {reason} | {n} |' for reason, n in reason_counts.items())
md5_table = '\n'.join(f'| `{p}` | `{h}` |' for p, h in md5.items())
text = f'''# Phiếu 221 · Wordwoven · Map 1 · Danh sách âm Adobe Firefly

Ngày 30/10/2026. Làm tại repo cha, nhánh hiện có `{command('git', 'branch', '--show-current').strip()}`. Chỉ lập danh sách SFX cho `w1-silverfall`; chưa tạo âm, chưa nghe duyệt, chưa gắn vào game.

## Kết quả giao

Đã viết [bản chủ dự án đọc](../games/audio/firefly/typing-defense.md), [JSON theo lược đồ chung](../games/audio/firefly/typing-defense.json), [tập id phát](221/fired-ids.json) và [script kiểm](221/check.mjs). Danh sách có **61 hàng · 85 lượt dự kiến**, P0 **43**, P1 **30**, P2 **12**. Một lượt là một file kết quả dự kiến, chưa suy ra số thao tác/credit. `retired` có **0** mục.

Nguồn game được đọc **chỉ bằng `git show`/`git grep` object `td-1c`**, không đọc file checkout hay mở worktree bị cấm. Commit `td-1c`: `{data['sourceCommits']['td-1c']}`; `a2-days`: `{data['sourceCommits']['a2-days']}`. Checkout chính chỉ dùng lệnh branch/status/rev-parse để lưu trạng thái; không ghi `games/**`.

Có [source-evidence.json](221/source-evidence.json) lưu 30 thẻ đã đọc các trường when, purpose, prompt.text, duration, variants, playback; danh sách 65 id và nhóm tạo. [source-checks.txt](221/source-checks.txt) giữ các lượt grep âm nền, emitter và stdout xác nhận phím sai ở `646e889` (lệnh log đó chạy đúng **1 lần**). [make-data.mjs](221/make-data.mjs) dựng lại JSON/Markdown/fired-ids từ dữ liệu biên tập; [make-report.py](221/make-report.py) dựng báo cáo và chụp trạng thái, đều chỉ ghi trong phạm vi phiếu.

Đối chiếu pha bằng skill [game-vfx-layered](../../.agents/skills/game-vfx-layered/SKILL.md), VFX_STANDARD §3.1/§3.4; chỉ đọc mã và ghi ý đồ, không dựng VFX, không capture hay tuyên bố nghiệm thu hình/nghe. Các bước sửa game, changelog và kiểm hình của skill nằm ngoài phiếu chỉ viết danh sách, nên không thực hiện.

## Điều kiện trước

**6/6 đạt**, đầu ra từng lệnh ở [preconditions.txt](221/preconditions.txt). Commit chung 212 là `83217b53870b330d345d1ee8a97f82e0adee757d`. Đủ 5 hàm export, các trường cấp file và 3 trường hàng tùy chọn. Game `a2-days` sạch; `td-1c` resolve đúng mã. Có **30** thẻ. Ba đường đích chưa tồn tại trước khi tạo `221/`. Ba MD5 trước/sau đều khớp:

| File chỉ đọc | MD5 cuối, giống trước |
|---|---|
{md5_table}

## Bảy mục kiểm có số

| Mục | Số và kết quả |
|---|---|
| 1. Script kiểm thường | **Thoát 0**; thiếu **0**, lạ **0**, trùng **0**, lược đồ **0**, phép tính **0**, lệch thẻ **0**, ASCII prompt/tên **0/0**, tên riêng **0**, từ cấm **0**, phủ định **0**, cồng thiếu lý do **0**, lệch Markdown/JSON **0**. Xem nguyên stdout bên dưới. |
| 2. Selftest | **Thoát 0; bắt 3/3**: bỏ hàng map1=true, thêm id lạ, thêm chữ có dấu. Chỉ cài lỗi vào bản chép trong bộ nhớ. |
| 3. Tập id và sản lượng | **62/65** id mã có đường phát ở map 1; **0** id phát thêm; hợp mã/thẻ **71** id. **61** hàng, **10** excluded, **0** retired. Bảng nhóm và lý do loại ở dưới. P0 **43**, P1 **30**, P2 **12**, tổng **85** lượt. Prompt dài nhất `{check['longestPrompt']['id']}`: **{check['longestPrompt']['characters']} ký tự ASCII**. |
| 4. Truy số về thẻ/mã | **23** hàng có thẻ, giữ nguyên min_ms/max_ms/variants.target; **38** hàng specCard=null có đề xuất số và căn cứ file:dòng trong basis. Tất cả **61** hàng có targetMs, variants và basis; **0** lệch số thẻ. Các số không thẻ là quyết định biên tập dựa nhịp sự kiện, không giả làm hằng số âm có sẵn. |
| 5. Commit nguồn | `td-1c` **{data['sourceCommits']['td-1c']}**; `a2-days` **{data['sourceCommits']['a2-days']}**; script đọc lại refs, **0** lệch. Claude chạy lại sau khi merge hoặc ref đổi; phải rà căn cứ trước khi cập nhật hash. |
| 6. Checkout game trước/sau | **{'Đạt' if state['gameUnchanged'] else 'Khác do đồng thời'}**, game-before và game-after {'giống từng byte' if state['gameUnchanged'] else 'khác nhau; xem mục trạng thái'}. Nhánh `a2-days`; **{len(game_after.splitlines())-1}** dòng status sau. Phiếu này ghi **0** đường trong games/**. |
| 7. Repo cha trước/sau | Trước **{state['parentBeforeEntries']}**, sau **{state['parentAfterEntries']}** dòng status. Phiếu thêm **{len(state['taskAdded'])}** file, chỉ trong 4 gốc được cho phép. Có **{len(concurrent_added)}** dòng thêm/đổi và **{len(concurrent_removed)}** dòng mất/đổi ngoài phạm vi do làn đồng thời; liệt kê dưới, không chạm vào. |

### Ngoại lệ bắt buộc từ chính phiếu

Mục 1 đòi `map1` phản ánh khả năng phát; mục 6 lại bắt buộc **key-right vào excluded** vì thuộc bộ 189–193. Do đó giữ `key-right.map1=true` (không khai sai thành false), excluded có `firstStage=w1-silverfall`; luật “map1=true phải là rows” có đúng **1 ngoại lệ nguồn**, được công khai trong check.txt/check.json và script. **61** id map1 còn lại đều là hàng. Nếu áp nguyên văn cả hai mệnh đề mà không có ngoại lệ thì không thể đồng thời thỏa; Claude/chủ dự án cần xem quyết định này. Kiểm thường vẫn báo 0 lỗi theo chính sách nguồn cụ thể ở mục 6.

### Nhóm buổi tạo

| Nhóm | Hàng | Lượt |
|---|---:|---:|
{group_table}

Mỗi id rows thuộc đúng một nhóm. UI và nền có **4 UI**, **0** nền loop; toàn danh sách **60** hits, **1** single (`boss-lull`), **0** loop.

### Loại theo lý do

| Lý do | Id |
|---|---:|
{reason_table}

Hai id ngoài sóng truyện: `direct-pin` (Zombie Leader), `direct-shield` (Troll), chưa có ải đầu nên firstStage=null. Không suy đoán map sau. `amb-dusk` chỉ có thẻ: grep `amb-` **0 dòng**, grep `dusk` **6 dòng** chỉ màu/ảnh. Bốn music-* theo đường nhạc riêng ở `src/view/music.ts`, không thành hàng SFX.

**Phát hiện so với dự kiến đầu phiếu:** `feather-fall` chỉ có khóa FIRES (sound-map.ts:13), `ult.drop` (ult.ts:102–110) gọi P.add trực tiếp; P.add (projectiles.ts:33–46) không đẩy ring. Toàn src chỉ `combat.ts:86` đẩy FX.fire, và lông không đi qua launch đó. Vì vậy **map1=false, firstStage=null**, không tạo hàng giả. Lông lửa vẫn rơi và phát `blast` lúc chạm. Thời gian bay lông được ghi ở excluded.basis cho phiếu gắn: SPEED=12 m/s, FROM dài 9,6 m, fallS=0,8 s, khoảng **48 khung** với đích đứng yên. Không sửa mã để mở id trong phiếu này.

38 hàng không thẻ: {without}.

## Nguyên stdout kiểm

```text
{(HERE / 'check.txt').read_text().rstrip()}
```

## Nguyên stdout selftest

```text
{(HERE / 'check-selftest.txt').read_text().rstrip()}
```

Kết quả máy đọc ở [check.json](221/check.json) và [check-selftest.json](221/check-selftest.json). Validator import của 212 kiểm đúng tập từ khóa lược đồ đang dùng; import không chạy CLI 212, MD5 file 212 không đổi. Phủ id được tự kiểm, **không dùng audit 212**, nên sáu id chỉ có thẻ được excluded đúng phạm vi.

## fired-ids rút gọn (65/65)

Đường trong trigger và map1Basis tính từ gốc object `td-1c`, không phải dòng của checkout `a2-days`. `map1=true` nghĩa có đường gọi âm khi đủ điều kiện, không phải luôn phát mọi ván và không phải đã có file thật. `bus` giữ đúng busOf: `wordshot-fire` là world, khác họ `word-*` có dấu gạch. `sourceEvent`, `firstStage` và đầy đủ căn cứ nằm trong JSON.

| Id | map1 | Trigger td-1c | Lý do loại / nơi xử lý |
|---|---|---|---|
{fired_table}

`day-countdown` và **4** id `ui-*` đều đã có trong SOUND_IDS.made, nên phát thêm **0**. Tiếng gọi màn tựa gọi goi trực tiếp không có id, được giải thích riêng dưới, không bịa entry trong fired-ids.

## Âm có cồng, chủ dự án ký duyệt

Theo AUDIO_PIPELINE §8.2, mỗi âm có cồng phải được chủ dự án duyệt riêng; chưa coi danh sách hay validator là đã nghe duyệt.

| Hàng | Lý do |
|---|---|
{gong_table}

**3 hàng**, mỗi eraNote chứa `gong:`. Các tiếng báo khác chọn kẻng sắt/trống hội; boss-phase bỏ cồng của mã cũ, giữ nứt vỏ gỗ và chuông đồng nhỏ để không dùng cồng tùy tiện.

## Việc ghi âm của chủ dự án, ngoài Firefly

**amb-villager-call — giọng người, chủ dự án ghi âm.** AUDIO_PIPELINE §3.2 **dòng 129**: chủ dự án/người nhà ghi **4 biến thể**, có giấy đồng ý, không dùng AI. Thẻ `tools/audio-lab/specs/typing-defense/amb-villager-call.yaml:13,96,102,170` ghi voice, owner-recording, chặn bởi chủ dự án ghi âm và giấy đồng ý. Không có prompt Firefly cho mục này.

Mã **vẫn có** tiếng gọi tổng hợp ở màn tựa: `src/view/audio-min.ts:119–124` gọi `goi` mỗi **3–7 s**, trái/phải, qua `src/view/folk.ts:135` mà không qua id. Phiếu gắn sau phải cho tiếng này đi qua **amb-villager-call** rồi dùng bản ghi thật. `firstStage=null` ở excluded nghĩa chưa có ải phát nó qua id, không phải màn tựa đang im. Không sửa hay tạo âm thay thế ở phiếu 221.

## Chọn chất liệu khi thẻ cũ lệch bible

ART_DIRECTION §2 và cột “Tiếng bible đòi” §8.2 thắng thẻ/THEME_SOUND_LIST về cách diễn; độ dài và biến thể vẫn giữ thẻ. Hướng mới là **cõi đá vôi huyền ảo hùng vĩ**, không gian sân đá và thung lũng; giữ độ nhỏ của phím, UI và cung, không biến mọi nguồn thành tiếng boss. Luật cứng AUDIO_PIPELINE §8.2/TK 22.1 giữ nguyên. Prompt khẳng định, ASCII, không tên riêng, không âm tôn giáo, không chất liệu điện tử hay nhạc cụ nước khác dán nhãn Việt; sáo là ống mở sạch, không rè màng.

| Hàng/họ | Khác nguồn cũ | Cách chọn |
|---|---|---|
| word-hit | Thẻ/THEME_SOUND_LIST:32 dùng đàn tranh | Chuyển chuông đồng nhỏ theo §8.2; giữ **640–960 ms**, **7** biến thể, 6 cao độ + 1 luyến là đề xuất chưa phải ngân hàng engine theo nốt. |
| call-harvest / Reap | Thẻ dùng chuông | Theo §8.2 chọn liềm cắt và sột lúa; giữ **720–1080 ms**, **1** biến thể. |
| call-quiz / Quiz | Thẻ dùng sáo | Chọn chuông theo chuỗi chất liệu lời gọi của §8.2; giữ **280–420 ms**, **1** biến thể. |
| dawn | Thẻ/THEME_SOUND_LIST:47 là câu sáo | Chọn gà gáy xa và gió bình minh theo §8.2; **800–1200 ms**, **1** biến thể. Gà là động vật, không phải giọng người. |
| key-wrong | Thẻ nói giữ tổng hợp | Mục 6 giữ hàng riêng; phách tre lệch theo §8.2, **32–48 ms**, **2** biến thể; log 646e889 xác nhận tiếng phím sai riêng. |
| UI, coin | Thanh tre/khay gỗ làng nhỏ | UI dùng gỗ sơn mài, giấy, đồng nhỏ theo §2/§8.2; coin chạm khay gỗ sơn mài. |
| wordshot-fire, arrow-fire, blast, ink-puff | Đuôi vang làng, nổ trống/giấy chung | Đuôi thung lũng đá vôi ngắn/thấp, Word Shot thêm ting cao; blast nổ ba lớp và mảnh đá; giữ số thẻ. ink-puff vẫn là id chết chung, không giả có âm từng loài. |
| Boss, direct-break, helper-panic | Chuông/cồng hoặc gõ ngắn của SYNTH | Gỗ cổ thụ/rễ/đá đúng cỡ boss; ngắt là trống ngừng, Helper chân/lông. Không thêm lời hô người vào prompt. |

`era=kept` ở word-hit-bell vì giữ cách diễn chuông của thẻ; các hàng còn lại `reworded` ghi đổi quy mô/chất liệu hoặc là đề xuất chưa có thẻ. Không sửa thẻ cũ, THEME_SOUND_LIST, README hay schema.

## Nhịp VFX và giới hạn tích hợp

- **Fort:** 34 m/s, 9 m → khoảng **265 ms**, **16 khung**. **Archer Tower:** 30 m/s, 10/11/12 m → **333/367/400 ms**, **20/22/24 khung**. **Cannon Tower:** 18 m/s, 9/9,5/10 m → **500/528/556 ms**, **30/32/34 khung**. Nguồn slice-1a.ts:25–30,41–59, compile.ts:42.
- **Word Shot:** rewards.ts:55 dùng attack của tháp, không có tốc độ riêng: cùng dải **333–400 ms** hoặc **500–556 ms**. Fort đi bolt (rewards.ts:51). **Draconis:** 20 m/s, 9 m → **450 ms**, **27 khung** (slice-1a.ts:148, agents.ts:166). Đây là ước tính rìa tầm, đích đứng yên; sim theo đích di chuyển và tick, không phải độ trễ mới.
- **Trúng/chết:** FX.hit khi tới đích đơn còn sống, FX.burst khi splash tới điểm, FX.death khi chết. R ở nguồn phải trước I; chuẩn bị đòn chữ trong gõ, không đợi file chạy hết.
- **Boss:** roots **1,5 s/90 khung**; slam và keep **1,2 s/72 khung**; drain **1,2 s/72 khung**, đều nhân warnK (relax/learn **1,33**, balanced **1**, challenge **0,8**) rồi quy tick. Summon **0,8 s/48 khung** không nhân warnK. Cửa sổ có thể dưới mức boss ≥72 khung của VFX_STANDARD §3.4; chỉ ghi hiện trạng, không đổi sim. boss-slam dùng cả keep hit; slam/keep báo đầu hiện không trả id. boss-summon hiện cùng id cả báo và chạm. drain-hit có thể chồng leak cùng tick. Phiếu gắn phải xử lý chọn/cắt và nghe chồng, không suy diễn prompt là đã tích hợp đúng.
- **61/61** hàng có `clips=[]`, cùng clipsWhy “docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven”. Đọc FxPool tuổi 0/đuôi, FxPipe, fx-2d và boss-2d chỉ cho căn cứ view; chưa có clip Wordwoven để ghép.

## Bible đòi nhưng mã chưa có id

Đây là danh sách cho phiếu gắn/thiết kế sau, **0 hàng bổ sung** ở JSON:

- Tiếng riêng theo từng loài khi ra, đi (loop), đánh, trúng và chết; Hopping Zombie, Ghost Flame, River Serpent, Sapling, Raccoon Dog, Split Blob và Little Blob. hit/ink-puff còn dùng chung.
- Phân pha và chất liệu đủ 5 pha của Fort/Archer Tower/Cannon Tower; tiếng cung cắm, nổ ba lớp riêng pháo, lửa hai lớp riêng Draconis hiện còn dùng chung các id.
- Draconis nón lửa/gầm riêng; trống tăng theo tiến độ Spell; mở emitter cho feather-fall nếu muốn file từng lông. Đã có id registry nên không bịa thêm id thay nó.
- Báo trước slam/keep riêng; phân âm báo và lúc mọc Sapling của summon. Không thêm chờ vào sim.
- Lính đâm giáo/hô ghi thật; Helper từng nhịp chân/giọng ghi; công trình bị đánh, đổ nát và sửa riêng ngoài các id chung đã có.
- Nền thác/gió/chim theo cõi đá vôi, không lấy thẻ amb-dusk là đã phát. Seal Dais, Herb House, Lumber Camp ngoài sáu công trình map 1 nên chỉ nêu thiếu, không mở hàng.
- amb-villager-call theo đường chủ dự án ghi âm và giấy đồng ý, không Firefly.

## Firefly còn chưa biết

Giống README 212: **giới hạn ký tự prompt**, tùy chọn và phạm vi **độ dài file**, **số kết quả mỗi lượt thao tác/credit**, giới hạn tốc độ, hiệu quả gợi ý giọng, khả năng cắt loop liền, tỷ lệ dùng được và chất lượng khi lặp dày. Lô 189 từng xuất WAV **48 kHz stereo 16-bit khoảng 12 s** chỉ là quan sát của lô đó; không xác minh mới bằng mạng, không coi là giới hạn sản phẩm. **75%** dùng được là giả định, cần sửa sau lượt đầu. Prompt dài nhất **{check['longestPrompt']['characters']}** ký tự chưa được thử trên giao diện. Không phát sinh file âm hoặc thư mục inbox.

## Trạng thái trước/sau và phạm vi ghi

[game-before.txt](221/game-before.txt) và [game-after.txt](221/game-after.txt): **{'giống từng byte' if state['gameUnchanged'] else 'khác'}**.

```text
{game_after.rstrip()}
```

Ảnh chụp repo cha đầy đủ: [status-before.txt](221/status-before.txt), [status-after.txt](221/status-after.txt), đối chiếu [state-check.json](221/state-check.json). Repo vốn bẩn; không dọn thay đổi của làn khác. Những dòng mới thuộc phiếu:

```text
{own_lines}
```

Ngoài phạm vi, thêm/đổi hoặc mất/đổi so với ảnh chụp đầu (liệt kê nguyên từng đường, không khẳng định nội dung của làn khác):

```text
{state_lines}
```

Không chạy Git có ghi, không commit/push/reset/clean/stash; không đổi nhánh, không worktree; không mạng, dev server, trình duyệt, build hay test suite game. Không mở làn bị cấm, không chạm Tu Tiên, không sửa tools/** hoặc shared/**. Không tạo ảnh vì phiếu chỉ lập danh sách âm; không tạo/tải/sửa âm vì chủ dự án tự tạo SFX và tự ghi giọng người. **Claude duyệt rồi commit**, sau đó chủ dự án dùng Markdown để tạo âm; các mục cồng, ngoại lệ key-right và emitter feather-fall cần được đọc trước khi giao lô.
'''
REPORT.write_text(text)
print(json.dumps({k: state[k] for k in ['gameUnchanged', 'parentBeforeEntries', 'parentAfterEntries', 'protectedMD5Unchanged']}, ensure_ascii=False))
print('file của phiếu:', len(state['taskAdded']), '; dòng đồng thời thêm/đổi:', len(concurrent_added), '; dòng mất/đổi:', len(concurrent_removed))
