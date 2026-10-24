# Audit Agent Skills — 20/10/2026

**Cập nhật:** bốn cải thiện nhỏ đã được triển khai sau khi người dùng đồng ý;
xem [kết quả triển khai](#triển-khai-sau-audit). Các phần audit bên dưới giữ lại
trạng thái và đề xuất tại thời điểm đánh giá.

## Kết luận và phạm vi

Giữ bộ đang hoạt động; ưu tiên tinh gọn routing và cập nhật reference. Chưa có
bằng chứng để thay toàn bộ Majid bằng CloudAI-X, xóa phần lớn skill riêng hoặc
bổ sung bốn skill art/Blender/animation/VFX mới.

Đây là bước audit có giới hạn đã thống nhất: đọc nội dung, nguồn công khai,
kiểm tra discovery và lập phương án. Không cài/gỡ/nâng cấp plugin, sửa skill,
runtime, dependency, lockfile, cấu hình tài khoản hoặc commit/push.
Chưa chạy A/B bằng model, Blender hoặc playtest game trong lần này; không tuyên bố
bộ nào “tốt nhất” từ số lượng skill, stars hay điểm tự chấm.

## Hiện trạng có bằng chứng

[Dữ liệu kiểm tra](agent-skills/audit-2026-10-20.json) lưu thời điểm, HEAD,
metadata discovery, checksum và kết quả kiểm tra; không lưu thông tin đăng nhập.

| Hạng mục | Kết quả trực tiếp |
| --- | --- |
| Project skills | 13 canonical trong `.agents/skills`; Codex nhận và enabled cả 13 tại root |
| Claude copies | 13 bản sao; `--check` báo không có thay đổi, manifest hiện hành |
| Majid Three.js | 9 user skills nhận được và enabled; checksum 9/9 khớp provenance |
| Game Studio | Installed/enabled; `plugin/read` trả 9 skill enabled; checksum cache 9/9 khớp |
| System skills | App-server liệt kê 5, gồm `review-agent`; chưa thử gọi review-agent trong chat hiện tại |
| Superpowers | Marketplace 5.0.7; chưa installed/enabled |
| Plugin Eval | Marketplace 0.1.0; chưa installed/enabled |
| Mở riêng Space Typing | Thấy 0 project skills của parent; vẫn có 9 user skills |
| Monkeytype | Có `games/monkeytype/AGENTS.md`, quy ước SolidJS, lint/typecheck riêng |
| Blender | Không thấy qua PATH hoặc executable chuẩn trong `/Applications/Blender.app`; chưa kiểm tra mọi vị trí khác |

Parent HEAD: `1b6d90d28af81c9deaf245d571936ac7c166727a`.
Space Typing HEAD: `8941c1cc9ce5565d09da5921e057aabfc355a6dd`.
Monkeytype HEAD: `e27ec8ffc2e1b005538067dff2f74fdd5ccf93fa`.
Cây làm việc có thay đổi sẵn; SHA không đại diện toàn bộ nội dung dirty.

Majid pin commit `8286774b22a2566bf894dbc825825c16921866af`.
Game Studio marketplace pin `82fd64bce3869f0d4c0bb2bf0e36a6e262ca5ad8`,
manifest `0.1.0`. Xem [provenance](../.agents/skill-sources.json).
Checksum xác minh tính toàn vẹn so với bản ghi, không chứng minh chất lượng hay
việc đã audit an toàn toàn bộ mã của nhà cung cấp.

## Quyết định cho 13 skill riêng

“Giữ” nghĩa là chọn khi đúng task, không nạp tất cả mỗi lượt. Các entrypoint
đã đọc nằm trong [nguồn canonical](../.agents/skills).

| Skill | Quyết định | Giá trị riêng / cải thiện đề nghị |
| --- | --- | --- |
| `space-typing-director` | Giữ router | Parent/submodule, nhiều mode, kế hoạch khác runtime. Chọn specialist kỹ thuật chính, tránh mở thêm hai generic director. |
| `space-typing-gameplay` | Giữ | Stationary combat, letter ownership, typed completion, phân biệt Campaign/Duel/Defense. |
| `typing-input-ime` | Giữ | Composition guard khác hỗ trợ tiếng Việt; scoring/caret/native IME không thuộc kỹ thuật Three.js. |
| `voice-typing-runtime` | Giữ | Parent sở hữu ASR; game sở hữu target/completion/reward; session fences và Hybrid ownership. |
| `realtime-duel-pvp` | Giữ | Authority clock, travel rồi impact/damage, sequence/round identity, chống xử lý trùng. |
| `progression-economy` | Giữ | Warp, wallet authority, receipt/idempotency, migration, Practice boundary; không chỉ là economy chung. |
| `admin-runtime-authoring` | Giữ | UI → schema → revision → bridge → resolver → runtime; Draft/Published isolation. |
| `game-asset-2d-to-3d` | Giữ, ưu tiên cập nhật reference | Relief/GLB/Campaign 3D, sockets/clips/tier. Thiếu link trực tiếp tới tài liệu Vanguard/Fleet mới. |
| `combat-vfx-audio` | Giữ | Launch/impact/damage, chữ dễ đọc, phối hợp pronunciation/announcer. Shader recipes lấy từ specialist kỹ thuật. |
| `game-ui-ux-review` | Giữ lớp project; có thể rút gọn | Player typing và Admin workflow riêng; giảm checklist phổ thông khi sửa, giữ role/route/state và visual evidence. |
| `game-performance-quality` | Giữ lớp project; có thể rút gọn | Canvas/WebGL, mode/tier, typing responsiveness. Profiling chung lấy từ specialist khi cần. |
| `space-typing-playtest` | Giữ | Route/build identity, Portal/Test Lab/CDP, browser profile, native IME/audio evidence riêng. |
| `game-ci-resumable` | Giữ | Parent/child HEAD, gate hiện tại, worker đồng thời, continuation policy. Chưa nên dồn checklist dài vào AGENTS. |

Thay vì thêm bốn skill mới:

| Nhu cầu | Nơi xử lý đề nghị |
| --- | --- |
| Art direction | Asset skill giữ phong cách project; Majid graphics cung cấp critique; UI review kiểm tra chữ/HUD |
| Blender pipeline | Asset skill + Game Studio asset pipeline; thêm một bộ Blender chuyên sâu khi task thực tế cần |
| Rigging/animation | Asset skill giữ sockets/clips/runtime; chọn Blender specialist sau thử xuất GLB/phát animation |
| VFX/shader | Combat skill giữ event/readability; graphics cung cấp recipes; performance/playtest kiểm chứng |

Không gộp tất cả thành một entrypoint dài. Chỉ tách thêm khi quan sát được lỗi
routing hoặc thiếu hướng dẫn lặp lại qua task thực tế.

## Nguồn kỹ thuật công khai

| Nguồn | Đánh giá và lựa chọn |
| --- | --- |
| Game Studio đang cài | Giữ làm nền. `three-webgl-game` tự ghi độ sâu 3D thấp hơn nhánh 2D. Không áp mặc định Phaser/Rapier/DOM HUD để thay kiến trúc hiện hữu. |
| Majid đang cài | Giữ, dùng specialist chọn lọc. Director yêu cầu đọc năm production skills cho task rộng; không cần mở nó khi router project đã phân việc. Generator dùng theo task/provider thực có. |
| [CloudAI-X](https://github.com/CloudAI-X/threejs-skills) | Ứng viên cho API/rendering cụ thể. README nhắm r186, kiểm tra với `three@0.186.1`; game pin `0.170.0`. Phải kiểm tra API/chunks/import tương thích; chưa cài toàn bộ hoặc thay Majid. |
| [Scenario Labs Blender](https://github.com/scenario-labs/skills/blob/main/skills/dcc/blender/README.md) | Shortlist authoring chuyên sâu: 14 skill, sibling/shared scripts, Blender 5.2. Tác giả công bố 12 headless suites và giới hạn sculpt/hair/retopology; chưa tái chạy tại máy này. |
| [EL4CTEO Blender](https://github.com/EL4CTEO/blender-skills) | Shortlist export/QA: README có runner 50 headless tests, Blender 5.2. Chưa xác minh bằng artifact trong pipeline dự án; chưa chọn người thắng giữa hai bộ. |
| [Superpowers](https://github.com/obra/superpowers) | Framework của Jesse Vincent, không phải OpenAI viết. Marketplace 5.0.7 có trigger rộng, brainstorming approval/commit flow. Không chọn làm workflow bắt buộc toàn repo; đánh giá module và revision cụ thể khi cần. |
| Plugin Eval marketplace 0.1.0 | Chưa cần cài. Mã local ghi budget là `estimated-static`; live benchmark có thể copy `auth.json`/`config.toml` vào Codex home tạm. Thư mục tạm không đủ chứng minh cô lập. |
| GitHub / reviewer / security | Session có GitHub connector; app-server có system review-agent. Kiểm tra khả năng gọi/quyền khi cần; không thêm plugin chỉ để đọc Git cục bộ. |

Đây là shortlist dựa trên bản đang cài và tài liệu upstream, chưa phải audit
toàn bộ source/license/dependency của ứng viên. Trước khi cài: pin commit, đọc
LICENSE, executable hooks/scripts, dependency closure, đường dẫn ghi và truy cập
mạng. Các gate này phải qua trước khi so điểm chất lượng.
Nhận xét Superpowers ở trên áp dụng bản marketplace đã đọc, không mặc định cho
mọi revision upstream.

## Context và routing đề nghị

13 entrypoint project: **25.631 byte**; references: **56.485 byte**.
Tên + description: **2.982 ký tự**, chưa gồm path, định dạng catalog và các
system/global/plugin skills. Đây không phải token thực dùng.

[OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills) mô tả
metadata được nạp trước, nội dung đầy đủ đọc khi chọn skill. Không cộng mọi
reference để kết luận chúng đều tốn context mỗi lượt. Catalog nhiều skill vẫn
có thể bị rút gọn/giới hạn; phải xem session thực tế.

`AGENTS.md` đang có 19 dòng; không cần kéo lên 80–150 dòng.

| Task | Chủ hợp đồng project | Bổ trợ kỹ thuật khi cần |
| --- | --- | --- |
| 3D runtime | Gameplay hoặc asset theo ownership | `game-studio:three-webgl-game` |
| GLB/Vanguard/Fleet | `game-asset-2d-to-3d` | `game-studio:web-3d-asset-pipeline` |
| Nâng hình ảnh | Asset hoặc combat presentation | `threejs-aaa-graphics-builder` |
| HUD/menu | `game-ui-ux-review` | Chọn Game Studio UI hoặc Majid UI theo task |
| Chậm frame | `game-performance-quality` | `threejs-debug-profiler` |
| Kiểm chứng | `space-typing-playtest` | Chọn Game Studio playtest hoặc Majid QA theo tooling |
| IME/Voice/Duel/economy/Admin | Specialist project tương ứng | Bổ sung kỹ thuật ngoài khi cần |
| Monkeytype | AGENTS và source của Monkeytype | Không mặc định route sang Space Typing |

Task hẹp có thể chỉ cần một skill. Task nhiều domain mở thêm theo phụ thuộc thật.

## Các thay đổi cụ thể đáng làm sau audit

Đây là phương án tại thời điểm audit; các mục 1–4 đã được triển khai trong đợt
tiếp theo, ghi ở cuối báo cáo. Mục 5 giữ hướng dẫn mở root đang có:

1. **Asset reference:** thêm [Vanguard](../games/space-typing/docs/VANGUARD_MESHY_INTEGRATION_2026-10-17.md),
   [Fleet 12](../games/space-typing/docs/FLEET_12_MESHY_INTEGRATION_2026-10-20.md)
   và catalog/consumer hiện hành. Giữ phân biệt CharacterId/visual ID.
   Kiểm tra source trước khi coi mô tả trong tài liệu là trạng thái hiện tại.
2. **Routing:** cập nhật `space-typing-director/references/project-map.md` theo
   bảng trên; tránh bắt đầu lại nhiều workflow director cho cùng task.
3. **Tương thích:** đối chiếu package, renderer, Blender executable thực tế.
   r170 là snapshot audit, không phải version bắt buộc duy trì mãi.
4. **Provenance:** mô tả lúc audit chỉ nói “sorted traversal”; cách đã dùng là
   recursive per-directory `name.localeCompare` của Node. Audit tái tạo và khớp
   18/18. Bổ sung thuật toán/locale; nếu đổi sang thứ tự byte ổn định, version hóa
   thuật toán và tái tính có chủ đích, không coi hash cũ là hỏng.
5. **Discovery:** giữ hướng dẫn mở root. AGENTS trong submodule có thể hướng dẫn
   người dùng nhưng không tự làm parent skills được discovery. Không tạo thêm
   bản copy/symlink thứ ba.

Sau sửa canonical nhỏ: validator → sync dry-run → sync → sync check → discovery →
diff. Không cần full game build cho thay đổi chỉ tài liệu.

Nếu về sau gộp/xóa: backup canonical, Claude, manifest ngoài repo; chuyển hợp đồng
riêng và sửa inbound links trước; migration kiểm tra hash cả hai phía và manifest.
Sync hiện tại từ chối canonical/file bị xóa; không thêm force/prune để bỏ xung đột.
Kiểm tra phục hồi trước khi áp dụng.

## Đánh giá hành vi khi cần quyết định thay thế

Không cần benchmark cả hệ sinh thái trước một cập nhật reference nhỏ. Với lựa
chọn còn tranh luận, so ba cấu hình:

- A: source/tài liệu project, không thêm skill đang so sánh.
- B: cùng source/tài liệu + bộ public được chọn.
- C: như B + lớp skill project.

Giữ cùng model/version, reasoning, tools, revision và snapshot dirty; workspace
riêng mỗi trial. Kiểm soát parent AGENTS, global skills, plugin hooks và lịch sử
để baseline không bị lẫn skill. Chấm artifact không kèm nhãn A/B/C.

| Bài thử | Bằng chứng tối thiểu |
| --- | --- |
| Model theo Vanguard/Fleet | Contract, orientation/socket, visual selection và ảnh nhiều góc |
| Tối ưu cảnh nặng | Baseline/candidate cùng scene/viewport/DPR/quality; frame time và readability |
| HUD che từ | Tương tác gõ trong browser, trạng thái và ảnh trước/sau |
| VFX impact Duel | Damage giữ authority timing, effect đồng bộ, chữ dễ đọc |
| Asset rigged | Bone/clip export, browser playback/transitions; không chỉ header GLB hợp lệ |
| Resume CI khi child HEAD đổi | Bảo toàn dirty work, kiểm tra revision hiện tại, không reset checkpoint |

Loại trial vi phạm contract, sửa ngoài scope hoặc báo test chưa thực hiện. Sau đó
so độ đúng, chất lượng artifact, công sửa lại, thời gian và token đo thực tế.
Một lượt là sàng lọc; lặp bài sát điểm trước khi thay bộ.

Vòng đầu đề nghị một bài × ba cấu hình × một lượt, tối đa 10 phút/lượt, không
paid asset generation. Trước khi chạy chốt model và trần token/chi phí theo runner;
timeout không phải trần chi phí. Không tự copy profile/auth vào output hoặc mở
MCP/network ngoài phạm vi thử nghiệm. Kế hoạch này **chưa thực thi**.

## Kiểm tra đã chạy và giới hạn

- Validator: PASS, 13 skill, 0 lỗi, 0 cảnh báo.
- Claude sync check: PASS, 0 thay đổi, manifest hiện hành.
- App-server: root/child discovery; plugin/read cho Game Studio, Superpowers,
  Plugin Eval. Không tạo conversation/gọi model.
- Checksum 18 skill ngoài: 18/18 khớp provenance.
- `git diff --check`: PASS.
- Hash file skill/config/dependency được bảo vệ trước/sau: trường
  `auditProtection` trong JSON. Báo cáo là đầu ra mới của lần này.

Chưa chạy live A/B, native IME, microphone, browser acceptance, Blender export,
provider generation hay kiểm chứng GUI plugin picker trong Cursor. Discovery
không tự chứng minh các công cụ đó khả dụng.

## Triển khai sau audit

Người dùng đã đồng ý áp dụng bốn cải thiện nhỏ. Bộ skill vẫn gồm 13 project skills;
không cài/gỡ skill ngoài hoặc chạy live A/B. Đã cập nhật:

- Asset reference: Vanguard/Fleet, catalog và CharacterId/visual ID, hai nhánh
  GLB/relief, sidecar/hash, preset/socket và tier thật của Campaign/Duel.
- Director reference: chọn specialist chính theo nhu cầu, nạp thêm theo phụ thuộc;
  giữ hợp đồng IME/Voice/Duel/economy/Admin và hướng dẫn Monkeytype riêng.
- Compatibility: đối chiếu package, renderer, API/shader chunks; xác định Blender
  executable/version trước generation. Combat reference trỏ tới cùng hướng dẫn.
- Provenance: ghi rõ thuật toán/collator/locale và phạm vi hash, giữ nguyên 18 hash.
  Thêm [verifier chỉ đọc](../scripts/verify-agent-skill-sources.mjs) để tái kiểm tra.

Ngoài kiểm tra PATH/app chuẩn lúc audit, lần này tìm thấy executable Blender tạm
được Fleet ghi lại; chạy `--version` trả Blender **4.5.7 LTS**. Đường dẫn tạm không
phải cài đặt bền vững. Lệnh in một cảnh báo USD về cache-line size nhưng trả 0;
chưa chạy export/render nên không suy ra toàn pipeline hoạt động từ kiểm tra này.

Kết quả xác minh và danh sách thay đổi của đợt này:
[refinement-2026-10-20.json](agent-skills/refinement-2026-10-20.json).
Audit JSON ban đầu vẫn là snapshot trước khi sửa, không được viết lại để đổi lịch sử.
