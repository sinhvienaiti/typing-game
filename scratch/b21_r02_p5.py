import json

# Manual word-by-word cognitive review for Batch 21 Round 2 Part 5 (records 900-999, IDs 200k.000902 to 200k.001001)
reviewed_entries = [
    # 900: end run
    {"ipa": "/ɛnd rʌn/", "vi": "pha bọc sườn; thủ đoạn né tránh", "pos": "phrase"},
    # 901: fire up
    {"ipa": "/ˈfaɪər ʌp/", "vi": "khởi động động cơ; khơi dậy lửa", "pos": "phrase"},
    # 902: game law
    {"ipa": "/ɡeɪm lɔː/", "vi": "luật săn bắn thú hoang", "pos": "phrase"},
    # 903: great white way
    {"ipa": "/ɡreɪt waɪt weɪ/", "vi": "khu kịch nghệ Broadway New York", "pos": "phrase"},
    # 904: law school
    {"ipa": "/lɔː skuːl/", "vi": "trường đào tạo luật; khoa luật", "pos": "phrase"},
    # 905: level best
    {"ipa": "/ˈlɛvəl bɛst/", "vi": "hết sức bình sinh; nỗ lực tối đa", "pos": "phrase"},
    # 906: life history
    {"ipa": "/laɪf ˈhɪstəri/", "vi": "tiểu sử; chu trình phát triển sống", "pos": "phrase"},
    # 907: like fun
    {"ipa": "/laɪk fʌn/", "vi": "không đời nào; ngược đời", "pos": "phrase"},
    # 908: living will
    {"ipa": "/ˈlɪvɪŋ wɪl/", "vi": "di chúc sinh mệnh khi còn sống", "pos": "phrase"},
    # 909: long ago
    {"ipa": "/lɔːŋ əˈɡoʊ/", "vi": "từ rất lâu; cách đây đã lâu", "pos": "phrase"},
    # 910: move back
    {"ipa": "/muːv bæk/", "vi": "lùi lại; chuyển về chỗ cũ", "pos": "phrase"},
    # 911: new deal
    {"ipa": "/nuː diːl/", "vi": "Chính sách kinh tế mới New Deal", "pos": "phrase"},
    # 912: second power
    {"ipa": "/ˈsɛkənd ˈpaʊər/", "vi": "lũy thừa bậc hai; bình phương", "pos": "phrase"},
    # 913: stop number
    {"ipa": "/stɑːp ˈnʌmbər/", "vi": "chỉ số khẩu độ ống kính máy ảnh", "pos": "phrase"},
    # 914: true to life
    {"ipa": "/truː tuː laɪf/", "vi": "chân thực; sống động như thật", "pos": "phrase"},
    # 915: war game
    {"ipa": "/wɔːr ɡeɪm/", "vi": "trò diễn tập chiến thuật quân sự", "pos": "phrase"},
    # 916: watch over
    {"ipa": "/wɑːtʃ ˈoʊvər/", "vi": "trông coi; canh chừng; bảo bọc", "pos": "phrase"},
    # 917: act out
    {"ipa": "/ækt aʊt/", "vi": "đóng kịch diễn xuất; quậy phá", "pos": "phrase"},
    # 918: at the ready
    {"ipa": "/æt ðə ˈrɛdi/", "vi": "ở tư thế sẵn sàng chiến đấu", "pos": "phrase"},
    # 919: back saw
    {"ipa": "/bæk sɔː/", "vi": "cưa lưng sắt mộc", "pos": "phrase"},
    # 920: bring in
    {"ipa": "/brɪŋ ɪn/", "vi": "mang về; đưa lại thu nhập; mời vào", "pos": "phrase"},
    # 921: bring on
    {"ipa": "/brɪŋ ɑːn/", "vi": "dẫn đến; gây phát sinh hậu quả", "pos": "phrase"},
    # 922: buy into
    {"ipa": "/baɪ ˈɪntuː/", "vi": "mua cổ phần; tin theo quan điểm", "pos": "phrase"},
    # 923: call number
    {"ipa": "/kɔːl ˈnʌmbər/", "vi": "mã phân loại xếp giá thư viện", "pos": "phrase"},
    # 924: check up on
    {"ipa": "/tʃɛk ʌp ɑːn/", "vi": "kiểm tra tra cứu; theo dõi sát", "pos": "phrase"},
    # 925: close off
    {"ipa": "/kloʊz ɔːf/", "vi": "phong tỏa; rào chắn lối đi", "pos": "phrase"},
    # 926: doing business as
    {"ipa": "/ˈduːɪŋ ˈbɪznəs æz/", "vi": "dưới tên thương mại; hoạt động là", "pos": "phrase"},
    # 927: family line
    {"ipa": "/ˈfæməli laɪn/", "vi": "dòng dõi gia tộc; huyết thống", "pos": "phrase"},
    # 928: far left
    {"ipa": "/fɑːr lɛft/", "vi": "phái cực tả; phe tả cực đoan", "pos": "phrase"},
    # 929: first light
    {"ipa": "/fɜːrst laɪt/", "vi": "ánh sáng ban mai; lúc rạng đông", "pos": "phrase"},
    # 930: first world war
    {"ipa": "/fɜːrst wɜːrld wɔːr/", "vi": "Chiến tranh thế giới thứ nhất", "pos": "phrase"},
    # 931: for example
    {"ipa": "/fɔːr ɪɡˈzæmpəl/", "vi": "ví dụ như; chẳng hạn là", "pos": "phrase"},
    # 932: good deal
    {"ipa": "/ɡʊd diːl/", "vi": "món hời; số lượng tương đối lớn", "pos": "phrase"},
    # 933: good morning
    {"ipa": "/ɡʊd ˈmɔːrnɪŋ/", "vi": "chào buổi sáng", "pos": "phrase"},
    # 934: good turn
    {"ipa": "/ɡʊd tɜːrn/", "vi": "việc làm tốt; ân huệ giúp đỡ", "pos": "phrase"},
    # 935: home court
    {"ipa": "/hoʊm kɔːrt/", "vi": "sân nhà; lợi thế địa bàn nhà", "pos": "phrase"},
    # 936: home office
    {"ipa": "/hoʊm ˈɔːfɪs/", "vi": "Bộ Nội vụ Anh; văn phòng tại nhà", "pos": "phrase"},
    # 937: house of war
    {"ipa": "/haʊs ʌv wɔːr/", "vi": "vùng chiến sự phi Hồi giáo", "pos": "phrase"},
    # 938: human right
    {"ipa": "/ˈhjuːmən raɪt/", "vi": "nhân quyền; quyền cơ bản của người", "pos": "phrase"},
    # 939: keep in line
    {"ipa": "/kiːp ɪn laɪn/", "vi": "bắt giữ kỷ luật; kiểm soát chặt", "pos": "phrase"},
    # 940: keep open
    {"ipa": "/kiːp ˈoʊpən/", "vi": "mở cửa tiếp tục; để ngỏ cơ hội", "pos": "phrase"},
    # 941: money order
    {"ipa": "/ˈmʌni ˈɔːrdər/", "vi": "lệnh phiếu bưu điện chuyển tiền", "pos": "phrase"},
    # 942: power company
    {"ipa": "/ˈpaʊər ˈkʌmpəni/", "vi": "công ty điện lực", "pos": "phrase"},
    # 943: power play
    {"ipa": "/ˈpaʊər pleɪ/", "vi": "lối chơi áp đảo; màn phô trương uy", "pos": "phrase"},
    # 944: quite an
    {"ipa": "/kwaɪt æn/", "vi": "quả thật là một; thực sự là", "pos": "phrase"},
    # 945: school of law
    {"ipa": "/skuːl ʌv lɔː/", "vi": "trường đại học luật", "pos": "phrase"},
    # 946: see the light
    {"ipa": "/siː ðə laɪt/", "vi": "hiểu ra chân lý; giác ngộ", "pos": "phrase"},
    # 947: set point
    {"ipa": "/sɛt pɔɪnt/", "vi": "điểm quyết định ván đấu quần vợt", "pos": "phrase"},
    # 948: stay over
    {"ipa": "/steɪ ˈoʊvər/", "vi": "ở lại qua đêm; ngủ lại", "pos": "phrase"},
    # 949: take the air
    {"ipa": "/teɪk ðə ɛr/", "vi": "đi dạo mát; hóng gió trời", "pos": "phrase"},
    # 950: water company
    {"ipa": "/ˈwɔːtər ˈkʌmpəni/", "vi": "công ty cung cấp nước sạch", "pos": "phrase"},
    # 951: better half
    {"ipa": "/ˈbɛtər hæf/", "vi": "nửa kia; người bạn đời; bà xã", "pos": "phrase"},
    # 952: body part
    {"ipa": "/ˈbɑːdi pɑːrt/", "vi": "bộ phận thân thể người", "pos": "phrase"},
    # 953: chance on
    {"ipa": "/tʃæns ɑːn/", "vi": "tình cờ gặp; ngẫu nhiên bắt gặp", "pos": "phrase"},
    # 954: check into
    {"ipa": "/tʃɛk ˈɪntuː/", "vi": "điều tra khảo sát; nhận phòng nghỉ", "pos": "phrase"},
    # 955: city line
    {"ipa": "/ˈsɪti laɪn/", "vi": "địa giới ranh giới thành phố", "pos": "phrase"},
    # 956: close down
    {"ipa": "/kloʊz daʊn/", "vi": "đóng cửa vĩnh viễn; phá sản", "pos": "phrase"},
    # 957: come to hand
    {"ipa": "/kʌm tuː hænd/", "vi": "đến tận tay; nhận được trong tay", "pos": "phrase"},
    # 958: come to mind
    {"ipa": "/kʌm tuː maɪnd/", "vi": "chợt lóe lên trong đầu; nhớ ra", "pos": "phrase"},
    # 959: day watch
    {"ipa": "/deɪ wɑːtʃ/", "vi": "ca trực ban ngày", "pos": "phrase"},
    # 960: far and away
    {"ipa": "/fɑːr ænd əˈweɪ/", "vi": "vượt trội hơn hẳn; không bàn cãi", "pos": "phrase"},
    # 961: get behind
    {"ipa": "/ɡɛt bɪˈhaɪnd/", "vi": "tụt lại phía sau; ủng hộ bảo trợ", "pos": "phrase"},
    # 962: give thanks
    {"ipa": "/ɡɪv θæŋks/", "vi": "dâng lời cảm tạ; tạ ơn Chúa", "pos": "phrase"},
    # 963: good form
    {"ipa": "/ɡʊd fɔːrm/", "vi": "phép lịch thiệp; ứng xử đúng mực", "pos": "phrase"},
    # 964: high court
    {"ipa": "/haɪ kɔːrt/", "vi": "tòa án tối cao cấp cao", "pos": "phrase"},
    # 965: home room
    {"ipa": "/hoʊm ruːm/", "vi": "phòng sinh hoạt lớp chủ nhiệm", "pos": "phrase"},
    # 966: human being
    {"ipa": "/ˈhjuːmən ˈbiːɪŋ/", "vi": "con người; sinh linh nhân loại", "pos": "phrase"},
    # 967: job lot
    {"ipa": "/dʒɑːb lɑːt/", "vi": "lô hàng tạp xả kho; hàng gom chung", "pos": "phrase"},
    # 968: life class
    {"ipa": "/laɪf klæs/", "vi": "lớp vẽ mẫu khỏa thân nghệ thuật", "pos": "phrase"},
    # 969: little hand
    {"ipa": "/ˈlɪtəl hænd/", "vi": "kim giờ ngắn của đồng hồ", "pos": "phrase"},
    # 970: march on
    {"ipa": "/mɑːrtʃ ɑːn/", "vi": "hành quân tiếp; thời gian trôi mau", "pos": "phrase"},
    # 971: old hand
    {"ipa": "/oʊld hænd/", "vi": "tay lão luyện; người dày dạn kinh", "pos": "phrase"},
    # 972: out front
    {"ipa": "/aʊt frʌnt/", "vi": "dẫn đầu cuộc đua; ở phía trước", "pos": "phrase"},
    # 973: point system
    {"ipa": "/pɔɪnt ˈsɪstəm/", "vi": "hệ thống thang điểm đánh giá", "pos": "phrase"},
    # 974: post house
    {"ipa": "/poʊst haʊs/", "vi": "trạm dịch đổi ngựa bưu chính", "pos": "phrase"},
    # 975: put together
    {"ipa": "/pʊt təˈɡɛðər/", "vi": "lắp ráp; ghép lại; tổ chức nên", "pos": "phrase"},
    # 976: run away
    {"ipa": "/rʌn əˈweɪ/", "vi": "bỏ trốn; trốn chạy; lẩn tránh", "pos": "phrase"},
    # 977: see red
    {"ipa": "/siː rɛd/", "vi": "nổi giận đùng đùng; phát cáu", "pos": "phrase"},
    # 978: set to music
    {"ipa": "/sɛt tuː ˈmjuːzɪk/", "vi": "phổ nhạc bài thơ; viết nhạc cho", "pos": "phrase"},
    # 979: state of mind
    {"ipa": "/steɪt ʌv maɪnd/", "vi": "tâm trạng; trạng thái tinh thần", "pos": "phrase"},
    # 980: time plan
    {"ipa": "/taɪm plæn/", "vi": "kế hoạch mua trả góp định kỳ", "pos": "phrase"},
    # 981: turn over
    {"ipa": "/tɜːrn ˈoʊvər/", "vi": "lật ngược lại; chuyển nhượng; nộp", "pos": "phrase"},
    # 982: very light
    {"ipa": "/ˈvɛri laɪt/", "vi": "pháo sáng Very; pháo hiệu báo nguy", "pos": "phrase"},
    # 983: video game
    {"ipa": "/ˈvɪdioʊ ɡeɪm/", "vi": "trò chơi điện tử; game điện tử", "pos": "phrase"},
    # 984: righter
    {"ipa": "/ˈraɪtər/", "vi": "thẳng thắn hơn; đúng đắn hơn", "pos": "adj"},
    # 985: bad person
    {"ipa": "/bæd ˈpɜːrsən/", "vi": "kẻ xấu; người có nhân cách tệ", "pos": "phrase"},
    # 986: best friend
    {"ipa": "/bɛst frɛnd/", "vi": "bạn thân nhất; bạn tri kỷ", "pos": "phrase"},
    # 987: bring about
    {"ipa": "/brɪŋ əˈbaʊt/", "vi": "mang lại; đem đến sự thay đổi", "pos": "phrase"},
    # 988: bring out
    {"ipa": "/brɪŋ aʊt/", "vi": "phát hành; làm nổi bật lên", "pos": "phrase"},
    # 989: bring up
    {"ipa": "/brɪŋ ʌp/", "vi": "nuôi nấng dưỡng dục; nêu ra vấn đề", "pos": "phrase"},
    # 990: buy back
    {"ipa": "/baɪ bæk/", "vi": "mua lại tài sản; chuộc lại", "pos": "phrase"},
    # 991: by chance
    {"ipa": "/baɪ tʃæns/", "vi": "tình cờ ngẫu nhiên; tình cờ gặp", "pos": "phrase"},
    # 992: case in point
    {"ipa": "/keɪs ɪn pɔɪnt/", "vi": "ví dụ điển hình; ví dụ minh họa", "pos": "phrase"},
    # 993: check over
    {"ipa": "/tʃɛk ˈoʊvər/", "vi": "kiểm tra kỹ càng; rà soát lại", "pos": "phrase"},
    # 994: come along
    {"ipa": "/kʌm əˈlɔːŋ/", "vi": "đi cùng; tiến triển tốt; xuất hiện", "pos": "phrase"},
    # 995: court game
    {"ipa": "/kɔːrt ɡeɪm/", "vi": "môn thể thao thi đấu trên sân", "pos": "phrase"},
    # 996: cut in
    {"ipa": "/kʌt ɪn/", "vi": "nói chen ngang; tạt đầu xe", "pos": "phrase"},
    # 997: cut to
    {"ipa": "/kʌt tuː/", "vi": "chuyển cảnh sang; cắt ngang tới", "pos": "phrase"},
    # 998: every so often
    {"ipa": "/ˈɛvri soʊ ˈɔːfən/", "vi": "thỉnh thoảng; chốc chốc lại làm", "pos": "phrase"},
    # 999: four times
    {"ipa": "/fɔːr taɪmz/", "vi": "bốn lần; gấp bốn lần", "pos": "phrase"},
]

with open('scratch/b21_r02_raw_p5.json') as f:
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

with open('scratch/b21_r02_p5.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r02_p5.json created successfully and validated!")
