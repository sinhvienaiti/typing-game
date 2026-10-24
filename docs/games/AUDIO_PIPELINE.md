# Đường ống âm thanh cho các game gõ chữ

> **Ngày:** 23/10/2026. **Trạng thái:** bản chính thức đầu tiên. Đã sửa theo hai bản phản biện: một về giấy phép và vận hành, một về thiết kế âm và bộ chấm. Danh sách lỗi đã sửa ở [phụ lục B](#phụ-lục-b-phản-biện-đã-xử-lý).
> **Dành cho:** chủ dự án, Claude khi làm âm, và các làn ráp game.
> **Phạm vi:** Rồng Giữ Ải (`games/dragon-hold`), Lời Gọi (`games/typing-defense`), Tuyến Cuối (`games/typing-survival`) và Space Typing.
> **Dựa trên:** 7 hướng nghiên cứu làm ngày 23/10/2026, hai bản thử "tai AI" chạy thật trên máy của chủ dự án (số liệu ở [phụ lục A](#phụ-lục-a-bản-thử-tai-ai-số-liệu-và-cách-chạy-lại)), và hai bản phản biện. Nguồn ghi bằng số [n], bấm vào để mở link. Danh sách đủ ở cuối bài. Ý nào chưa kiểm chứng thì ghi "(chưa kiểm chứng)".
> **Thứ tự ưu tiên:** tài liệu và mã của từng game (`catalog.ts`, `THEME_SOUND_LIST.md`, `M0_SOUND_LIST.md`) thắng tài liệu này. Con số nào ở đây khác tài liệu game thì chỉ là **đề xuất**. Phải sửa tài liệu game, có chủ dự án duyệt, rồi mới dùng.

---

## 0. Trả lời ngắn

Câu hỏi: có công cụ nào giúp AI tạo âm hay không, và có cách nào tốt hơn đề xuất của ChatGPT không?

- **Có cách tốt hơn, nhưng không có phép màu.** Khung của ChatGPT đúng hướng: viết spec, tạo âm, đo kỹ thuật, chủ dự án nghe, rồi sửa. Nhưng khung đó chỉ kiểm âm có "sạch" không. Nó không kiểm âm có hợp game không, có cùng một họ không, và có nghe rõ giữa trận không.
- **Năm thay đổi chính:**
  1. **Chọn nguồn theo loại âm, không dùng AI cho mọi thứ.** Phím giữ tổng hợp bằng mã. Nốt nhạc cụ lấy từ mẫu thu thật CC0. Lửa, nổ, nền và quái thì dùng mô hình chạy trên máy. Nhạc thì Claude viết MIDI rồi phát bằng mẫu thật.
  2. **Chọn phong cách trước, rồi mới tạo hàng loạt.** Mỗi game có một "bảng phong cách": 2–3 hướng âm, mỗi hướng 3–4 âm chữ ký, nghe trong một đoạn trận 20 s. Chủ dự án chọn hướng. Hướng thắng thành âm tham chiếu đầu tiên.
  3. **Tạo nhiều, máy lọc bản hỏng, người chọn bản hay.** Mỗi id tạo 16–32 ứng viên. Ở lô 1, máy chỉ được **chặn** bản hỏng kỹ thuật (clip, im lặng đầu, đuôi cụt, mối nối hở). Mọi chỉ số khác chỉ dùng để **xếp hạng** hoặc **gắn cờ**. Danh sách nghe luôn có một bản "khác nhất" và, ở khoảng 30 % số id, một bản máy xếp thấp. Nhờ vậy âm có cá tính không bị máy lọc mất, và ta đo được máy loại nhầm bao nhiêu.
  4. **Chấm âm ngay trong trận.** Máy dựng lại tiếng trận bằng bộ trộn thật của game. Có cả chuỗi thật "gõ xong từ → âm thưởng → giọng đọc từ", vì đây là chỗ dễ che tiếng đọc nhất.
  5. **Mỗi lần chủ dự án chấm đều thành dữ liệu.** Nghe mù, các bản đã cân cùng độ to, nhãn cố định. Máy chỉ được giao thêm quyền loại khi đã **đo được** nó loại đúng.
- **Công cụ chính đều miễn phí và chạy được trên Mac M4 16 GB** (bảng xếp hạng ở mục 3.1):
  - **Stable Audio 3 Small-SFX**, chạy qua MLX [[1]][s1][[2]][s2]. Trên M1, máy tạo một đoạn 10 s trong khoảng 1 s. Mô hình làm được biến thể từ một âm gốc, sửa lại một đoạn, và học thêm phong cách bằng LoRA. **Có điều kiện giấy phép** (xem dưới).
  - **ACE-Step 1.5** để phác nhạc, giấy phép MIT [[6]][s6].
  - **Thư viện CC0:** Kenney [[40]][s40], VCSL [[42]][s42] (có đàn tranh, cồng, mõ gỗ, trống khung), VSCO-2-CE [[43]][s43] (có cello, đàn hạc, sáo, kèn co [[85]][s85]).
  - **Bộ "tai":** ffmpeg, pyloudnorm, librosa, MoSQITo, audiobox-aesthetics, CLAP và AST [[15]][s15][[16]][s16][[18]][s18][[19]][s19][[20]][s20][[21]][s21].
- **Điều kiện giấy phép quan trọng nhất:** Stable Audio 3 theo Stability AI Community License [[4]][s4]. Làm game định bán là "mục đích thương mại" ngay từ lúc làm sản phẩm. Vì vậy phải đăng ký **khi bắt đầu làm**, không đợi lúc bán. Trần 1 triệu USD/năm tính cả các công ty liên kết và mọi nguồn thu. Chủ dự án xác nhận điều này ở bước 0 (mục 15) trước khi Claude tải mô hình.
- **Không cần tài khoản Hugging Face.** Bản MLX tải từ kho `stabilityai/stable-audio-3-optimized`, kho này không có cổng [[75]][s75]. Mọi script của Claude tắt việc dùng token ngầm.
- **Thời gian của chủ dự án:** khoảng 1 giờ chuẩn bị. Lô 1 (28 âm, 3 game) khoảng 1,5–2 giờ, chia 4–5 phiên. Cả tháng đầu khoảng 4–6 giờ.
- **Không tốn tiền vẫn làm được.** Nếu có 6 USD, khoản đáng chi nhất là một tháng ElevenLabs Starter, dành cho vài tiếng súng và tiếng quái khó [[34]][s34].
- **Nói thật:** Claude vẫn không nghe được. Bản thử cho thấy luật đo và ảnh phổ bắt lỗi kỹ thuật tốt. Các mô hình học máy chỉ bắt được một phần, có mô hình còn chấm bản lỗi cao hơn bản tốt. Chưa ai đo được máy loại đúng bao nhiêu phần trăm số bản chủ dự án sẽ chê. Ta sẽ đo bằng "bản dò" (mục 4.6). Tai chủ dự án vẫn là cổng cuối.

---

## 1. So với đề xuất của ChatGPT

| Bước | ChatGPT đề xuất | Còn thiếu gì | Bản này làm gì |
|---|---|---|---|
| Phong cách | Không có | 28 âm tạo rời rạc sẽ không cùng một thế giới | Bảng phong cách cho từng game trước lô 1 (mục 5.2) |
| Spec | AI viết spec | Spec là văn xuôi, máy không kiểm được | Mỗi id có một thẻ spec YAML, sinh từ `catalog.ts` và danh sách âm. Thẻ ghi độ dài, điểm bắt đầu, số biến thể, nhãn loại âm, âm tham chiếu và vai trò tần số |
| Tạo | Dùng một công cụ SFX | Mô hình AI yếu ở 4 loại: tiếng ngắn dưới 50 ms, nốt đúng cao độ, nhạc cụ Việt, và stem nhạc khớp ô nhịp | Chọn nguồn theo loại âm (mục 3). Mỗi id có 16–32 ứng viên |
| Đo kỹ thuật | Đo độ dài, dạng sóng, đỉnh, RMS/LUFS, clip, phổ | LUFS tích hợp vô nghĩa với tiếng dưới 400 ms (cửa sổ BS.1770 dài 400 ms [[20]][s20]). Đo sau khi chuẩn hóa thì không thấy clip có sẵn trong file gốc. Không có bộ dò lỗi riêng của âm do AI tạo | Đo trên **file gốc** trước, rồi đo lại sau khi sửa. Có bộ dò lỗi do mô hình tạo (mục 4.3). Ngưỡng lấy từ âm tham chiếu đã duyệt |
| Chặn hay xếp hạng | Đạt luật là xong | "Đạt luật" không có nghĩa là "hay". Bản thử gắn nhãn WEAK cho 5/8 âm Kenney chuyên nghiệp | Lô 1 chỉ chặn lỗi vệ sinh. Ngưỡng phổ, độ dày, độ to chỉ dùng để xếp hạng, cho đến khi có âm đã duyệt |
| Sửa | Tạo lại | Tạo lại tốn lượt, trong khi nhiều lỗi sửa được bằng xử lý tín hiệu | Sửa trước: cắt đầu, làm mờ, lọc, giới hạn đỉnh, tạo lại riêng đoạn hỏng. Chỉ tạo lại khi không sửa được |
| Chọn | Chủ dự án nghe | Không xếp hạng, không nghe mù, bản to hơn thường nghe "hay hơn". Nếu chỉ nghe top-3 của máy thì không biết máy loại nhầm gì | Nghe mù, đã cân độ to. Danh sách nghe gồm bản đứng đầu, bản khác nhất, và bản dò máy xếp thấp |
| Biến thể | Không có | Bộ biến thể mới là thứ người chơi nghe hàng trăm lần mỗi trận | Có lượt nghe biến thể riêng, khoảng 30 s mỗi id (mục 5.1 bước 10) |
| Bối cảnh | Ghép vào game rồi nghe | Không đo tiếng trận che giọng đọc, không đo mật độ, không đo độ mỏi tai | Dựng tiếng trận bằng bộ trộn thật, gồm chuỗi "xong từ → giọng đọc" (mục 6) |
| Phản hồi | AI tự chỉnh | Nhận xét rời rạc, không thành dữ liệu | Nhãn cố định đi kèm cách sửa định sẵn. Điểm chấm dùng để hiệu chỉnh từng họ âm (mục 4.6) |
| Giấy phép | Không có | Không biết file nào được phát hành | Mỗi file có một mục trong `SOURCES.json`. Script kiểm giấy phép chặn bản dựng khi có lỗi (mục 10) |

**Những điểm đúng của ChatGPT, nên giữ:** có spec trước khi tạo, đo bằng ffmpeg và librosa, có vòng lặp tự động, và tai chủ dự án là cổng cuối. Bản này giữ nguyên khung đó, chỉ thêm những gì còn thiếu.

---

## 2. Điều kiện thực tế

| Mục | Hiện trạng (kiểm trên máy ngày 23/10/2026) | Ảnh hưởng |
|---|---|---|
| Máy | Mac mini, Apple M4 (4 nhân hiệu năng, 6 nhân tiết kiệm), RAM 16 GB, macOS 15.5. Ổ còn trống 81 GiB. Hai bản thử đang chiếm khoảng 15 GB trong scratchpad, xóa được sau giai đoạn 0 | Chạy được mô hình tạo âm nhỏ (dưới 2B tham số) và mô hình nghe khoảng 7B ở 4-bit. Mỗi lúc chỉ chạy một mô hình nặng, không chạy cùng Vite và Chrome |
| Phần mềm | Có Homebrew, Node 24, pnpm 11, Chrome 155, rclone, lệnh `say` của macOS. **Chưa có:** ffmpeg, sox, uv, cmake, Xcode đầy đủ, **Rosetta**. Python của hệ thống là 3.9.6 | Cần `brew install ffmpeg uv`. Mọi việc Python chạy trong venv 3.12, vì librosa 1.0 cần Python 3.12 trở lên. Công cụ chỉ có bản x86_64 (như `sfizz_render`) không chạy được |
| Cài cần quyền admin | Surge XT qua Homebrew là gói `.pkg` [[79]][s79], thường hỏi mật khẩu admin | Surge XT thành tùy chọn. Mặc định tổng hợp tiếng điện bằng numpy và pedalboard |
| Loa | Mac mini chỉ có một loa trong máy | Giả lập loa nhỏ bằng bộ lọc cao 200 Hz. Mỗi lô, chủ dự án nghe bản trộn trên điện thoại và laptop một lần |
| Tiền | Không dùng API trả phí. Có ChatGPT Plus | ChatGPT không tạo âm được: Sora đã đóng app ngày 26/4 và API ngày 24/9/2026 [[33]][s33]. Codex CLI chỉ nhận ảnh [[32]][s32], và hiện chỉ nằm trong extension của Cursor, không có trên PATH |
| Repo | Các repo game công khai. Media không vào Git. Chưa repo nào có file `LICENSE` | Âm, trọng số mô hình, LoRA và dữ liệu huấn luyện để ngoài repo hoặc trên Drive |
| Khóa | Claude không dùng và không giữ khóa API hay token | Mọi việc đăng nhập, mở tài khoản và chấp nhận giấy phép do chủ dự án làm |
| Làm song song | Ba làn cân bằng đang sửa cả ba game | Việc sửa mã âm trong game (mục 6.3) làm sau khi các làn đó merge, hoặc trong worktree riêng. Việc tạo âm ngoài repo không bị chặn |
| Mã âm | Rồng Giữ Ải có `FileBank`, `LayeredBank`, `manifest.json` và bộ thử (harness) dựng tiếng không cần chạy game. Tuyến Cuối dùng `SceneAudio` của kit với `sounds: {}`. Lời Gọi tự tổng hợp âm, chưa có bộ tải file | Rồng Giữ Ải gần ghép được file nhất. Hai game kia cần nối bộ tải trước (mục 6.3) |
| Giọng đọc từ | Phát bằng `speechSynthesis` của trình duyệt, nằm **ngoài** đồ thị WebAudio. Giọng ưu tiên gồm "Google US English" của Chrome, là giọng qua mạng | Bài thử không chạy game không thu được giọng thật. Phải dùng bản ghi giọng làm mẫu thử (mục 6.1, bài C) |

---

## 3. Công cụ và nguồn âm

### 3.1 Bảng xếp hạng công cụ

Xếp theo giá trị cho chủ dự án: miễn phí, chạy trên máy, giấy phép cho phép bán sau này.

**A. Nguồn hiệu ứng (SFX)**

| Hạng | Công cụ | Dùng cho | Chi phí | Giấy phép | Chạy trên M4 16 GB | Điều kiện |
|---|---|---|---|---|---|---|
| 1 | **Stable Audio 3 Small-SFX** (ra ngày 20/5/2026 [[5]][s5]) qua MLX [[1]][s1][[2]][s2][[3]][s3] | Lửa, nổ, bẫy, quái, thân tiếng súng, nền | 0 đ | Stability AI Community License [[4]][s4]. Thương mại miễn phí khi bạn **và công ty liên kết** có doanh thu dưới 1 triệu USD/năm từ mọi nguồn. Phải đăng ký khi bắt đầu làm game định bán. Bạn sở hữu âm tạo ra. Không dùng âm tạo ra để huấn luyện mô hình nền. Áp dụng thêm chính sách sử dụng (AUP) và điều khoản Gemma cho bộ mã hóa chữ T5Gemma [[86]][s86] | Có đường MLX chính thức. Trên M1 8 GB: khoảng 1 s cho 10 s âm, RAM đỉnh 1,6 GB. README nói M4 nhanh hơn 2–3 lần [[2]][s2]. **Chưa đo trên máy này** | Chỉ dùng khi bước 0 (mục 10.1) trả lời "đủ điều kiện". Bản thử 6 id (giai đoạn 2) quyết định đi tiếp hay không |
| 2 | **Ghép lớp từ thư viện CC0:** Kenney [[40]][s40], VCSL [[42]][s42], VSCO-2-CE [[43]][s43] | Lớp đầu tiếng, UI, gỗ, kim loại, nốt nhạc cụ, kèn | 0 đ | CC0, không cần ghi công | Chỉ là file. Claude tải được, không cần tài khoản | Thành hạng 1 nếu không dùng được Stable Audio 3 |
| 3 | **Tổng hợp bằng mã:** WebAudio hiện có, numpy, pedalboard [[45]][s45] | Phím, UI, tiếng điện, lớp trầm (sub) | 0 đ | Mã của dự án. pedalboard là GPL-3.0, chỉ dùng trên máy | Có | Surge XT [[46]][s46] là tùy chọn, cần mật khẩu admin |
| 4 | **Tự ghi bằng điện thoại** | Tre, giấy, chuông đồng, cồng, sáo trúc, giọng người | 0 đ | Của chủ dự án. Người khác ghi thì cần giấy đồng ý (mục 10.4) | — | Sạch giấy phép nhất |
| 5 | **MOSS-SoundEffect v2.0** [[8]][s8] | Bộ tạo SFX thứ hai | 0 đ | Apache-2.0 | Tài liệu chỉ nói CUDA. Chạy trên MPS chưa kiểm chứng | Thử sớm nếu bước 0 trả lời "không đủ điều kiện" |
| 6 | **ElevenLabs Starter** [[34]][s34] | Vài tiếng súng, tiếng quái khó | 6 USD/tháng (1 USD tháng đầu, đến hết 1/11/2026) | Có quyền thương mại cho âm tạo trong thời gian đăng ký | Trình duyệt. Chủ dự án tự chạy | Chỉ khi lô 1 cho thấy thiếu |

**B. Nhạc**

| Hạng | Công cụ | Dùng cho | Chi phí | Giấy phép | Chạy trên M4 16 GB | Điều kiện |
|---|---|---|---|---|---|---|
| 1 | **MIDI do Claude viết + bộ phát mẫu bằng Python** (numpy, soundfile, mido [[88]][s88]) với mẫu VCSL và VSCO-2-CE | Stem đúng BPM, đúng giọng, khớp ô nhịp | 0 đ | CC0 cho mẫu. Mã của dự án. mido theo MIT (chưa kiểm lại) | Có, thuần Python trong venv | Thay cho `sfizz_render`: bản macOS chính thức duy nhất (1.2.3, 01/2024) chỉ là x86_64 [[78]][s78], và máy không có Rosetta |
| 2 | **ACE-Step 1.5** [[6]][s6][[7]][s7] | Phác chủ đề, stinger | 0 đ | MIT cho cả mã và trọng số | Phần mô hình ngôn ngữ chạy MLX, phần DiT chạy MPS [[6]][s6]. Dùng bản 0,6B hoặc 1,7B với DiT turbo. Kho trọng số khoảng 10,1 GB [[87]][s87]. Bản XL không vừa máy | Kho có mã mô hình tùy biến, tự tải khi chạy lần đầu. Phải ghim phiên bản. README cảnh báo nhạc tạo ra có thể giống nhạc có sẵn |
| 3 | **Stable Audio 3 Small-Music** | Pad, kết cấu | 0 đ | Như Stable Audio 3 | Như Stable Audio 3 | Cùng điều kiện bước 0. Chưa kiểm với nhạc cụ Việt |
| 4 | **Magenta RealTime 2** [[9]][s9] | Nền nhạc thích ứng, khóa thang âm bằng MIDI | 0 đ | Mã Apache-2.0, trọng số CC-BY 4.0 (phải ghi công) | Bản `mrt2_small` chạy kịp thời gian thực trên M4 thường [[9]][s9] | Thiên về nhạc phương Tây. Giai đoạn 7 |

**C. Tai AI** (đều chạy trên máy, không cần tài khoản)

| Hạng | Công cụ | Vai trò | Giấy phép | Trên máy này | Đã chạy trong bản thử? |
|---|---|---|---|---|---|
| 1 | Luật đo: ffmpeg [[21]][s21], pyloudnorm [[20]][s20], librosa, numpy | Cổng vệ sinh, đặc trưng xếp hạng | GPL, MIT, ISC. Chỉ dùng trên máy | Khoảng 0,4 s mỗi file, kể cả vẽ ảnh | Có |
| 2 | Thẻ ảnh PNG cho Claude đọc | Nhìn lỗi cấu trúc: clip, đầu tiếng chậm, đuôi cụt, mối nối | matplotlib | Có | Có |
| 3 | MoSQITo [[19]][s19] | Độ chói, độ gắt, chỉ số dễ hiểu lời nói (SII) | Apache-2.0 | Thuần Python | Chưa |
| 4 | audiobox-aesthetics [[15]][s15] | Xếp hạng trong cùng một nhóm âm | CC-BY-4.0 | MPS, 0,15–0,29 s mỗi file, tải 415,5 MB | Có |
| 5 | CLAP của LAION [[16]][s16] | Nhận loại âm, chỉ để gắn cờ | Apache-2.0 (nhãn trên Hugging Face) | MPS, hai bản 614 MB và 776 MB | Có |
| 6 | AST [[18]][s18] | Nhãn AudioSet, chỉ để gắn cờ | BSD-3 | MPS, 346 MB | Có |
| 7 | Qwen2.5-Omni-7B qua llama.cpp [[23]][s23] (tùy chọn) | Chú thích để tham khảo | File LICENSE gốc là Apache-2.0 [[82]][s82], nhưng kho GGUF mà llama.cpp tải lại gắn nhãn `qwen-research` [[81]][s81] | Khoảng 6,2 GB, 13–41 s mỗi lần gọi | Có, ở bản thử 1. Yếu với SFX ngắn |

**D. Dịch vụ online:** xem mục 3.3. Mọi dịch vụ đều cần tài khoản và khóa của chủ dự án, và chủ dự án tự chạy.

### 3.2 Nguồn theo loại âm

| Loại âm | Hạng 1 | Hạng 2 | Hạng 3 | Ghi chú |
|---|---|---|---|---|
| **Phím đúng/sai** (`key.ok`, `type.key`, `key-right`, `key-wrong`) | Tổng hợp bằng mã (theo luật dự án), chỉnh bằng bản dựng không chạy game và tai AI | Một mẫu thu thật (Kenney CC0 hoặc tự ghi), mã đổi cao độ | — | Mô hình khuếch tán yếu với tiếng dưới 50 ms. Lời Gọi giữ `key-right`/`key-wrong` tổng hợp (TK 24.6). Đề xuất phổ mới cho phím ở mục 6.2 |
| **UI** | Kenney Interface/UI Audio (CC0) [[40]][s40], có xử lý | Tự ghi tiếng tre, giấy, gỗ | Stable Audio 3, rồi cắt ngắn | Không to hơn tiếng phím |
| **Thưởng có cao độ** (`word-hit`, `kill.chime`, `type.word`, `learn.*`) | Mẫu nhạc cụ thật từ VCSL, phát từng nốt bằng bộ phát mẫu Python. **Dời cao độ tối đa 3 bán cung** | Lấy một nốt tốt, mã đổi cao độ trong khoảng đó | Mô hình vật lý Faust (chuông, sáo) [[48]][s48] | Không viết prompt cho từng nốt. Nốt lệch dưới 10 cent. Đàn tranh VCSL chỉ có B1–B4, các nốt C#, D#, F#, G#, B [[83]][s83]. Xem mục 8.2 về `word-hit` |
| **Va chạm, trúng** (`hit.*`, `fire.impact.*`, `enemy.*.hit`) | Ghép lớp: lớp đầu từ Kenney Impact (CC0), thân và đuôi từ Stable Audio 3 | Stable Audio 3 nguyên khối, tạo lại thân hoặc đuôi bằng inpaint | Tổng hợp | Bậc trúng của Tuyến Cuối ghép lúc chạy từ các lớp riêng (mục 6.3) |
| **Súng, khạc, bắn** (`gun.xung`, `fire.cast`, `arrow-fire`, `wordshot-fire`) | Stable Audio 3, cộng lớp cơ khí Kenney, cộng sub tổng hợp | ElevenLabs gói trả phí | Tổng hợp thuần | `gun.xung` phát 5 lần mỗi giây nên phải ngắn |
| **Điện, hồ quang** (`gun.tia.*`, `hurt.drain`) | Tổng hợp bằng numpy và pedalboard | Stable Audio 3 | Surge XT (nếu chủ dự án cài), 99Sounds Electromagnetic [[50]][s50] | Giới hạn năng lượng 2–5 kHz khi đông quái |
| **Nổ, bẫy** (`blast`, `trap.pine-bomb.trigger`, `dragon.skyfire.impact`) | Stable Audio 3 Small-SFX | Ghép từ Kenney | ElevenLabs gói trả phí | Ở Rồng Giữ Ải chỉ Bom Hạt Thông là nổ. Lưới Phóng và Gai Chông không nổ. Lời Gọi dùng trống và giấy, không nổ lách tách |
| **Lửa, luồng lửa** (`dragon.breath`) | Stable Audio 3 | Bản ghi lửa CC0 trên Freesound (chủ dự án tải) [[41]][s41] | ElevenLabs gói trả phí | Tách 3 phần: đầu, vòng lặp, cuối |
| **Tiếng sinh vật** (`*.spawn`, `dragon.hurt`, `dragon.roar`) | Ghép tiếng thú thật CC0, hạ 5–12 bán cung rồi xếp lớp. Đây là cách làm tiếng rồng của Game of Thrones và How to Train Your Dragon [[61]][s61] | Stable Audio 3. Tốt cho kết cấu, còn tiếng kêu thì chưa kiểm chứng | Chủ dự án tự gầm vào điện thoại, Claude hạ giọng. Randy Thom cũng dùng chính giọng mình [[61]][s61] | Cấm nhãn Speech |
| **Nền lặp** (`amb.*`, `*.march`) | Stable Audio 3, rồi sửa mối nối | Bản ghi hiện trường CC0 | Tổng hợp bằng mã (như hiện nay) | Độ dài theo tài liệu game. Ví dụ `amb.forest` là vòng 6 s |
| **Báo nguy, stinger** (`wave.horn`, `alarm.surge`, `leak`, `end.*`) | Mẫu nhạc cụ (kèn co VSCO [[85]][s85], cồng và trống khung VCSL [[84]][s84]) cộng MIDI | Stable Audio 3 (tù và, còi) | ElevenLabs | Báo nguy chỉ có một phiên bản cố định, để người chơi học được |
| **Nhạc nhiều lớp** (`music.*`) | MIDI do Claude viết, phát bằng mẫu CC0 qua bộ phát mẫu Python. Đúng BPM, đúng giọng, stem khớp ô nhịp | ACE-Step 1.5 để phác ý tưởng và làm stinger | Stable Audio 3 Small-Music cho pad. Magenta RealTime 2 cho nền thích ứng | Mô hình tạo nhạc không tự sinh các stem tách rời trên cùng một lưới nhịp |
| **Nhạc cụ dân gian Việt** | Chủ dự án tự ghi hoặc nhờ người ghi (sáo trúc, trống cơm), có giấy đồng ý | VCSL: Dan Tranh, Slit Drum, Woodblock, Frame Drum [[42]][s42] | LoRA của Stable Audio 3 học trên bản ghi của chủ dự án. Faust `fluteModel` [[48]][s48] | Chưa tìm được thư viện miễn phí đã kiểm chứng cho sáo trúc, trống cơm hay đàn bầu. Chuông và cồng VCSL phải được chủ dự án duyệt (mục 8.2) |
| **Giọng người** (`amb-villager-call`, tiếng "Ơ… ơi!") | Chủ dự án và người nhà ghi 4 biến thể, có giấy đồng ý | — | — | Không dùng AI. Stable Audio 3 không có giọng người [[3]][s3] |

**Không dùng Sonniss ở lô 1 và lô 2.** Kenney, VCSL, VSCO-2-CE, Freesound CC0 và bản tự ghi là đủ. Lý do ở mục 10.2.

### 3.3 Dịch vụ online (chủ dự án mở tài khoản, giữ khóa và tự chạy)

| Dịch vụ | Gói miễn phí | Quyền thương mại | Cách dùng |
|---|---|---|---|
| **ElevenLabs Sound Effects** [[34]][s34] | 10.000 credit mỗi tháng. Mỗi giây âm tốn khoảng 40 credit khi đặt độ dài. Tính ra khoảng 250 giây SFX mỗi tháng | Gói miễn phí: trang trợ giúp nói không được dùng thương mại và phải ghi công, còn trang thư viện SFX lại nói khác. Coi như **không thương mại**. Gói Starter giá 6 USD/tháng (1 USD tháng đầu, đến hết 1/11/2026) có quyền thương mại cho âm tạo trong thời gian đăng ký | Gói miễn phí chỉ để chủ dự án dò prompt cho âm khó, không phát hành âm đó. Nếu có tiền: mua một tháng Starter, tạo hết bản cuối, rồi hủy |
| **Stability API (bản online)** [[68]][s68] | 25 credit cho tài khoản mới, khoảng 3 lần tạo | 0,08 USD mỗi lần tạo | Chỉ để so với bản chạy trên máy. Cần tài khoản và khóa |
| **fal.ai** [[74]][s74] | Không | 0,002 USD mỗi giây ElevenLabs SFX | Cần khóa của chủ dự án |
| **Suno** [[35]][s35] | Không cho tải về | Gói Pro 8 USD có quyền thương mại, nhưng người dùng không phải chủ sở hữu. Tải tối đa 20 bài mỗi tháng | Không khuyên dùng |
| **Udio** [[36]][s36] | Đã tắt tải về từ 30/10/2025 | — | Không dùng |
| **Lyria 3.5 qua Gemini API** [[30]][s30] | API không có gói miễn phí | 0,08 USD mỗi bài, có dấu SynthID | Dùng cho nhạc nếu có ít tiền. Cần khóa |
| **Flow Music trong Google AI Plus** [[38]][s38] | Có tín dụng hằng ngày (nguồn thứ cấp) | Gói AI Plus có quyền thương mại. Giá ở Việt Nam lúc ra mắt khoảng 122.000 đ/tháng (giá hiện tại chưa kiểm) | Phác nhạc nếu có ít tiền |
| **Gemini API để "nghe"** [[30]][s30] | Bản Flash có gói miễn phí. Âm gửi lên bị nén còn 16 kbps mono | Dữ liệu gói miễn phí được dùng để cải thiện sản phẩm và có thể có người đọc | Mặc định tắt |
| **Gemini CLI** [[31]][s31] | Từ 18/6/2026, gói miễn phí đăng nhập bằng Google đã chuyển sang Antigravity CLI | — | Chưa kiểm chứng Antigravity có nhận file âm không |
| **ChatGPT Plus, Codex CLI** [[32]][s32][[33]][s33] | Không tạo được âm | — | Dùng để viết lại prompt. Codex làm người duyệt ảnh thứ hai **chỉ khi chủ dự án đồng ý**, vì nó dùng phiên đăng nhập ChatGPT của chủ dự án |
| **Hugging Face ZeroGPU** [[67]][s67] | Tài khoản miễn phí được 5 phút GPU mỗi ngày | Theo giấy phép từng mô hình | Dự phòng nếu MOSS không chạy được trên Mac. Chủ dự án đăng nhập |

### 3.4 Thư viện và công cụ dựng âm

| Nguồn | Có gì | Giấy phép | Cách dùng |
|---|---|---|---|
| **Kenney** [[40]][s40] | 10 gói âm: Impact 130 file (26 họ, mỗi họ 5 bản đánh số), Interface 100, Sci-fi 70, RPG 50 | CC0 | Lớp đầu tiếng, UI, âm tham chiếu ban đầu. 26 họ × 5 bản của gói Impact là chuẩn tham chiếu cho độ khác giữa các biến thể (mục 5.2) |
| **VCSL** [[42]][s42] | Dan Tranh (Normal, Gliss, Tremolo, Vibrato, FX; B1–B4) [[83]][s83], Gong 1 và 2, Slit Drum, Woodblock, Anvil, Brake Drum, Hand Chimes, Tubular Bells, Hand Bells Nepalese [[84]][s84], Frame Drum, Folk Harp, Concert Harp | CC0 | Nốt thưởng, bộ gõ dân gian, nhạc. Kho khoảng 3,8 GB, nên chỉ tải thưa (sparse checkout) các nhạc cụ cần |
| **VSCO-2-CE** [[43]][s43] | Dây: Cello Section, Harp, Viola, Violin. Gỗ: Flute, Piccolo, Clarinet, Oboe, Bassoon. Đồng: F Horn, Trombone, Trumpet, Tuba. Bộ gõ [[85]][s85] | CC0 | Nhạc của Rồng Giữ Ải, tù và |
| **Freesound** [[41]][s41] | Lọc được theo giấy phép, điểm đánh giá và lượt tải | Tùy từng âm. CC0 dùng được. CC-BY phải ghi công. NC và Sampling+ thì cấm. Người tải lên có thể đặt "tùy chọn AI tạo sinh" [[80]][s80]. Điều khoản API nói dùng API cho mục đích thương mại phải thương lượng riêng | Chủ dự án **tìm và tải bằng tay trên web**. Script tìm qua API chỉ dùng như công cụ nghiên cứu trước khi bán. Ghi tùy chọn AI của từng âm vào sổ nguồn |
| **99Sounds** [[50]][s50] | Âm điện ảnh, gói Electromagnetic | Miễn phí bản quyền, kể cả làm game. Cấm bán lại | Lớp tiếng điện cho Tuyến Cuối. Có thể phải đăng ký bằng email (chủ dự án làm) |
| **Sonniss GDC** [[39]][s39] | Gói 2026 khoảng 7,47 GB, cộng kho các năm 2015–2024 | v2.0, hiệu lực từ 27/8/2026. Dùng thương mại, không cần ghi công. Cấm phân phối lại "như hiệu ứng âm". Có mục "NO AI TRAINING OR USAGE" | **Không dùng ở lô 1–2.** Điều kiện dùng sau này ở mục 10.2 |
| **Mixkit** [[49]][s49] | Kho âm có tuyển chọn | Dùng trong game được. Cấm phân phối file riêng lẻ | Ít dùng |

**Công cụ dựng âm**, đều chỉ dùng trên máy và không đóng gói vào game:

- **ffmpeg** (GPL) [[21]][s21]: đo đỉnh thật bằng `ebur128 peak=true`, chạy `astats`, `silencedetect`, và vẽ ảnh bằng `showspectrumpic`.
- **pyloudnorm** (MIT) [[20]][s20]: đặt `block_size=0.1` khi đo tiếng ngắn.
- **librosa** (ISC).
- **MoSQITo** (Apache-2.0) [[19]][s19]: đo độ chói (sharpness), độ gắt (roughness) và SII.
- **pedalboard** (GPL-3.0) [[45]][s45]: chuỗi xử lý tín hiệu. Không bao giờ chép mã của nó vào repo (mục 10.9).
- **Bộ phát mẫu Python** (sẽ viết): đọc tên file VCSL (nốt, cường độ), đọc MIDI bằng mido, trộn bằng numpy.
- **rubberband** (GPL) [[90]][s90]: dời cao độ giữ formant, chỉ khi cần dời quá 3 bán cung. Cần `brew install rubberband` (chủ dự án duyệt). Cờ chính xác chưa kiểm.
- **node-web-audio-api** (BSD-3) [[47]][s47]: chạy `OfflineAudioContext` trong Node.
- **Faust** [[48]][s48]: mô hình vật lý chuông, sáo (giai đoạn 7).
- **Không dùng mặc định:** `sfizz_render` [[44]][s44] (chỉ có bản x86_64 [[78]][s78]) và FluidSynth (cần soundfont SF2, chưa có bộ SF2 CC0 nào được chọn).

### 3.5 Không dùng

- **Mô hình có trọng số phi thương mại:** AudioGen, MusicGen, MAGNeT [[10]][s10], MMAudio [[11]][s11], Woosh [[12]][s12], TangoFlux [[13]][s13], AudioX [[14]][s14], AudioLDM 1 và 2 [[69]][s69], ThinkSound và PrismAudio [[70]][s70]. **Không tải về cho dự án này, kể cả chỉ để so chất lượng.** Dùng để đo chuẩn cho một game định bán cũng có thể bị coi là mục đích thương mại. Thước đo chất lượng là âm CC0 tham chiếu và lựa chọn của chủ dự án.
- **Mô hình "nghe" phi thương mại:** Qwen2.5-Omni-3B [[24]][s24], Audio Flamingo 2 và 3 [[25]][s25], các mô hình huấn luyện sẵn của Essentia [[73]][s73].
- **Quá nặng cho 16 GB:** HunyuanVideo-Foley [[71]][s71] (cần video đầu vào, giấy phép loại trừ EU, Anh và Hàn Quốc), YuE2 [[72]][s72], Qwen3-Omni (bản Q4 nặng 18,6 GB) [[26]][s26].
- **Thư viện không dùng:**
  - BBC Sound Effects: chỉ cho dùng cá nhân và giáo dục [[49]][s49].
  - Pixabay: cấm khai thác dữ liệu cho học máy, và nguồn gốc file không rõ [[49]][s49].
  - Zapsplat: chưa đọc được điều khoản.

---

## 4. "Tai AI": bộ phê bình nhiều lớp

> Claude không nghe được. Claude chỉ làm được ba việc: đo, nhìn ảnh và so sánh. Bộ phê bình dưới đây ghép nhiều tín hiệu yếu để **loại bản hỏng** và **xếp hạng** bản còn lại. Nó không quyết định âm nào "hay". Mỗi lớp chỉ được giao việc mà bản thử đã cho thấy nó làm được.

### 4.1 Các lớp

| Lớp | Câu hỏi | Công cụ | Vai trò ở lô 1 | Khi nào được thêm quyền | Điểm mù |
|---|---|---|---|---|---|
| **L0. Thẻ spec** | Âm này cần thế nào? | Thẻ YAML cho mỗi id | Nơi đặt ngưỡng, ghi âm tham chiếu và vai trò tần số | — | Chỉ tốt khi âm tham chiếu tốt |
| **L1. Cổng vệ sinh** | Âm có hỏng kỹ thuật không? | ffmpeg `ebur128` (đỉnh thật), pyloudnorm, numpy [[20]][s20][[21]][s21]. Đo trên **file gốc**, rồi đo lại sau khi sửa | **Chặn** (mục 4.3) | — | Không đo được gu |
| **L1b. Dò lỗi do mô hình tạo** | Có tiếng vọng trước đầu tiếng, rít cao tần, xoáy pha, rung cao độ không? | numpy, librosa | **Gắn cờ** | Thành cổng chặn sau khi chỉnh ngưỡng bằng nhãn "rè/lỗi" của chủ dự án ở lô 0 | Ngưỡng chưa có |
| **L2. Đặc trưng cảm nhận** | Có lực không? Đục không? Chói không? Mỏng không? | librosa và MoSQITo [[19]][s19]: thời gian lên, độ nảy (punch) theo mô hình của Fenton [[65]][s65], độ sắc ở điểm trúng, dải đục 200–500 Hz, độ chói, độ gắt, đuôi, độ mất trên loa nhỏ, tỉ lệ năng lượng theo dải | **Xếp hạng và gắn cờ.** Không chặn | Có mục tiêu theo chất liệu khi họ âm có từ 5 âm đã duyệt | Ngưỡng chung chặn nhầm âm tốt: bản thử gắn WEAK cho 5/8 âm Kenney |
| **L3. Thẩm mỹ học máy** | Nghe có "chuyên nghiệp" không? | audiobox-aesthetics PQ và CE [[15]][s15] | Xếp hạng trong cùng một nhóm. **Trọng số 0 với họ âm "bẩn có chủ ý"** (mục 4.4) | Họ âm bẩn: khi có từ 10 âm đã duyệt | Chỉ nghe 16 kHz mono. Đệm mọi âm thành 10 s. Không phát hiện âm mỏng. Phạt cả âm cố ý bẩn |
| **L4. Ngữ nghĩa** | Đúng loại âm, đúng chất liệu không? | CLAP zero-shot [[16]][s16], AST [[18]][s18] | **Chỉ gắn cờ**, trọng số tối đa 0,1. Âm ngắn chấm trên bản lặp 3–4 s | Khi đã kiểm trên ít nhất 20 âm đã duyệt của từng game | Điểm giống prompt không phải điểm chất lượng. CLAP gọi nhiều tiếng trúng là "UI click". AST gắn "Music" cho tiếng laser |
| **L5. Khoảng cách tham chiếu** | Âm này có giống bộ âm đã duyệt không? | Vector CLAP hoặc PANNs, chỉ số KAD [[22]][s22] | **Trọng số 0** | Khi họ âm có từ 5 âm đã duyệt. KAD cho cả bộ khi có từ 20 | Ở lô 1 chưa có gì để so, ngoài âm thắng bảng phong cách |
| **L6. Thẻ ảnh** | Nhìn thấy lỗi gì? | PNG: dạng sóng có vạch clip, mel spectrogram tới 24 kHz có vạch 8 kHz, đường độ to, ảnh phóng mối nối | Claude đọc ảnh của top-6, bản dò và mọi ca bị cờ | — | Thấy cấu trúc, không thấy gu. Chỉ gửi ảnh của âm CC0, âm tự ghi và âm do mô hình tạo (mục 10.3) |
| **L7. Mô hình nghe** (tùy chọn) | Mô hình nghe thấy gì? | Qwen2.5-Omni-7B qua `llama-server` [[23]][s23] | Chú thích để tham khảo. Chỉ tính khi khớp với AST | — | Dễ bị prompt dẫn dắt. Bỏ sót clip và khoảng im lặng |
| **L8. Chủ dự án** | Âm có hay không, có hợp game không? | Bảng Nghe (mục 7) | Cổng cuối, và là nguồn dữ liệu hiệu chỉnh | — | Tai mỏi. Thiết bị nghe khác nhau |

### 4.2 Bằng chứng từ hai bản thử trên máy chủ dự án

Hai bản thử chạy trên M4 16 GB, không cần tài khoản hay khóa. Bản thứ hai có 40 âm: 8 âm tổng hợp mẫu, 8 âm Kenney CC0 và 24 bản làm hỏng có kiểm soát. Số liệu đầy đủ và lệnh chạy lại ở phụ lục A.

| Lớp | Bắt clip (8 cặp) | Bắt đục (8 cặp) | Bắt mỏng (8 cặp) | Lỗi đáng nhớ |
|---|---|---|---|---|
| Luật đo | 8/8 | 8/8 | 5,5/8 | Kết quả hơi "vòng tròn": cùng một người viết luật và bản làm hỏng. Luật báo "đục" nhầm cho tiếng chuông. Gắn WEAK cho 5/8 âm Kenney chuyên nghiệp |
| audiobox PQ | 8/8 | 6/8 | 1/8 | Bản mỏng thắng 7/8 cặp. Ở bản thử 1, tiếng "bíp" sóng sin được PQ cao nhất (7,37). Phạt âm cố ý gắt: tiếng nổ Kenney 5,27, tiếng động cơ 4,38 |
| CLAP, điểm giống prompt | 2–4/8 | 4–5/8 | 3–6/8 | Cả hai bản CLAP đều chấm bản bị clip là "punchy impact" nhất |
| CLAP zero-shot, loại âm | — | — | — | **Đúng:** laser, nổ, lửa, chuông đồng, động cơ, cú đấm. **Sai:** bản CLAP lớn gọi 7/16 âm gốc là "a user interface click", gồm Kenney Metal, Wood, Generic và tiếng trúng tổng hợp tốt. Bản CLAP nhỏ gọi tiếng trúng đục là "a fire breath whoosh" |
| AST | 4/8 | 3/8 | 6/8 | **Đúng:** nổ, động cơ, keng, gõ. **Sai:** laser Kenney thành "Music 0,246", tiếng zap tổng hợp "Music 0,178", Kenney Wood chỉ được "Sound effect 0,127", Kenney Generic có "Speech 0,183" ở hạng 2. Tiếng "bíp" yếu không có nhãn nào tự tin (0,057) |
| MiDashengLM-0.6B [[27]][s27] | — | — | — | Trả lời "distorted" cho cả 40/40 file. Gọi một tiếng click là "người đang nói" |
| Qwen2.5-Omni-7B (bản thử 1) | Bỏ sót | — | — | Không phát hiện clip, không phát hiện 250 ms im lặng ở đầu. Khi prompt dẫn dắt, gọi sóng sin là "vũ khí nặng". Gọi tiếng click là "tiếng ù liên tục" |
| Thẻ ảnh PNG | Thấy | Thấy | Thấy | Thấy clip, đầu tiếng chậm 80 ms, đuôi cụt có tiếng tách, bước nhảy ở mối nối. Thấy cả lỗi thật ở mối nối file Kenney `spaceEngineLow` |

**Những gì bản thử chưa chứng minh:**

- Chưa có âm thật do Stable Audio 3 tạo. Lỗi thật của mô hình (đầu tiếng nhòe, tiếng kim loại xoáy pha, rít cao tần) tinh vi hơn nhiều so với clip +18 dB.
- Chỉ có 16 âm gốc. Mọi tỉ lệ ở trên là chỉ dẫn, không phải độ chính xác.
- Chưa đo được máy loại nhầm bao nhiêu bản chủ dự án thích.

Nghiên cứu bên ngoài cho kết quả tương tự:

- Điểm CLAPScore chỉ tương quan với người ở mức SRCC khoảng 0,28 [[17]][s17].
- Gemini-2.5-pro, khi được hỏi bằng prompt, đạt PCC 0,46 với người trên SFX. Một bộ chấm huấn luyện riêng đạt 0,815 [[28]][s28].
- Bộ chấm bằng mô hình ngôn ngữ thiên vị theo thứ tự trình bày và theo độ dài câu trả lời [[29]][s29].

### 4.3 Ngưỡng

#### 4.3.1 Cổng vệ sinh (L1): chặn từ lô 1

| Kiểm | Đo trên | Ngưỡng | Nếu trượt |
|---|---|---|---|
| Clip trong file gốc | File gốc | Không có 3 mẫu liền nhau từ 0,999 FS trở lên. Không có 4 mẫu liền nhau cùng độ lớn ("đỉnh phẳng") ở bất kỳ mức nào trên −20 dBFS. Lý do: Stable Audio 3 ghi PCM 16-bit [[2]][s2], nên phần vượt đỉnh đã bị cắt khi ghi file. Sau khi chuẩn hóa, đỉnh phẳng này nằm thấp hơn 0,999 và lọt qua luật cũ | Loại. Không sửa được |
| Thời gian lên 10–90 % | Gốc và sau sửa | Phím, UI: ≤ 3 ms. Trúng, bắn, nổ: ≤ 10 ms. Sinh vật: ≤ 30 ms. Nền, tiếng vút: không kiểm | Chọn cửa sổ khác trong đoạn tạo dài (mục 5.1), hoặc loại |
| Im lặng ở đầu | Sau sửa | Phím, UI: ≤ 2 ms. Sinh vật: ≤ 15 ms. Còn lại: ≤ 5 ms | Sửa bằng cắt đầu |
| Lệch DC | Sau sửa | Dưới 0,1 % FS | Sửa bằng lọc cao |
| Đỉnh thật | Sau sửa | ≤ −1 dBTP | Sửa bằng bộ giới hạn |
| Độ dài | Sau sửa | Lệch spec không quá 20 % | Cắt, hoặc tạo dài hơn |
| Đuôi | Sau sửa | Tắt xuống −60 dB trước cuối file, hoặc có đoạn làm mờ từ 5 ms | Sửa bằng làm mờ |
| Mối nối vòng lặp | Sau sửa | Bước nhảy mẫu < −40 dBFS. RMS lệch < 1 dB. Trọng tâm phổ lệch < 10 % (so 50 ms cuối với 50 ms đầu) | Sửa bằng crossfade, hoặc inpaint chỗ nối |
| Định dạng | Sau sửa | 48 kHz. Mono, trừ nhạc, nền và stinger kết trận | Sửa |
| Stereo | Âm stereo | Hệ số tương quan lớn hơn 0 | Lấy kênh giữa |
| Nhạc | Sau sửa | Đúng số ô nhịp, lệch không quá 1 ms. Nhịp lệch không quá 1 BPM. Tổng các stem ≤ −1 dBTP. Các stem phát cùng nhau phải cùng giọng và điệu (bài J, mục 6.1) | Sửa MIDI hoặc tạo lại |

Độ dài chuẩn của vòng nhạc:

- Tuyến Cuối: 8 ô nhịp ở 96 BPM, dài đúng 20,000 s.
- Rồng Giữ Ải: 8 ô nhịp ở 84 BPM, dài 22,857 s.
- Lời Gọi: 16 ô nhịp ở 84 BPM, dài 45,714 s.

#### 4.3.2 Dò lỗi do mô hình tạo (L1b): chỉ gắn cờ ở lô 1

Đo trên file gốc, **trước** khi gộp về mono. Mọi ngưỡng là điểm xuất phát (chưa kiểm chứng). Chúng được chỉnh bằng nhãn "rè/lỗi" của chủ dự án ở lô 0.

| Lỗi | Đo gì | Gắn cờ khi |
|---|---|---|
| Tiếng vọng trước đầu tiếng | Năng lượng trong 30 ms trước điểm bắt đầu | Trên −40 dB so với đỉnh |
| Rít, xì cao tần | Độ phẳng phổ (spectral flatness) ở 8–16 kHz theo thời gian, ở phần thân và đuôi | Cao và tăng dần, trong khi âm tham chiếu cùng họ không có |
| Xoáy pha, "kim loại giả" | Độ biến thiên phổ (spectral flux) ở 4–16 kHz trong phần ngân | Trên mức P90 của âm tham chiếu cùng họ |
| Rung cao độ ở đuôi có cao độ | Độ rung f0 ở đuôi chuông, nốt | Rung quá 20 cent |
| Hai kênh lệch nhau | Tương quan giữa hai kênh; độ mất khi gộp mono (năng lượng kênh giữa so với L+R) | Tương quan dưới 0,3, hoặc mất quá 3 dB khi gộp |
| Nền nhiễu | Mức nhiễu ở đuôi | Trên −60 dBFS |

#### 4.3.3 Đặc trưng xếp hạng theo nhóm (L2): không chặn

Bảng này là **điểm xuất phát** để xếp hạng và gắn cờ. Không dùng để loại ở lô 1. Khi một họ âm có từ 5 âm đã duyệt, mỗi ngưỡng được thay bằng khoảng P10–P90 của bộ âm đó.

**Độ to:** mọi âm ngắn được chuẩn hóa về **một mức chung**: LUFS-M max −20, đo sau khi đệm im lặng cho đủ 0,4 s. Mức tương đối giữa các âm chỉ nằm trong `gainDb` của catalog và mức bus. Cột "Mức trong bản trộn" dưới đây là thứ bài thử A và B kiểm trên bản trộn, không phải đích của từng file.

| Nhóm | Ví dụ id | Dài | Mức trong bản trộn (LUFS-M max) | Phổ, độ nảy | Số biến thể |
|---|---|---|---|---|---|
| Phím đúng | `key.ok`, `type.key`, `key-right` | 15–60 ms | −28 đến −24 | **Đề xuất mới** (mục 6.2): tiếng tách chủ yếu trên 4 kHz, thân dưới 800 Hz, dải 1–4 kHz thấp hơn dải 4–8 kHz ít nhất 6 dB. Tài liệu game thắng cho đến khi sửa | 6–10 (Tuyến Cuối: 4–6, theo danh sách của game) |
| Phím sai | `key.bad`, `type.miss`, `key-wrong` | 60–150 ms | Nhỏ hơn phím đúng ít nhất 3 dB | Năng lượng ở 150–600 Hz. Phần trên 3 kHz thấp hơn ít nhất 20 dB [[59]][s59] | 2–3 |
| UI | `ui.*`, `ui-*` | 10–250 ms | −30 đến −22, không to hơn phím | 1–5 kHz, mềm | 1–3 |
| Thưởng xong từ | `word.load`, `type.word`, `word-hit`, `fire.cast` | 150–900 ms, tùy bậc | Từ −22 (bậc C) đến −16 (bậc S) | Nốt đúng thang, lệch không quá 10 cent. **Năng lượng 1–4 kHz giảm ít nhất 15 dB trong 100 ms sau đầu tiếng** (mục 6.2) | 1–3 |
| Bắn, khạc | `gun.xung`, `arrow-fire` | 80–350 ms | −24 đến −18 | Súng: từ 25 % năng lượng dưới 150 Hz, crest từ 12 dB. Khạc hoặc phóng: dưới 120 Hz thấp hơn ít nhất 12 dB | 4–6 |
| Trúng nhỏ | `hit.t1`, `enemy.*.hit` | 50–150 ms | −22 đến −20 | Đầu tiếng 2–6 kHz, thân 200–800 Hz, crest từ 12 dB | 6–8 |
| Trúng vừa, nặng | `fire.impact.*`, lớp `hit.*` | 120–600 ms | Vừa: −19 đến −17. Nặng: −16 đến −14 | Tiếng nặng có sub 40–90 Hz, dài không quá 150 ms | 3–6 |
| Nổ | `blast`, `trap.pine-bomb.trigger` | 0,6–2 s | LUFS-S max −15 đến −12 | Tiếng nứt 2–8 kHz trong 30 ms đầu. Sub dài không quá 300 ms | 3–5 |
| Chết bầy | `kill.swarm`, `enemy.swarm.death`, `ink-puff` | 80–200 ms | −24 đến −21 | Dải giữa và cao, nhẹ | 8–10 |
| Chết lớn | `kill.elite`, `enemy.quadruped.death` | 400–900 ms | −20 đến −15 | Tiếng thịch 60–150 Hz | 3–4 |
| Tiếng sinh vật | `*.spawn`, `dragon.hurt`, `dragon.roar` | 0,2–1,6 s | −20 đến −15 | AST nên gắn Roar, Growling hoặc Animal, không gắn Speech (cờ) | 3–4. Rồng chính: 1–2 |
| Báo nguy | `warn.*`, `alarm.surge`, `leak` | 0,25–2 s | −17 đến −14 | Không có âm kéo dài ở 1–4 kHz | 1, cố định |
| Nền lặp | `amb.*`, `*.march` | Theo tài liệu game | LUFS-I theo tài liệu game (nền −26) | Phần lớn năng lượng dưới 300 Hz và ở 4–10 kHz | 1 |
| Nhạc | `music.*`, `forest`, `wave` | Đúng số ô nhịp | LUFS-I theo game (−18; Tuyến Cuối −16) | Lời Gọi: từ 80 % năng lượng chroma rơi vào 5 nốt ngũ cung | — |
| Stinger | `end.*`, `stinger.*`, `wave.horn` | 1–3,6 s | LUFS-S max −16 đến −12 | Cùng giọng với nhạc | 1 |

**Nguồn gốc các con số:**

- Độ to và độ dài là điểm xuất phát, suy ra từ tài liệu thiết kế và các chuẩn đo: IESD [[51]][s51], độ trễ Kaaresoja [[52]][s52], SII [[53]][s53]. Đây không phải chuẩn công nghiệp.
- Tài liệu game đã ghi thì giữ đúng. Ví dụ: onset dưới 5 ms ở Tuyến Cuối, đỉnh −1 dBFS, nền −26 LUFS.

### 4.4 Luật cho các lớp học máy

- **Họ âm "bẩn có chủ ý":** súng, nổ, hồ quang điện, lửa lách tách, động cơ, tiếng vỡ giòn của bầy. Với các họ này, audiobox có trọng số 0 và bỏ cặp prompt "sạch đối với có lỗi" của PAM, cho đến khi họ có từ 10 âm đã duyệt. Chỉ xếp hạng bằng L2 và lựa chọn của chủ dự án.
- **Âm ngắn dưới 300 ms:** L3, L4 và L5 chấm trên một **bản lặp 3–4 s**: khoảng 10 lần phát theo nhịp thật của game, xoay vòng các biến thể. Không chấm một file 100 ms đứng riêng. Bản lặp này cũng thử luôn cách âm được dùng.
- **audiobox (L3):** chỉ so trong cùng một nhóm âm, đổi sang z-score trong nhóm. Không bao giờ so khác họ.
- **CLAP (L4):** mỗi game có bộ từ vựng 15–25 nhãn. Gắn cờ khi nhãn mong đợi không nằm trong top-3. Thêm cặp prompt đối lập để gắn cờ chất liệu, ví dụ:
  - *"a hollow bamboo knock"* đối với *"a metallic sci-fi clang"*
  - *"a heavy industrial autocannon shot"* đối với *"a thin toy laser pew"*
  - *"a dragon's roaring fire breath"* đối với *"a gas stove hiss"*

  **Không bao giờ dùng điểm giống prompt làm điểm chất lượng.**
- **AST (L4):** gắn cờ khi nhãn Speech đứng đầu ở một tiếng SFX. **Không** gắn cờ nhãn Music với SFX có cao độ kiểu sci-fi (laser, zap). Độ tự tin cao nhất dưới 0,1 thì gắn cờ "khó nhận ra". Chỉ kiểm nhãn mong đợi với loại âm có trong thế giới thật (gỗ, chuông, súng, nổ, đàn tranh thuộc nhãn "Zither", sáo).
- **Khoảng cách tham chiếu (L5):** khi họ âm có từ 5 âm đã duyệt, độ giống với âm đã duyệt gần nhất phải từ mức P10 của độ giống trong họ trở lên. Khi có từ 20 âm đã duyệt, tính KAD cho cả bộ.
- **Mô hình nghe (L7):** prompt trung tính, ví dụ "Bạn nghe thấy những nguồn âm nào?". Chỉ tính khi khớp với AST. Khi so A với B, đảo thứ tự rồi hỏi lại, chỉ giữ kết luận nhất quán [[29]][s29].

### 4.5 Điểm tổng và khi nào hỏi chủ dự án

Trọng số theo giai đoạn. "Họ bẩn" theo nghĩa ở mục 4.4.

| Giai đoạn | L2 đặc trưng | L3 audiobox | L4 ngữ nghĩa | L5 tham chiếu |
|---|---|---|---|---|
| Lô 1, họ thường | 0,6 | 0,3 | 0,1 | 0 |
| Lô 1, họ bẩn | 0,9 | 0 | 0,1 | 0 |
| Họ có từ 5 âm đã duyệt | 0,45 | 0,25 (họ bẩn: 0 cho đến 10 âm) | 0,1 | 0,2 |
| Họ có từ 30 lượt chấm | Ước lại bằng hồi quy (mục 4.6) | | | |

- **Gắn cờ bất đồng** khi thứ hạng theo L2 và theo L3 lệch nhau quá 3 bậc, hoặc khi L4 hay L1b gắn cờ. Ca bị cờ luôn được Claude đọc thẻ ảnh.
- Claude ghi 1–2 dòng nhận xét cho mỗi bản trong top-6, bằng ngôn ngữ thiết kế âm. Ví dụ: "thiếu lớp tách 2–6 kHz", "thừa ù ở 300 Hz", "đuôi dài 200 ms".

### 4.6 Hiệu chỉnh theo điểm của chủ dự án

1. **Lô 0, hai phần, mỗi phần 15 phút:**
   - **0a.** Chấm bộ hiệu chỉnh của bản thử (24 cặp âm hỏng và âm tốt) cùng 8 âm Kenney. Phần này chỉ kiểm luật đo có khớp tai với lỗi rõ ràng không. Nó dễ, nên không được coi là bằng chứng máy đã "hiểu" gu.
   - **0b.** Chấm âm **thật** do Stable Audio 3 tạo cho 6 id (lấy từ bản thử ở giai đoạn 2): một tiếng trúng ngắn, một tiếng gõ tre hoặc gỗ, một tiếng súng bẩn, một nền, một tiếng sinh vật, một tiếng lửa. Gắn nhãn "rè/lỗi" ở phần này dùng để chỉnh bộ dò L1b.
2. **Danh sách nghe của mỗi id** gồm:
   - bản đứng đầu theo điểm tổng;
   - bản **khác nhất** trong số bản qua cổng vệ sinh (xa bản đứng đầu nhất);
   - ở khoảng 30 % số id, thêm một **bản dò**: chọn ngẫu nhiên trong số bản máy xếp nửa dưới hoặc bị cờ loại. Không lấy bản hỏng vệ sinh rõ ràng.

   Chủ dự án không biết bản nào là bản dò.
3. **Mỗi lượt chấm** ghi một dòng vào `art-src/audio/review/ratings.jsonl` (mục 7).
4. **Gộp họ âm qua các game** để đủ dữ liệu. Dùng 8 họ chung, game là một biến phụ:
   1. phím và UI ngắn;
   2. thưởng có cao độ;
   3. bắn, phóng;
   4. trúng, va chạm;
   5. nổ, bẫy;
   6. chết quái;
   7. sinh vật;
   8. nền, báo nguy, stinger.
5. **Mô hình nhận hay loại cho từng họ:** hồi quy logistic trên 3–6 đặc trưng đã chuẩn hóa, game là biến phụ, kiểm tra bằng leave-one-out. Khi còn ít dữ liệu, dùng ngưỡng phần trăm. Mỗi phiên chèn thêm 2–3 cặp so **bản thắng của hai id khác nhau trong cùng họ**, để mô hình học được chủ dự án thích đặc trưng nào. Có thể dùng `choix` [[63]][s63] để tính thứ hạng từ các cặp đó.
6. **Cặp mốc:** mỗi phiên chèn lại 4–6 cặp đã chấm trước, hoặc tính trên 20 cặp mốc gần nhất. Nếu độ nhất quán dưới 70 %, phiên đó được tính nhẹ đi một nửa.
7. **Mục tiêu, đo chỉ trên bản dò:** máy tự loại được ít nhất 70 % số bản chủ dự án loại, và loại nhầm không quá 10 % số bản chủ dự án chọn. Khi một họ có dưới 30 bản dò đã chấm thì **không tuyên bố gì**, và danh sách nghe vẫn giữ 3 bản. Khi đạt mục tiêu, họ đó chuyển sang nghe 2 bản.
8. Ước lại sau mỗi 20–30 lượt chấm mới. Ghi độ trôi vào changelog của game.
9. Âm đã duyệt trở thành âm tham chiếu của lớp L5.

**"Âm được người chơi đánh giá cao":** chưa có bộ dữ liệu công khai nào về điểm người chơi chấm cho SFX game. Vì vậy dùng ba thứ thay thế:

- Bộ âm tham chiếu CC0: Kenney, cộng âm Freesound CC0 có điểm trung bình từ 4 và ít nhất 10 lượt chấm [[41]][s41].
- Bộ âm chủ dự án đã duyệt. Bộ này thành tham chiếu chính từ lô 2.
- 3–5 người chơi thử nghe A/B danh sách rút gọn ngay trong game, ở giai đoạn 5.

Các nguyên tắc từ những game được khen được viết thành luật kiểm (mục 8.5).

---

## 5. Vòng tạo, chấm và tạo lại

### 5.1 Các bước cho một id

1. **Spec.** Sinh thẻ YAML từ `catalog.ts` hoặc bảng trong tài liệu game. Claude viết 4 cách diễn đạt prompt, có gốc prompt của hướng phong cách đã chọn (mục 5.2). Mỗi id chọn 2–3 âm tham chiếu.
2. **Tạo.**
   - **Stable Audio 3:** chạy trong **một tiến trình Python** với `--no-free-models` để mô hình nằm sẵn trong bộ nhớ [[2]][s2]. 4 prompt × 6 seed = 24 ứng viên. CLI không có lệnh chạy nhiều seed một lúc, nên lớp gọi của Claude tự lặp seed.
   - **Id dài dưới 300 ms:** tạo đoạn 1–2 s. Bộ chấm chọn cửa sổ có đầu tiếng tốt nhất. Mỗi ứng viên là một cặp "đoạn + cửa sổ".
   - **CFG và negative prompt:** README ghi `--negative-prompt` chỉ có tác dụng khi `--cfg` khác 1,0, mà mặc định là 1,0 (tắt) [[2]][s2]. Vì vậy mặc định **không** dùng negative prompt. Chỉ bật CFG > 1 sau khi A/B cho thấy có lợi. Giá trị `cfg` ghi vào `SOURCES.json`.
   - **Ghép lớp:** 12–24 tổ hợp từ công thức.
   - **MIDI hoặc mẫu nhạc cụ:** phát trực tiếp 1–3 bản.
   - Thời gian thật trên M4 chưa đo. Bản thử ở giai đoạn 2 sẽ đo.
3. **Đo file gốc.** Clip và đỉnh phẳng, tương quan hai kênh, độ mất khi gộp mono, bộ dò L1b. Ghi vào phần `raw` của `review/qa/<id>.json`.
4. **Sửa tự động.**
   - Cắt im lặng ở đầu cho đến khi đạt spec. Làm mờ đầu 1–2 ms nếu có tiếng tách.
   - Làm mờ phần đuôi. Lọc cao 30–40 Hz để bỏ DC và tiếng ù trầm.
   - Đổi tần số lấy mẫu sang 48 kHz bằng `aresample=resampler=soxr`.
   - Gộp về mono: nếu mất khi gộp không quá 3 dB thì lấy kênh giữa; nếu hơn thì lấy kênh tốt hơn.
   - Giới hạn đỉnh thật ở −1 dBTP. Chuẩn hóa âm ngắn về LUFS-M max −20. Nhạc và nền theo LUFS-I của tài liệu game.
5. **Cổng L1** trên file gốc và file đã sửa. Bản trượt bị loại, lý do được ghi lại.
6. **Xếp hạng L2–L5** theo trọng số ở mục 4.5. Ghi cờ L1b, L4.
7. **Claude đọc thẻ ảnh và JSON** của top-6, bản dò và mọi ca bị cờ. Claude lập danh sách nghe theo mục 4.6 bước 2.
8. **Chủ dự án nghe trên Bảng Nghe** và chọn âm gốc (hero). Nếu không bản nào được, chủ dự án bấm "Không bản nào đạt" kèm nhãn.
9. **Tạo họ biến thể.**
   - **Tiếng ngắn có đầu tiếng sắc** (trúng, bắn, phím mẫu, chết bầy): giữ nguyên lớp đầu tiếng. Tạo biến thể bằng cách đổi lớp thân, dịch ±cent, chỉnh EQ nhẹ. Chỉ dùng `--init-audio` hoặc `--inpaint-range` cho phần thân và đuôi, sau điểm đầu tiếng. Lý do: tạo lại từ âm gốc thường làm nhòe đầu tiếng.
   - **Tiếng dài** (lửa, nền, sinh vật): `--init-audio hero.wav --init-noise-level` 0,4–0,7, ra 12 bản. File hero phải là WAV 44,1 kHz 16-bit, đúng yêu cầu của [[2]][s2].
   - Giữ 4–6 bản có độ khác nằm trong khoảng đã định (mục 5.2).
10. **Lượt nghe biến thể** của chủ dự án, khoảng 30 s mỗi id. Bảng Nghe phát cả bộ biến thể ở chế độ "Lặp 20 lần" và "Trong trận", xoay vòng như trong game. Chủ dự án bỏ từng bản không hợp.
11. **Sửa chọn lọc.** Đuôi hỏng thì dùng `--inpaint-range`, không tạo lại cả âm.
12. **Kiểm trong bối cảnh trận** (mục 6). Đạt thì ghi `manifest.json`, `SOURCES.json` và nhật ký.

Thời gian máy cho mỗi id ước khoảng 1–2 phút, chưa tính thời gian Claude viết prompt và đọc ảnh. Con số thật lấy từ bản thử ở giai đoạn 2.

### 5.2 Giữ một họ âm nhất quán

- **Bảng phong cách trước lô 1, cho từng game.** Claude dựng 2–3 hướng âm. Mỗi hướng gồm 3–4 âm chữ ký, đặt trong một đoạn trận 20 s có nền nhạc thô đúng giọng và BPM. Chủ dự án chọn một hướng. Với Lời Gọi, chủ dự án duyệt luôn phần văn hóa. Âm của hướng thắng là âm tham chiếu đầu tiên.
- **Gốc prompt cho mỗi game**, chốt sau bảng phong cách. Mỗi id thêm phần đuôi riêng. Điểm xuất phát:
  - Tuyến Cuối: *industrial, steel, close, punchy*. Đuôi kim loại trong không gian rộng là **một lớp riêng** dùng chung (`hit.tail`, mục 6.3), không nằm trong gốc prompt. Nhờ vậy gốc prompt không còn mâu thuẫn với bảng âm ở mục 8.3.
  - Lời Gọi: *bamboo, wood, bronze, paper, Vietnamese village, dry, outdoor*.
  - Rồng Giữ Ải: *painterly fantasy forest, warm, organic, outdoor*.
- **Các bậc dùng chung lớp.** Tuyến Cuối ghép bậc trúng lúc chạy từ các lớp riêng (mục 6.3). Rồng Giữ Ải: `fire.impact.c` gồm `fire.impact.a` cộng thêm tiếng bùng lửa.
- **Mỗi game có một lớp "chữ ký"** (sweetener):
  - Tuyến Cuối: tia điện và thép ngân.
  - Lời Gọi: tre, chuông đồng và đàn tranh.
  - Rồng Giữ Ải: than hồng lách tách và đàn hạc.
- **Đo độ khác giữa các biến thể bằng âm học**, không bằng CLAP:
  - khoảng cách mel trong cửa sổ đầu tiếng 0–50 ms;
  - độ trải của trọng tâm phổ và của cao độ đỉnh;
  - tương quan đường bao đầu tiếng.

  Khoảng chấp nhận lấy từ P10–P90 của 26 họ × 5 bản đánh số trong gói Kenney Impact. CLAP chỉ dùng để kiểm cả họ không trôi sang loại âm khác.
- **Đo độ gắn kết** (khi có từ 5 âm đã duyệt): âm mới phải gần tâm bộ âm đã duyệt của game mình hơn tâm của game khác.
- **Phân biệt sự kiện:** mỗi sự kiện có chữ ký phổ và chữ ký thời gian riêng. Đây là nguyên tắc "chơi bằng tai" của Overwatch và nguyên tắc rõ ràng của Riot [[56]][s56]. Vai trò tần số của từng lớp ở mục 6.4.
- **Tái tạo được:** ghi seed, prompt, `cfg`, phiên bản mô hình và mã băm công thức.
- **Về sau:** huấn luyện LoRA cho Stable Audio 3 trên bản ghi của chính chủ dự án. Không huấn luyện trên âm do Stable Audio 3 tạo ra, không dùng Sonniss, không dùng âm Freesound có người tải lên từ chối AI.

### 5.3 Biến thể và độ ngẫu nhiên khi chơi

| Nhóm | Cao độ | Độ to | Luật khác |
|---|---|---|---|
| Phím đúng | ±50 cent | ±1 dB | Tránh lặp 2 bản gần nhất. Monkeytype dùng 3–10 mẫu cho mỗi phím [[58]][s58] |
| Phím sai | ±30 cent | — | Nghỉ 150 ms giữa hai lần, để gõ loạn không ra tiếng dồn |
| Thưởng theo từng từ (`word.load`, `fire.cast`, `word-hit`) | ±20–30 cent, hoặc leo một bậc thang âm | ±1 dB | Phát sau mỗi từ nên cần chút khác biệt. Lời Gọi đã leo bậc theo Chuỗi |
| Thưởng hiếm, UI, báo nguy, stinger | **Không đổi ngẫu nhiên** | — | Âm thưởng hiếm được nhận ra nhờ luôn giống nhau. Chuỗi thưởng leo nốt theo thang, tối đa 8–12 bậc |
| Bắn | ±100 cent | ±2 dB | Tối đa 4 tiếng cho mỗi loại vũ khí. Hai lần phát cách nhau ít nhất 30 ms |
| Trúng nhỏ | ±150 cent | ±2 dB | Gom trong 38–45 ms (kit đang dùng 38 ms) |
| Trúng nặng | ±80 cent | ±1 dB | Hạ tiếng trúng nhỏ 3–6 dB trong 150 ms |
| Nổ | ±150 cent | — | Tối đa 4 lần mỗi 120 ms. Mỗi lần sau nhỏ hơn 3 dB ("volume scale" của UE [[57]][s57]) |
| Chết bầy | ±300 cent | ±3 dB | Tối đa 4 tiếng. Khi hơn 6 con chết trong 100 ms, thêm một lớp "chết hàng loạt" |

Mã hiện tại đổi ngẫu nhiên như nhau cho mọi âm. Rồng Giữ Ải dùng ±4 % cao độ, ±1,5 dB, lệch 0–12 ms. `SceneAudio` dùng ±5 % tốc độ phát. Cần cho phép mỗi nhóm có giá trị riêng (mục 6.3).

### 5.4 Từ nhãn chê đến cách sửa

| Nhãn | Claude làm gì trước | Nếu vẫn chưa được |
|---|---|---|
| chói | Hạ 3 dB ở 2,5–5 kHz, giảm độ chói | Thêm vào prompt "darker, less harsh" |
| đục | Lọc cao 80–120 Hz, cắt 200–400 Hz | Thêm vào prompt "tight, crisp" |
| yếu, mỏng | Thêm lớp sub hoặc lớp đầu tiếng, tăng crest | Đổi nguồn sang ghép lớp |
| quá dài | Cắt đuôi, làm mờ | Đặt độ dài nhỏ hơn khi tạo |
| rè, lỗi | Loại. Thêm mẫu vào bộ chỉnh L1b | Tạo lại |
| sai chất liệu | Viết lại prompt bằng từ chỉ chất liệu. Negative prompt chỉ khi đã bật CFG > 1 | Chuyển sang mẫu thật hoặc tự ghi |
| lạc thể loại | Thêm từ trong bảng âm của game (mục 8) | Đổi âm tham chiếu |
| nhàm khi lặp | Thêm biến thể, hạ 2 dB, giảm độ chói | Cho mỗi biến thể khác lớp hơn |
| rẻ tiền | Thêm một lớp, thêm đuôi phòng ngắn | Đổi nguồn |
| khó nghe tiếng đọc | Giảm năng lượng ở 1–4 kHz, rút ngắn phần 1–4 kHz của âm thưởng | Sửa mức nhường tiếng hoặc thời điểm đọc (mục 6.2) |
| chậm | Cắt đầu đến dưới 2 ms | Đổi cách tải âm |

### 5.5 Khi nào dừng

- Mỗi id chỉ chạy tối đa 3 vòng sửa prompt.
- Sau 3 vòng mà còn dưới 3 bản qua cổng, hoặc chủ dự án chê cả 2 lần liền, thì đổi nguồn. Thứ tự đổi: thư viện, rồi mã, rồi tự ghi. Nếu vẫn không được, đưa id vào danh sách "ghi hoặc mua sau".
- Không để vòng tự động chạy mãi chỉ để "qua luật". Tối ưu theo điểm máy sẽ kéo âm về hướng sạch mà nhạt (định luật Goodhart).

---

## 6. Kiểm tra trong game

### 6.1 Các bài thử

Mọi bài thử dựng tiếng bằng **bộ trộn thật của game** trong `OfflineAudioContext`, không cần chạy game. Rồng Giữ Ải đã có `src/audio/dev/harness.ts` và `audio-check.mjs`. Tuyến Cuối có `scripts/visual/evals/sfx-levels.js`. Cả hai cần thêm chế độ đọc file và xuất WAV, để kết quả đi qua cùng bộ phê bình. Chuỗi sự kiện lấy từ các bot gõ giống người của module cân bằng trong kit (25, 40 và 80 WPM).

**Nền nhạc thô trước lô 1:** bài C và D cần nhạc gần với nhạc thật. Trước giai đoạn 4, Claude dựng một nền nhạc thô cho mỗi game bằng MIDI và mẫu CC0, đúng giọng và BPM. Sau giai đoạn 6 (nhạc thật), chạy lại bài C và D.

| Bài thử | Cách làm | Đo gì | Đạt khi |
|---|---|---|---|
| **A. Độ to theo bus** | Dựng 5–10 phút chơi bằng bot | LUFS-I của cả bản trộn, đỉnh thật, LRA, phần đóng góp của từng bus, và mức của từng nhóm âm | −18 ± 2 LUFS-I, đỉnh ≤ −1 dBTP, LRA 8–15 LU, suy từ khoảng của thiết bị di động trong IESD [[51]][s51], vì web không có chuẩn riêng. Mỗi nhóm nằm trong cột "Mức trong bản trộn" (mục 4.3.3) ±2 LU |
| **B. Thay file không làm lệch mix** | So từng id: bản file với bản tổng hợp hiện tại | Chênh lệch độ to trong bản trộn | Lệch không quá 1 LU lúc mới thay. Sau đó chủ dự án mới chỉnh tiếp |
| **C. Giọng đọc từ trong trận** | **Mẫu giọng:** Claude ghi 2–3 giọng tiếng Anh của macOS bằng `say -v <giọng> -o <file>`. Giọng "Google US English" của Chrome là giọng qua mạng, chỉ có khi chủ dự án ghi lại (tùy chọn). **Chuỗi thật:** (1) khóa từ → giọng đọc, trong lúc bot gõ; (2) gõ xong từ → âm thưởng (`fire.cast`, `word-hit`, `word.load`) → giọng đọc; (3) trận dày nhất. Quét mức giọng ±6 dB, và độ trễ bắt đầu đọc 0, 150 và 400 ms | Trong 300 ms đầu của giọng: giọng cao hơn phần còn lại bao nhiêu ở 1–4 kHz. SII bằng MoSQITo `sii_ansi` [[19]][s19] | Ở ca xấu nhất: giọng cao hơn ít nhất 10 dB ở 1–4 kHz. SII từ khoảng 0,75 (chưa kiểm chứng). Chủ dự án nghe ca xấu nhất để xác nhận. Lý do: 1–4 kHz chiếm khoảng 71 % trọng số dễ hiểu, và người nghe không phải bản ngữ cần tỉ số tín hiệu trên nhiễu tốt hơn 1–7 dB [[53]][s53] |
| **D. Mật độ** | Rồng Giữ Ải: 200 quái tràn lên. Tuyến Cuối: 40 con chết trong 120 ms cộng `gun.xung` 5 lần mỗi giây. Lời Gọi: tên bắn 4 lần mỗi giây × số tháp, cộng `ink-puff` 8 lần mỗi giây | Số tiếng cùng lúc, thời gian bộ giới hạn ép hơn 3 dB, clip, độ chói ở 2–5 kHz, và **nhóm nào chiếm từng dải** | Số tiếng không vượt trần. Thời gian ép hơn 3 dB dưới 5 %. Không clip. Độ chói dưới mức P90 của âm tham chiếu. Mỗi dải do đúng nhóm đã định chiếm (mục 6.4) |
| **E. Mỏi tai** | Dựng **10 phút** ở WPM của bot, gồm mọi âm phát theo từ và tần suất cao: phím, `fire.cast`, `word.load`, `word-hit`, `coin` (3 lần/s), `arrow-fire` (4 lần/s), `ink-puff` (8 lần/s), `gun.xung` | Độ chói và độ gắt trung bình của tổng các bus, tỉ lệ biến thể bị lặp liền | Không biến thể nào phát 2 lần liền. Độ chói dưới P90 tham chiếu. Chủ dự án nghe 3 phút, bắt đầu quanh phút thứ 8, và không gắn nhãn "nhàm khi lặp" |
| **F. Loa nhỏ** | Lọc cao 200 Hz. Mỗi lô, chủ dự án mở bản trộn trên điện thoại và laptop một lần (chép qua mạng nội bộ, không xuất bản) | Lượng mất đi ở phím, UI và báo nguy | Mất không quá 6 dB. Chủ dự án không gắn nhãn "khó nghe" |
| **G. Độ trễ** | Đọc `baseLatency` và `outputLatency` trên Safari và Chrome | Độ trễ từ lúc bấm phím đến lúc ra tiếng | Không quá 50 ms. Khuyến nghị là 20–70 ms [[52]][s52]. Phím và UI phải giải mã sẵn khi mở game |
| **H. Hit-stop** | Phát đòn có hit-stop | Tiếng có bị khựng hay chậm lại không | Âm phát đúng khung trúng và vẫn phát trong lúc dừng hình. Không tạm dừng hay làm chậm `AudioContext` [[55]][s55] |
| **I. Bậc trúng** (Tuyến Cuối) | Dựng từng bậc T0–T5, mỗi bậc với 1, 5 và 20 viên trúng gom lại | Độ to và độ dài | Độ to và độ dài tăng đều theo bậc và theo số viên |
| **J. Giọng và điệu giữa các stem** | Các stem phát cùng lúc | Chroma, nốt lạ so với giọng chung | Không có nốt va nhau. Ví dụ: stem `general` của Rồng Giữ Ải ghi "D minor", đè lên các stem Rê Dorian; nốt Si giáng sẽ va với Si thường trên hợp âm G (mục 16) |

### 6.2 Luật thời điểm giữa âm thưởng, phím và giọng đọc

Vấn đề: ở Rồng Giữ Ải, từ mới được đọc khi khóa từ và khi gõ xong; từ yếu và chế độ "all" được đọc khi gõ xong (`games/dragon-hold/src/app/learning.ts`). Âm xong từ (`fire.cast`, `word-hit`, `word.load`) phát **cùng sự kiện đó**. Hạ tiếng trước không cứu được, vì hai thứ có chung một mốc. Đề xuất sau là **thay đổi hợp đồng**, phải sửa tài liệu từng game và có chủ dự án duyệt:

1. **Âm xong từ là âm được nhường**, không phải âm cảnh báo. Ở Tuyến Cuối, `word.load` và `word.perfect` đang đi bus `alerts` (chỉ hạ −2 dB). Chuyển sang bus được hạ sâu hơn.
2. **Hình dạng âm xong từ:** năng lượng 1–4 kHz giảm ít nhất 15 dB trong 100 ms sau đầu tiếng. Phần ngân dài hơn phải nằm dưới 1 kHz hoặc trên 4 kHz. Nếu một âm không làm được vậy (ví dụ arpeggio bậc S), giọng đọc chờ 150 ms sau đầu tiếng của âm đó.
3. **Phím trong lúc đọc:** hạ khoảng −8 dB. Hiện tại: Rồng Giữ Ải −2 dB, Tuyến Cuối −4,4 dB. Nếu bài C vẫn trượt, phím mới theo phổ đề xuất: tiếng tách trên 4 kHz, thân dưới 800 Hz, khoét dải 1–4 kHz.
4. **Hạ tiếng bắt đầu khi game gửi yêu cầu đọc** (`pronouncer.request`), không đợi giọng cất lên. Giữ đến sự kiện `end` của `SpeechSynthesisUtterance` [[89]][s89], có giới hạn thời gian (ví dụ 3 s) phòng khi `end` không đến. Nhả trong 300–500 ms. Lý do: giọng của Chrome đi qua mạng, thời điểm bắt đầu không biết trước.
5. **Nhạc:** cả ba tài liệu game đã ghi nhạc nhường giọng đọc: Rồng Giữ Ải −4 dB, Tuyến Cuối −4 dB, Lời Gọi −9 dB. Ghi chú trong `shared/game-kit/speech/speech.ts` lại nói nhạc không nên nhường. Tài liệu game thắng. Bản này **không** đổi mức nhạc. Chỉ khi bài C trượt mới đề xuất mức mới cho từng game.

### 6.3 Mã cần sửa trước khi ghép file

**Khi nào làm:** sau khi các làn cân bằng merge, hoặc trong một worktree riêng. Lý do: các làn đó đang sửa cả ba game.

1. **Kit `SceneAudio`** đang có 4 hạn chế: mỗi id chỉ có một file, mọi file được giải mã hết lúc `unlock()`, không có bản tổng hợp dự phòng, và nhạc nối thẳng ra loa nên không đi qua bus. Cách sửa: đưa `FileBank`, `LayeredBank` và schema manifest của Rồng Giữ Ải vào `shared/game-kit/audio`. Thêm biến thể, độ dài đo từ file, ngẫu nhiên theo nhóm, nhạc đi qua bus (mức nhường theo tài liệu từng game), và tải theo độ ưu tiên.
2. **Kit `AudioCues`** hiện hạ tiếng `shots` và `hits` khi giọng đã cất lên, không hạ `kills`. Sửa theo mục 6.2 bước 4, và thêm `kills`.
3. **Bậc trúng của Tuyến Cuối ghép lúc chạy.** `flush()` trong `theme-audio.ts` đang gộp 6 bậc T0–T5 vào 3 id, chỉnh độ to theo log2 số viên trúng, kéo dài tiếng thép theo bậc, thêm trầm từ T2 và đuôi từ T4. Nếu nướng sub và đuôi vào file `hit.t2`, `hit.t4` thì mất các tầng này và có thể bị chồng lớp. Cách sửa: mỗi bậc có file **đầu tiếng + thân** riêng. Thêm một file **sub dùng chung** (`hit.sub`) và một file **đuôi dùng chung** (`hit.tail`). Mã ghép lớp theo cờ `bass` và `tail` của `tiers.ts`, và giữ trong mã phần độ to theo số viên và độ dài theo bậc. Bài I kiểm kết quả. Hai id mới cần thêm vào `THEME_SOUND_LIST.md` của Tuyến Cuối.
4. **Bộ giới hạn của Rồng Giữ Ải** đang tính chỗ cho tiếng theo `lengthMs` của bản tổng hợp. Đổi sang độ dài thật của file.
5. **Harness của Rồng Giữ Ải** mới chỉ thử bank tổng hợp. Thêm chế độ file (`files: true`), xuất WAV, và nhận mẫu giọng của bài C.
6. **Lời Gọi** chưa có bộ tải file. Hai cách: thêm một lớp kiểu `FileBank` vào `TypingAudio`, hoặc chuyển sang dùng kit.
7. **`manifest.json` của Rồng Giữ Ải** đang không vào Git, cũng không vào Drive, vì JSON không phải media. Cách sửa: mở danh sách cho phép trong `.gitignore` (mục 11), và cho `media:check` kiểm tham chiếu âm.

### 6.4 Vai trò tần số theo game

Bảng này là điểm xuất phát. Bài D kiểm nhóm nào thực sự chiếm từng dải. Dải 1–4 kHz dành cho giọng đọc từ, nên âm phát dày không được ngân lâu ở đó.

| Dải | Tuyến Cuối | Lời Gọi | Rồng Giữ Ải |
|---|---|---|---|
| Dưới 120 Hz | Sub súng, sub dùng chung `hit.sub` | Trống, `blast` | Thân gầm rồng, Bom Hạt Thông |
| 120–800 Hz | Thân súng, thân tiếng trúng | Thân gỗ, thân tre | Thân lửa, thân quái |
| 1–4 kHz (giọng) | Chỉ đầu tiếng rất ngắn; báo nguy ngắn | Chỉ đầu tiếng rất ngắn | Chỉ đầu tiếng rất ngắn |
| 4–8 kHz | Tách phím, lách tách điện, đầu tiếng `hit.t1` | Tách tre, giấy, `ink-puff` | Lách tách than hồng, tiếng tách phím gỗ |
| Có cao độ | `kill.chime` theo ngũ cung La thứ | `word-hit` đàn tranh theo thang Hò–Xự–Xang–Xê–Cống | Chuông nhỏ và đàn hạc theo ngũ cung |

---

## 7. Bảng Nghe (Listening Board)

**Bảng Nghe là gì:** một trang web chạy trên máy ở địa chỉ `127.0.0.1`. Trang không công khai và không xuất bản ra ngoài, vì âm chưa phát hành không được rời máy.

**Cách mở** (lệnh đề xuất): `pnpm audio:board --game dragon-hold --batch 2026-10-24`. Lệnh chạy một server Node nhỏ chỉ nghe trên `127.0.0.1`. Server đọc ứng viên từ `~/AudioLab/work/...`. Kết quả ghi vào `art-src/audio/review/ratings.jsonl`.

**Bối cảnh nghe:**

| Bối cảnh | Có từ | Cách phát |
|---|---|---|
| **Một mình** | Bảng v1 (giai đoạn 1) | Phát riêng âm |
| **Lặp 20 lần** | Bảng v1 | Phát đúng nhịp như trong game, xoay vòng các biến thể |
| **Loa nhỏ** | Bảng v1 | Lọc cao 200 Hz |
| **Trong trận** | Bảng v2 (sau giai đoạn 3) | Âm chồng lên nền nhạc thô, nền và tiếng trận điển hình, theo mức bus thật và có nhường tiếng |

**Bối cảnh mặc định theo họ âm** (để tiết kiệm thời gian):

- Âm phát dày (phím, bắn, trúng, chết bầy, xu, thưởng theo từ): **Trong trận** và **Lặp 20 lần**.
- Stinger, báo nguy và nền: **Một mình** và **Trong trận**.
- Còn lại: **Một mình** và **Trong trận**.
- Trước giai đoạn 3, "Trong trận" được thay bằng "Lặp 20 lần".

**Bốn chế độ:**

1. **Chọn âm gốc:** 2–3 ứng viên với nhãn A, B, C xếp ngẫu nhiên, theo danh sách ở mục 4.6 bước 2.
2. **Lượt biến thể:** khoảng 30 s mỗi id. Phát cả bộ biến thể. Bấm để bỏ từng bản.
3. **Bảng phong cách:** 2–3 đoạn trận 20 s, mỗi đoạn một hướng âm.
4. **Cuối phiên:** một đoạn 20 s "mật độ" và một đoạn 3 phút "mỏi tai" của game đó.

**Mọi thẻ:**

- Thẻ không lộ nguồn âm, không lộ điểm máy, không lộ bản nào là bản dò.
- Các bản tự cân cùng độ to (LUFS-M) trước khi phát, vì bản to hơn thường nghe "hay hơn" [[29]][s29].
- Chấm 1–5 cho từng bản, chọn bản tốt nhất, chọn nhãn và ghi chú ngắn. Có nút **"Không bản nào đạt"**.
- Chấm xong thì thẻ ảnh và số đo mới hiện ra, để số đo không dẫn dắt người nghe.

**Cách dùng phím:** A, B, C để phát. 1–5 để chấm bản đang chọn. Enter để lưu. Space để phát lại.

**Mỗi phiên:**

- Tối đa 10 id và 20 phút, để tai không mỏi.
- Bảng tự chèn 4–6 cặp mốc (mục 4.6).
- Ghi thiết bị đang dùng ("tai nghe" hay "loa"). Bảng nhắc giữ âm lượng máy ở một mức cố định.

**Nhãn cố định:** hay, hợp game, chói, đục, rè/lỗi, yếu/mỏng, quá dài, quá to, quá nhỏ, chậm, sai chất liệu, lạc thể loại, nhàm khi lặp, rẻ tiền, khó nghe tiếng đọc.

**Một dòng dữ liệu:**

```json
{"ts":"2026-10-24T20:15:03+07:00","game":"typing-survival","id":"gun.xung","family":"ban","batch":"b1","session":"s3",
 "mode":"hero","context":"mix","device":"headphones","shown":["c7f2…","1a9e…","e04b…"],"order":["B","A","C"],
 "roles":{"c7f2…":"top","1a9e…":"distinct","e04b…":"probe"},
 "stars":{"c7f2…":4,"1a9e…":2,"e04b…":3},"pick":"c7f2…","tags":{"1a9e…":["đục","yếu/mỏng"]},
 "note":"B có lực nhưng đuôi dài","anchor":false}
```

Trường `roles` chỉ ghi vào file, không hiện trên bảng.

**Thời gian của chủ dự án:**

| Việc | Khi nào | Thời gian |
|---|---|---|
| Lô 0a, hiệu chỉnh trên bản thử | Một lần | 15 phút |
| Lô 0b, âm Stable Audio 3 thật (6 id) | Một lần | 15 phút |
| Bảng phong cách | Mỗi game, trước lô 1 | Khoảng 10 phút |
| Chọn âm gốc | Mỗi id | 2–3 phút |
| Lượt biến thể | Mỗi id có biến thể | Khoảng 30 s |
| Đoạn mật độ và mỏi tai | Mỗi game, mỗi lô | 4 phút |
| Nghe bản trộn trên điện thoại và laptop | Mỗi lô | 5 phút |
| Duyệt văn hóa một stem nhạc Lời Gọi | Mỗi stem | 2–3 phút |
| **Lô 1 (28 id, 3 game), gồm bảng phong cách** | Một lần | **Khoảng 1,5–2 giờ, chia 4–5 phiên** |
| **Cả tháng đầu** | — | **Khoảng 4–6 giờ** |

---

## 8. Bảng âm theo từng game

### 8.1 Rồng Giữ Ải (rừng thần thoại vẽ tay)

- **Lửa Rồng:** dùng lửa thật như đuốc, khí đốt, giẻ cháy vung trên sào. Đây là cách của How to Train Your Dragon 2 [[61]][s61]. Cộng thân gầm 60–250 Hz, đuôi lách tách, và tiếng xèo của than hồng khi trúng. Phun Lửa tách 3 phần: đầu, vòng lặp, cuối.
- **Hai Rồng có hai tính cách riêng.** Ghép tiếng thú khác nhau như mèo lớn, cá sấu rít, chim săn mồi, rùa rên trầm, rồi hạ giọng. Đây là cách làm của Game of Thrones [[61]][s61].
- **Quái:**
  - Hai chân: giáp vỏ cây và lá, kèm tiếng gầm gừ.
  - Bốn chân: tiếng vó và tiếng khịt.
  - Bay: tiếng cánh và tiếng rít 2–5 kHz.
  - Bầy: lạo xạo, nhỏ, được gộp lại.
- **Bẫy:**
  - Gai Chông: tiếng gỗ đâm lên. Không nổ.
  - Bom Hạt Thông: nổ trầm, hạt văng. Đây là bẫy duy nhất nổ.
  - Lưới Phóng: dây quấn, không có tiếng nổ.
- **Nhạc:** Rê Dorian, 84 BPM. Gồm sáo gỗ, đàn hạc, cello và trống khung. Trống khung là lớp tăng độ dồn. Mẫu lấy từ VSCO-2-CE (Cello Section, Harp, Flute [[85]][s85]) và VCSL Folk Harp, Frame Drum [[42]][s42]. Stem `general` đang ghi "D minor" (mục 16).
- **Phím:** tiếng gỗ mềm, kèm chuông nhỏ theo ngũ cung Fa trưởng (đúng như tài liệu của game).

### 8.2 Lời Gọi (làng tre Việt)

- **Chất liệu:** tre, gỗ, chuông đồng, cồng, giấy, trống cơm, sáo trúc, đàn tranh. Không dùng laser và không dùng synth điện tử.
- **Thang âm:** Hò, Xự, Xang, Xê, Cống, gần với C D F G A.
- **Luật của game (TK 22.1):** không chuông chùa, không mõ chùa, không tiếng tụng. Cồng là cồng hội làng. Phách tre dùng thay mõ.
- **Thêm từ nghiên cứu [[60]][s60]:**
  - Sáo trúc của Việt Nam không có màng rung. Đây là điểm khác sáo dizi của Trung Quốc, nên không để tiếng "rè màng".
  - Trống cơm có hai mặt, thường lên dây cách nhau khoảng một quãng năm.
  - Đàn tranh có luyến láy bằng tay trái.
  - Cồng gắn với nghi lễ cộng đồng (UNESCO). Chỉ dùng cồng cho lúc trang trọng hoặc báo nguy, không dùng để đùa.
  - Tránh âm hưởng kèn đám ma cho sự kiện thường và sự kiện thắng.
  - Tránh âm thanh Trung Quốc hay Nhật Bản dán nhãn Việt, như nhị dẫn giai điệu, shakuhachi, taiko.
  - Báo động dùng kẻng sắt hoặc trống hội, không dùng mõ.
- **Điệu (gợi ý, chờ chủ dự án duyệt):** thắng dùng điệu Bắc (sáng). Thua dùng điệu Nam hoặc Oán (buồn).
- **Đàn tranh cho `word-hit`:** tài liệu game cần các nốt C5 D5 F5 G5 A5 C6. Mẫu VCSL chỉ có B1–B4, các nốt C#, D#, F#, G#, B [[83]][s83]. Muốn C6 phải dời B4 lên 13 bán cung: tiếng ngân 0,8 s bị ngắn lại và nghe như đồ chơi. Mặc định đề xuất: **hạ `word-hit` một quãng tám, thành C4–C5**. Khi đó mỗi nốt chỉ cần dời 1–2 bán cung từ mẫu gần nhất. Bản vuốt lên lấy từ thư mục Gliss. Nếu chủ dự án giữ C5–C6: dời bằng rubberband có giữ formant rồi A/B với bản tổng hợp hiện tại, hoặc tự ghi.
- **Chuông và cồng:** **không** dùng VCSL "Hand Bells, Nepalese" làm mặc định, vì đó là chuông nghi lễ vùng Himalaya, trái luật "không chuông chùa". Ứng viên thay: VCSL Hand Chimes, Tubular Bells [[84]][s84], hoặc chuông đồng tự ghi. VCSL Gong 1 và 2 chưa rõ là tam-tam hay cồng có núm (chưa kiểm chứng). Với `leak` có thể dùng VCSL Anvil hoặc Brake Drum cho tiếng giống kẻng sắt. **Chủ dự án nghe và duyệt nguồn chuông, cồng trước lô 1c.**
- **Nhạc cụ khác:** VCSL Slit Drum, Woodblock, Frame Drum (tạm thay trống cơm) [[42]][s42]. Sáo trúc: chủ dự án tự ghi, hoặc dùng Faust `fluteModel` [[48]][s48].
- **Chủ dự án ký duyệt từng stem nhạc và từng âm có cồng.**

### 8.3 Tuyến Cuối (trạm thép bên mép hố đen)

- **Súng:** ghép bốn lớp.
  - Tiếng thịch: sub 40–90 Hz, dài không quá 120 ms.
  - Lớp cơ khí: khóa nòng, rơ-le, servo. Giữ ngắn để không ngân ở 1–4 kHz.
  - Lớp năng lượng.
  - Đuôi kim loại trong không gian rộng: dùng chung lớp `hit.tail`.

  Hai mẹo của DOOM: một xung ngắn cắt gọn thành im lặng rồi mới tới tiếng bắn, và làm méo nhẹ tiếng kim loại cho "chắc" [[54]][s54]. Đây là họ "bẩn có chủ ý" (mục 4.4).
- **Điện:** tiếng lách tách 2–8 kHz cộng tiếng ù 50/100 Hz. Khi đông quái, giới hạn tổng năng lượng ở 2–5 kHz bằng chỉ số độ chói.
- **Bầy quái:**
  - Gộp tiếng chết và đặt trần theo họ quái.
  - Ưu tiên theo vị trí trên màn hình và mức đe dọa với tuyến. Torchlight III dùng cách này (nguồn thứ cấp).
  - `kill.chime` là thanh thép leo ngũ cung, tách riêng để mã chỉnh được cao độ.
- **Bậc trúng:** ghép lúc chạy từ lớp đầu tiếng và thân của từng bậc, cộng `hit.sub` và `hit.tail` dùng chung (mục 6.3).
- **Nhạc:** 96 BPM, La thứ. Lớp chiến là những cú "bùng" ngắn, nghịch phách. Khi đánh, không dùng pad dài ở dải giữa, theo cách của Mick Gordon [[54]][s54]. Dựng bằng MIDI, bộ phát mẫu Python, mẫu bộ gõ kim loại VCSL Anvil, Brake Drum [[84]][s84], và synth tổng hợp bằng mã (Surge XT nếu chủ dự án cài).
- **Phím:** tiếng rơ-le thép khô.

### 8.4 Space Typing

- Giữ nền âm Kenney Sci-fi. Thay dần các lớp mỏng bằng cùng đường ống này.
- 116 file âm CC0 đang nằm trong Git. Mặc định giữ nguyên (mục 16). File mới thì theo luật không đưa media vào Git.
- **Phải thay các câu thoại DotA trước khi phát hành công khai hoặc thương mại**, vì Valve giữ bản quyền. Hiện chúng chỉ dùng riêng, nằm ở `art-src/Dota-Sounds` và `public/local-assets`.

### 8.5 Nguyên tắc từ những game được khen, viết thành luật kiểm

| Nguồn | Nguyên tắc | Thành luật nào |
|---|---|---|
| DOOM 2016 [[54]][s54] | Vũ khí là "nhân vật chính", tiếng kim loại hơi méo cho "chắc" | Ở đây ưu tiên số 0 là giọng đọc từ (mục 6.2). Súng có crest từ 12 dB. Súng thuộc họ bẩn, audiobox không được phạt |
| Mick Gordon [[54]][s54] | Nhạc khi đánh là những cú bùng ngắn, không dùng nốt dài | Stem chiến không có pad kéo dài ở 300 Hz–3 kHz |
| Dead Cells, Sakurai [[55]][s55] | Đòn chí mạng có tiếng riêng. Hit-stop dài hơn khi sát thương lớn hơn, nhưng có trần | Có lớp chí mạng riêng. Âm không dừng theo hit-stop |
| Overwatch, Riot [[56]][s56] | Chơi được bằng tai. Mức gây chú ý của âm phải bằng mức quan trọng | Mỗi sự kiện có chữ ký riêng (mục 6.4). Đòn lớn có âm báo trước |
| Vampire Survivors [[64]][s64] (nguồn thứ cấp) | Mỗi lần nhặt ngọc kêu một tiếng chuông, cả bầy chết thành một "dàn" | Tiếng chết bầy nhỏ từng tiếng nhưng nghe đã khi cộng lại. Thưởng tỉ lệ với thành tích |
| Monkeytype [[58]][s58] | Mỗi phím 3–10 mẫu. Tiếng lỗi là tùy chọn | Phím có 6–10 biến thể. Người chơi tắt được tiếng lỗi |
| Batmaz 2021 [[59]][s59] | Tiếng báo lỗi cao làm người dùng gõ kém đi | Tiếng phím sai trầm, mềm, không to hơn tiếng phím đúng |

Các tuyên bố về âm thanh của Hades, Kingdom Rush, Bloons TD 6, Brotato và Risk of Rain 2 chưa có nguồn gốc nào từ chính nhà làm game. Vì vậy không dùng chúng làm bằng chứng.

---

## 9. Lô đầu tiên: 28 âm

**Cách chọn:** ưu tiên âm phát nhiều, dễ nghe thấy, và bản tổng hợp hiện tại yếu. Ưu tiên tiếp những game đã ghép file được ngay.

**Trước lô 1:**

1. **Bản thử Stable Audio 3, 6 id** (giai đoạn 2): `hit.t1`, `call-chop`, `gun.xung`, `amb.forest`, `enemy.quadruped.howl`, `fire.impact.a`. Đo tốc độ và RAM trên M4. Kết quả dùng luôn cho lô 0b. **Đi tiếp khi:** 24 ứng viên dưới 2 s tạo xong trong khoảng 1 phút khi mô hình nằm sẵn; RAM đỉnh dưới 4 GB; ít nhất 4/6 id có từ 3 bản qua cổng vệ sinh; ít nhất 3/6 id có một bản được chủ dự án chấm từ 3/5. **Nếu không đạt:** hạng 1 SFX chuyển sang ghép lớp CC0 và tổng hợp; thử MOSS; cân nhắc một tháng ElevenLabs.
2. **Bảng phong cách** cho từng game, ngay trước lô của game đó. Âm chữ ký:
   - Rồng Giữ Ải: `fire.cast`, `fire.impact.a`, `enemy.quadruped.howl`, `amb.forest`.
   - Tuyến Cuối: `gun.xung`, `hit.t1`, `kill.swarm`, `word.load`.
   - Lời Gọi: `word-hit`, `arrow-fire`, `ink-puff`, `coin`.
3. **Nền nhạc thô** cho từng game (mục 6.1).

**Thứ tự làm:**

- **1a. Rồng Giữ Ải:** đã có `FileBank`. Ghép vào game sau khi harness có chế độ file.
- **1b. Tuyến Cuối:** sau khi nâng cấp kit và tách bậc trúng thành lớp.
- **1c. Lời Gọi:** sau khi có bộ tải file, và sau khi chủ dự án duyệt nguồn chuông, cồng và quãng tám của `word-hit`.

Riêng nốt đàn tranh của Lời Gọi không cần AI, nên tạo trước được.

| # | Game | Id | Vì sao làm trước | Nguồn | Biến thể |
|---|---|---|---|---|---|
| 1 | Rồng Giữ Ải | `fire.cast` | Phát sau mỗi từ | Stable Audio 3 (lửa). Lớp gầm thú thêm sau (Freesound CC0 do chủ dự án tải, hoặc tự gầm). Theo luật âm xong từ (mục 6.2) | 4 |
| 2 | Rồng Giữ Ải | `fire.impact.a` | Đòn trúng nghe nhiều nhất | Stable Audio 3 cộng lớp đầu Kenney Impact, làm âm gốc của họ | 4 |
| 3 | Rồng Giữ Ải | `fire.impact.b` | Cùng họ | Từ #2: đổi lớp thân, dịch ±cent, giữ đầu tiếng | 3 |
| 4 | Rồng Giữ Ải | `fire.impact.c` | Đòn bậc T3 trở lên | #2 cộng tiếng bùng lửa | 3 |
| 5 | Rồng Giữ Ải | `wave.horn` | Mốc mỗi đợt | Kèn co VSCO (F Horn) và trống khung VCSL qua bộ phát mẫu Python, hoặc Stable Audio 3 | 1 |
| 6 | Rồng Giữ Ải | `general.g01.horn` | Tướng xuất hiện | Như #5, trầm hơn. Kiểm điệu với stem `general` | 1 |
| 7 | Rồng Giữ Ải | `amb.forest` | Phát liên tục | Stable Audio 3, vòng lặp 6 s đúng tài liệu game | 1 |
| 8 | Rồng Giữ Ải | `amb.river` | Phát liên tục | Stable Audio 3, vòng lặp 5 s | 1 |
| 9 | Rồng Giữ Ải | `enemy.swarm.march` | Có bầy là phát | Stable Audio 3 | 1 |
| 10 | Rồng Giữ Ải | `enemy.quadruped.march` | Có thú là phát | Stable Audio 3 | 1 |
| 11 | Tuyến Cuối | `gun.xung` | Phát 5 lần mỗi giây | Ghép lớp: cơ khí Kenney (Impact Metal, Plate), thân Stable Audio 3, sub tổng hợp. Họ bẩn | 6 |
| 12 | Tuyến Cuối | `hit.t1` | Mỗi viên đạn trúng | Đầu tiếng Kenney Impact Metal cộng thân Stable Audio 3 | 6 |
| 13 | Tuyến Cuối | `hit.t2` (đầu tiếng + thân) và `hit.sub` (mới) | Chí mạng | Thân nặng hơn #12. `hit.sub` tổng hợp, dùng chung | 4 + 1 |
| 14 | Tuyến Cuối | `hit.t4` (đầu tiếng + thân) và `hit.tail` (mới) | Đòn lớn | Thân nặng nhất. `hit.tail` từ VCSL Anvil, Brake Drum cộng vang phòng rộng, dùng chung | 3 + 1–2 |
| 15 | Tuyến Cuối | `kill.swarm` | Hàng trăm lần mỗi trận | Stable Audio 3 (mảnh kim loại vụn). Nốt `kill.chime` tách riêng. Họ bẩn | 8 |
| 16 | Tuyến Cuối | `kill.elite` | Lính tinh nhuệ | Stable Audio 3 cộng tia điện tổng hợp | 3 |
| 17 | Tuyến Cuối | `word.load` | Phát sau mỗi từ | Stable Audio 3 cộng tiếng cơ khí Kenney. Theo luật âm xong từ. Đổi ±20–30 cent khi phát | 3 |
| 18 | Tuyến Cuối | `word.perfect` | Thưởng | #17 cộng tiếng nạp điện tổng hợp | 2 |
| 19 | Tuyến Cuối | `gun.tia.pulse` | Mỗi 0,1 s của Tia | Tổng hợp bằng numpy và pedalboard, cộng Stable Audio 3 | 4 |
| 20 | Tuyến Cuối | `hurt.breach` | Báo nguy chính | Stable Audio 3 cộng còi tổng hợp | 1 |
| 21 | Lời Gọi | `word-hit` | Phát sau mỗi từ | VCSL Dan Tranh (Normal và Gliss) qua bộ phát mẫu Python, dời tối đa 3 bán cung. Mặc định C4–C5 (chờ duyệt) | 7 file |
| 22 | Lời Gọi | `word-hit-bell` | Hoàn hảo, Chớp | VCSL Hand Chimes hoặc Tubular Bells, hoặc tự ghi. Không dùng Hand Bells Nepalese. Chờ duyệt | 1 |
| 23 | Lời Gọi | `wordshot-fire` | Mỗi lần bắn chữ | Stable Audio 3 (tiếng vút) cộng tiếng giấy | 4 |
| 24 | Lời Gọi | `arrow-fire` | 4 lần mỗi giây | Stable Audio 3, hoặc tự ghi tiếng dây cung tre | 4 |
| 25 | Lời Gọi | `ink-puff` | 8 lần mỗi giây | Stable Audio 3 (bao giấy nổ) | 6 |
| 26 | Lời Gọi | `blast` | Tiếng nổ | VCSL Frame Drum hoặc Timpani cộng Stable Audio 3 (giấy bung) | 3 |
| 27 | Lời Gọi | `coin` | 3 lần mỗi giây | Kenney RPG cộng VCSL Hand Chimes | 4 |
| 28 | Lời Gọi | `leak` | Báo nguy | VCSL Gong 1/2, hoặc Anvil, Brake Drum cho tiếng kẻng. Chờ duyệt | 1 |

**Ngoài lô này:** `key.ok`, `type.key` và `key-right` vẫn giữ tổng hợp. Claude chỉnh tham số bằng bản dựng không cần chạy game và tai AI. Chủ dự án nghe trong bài mỏi tai (bài E).

---

## 10. Giấy phép và nguồn gốc

### 10.1 Stable Audio 3: điều kiện dùng (bước 0)

Theo Stability AI Community License (cập nhật 5/7/2024) [[4]][s4]:

- **"Mục đích thương mại"** gồm mọi mục đích nhằm lợi ích thương mại, **kể cả tạo ra sản phẩm của bạn**. Làm âm cho một game định bán đã là mục đích thương mại.
- **Đăng ký:** ai dùng cho mục đích thương mại phải đăng ký với Stability. Vì vậy phải đăng ký **khi bắt đầu tạo âm cho game**, không đợi lúc bán.
- **Trần doanh thu:** tính bạn **và các đơn vị liên kết** (cùng kiểm soát trên 50 %), cộng lại, từ **mọi nguồn thu**, không chỉ từ game. Vượt 1 triệu USD/năm thì giấy phép không còn áp dụng, phải mua giấy phép Enterprise.
- **Âm tạo ra:** bạn sở hữu. Không dùng âm tạo ra để tạo hay cải thiện mô hình AI nền.
- **Chính sách sử dụng (AUP)** được đưa vào giấy phép.
- **Thời hạn** bắt đầu khi bạn chấp nhận giấy phép **hoặc** truy cập tài liệu của Stability. Tải trọng số về là đã chấp nhận.
- Bộ mã hóa chữ T5Gemma đi kèm theo điều khoản Gemma [[86]][s86].

**Bước 0 của chủ dự án** (mục 15):

| Câu hỏi | Nếu "có" | Nếu "không" hoặc "chưa chắc" |
|---|---|---|
| Ai sở hữu và phát hành các game: cá nhân chủ dự án, hay một công ty? Người đó cộng các đơn vị liên kết có doanh thu năm dưới 1 triệu USD, tính mọi nguồn? | Đăng ký Community License (miễn phí) **ngay**. Lưu xác nhận có ngày vào `art-src/audio/licences/stability-registration.txt`. Đọc và chấp nhận AUP và điều khoản Gemma. Sau đó Claude mới tải mô hình | **Không dùng Stable Audio 3 cho dự án này, kể cả bản nháp**, cho đến khi có giấy phép Enterprise. Lý do: định nghĩa "mục đích thương mại" gồm cả việc làm sản phẩm. Hạng 1 SFX chuyển sang ghép lớp CC0, tổng hợp và tự ghi. Thử MOSS-SoundEffect (Apache-2.0) trên MPS. Nếu có tiền, dùng ElevenLabs gói trả phí |

### 10.2 Chính sách

| Được dùng | Có điều kiện | Cấm |
|---|---|---|
| CC0 (Kenney, VCSL, VSCO-2-CE, Freesound CC0 không từ chối AI) | **Stable Audio 3:** theo mục 10.1. Nếu phân phối LoRA thì phải kèm NOTICE và dòng "Powered by Stability AI" [[4]][s4] | Mọi trọng số phi thương mại (mục 3.5), kể cả chỉ để so |
| MIT, Apache-2.0 (ACE-Step, MOSS-SoundEffect) | **CC-BY:** phải ghi công. Script tự sinh `CREDITS.md` | Freesound CC-BY-NC, Sampling+ |
| Bản ghi của chính chủ dự án | **Bản ghi của người khác** (người nhà, người chơi): chỉ dùng khi có giấy đồng ý (mục 10.4) | BBC Sound Effects, Pixabay (học máy), nhạc hay âm trích từ game khác |
| Mã tổng hợp của dự án | **Freesound CC0 có người tải lên từ chối AI** [[80]][s80]: chỉ ghép tay. Không vào bước AI nào, không vào LoRA | Âm từ gói miễn phí của ElevenLabs hay Suno, nếu đem phát hành |
| | **Magenta RT 2:** trọng số CC-BY. Ghi công nếu phân phối mô hình | Sonniss trong bất kỳ bước AI nào |
| | **ElevenLabs:** chỉ âm tạo trong thời gian đăng ký gói trả phí | |
| | **Sonniss:** không dùng ở lô 1–2. Sau đó chỉ khi: chủ dự án tự ghép tay, **hoặc** Claude chỉ chạm vào bằng số đo xử lý tín hiệu trên máy. Không gửi âm hay ảnh có lớp Sonniss cho AI chạy trên mây nào, **kể cả Claude**. Không đưa vào CLAP, audiobox, LoRA hay âm gốc audio-to-audio. Hoặc chủ dự án xin phép Sonniss bằng văn bản. File có lớp Sonniss được xếp hạng trên một **luồng riêng** (L1, L2 và tai người), chỉ so với luồng khác trên Bảng Nghe | |

Thêm 4 lưu ý:

- Game web lộ file âm qua URL. Vì vậy chỉ phát hành bản đã xử lý hoặc đã ghép lớp, không bao giờ đưa thư mục thư viện thô lên.
- Dữ liệu huấn luyện của Stable Audio 3 có cả âm Freesound CC-BY và Sampling+ [[3]][s3]. Stability vẫn nói người dùng sở hữu âm tạo ra. Đây là một câu hỏi nguồn gốc còn treo, cần kiểm lại trước khi ra mắt.
- Nếu sau này đưa game lên Steam, phải khai báo nội dung tạo bằng AI (chưa kiểm chứng điều khoản hiện hành).
- Mô hình nghe L7: ghi URL file LICENSE gốc [[82]][s82] và mã băm của nó vào danh sách công cụ, kèm ghi chú kho GGUF gắn nhãn `qwen-research` [[81]][s81]. L7 là tùy chọn và chỉ dùng nội bộ.

### 10.3 Dữ liệu gửi lên AI chạy trên mây

Thẻ ảnh PNG và số đo mà Claude đọc được gửi tới Anthropic. Codex và ChatGPT gửi tới OpenAI. Gemini gói miễn phí gửi tới Google và có thể có người đọc [[30]][s30].

- Chỉ gửi thẻ của âm CC0, âm tự ghi và âm do mô hình tạo. Không bao giờ gửi thẻ có lớp Sonniss.
- Trước khi gửi thẻ của âm chưa phát hành hay âm tự ghi, chủ dự án kiểm trong tài khoản Claude và ChatGPT rằng mục "dùng dữ liệu của tôi để cải thiện mô hình" đang **tắt** (bước 3, mục 15).
- Codex làm người duyệt thứ hai chỉ khi chủ dự án đồng ý, vì nó dùng phiên đăng nhập ChatGPT của chủ dự án. Mặc định không dùng.
- Gemini mặc định tắt.

### 10.4 Giấy đồng ý cho bản ghi của người khác

Ai không phải chủ dự án mà góp bản ghi (giọng, sáo trúc, trống cơm, foley) thì ký một đoạn ngắn. Lưu thành `art-src/audio/licences/release-<tên>-<ngày>.txt`. Mẫu:

> Tôi, `<họ tên>`, là người thu và/hoặc người phát ra các bản ghi liệt kê dưới đây, ghi ngày `<ngày>`. Tôi tặng các bản ghi này vào phạm vi công cộng theo CC0 1.0, hoặc chuyển toàn bộ quyền cho `<chủ dự án>`, để dùng trong mọi sản phẩm, kể cả sản phẩm thương mại, và để chỉnh sửa, kể cả bằng công cụ AI. Tôi đồng ý cho dùng giọng nói của tôi trong các bản ghi đó. Danh sách file: `<…>`. Ký: `<…>`.

### 10.5 Hồ sơ cho mỗi file phát hành (`art-src/audio/SOURCES.json`)

```json
{
  "gun.xung-3.ogg": {
    "id": "gun.xung", "variant": 3, "sha256": "…", "date": "2026-10-25",
    "recipe": "recipes/gun.xung.json", "recipeHash": "…",
    "layers": [
      {"role": "body", "tool": "stable-audio-3", "model": "stabilityai/stable-audio-3-optimized@<revision>",
       "licence": "Stability-Community-2024", "licenceAccepted": "licences/stability-registration.txt",
       "prompt": "…", "cfg": 1.0, "seed": 811, "window": [0.12, 0.30],
       "initAudio": "hero sha256 …", "initNoise": 0.55},
      {"role": "mech", "source": "kenney/impact-sounds/impactMetal_light_002.ogg",
       "licence": "CC0-1.0", "sourceSha256": "…"}
    ],
    "chain": "raw-qa, trim<2ms, hpf35, soxr48k, mid-mono, tp-1, lufsM-20",
    "rawQa": "review/qa/gun.xung.json#raw",
    "tools": {"ffmpeg": "9.0.2", "pedalboard": "0.9.26"},
    "review": {"owner": "pick", "stars": 4, "batch": "b1", "variantPass": "kept"}
  }
}
```

### 10.6 Sổ nguồn (`art-src/audio/licences.jsonl`)

Mỗi file nguồn có một dòng. Mỗi dòng ghi:

- `sha256`, thư viện, gói và năm, tên file gốc, URL, tác giả.
- Mã giấy phép và phiên bản giấy phép, ngày tải, đường dẫn tới bản lưu giấy phép trong `art-src/audio/licences/`.
- Các cờ: `commercial_ok`, `attribution_required`, `attribution_text`, `ai_input_allowed`, `raw_redistribution_allowed`, `genai_preference` (của Freesound), `release_file` (với bản ghi của người khác).

Giấy phép phải lưu kèm ngày tải. Lý do: Sonniss áp dụng phiên bản giấy phép có hiệu lực vào ngày tải [[39]][s39].

Sổ cũng có một dòng cho mỗi lần chấp nhận giấy phép mô hình (Stability, Gemma, ACE-Step MIT): ai chấp nhận, ngày nào, phiên bản nào.

### 10.7 Script kiểm (`pnpm audio:licence-check`, gọi từ `media:check`)

Script chặn bản dựng khi gặp một trong các trường hợp sau:

- File phát hành không có hồ sơ.
- Có nguồn mà `commercial_ok=false`.
- Có giấy phép lạ.
- Có nguồn mang `ai_input_allowed=false` đã đi qua một bước AI, kể cả bước chấm bằng mô hình.
- Có lớp Stable Audio 3 mà chưa có dòng đăng ký Stability.
- Có bản ghi của người khác mà chưa có giấy đồng ý.
- Có nguồn CC-BY mà chưa có trong `CREDITS.md`.

### 10.8 An toàn khi cài và tải

- **Không token:** mọi script của Claude chạy với `HF_TOKEN` và `HUGGING_FACE_HUB_TOKEN` bị bỏ, `HF_HUB_DISABLE_IMPLICIT_TOKEN=1`, và `HF_HUB_OFFLINE=1` sau lần tải đầu. Lý do: `weights.py` của Stable Audio 3 tự dùng `HF_TOKEN` hoặc phiên đăng nhập đã lưu nếu có [[77]][s77]. Nếu chủ dự án cần đăng nhập Hugging Face vì việc khác, chủ dự án tự tải rồi chạy `hf auth logout`.
- **Cài uv bằng Homebrew trước khi chạy `install.sh`**, để script không gọi `curl … | sh` [[76]][s76]. Không chạy lệnh cài một dòng `curl | bash`.
- **Đọc trước khi chạy:** `install.sh`, `scripts/install.py`, `scripts/weights.py`, `requirements.txt` của Stable Audio 3. Với ACE-Step: đọc cả mã mô hình tùy biến trong kho trọng số (`modeling_acestep_v15_turbo.py`, `configuration_acestep_v15.py`) [[87]][s87].
- **Ghim phiên bản:** commit git của `stable-audio-3` và `ACE-Step-1.5`, `revision=` của từng kho Hugging Face, và file khóa pip có mã băm (`uv lock`).
- **Không mở ra ngoài:** mọi giao diện chạy trên máy phải nghe ở `127.0.0.1`. Kiểm bằng `lsof -iTCP -sTCP:LISTEN`. Gradio của Stable Audio 3 mặc định mở link công khai, nên **luôn chạy `--no-share`** [[2]][s2]. Với ACE-Step, dùng CLI hoặc API thay cho Gradio.
- **Không tải trọng số phi thương mại** (mục 3.5).

### 10.9 Công cụ GPL

- pedalboard (GPL-3.0) chỉ được `import` từ script trên máy. Không chép mã hay file của nó vào repo. venv không vào Git.
- Các repo chưa có file `LICENSE`. Khi thêm giấy phép cho `tools/audio-lab`, chọn loại tương thích GPL, hoặc chỉ gọi ffmpeg và sox qua dòng lệnh.
- Chỉ âm đã dựng được đóng vào game. Không đóng công cụ GPL nào vào bản web.

---

## 11. Bố cục file, manifest và media:push

```
~/AudioLab/                         # ngoài mọi repo; không vào Git
  models/                           # repo Stable Audio 3 kèm .venv, ACE-Step, cache Hugging Face (đã gộp file trùng)
  libraries/kenney/ vcsl/ vsco2ce/ freesound-cc0/     # VCSL tải thưa; mỗi thư viện có LICENSE-<ngày>.txt
  libraries/_no-ai/                 # (sau lô 2, nếu có) Sonniss; cấm khỏi mọi bước AI
  work/<game>/<id>/<run>/           # ứng viên, thẻ PNG, JSON; xóa sau khi chốt

typing-game/tools/audio-lab/        # chỉ có mã; venv bị Git bỏ qua
  critic/  gen/  build/  sampler/  board/  harness/  specs/  fixtures-tts/ (chỉ script ghi giọng)

games/<game>/art-src/audio/
  specs/<id>.yaml                   # Git
  recipes/<id>.json                 # Git
  SOURCES.json, licences.jsonl      # Git
  licences/*.txt                    # Git: bản lưu giấy phép, xác nhận đăng ký, giấy đồng ý
  review/ratings.jsonl, review/qa/<id>.json   # Git (PNG trong review/ bị chặn bởi *.png)
  masters/<id>/<id>-v<n>.wav        # Drive, qua media:push
  foley/<phiên>/*.wav               # Drive
  stems/<lớp>.wav                   # Drive

games/<game>/public/assets/<game>/audio/
  manifest.json                     # Git
  sfx/<nhóm>/<id>-<n>.ogg           # Drive
  music/<lớp>.ogg                   # Drive
```

**Vì sao ứng viên không nằm trong `art-src`:** `media:push` đẩy mọi file media trong `art-src`. Nếu để ứng viên ở đó, Drive sẽ đầy file nháp.

**`.gitignore` của Rồng Giữ Ải và Tuyến Cuối:** hiện cả `art-src/` và `public/assets/**` bị bỏ qua. Git không đưa lại được một file khi thư mục cha đã bị loại, nên chỉ một dòng `!…/manifest.json` là không đủ. Chép mẫu ba dòng của Lời Gọi. Thay dòng `art-src/` bằng chuỗi sau (đổi `<game>` thành tên game), giữ nguyên các dòng `*.png`, `*.wav`, `*.ogg`:

```
public/assets/**
!public/assets/<game>/
!public/assets/<game>/**/
!public/assets/<game>/**/manifest.json
art-src/*
!art-src/audio/
art-src/audio/*
!art-src/audio/specs/
!art-src/audio/recipes/
!art-src/audio/review/
!art-src/audio/licences/
!art-src/audio/SOURCES.json
!art-src/audio/licences.jsonl
```

Sau khi đổi, kiểm bằng `git check-ignore -v` trên ba file mẫu: một `manifest.json` (phải được theo dõi), một `ratings.jsonl` (phải được theo dõi) và một `.wav` (phải bị bỏ qua).

**Manifest v2:** schema hiện tại của Rồng Giữ Ải ánh xạ id thành mảng đường dẫn. Bản v2 mở rộng mà vẫn tương thích ngược, vì bộ tải của kit nhận được cả hai dạng. Manifest do script sinh ra từ thư mục masters. Manifest **không** chứa mức to: mọi file đã chuẩn hóa về một mức chung, mức tương đối chỉ nằm trong `gainDb` của catalog và mức bus.

```json
{
  "version": 2,
  "sounds": {
    "gun.xung": {"files": ["sfx/guns/gun-xung-1.ogg", "sfx/guns/gun-xung-2.ogg"],
                 "durationMs": [118, 121], "loop": false}
  },
  "music": {"calm": {"file": "music/calm.ogg", "bpm": 96, "bars": 8}}
}
```

**Định dạng:**

- Giữ OGG Vorbis 48 kHz, đúng quy ước hiện tại.
- Safari hỗ trợ đầy đủ từ bản 18.4 [[62]][s62]. Với Safari cũ, có thể thêm bản `.m4a` dự phòng trong manifest.
- Vòng lặp dùng OGG hoặc WAV, không dùng MP3, vì MP3 có khoảng đệm gây hở mối nối.

**Gộp file (sprite):** chưa làm. Mỗi giây âm mono 48 kHz sau khi giải mã chiếm khoảng 192 KB. Khi Rồng Giữ Ải có 300–500 file, cần đo bộ nhớ và thời gian tải trước. Ưu tiên tải theo mức ưu tiên thay vì giải mã hết lúc mở.

**`media:push`:** các đuôi ogg, wav, flac và opus đã có sẵn trong `mediaExtensions`. JSON không phải media nên đi qua Git. `media:check` cần thêm phần kiểm tham chiếu âm, song song với phần đang kiểm `modelsManifest`.

**Dung lượng ổ:** dự trù 40–50 GB ngoài repo.

| Phần | Ước tính |
|---|---|
| Stable Audio 3 MLX (sm-sfx, sm-music, bộ giải mã, T5Gemma) | Vài GB (chưa kiểm dung lượng từng file) |
| ACE-Step 1.5 | Khoảng 10,1 GB [[87]][s87] |
| Mô hình chấm (audiobox, CLAP, AST), sau khi gộp file `.bin` và `.safetensors` trùng | 2–3 GB (bản thử chưa gộp: 5,9 GB) |
| Qwen2.5-Omni-7B (tùy chọn) | Khoảng 6,2 GB |
| venv và cache uv | Khoảng 3 GB |
| Thư viện CC0 (VCSL tải thưa, VSCO-2-CE, Kenney) | Khoảng 3–5 GB (VCSL đủ bộ khoảng 3,8 GB) |
| Ứng viên đang làm | Khoảng 5 GB, xóa sau khi chốt |

---

## 12. Kế hoạch theo giai đoạn

Thời gian của Claude là ước tính, tính bằng ngày làm việc. Tổng khoảng 17–23 ngày.

| Giai đoạn | Việc | Claude | Chủ dự án | Tài khoản, chấp nhận, duyệt | Xong khi |
|---|---|---|---|---|---|
| **0. Chuẩn bị** | `brew install ffmpeg uv`. Chuyển hai bản thử vào `tools/audio-lab`, ghim phiên bản, thêm biến môi trường không token vào `run_all.sh` | 0,5 ngày | Khoảng 1 giờ (bước 0–4, mục 15) | Bước 0 (Stability). Chấp nhận giấy phép. Duyệt cài đặt và 40–50 GB ổ. Kiểm cài đặt dữ liệu của Claude và ChatGPT | Chạy lại được bản thử. Có quyết định bước 0 |
| **1. Tai AI và Bảng Nghe v1** | Gói phê bình L1, L1b, L2–L6. Thẻ spec sinh từ `catalog.ts` và các tài liệu. Thẻ ảnh. Sổ giấy phép và script kiểm. Bảng Nghe với bối cảnh Một mình, Lặp 20 lần, Loa nhỏ | 3–4 ngày | 15 phút (lô 0a) | — | Có báo cáo JSON và PNG cho 40 âm thử. Có dữ liệu lô 0a |
| **2. Nguồn và bản thử Stable Audio 3** | Đọc mã cài đặt, rồi cài Stable Audio 3 MLX (nếu bước 0 cho phép). Lớp gọi có ghi seed, `cfg`, hồ sơ. Bản thử 6 id (mục 9). Tải Kenney, VCSL (tải thưa), VSCO-2-CE. Bộ phát mẫu Python. Bộ ghép lớp và chuỗi xử lý cuối. Nền nhạc thô cho 3 game. Ghi mẫu giọng macOS | 1,5–2 ngày | 15 phút (lô 0b) | — | Quyết định đi tiếp hay đổi hạng 1. 1 id mẫu đi hết vòng ở mục 5.1 |
| **3. Nối vào game** (sau khi các làn cân bằng merge, hoặc worktree riêng) | Đưa `FileBank` vào kit, thêm biến thể, ngẫu nhiên theo nhóm, nhạc đi qua bus, hạ tiếng từ lúc yêu cầu đọc đến `end`. Tách bậc trúng Tuyến Cuối thành lớp. Sửa bộ giới hạn của Rồng Giữ Ải. Harness đọc file, xuất WAV, nhận mẫu giọng. Bộ tải cho Lời Gọi. `.gitignore`, manifest, `media:check` kiểm âm. Bảng Nghe v2 có "Trong trận" | 3–4 ngày | 10 phút duyệt mức nhường tiếng. Duyệt các thay đổi hợp đồng ở mục 6.2 | Duyệt đổi `.gitignore` | Bài thử A–J chạy được trên bản tổng hợp |
| **4. Lô 1 (28 âm)** | Mỗi game: bảng phong cách, rồi các id. Thứ tự 1a, 1b, 1c (mục 9) | Khoảng 1 ngày mỗi game | Khoảng 1,5–2 giờ, 4–5 phiên | Duyệt nguồn chuông, cồng, quãng tám `word-hit` trước 1c | 28 id có file. Bài thử A–J đạt. Có changelog |
| **5. Hiệu chỉnh, lô 2, người chơi thử** | Ước lại ngưỡng theo bản dò. Làm phần SFX còn lại, khoảng 100 id. 3–5 người chơi thử nghe A/B trong game | 4–5 ngày | 6–8 phiên × 15–20 phút. Mời người chơi thử | (Tùy chọn) tài khoản Freesound | Có số đo loại nhầm trên bản dò cho từng họ |
| **6. Nhạc** | Viết MIDI và render bằng bộ phát mẫu Python với mẫu CC0. ACE-Step phác ý tưởng. Kiểm mối nối, BPM, giọng giữa các stem. Chạy lại bài C và D với nhạc thật | 2,5–3,5 ngày | 30 phút duyệt văn hóa | — | Có stem cho 3 game |
| **7. Tùy chọn** | Buổi tự ghi foley. LoRA Stable Audio 3 trên bản ghi của chủ dự án. Thử MOSS. Magenta RT. Mô hình nghe Qwen-Omni. Một tháng ElevenLabs. Surge XT | Theo việc | Ghi foley 30 phút | ElevenLabs, Google AI Plus (nếu chi tiền). Mật khẩu admin cho Surge XT | — |

---

## 13. Không tốn tiền và ít tiền

| Hạng mục | Không tốn tiền (mặc định) | Ít tiền (chỉ khi lô 1 cho thấy thiếu) |
|---|---|---|
| SFX | Stable Audio 3 chạy trên máy (nếu đủ điều kiện), thư viện CC0, mã tổng hợp, tự ghi | Một tháng ElevenLabs Starter: 6 USD, hoặc 1 USD tháng đầu nếu mua trước 1/11/2026 [[34]][s34]. Tạo hết bản cuối trong tháng đó rồi hủy. Hoặc trả theo giây qua fal.ai, 0,002 USD/giây [[74]][s74] (cần khóa của chủ dự án) |
| Nhạc | MIDI cộng mẫu CC0, ACE-Step 1.5 | Google AI Plus (Flow Music, có quyền thương mại) [[38]][s38], hoặc Lyria 3.5 với 0,08 USD/bài [[30]][s30]. Không khuyên Suno [[35]][s35], Udio [[36]][s36] |
| Nhạc cụ Việt | VCSL, tự ghi | Mua thư viện mẫu sáo trúc hoặc trống cơm nếu tìm được nguồn rõ giấy phép (chưa tìm thấy) |
| Tai AI | Mọi lớp L1–L7 chạy trên máy | Gemini API gói miễn phí. Không tốn tiền, nhưng dữ liệu bị dùng để cải thiện sản phẩm [[30]][s30], nên mặc định tắt |
| Ghi âm | Điện thoại, phòng yên tĩnh | Một micro cài áo rẻ (tùy chọn) |

---

## 14. Rủi ro và điều chưa kiểm chứng

- **Điều kiện Stable Audio 3.** Nếu bước 0 trả lời "không", công cụ hạng 1 rơi khỏi kế hoạch. Phương án thay đã có (mục 10.1) nhưng chất lượng chưa biết.
- **Chất lượng của Stable Audio 3 với SFX game chưa được kiểm độc lập.** Mô hình có thể yếu với tiếng dưới 50 ms, cao độ chính xác và nhạc cụ Việt. Bản thử 6 id trả lời câu hỏi này.
- **Bộ chấm chưa thử trên âm do mô hình tạo.** Bản thử chỉ có 16 âm gốc và lỗi làm hỏng có chủ ý. Lỗi thật tinh vi hơn. Vì vậy bộ dò L1b chỉ gắn cờ cho đến lô 0b.
- **Điểm máy dễ bị "lách".** audiobox ưa âm sạch mà nhạt. CLAP thưởng cả âm bị méo. Vì vậy điểm máy chỉ dùng để xếp hạng, và luôn có bản dò.
- **Mô hình nghe có điểm mù.** Mọi mô hình nghe đã kiểm đều hạ âm xuống 16 kHz mono. Chúng không nghe được phần trên 8 kHz và không nghe được stereo. Gemini còn nén âm xuống 16 kbps [[30]][s30]. Thẻ ảnh và luật đo phải phủ phần này.
- **Giọng đọc nằm ngoài WebAudio.** Mức và thời điểm của giọng đổi theo hệ điều hành và trình duyệt. Bài C dùng mẫu giọng và quét mức, nhưng giọng Chrome qua mạng chỉ có khi chủ dự án ghi lại. Giọng của Windows chưa có mẫu.
- **Thời gian của chủ dự án.** Hiệu chỉnh cần nhiều lượt chấm. Gộp họ âm giúp giảm, nhưng tháng đầu vẫn khoảng 4–6 giờ.
- **Đụng việc với các làn cân bằng.** Mã âm trong game sửa sau khi các làn merge, hoặc trong worktree riêng.
- **Bộ nhớ 16 GB.** Mô hình nghe 7B, Stable Audio 3 hoặc ACE-Step, cộng Chrome và Vite cùng lúc có thể làm máy phải dùng swap. Mỗi lúc chỉ chạy một mô hình nặng.
- **Rủi ro giấy phép:**
  - Stability Community không phải giấy phép mã nguồn mở. Có trần doanh thu tính cả công ty liên kết, và phải đăng ký từ lúc làm.
  - Sonniss có mục "NO AI TRAINING OR USAGE".
  - Freesound có giấy phép lẫn lộn và tùy chọn AI của người tải lên.
  - Câu chữ về gói miễn phí của ElevenLabs tự mâu thuẫn [[34]][s34].
  - Kho GGUF của Qwen2.5-Omni-7B gắn nhãn khác file LICENSE gốc.
  - Các điều khoản thay đổi rất nhanh trong năm 2026: Sora đóng, Udio tắt tải, Suno giới hạn tải, Gemini CLI đổi.
- **Cài đặt:** script cài có thể gọi `curl | sh` nếu thiếu uv, và ACE-Step tự tải mã mô hình. Biện pháp ở mục 10.8.
- **Văn hóa:** mô hình tạo âm dễ trượt về âm thanh "châu Á chung chung". Mọi âm và nhạc của Lời Gọi cần chủ dự án duyệt.
- **Nhạc giống bài có sẵn:** README của ACE-Step tự cảnh báo điều này [[6]][s6]. Cần kiểm giai điệu trước khi bán.
- **Chưa kiểm chứng:**
  - Tốc độ và RAM thật của Stable Audio 3 trên M4 của chủ dự án; dung lượng bộ MLX.
  - MOSS chạy trên MPS.
  - Antigravity CLI có nhận file âm không.
  - Giá Google AI Plus tại Việt Nam hiện nay.
  - VCSL Gong 1 và 2 là loại cồng nào.
  - Cờ giữ formant chính xác của rubberband.
  - 99Sounds có bắt đăng ký email không; Surge XT có hỏi mật khẩu admin không.
  - Giấy phép của mido (thường là MIT).
  - Ngưỡng SII 0,75, ngưỡng L1b, và mọi con số trong mục 4.3.3 chưa có trong tài liệu game.
- **Bản thử nằm trong `/private/tmp`.** Hệ điều hành có thể xóa thư mục này. Giai đoạn 0 phải chuyển mã vào repo, và `run_all.sh` phải chạy lại được từ đầu.

---

## 15. Ai làm gì

### 15.1 Chủ dự án làm (theo thứ tự)

| Bước | Việc | Thời gian | Cần tài khoản, chấp nhận hay quyền gì |
|---|---|---|---|
| **0** | **Quyết định pháp lý cho Stable Audio 3** (mục 10.1): ai sở hữu và phát hành game; doanh thu năm của người đó cộng đơn vị liên kết có dưới 1 triệu USD không. Nếu có: đăng ký Stability Community License ngay, lưu xác nhận có ngày vào `art-src/audio/licences/stability-registration.txt` | 10–15 phút | Mẫu đăng ký của Stability (cần email) |
| 1 | **Đọc và chấp nhận giấy phép mô hình:** Stability Community License và AUP [[4]][s4], điều khoản Gemma [[86]][s86], MIT của ACE-Step [[6]][s6]. Ghi ngày chấp nhận vào `licences.jsonl` (Claude tạo sẵn dòng, chủ dự án xác nhận). Tải trọng số về là đã chấp nhận, nên Claude chỉ tải sau bước này | 20 phút | Chấp nhận giấy phép. **Không cần tài khoản Hugging Face** |
| 2 | **Duyệt cài đặt:** `brew install ffmpeg uv` và 40–50 GB ổ đĩa ngoài repo | 5 phút | Duyệt cài đặt |
| 3 | **Kiểm cài đặt dữ liệu:** trong tài khoản Claude và ChatGPT, mục "dùng dữ liệu để cải thiện mô hình" đang tắt | 5 phút | Tài khoản của chủ dự án |
| 4 | **Quyết định chính sách** (mục 16): đưa `manifest.json` và file chữ trong `art-src/audio/` vào Git; 116 file của Space Typing; loại trừ mô hình phi thương mại; các thay đổi hợp đồng ở mục 6.2; `word-hit`; `amb.forest`; stem `general` | 15 phút | — |
| 5 | **Lô 0a** trên Bảng Nghe | 15 phút | — |
| 6 | **Lô 0b** (âm Stable Audio 3 thật, 6 id) | 15 phút | — |
| 7 | **Kể tên 3–5 game** mà chủ dự án thích tiếng trận, cho mỗi thể loại. Chỉ dùng để mô tả, không lấy âm | 10 phút | — |
| 8 | **Duyệt nguồn chuông, cồng và quãng tám `word-hit`** của Lời Gọi | 10 phút | — |
| 9 | **Bảng phong cách** cho từng game, có duyệt văn hóa cho Lời Gọi | 3 × 10 phút | — |
| 10 | **Lô 1**, gồm lượt biến thể | 1,5–2 giờ, 4–5 phiên | — |
| 11 | **Duyệt mức nhường tiếng** trên bản dựng ca xấu nhất của bài C | 10 phút | Duyệt đổi `.gitignore` |
| 12 | **Nghe bản trộn trên điện thoại và laptop**, mỗi lô một lần | 5 phút | — |
| 13 | **Giai đoạn 5:** mời 3–5 người chơi thử; chấm lô 2 | 6–8 × 15–20 phút | — |
| 14 | **Duyệt văn hóa** các stem nhạc và âm có cồng của Lời Gọi | 30 phút | — |
| 15 | **Trước khi bán:** kiểm lại giấy phép của từng phiên bản mô hình đã dùng; thay các câu thoại DotA trong Space Typing; khai báo AI nếu lên Steam | — | — |

**Tùy chọn** (chỉ khi cần):

| Việc | Cần gì |
|---|---|
| Cài Surge XT (`brew install --cask surge-xt`) | Gói `.pkg`, thường hỏi mật khẩu admin [[79]][s79] |
| Cài `cmake` để dựng `sfizz` bản arm64 | Duyệt cài đặt. Mặc định không cần, vì đã có bộ phát mẫu Python. Không khuyên cài Rosetta |
| Cài `rubberband` | Duyệt cài đặt. Chỉ khi giữ `word-hit` ở C5–C6 |
| Tải gói 99Sounds Electromagnetic | Có thể phải đăng ký email |
| Freesound: tìm và tải âm CC0 bằng tay trên web | Tài khoản Freesound. Nếu muốn script tìm qua API: chủ dự án tạo khóa, giữ trong Keychain, và tự chạy script |
| Ghi foley 30 phút theo danh sách Claude viết (tre, giấy, nón lá, chuông đồng, cồng, nồi, đồ thép; nếu được thêm sáo trúc, trống cơm, tiếng "Ơ… ơi!") | Người khác góp bản ghi thì ký giấy đồng ý (mục 10.4) |
| Ghi giọng "Google US English" của Chrome cho bài C | Ghi bằng điện thoại cạnh loa |
| Cho Codex làm người duyệt ảnh thứ hai | Đồng ý dùng phiên ChatGPT; đưa Codex lên PATH |
| ElevenLabs, Stability API, fal.ai, Lyria, Gemini, Google AI Plus, ZeroGPU | Tài khoản và khóa của chủ dự án. Chủ dự án tự chạy. Claude không giữ khóa |
| Sonniss (sau lô 2) | Chủ dự án tự tải và đọc giấy phép, để ngoài repo và ngoài Drive công khai. Muốn dùng trong bước AI thì xin phép Sonniss bằng văn bản |
| Mua một tháng ElevenLabs Starter | Quyết định sau lô 1 |

### 15.2 Claude tự làm (không cần tài khoản, khóa hay quyền admin)

- Viết thẻ spec, công thức, bộ phê bình, bộ phát mẫu Python, Bảng Nghe và script kiểm giấy phép.
- Tải Kenney, VCSL (tải thưa) và VSCO-2-CE. Đây là CC0, không cần tài khoản. Lưu bản giấy phép kèm ngày tải.
- Sau bước 0–2: tải trọng số Stable Audio 3 MLX từ kho không có cổng, và ACE-Step, với môi trường không token, có ghim phiên bản.
- Tạo ứng viên, sửa tự động, đo, xếp hạng, đọc thẻ ảnh, lập danh sách nghe có bản dò.
- Ghi mẫu giọng macOS bằng `say -o` cho bài C.
- Dựng nền nhạc thô, bản trận, bài thử A–J, và báo cáo.
- Ghi `SOURCES.json`, `licences.jsonl`, `ratings.jsonl` phân tích, changelog của từng game.
- Không commit. Người điều phối commit.

---

## 16. Câu hỏi mở và mặc định

| # | Câu hỏi | Mặc định nếu chủ dự án chưa trả lời |
|---|---|---|
| 1 | Ai sở hữu, phát hành game, và có đủ điều kiện Stability Community không? | Chưa tải Stable Audio 3. Claude làm trước phần CC0, tổng hợp, bộ chấm và Bảng Nghe |
| 2 | Nhạc nhường giọng đọc bao nhiêu? | Giữ mức hiện tại của từng game: Rồng Giữ Ải −4 dB, Tuyến Cuối −4 dB, Lời Gọi −9 dB. Chỉ đề xuất mức mới khi bài C trượt |
| 3 | Âm xong từ và phím trong lúc đọc (mục 6.2) | Âm xong từ giảm 1–4 kHz ít nhất 15 dB trong 100 ms; nếu không được thì giọng chờ 150 ms. Phím hạ −8 dB khi đọc. Chỉ đổi phổ phím khi bài C trượt |
| 4 | `word-hit` hạ một quãng tám thành C4–C5? | Có, đề xuất hạ. Chờ chủ dự án duyệt trước lô 1c |
| 5 | Nguồn chuông và cồng của Lời Gọi | Không dùng VCSL Hand Bells Nepalese. Chủ dự án nghe Hand Chimes, Tubular Bells, Gong, Anvil rồi chọn. Không được thì tự ghi |
| 6 | Tách bậc trúng Tuyến Cuối thành lớp, thêm `hit.sub` và `hit.tail` | Có. Sửa `THEME_SOUND_LIST.md` trước lô 1b |
| 7 | `amb.forest` giữ vòng 6 s hay làm nền dài nhiều lớp? | Giữ 6 s theo tài liệu game |
| 8 | Stem `general` của Rồng Giữ Ải ghi "D minor" trên các stem Rê Dorian | Đề xuất đổi sang Rê Dorian, hoặc tránh nốt Si giáng khi đang ở hợp âm G. Chủ dự án chọn |
| 9 | 116 file âm CC0 của Space Typing đang trong Git | Giữ nguyên. File mới không vào Git |
| 10 | Cài Surge XT (cần mật khẩu admin)? | Không cài. Tiếng điện tổng hợp bằng numpy và pedalboard |
| 11 | Dùng Sonniss? | Không dùng ở lô 1–2 |
| 12 | Sửa mã âm trong game khi nào? | Sau khi các làn cân bằng merge, hoặc trong worktree riêng |

---

## Phụ lục A. Bản thử "tai AI": số liệu và cách chạy lại

Thư mục: `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/ea3cd405-f9d2-442c-a760-74fe0277c6ca/scratchpad/audio-research/poc`. Bảng gốc do script sinh: `out/tables.md` và `out/pairs.md`.

### A.1 Môi trường

- Apple M4, 16 GB, macOS 15.5. Không cài gì vào hệ thống, không tài khoản, không khóa.
- uv 0.13.5 riêng (kiểm SHA-256) trong thư mục bản thử. CPython 3.12.15 do uv tải.
- Hai venv: `.venv` (transformers 5.20.2) và `.venv-tf4` (transformers 4.57.6, chỉ cho MiDashengLM).
- librosa 1.0.0, torch 2.14.1 chạy MPS, audiobox-aesthetics 0.0.4. libsndfile 1.2.2 đọc được OGG và MP3, nên không cần ffmpeg.
- Dung lượng: 9,2 GB (venv 2,1 GB, cache Hugging Face 5,9 GB, cache uv 1,1 GB). Bản thử 1 chiếm thêm 5,9 GB ở `scratchpad/dl` (gồm GGUF của Qwen2.5-Omni).

### A.2 Tập thử

- **8 âm tổng hợp** (`gen_samples.py`, seed 7): tiếng "bíp" yếu 3 ms; tiếng trúng tốt nhiều lớp; bản clip gắt (+18 dB, méo, cắt cứng); bản đục (lên 45 ms, +9 dB ở 300 Hz, lọc thấp 600 Hz, vang tối); vòng lặp liền; vòng lặp hở; tiếng zap sci-fi; tiếng vút lửa.
- **8 âm Kenney CC0** (Impact Sounds 1.0 và Sci-Fi Sounds 1.0). Giấy phép CC0 đã kiểm trên trang và trong `License.txt` của từng zip.
- **24 bản làm hỏng** (`degrade.py`) từ 8 âm tốt: clip, đục, mỏng.

### A.3 Luật đo (`analyze.py`) trên 16 âm gốc

| File | Hồ sơ | Dài (s) | Đỉnh thật (dBTP) | LUFS-M max | Crest (dB) | Lên (ms) | Punch (dB) | Mất trên laptop (dB) | Mẫu clip | Điểm lặp | Kết luận: cờ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| syn_clipped_harsh | impact | 1,20 | +3,89 | −0,3 | 2,5 | 0,0 | 0,32 | 0,22 | 25.373 | — | **FAIL**: clipping, true_peak, dc_offset, weak_punch, over_compressed, loudness, tail_cut |
| syn_fire_whoosh | whoosh | 1,80 | −2,87 | −11,88 | 15,25 | 633,0 | −9,64 | 0,0 | 0 | — | **PASS** |
| syn_loop_broken | loop | 2,00 | −5,99 | −16,92 | 10,09 | 32,5 | 1,97 | 8,32 | 0 | 0,571 | **FAIL**: loop_seam, unstable_level |
| syn_loop_seamless | loop | 2,00 | −5,99 | −17,09 | 8,62 | 33,0 | 1,3 | 8,04 | 0 | 0,84 | **PASS** |
| syn_muddy_low | impact | 1,60 | −1,49 | −12,3 | 13,19 | 58,0 | −5,17 | 7,68 | 0 | — | **WEAK**: dc_offset, soft_attack, weak_punch, dull, small_speaker |
| syn_punchy_impact | impact | 1,20 | −0,75 | −19,36 | 20,48 | 1,0 | 9,59 | 4,11 | 0 | — | **OK_WITH_NOTES**: true_peak |
| syn_scifi_zap | impact | 0,35 | −1,89 | −14,02 | 13,24 | 1,0 | 13,71 | 0,01 | 0 | — | **WEAK**: thin, tail_cut |
| syn_weak_click | impact | 0,15 | −23,94 | −49,38 | 7,26 | 1,0 | 40,0 | 0,0 | 0 | — | **WEAK**: over_compressed, thin, no_body, loudness |
| kenney_explosionCrunch_000 | impact | 0,78 | −0,94 | −14,93 | 12,52 | 0,5 | 4,34 | 3,46 | 0 | — | **WEAK**: true_peak, weak_punch |
| kenney_impactBell_heavy_000 | impact | 1,48 | −1,13 | −18,82 | 22,89 | 0,5 | 12,06 | 0,25 | 0 | — | **OK_WITH_NOTES**: muddy (báo nhầm) |
| kenney_impactGeneric_light_000 | ui | 0,14 | −1,23 | −23,01 | 16,5 | 0,5 | 31,38 | 0,8 | 0 | — | **WEAK**: muddy, dull, tail_cut |
| kenney_impactMetal_heavy_000 | impact | 0,17 | −0,91 | −24,01 | 19,63 | 1,0 | 24,92 | 3,52 | 0 | — | **WEAK**: true_peak, loudness, tail_cut |
| kenney_impactPunch_heavy_000 | impact | 0,65 | −0,96 | −15,35 | 14,19 | 1,0 | 17,95 | 5,01 | 0 | — | **WEAK**: true_peak, dull |
| kenney_impactWood_heavy_000 | impact | 0,31 | −0,93 | −20,5 | 14,71 | 2,49 | 32,57 | 13,73 | 0 | — | **WEAK**: true_peak, dull, small_speaker, loudness, tail_cut |
| kenney_laserLarge_000 | impact | 0,68 | −0,24 | −15,77 | 14,24 | 2,0 | 12,47 | 3,11 | 0 | — | **OK_WITH_NOTES**: true_peak |
| kenney_spaceEngineLow_000 | loop | 5,00 | −0,98 | −8,58 | 6,67 | 7,48 | 1,45 | 7,66 | 0 | 0,49 | **FAIL**: true_peak, loudness, loop_seam (lỗi thật ở mối nối) |

Đọc bảng: luật xếp đúng thứ tự tốt > yếu > đục > clip. Kenney: 5/8 WEAK, 1/8 FAIL, 2/8 OK_WITH_NOTES. Phần lớn cờ của Kenney đến từ ngưỡng chung (độ to, đuôi, đỉnh thật), không phải lỗi thật. Đây là lý do lô 1 chỉ chặn lỗi vệ sinh.

### A.4 Các lớp học máy trên 16 âm gốc

| File | AES PQ | AES CE | CLAP nhỏ, loại #1 | CLAP lớn, loại #1 | AST nhãn đầu | MiDashengLM "sạch?" |
|---|---|---|---|---|---|---|
| syn_clipped_harsh | 4,932 | 2,707 | a big explosion | a metal impact clang | Explosion 0,505 | No |
| syn_fire_whoosh | 4,799 | 2,319 | a fire breath whoosh | a fire breath whoosh | Whip 0,384 | Yes |
| syn_loop_broken | 5,129 | 2,216 | an industrial machine drone | a user interface click | Sine wave 0,398 | No |
| syn_loop_seamless | 4,879 | 1,923 | an industrial machine drone | a user interface click | Sine wave 0,393 | yes |
| syn_muddy_low | 5,808 | 3,11 | a fire breath whoosh | a user interface click | Explosion 0,366 | yes |
| syn_punchy_impact | 6,925 | 3,858 | a sci-fi laser gun shot | a user interface click | Bang 0,374 | Yes |
| syn_scifi_zap | 7,558 | 3,29 | a sci-fi laser gun shot | a sci-fi laser gun shot | Music 0,178 | Yes |
| syn_weak_click | 6,521 | 2,737 | a user interface click | a user interface click | Sound effect 0,057 | Yes |
| kenney_explosionCrunch_000 | 5,269 | 2,091 | a big explosion | a fire breath whoosh | Explosion 0,661 | Yes |
| kenney_impactBell_heavy_000 | 7,146 | 3,474 | a metal impact clang | a bronze bell strike | Clang 0,281 | Yes |
| kenney_impactGeneric_light_000 | 7,503 | 4,346 | a user interface click | a user interface click | Boing 0,247 (Speech 0,183 thứ hai) | Yes |
| kenney_impactMetal_heavy_000 | 7,799 | 4,011 | a user interface click | a user interface click | Ding 0,569 | Yes |
| kenney_impactPunch_heavy_000 | 7,001 | 3,398 | a wooden hit knock | a body punch hit | Knock 0,46 | Yes |
| kenney_impactWood_heavy_000 | 7,161 | 3,193 | a wooden hit knock | a user interface click | Sound effect 0,127 | Yes |
| kenney_laserLarge_000 | 6,471 | 3,652 | a sci-fi laser gun shot | a sci-fi laser gun shot | Music 0,246 | Yes |
| kenney_spaceEngineLow_000 | 4,379 | 2,045 | an industrial machine drone | an industrial machine drone | Vehicle 0,347 | yes |

MiDashengLM trả lời câu hỏi mở về chất lượng là "distorted" cho cả 40/40 file.

### A.5 24 cặp làm hỏng: lớp nào chọn đúng bản tốt

| Lớp | Clip | Đục | Mỏng | Tổng |
|---|---|---|---|---|
| Luật đo (điểm phạt) | 8/8 | 8/8 | 5,5/8 | **21,5/24** |
| AES PQ | 8/8 | 6/8 | 1/8 | **15/24** |
| AES CE | 7/8 | 7/8 | 1/8 | **15/24** |
| AES CU | 7/8 | 4/8 | 2/8 | **13/24** |
| CLAP lớn, P(punchy) | 6/8 | 3,5/8 | 6,5/8 | **16/24** |
| CLAP lớn, PAM "sạch" | 4,5/8 | 7/8 | 4/8 | **15,5/24** |
| CLAP lớn, giống prompt | 2/8 | 4/8 | 3/8 | **9/24** |
| CLAP nhỏ, P(punchy) | 2/8 | 5/8 | 8/8 | **15/24** |
| CLAP nhỏ, PAM "sạch" | 8/8 | 5/8 | 1/8 | **14/24** |
| CLAP nhỏ, giống prompt | 4/8 | 5/8 | 6/8 | **15/24** |
| AST, độ tự tin nhãn đầu | 4/8 | 3/8 | 6/8 | **13/24** |
| MiDashengLM nói "sạch" | 5/8 | 4/8 | 5/8 | **14/24** |
| MiDashengLM chấm punch 1–10 | 2,5/8 | 2,5/8 | 5,5/8 | **10,5/24** |

Ngẫu nhiên là 12/24. Luật đo cao nhất nhưng "vòng tròn" (cùng người viết luật và bản làm hỏng).

### A.6 Bốn âm mẫu tổng hợp: lớp nào xếp đúng

Cao hơn là tốt hơn ở mọi cột.

| Lớp | Tốt | Yếu | Đục | Clip | Tốt đứng đầu? | Clip đứng cuối? |
|---|---|---|---|---|---|---|
| Luật đo (điểm phạt) | −1 | −4 | −5 | −11 | Có | Có |
| AES PQ | 6,925 | 6,521 | 5,808 | 4,932 | Có | Có |
| AES CE | 3,858 | 2,737 | 3,110 | 2,707 | Có | Có |
| AES CU | 6,547 | 6,632 | 5,899 | 2,999 | Không (bản yếu) | Có |
| CLAP lớn, P(punchy) | 0,981 | 0,000 | 0,810 | 0,077 | Có | Không |
| CLAP lớn, giống prompt | 0,129 | −0,045 | 0,114 | 0,216 | Không (bản clip) | Không |
| CLAP nhỏ, giống prompt | 0,352 | 0,025 | 0,413 | 0,497 | Không (bản clip) | Không |
| AST, độ tự tin nhãn đầu | 0,374 | 0,057 | 0,366 | 0,505 | Không (bản clip) | Không |
| MiDashengLM chấm punch | 3 | 5 | 5 | 10 | Không (bản clip) | Không |

### A.7 Tốc độ và dung lượng (lần chạy đầu, có tải)

| Lớp | Nạp mô hình | Mỗi file | Cache tăng thêm |
|---|---|---|---|
| `analyze.py` (luật đo và ảnh) | — | Khoảng 0,4 s | — |
| audiobox-aesthetics | 17,31 s (2,4 s khi đã có cache) | 0,286 s | 415,5 MB |
| CLAP nhỏ (`clap-htsat-unfused`) | 31,8 s | 0,069 s | Hai bản CLAP cộng lại 2.012,6 MB, vì transformers 5 tải cả `.bin` lẫn `.safetensors` |
| CLAP lớn (`larger_clap_general`) | 40,77 s | 0,036 s | (như trên) |
| AST | 18,28 s | 0,111 s | 1.122,8 MB |
| MiDashengLM-0.6B | 2,9 s (có cache) | 0,42 s mỗi câu hỏi | Khoảng 2,75 GB |

Mọi lớp tự chạy trên MPS.

### A.8 Bản thử 1 (6 âm tổng hợp, 4 âm Kenney UI)

- **audiobox (CE/CU/PC/PQ):** trúng sạch 3,54/6,83/1,77/6,67; bản clip 2,91/6,60/1,78/6,06; bản 250 ms im lặng đầu 3,53/7,27/1,74/7,24; bản đục 3,07/6,22/1,74/6,17; "bíp" sóng sin 2,39/7,35/1,60/**7,37**; nhiễu trắng 2,71/4,45/1,96/5,32. Bốn âm Kenney UI: PQ 7,2–8,07, CE 3,5–4,8.
- **CLAP:** với prompt "punchy explosion", bản clip được 0,19, bản sạch 0,12.
- **AST:** "bíp" thành "Beep, bleep" 0,73; nhiễu thành "Static" 0,55; tiếng trúng tổng hợp thành "Sound effect/Music/Drum machine/Bang".
- **Qwen2.5-Omni-7B Q4_K_M** qua llama.cpp b11669: 13–41 s mỗi lần gọi CLI (mỗi lần nạp lại mô hình). Với prompt dẫn dắt: "không clip, không im lặng, punch 5/5" cho bản clip và bản im lặng đầu; gọi sóng sin là tiếng vũ khí. Với prompt trung tính: đúng tiếng "bíp", gần đúng tiếng nhiễu, gọi tiếng click là "tiếng ù trầm liên tục".
- **LUFS tích hợp không ổn với tiếng ngắn:** cùng một tiếng trúng đo −17,7 LUFS, thêm 250 ms im lặng ở đầu thì thành −15,5 LUFS.
- **Thẻ ảnh** (`scratchpad/card.png`): thấy rõ đỉnh phẳng do clip, đầu tiếng chậm 80 ms, đuôi cụt có tiếng tách.

### A.9 Lệnh chạy lại

```bash
P=/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/ea3cd405-f9d2-442c-a760-74fe0277c6ca/scratchpad/audio-research/poc

# Chạy lại từ đầu: tải uv riêng (kiểm SHA-256), CPython 3.12, thư viện,
# khoảng 2,7 GB trọng số ở lần đầu, và 2 gói Kenney CC0. Không cần tài khoản hay khóa.
# Cần macOS arm64, curl, unzip, khoảng 10 GB ổ trống, có mạng lần đầu.
bash "$P/run_all.sh"

# Chỉ chấm lại, không cần mạng (trọng số đã có trong cache):
cd "$P"
export UV_CACHE_DIR="$P/cache/uv" UV_PYTHON_INSTALL_DIR="$P/cache/python" UV_NO_CONFIG=1
export HF_HOME="$P/cache/hf" HF_HUB_OFFLINE=1 HF_HUB_DISABLE_IMPLICIT_TOKEN=1 \
       HF_HUB_DISABLE_TELEMETRY=1 TOKENIZERS_PARALLELISM=false
unset HF_TOKEN HUGGING_FACE_HUB_TOKEN
.venv/bin/python -I analyze.py samples/synthetic/*.wav samples/cc0_kenney/*.ogg --out out/analyze --profile-map profile_map.json
.venv/bin/python -I analyze.py samples/degraded/*.wav --out out/analyze_degraded --profile impact
.venv/bin/python -I critics.py --manifest manifest.json --out out/critics.json --only aes,clap,ast
.venv/bin/python -I critics.py --manifest manifest_degraded.json --out out/critics_degraded.json --only aes,clap,ast
.venv-tf4/bin/python -I listener.py --manifest manifest.json --out out/listener.json
.venv-tf4/bin/python -I listener.py --manifest manifest_degraded.json --out out/listener_degraded.json
.venv/bin/python -I score_pairs.py > out/pairs.md
.venv/bin/python -I make_tables.py > out/tables.md
```

Ghi chú cho giai đoạn 0:

- `run_all.sh` tải uv bản "latest". Khi chuyển vào `tools/audio-lab`, ghim phiên bản (hoặc dùng uv của Homebrew).
- `run_all.sh` tải trọng số không kèm token, nhưng chưa đặt `HF_HUB_DISABLE_IMPLICIT_TOKEN=1`. Thêm vào.
- Dòng cuối của `run_all.sh` nhắc tới `report.md`, nhưng file này không được tạo. Nội dung của nó chính là phụ lục này.
- Bản thử 1 (`scratchpad/scripts/gen.py`, `score.py`, `sem.py`, `card.py`) không có script chạy lại. Giai đoạn 0 gộp vào `tools/audio-lab`.
- Khi xong, xóa khoảng 15 GB trong scratchpad (`.venv`, `.venv-tf4`, `cache/`, `scratchpad/dl`).

---

## Phụ lục B. Phản biện đã xử lý

| Mức | Vấn đề | Đã sửa ở |
|---|---|---|
| Cao | Điều kiện Stability: đăng ký từ lúc làm, trần tính cả công ty liên kết, AUP, phương án khi không đủ điều kiện | 0, 3.1, 10.1, 15.1 bước 0, 16 |
| Cao | Giọng đọc trùng thời điểm với âm xong từ; hạ trước không cứu được | 4.3.3, 6.1 (bài C), 6.2, 9 |
| Cao | Giọng đọc là `speechSynthesis`, nằm ngoài WebAudio; nhạc nhường giọng là quyết định có chủ ý | 2, 6.1 (bài C), 6.2 bước 4–5, 16 |
| Cao | Bộ biến thể phát hành không được ai nghe; CLAP không đo được độ khác | 5.1 bước 9–10, 5.2, 7 |
| Cao | Hiệu chỉnh chỉ thấy top của máy; mục tiêu 70 %/10 % không đo được; lời hứa ở mục 0 | 0, 4.6, 7 |
| Cao | Không chọn phong cách trước lô 1; L5 không có gì để so; gốc prompt mâu thuẫn bảng âm | 5.2, 4.5, 9, 12 |
| Vừa | Đăng nhập Hugging Face không cần và làm lộ token ngầm | 0, 10.8, 15.1 |
| Vừa | `sfizz_render` không chạy được (x86_64, không Rosetta, không cmake); FluidSynth cần SF2 | 3.1 B, 3.4, 12 (giai đoạn 6 thêm 0,5 ngày) |
| Vừa | Sonniss tự mâu thuẫn; thẻ ảnh gửi Claude; Codex dùng phiên của chủ dự án | 3.2, 3.3, 10.2, 10.3 |
| Vừa | Công sức, thời gian chủ dự án, ổ đĩa bị ước thấp; đụng làn cân bằng | 0, 2, 7, 11, 12, 15 |
| Vừa | Thiếu bước của chủ dự án: admin, cmake/Rosetta, email, chấp nhận giấy phép, giấy đồng ý ghi âm, dịch vụ online | 10.4, 15.1 |
| Vừa | Lớp học máy phạt âm bẩn có chủ ý | 4.1, 4.4, 4.5 |
| Vừa | Lớp ngữ nghĩa sai với âm ngắn; chỉ báo phần đúng | 4.1, 4.2, 4.4 |
| Vừa | Ngưỡng chung thành cổng cứng, chặn nhầm âm tốt | 4.3.1, 4.3.3 |
| Vừa | Cổng chạy sau khi sửa nên không thấy clip trong file gốc | 4.3.1, 5.1 bước 3 |
| Vừa | Không dò lỗi riêng của âm do mô hình tạo | 4.3.2, 4.6 (lô 0b) |
| Vừa | Negative prompt vô tác dụng khi CFG mặc định; chỉ ra stereo; âm ngắn; mô hình không nằm sẵn | 5.1 bước 2–4 |
| Vừa | Nướng bậc trúng vào file làm phẳng các tầng của Tuyến Cuối | 6.3 mục 3, 6.1 (bài I), 8.3, 9 |
| Vừa | Bài mỏi tai thiếu âm theo từ và độ dài trận; thưởng theo từ bị cấm đổi | 5.3, 6.1 (bài E) |
| Vừa | Chấm trong trận trên nhạc tạm; không có bản đồ vai trò tần số | 6.1, 6.4, 12 |
| Vừa | Đàn tranh VCSL không phủ quãng `word-hit`; chuông Nepal trái luật | 3.2, 8.2, 9, 16 |
| Vừa | Thời gian chủ dự án bị ước thấp | 0, 7, 15.1 |
| Thấp | Bỏ ngoại lệ chạy mô hình phi thương mại để so | 3.5, 10.2 |
| Thấp | Chuỗi cung ứng khi cài | 10.8 |
| Thấp | `.gitignore` không đưa lại được `manifest.json` | 11 |
| Thấp | Freesound: điều khoản API, tùy chọn AI | 3.4, 10.2, 10.6 |
| Thấp | Nhãn giấy phép GGUF của Qwen | 3.1 C, 10.2 |
| Thấp | pedalboard GPL trong repo không có `LICENSE` | 10.9 |
| Thấp | Mức to đặt ở hai nơi | 4.3.3, 11 (manifest v2) |
| Thấp | Âm có Sonniss không so được với luồng khác | 10.2 |
| Thấp | Cặp mốc quá ít, chưa lên lịch người chơi thử, loa nhỏ là phép thử yếu | 4.6, 6.1 (bài F), 12, 15.1 |
| Thấp | Mâu thuẫn trong tài liệu game: `general` D minor, `amb.forest` 6 s, bẫy nổ | 3.2, 6.1 (bài J), 8.1, 9, 16 |

---

## Nguồn

**Bằng chứng trên máy:**

- Bản thử 1 ("tai AI"): `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/ea3cd405-f9d2-442c-a760-74fe0277c6ca/scratchpad/scripts/` và `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/ea3cd405-f9d2-442c-a760-74fe0277c6ca/scratchpad/card.png`
- Bản thử 2 (40 âm): `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/ea3cd405-f9d2-442c-a760-74fe0277c6ca/scratchpad/audio-research/poc/`. Gồm `gen_samples.py`, `degrade.py`, `analyze.py`, `critics.py`, `listener.py`, `score_pairs.py`, `make_tables.py`, `run_all.sh`, `samples/LICENSES.md`, `out/tables.md`, `out/pairs.md`.
- Kiểm máy ngày 23/10/2026: `arch -x86_64 /usr/bin/true` báo "Bad CPU type" (không có Rosetta); không có `cmake`, `ffmpeg`, `uv`, `sox`; ổ còn 81 GiB.
- Mã của dự án:
  - `/Users/toandx/htdocs/typing-game/shared/game-kit/audio/scene-audio.ts`
  - `/Users/toandx/htdocs/typing-game/shared/game-kit/feedback/audio-cues.ts`
  - `/Users/toandx/htdocs/typing-game/shared/game-kit/speech/speech.ts`
  - `/Users/toandx/htdocs/typing-game/games/dragon-hold/src/app/learning.ts`
  - `/Users/toandx/htdocs/typing-game/games/dragon-hold/src/audio/bank.ts`
  - `/Users/toandx/htdocs/typing-game/games/dragon-hold/src/audio/catalog.ts`
  - `/Users/toandx/htdocs/typing-game/games/dragon-hold/src/audio/dev/harness.ts`
  - `/Users/toandx/htdocs/typing-game/games/typing-survival/src/audio/theme-audio.ts`
  - `/Users/toandx/htdocs/typing-game/games/typing-survival/src/kit/feedback/tiers.ts`
  - `/Users/toandx/htdocs/typing-game/games/typing-defense/src/view/audio-min.ts`
  - `/Users/toandx/htdocs/typing-game/games/typing-defense/.gitignore`
  - `/Users/toandx/htdocs/typing-game/media/media.config.json`
- Danh sách âm:
  - `/Users/toandx/htdocs/typing-game/games/dragon-hold/docs/audio/M0_SOUND_LIST.md`
  - `/Users/toandx/htdocs/typing-game/games/typing-defense/docs/audio/THEME_SOUND_LIST.md`
  - `/Users/toandx/htdocs/typing-game/games/typing-survival/docs/audio/THEME_SOUND_LIST.md`

**Nguồn trên web** (đọc ngày 23/10/2026):

- [1] https://github.com/Stability-AI/stable-audio-3
- [2] https://raw.githubusercontent.com/Stability-AI/stable-audio-3/main/optimized/mlx/README.md (đọc lại ngày 23/10/2026: cờ `--cfg` mặc định 1,0 là tắt; `--negative-prompt` chỉ có tác dụng khi `--cfg` khác 1,0; đầu ra PCM 16-bit stereo 44,1 kHz; `--no-free-models`; Gradio mặc định chia sẻ công khai)
- [3] https://huggingface.co/stabilityai/stable-audio-3-small-sfx
- [4] https://stability.ai/community-license-agreement (đọc lại ngày 23/10/2026; cập nhật lần cuối 5/7/2024)
- [5] https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models
- [6] https://github.com/ACE-Step/ACE-Step-1.5
- [7] https://huggingface.co/ACE-Step/Ace-Step1.5
- [8] https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect-v2.0 ; https://github.com/OpenMOSS/MOSS-TTS
- [9] https://github.com/magenta/magenta-realtime
- [10] https://github.com/facebookresearch/audiocraft/blob/main/LICENSE_weights
- [11] https://github.com/hkchengrex/MMAudio
- [12] https://github.com/SonyResearch/Woosh
- [13] https://huggingface.co/declare-lab/TangoFlux
- [14] https://github.com/ZeyueT/AudioX
- [15] https://github.com/facebookresearch/audiobox-aesthetics ; https://arxiv.org/abs/2502.05139
- [16] https://huggingface.co/laion/larger_clap_general ; https://huggingface.co/laion/clap-htsat-unfused ; https://github.com/LAION-AI/CLAP
- [17] https://arxiv.org/pdf/2506.23582
- [18] https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593
- [19] https://github.com/Eomys/MoSQITo
- [20] https://github.com/csteinmetz1/pyloudnorm
- [21] https://ffmpeg.org/ffmpeg-filters.html
- [22] https://github.com/YoonjinXD/kadtk ; https://github.com/microsoft/fadtk
- [23] https://huggingface.co/Qwen/Qwen2.5-Omni-7B ; https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md
- [24] https://huggingface.co/Qwen/Qwen2.5-Omni-3B/resolve/main/LICENSE
- [25] https://huggingface.co/nvidia/audio-flamingo-3-hf
- [26] https://huggingface.co/ggml-org/Qwen3-Omni-30B-A3B-Instruct-GGUF
- [27] https://huggingface.co/mispeech/midashenglm-0.6b-fp32
- [28] https://arxiv.org/html/2512.18099
- [29] https://arxiv.org/abs/2507.12705
- [30] https://ai.google.dev/gemini-api/docs/audio ; https://ai.google.dev/gemini-api/docs/pricing ; https://ai.google.dev/gemini-api/terms
- [31] https://geminicli.com/docs/resources/quota-and-pricing/
- [32] https://developers.openai.com/codex/cli/reference.md
- [33] https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/
- [34] https://elevenlabs.io/pricing ; https://elevenlabs.io/docs/help-center/legal/can-i-publish-the-content-i-generate-on-the-platform ; https://elevenlabs.io/sound-effects/commercial ; https://elevenlabs.io/docs/overview/capabilities/sound-effects
- [35] https://suno.com/pricing
- [36] https://www.digitalmusicnews.com/2025/10/31/udio-downloads-disabled-umg-deal/
- [37] https://artificialanalysis.ai/music/leaderboard/instrumental
- [38] https://support.google.com/googleone/answer/16882689?hl=en ; https://en.baobacninhtv.vn/google-launches-ai-service-package-in-vietnam-for-5-postid427355.bbg
- [39] https://sonniss.com/gdc-bundle-license/ ; https://sonniss.com/gameaudiogdc ; https://gdc.sonniss.com/ (v2.0, hiệu lực 27/8/2026)
- [40] https://kenney.nl/assets/category:Audio ; https://www.kenney.nl/support
- [41] https://freesound.org/help/tos_api/ ; https://freesound.org/docs/api/resources_apiv2.html ; https://freesound.org/docs/api/authentication.html
- [42] https://github.com/sgossner/VCSL
- [43] https://github.com/sgossner/VSCO-2-CE
- [44] https://sfz.tools/sfizz/ ; https://formulae.brew.sh/api/formula/fluid-synth.json
- [45] https://github.com/spotify/pedalboard
- [46] https://surge-synthesizer.github.io/ ; https://www.airwindows.com/
- [47] https://github.com/ircam-ismm/node-web-audio-api
- [48] https://faustlibraries.grame.fr/libs/physmodels/
- [49] https://sound-effects.bbcrewind.co.uk/ ; https://pixabay.com/service/terms/ ; https://mixkit.co/license/
- [50] https://99sounds.org/license/
- [51] https://www.audiogang.org/wp-content/uploads/2015/04/IESD-Mix-Ref-Levels-v03.02.pdf
- [52] https://eprints.gla.ac.uk/104653
- [53] https://rdrr.io/rforge/SII/man/critical.html ; https://repository.tno.nl/SingleDoc?docId=8673
- [54] https://www.adsrsounds.com/news/the-sound-design-of-doom-exclusive-qa/ ; https://sifter.com.au/post/the-ingredients-of-doom-composer-mick-gordon-on-the-soundtrack-of-doom-eternal
- [55] https://80.lv/articles/interview-with-the-developers-of-dead-cells ; https://sourcegaming.info/2015/11/11/thoughts-on-hitstop-sakurais-famitsu-column-vol-490-1/
- [56] https://www.leagueoflegends.com/en-gb/news/dev/clarity-in-league/ ; https://www.pcgamesn.com/overwatch/overwatch-devs-on-creating-a-game-you-can-play-by-sound-and-announcing-dolby-atmos-support
- [57] https://dev.epicgames.com/documentation/unreal-engine/sound-concurrency-reference-guide ; https://docs.unity3d.com/Manual/AudioRandomContainer-UI.html
- [58] https://raw.githubusercontent.com/monkeytypegame/monkeytype/master/frontend/src/ts/constants/sounds.ts
- [59] https://vvise.iat.sfu.ca/pubs/batmaz2021pitch
- [60] https://en.wikipedia.org/wiki/S%C3%A1o_tr%C3%BAc ; https://en.wikipedia.org/wiki/%C4%90%C3%A0n_tranh ; https://en.wikipedia.org/wiki/Tr%E1%BB%91ng_c%C6%A1m ; https://ich.unesco.org/en/RL/space-of-gong-culture-00120
- [61] https://www.cbc.ca/lite/story/1.5147762 ; https://www.npr.org/transcripts/321952974
- [62] https://caniuse.com/ogg-vorbis ; https://caniuse.com/opus
- [63] https://pypi.org/project/choix/
- [64] https://en.wikipedia.org/wiki/Vampire_Survivors
- [65] https://pure.hud.ac.uk/en/publications/a-perceptual-model-of-punch-based-on-weighted-transient-loudness/
- [66] https://huggingface.co/thepatch/foundation-1-GGUF
- [67] https://huggingface.co/docs/hub/spaces-zerogpu
- [68] https://docs.stability.ai/pricing
- [69] https://huggingface.co/cvssp/audioldm2
- [70] https://github.com/FunAudioLLM/ThinkSound
- [71] https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley
- [72] https://github.com/multimodal-art-projection/YuE
- [73] https://essentia.upf.edu/models.html
- [74] https://fal.ai/models/fal-ai/elevenlabs/sound-effects/v2
- [75] https://huggingface.co/api/models/stabilityai/stable-audio-3-optimized (đọc ngày 23/10/2026: `gated: false`, giấy phép `stable-audio-community`, có các file `MLX/dit_sm-sfx_f16.npz`, `MLX/t5gemma_f16.npz` và bản `-base` cho LoRA)
- [76] https://raw.githubusercontent.com/Stability-AI/stable-audio-3/main/optimized/mlx/install.sh
- [77] https://raw.githubusercontent.com/Stability-AI/stable-audio-3/main/optimized/mlx/scripts/weights.py
- [78] https://github.com/sfztools/sfizz/releases (bản mới nhất 1.2.3, 14/1/2024; người phản biện đã mở gói macOS trong thư mục tạm: `sfizz_render` là Mach-O x86_64, không ký)
- [79] https://formulae.brew.sh/api/cask/surge-xt.json
- [80] https://blog.freesound.org/?p=2417
- [81] https://huggingface.co/api/models/ggml-org/Qwen2.5-Omni-7B-GGUF
- [82] https://huggingface.co/Qwen/Qwen2.5-Omni-7B/resolve/main/LICENSE
- [83] https://github.com/sgossner/VCSL/tree/master/Chordophones/Zithers/Dan%20Tranh/Normal (đọc ngày 23/10/2026: các nốt B1–B4 thuộc C#, D#, F#, G#, B; thư mục cha có Normal, Gliss, Tremolo, Vibrato, FX)
- [84] https://github.com/sgossner/VCSL/tree/master/Idiophones/Struck%20Idiophones (đọc ngày 23/10/2026: có Anvil, Brake Drum, Gong 1, Gong 2, Hand Bells Nepalese, Hand Chimes, Slit Drum, Tubular Bells 1–2, Woodblock)
- [85] https://github.com/sgossner/VSCO-2-CE/tree/master/Strings ; https://github.com/sgossner/VSCO-2-CE/tree/master/Woodwinds ; https://github.com/sgossner/VSCO-2-CE/tree/master/Brass (đọc ngày 23/10/2026: Cello Section, Harp, Flute, F Horn, Trumpet, Trombone, Tuba)
- [86] https://ai.google.dev/gemma/terms
- [87] https://huggingface.co/api/models/ACE-Step/Ace-Step1.5
- [88] https://pypi.org/project/mido/
- [89] https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisUtterance/end_event
- [90] https://formulae.brew.sh/api/formula/rubberband.json

[s1]: https://github.com/Stability-AI/stable-audio-3
[s2]: https://raw.githubusercontent.com/Stability-AI/stable-audio-3/main/optimized/mlx/README.md
[s3]: https://huggingface.co/stabilityai/stable-audio-3-small-sfx
[s4]: https://stability.ai/community-license-agreement
[s5]: https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models
[s6]: https://github.com/ACE-Step/ACE-Step-1.5
[s7]: https://huggingface.co/ACE-Step/Ace-Step1.5
[s8]: https://huggingface.co/OpenMOSS-Team/MOSS-SoundEffect-v2.0
[s9]: https://github.com/magenta/magenta-realtime
[s10]: https://github.com/facebookresearch/audiocraft/blob/main/LICENSE_weights
[s11]: https://github.com/hkchengrex/MMAudio
[s12]: https://github.com/SonyResearch/Woosh
[s13]: https://huggingface.co/declare-lab/TangoFlux
[s14]: https://github.com/ZeyueT/AudioX
[s15]: https://github.com/facebookresearch/audiobox-aesthetics
[s16]: https://huggingface.co/laion/larger_clap_general
[s17]: https://arxiv.org/pdf/2506.23582
[s18]: https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593
[s19]: https://github.com/Eomys/MoSQITo
[s20]: https://github.com/csteinmetz1/pyloudnorm
[s21]: https://ffmpeg.org/ffmpeg-filters.html
[s22]: https://github.com/YoonjinXD/kadtk
[s23]: https://huggingface.co/Qwen/Qwen2.5-Omni-7B
[s24]: https://huggingface.co/Qwen/Qwen2.5-Omni-3B/resolve/main/LICENSE
[s25]: https://huggingface.co/nvidia/audio-flamingo-3-hf
[s26]: https://huggingface.co/ggml-org/Qwen3-Omni-30B-A3B-Instruct-GGUF
[s27]: https://huggingface.co/mispeech/midashenglm-0.6b-fp32
[s28]: https://arxiv.org/html/2512.18099
[s29]: https://arxiv.org/abs/2507.12705
[s30]: https://ai.google.dev/gemini-api/docs/audio
[s31]: https://geminicli.com/docs/resources/quota-and-pricing/
[s32]: https://developers.openai.com/codex/cli/reference.md
[s33]: https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/
[s34]: https://elevenlabs.io/pricing
[s35]: https://suno.com/pricing
[s36]: https://www.digitalmusicnews.com/2025/10/31/udio-downloads-disabled-umg-deal/
[s37]: https://artificialanalysis.ai/music/leaderboard/instrumental
[s38]: https://support.google.com/googleone/answer/16882689?hl=en
[s39]: https://sonniss.com/gdc-bundle-license/
[s40]: https://kenney.nl/assets/category:Audio
[s41]: https://freesound.org/help/tos_api/
[s42]: https://github.com/sgossner/VCSL
[s43]: https://github.com/sgossner/VSCO-2-CE
[s44]: https://sfz.tools/sfizz/
[s45]: https://github.com/spotify/pedalboard
[s46]: https://surge-synthesizer.github.io/
[s47]: https://github.com/ircam-ismm/node-web-audio-api
[s48]: https://faustlibraries.grame.fr/libs/physmodels/
[s49]: https://sound-effects.bbcrewind.co.uk/
[s50]: https://99sounds.org/license/
[s51]: https://www.audiogang.org/wp-content/uploads/2015/04/IESD-Mix-Ref-Levels-v03.02.pdf
[s52]: https://eprints.gla.ac.uk/104653
[s53]: https://rdrr.io/rforge/SII/man/critical.html
[s54]: https://www.adsrsounds.com/news/the-sound-design-of-doom-exclusive-qa/
[s55]: https://80.lv/articles/interview-with-the-developers-of-dead-cells
[s56]: https://www.leagueoflegends.com/en-gb/news/dev/clarity-in-league/
[s57]: https://dev.epicgames.com/documentation/unreal-engine/sound-concurrency-reference-guide
[s58]: https://raw.githubusercontent.com/monkeytypegame/monkeytype/master/frontend/src/ts/constants/sounds.ts
[s59]: https://vvise.iat.sfu.ca/pubs/batmaz2021pitch
[s60]: https://en.wikipedia.org/wiki/S%C3%A1o_tr%C3%BAc
[s61]: https://www.cbc.ca/lite/story/1.5147762
[s62]: https://caniuse.com/ogg-vorbis
[s63]: https://pypi.org/project/choix/
[s64]: https://en.wikipedia.org/wiki/Vampire_Survivors
[s65]: https://pure.hud.ac.uk/en/publications/a-perceptual-model-of-punch-based-on-weighted-transient-loudness/
[s66]: https://huggingface.co/thepatch/foundation-1-GGUF
[s67]: https://huggingface.co/docs/hub/spaces-zerogpu
[s68]: https://docs.stability.ai/pricing
[s69]: https://huggingface.co/cvssp/audioldm2
[s70]: https://github.com/FunAudioLLM/ThinkSound
[s71]: https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley
[s72]: https://github.com/multimodal-art-projection/YuE
[s73]: https://essentia.upf.edu/models.html
[s74]: https://fal.ai/models/fal-ai/elevenlabs/sound-effects/v2
[s75]: https://huggingface.co/api/models/stabilityai/stable-audio-3-optimized
[s76]: https://raw.githubusercontent.com/Stability-AI/stable-audio-3/main/optimized/mlx/install.sh
[s77]: https://raw.githubusercontent.com/Stability-AI/stable-audio-3/main/optimized/mlx/scripts/weights.py
[s78]: https://github.com/sfztools/sfizz/releases
[s79]: https://formulae.brew.sh/api/cask/surge-xt.json
[s80]: https://blog.freesound.org/?p=2417
[s81]: https://huggingface.co/api/models/ggml-org/Qwen2.5-Omni-7B-GGUF
[s82]: https://huggingface.co/Qwen/Qwen2.5-Omni-7B/resolve/main/LICENSE
[s83]: https://github.com/sgossner/VCSL/tree/master/Chordophones/Zithers/Dan%20Tranh/Normal
[s84]: https://github.com/sgossner/VCSL/tree/master/Idiophones/Struck%20Idiophones
[s85]: https://github.com/sgossner/VSCO-2-CE/tree/master/Strings
[s86]: https://ai.google.dev/gemma/terms
[s87]: https://huggingface.co/api/models/ACE-Step/Ace-Step1.5
[s88]: https://pypi.org/project/mido/
[s89]: https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisUtterance/end_event
[s90]: https://formulae.brew.sh/api/formula/rubberband.json
