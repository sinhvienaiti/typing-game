# Giao việc cho Codex

Mục đích: giao cho Codex những việc **hình ảnh, prompt âm thanh và tài liệu phụ**, để Claude giữ phần thiết kế lõi, code gameplay và kiểm tra. Chủ dự án yêu cầu ngày 25/10/2026, cũng để tiết kiệm quota.

## Cài trên máy Dell

- **Codex CLI:** dùng bản **0.164.0** chính thức tải từ GitHub `openai/codex`, đặt ở `D:\_tools\codex-0.164.0\codex-x86_64-pc-windows-msvc.exe`, kèm `codex-code-mode-host.exe` và `codex.cmd`.
  - Bản 0.146 trong extension Cursor chỉ gọi được `gpt-5.6-sol`. Với `gpt-6.x`, máy chủ báo "not supported when using Codex with a ChatGPT account".
- **Đăng nhập:** bằng ChatGPT (`~/.codex/auth.json` của Windows). **Không dùng API key**: `run.ps1` xóa `OPENAI_API_KEY`, `CODEX_API_KEY`.
- **Model mặc định:** `gpt-6.1-sol`, suy luận `high`. Mỗi dòng làn ghi model và mức của nó (cột 4 và 6), chọn theo bảng "Chọn model" dưới đây (chủ dự án 27/10: không dùng ultra cho mọi việc).

### Từ 04/11/2026: Codex là người làm code, logic và âm thanh

Khối này thay mục đích ở đầu trang và bảng 27/10 bên dưới ở chỗ nào hai bên khác nhau. Chủ dự án dặn 04/11: "giao cho nó việc chính là cũng xử lý code, logic, âm thanh… codex chỉ là 1 đứa làm việc thay bạn xử lý code hoặc logic… khi nào 2 đứa chatgpt và gemini đạt giới hạn tạo ảnh thì kêu codex tạo ảnh… ưu tiên dùng 1 luồng… dùng model sol 6.1 medium, high, extra hoặc ultra tuỳ công việc, nếu liên quan tới logic, code thì cứ extra hoặc ultra". Đầy đủ ở skill `agent-orchestration`.

- **Giao gì:** code, logic, âm thanh (chuỗi xử lý âm, mã Web Audio, script trộn). Chỉ giao khi Claude đã có lời giải đầy đủ, sau lượt duyệt hai lần liên tiếp của ChatGPT rồi Gemini, hoặc sau quyết định của chủ dự án.
- **Không giao:** phân tích, thiết kế, quyết định.
- **Ảnh:** ChatGPT và Gemini vẽ. Codex chỉ vẽ khi cả hai đã chạm giới hạn tạo ảnh.
- **Model `gpt-6.1-sol`, mức theo việc:**

  | Loại việc | Mức |
  |---|---|
  | Việc vặt | `medium` |
  | Âm thanh, sửa nhỏ có chỉ dẫn, ảnh khi buộc phải vẽ | `high` |
  | Code và logic | `xhigh` |
  | Code lớn nhiều phần hoặc logic khó | `ultra` |

  Code và logic không cần hỏi chủ dự án từng phiếu nữa.
- **Một làn.** Chỉ mở thêm khi chủ dự án bảo.

### Chọn model (chủ dự án 27/10)

Hạn mức Codex rất thấp (cửa sổ 5 giờ). Làm ảnh trước, ảnh xong mới giao việc khác. Chọn model và mức theo loại việc:

| Loại việc | Model | Mức | Vì sao |
|---|---|---|---|
| Tạo ảnh, sửa ảnh bằng công cụ | `gpt-6.1-sol` | `high` | Ảnh do công cụ `image_gen` vẽ; model chỉ viết prompt, chạy magick, tự chấm, và Claude chấm lại. Ultra tự chia việc cho agent con nên tốn hạn mức mà ảnh không đẹp hơn |
| Sửa mã nhỏ có chỉ dẫn sẵn, chép kit, đo số | `gpt-6.1-sol` | `high` | Model chính cho code; phiếu đã ghi file, cách sửa, cách kiểm |
| Kiểm lại độc lập, phản biện (đọc diff, tìm lỗi người sửa bỏ sót) | `gpt-6.1-sol` | `xhigh` | Cần suy luận sâu trong một repo; không cần chia agent con |
| Việc vặt (dời file, cập nhật bảng, đếm) | `gpt-6-luna` | `medium` | Model nhanh, rẻ cho việc dễ. Chưa thử với tài khoản ChatGPT này: chạy thử một phiếu nhỏ trước |
| Việc rất khó, nhiều phần độc lập | `gpt-6-astra` `high`, hoặc `gpt-6.1-sol` `max`/`ultra` | | Chỉ khi chủ dự án đồng ý từng phiếu: tốn hạn mức nhất. Astra chưa thử với tài khoản này |

`run.sh` chỉ nhận các model trong bảng (`gpt-6-sol` là bản cũ, để dự phòng).
- **Trên Mac mini M4:** Codex CLI có sẵn trong extension ChatGPT của Cursor (không nằm trong PATH): `~/.cursor/extensions/openai.chatgpt-<bản>/bin/macos-aarch64/codex`. Bản 0.162.0-alpha.17.2 gọi được `gpt-6.1-sol` (thử ngày 25/10/2026), nên trên Mac không cần ≥ 0.164. Mac không có `pwsh`, nên dùng hai bản bash cùng cách làm:
  - `tools/codex-run/run.sh <tên> <phiếu> [thư mục] [effort] [sandbox]`;
  - `tools/codex-run/queue.sh <danh sách>`: cùng định dạng danh sách. **Hạn mức không bao giờ làm bỏ phiếu** (chủ dự án 31/10: hết hạn mức thì chờ, có lại thì chạy tiếp, không dừng hẳn):
    - hết hạn mức ChatGPT: chờ tới giờ Codex báo ("try again at …") cộng 2 phút, không biết giờ thì 30 phút, rồi chạy lại phiếu; không giới hạn số lần;
    - công cụ trong phiếu hết lượt (ví dụ `image_gen` trả 429) hoặc phiếu ghi "chưa được chạy trước 19:48": theo luật trong `run.sh`, Codex ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`); hàng chờ chờ tới giờ đó rồi chạy lại phiếu, lần sau làm tiếp từ chỗ đã xong;
    - rớt kết nối: chạy lại sau 2 phút, từ lần thứ năm thì 15 phút một lần.
    - Bản Windows `queue.ps1` chưa đổi: vẫn giới hạn 12 và 4 lần.
  - Hai script tự tìm bản mới nhất trong extension Cursor; đặt `CODEX_BIN` nếu muốn dùng bản khác.
  - Trên Mac dùng sandbox `workspace-write` (không cần `danger-full-access`, vì git, node, ImageMagick chạy thẳng, không qua WSL).

## Cách dùng

```powershell
powershell -File tools\codex-run\run.ps1 -Name <id> -Brief docs\codex-queue\<phiếu>.md -Cwd <thư mục làm việc> [-Effort xhigh] [-Image ảnh-tham-chiếu.png]
```

- Mỗi việc là một **phiếu** markdown trong `docs/codex-queue/`. Phiếu ghi rõ: mục tiêu, đường dẫn được ghi, đường dẫn cấm đụng, nguồn prompt, tiêu chí xong.
- Log của mỗi lần chạy nằm ở `.local/codex-runs/<id>/` (gitignored), gồm:
  - `brief.md`: phiếu đã kèm phần luật chung;
  - `events.jsonl`;
  - `last.md`: báo cáo cuối của Codex;
  - `err.txt`.
- **Codex không commit.** Claude (hoặc chủ dự án) xem kết quả, kiểm, rồi commit phần văn bản. Ảnh và âm là media, không vào Git: sao lưu bằng `pnpm media:push`.
- **`-Sandbox danger-full-access`** cho phiếu cần gọi `wsl.exe` (git, node, pnpm, ImageMagick chỉ có trong WSL). Sandbox `workspace-write` chặn lệnh này (`E_ACCESSDENIED`). Phiếu loại này phải tự ghi rõ đường dẫn được ghi.

## Chạy nhiều phiếu

```powershell
powershell -File tools\codex-run\queue.ps1 -List .local\codex-lane-a.txt [-WaitFor <chữ trong lệnh của hàng chờ khác>]
```

- File danh sách: mỗi dòng `tên | phiếu | thư mục | effort | sandbox | model` (model bỏ trống thì là `gpt-6.1-sol`). Dòng bắt đầu bằng `#` là chú thích.
- Gặp hạn mức ChatGPT ("try again at 8:54 AM"), `queue.ps1` chờ tới giờ đó cộng 2 phút rồi chạy lại phiếu. Log lần hỏng được giữ dưới tên `<tên>-prev-<giờ>`.
- `-WaitFor` chờ hàng chờ khác xong rồi mới bắt đầu, để hai lượt sinh ảnh không giành hạn mức của nhau.
- Hai danh sách chạy song song được, miễn là không ghi cùng thư mục.

## Ưu tiên (chủ dự án, 25/10)

1. Tạo **file ảnh** trước: ảnh 2D concept và ảnh tham chiếu cho Tripo/Meshy.
2. **Nhạc và âm:**
   - Sinh âm thật cần audio-lab trên Mac (Stable Audio 3 bản MLX).
   - Trên Dell chỉ chuẩn bị spec và prompt.
   - Codex không có công cụ tạo âm.
3. **3D:**
   - Trước hết viết **một file yêu cầu 3D**: prompt Tripo/Meshy, thông số, ảnh đính kèm.
   - Tạo model 3D làm sau, khi chủ dự án có giờ.

Danh sách phiếu và trạng thái: [`docs/CODEX_QUEUE.md`](../../docs/CODEX_QUEUE.md).
