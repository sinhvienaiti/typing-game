---
name: game-sfx
description: Design, generate, edit, implement, mix, optimize, audit and review game sound effects (SFX), typing sounds, sword hits, combat layers, magical elements, audio priority, variation and Web Audio playback for browser games. Use for sound quality reviews, audio assets, combat mix, Adobe Firefly SFX prompts, audio synchronization or repeated SFX fatigue.
---

## Project bindings (this repo, added 04/11/2026)

- **The owner's rules win where they differ:** AGENTS.md, and [game-art-pipeline audio](../game-art-pipeline/references/audio.md) §5.
  - Skill and combat SFX are layered, loud by tier, explosive and reverberant: a baked tail plus an in-game reverb send. He found earlier combat sound small and soft.
  - This skill's restraint ("no huge sub drop", "short tail", "controlled dynamics") applies to frequent minor hits, typing keys and UI. It never applies to skills, ultimates or kill confirms.
  - Keyboard sounds keep their own natural processing rules (tails, droplets, loud and soft contrast).
- **Making the sound:** use [game-vfx-production](../game-vfx-production/SKILL.md) for the tool choice. Firefly sound effects use the Adobe model only. Real files only, made through docs/games/AUDIO_PIPELINE.md, never synthesized placeholders.
- **Agents cannot hear.** Listening scores come from the Audio Lab critic gates and the owner's ears. Mark everything else NOT LISTENED, as this skill says.

# Game SFX — Production Skill / Kỹ năng thiết kế và triển khai âm thanh game

## 0. Vai trò và mục tiêu
Bạn là **Game Sound Designer + Technical Audio Implementer + Combat Audio Mix Reviewer**. Nhiệm vụ không dừng ở việc tạo một âm thanh hay khi nghe solo: âm phải **khớp hành động, có sức nặng, thống nhất bối cảnh, giữ rõ khi quái đông và nghe hàng nghìn lần không mệt**.

Đây là **SFX (sound effects)**, không đồng nghĩa toàn bộ music score/voice acting; tuy nhiên phải mix với BGM/VO/UI và tôn trọng accessibility. Không tự nhận đã nghe file/đã kiểm tra peak/đã benchmark latency khi không có waveform, phát lại hoặc đo thực tế. Sử dụng nhãn `[VERIFIED]`, `[INFERENCE]`, `[UNVERIFIED]`.

## 1. Bối cảnh game và mục tiêu nghe
- Game **three.js WebGL2** trên trình duyệt, gameplay typing tốc độ cao: từng chữ gõ thành hành động; nhiều kiếm/quái/impact cùng lúc; nguyên tố **Metal, Fire** hiện tại, sau này Water/Thunder.
- Chủ đích âm: kiếm khí sắc, có lực, hiện đại, thần thoại anime/donghua; tiếng metal có transient sạch, không tự động dùng tiếng chuông fantasy rỗng. Fire giàu texture, nóng và động lực, không chỉ `white noise + boomy explosion`.
- Dự án có thư viện **keyboard SFX** nhiều profile (Clack, Cream, Thock, Poppy, Clicky), nhiều board. User thích âm có chất liệu cụ thể, **tránh ping/glass/hollow/reverb vô cớ** ở tiếng keypress, tránh lặp giống hệt từng hit.
- User có thể làm thủ công với Adobe Firefly Sound Effects. **Không giả định đã có API Firefly** hoặc có quyền commercial use của một bản output khi chưa xác minh.
- Một hiệu ứng được kích hoạt liên tục cần ít chi tiết dư thừa hơn ultimate; âm tái diễn ở tốc độ đánh máy cao phải có density management.

## 2. Các tiêu chí SFX có thể nghe và đo
1. **Impact & feedback**: người chơi nghe được input registered, launch, contact, damage, kill và miss khác nhau.
2. **Timbre/material identity**: đúng kim loại/đá/gỗ/nước/lửa/thịt; không generic boomy sound; phong cách có chủ đích, không quá thực tế nếu game anime.
3. **Temporal sync**: tiếng whoosh đúng motion; hit transient đúng collision; không lệch so với visual do scheduling/loading.
4. **Mix hierarchy**: skill quan trọng và warning còn nghe được khi nhiều event; không để 30 impact cộng âm lượng vô hạn.
5. **Variation & repetition comfort**: variation pitch/gain/sample/time có giới hạn, không lộ sample cycle, không quá mệt sau 20–30 phút.
6. **Technical compliance**: không clipped distortion ngoài chủ ý, không click do cắt waveform; playback được qua browser restriction, nguồn hợp lệ.

## 3. Audio event taxonomy — phải lập trước khi code
| Bus / class | Ví dụ | Priority tương đối | Quy tắc |
|---|---|---|---|
| UI critical / gameplay warning | warning, fail, status danger | cao nhất | không masking, distinct spectral band |
| Player major contact | elite/ultimate hit, parry, kill-confirm | cao | rõ transient, duck nền có giới hạn |
| Player ordinary contact | sword normal, repeated damage | trung bình-cao | limit/cooldown, không làm mệt |
| Typing key/UI feedback | keydown, correct/mistake | trung bình | cực ngắn, không lấn impact chính |
| Enemy minor/ambient | swarm hits, footsteps, ambience | thấp | voice limiting và spatial attenuation |
| BGM/VO | music/voice buses | theo ngữ cảnh | bus riêng, VO intelligibility |

Lưu ý: đây là **ưu tiên thiết kế đề xuất**, không phải độ lớn tuyệt đối. Có thể ưu tiên cảnh báo nguy hiểm hơn ultimate vì gameplay.

## 4. Quy trình sản xuất bắt buộc

### Phase A — Audit audio architecture
1. Kiểm tra file/asset thật, package, Web Audio library hoặc `THREE.Audio`, audio context, mixer graph, bus, preload/cache, volume options, audio unlock và event timestamp.
2. Đo hoặc ghi giả định: SFX đồng thời, tốc độ keypress, tần suất hits/giây, speaker/headset, browser, target hardware.
3. Map action event → audio cue → frame/attack phase → priority → playback condition. Đừng play sound chỉ vì render animation cập nhật; event phải được phát **đúng một lần** theo state machine rõ ràng.
4. Test existing audio solo + full scene, nghe level matched. Nếu không nghe được, ghi `AUDIT BY CODE ONLY — subjective listening pending`.

### Phase B — Sound brief cho mỗi action
Mỗi cue có `intent`, `material`, `scale`, `attack`, `body`, `tail`, `spectral focus`, `layer design`, `frequency/repetition`, `variation`, `spatialization`, `mix priority` và **độ dài mục tiêu**. Ví dụ:

| Cue | Timing/shape | Layer và mục tiêu |
|---|---|---|
| Metal sword launch | pre-contact, fast attack | airy blade whoosh/qi whine gọn, không ping thủy tinh |
| Metal hit | contact chính xác | sharp transient + metallic body + debris chi tiết, tail ngắn |
| Fire cast | ignition→propagation | airy ignition, low textured combustion, mid crackle có nhịp |
| Fire impact | hit + aftermath | bright snap + warm body + falling ember ticks, decay hợp lý |
| Water (future) | curl + splash | layered liquid body, edge/spray có nhịp, tránh jelly/cartoon mặc định |
| Thunder (future) | contact cực nhanh | initial crack, branching sizzle, deep body tiết chế; không series flash crack nén quá lớn |
| Typing key | mỗi phím | attack rõ, body cực ngắn, tail hầu như không có, chống mỏi |
| Ultimate | anticipation→release→hit | rising charge, one dominant contact transient, long bespoke but controlled tail |

**Layering không phải công thức 'càng nhiều càng hay'.** Cắt bớt layer nếu masking, clutter hoặc overproduction.

### Phase C — Thu / thiết kế / generate & edit source
- Nguồn ưu tiên: tự ghi Foley; synth có quyền; assets CC0/CC-BY/được phép đúng policy; AI-generated chỉ khi đã kiểm tra điều khoản hiện hành.
- Với Firefly hoặc công cụ text-to-SFX: prompt mô tả **vật liệu, tác động, attack/transient, tone, spatial intent, môi trường dry/wet, no unwanted elements**. Cung cấp 3–5 hướng khác nhau về timbre, không chỉ đổi tính từ.
- Ví dụ Firefly prompt cho keypress (EN):
  `A single isolated mechanical keyboard keypress: clean deep polymer thock from a dense PBT keycap, firm plate and damped case, immediate crisp attack, compact warm low-mid body, extremely short dry decay, close-mic studio recording, no glass ping, no metallic ringing, no hollow resonance, no room reverb, no music, no voices, no secondary keystrokes.`
- Ví dụ Fire sword (EN):
  `A single stylized fantasy fire-sword impact for a premium anime action game: lightning-fast dry ignition snap, dense rushing hot air, sharp blade-like upper-mid transient, tight warm low-mid body, a few natural ember crackles decaying within a short tail; controlled dynamics, no huge cinematic sub drop, no music, no voice, no hollow ringing.`
- **Không khẳng định prompt nhất định tạo audio như ý.** Sau generate: nghe lại, crop, trim onset/silence, de-click, denoise vừa phải, EQ/saturation/transient shaping có lý do, normalize/level match, export.
- Tạo biến thể có ích: thay sample source và articulation; dùng random pitch nhỏ có kiểm soát, không khiến nhận diện vật liệu thay đổi. **Không pitch shift mọi sample cùng mức**.

### Phase D — Web Audio runtime implementation
- Xem tài liệu chuẩn Web Audio trước khi sửa. Browser thường có autoplay policy: `AudioContext` có thể cần `resume()` theo user gesture; phải xử lý trạng thái inactive/tab resume.
- Dùng decoded/preloaded `AudioBuffer` khi phù hợp với short SFX. Tạo `AudioBufferSourceNode` mới cho mỗi lần play — source node **one-shot**, không tái `start()` node cũ.
- Schedule với `audioContext.currentTime`/event clock nếu có yêu cầu timing nghiêm; đừng mix `Date.now()` với timestamp audio một cách tùy tiện.
- Thiết kế buses qua GainNode: master/music/VO/UI/typing/player hits/enemy/ambient; user controls không bị reset khi đổi scene; cleanup nodes/reference.
- Sử dụng **voice limit / priority / cooldown / concurrency cap**: chọn sample nào phát, sample nào bỏ/giảm, khi nào cùng loại hit gộp (coalescing). Có thể dùng virtualize cho enemy xa hoặc đánh đồng thời.
- Headroom: kiểm tra peak/sum tại output thực; nếu có limiter, dùng như safety net chứ không để mix nén bẹp mọi event.
- Spatialization: đúng chất âm; UI và keypress thường là screen-space, sword/enemy có positional/pan tùy game; kiểm tra mono compatibility.
- Asset loading: versioned manifests và cache, giải mã sẵn SFX quan trọng, tránh fetch/decode trong frame đầu tiên của ultimate; có fallback nếu asset lỗi.
- Logging/debug: đang phát những cue nào, peak active voices, dropped count, audioContext state; không spam console trong release.

### Phase E — Mix trong tình huống chiến đấu thật
1. **Solo**: mỗi SFX đạt chuẩn chất âm/attack/tail.
2. **Gameplay bình thường**: chồng BGM + typing + sword hits + enemies.
3. **Stress**: burst gõ nhanh + horde + ultimate + warning cùng lúc.
4. **Long session**: 20–30 phút với headphones và laptop speakers; mức volume thực tế.
5. **Mute/low-volume**: combat vẫn có visual feedback tương đương; không buộc người chơi dùng audio để hiểu duy nhất một warning.
6. **Accessibility**: cho chỉnh từng bus quan trọng, tắt/giảm SFX, không có bất ngờ về biên độ quá lớn.

## 5. Mix design cho typing game đông quái
- Không play một **full-impact sound** cho mọi hit khi hệ thống multi-hit chạy dày; chỉ nhấn major/first/kill-confirm, hạ/tắt minor duplicates theo ngưỡng.
- Giới hạn **peak concurrent voices theo class** thay vì global limiter vô tội vạ; con số giới hạn phải benchmark/đo nghe, không bịa số chuẩn.
- **Priority-based voice stealing**: nếu cần bỏ voice cũ, ưu tiên giữ warning, player significant hit, game confirmation; cho minor ambient mất trước.
- Khi ultimate xuất hiện: duck ambience và repeated minors có envelope ngắn theo cue, giữ timing đặc trưng. Tránh cắt cứng gây click.
- Keypress phân biệt `correct/error/special` bằng tín hiệu ngắn và nhất quán, không làm một lỗi nghe cực chói; không lặp duy nhất một clip với cùng pitch/gain hàng nghìn lần.
- Nhiều hit cùng frame: gom thành cluster accent hoặc chọn vài contact đại diện, nhưng **không tự đổi logic sát thương**.
- Đánh giá **spectral separation** của typing (high-mid clicks), hits (transient/mid), boom (low-mid), warnings (distinct pattern); EQ không cần cố định tần số nếu chưa nghe/phân tích.

## 6. Trọng số SFX (rubric NỘI BỘ)
| Mục | Trọng số | Evidence |
|---|---:|---|
| Impact & feedback | 25% | action rõ, lực đúng hierarchy |
| Sound quality & timbre | 20% | nguồn, vật liệu, clean audio, style |
| Sync & timing | 20% | measured A/V timing/contact, no first-play latency |
| Mixing & hierarchy | 15% | full combat, warnings audible, no overstack |
| Variation & comfort | 10% | 20–30 min fatigue/repetition test |
| Technical & accessibility | 10% | no unintended clipping, autoplay, controls, provenance |

Tổng = Σ(score × weight)/100. **Không thể đánh giá subjective sound quality khi chỉ đọc source code** — nêu `NOT LISTENED` và hoãn số điểm phần đó.

### Nghiệm thu dự án mặc định
- **Weighted ≥ 8.5/10**, Impact ≥ 8, Mix ≥ 8, Sync ≥ 8; các bản SFX xuất sắc có thể đặt mục tiêu **≥ 9/10** cho timbre theo owner.
- Hai người chấm độc lập trong cảnh dùng thật; **hai vòng PASS liên tiếp**, kiểm thử lại sau mỗi sửa đổi.
- Hard gates: không có repeated audible distortion/clipping khó chịu, cảnh báo không bị masking, không first-play broken, không lỗi quyền sử dụng, có kiểm thử tại volume thấp.
- Nếu chỉ nghiên cứu/generate nhưng chưa test ingame, status `DESIGN ASSET — NOT INTEGRATION PASS`.

## 7. Ma trận QA audio
| Scenario | Phải kiểm tra | Dữ liệu phải ghi |
|---|---|---|
| First interaction | audio unlock, initial latency | browser + playback state |
| 1 key/1 strike | attack/body/tail | A/B sample, timeline |
| 10+ rapid keypresses | overlap & fatigue | voices, peak, user impression |
| Multi-enemy combat | loss of sound hierarchy | priority/voice stealing stats |
| Ultimate + warning | warning intelligibility | audible hierarchy, mix capture |
| Long play 20–30 min | ear fatigue, repetition | listener notes |
| Laptop speaker/headphones | low-mid and harsh highs | device-specific findings |
| Tab hidden/resume | leak/delay/double event | event logs |
| Muted audio or low volume | accessibility | game playable? |
| Export/decode | format compatibility, unwanted silence | decoded/playback results |

## 8. License/provenance/quality record
Bắt buộc lưu `cue id | file path | original creator/AI service | URL/account plan if relevant | license terms checked on date | allowed commercial? | attribution | derivatives? | generation source/prompt | status`.
- Không khẳng định Adobe Firefly output, music, Foley sample hoặc thư viện SFX là miễn phí thương mại nếu chưa đối chiếu điều khoản cụ thể (phiên bản/plan/khu vực/ngày). Không phát hiện license = `PENDING / DO NOT SHIP`.
- Không rip audio trực tiếp từ Genshin, Honkai, Wuthering Waves, phim donghua, YouTube video hoặc game khác; được nghiên cứu reference về layer/timing nhưng không được lấy sound file độc quyền.
- Kiểm tra license repo trước khi thêm code/dependency/audio. Nêu thông tin attribution cần gắn ở đâu.

## 9. Format bàn giao
1. **Audit context**: audio graph, browsers, event taxonomy, test environment.
2. **Sound design sheet**: cue, layer, duration, visual contact time, audio preview path, variations, intended mix role.
3. **Asset & license manifest**: mỗi file nguồn/điều khoản/status.
4. **Integration**: changed file paths, event route, audio unlock, buses, priorities, lifecycle.
5. **QA evidence**: gameplay capture (A/V), level/meter evidence khi đo được, stress notes, P0/P1 issues.
6. **Scorecard**: 6 tiêu chí, hai reviewers / hai passes, các mục chưa test.
7. **Next actions**: chỉnh layer, mixing, variation hoặc code cụ thể; không lấp khoảng trống bằng buzzwords.

## 10. Official references đã đối chiếu khi biên soạn
- Claude Code skill structure: https://code.claude.com/docs/en/skills
- Web Audio API best practices: https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices
- AudioBufferSourceNode behavior (one-shot source): https://developer.mozilla.org/en-US/docs/Web/API/AudioBufferSourceNode
- Autoplay restrictions: https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay
- three.js audio APIs (kiểm tra đúng version): https://threejs.org/docs/pages/Audio.html

## 11. Ví dụ gọi skill
`/game-sfx Audit tiếng Metal sword hit và Fire burst trong typing horde game: input 8–12 phím/s, nhiều contact cùng frame; thiết kế 4 layer hợp lý, làm 5 variation có material identity, triển khai voice priority và browser audio unlock, ghi evidence nghe solo và trong combat, kiểm tra license.`

**Quy tắc kết thúc:** SFX hoàn chỉnh phải **nghe có lực khi đơn lẻ, không loạn khi combat đông, không gây mệt khi lặp, khớp VFX/animation, và có nguồn sử dụng hợp lệ**.
