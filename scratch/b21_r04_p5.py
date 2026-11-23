import json

# Manual word-by-word cognitive review for Batch 21 Round 4 Part 5 (records 1900-1999, IDs 200k.001902 to 200k.002001)
reviewed_entries = [
    # 1900: land line
    {"ipa": "/lænd laɪn/", "vi": "đường dây điện thoại bàn cố định", "pos": "phrase"},
    # 1901: left bank
    {"ipa": "/lɛft bæŋk/", "vi": "Tả ngạn sông Seine; bờ sông trái", "pos": "phrase"},
    # 1902: legal right
    {"ipa": "/ˈliːɡəl raɪt/", "vi": "quyền lợi hợp pháp; quyền pháp định", "pos": "phrase"},
    # 1903: let alone
    {"ipa": "/lɛt əˈloʊn/", "vi": "huống hồ là; chưa nói tới", "pos": "phrase"},
    # 1904: local road
    {"ipa": "/ˈloʊkəl roʊd/", "vi": "đường nội bộ; đường dân sinh xã", "pos": "phrase"},
    # 1905: main course
    {"ipa": "/meɪn kɔːrs/", "vi": "món ăn chính trong bữa tiệc", "pos": "phrase"},
    # 1906: mark out
    {"ipa": "/mɑːrk aʊt/", "vi": "phân định ranh giới; định đoạt số", "pos": "phrase"},
    # 1907: mark up
    {"ipa": "/mɑːrk ʌp/", "vi": "tăng giá bán; đánh dấu chỉnh sửa", "pos": "phrase"},
    # 1908: match game
    {"ipa": "/mætʃ ɡeɪm/", "vi": "trận đấu tranh ngôi vô địch", "pos": "phrase"},
    # 1909: military music
    {"ipa": "/ˈmɪlətɛri ˈmjuːzɪk/", "vi": "quân nhạc; nhạc quân hành", "pos": "phrase"},
    # 1910: natural state
    {"ipa": "/ˈnætʃərəl steɪt/", "vi": "trạng thái tự nhiên nguyên sơ", "pos": "phrase"},
    # 1911: offer up
    {"ipa": "/ˈɔːfər ʌp/", "vi": "dâng lên hiến tế; dâng lời nguyện", "pos": "phrase"},
    # 1912: one percent
    {"ipa": "/wʌn pərˈsɛnt/", "vi": "tỷ lệ một phần trăm; giới siêu giàu", "pos": "phrase"},
    # 1913: open account
    {"ipa": "/ˈoʊpən əˈkaʊnt/", "vi": "tài khoản tín dụng mở ghi nợ", "pos": "phrase"},
    # 1914: pass out
    {"ipa": "/pæs aʊt/", "vi": "ngất xỉu bất tỉnh; phân phát giấy", "pos": "phrase"},
    # 1915: pass up
    {"ipa": "/pæs ʌp/", "vi": "bỏ lỡ cơ hội; khước từ lời mời", "pos": "phrase"},
    # 1916: person hour
    {"ipa": "/ˈpɜːrsən ˈaʊər/", "vi": "giờ công lao động của một người", "pos": "phrase"},
    # 1917: point of view
    {"ipa": "/pɔɪnt ʌv vjuː/", "vi": "góc nhìn; quan điểm cá nhân", "pos": "phrase"},
    # 1918: post road
    {"ipa": "/poʊst roʊd/", "vi": "tuyến đường chuyển thư bưu chính", "pos": "phrase"},
    # 1919: power couple
    {"ipa": "/ˈpaʊər ˈkʌpəl/", "vi": "cặp đôi quyền lực giàu sang", "pos": "phrase"},
    # 1920: present times
    {"ipa": "/ˈprɛzənt taɪmz/", "vi": "thời buổi hiện đại; thời nay", "pos": "phrase"},
    # 1921: price war
    {"ipa": "/praɪs wɔːr/", "vi": "cuộc chiến giảm giá cạnh tranh", "pos": "phrase"},
    # 1922: property man
    {"ipa": "/ˈprɑːpərti mæn/", "vi": "người quản lý đạo cụ sân khấu kịch", "pos": "phrase"},
    # 1923: red light
    {"ipa": "/rɛd laɪt/", "vi": "đèn giao thông đỏ; cảnh báo dừng", "pos": "phrase"},
    # 1924: rest area
    {"ipa": "/rɛst ˈɛriə/", "vi": "trạm dừng chân nghỉ ngơi cao tốc", "pos": "phrase"},
    # 1925: right of election
    {"ipa": "/raɪt ʌv ɪˈlɛkʃən/", "vi": "quyền chọn hưởng di sản hôn phối", "pos": "phrase"},
    # 1926: send around
    {"ipa": "/sɛnd əˈraʊnd/", "vi": "gửi luân chuyển tài liệu vòng quanh", "pos": "phrase"},
    # 1927: sleep out
    {"ipa": "/sliːp aʊt/", "vi": "làm giúp việc nhưng không ngủ lại", "pos": "phrase"},
    # 1928: social action
    {"ipa": "/ˈsoʊʃəl ˈækʃən/", "vi": "hành động phong trào xã hội", "pos": "phrase"},
    # 1929: social process
    {"ipa": "/ˈsoʊʃəl ˈprɑːsɛs/", "vi": "tiến trình tương tác xã hội", "pos": "phrase"},
    # 1930: south by west
    {"ipa": "/saʊθ baɪ wɛst/", "vi": "hướng nam chếch tây một góc nhỏ", "pos": "phrase"},
    # 1931: speak for
    {"ipa": "/spiːk fɔːr/", "vi": "đại diện phát biểu; nói thay lời", "pos": "phrase"},
    # 1932: stop dead
    {"ipa": "/stɑːp dɛd/", "vi": "đứng khựng lại; phanh kít dừng hẳn", "pos": "phrase"},
    # 1933: street girl
    {"ipa": "/striːt ɡɜːrl/", "vi": "gái đứng đường; gái bán hoa", "pos": "phrase"},
    # 1934: test case
    {"ipa": "/tɛst keɪs/", "vi": "vụ án điểm lập án lệ; ca thử nghiệm", "pos": "phrase"},
    # 1935: voice over
    {"ipa": "/vɔɪs ˈoʊvər/", "vi": "giọng đọc thuyết minh lồng tiếng", "pos": "phrase"},
    # 1936: war department
    {"ipa": "/wɔːr dɪˈpɑːrtmənt/", "vi": "Bộ Chiến tranh thời xưa", "pos": "phrase"},
    # 1937: west by south
    {"ipa": "/wɛst baɪ saʊθ/", "vi": "hướng tây chếch nam một góc nhỏ", "pos": "phrase"},
    # 1938: white lead
    {"ipa": "/waɪt lɛd/", "vi": "chì trắng; bột màu trắng kiềm tính", "pos": "phrase"},
    # 1939: whole rest
    {"ipa": "/hoʊl rɛst/", "vi": "dấu lặng tròn trong bản nhạc", "pos": "phrase"},
    # 1940: write in
    {"ipa": "/raɪt ɪn/", "vi": "viết thư gửi về; ghi thêm tên bầu", "pos": "phrase"},
    # 1941: write of
    {"ipa": "/raɪt ʌv/", "vi": "viết bài văn kể về sự việc", "pos": "phrase"},
    # 1942: write on
    {"ipa": "/raɪt ɑːn/", "vi": "viết tiểu luận nghiên cứu về", "pos": "phrase"},
    # 1943: gives
    {"ipa": "/ɡɪvz/", "vi": "độ co giãn; những điểm nhún nhường", "pos": "noun"},
    # 1944: age of reason
    {"ipa": "/eɪdʒ ʌv ˈriːzən/", "vi": "Thời đại Ánh sáng Khai minh", "pos": "phrase"},
    # 1945: air current
    {"ipa": "/ɛr ˈkɜːrənt/", "vi": "luồng không khí; dòng khí đối lưu", "pos": "phrase"},
    # 1946: art class
    {"ipa": "/ɑːrt klæs/", "vi": "lớp học vẽ mỹ thuật", "pos": "phrase"},
    # 1947: ball up
    {"ipa": "/bɔːl ʌp/", "vi": "cuộn tròn lại; làm rối tung việc", "pos": "phrase"},
    # 1948: big blue
    {"ipa": "/bɪɡ bluː/", "vi": "biệt danh tập đoàn IBM; bom BLU-82", "pos": "phrase"},
    # 1949: big league
    {"ipa": "/bɪɡ liːɡ/", "vi": "giải thể thao nhà nghề hạng nhất", "pos": "phrase"},
    # 1950: box up
    {"ipa": "/bɑːks ʌp/", "vi": "đóng gói vào thùng; nhốt chặt", "pos": "phrase"},
    # 1951: break water
    {"ipa": "/breɪk ˈwɔːtər/", "vi": "trồi lên mặt nước; vỡ ối lúc sinh", "pos": "phrase"},
    # 1952: build up
    {"ipa": "/bɪld ʌp/", "vi": "xây dựng phát triển; tích tụ dần", "pos": "phrase"},
    # 1953: call center
    {"ipa": "/kɔːl ˈsɛntər/", "vi": "tổng đài chăm sóc khách hàng", "pos": "phrase"},
    # 1954: class list
    {"ipa": "/klæs lɪst/", "vi": "bảng vàng danh sách tốt nghiệp", "pos": "phrase"},
    # 1955: college girl
    {"ipa": "/ˈkɑːlɪdʒ ɡɜːrl/", "vi": "nữ sinh viên trường đại học", "pos": "phrase"},
    # 1956: country club
    {"ipa": "/ˈkʌntri klʌb/", "vi": "câu lạc bộ thể thao ngoại ô", "pos": "phrase"},
    # 1957: day bed
    {"ipa": "/deɪ bɛd/", "vi": "giường kiêm ghế tựa ban ngày", "pos": "phrase"},
    # 1958: due west
    {"ipa": "/djuː wɛst/", "vi": "hướng thẳng chính tây", "pos": "phrase"},
    # 1959: field hand
    {"ipa": "/fiːld hænd/", "vi": "nông dân làm công đồng áng", "pos": "phrase"},
    # 1960: go to bed
    {"ipa": "/ɡoʊ tuː bɛd/", "vi": "đi lên giường ngủ", "pos": "phrase"},
    # 1961: high quality
    {"ipa": "/haɪ ˈkwɑːləti/", "vi": "chất lượng cao hảo hạng", "pos": "phrase"},
    # 1962: high style
    {"ipa": "/haɪ staɪl/", "vi": "phong cách thời trang đẳng cấp cao", "pos": "phrase"},
    # 1963: hit list
    {"ipa": "/hɪt lɪst/", "vi": "danh sách đen trừng phạt sát hại", "pos": "phrase"},
    # 1964: in effect
    {"ipa": "/ɪn ɪˈfɛkt/", "vi": "có hiệu lực thi hành; thực chất là", "pos": "phrase"},
    # 1965: in store
    {"ipa": "/ɪn stɔːr/", "vi": "sắp sửa xảy đến; đang chờ đón phía", "pos": "phrase"},
    # 1966: in two ways
    {"ipa": "/ɪn tuː weɪz/", "vi": "theo hai cách thức khác nhau", "pos": "phrase"},
    # 1967: inside job
    {"ipa": "/ˈɪnˌsaɪd dʒɑːb/", "vi": "vụ trộm do người nội bộ cấu kết", "pos": "phrase"},
    # 1968: keep step
    {"ipa": "/kiːp stɛp/", "vi": "bước đều nhịp bước; theo kịp nhịp", "pos": "phrase"},
    # 1969: land area
    {"ipa": "/lænd ˈɛriə/", "vi": "diện tích đất đai khu vực", "pos": "phrase"},
    # 1970: lead line
    {"ipa": "/lɛd laɪn/", "vi": "dây dọi chì đo độ sâu đáy biển", "pos": "phrase"},
    # 1971: little brother
    {"ipa": "/ˈlɪtəl ˈbrʌðər/", "vi": "em trai bé nhỏ", "pos": "phrase"},
    # 1972: local department
    {"ipa": "/ˈloʊkəl dɪˈpɑːrtmənt/", "vi": "sở ban ngành chính quyền địa phương", "pos": "phrase"},
    # 1973: military service
    {"ipa": "/ˈmɪlətɛri ˈsɜːrvɪs/", "vi": "nghĩa vụ quân sự; binh nghiệp", "pos": "phrase"},
    # 1974: moving in
    {"ipa": "/ˈmuːvɪŋ ɪn/", "vi": "việc dọn đồ đạc vào nhà mới", "pos": "phrase"},
    # 1975: no ball
    {"ipa": "/noʊ bɔːl/", "vi": "cú ném bóng phạm quy bóng gậy", "pos": "phrase"},
    # 1976: old style
    {"ipa": "/oʊld staɪl/", "vi": "phong cách kiểu cổ; lịch cũ Julius", "pos": "phrase"},
    # 1977: pick off
    {"ipa": "/pɪk ɔːf/", "vi": "bắn tỉa từng tên một; bắt bài loại", "pos": "phrase"},
    # 1978: picture show
    {"ipa": "/ˈpɪktʃər ʃoʊ/", "vi": "buổi chiếu phim rạp; rạp xi-nê", "pos": "phrase"},
    # 1979: policy change
    {"ipa": "/ˈpɑːləsi tʃeɪndʒ/", "vi": "sự thay đổi chủ trương chính sách", "pos": "phrase"},
    # 1980: public press
    {"ipa": "/ˈpʌblɪk prɛs/", "vi": "báo chí công luận đại chúng", "pos": "phrase"},
    # 1981: second reading
    {"ipa": "/ˈsɛkənd ˈriːdɪŋ/", "vi": "phiên đọc dự luật lần thứ hai", "pos": "phrase"},
    # 1982: security service
    {"ipa": "/sɪˈkjʊrəti ˈsɜːrvɪs/", "vi": "cơ quan an ninh tình báo nội địa", "pos": "phrase"},
    # 1983: service club
    {"ipa": "/ˈsɜːrvɪs klʌb/", "vi": "câu lạc bộ hoạt động thiện nguyện", "pos": "phrase"},
    # 1984: side view
    {"ipa": "/saɪd vjuː/", "vi": "góc nhìn nghiêng; hình chiếu cạnh", "pos": "phrase"},
    # 1985: sign off
    {"ipa": "/saɪn ɔːf/", "vi": "kết thúc buổi phát sóng; phê chuẩn", "pos": "phrase"},
    # 1986: special act
    {"ipa": "/ˈspɛʃəl ækt/", "vi": "đạo luật đặc biệt áp dụng riêng", "pos": "phrase"},
    # 1987: staff of life
    {"ipa": "/stæf ʌv laɪf/", "vi": "lương thực thiết yếu; bánh mì", "pos": "phrase"},
    # 1988: straight up
    {"ipa": "/streɪt ʌp/", "vi": "rượu không pha đá; thật lòng", "pos": "phrase"},
    # 1989: time note
    {"ipa": "/taɪm noʊt/", "vi": "kỳ phiếu vay tiền có kỳ hạn", "pos": "phrase"},
    # 1990: trade school
    {"ipa": "/treɪd skuːl/", "vi": "trường dạy nghề thực hành", "pos": "phrase"},
    # 1991: us army
    {"ipa": "/juː ɛs ˈɑːrmi/", "vi": "Lục quân Hoa Kỳ; quân đội Mỹ", "pos": "phrase"},
    # 1992: walk of life
    {"ipa": "/wɔːk ʌv laɪf/", "vi": "tầng lớp xuất thân trong xã hội", "pos": "phrase"},
    # 1993: walk off
    {"ipa": "/wɔːk ɔːf/", "vi": "bỏ đi trong bực bội; ẵm giải thưởng", "pos": "phrase"},
    # 1994: wall up
    {"ipa": "/wɔːl ʌp/", "vi": "bịt kín bằng tường gạch xây", "pos": "phrase"},
    # 1995: watch fire
    {"ipa": "/wɑːtʃ ˈfaɪər/", "vi": "đống lửa trạm gác canh đêm", "pos": "phrase"},
    # 1996: world council
    {"ipa": "/wɜːrld ˈkaʊnsəl/", "vi": "hội đồng giáo hội thế giới", "pos": "phrase"},
    # 1997: allow in
    {"ipa": "/əˈlaʊ ɪn/", "vi": "cho phép bước vào trong", "pos": "phrase"},
    # 1998: american english
    {"ipa": "/əˈmɛrɪkən ˈɪŋɡlɪʃ/", "vi": "tiếng Anh-Mỹ; ngữ hệ Anh-Mỹ", "pos": "phrase"},
    # 1999: amount of money
    {"ipa": "/əˈmaʊnt ʌv ˈmʌni/", "vi": "khoản tiền lớn; lượng tiền tệ", "pos": "phrase"},
]

with open('scratch/b21_r04_raw_p5.json') as f:
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

with open('scratch/b21_r04_p5.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r04_p5.json created successfully and validated!")
