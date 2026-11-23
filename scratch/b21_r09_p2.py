import json

# Manual word-by-word cognitive review for Batch 21 Round 9 Part 2 (records 4100-4199, IDs 200k.004102 to 200k.004201)
reviewed_entries = [
    # 4100: water glass
    {"ipa": "/ˈwɔːtər ɡlæs/", "vi": "ly thủy tinh uống nước; cốc nước", "pos": "phrase"},
    # 4101: west africa
    {"ipa": "/wɛst ˈæfrɪkə/", "vi": "khu vực Tây Phi; xứ Tây Phi", "pos": "phrase"},
    # 4102: white heat
    {"ipa": "/waɪt hiːt/", "vi": "sức nóng trắng; trạng thái cực độ", "pos": "phrase"},
    # 4103: world health organization
    {"ipa": "/wɜːrld hɛlθ ˌɔːrɡənəˈzeɪʃən/", "vi": "Tổ chức Y tế Thế giới; khối WHO", "pos": "phrase"},
    # 4104: writing paper
    {"ipa": "/ˈraɪtɪŋ ˈpeɪpər/", "vi": "giấy viết thư; giấy viết thư từ", "pos": "phrase"},
    # 4105: socials
    {"ipa": "/ˈsoʊʃlz/", "vi": "các buổi dạ hội; tiệc giao lưu", "pos": "noun"},
    # 4106: talked
    {"ipa": "/tɔːkt/", "vi": "đã trò chuyện; đã phát biểu tâm sự", "pos": "verb"},
    # 4107: facts
    {"ipa": "/fækts/", "vi": "các sự thật; những dữ kiện thực tế", "pos": "noun"},
    # 4108: givens
    {"ipa": "/ˈɡɪvnz/", "vi": "những điều đã biết; các tiền đề", "pos": "noun"},
    # 4109: handing
    {"ipa": "/ˈhændɪŋ/", "vi": "đang trao tận tay; đang chuyền đưa", "pos": "verb"},
    # 4110: leveled
    {"ipa": "/ˈlɛvld/", "vi": "đã san bằng; đã chĩa súng ngắm", "pos": "verb"},
    # 4111: oftenest
    {"ipa": "/ˈɔːfnɪst/", "vi": "thường xuyên nhất; hay xảy ra nhất", "pos": "adv"},
    # 4112: singled
    {"ipa": "/ˈsɪŋɡld/", "vi": "đã chọn riêng ra; đã đánh đòn đơn", "pos": "verb"},
    # 4113: singling
    {"ipa": "/ˈsɪŋɡlɪŋ/", "vi": "đang chọn riêng ra; đang tách riêng", "pos": "verb"},
    # 4114: access code
    {"ipa": "/ˈæksɛs koʊd/", "vi": "mã số truy cập; mật mã truy cập", "pos": "phrase"},
    # 4115: air sick
    {"ipa": "/ɛr sɪk/", "vi": "say máy bay; nôn nao trên phi cơ", "pos": "phrase"},
    # 4116: association football
    {"ipa": "/əˌsoʊsiˈeɪʃən ˈfʊtbɔːl/", "vi": "môn bóng đá quốc tế truyền thống", "pos": "phrase"},
    # 4117: at length
    {"ipa": "/æt lɛŋkθ/", "vi": "dài dòng tỉ mỉ; rốt cuộc sau cùng", "pos": "phrase"},
    # 4118: before christ
    {"ipa": "/bɪˈfɔːr kraɪst/", "vi": "trước Công nguyên; thời kỳ trước CN", "pos": "phrase"},
    # 4119: bill of sale
    {"ipa": "/bɪl ʌv seɪl/", "vi": "chứng từ chuyển nhượng quyền sở hữu", "pos": "phrase"},
    # 4120: board rule
    {"ipa": "/bɔːrd ruːl/", "vi": "thước đo khối lượng gỗ ván hộp", "pos": "phrase"},
    # 4121: brand name
    {"ipa": "/brænd neɪm/", "vi": "tên nhãn hiệu; tên gọi thương hiệu", "pos": "phrase"},
    # 4122: brown cup
    {"ipa": "/braʊn kʌp/", "vi": "nấm cốc nâu đất; nấm hình chén nâu", "pos": "phrase"},
    # 4123: bus company
    {"ipa": "/bʌs ˈkʌmpəni/", "vi": "công ty xe buýt vận chuyển khách", "pos": "phrase"},
    # 4124: camp down
    {"ipa": "/kæmp daʊn/", "vi": "dựng lều cắm trại; hạ trại nghỉ", "pos": "phrase"},
    # 4125: cast down
    {"ipa": "/kæst daʊn/", "vi": "cúi gằm mặt; làm chán nản ngã lòng", "pos": "phrase"},
    # 4126: cast off
    {"ipa": "/kæst ɔːf/", "vi": "tháo dây nhổ neo tàu; vứt bỏ đồ cũ", "pos": "phrase"},
    # 4127: cell death
    {"ipa": "/sɛl dɛθ/", "vi": "chết tế bào sinh học; tiêu tế bào", "pos": "phrase"},
    # 4128: central standard time
    {"ipa": "/ˈsɛntrəl ˈstændərd taɪm/", "vi": "giờ chuẩn miền Trung Bắc Mỹ CST", "pos": "phrase"},
    # 4129: civil action
    {"ipa": "/ˈsɪvl ˈækʃən/", "vi": "vụ kiện dân sự; tố tụng dân sự", "pos": "phrase"},
    # 4130: commission plan
    {"ipa": "/kəˈmɪʃən plæn/", "vi": "mô hình chính quyền cấp ủy ban", "pos": "phrase"},
    # 4131: common knowledge
    {"ipa": "/ˈkɑːmən ˈnɑːlɪdʒ/", "vi": "kiến thức phổ thông ai cũng biết", "pos": "phrase"},
    # 4132: computer industry
    {"ipa": "/kəmˈpjuːtər ˈɪndəstri/", "vi": "ngành công nghiệp máy vi tính", "pos": "phrase"},
    # 4133: construction industry
    {"ipa": "/kənˈstrʌkʃən ˈɪndəstri/", "vi": "ngành công nghiệp xây dựng hạ tầng", "pos": "phrase"},
    # 4134: copy out
    {"ipa": "/ˈkɑːpi aʊt/", "vi": "chép lại toàn bộ; sao chép văn bản", "pos": "phrase"},
    # 4135: council table
    {"ipa": "/ˈkaʊnsl ˈteɪbl/", "vi": "bàn họp hội đồng cơ quan", "pos": "phrase"},
    # 4136: date bar
    {"ipa": "/deɪt bɑːr/", "vi": "thanh bánh ngọt nhân quả chà là", "pos": "phrase"},
    # 4137: day camp
    {"ipa": "/deɪ kæmp/", "vi": "trại hè sinh hoạt ban ngày cho trẻ", "pos": "phrase"},
    # 4138: direct fire
    {"ipa": "/dəˈrɛkt faɪər/", "vi": "hỏa lực bắn thẳng mục tiêu", "pos": "phrase"},
    # 4139: do drugs
    {"ipa": "/duː drʌɡz/", "vi": "sử dụng chất ma túy; nghiện ngập", "pos": "phrase"},
    # 4140: economic growth
    {"ipa": "/ˌekəˈnɑːmɪk ɡroʊθ/", "vi": "tăng trưởng kinh tế quốc dân", "pos": "phrase"},
    # 4141: election district
    {"ipa": "/ɪˈlɛkʃən ˈdɪstrɪkt/", "vi": "khu vực bầu cử; đơn vị bầu cử", "pos": "phrase"},
    # 4142: european box
    {"ipa": "/ˌjʊrəˈpiːən bɑːks/", "vi": "cây hoàng dương châu Âu cảnh", "pos": "phrase"},
    # 4143: eye cup
    {"ipa": "/aɪ kʌp/", "vi": "cốc rửa mắt; đệm ngắm thị kính", "pos": "phrase"},
    # 4144: famous person
    {"ipa": "/ˈfeɪməs ˈpɜːrsn/", "vi": "người nổi tiếng; nhân vật có tiếng", "pos": "phrase"},
    # 4145: field of battle
    {"ipa": "/fiːld ʌv ˈbætl/", "vi": "chiến trường chiến sự; trận tiền", "pos": "phrase"},
    # 4146: floor board
    {"ipa": "/flɔːr bɔːrd/", "vi": "tấm ván sàn nhà lát gỗ", "pos": "phrase"},
    # 4147: foreign minister
    {"ipa": "/ˈfɔːrən ˈmɪnɪstər/", "vi": "bộ trưởng ngoại giao; ngoại trưởng", "pos": "phrase"},
    # 4148: form of address
    {"ipa": "/fɔːrm ʌv əˈdrɛs/", "vi": "cách xưng hô; tước hiệu chào hỏi", "pos": "phrase"},
    # 4149: fresh start
    {"ipa": "/frɛʃ stɑːrt/", "vi": "sự khởi đầu mới mẻ; làm lại từ đầu", "pos": "phrase"},
    # 4150: gas range
    {"ipa": "/ɡæs reɪndʒ/", "vi": "bếp nấu bằng gas; bếp ga gia đình", "pos": "phrase"},
    # 4151: george washington
    {"ipa": "/dʒɔːrdʒ ˈwɑːʃɪŋtən/", "vi": "Tổng thống George Washington Mỹ", "pos": "phrase"},
    # 4152: get onto
    {"ipa": "/ɡɛt ˈɑːntuː/", "vi": "bước lên xe; nhận thức ra vấn đề", "pos": "phrase"},
    # 4153: give rise
    {"ipa": "/ɡɪv raɪz/", "vi": "làm phát sinh; khơi mào cho việc", "pos": "phrase"},
    # 4154: greater new york
    {"ipa": "/ˈɡreɪtər nuː jɔːrk/", "vi": "vùng đô thị mở rộng Đại New York", "pos": "phrase"},
    # 4155: ground forces
    {"ipa": "/ɡraʊnd ˈfɔːrsɪz/", "vi": "lực lượng lục quân; quân bộ mặt đất", "pos": "phrase"},
    # 4156: hair ball
    {"ipa": "/hɛr bɔːl/", "vi": "búi lông trong ruột thú cưng", "pos": "phrase"},
    # 4157: hand and foot
    {"ipa": "/hænd ænd fʊt/", "vi": "trói gô chân tay; phục vụ tận răng", "pos": "phrase"},
    # 4158: heart disease
    {"ipa": "/hɑːrt dɪˈziːz/", "vi": "bệnh tim mạch; tổn thương tim", "pos": "phrase"},
    # 4159: house agent
    {"ipa": "/haʊs ˈeɪdʒənt/", "vi": "môi giới bất động sản nhà đất", "pos": "phrase"},
    # 4160: in cold blood
    {"ipa": "/ɪn koʊld blʌd/", "vi": "máu lạnh tàn nhẫn; nhẫn tâm cố sát", "pos": "phrase"},
    # 4161: james ii
    {"ipa": "/dʒeɪmz ðə ˈsɛkənd/", "vi": "vua James Đệ nhị của nước Anh", "pos": "phrase"},
    # 4162: know apart
    {"ipa": "/noʊ əˈpɑːrt/", "vi": "nhận biết phân biệt; chia tách rõ", "pos": "phrase"},
    # 4163: land of opportunity
    {"ipa": "/lænd ʌv ˌɑːpərˈtuːnəti/", "vi": "vùng đất đầy ắp cơ hội vươn lên", "pos": "phrase"},
    # 4164: letter security
    {"ipa": "/ˈlɛtər sɪˈkjʊrəti/", "vi": "chứng khoán tư nhân không đăng ký", "pos": "phrase"},
    # 4165: market analysis
    {"ipa": "/ˈmɑːrkɪt əˈnæləsɪs/", "vi": "phân tích nghiên cứu thị trường", "pos": "phrase"},
    # 4166: metal money
    {"ipa": "/ˈmɛtl ˈmʌni/", "vi": "tiền xu kim loại đúc phát hành", "pos": "phrase"},
    # 4167: military leader
    {"ipa": "/ˈmɪlətɛri ˈliːdər/", "vi": "chỉ huy quân sự; thủ lĩnh quân ngũ", "pos": "phrase"},
    # 4168: military unit
    {"ipa": "/ˈmɪlətɛri ˈjuːnɪt/", "vi": "đơn vị quân đội vũ trang đóng quân", "pos": "phrase"},
    # 4169: natural gas
    {"ipa": "/ˈnætʃrəl ɡæs/", "vi": "khí đốt thiên nhiên; khí gas đốt", "pos": "phrase"},
    # 4170: on request
    {"ipa": "/ɑːn rɪˈkwɛst/", "vi": "khi có yêu cầu đòi hỏi từ trước", "pos": "phrase"},
    # 4171: operations research
    {"ipa": "/ˌɑːpəˈreɪʃənz rɪˈsɜːrtʃ/", "vi": "nghiên cứu vận hành tối ưu hóa", "pos": "phrase"},
    # 4172: percent sign
    {"ipa": "/pərˈsɛnt saɪn/", "vi": "dấu phần trăm ký hiệu toán học", "pos": "phrase"},
    # 4173: personal letter
    {"ipa": "/ˈpɜːrsənl ˈlɛtər/", "vi": "lá thư riêng tư gửi cho cá nhân", "pos": "phrase"},
    # 4174: police captain
    {"ipa": "/pəˈliːs ˈkæptɪn/", "vi": "đại úy cảnh sát; đồn trưởng công an", "pos": "phrase"},
    # 4175: poor box
    {"ipa": "/pʊr bɑːks/", "vi": "hòm tiền từ thiện tại nhà thờ", "pos": "phrase"},
    # 4176: power structure
    {"ipa": "/ˈpaʊər ˈstrʌktʃər/", "vi": "cơ cấu quyền lực trong tổ chức", "pos": "phrase"},
    # 4177: price floor
    {"ipa": "/praɪs flɔːr/", "vi": "mức giá sàn tối thiểu được quy định", "pos": "phrase"},
    # 4178: pull away
    {"ipa": "/pʊl əˈweɪ/", "vi": "lăn bánh rời đi; bứt tốc vượt lên", "pos": "phrase"},
    # 4179: push away
    {"ipa": "/pʊʃ əˈweɪ/", "vi": "đẩy lùi ra xa; khước từ tình cảm", "pos": "phrase"},
    # 4180: queen post
    {"ipa": "/kwiːn poʊst/", "vi": "cột giàn vì kèo mái nhà kiến trúc", "pos": "phrase"},
    # 4181: ready cash
    {"ipa": "/ˈrɛdi kæʃ/", "vi": "tiền mặt có sẵn chi tiêu ngay", "pos": "phrase"},
    # 4182: red notice
    {"ipa": "/rɛd ˈnoʊtɪs/", "vi": "lệnh truy nã đỏ của Interpol", "pos": "phrase"},
    # 4183: religious order
    {"ipa": "/rɪˈlɪdʒəs ˈɔːrdər/", "vi": "dòng tu tôn giáo; hội dòng giáo sĩ", "pos": "phrase"},
    # 4184: religious service
    {"ipa": "/rɪˈlɪdʒəs ˈsɜːrvɪs/", "vi": "buổi lễ phụng vụ tôn giáo nhà thờ", "pos": "phrase"},
    # 4185: rock oil
    {"ipa": "/rɑːk ɔɪl/", "vi": "dầu mỏ thô tự nhiên trong lòng đất", "pos": "phrase"},
    # 4186: rose family
    {"ipa": "/roʊz ˈfæməli/", "vi": "họ thực vật hoa hồng Rosaceae", "pos": "phrase"},
    # 4187: royal line
    {"ipa": "/ˈrɔɪəl laɪn/", "vi": "dòng dõi hoàng gia; huyết thống vua", "pos": "phrase"},
    # 4188: second estate
    {"ipa": "/ˈsɛkənd ɪˈsteɪt/", "vi": "đẳng cấp quý tộc phong kiến Pháp", "pos": "phrase"},
    # 4189: sense of movement
    {"ipa": "/sɛns ʌv ˈmuːvmənt/", "vi": "cảm giác về sự chuyển động cơ thể", "pos": "phrase"},
    # 4190: service tree
    {"ipa": "/ˈsɜːrvɪs triː/", "vi": "cây thanh trà châu Âu ăn quả", "pos": "phrase"},
    # 4191: shop class
    {"ipa": "/ʃɑːp klæs/", "vi": "tiết học nghề thủ công cơ khí", "pos": "phrase"},
    # 4192: shop girl
    {"ipa": "/ʃɑːp ɡɜːrl/", "vi": "cô gái bán hàng tại cửa tiệm", "pos": "phrase"},
    # 4193: smart set
    {"ipa": "/smɑːrt sɛt/", "vi": "giới thượng lưu sành điệu ăn chơi", "pos": "phrase"},
    # 4194: social status
    {"ipa": "/ˈsoʊʃl ˈsteɪtəs/", "vi": "địa vị xã hội; thân thế xã hội", "pos": "phrase"},
    # 4195: song and dance
    {"ipa": "/sɔːŋ ænd dæns/", "vi": "tiết mục ca vũ; chuyện bịa đặt", "pos": "phrase"},
    # 4196: space bar
    {"ipa": "/speɪs bɑːr/", "vi": "phím cách dài trên bàn phím gõ", "pos": "phrase"},
    # 4197: spirit off
    {"ipa": "/ˈspɪrɪt ɔːf/", "vi": "bí mật đem đi mất; thủ tiêu bí mật", "pos": "phrase"},
    # 4198: spirit world
    {"ipa": "/ˈspɪrɪt wɜːrld/", "vi": "thế giới tâm linh linh hồn cõi âm", "pos": "phrase"},
    # 4199: stage effect
    {"ipa": "/steɪdʒ ɪˈfɛkt/", "vi": "hiệu ứng sân khấu biểu diễn kịch", "pos": "phrase"}
]

with open("scratch/b21_r09_raw_p2.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100
assert len(reviewed_entries) == 100

output = []
for i, item in enumerate(raw_data):
    rev = reviewed_entries[i]
    assert len(rev["vi"]) <= 35, f"Too long: {item['hw']} -> {rev['vi']} ({len(rev['vi'])} chars)"
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/"), f"Bad IPA: {item['hw']} -> {rev['ipa']}"
    assert rev["ipa"].count("/") == 2, f"Bad slash count: {item['hw']} -> {rev['ipa']}"
    assert rev["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"]

    entry = {
        "id": item["id"],
        "hw": item["hw"],
        "pos": rev["pos"],
        "ipa": rev["ipa"],
        "vi": rev["vi"],
        "cefr": item["cefr"],
        "tier": item["tier"],
        "status": "reviewed",
        "notes": item["notes"]
    }
    output.append(entry)

with open("scratch/b21_r09_p2.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Round 9 Part 2.")
