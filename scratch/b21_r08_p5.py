import json

# Manual word-by-word cognitive review for Batch 21 Round 8 Part 5 (records 3900-3999, IDs 200k.003902 to 200k.004001)
reviewed_entries = [
    # 3900: blue note
    {"ipa": "/bluː noʊt/", "vi": "nốt thăng giáng blues; nốt lam", "pos": "phrase"},
    # 3901: blue wall
    {"ipa": "/bluː wɔːl/", "vi": "bức tường im lặng của cảnh sát", "pos": "phrase"},
    # 3902: build upon
    {"ipa": "/bɪld əˈpɑːn/", "vi": "xây dựng dựa trên; phát triển từ", "pos": "phrase"},
    # 3903: business activity
    {"ipa": "/ˈbɪznəs ækˈtɪvəti/", "vi": "hoạt động sản xuất kinh doanh", "pos": "phrase"},
    # 3904: camp out
    {"ipa": "/kæmp aʊt/", "vi": "cắm trại ngoài trời; ngủ lều ngoài", "pos": "phrase"},
    # 3905: cast about
    {"ipa": "/kæst əˈbaʊt/", "vi": "ráo riết tìm kiếm; lùng kiếm cách", "pos": "phrase"},
    # 3906: cast out
    {"ipa": "/kæst aʊt/", "vi": "trục xuất; xua đuổi; đuổi ra ngoài", "pos": "phrase"},
    # 3907: change of location
    {"ipa": "/tʃeɪndʒ ʌv loʊˈkeɪʃən/", "vi": "sự thay đổi vị trí; chuyển chỗ ở", "pos": "phrase"},
    # 3908: credit hour
    {"ipa": "/ˈkrɛdɪt ˈaʊər/", "vi": "tín chỉ học phần; đơn vị học trình", "pos": "phrase"},
    # 3909: current unit
    {"ipa": "/ˈkɜːrənt ˈjuːnɪt/", "vi": "đơn vị cường độ dòng điện", "pos": "phrase"},
    # 3910: damage control
    {"ipa": "/ˈdæmɪdʒ kənˈtroʊl/", "vi": "kiểm soát thiệt hại; giảm thiểu lỗ", "pos": "phrase"},
    # 3911: dark blue
    {"ipa": "/dɑːrk bluː/", "vi": "màu xanh lam thẫm; màu xanh đậm", "pos": "phrase"},
    # 3912: dead drop
    {"ipa": "/dɛd drɑːp/", "vi": "hộp thư chết giao nhận tin tình báo", "pos": "phrase"},
    # 3913: department of justice
    {"ipa": "/dɪˈpɑːrtmənt ʌv ˈdʒʌstɪs/", "vi": "Bộ Tư pháp Hoa Kỳ", "pos": "phrase"},
    # 3914: double gold
    {"ipa": "/ˈdʌbl ɡoʊld/", "vi": "hoa cúc vạn thọ kép; hoa cúc vàng", "pos": "phrase"},
    # 3915: draw off
    {"ipa": "/drɔː ɔːf/", "vi": "rút bớt chất lỏng; tháo nước ra", "pos": "phrase"},
    # 3916: drop dead
    {"ipa": "/drɑːp dɛd/", "vi": "chết bất đắc kỳ tử; đột tử lăn ra", "pos": "phrase"},
    # 3917: eating away
    {"ipa": "/ˈiːtɪŋ əˈweɪ/", "vi": "sự xói mòn bào mòn dần dần", "pos": "phrase"},
    # 3918: education secretary
    {"ipa": "/ˌɛdʒuˈkeɪʃən ˈsɛkrətɛri/", "vi": "bộ trưởng bộ giáo dục", "pos": "phrase"},
    # 3919: estate for life
    {"ipa": "/ɪˈsteɪt fɔːr laɪf/", "vi": "quyền sở hữu bất động sản trọn đời", "pos": "phrase"},
    # 3920: european union
    {"ipa": "/ˌjʊrəˈpiːən ˈjuːnjən/", "vi": "Liên minh châu Âu; khối EU", "pos": "phrase"},
    # 3921: eye bank
    {"ipa": "/aɪ bæŋk/", "vi": "ngân hàng giác mạc ghép mắt", "pos": "phrase"},
    # 3922: federal district
    {"ipa": "/ˈfɛdərəl ˈdɪstrɪkt/", "vi": "đặc khu liên bang; quận liên bang", "pos": "phrase"},
    # 3923: field gun
    {"ipa": "/fiːld ɡʌn/", "vi": "pháo dã chiến chiến trường", "pos": "phrase"},
    # 3924: fire insurance
    {"ipa": "/faɪər ɪnˈʃʊrəns/", "vi": "bảo hiểm hỏa hoạn cháy nổ", "pos": "phrase"},
    # 3925: fire ship
    {"ipa": "/faɪər ʃɪp/", "vi": "thuyền hỏa công chở thuốc nổ thiêu", "pos": "phrase"},
    # 3926: firm up
    {"ipa": "/fɜːrm ʌp/", "vi": "chốt hạ thỏa thuận; củng cố vững", "pos": "phrase"},
    # 3927: floor plan
    {"ipa": "/flɔːr plæn/", "vi": "sơ đồ mặt bằng kiến trúc tòa nhà", "pos": "phrase"},
    # 3928: food fish
    {"ipa": "/fuːd fɪʃ/", "vi": "cá thương phẩm làm thức ăn", "pos": "phrase"},
    # 3929: forward pass
    {"ipa": "/ˈfɔːrwərd pæs/", "vi": "đường chuyền bóng về phía trước", "pos": "phrase"},
    # 3930: fourth part
    {"ipa": "/fɔːrθ pɑːrt/", "vi": "một phần tư; góc phần tư", "pos": "phrase"},
    # 3931: freedom of thought
    {"ipa": "/ˈfriːdəm ʌv θɔːt/", "vi": "tự do tư tưởng; tự do suy nghĩ", "pos": "phrase"},
    # 3932: french door
    {"ipa": "/frɛntʃ dɔːr/", "vi": "cửa kính kiểu Pháp hai cánh", "pos": "phrase"},
    # 3933: glad hand
    {"ipa": "/ɡlæd hænd/", "vi": "bắt tay niềm nở; nụ cười xã giao", "pos": "phrase"},
    # 3934: government activity
    {"ipa": "/ˈɡʌvərnmənt ækˈtɪvəti/", "vi": "hoạt động của bộ máy chính phủ", "pos": "phrase"},
    # 3935: green card
    {"ipa": "/ɡriːn kɑːrd/", "vi": "thẻ xanh thường trú nhân Mỹ", "pos": "phrase"},
    # 3936: green river
    {"ipa": "/ɡriːn ˈrɪvər/", "vi": "sông Green River tại Bắc Mỹ", "pos": "phrase"},
    # 3937: ground effect
    {"ipa": "/ɡraʊnd ɪˈfɛkt/", "vi": "hiệu ứng mặt đất trong khí động", "pos": "phrase"},
    # 3938: growth rate
    {"ipa": "/ɡroʊθ reɪt/", "vi": "tốc độ tăng trưởng; tỷ lệ gia tăng", "pos": "phrase"},
    # 3939: hard drug
    {"ipa": "/hɑːrd drʌɡ/", "vi": "ma túy liều nặng; chất nghiện mạnh", "pos": "phrase"},
    # 3940: hell on earth
    {"ipa": "/hɛl ɑːn ɜːrθ/", "vi": "địa ngục trần gian; cảnh khốn cùng", "pos": "phrase"},
    # 3941: holy order
    {"ipa": "/ˈhoʊli ˈɔːrdər/", "vi": "thánh chức; chức thánh giáo hội", "pos": "phrase"},
    # 3942: justice department
    {"ipa": "/ˈdʒʌstɪs dɪˈpɑːrtmənt/", "vi": "bộ tư pháp; cơ quan tư pháp", "pos": "phrase"},
    # 3943: legal code
    {"ipa": "/ˈliːɡl koʊd/", "vi": "bộ luật thành văn; luật pháp điển", "pos": "phrase"},
    # 3944: life estate
    {"ipa": "/laɪf ɪˈsteɪt/", "vi": "bất động sản hưởng dụng suốt đời", "pos": "phrase"},
    # 3945: life ring
    {"ipa": "/laɪf rɪŋ/", "vi": "phao cứu sinh tròn; phao cứu đắm", "pos": "phrase"},
    # 3946: line block
    {"ipa": "/laɪn blɑːk/", "vi": "bản in khắc kẽm; bản kẽm in hình", "pos": "phrase"},
    # 3947: local area network
    {"ipa": "/ˈloʊkl ˈɛriə ˈnɛtwɜːrk/", "vi": "mạng máy tính cục bộ; mạng LAN", "pos": "phrase"},
    # 3948: louis the great
    {"ipa": "/ˈluːɪs ðə ɡreɪt/", "vi": "vua Louis Đại đế của nước Pháp", "pos": "phrase"},
    # 3949: love seat
    {"ipa": "/lʌv siːt/", "vi": "ghế bành đôi; ghế sofa tình nhân", "pos": "phrase"},
    # 3950: low sunday
    {"ipa": "/loʊ ˈsʌndeɪ/", "vi": "Chúa nhật sau lễ Phục Sinh", "pos": "phrase"},
    # 3951: man jack
    {"ipa": "/mæn dʒæk/", "vi": "từng người một; không chừa ai cả", "pos": "phrase"},
    # 3952: medical student
    {"ipa": "/ˈmɛdɪkl ˈstuːdnt/", "vi": "sinh viên y khoa; bác sĩ thực tập", "pos": "phrase"},
    # 3953: mental state
    {"ipa": "/ˈmɛntl steɪt/", "vi": "trạng thái tinh thần; tâm lý", "pos": "phrase"},
    # 3954: music hall
    {"ipa": "/ˈmjuːzɪk hɔːl/", "vi": "nhà hát tạp kỹ ca vũ nhạc kịch", "pos": "phrase"},
    # 3955: new edition
    {"ipa": "/nuː ɪˈdɪʃən/", "vi": "ấn bản mới tái bản; bản in mới", "pos": "phrase"},
    # 3956: north africa
    {"ipa": "/nɔːrθ ˈæfrɪkə/", "vi": "khu vực Bắc Phi; vùng đất Bắc Phi", "pos": "phrase"},
    # 3957: open primary
    {"ipa": "/ˈoʊpən ˈpraɪmɛri/", "vi": "bầu cử sơ bộ rộng mở cho cử tri", "pos": "phrase"},
    # 3958: open shop
    {"ipa": "/ˈoʊpən ʃɑːp/", "vi": "xí nghiệp không ép vào công đoàn", "pos": "phrase"},
    # 3959: physical education
    {"ipa": "/ˈfɪzɪkl ˌɛdʒuˈkeɪʃən/", "vi": "môn giáo dục thể chất; môn thể dục", "pos": "phrase"},
    # 3960: picture card
    {"ipa": "/ˈpɪktʃər kɑːrd/", "vi": "quân bài hình người J Q K tây", "pos": "phrase"},
    # 3961: pop music
    {"ipa": "/pɑːp ˈmjuːzɪk/", "vi": "dòng nhạc pop đương đại đại chúng", "pos": "phrase"},
    # 3962: power politics
    {"ipa": "/ˈpaʊər ˈpɑːlətɪks/", "vi": "chính trị cường quyền dùng sức mạnh", "pos": "phrase"},
    # 3963: press association
    {"ipa": "/prɛs əˌsoʊsiˈeɪʃən/", "vi": "hiệp hội thông tấn; hội nhà báo", "pos": "phrase"},
    # 3964: press conference
    {"ipa": "/prɛs ˈkɑːnfərəns/", "vi": "buổi họp báo phóng viên báo đài", "pos": "phrase"},
    # 3965: professional football
    {"ipa": "/prəˈfɛʃənl ˈfʊtbɔːl/", "vi": "bóng đá chuyên nghiệp đỉnh cao", "pos": "phrase"},
    # 3966: progress to
    {"ipa": "/ˈprɑːɡrɛs tuː/", "vi": "tiến tới bước tiếp; phát triển lên", "pos": "phrase"},
    # 3967: proud of
    {"ipa": "/praʊd ʌv/", "vi": "tự hào hãnh diện về ai điều gì", "pos": "phrase"},
    # 3968: public library
    {"ipa": "/ˈpʌblɪk ˈlaɪbrɛri/", "vi": "thư viện công cộng phục vụ bạn đọc", "pos": "phrase"},
    # 3969: pull down
    {"ipa": "/pʊl daʊn/", "vi": "phá dỡ tòa nhà; kéo tụt xuống", "pos": "phrase"},
    # 3970: pull through
    {"ipa": "/pʊl θruː/", "vi": "vượt qua bạo bệnh; qua cơn nguy nan", "pos": "phrase"},
    # 3971: push down
    {"ipa": "/pʊʃ daʊn/", "vi": "ấn xuống thấp; ghìm nén giá xuống", "pos": "phrase"},
    # 3972: push through
    {"ipa": "/pʊʃ θruː/", "vi": "thông qua dự luật; cố sức vượt qua", "pos": "phrase"},
    # 3973: rate of growth
    {"ipa": "/reɪt ʌv ɡroʊθ/", "vi": "tốc độ gia tăng; tỷ lệ tăng trưởng", "pos": "phrase"},
    # 3974: ride away
    {"ipa": "/raɪd əˈweɪ/", "vi": "cưỡi ngựa phi đi; phóng xe đi mất", "pos": "phrase"},
    # 3975: road construction
    {"ipa": "/roʊd kənˈstrʌkʃən/", "vi": "thi công xây dựng đường giao thông", "pos": "phrase"},
    # 3976: russian bank
    {"ipa": "/ˈrʌʃn bæŋk/", "vi": "trò chơi bài lá Russian Bank", "pos": "phrase"},
    # 3977: school bus
    {"ipa": "/skuːl bʌs/", "vi": "xe buýt chuyên đưa đón học sinh", "pos": "phrase"},
    # 3978: sea dog
    {"ipa": "/siː dɔːɡ/", "vi": "lão thủy thủ sương gió; con hải cẩu", "pos": "phrase"},
    # 3979: secret police
    {"ipa": "/ˈsiːkrət pəˈliːs/", "vi": "cảnh sát mật; mật vụ tình báo ngầm", "pos": "phrase"},
    # 3980: secretary of education
    {"ipa": "/ˈsɛkrətɛri ʌv ˌɛdʒuˈkeɪʃən/", "vi": "Bộ trưởng Giáo dục Hoa Kỳ", "pos": "phrase"},
    # 3981: service agency
    {"ipa": "/ˈsɜːrvɪs ˈeɪdʒənsi/", "vi": "cơ quan cung ứng dịch vụ hỗ trợ", "pos": "phrase"},
    # 3982: sexual love
    {"ipa": "/ˈsɛkʃuəl lʌv/", "vi": "tình yêu thể xác; quan hệ xác thịt", "pos": "phrase"},
    # 3983: shut in
    {"ipa": "/ʃʌt ɪn/", "vi": "giam hãm trong phòng; nhốt kín lại", "pos": "phrase"},
    # 3984: sound effect
    {"ipa": "/saʊnd ɪˈfɛkt/", "vi": "hiệu ứng âm thanh kỹ xảo phim ảnh", "pos": "phrase"},
    # 3985: spirit up
    {"ipa": "/ˈspɪrɪt ʌp/", "vi": "cổ vũ tinh thần; làm phấn chấn lên", "pos": "phrase"},
    # 3986: subject field
    {"ipa": "/ˈsʌbdʒɪkt fiːld/", "vi": "lĩnh vực chuyên môn; ngành học vấn", "pos": "phrase"},
    # 3987: take up arms
    {"ipa": "/teɪk ʌp ɑːrmz/", "vi": "cầm vũ khí chiến đấu; nổi dậy đánh", "pos": "phrase"},
    # 3988: to advantage
    {"ipa": "/tuː ədˈvæntɪdʒ/", "vi": "phát huy vẻ đẹp; làm tăng giá trị", "pos": "phrase"},
    # 3989: trial run
    {"ipa": "/ˈtraɪəl rʌn/", "vi": "cuộc chạy thử nghiệm kiểm tra máy", "pos": "phrase"},
    # 3990: us senate
    {"ipa": "/juː ɛs ˈsɛnət/", "vi": "Thượng viện Hoa Kỳ; viện nghị sĩ", "pos": "phrase"},
    # 3991: wearing away
    {"ipa": "/ˈwɛrɪŋ əˈweɪ/", "vi": "sự mài mòn dần dần; sự phong hóa", "pos": "phrase"},
    # 3992: weather side
    {"ipa": "/ˈwɛðər saɪd/", "vi": "phía đón gió của con tàu trên biển", "pos": "phrase"},
    # 3993: western church
    {"ipa": "/ˈwɛstərn tʃɜːrtʃ/", "vi": "Giáo hội Tây phương La Mã", "pos": "phrase"},
    # 3994: white cell
    {"ipa": "/waɪt sɛl/", "vi": "tế bào bạch cầu trong dòng máu", "pos": "phrase"},
    # 3995: wonder child
    {"ipa": "/ˈwʌndər tʃaɪld/", "vi": "đứa trẻ thần đồng; thần đồng nhí", "pos": "phrase"},
    # 3996: work animal
    {"ipa": "/wɜːrk ˈænɪml/", "vi": "động vật kéo cày; thú cày kéo tải", "pos": "phrase"},
    # 3997: working agreement
    {"ipa": "/ˈwɜːrkɪŋ əˈɡriːmənt/", "vi": "thỏa thuận nguyên tắc khi làm việc", "pos": "phrase"},
    # 3998: ablest
    {"ipa": "/ˈeɪblɪst/", "vi": "có tài năng nhất; tháo vát nhất", "pos": "adj"},
    # 3999: locals
    {"ipa": "/ˈloʊklz/", "vi": "người dân bản xứ; quán rượu gần nhà", "pos": "noun"}
]

with open("scratch/b21_r08_raw_p5.json", "r", encoding="utf-8") as f:
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

with open("scratch/b21_r08_p5.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Part 5.")
