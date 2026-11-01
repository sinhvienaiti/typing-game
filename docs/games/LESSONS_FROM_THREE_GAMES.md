# Bài học từ ba game (Dragonhold, Wordwoven, Last Line), 01/11/2026

Viết cho game mới, trước hết là Tu Tiên Thủ Ải (`games/immortality-cultivation`), để không lặp lại các lỗi đã gặp. Mỗi mục ghi: lỗi đã xảy ra, rồi luật phải làm. Luật gốc nằm ở `AGENTS.md` (repo cha) và các file được dẫn.

## 1. Chấm điểm

- **Lỗi:** tôi tự chấm cao hơn giám khảo (metronome tôi cho 8, giám khảo 7). Icon chấm trên tờ 256 px được 8, vào game ở 16–24 px chỉ còn 6,2. Ảnh chấm ở bản dev có cờ URL đẹp hơn bản người chơi thấy. Lửa, icon, title được "gắn tạm" dưới mốc rồi coi như xong.
- **Luật:**
  - Mức đạt 8,5: hai giám khảo mù độc lập, chấm trong bản build trên host chơi, đúng thiết lập người chơi, không cờ URL. Không có "tạm", không có "tốt hơn trước". Hệ dùng chung (gõ phím, âm phím, animation nhân vật) cần 9.
  - Chấm mù thật: nhãn trung tính (A/B/C), khóa để ngoài thư mục giám khảo, giám khảo không đọc báo cáo hay prompt. Giám khảo viết "thấy gì" trước rồi mới cho điểm.
  - Mốc so là bảng tham chiếu thương mại (ví dụ `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp` = 9), không phải style guide của ta.
  - Chấm icon và UI đúng cỡ, đúng chỗ trong game.

## 2. Map và cảnh

- **Lỗi:** map dựng trước khi có ý tưởng, nên ra "công viên đồ chơi": đồng cỏ phẳng màu chói, nước như mảng màu, cây lặp mẫu, không có điểm nhìn. Concept vẽ dải trời trong khi camera 42–55° không bao giờ thấy trời. Đường đi kém nổi so với cỏ; quái chìm vào nền.
- **Luật:**
  - Mỗi màn có ý tưởng map trước, viết theo camera thật. Có ảnh nền chụp từ camera game kèm legend tọa độ.
  - Gửi ChatGPT duyệt ở **chế độ Chat, thinking High, không bao giờ dùng Work**.
    - Trình duyệt trong app **không gửi được ảnh lên ChatGPT**, vì trang chặn file trên máy. Chủ dự án đính kèm ảnh nền, ChatGPT vẽ đè lên.
    - Không có ảnh nền thì ChatGPT lệch bố cục: điểm bố cục chỉ 5,5–7,5.
  - Tính theo camera trước khi vẽ:
    - mép trên khung nhìn thấp hơn chân trời bao nhiêu độ, tức là có thấy trời không;
    - vật cao bao nhiêu thì bị cắt ở mép trên;
    - vật gì không được che đường hay ô xây.
  - **Thứ bậc độ sáng:**
    - đường sáng hơn cỏ một bậc rõ (đo tỉ số);
    - quái tách khỏi nền bằng bóng chân và viền sáng;
    - vùng chơi chính tối và yên để thẻ chữ nổi.
  - **Màu dành cho tín hiệu,** chốt từ đầu: màu nào chỉ dành cho quái, đòn quái, quái đầu đàn, phe ta. Môi trường không dùng những màu đó ở cường độ cao.
  - Ngân sách ánh sáng: một nguồn sáng chính, ít điểm sáng, có thứ tự mắt nhìn.
- Xem: `docs/games/maps/*-MAP_CONCEPTS.md` (bản 1.2), `docs/games/maps/*-CHATGPT_REVIEW.md`.

## 3. Hình 2D (Firefly)

- **Lỗi:**
  - Nền xanh khóa hắt màu lên vật.
  - Vật tràn khung.
  - Ảnh tham chiếu của Firefly Image 5 chép luôn chủ thể và ép tỉ lệ khung.
  - Firefly không giữ được một thiết kế qua 4 góc nhìn: mũ đổi theo góc, ảnh "mặt sau" vẫn là mặt trước.
  - Sáu ảnh một bộ ra năm kiểu vẽ, năm màu đá.
  - Firefly từ chối vài prompt về súng.
- **Luật:**
  - Chỉ dùng model của Adobe (Firefly Image 5), không dùng model đối tác (Gemini, GPT Image…). Prompt tối đa khoảng 1024 ký tự.
  - Mỗi bộ ảnh có **một chuẩn chung** trong mọi prompt: chất liệu, một kiểu motif, một hướng sáng, một màu nền khóa, góc ba phần tư khoảng 30–35°, lề ≥ 6–8 %, không bóng đổ, không nền đất.
  - Tách câu chất liệu theo vật: câu "sắt và gỗ" kéo sắt vào cả tượng đá.
  - Vật cao dùng khung dọc 3:4.
  - Sau khi tạo: kiểm khung bằng script (lề, một khối liền, bóng đổ); nới nền nếu thiếu lề; khử ám xanh chỉ trên vật.
  - Khi tự vẽ đã chững (sau 2–3 vòng không lên), tìm nguồn có sẵn miễn phí trước khi vẽ thêm.

## 4. Model 3D (Tripo)

- **Lỗi:** các đợt trước để face 2–4k nên model trông như nhựa. Ảnh nguồn không đạt nên model không thể đạt. Ultra không khác High thật.
- **Luật:**
  - Ưu tiên **API** (`tripo` CLI, ví khoảng 970 credit; khoảng 40 credit một model). Dùng texture HD, PBR, model v3.1.
  - `face_limit` theo loại, nâng hơn trước nhưng không để tối đa: nhân vật chính 50k, công trình 30–50k, súng 15k, vật nhỏ 12k.
  - **Chỉ dựng khi ảnh nguồn được hai giám khảo cùng cho từ 8,5**, cả mức thị trường lẫn độ hợp Tripo. Chủ dự án 01/11: "Chờ ảnh đạt 8,5". Luôn chạy `--dry-run` trước, dựng một model trước rồi kiểm (tam giác, map, vòng quay), sau đó mới dựng tiếp.
  - Giữ số face, normal map và roughness map của bản gốc theo sàn trong `docs/games/MODEL_QUALITY.md`. Chỉ cắt khi đo thấy vượt ngân sách khung hình, theo thứ tự doc đó.
  - **Dùng lại quái 3D sẵn có** trước khi làm mới (`docs/games/MONSTER_MODEL_INVENTORY.md`, 195 model).
  - Tripo chỉ lo hình; rig, clip, chuyển động và VFX là việc của ta.
- Xem: `docs/games/TRIPO_TODO.md`.

## 5. VFX và ánh sáng

- **Lỗi:**
  - Bloom quá tay làm đạn thành vệt sữa: Heat Beam rộng 78–84 px, trắng xóa cả làn.
  - Khói cộng sáng thành sương sữa.
  - Không có khử răng cưa ở High/Ultra.
  - Hạ bloom chung làm mất luôn dấu sáng gõ phím, vốn là hệ dùng chung.
- **Luật:**
  - Theo `docs/games/VFX_STANDARD.md`: mỗi đòn có năm pha (gồng, phóng ở nòng, bay, trúng, dư âm).
  - **Bloom:** chỉ lõi HDR mảnh (3–6) được bloom; quầng ≤ 0,9 mỗi kênh. Strength 0,4–0,5, radius 0,1–0,15. Tone map Neutral hoặc AgX.
  - Khói dùng pool trộn thường, làm tối chứ không cộng sáng. High/Ultra có MSAA.
  - Hệ dùng chung (gõ phím, âm phím, animation) không được đổi ngầm: chạy lại kịch bản đo của nó và so với bản cũ.
  - Mỗi lần đổi VFX có tờ khung trước/sau ở 720p và 1080p.

## 6. Âm thanh

- **Luật:**
  - Âm thanh là file thật, theo `docs/games/AUDIO_PIPELINE.md`. Không dùng âm tổng hợp tạm.
  - Chủ dự án 01/11: dùng Firefly để tạo âm thanh. Đi theo pipeline: danh sách, tạo, chấm, ingest.
  - Âm phím xử lý tự nhiên: giữ đuôi, độ cao và độ chênh to/nhỏ.

## 7. UI

- **Luật:**
  - Không có thứ vẽ bằng mã thay cho tranh: không SVG hay canvas làm cảnh, không icon bằng CSS, không emoji.
  - Mọi chi tiết UI có art thật.
  - Có bánh răng Settings và loa Sound trong trận (`docs/games/IN_GAME_SETTINGS.md`, một component của kit).

## 8. Hiệu năng và mức chất lượng

- **Luật:**
  - Mỗi mức (Low/Medium/High/Ultra) có cổng frame time. Đo bằng kịch bản bench trên GPU thật (`.local/bin/heavy.sh --gpu`), đo ở dpr 1 và dpr 2.
  - Ultra phải khác High thật.
  - Đổi Quality phải có hiệu lực, nên tự tải lại trang.
  - Mỗi khung không cấp phát bộ nhớ trong vòng lặp vẽ.

## 9. Tài nguyên miễn phí

- **Luật:**
  - Được dùng: CC0, CC-BY (ghi công), Zlib/MIT cho mã, giấy phép kiểu Quaternius (QAL).
  - Không dùng: NC, ND, SA, GPL, Mixamo, Fab, Sketchfab "Standard", thứ gắn NoAI, thứ phải trả tiền.
  - Kiểm giấy phép trên trang của từng tài nguyên và trích đúng câu chữ. Không cào dữ liệu, không tải hàng loạt bằng script (điều khoản Poly Haven cấm).
  - Ghi vào `docs/games/THIRD_PARTY.md`.
- Xem: `docs/games/FREE_ASSET_SOURCES.md`, `docs/games/SHARED_SYSTEMS_BAR.md` §5.

## 10. Cách làm việc

- **Lỗi:** agent bị cắt giữa chừng do hết hạn mức; ảnh chụp thô làm đầy đĩa (77 GB); trình duyệt trong app chạm trần khoảng 9 tab nên agent không mở được tab mới; gửi tin cho agent đang chạy làm nó chạy trùng.
- **Luật:**
  - **Commit:** commit nhỏ, thường xuyên. Workflow chạy lại bằng `resumeFromRunId`. Không nhắn tin cho agent đang chạy trong workflow.
  - **Ảnh chụp:** để dưới `tmp/` của game; xong thì dọn ảnh thô của chính mình bằng `node tools/capture-prune/prune.mjs <thư mục> --apply`.
  - **Tab:** đóng các tab mình mở, dùng tab riêng, không đụng tab của session khác.
  - **Media:** không đưa media vào Git; media đi qua `pnpm media:push`. Mỗi lần cập nhật có changelog.
