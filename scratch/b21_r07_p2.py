import json

# Manual word-by-word cognitive review for Batch 21 Round 7 Part 2 (records 3100-3199, IDs 200k.003102 to 200k.003201)
reviewed_entries = [
    # 3100: train set
    {"ipa": "/treɪn sɛt/", "vi": "bộ đồ chơi mô hình đoàn tàu hỏa", "pos": "phrase"},
    # 3101: trust account
    {"ipa": "/trʌst əˈkaʊnt/", "vi": "tài khoản tiền gửi ủy thác", "pos": "phrase"},
    # 3102: university student
    {"ipa": "/ˌjuːnɪˈvɜːrsəti ˈstuːdənt/", "vi": "sinh viên theo học trường đại học", "pos": "phrase"},
    # 3103: us congress
    {"ipa": "/juː ɛs ˈkɑːŋɡrəs/", "vi": "Quốc hội Hợp chúng quốc Hoa Kỳ", "pos": "phrase"},
    # 3104: works council
    {"ipa": "/wɜːrks ˈkaʊnsəl/", "vi": "hội đồng đại diện công nhân nhà máy", "pos": "phrase"},
    # 3105: written word
    {"ipa": "/ˈrɪtən wɜːrd/", "vi": "văn tự chữ viết; câu chữ trên sách", "pos": "phrase"},
    # 3106: fours
    {"ipa": "/fɔːrz/", "vi": "những con số bốn; nhóm bốn người", "pos": "noun"},
    # 3107: harder
    {"ipa": "/ˈhɑːrdər/", "vi": "khó khăn hơn; cứng rắn hơn rõ rệt", "pos": "adj"},
    # 3108: meaner
    {"ipa": "/ˈmiːnər/", "vi": "keo kiệt bủn xỉn hơn; xấu tính hơn", "pos": "adj"},
    # 3109: meanest
    {"ipa": "/ˈmiːnɪst/", "vi": "keo kiệt nhất; hèn hạ tồi tệ nhất", "pos": "adj"},
    # 3110: tells
    {"ipa": "/tɛlz/", "vi": "những biểu hiện vô thức lộ tẩy", "pos": "noun"},
    # 3111: blue star
    {"ipa": "/bluː stɑːr/", "vi": "ngôi sao xanh; hoa sao xanh biếc", "pos": "phrase"},
    # 3112: book fair
    {"ipa": "/bʊk fɛr/", "vi": "hội chợ triển lãm sách báo xuất bản", "pos": "phrase"},
    # 3113: brown university
    {"ipa": "/braʊn ˌjuːnɪˈvɜːrsəti/", "vi": "Đại học Brown thuộc nhóm Ivy League", "pos": "phrase"},
    # 3114: carry back
    {"ipa": "/ˈkæri bæk/", "vi": "kết chuyển lỗ ngược về năm trước", "pos": "phrase"},
    # 3115: carry over
    {"ipa": "/ˈkæri ˈoʊvər/", "vi": "chuyển số dư sang kỳ sau; tồn đọng", "pos": "phrase"},
    # 3116: catch out
    {"ipa": "/kætʃ aʊt/", "vi": "bắt quả tang sai sót; gài bẫy", "pos": "phrase"},
    # 3117: catch up
    {"ipa": "/kætʃ ʌp/", "vi": "bắt kịp tiến độ; theo kịp bạn bè", "pos": "phrase"},
    # 3118: check mark
    {"ipa": "/tʃɛk mɑːrk/", "vi": "dấu tích kiểm tra; dấu kiểm nhận", "pos": "phrase"},
    # 3119: city centre
    {"ipa": "/ˈsɪti ˈsɛntər/", "vi": "khu vực trung tâm lõi của thành phố", "pos": "phrase"},
    # 3120: conference room
    {"ipa": "/ˈkɑːnfərəns ruːm/", "vi": "phòng hội nghị; phòng họp cơ quan", "pos": "phrase"},
    # 3121: cover song
    {"ipa": "/ˈkʌvər sɔːŋ/", "vi": "bản phối lại bài hát; bản hát lại", "pos": "phrase"},
    # 3122: dance school
    {"ipa": "/dæns skuːl/", "vi": "trường dạy khiêu vũ; học viện múa", "pos": "phrase"},
    # 3123: dark red
    {"ipa": "/dɑːrk rɛd/", "vi": "gam màu đỏ sẫm; sắc đỏ thẫm trầm", "pos": "phrase"},
    # 3124: deep red
    {"ipa": "/diːp rɛd/", "vi": "màu đỏ đậm đà; sắc đỏ thắm thẫm", "pos": "phrase"},
    # 3125: defense team
    {"ipa": "/dɪˈfɛns tiːm/", "vi": "đoàn luật sư bào chữa cho bị can", "pos": "phrase"},
    # 3126: drink down
    {"ipa": "/drɪŋk daʊn/", "vi": "uống ực một hơi; uống cạn chén rượu", "pos": "phrase"},
    # 3127: foot up
    {"ipa": "/fʊt ʌp/", "vi": "cộng tổng một cột số; thanh toán nợ", "pos": "phrase"},
    # 3128: gun case
    {"ipa": "/ɡʌn keɪs/", "vi": "hộp bao da đựng súng săn cá nhân", "pos": "phrase"},
    # 3129: hold fast
    {"ipa": "/hoʊld fæst/", "vi": "bám chặt không buông; kiên định giữ", "pos": "phrase"},
    # 3130: ii john
    {"ipa": "/tuː dʒɑːn/", "vi": "thư thứ hai của Thánh Gioan Tông đồ", "pos": "phrase"},
    # 3131: in condition
    {"ipa": "/ɪn kənˈdɪʃən/", "vi": "thể lực sung mãn; phong độ đỉnh cao", "pos": "phrase"},
    # 3132: in flight
    {"ipa": "/ɪn flaɪt/", "vi": "đang bay lượn; trong chuyến bay", "pos": "phrase"},
    # 3133: john brown
    {"ipa": "/dʒɑːn braʊn/", "vi": "nhà bãi nô John Brown của nước Mỹ", "pos": "phrase"},
    # 3134: left brain
    {"ipa": "/lɛft breɪn/", "vi": "bán cầu não trái tư duy logic số", "pos": "phrase"},
    # 3135: legal action
    {"ipa": "/ˈliːɡəl ˈækʃən/", "vi": "biện pháp khởi kiện pháp lý ra tòa", "pos": "phrase"},
    # 3136: married woman
    {"ipa": "/ˈmærid ˈwʊmən/", "vi": "người phụ nữ đã kết hôn có chồng", "pos": "phrase"},
    # 3137: mean sun
    {"ipa": "/miːn sʌn/", "vi": "mặt trời giả định đo giờ thiên văn", "pos": "phrase"},
    # 3138: military science
    {"ipa": "/ˈmɪlətɛri ˈsaɪəns/", "vi": "ngành khoa học quân sự tác chiến", "pos": "phrase"},
    # 3139: national income
    {"ipa": "/ˈnæʃənəl ˈɪnkʌm/", "vi": "tổng thu nhập quốc dân của nền kinh", "pos": "phrase"},
    # 3140: night letter
    {"ipa": "/naɪt ˈlɛtər/", "vi": "bức điện tín gửi ban đêm giá rẻ", "pos": "phrase"},
    # 3141: opening night
    {"ipa": "/ˈoʊpənɪŋ naɪt/", "vi": "đêm công diễn mở màn đầu tiên vở", "pos": "phrase"},
    # 3142: outside door
    {"ipa": "/ˌaʊtˈsaɪd dɔːr/", "vi": "cửa ra vào phía ngoài căn nhà", "pos": "phrase"},
    # 3143: pop out
    {"ipa": "/pɑːp aʊt/", "vi": "bất ngờ xuất hiện; lồi hẳn ra ngoài", "pos": "phrase"},
    # 3144: pop up
    {"ipa": "/pɑːp ʌp/", "vi": "bật lên bất ngờ; cửa sổ bật lên", "pos": "phrase"},
    # 3145: popular front
    {"ipa": "/ˈpɑːpjələr frʌnt/", "vi": "Mặt trận Bình dân cánh tả liên minh", "pos": "phrase"},
    # 3146: population control
    {"ipa": "/ˌpɑːpjəˈleɪʃən kənˈtroʊl/", "vi": "biện pháp kiểm soát mức sinh dân số", "pos": "phrase"},
    # 3147: pressure level
    {"ipa": "/ˈprɛʃər ˈlɛvəl/", "vi": "mức áp suất; cấp độ áp lực chất", "pos": "phrase"},
    # 3148: public knowledge
    {"ipa": "/ˈpʌblɪk ˈnɑːlɪdʒ/", "vi": "điều ai nấy đều biết; tin công khai", "pos": "phrase"},
    # 3149: rate of return
    {"ipa": "/reɪt ʌv rɪˈtɜːrn/", "vi": "tỷ suất sinh lời của khoản đầu tư", "pos": "phrase"},
    # 3150: report card
    {"ipa": "/rɪˈpɔːrt kɑːrd/", "vi": "phiếu liên lạc; bảng điểm học tập", "pos": "phrase"},
    # 3151: rich man
    {"ipa": "/rɪtʃ mæn/", "vi": "người đàn ông giàu có; bậc cự phú", "pos": "phrase"},
    # 3152: running title
    {"ipa": "/ˈrʌnɪŋ ˈtaɪtl/", "vi": "dòng tiêu đề đầu trang sách in ấn", "pos": "phrase"},
    # 3153: school ship
    {"ipa": "/skuːl ʃɪp/", "vi": "tàu thực tập huấn luyện thủy thủ", "pos": "phrase"},
    # 3154: section hand
    {"ipa": "/ˈsɛkʃən hænd/", "vi": "công nhân duy tu đường tàu hỏa", "pos": "phrase"},
    # 3155: security review
    {"ipa": "/sɪˈkjʊrəti rɪˈvjuː/", "vi": "quy trình rà soát an ninh bảo mật", "pos": "phrase"},
    # 3156: seeing red
    {"ipa": "/ˈsiːɪŋ rɛd/", "vi": "nổi trận lôi đình; giận sôi gan", "pos": "phrase"},
    # 3157: senior high
    {"ipa": "/ˈsiːnjər haɪ/", "vi": "trường trung học phổ thông cấp ba", "pos": "phrase"},
    # 3158: sex character
    {"ipa": "/sɛks ˈkærəktər/", "vi": "đặc tính giới tính thứ cấp sinh học", "pos": "phrase"},
    # 3159: sit down
    {"ipa": "/sɪt daʊn/", "vi": "ngồi xuống ghế; cuộc biểu tình ngồi", "pos": "phrase"},
    # 3160: south island
    {"ipa": "/saʊθ ˈaɪlənd/", "vi": "Đảo Nam của đất nước New Zealand", "pos": "phrase"},
    # 3161: star of david
    {"ipa": "/stɑːr ʌv ˈdeɪvɪd/", "vi": "ngôi sao David sáu cánh Do Thái", "pos": "phrase"},
    # 3162: subject case
    {"ipa": "/ˈsʌbdʒɪkt keɪs/", "vi": "chủ cách trong ngữ pháp ngôn ngữ", "pos": "phrase"},
    # 3163: systems program
    {"ipa": "/ˈsɪstəmz ˈproʊɡræm/", "vi": "chương trình hệ thống máy tính điều", "pos": "phrase"},
    # 3164: take notice
    {"ipa": "/teɪk ˈnoʊtɪs/", "vi": "chú ý lưu tâm; để mắt quan sát", "pos": "phrase"},
    # 3165: tax break
    {"ipa": "/tæks breɪk/", "vi": "chính sách ưu đãi miễn giảm thuế", "pos": "phrase"},
    # 3166: tax return
    {"ipa": "/tæks rɪˈtɜːrn/", "vi": "tờ khai quyết toán thuế hàng năm", "pos": "phrase"},
    # 3167: test drive
    {"ipa": "/tɛst draɪv/", "vi": "buổi lái thử xe ô tô; lái thử xe", "pos": "phrase"},
    # 3168: test match
    {"ipa": "/tɛst mætʃ/", "vi": "trận đấu bóng gậy quốc tế đỉnh cao", "pos": "phrase"},
    # 3169: third base
    {"ipa": "/θɜːrd beɪs/", "vi": "chốt gôn số ba trong môn bóng chày", "pos": "phrase"},
    # 3170: this evening
    {"ipa": "/ðɪs ˈiːvnɪŋ/", "vi": "buổi tối ngày hôm nay; tối nay", "pos": "phrase"},
    # 3171: musics
    {"ipa": "/ˈmjuːzɪks/", "vi": "các dòng âm nhạc; các nền âm nhạc", "pos": "noun"},
    # 3172: air gas
    {"ipa": "/ɛr ɡæs/", "vi": "khí đốt điều chế từ không khí", "pos": "phrase"},
    # 3173: air pressure
    {"ipa": "/ɛr ˈprɛʃər/", "vi": "áp suất khí quyển không khí ép nén", "pos": "phrase"},
    # 3174: air station
    {"ipa": "/ɛr ˈsteɪʃən/", "vi": "căn cứ không quân bờ biển hải quân", "pos": "phrase"},
    # 3175: air travel
    {"ipa": "/ɛr ˈtrævəl/", "vi": "chuyến bay bằng máy bay hàng không", "pos": "phrase"},
    # 3176: baby bed
    {"ipa": "/ˈbeɪbi bɛd/", "vi": "chiếc nôi cũi ngủ của em bé sơ sinh", "pos": "phrase"},
    # 3177: ball of fire
    {"ipa": "/bɔːl ʌv ˈfaɪər/", "vi": "quả cầu lửa; người đầy nhiệt huyết", "pos": "phrase"},
    # 3178: bank bill
    {"ipa": "/bæŋk bɪl/", "vi": "tờ giấy bạc ngân phiếu ngân hàng", "pos": "phrase"},
    # 3179: bank rate
    {"ipa": "/bæŋk reɪt/", "vi": "lãi suất chuẩn ngân hàng trung ương", "pos": "phrase"},
    # 3180: battle group
    {"ipa": "/ˈbætəl ɡruːp/", "vi": "cụm tác chiến tàu sân bay quân sự", "pos": "phrase"},
    # 3181: beach house
    {"ipa": "/biːtʃ haʊs/", "vi": "ngôi nhà nghỉ dưỡng ven bãi biển", "pos": "phrase"},
    # 3182: big band
    {"ipa": "/bɪɡ bænd/", "vi": "dàn nhạc jazz lớn biên chế đông", "pos": "phrase"},
    # 3183: book of numbers
    {"ipa": "/bʊk ʌv ˈnʌmbərz/", "vi": "Sách Dân số trong bộ Cựu Ước kinh", "pos": "phrase"},
    # 3184: business leader
    {"ipa": "/ˈbɪznəs ˈliːdər/", "vi": "nhà lãnh đạo giới doanh nhân", "pos": "phrase"},
    # 3185: business letter
    {"ipa": "/ˈbɪznəs ˈlɛtər/", "vi": "thư từ trao đổi thương mại làm ăn", "pos": "phrase"},
    # 3186: carry off
    {"ipa": "/ˈkæri ɔːf/", "vi": "đoạt giải lớn; cướp đi sinh mạng", "pos": "phrase"},
    # 3187: carry through
    {"ipa": "/ˈkæri θruː/", "vi": "thực hiện thành công; giúp vượt khó", "pos": "phrase"},
    # 3188: catch up with
    {"ipa": "/kætʃ ʌp wɪð/", "vi": "đuổi kịp đối thủ; trả giá quả báo", "pos": "phrase"},
    # 3189: center of attention
    {"ipa": "/ˈsɛntər ʌv əˈtɛnʃən/", "vi": "tâm điểm của mọi sự chú ý quan tâm", "pos": "phrase"},
    # 3190: central american country
    {"ipa": "/ˈsɛntrəl əˈmɛrɪkən ˈkʌntri/", "vi": "quốc gia nằm trong vùng Trung Mỹ", "pos": "phrase"},
    # 3191: choice of words
    {"ipa": "/tʃɔɪs ʌv wɜːrdz/", "vi": "cách dùng từ ngữ diễn đạt câu cú", "pos": "phrase"},
    # 3192: christian year
    {"ipa": "/ˈkrɪstʃən jɪr/", "vi": "năm phụng vụ trong Kitô giáo thánh", "pos": "phrase"},
    # 3193: coffee can
    {"ipa": "/ˈkɔːfi kæn/", "vi": "hộp thiếc đậy kín đựng cà phê hạt", "pos": "phrase"},
    # 3194: cost increase
    {"ipa": "/kɔːst ˈɪnkriːs/", "vi": "sự gia tăng chi phí sản xuất vốn", "pos": "phrase"},
    # 3195: council board
    {"ipa": "/ˈkaʊnsəl bɔːrd/", "vi": "bàn hội đồng bàn việc nghị sự chung", "pos": "phrase"},
    # 3196: cross bit
    {"ipa": "/krɔːs bɪt/", "vi": "mũi khoan đá hình chữ thập bốn cánh", "pos": "phrase"},
    # 3197: data track
    {"ipa": "/ˈdeɪtə træk/", "vi": "rãnh từ ghi dữ liệu trên đĩa cứng", "pos": "phrase"},
    # 3198: easy mark
    {"ipa": "/ˈiːzi mɑːrk/", "vi": "con mồi dễ xơi; mục tiêu dễ lừa gạt", "pos": "phrase"},
    # 3199: far and wide
    {"ipa": "/fɑːr ænd waɪd/", "vi": "khắp bốn phương trời; rộng khắp nơi", "pos": "phrase"},
]

with open('scratch/b21_r07_raw_p2.json') as f:
    raw_data = json.load(f)

assert len(raw_data) == 100
assert len(reviewed_entries) == 100

output = []
for i, item in enumerate(raw_data):
    rev = reviewed_entries[i]
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2
    assert len(rev["vi"]) <= 35, f"vi too long: {rev['vi']} ({len(rev['vi'])} chars)"
    assert rev["pos"] in ["noun", "verb", "adj", "adv", "phrase", "intj", "prep", "conj", "pron", "det", "num"]
    
    new_item = {
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
    output.append(new_item)

with open('scratch/b21_r07_p2.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r07_p2.json created successfully and validated!")
