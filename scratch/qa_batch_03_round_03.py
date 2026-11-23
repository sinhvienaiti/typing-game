import json

OVERRIDES_B03_R03 = {
    # 1001-1050
    "lex.en.100k.011005": {"pos": "noun", "vi": "màu sắc; sắc thái"},  # colour
    "lex.en.100k.011006": {"vi": "họ Davis; tên riêng Davis"},  # davis
    "lex.en.100k.011009": {"vi": "dấu vết; điểm số; nhãn hiệu"},  # marks
    "lex.en.100k.011022": {"vi": "xác minh; tìm hiểu chắc chắn"},  # ascertain
    "lex.en.100k.011024": {"vi": "xét nghiệm; phân tích định lượng"},  # assay
    "lex.en.100k.011029": {"vi": "sách bán chạy nhất; sản phẩm hot"},  # bestseller
    "lex.en.100k.011031": {"vi": "sự đổ máu; cuộc thảm sát"},  # bloodshed
    "lex.en.100k.011034": {"vi": "thế hệ Boomer (sinh 1946-1964)"},  # boomer
    "lex.en.100k.011035": {"vi": "giòn dễ vỡ; mong manh dễ gãy"},  # brittle
    "lex.en.100k.011040": {"vi": "bệnh tả (y học)"},  # cholera (fixed single character 'tả')
    "lex.en.100k.011042": {"vi": "bị tắc nghẽn; bị ứ đọng"},  # clogged (fixed single character 'tắc')
    "lex.en.100k.011043": {"vi": "việc đi lại làm việc hàng ngày"},  # commuting
    "lex.en.100k.011044": {"vi": "nước da; sắc diện khuôn mặt"},  # complexion
    "lex.en.100k.011047": {"vi": "thuộc về cơ quan lãnh sự"},  # consular
    "lex.en.100k.011049": {"vi": "chật chội; tù túng; gò bó"},  # cramped

    # 1051-1100
    "lex.en.100k.011053": {"vi": "thuộc hệ thập phân; số thập phân"},  # decimal
    "lex.en.100k.011055": {"vi": "liệu trình thanh lọc; cai nghiện"},  # detox
    "lex.en.100k.011060": {"vi": "thương nhân buôn vải vóc"},  # draper
    "lex.en.100k.011061": {"vi": "người mộng mơ; người lý tưởng hóa"},  # dreamer
    "lex.en.100k.011067": {"vi": "xóa bỏ hoàn toàn; bài trừ sạch"},  # eradicate
    "lex.en.100k.011072": {"vi": "tăng theo cấp số nhân"},  # exponentially
    "lex.en.100k.011073": {"vi": "nhà xuất khẩu; công ty xuất khẩu"},  # exporter
    "lex.en.100k.011075": {"vi": "quá trình lên men vi sinh"},  # fermentation
    "lex.en.100k.011086": {"vi": "màu xám; hoa râm (tóc)"},  # grey
    "lex.en.100k.011089": {"vi": "chăm chỉ; cần cù chịu khó"},  # hardworking
    "lex.en.100k.011091": {"vi": "kinh khủng; tồi tệ khó chịu"},  # horrid
    "lex.en.100k.011094": {"vi": "họ Howard; tên riêng Howard"},  # howard
    "lex.en.100k.011098": {"vi": "hương trầm; nén nhang thắp"},  # incense
    "lex.en.100k.011100": {"vi": "không đủ điều kiện; không tư cách"},  # ineligible

    # 1101-1150
    "lex.en.100k.011105": {"vi": "môn võ judo; nhu đạo"},  # judo
    "lex.en.100k.011107": {"pos": "verb", "vi": "quỳ gối; quỳ xuống"},  # kneel
    "lex.en.100k.011111": {"vi": "họ Lewis; tên riêng Lewis"},  # lewis
    "lex.en.100k.011115": {"vi": "gỗ gụ; cây gỗ gụ (mahogany)"},  # mahogany (purged crude 'dái ngựa')
    "lex.en.100k.011116": {"vi": "cocktail Margarita"},  # margarita
    "lex.en.100k.011120": {"vi": "tiếng mèo kêu meo meo"},  # meow
    "lex.en.100k.011123": {"vi": "chày nghiền thuốc; dụng cụ nghiền"},  # muller
    "lex.en.100k.011124": {"vi": "người định vị; hoa tiêu dẫn đường"},  # navigator
    "lex.en.100k.011131": {"vi": "tràng pháo tay nhiệt liệt hoan hô"},  # ovation
    "lex.en.100k.011132": {"vi": "vượt xe khác; đuổi kịp vượt qua"},  # overtake
    "lex.en.100k.011135": {"pos": "verb", "vi": "lát đường; mở đường cho"},  # pave
    "lex.en.100k.011136": {"vi": "sự hoàn vốn đầu tư; sự trả đũa"},  # payback
    "lex.en.100k.011141": {"vi": "gỗ dán; ván ép công nghiệp"},  # plywood
    "lex.en.100k.011145": {"vi": "khúc dạo đầu; bước mở đầu"},  # prelude (fixed typo 'dạo dầu')
    "lex.en.100k.011150": {"vi": "bãi nôn; sự nôn mửa"},  # puke

    # 1151-1200
    "lex.en.100k.011152": {"vi": "khí (đông y); khí công"},  # qi
    "lex.en.100k.011157": {"vi": "hồng hào; lạc quan tươi sáng"},  # rosy
    "lex.en.100k.011158": {"vi": "độ võng lún; sự sụt giảm tạm"},  # sag
    "lex.en.100k.011159": {"vi": "tên riêng Sarah"},  # sarah
    "lex.en.100k.011160": {"vi": "chứng xơ cứng mô (y học)"},  # sclerosis
    "lex.en.100k.011165": {"vi": "các phiên họp; các buổi làm việc"},  # sessions
    "lex.en.100k.011168": {"vi": "tên riêng Simon"},  # simon
    "lex.en.100k.011170": {"vi": "nặng mùi; có mùi hôi hám"},  # smelly
    "lex.en.100k.011171": {"vi": "tiếng khóc nấc; tiếng thổn thức"},  # sob
    "lex.en.100k.011173": {"vi": "bảng tính điện tử (Excel/Sheet)"},  # spreadsheet
    "lex.en.100k.011175": {"vi": "giám sát; quản lý công việc"},  # supervise
    "lex.en.100k.011176": {"vi": "báo lá cải; báo giật gân (tabloid)"},  # tabloid
    "lex.en.100k.011177": {"vi": "mũ nồi len phong cách Scotland"},  # tam
    "lex.en.100k.011181": {"vi": "cảm giác buồn buồn; sự cù lét"},  # tickle
    "lex.en.100k.011184": {"vi": "thành phố Tripoli; bột mài tripoli"},  # tripoli
    "lex.en.100k.011186": {"vi": "hệ thống đường ống; ống mềm"},  # tubing
    "lex.en.100k.011190": {"vi": "dỡ hàng hóa; giải tỏa áp lực"},  # unload (fixed single character 'dỡ')
    "lex.en.100k.011194": {"vi": "cao cấp; thượng lưu; hạng sang"},  # upscale
    "lex.en.100k.011196": {"vi": "thiết bị đeo thông minh (wearable)"},  # wearable
    "lex.en.100k.011198": {"vi": "trát của tòa án; lệnh triệu tập"},  # writ

    # 1201-1250
    "lex.en.100k.011201": {"vi": "tên riêng Elizabeth; Nữ hoàng"},  # elizabeth
    "lex.en.100k.011204": {"vi": "tên riêng Drew; quá khứ draw"},  # drew
    "lex.en.100k.011206": {"vi": "tên riêng Jason"},  # jason
    "lex.en.100k.011209": {"vi": "tên riêng Luke; Thánh Luca"},  # luke
    "lex.en.100k.011211": {"vi": "thành Rome; thủ đô Rô-ma"},  # rome
    "lex.en.100k.011212": {"vi": "họ Harris; tên riêng Harris"},  # harris
    "lex.en.100k.011215": {"vi": "họ Kelly; tên riêng Kelly"},  # kelly
    "lex.en.100k.011216": {"pos": "verb", "vi": "hủy bỏ tiến trình (IT); phá thai"},  # abort
    "lex.en.100k.011221": {"vi": "biên độ sóng; phạm vi rộng lớn"},  # amplitude
    "lex.en.100k.011227": {"vi": "tai ương; nỗi ám ảnh triền miên"},  # bane
    "lex.en.100k.011229": {"vi": "mọi rợ; dã man; kẻ man di"},  # barbarian (purged 'mọi; rợ')
    "lex.en.100k.011230": {"vi": "dã man; man rợ; tàn bạo"},  # barbaric
    "lex.en.100k.011234": {"vi": "cây dẻ gai; gỗ sồi dẻ (beech)"},  # beech
    "lex.en.100k.011235": {"vi": "ngành kinh doanh; giới làm ăn (biz)"},  # biz
    "lex.en.100k.011240": {"vi": "vết bầm tím; vết thâm tím"},  # bruise
    "lex.en.100k.011243": {"vi": "họa tiết chữ V; quân hàm chữ V"},  # chevron
    "lex.en.100k.011244": {"vi": "sự cưỡng bức; hành vi ép buộc"},  # coercion
    "lex.en.100k.011250": {"vi": "nghệ nhân; thợ thủ công lành nghề"},  # craftsman

    # 1251-1300
    "lex.en.100k.011251": {"vi": "người tàn tật; kẻ què quặt"},  # cripple
    "lex.en.100k.011252": {"vi": "vùng đáy quần; ngã ba háng"},  # crotch
    "lex.en.100k.011256": {"vi": "phi tập trung (IT); phân quyền"},  # decentralized
    "lex.en.100k.011257": {"vi": "sự phân hủy hữu cơ; sự phân rã"},  # decomposition
    "lex.en.100k.011260": {"vi": "món cao lương mỹ vị; sự tinh tế"},  # delicacy
    "lex.en.100k.011261": {"vi": "phá dỡ công trình; triệt phá"},  # demolish
    "lex.en.100k.011262": {"vi": "Pháp (trong Phật giáo/Ấn Độ giáo)"},  # dharma
    "lex.en.100k.011263": {"vi": "chạy thận nhân tạo; lọc máu"},  # dialysis
    "lex.en.100k.011269": {"vi": "ở xa trung tâm; phía xa (giải phẫu)"},  # distal (fixed single character 'xa')
    "lex.en.100k.011271": {"vi": "giáo điều cứng nhắc; tín điều"},  # dogma
    "lex.en.100k.011274": {"vi": "bằng phương tiện điện tử"},  # electronically
    "lex.en.100k.011279": {"vi": "độ hỗn loạn entropy (vật lý/IT)"},  # entropy
    "lex.en.100k.011281": {"vi": "cây dương xỉ"},  # fern
    "lex.en.100k.011285": {"vi": "cẳng tay; phần cánh tay dưới"},  # forearm
    "lex.en.100k.011287": {"vi": "phím đàn guitar; sự lo âu phiền"},  # fret
    "lex.en.100k.011289": {"vi": "mầm bệnh; vi khuẩn; mầm mống"},  # germ
    "lex.en.100k.011293": {"vi": "gấu xám Bắc Mỹ (grizzly bear)"},  # grizzly
    "lex.en.100k.011296": {"vi": "đồng xu nhỏ heller (châu Âu)"},  # heller
    "lex.en.100k.011297": {"pos": "verb", "vi": "mài giũa kỹ năng; mài sắc bén"},  # hone

    # 1301-1350
    "lex.en.100k.011311": {"vi": "thuộc về chức vụ thị trưởng"},  # mayoral
    "lex.en.100k.011314": {"vi": "theo phong cách tối giản"},  # minimalist
    "lex.en.100k.011316": {"vi": "người vận chuyển; người khởi xướng"},  # mover
    "lex.en.100k.011320": {"vi": "chim dạ oanh (họa mi đêm)"},  # nightingale
    "lex.en.100k.011326": {"pos": "verb", "vi": "lật nhào xe; hủy bỏ phán quyết"},  # overturn
    "lex.en.100k.011327": {"vi": "khoa nhi; ngành nhi khoa"},  # pediatrics
    "lex.en.100k.011332": {"vi": "lỗ chân lông; lỗ li ti"},  # pore
    "lex.en.100k.011333": {"vi": "hiệu lực thuốc; tiềm lực; sức mạnh"},  # potency
    "lex.en.100k.011338": {"vi": "cổ kính độc đáo; nét xưa cũ"},  # quaint
    "lex.en.100k.011340": {"vi": "buổi độc tấu âm nhạc; ngâm thơ"},  # recital
    "lex.en.100k.011344": {"vi": "tinh chế; trau chuốt; cải tiến"},  # refine
    "lex.en.100k.011347": {"vi": "việc bán lại; giá trị bán lại"},  # resale
    "lex.en.100k.011350": {"vi": "sự vỡ mạch máu; sự rạn nứt"},  # rupture

    # 1351-1400
    "lex.en.100k.011354": {"vi": "gia vị nêm nếm thức ăn"},  # seasoning
    "lex.en.100k.011359": {"vi": "chất silic đi-ô-xít; hạt chống ẩm"},  # silica
    "lex.en.100k.011362": {"pos": "verb", "vi": "hớt váng bọt; đọc lướt nhanh"},  # skim
    "lex.en.100k.011363": {"vi": "trở ngại bất ngờ; vết rách xước"},  # snag
    "lex.en.100k.011364": {"vi": "quả bóng tuyết; hiệu ứng tuyết lăn"},  # snowball
    "lex.en.100k.011370": {"vi": "địa chủ nông thôn Anh; cận vệ"},  # squire
    "lex.en.100k.011374": {"vi": "người nghiện hút cần sa (stoner)"},  # stoner
    "lex.en.100k.011376": {"vi": "bị đốt (ong/kiến); bị tổn thương"},  # stung
    "lex.en.100k.011377": {"vi": "phụ đề phim (subtitle)"},  # subtitle
    "lex.en.100k.011379": {"vi": "sự dịu dàng âu yếm; cảm giác đau"},  # tenderness
    "lex.en.100k.011380": {"vi": "nhiệt kế đo nhiệt độ"},  # thermometer
    "lex.en.100k.011382": {"vi": "kẻ lang thang; tiếng chân nện nặng"},  # tramp
    "lex.en.100k.011384": {"vi": "hoa uất kim hương (tulip)"},  # tulip
    "lex.en.100k.011385": {"vi": "sự tinh chỉnh nhỏ; chỉnh sửa nhẹ"},  # tweak
    "lex.en.100k.011387": {"vi": "không được bảo vệ; không an toàn"},  # unprotected
    "lex.en.100k.011391": {"pos": "adv", "vi": "một cách yếu ớt; ẻo lả"},  # weakly
    "lex.en.100k.011392": {"vi": "ý thích chợt nảy ra; sự tùy hứng"},  # whim
    "lex.en.100k.011393": {"vi": "tiếng than vãn mè nheo; rên rỉ"},  # whine
    "lex.en.100k.011396": {"vi": "lòng sốt sắng; nhiệt huyết hăng"},  # zeal
    "lex.en.100k.011399": {"vi": "thành phố Liverpool; CLB bóng đá"},  # liverpool
    "lex.en.100k.011400": {"ipa": "/ˌɛnˈwaɪ/"},  # ny

    # 1401-1450
    "lex.en.100k.011404": {"vi": "họ Morgan; tên riêng Morgan"},  # morgan
    "lex.en.100k.011406": {"vi": "nguyên tố Natri; không áp dụng"},  # na
    "lex.en.100k.011408": {"vi": "tên riêng Anthony"},  # anthony
    "lex.en.100k.011409": {"vi": "vua Arthur; tên riêng Arthur"},  # arthur
    "lex.en.100k.011415": {"vi": "tên riêng Alexander; vua đại đế"},  # alexander
    "lex.en.100k.011419": {"pos": "verb", "vi": "làm sống động; tạo hoạt họa"},  # animate
    "lex.en.100k.011420": {"vi": "hậu môn (y học)"},  # anus (PURGED CRUDE VULGAR WORD 'lỗ đít')
    "lex.en.100k.011422": {"vi": "tầng lớp quý tộc; giới quý tộc"},  # aristocracy
    "lex.en.100k.011423": {"vi": "thợ thủ công lành nghề; nghệ nhân"},  # artisan
    "lex.en.100k.011441": {"vi": "mô sụn; chất sụn (giải phẫu)"},  # cartilage
    "lex.en.100k.011448": {"vi": "mặt lồi; có hình cong lồi"},  # convex
    "lex.en.100k.011449": {"pos": "verb", "vi": "ngồi xổm; khom lưng né tránh"},  # crouch

    # 1451-1500
    "lex.en.100k.011454": {"vi": "cây hoa thụy hương (daphne)"},  # daphne
    "lex.en.100k.011455": {"vi": "nạn phá rừng; tàn phá rừng"},  # deforestation
    "lex.en.100k.011467": {"vi": "phát ra (tia/sóng); thải ra khí"},  # emit
    "lex.en.100k.011468": {"vi": "đường xích đạo Trái Đất"},  # equator
    "lex.en.100k.011469": {"vi": "vùng cửa sông đổ ra biển"},  # estuary
    "lex.en.100k.011470": {"vi": "được khắc axit; khắc sâu tâm trí"},  # etched
    "lex.en.100k.011473": {"vi": "sự dẫn độ tội phạm giữa các nước"},  # extradition
    "lex.en.100k.011476": {"vi": "hỏa lực quân sự; sức tấn công"},  # firepower
    "lex.en.100k.011481": {"vi": "mang tính định hình tính cách"},  # formative
    "lex.en.100k.011483": {"vi": "cái nhíu mày; vẻ mặt cau có"},  # frown
    "lex.en.100k.011484": {"vi": "tiết kiệm; đạm bạc; tằn tiện"},  # frugal
    "lex.en.100k.011487": {"vi": "vùng bẹn háng; đê chắn sóng"},  # groin
    "lex.en.100k.011491": {"vi": "lòng quả cảm; chủ nghĩa anh hùng"},  # heroism
    "lex.en.100k.011493": {"vi": "khiêm nhường; thấy mình nhỏ bé"},  # humbled
    "lex.en.100k.011494": {"vi": "được cung cấp đủ nước; ngậm nước"},  # hydrated
    "lex.en.100k.011498": {"vi": "đầy sáng tạo; giàu óc sáng kiến"},  # inventive
    "lex.en.100k.011500": {"vi": "bồi thẩm viên (bồi thẩm đoàn)"},  # juror
}

# Verify lengths <= 35
for k, v in OVERRIDES_B03_R03.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

records = batch_data['records']
target_records = records[1000:1500]

applied_count = 0
for r in target_records:
    rid = r['id']
    if rid in OVERRIDES_B03_R03:
        for k, v in OVERRIDES_B03_R03[rid].items():
            r[k] = v
        applied_count += 1
    assert len(r['vi']) <= 35, f"Target record length > 35: {rid} {r['vi']}"

# Update reviewedCount for Batch 03 to 1500 (Round 3 completed)
batch_data['reviewedCount'] = 1500

with open('content/english/qa-batches/batch-03.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 03 Round 3 ({applied_count} overrides). Reviewed: 1500/5000.")
