# Agent Skills cho Typing Game / Space Typing

Kiểm tra và cài ngày 20/10/2026. Các skill hướng dẫn agent; chúng không tự cài
Blender, trình duyệt, dịch vụ ASR hoặc cấp quyền dùng API trả phí.

Đánh giá lại sau cài đặt: [audit 20/10/2026](AGENT_SKILLS_AUDIT_2026-10-20.md)
ghi kết quả discovery, quyết định giữ/thay và đợt tinh gọn đã triển khai.

## Đánh giá và lựa chọn

Bộ yêu cầu phù hợp với project. Giữ 13 skill riêng theo hợp đồng nghiệp vụ, dùng
skill tổng quát cho kỹ thuật engine. Những bổ sung đã chọn:

- Ghi nguồn và commit của bộ skill bên ngoài để kiểm tra, tái tạo và nâng cấp có chủ đích.
- Phân biệt hợp đồng sản phẩm, code đang chạy và tài liệu nháp; không coi mọi mô tả
  trong prompt hay kế hoạch cũ là tính năng đã có.
- Kiểm tra discovery bằng `skills/list` của chính Codex, ngoài kiểm tra file.
- Đồng bộ Claude qua checksum, kiểm tra toàn bộ xung đột trước khi ghi.
- Dùng Node có sẵn; không thêm dependency hay sửa lockfile của game.

## Đã cài

Codex CLI đi kèm extension `openai.chatgpt-26.1007.21434` trong Cursor:
`codex-cli 0.162.0-alpha.17.2`. Node `v24.22.0`, npm/npx `11.19.1`, Git `2.56.0`.

OpenAI Game Studio được cài bằng `codex plugin add game-studio@openai-curated --json`.
Manifest `0.1.0`, cache revision `82fd64bc`. Plugin sở hữu chín skill:
`game-studio`, `three-webgl-game`, `web-3d-asset-pipeline`, `game-ui-frontend`,
`game-playtest`, `sprite-pipeline`, `phaser-2d-game`, `react-three-fiber-game`,
`web-game-foundations`. Không copy chúng vào repo.
Tên gọi qua catalog có prefix plugin, ví dụ `game-studio:three-webgl-game`.

Three.js pack: [majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills),
commit `8286774b22a2566bf894dbc825825c16921866af`, package `0.1.0`.
Đã đọc README, package.json, install.sh, entrypoint và helper liên quan trước khi cài.
Installer upstream có nhánh force/prune và lệnh xóa thư mục đích; không chạy nó.
Dùng `skill-installer` có sẵn của Codex để tải đúng commit vào `~/.agents/skills`.
Không chạy `npx` lấy phiên bản thay đổi hoặc tạo bản sao thứ hai ở `~/.codex/skills`.

Chín skill: `threejs-game-director`, `threejs-gameplay-systems`,
`threejs-aaa-graphics-builder`, `threejs-game-ui-designer`, `threejs-debug-profiler`,
`threejs-qa-release`, `threejs-3d-generator`, `threejs-image-generator`,
`threejs-audio-generator`.

Nguồn, revision và checksum được lưu ở [skill-sources.json](../.agents/skill-sources.json).
Global skills là thiết lập từng máy; bản ghi trong Git không tự cài chúng cho máy mới.
Khi cài lại, dùng skill-installer với repo, `--ref` nói trên, `--dest ~/.agents/skills`
và các đường dẫn `skills/<tên>`; installer từ chối ghi đè thư mục đã có.
Đọc và so sánh thay đổi trước mỗi lần nâng cấp, giữ sửa đổi cục bộ.

Kiểm tra lại skill ngoài bằng
`node scripts/verify-agent-skill-sources.mjs`. Script chỉ đọc các thư mục skill
đã ghi, so số file và SHA-256; không cập nhật baseline. `hashAlgorithm` trong
provenance ghi rõ locale `en-US`, các tùy chọn collator và Node/ICU đã dùng để
tái tạo hash. Sắp xếp từng thư mục rồi duyệt sâu; mỗi file đóng góp đường dẫn
POSIX tương đối, NUL, SHA-256 hex của byte gốc và LF. Không đổi CRLF hay sắp xếp
toàn bộ đường dẫn theo ASCII. Bỏ qua `.DS_Store`/`__pycache__`; từ chối symlink.
18 hash hiện tại được giữ nguyên. Phạm vi hash chỉ là từng thư mục skill;
scripts/references dùng chung ở cấp plugin chưa nằm trong các hash này.

## Skill riêng và routing

Nguồn canonical: [`.agents/skills`](../.agents/skills).
Với yêu cầu rộng bắt đầu ở `space-typing-director`; yêu cầu hẹp dùng specialist trực tiếp.
Router project chọn specialist kỹ thuật chính cho nhu cầu hiện tại; chỉ nạp thêm
khi có phụ thuộc cụ thể. Không cần bắt đầu lại workflow của mọi generic director.
Đọc package/renderer và phiên bản Blender thực tế trước khi áp dụng recipe ngoài;
không nâng dependency chỉ để khớp ví dụ. Asset reference hiện trỏ trực tiếp tới
Vanguard/Fleet, catalog ngoại hình và chính sách tier theo từng consumer.

| Phạm vi | Skill |
| --- | --- |
| Điều phối nhiều domain | `space-typing-director` |
| Stage, boss, combat, equipment | `space-typing-gameplay` |
| Input, composition, caret, sửa lỗi, accuracy | `typing-input-ime` |
| Voice, Hybrid, ASR và microphone | `voice-typing-runtime` |
| Duel real-time và projectile/impact | `realtime-duel-pvp` |
| Wallet, reward, unlock, Warp/stamina | `progression-economy` |
| Admin schema, save, preview và runtime | `admin-runtime-authoring` |
| Concept, Blender, GLB và animation | `game-asset-2d-to-3d` |
| Combat FX, SFX, BGM và announcer | `combat-vfx-audio` |
| Review UX người chơi/admin | `game-ui-ux-review` |
| Đo frame time, bộ nhớ và ngân sách render | `game-performance-quality` |
| Kiểm thử trình duyệt và bằng chứng hình ảnh | `space-typing-playtest` |
| CI, HEAD mới và tiếp tục công việc | `game-ci-resumable` |

### Skill theo từng game

13 skill trong `.agents/skills` viết cho Space Typing. Ba game tách ra theo
[kế hoạch tách](games/SPLIT_PLAN.md) dùng skill Game Studio, `threejs-*` và tài
liệu thiết kế của chính game; skill Space chỉ để tham khảo, không phải hợp đồng.

| Game | Skill | Nguồn thiết kế |
| --- | --- | --- |
| Space Typing (`games/space-typing`) | 13 skill dự án, bắt đầu ở `space-typing-director` | Tài liệu và `contracts/` của Space |
| Rồng Giữ Ải (`games/dragon-hold`) | Game Studio, `threejs-*` | [`docs/games/dragon-lane`](games/dragon-lane/DESIGN.md) |
| Lời Gọi (`games/typing-defense`) | Game Studio, `threejs-*` | `docs/` của game (trước khi tách: `docs/td` của Space) |
| Tuyến Cuối (`games/typing-survival`) | Game Studio, `threejs-*` | `docs/` của game (trước khi tách: `docs/survival` của Space) |
| Portal, nginx, script khởi chạy | `game-ci-resumable` khi tiếp tục CI/Git | [Kế hoạch tách](games/SPLIT_PLAN.md) mục 9–10 |

Thứ tự: yêu cầu người dùng và hợp đồng project → specialist engine → kiến thức chung.
[AGENTS.md](../AGENTS.md) chỉ chứa routing ngắn. Không tự đổi engine, thêm di chuyển
WASD hoặc dựng lại project từ scaffold vì skill generic gợi ý.

Các điểm cần hiểu đúng: input Campaign/Duel hiện chủ yếu nhận chữ tiếng Anh;
composition guard không chứng minh hỗ trợ tiếng Việt đầy đủ. Ma trận native IME
là yêu cầu kiểm thử khi thay input, không phải kết quả đã test trên Windows/macOS.
Defense V2 vẫn là bản nháp; `defense-bench.html` là benchmark riêng.

## Kiểm tra và đồng bộ

Chạy ở root của `typing-game`:

```bash
node scripts/validate-agent-skills.mjs
node scripts/verify-agent-skill-sources.mjs
bash scripts/sync-agent-skills.sh --dry-run
bash scripts/sync-agent-skills.sh
bash scripts/sync-agent-skills.sh --check
node scripts/inspect-codex-skills.mjs
git diff --check
git status --short
```

Validator kiểm tra YAML subset gồm các trường chuỗi, tên/folder, mô tả, placeholder
và đường dẫn Markdown/source trong bộ skill. Frontmatter phức tạp hơn cần mở rộng
parser có chủ đích; không coi đây là validator cho mọi cấu trúc YAML.

Sync một chiều từ `.agents/skills` sang `.claude/skills`, dùng Node 24 qua Bash
(macOS/Linux/WSL/Git Bash). Có thể gọi thẳng `node scripts/sync-agent-skills.mjs`
trên Windows. Không phụ thuộc symlink. Commit cả canonical, Claude copies và
`.claude/.agent-skills-sync.json` khi chủ dự án cho phép commit. Chỉ sửa canonical.
Nếu bản Claude đã sửa tay, file bị xóa hoặc có xung đột, script dừng trước khi ghi;
đọc diff, hợp nhất thay đổi vào canonical rồi chủ động hòa giải bản sao. Không có
force/prune và không tự xóa skill cũ.

Inspector mở app-server tạm, gọi `initialize` và `skills/list` rồi đóng lại.
Không tạo conversation hoặc gọi model; chỉ in metadata discovery, không in config/token.
Một runner sandbox có thể cần quyền khởi tạo CLI để chạy inspector.
Skill discovery không chứng minh browser/paid-provider capability hoạt động.

`skills/list` của bản CLI này liệt kê skill local; dùng `plugin/read` để kiểm tra
skill trong plugin. Inspector cũng hỗ trợ cách kiểm tra này:

```bash
node scripts/inspect-codex-skills.mjs --plugin game-studio \
  --marketplace-path "$HOME/.codex/.tmp/plugins/.agents/plugins/marketplace.json"
codex plugin list --marketplace openai-curated --json
```

Đường dẫn marketplace trên là snapshot thực tế của máy đã kiểm tra; khi đổi máy,
xem `codex plugin marketplace list` để tìm manifest tương ứng.

## Kết quả kiểm tra

- `quick_validate.py` của skill-creator: 13/13 pass, dùng PyYAML trong virtualenv
  tạm ngoài repo; không sửa Python hệ thống hoặc dependency game.
- Validator project: 13 skill, 0 lỗi, 0 cảnh báo; liên kết tới source/reference tồn tại.
- Codex app-server tại root: đủ 13 project skills và 9 Three.js user skills,
  tất cả enabled, không có lỗi discovery.
- `plugin/read` và plugin list đúng marketplace: Game Studio installed/enabled,
  9 skill namespaced đều enabled.
- Claude sync: 13 skill; lần chạy lại không có thay đổi, checksum manifest hiện hành.
  Fixture tạm kiểm tra cập nhật an toàn, sửa tay/xóa bản sao, xung đột trước khi ghi,
  bảo toàn skill không thuộc bộ này và tiếp tục sau gián đoạn.
- Review độc lập thử routing nhiều domain và tiếp tục CI khi thiếu log cũ: pass.
- Syntax scripts và `git diff --check`: pass. Không sửa runtime hoặc chạy full build
  cho thay đổi chỉ gồm skill/config/tài liệu/tooling.

Đợt tinh gọn sau audit giữ 13 skill và toàn bộ revision/hash ngoài. Bổ sung
verifier provenance không dependency; fixture kiểm tra hash chuẩn, file đổi/thêm/
xóa, symlink và cách tìm thư mục skill trong plugin. Chi tiết kiểm tra mới nằm
trong [phần triển khai của audit](AGENT_SKILLS_AUDIT_2026-10-20.md#triển-khai-sau-audit).

**Giới hạn scope đã kiểm chứng:** mở Codex trực tiếp tại `games/space-typing`
(một Git submodule riêng) chỉ thấy global skills, không thấy 13 skill ở parent.
Mở project `typing-game` và bắt đầu chat tại root để dùng bộ project skills.
Không tạo thêm bản copy/symlink trong submodule để tránh nguồn trùng và link sai.

Đợt cài ban đầu tạo `.agents/`, `.claude/`, `AGENTS.md`, tài liệu này và bốn script
quản lý skill; đợt tinh gọn thêm verifier provenance và cập nhật references.
Các thay đổi Git tồn tại từ trước được giữ nguyên; không commit/push. Trong
lúc thực hiện, một worker khác đã đưa child HEAD từ `1d62e596` lên `8941c1cc`;
không khôi phục về checkpoint cũ. Parent HEAD vẫn `1b6d90d2` tại lần kiểm tra.

## Tài liệu chính thức và thử trong IDE

[OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) mô tả
`.agents/skills`, progressive disclosure và gọi skill bằng `$` hoặc `/skills`.
Session hiện tại có catalog riêng; kết quả app-server mới không đồng nghĩa catalog
đang hiển thị trong chat đã reload. Mở một cuộc trò chuyện Codex mới trong Cursor
tại root project; nếu chưa thấy, reload cửa sổ Cursor.

Prompt kiểm tra không sửa code:

```text
Use $space-typing-director to inspect the current Space Typing project and tell me
which specialist skills should handle gameplay, typing/IME, 3D assets, UI/UX,
performance, CI, and browser playtesting. Do not modify code.
```
