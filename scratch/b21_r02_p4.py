import json

# Manual word-by-word cognitive review for Batch 21 Round 2 Part 4 (records 800-899, IDs 200k.000802 to 200k.000901)
reviewed_entries = [
    # 800: win over
    {"ipa": "/wɪn ˈoʊvər/", "vi": "thuyết phục; tranh thủ sự ủng hộ", "pos": "phrase"},
    # 801: ask out
    {"ipa": "/æsk aʊt/", "vi": "mời hẹn hò; rủ đi chơi riêng", "pos": "phrase"},
    # 802: back room
    {"ipa": "/bæk ruːm/", "vi": "phòng sau; mật thất chính trị", "pos": "phrase"},
    # 803: buy at
    {"ipa": "/baɪ æt/", "vi": "mua ở mức giá; mua sắm tại", "pos": "phrase"},
    # 804: company name
    {"ipa": "/ˈkʌmpəni neɪm/", "vi": "tên doanh nghiệp; tên công ty", "pos": "phrase"},
    # 805: end point
    {"ipa": "/ɛnd pɔɪnt/", "vi": "điểm kết thúc; điểm cuối; đích đến", "pos": "phrase"},
    # 806: go wrong
    {"ipa": "/ɡoʊ rɔːŋ/", "vi": "trục trặc; hỏng hóc; lầm đường", "pos": "phrase"},
    # 807: good old days
    {"ipa": "/ɡʊd oʊld deɪz/", "vi": "ngày xưa tươi đẹp; thời hoàng kim", "pos": "phrase"},
    # 808: head game
    {"ipa": "/hɛd ɡeɪm/", "vi": "trò tâm lý chiến; trò thao túng", "pos": "phrase"},
    # 809: in due time
    {"ipa": "/ɪn djuː taɪm/", "vi": "vào thời điểm thích hợp; đúng lúc", "pos": "phrase"},
    # 810: leave out
    {"ipa": "/liːv aʊt/", "vi": "bỏ sót; loại ra ngoài; không tính", "pos": "phrase"},
    # 811: love story
    {"ipa": "/lʌv ˈstɔːri/", "vi": "chuyện tình yêu; truyện tình cảm", "pos": "phrase"},
    # 812: music school
    {"ipa": "/ˈmjuːzɪk skuːl/", "vi": "trường dạy nhạc; nhạc viện", "pos": "phrase"},
    # 813: question time
    {"ipa": "/ˈkwɛstʃən taɪm/", "vi": "phiên chất vấn trước nghị viện", "pos": "phrase"},
    # 814: right hand
    {"ipa": "/raɪt hænd/", "vi": "bàn tay phải; cánh tay đắc lực", "pos": "phrase"},
    # 815: school of music
    {"ipa": "/skuːl ʌv ˈmjuːzɪk/", "vi": "nhạc viện; trường đào tạo âm nhạc", "pos": "phrase"},
    # 816: sure enough
    {"ipa": "/ʃʊr ɪˈnʌf/", "vi": "quả nhiên; đúng như dự đoán", "pos": "phrase"},
    # 817: time series
    {"ipa": "/taɪm ˈsɪriːz/", "vi": "chuỗi thời gian theo số liệu", "pos": "phrase"},
    # 818: watch out
    {"ipa": "/wɑːtʃ aʊt/", "vi": "coi chừng; cẩn thận đề phòng", "pos": "phrase"},
    # 819: white house
    {"ipa": "/waɪt haʊs/", "vi": "Nhà Trắng; dinh Tổng thống Mỹ", "pos": "phrase"},
    # 820: win back
    {"ipa": "/wɪn bæk/", "vi": "giành lại; lấy lại được lòng tin", "pos": "phrase"},
    # 821: working man
    {"ipa": "/ˈwɜːrkɪŋ mæn/", "vi": "người lao động; công nhân", "pos": "phrase"},
    # 822: about turn
    {"ipa": "/əˈbaʊt tɜːrn/", "vi": "quay đằng sau; sự đổi ý hoàn toàn", "pos": "phrase"},
    # 823: act as
    {"ipa": "/ækt æz/", "vi": "đóng vai trò là; quyền như là", "pos": "phrase"},
    # 824: act on
    {"ipa": "/ækt ɑːn/", "vi": "hành động theo; tác động lên", "pos": "phrase"},
    # 825: at heart
    {"ipa": "/æt hɑːrt/", "vi": "trong thâm tâm; bản chất sâu xa", "pos": "phrase"},
    # 826: back matter
    {"ipa": "/bæk ˈmætər/", "vi": "phần phụ lục cuối sách", "pos": "phrase"},
    # 827: body of work
    {"ipa": "/ˈbɑːdi ʌv wɜːrk/", "vi": "toàn bộ tác phẩm; gia tài sáng tác", "pos": "phrase"},
    # 828: buy up
    {"ipa": "/baɪ ʌp/", "vi": "mua đứt; gom sạch cổ phần", "pos": "phrase"},
    # 829: by heart
    {"ipa": "/baɪ hɑːrt/", "vi": "thuộc lòng; ghi nhớ nằm lòng", "pos": "phrase"},
    # 830: city of god
    {"ipa": "/ˈsɪti ʌv ɡɑːd/", "vi": "Thành phố của Chúa; Thiên đường", "pos": "phrase"},
    # 831: come together
    {"ipa": "/kʌm təˈɡɛðər/", "vi": "tụ họp; gắn kết; tiến triển êm đẹp", "pos": "phrase"},
    # 832: first class
    {"ipa": "/fɜːrst klæs/", "vi": "hạng nhất; loại xuất sắc", "pos": "phrase"},
    # 833: for fun
    {"ipa": "/fɔːr fʌn/", "vi": "để cho vui; đùa vui không ác ý", "pos": "phrase"},
    # 834: from the heart
    {"ipa": "/frʌm ðə hɑːrt/", "vi": "từ tận đáy lòng; rất chân thành", "pos": "phrase"},
    # 835: go along
    {"ipa": "/ɡoʊ əˈlɔːŋ/", "vi": "đồng thuận; đi cùng; tiếp diễn", "pos": "phrase"},
    # 836: good looks
    {"ipa": "/ɡʊd lʊks/", "vi": "vẻ ngoài ưa nhìn; nhan sắc đẹp", "pos": "phrase"},
    # 837: half life
    {"ipa": "/hæf laɪf/", "vi": "chu kỳ bán rã trong vật lý", "pos": "phrase"},
    # 838: hard put
    {"ipa": "/hɑːrd pʊt/", "vi": "gặp nhiều khó khăn; lúng túng", "pos": "phrase"},
    # 839: hard to please
    {"ipa": "/hɑːrd tuː pliːz/", "vi": "khó tính; khó làm cho vừa ý", "pos": "phrase"},
    # 840: high country
    {"ipa": "/haɪ ˈkʌntri/", "vi": "vùng cao nguyên; miền núi non", "pos": "phrase"},
    # 841: high season
    {"ipa": "/haɪ ˈsiːzən/", "vi": "mùa du lịch cao điểm", "pos": "phrase"},
    # 842: house party
    {"ipa": "/haʊs ˈpɑːrti/", "vi": "tiệc tại gia; dạ hội gia đình", "pos": "phrase"},
    # 843: in fun
    {"ipa": "/ɪn fʌn/", "vi": "nói đùa; không nghiêm túc", "pos": "phrase"},
    # 844: level off
    {"ipa": "/ˈlɛvəl ɔːf/", "vi": "chững lại; duy trì thế thăng bằng", "pos": "phrase"},
    # 845: light time
    {"ipa": "/laɪt taɪm/", "vi": "thời gian truyền ánh sáng", "pos": "phrase"},
    # 846: light up
    {"ipa": "/laɪt ʌp/", "vi": "bừng sáng; thắp sáng; châm thuốc", "pos": "phrase"},
    # 847: man of means
    {"ipa": "/mæn ʌv miːnz/", "vi": "người giàu có; bậc phong lưu", "pos": "phrase"},
    # 848: morning time
    {"ipa": "/ˈmɔːrnɪŋ taɪm/", "vi": "buổi sáng; ban mai", "pos": "phrase"},
    # 849: number system
    {"ipa": "/ˈnʌmbər ˈsɪstəm/", "vi": "hệ thống đếm số; hệ cơ số", "pos": "phrase"},
    # 850: old country
    {"ipa": "/oʊld ˈkʌntri/", "vi": "cố hương; quê cha đất tổ", "pos": "phrase"},
    # 851: on fire
    {"ipa": "/ɑːn ˈfaɪər/", "vi": "đang bốc cháy; phong độ đỉnh cao", "pos": "phrase"},
    # 852: party game
    {"ipa": "/ˈpɑːrti ɡeɪm/", "vi": "trò chơi tập thể tiệc tùng", "pos": "phrase"},
    # 853: pay off
    {"ipa": "/peɪ ɔːf/", "vi": "thanh toán hết; đền đáp xứng đáng", "pos": "phrase"},
    # 854: play group
    {"ipa": "/pleɪ ɡruːp/", "vi": "nhóm trẻ mầm non cùng chơi", "pos": "phrase"},
    # 855: pretty much
    {"ipa": "/ˈprɪti mʌtʃ/", "vi": "hầu như; gần như toàn bộ", "pos": "phrase"},
    # 856: second person
    {"ipa": "/ˈsɛkənd ˈpɜːrsən/", "vi": "ngôi thứ hai trong ngữ pháp", "pos": "phrase"},
    # 857: state of war
    {"ipa": "/steɪt ʌv wɔːr/", "vi": "tình trạng chiến tranh", "pos": "phrase"},
    # 858: stay up
    {"ipa": "/steɪ ʌp/", "vi": "thức khuya; không đi ngủ sớm", "pos": "phrase"},
    # 859: take control
    {"ipa": "/teɪk kənˈtroʊl/", "vi": "nắm quyền kiểm soát; điều hành", "pos": "phrase"},
    # 860: take office
    {"ipa": "/teɪk ˈɔːfɪs/", "vi": "nhậm chức vụ; bước vào nhiệm kỳ", "pos": "phrase"},
    # 861: taken up
    {"ipa": "/ˈteɪkən ʌp/", "vi": "bị chiếm dụng; mải mê đắm chìm", "pos": "phrase"},
    # 862: talk down
    {"ipa": "/tɔːk daʊn/", "vi": "nói giọng trịch thượng; át lời", "pos": "phrase"},
    # 863: talking to
    {"ipa": "/ˈtɔːkɪŋ tuː/", "vi": "lời khiển trách; sự răn đe", "pos": "phrase"},
    # 864: turn up
    {"ipa": "/tɜːrn ʌp/", "vi": "xuất hiện; tình cờ đến; vặn to", "pos": "phrase"},
    # 865: with child
    {"ipa": "/wɪð tʃaɪld/", "vi": "mang thai; đang có bầu", "pos": "phrase"},
    # 866: world court
    {"ipa": "/wɜːrld kɔːrt/", "vi": "Tòa án Công lý Quốc tế", "pos": "phrase"},
    # 867: air well
    {"ipa": "/ɛr wɛl/", "vi": "giếng trời; giếng thông gió tòa nhà", "pos": "phrase"},
    # 868: buy out
    {"ipa": "/baɪ aʊt/", "vi": "mua đứt; thâu tóm toàn bộ cổ phần", "pos": "phrase"},
    # 869: buy time
    {"ipa": "/baɪ taɪm/", "vi": "câu giờ; tìm cách trì hoãn", "pos": "phrase"},
    # 870: car part
    {"ipa": "/kɑːr pɑːrt/", "vi": "phụ tùng ô tô; linh kiện xe hơi", "pos": "phrase"},
    # 871: country house
    {"ipa": "/ˈkʌntri haʊs/", "vi": "biệt thự nông thôn; nhà vùng quê", "pos": "phrase"},
    # 872: deal out
    {"ipa": "/diːl aʊt/", "vi": "chia bài; phân phát; giáng đòn phạt", "pos": "phrase"},
    # 873: first cause
    {"ipa": "/fɜːrst kɔːz/", "vi": "nguyên nhân đầu tiên; khởi nguyên", "pos": "phrase"},
    # 874: go past
    {"ipa": "/ɡoʊ pæst/", "vi": "đi ngang qua; vượt qua mặt", "pos": "phrase"},
    # 875: hand down
    {"ipa": "/hænd daʊn/", "vi": "truyền lại cho đời sau; tuyên án", "pos": "phrase"},
    # 876: in front
    {"ipa": "/ɪn frʌnt/", "vi": "ở phía trước; đằng trước", "pos": "phrase"},
    # 877: last half
    {"ipa": "/læst hæf/", "vi": "hiệp hai; nửa thời gian sau", "pos": "phrase"},
    # 878: last not least
    {"ipa": "/læst nɑːt liːst/", "vi": "sau cùng nhưng không kém quan trọng", "pos": "phrase"},
    # 879: life office
    {"ipa": "/laɪf ˈɔːfɪs/", "vi": "hãng bảo hiểm nhân thọ", "pos": "phrase"},
    # 880: make happy
    {"ipa": "/meɪk ˈhæpi/", "vi": "làm cho hạnh phúc; đem lại niềm vui", "pos": "phrase"},
    # 881: move into
    {"ipa": "/muːv ˈɪntuː/", "vi": "dọn vào ở; bắt đầu tham gia ngành", "pos": "phrase"},
    # 882: move over
    {"ipa": "/muːv ˈoʊvər/", "vi": "nhường chỗ; xích sang một bên", "pos": "phrase"},
    # 883: open house
    {"ipa": "/ˈoʊpən haʊs/", "vi": "ngày hội mở cửa; tiệc mở tự do", "pos": "phrase"},
    # 884: reason out
    {"ipa": "/ˈriːzən aʊt/", "vi": "suy luận thấu đáo; tìm ra lời giải", "pos": "phrase"},
    # 885: report out
    {"ipa": "/rɪˈpɔːrt aʊt/", "vi": "thông qua dự luật tại ủy ban", "pos": "phrase"},
    # 886: right along
    {"ipa": "/raɪt əˈlɔːŋ/", "vi": "suốt từ đầu; liên tục không ngớt", "pos": "phrase"},
    # 887: still room
    {"ipa": "/ˈstɪl ruːm/", "vi": "phòng chưng cất; phòng pha chế trà", "pos": "phrase"},
    # 888: the street
    {"ipa": "/ðə striːt/", "vi": "Phố Wall; giới tài chính New York", "pos": "phrase"},
    # 889: too large
    {"ipa": "/tuː lɑːrdʒ/", "vi": "quá khổ; quá đồ sộ", "pos": "phrase"},
    # 890: turn out
    {"ipa": "/tɜːrn aʊt/", "vi": "hóa ra; sản xuất; có mặt tham dự", "pos": "phrase"},
    # 891: verier
    {"ipa": "/ˈvɛriər/", "vi": "đúng thực hơn; xác thực hơn", "pos": "adj"},
    # 892: veriest
    {"ipa": "/ˈvɛriɪst/", "vi": "đúng thực nhất; đích thực nhất", "pos": "adj"},
    # 893: young man
    {"ipa": "/jʌŋ mæn/", "vi": "chàng trai trẻ; thanh niên nam", "pos": "phrase"},
    # 894: evener
    {"ipa": "/ˈiːvənər/", "vi": "đều đặn hơn; bằng phẳng hơn", "pos": "adj"},
    # 895: evenest
    {"ipa": "/ˈiːvənɪst/", "vi": "đều đặn nhất; bằng phẳng nhất", "pos": "adj"},
    # 896: act up
    {"ipa": "/ækt ʌp/", "vi": "dở chứng; nghịch ngợm quậy phá", "pos": "phrase"},
    # 897: ask over
    {"ipa": "/æsk ˈoʊvər/", "vi": "mời qua nhà chơi", "pos": "phrase"},
    # 898: bring to
    {"ipa": "/brɪŋ tuː/", "vi": "hồi tỉnh; đánh thức dậy", "pos": "phrase"},
    # 899: check out
    {"ipa": "/tʃɛk aʊt/", "vi": "trả phòng khách sạn; kiểm tra kỹ", "pos": "phrase"},
]

with open('scratch/b21_r02_raw_p4.json') as f:
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

with open('scratch/b21_r02_p4.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r02_p4.json created successfully and validated!")
