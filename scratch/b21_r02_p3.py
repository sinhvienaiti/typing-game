import json

# Manual word-by-word cognitive review for Batch 21 Round 2 Part 3 (records 700-799, IDs 200k.000702 to 200k.000801)
reviewed_entries = [
    # 700: keep away
    {"ipa": "/kiːp əˈweɪ/", "vi": "tránh xa; giữ khoảng cách; lánh đi", "pos": "phrase"},
    # 701: life line
    {"ipa": "/ˈlaɪf laɪn/", "vi": "đường sinh mệnh; phao cứu sinh", "pos": "phrase"},
    # 702: line of life
    {"ipa": "/laɪn ʌv laɪf/", "vi": "đường sinh mệnh; đường sinh đạo", "pos": "phrase"},
    # 703: move in
    {"ipa": "/muːv ɪn/", "vi": "dọn đến ở; chuyển vào sống chung", "pos": "phrase"},
    # 704: move on
    {"ipa": "/muːv ɑːn/", "vi": "bước tiếp; tiến lên; đi tiếp", "pos": "phrase"},
    # 705: no matter
    {"ipa": "/noʊ ˈmætər/", "vi": "bất kể; dù sao đi nữa", "pos": "phrase"},
    # 706: of late
    {"ipa": "/ʌv leɪt/", "vi": "gần đây; dạo gần đây", "pos": "phrase"},
    # 707: old person
    {"ipa": "/oʊld ˈpɜːrsən/", "vi": "người già; người cao tuổi", "pos": "phrase"},
    # 708: old times
    {"ipa": "/oʊld taɪmz/", "vi": "thời xưa; ngày xưa; kỷ niệm cũ", "pos": "phrase"},
    # 709: pretty up
    {"ipa": "/ˈprɪti ʌp/", "vi": "làm đẹp; chải chuốt; trang điểm", "pos": "phrase"},
    # 710: put away
    {"ipa": "/pʊt əˈweɪ/", "vi": "cất đi; dọn dẹp; dành dụm", "pos": "phrase"},
    # 711: run down
    {"ipa": "/rʌn daʊn/", "vi": "tông phải; chỉ trích; cạn kiệt", "pos": "phrase"},
    # 712: run through
    {"ipa": "/rʌn θruː/", "vi": "tiêu sạch; duyệt qua; chảy xiết", "pos": "phrase"},
    # 713: school of thought
    {"ipa": "/skuːl ʌv θɔːt/", "vi": "trường phái tư tưởng; học thuyết", "pos": "phrase"},
    # 714: state change
    {"ipa": "/steɪt tʃeɪndʒ/", "vi": "sự chuyển trạng thái; biến đổi pha", "pos": "phrase"},
    # 715: talk into
    {"ipa": "/tɔːk ˈɪntuː/", "vi": "thuyết phục; dụ dỗ làm gì", "pos": "phrase"},
    # 716: three year old
    {"ipa": "/θriː jɪr oʊld/", "vi": "lên ba; trẻ ba tuổi; ngựa ba tuổi", "pos": "phrase"},
    # 717: wait on
    {"ipa": "/weɪt ɑːn/", "vi": "hầu bàn; phục vụ; chăm sóc", "pos": "phrase"},
    # 718: white man
    {"ipa": "/waɪt mæn/", "vi": "người da trắng; nam giới da trắng", "pos": "phrase"},
    # 719: air out
    {"ipa": "/ɛr aʊt/", "vi": "cho thoáng khí; phơi gió sổ lồng", "pos": "phrase"},
    # 720: ask for
    {"ipa": "/æsk fɔːr/", "vi": "xin; yêu cầu; tự chuốc lấy", "pos": "phrase"},
    # 721: ask in
    {"ipa": "/æsk ɪn/", "vi": "mời vào nhà; mời vào trong", "pos": "phrase"},
    # 722: back talk
    {"ipa": "/bæk tɔːk/", "vi": "sự cãi lại; lời hỗn xược", "pos": "phrase"},
    # 723: be due
    {"ipa": "/biː djuː/", "vi": "đến hạn; sắp xảy ra; xứng đáng", "pos": "phrase"},
    # 724: business school
    {"ipa": "/ˈbɪznəs skuːl/", "vi": "trường kinh doanh; viện quản trị", "pos": "phrase"},
    # 725: face off
    {"ipa": "/feɪs ɔːf/", "vi": "đối đầu; phát bóng khúc côn cầu", "pos": "phrase"},
    # 726: family name
    {"ipa": "/ˈfæməli neɪm/", "vi": "họ; tên dòng họ", "pos": "phrase"},
    # 727: first half
    {"ipa": "/fɜːrst hæf/", "vi": "hiệp một; nửa đầu tiên", "pos": "phrase"},
    # 728: get along
    {"ipa": "/ɡɛt əˈlɔːŋ/", "vi": "hòa thuận; sống hòa hợp; xoay xở", "pos": "phrase"},
    # 729: give care
    {"ipa": "/ɡɪv kɛr/", "vi": "chăm sóc; quan tâm; trông nom", "pos": "phrase"},
    # 730: hand over
    {"ipa": "/hænd ˈoʊvər/", "vi": "bàn giao; giao nộp; trao quyền", "pos": "phrase"},
    # 731: head home
    {"ipa": "/hɛd hoʊm/", "vi": "đi về nhà; hướng về nhà", "pos": "phrase"},
    # 732: high point
    {"ipa": "/haɪ pɔɪnt/", "vi": "đỉnh điểm; điểm nhấn đáng nhớ", "pos": "phrase"},
    # 733: house of god
    {"ipa": "/haʊs ʌv ɡɑːd/", "vi": "nhà chúa; nơi thờ tự; giáo đường", "pos": "phrase"},
    # 734: keep company
    {"ipa": "/kiːp ˈkʌmpəni/", "vi": "làm bạn; đi cùng; bầu bạn", "pos": "phrase"},
    # 735: move in on
    {"ipa": "/muːv ɪn ɑːn/", "vi": "tiếp cận mục tiêu; vây bắt", "pos": "phrase"},
    # 736: part music
    {"ipa": "/pɑːrt ˈmjuːzɪk/", "vi": "nhạc nhiều bè; thanh nhạc phức điệu", "pos": "phrase"},
    # 737: per year
    {"ipa": "/pɜːr jɪr/", "vi": "mỗi năm; tính theo từng năm", "pos": "phrase"},
    # 738: public house
    {"ipa": "/ˈpʌblɪk haʊs/", "vi": "quán rượu; quán pub", "pos": "phrase"},
    # 739: public school
    {"ipa": "/ˈpʌblɪk skuːl/", "vi": "trường công lập", "pos": "phrase"},
    # 740: school system
    {"ipa": "/skuːl ˈsɪstəm/", "vi": "hệ thống giáo dục học đường", "pos": "phrase"},
    # 741: talk over
    {"ipa": "/tɔːk ˈoʊvər/", "vi": "thảo luận kỹ; bàn bạc cặn kẽ", "pos": "phrase"},
    # 742: working day
    {"ipa": "/ˈwɜːrkɪŋ deɪ/", "vi": "ngày làm việc; ngày công", "pos": "phrase"},
    # 743: after hours
    {"ipa": "/ˈæftər ˈaʊərz/", "vi": "ngoài giờ làm việc; sau ca làm", "pos": "phrase"},
    # 744: ask for it
    {"ipa": "/æsk fɔːr ɪt/", "vi": "tự chuốc lấy phiền toái", "pos": "phrase"},
    # 745: big top
    {"ipa": "/bɪɡ tɑːp/", "vi": "lều xiếc chính; rạp xiếc lớn", "pos": "phrase"},
    # 746: buy in
    {"ipa": "/baɪ ɪn/", "vi": "mua gom; mua cổ phần; đồng tình", "pos": "phrase"},
    # 747: close out
    {"ipa": "/kloʊz aʊt/", "vi": "thanh lý xả hàng; khép lại sổ sách", "pos": "phrase"},
    # 748: close up
    {"ipa": "/kloʊz ʌp/", "vi": "đóng cửa hẳn; đặc tả; thu hẹp", "pos": "phrase"},
    # 749: day book
    {"ipa": "/deɪ bʊk/", "vi": "sổ nhật ký kế toán; sổ nhật trình", "pos": "phrase"},
    # 750: each week
    {"ipa": "/iːtʃ wiːk/", "vi": "mỗi tuần; đều đặn từng tuần", "pos": "phrase"},
    # 751: for short
    {"ipa": "/fɔːr ʃɔːrt/", "vi": "gọi tắt là; nói ngắn gọn là", "pos": "phrase"},
    # 752: full house
    {"ipa": "/fʊl haʊs/", "vi": "chật kín rạp; cù lũ trong xì phé", "pos": "phrase"},
    # 753: get along with
    {"ipa": "/ɡɛt əˈlɔːŋ wɪð/", "vi": "hòa thuận với; ăn ý với", "pos": "phrase"},
    # 754: good guy
    {"ipa": "/ɡʊd ɡaɪ/", "vi": "người tốt; nhân vật chính diện", "pos": "phrase"},
    # 755: great war
    {"ipa": "/ɡreɪt wɔːr/", "vi": "Đại chiến thế giới lần thứ nhất", "pos": "phrase"},
    # 756: head of state
    {"ipa": "/hɛd ʌv steɪt/", "vi": "nguyên thủ quốc gia", "pos": "phrase"},
    # 757: high water
    {"ipa": "/haɪ ˈwɔːtər/", "vi": "nước lớn; đỉnh triều cường", "pos": "phrase"},
    # 758: hit it up
    {"ipa": "/hɪt ɪt ʌp/", "vi": "ăn chơi chè chén; vui chơi hết mình", "pos": "phrase"},
    # 759: home run
    {"ipa": "/hoʊm rʌn/", "vi": "cú chạy trọn vòng; thắng lợi rực rỡ", "pos": "phrase"},
    # 760: in short
    {"ipa": "/ɪn ʃɔːrt/", "vi": "tóm lại; nói tóm lại là", "pos": "phrase"},
    # 761: in turn
    {"ipa": "/ɪn tɜːrn/", "vi": "lần lượt; kết quả là", "pos": "phrase"},
    # 762: life story
    {"ipa": "/laɪf ˈstɔːri/", "vi": "câu chuyện cuộc đời; tiểu sử sống", "pos": "phrase"},
    # 763: long run
    {"ipa": "/lɔːŋ rʌn/", "vi": "chặng đường dài; đường dài", "pos": "phrase"},
    # 764: love line
    {"ipa": "/lʌv laɪn/", "vi": "đường tâm đạo; tuyến tình cảm", "pos": "phrase"},
    # 765: new york
    {"ipa": "/nuː jɔːrk/", "vi": "thành phố New York; bang New York", "pos": "phrase"},
    # 766: of age
    {"ipa": "/ʌv eɪdʒ/", "vi": "đến tuổi trưởng thành; đủ tuổi", "pos": "phrase"},
    # 767: party man
    {"ipa": "/ˈpɑːrti mæn/", "vi": "đảng viên trung kiên; người mê tiệc", "pos": "phrase"},
    # 768: place of business
    {"ipa": "/pleɪs ʌv ˈbɪznəs/", "vi": "nơi kinh doanh; địa điểm buôn bán", "pos": "phrase"},
    # 769: service man
    {"ipa": "/ˈsɜːrvɪs mæn/", "vi": "quân nhân; thợ bảo dưỡng kỹ thuật", "pos": "phrase"},
    # 770: stay on
    {"ipa": "/steɪ ɑːn/", "vi": "ở lại thêm; tiếp tục lưu lại", "pos": "phrase"},
    # 771: take five
    {"ipa": "/teɪk faɪv/", "vi": "nghỉ năm phút; giải lao một lát", "pos": "phrase"},
    # 772: taken with
    {"ipa": "/ˈteɪkən wɪð/", "vi": "say mê; bị cuốn hút bởi", "pos": "phrase"},
    # 773: turn in
    {"ipa": "/tɜːrn ɪn/", "vi": "giao nộp; gửi bài; đi ngủ", "pos": "phrase"},
    # 774: turn to
    {"ipa": "/tɜːrn tuː/", "vi": "quay sang; nhờ cậy; trông mong", "pos": "phrase"},
    # 775: world war
    {"ipa": "/wɜːrld wɔːr/", "vi": "chiến tranh thế giới; thế chiến", "pos": "phrase"},
    # 776: uses (headword is 'uses', noun plural of 'use', crawler previously hallucinated US)
    {"ipa": "/ˈjuːsɪz/", "vi": "các công dụng; những cách sử dụng", "pos": "noun"},
    # 777: also known as
    {"ipa": "/ˈɔːlsoʊ noʊn æz/", "vi": "còn được biết đến là; viết tắt là", "pos": "phrase"},
    # 778: american state
    {"ipa": "/əˈmɛrɪkən steɪt/", "vi": "bang của Mỹ; tiểu bang Hoa Kỳ", "pos": "phrase"},
    # 779: at first hand
    {"ipa": "/æt fɜːrst hænd/", "vi": "trực tiếp; tận mắt chứng kiến", "pos": "phrase"},
    # 780: big business
    {"ipa": "/bɪɡ ˈbɪznəs/", "vi": "giới đại tài phiệt; kinh doanh lớn", "pos": "phrase"},
    # 781: buy it
    {"ipa": "/baɪ ɪt/", "vi": "mất mạng; tin sái cổ", "pos": "phrase"},
    # 782: check in
    {"ipa": "/tʃɛk ɪn/", "vi": "làm thủ tục nhận phòng; điểm danh", "pos": "phrase"},
    # 783: coming back
    {"ipa": "/ˈkʌmɪŋ bæk/", "vi": "sự trở lại; sự tái xuất", "pos": "phrase"},
    # 784: family business
    {"ipa": "/ˈfæməli ˈbɪznəs/", "vi": "kinh doanh gia đình; việc riêng tư", "pos": "phrase"},
    # 785: free thought
    {"ipa": "/friː θɔːt/", "vi": "tư tưởng tự do; độc lập suy nghĩ", "pos": "phrase"},
    # 786: move out
    {"ipa": "/muːv aʊt/", "vi": "dọn ra ngoài; chuyển nhà đi", "pos": "phrase"},
    # 787: move up
    {"ipa": "/muːv ʌp/", "vi": "thăng tiến; tiến lên phía trước", "pos": "phrase"},
    # 788: once again
    {"ipa": "/wʌns əˈɡɛn/", "vi": "một lần nữa; lại thêm một lần", "pos": "phrase"},
    # 789: pay back
    {"ipa": "/peɪ bæk/", "vi": "trả nợ; hoàn tiền; báo thù", "pos": "phrase"},
    # 790: real number
    {"ipa": "/riːl ˈnʌmbər/", "vi": "số thực trong toán học", "pos": "phrase"},
    # 791: run around
    {"ipa": "/rʌn əˈraʊnd/", "vi": "chạy loanh quanh; chạy ngược xuôi", "pos": "phrase"},
    # 792: second thought
    {"ipa": "/ˈsɛkənd θɔːt/", "vi": "suy tính lại; ý nghĩ đắn đo", "pos": "phrase"},
    # 793: set free
    {"ipa": "/sɛt friː/", "vi": "trả tự do; giải phóng; phóng thích", "pos": "phrase"},
    # 794: show business
    {"ipa": "/ʃoʊ ˈbɪznəs/", "vi": "giới giải trí; ngành biểu diễn", "pos": "phrase"},
    # 795: social work
    {"ipa": "/ˈsoʊʃəl wɜːrk/", "vi": "ngành công tác xã hội", "pos": "phrase"},
    # 796: state line
    {"ipa": "/steɪt laɪn/", "vi": "ranh giới tiểu bang", "pos": "phrase"},
    # 797: stay at
    {"ipa": "/steɪ æt/", "vi": "ở tại; cư trú tại; duy trì ở mức", "pos": "phrase"},
    # 798: taking over
    {"ipa": "/ˈteɪkɪŋ ˈoʊvər/", "vi": "sự tiếp quản; sự giành quyền lực", "pos": "phrase"},
    # 799: turn on
    {"ipa": "/tɜːrn ɑːn/", "vi": "bật máy; khởi động; gây hưng phấn", "pos": "phrase"},
]

with open('scratch/b21_r02_raw_p3.json') as f:
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

with open('scratch/b21_r02_p3.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r02_p3.json created successfully and validated!")
