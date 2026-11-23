import json

# Manual word-by-word cognitive review for Batch 21 Round 6 Part 5 (records 2900-2999, IDs 200k.002902 to 200k.003001)
reviewed_entries = [
    # 2900: law student
    {"ipa": "/lɔː ˈstuːdənt/", "vi": "sinh viên chuyên ngành luật", "pos": "phrase"},
    # 2901: legal community
    {"ipa": "/ˈliːɡəl kəˈmjuːnəti/", "vi": "giới luật sư; cộng đồng pháp lý", "pos": "phrase"},
    # 2902: life insurance
    {"ipa": "/laɪf ɪnˈʃʊrəns/", "vi": "hợp đồng bảo hiểm nhân thọ trọn đời", "pos": "phrase"},
    # 2903: limited war
    {"ipa": "/ˈlɪmɪtɪd wɔːr/", "vi": "chiến tranh cục bộ hạn chế mục tiêu", "pos": "phrase"},
    # 2904: line double
    {"ipa": "/laɪn ˈdʌbəl/", "vi": "cú đánh bóng căng trúng hai gôn", "pos": "phrase"},
    # 2905: little sister
    {"ipa": "/ˈlɪtəl ˈsɪstər/", "vi": "em gái ruột; cô em gái nhỏ bé", "pos": "phrase"},
    # 2906: love letter
    {"ipa": "/lʌv ˈlɛtər/", "vi": "lá thư tình; bức thư tình yêu", "pos": "phrase"},
    # 2907: military training
    {"ipa": "/ˈmɪlətɛri ˈtreɪnɪŋ/", "vi": "khóa huấn luyện quân sự nhập ngũ", "pos": "phrase"},
    # 2908: national capital
    {"ipa": "/ˈnæʃənəl ˈkæpɪtl/", "vi": "thủ đô quốc gia; nguồn vốn nhà nước", "pos": "phrase"},
    # 2909: old lady
    {"ipa": "/oʊld ˈleɪdi/", "vi": "bà lão; bà xã; người mẹ kính yêu", "pos": "phrase"},
    # 2910: on the spot
    {"ipa": "/ɑːn ðə spɑːt/", "vi": "ngay tại chỗ; giải quyết tức thì", "pos": "phrase"},
    # 2911: post card
    {"ipa": "/poʊst kɑːrd/", "vi": "tấm bưu thiếp gửi qua bưu điện", "pos": "phrase"},
    # 2912: power station
    {"ipa": "/ˈpaʊər ˈsteɪʃən/", "vi": "nhà máy phát điện; trạm phát điện", "pos": "phrase"},
    # 2913: present perfect
    {"ipa": "/ˈprɛzənt ˈpɜːrfɪkt/", "vi": "thì hiện tại hoàn thành ngữ pháp", "pos": "phrase"},
    # 2914: production cost
    {"ipa": "/prəˈdʌkʃən kɔːst/", "vi": "chi phí sản xuất gia công hàng hóa", "pos": "phrase"},
    # 2915: rich people
    {"ipa": "/rɪtʃ ˈpiːpəl/", "vi": "giới nhà giàu; tầng lớp thượng lưu", "pos": "phrase"},
    # 2916: room access
    {"ipa": "/ruːm ˈæksɛs/", "vi": "lối vào phòng; quyền sử dụng phòng", "pos": "phrase"},
    # 2917: sea room
    {"ipa": "/siː ruːm/", "vi": "khoảng biển trống để điều khiển tàu", "pos": "phrase"},
    # 2918: second nature
    {"ipa": "/ˈsɛkənd ˈneɪtʃər/", "vi": "thói quen thành bản năng tự nhiên", "pos": "phrase"},
    # 2919: secretary of state
    {"ipa": "/ˈsɛkrətɛri ʌv steɪt/", "vi": "Ngoại trưởng Hoa Kỳ; bộ trưởng", "pos": "phrase"},
    # 2920: service charge
    {"ipa": "/ˈsɜːrvɪs tʃɑːrdʒ/", "vi": "phí dịch vụ; tiền phụ thu dịch vụ", "pos": "phrase"},
    # 2921: service station
    {"ipa": "/ˈsɜːrvɪs ˈsteɪʃən/", "vi": "trạm xăng dầu kiêm sửa chữa xe ô tô", "pos": "phrase"},
    # 2922: sit by
    {"ipa": "/sɪt baɪ/", "vi": "khoanh tay đứng nhìn; bàng quan", "pos": "phrase"},
    # 2923: sit out
    {"ipa": "/sɪt aʊt/", "vi": "ngồi ngoài không tham gia hoạt động", "pos": "phrase"},
    # 2924: sit up
    {"ipa": "/sɪt ʌp/", "vi": "ngồi thẳng lưng dậy; thức khuya chờ", "pos": "phrase"},
    # 2925: small capital
    {"ipa": "/smɔːl ˈkæpɪtl/", "vi": "chữ in hoa nhỏ font chữ; vốn ít", "pos": "phrase"},
    # 2926: take stock
    {"ipa": "/teɪk stɑːk/", "vi": "kiểm kê hàng; đánh giá lại thế trận", "pos": "phrase"},
    # 2927: tax cut
    {"ipa": "/tæks kʌt/", "vi": "biện pháp cắt giảm biểu thuế suất", "pos": "phrase"},
    # 2928: town meeting
    {"ipa": "/taʊn ˈmiːtɪŋ/", "vi": "phiên họp hội đồng dân cư thị trấn", "pos": "phrase"},
    # 2929: trip out
    {"ipa": "/trɪp aʊt/", "vi": "phê thuốc ảo giác; đê mê mộng mị", "pos": "phrase"},
    # 2930: trip up
    {"ipa": "/trɪp ʌp/", "vi": "ngáng chân ngã; vấp lỗi sơ đẳng", "pos": "phrase"},
    # 2931: tv star
    {"ipa": "/ˌtiːˈviː stɑːr/", "vi": "ngôi sao sáng trên màn ảnh nhỏ", "pos": "phrase"},
    # 2932: waiting room
    {"ipa": "/ˈweɪtɪŋ ruːm/", "vi": "phòng ngồi chờ tàu xe bệnh viện", "pos": "phrase"},
    # 2933: water gas
    {"ipa": "/ˈwɔːtər ɡæs/", "vi": "hỗn hợp khí than ướt làm nhiên liệu", "pos": "phrase"},
    # 2934: water ice
    {"ipa": "/ˈwɔːtər aɪs/", "vi": "nước đá đông lạnh; món kem đá bào", "pos": "phrase"},
    # 2935: water travel
    {"ipa": "/ˈwɔːtər ˈtrævəl/", "vi": "chuyến đi du hành bằng đường thủy", "pos": "phrase"},
    # 2936: white russian
    {"ipa": "/waɪt ˈrʌʃən/", "vi": "người Bạch Nga; ly cocktail sữa", "pos": "phrase"},
    # 2937: word picture
    {"ipa": "/wɜːrd ˈpɪktʃər/", "vi": "bức họa miêu tả sống động bằng lời", "pos": "phrase"},
    # 2938: written report
    {"ipa": "/ˈrɪtən rɪˈpɔːrt/", "vi": "bản báo cáo trình bày bằng văn bản", "pos": "phrase"},
    # 2939: persons
    {"ipa": "/ˈpɜːrsənz/", "vi": "những cá nhân; các đối tượng người", "pos": "noun"},
    # 2940: air base
    {"ipa": "/ɛr beɪs/", "vi": "căn cứ không quân; sân bay quân sự", "pos": "phrase"},
    # 2941: association area
    {"ipa": "/əˌsoʊsiˈeɪʃən ˈɛriə/", "vi": "vùng liên hợp chức năng vỏ não", "pos": "phrase"},
    # 2942: bank account
    {"ipa": "/bæŋk əˈkaʊnt/", "vi": "tài khoản tiền gửi tại ngân hàng", "pos": "phrase"},
    # 2943: base hit
    {"ipa": "/beɪs hɪt/", "vi": "cú đánh bóng giúp chiếm gôn an toàn", "pos": "phrase"},
    # 2944: big gun
    {"ipa": "/bɪɡ ɡʌn/", "vi": "khẩu đại bác lớn; nhân vật quyền uy", "pos": "phrase"},
    # 2945: blood type
    {"ipa": "/blʌd taɪp/", "vi": "nhóm máu trong hệ kháng nguyên ABO", "pos": "phrase"},
    # 2946: box office
    {"ipa": "/bɑːks ˈɔːfɪs/", "vi": "quầy bán vé xem phim; doanh thu vé", "pos": "phrase"},
    # 2947: broken in
    {"ipa": "/ˈbroʊkən ɪn/", "vi": "đã được thuần hóa; đi vừa chân êm", "pos": "phrase"},
    # 2948: carry out
    {"ipa": "/ˈkæri aʊt/", "vi": "thực hiện triển khai; thi hành lệnh", "pos": "phrase"},
    # 2949: carry the can
    {"ipa": "/ˈkæri ðə kæn/", "vi": "đứng mũi chịu sào; gánh trách nhiệm", "pos": "phrase"},
    # 2950: chance upon
    {"ipa": "/tʃæns əˈpɑːn/", "vi": "tình cờ bắt gặp; ngẫu nhiên gặp", "pos": "phrase"},
    # 2951: city manager
    {"ipa": "/ˈsɪti ˈmænɪdʒər/", "vi": "viên chức điều hành quản trị đô thị", "pos": "phrase"},
    # 2952: country and western
    {"ipa": "/ˈkʌntri ænd ˈwɛstərn/", "vi": "dòng nhạc đồng quê viễn tây nước Mỹ", "pos": "phrase"},
    # 2953: credit line
    {"ipa": "/ˈkrɛdɪt laɪn/", "vi": "hạn mức tín dụng; dòng tên ghi nhận", "pos": "phrase"},
    # 2954: credit order
    {"ipa": "/ˈkrɛdɪt ˈɔːrdər/", "vi": "lệnh mở tín dụng; đơn hàng mua nợ", "pos": "phrase"},
    # 2955: credit side
    {"ipa": "/ˈkrɛdɪt saɪd/", "vi": "bên Có trong bảng đối chiếu kế toán", "pos": "phrase"},
    # 2956: cross country
    {"ipa": "/krɔːs ˈkʌntri/", "vi": "chạy việt dã; băng đồng đường dài", "pos": "phrase"},
    # 2957: dark matter
    {"ipa": "/dɑːrk ˈmætər/", "vi": "vật chất tối trong vũ trụ học", "pos": "phrase"},
    # 2958: end product
    {"ipa": "/ɛnd ˈprɑːdʌkt/", "vi": "thành phẩm hoàn thiện cuối cùng", "pos": "phrase"},
    # 2959: federal department
    {"ipa": "/ˈfɛdərəl dɪˈpɑːrtmənt/", "vi": "bộ liên bang trực thuộc chính phủ", "pos": "phrase"},
    # 2960: fire code
    {"ipa": "/ˈfaɪər koʊd/", "vi": "bộ quy chuẩn phòng cháy chữa cháy", "pos": "phrase"},
    # 2961: fire door
    {"ipa": "/ˈfaɪər dɔːr/", "vi": "cửa thép ngăn lửa chống cháy lan", "pos": "phrase"},
    # 2962: full service bank
    {"ipa": "/fʊl ˈsɜːrvɪs bæŋk/", "vi": "ngân hàng đa năng dịch vụ toàn diện", "pos": "phrase"},
    # 2963: funny story
    {"ipa": "/ˈfʌni ˈstɔːri/", "vi": "mẩu chuyện cười; chuyện hài hước", "pos": "phrase"},
    # 2964: good luck
    {"ipa": "/ɡʊd lʌk/", "vi": "vận may cát tường; lời chúc may mắn", "pos": "phrase"},
    # 2965: high bar
    {"ipa": "/haɪ bɑːr/", "vi": "xà đơn thể dục; mức chuẩn mực cao", "pos": "phrase"},
    # 2966: home rule
    {"ipa": "/hoʊm ruːl/", "vi": "quyền tự trị quản lý địa phương", "pos": "phrase"},
    # 2967: in agreement
    {"ipa": "/ɪn əˈɡriːmənt/", "vi": "đồng thuận nhất trí quan điểm chung", "pos": "phrase"},
    # 2968: in theory
    {"ipa": "/ɪn ˈθiːəri/", "vi": "về mặt lý thuyết trên giấy tờ", "pos": "phrase"},
    # 2969: key word
    {"ipa": "/kiː wɜːrd/", "vi": "từ khóa tìm kiếm; từ vựng mấu chốt", "pos": "phrase"},
    # 2970: land tax
    {"ipa": "/lænd tæks/", "vi": "thuế sử dụng đất đai tài sản", "pos": "phrase"},
    # 2971: law of effect
    {"ipa": "/lɔː ʌv ɪˈfɛkt/", "vi": "quy luật tác động trong tâm lý học", "pos": "phrase"},
    # 2972: lead bank
    {"ipa": "/liːd bæŋk/", "vi": "ngân hàng đầu mối thu xếp vốn vay", "pos": "phrase"},
    # 2973: legal age
    {"ipa": "/ˈliːɡəl eɪdʒ/", "vi": "tuổi thành niên theo quy định luật", "pos": "phrase"},
    # 2974: line of credit
    {"ipa": "/laɪn ʌv ˈkrɛdɪt/", "vi": "hạn mức thấu chi tín dụng ngân hàng", "pos": "phrase"},
    # 2975: luck into
    {"ipa": "/lʌk ˈɪntuː/", "vi": "tình cờ vớ được may mắn; gặp thời", "pos": "phrase"},
    # 2976: medical record
    {"ipa": "/ˈmɛdɪkəl ˈrɛkərd/", "vi": "hồ sơ bệnh án theo dõi sức khỏe", "pos": "phrase"},
    # 2977: middle english
    {"ipa": "/ˈmɪdəl ˈɪŋɡlɪʃ/", "vi": "tiếng Anh thời kỳ Trung cổ lịch sử", "pos": "phrase"},
    # 2978: military press
    {"ipa": "/ˈmɪlətɛri prɛs/", "vi": "động tác đẩy tạ qua đầu đứng thẳng", "pos": "phrase"},
    # 2979: movie film
    {"ipa": "/ˈmuːvi fɪlm/", "vi": "cuộn phim nhựa chiếu bóng điện ảnh", "pos": "phrase"},
    # 2980: national park service
    {"ipa": "/ˈnæʃənəl pɑːrk ˈsɜːrvɪs/", "vi": "Cục Quản lý Công viên Quốc gia Mỹ", "pos": "phrase"},
    # 2981: natural process
    {"ipa": "/ˈnætʃərəl ˈprɑːsɛs/", "vi": "tiến trình phát triển tự nhiên", "pos": "phrase"},
    # 2982: no doubt
    {"ipa": "/noʊ daʊt/", "vi": "chắc chắn không chút nghi ngờ gì", "pos": "phrase"},
    # 2983: north sea
    {"ipa": "/nɔːrθ siː/", "vi": "vùng Biển Bắc lạnh giá châu Âu", "pos": "phrase"},
    # 2984: note of hand
    {"ipa": "/noʊt ʌv hænd/", "vi": "giấy hẹn nợ viết tay; kỳ phiếu vay", "pos": "phrase"},
    # 2985: on purpose
    {"ipa": "/ɑːn ˈpɜːrpəs/", "vi": "cố tình chủ ý; cố ý từ trước", "pos": "phrase"},
    # 2986: pass along
    {"ipa": "/pæs əˈlɔːŋ/", "vi": "chuyền tay gửi tiếp; truyền đạt lại", "pos": "phrase"},
    # 2987: plan of attack
    {"ipa": "/plæn ʌv əˈtæk/", "vi": "kế hoạch tác chiến; phương án xử lý", "pos": "phrase"},
    # 2988: required course
    {"ipa": "/rɪˈkwaɪərd kɔːrs/", "vi": "học phần bắt buộc phải hoàn thành", "pos": "phrase"},
    # 2989: responsible for
    {"ipa": "/rɪˈspɑːnsəbəl fɔːr/", "vi": "chịu trách nhiệm pháp lý về việc", "pos": "phrase"},
    # 2990: round shot
    {"ipa": "/raʊnd ʃɑːt/", "vi": "viên đạn đại bác tròn bằng đặc gang", "pos": "phrase"},
    # 2991: security interest
    {"ipa": "/sɪˈkjʊrəti ˈɪntrəst/", "vi": "quyền lợi bảo đảm tài sản thế chấp", "pos": "phrase"},
    # 2992: sell someone out
    {"ipa": "/sɛl ˈsʌmwʌn aʊt/", "vi": "bán đứng phản bội bạn hữu đồng đội", "pos": "phrase"},
    # 2993: send word
    {"ipa": "/sɛnd wɜːrd/", "vi": "gửi tin tức nhắn nhủ; báo tin sang", "pos": "phrase"},
    # 2994: sick of
    {"ipa": "/sɪk ʌv/", "vi": "chán ngấy ngán ngẩm; phát ngấy vì", "pos": "phrase"},
    # 2995: skin over
    {"ipa": "/skɪn ˈoʊvər/", "vi": "lên da non kéo vảy vết thương", "pos": "phrase"},
    # 2996: stuff shot
    {"ipa": "/stʌf ʃɑːt/", "vi": "cú úp rổ dũng mãnh trong bóng rổ", "pos": "phrase"},
    # 2997: sun city
    {"ipa": "/sʌn ˈsɪti/", "vi": "khu đô thị hưu trí Sun City tại Mỹ", "pos": "phrase"},
    # 2998: time machine
    {"ipa": "/taɪm məˈʃiːn/", "vi": "cỗ máy thời gian du hành quá khứ", "pos": "phrase"},
    # 2999: turn of events
    {"ipa": "/tɜːrn ʌv ɪˈvɛnts/", "vi": "bước ngoặt diễn biến của cục diện", "pos": "phrase"},
]

with open('scratch/b21_r06_raw_p5.json') as f:
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

with open('scratch/b21_r06_p5.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r06_p5.json created successfully and validated!")
