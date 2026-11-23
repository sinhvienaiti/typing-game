import json

reviewed_items = [
    {
        "id": "lex.en.200k.043902",
        "hw": "ectopic pregnancy",
        "pos": "phrase",
        "ipa": "/ɛkˈtɑːpɪk ˈprɛɡnənsi/",
        "vi": "tình trạng thai ngoài tử cung",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043903",
        "hw": "epidermal cell",
        "pos": "phrase",
        "ipa": "/ˌɛpɪˈdɜːrml sɛl/",
        "vi": "tế bào biểu bì da bên ngoài",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043904",
        "hw": "factor of proportionality",
        "pos": "phrase",
        "ipa": "/ˈfæktər əv prəˌpɔːrʃəˈnæləti/",
        "vi": "hệ số tỷ lệ thuận trong toán học",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043905",
        "hw": "faroe islands",
        "pos": "phrase",
        "ipa": "/ˈfɛroʊ ˈaɪləndz/",
        "vi": "quần đảo Faroe thuộc Đan Mạch",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043906",
        "hw": "filename extension",
        "pos": "phrase",
        "ipa": "/ˈfaɪlneɪm ɪkˈstɛnʃən/",
        "vi": "phần mở rộng của tệp tin máy tính",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043907",
        "hw": "francisco de goya",
        "pos": "phrase",
        "ipa": "/frænˈsɪskoʊ də ˈɡɔɪə/",
        "vi": "danh họa Tây Ban Nha Francisco Goya",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043908",
        "hw": "francisco goya",
        "pos": "phrase",
        "ipa": "/frænˈsɪskoʊ ˈɡɔɪə/",
        "vi": "danh họa Francisco Goya Tây Ban Nha",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043909",
        "hw": "fringed orchid",
        "pos": "phrase",
        "ipa": "/frɪndʒd ˈɔːrkɪd/",
        "vi": "loài lan có viền tua cánh hoa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043910",
        "hw": "gall midge",
        "pos": "phrase",
        "ipa": "/ɡɔːl mɪdʒ/",
        "vi": "loài muỗi năn hại lúa tạo u bướu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043911",
        "hw": "genus eugenia",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs juːˈdʒiːniə/",
        "vi": "chi Trâm; chi thực vật trâm ổi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043912",
        "hw": "genus fuchsia",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs ˈfjuːʃə/",
        "vi": "chi hoa lồng đèn; chi vân anh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043913",
        "hw": "genus mimosa",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs mɪˈmoʊsə/",
        "vi": "chi thực vật trinh nữ xấu hổ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043914",
        "hw": "genus uta",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs ˈjuːtə/",
        "vi": "chi thằn lằn hông đốm Uta",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043915",
        "hw": "geometrical regularity",
        "pos": "phrase",
        "ipa": "/ˌdʒiːəˈmɛtrɪkl ˌrɛɡjʊˈlærəti/",
        "vi": "tính đều đặn đối xứng hình học",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043916",
        "hw": "georg friedrich handel",
        "pos": "phrase",
        "ipa": "/ɡeɪˈɔːrɡ ˈfriːdrɪk ˈhændl/",
        "vi": "nhà soạn nhạc cổ điển Handel Đức",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043917",
        "hw": "george paget thomson",
        "pos": "phrase",
        "ipa": "/dʒɔːrdʒ ˈpædʒɪt ˈtɑːmsən/",
        "vi": "nhà vật lý George Paget Thomson",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043918",
        "hw": "giuseppe verdi",
        "pos": "phrase",
        "ipa": "/dʒʊˈzɛpi ˈvɛərdi/",
        "vi": "nhà soạn nhạc opera Giuseppe Verdi",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043919",
        "hw": "golden oldie",
        "pos": "phrase",
        "ipa": "/ˈɡoʊldən ˈoʊldi/",
        "vi": "bài hát kinh điển được ưa chuộng",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043920",
        "hw": "grand teton",
        "pos": "phrase",
        "ipa": "/ɡrænd ˈtiːtɑːn/",
        "vi": "đỉnh núi Grand Teton ở bang Wyoming",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043921",
        "hw": "greyish brown",
        "pos": "phrase",
        "ipa": "/ˈɡreɪɪʃ braʊn/",
        "vi": "màu nâu pha xám; sắc nâu ánh xám",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043922",
        "hw": "horned rattlesnake",
        "pos": "phrase",
        "ipa": "/hɔːrnd ˈrætlsneɪk/",
        "vi": "rắn chuông có sừng sa mạc Bắc Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043923",
        "hw": "immovable bandage",
        "pos": "phrase",
        "ipa": "/ɪˈmuːvəbl ˈbændɪdʒ/",
        "vi": "băng bột cố định xương bất động",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043924",
        "hw": "inside caliper",
        "pos": "phrase",
        "ipa": "/ˈɪnsaɪd ˈkæləpər/",
        "vi": "thước kẹp đo đường kính trong",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043925",
        "hw": "jamaica honeysuckle",
        "pos": "phrase",
        "ipa": "/dʒəˈmeɪkə ˈhʌnisʌkl/",
        "vi": "cây lạc tiên thơm xứ Jamaica",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043926",
        "hw": "julian the apostate",
        "pos": "phrase",
        "ipa": "/ˈdʒuːliən ði əˈpɑːsteɪt/",
        "vi": "hoàng đế La Mã Julian Kẻ Bội Giáo",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043927",
        "hw": "knuckle duster",
        "pos": "phrase",
        "ipa": "/ˈnʌkl ˈdʌstər/",
        "vi": "tay gấu đấm kim loại; quả đấm sắt",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043928",
        "hw": "lead colic",
        "pos": "phrase",
        "ipa": "/lɛd ˈkɑːlɪk/",
        "vi": "chứng đau bụng quặn do ngộ độc chì",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043929",
        "hw": "leeward islands",
        "pos": "phrase",
        "ipa": "/ˈliːwərd ˈaɪləndz/",
        "vi": "quần đảo Leeward ở vùng Caribe",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043930",
        "hw": "lentil soup",
        "pos": "phrase",
        "ipa": "/ˈlɛntl suːp/",
        "vi": "món súp đậu lăng nấu rau củ",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043931",
        "hw": "male pattern baldness",
        "pos": "phrase",
        "ipa": "/meɪl ˈpætərn ˈbɔːldnəs/",
        "vi": "chứng rụng tóc hói đầu ở nam giới",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043932",
        "hw": "medellin cartel",
        "pos": "phrase",
        "ipa": "/ˌmɛdəˈjiːn kɑːrˈtɛl/",
        "vi": "băng ma túy Medellín ở Colombia",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043933",
        "hw": "mount elbert",
        "pos": "phrase",
        "ipa": "/maʊnt ˈɛlbərt/",
        "vi": "đỉnh núi Elbert cao nhất Colorado",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043934",
        "hw": "mullah mohammed omar",
        "pos": "phrase",
        "ipa": "/ˈmʊlə moʊˈhæməd ˈoʊmɑːr/",
        "vi": "thủ lĩnh Taliban Mullah Omar",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043935",
        "hw": "neuromuscular blocking agent",
        "pos": "phrase",
        "ipa": "/ˌnʊəroʊˈmʌskjələr ˈblɑːkɪŋ ˈeɪdʒənt/",
        "vi": "thuốc giãn cơ ức chế thần kinh cơ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043936",
        "hw": "neuromuscular junction",
        "pos": "phrase",
        "ipa": "/ˌnʊəroʊˈmʌskjələr ˈdʒʌŋkʃən/",
        "vi": "khớp tiếp hợp giữa thần kinh và cơ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043937",
        "hw": "nob hill",
        "pos": "phrase",
        "ipa": "/nɑːb hɪl/",
        "vi": "khu đồi Nob Hill ở San Francisco",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043938",
        "hw": "norbert wiener",
        "pos": "phrase",
        "ipa": "/ˈnɔːrbərt ˈwiːnər/",
        "vi": "nhà toán học Norbert Wiener nước Mỹ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043939",
        "hw": "nouvelle cuisine",
        "pos": "phrase",
        "ipa": "/nuːˌvɛl kwɪˈziːn/",
        "vi": "trường phái ẩm thực tân kỳ Pháp",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043940",
        "hw": "nouvelle vague",
        "pos": "phrase",
        "ipa": "/nuːˌvɛl væɡ/",
        "vi": "trào lưu Làn sóng Mới điện ảnh Pháp",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043941",
        "hw": "occipital vein",
        "pos": "phrase",
        "ipa": "/ɑːkˈsɪpɪtl veɪn/",
        "vi": "tĩnh mạch chẩm phía sau đầu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043942",
        "hw": "ophthalmic vein",
        "pos": "phrase",
        "ipa": "/ɑːfˈθælmɪk veɪn/",
        "vi": "tĩnh mạch hốc mắt trong giải phẫu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043943",
        "hw": "orange balsam",
        "pos": "phrase",
        "ipa": "/ˈɔːrɪndʒ ˈbɔːlsəm/",
        "vi": "cây bóng nước hoa cam mọc hoang dại",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043944",
        "hw": "outside caliper",
        "pos": "phrase",
        "ipa": "/ˈaʊtsaɪd ˈkæləpər/",
        "vi": "thước cặp đo bề dày; compa đo ngoài",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043945",
        "hw": "phnom penh",
        "pos": "phrase",
        "ipa": "/pnɔːm ˈpɛn/",
        "vi": "thủ đô Phnôm Pênh của Campuchia",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043946",
        "hw": "plantain lily",
        "pos": "phrase",
        "ipa": "/ˈplæntɪn ˈlɪli/",
        "vi": "cây hoa ngọc trâm; hoa ngọc huệ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043947",
        "hw": "potassium bromide",
        "pos": "phrase",
        "ipa": "/pəˈtæsiəm ˈbroʊmaɪd/",
        "vi": "hóa chất kali bromua an thần",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043948",
        "hw": "prairie mimosa",
        "pos": "phrase",
        "ipa": "/ˈprɛri mɪˈmoʊsə/",
        "vi": "loài cây trinh nữ đồng cỏ Bắc Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043949",
        "hw": "pro rata",
        "pos": "phrase",
        "ipa": "/proʊ ˈrɑːtə/",
        "vi": "tính theo tỷ lệ tương ứng phân bổ",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043950",
        "hw": "pulmonary emphysema",
        "pos": "phrase",
        "ipa": "/ˈpʊlmənɛri ˌɛmfəˈziːmə/",
        "vi": "chứng bệnh giãn phế nang phổi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043951",
        "hw": "rosebud orchid",
        "pos": "phrase",
        "ipa": "/ˈroʊzbʌd ˈɔːrkɪd/",
        "vi": "loài hoa lan nụ hồng hoang dã",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043952",
        "hw": "sea crawfish",
        "pos": "phrase",
        "ipa": "/siː ˈkrɔːfɪʃ/",
        "vi": "tôm hùm đá; tôm rồng không càng gai",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043953",
        "hw": "shariah law",
        "pos": "phrase",
        "ipa": "/ʃəˈriːə lɔː/",
        "vi": "luật Hồi giáo Sharia thiêng liêng",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043954",
        "hw": "shoestring catch",
        "pos": "phrase",
        "ipa": "/ˈʃuːstrɪŋ kætʃ/",
        "vi": "pha bắt bóng sát mặt đất bóng chày",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043955",
        "hw": "sickle alfalfa",
        "pos": "phrase",
        "ipa": "/ˈsɪkl ælˈfælfə/",
        "vi": "cây cỏ linh lăng quả hình lưỡi liềm",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043956",
        "hw": "sine qua non",
        "pos": "phrase",
        "ipa": "/ˌsɪneɪ kwɑː ˈnoʊn/",
        "vi": "điều kiện thiết yếu tiên quyết",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043957",
        "hw": "soup ladle",
        "pos": "phrase",
        "ipa": "/suːp ˈleɪdl/",
        "vi": "chiếc muôi lớn chuyên múc súp canh",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043958",
        "hw": "splint bone",
        "pos": "phrase",
        "ipa": "/splɪnt boʊn/",
        "vi": "xương thoái hóa bàn chân ngựa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043959",
        "hw": "squamous cell",
        "pos": "phrase",
        "ipa": "/ˈskweɪməs sɛl/",
        "vi": "tế bào biểu mô dạng vảy cá",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043960",
        "hw": "squash racquet",
        "pos": "phrase",
        "ipa": "/skwɑːʃ ˈrækɪt/",
        "vi": "chiếc vợt chơi môn bóng quần squash",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043961",
        "hw": "star anise",
        "pos": "phrase",
        "ipa": "/stɑːr ˈænɪs/",
        "vi": "hoa hồi gia vị; quả đại hồi khô",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043962",
        "hw": "stinking smut",
        "pos": "phrase",
        "ipa": "/ˈstɪŋkɪŋ smʌt/",
        "vi": "bệnh than đen hôi thối ở lúa mì",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043963",
        "hw": "taoist trinity",
        "pos": "phrase",
        "ipa": "/ˈdaʊɪst ˈtrɪnəti/",
        "vi": "Tam Thanh tôn kính của Đạo giáo",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043964",
        "hw": "tenor saxophonist",
        "pos": "phrase",
        "ipa": "/ˈtɛnər sækˈsɑːfənɪst/",
        "vi": "nghệ sĩ chơi đàn kèn săng-xô tê-no",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043965",
        "hw": "teton range",
        "pos": "phrase",
        "ipa": "/ˈtiːtɑːn reɪndʒ/",
        "vi": "dãy núi Grand Teton hiểm trở ở Mỹ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043966",
        "hw": "tine test",
        "pos": "phrase",
        "ipa": "/taɪn tɛst/",
        "vi": "xét nghiệm lao bì bằng kim chích",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043967",
        "hw": "trawl line",
        "pos": "phrase",
        "ipa": "/trɔːl laɪn/",
        "vi": "dây câu cá ngừ dài đáy biển sâu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043968",
        "hw": "trawl net",
        "pos": "phrase",
        "ipa": "/trɔːl nɛt/",
        "vi": "tấm lưới kéo đáy bắt cá biển khơi",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043969",
        "hw": "ugly duckling",
        "pos": "phrase",
        "ipa": "/ˈʌɡli ˈdʌklɪŋ/",
        "vi": "chú vịt con xấu xí hóa thiên nga",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043970",
        "hw": "white fringed orchid",
        "pos": "phrase",
        "ipa": "/waɪt frɪndʒd ˈɔːrkɪd/",
        "vi": "loài lan viền tua trắng tuyết",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043971",
        "hw": "wilhelm von opel",
        "pos": "phrase",
        "ipa": "/ˈvɪlhɛlm fɔn ˈoʊpəl/",
        "vi": "nhà chế tạo ô tô Wilhelm von Opel",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043972",
        "hw": "william dean howells",
        "pos": "phrase",
        "ipa": "/ˈwɪliəm diːn ˈhaʊəlz/",
        "vi": "nhà văn Mỹ William Dean Howells",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043973",
        "hw": "zebra mussel",
        "pos": "phrase",
        "ipa": "/ˈziːbrə ˈmʌsl/",
        "vi": "loài trai vằn vỏ sọc xâm lấn thủy",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043974",
        "hw": "amethysts",
        "pos": "noun",
        "ipa": "/ˈæməθɪsts/",
        "vi": "những viên đá ngọc thạch anh tím",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043975",
        "hw": "anils",
        "pos": "noun",
        "ipa": "/ˈænɪlz/",
        "vi": "cây chàm dại; thuốc nhuộm chàm xanh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043976",
        "hw": "bovines",
        "pos": "noun",
        "ipa": "/ˈboʊvaɪnz/",
        "vi": "động vật thuộc phân họ trâu bò",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043977",
        "hw": "cabots",
        "pos": "noun",
        "ipa": "/ˈkæbəts/",
        "vi": "những người mang họ Cabot",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043978",
        "hw": "capricorns",
        "pos": "noun",
        "ipa": "/ˈkæprɪkɔːrnz/",
        "vi": "người cung Ma Kết; chòm sao Ma Kết",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043979",
        "hw": "cervices",
        "pos": "noun",
        "ipa": "/ˈsɜːrvɪsiːz/",
        "vi": "các vùng cổ tử cung; đoạn cổ gáy",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043980",
        "hw": "cheerier",
        "pos": "adj",
        "ipa": "/ˈtʃɪriər/",
        "vi": "tươi vui phấn khởi hơn; rạng rỡ hơn",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043981",
        "hw": "cheeriest",
        "pos": "adj",
        "ipa": "/ˈtʃɪriɪst/",
        "vi": "tươi vui nhất; rạng rỡ hớn hở nhất",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043982",
        "hw": "chits",
        "pos": "noun",
        "ipa": "/tʃɪts/",
        "vi": "phiếu thanh toán ký nợ; cô bé ranh",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043983",
        "hw": "chomskies",
        "pos": "noun",
        "ipa": "/ˈtʃɑːmskiz/",
        "vi": "những người mang họ Chomsky",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043984",
        "hw": "cogging",
        "pos": "verb",
        "ipa": "/ˈkɑːɡɪŋ/",
        "vi": "đang cán ép sơ bộ thỏi thép mộc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043985",
        "hw": "cogs",
        "pos": "noun",
        "ipa": "/kɑːɡz/",
        "vi": "các răng cưa; chi tiết bánh răng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043986",
        "hw": "connectives",
        "pos": "noun",
        "ipa": "/kəˈnɛktɪvz/",
        "vi": "từ liên kết trong câu; mô liên kết",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043987",
        "hw": "crustier",
        "pos": "adj",
        "ipa": "/ˈkrʌstiər/",
        "vi": "nhiều vỏ giòn hơn; cẳn nhằn hơn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043988",
        "hw": "crustiest",
        "pos": "adj",
        "ipa": "/ˈkrʌstiɪst/",
        "vi": "nhiều vỏ giòn nhất; càu nhàu nhất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043989",
        "hw": "daweses",
        "pos": "noun",
        "ipa": "/ˈdɔːzɪz/",
        "vi": "những người mang họ Dawes",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043990",
        "hw": "decals",
        "pos": "noun",
        "ipa": "/ˈdiːkælz/",
        "vi": "hình dán đề-can; tấm decal họa tiết",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043991",
        "hw": "delphis",
        "pos": "noun",
        "ipa": "/ˈdɛlfaɪz/",
        "vi": "thành cổ Delphi; mô hình Delphi",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043992",
        "hw": "dissections",
        "pos": "noun",
        "ipa": "/dɪˈsɛkʃənz/",
        "vi": "các cuộc mổ xẻ phân tích thi thể",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043993",
        "hw": "distillations",
        "pos": "noun",
        "ipa": "/ˌdɪstɪˈleɪʃənz/",
        "vi": "quá trình chưng cất; tinh hoa đọng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043994",
        "hw": "drabbed",
        "pos": "verb",
        "ipa": "/dræbd/",
        "vi": "đã làm buồn tẻ; đã nhuộm màu xám",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043995",
        "hw": "drabber",
        "pos": "adj",
        "ipa": "/ˈdræbər/",
        "vi": "buồn tẻ tẻ nhạt hơn; xám xịt hơn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043996",
        "hw": "drabbest",
        "pos": "adj",
        "ipa": "/ˈdræbɪst/",
        "vi": "buồn tẻ nhất; ảm đạm xám xịt nhất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043997",
        "hw": "drabbing",
        "pos": "verb",
        "ipa": "/ˈdræbɪŋ/",
        "vi": "làm cho buồn tẻ xám xịt; trụy lạc",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043998",
        "hw": "drabs",
        "pos": "noun",
        "ipa": "/dræbz/",
        "vi": "vải len thô xám; phụ nữ lẳng lơ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043999",
        "hw": "eegs",
        "pos": "noun",
        "ipa": "/ˌiː iː ˈdʒiːz/",
        "vi": "kỹ thuật đo điện não đồ lâm sàng",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044000",
        "hw": "ellingtons",
        "pos": "noun",
        "ipa": "/ˈɛlɪŋtənz/",
        "vi": "những người mang họ Ellington",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044001",
        "hw": "enmities",
        "pos": "noun",
        "ipa": "/ˈɛnmətiz/",
        "vi": "sự căm ghét thù địch; mối thù oán",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r08_raw_p5.json') as f:
    raw = json.load(f)

assert len(reviewed_items) == 100, f"Expected 100 items, got {len(reviewed_items)}"
assert len(raw) == 100, f"Expected 100 raw items, got {len(raw)}"

valid_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}

for i, (rev, orig) in enumerate(zip(reviewed_items, raw)):
    assert rev["id"] == orig["id"], f"ID mismatch at {i}: {rev['id']} vs {orig['id']}"
    assert rev["hw"] == orig["hw"], f"HW mismatch at {i}: {rev['hw']} vs {orig['hw']}"
    assert rev["pos"] in valid_pos, f"Invalid POS at {i}: {rev['pos']}"
    assert len(rev["vi"]) <= 35, f"VI too long ({len(rev['vi'])}) at {i}: {rev['vi']}"
    assert rev["status"] == "reviewed", f"Invalid status at {i}"
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/"), f"Invalid IPA at {i}: {rev['ipa']}"
    assert rev["ipa"].count("/") == 2, f"IPA slashes count != 2 at {i}: {rev['ipa']}"

with open('scratch/b29_r08_p5.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 8 Part 5 verified and written successfully.")
