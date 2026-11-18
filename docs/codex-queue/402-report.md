# Phiếu 402 — Tuyệt kỹ Kim theo ảnh 396

Ngày 16/11/2026. **Đã dựng công thức, cắt ảnh, nối lab và âm Kim; kiểm kiểu và probe CPU đạt. Chưa hoàn tất nghiệm thu hình ảnh/âm thanh hoặc GPU do chặn trình duyệt và quyền ghi review.** Không commit, không đổi nhánh, không staging media, không chạy build hoặc bộ test game.

## Đã làm

Trong `games/.wt-ic-lab-all/src/lab/`:

- `metal-ult-cut.mjs`: cắt đúng `art-src/concept/ult-metal/ult-metal-components.v1-try2.png`, khử nền đen thành straight alpha và giữ tỉ lệ. Chỉ làm mềm mép hai phần nhỏ được tách riêng, không vẽ hoặc sinh hình. Đã xuất 11 PNG lẻ, atlas RGBA 2048×2048, 12 tệp `.prompt.txt` và `manifest.json` vào `art-src/lab/vfx/metal-ult/`. Prompt nguồn nguyên văn, vùng cắt và SHA-256 được giữ. Đã xem ảnh nguồn, ảnh đích và atlas.
- `metal-ult-sprites.ts`: 204 cụm kiếm billboard trục Y; **144 cụm ở ba vành chồng lấn**, 36 cụm trong vùng, 24 cụm quanh nhóm quái. Sóng đi 26 m/s tới 30 m; cụm mọc 0,2 s. 64 decal vết chém và một nhấn tâm lấy đúng ô mặt đất của bảng thành phần, mở theo sóng rồi tan/xói alpha 2,5 s sau 3 s giữ.
- Một kiếm ở tâm, lệch trước người tung chiêu 3,8 m, hướng camera để đọc từ góc trên. Đây là **thẻ HDR duy nhất** của công thức; các thẻ phụ giữ mỗi kênh ≤ 0,9. Không thêm đèn hoặc bloom mới. Tia, lóe và bụi đều dùng ảnh cắt, code chỉ bố trí, chuyển động và làm tan.
- Trói mỗi quái bằng một vòng kiếm phẳng dưới chân, bốn lưỡi nhỏ bay quanh hông có khoảng hở ngoài thân. Giữ 3 s rồi lưỡi bay rời, sáu mảnh kim loại và tám tia/bụi xuất hiện. Không có vỏ hoặc billboard bọc thân. Các quái dùng chung ba kho instance cho vòng, lưỡi/mảnh và tia/bụi.
- `metal-ult-tint.ts`: clone vật liệu theo batch, nối hook shader cũ và dùng thuộc tính riêng `iMetalBindClock`; tông vàng nhẹ trên mô hình thật, giữ opacity/transparent. Gỡ khi hết trói, chết sớm hoặc xoá phép; không thêm lượt vẽ.
- `metal-ult-layered.ts`: đủ năm pha theo `VFX_STANDARD`, chủ lab tiếp tục sở hữu đứng hình, sát thương, số sát thương, phản ứng và màn hình. Theo dõi số trói/vỡ/tint, huỷ sớm và quá trần 128 trong `__lab.metalUlt().last`.
- `metal-ult-sound.ts`: nối 10 file có sẵn, take 1/3 của năm nhóm: `tt-sfx-el-metal-charge`, `tt-sfx-metal-sword-draw`, `tt-sfx-metal-qi-slash`, `tt-sfx-metal-big-burst`, `tt-sfx-metal-glint`. Đã kiểm file và prompt nguồn theo Q6, đo LUFS-M/true peak bằng ffmpeg, bù gain qua bus hiện có, pitch 0,96–1,04. Một tiếng vỡ chung cho cả sóng; không phát một tiếng nổ cho mỗi quái. **Không thiếu file âm; chưa nghe hỗn âm thật.**
- `skills-main.ts`: Kim đứng **ngay sau Băng**, trước Mộc trong danh sách phím 8. `Y` đổi bản lớp/video; **`P` phát thẳng video cũ `ult-metal-geng`**; `?ultMetal=video` mở bản cũ. Phím `I` đổi bộ icon vẫn giữ. Mặt nạ chữ dùng chung được áp dụng; thẻ dựng đứng/hạt bị cắt khỏi vùng người tung chiêu. Giới hạn diện tích thẻ theo phép chiếu bốn góc là 14% khung.
- `metal-ult-check.mjs`: kiểm kiểu và probe riêng 100 mục tiêu.
- `metal-ult-review.mjs`: kịch bản chụp hai góc và ghép cạnh ảnh đích, để chạy tiếp khi môi trường cho phép.

Ngoài worktree: cập nhật đúng `docs/games/tu-tien/skills/VFX_LIBRARY.md` và báo cáo được yêu cầu này. `art-src` của worktree vốn là symlink tới `games/immortality-cultivation/art-src`; chỉ ghi thư mục con `lab/vfx/metal-ult/` được phiếu cho phép. Không sửa `ice-ult-*`, mã game chính, scripts/tests của game hoặc các thay đổi đang có của agent khác.

## Kiểm tra đã chạy

Trong worktree:

```sh
ART_MAGICK=/opt/homebrew/bin/magick node src/lab/metal-ult-cut.mjs
node src/lab/metal-ult-check.mjs
node src/lab/wood-ult-check.mjs
node --check src/lab/metal-ult-cut.mjs
node --check src/lab/metal-ult-review.mjs
```

- TypeScript strict và `noUncheckedIndexedAccess`: **0 chẩn đoán**, gồm bốn file TS mới, `skills-main.ts` và chuỗi import; không lọc bỏ lỗi ở dependency của các file đó.
- **100/100** mục tiêu trói và ghép tint; một mục tiêu chết sớm bị huỷ vòng, lưỡi, mảnh chờ và tint. **99/99** mục tiêu còn lại nhận đúng một đòn power 1, sau 3 s trong sai số một bước 1/60 s; đúng một cú trúng chính.
- Vật liệu nguồn không đổi; bốn hook gốc được gọi tiếp. Xoá/tung lại năm lần không để tint hoặc instance sót. Trường hợp rỗng và vượt 128 trói kết thúc sạch; giới hạn chỉ cắt hình, không cắt trói/sát thương.
- 144 cụm vành có khoảng cách tới cụm kế nhỏ hơn chiều rộng cả hai; lịch mọc khớp khoảng cách/26. Một thẻ kiếm tâm mang mode HDR.
- Phép chiếu độc lập kiểm **270 trường hợp** thẻ dựng đứng, sát đất và hướng camera, cả màn ngang/dọc và camera sát: diện tích lớn nhất khoảng **12,96%**, dưới giới hạn 14%. Kiểm mặt nạ người tung chiêu ở tám trạng thái góc/cỡ màn/vị trí. Đây là kiểm toán học CPU, chưa chứng minh hình vẽ thực tế không che nhân vật.
- Probe cập nhật riêng công thức Kim p95 khoảng **0,02–0,04 ms**, lập kế hoạch khoảng **1,5–3,6 ms** qua các lần chạy. Lần cuối hai probe CPU chạy song song: p95 Kim **0,0421 ms**, lập kế hoạch **3,591 ms**. **Không phải frame time, số đo GPU hoặc cam kết 60 FPS.**
- Probe Mộc hiện có vẫn **PASS** sau thay thứ tự danh sách. Không chạy bộ test hoặc build game.

| Kho khi có 100 mục tiêu trói | Instance nộp |
| --- | ---: |
| Cụm kiếm và kiếm tâm | 205 |
| Vết chém, vòng chân và vòng tụ | 194 |
| Lưỡi và mảnh kim loại | 1.408 |
| Tia và bụi vàng | 1.444 |
| **Tổng** | **3.251** |

Các số trên gồm ô trống dự trữ và thẻ chờ shader ẩn, không phải tất cả sáng đồng thời. Công thức dùng **4 kho vẽ**; trói dùng chung **3 kho**, tint thêm **0**. Chưa đo số lượt vẽ renderer, overdraw, shadow hoặc hậu xử lý.

## Chặn thực tế và phần còn thiếu

1. CUA trả `Browsers: Error: The browser access host is unavailable`, inventory không có browser. Đã kết thúc phần CUA; không dùng driver khác vượt chặn. **Chưa upload PNG/biên dịch GLSL trên GPU, chưa xem chuyển động, chưa nghe âm trong lab.**
2. Tạo đúng thư mục giao nộp bị sandbox từ chối:

   ```text
   mkdir: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/ult-metal: Operation not permitted
   ```

   Vì vậy **chưa có ảnh góc trên/sau lưng, bảng so ảnh hoặc `ABOUT.md` tại thư mục review**. Không ghi capture sang `art-src`, `public`, `docs` hay nơi khác. Không có capture mới để cập nhật index hoặc dọn raw frame.
3. `stress.html` hiện có 87 mục tiêu nhận phép và 13 walker trang trí. Kịch bản ghi số trói/tint thực tế; chỉ đặt `passes100BoundFoes=true` khi thật sự đủ 100. Không sửa stress/herd ngoài phạm vi để đổi workload. Probe CPU đủ 100 mục tiêu không thay cho kiểm render 100 quái.
4. Chưa có điểm 8,5, hai giám khảo hoặc owner duyệt. Cần xem vành có đủ dày/chồng lấn, kiếm tâm có đọc được từ trên, hông/thân quái còn rõ trong đủ 3 s, mép alpha/vết chém, chuyển tiếp vỡ và hỗn âm Kim. Chưa tự công nhận nghiệm thu.

## Tiếp tục khi môi trường cho phép

Phục vụ đúng worktree hiện tại; chỉ dùng cổng dưới đây nếu nó đang phục vụ worktree đó. Script không mở server hoặc build game:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/stress.html \
ART_MAGICK=/opt/homebrew/bin/magick \
node src/kit/tools/cdp-run.mjs src/lab/metal-ult-review.mjs \
  --width=1920 --height=1080 --dpr=1
```

Kịch bản mới qua kiểm cú pháp, **chưa chạy**. Nó kiểm đúng API/phiên bản, chờ atlas sẵn sàng, làm nóng các pha; chụp tụ, tung, sóng, giữ, hết trói, vỡ và tan đất ở góc trên/sau lưng; ghép cạnh `ult-metal-moment-b.v1-try1.png`; ghi 440 mẫu CPU/tổng có readback mỗi góc cùng số quái thật, console và exceptions; cập nhật index sau khi ghi. Không gọi số tổng có readback là GPU time thuần.

Nội dung ABOUT đã nằm trong script:

```text
purpose: Phiếu 402: so ảnh đích với mốc tung 0,60 s, sóng 1,20/1,90 s và lúc trói; góc trên và sau lưng
made-by: Kịch bản Codex src/lab/metal-ult-review.mjs, phiếu 402
doc: /Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/402-report.md
delete-when: Sau khi owner duyệt và không còn cần đối chiếu
```

Hạn mức trước khi làm: `primary.used_percent=43`, còn 57%; không gặp giới hạn quota hoặc tạo ảnh. Không gọi công cụ sinh ảnh vì phiếu yêu cầu cắt hình đã có.
