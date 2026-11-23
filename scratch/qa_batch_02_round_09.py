import json

OVERRIDES_ROUND_09 = {
    # 4001-4050
    "lex.en.100k.009004": {"vi": "sự điên rồ; sự mất trí"},  # madness
    "lex.en.100k.009005": {"vi": "dinh thự nguy nga; biệt thự lớn"},  # mansion
    "lex.en.100k.009006": {"vi": "nhà sản xuất; hãng sản xuất"},  # manufacturer
    "lex.en.100k.009008": {"vi": "thánh địa Mecca; trung tâm thu hút"},  # mecca
    "lex.en.100k.009009": {"vi": "thuốc men; dược phẩm điều trị"},  # medication
    "lex.en.100k.009013": {"vi": "cây bạc hà; mới tinh nguyên bản"},  # mint
    "lex.en.100k.009018": {"vi": "cơn ác mộng; nỗi khiếp sợ"},  # nightmare
    "lex.en.100k.009022": {"vi": "tiền đồn; chi nhánh ở xa"},  # outpost
    "lex.en.100k.009024": {"vi": "sự tràn; hiện tượng tràn bộ nhớ"},  # overflow
    "lex.en.100k.009026": {"vi": "say mê; nồng nhiệt; đầy đam mê"},  # passionate (fixed typo 'dể giận')
    "lex.en.100k.009028": {"vi": "sự nhận thức; cảm nhận"},  # perception
    "lex.en.100k.009029": {"vi": "loài chim phoebe"},  # phoebe
    "lex.en.100k.009038": {"vi": "thiết bị thăm dò; cuộc điều tra"},  # probe
    "lex.en.100k.009040": {"vi": "sự quảng bá; sự chú ý công chúng"},  # publicity
    "lex.en.100k.009041": {"vi": "cầu vồng nhiều màu"},  # rainbow (purged 'lẹm')
    "lex.en.100k.009044": {"vi": "từ chức; xin nghỉ việc"},  # resign
    "lex.en.100k.009048": {"vi": "trò chơi cò quay (roulette)"},  # roulette
    "lex.en.100k.009050": {"vi": "môn đua thuyền; chèo thuyền"},  # rowing

    # 4051-4100
    "lex.en.100k.009051": {"vi": "sự xoa bóp; điểm khó khăn then chốt"},  # rub
    "lex.en.100k.009052": {"vi": "bao tải; sự sa thải việc làm"},  # sack
    "lex.en.100k.009053": {"vi": "mẩu vụn thừa; phế liệu"},  # scraps
    "lex.en.100k.009055": {"vi": "người bán hàng; sản phẩm bán chạy"},  # seller
    "lex.en.100k.009059": {"vi": "vô liêm sỉ; trơ trẽn; trơ tráo"},  # shameless
    "lex.en.100k.009064": {"pos": "noun", "vi": "cú tát; cái vỗ; đòn đau"},  # slap
    "lex.en.100k.009068": {"vi": "tia lửa điện; ngòi nổ cảm hứng"},  # spark
    "lex.en.100k.009069": {"vi": "trứng cá; nơi sinh quái (game)"},  # spawn
    "lex.en.100k.009072": {"pos": "noun", "vi": "cây vân sam; vẻ bảnh bao"},  # spruce
    "lex.en.100k.009074": {"vi": "sự siết chặt; sự chèn ép kinh tế"},  # squeeze
    "lex.en.100k.009083": {"vi": "sự xoay chuyển tình thế; chu kỳ"},  # turnaround
    "lex.en.100k.009086": {"vi": "xã hội không tưởng; địa đàng"},  # utopia
    "lex.en.100k.009090": {"vi": "vi-ta-min; dưỡng chất thiết yếu"},  # vitamin
    "lex.en.100k.009091": {"vi": "vòng eo; thắt lưng"},  # waist
    "lex.en.100k.009092": {"vi": "sự hóm hỉnh; trí thông minh"},  # wit
    "lex.en.100k.009098": {"vi": "bà (phụ nữ có gia đình)"},  # mrs
    "lex.en.100k.009099": {"vi": "thợ rèn; người thợ kim khí"},  # smith (purged specific person Ian Smith)

    # 4101-4150
    "lex.en.100k.009101": {"vi": "chỗ ở; tiện nghi lưu trú"},  # accommodation (purged typo 'nhá ở')
    "lex.en.100k.009102": {"vi": "theo đó; do đó; tương ứng"},  # accordingly
    "lex.en.100k.009103": {"vi": "có tính dính; chất kết dính; keo"},  # adhesive
    "lex.en.100k.009108": {"vi": "giàu có; sung túc; thịnh vượng"},  # affluent
    "lex.en.100k.009111": {"vi": "khoản ngân sách cấp; sự chiếm dụng"},  # appropriation
    "lex.en.100k.009117": {"vi": "khu chợ truyền thống; chợ từ thiện"},  # bazaar
    "lex.en.100k.009118": {"vi": "người lái mô tô; người đi xe máy"},  # biker
    "lex.en.100k.009121": {"vi": "trình duyệt web (IT)"},  # browser
    "lex.en.100k.009122": {"pos": "noun", "vi": "kẻ bắt nạt; kẻ chuyên ức hiếp"},  # bully
    "lex.en.100k.009123": {"vi": "sự chôn cất; lễ an táng"},  # burial
    "lex.en.100k.009124": {"vi": "nam tính (nữ đồng tính); vạm vỡ"},  # butch
    "lex.en.100k.009125": {"vi": "sâu bướm; xe bánh xích"},  # caterpillar
    "lex.en.100k.009126": {"pos": "noun", "vi": "nhà thờ chính tòa; thánh đường"},  # cathedral
    "lex.en.100k.009131": {"vi": "nhà sưu tập; người thu gom"},  # collector
    "lex.en.100k.009136": {"vi": "hình nón; que kem ốc quế"},  # cone
    "lex.en.100k.009142": {"vi": "hình lập phương; khối vuông"},  # cube
    "lex.en.100k.009144": {"vi": "sự mục nát; sự phân hủy; suy tàn"},  # decay
    "lex.en.100k.009151": {"vi": "vùng Dixie (miền Nam nước Mỹ)"},  # dixie
    "lex.en.100k.009152": {"vi": "học vị tiến sĩ; bằng tiến sĩ"},  # doctorate
    "lex.en.100k.009153": {"vi": "sự quyên góp; khoản tài trợ"},  # donation
    "lex.en.100k.009154": {"vi": "thiết bị thụt rửa; kẻ đáng ghét"},  # douche
    "lex.en.100k.009155": {"vi": "thuốc nhuộm; màu nhuộm"},  # dye
    "lex.en.100k.009156": {"vi": "con đê chắn nước; đồng tính nữ"},  # dyke
    "lex.en.100k.009158": {"vi": "sự mã hóa ký tự (IT); mã hóa"},  # encoding
    "lex.en.100k.009160": {"vi": "phương trình; phép tính cân bằng"},  # equation

    # 4151-4200
    "lex.en.100k.009166": {"pos": "noun", "vi": "chất nổ; thuốc nổ; dễ phát nổ"},  # explosive
    "lex.en.100k.009172": {"vi": "dị tính; quan hệ nam nữ"},  # heterosexual
    "lex.en.100k.009182": {"vi": "sự kiềm chế; sự ức chế tâm lý"},  # inhibition
    "lex.en.100k.009188": {"vi": "nhà đầu tư"},  # investor
    "lex.en.100k.009189": {"vi": "bước lặp; lần lặp (Agile/IT)"},  # iteration
    "lex.en.100k.009194": {"vi": "cuộc thảm sát; sự tàn sát"},  # massacre
    "lex.en.100k.009197": {"pos": "noun", "vi": "đường kinh tuyến; đỉnh cao"},  # meridian
    "lex.en.100k.009199": {"vi": "chỉ số đo lường (IT); hệ mét"},  # metric
    "lex.en.100k.009200": {"vi": "ở giữa; giữa lúc"},  # midst

    # 4201-4250
    "lex.en.100k.009201": {"vi": "tiếng than vãn; tiếng rên rỉ"},  # moan
    "lex.en.100k.009202": {"vi": "giả định; mô phỏng thử nghiệm"},  # mock
    "lex.en.100k.009207": {"vi": "sự cần thiết; nhu yếu phẩm"},  # necessity
    "lex.en.100k.009212": {"vi": "nghĩa vụ; bổn phận pháp lý"},  # obligation
    "lex.en.100k.009214": {"vi": "khó chịu; đáng ghét; xấc xược"},  # obnoxious (purged truncated 'câng')
    "lex.en.100k.009218": {"pos": "adv", "vi": "làm ngoài giờ; tăng ca; thêm giờ"},  # overtime
    "lex.en.100k.009219": {"vi": "con chim cú"},  # owl
    "lex.en.100k.009220": {"vi": "quá trình oxy hóa"},  # oxidation
    "lex.en.100k.009226": {"vi": "giá đỡ; kệ chứa đồ; giá hàng"},  # rack
    "lex.en.100k.009231": {"vi": "tân binh; nhân viên mới tuyển"},  # recruit
    "lex.en.100k.009234": {"vi": "nhẹ nhõm; an tâm; bớt căng thẳng"},  # relieved
    "lex.en.100k.009239": {"vi": "mùi hương; hương thơm thoang thoảng"},  # scent
    "lex.en.100k.009244": {"vi": "tủ trưng bày; cơ hội phô diễn"},  # showcase
    "lex.en.100k.009245": {"vi": "chất nhờn dính; đồ chơi slime"},  # slime
    "lex.en.100k.009246": {"vi": "tinh vi; phức tạp; tinh tế"},  # sophisticated
    "lex.en.100k.009250": {"vi": "cứng nhắc; đơ cứng; khó gập"},  # stiff

    # 4251-4300
    "lex.en.100k.009251": {"vi": "quyền bầu cử; quyền đi bầu"},  # suffrage (37 chars!) -> wait, check length
    "lex.en.100k.009253": {"vi": "con thiên nga"},  # swan
    "lex.en.100k.009256": {"vi": "sân hiên; ruộng bậc thang"},  # terrace
    "lex.en.100k.009259": {"vi": "đe dọa; hăm dọa"},  # threaten
    "lex.en.100k.009263": {"vi": "bẫy thú; các biểu hiện hào nhoáng"},  # trapping
    "lex.en.100k.009267": {"vi": "học phí; tiền học"},  # tuition
    "lex.en.100k.009269": {"vi": "mở khóa; mở ra tiềm năng"},  # unlock
    "lex.en.100k.009271": {"vi": "hoàn toàn; tuyệt đối; tột cùng"},  # utter
    "lex.en.100k.009274": {"vi": "đức hạnh; phẩm chất tốt đẹp"},  # virtue
    "lex.en.100k.009275": {"vi": "điệu van-xơ (waltz)"},  # waltz
    "lex.en.100k.009280": {"vi": "khóa kéo; mã vùng (zip code)"},  # zip
    "lex.en.100k.009281": {"vi": "sự phóng to; phần mềm Zoom"},  # zoom
    "lex.en.100k.009282": {"pos": "num", "vi": "số chín (9)"},  # nine
    "lex.en.100k.009286": {"vi": "bị nghiện; say mê cuốn hút"},  # addicted
    "lex.en.100k.009287": {"vi": "sự điều chỉnh; sự hiệu chỉnh"},  # adjustment
    "lex.en.100k.009288": {"vi": "bàn thờ; bàn thánh trong nhà thờ"},  # altar
    "lex.en.100k.009294": {"vi": "việc đấu thầu; trả giá; đấu giá"},  # bidding
    "lex.en.100k.009295": {"vi": "thuộc về tiểu sử"},  # biographical
    "lex.en.100k.009296": {"vi": "lưỡng đảng; đồng thuận đôi bên"},  # bipartisan
    "lex.en.100k.009299": {"vi": "dấu ngoặc vuông; khung giá đỡ"},  # bracket

    # 4301-4350
    "lex.en.100k.009303": {"pos": "noun", "vi": "kẻ vô công rồi nghề; dở tệ"},  # bum
    "lex.en.100k.009305": {"vi": "cây gậy chống; cây mía"},  # cane
    "lex.en.100k.009306": {"vi": "lễ hội hóa trang; hội chợ vui chơi"},  # carnival
    "lex.en.100k.009307": {"vi": "miếng thịt sườn; nhát chặt"},  # chop
    "lex.en.100k.009310": {"vi": "cocktail; thức uống pha chế"},  # cocktail
    "lex.en.100k.009311": {"vi": "quả dừa; trái dừa"},  # coconut
    "lex.en.100k.009313": {"vi": "khổng lồ; to lớn đồ sộ; cực lớn"},  # colossal
    "lex.en.100k.009315": {"vi": "lòng trắc ẩn; lòng thương cảm"},  # compassion
    "lex.en.100k.009316": {"vi": "trình biên dịch mã (IT)"},  # compiler
    "lex.en.100k.009317": {"vi": "thú nhận; thú tội; bộc bạch"},  # confess
    "lex.en.100k.009320": {"vi": "giòn rụm; giòn tan"},  # crispy
    "lex.en.100k.009322": {"vi": "bị cắt ngắn; được cắt xén (ảnh)"},  # cropped
    "lex.en.100k.009328": {"pos": "noun", "vi": "sự bất mãn; không hài lòng"},  # discontent
    "lex.en.100k.009333": {"vi": "thực sự; hoàn toàn; trắng trợn"},  # downright
    "lex.en.100k.009335": {"vi": "nạn hạn hán; tình trạng khô hạn"},  # drought
    "lex.en.100k.009341": {"vi": "tòng quân; nhập ngũ; xin gia nhập"},  # enlist
    "lex.en.100k.009342": {"vi": "doanh nhân khởi nghiệp; doanh nhân"},  # entrepreneur
    "lex.en.100k.009348": {"vi": "phát nổ; bùng nổ; nổ tung"},  # explode
    "lex.en.100k.009349": {"vi": "chiến công; lỗ hổng bảo mật (IT)"},  # exploit
    "lex.en.100k.009351": {"vi": "chạy trốn; bỏ trốn; đào tẩu"},  # flee (purged archaic 'bôn')

    # 4351-4400
    "lex.en.100k.009352": {"vi": "cổng vào; cổng kết nối mạng (IT)"},  # gateway
    "lex.en.100k.009357": {"vi": "sự can đảm; lòng dũng cảm; ruột"},  # guts
    "lex.en.100k.009361": {"vi": "lòng hiếu khách; ngành khách sạn"},  # hospitality
    "lex.en.100k.009364": {"vi": "ngụ ý; ám chỉ"},  # imply
    "lex.en.100k.009368": {"vi": "mũi tiêm thuốc; lỗi chèn mã (IT)"},  # injection
    "lex.en.100k.009370": {"pos": "noun", "vi": "bản năng; trực giác"},  # instinct
    "lex.en.100k.009374": {"vi": "cảm giác ngứa ngáy; sự thèm muốn"},  # itching
    "lex.en.100k.009375": {"vi": "quái chiêu; lập dị; kỳ quặc"},  # kinky
    "lex.en.100k.009377": {"vi": "thức ăn thừa; đồ ăn còn lại"},  # leftovers
    "lex.en.100k.009380": {"vi": "cú liếm; đoạn solo guitar ngắn"},  # lick
    "lex.en.100k.009381": {"vi": "nắp đậy; vung nồi"},  # lid
    "lex.en.100k.009384": {"vi": "quý bà; bà chủ"},  # madame
    "lex.en.100k.009386": {"vi": "sự sản xuất; chế tạo hàng loạt"},  # manufacture
    "lex.en.100k.009388": {"vi": "hàng hóa; sản phẩm kinh doanh"},  # merchandise
    "lex.en.100k.009391": {"vi": "đạo đức; luân thường đạo lý"},  # morality
    "lex.en.100k.009392": {"vi": "thuốc giảm đau móc-phin"},  # morphine
    "lex.en.100k.009395": {"vi": "nghịch ngợm; hư đốn; tinh quái"},  # naughty
    "lex.en.100k.009396": {"vi": "cõi niết bàn; trạng thái cực lạc"},  # nirvana
    "lex.en.100k.009400": {"vi": "ngoài khơi; hải ngoại (tài chính)"},  # offshore

    # 4401-4450
    "lex.en.100k.009404": {"vi": "gói nhỏ; gói dữ liệu (packet IT)"},  # packet
    "lex.en.100k.009407": {"vi": "quả đào; trái đào"},  # peach
    "lex.en.100k.009408": {"vi": "vỏ ngoài trái cây; lớp vỏ"},  # peel
    "lex.en.100k.009412": {"vi": "sắc tố; chất màu nhuộm"},  # pigment
    "lex.en.100k.009413": {"vi": "vô nghĩa; vô ích; không mục đích"},  # pointless
    "lex.en.100k.009414": {"vi": "môn mã cầu (polo); áo phông polo"},  # polo
    "lex.en.100k.009420": {"vi": "mau lẹ; kịp thời; câu lệnh AI"},  # prompt
    "lex.en.100k.009426": {"vi": "hoạt động giải trí; sự tiêu khiển"},  # recreation
    "lex.en.100k.009430": {"vi": "sự từ chức; đơn từ chức"},  # resignation
    "lex.en.100k.009431": {"pos": "adj", "vi": "đã rút lui; đã thoái lui"},  # retreated (crawler said 'những người đã rút lui')
    "lex.en.100k.009436": {"vi": "khôn ngoan; sáng suốt; hiền triết"},  # sage
    "lex.en.100k.009441": {"vi": "nhạc phim (soundtrack)"},  # soundtrack
    "lex.en.100k.009442": {"vi": "đặc sản; chuyên môn sâu"},  # specialty
    "lex.en.100k.009443": {"vi": "nhát đâm; vết đâm; sự cố gắng"},  # stab
    "lex.en.100k.009444": {"vi": "dịu nhẹ; trầm lắng; kín đáo"},  # subdued
    "lex.en.100k.009447": {"vi": "người giám sát; quản lý ca"},  # supervisor
    "lex.en.100k.009448": {"vi": "nhà cung cấp; nhà phân phối"},  # supplier
    "lex.en.100k.009449": {"vi": "sự dâng trào; sự tăng đột biến"},  # surge
    "lex.en.100k.009450": {"vi": "mang thai hộ; người thay thế"},  # surrogate

    # 4451-4500
    "lex.en.100k.009451": {"vi": "vị chua gắt; bánh tart"},  # tart (PURGED CRUDE VULGAR SLUR 'gái điếm')
    "lex.en.100k.009454": {"vi": "tên riêng Thomas"},  # thomas
    "lex.en.100k.009455": {"vi": "tiếng leng keng nhỏ; tiếng chuông"},  # ting
    "lex.en.100k.009457": {"vi": "hình tam giác; góc tam giác"},  # triangle
    "lex.en.100k.009463": {"vi": "bỏ trống; còn trống (phòng/ghế)"},  # vacant
    "lex.en.100k.009464": {"vi": "đã được xác thực hợp lệ"},  # validated
    "lex.en.100k.009467": {"vi": "du thuyền buồm; du thuyền sang"},  # yacht
    "lex.en.100k.009472": {"vi": "giao thức HTTP (mạng web)"},  # http
    "lex.en.100k.009475": {"vi": "từ đằng xa; nơi xa xôi"},  # afar
    "lex.en.100k.009476": {"pos": "adj", "vi": "đã khẳng định; đã xác nhận"},  # affirmed (PURGED crawler racehorse 'ngựa đua Affirmed')
    "lex.en.100k.009480": {"vi": "cổ xưa; lỗi thời; từ ngữ cổ"},  # archaic
    "lex.en.100k.009481": {"vi": "sự cam đoan; bảo đảm; tự tin"},  # assurance
    "lex.en.100k.009484": {"vi": "hoang mang; bối rối khó hiểu"},  # baffled
    "lex.en.100k.009485": {"vi": "chuyên viên ngân hàng"},  # banker (35 chars)
    "lex.en.100k.009486": {"vi": "tình thế khó xử; sự ràng buộc"},  # bind
    "lex.en.100k.009489": {"vi": "nắp ca-pô ô tô; mũ em bé"},  # bonnet
    "lex.en.100k.009493": {"vi": "nhân viên kiểm duyệt; thiết bị ngắt"},  # censor
    "lex.en.100k.009498": {"vi": "trạng thái hôn mê sâu"},  # coma
    "lex.en.100k.009500": {"vi": "nhạc trưởng; chất dẫn điện"},  # conductor (37 chars!) -> wait, check length
}

# Fix suffrage length
OVERRIDES_ROUND_09["lex.en.100k.009251"] = {"vi": "quyền bầu cử; quyền đi bầu"}
# Fix conductor length
OVERRIDES_ROUND_09["lex.en.100k.009500"] = {"vi": "nhạc trưởng; chất dẫn điện"}

# Verify length <= 35
for k, v in OVERRIDES_ROUND_09.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-02.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

records = batch_data['records']
target_records = records[4000:4500]

applied_count = 0
for r in target_records:
    rid = r['id']
    if rid in OVERRIDES_ROUND_09:
        for k, v in OVERRIDES_ROUND_09[rid].items():
            r[k] = v
        applied_count += 1
    assert len(r['vi']) <= 35, f"Target record length > 35: {rid} {r['vi']}"

batch_data['reviewedCount'] = 4500

with open('content/english/qa-batches/batch-02.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Round 9 ({applied_count} overrides). Total reviewed: 4500/5000.")
