import json

raw_items = json.load(open("scratch/b22_r03_raw_p2.json"))

reviews = [
    # 00: round file
    {"pos": "phrase", "ipa": "/raʊnd faɪl/", "vi": "giũa tròn; sọt rác công sở"},
    # 01: scientific fact
    {"pos": "phrase", "ipa": "/ˌsaɪənˈtɪfɪk fækt/", "vi": "sự thật khoa học; chân lý khoa học"},
    # 02: security guard
    {"pos": "phrase", "ipa": "/sɪˈkjʊrəti ɡɑːrd/", "vi": "nhân viên bảo vệ; vệ sĩ an ninh"},
    # 03: seek out
    {"pos": "phrase", "ipa": "/siːk aʊt/", "vi": "tìm kiếm săn đón; chủ động tìm"},
    # 04: seek time
    {"pos": "phrase", "ipa": "/siːk taɪm/", "vi": "thời gian định vị tìm rãnh ổ đĩa"},
    # 05: sense of taste
    {"pos": "phrase", "ipa": "/sɛns əv teɪst/", "vi": "vị giác; khiếu thẩm mỹ tinh tế"},
    # 06: single entry
    {"pos": "phrase", "ipa": "/ˈsɪŋɡl ˈɛntri/", "vi": "phương pháp kế toán ghi đơn"},
    # 07: skin disease
    {"pos": "phrase", "ipa": "/skɪn dɪˈziːz/", "vi": "bệnh da liễu ngoài da"},
    # 08: skin doctor
    {"pos": "phrase", "ipa": "/skɪn ˈdɑːktər/", "vi": "bác sĩ da liễu; chuyên gia da"},
    # 09: snow job
    {"pos": "phrase", "ipa": "/snoʊ dʒɑːb/", "vi": "trò lừa gạt ngọt ngào khéo léo"},
    # 10: snow line
    {"pos": "phrase", "ipa": "/snoʊ laɪn/", "vi": "đường ranh tuyết vĩnh cửu"},
    # 11: spending cut
    {"pos": "phrase", "ipa": "/ˈspɛndɪŋ kʌt/", "vi": "sự cắt giảm chi tiêu ngân sách"},
    # 12: squad car
    {"pos": "phrase", "ipa": "/skwɑːd kɑːr/", "vi": "xe ô tô tuần tra cảnh sát"},
    # 13: stage setting
    {"pos": "phrase", "ipa": "/steɪdʒ ˈsɛtɪŋ/", "vi": "bối cảnh sân khấu biểu diễn"},
    # 14: station agent
    {"pos": "phrase", "ipa": "/ˈsteɪʃn ˈeɪdʒənt/", "vi": "trưởng ga tàu hỏa bến xe"},
    # 15: stone wall
    {"pos": "phrase", "ipa": "/stoʊn wɔːl/", "vi": "bức tường đá; chướng ngại vật cứng"},
    # 16: stop payment
    {"pos": "phrase", "ipa": "/stɑːp ˈpeɪmənt/", "vi": "lệnh đình chỉ thanh toán séc"},
    # 17: stress test
    {"pos": "phrase", "ipa": "/strɛs tɛst/", "vi": "thử nghiệm chịu tải; test ứng suất"},
    # 18: switch on
    {"pos": "phrase", "ipa": "/swɪtʃ ɑːn/", "vi": "bật công tắc điện; khởi động máy"},
    # 19: tea break
    {"pos": "phrase", "ipa": "/tiː breɪk/", "vi": "giờ nghỉ giải lao uống trà ngắn"},
    # 20: time draft
    {"pos": "phrase", "ipa": "/taɪm dræft/", "vi": "hối phiếu kỳ hạn ngân hàng"},
    # 21: trade balance
    {"pos": "phrase", "ipa": "/treɪd ˈbæləns/", "vi": "cán cân thương mại quốc tế"},
    # 22: tree of knowledge
    {"pos": "phrase", "ipa": "/triː əv ˈnɑːlɪdʒ/", "vi": "Cây Tri thức thiện ác"},
    # 23: tv audience
    {"pos": "phrase", "ipa": "/ˌtiːˈviː ˈɔːdiəns/", "vi": "khán giả truyền hình theo dõi"},
    # 24: voting right
    {"pos": "phrase", "ipa": "/ˈvoʊtɪŋ raɪt/", "vi": "quyền bầu cử; quyền bỏ phiếu"},
    # 25: water hole
    {"pos": "phrase", "ipa": "/ˈwɔːtər hoʊl/", "vi": "vũng nước uống động vật; hố nước"},
    # 26: wave off
    {"pos": "phrase", "ipa": "/weɪv ɔːf/", "vi": "vẫy tay xua đi; gạt bỏ cảnh báo"},
    # 27: weather ship
    {"pos": "phrase", "ipa": "/ˈwɛðər ʃɪp/", "vi": "tàu thám sát thời tiết khí tượng"},
    # 28: white fox
    {"pos": "phrase", "ipa": "/waɪt fɑːks/", "vi": "cáo trắng tuyết Bắc Cực"},
    # 29: white leg
    {"pos": "phrase", "ipa": "/waɪt lɛɡ/", "vi": "chứng phù trắng chân sản phụ"},
    # 30: whole milk
    {"pos": "phrase", "ipa": "/hoʊl mɪlk/", "vi": "sữa tươi nguyên kem nguyên chất"},
    # 31: wide screen
    {"pos": "phrase", "ipa": "/waɪd skriːn/", "vi": "màn ảnh rộng điện ảnh"},
    # 32: wild card
    {"pos": "phrase", "ipa": "/waɪld kɑːrd/", "vi": "vé vớt đặc cách; nhân tố bí ẩn"},
    # 33: window box
    {"pos": "phrase", "ipa": "/ˈwɪndoʊ bɑːks/", "vi": "chậu hoa bậu cửa sổ treo ngoài"},
    # 34: winter sweet
    {"pos": "phrase", "ipa": "/ˈwɪntər swiːt/", "vi": "cây hoa hoàng mai mùa đông"},
    # 35: yellow light
    {"pos": "phrase", "ipa": "/ˈjɛloʊ laɪt/", "vi": "tín hiệu đèn vàng giao thông"},
    # 36: americas
    {"pos": "noun", "ipa": "/əˈmɛrɪkəz/", "vi": "châu Mỹ; toàn bộ châu Mỹ"},
    # 37: shots
    {"pos": "noun", "ipa": "/ʃɑːts/", "vi": "các phát súng; những cú sút bóng"},
    # 38: active application
    {"pos": "phrase", "ipa": "/ˈæktɪv ˌæplɪˈkeɪʃn/", "vi": "ứng dụng đang hoạt động trực tiếp"},
    # 39: adult female
    {"pos": "phrase", "ipa": "/əˈdʌlt ˈfiːmeɪl/", "vi": "phụ nữ trưởng thành; con thú cái"},
    # 40: air national guard
    {"pos": "phrase", "ipa": "/ɛr ˈnæʃnəl ɡɑːrd/", "vi": "Không quân Vệ binh Quốc gia Mỹ"},
    # 41: animal nature
    {"pos": "phrase", "ipa": "/ˈænɪml ˈneɪtʃər/", "vi": "thú tính; bản năng động vật"},
    # 42: bank failure
    {"pos": "phrase", "ipa": "/bæŋk ˈfeɪljər/", "vi": "sự sụp đổ phá sản ngân hàng"},
    # 43: bank guard
    {"pos": "phrase", "ipa": "/bæŋk ɡɑːrd/", "vi": "bảo vệ ngân hàng; vệ sĩ nhà băng"},
    # 44: battle royal
    {"pos": "phrase", "ipa": "/ˈbætl ˈrɔɪəl/", "vi": "cuộc hỗn chiến sinh tồn; đại chiến"},
    # 45: bird family
    {"pos": "phrase", "ipa": "/bɜːrd ˈfæməli/", "vi": "họ loài chim sinh học"},
    # 46: bird of night
    {"pos": "phrase", "ipa": "/bɜːrd əv naɪt/", "vi": "chim ăn đêm; loài cú vọ"},
    # 47: boat club
    {"pos": "phrase", "ipa": "/boʊt klʌb/", "vi": "câu lạc bộ đua thuyền ca nô"},
    # 48: bomb out
    {"pos": "phrase", "ipa": "/bɑːm aʊt/", "vi": "mất nhà do bom đạn; thua thảm hại"},
    # 49: bomb up
    {"pos": "phrase", "ipa": "/bɑːm ʌp/", "vi": "nạp bom lên máy bay chiến đấu"},
    # 50: british east africa
    {"pos": "phrase", "ipa": "/ˈbrɪtɪʃ iːst ˈæfrɪkə/", "vi": "Đông Phi thuộc Anh thời thuộc địa"},
    # 51: cat box
    {"pos": "phrase", "ipa": "/kæt bɑːks/", "vi": "khay vệ sinh đi tiểu cho mèo"},
    # 52: character reference
    {"pos": "phrase", "ipa": "/ˈkærəktər ˈrɛfrəns/", "vi": "thư nhận xét phẩm chất đạo đức"},
    # 53: charge account credit
    {"pos": "phrase", "ipa": "/tʃɑːrdʒ əˈkaʊnt ˈkrɛdɪt/", "vi": "tín dụng tài khoản mua trả chậm"},
    # 54: cheap shot
    {"pos": "phrase", "ipa": "/tʃiːp ʃɑːt/", "vi": "đòn chơi xấu hèn hạ; đả kích bẩn"},
    # 55: church festival
    {"pos": "phrase", "ipa": "/tʃɜːrtʃ ˈfɛstəvl/", "vi": "ngày hội lễ nhà thờ giáo xứ"},
    # 56: closed primary
    {"pos": "phrase", "ipa": "/kloʊzd ˈpraɪmɛri/", "vi": "cuộc bầu cử sơ bộ kín nội bộ đảng"},
    # 57: closed shop
    {"pos": "phrase", "ipa": "/kloʊzd ʃɑːp/", "vi": "xưởng chỉ thuê đoàn viên công đoàn"},
    # 58: commercial activity
    {"pos": "phrase", "ipa": "/kəˈmɜːrʃl ækˈtɪvəti/", "vi": "hoạt động thương mại buôn bán"},
    # 59: commercial agency
    {"pos": "phrase", "ipa": "/kəˈmɜːrʃl ˈeɪdʒənsi/", "vi": "cơ quan thông tin xếp hạng tín dụng"},
    # 60: crazy horse
    {"pos": "phrase", "ipa": "/ˈkreɪzi hɔːrs/", "vi": "thủ lĩnh da đỏ Crazy Horse"},
    # 61: crew cut
    {"pos": "phrase", "ipa": "/kruː kʌt/", "vi": "kiểu tóc đầu đinh cua cắt ngắn"},
    # 62: cry for
    {"pos": "phrase", "ipa": "/kraɪ fɔːr/", "vi": "kêu gào đòi hỏi; rất cần khao khát"},
    # 63: cutting off
    {"pos": "phrase", "ipa": "/ˈkʌtɪŋ ɔːf/", "vi": "việc cắt đứt cô lập; đoạn tuyệt"},
    # 64: data communication
    {"pos": "phrase", "ipa": "/ˈdeɪtə kəˌmjuːnɪˈkeɪʃn/", "vi": "truyền thông dữ liệu máy tính"},
    # 65: de forest
    {"pos": "phrase", "ipa": "/də ˈfɔːrɪst/", "vi": "nhà phát minh Lee De Forest"},
    # 66: dead mail
    {"pos": "phrase", "ipa": "/dɛd meɪl/", "vi": "thư vô thừa nhận; thư chết"},
    # 67: digital computer
    {"pos": "phrase", "ipa": "/ˈdɪdʒɪtl kəmˈpjuːtər/", "vi": "máy vi tính kỹ thuật số"},
    # 68: dinner table
    {"pos": "phrase", "ipa": "/ˈdɪnər ˈteɪbl/", "vi": "bàn ăn cơm tối gia đình"},
    # 69: direct primary
    {"pos": "phrase", "ipa": "/dəˈrɛkt ˈpraɪmɛri/", "vi": "bầu cử sơ bộ trực tiếp cử tri"},
    # 70: doctor of laws
    {"pos": "phrase", "ipa": "/ˈdɑːktər əv lɔːz/", "vi": "bằng Tiến sĩ Luật học danh dự LLD"},
    # 71: double negative
    {"pos": "phrase", "ipa": "/ˈdʌbl ˈnɛɡətɪv/", "vi": "phủ định kép trong ngữ pháp câu"},
    # 72: dress code
    {"pos": "phrase", "ipa": "/drɛs koʊd/", "vi": "quy định trang phục chuẩn mực"},
    # 73: duty period
    {"pos": "phrase", "ipa": "/ˈduːti ˈpɪriəd/", "vi": "ca trực làm việc; thời gian làm ca"},
    # 74: easy chair
    {"pos": "phrase", "ipa": "/ˈiːzi tʃɛr/", "vi": "ghế bành tựa êm ái thư giãn"},
    # 75: economic aid
    {"pos": "phrase", "ipa": "/ˌiːkəˈnɑːmɪk eɪd/", "vi": "viện trợ kinh tế phát triển"},
    # 76: face pack
    {"pos": "phrase", "ipa": "/feɪs pæk/", "vi": "mặt nạ dưỡng da mặt làm đẹp"},
    # 77: false name
    {"pos": "phrase", "ipa": "/fɔːls neɪm/", "vi": "tên giả mạo; biệt danh che giấu"},
    # 78: fine arts
    {"pos": "phrase", "ipa": "/faɪn ɑːrts/", "vi": "mỹ thuật; nghệ thuật tạo hình"},
    # 79: fixed cost
    {"pos": "phrase", "ipa": "/fɪkst kɔːst/", "vi": "định phí; chi phí cố định"},
    # 80: for instance
    {"pos": "phrase", "ipa": "/fɔːr ˈɪnstəns/", "vi": "chẳng hạn như; ví dụ như"},
    # 81: get the goods
    {"pos": "phrase", "ipa": "/ɡɛt ðə ɡʊdz/", "vi": "nắm bằng chứng vạch trần tội phạm"},
    # 82: get the hang
    {"pos": "phrase", "ipa": "/ɡɛt ðə hæŋ/", "vi": "nắm được bí quyết; thành thạo"},
    # 83: government revenue
    {"pos": "phrase", "ipa": "/ˈɡʌvərnmənt ˈrɛvənuː/", "vi": "nguồn thu ngân sách nhà nước"},
    # 84: grade point average
    {"pos": "phrase", "ipa": "/ɡreɪd pɔɪnt ˈævrɪdʒ/", "vi": "điểm trung bình tích lũy; GPA"},
    # 85: guide dog
    {"pos": "phrase", "ipa": "/ɡaɪd dɔːɡ/", "vi": "chó dẫn đường người khiếm thị"},
    # 86: hang out
    {"pos": "phrase", "ipa": "/hæŋ aʊt/", "vi": "đi chơi la cà tụ tập bạn bè"},
    # 87: hang up
    {"pos": "phrase", "ipa": "/hæŋ ʌp/", "vi": "gác máy cúp điện thoại; treo đồ lên"},
    # 88: henry james
    {"pos": "phrase", "ipa": "/ˈhɛnri dʒeɪmz/", "vi": "nhà văn Henry James"},
    # 89: hit squad
    {"pos": "phrase", "ipa": "/hɪt skwɑːd/", "vi": "đội sát thủ ám sát thanh trừng"},
    # 90: horse race
    {"pos": "phrase", "ipa": "/hɔːrs reɪs/", "vi": "cuộc đua ngựa; đường đua quyết liệt"},
    # 91: internal control
    {"pos": "phrase", "ipa": "/ɪnˈtɜːrnl kənˈtroʊl/", "vi": "hệ thống kiểm soát nội bộ tổ chức"},
    # 92: international affairs
    {"pos": "phrase", "ipa": "/ˌɪntərˈnæʃnəl əˈfɛrz/", "vi": "các vấn đề bang giao quốc tế"},
    # 93: investment letter
    {"pos": "phrase", "ipa": "/ɪnˈvɛstmənt ˈlɛtər/", "vi": "thư cam kết giữ cổ phiếu dài hạn"},
    # 94: iron blue
    {"pos": "phrase", "ipa": "/ˈaɪərn bluː/", "vi": "sắc xanh sắt Phổ ngả lam"},
    # 95: joint return
    {"pos": "phrase", "ipa": "/dʒɔɪnt rɪˈtɜːrn/", "vi": "tờ khai thuế chung của vợ chồng"},
    # 96: kingdom come
    {"pos": "phrase", "ipa": "/ˈkɪŋdəm kʌm/", "vi": "thế giới bên kia cõi vĩnh hằng"},
    # 97: little giant
    {"pos": "phrase", "ipa": "/ˈlɪtl ˈdʒaɪənt/", "vi": "chính khách Stephen Douglas"},
    # 98: long wave
    {"pos": "phrase", "ipa": "/lɔːŋ weɪv/", "vi": "sóng vô tuyến dài viễn thông"},
    # 99: lying in wait
    {"pos": "phrase", "ipa": "/ˈlaɪɪŋ ɪn weɪt/", "vi": "sự phục kích mai phục con mồi"}
]

for r in reviews:
    r["ipa"] = r["ipa"].strip()

assert len(reviews) == 100
assert len(raw_items) == 100

out_items = []
for i in range(100):
    item = dict(raw_items[i])
    rev = reviews[i]
    item["pos"] = rev["pos"]
    item["ipa"] = rev["ipa"]
    item["vi"] = rev["vi"]
    item["status"] = "reviewed"
    
    assert len(item["vi"]) <= 35, f"vi too long at {i}: {item['vi']}"
    assert len(item["vi"]) > 0
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2
    out_items.append(item)

json.dump(out_items, open("scratch/b22_r03_p2.json", "w"), ensure_ascii=False, indent=2)
print("Round 3 Part 2 reviewed successfully: 100 items saved to scratch/b22_r03_p2.json")
