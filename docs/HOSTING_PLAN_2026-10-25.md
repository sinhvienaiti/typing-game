# Đưa các game lên mạng: dung lượng thật và Cloudflare Free (25/10/2026)

> **Câu hỏi của chủ dự án (25/10):** game nào cũng nặng, sau này tách riêng từng game; gói Free hay gói 5 USD của Cloudflare có đủ chỗ cho source và ảnh không?
>
> **Trả lời ngắn: về dung lượng thì đủ.** Theo tài liệu Cloudflare hiện tại, gói Free đủ chỗ cho file của 5 game chiến đấu và portal. Gói 5 USD không cần cho phần file.
> 1. **Source không đưa lên Cloudflare.** Source ở GitHub, miễn phí.
> 2. **Phần nặng nhất không bao giờ lên mạng:** ảnh gốc `art-src`, bằng chứng `tmp`, nhạc riêng; tổng khoảng 11.800 MiB.
> 3. **Phần thật sự phục vụ người chơi chỉ khoảng 680 MiB**, và Cloudflare không ghi giới hạn tổng dung lượng file tĩnh.
> 4. **Gói 5 USD chỉ cần cho backend online** (tài khoản, chat, đấu đôi, phòng đội), khi tải vượt hạn mức (mục 3).
>
> **Cái khó nằm ở mã, không ở dung lượng.** Mọi game ghi cứng địa chỉ portal của máy nhà, nên muốn chạy online phải sửa mã (mục 6).
>
> **Nguồn:**
> - Đo trên ổ D: máy Dell ngày 25/10.
> - Giới hạn Cloudflare đọc trên trang chính thức ngày 25/10 (phần lớn cập nhật tháng 8–10/2026).
> - Hai agent độc lập đã phản biện bản nháp:
>   - một agent đối chiếu số và giá với trang chính thức: không có số Cloudflare nào sai;
>   - một agent đối chiếu kiến trúc với mã: tìm ra nhiều chỗ thiếu, đã sửa trong bản này.
> - Đường dẫn và dòng mã trích ở mục 8.

## 1. Dung lượng thật của từng game (MiB)

"Phục vụ" là thư mục `dist` sau khi build, gồm cả media trong `public/assets`.

| Game | Phục vụ người chơi | Số file | File lớn nhất | Source trong Git | Không bao giờ lên mạng |
|---|---:|---:|---:|---:|---|
| Space Typing | 591,3 | 1.731 | 12,0 (`tyrant-g01.glb`, có vẻ không dùng) | 283,7 (268,4 là media **đang dùng**) | `art-src` 6.426 |
| Rồng Giữ Ải | 17,6 | 47 | 4,2 | 2,6 | `art-src` 176; `tmp` 2.246 |
| Lời Gọi | 19,8 | 110 | 1,2 | 3,3 | `art-src` 545; `tmp` 1.127 |
| Tuyến Cuối | 1,3 (+ 359,8 model mượn của Space) | 45 | — | 1,6 | `tmp` 676 |
| Tu Tiên Thủ Ải | 1,2 (chưa có media) | 38 | — | 1,8 | `art-src` 125 |
| Portal | 47,4 | 149 | **39,2** (mô hình giọng Vosk) | 16,2 file hiện có (repo cha) | `shared/music` 457 (nhạc riêng) |
| **Cộng** | **≈ 680 (≈ 0,7 GB)** | | | | **≈ 11.800 (≈ 12 GB)** |

**Ghi chú:**
- **Tuyến Cuối nạp thư viện model của Space** (379 file, 359,8 MiB) qua alias nginx `/assets/space-typing/models/`. Tu Tiên cũng có sẵn alias này trong nginx, nhưng mã của Tu Tiên chưa nạp model nào của Space.
- **Media của Space nằm trong Git (268,4 MiB):** nền, nhạc, 19 GLB. Build vẫn cần chúng; chúng được commit trước khi có quy tắc "media không vào Git". **Đừng xóa.**
- **Cỡ `dist` của Space phụ thuộc máy build có đủ media từ Drive hay không:**
  - gói deploy 20/10: 315,6 MiB (gồm cả thư mục dùng chung);
  - `dist` khi rà soát 21/10: 681 MB;
  - Dell 24/10: 591,3 MiB.
  - Mọi bước kiểm kích cỡ của Space chỉ báo cáo, không chặn.
- **Tu Tiên khi có đủ hình:** theo phiếu ảnh hiện tại là 19 GLB, khoảng 70 ảnh 2D chạy trong game (WebP), cộng âm Opus. Ước 50–100 MiB; chưa đo.
- **Portal còn 4 game luyện gõ chưa đo** (Monkeytype, Vocabulary Shooter, Recall, Karaoke). Xem mục 6, bước 0.

## 2. Cloudflare Free cho gì (đã kiểm 25/10/2026)

| Mảng | Gói Free | Gói Workers Paid 5 USD/tháng |
|---|---|---|
| **File tĩnh của game** (Workers Static Assets) | Tài liệu **không ghi giới hạn tổng dung lượng**. Lưu không mất tiền. Lượt tải file tĩnh **miễn phí, không giới hạn**. Mỗi bản deploy tối đa **20.000 file**, mỗi file tối đa **25 MiB** | 100.000 file mỗi bản deploy; **vẫn 25 MiB** mỗi file |
| Số Worker | 100 mỗi tài khoản: mỗi game một Worker, mỗi game có quỹ 20.000 file riêng | 500 |
| Lượt chạy mã Worker (API, chat, phòng đội) | **100.000 lượt/ngày cho cả tài khoản**, mọi Worker dùng chung; 10 ms CPU mỗi lượt | 10 triệu lượt/tháng, sau đó 0,30 USD mỗi triệu |
| D1 (cơ sở dữ liệu) | Tối đa 10 cơ sở dữ liệu, **mỗi cái 500 MB** (5 GB cả tài khoản; Space dùng 1 cái); 5 triệu dòng đọc, 100.000 dòng ghi mỗi ngày | 10 GB mỗi cái; 25 tỷ dòng đọc, 50 triệu dòng ghi mỗi tháng |
| Durable Objects (phòng chơi đội) | 100.000 lượt/ngày; 13.000 GB-giây/ngày | Tính theo dùng |
| Bộ đệm CDN | File tới 512 MB. Mặc định **không đệm** `.glb`, `.ktx2`, `.json`, `.wav`, `.m4a`, `.opus`; cần Cache Rule (Free có 10) | Như Free |

**R2 (kho file lớn) tính tiền riêng**, không thuộc gói 5 USD, dù tài khoản ở gói nào:
- Miễn phí mỗi tháng: 10 GB lưu, 1 triệu thao tác loại A (ghi, liệt kê), 10 triệu thao tác loại B (đọc). Tải ra không mất tiền.
- Vượt thì tính: 0,015 USD/GB-tháng; 4,50 USD mỗi triệu loại A; 0,36 USD mỗi triệu loại B.
- File đã nằm trong bộ đệm CDN thì không đọc lại R2, nên không tốn lượt loại B.

**Điều khoản dùng (bản 28/09/2026):**
- Điều khoản CDN bắt khách không phải Enterprise dùng "Paid Services (ví dụ Developer Platform, Images, Stream)" để phục vụ video và file lớn.
- Điều khoản Developer Platform (gồm Workers, Pages, R2) ghi nền tảng này "được dùng để lưu nội dung".
- Vì vậy ảnh, âm, GLB phục vụ từ **Workers, Pages hoặc R2** là đường điều khoản chỉ định.
  - Điều khoản không nói rõ dùng ở mức miễn phí có được tính là "Paid Service" không.
  - Đây là cách hiểu hợp lý nhất, không phải lời xác nhận của Cloudflare.
- **Đường rủi ro:** để file lớn ở nơi khác (Google Drive, Backblaze, máy riêng) rồi cho đi qua CDN Free. **Không làm cách đó.**
- Điều khoản Developer Platform vẫn cho Cloudflare quyền tạm giới hạn dung lượng hoặc số lượt.

**Lưu ý đã kiểm:**
- **Lượt tải file tĩnh gần như chắc không trừ vào 100.000 lượt/ngày.**
  - Trang giá Pages ghi rõ chỉ lượt chạy mã mới bị trừ; ví dụ tính tiền của Workers cũng không tính lượt file tĩnh.
  - Ngoại lệ: đường dẫn khớp `run_worker_first`, hoặc không khớp file nào khi Worker có mã, thì vẫn chạy Worker và bị trừ.
  - Đo lại trên dashboard sau lần deploy đầu.
- **Không bật "Workers Cache"** (tùy chọn mới). Khi bật, mọi lượt tải file tĩnh bị tính như lượt chạy Worker.
- **Bật R2 cần phương thức thanh toán hợp lệ:** thẻ Visa/Mastercard, PayPal, Apple Pay hoặc Google Pay; thẻ trả trước có thể bị từ chối.
  - R2 **không có trần chi tiêu**: vượt hạn mức là tự trừ tiền hằng tháng.
  - Thanh toán lỗi thì bucket ngừng phục vụ; không sửa trong 30 ngày thì dữ liệu có thể bị xóa.
- **Tên miền riêng cho R2** (ví dụ `media.<tên-miền>`) phải là zone dùng nameserver của Cloudflare. Địa chỉ `r2.dev` chỉ để thử: bị giới hạn tốc độ, không có bộ đệm.
- **Phục vụ R2 qua mã Worker thì mỗi file là một lượt Worker.** Chỉ chấp nhận được cho file tải ít lần, như mô hình giọng (mục 6).

## 3. Vì sao không thiếu chỗ, và khi nào cần 5 USD

1. **Source ở GitHub, không ở Cloudflare.**
   - Repo các game dưới 5 MB. Repo cha khoảng 28 MB lịch sử Git; thư mục `.git` trên Dell đang 360 MB vì có 250 MB file tạm hỏng và thư mục `cursor`, dọn được.
   - Repo Space khoảng 320 MiB, dưới mức GitHub khuyên (dưới 1 GB, rất nên dưới 5 GB).
   - Không cần Git LFS: LFS chỉ miễn phí 10 GiB lưu và 10 GiB tải mỗi tháng, sau đó tính 0,0875 USD/GiB. Mỗi lần clone trên Mac hay Dell đều trừ vào hạn mức này.
2. **Ảnh gốc, bằng chứng và nhạc riêng không lên mạng.**
   - Ảnh gốc `art-src` và nhạc riêng nằm trên máy và bản sao lưu Google Drive (`pnpm media:push`).
   - **Thư mục bằng chứng `tmp` (khoảng 4 GB) chỉ nằm trên máy, không được sao lưu.**
3. **Phần phục vụ dưới 1 GB, Cloudflare không ghi giới hạn tổng.**
   - Giới hạn thật là số file và cỡ một file. Space có 1.731 file, còn xa mức 20.000; file lớn nhất 12 MiB, dưới mức 25 MiB.
   - Mỗi game một Worker thì mỗi game có quỹ 20.000 file riêng; tách game càng nhiều thì quỹ càng rộng.
4. **Chỉ có 1 file vượt 25 MiB:** mô hình giọng 39,2 MiB của portal. Xem mục 6, bước 1.

**Khi nào mới cần gói 5 USD** (chỉ do backend):
- **Một trong các điều sau xảy ra:**
  - vượt 100.000 lượt chạy Worker hoặc 100.000 dòng ghi D1 trong ngày;
  - cơ sở dữ liệu gần 500 MB;
  - bản lưu thường xuyên trên 150 KB (vượt 10 ms CPU mỗi lượt);
  - phòng chơi dùng hết 13.000 GB-giây/ngày của Durable Objects.
- **Ước tính của tài liệu online Space** (chưa đo tải thật):
  - gói Free đủ cho khoảng **800 người chơi mỗi ngày** khi đã bật ví, mỗi người 30 phút có đăng nhập;
  - giới hạn chạm trước là 100.000 dòng ghi D1 mỗi ngày;
  - hạn mức tính cho cả tài khoản, nên mở thêm đấu đôi hay phòng đội Tu Tiên thì số này thấp xuống.
- **Cloudflare không có cảnh báo 70 % sẵn cho gói Free.** D1 chỉ gửi email khi đã chạm hạn mức. Phải tự xem dashboard hoặc viết script đọc số liệu qua API.
- **Phần file của game không cần gói 5 USD**, trừ khi một game vượt 20.000 file. Gói 5 USD cũng không nâng mức 25 MiB mỗi file. Điều kiện:
  - không bật Workers Cache;
  - không đặt `run_worker_first` cho mọi đường dẫn;
  - Cloudflare không đổi điều khoản.

## 4. Kiến trúc đề xuất

```text
GitHub (miễn phí)            source của repo cha và từng game; không LFS
Máy Dell / Mac               build sau khi `pnpm media:pull` (CI không có media)
Google Drive (rclone)        chỉ sao lưu; KHÔNG bao giờ phục vụ người chơi

Cloudflare (Free)
  <tên-miền>                 Worker portal: file tĩnh, games.json thật, /vocabulary/, /typing-texts/;
                             bản build không có mục Space Admin; /assets/voice/<id>.tar.gz đọc từ R2
  space.<tên-miền>           MỘT Worker `space-typing-api`: file tĩnh + API tài khoản và chat
                             (cùng nguồn vì cookie và CSRF cần vậy); D1, Durable Object chat
  dragon. / td. / survival. / tutien.<tên-miền>
                             mỗi game một Worker chỉ có file tĩnh, media đi kèm, cùng nguồn
                             (survival kèm bản chép thư viện model của Space)
  R2 (không tên miền riêng lúc đầu)  mô hình giọng 39 MB; sau này media quá 25 MiB hoặc dùng chung
```

- **Media đi kèm Worker của từng game, cùng nguồn.**
  - Không cần CORS, không cần sửa đường media trong mã.
  - Lưu file tĩnh không mất tiền, nên chép thư viện model của Space (359,8 MiB, 379 file) vào gói deploy của Tuyến Cuối, đúng đường cũ, là cách không sửa mã.
- **Chỉ dùng một tên miền media chung (`media.<tên-miền>` trên R2) khi thật cần**, ví dụ khi nhiều game dùng chung model lớn. Khi đó phải sửa mã:
  - biến gốc media;
  - khoảng 208 chuỗi `"/assets/…"` cứng trong Space;
  - `crossOrigin` cho nhạc đi qua WebAudio và cho ảnh có đọc pixel;
  - manifest ghi URL `https://` đầy đủ; công cụ model hiện từ chối URL loại này.
- **Space: một Worker cho cả file tĩnh và API.** `run_worker_first` chỉ gồm `/api/account/*`, `/internal/admin/*`, `/healthz`, **không** dùng `/api/*`. Nếu dùng `/api/*`, mỗi lần mở Space tốn thêm khoảng 8 lượt Worker vô ích, vì Space gọi API runtime của Admin mà bản online không có.
- **Không cần Pages.** Cloudflare khuyên dự án mới dùng Workers Static Assets. Pages chỉ hơn ở chỗ tên miền **con** không cần nameserver ở Cloudflare; tên miền gốc (chỗ đặt portal) vẫn phải đặt ở Cloudflare, nên với sơ đồ này Pages không có lợi gì.

## 5. So với chỗ khác

Giả định mỗi người chơi tải 60 MB mỗi tháng (chưa đo). Người chơi nhiều màn của Space có thể tải gấp vài lần; khi đó các nơi tính tiền theo GB tăng theo cùng tỉ lệ.

| Nơi phục vụ media | 1.000 người/tháng | 10.000 | 100.000 | Ghi chú |
|---|---:|---:|---:|---|
| **Cloudflare Workers (+ R2 cho file lớn)** | **0 USD** | **0 USD** | **0 USD** | Đường đề xuất. Cộng 5 USD nếu backend vượt hạn mức |
| Backblaze B2 + Bunny CDN | ~2 USD | ~18 USD | ~180 USD | Giá vùng châu Á. Mạng Volume rẻ hơn, nhưng chỉ 10 điểm, chưa rõ có phủ Việt Nam. Dự phòng nếu Cloudflare đổi điều khoản |
| GitHub Pages | 0 USD | không được | không được | Trang tối đa 1 GB; lưu lượng mềm 100 GB/tháng; không cho dùng làm hosting miễn phí cho kinh doanh online |
| Firebase (Blaze) | ~7,5 USD | ~88,5 USD | ~898,5 USD | Gói Spark tắt trang khi hết hạn mức |
| Netlify | ~14 USD | ~90 USD | ~840 USD | Gói Free khóa **mọi** trang khi hết 300 credit |
| Vercel | 20 USD (Pro) | 20 USD | ~770–1.770 USD | Gói Hobby cấm dùng thương mại |

**Không dùng làm nơi phục vụ:**
- **Google Drive:** chính sách cấm dùng thay CDN; file tải nhiều bị khóa tới 24 giờ.
- **GitHub Releases:** không gửi header CORS, trình duyệt không tải được GLB.
- **jsDelivr:** cấm dùng làm kho media chung.
- **Hugging Face.**

**itch.io** dùng được làm kênh phát hành phụ cho game nhỏ. Giới hạn 500 MB và 1.000 file mỗi game; Space hiện vượt cả hai.

## 6. Việc phải làm khi đưa lên (theo thứ tự)

| Bước | Việc | Ai |
|---|---|---|
| 0 | **Tên miền:** đặt nameserver ở Cloudflare.<br>• Nếu tên miền đang có web hay email: kiểm danh sách bản ghi DNS Cloudflare chép sang **trước khi** đổi, và tắt DNSSEC ở nơi mua trước.<br>• Chờ zone báo Active (có thể vài giờ). | **Chủ dự án** |
| 0 | **Thanh toán:** thêm phương thức thanh toán để bật R2. | **Chủ dự án** |
| 0 | **Quyết:**<br>• nhạc riêng `shared/music` **không được phát hành**: cần bộ nhạc có giấy phép, hoặc tắt nhạc trên bản online;<br>• 4 game luyện gõ: đưa lên cùng, hay bỏ khỏi `games.json` online. | **Chủ dự án** |
| 1 | **Sửa mã: nguồn portal.** Mọi game ghi cứng nguồn portal `https://typing-game.local` (`PARENT_ORIGIN` trong kit và trong Space). Đổi thành biến lúc build (ví dụ `VITE_PORTAL_ORIGIN`) rồi build lại từng game. Không sửa thì trong portal online sẽ hỏng:<br>• mất kết quả học và Smart Review;<br>• phím không vào game;<br>• chế độ Voice của Space không chạy;<br>• trình duyệt không báo lỗi nào. | Claude, có phản biện |
| 1 | **Sửa mã: portal online.**<br>• Bản build bỏ mục Space Admin (Admin chỉ chạy ở máy nhà).<br>• Mô hình giọng: để trong R2, Worker của portal trả nó ở đúng đường `/assets/voice/<id>.tar.gz` (chỉ đường này chạy Worker). Người chơi tải một lần; không cần CORS, không đổi mã nạp.<br>• Object có `Content-Type: application/gzip`, không có `Content-Encoding`.<br>• Bước build portal phải chạy `pnpm voice:prepare`. | Claude |
| 1 | **Sửa mã: Tuyến Cuối và `games.json`.**<br>• Tuyến Cuối kèm bản chép thư viện model của Space trong gói deploy.<br>• `games.json` thật, với tên miền con thật. | Claude |
| 2 | **Script đóng gói** cho từng game: `build` → `.deploy/<game>/` → kiểm trước khi đẩy.<br>• Chép `shared/vocabulary` vào `/vocabulary/`; `shared/typing-texts` vào cả `/typing-texts/` (game dùng kit) và `/shared/typing-texts/` (Space). Portal cũng cần `/vocabulary/`.<br>• Kiểm trước khi đẩy: không file nào trên 25 MiB; dưới 20.000 file; không file riêng tư (`shared/music`, Dota-Sounds, `local-assets`).<br>• Bỏ `.DS_Store` và README nội bộ, nhưng **giữ** `ATTRIBUTION.md`, `SOURCE.md`, `LICENSE`, `NOTICE`: dữ liệu từ vựng theo CC BY-SA 4.0 bắt buộc ghi nguồn, và portal có link tới `/vocabulary/ATTRIBUTION.md`. | Claude |
| 2 | **`_headers`:** chỉ chọn được theo đường dẫn, không theo `?v=`. Làm giống nginx đang làm:<br>• `/assets/<id-game>/*` để `no-cache`;<br>• chỉ JS/CSS có hash trong tên mới để `immutable`.<br>• Media chưa có phiên bản (GLB của Rồng, ảnh của Lời Gọi, âm của Space) phải đổi sang tên có hash trước, rồi mới được để lâu. | Claude |
| 3 | **Deploy:** từng game, portal sau cùng. Đo trên dashboard xem lượt tải file tĩnh có bị trừ vào hạn mức không. | Claude |
| 4 | **Backend Space** khi anh muốn mở tài khoản online. Worker API đã chạy 112/112 test trên workerd. Tự theo dõi hạn mức (mục 3). | Claude, anh duyệt |

**Những thứ chưa đưa lên được, cần ghi rõ cho người chơi:**
- **API runtime của Admin** (`/api/runtime/space-typing/*`, cổng 3199) chưa có chỗ chạy trên Cloudflare.
  - Bản online của Space dùng cấu hình có sẵn trong mã. Những gì anh Publish trong Admin (thế giới, màn, tàu, cửa hàng, thư liveops, ảnh tàu) sẽ không tới người chơi online.
  - Muốn có: khi bấm Publish thì xuất file JSON tĩnh, đưa lên cùng tên miền với Space (mã chỉ nhận đường dẫn cùng nguồn). Đây là việc riêng.
- **Đấu đôi online của Space:** máy chủ Duel là Node (`games/space-typing/server/duel/ws-server.ts`), phải viết lại bằng Durable Objects. Bản online đầu tiên chỉ có Practice với bot.
- **Phòng đội của Tu Tiên** mới là thiết kế (canon §19.2).

**Chưa có tên miền?** Chỉ thử được từng game riêng trên `*.workers.dev`:
- không có `media.`, không có luật chặn spam WAF;
- khi chuyển sang tên miền thật phải build lại mọi game (đổi nguồn portal) và đăng ký lại callback đăng nhập Google, Facebook.

## 7. Vẫn nên làm nhẹ game, vì người chơi chứ không vì Cloudflare

Đo thử trên file thật, chưa sửa gì trong repo.

- **Model là đòn bẩy lớn nhất.** Bậc High dùng texture 2048; texture chiếm 83 % dung lượng các GLB bậc High (263 MiB).
  - Hạ về 1024 và nén meshopt mức `high`: `warden-prism` từ 3,90 xuống 1,35 MiB (−65 %); dùng AVIF thì còn 1,14.
  - Bộ nhớ GPU mỗi boss từ khoảng 89 MB xuống khoảng 22 MB.
  - Không dùng Draco: meshopt đã có và nhẹ hơn.
- **Bỏ file thừa.**
  - `tyrant-g01.glb` 12 MiB không thấy mã nào tải; cần xác nhận bằng log mạng trong trình duyệt.
  - Texture trùng giữa các GLB khoảng 22 MiB.
- **Ảnh 2D mới** (Rồng, Tu Tiên đang là PNG): dùng WebP.
  - Ví dụ: PNG 2,6 MB xuống 186 KB; ảnh đội hình Tu Tiên 3,35 MB xuống 353 KB.
  - Cỡ tối đa theo việc dùng: nền toàn màn 1920; icon 256.
- **Âm:**
  - Opus trong Ogg: nhạc 64–96 kbps; SFX mono 32–64 kbps. Nhạc bài hát của Space đã là Opus.
  - Ogg chỉ chạy từ iOS 18.4: cần bản AAC dự phòng, và thử trên iPhone thật.
- **Chất lượng mặc định theo máy:** Space luôn tải High (`main.ts:753`), kể cả trên điện thoại. Màn hình nhỏ, chạm, hoặc bật tiết kiệm dữ liệu thì dùng Medium.
- **Ngân sách lần chơi đầu mỗi game:**
  - Space ≤ 8 MB ở High (hiện khoảng 17 MB);
  - Rồng ≤ 5 MB; Lời Gọi ≤ 6 MB; Tuyến Cuối, Tu Tiên ≤ 4 MB.
- **Kết quả ước:** Space từ 591 MiB còn khoảng 250–300 MiB (WebP) hoặc khoảng 200 MiB (AVIF); màn đầu từ khoảng 17 MB còn khoảng 7 MB.

**Công cụ:**
- Đã có trong WSL: ffmpeg (Opus, AAC, AV1), ImageMagick 7, sharp, gltf-transform 4.5, meshoptimizer.
- Cài thêm khi cần, không cần sudo: `@gltf-transform/cli`, KTX-Software 4.4 (chỉ khi cần giảm bộ nhớ GPU), gltfpack.

**Giao việc:** việc đổi định dạng hàng loạt giao Codex được. Mã nạp media và kiểm hình phải qua phản biện của Claude.

## 8. Nguồn

**Cloudflare** (đọc 25/10/2026):
- Giới hạn Workers và Static Assets: <https://developers.cloudflare.com/workers/platform/limits/>
- Tính tiền file tĩnh: <https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/>
- Giá Pages Functions (chỉ lượt chạy mã bị trừ): <https://developers.cloudflare.com/pages/functions/pricing/>
- Giá Workers và gói 5 USD: <https://developers.cloudflare.com/workers/platform/pricing/>
- Giá R2: <https://developers.cloudflare.com/r2/pricing/>
- Bucket công khai và tên miền riêng: <https://developers.cloudflare.com/r2/buckets/public-buckets/>
- CORS của R2: <https://developers.cloudflare.com/r2/buckets/cors/>
- Bộ đệm mặc định: <https://developers.cloudflare.com/cache/concepts/default-cache-behavior/>
- Cache Rules: <https://developers.cloudflare.com/cache/how-to/cache-rules/>
- File đã đệm không đọc lại R2: <https://developers.cloudflare.com/billing/manage/optimize-costs/>
- D1: <https://developers.cloudflare.com/d1/platform/limits/>
- Durable Objects: <https://developers.cloudflare.com/durable-objects/platform/pricing/>
- Điều khoản CDN: <https://www.cloudflare.com/service-specific-terms-application-services/>
- Điều khoản Developer Platform: <https://www.cloudflare.com/service-specific-terms-developer-platform/>
- Chính sách thanh toán: <https://developers.cloudflare.com/billing/understand/billing-policy/>
- Tên miền riêng của Pages: <https://developers.cloudflare.com/pages/configuration/custom-domains/>

**Repo:**
- Kế hoạch online của Space: `games/space-typing/docs/ONLINE_CLOUDFLARE_DEPLOY.md` (Worker API, D1, chat; ước số người chơi, ngưỡng lên 5 USD); cấu hình `games/space-typing/cloud/wrangler.jsonc`.
- Kho media: `docs/MEDIA_STORAGE.md`, `media/media.config.json`.
- Play mode: `infra/nginx/typing-game.local.play.conf`. Alias model Space cho Tuyến Cuối ở dòng 219–223.
- Nạp model của Tuyến Cuối: `games/typing-survival/src/view/models.ts:8`.
- Portal tin nguồn theo `games.json`: `portal/src/main.ts:83-86`, `portal/src/learning/bridge.ts:73-77`.
- Mô hình giọng: `portal/src/voice/model-cache.ts`.
- Đường media cứng: `games/space-typing/src/**` có khoảng 208 chỗ `"/assets/"`. Kit nhận tham số ở `shared/game-kit/three/model-loader.ts:92-116` và `audio/scene-audio.ts:30`.
- Máy chủ đấu đôi: `games/space-typing/server/duel/ws-server.ts`.
- Đóng gói model: `games/space-typing/scripts/models/prepare-models.mjs:220-235`.

**Số trong tài liệu này:** đo ngày 25/10/2026. Bản đo và hai bản phản biện lưu ngoài repo, trong thư mục scratch `hosting/` của phiên làm việc.
