# Hướng dẫn thiết kế nhân vật: sức hút, bộ hào quang, đường ống làm

Ngày 01/11/2026, tối · Áp dụng cho mọi nhân vật ở mọi game trong repo (Dragonhold, Wordwoven, Last Line, Tu Tiên Thủ Ải, Space Typing và các game sau) · Viết từ bảy ghi chú nghiên cứu cùng tối: thần thoại, tu tiên, hoàng gia, chiến binh sci-fi, hào quang khi chơi, cách người khác dựng hiệu ứng, và ý kiến thứ hai của ChatGPT đã kiểm từng ý · Công thức hiệu ứng: [HERO_PRESENCE_VFX.md](HERO_PRESENCE_VFX.md) · Skill dùng tài liệu này: `game-character-design` (thiết kế và nhận ảnh), `game-hero-presence-vfx` (hào quang khi chạy).

**Đọc nhanh**
- Mọi brief nhân vật phải qua **danh sách kiểm sức hút** ở §3 trước khi viết prompt; prompt viết theo thứ tự ở §3.1, giám khảo điền phiếu ở §3.2.
- **Ánh sáng không bao giờ vẽ vào ảnh nguồn hay vào model.** Hình khối cứng chạm thân nằm trong model; mảnh cứng lớn đứng tách khỏi thân là phụ kiện riêng gắn cứng vào xương; mọi thứ bay, quay, phát sáng hay đổi theo trạng thái là VFX gắn vào socket (§7).
- **Last Line:** ba hướng nhân vật và ba hướng drone ở §4 để chủ dự án chọn; quy cách hào quang khi chơi ở §5.
- **Chấm:** hai giám khảo mù cùng cho từ 8,5, có điểm sức hút cạnh điểm mức thị trường. Đơn giản hay trơn thì trượt (§6).

**Ký hiệu**

| Viết tắt | Tài liệu |
|---|---|
| `VFX` | [VFX_STANDARD.md](VFX_STANDARD.md) |
| `QR` | [QUALITY_RESCUE_2026-11-01.md](QUALITY_RESCUE_2026-11-01.md) |
| `LESSONS` | [LESSONS_FROM_THREE_GAMES.md](LESSONS_FROM_THREE_GAMES.md) |
| `HPV` | [HERO_PRESENCE_VFX.md](HERO_PRESENCE_VFX.md) |
| `[TT1]`… | nguồn web, danh sách ở cuối tài liệu (TT thần thoại, TX tu tiên, HG hoàng gia, SF sci-fi và game, HQ hào quang, PL đường ống, GP ChatGPT) |

---

## 1. Vì sao có tài liệu này

Ngày 01/11/2026 chủ dự án loại hai bản thiết kế nữ xạ thủ Last Line liền nhau vì trơn, giống phản diện và đơn giản: mặt nạ đen kín mặt, hai vây như sừng ở tai, giáp nhựa trơn. Bản thứ ba vẽ luôn vòng sáng vào ảnh nhân vật, và chủ dự án thấy lạ. Chủ dự án muốn hình đẹp, cuốn hút, phong cách, sang trọng, thời trang, hiện đại, và nói rõ phải nghiên cứu trước khi vẽ:

> "những yếu tố để khiến nhân vật đẹp hơn, ví dụ như vòng ánh sáng, hoặc các thứ xung quanh người chơi như ánh sáng nhỏ… trước khi thiết kế nhân vật, bạn phải đi tìm các tài liệu, đọc và phân tích những nhân vật thần thoại hoặc truyền thuyết hoặc tu tiên, hoàng gia, chiến binh để lấy những ý tưởng đó đưa vào những chi tiết của nhân vật"

Tài liệu này ghi kết quả nghiên cứu đó và các luật rút ra.

- **Áp cho mọi nhân vật ở mọi game:** anh hùng, bạn đồng hành (drone, thú cưng), rồng (Hỏa Long, Bạch Long, Draconis), boss, nhân vật có tên.
- **Quái và boss:** tìm ở `docs/games/MONSTER_MODEL_INVENTORY.md` trước và dùng lại. Sức hút vẫn áp, nhưng chiều bạn–thù đảo lại: quái được mang dấu hiệu phản diện và màu phe địch, anh hùng thì không.
- **Phân vai:** design doc của từng game quyết nhân vật là ai; tài liệu này quyết thiết kế và nhận nhân vật thế nào.
- **Mức nhận:** 8,5 từ hai giám khảo mù (`ART_ACCEPTANCE.md`). Animation nhân vật là hệ dùng chung, mức 9 (`SHARED_SYSTEMS_BAR.md`).

---

## 2. Tóm tắt nghiên cứu theo lăng kính

Cách đọc:
- Mỗi bảng ghi thiết bị (device) hình ảnh, vì sao nó hiệu quả, và nguồn.
- "Chưa kiểm" là chỗ người nghiên cứu không mở được nguồn, hoặc chỉ thấy nguồn yếu. Không đưa chỗ đó vào brief khi chưa kiểm lại.
- Cỡ trên màn của từng thiết bị ở camera chơi nằm ở §3 mục 9 và §4.1.

### 2.1 Thần thoại và truyền thuyết

| # | Thiết bị | Vì sao hiệu quả | Nguồn |
|---|---|---|---|
| 1 | Nimbus và vương miện tia (radiate crown) | Ánh sáng tỏa từ chính người đó: dấu hiệu cổ nhất của cả vương quyền lẫn thần thánh. Hoàng đế La Mã dùng trước các thánh; về sau hào quang thu lại thành một vòng vàng mảnh | TT1 |
| 2 | Mandorla, "glory" | Quầng hình hạt hạnh quanh cả thân, dành cho bậc cao nhất. Càng nhiều sáng quanh thân, bậc càng cao | TT2 |
| 3 | Quầng viền lửa | Mép quầng tách thành lưỡi lửa (tượng Phật Khotan ở Met; karuraen của Fudō Myōō, lửa hình cánh garuda): sức mạnh sống, thanh tẩy. Chưa kiểm hết: trang Met trả HTTP 429, mô tả lấy từ kết quả tìm kiếm | TT3 |
| 4 | Vòng lửa quanh thân (prabhamandala của Nataraja) | Đặt nhân vật ở tâm vũ trụ | TT4 |
| 5 | Cánh dang che chở (Isis, Nut) | Cánh nghĩa là bảo vệ, không phải tấn công. Hợp với người giữ phòng tuyến | TT5 |
| 6 | Cánh vuốt ra sau, vải bay (Nike Samothrace) | Đọc ra "chiến thắng đang tới" | TT6 |
| 7 | Cánh nhiều tầng (seraphim) | Bậc tăng theo số đôi cánh | TT7 |
| 8 | Chiến binh thánh mặc giáp (Tổng lãnh Michael, Joan of Arc của Ingres) | Đọc ra quán quân thánh, không phải lính thường | TT8 |
| 9 | Mũ có mào, chất liệu quý, thần nhỏ theo hầu (Athena Parthenos cầm Nike trên tay) | Mào và người theo hầu làm nên vị thế | TT9 |
| 10 | Vương miện có biểu tượng, khăn lụa mỏng bay (Quan Âm) | Khăn chuyển động làm hình nhẹ và thanh thoát | TT10 |
| 11 | Thanh ngang rộng trên đầu và đoàn tùy tùng (*sheng* của Tây Vương Mẫu) | Quyền lực đến từ độ rộng ở đầu và từ người theo hầu | TT11 |
| 12 | Nâng đĩa mặt trời, mặt trăng (Phục Hy, Nữ Oa) | Cầm chính ánh sáng: quyền năng vũ trụ | TT12 |
| 13 | Tay tỏa thành quạt (Durga) | Vũ khí xếp thành hào quang | TT13 |
| 14 | Mũ lông chim cao, dòng dõi chim (trống Ngọc Lũ, Âu Cơ) | Chiều cao và chất anh hùng Việt cổ | TT14 |
| 15 | Màu là cõi (Đạo Mẫu: đỏ là trời, xanh là núi rừng, trắng là sông nước); Thánh Gióng bay về trời | Mỗi anh hùng một màu riêng, đọc từ xa | TT15 |

Chưa kiểm: "tre lửa" của Thánh Gióng chỉ có trên một trang bách khoa do AI viết (nguồn thật ghi ngựa sắt và tre thường hoặc tre vàng). "Tia nắng" của Amaterasu chỉ có ở trang phổ thông.

### 2.2 Tu tiên và võ hiệp

| # | Thiết bị | Vì sao hiệu quả | Nguồn |
|---|---|---|---|
| 1 | Pibo (khăn lụa dài trên 2 m, thời Đường muộn tới 5 m) và dải lụa | Phi thiên Đôn Hoàng bay nhờ vải và dải màu, không cần cánh: bay không gắng sức, thanh thoát | TX1, TX2, TX20 |
| 2 | Vòng đầu và quầng thân (hai vòng), tia vàng mảnh hay dải lửa nhỏ ở mép | Thiêng liêng và phẩm bậc | TT1 |
| 3 | Phi kiếm | Kiếm nghe theo thân: làm chủ bình thản. Yanqing (Honkai: Star Rail) điều kiếm từ xa và cưỡi kiếm. Không tìm được bài nhà làm game nói về thiết kế kiếm bay vòng quanh | TX3, TX4, TX5 |
| 4 | Trận pháp và chữ phù | Chữ phù cố ý không đọc được, và điều đó báo quyền năng | TX3, TX6 |
| 5 | Tường vân | Mây tiên cưỡi, điềm thái bình; hình đổi theo thời (dải thời Ngụy Tấn, hoa thời Đường, đầu như ý thời Tống Nguyên) | TX7 |
| 6 | Đài sen | Sạch từ bùn; nâng nhân vật lên | TX8 |
| 7 | Ngọc | Đức của người quân tử và vua hiền. Xiao (Genshin) dùng ngọc cho "trường thọ, bí ẩn" | TX9, TX10 |
| 8 | Bộ diêu (buyao) | Trâm có tua đung đưa theo bước; thời Hán chỉ nữ hoàng tộc được cài. Chuyển động nhỏ theo bước đọc ra quý phái | TX11 |
| 9 | Phượng quan | Khảm lông chim bói cá, vàng, chuỗi ngọc trai, lưỡi như cánh ở thái dương. Xanh bói cá là điểm "hoàng gia" | TX12 |
| 10 | Hạc và hạc xưởng (áo choàng lông hạc chạm đất) | Chim tiên; trên áo quan chỉ dưới rồng phượng | TX13 |
| 11 | Cờ lệnh sau lưng (đại khải kinh kịch) | Thiết kế để đọc từ sau lưng; đính sequin vàng bạc dày | TX14 |
| 12 | Áo nhiều lớp, tay áo thủy tụ, màu theo phẩm | Vàng cho hoàng tộc, tím cho quan cao, đỏ cho bậc cao hay đức lớn | TX15 |
| 13 | Một màu chủ đạo (phim *Anh Hùng*, 2002) | Mỗi đoạn một màu; một màu mạnh đứng vững ở xa | TX16 |
| 14 | Tiết chế, chừa khoảng trống | Naraka nhắm nét thủy mặc và khoảng trống (phỏng vấn báo chí); *Na Tra 2* cân khoảng trống với hạt dày; Liyue cân hoa, núi với khoảng trống | TX17 |
| 15 | Tu tiên trong sci-fi (Xianzhou của Honkai: Star Rail) | Vừa cổ vừa tương lai. Cầu nối cho Last Line: drone đóng vai phi kiếm, công nghệ trạm đóng vai hào quang và trận pháp | TX18 |

Chưa kiểm: không có nguồn nhà làm game cho Wuthering Waves hay cho kiếm bay vòng quanh; lông trĩ kinh kịch (lingzi) chỉ có ở trang bán hàng nên bỏ. Ý "phi thiên bay bằng dải lụa" có nguồn tầm trung; trang phi thiên của Met không bàn tới dải lụa.

### 2.3 Hoàng gia và thời trang

| # | Thiết bị | Vì sao hiệu quả | Nguồn |
|---|---|---|---|
| 1 | Vương miện tia mặt trời | Tia nhọn dần tỏa ra từ đầu: ánh sáng từ người đội | HG1 |
| 2 | Tiara kokoshnik, "halo tiara" | Thanh cao nhất ở giữa, thấp dần ra hai bên. Bước đều đọc ra trật tự bình thản, không hung hăng | HG2 |
| 3 | Hào quang vàng của hoàng đế (Theodora ở San Vitale) | Hào quang cũng là dấu phẩm bậc: uy nghi và ánh sáng thành một | HG3 |
| 4 | Pendilia (chuỗi ngọc rủ từ vương miện xuống vai) | Đóng khung mặt, chuyển động theo người, bắt sáng | HG4 |
| 5 | Cổ áo superhumeral (yếm vai bằng tấm vàng chạm lỗ, gắn đá) và loros | Mở rộng đường vai, đặt chất liệu quý nhất sát đầu | HG5 |
| 6 | Cổ đứng có khung (rebato, cổ Medici) | Khung đứng sau đầu: tổ tiên cung đình của hình hào quang | HG6 |
| 7 | Áo choàng lót màu tương phản và đuôi áo (Garter: nhung xanh thẫm lót taffeta trắng) | Chỉ áo của vua có đuôi: độ dài đuôi là phẩm bậc | HG7 |
| 8 | Dây chuyền huân chương có huy hiệu treo | Mắt xích lặp: nhịp điệu và dòng dõi | HG8 |
| 9 | Giáp nghi lễ khắc mạ vàng, chạm nổi (Greenwich 1527, Negroli) | Thép thành điêu khắc và trang sức cùng lúc | HG9 |
| 10 | Mào mũ ở bốn phía (tatemono của kabuto) | Mào là dấu nhận diện từ xa; ban đầu chỉ chủ tướng được đội | HG10 |
| 11 | Vật trang trí giữa lưng (agemaki, horo, sashimono) | Giáp samurai được thiết kế để đọc từ sau lưng | HG11 |
| 12 | Luật màu huy hiệu (tincture) và viền tách (fimbriation) | Không đặt kim loại lên kim loại, màu lên màu; hai vùng tối chạm nhau thì có viền sáng mảnh. Hình nào cũng rõ ở xa | HG12 |
| 13 | Cấu trúc couture: Balenciaga (vải cứng đứng xa thân, điểm nhấn ở lưng), McQueen (cổ lông vàng như giáp), Iris van Herpen (cấu trúc phản quang) | Sang đến từ cấu trúc, không từ chồng trang sức | HG13 |

Hai nguồn game hỗ trợ: hướng dẫn nhân vật Dota 2 (nhiều vùng nghỉ, chi tiết chỉ ở chỗ quan trọng) [SF3]; Bungie trộn giáp Nhật và áo choàng vào sci-fi ("mythic sci-fi") [HG14].

### 2.4 Chiến binh sci-fi và thiết kế anh hùng trong game

| # | Thiết bị | Vì sao hiệu quả | Nguồn |
|---|---|---|---|
| 1 | Một hình "móc câu" riêng | Riot cho mỗi tướng một nét chính mà không skin nào được bỏ hay đổi mạnh; viền hình phải nói nguồn sức mạnh và hướng nhìn | SF1 |
| 2 | Thứ tự đọc: viền ngoài, rồi khối trong, rồi chi tiết | Valve thử từng lớp TF2 bằng bóng đen trước khi thiết kế khối bên trong | SF2 |
| 3 | Chân tối, ngực và đầu sáng | TF2 và Dota 2 đặt tương phản mạnh nhất ở thân trên; mắt đi lên đầu và vai | SF2, SF3 |
| 4 | Vùng nghỉ và vùng chi tiết | Chi tiết chỉ ở một phần nhỏ thân, đặt đúng chỗ; chi tiết quá nhỏ thành nhiễu | SF3 |
| 5 | Một vật trang trí trung tâm làm điểm nhìn | Octavia Prime đặt một cuộn đàn cello giữa mũ và giảm các mô típ khác; Grendel Prime bỏ ngà vai thừa | SF4 |
| 6 | Viền vàng đánh dấu bậc cao | Warframe Prime giữ nhận diện, thêm chi tiết vàng (Rococo, Baroque muộn) trên mép tấm có sẵn | SF5 |
| 7 | Mythic sci-fi: giáp cộng vải huy hiệu | Destiny ghép giáp kiểu mecha với áo choàng, cờ và trang trí trung cổ. Vải biến công nghệ thành quý tộc, và là mảng lớn nhất nhìn từ sau | SF6, HG14 |
| 8 | Một sọc hay một huy hiệu nhấn | Sọc đỏ N7 của Shepard thành thương hiệu riêng | SF7 |
| 9 | Công nghệ cứng mang năng lượng, dải màu hẹp | PROJECT giữ màu trong một dải vàng–đỏ, màu khác dịu đi | SF8 |
| 10 | Ánh sáng đi theo đường thật | Glitchpop: sáng chạy theo dây từ pin tới máy chiếu, một gradient. Sáng có đường đi trông như được thiết kế, đắt tiền | SF9 |
| 11 | Ánh sáng theo trạng thái trận | Giáp Solstice của Destiny sáng dần khi Super nạp; Riot tránh biến hình sáng gần như suốt trận | SF10, SF1 |
| 12 | Khung cánh, mũ hình chim săn | Mercy (bộ Valkyrie), Pharah (Raptora, vàng trên lam và đen): cánh và mào cho chất thiên thần trong sci-fi | SF11 |
| 13 | Vai to, bảng màu tươi sáng | Overwatch chọn thế giới hy vọng, kiểm không viền nào giống viền tướng khác; Riot: vai to giúp viền, vai nhọn quá cỡ làm nhòe | SF12 |
| 14 | Viền sáng thay viền tối; bóng ngả lạnh | TF2 tách nhân vật khỏi cảnh bằng viền sáng rộng | SF13 |
| 15 | Thiết kế cho góc người chơi thấy | Warframe sửa chi tiết đẹp từ trước nhưng hỏng khi nhìn nghiêng; đạo diễn Shift Up chăm lưng nhân vật Stellar Blade vì đó là góc người chơi thấy nhiều nhất; NIKKE cố ý cho thấy lưng khi chiến đấu | SF5, SF14, GP19 |

Không dùng làm căn cứ: NIKKE, Honkai Impact 3rd, Arknights, FFXIV, Halo chỉ có tin tóm tắt, không giải thích lựa chọn thiết kế (trừ bài phỏng vấn NIKKE mà ChatGPT tìm, §2.7).

### 2.5 Hào quang khi chơi (presence)

| # | Thiết bị | Vì sao hiệu quả | Nguồn |
|---|---|---|---|
| 1 | Vòng hào quang mảnh | Họa sĩ Ý thu hào quang thành vòng vàng mảnh vẽ theo phối cảnh: đánh dấu mà không che. Vòng mảnh đọc ra quý phái; đĩa đặc trông cũ | TT1 |
| 2 | Quầng toàn thân (mandorla, vòm lửa của Nataraja) | Nhân vật như làm chủ không gian quanh mình | HQ1, TT2 |
| 3 | Vương miện tia | Mặt trời và vua | TT1 |
| 4 | Viền sáng fresnel | Valve dùng viền sáng ở TF2 để tách nhân vật khỏi cảnh, lái theo ánh sáng môi trường | HQ2 |
| 5 | Dải độ sáng từ chân tối lên thân trên sáng | Chân sáng bằng đầu thì mắt không đọc được anh hùng | HQ2, HQ3 |
| 6 | Vũng sáng dưới chân | Diablo coi đó là chỉ số Light Radius. Từ trên nhìn xuống, một elip sáng dưới chân làm nhân vật sáng nhất trên nền tối | HQ4 |
| 7 | Đốm sáng bay quanh | Warframe bán riêng ephemera (hiệu ứng hào quang và bước chân). Đốm chậm, thưa đọc ra phép và giàu | HQ5 |
| 8 | Vật theo hầu bay cạnh vai (Ghost của Destiny) | Bungie tách vẻ ngoài của Ghost khỏi lối chơi để người chơi chọn theo gu. Drone Last Line là "viên ngọc bay" của nhân vật | HQ6 |
| 9 | Áo choàng, khăn, dải lụa có chuyển động phụ | Khăn của Journey mang ký tự sáng báo mức nạp, dài ra khi nhặt biểu tượng: vừa trang trí vừa là thước đo | HQ7 |
| 10 | Vệt khi di chuyển | Riot cho hướng đi bằng đuôi mờ | SF1 |
| 11 | Dấu chân sáng | Blazing Step của Warframe để lại dấu lửa: "mặt đất đáp lại nàng" | HQ5 |
| 12 | Nhịp sáng theo hành động | Fortnite có skin đổi theo sự kiện; Riot chỉ cho biến hình sáng lớn ở trạng thái được tăng sức | HQ8, SF1 |
| 13 | Hạt mềm (soft particle) | Sprite mờ dần chỗ chạm sàn; không có thì quầng trông như dán lên | HQ9 |

Quy tắc của Diablo IV: chi tiết phải phục vụ camera isometric, khối to hơn, ít phần tử hơn [HQ10]. Diablo III đặt độ đọc dưới camera isometric làm luật đầu: chốt bóng hình trước, thêm ánh sáng và chi tiết sau [HQ19]. Rocksteady (GDC 2024): khi mọi hành động đều có phản hồi lớn thì người chơi quá tải [HQ11].

### 2.6 Cách người khác dựng hiệu ứng

Tóm tắt; chi tiết thư viện và công thức ở `HPV`, quyết định ở §7.

- **Game thương mại tách ba loại:** giáp gắn vật lý, mảnh đeo sau lưng (syandana) và hạt (ephemera) ở Warframe [HQ5]; hạt, shader trên lưới và lens flare ở Destiny 2, ưu tiên shader trên lưới cho hiệu ứng tồn tại lâu [HQ13]; áo choàng và khăn mô phỏng như vải ở Destiny [HQ14]; khoảng 95 % hiệu ứng League là hạt lưới chạy bằng shader [HQ12].
- **Hào quang của avatar** là prefab riêng gắn vào xương đầu [HQ16]; Unreal có socket [HQ17]; three.js cho gắn vật làm con của `Bone` [PL15].
- **Tripo yếu ở phần mảnh** (nan, dây), vật trong suốt, vùng bị che; nhiều chủ thể bị gộp thành một lưới; thiếu ảnh sau lưng thì nó bịa "cấu trúc thừa trên lưng" [PL1, PL6, PL7]. Các bộ tạo texture 3D hiện có chỉ ra vài loại map PBR không phát sáng [PL4], và Tripo không xuất map phát sáng làm đầu ra chính [PL5]; nên ánh sáng vẽ vào ảnh nguồn chỉ còn chỗ rơi vào màu nền (albedo). Câu sau là suy luận của ta từ hai nguồn đó.
- **Đường mảnh dưới 1 px nhấp nháy;** kỹ thuật "dây điện thoại" giữ đường rộng ít nhất 1 px và giảm alpha thay vì làm mảnh hơn [HQ15].
- **Công cụ khác cùng giới hạn:** Meshy và Rodin nhận nhiều ảnh góc; Rodin khuyên giữ phần mảnh lộ rõ, tránh che khuất và phản chiếu [PL11, PL12].

### 2.7 Ý kiến thứ hai của ChatGPT: nhận gì, không nhận gì

ChatGPT (chế độ Chat, mức High, cuộc chat mới, khoảng 8 phút) được hỏi cùng câu hỏi [GP0]. Người nghiên cứu mở nguồn kiểm 33 ý: 25 đúng, 4 ý "không có nguồn" mà ta cũng không tìm ra, 4 ý đúng một phần, không ý nào bịa. Chỗ yếu: bỏ sót một chi phí, lệch phiên bản với mã của ta, một trích dẫn lệch chủ đề. Tôi kiểm lại thêm vài nguồn then chốt (cuối mục).

| Ý của ChatGPT | Kết luận của ta | Lý do |
|---|---|---|
| Loại cách A (mọi thứ trong một ảnh, một model) | **Nhận** | Tài liệu của chính Tripo nêu phần mảnh, vật trong suốt, vùng bị che là chỗ yếu [GP1, GP2] |
| Cần một mảnh khối cứng làm nền cho hào quang ("vương miện sau lưng" hay hình lưỡi liềm nối giáp bằng hai trụ đủ dày); vòng sáng, quầng, đốm là VFX | **Nhận, chỉnh lại** | Đúng hướng. Ta tách thêm: mảnh chạm thân nằm trong model (C), mảnh lớn đứng tách là phụ kiện riêng (B) (§7) |
| Thử ở 68, 84, 100 px theo thứ tự bóng đen → màu phẳng → lõi phát sáng → bloom; tắt bloom mà hết đẹp thì hình khối chưa đủ | **Nhận** | Đây thành cổng kiểm ở §6 và §7.6 |
| Không có nguồn cho ngưỡng điểm ảnh của hào quang ở 68–100 px | **Đồng ý** | Ta cũng không tìm ra. Con số ở §5 là ước tính phải đo |
| Bảng màu: ngà ngọc trai, vàng champagne, chút cyan | **Không nhận phần vàng** | Vàng dành cho Pack Leader (`QR` §4.4); màu `crit` (#ffc23a) và dấu gõ chữ (#ffd36a) cũng là vàng. Thay bằng bạch kim, bạc trắng |
| Hình tròn, elip, vòm, cánh hoa thon, quạt nhiều lớp; tránh sừng ngược, ăng-ten như dao, vương miện gai, vai móng vuốt, mặt nạ nhọn | **Nhận** | Có nguồn: bài Overwatch về hình cơ bản, Warframe (hình tròn cho vui, gai cho ác), Island Time VR [GP12, GP13, GP14] |
| Mặt sau là thiết kế chính (NIKKE) | **Nhận** | Đã kiểm: Kim Hyung-tae, 04/10/2024 [GP19] |
| Biểu tượng: hào quang từ vương miện tia của Helios và hoàng đế La Mã; vương miện nhiều trang sức là vua vũ trụ (cakravartin); Amaterasu là ánh sáng trở lại; Honkai: Star Rail tạo sức sống và gu thời trang qua tóc và trang phục | **Nhận** | Đã kiểm [GP15–GP18]. Trang Met về Crowned Buddha còn ghi "diadem ba phần cao" và "áo choàng có tua", hợp với ý vương miện lưng |
| Drone: thân tròn hay oval, một "mắt" sáng lớn, vây trơn, không gai | **Nhận** | Hình tròn đọc ra thân thiện, gai đọc ra lạnh hay hiểm [GP12, GP13, GP14]; một mắt lớn là cách Destiny cho Ghost một "gương mặt" [HQ6]. `QR` §4.4 đã chốt thân giọt nước, một khe cyan. Ý "một mắt" là quy ước, không có nguồn nói nó tốt hơn hai mắt |
| Prototype đầu bằng TSL `BloomNode` (WebGPU) | **Không nhận** | Last Line chạy `WebGLRenderer`, `EffectComposer`, three **0.170**; TSL cần `WebGPURenderer`, còn `ShaderMaterial` và `onBeforeCompile` không chạy trên đó (`VFX` §4.1). ChatGPT tưởng ta dùng r187 |
| Selective bloom theo ví dụ của three.js | **Không nhận** | Ví dụ đổi mọi lưới không bloom sang vật liệu đen rồi vẽ cảnh hai lần [GP23]. Ngưỡng bloom 1,0 với lõi HDR đã chỉ cho lõi bloom trong một lần vẽ |
| three.quarks 0.17.x | **Không nhận** | 0.17.x đòi three ≥ 0.182; bản cuối hợp 0.170 là 0.16.0 (`VFX` §4.3) |
| 12–24 đốm sáng | **Chỉnh** | Ở 68 px ta chọn 8–12 khi nghỉ, tăng theo chuỗi gõ (§5). Lý do: Riot và Rocksteady về độ rõ [SF1, HQ11] |
| Mixamo hỏng với mảnh rời, cánh, đuôi lớn [PL13] | **Chỉ là bằng chứng gián tiếp** | Ta không dùng Mixamo (`SHARED_SYSTEMS_BAR.md` §5) và không dùng auto rig của Tripo (`CHARACTER_ANIMATION.md` §5.3). Rig của ta là Mesh2Motion trong Blender; lý lẽ đúng cho B là kiểm soát trọng số, không phải "rig tự động hỏng" |
| Không có nguồn về ngữ pháp hình tu tiên | **Đồng ý một phần** | ChatGPT gần như không tìm. Ghi chú tu tiên ở §2.2 có nguồn bách khoa và bảo tàng; nếu cần sâu hơn, hỏi lại ChatGPT bằng thuật ngữ Hán (法相, 背光, 剑阵, 飘带) và chỉ nhận nguồn học thuật, bảo tàng |

**ChatGPT bỏ sót, ta bổ sung:**
- Tripo tự khuyên tách phần: trang trợ giúp ghi tách thân và quần áo khi tạo nhân vật để hình sạch và rig dễ; module Segmentation ghi "tách phần cứng trước khi rig" và "mô-đun hóa tài sản game" [PL6, PL9].
- Rig của Tripo không có xương áo choàng, tóc đứng yên, không sửa được trọng số [PL8]. Với ta điều này không chặn, vì rig làm trong Blender, nhưng nó nhắc rằng chuyển động áo choàng và dải lụa là việc của ta.
- Hào quang phải thiết kế cho camera cố định (§4.1, §5).
- Chi phí các kiểu bloom chọn lọc, và mã hiện tại của Last Line (`HPV` §3).

**Tôi kiểm lại (01/11, tối):**
- Bài "Clarity in League" (12/03/2021): đúng như ghi chú, gồm ví dụ Eclipse Leona sáng gần như suốt trận nên không rõ trạng thái, câu "không bao giờ vặn mọi thứ lên 11", luật nét chính không skin nào được bỏ, và ví dụ vòng đất của Arcane Comet [SF1].
- three-nebula trên npm: bản 13.3.0, MIT, peer three `>=0.122.0 <1.0.0`, không có phụ thuộc chạy [V5 ở `HPV`].
- Các trang của Tripo trả HTTP 403 với công cụ đọc web của tôi, nên ý về Tripo dựa vào người nghiên cứu đã mở bằng trình duyệt. Một kết quả tìm kiếm khác của blog Tripo mô tả cách tạo riêng thân có quần áo, đầu không tóc, tóc kèm mũ rồi ghép trong Blender [PL10]; điều này khớp với cách B.
- Lượt phản biện (01/11, khuya) mở lại các nguồn chỉ có tên miền và số bài, rồi ghi đường dẫn đầy đủ: GP12 là bài Blizzard "What it's like to work on Overwatch as a concept artist" (Qiu Fang: hình lớn đặt gần đỉnh nhân vật để thấy từ xa); GP13 do Adam Volker viết, Ruby Wang là người được trích (bản tròn của Carl "đọc ra thân thiện"; VR cần bóng hình lớn, rõ từ trên nhìn xuống); GP14 là phỏng vấn Michael Skyers (Digital Extremes, 26/03/2026: chủ đề nghịch ngợm dùng hình tròn, chủ đề lạnh hay hiểm dùng hình cứng và gai); GP18 là phỏng vấn 4Gamer 29/12/2023 (HoYoverse nhấn sức sống và tính thời trang của Trailblazer qua màu tóc và trang phục); GP19 là phỏng vấn Game Watch 04/10/2024 (Kim Hyung-tae muốn cho thấy tư thế bắn từ sau và trước, nguồn gốc ý "nhìn từ lưng"). PL4 nay trỏ thẳng vào bài báo arXiv; PL14 có trang hướng dẫn của Reallusion.
- Ghi chú kiểm ChatGPT viết "Last Line đã làm luật chỉ lõi HDR bloom". **Chỉ đúng một phần:** ở `main` của `games/typing-survival` (tối 01/11) `scene.ts` vẫn là ACES và bloom 0,85 / 0,3 / ngưỡng 1,0. Bản sửa L1 (strength 0,45, radius 0,12, ngưỡng 1, Neutral, MSAA 4, `FeelBloomPass` giữ dấu gõ chữ) nằm ở nhánh `ts-wave1`, chưa gộp. Hào quang phải chỉnh theo giá trị của nhánh đó.

### 2.8 Điểm chung của sáu lăng kính

1. **Ánh sáng tỏa từ chính nhân vật** (hào quang, vương miện tia, quầng thân) là dấu hiệu chung của thần, vua và anh hùng qua nhiều nền văn hóa.
2. **Lưng mang nhận diện** khi camera thấy lưng: agemaki, horo, sashimono, cờ lệnh kinh kịch, nơ lưng Balenciaga, NIKKE, Stellar Blade.
3. **Một nét chính, một nét phụ, một nét thứ ba** (Riot, Valve, Octavia Prime). Mọi thứ cùng lúc thành nhiễu ở 80 px.
4. **Sang là tiết chế:** khoảng 75 % thân là vùng nghỉ; chất quý đặt ở đầu, vai, huy hiệu lưng; kim loại quý là dải viền, không phủ kín.
5. **Lúc nghỉ thì dịu, ánh sáng phải "kiếm được"** (Riot, Destiny Solstice, Journey). Sáng suốt trận làm mất đỉnh và mất trạng thái.
6. **Hình anh hùng:** tròn, vươn lên, bước đều, đầu nhọn bo tròn; che chở thay vì tấn công. **Hình phản diện:** gai, sừng, móng vuốt chĩa xuống, đỏ trên đen, hào quang đen, sáng từ dưới lên, mặt kín tối.
7. **Thứ mảnh hay bay thì là VFX;** thứ đặc và chạm thân thì là hình khối.
8. **Dịch, không chép:** lấy cấu trúc và logic màu, không chép biểu tượng thiêng (thánh giá, Phật trên mũ, trang phục hầu đồng thật, chữ phù thật) và không chép nhân vật có tên (Xiao, Yanqing, Mercy, N7, hoa văn Prime).

---

## 3. Danh sách kiểm sức hút (bắt buộc trước mọi brief nhân vật)

**Dùng hai lần:**
- **Trong brief:** mỗi mục là một lựa chọn cụ thể (một hình, một chất liệu có tên, một màu kèm tỉ lệ), không phải tính từ.
- **Khi chấm:** mỗi mục ghi có, một phần hay không, kèm một dòng mô tả thấy gì. Một "không" là lỗi có tên, phải sửa trước khi đưa giám khảo.

Skill `game-character-design` giữ bản tiếng Anh của danh sách này (`references/appeal-checklist.md`); hai bản phải khớp.

| # | Mục | Brief phải ghi | Đạt khi |
|---|---|---|---|
| 1 | **Bóng hình và ngôn ngữ hình khối** | Một nét chính (ví dụ khung cánh, cổ quạt đứng, cờ lưng), một nét phụ (vương miện, hào quang), một nét thứ ba (đốm sáng, màu ngọc). Hình anh hùng: vươn lên, chữ V, vai rộng bo tròn hay vuốt ra sau | Tô đen toàn thân, thu về cỡ chơi, nhìn từ phía camera thấy: vẫn đọc ra đúng nhân vật, đúng vai, là bạn chứ không phải thù; không giống viền của nhân vật hay quái nào khác trong game |
| 2 | **Điểm nhìn** | Một chỗ mắt rơi vào trước (đầu và vương miện, hay lõi). Camera thấy lưng thì có điểm nhìn thứ hai ở lưng (lõi lưng, huy hiệu lưng) | Tương phản và ánh sáng mạnh nhất nằm đúng ở đó; không có điểm thứ hai cạnh tranh |
| 3 | **Nhóm độ sáng và mật độ chi tiết** | Ba nhóm sáng, vừa, tối kèm tỉ lệ; vùng chi tiết (đầu, vai, huy hiệu lưng) và vùng nghỉ (khoảng 75 %) | Làm mờ ảnh vẫn thấy ba nhóm; ảnh xám ở cỡ chơi vẫn tách được đầu, vai, lưng. Trượt nếu chi tiết rải đều hay có tấm trống lớn |
| 4 | **Chất liệu cao cấp** | Tên từng chất liệu và độ bóng: gốm ngà ngọc trai, chỉ bạch kim, kim loại chải xước, men, lụa, kính phát sáng | Có tương phản mờ–bóng, vải mềm–tấm cứng. Trượt nếu một độ bóng nhựa đều khắp |
| 5 | **Cấu trúc hiện đại nhiều lớp** | Đếm được lớp: đồ lót thân, tấm giáp phân đoạn có đường ghép và vát, khớp cơ khí, viền, rãnh sáng chìm, vải phủ ngoài giáp | Các tấm chồng và bậc lên nhau, mép có viền. Trượt nếu là một lớp vỏ trơn |
| 6 | **Dấu hiệu hoàng gia, thần thánh** | Chọn từ §2, từ một nguồn văn hóa thống nhất hay một pha trộn có chủ ý: vương miện, diadem, cổ đứng, huy hiệu, áo choàng, dải lụa, hào quang | Phẩm bậc và vẻ thanh lịch hiện ra mà vẫn rõ là chiến binh (thế đứng, vũ khí, giáp). Không phải đồ hóa trang ghép thời đại |
| 7 | **Bộ hào quang** | Bốn phần: hào quang hay mandorla; kênh phát sáng trên giáp; đốm sáng hay vật trang trí bay quanh; áo choàng hay dải lụa chuyển động. Mỗi phần ghi: dạng (hình khối hay VFX theo §7), socket, màu, lúc sáng lên (nghỉ, chuỗi gõ, chiêu, thắng) | Mọi phần VFX bắt đầu từ một phần của model (giá gắn, đầu vây, đuôi khăn), nên trông như được mang trên người chứ không dán lên. Ảnh nguồn không có ánh sáng vẽ sẵn |
| 8 | **Kịch bản màu và màu dành riêng** | Trước hết liệt kê màu game dành cho tín hiệu: quái, đòn quái, quái tinh anh, phe ta, vật nhặt, tín hiệu gõ. Rồi chọn màu nền, màu phụ, màu nhấn (khoảng 60/30/10) và một màu phát sáng | Không dùng màu dành riêng ở cường độ cao; nhân vật tách khỏi độ sáng của nền map; vùng tối chạm nhau có viền sáng mảnh (fimbriation) |
| 9 | **Đọc được ở camera chơi** | Cỡ thật trên màn ở 1280×720 và 1920×1080, mặt camera thấy, góc nhìn. Cỡ tối thiểu: nét ≥ 2 px ở 720p; điểm nhấn ≥ 6 px; hào quang ≥ 2 lần chiều cao đầu | Ô kiểm ở cỡ thật, trên khung map thật, cạnh một con quái: bóng, điểm nhấn, vai trò, bạn hay thù đều đọc được không cần phóng. Mặt camera thấy nhiều nhất được thiết kế kỹ nhất |
| 10 | **Model Tripo hay VFX** | Bảng chia từng phần theo §7: trong thân (C), phụ kiện riêng gắn cứng (B), VFX (D); socket cho mỗi điểm neo | Ảnh nguồn không có phần bay, không có ánh sáng vẽ; mỗi model là một vật liền; mỗi lớp VFX có socket |
| 11 | **Bẫy** | Đối chiếu danh sách bẫy dưới bảng | Không mắc bẫy nào |
| 12 | **Sức hút, nói thẳng** | Một câu nói ý tưởng của thiết kế | Người chơi có muốn chụp màn hình không? Đặt cạnh bảng tham chiếu thương mại có đứng được không? "Sạch nhưng thường", "chung chung", "đơn giản" là trượt dù không sai gì |

**Bẫy và cách tránh**

| Bẫy | Trông ra sao | Cách tránh |
|---|---|---|
| Phản diện | Mặt nạ kín tối, sừng hay vây như sừng ở tai (mũ sừng còn là sáo mòn từ thế kỷ 19 [TT16]), gai, móng vuốt chĩa xuống, đỏ trên đen, mắt đỏ, hào quang đen, sáng từ dưới lên [HQ18], lửa đỏ cam lớn trên thân tối (vẻ minh vương phẫn nộ), áo trùm đầu tối, mặt nạ quái trên vai | Tia đứng, bước đều, đầu bo tròn; lót sáng; mặt và đầu để lộ; mào đặt ở đỉnh và sau đầu, không ở tai |
| Che mất nhân vật | Đĩa hào quang đặc nằm giữa camera và đầu; mandorla đứng che cả lưng; cổ hay vương miện che đầu; áo choàng che hết lưng | Vòng mở mảnh; mandorla chỉ lấy cung trên vai hoặc nằm dưới đất; giữ eo và vai lộ ra |
| Rối | Cánh sáu tầng cộng tia cộng mandorla cộng đốm; mười vật trang trí nhỏ; hoa văn mảnh trong texture; anh hùng phủ chi tiết nhỏ mất hình ở xa, còn mảng vàng lớn của Tracer thì giữ được [SF15] | Một nét chính, một nét phụ, một nét thứ ba; tối đa 3 lớp hào quang tách khỏi thân cùng lúc khi nghỉ (lớp trên bề mặt model không tính, `HPV` §1) |
| Rẻ tiền | Bloom mềm to, hào quang sáng cả mặt, gradient cầu vồng, vàng phủ khắp thân, dải lụa sáng nguyên dải | Chỉ lõi HDR mảnh được bloom; vàng (hay bạch kim) chỉ là dải viền trên nền sâu |
| Lẫn với lối chơi | Vòng dưới đất giống cảnh báo vùng đánh; sáng suốt trận giống đang dùng chiêu | Vũng sáng mềm không có viền vòng; nghỉ thì dịu; chiêu và chuỗi gõ mới sáng |
| Chỉ đẹp phía trước | Huy hiệu ngực, vòng cổ, trang sức mặt khi camera thấy lưng | Dời điểm nhấn ra lưng, gáy, sau mũ |
| Tối trên tối | Áo choàng xanh thẫm trên đồ lót đen trên sàn trạm tối | Viền sáng mảnh, viền sáng fresnel, thân trên sáng |
| Ghép thời đại | Byzantine cộng Tudor cộng samurai ngẫu nhiên; trang phục cung đình hay kinh kịch mặc nguyên văn trông như sân khấu (Yun Jin trộn kinh kịch với thời trang thường ngày [TX19]) | Chọn một ngữ pháp rồi dịch chất liệu sang sci-fi (men thành khảm phát sáng, ngọc trai thành hạt gốm, nhung thành vải nano mờ) |
| Chép biểu tượng thiêng hay nhân vật có tên | Thánh giá, Phật trên mũ, trang phục hầu đồng thật, chữ phù thật, N7, cánh Mercy | Lấy cấu trúc và logic màu; chữ phù tự vẽ, không đọc được |
| Phần bay trong ảnh nguồn | Hào quang mảnh, lông vũ rời, ánh sáng vẽ | Đưa sang VFX (§7) |

### 3.1 Từ danh sách sang prompt ảnh

Prompt viết bằng tiếng Anh, theo đúng thứ tự dưới đây; mỗi dòng lấy từ một mục ở trên, không thêm tính từ không có trong brief.

| Thứ tự | Dòng prompt | Lấy từ mục |
|---|---|---|
| 1 | Một câu ý tưởng: ai, vai gì, phe ta | 12 |
| 2 | Nét chính, nét phụ, nét thứ ba, mỗi nét một hình có tên và cỡ so với thân (ví dụ "wing frames 1.6× shoulder width") | 1 |
| 3 | Mặt camera thấy và điểm nhìn ở mặt đó (ví dụ "the back carries the identity: …") | 2, 9 |
| 4 | Chất liệu có tên và độ bóng, từng vùng | 4, 5 |
| 5 | Màu nền, phụ, nhấn kèm tỉ lệ; màu bị cấm ghi tên | 8 |
| 6 | Dấu hiệu hoàng gia, thần thánh đã chọn và nguồn văn hóa | 6 |
| 7 | Kênh sáng **vẽ màu phẳng** ("flat pale-cyan paint lines, unlit") | 7, 10 |
| 8 | Ràng buộc dựng: một vật liền, mọi mảnh cứng đủ dày và chạm thân, A-pose, tay tách thân, vạt áo tách chân | 10 |
| 9 | Góc nhìn, nền khóa màu, ánh sáng phẳng (§7.6 bước 4) | — |

**Câu cấm luôn có** (dịch từ mục 7, 8, 11): no glow, no bloom, no light rays, no halo ring, no floating parts, no particles, no closed or dark face mask, no horns or fins at the ears, no spikes or claws, no saturated gold (khi game dành vàng cho tín hiệu), no text or symbols. Ảnh nào còn một thứ trong danh sách này là trượt mục 10, không cần đưa giám khảo.

### 3.2 Phiếu chấm theo danh sách

Giám khảo (và làn làm, khi tự chấm) điền một dòng cho mỗi mục 1–12: **có / một phần / không**, một câu thấy gì, và số đo khi mục đó có số.

| Mục | Số đo phải ghi |
|---|---|
| 1 Bóng hình | Bóng đen ở 68, 84 và 100 px từ camera chơi: kể được nét chính không cần nhìn ảnh màu |
| 2 Điểm nhìn | Vị trí điểm sáng nhất trên ảnh xám cỡ chơi; có trùng điểm nhìn đã ghi không |
| 3 Nhóm độ sáng | Ảnh làm mờ: đếm được ba nhóm; tỉ lệ vùng nghỉ ước khoảng 75 % |
| 8 Màu | Không màu nào trùng màu dành riêng (so cạnh ô màu của game) |
| 9 Độ đọc | Cỡ điểm nhấn lưng và nét mảnh nhất tính bằng điểm ảnh ở 720p (≥ 6 px và ≥ 2 px) |
| 10 Dựng | Đếm phần bay, khe hở, mảnh mảnh hơn 2 px ở 720p: phải bằng 0 |

Mục 4, 5, 6, 7, 11, 12 chấm bằng mắt, nhưng câu "thấy gì" phải nêu vật cụ thể (ví dụ "viền bạch kim trên 4 tấm vai"), không chỉ "đẹp" hay "sang". Bản tiếng Anh trong skill (`references/appeal-checklist.md`) phải cập nhật theo hai mục này.

---

## 4. Áp dụng cho Last Line: nữ xạ thủ và drone

### 4.1 Số đo camera và màu

| Mục | Giá trị | Nguồn |
|---|---|---|
| Camera | Pitch 36°, FOV 42; thấy nhân vật từ sau lưng, chếch khoảng 46° từ trên | `QR` §4.1 |
| Chiều cao trên màn | Tỉ lệ đề xuất 2,6 m: khoảng 68 px ở 720p, 100 px ở 1080p. Nếu giữ 1,8 m: 47 và 69 px (khi đó mọi số dưới đây nhỏ đi 30 %, và nên thử camera 30°, `QR` §4.2) | `QR` §4.1 |
| Điểm ảnh | 1 % chiều cao = 0,68–1 px. Ở tỉ lệ 2,6 m: 1 px ≈ 3,8 cm (720p) và 2,6 cm (1080p) trong thế giới | tính |
| Cỡ thân (theo tỉ lệ 8 đầu) | Đầu khoảng 8,5–12,5 px; vai 17–25 px, tới 20–35 px nếu vai phóng 1,2–1,4 lần kiểu anh hùng | tính |
| Ngưỡng nhìn thấy | Nét dưới 2 px (khoảng 3 % chiều cao, khoảng 7,5 cm ở tỉ lệ 2,6 m) nhấp nháy hoặc biến mất | Hình mảnh dưới 1 px vỡ thành chấm [HQ15]; mức 2 px là biên an toàn ta chọn, chưa có nguồn cho đúng con số này (§2.7), phải đo ở T1 (§7.7) |
| Phối cảnh | Mặt đứng (lưng) còn cos 46° ≈ 0,69; mặt nằm (đỉnh đầu, đỉnh vai) còn sin 46° ≈ 0,72. Lưng và đỉnh đầu được số điểm ảnh gần bằng nhau. Mặt, ngực và kính cyan quay về phía quái nên không thấy | tính, `QR` §4.1 |
| Nền | Sàn trạm tối, trời hố đen với đĩa bồi tụ cam (`PALETTE.hot` #ff7a1f) | `games/typing-survival/src/view/theme.ts` |
| Màu dành riêng | Vàng: Pack Leader (`beacon` #ffcf4a), `crit` (#ffc23a), dấu gõ chữ (#ffd36a), quái Bọc Thép chết (`armour` #ffd27a), đạn Tán (`tan` #ffc53d). Đỏ `danger` (#ff3b3b): đòn quái. Cam `hot`: Heat Beam, hố đen. Lam `volt` (#3db8ff): ống dẫn, Pulse Gun. Xanh ngọc nhạt `perfect` (#9ffff2) và `repair` (#7ff5e0): tín hiệu gõ chữ, gói sửa. **Nhóm cyan của phe địch:** `voltHi` (#a6e0ff) khi quái tinh anh chết, tường năng lượng của quái mang khiên `shield` (#4fc8ff) và mảnh kính `glass` (#9fe6ff). Đạn ta: `pierce` (#bfe9ff), Rail `ray` (nhánh `ts-wave1`: lam coban #3d6bff). Phe địch: tím (đề xuất O5) | `QR` §2.3, §3 (O5), §4.4; `theme.ts` (`PALETTE`, `BLOW`) |
| Bảng màu của nhân vật | Gốm ngà ngọc trai, chỉ bạch kim hay bạc trắng, ánh sáng cyan điện, áo choàng xanh navy; đồ lót graphite | `QR` §4.4 |
| Bảng màu của súng | Cùng bảng với nhân vật: vỏ gốm ngà trên graphite, viền bạch kim. Màu riêng của từng súng (Tán hổ phách, Heat Beam cam, Rail coban, Pháo Sao đỏ son) chỉ có ở lõi sáng và VFX đòn, không ở vật liệu vỏ | `QR` §4.4 ("nhân vật, drone và súng dùng gốm ngà và graphite"); `theme.ts` |
| Chỗ chữ bay vào | Chữ của từ gõ xong bay vào `FX_CORE` của súng thuộc bến đang nạp | `QR` §4.7 |

Hệ quả cho thiết kế:
- **Không vàng bão hòa** trên nàng, drone hay vỏ súng: kim loại quý là bạch kim, bạc trắng. Huy hiệu, sao, viền đều bạch kim.
- **Cyan là ánh sáng của nàng,** nhưng vùng cyan trên màn đã đông: tín hiệu gõ chữ ở hue khoảng 169–172° (`perfect`, `repair`), nhóm phe địch và đạn ta ở 196–202° (`volt`, `voltHi`, `shield`, `glass`, `pierce`). Đề xuất khởi đầu, phải đo trong lab: rìa sáng của nàng ở hue khoảng 188–192°, độ bão hòa ≤ 0,35 (ví dụ #a8f0ff), lõi gần trắng ngà. Vì hue gần nhau, phần tách chính là **hình** (vòng, cung, vũng mềm, dải lượn của nàng so với tường lục giác và tia phóng điện của quái), **chỗ neo** (luôn bám một phần của nàng) và **độ sáng** (nghỉ dịu). Kiểm: đặt ô màu của nàng cạnh từng token trên ở cỡ chơi; ai nhìn cũng nói được ô nào là của nàng.
- Lúc nghỉ ánh sáng của nàng dịu và nghiêng về trắng ngà, để tín hiệu Hoàn hảo vẫn là cyan sáng nhất trên màn.
- Lưng, gáy, đỉnh đầu và đỉnh vai mang toàn bộ nhận diện.
- Vùng quanh tay và lõi súng là đường bay của chữ (hệ dùng chung mức 9): hào quang ở đó luôn dịu hơn dấu chữ.

### 4.2 Ba hướng cho nữ xạ thủ

Ba hướng khác nhau về ý, không chỉ về màu: khác nét chính, khác nguồn hoàng gia hay thần thánh, khác ngôn ngữ ánh sáng. Cả ba đều dùng bảng màu ở §4.1, đều rõ là chiến binh (thế đứng, súng cầm tay, giáp), không có mặt nạ kín, không có vây ở tai. Socket chung: `FX_HAND_R/L`, `FX_CORE`, `FX_BACK_CORE`, `FX_VISOR`, thêm `FX_HALO` (tâm hào quang, đặt trên giá gắn).

**Luật dựng chung cho cả ba** (để mỗi hướng thành một model liền, phần bay sang VFX):
- **Cỡ tối thiểu của mảnh cứng:** rộng ≥ 8 cm (≥ 2 px ở 720p) theo mặt camera thấy, dày ≥ 4 cm. Mảnh mảnh hơn thì Tripo làm vỡ hay rơi [PL1, PL7] và trên màn nó nhấp nháy (§4.1). Tua, nan, dây mảnh hơn mức này chỉ là chạm nổi trên mảnh lớn, không đứng riêng.
- **Chạm thân:** mỗi mảnh cứng nối vào thân hay vào mảnh cứng khác bằng một gốc liền rộng ít nhất một phần ba chiều dài mảnh; không khe hở nhìn xuyên được ở bất kỳ góc nào trong tờ bốn góc.
- **Mặt sau là mặt chính:** camera thấy lưng, đỉnh đầu, đỉnh vai (§4.1). Mặt sau của mọi mảnh lớn (khung cánh, cổ quạt, cờ lưng) mang chi tiết, viền và kênh sáng, không để trơn.
- **Phần nào là VFX** ghi ngay trong từng hướng (mục "VFX riêng" và bảng P ở §5.1); ảnh nguồn không có phần đó.
- **Không chép nhân vật có sẵn:** mỗi hướng ghi nhân vật thương mại gần nhất và chỗ khác; giám khảo kiểm dòng này.

**So nhanh ba hướng**

| | H1 Aegis Seraph | H2 Star Regent | H3 Skyweave Warden |
|---|---|---|---|
| Nét chính (bóng đen từ sau, 68 px) | Hai khung cánh xếp hình chữ V hở ở giữa | Cổ quạt 7 nan sau đầu cộng áo choàng 3 vạt hình thang | Bốn lá cờ lưng xòe trên vai cộng quan búi tóc |
| Nét phụ / nét thứ ba (khi nghỉ) | Hào quang 3 cung / đốm | Cung hào quang trên quạt (tia chỉ khi chuỗi gõ) / hạt ngọc trai bay | Dải sáng lượn chữ S / vòng đầu mảnh |
| Nguồn | Thần hộ vệ có cánh, quán quân thánh | Vương quyền châu Âu, couture | Phi thiên, phẩm phục, tu tiên trong sci-fi |
| Ngôn ngữ ánh sáng | Khiên: sáng căng giữa các lá cánh | Vương miện: tia tỏa từ đầu | Gió: dải lượn và trận pháp |
| Hiện đại ở đâu | Khung cánh gập như cơ khí, khớp lộ, đường ghép tấm giáp | Vai cấu trúc couture, vải đứng xa thân [HG13] | Lá vai lớp lang như giáp module, viền mây cách điệu phẳng như in |
| Chiến binh ở đâu | Giáp đầy đủ nhất, tư thế khiên | Yếm vai và giáp ngực dày dưới áo choàng | Găng và ống tay giáp, đai súng ở hông |
| Rủi ro dựng | Khung cánh (B) xuyên áo choàng | Thấp nhất; cổ quạt (B) che gáy | Phụ thuộc VFX nhất; bốn cờ dễ thành nan mảnh |

#### H1 Aegis Seraph: thiên thần hộ vệ

Nguồn: cánh che chở của Isis và Nut, Nike Samothrace, Tổng lãnh Michael [TT5, TT6, TT8]; khung cánh sci-fi của Pharah [SF11]. Ý: nàng là tấm khiên của tuyến cuối; hai khung cánh xếp sau lưng là nét chính, vươn ra ngoài viền thân nên đọc rõ nhất từ sau. Hào quang là nét phụ, đốm sáng là nét thứ ba.

- **Mũ và diadem:** mũ vương miện hở mặt; một dải kính cyan mỏng ngang mắt (vẽ màu phẳng, không trong suốt, vì Tripo yếu với vật trong suốt); mào thấp ở đỉnh và sau đầu, bậc thấp dần ra hai bên, đầu bo tròn. Tóc dài sẫm thoát ra sau mũ tới bả vai.
- **Hào quang:** vòng ánh sáng chia 3 cung có khe, sau và trên đầu, neo vào một vòng cổ nhỏ ở gáy (giá gắn hình khối). Chỉ ánh sáng là VFX.
- **Khung cánh:** hai khung cánh xếp, mỗi bên 3 lá lớn hình lông vũ cách điệu, tối đa 2 tầng; gốc gắn liền tấm lưng ở mép ngoài hai bả vai, chừa khe chữ V ở giữa để camera vẫn thấy sống lưng và lõi lưng; sải 1,4–1,8 lần vai; đầu lá nâng 20–35° để nổi trên sàn khi nhìn từ trên. Mỗi lá rộng ≥ 15 cm, dày ≥ 4 cm, đầu bo tròn. Mép lá có rãnh sáng chìm; socket `FX_WING_L/R` ở đầu lá trên cùng.
- **Giáp nhiều lớp:** tấm gốm ngà ngọc trai phân đoạn trên đồ lót graphite; vai tròn vuốt ra sau, phóng 1,2–1,3 lần; viền chỉ bạch kim dọc mép 3–5 tấm lớn nhất; khớp cơ khí ở khuỷu và gối.
- **Áo choàng:** hai vạt navy hẹp từ hông tới giữa bắp chân, lót ngà, viền ngà mảnh; để lộ tấm lưng và khung cánh.
- **Kênh phát sáng:** ba kênh: dọc sống lưng tới lõi lưng, dọc gân hai khung cánh, dọc mép vạt áo; rộng ≥ 8 cm ở tỉ lệ 2,6 m.
- **Vật đính:** huy hiệu hình khiên tròn giữa hai bả vai làm lõi lưng (`FX_BACK_CORE`), rộng ≥ 9 % chiều cao (≥ 6 px ở 720p).
- **VFX riêng:** khi chuỗi gõ lên đỉnh hay khi thắng, một màng sáng mảnh căng giữa ba lá mỗi bên, hai bên ghép thành hình khiên tròn sau lưng (thân glow ≤ 0,9, chỉ mép là lõi HDR mảnh), neo ở `FX_WING_L/R` và `FX_BACK_CORE`.
- **Không chép:** gần nhất là Mercy (bộ Valkyrie) và Pharah của Overwatch [SF11]. Khác ở chỗ: cánh khép thành khiên che chở chứ không xòe như lưỡi bay; lá là gốm đặc, không có lưỡi lông vũ phát sáng kéo dài; không có cánh tay hay vũ khí kiểu y tế; bảng màu ngà, navy, cyan, không trắng–vàng; mũ hở mặt có mào thấp, không mũ chim săn.

#### H2 Star Regent: nữ vương ánh sao

Nguồn: tiara kokoshnik và vương miện tia, cổ superhumeral và hào quang của Theodora, áo choàng Garter lót tương phản, cổ đứng rebato, nơ lưng Balenciaga [HG1–HG7, HG13]. Ý: hào quang là một phần trang phục; cổ quạt đứng sau đầu là nét chính, áo choàng là mảng lớn nhất từ trên nhìn xuống. Đây là hướng gần nhất với bible hiện tại (áo choàng navy có hoa văn, lõi lưng) và ít rủi ro Tripo nhất.

- **Mũ và diadem:** diadem gồm 5–7 thanh tia thấp, dày, cao nhất ở giữa, đầu bo tròn như ngọc trai, gắn liền tóc. Không mũ kín; dải kính cyan mỏng gắn vào diadem. Diadem ở phía trước nên ở camera chơi chỉ thấy đầu tia từ trên xuống; nó phục vụ menu và chân dung, còn ở trận cổ quạt gánh phần đầu.
- **Hào quang:** khung hình khối là cổ quạt đứng 7 nan gốm viền bạch kim, từ tai này sang tai kia sau đầu, không cao quá đỉnh đầu (cao hơn vai, nên vẫn là phụ kiện B ở §7.4). Camera thấy **mặt sau** của quạt: nan nổi, viền bạch kim và kênh sáng nằm ở mặt sau và mép trên, không chỉ ở mặt trong. Mỗi nan rộng ≥ 8 cm, nối liền với nhau bằng một vành đáy. VFX: một cung sáng mảnh phía trên quạt (P3, có cả khi nghỉ), và các nan kéo dài thành 5–7 tia sáng rộng chỉ khi chuỗi gõ lên bậc.
- **Giáp nhiều lớp:** yếm vai superhumeral bằng tấm gốm chạm lỗ, viền bạch kim; vai cấu trúc kiểu couture; giáp ngực và găng dày dưới áo choàng; dải bạch kim chạm nổi dọc sống lưng và mép vai (làm trong albedo, metalness, normal).
- **Áo choàng:** navy mờ kiểu nhung nano, lót ngà ngọc trai, chia 3 vạt dừng ở giữa bắp chân, viền ngà mảnh làm fimbriation. Không kéo lê sàn.
- **Kênh phát sáng:** mép trên và các nan ở mặt sau cổ quạt, dọc sống lưng, viền vạt áo.
- **Vật đính:** ngôi sao huân chương 8 cánh bằng bạch kim giữa hai bả vai làm lõi lưng, nằm ngay dưới cổ quạt để không bị che; dây chuyền huân chương chạm nổi qua vai (chỉ là chạm nổi, ở cỡ chơi nó chỉ đọc thành ánh lấp lánh).
- **VFX riêng:** "đuôi áo ánh sáng" nối dài vạt áo trên sàn, mờ dần trong khoảng 1 m, chỉ khi di chuyển; 6–12 hạt như ngọc trai bay chậm thay cho pendilia.
- **Không chép:** không có nhân vật game cụ thể nào gần; rủi ro là chép nguyên văn trang phục lịch sử (cổ Elizabeth I, áo Garter thật). Dịch sang vật liệu sci-fi theo bẫy "Ghép thời đại" ở §3.

#### H3 Skyweave Warden: tiên nữ dệt trời

Nguồn: pibo và phi thiên Đôn Hoàng, trâm bộ diêu, phượng quan, hạc, cờ lệnh đại khải, Xianzhou [TX1, TX2, TX11–TX14, TX18]. Ý: tu tiên dịch sang công nghệ trạm. Bốn lá cờ lưng và quan là nét chính của bóng model; dải khăn ánh sáng lượn quanh thân là nét phụ và là phần chuyển động mạnh nhất; drone là phi kiếm của nàng.

- **Mũ và diadem:** quan (mũ búi tóc) bạch kim viền mây cách điệu, rộng ≥ 6–8 px ở cỡ chơi; tua bộ diêu ngắn, gắn liền, chỉ đọc thành chuyển động nhỏ.
- **Hào quang:** hai vòng: vòng đầu mảnh, và cung trên của quầng thân (mandorla) chỉ hiện khi chuỗi gõ lên đỉnh. Giá gắn là một vòng cổ cao ở gáy.
- **Giáp nhiều lớp:** vai bằng nhiều lá như lông hạc chồng nhau; áo giáp nhiều lớp có viền mây ở gấu; găng và ống tay giáp, đai súng ở hông (giữ chất chiến binh khi khăn và cờ làm hình mềm đi); tấm ngọc là vùng phát sáng trong texture (màu cyan, không dùng xanh ngọc để không trùng `perfect`).
- **Cờ lưng:** bốn lá cứng như cờ lệnh, xòe nhẹ trên bả vai, gắn liền tấm lưng, đầu bo tròn. Mỗi lá rộng ≥ 12 cm, dày ≥ 4 cm (cờ lệnh thật là cán mảnh và vải: ở đây thành tấm đặc, không có cán rời).
- **Bóng khi tắt VFX:** bóng đen của riêng model (bốn cờ, quan, lá vai) phải đọc được ở 68 px. Dải khăn sáng chỉ cộng thêm; nếu bỏ nó mà hết nhận ra thì hướng này trượt cổng bloom ở §6.
- **Dải khăn:** khăn navy và ngà vắt qua vai, vòng qua hai khuỷu, có hình khối ở chỗ chạm thân (vai, khuỷu, hông); phần bay tự do là VFX dải ánh sáng lượn chữ S chậm, rộng ≥ 3 px, vươn ra ngoài viền thân.
- **Kênh phát sáng:** gân bốn lá cờ, mép lá vai, đường nối khăn.
- **Vật đính:** lõi lưng hình hoa sen cách điệu giữa bốn lá cờ.
- **VFX riêng:** trận pháp dưới đất với chữ phù tự vẽ, không đọc được (texture art, không vẽ bằng mã), chỉ khi chuỗi gõ lên đỉnh hay khi thắng.
- **Không chép:** gần nhất là các nhân vật Xianzhou của Honkai: Star Rail (Yanqing điều kiếm bay [TX5]) và phi thiên Đôn Hoàng. Không lấy kiểu tóc, mũ, hoa văn hay bộ kiếm của nhân vật có tên nào; chỉ lấy cấu trúc (khăn bay, cờ lưng, quan) từ nguồn bảo tàng và bách khoa [TX1, TX12, TX14].

### 4.3 Ba hướng cho drone

Drone dài 0,9–1,0 m: khoảng 23–26 px ở 720p, 35–38 px ở 1080p. Drone bắn súng bến 2, bám vai phải, chuyển động bằng mã, không rig (`QR` §4.5, §4.6). Socket: `FX_EYE`, `FX_RING`, `FX_THRUST`, cộng `FX_MUZZLE` của ống phát dưới mắt. Vòng sáng của drone đổi màu theo súng bến 2, nên thân vòng giữ màu ngà trung tính và chỉ lõi sáng mang màu súng. Màu súng chỉ hiện ở lõi mảnh trong lúc nạp và phóng bến 2 (pha nạp của VFX đòn, khoảng 0,35 s); khi nghỉ vòng là ngà–cyan như nàng. Nhờ vậy khi bến 2 là Tán (hổ phách #ffc53d), drone vẫn không mang vàng bão hòa: màu đó thuộc về đòn, không thuộc về drone.

Luật dựng chung như §4.2: mọi mảnh cứng rộng ≥ 2 px ở 720p (≥ 8 cm), dày ≥ 4 cm, chạm thân; vòng trên giá nối bằng trụ, không lơ lửng.

#### D1 Halo Wisp (đi với H1)

Ý: một "thiên thần nhỏ" mang hào quang của chính nó; vòng quanh thân là nét chính.

- **Thân:** oval gốm ngà ngọc trai, đáy graphite, đường ghép mảnh.
- **Mắt:** một mắt tròn lớn, thấu kính cyan trong vành graphite, rộng ≥ 3 px ở 720p.
- **Vòng trên giá:** một vòng dày (≥ 8 cm, tức ≥ 2 px ở 720p) bao quanh eo thân, nối bằng ba thanh giằng dày; mặt trong vòng có rãnh sáng.
- **Vây:** bốn vây hình cánh hoa vuốt ra sau, đầu bo tròn.
- **VFX:** 4–6 đốm sáng chạy trên mặt phẳng của vòng.
- **Không chép:** gần nhất là Ghost của Destiny [HQ6]. Khác ở chỗ: thân là một vỏ oval liền, không phải nhiều mảnh đa diện tách quanh mắt; nhận diện nằm ở vòng quanh eo, không ở vỏ.

#### D2 Herald: người cầm cờ (đi với H2)

Ý: sashimono bay, mang ánh sáng huy hiệu phía trên và sau nàng.

- **Thân:** giọt nước nhọn hơn (`QR` §4.4), gốm ngà, khe cyan hẹp.
- **Mắt:** một mắt lớn ở đầu giọt nước.
- **Vòng trên giá:** một vòng như vương miện nhỏ trên đỉnh, nối bằng hai trụ ngắn dày.
- **Vây:** một vây đứng như lá cờ trên lưng drone mang ngôi sao 8 cánh nhỏ; hai vây ổn định ngắn hai bên.
- **VFX:** khi drone di chuyển nhanh, đầu vây cờ kéo một dải sáng như đuôi cờ.

#### D3 Lotus Blade: phi kiếm hoa sen (đi với H3)

Ý: phi kiếm của tu tiên trong dáng công nghệ; cánh hoa mở là nhịp bắn.

- **Thân:** dài như chuôi kiếm và nụ sen, gốm ngà, gân bạch kim.
- **Mắt:** một mắt ở mũi.
- **Vòng trên giá:** vòng hào quang ở đuôi, nối bằng hai trụ.
- **Vây:** sáu vây cánh hoa ôm thân, mở ra khi bắn và khép lại sau đó. Vây phải là các nút riêng trong GLB (tách bằng Tripo Segmentation hay trong Blender) để mã xoay được.
- **VFX:** 2–3 lưỡi sáng nhỏ dài 6–8 px bay vòng quanh như kiếm trận.
- **Không chép:** không lấy dáng kiếm của Yanqing hay nhân vật Xianzhou nào [TX5]; lưỡi sáng là hình thoi đơn giản của ta.

### 4.4 Đưa chủ dự án chọn

- **Mỗi hướng một bảng** (theo skill `game-character-design`):
  - ảnh mặt trước và mặt sau;
  - bóng đen ở 68 và 100 px nhìn từ camera chơi;
  - ô màu kèm tỉ lệ;
  - danh sách bộ hào quang kèm cách chia ở §7;
  - ô kiểm cỡ thật trên khung map thật;
  - một dòng ý tưởng.
- **Tự chấm theo §3 trước khi đưa;** chỉ đưa hướng mình bảo vệ được.
- **Ghép đôi gợi ý:** H1 với D1, H2 với D2, H3 với D3. Chủ dự án được ghép khác.
- **Nhận xét của tôi:**
  - H2 gần bible nhất và ít rủi ro Tripo nhất.
  - H1 có bóng từ sau lưng mạnh nhất, nhưng khung cánh và vạt áo phải chia chỗ, rủi ro xuyên lưới cao hơn.
  - H3 khác biệt nhất, nhưng dựa vào VFX nhiều nhất, nên chỉ đạt khi dải ánh sáng đạt.
- **Ghi lại hướng chủ dự án chọn và lời của chủ dự án.** Chưa có lựa chọn thì chưa vẽ tờ bốn góc.

---

## 5. Quy cách hào quang khi chơi (nữ xạ thủ và drone)

Cách dựng từng lớp nằm ở `HPV`; tên lớp P1–P10 theo skill `game-hero-presence-vfx`.

**Hai loại độ sáng** (luật bloom, `VFX` §3.5):
- **core:** lõi HDR 3–6, mảnh (≤ 1,5 px ở 720p, ≤ 2 px ở 1080p), `toneMapped: false`; là thứ duy nhất được bloom.
- **glow:** ≤ 0,9 mỗi kênh trước tone map, không bao giờ bloom. Độ mềm vẽ sẵn trong shader.

Bloom của Last Line theo nhánh `ts-wave1`: strength 0,45, radius 0,12, ngưỡng 1, tone map Neutral, MSAA 4 ở High và Ultra. Medium và Low không có bloom: hào quang vẫn phải đọc được ở đó.

Hai luật đi kèm:
- **Mỗi nhân vật tối đa một lõi HDR khi nghỉ:** nữ xạ thủ là lõi lưng, drone là mắt. Hai lõi thở lệch nửa chu kỳ, nên trên màn mỗi lúc chỉ có một đỉnh.
- **Cỡ điểm ảnh** trong bảng là điểm ảnh CSS ở 720p / 1080p. Game vẽ ở tỉ lệ điểm ảnh 1 (Low, Medium), 1,5 (High), 2 (Ultra), nên shader nhân cỡ với tỉ lệ đó (`HPV` §4.1, §4.2).

### 5.1 Lớp của nữ xạ thủ

Cỡ tính ở tỉ lệ 2,6 m; "720p / 1080p".

| Lớp | Neo | Hình và cỡ | Màu | Loại sáng | Bậc |
|---|---|---|---|---|---|
| P3 Hào quang | `FX_HALO` trên giá gắn ở gáy hay cổ quạt | Vòng chia 3–4 cung (khe 8–12°); đường kính ≈ 19 / 28 px, tức khoảng **0,5 m** ở tỉ lệ 2,6 m: mặt phẳng nhìn của camera chơi có khoảng 38 px/m ở 720p (57 ở 1080p) tại chỗ nàng; 26 px/m chỉ đúng cho chiều cao thân, vốn bị co theo cos 46°, nên vòng 0,72 m (2,2 lần đầu) ra 27 / 40 px (đo lab Last Line 01/11). Thân glow rộng 1,5–2,5 / 2,2–3,5 px, lõi 1–1,5 / 1,5–2 px. Pháp tuyến hướng về camera chơi (nghiêng khoảng 45° so với phương đứng) nên thấy gần tròn; xoay quanh trục đứng của thân theo camera; vị trí theo lò xo trễ 60–100 ms. Cung quay chậm, chu kỳ ≥ 8 s. Vòng 2 của hai giám khảo (01/11) đổi hình, chỗ đặt và chuyển động: xem ghi chú dưới bảng | Lõi trắng ngà, rìa cyan | Thân glow ≤ 0,9. **Đường vòng ≤ 0,9 ở mọi trạng thái; HDR chỉ ở các điểm lóe** (chấm ≤ 1–1,5 / 1,5–2 px ở đầu tia hay giữa cung): khi nghỉ không có; theo bậc chuỗi gõ 1,35–1,7; lúc phóng 1,5 trong ≤ 3 khung. Số cũ (lõi HDR 3–4 chạy hết đường vòng, đỉnh 5–6) làm vòng thành đĩa trắng ở 68 px: loe bloom 2,8× / 2,6× so với trần 1,5×; điểm lóe 2,5–3,5 còn loe 1,3×. Ở 1,35–1,7: loe 1,00–1,05×, ánh sáng của vòng (cả bloom) ra tới ≤ 1,1 lần cỡ vòng khi phóng, ≤ 1 khi nghỉ | Mọi bậc (Low: đứng yên) |
| P9 Lõi lưng | `FX_BACK_CORE` | Lõi ≤ 1,5 / 2 px giữa một quầng glow 3 / 4 px, trên nền graphite tối của model; vỏ trong model rộng ≥ 6 / 9 px | Trắng ngà | Lõi core HDR 3, thở 3 ± 0,4 chu kỳ 3–4 s: điểm sáng duy nhất của nàng được bloom khi nghỉ; quầng glow ≤ 0,9 | Mọi bậc |
| P2 Kênh phát sáng | Map phát sáng của model | 2–3 kênh (sống lưng, mép vạt áo, gân cánh hay cờ), rộng ≥ 2 / 3 px | Cyan nhạt | Glow 0,4–0,6 khi nghỉ. Mỗi từ gõ xong: một dải sáng chạy từ hông lên hào quang trong 0,3 s; chỉ đường giữa kênh (≤ 1,5 / 2 px) lên HDR 3 | Medium trở lên |
| P1 Viền fresnel | Vật liệu của model | Mũ 3–4, cường độ 0,25–0,4; thân trên 1×, chân 0,3× (chân tối, thân trên sáng); không phủ da mặt | Cyan ngà | Glow ≤ 0,9, không bao giờ HDR | Mọi bậc |
| P4 Đốm sáng | Tâm thân, hai dải nghiêng | Nghỉ 8–12 đốm, 2–3 / 3–4 px; bán kính 0,5–0,8 m (≈ 13–21 / 19–31 px tính từ trục); 0,15–0,3 vòng/s, có lệch pha và lệch bán kính; nhấp nháy ≤ 15 % thời gian. Mỗi bậc chuỗi gõ thêm 4 đốm, tối đa 20, nhanh ×1,5 | Ngà, vài đốm cyan | Glow; từ bậc chuỗi gõ đầu tiên, 2–3 đốm lớn nhất có lõi HDR 3 cỡ 1 px (khi nghỉ mọi đốm ≤ 0,9, vì lõi HDR duy nhất khi nghỉ là lõi lưng) | Khi nghỉ: Medium 6, High 10, Ultra 12. Trần khi chuỗi gõ: Medium 10, High 16, Ultra 20 |
| P5 Dải sáng, vệt | Đuôi khăn (H3), viền vạt áo (H2), đầu lá cánh (H1), gót | H3: 2 dải 1,2–1,8 m, rộng ≥ 3 / 4 px, lượn chữ S cả khi đứng yên; vì vậy H3 tắt đốm P4 khi nghỉ (dải khăn thay chỗ) để giữ trần ba lớp tách thân, đốm chỉ đến theo chuỗi gõ. H2: đuôi áo sáng khi di chuyển. Vệt khi trôi ngang rộng ≥ 3 px, tắt trong 0,3–0,5 s | Ngà, cyan | Thân glow; lõi giữa HDR 3 rộng ≤ 1,5 / 2 px chỉ khi di chuyển, chuỗi gõ hay hành động (dải H3 khi nghỉ: lõi ≤ 0,9) | High trở lên |
| P7 Vũng sáng dưới chân | Dưới chân | Đĩa mềm 1,0–1,2 lần chiều cao (≈ 68–80 / 100–120 px ngang, elip 0,72); **không có viền vòng** khi nghỉ; thở chu kỳ 3–4 s, ±10 % | Cyan ngà | Glow, tâm ≤ 0,35 | Mọi bậc |
| P6 Quầng thân | Quanh thân | Chỉ cung trên của mandorla, hay vỏ fresnel độ đục ≤ 0,25; chỉ khi chuỗi gõ lên đỉnh và khi thắng | Ngà | Glow | High trở lên |
| P8 Đèn | Một đèn trong kho | Không dùng khi nghỉ (kho `DECK_LIGHTS` dành cho đòn); chỉ khi thắng, ở Ultra, và chỉ khi đo cho phép | — | — | Ultra |
| P10 Méo không khí | — | Không dùng | — | — | — |

**P3 sau vòng 1 của hai giám khảo mù (01/11, trang thử Last Line, thân thế chỗ là hình nộm; chưa nghiệm thu):** số đo và lý do ở `games/typing-survival/docs/changelog/2026-11-01-presence-lab.md` §9 (nhánh `ts-presence-lab`). Tóm tắt, chưa phải quy cách chốt:
- Hình vương miện, không phải vòng có tâm: hở dưới (70°, hai đầu vuốt nhọn), khe đỉnh, hai khe hông, 4 tia ở nửa trên; không quay, gắn cứng (không lò xo: lúc trúng đòn vòng không trượt khỏi thân).
- Ở camera chơi, vạch đỏ đi ngang đầu và vai nàng (68 px ở 720p), nên vòng không đặt sau đầu mà treo xuống lưng, đỉnh vòng ngay dưới lõi lưng, cách mép dưới dải vạch đỏ ≥ 3 px ở mọi tư thế; không đặt phía trên vạch (sẽ nằm trong làn quái). `FX_BACK_CORE` trên model thật phải đủ thấp cho chỗ này.
- Lõi lưng thành một dấu hình thoi 3 × 3,8 px, glow, không HDR khi nghỉ: khi nghỉ không có gì của nàng được bloom.

### 5.2 Lớp của drone

| Lớp | Neo | Hình và cỡ | Loại sáng |
|---|---|---|---|
| Mắt | `FX_EYE` | Lõi ≤ 1,5 / 2 px giữa thấu kính glow 3 / 4 px, trên vành graphite của model | Lõi core HDR 3 (lõi HDR duy nhất của drone khi nghỉ); lúc bắn bến 2 lên 5 trong 2–3 khung (chớp ở nòng thuộc VFX đòn). Thấu kính glow ≤ 0,9 |
| Vòng | `FX_RING` | Rãnh sáng trên vòng hình khối; ngà–cyan khi nghỉ, màu súng bến 2 chỉ ở lõi khi nạp (§4.3) | Glow 0,4 khi nghỉ; lõi HDR 3 rộng ≤ 1,5 / 2 px khi nạp bến 2 |
| Động cơ | `FX_THRUST` | Quầng 2–3 px; khi lao nhanh có lõi ≤ 1,5 / 2 px và vệt ≥ 2 px tắt trong 0,25 s | Glow; lõi HDR 3 chỉ khi lao |
| Đốm hay lưỡi sáng | Mặt phẳng vòng (D1), quanh thân (D3) | D1: 4–6 đốm; D3: 2–3 lưỡi dài 6–8 px | Glow |
| Viền fresnel | Vật liệu | Cường độ 0,3 | Glow |
| Lơ lửng | Mã | Biên độ 0,03 m, 0,3 Hz; vị trí theo `QR` §4.5 | — |

### 5.3 Trạng thái

| Trạng thái | Nữ xạ thủ | Drone |
|---|---|---|
| **Nghỉ** | Hào quang glow, lõi lưng thở, đốm trôi chậm, vũng sáng thở. Không có gì nhấp nháy; tối đa một điểm nhấn sáng mỗi 2 s | Mắt HDR 3, vòng glow 0,4, lơ lửng |
| **Sẵn sàng, chuỗi gõ** | Mỗi bậc chuỗi gõ: lõi hào quang lên một nấc (≤ 0,9 → 3 → 4), thêm đốm. Ở bậc cao nhất: cung mandorla, lông vũ hay tia hay trận pháp theo hướng | Vòng sáng dần theo chuỗi (`QR` §4.6 mục 6) |
| **Di chuyển** (trôi ngang ±1,6 m) | Áo choàng theo xương lò xo; vệt từ đuôi áo hay gót; đốm trễ theo lò xo; vũng sáng đi theo | Nghiêng theo hướng; vệt động cơ khi lao |
| **Bắn** (Load 0,35 s, rồi phóng) | Hào quang và dải sáng sống lưng phồng theo pha phóng của đòn rồi lắng trong 150–300 ms. Đốm **không** bay vào súng (đường đó là của chữ); chúng chỉ siết quỹ đạo còn 0,8 | Vây D3 mở; mắt lên 5 trong 2–3 khung |
| **Trúng đòn** (`playerHit`, `breach`, `drain`) | Hào quang và viền hạ còn 50 % trong ≤ 100 ms rồi về; `breach`: hào quang tắt 200 ms rồi bật lại; `drain`: đốm chậm và mờ theo lượng giáp mất. Không dùng đỏ trên nàng | Khiên lục giác lam phía trước nàng (`QR` §4.6 mục 4). Quái mang khiên đã có tường năng lượng `shield` #4fc8ff: khiên của ta phải khác cả hình lẫn màu (ví dụ cung cong ngà–cyan neo ở drone, không phải tường phẳng lam), kẻo người chơi đọc nhầm phe |
| **Giáp thấp** | Mờ, giảm bão hòa, chậm lại; còn 4 đốm. HUD lo báo động, không nhấp nháy | Vòng mờ |
| **Thắng** | Đốm xoáy vào, hào quang đỉnh HDR 5 trong ≤ 3 khung rồi giữ 3; cung mandorla hiện | Bay vòng quanh nàng |
| **Thua** | Tắt lần lượt: đốm rơi, hào quang mờ trong 600 ms, lõi lưng tắt cuối | Rơi xuống, tắt đèn cạnh nàng đang quỳ |

Chuyển giữa trạng thái êm ≥ 150 ms, trừ trúng đòn và lúc phóng.

### 5.4 Giới hạn

Đây là trần khởi đầu; số đo của game thắng khi đã đo. Trần chi phí ở `HPV` §5, cách đo ở `HPV` §7.

| Mục | Trần |
|---|---|
| Thứ tự sáng | Nền < hào quang nghỉ < sẵn sàng < phản hồi đòn < thẻ chữ và khung học |
| Thời gian khung | Mỗi lớp ≤ 0,25 ms; cả hào quang một nhân vật ≤ 0,75 ms và ≤ 25 % khoảng trống VFX đo được, ở bậc mặc định 1080p |
| Trắng xóa | Riêng hào quang: điểm ảnh độ sáng ≥ 0,95 chiếm ≤ 1 % sân |
| Vùng cần bảo vệ | Dải chữ, khung học, cảnh báo của quái, HUD, đường chữ bay vào `FX_CORE` của súng: thêm ≤ 10 % độ sáng |
| Tương phản thẻ chữ | ≥ 7 : 1 ở p99 khi hào quang bật |
| Độ loe bloom | Lõi mảnh rộng ra ≤ 1,5 lần khi bật bloom |
| Chớp | ≤ 2 lần mỗi giây trên toàn màn |
| Khung đầu | Chớp lúc đổi trạng thái đạt ≥ 95 % đỉnh ngay ở tuổi 0 |
| Gõ chữ | Chạy lại `survival-feel` khi bật hào quang: f8 và nền dưới dòng chữ tăng ≤ +0,02 (`QR` §4.7). Đổi thấy được ở dấu gõ là đổi hệ dùng chung: hai giám khảo từ 9, chủ dự án ký |
| Giảm chuyển động | Theo `motionReduced()`: viền và hào quang giữ (hào quang không quay); kênh sáng, đốm, dải sáng, quầng làm dịu; méo không khí bỏ. Mức chuỗi gõ luôn giữ dưới dạng độ sáng đứng yên |

---

## 6. Cách chấm

**Ai và ở đâu:**
- Hai giám khảo mù độc lập, cả hai từ 8,5 (`ART_ACCEPTANCE.md`). Animation nhân vật là hệ dùng chung: cả hai từ 9, không hạng mục con nào dưới 8,5, chủ dự án ký cuối.
- Chấm cuối trên bản chơi đã build, đúng cài đặt của người chơi, không tham số URL. Trang thử (lab) chỉ để lọc.
- Không "tốt nhất sau 3 lượt", không "tốt hơn bản cũ".

**Ba điểm, chấm cạnh nhau:**

| Điểm | Câu hỏi | Trượt khi |
|---|---|---|
| **Mức thị trường** | Đặt cạnh bảng tham chiếu thương mại có đứng được không? | Trông như đồ chơi, nhựa, hay như bản nháp |
| **Sức hút** | Cuốn hút, phong cách, sang trọng, thời trang, hiện đại, giàu chi tiết có lớp lang? | Đơn giản, trơn, chung chung, kể cả khi không sai gì. **Đơn giản là trượt 8,5** |
| **Độ đọc** | Ở 68 và 100 px với HUD, dải chữ và VFX đòn bật: bóng, điểm nhấn, vai trò, bạn hay thù có rõ không? | Phải phóng mới thấy, lẫn vào sàn, giống quái, hào quang che chữ |

Mỗi giám khảo điền phiếu §3.2 trước khi cho điểm. Cộng các tiêu chí của skill `game-character-design`: đúng đề, hợp bộ, hình khối, hợp bước sau, nhất quán giữa các góc (bộ nhiều góc lệch một chi tiết là trượt).

**Bảng tham chiếu:** chọn theo nguyên tắc, không chép. Ví dụ: lưng nhân vật NIKKE và Stellar Blade (thiết kế cho góc sau); áo choàng của Destiny; Warframe Prime (kim loại quý làm viền; ở Last Line dịch thành bạch kim, không vàng); Mercy và Pharah (khung cánh); nhân vật Xianzhou (tu tiên trong sci-fi). Bảng tham chiếu cũng là danh sách để giám khảo kiểm "có giống nhân vật nào quá không" (dòng "Không chép" ở §4.2, §4.3).

**Giám khảo nhận:**
- tờ bốn góc;
- bóng đen ở cỡ chơi;
- bốn ảnh chơi theo thứ tự cổng: bóng đen → màu phẳng → thêm lõi phát sáng → thêm bloom, ở 68, 84 và 100 px;
- ảnh xám ở cỡ chơi;
- ảnh cắt 2×;
- clip thật khoảng 3 s cho từng trạng thái ở §5.3;
- bảng tham chiếu.

Không nhận prompt hay báo cáo của làn làm. Nhãn trung tính (A, B, C), chìa khóa để ngoài thư mục giám khảo. Mỗi người viết thấy gì trước khi cho điểm.

**Cổng bloom:** tắt bloom mà nhân vật hết đẹp thì lỗi ở hình khối, không sửa bằng ánh sáng.

**Dưới 8,5:** ghi năm sửa cụ thể nhất và sửa đúng lỗi đó. Hai lượt không tiến thì đổi cách (nghiên cứu thêm, tham chiếu tốt hơn, nguồn có sẵn, công cụ khác), không vẽ lại cùng cách.

---

## 7. Quyết định đường ống

### 7.1 Câu hỏi

Chủ dự án, tối 01/11, sau khi thấy vòng sáng vẽ thẳng vào ảnh nhân vật:

> "bạn nên tìm hiểu xem cách nào làm đúng, vì tôi k biết làm gộp thành 1 ảnh như bạn thì là đúng, hay là cách khác mới đúng và hiệu quả"

Chủ dự án không chỉ định cách; chủ dự án muốn cách đúng, có bằng chứng, để thôi phải vẽ lại cùng một ảnh.

### 7.2 Bốn cách

| Cách | Trong ảnh nguồn và model | Trong engine |
|---|---|---|
| **A** | Mọi thứ: hào quang, ánh sáng, đốm | Không gì thêm |
| **B** | Thân sạch; mảnh cứng lớn (vương miện lưng, khung cánh, giá hào quang) là phụ kiện riêng, một vật liền, gắn cứng vào xương | Ánh sáng, đốm, dải sáng |
| **C** | Hào quang hay mảnh cứng là một phần hình khối của thân | Ánh sáng, đốm |
| **D** | Chỉ thân | Toàn bộ bộ hào quang |

### 7.3 Bằng chứng theo tiêu chí

| Tiêu chí | A | B | C | D |
|---|---|---|---|---|
| **Tripo** | Tripo tự nhận phần mảnh hỏng vì ít dữ liệu huấn luyện và topology vỡ [PL1, PL7]; nhiều chủ thể bị gộp [PL6]; tách theo độ liền thì mảnh bay thành phần riêng [PL2]; chế độ parts không đi cùng texture, PBR [PL3]. Vòng mảnh bị dính hay rơi mất | Mỗi phần là một vật liền. Tripo tự khuyên tách thân và quần áo khi tạo nhân vật, và tách phần cứng trước khi rig [PL6, PL9]; blog Tripo ghép phần trong Blender [PL10] | Mảnh đặc, rộng, chạm thân thì được nếu đủ dày; vòng mảnh hỏng như A. Thiếu ảnh sau lưng thì Tripo bịa cấu trúc trên lưng [PL6] | Không có gì thêm |
| **Ánh sáng trong ảnh nguồn** | Bộ tạo texture 3D hiện có chỉ ra map PBR không phát sáng [PL4]; Tripo không xuất map phát sáng làm đầu ra chính [PL5]; nên ánh sáng vẽ rơi vào albedo (suy luận). Thành sơn phẳng: không bloom được, không đổi theo chuỗi gõ | Không có | Không có | Không có |
| **Rig** | Phần bay trong cùng lưới không chuyển động riêng được | Gắn cứng: trọng số 1,0 vào một xương, hay làm con của `Bone` [PL15]; giống prefab hào quang gắn xương đầu [HQ16], socket Unreal [HQ17], AccuRIG biến mảnh cứng tách sẵn thành phụ kiện gắn vào xương tương ứng để giữ cứng, và khuyên tách trái, phải để gắn đúng xương [PL14]. Rig Mesh2Motion của ta vốn đã khóa mũ và các tấm giáp vào xương (`QR` §4.3) | Trọng số tự động (bone heat) dễ trải mảnh lưng lớn sang vai; phải sửa tay trong Blender | Không đụng rig |
| **Đọc ở 68–100 px** | Vòng hình khối mảnh < 1 px thì nhấp nháy [HQ15] | Mảnh đặc ≥ 3 px đọc tốt; vòng sáng là vòng shader có khử răng cưa | Hướng cố định: vòng đứng sau đầu chỉ còn cos 46° ≈ 0,69, không thể vừa tròn ở camera chơi vừa đúng ở menu | Vòng shader xoay theo từng camera nên luôn gần tròn; nhưng billboard trôi tự do trông như dán lên |
| **Luật bloom** | Không theo được (sơn ≤ 1) | Theo được: lõi HDR và glow ở VFX | Theo được ở phần VFX | Dễ theo nhất |
| **Chi phí khung** | Thấp nhất | +1 draw call cho phụ kiện, +2 cho vòng shader; ước tính dưới 0,05 ms, chưa đo | Như B, bớt một draw call | Như B |
| **Tốc độ vòng sửa** | Mỗi lần sửa: ảnh nguồn mới, Tripo (khoảng 40 credit), Blender, rig, chấm lại | Ánh sáng: vài phút, không tốn credit. Phụ kiện: một lần Tripo cho riêng phụ kiện, không đụng thân | Mỗi lần sửa mảnh: tạo lại cả thân, rig lại, chấm lại cả nhân vật | Vài phút |
| **Thực tế ngành** | Không game nào làm thế; giám khảo K của Tu Tiên trừ điểm lông vũ rời (`docs/games/tu-tien/art-requests/demo1/judging/judge-K.md`); brief của ta đã cấm dây mảnh và mảnh bay (`docs/games/dragon-lane/art-requests/m0/03-pine-river-props.md`) | Warframe tách giáp, syandana, ephemera [HQ5]; Destiny tách hạt, shader lưới, vải [HQ13, HQ14]; League làm 95 % bằng hạt lưới có shader [HQ12] | Dùng cho mào và vương miện đặc | Ephemera, skin phản ứng, giáp Solstice [HQ5, HQ8, SF10] |

### 7.4 Quyết định

**Luật chung cho mọi nhân vật:**

1. **Ánh sáng không bao giờ vẽ vào ảnh nguồn hay model.** Phần phát sáng chỉ vẽ màu phẳng (ví dụ cyan nhạt phẳng) để sau này làm mặt nạ phát sáng.
2. **Mảnh cứng chạm thân, thấp và đặc** (mào, diadem, vương miện, cổ đứng thấp, vây lưng ngắn, cờ lưng ngắn, giá hào quang ở gáy, kênh sáng chìm) nằm trong model thân: **C**.
3. **Mảnh cứng lớn đứng tách khỏi thân** (vương miện lưng, khung cánh, cổ quạt cao, vòng trên giá của drone khi Tripo không giữ nổi) là **phụ kiện riêng: B**. Phụ kiện là một vật liền, chạm thân (không có khe), gắn cứng vào một xương trong Blender (trọng số 1,0) và xuất cùng GLB của nhân vật.
4. **Mọi thứ bay, quay, phát sáng hay đổi theo trạng thái là VFX: D.** Gồm: vòng sáng của hào quang, tia, quầng thân, đốm, dải sáng nối dài khăn, vệt, viền fresnel, vũng sáng, nhịp sáng.
5. **Luật cầu nối:** mỗi lớp VFX bắt đầu từ một phần của model (giá gắn, đầu vây, đuôi khăn, socket). Không có billboard trôi tự do.
6. **Vải chuyển động** (áo choàng, khăn, tóc) là hình khối có chuỗi xương lò xo (animation nhân vật, mức 9); phần bay tự do sau mép vải là VFX.

Tóm gọn: **B + D, C cho phần dính thân. Loại A.**

**Áp cho Last Line:**

| Phần | Cách | Ghi chú |
|---|---|---|
| Thân, mũ hay diadem, giáp, kênh sáng chìm, áo choàng (3 vạt), tóc | C | Một model Tripo đa góc (trước, trái, sau, phải), A-pose. Kênh sáng vẽ màu phẳng |
| Giá hào quang ở gáy (vòng cổ nhỏ), lõi lưng, cờ lưng ngắn (H3) | C | Đặc, chạm thân |
| Khung cánh (H1), cổ quạt cao (H2) | B | Phụ kiện riêng, một lần Tripo; gắn cứng vào xương ngực trên trong Blender |
| Vòng sáng hào quang, tia, cung mandorla | D | Vòng shader neo ở `FX_HALO` |
| Đốm, dải sáng, vệt, viền, vũng sáng, nhịp sáng | D | Theo §5 |
| Thân drone, mắt, vây | Model | Drone không rig; vây D3 là các nút riêng để mã xoay |
| Vòng trên giá của drone | C trước, B nếu cần | Thử trong lần Tripo của drone với giá dày; nếu dính, vỡ hay mảnh dưới 2 px thì dựng vỏ vòng trong Blender, nối liền thân. Không dựng vỏ vòng bằng hình học sinh từ mã (đó là hình vẽ tạm bằng mã, `AGENTS.md`) |
| Ánh sáng của drone | D | Theo §5.2 |

**Áp cho game khác:**
- **Dragonhold, Draconis:** sừng, mào và vây là hình khối (C); `FX_HALO`, `FX_CORE`, socket cánh có sẵn cho ánh sáng (D); dải lửa đầu cánh có sẵn ở làn VFX.
- **Tu Tiên:** yêu cầu ảnh hiện tại đã tách đúng hướng này: ảnh nguồn không có aura, ánh sáng phát ra, hạt hay vật trang trí bay (`docs/games/tu-tien/art-requests/m0b/00-identity.md`, `01-cultivators-bots.md`).
- **Wordwoven (2D):** ảnh nhân vật không vẽ hào quang; hào quang là lớp sprite riêng vẽ ở chế độ `lighter` (`VFX` §3.5). Luật cầu nối vẫn áp.

### 7.5 Vì sao, và chỗ tôi không theo ghi chú

**Vì sao chọn B + D:**
- Chính nhà làm công cụ nhận phần mảnh hỏng [PL1, PL7], và chính họ khuyên tách phần [PL6, PL9].
- Ánh sáng vẽ sẵn rơi vào albedo (bộ tạo texture 3D chỉ ra map không phát sáng [PL4, PL5]), nên không bloom và không đổi theo chuỗi gõ được.
- Game thương mại tách giáp gắn, vải và hạt [HQ5, HQ13, HQ14].
- Hình khối dưới 1 px nhấp nháy [HQ15]; vòng shader giữ được độ rộng tối thiểu.
- Camera cố định 46° là lý do mạnh nhất cho D: chỉ vòng VFX mới vừa tròn ở camera chơi vừa đúng ở menu và chân dung.
- Sửa ánh sáng mất vài phút; sửa model tốn credit và một vòng chấm.

**Chỗ tôi không theo ghi chú:**

| Ghi chú nói | Tôi chọn | Lý do |
|---|---|---|
| Ghi chú hào quang: nghiêng vòng khoảng 20° về camera | Khoảng 45° | Ở 46° vòng đứng chỉ còn 0,69; nghiêng 45° thì gần tròn |
| Ghi chú thư viện: vòng nằm trên đỉnh đầu (kiểu Phục Hưng) | Sau và trên đầu, bao lấy đầu trên màn | Vòng nằm ngang trên đầu dễ đọc thành dấu chọn đơn vị (ghi chú thư viện tự nhận đây là suy luận); vòng bao đầu là hình hào quang kinh điển |
| Ghi chú tu tiên: trận pháp dưới đất là cách đọc mạnh nhất | Chỉ khi chuỗi gõ lên đỉnh hay khi thắng | Khi nghỉ nó lẫn với vòng điểm rơi Star Mortar và cảnh báo của quái (ví dụ Arcane Comet của Riot [SF1]) |
| Ghi chú hào quang: vũng sáng thở 0,5–1 Hz, đốm 0,3–0,6 vòng/s | Thở 3–4 s; đốm 0,15–0,3 vòng/s | Nhanh thì đọc thành côn trùng hay báo động; lúc nghỉ phải dịu [SF1] |
| Ghi chú thư viện: tốn một lần Tripo (khoảng 40 credit) để thử vẽ hào quang vào ảnh nguồn | Không làm | Bằng chứng đã đủ (tài liệu Tripo, brief và giám khảo của ta). Dùng credit đó cho phép thử B ở §7.7 |
| Ghi chú kiểm ChatGPT: phương án B hay C cho vương miện lưng tùy cách đọc luật | B cho mảnh lớn, C cho mảnh dính thân | Mục đích của luật "một vật liền" là Tripo không gộp hay làm rơi mảnh bay; B giữ đúng mục đích đó (§7.8) |

### 7.6 Các bước

| Bước | Ai | Công cụ | Việc | Kiểm để qua bước |
|---|---|---|---|---|
| 0 | Claude | Mã game, `scene.ts`, `theme.ts` | Đo cỡ trên màn, mặt camera thấy, màu dành riêng | Số đo nằm đầu brief (như §4.1) |
| 1 | Claude, ChatGPT làm ý kiến thứ hai | Web; ChatGPT chế độ Chat, mức High | Ghi chú nghiên cứu theo các lăng kính ở §2 | Mỗi ý có đường dẫn; ý chính của ChatGPT đã mở nguồn kiểm; ghi rõ chỗ không đồng ý |
| 2 | Claude | §3 | Brief theo danh sách kiểm, rồi prompt theo §3.1 | 12 mục đều có lựa chọn cụ thể; bảng chia B, C, D có socket; prompt có đủ câu cấm |
| 3 | Claude điều khiển ChatGPT (Gemini khi ChatGPT hết lượt ảnh) | Tab trình duyệt riêng | 2–3 bảng hướng (§4.4) | Tự chấm theo §3; chủ dự án chọn |
| 4 | Như bước 3, cùng một cuộc chat | ChatGPT | Tờ bốn góc rồi từng góc (trước, trái, sau, phải; A-pose; ánh sáng phẳng; nền khóa màu; không ánh sáng vẽ). Phụ kiện B có tờ riêng (trước, sau, cạnh). Drone: trước, sau, trái, trên | Kiểm nhất quán (danh sách chi tiết, chiều cao lệch ≤ 3 %, ảnh sau đúng là ảnh sau); ô kiểm cỡ thật; hai giám khảo mù từ 8,5, gồm cả độ hợp Tripo |
| 5 | Claude | `tripo` CLI (ví API) trước, web Tripo nếu thiếu tính năng | Thân đa góc, texture HD, PBR; `face_limit` theo `LESSONS` §4 (nhân vật chính 50k, phụ kiện và drone theo lớp súng 15k trừ khi bảng đó ghi khác). Chạy `--dry-run` trước; dựng một model, kiểm rồi mới dựng tiếp | Mỗi model một thành phần liền; số tam giác; còn normal và roughness map; vòng quay; không có cấu trúc bịa trên lưng |
| 6 | Claude | Blender | Dọn lưới, đổi sang mét, làm bậc theo `MODEL_QUALITY.md`; rig Mesh2Motion (66 xương), bone heat, khóa mũ và tấm giáp; chuỗi xương áo choàng (3 vạt × 4 xương) và tóc; gắn phụ kiện B trọng số 1,0 vào xương ngực trên; tách mặt nạ phát sáng từ vùng màu phẳng rồi sửa tay; đặt socket | Anim Lab: chạy bộ clip (nghỉ, trôi ngang, Load, trúng đòn, quỳ), không xuyên lưới (áo choàng với chân và súng, phụ kiện với áo choàng và tóc); đủ socket theo hợp đồng |
| 7 | Claude | Lab trong game (`HPV` §7) | Dựng từng lớp hào quang ở §5, có công tắc riêng | Bảng đo của `HPV` §7 (loại sáng, độ loe bloom, trắng xóa, vùng bảo vệ, 7 : 1, bóng rõ hơn, ms) trong trần ở `HPV` §5 |
| 8 | Claude | Bản chơi | Ghép ở camera chơi; cổng bóng đen → màu phẳng → lõi phát sáng → bloom ở 68, 84 và 100 px; chạy lại đo gõ chữ | Tắt bloom vẫn đẹp; `survival-feel` trong trần |
| 9 | Hai giám khảo mù, chủ dự án | Bản chơi đã build | Chấm theo §6 | Model và hào quang từ 8,5; animation từ 9; chủ dự án ký |

### 7.7 Phép thử xác nhận

Phép thử nhỏ, trước khi tốn credit cho cả bộ.

**T1: vòng sáng (D so với C).**
- **Dựng:** trong trang lab dev của Last Line (không phát hành), dùng hình nộm Mesh2Motion (`human-base-animations.glb`, CC0) phóng 2,6 m. Gắn ba kiểu hào quang:
  - a) vòng xuyến hình khối dày 2–3 cm, đại diện cho C;
  - b) vòng shader SDF có độ rộng điểm ảnh tối thiểu, đại diện cho D;
  - c) billboard texture trôi tự do.
- **Chụp:** 720p và 1080p, High và Ultra, camera chơi và camera menu; nghỉ, trôi ngang, xoay thân nhắm ±50°; 24 khung mỗi cảnh.
- **D đạt khi:**
  - hình vòng liền trong 10/10 khung;
  - không nhấp nháy: độ phủ điểm ảnh của vòng lệch ≤ 10 % giữa các khung;
  - thêm ≤ 0,2 ms;
  - hai giám khảo mù xếp b trên a và c.
- **Kết quả này chỉ để lọc;** nghiệm thu thật vẫn ở bước 9.

**T2: phụ kiện riêng (B so với C).**
- **Dựng:** khi chủ dự án đã chọn hướng, một lần Tripo (khoảng 40 credit) cho riêng phụ kiện lớn của hướng đó (khung cánh H1 hay cổ quạt H2).
- **Kiểm:**
  - một thành phần liền, đủ tam giác, còn normal và roughness map;
  - gắn trọng số 1,0 vào xương ngực trên trong dưới 1 giờ;
  - chạy bộ clip ở Anim Lab, không xuyên áo choàng hay tóc.
- **So:** với cùng phần nếu nằm trong lần tạo thân (C): Tripo có làm dính, bịa thêm, và trọng số tự động có trải sang vai không.
- **B đạt khi:** phụ kiện sạch sau một lần tạo và gắn không xuyên lưới. Nếu Tripo giữ phần đó sạch ngay trong thân thì C vẫn được dùng cho phần đó.

### 7.8 Câu cần quyết

1. **Luật "một vật liền, không phần bay": đã chốt.** Chủ dự án 01/11 khoảng 21:45: "Cho phép" phụ kiện B (một vật liền, chạm thân, gắn cứng vào xương, cùng một GLB). Đề xuất: được, vì giữ đúng mục đích của luật. Nếu không, mọi mảnh lớn làm theo C và tốn thêm một lần tạo thân cho mỗi lần sửa.
2. **Tỉ lệ 2,6 m** (`QR` §4.2 mục 3): mọi số ở §4 và §5 tính theo tỉ lệ này.
3. **Hướng nhân vật và drone** (§4.4).
4. **Nếu sau này dùng Hunyuan3D:** bản 2.0 dùng "Tencent Hunyuan 3D 2.0 Community License" (21/01/2025): không áp dụng ở EU, Anh và Hàn Quốc, và bên dùng có trên 1 triệu người dùng tháng phải xin giấy phép riêng (https://github.com/Tencent-Hunyuan/Hunyuan3D-2/blob/main/LICENSE, đã kiểm 01/11). Bản khác phải đọc lại LICENSE của bản đó.

---

## Nguồn

### Trong repo

- `docs/games/QUALITY_RESCUE_2026-11-01.md` §2.3, §3, §4.1–4.8
- `docs/games/VFX_STANDARD.md` §3.5–3.8, §4.1, §4.3
- `docs/games/LESSONS_FROM_THREE_GAMES.md` §4, §5, §11
- `docs/games/ART_ACCEPTANCE.md`, `SHARED_SYSTEMS_BAR.md`, `MODEL_QUALITY.md`, `CHARACTER_ANIMATION.md` §5.3, `MONSTER_MODEL_INVENTORY.md`
- `docs/games/tu-tien/art-requests/m0b/` (ảnh nguồn không có aura), `docs/games/tu-tien/art-requests/demo1/judging/judge-K.md`, `docs/games/dragon-lane/art-requests/m0/03-pine-river-props.md`
- `games/typing-survival/src/view/scene.ts`, `theme.ts`, `gun-rules.ts` (nhánh `ts-wave1`: `BLOOM`)
- `shared/game-kit/three/model-contracts.ts`, `particles.ts`, `materials.ts`
- Skill: `.agents/skills/game-character-design/`, `.agents/skills/game-hero-presence-vfx/`

### Thần thoại (TT)

- TT1 https://en.wikipedia.org/wiki/Halo_(religious_iconography)
- TT2 https://en.wikipedia.org/wiki/Aureola · https://www.encyclopedia.com/religion/encyclopedias-almanacs-transcripts-and-maps/aureole-nimbus
- TT3 https://www.metmuseum.org/art/collection/search/39995 (không mở được, HTTP 429) · https://projects.mcah.columbia.edu/jaanus/record/karuraen
- TT4 https://www.getty.edu/research/institute/standards/cdwa/examples/70_Indian_sculpture.html
- TT5 https://www.metmuseum.org/art/collection/search/552609
- TT6 https://en.wikipedia.org/wiki/Winged_Victory_of_Samothrace
- TT7 https://christianiconography.info/seraphim.html · https://buffaloah.com/a/DCTNRY/icon/angels.html
- TT8 https://www.betsyporter.com/?p=776 · https://en.wikipedia.org/wiki/Joan_of_Arc_at_the_Coronation_of_Charles_VII
- TT9 https://www.worldhistory.org/article/785/athena-parthenos-by-phidias/
- TT10 https://www.metmuseum.org/art/collection/search/61509 · https://pages.vassar.edu/embodyingcompassion/2014/09/24/image-7/
- TT11 https://metmuseum.org/art/collection/search/640971 · https://en.wikipedia.org/wiki/Queen_Mother_of_the_West
- TT12 https://en.unesco.org/silkroad/silk-road-themes/mouvable-heritage-and-museums/fuxi-and-nuwa
- TT13 https://www.metmuseum.org/art/collection/search/924661
- TT14 https://en.wikipedia.org/wiki/Ngoc_Lu_drum · https://en.wikipedia.org/wiki/Vietnamese_dragon
- TT15 https://vietnamnet.vn/nhieu-nguoi-bac-ghe-hau-thanh-ma-khong-biet-hau-ai-2221300.html · https://en.wikipedia.org/wiki/Th%C3%A1nh_Gi%C3%B3ng
- TT16 https://historyskills.com/classroom/year-8/viking-helmets (mũ sừng là sáng tác của thế kỷ 19)

### Tu tiên (TX)

- TX1 https://en.wikipedia.org/wiki/Pibo
- TX2 https://en.chinaculture.org/library/2008-02/04/content_25914.htm
- TX3 https://en.wikipedia.org/wiki/Xianxia
- TX4 https://wuxiasociety.com/huanzhu-louzhu-novels/
- TX5 https://www.siliconera.com/heres-what-yanqing-can-do-in-honkai-star-rail/
- TX6 https://en.wikipedia.org/wiki/Fulu
- TX7 https://en.wikipedia.org/wiki/Xiangyun_(Auspicious_clouds)
- TX8 https://en.wikipedia.org/wiki/Lotus_throne
- TX9 https://www.sothebys.com/en/articles/four-ways-chinese-jade-became-the-quintessential-symbol-of-social-values
- TX10 https://www.siliconera.com/xiao-concept-art-and-design-details-focus-on-the-mighty-and-illuminated-adeptus/
- TX11 https://en.wikipedia.org/wiki/Buyao
- TX12 https://en.wikipedia.org/wiki/Fengguan
- TX13 https://en.wikipedia.org/wiki/Red-crowned_crane · https://en.wikipedia.org/wiki/Hechang
- TX14 https://www.roots.gov.sg/collection-landing/listing/1155531
- TX15 https://en.wikipedia.org/wiki/Peking_opera
- TX16 https://en.wikipedia.org/wiki/Hero_(2002_film)
- TX17 https://gamingcypher.com/naraka-bladepoint-interview · https://blogs.qub.ac.uk/eutopiafilmfest/2025/03/17/ne-zha-2-the-modern-breakthrough-and-aesthetic-reconstruction-of-eastern-mythology/ · https://animonlifeofficial.com/genshin-impact-info/1tsn2rgqwixckjr723bx8sb6fjdaj1
- TX18 https://www.siliconera.com/?p=962103
- TX19 https://siliconera.com/?p=912170 (Yun Jin: kinh kịch pha thời trang thường ngày)
- TX20 https://www.buddhistdoor.net/?p=19179

### Hoàng gia (HG)

- HG1 https://en.wikipedia.org/wiki/Radiate_crown
- HG2 https://www.thecourtjeweller.com/2017/05/queen-alexandras-kokoshnik-tiara.html · https://www.sothebys.com/en/articles/the-story-of-tiaras-a-history-of-elegance
- HG3 https://www.dailyartmagazine.com/san-vitale-mosaics/ · https://en.wikipedia.org/wiki/Basilica_of_San_Vitale
- HG4 https://en.wikipedia.org/wiki/Holy_Crown_of_Hungary · https://www.metmuseum.org/exhibitions/listings/2012/byzantium-and-islam/blog/topical-essays/posts/san-vitale
- HG5 https://fashionhistory.fitnyc.edu/545-549-san-vitale/ · https://en.wikipedia.org/wiki/Loros
- HG6 https://www.britannica.com/topic/rabato · https://en.wikipedia.org/wiki/Supportasse
- HG7 https://debretts.com/directories/orders-of-knighthood-and-chivalry/the-most-noble-order-of-the-garter/ · https://www.stgeorges-windsor.org/wp-content/uploads/2017/08/ResearchGuide1-The-Order-of-the-Garter.pdf
- HG8 https://sothebys.com/en/articles/a-royal-tradition-the-history-of-the-order-of-the-garter
- HG9 https://www.metmuseum.org/art/collection/search/22741 · https://www.metmuseum.org/essays/fire-gilding-of-arms-and-armor · https://www.metmuseum.org/met-publications/heroic-armor-of-the-italian-renaissance-filippo-negroli-and-his-contemporaries
- HG10 https://en.wikipedia.org/wiki/Kabuto · https://www.metmuseum.org/art/collection/search/27610
- HG11 https://artsandculture.google.com/asset/back-side-of-o-yoroi-armour/TgGqZ0qqU9pudA · https://en.wikipedia.org/wiki/Horo_(cloak) · https://www.metmuseum.org/exhibitions/listings/2009/art-of-the-samurai/photo-gallery
- HG12 https://en.wikipedia.org/wiki/Rule_of_tincture · https://en.wikipedia.org/wiki/Fimbriation
- HG13 https://www.vam.ac.uk/articles/secrets-of-balenciagas-construction · https://www.inkl.com/news/alexander-mcqueen-savage-beauty-review-superficially-magnificent · https://vogue.sg/iris-van-herpen-sculpting-the-senses-exhibition/
- HG14 https://gamingbolt.com/destinys-mythic-sci-fi-direction-gave-us-this-freedom-bungie

### Sci-fi và thiết kế game (SF)

- SF1 https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/ (12/03/2021; tôi đã mở kiểm)
- SF2 https://cdn.steamstatic.com/apps/valve/2008/GDC2008_StylizationWithAPurpose_TF2.pdf
- SF3 https://help.steampowered.com/faqs/view/0688-7692-4D5A-1935 (Dota 2 Character Art Guide)
- SF4 https://www.destructoid.com/how-taylor-swift-and-janet-jackson-helped-inspire-warframes-octavia-prime/ · https://www.warframe.com/news/prime-design-grendel-prime
- SF5 https://www.warframe.com/news/tennocon-2024-artists-deep-dive
- SF6 https://www.cookandbecker.com/en/article/133/the-art-of-destiny-2.html
- SF7 https://en.wikipedia.org/wiki/Commander_Shepard
- SF8 https://archive.runeterra.net/na/riot-official/Queo3flb
- SF9 https://playvalorant.com/en-us/news/dev/future-vision-the-glitchpop-story/
- SF10 https://mp1st.com/news/destiny-2-solstice-of-heroes-armor-discussed-by-bungie-fourth-armor-glow-tied-to-new-expansion
- SF11 https://en.wikipedia.org/wiki/Mercy_(Overwatch) · https://en.wikipedia.org/wiki/Pharah
- SF12 https://cookandbecker.com/en/article/378/designing-overwatch.html · https://www.leagueoflegends.com/en-us/news/dev/ask-riot-let-s-talk-clarity/ · https://gdcvault.com/play/1024268/
- SF13 https://www.cs.princeton.edu/courses/archive/fall07/cos597B/papers/mitchell-team-fortress.pdf
- SF14 https://gamesradar.com/stellar-blade-dev-also-known-for-butt-jiggling-game-nikke-says-he-put-special-attention-into-the-female-leads-back-because-thats-what-players-see-most-of-the-time
- SF15 https://80.lv/articles/comparing-team-fortress-2-and-overwatch-art-direction

### Hào quang (HQ)

- HQ1 https://collections.lacma.org/object/34041
- HQ2 https://wiki.teamfortress.com/wiki/Artstyle · https://www.gamedeveloper.com/art/in-depth-how-valve-makes-art-to-enhance-gameplay
- HQ3 https://polycount.com/discussion/comment/1598147
- HQ4 https://di.diablowiki.net/Light_radius · https://www.gamedeveloper.com/design/how-to-reduce-visual-confusion-in-your-game
- HQ5 https://www.ggrecon.com/guides/warframe-ephemera/ · https://wiki.warframe.com/w/Regalia · https://wiki.warframe.com/w/Blazing_Step_Ephemera
- HQ6 https://mp1st.com/news/destiny-2-ghost-changes-outlined-by-bungie-next-update-out-on-september-22
- HQ7 https://en.wikipedia.org/wiki/Journey_(2012_video_game) · https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation
- HQ8 https://www.epicgames.com/help/fortnite-battle-royale-c-202300000001636/gameplay-c-202300000001721/how-do-reactive-skins-work-in-fortnite-a202300000086082
- HQ9 https://developer.download.nvidia.com/whitepapers/2007/SDK10/SoftParticles_hi.pdf
- HQ10 https://www.destructoid.com/diablo-iv-character-customization-system-armor-dye/
- HQ11 https://gdcvault.com/play/1034360/Attention-Overload-Creating-Readable-VFX
- HQ12 https://80.lv/articles/constructing-vfx-worthy-of-league-of-legends/
- HQ13 https://80.lv/articles/destiny-2-vfx-production-tips/
- HQ14 https://advances.realtimerendering.com/s2013/Tatarchuk-Destiny-SIGGRAPH2013.pdf
- HQ15 https://geeks3d.com/?p=8334 (khử răng cưa "dây điện thoại" của Humus)
- HQ16 https://booth.pm/en/items/4822272 · https://booth.pm/zh-cn/items/8000365
- HQ17 https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine
- HQ18 https://www.premiumbeat.com/blog/cinematography-tips-lighting-villains/ (sáng từ dưới lên đọc ra hiểm ác)
- HQ19 https://gamedeveloper.com/design/gdc-2012-diablo-iii-s-art-director-shows-off-design-process · https://gdcvault.com/play/1015306/The-Art-of-Diablo

### Đường ống (PL)

- PL1 https://www.tripo3d.ai/blog/explore/ai-3d-model-generator-and-thin-structures-survival-strategies (blog của Tripo; chỉ đọc được đoạn trích từ kết quả tìm)
- PL2 https://help.scenario.com/articles/9861107995-tripo-segmentation-the-essentials
- PL3 https://docs.scenario.com/get-started/generation/3d-model-generation/3d-model-generation-tripo-ai
- PL4 https://arxiv.org/abs/2604.11006 (Zhang và cộng sự, 13/04/2026: "existing 3D texture generation methods are limited to producing only a few types of non-emissive PBR materials"; tôi đã mở kiểm phần tóm tắt) · bản tóm tắt thứ cấp: https://www.themoonlight.io/review/towards-realistic-3d-emission-materials-dataset-baseline-and-evaluation-for-emission-texture-generation
- PL5 https://www.tripo3d.ai/blog/export-a-3d-model-with-pbr-textures-so-it ("How do you export a 3D model with PBR textures so it looks correct in Unity or Unreal?": bộ map chính là màu nền, normal, roughness, metallic; emission chỉ được nhắc là "một số pipeline" dùng thêm; xác nhận lại qua kết quả tìm kiếm 01/11 vì trang trả HTTP 403 với công cụ đọc web)
- PL6 https://www.tripo3d.ai/help/features/how-to-get-better-image-to-3d-results (người nghiên cứu mở bằng trình duyệt; công cụ đọc web của tôi bị HTTP 403)
- PL7 https://www.tripo3d.ai/blog/how-to-turn-an-image-into-a-3d-model-with-ai
- PL8 https://www.tripo3d.ai/product-doc/module-post-processing/rigging-animation
- PL9 https://www.tripo3d.ai/product-doc/module-post-processing/segmentation (HTTP 403 với công cụ của tôi)
- PL10 https://www.tripo3d.ai/blog/gpt-6-astra-3d-character-workflow (chỉ đoạn trích từ kết quả tìm; HTTP 403)
- PL11 https://docs.meshy.ai/en/webapp/image-to-3d
- PL12 https://hyper3d.ai/help/articles/create-3d-models-from-images-with-rodin
- PL13 https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html (chỉ để tham khảo; ta không dùng Mixamo)
- PL14 https://manual.reallusion.com/Character-Creator-Pose-Tools/ENU/1.0/05-Prerequisite/Preparing-ZB-Model-for-AccuRIG.htm (tách mảnh cứng thành subtool riêng, trái và phải riêng; AccuRIG biến chúng thành phụ kiện cứng gắn xương) · https://manual.reallusion.com/Character-Creator-4/Content/ENU/4.1/09-AccuRIG/Creating-Character-with-Accessories.htm (lưới không bind thành phụ kiện cứng)
- PL15 https://threejs.org/docs/#api/en/objects/Bone

### ChatGPT (GP)

- GP0 https://chatgpt.com/c/6ae71421-3e3c-83ec-9d92-42b31a085d7b (cuộc chat, 01/11/2026)
- GP1 = PL6 · GP2 = PL7
- GP12 https://news.blizzard.com/en-us/article/23537427 ("What it's like to work on Overwatch as a concept artist": hình cơ bản quen thuộc như vuông, tròn cho cảm giác vững hay vô hại; Qiu Fang: hình lớn đặt gần đỉnh nhân vật để thấy từ xa; trang không ghi ngày)
- GP13 https://blog.playstation.com/?p=199639 (Island Time VR, Adam Volker viết, trích lời Ruby Wang, 03/04/2018)
- GP14 https://80.lv/articles/warframe-character-artist-on-designing-follie-and-evolving-silhouettes/ (Michael Skyers, Digital Extremes, 26/03/2026: hình tròn cho chủ đề nghịch ngợm, hình cứng và gai cho chủ đề lạnh hay hiểm)
- GP15 http://vocab.getty.edu/page/aat/300375684 (Getty AAT: halo)
- GP16 https://www.metmuseum.org/art/collection/search/39345 (Crowned Buddha)
- GP17 https://www.metmuseum.org/art/collection/search/670889 (Amaterasu, Kōno Bairei)
- GP18 https://www.4gamer.net/games/599/G059954/20231226029/ (Honkai: Star Rail, phỏng vấn đội thiết kế nhân vật, 29/12/2023)
- GP19 https://game.watch.impress.co.jp/docs/interview/1627639.html (NIKKE, Kim Hyung-tae, 04/10/2024)
- GP23 https://github.com/mrdoob/three.js/blob/r170/examples/webgl_postprocessing_unreal_bloom_selective.html · https://threejs.org/examples/#webgl_postprocessing_unreal_bloom_selective
