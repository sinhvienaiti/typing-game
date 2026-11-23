import json

# Manual word-by-word cognitive review for Batch 21 Round 3 Part 1 (records 1000-1099, IDs 200k.001002 to 200k.001101)
reviewed_entries = [
    # 1000: full point
    {"ipa": "/fʊl pɔɪnt/", "vi": "dấu chấm câu; dấu chấm hết", "pos": "phrase"},
    # 1001: hard times
    {"ipa": "/hɑːrd taɪmz/", "vi": "thời kỳ gian khó; lúc cơ hàn", "pos": "phrase"},
    # 1002: have words
    {"ipa": "/hæv wɜːrdz/", "vi": "lời qua tiếng lại; cãi vã to tiếng", "pos": "phrase"},
    # 1003: hit home
    {"ipa": "/hɪt hoʊm/", "vi": "thấm thía; chạm trúng tim đen", "pos": "phrase"},
    # 1004: hit man
    {"ipa": "/hɪt mæn/", "vi": "sát thủ giết thuê; tay súng ngầm", "pos": "phrase"},
    # 1005: in the main
    {"ipa": "/ɪn ðə meɪn/", "vi": "nhìn chung; phần lớn là", "pos": "phrase"},
    # 1006: leave off
    {"ipa": "/liːv ɔːf/", "vi": "dừng lại; ngưng; bỏ dở chừng", "pos": "phrase"},
    # 1007: light year
    {"ipa": "/laɪt jɪr/", "vi": "năm ánh sáng; khoảng cách xa vời", "pos": "phrase"},
    # 1008: little office
    {"ipa": "/ˈlɪtəl ˈɔːfɪs/", "vi": "kinh phụng vụ nguyện ngắn", "pos": "phrase"},
    # 1009: mind game
    {"ipa": "/maɪnd ɡeɪm/", "vi": "trò đấu trí; đòn tâm lý thao túng", "pos": "phrase"},
    # 1010: move through
    {"ipa": "/muːv θruː/", "vi": "băng qua; đi xuyên qua đám đông", "pos": "phrase"},
    # 1011: news show
    {"ipa": "/nuːz ʃoʊ/", "vi": "chương trình thời sự tin tức", "pos": "phrase"},
    # 1012: old south
    {"ipa": "/oʊld saʊθ/", "vi": "miền Nam nước Mỹ thời kỳ xưa", "pos": "phrase"},
    # 1013: police work
    {"ipa": "/pəˈliːs wɜːrk/", "vi": "công tác cảnh sát; nghiệp vụ", "pos": "phrase"},
    # 1014: power system
    {"ipa": "/ˈpaʊər ˈsɪstəm/", "vi": "hệ thống điện lực; mạng lưới điện", "pos": "phrase"},
    # 1015: support system
    {"ipa": "/səˈpɔːrt ˈsɪstəm/", "vi": "hệ thống nâng đỡ; mạng lưới hỗ trợ", "pos": "phrase"},
    # 1016: take leave
    {"ipa": "/teɪk liːv/", "vi": "cáo từ; xin phép rời đi; từ biệt", "pos": "phrase"},
    # 1017: turn back
    {"ipa": "/tɜːrn bæk/", "vi": "quay trở lại; quay đầu xe", "pos": "phrase"},
    # 1018: water system
    {"ipa": "/ˈwɔːtər ˈsɪstəm/", "vi": "hệ thống cấp nước; lưu vực sông", "pos": "phrase"},
    # 1019: week by week
    {"ipa": "/wiːk baɪ wiːk/", "vi": "từng tuần một; đều đặn hàng tuần", "pos": "phrase"},
    # 1020: world series
    {"ipa": "/wɜːrld ˈsɪriːz/", "vi": "Giải bóng chày World Series Mỹ", "pos": "phrase"},
    # 1021: beings
    {"ipa": "/ˈbiːɪŋz/", "vi": "những sinh linh; các sinh thể sống", "pos": "noun"},
    # 1022: all clear
    {"ipa": "/ɔːl klɪr/", "vi": "tín hiệu báo yên; báo hết nguy hiểm", "pos": "phrase"},
    # 1023: bit part
    {"ipa": "/bɪt pɑːrt/", "vi": "vai diễn phụ nhỏ; vai phụ mờ nhạt", "pos": "phrase"},
    # 1024: buy off
    {"ipa": "/baɪ ɔːf/", "vi": "mua chuộc bằng tiền; đút lót", "pos": "phrase"},
    # 1025: death house
    {"ipa": "/dɛθ haʊs/", "vi": "khu biệt giam tử tù chờ thi hành", "pos": "phrase"},
    # 1026: every bit
    {"ipa": "/ˈɛvri bɪt/", "vi": "từng chút một; hoàn toàn hệt như", "pos": "phrase"},
    # 1027: for the moment
    {"ipa": "/fɔːr ðə ˈmoʊmənt/", "vi": "tạm thời trước mắt; trong lúc này", "pos": "phrase"},
    # 1028: full stop
    {"ipa": "/fʊl stɑːp/", "vi": "dấu chấm câu; chấm hết dứt điểm", "pos": "phrase"},
    # 1029: head start
    {"ipa": "/hɛd stɑːrt/", "vi": "lợi thế xuất phát trước", "pos": "phrase"},
    # 1030: in force
    {"ipa": "/ɪn fɔːrs/", "vi": "có hiệu lực thi hành; rầm rộ đông", "pos": "phrase"},
    # 1031: line of thought
    {"ipa": "/laɪn ʌv θɔːt/", "vi": "mạch suy nghĩ; mạch tư duy", "pos": "phrase"},
    # 1032: little girl
    {"ipa": "/ˈlɪtəl ɡɜːrl/", "vi": "cô bé; bé gái nhỏ", "pos": "phrase"},
    # 1033: little john
    {"ipa": "/ˈlɪtəl dʒɑːn/", "vi": "nhân vật Little John huyền thoại", "pos": "phrase"},
    # 1034: make fun
    {"ipa": "/meɪk fʌn/", "vi": "trêu chọc; đem ra làm trò đùa", "pos": "phrase"},
    # 1035: making water
    {"ipa": "/ˈmeɪkɪŋ ˈwɔːtər/", "vi": "hành vi đi tiểu tiện", "pos": "phrase"},
    # 1036: march out
    {"ipa": "/mɑːrtʃ aʊt/", "vi": "hành quân ra ngoài; diễu hành ra", "pos": "phrase"},
    # 1037: meet up with
    {"ipa": "/miːt ʌp wɪð/", "vi": "gặp gỡ; hẹn gặp mặt ai", "pos": "phrase"},
    # 1038: new london
    {"ipa": "/nuː ˈlʌndən/", "vi": "thành phố New London tại Mỹ", "pos": "phrase"},
    # 1039: on board
    {"ipa": "/ɑːn bɔːrd/", "vi": "trên tàu xe; đồng thuận tham gia", "pos": "phrase"},
    # 1040: on the road
    {"ipa": "/ɑːn ðə roʊd/", "vi": "đang đi trên đường; đang lưu diễn", "pos": "phrase"},
    # 1041: party of god
    {"ipa": "/ˈpɑːrti ʌv ɡɑːd/", "vi": "Đảng của Thượng đế; nhóm Hezbollah", "pos": "phrase"},
    # 1042: power point
    {"ipa": "/ˈpaʊər pɔɪnt/", "vi": "ổ cắm điện; ổ cắm nguồn", "pos": "phrase"},
    # 1043: public service
    {"ipa": "/ˈpʌblɪk ˈsɜːrvɪs/", "vi": "dịch vụ công ích; công vụ", "pos": "phrase"},
    # 1044: small person
    {"ipa": "/smɔːl ˈpɜːrsən/", "vi": "người tầm vóc nhỏ; người tí hon", "pos": "phrase"},
    # 1045: state of matter
    {"ipa": "/steɪt ʌv ˈmætər/", "vi": "trạng thái vật chất", "pos": "phrase"},
    # 1046: stay off
    {"ipa": "/steɪ ɔːf/", "vi": "tránh xa; không chạm vào; kiêng", "pos": "phrase"},
    # 1047: system call
    {"ipa": "/ˈsɪstəm kɔːl/", "vi": "lời gọi hệ thống trong tin học", "pos": "phrase"},
    # 1048: talk show
    {"ipa": "/tɔːk ʃoʊ/", "vi": "chương trình tọa đàm; talk show", "pos": "phrase"},
    # 1049: too soon
    {"ipa": "/tuː suːn/", "vi": "quá sớm; vội vàng sớm", "pos": "phrase"},
    # 1050: top side
    {"ipa": "/tɑːp saɪd/", "vi": "phía trên cùng; phần mạn trên tàu", "pos": "phrase"},
    # 1051: turn off
    {"ipa": "/tɜːrn ɔːf/", "vi": "tắt máy; rẽ lối khác; gây mất hứng", "pos": "phrase"},
    # 1052: white person
    {"ipa": "/waɪt ˈpɜːrsən/", "vi": "người da trắng", "pos": "phrase"},
    # 1053: whole name
    {"ipa": "/hoʊl neɪm/", "vi": "từ chỉ toàn thể; tên gọi trọn vẹn", "pos": "phrase"},
    # 1054: whole number
    {"ipa": "/hoʊl ˈnʌmbər/", "vi": "số nguyên không âm; số toàn phần", "pos": "phrase"},
    # 1055: big hand
    {"ipa": "/bɪɡ hænd/", "vi": "kim phút đồng hồ; tràng vỗ tay lớn", "pos": "phrase"},
    # 1056: business line
    {"ipa": "/ˈbɪznəs laɪn/", "vi": "ngành hàng buôn bán; dây truyền", "pos": "phrase"},
    # 1057: car company
    {"ipa": "/kɑːr ˈkʌmpəni/", "vi": "hãng sản xuất ô tô", "pos": "phrase"},
    # 1058: check off
    {"ipa": "/tʃɛk ɔːf/", "vi": "đánh dấu kiểm tra; tích vào ô chọn", "pos": "phrase"},
    # 1059: clear out
    {"ipa": "/klɪr aʊt/", "vi": "dọn sạch sẽ; cuốn gói rời đi", "pos": "phrase"},
    # 1060: clear up
    {"ipa": "/klɪr ʌp/", "vi": "trời quang đãng; giải tỏa khúc mắc", "pos": "phrase"},
    # 1061: come close
    {"ipa": "/kʌm kloʊs/", "vi": "tiến lại gần; suýt chút nữa", "pos": "phrase"},
    # 1062: family court
    {"ipa": "/ˈfæməli kɔːrt/", "vi": "tòa án thụ lý hôn nhân gia đình", "pos": "phrase"},
    # 1063: game room
    {"ipa": "/ɡeɪm ruːm/", "vi": "phòng chơi game giải trí", "pos": "phrase"},
    # 1064: get word
    {"ipa": "/ɡɛt wɜːrd/", "vi": "nhận được tin tức; nghe phong thanh", "pos": "phrase"},
    # 1065: hard water
    {"ipa": "/hɑːrd ˈwɔːtər/", "vi": "nước cứng chứa nhiều khoáng chất", "pos": "phrase"},
    # 1066: line of business
    {"ipa": "/laɪn ʌv ˈbɪznəs/", "vi": "lĩnh vực hoạt động kinh doanh", "pos": "phrase"},
    # 1067: order of business
    {"ipa": "/ˈɔːrdər ʌv ˈbɪznəs/", "vi": "chương trình nghị sự buổi họp", "pos": "phrase"},
    # 1068: rest on
    {"ipa": "/rɛst ɑːn/", "vi": "tựa lên; dựa trên cơ sở; nhìn chăm", "pos": "phrase"},
    # 1069: small change
    {"ipa": "/smɔːl tʃeɪndʒ/", "vi": "tiền lẻ thối lại; chuyện vặt vãnh", "pos": "phrase"},
    # 1070: third world
    {"ipa": "/θɜːrd wɜːrld/", "vi": "các nước thuộc Thế giới thứ ba", "pos": "phrase"},
    # 1071: time study
    {"ipa": "/taɪm ˈstʌdi/", "vi": "nghiên cứu định mức thời gian", "pos": "phrase"},
    # 1072: to date
    {"ipa": "/tuː deɪt/", "vi": "cho đến nay; tính đến thời điểm này", "pos": "phrase"},
    # 1073: at rest
    {"ipa": "/æt rɛst/", "vi": "đang nghỉ ngơi; yên giấc ngàn thu", "pos": "phrase"},
    # 1074: back street
    {"ipa": "/bæk striːt/", "vi": "phố nhỏ hẻo lánh; ngõ ngách sau", "pos": "phrase"},
    # 1075: board up
    {"ipa": "/bɔːrd ʌp/", "vi": "bịt kín bằng ván gỗ; đóng ván chắn", "pos": "phrase"},
    # 1076: cut out
    {"ipa": "/kʌt aʊt/", "vi": "cắt bỏ; ngưng động cơ; phù hợp với", "pos": "phrase"},
    # 1077: cut up
    {"ipa": "/kʌt ʌp/", "vi": "chặt nhỏ ra; làm đau lòng xót xa", "pos": "phrase"},
    # 1078: early days
    {"ipa": "/ˈɜːrli deɪz/", "vi": "thời kỳ đầu; giai đoạn sơ khai", "pos": "phrase"},
    # 1079: get across
    {"ipa": "/ɡɛt əˈkrɔːs/", "vi": "truyền tải thành công; qua bên kia", "pos": "phrase"},
    # 1080: god of war
    {"ipa": "/ɡɑːd ʌv wɔːr/", "vi": "chiến thần; vị thần chiến tranh", "pos": "phrase"},
    # 1081: good example
    {"ipa": "/ɡʊd ɪɡˈzæmpəl/", "vi": "tấm gương tốt; khuôn mẫu đáng noi", "pos": "phrase"},
    # 1082: great deal
    {"ipa": "/ɡreɪt diːl/", "vi": "rất nhiều; thỏa thuận hời lớn", "pos": "phrase"},
    # 1083: hard line
    {"ipa": "/hɑːrd laɪn/", "vi": "đường lối cứng rắn; lập trường thép", "pos": "phrase"},
    # 1084: have sex
    {"ipa": "/hæv sɛks/", "vi": "quan hệ tình dục; giao hợp", "pos": "phrase"},
    # 1085: life form
    {"ipa": "/laɪf fɔːrm/", "vi": "dạng sống sinh học; loài sinh vật", "pos": "phrase"},
    # 1086: move around
    {"ipa": "/muːv əˈraʊnd/", "vi": "đi lại loanh quanh; chuyển vị trí", "pos": "phrase"},
    # 1087: point of order
    {"ipa": "/pɔɪnt ʌv ˈɔːrdər/", "vi": "vấn đề thủ tục quy chế phiên họp", "pos": "phrase"},
    # 1088: public law
    {"ipa": "/ˈpʌblɪk lɔː/", "vi": "ngành luật công", "pos": "phrase"},
    # 1089: put to death
    {"ipa": "/pʊt tuː dɛθ/", "vi": "xử tử hình; tước đoạt sinh mạng", "pos": "phrase"},
    # 1090: small white
    {"ipa": "/smɔːl waɪt/", "vi": "loài bướm trắng nhỏ", "pos": "phrase"},
    # 1091: take fire
    {"ipa": "/teɪk ˈfaɪər/", "vi": "bắt lửa cháy; phấn khích hào hứng", "pos": "phrase"},
    # 1092: take form
    {"ipa": "/teɪk fɔːrm/", "vi": "thành hình; định hình rõ nét", "pos": "phrase"},
    # 1093: take heart
    {"ipa": "/teɪk hɑːrt/", "vi": "vững dạ can đảm; lấy lại niềm tin", "pos": "phrase"},
    # 1094: take to heart
    {"ipa": "/teɪk tuː hɑːrt/", "vi": "khắc cốt ghi tâm; quá bận lòng", "pos": "phrase"},
    # 1095: turn down
    {"ipa": "/tɜːrn daʊn/", "vi": "từ chối bác bỏ; vặn nhỏ âm lượng", "pos": "phrase"},
    # 1096: war god
    {"ipa": "/wɔːr ɡɑːd/", "vi": "thần chiến tranh; tướng dũng mãnh", "pos": "phrase"},
    # 1097: white water
    {"ipa": "/waɪt ˈwɔːtər/", "vi": "dòng nước ghềnh cuộn bọt trắng xóa", "pos": "phrase"},
    # 1098: stiller
    {"ipa": "/ˈstɪlər/", "vi": "yên tĩnh hơn; bất động hơn", "pos": "adj"},
    # 1099: stillest
    {"ipa": "/ˈstɪlɪst/", "vi": "yên tĩnh nhất; tĩnh lặng nhất", "pos": "adj"},
]

with open('scratch/b21_r03_raw_p1.json') as f:
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

with open('scratch/b21_r03_p1.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r03_p1.json created successfully and validated!")
