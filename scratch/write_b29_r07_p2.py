import json

reviewed_items = [
    {
        "id": "lex.en.200k.043102",
        "hw": "adolf loos",
        "pos": "phrase",
        "ipa": "/ˈædɔːlf loʊs/",
        "vi": "kiến trúc sư Adolf Loos",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043103",
        "hw": "alpha centauri",
        "pos": "phrase",
        "ipa": "/ˌælfə sɛnˈtɔːraɪ/",
        "vi": "hệ sao Alpha Centauri gần nhất",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043104",
        "hw": "anterior vertebral vein",
        "pos": "phrase",
        "ipa": "/ænˈtɪəriər ˈvɜːrtəbrəl veɪn/",
        "vi": "tĩnh mạch đốt sống trước",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043105",
        "hw": "aromatic aster",
        "pos": "phrase",
        "ipa": "/ˌærəˈmætɪk ˈæstər/",
        "vi": "cây cúc tây thơm cánh tím",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043106",
        "hw": "ashley montagu",
        "pos": "phrase",
        "ipa": "/ˈæʃli ˈmɑːntəɡjuː/",
        "vi": "nhà nhân học Ashley Montagu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043107",
        "hw": "awning deck",
        "pos": "phrase",
        "ipa": "/ˈɔːnɪŋ dɛk/",
        "vi": "boong tàu có mái che bạt",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043108",
        "hw": "becker muscular dystrophy",
        "pos": "phrase",
        "ipa": "/ˈbɛkər ˈmʌskjələr ˈdɪstrəfi/",
        "vi": "bệnh loạn dưỡng cơ Becker",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043109",
        "hw": "benjamin britten",
        "pos": "phrase",
        "ipa": "/ˈbɛndʒəmɪn ˈbrɪtn/",
        "vi": "nhạc sĩ Benjamin Britten",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043110",
        "hw": "beta centauri",
        "pos": "phrase",
        "ipa": "/ˌbeɪtə sɛnˈtɔːraɪ/",
        "vi": "ngôi sao sáng Beta Centauri",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043111",
        "hw": "binomial distribution",
        "pos": "phrase",
        "ipa": "/baɪˈnoʊmiəl ˌdɪstrɪˈbjuːʃən/",
        "vi": "phân phối nhị thức xác suất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043112",
        "hw": "black bream",
        "pos": "phrase",
        "ipa": "/blæk briːm/",
        "vi": "cá vền đen; cá tráp đen nước lợ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043113",
        "hw": "black hollander",
        "pos": "phrase",
        "ipa": "/blæk ˈhɑːləndər/",
        "vi": "loài liễu đen đầm lầy châu Âu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043114",
        "hw": "blood coagulation",
        "pos": "phrase",
        "ipa": "/blʌd koʊˌæɡjuˈleɪʃən/",
        "vi": "quá trình đông tụ máu sinh học",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043115",
        "hw": "brazilian trumpeter",
        "pos": "phrase",
        "ipa": "/brəˈzɪliən ˈtrʌmpɪtər/",
        "vi": "chim vỗ mỏ sẫm màu Brazil",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043116",
        "hw": "burlap bag",
        "pos": "phrase",
        "ipa": "/ˈbɜːrlæp bæɡ/",
        "vi": "bao tải gai; bao làm bằng vải bố",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043117",
        "hw": "calcium lactate",
        "pos": "phrase",
        "ipa": "/ˈkælsiəm ˈlækteɪt/",
        "vi": "muối canxi lactat bổ sung",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043118",
        "hw": "california fuchsia",
        "pos": "phrase",
        "ipa": "/ˌkælɪˈfɔːrnjə ˈfjuːʃə/",
        "vi": "cây hoa vân anh đỏ California",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043119",
        "hw": "cardinal tetra",
        "pos": "phrase",
        "ipa": "/ˈkɑːrdɪnl ˈtɛtrə/",
        "vi": "loài cá neon đỏ hồng y cảnh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043120",
        "hw": "carpal tunnel syndrome",
        "pos": "phrase",
        "ipa": "/ˈkɑːrpl ˈtʌnl ˈsɪndroʊm/",
        "vi": "hội chứng chèn ép ống cổ tay",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043121",
        "hw": "cervical vertebra",
        "pos": "phrase",
        "ipa": "/ˈsɜːrvɪkl ˈvɜːrtəbrə/",
        "vi": "đốt sống vùng cổ giải phẫu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043122",
        "hw": "chemical irritant",
        "pos": "phrase",
        "ipa": "/ˈkɛmɪkl ˈɪrɪtənt/",
        "vi": "chất gây kích ứng hóa chất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043123",
        "hw": "chilean hazelnut",
        "pos": "phrase",
        "ipa": "/ˌtʃɪliən ˈheɪzəlnʌt/",
        "vi": "cây phỉ dại Chile; hạt phỉ Chile",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043124",
        "hw": "citric acid",
        "pos": "phrase",
        "ipa": "/ˌsɪtrɪk ˈæsɪd/",
        "vi": "axit xitric; axit chanh hữu cơ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043125",
        "hw": "citric acid cycle",
        "pos": "phrase",
        "ipa": "/ˌsɪtrɪk ˈæsɪd ˈsaɪkl/",
        "vi": "chu trình Crep axit xitric tế bào",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043126",
        "hw": "coagulation factor",
        "pos": "phrase",
        "ipa": "/koʊˌæɡjuˈleɪʃən ˈfæktər/",
        "vi": "yếu tố đông máu huyết tương",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043127",
        "hw": "cornelia otis skinner",
        "pos": "phrase",
        "ipa": "/kɔːrˈniːliə ˈoʊtɪs ˈskɪnər/",
        "vi": "nữ văn sĩ Cornelia Otis Skinner",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043128",
        "hw": "crystallized fruit",
        "pos": "phrase",
        "ipa": "/ˈkrɪstəlaɪzd fruːt/",
        "vi": "mứt trái cây ngào đường kết tinh",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043129",
        "hw": "daniel patrick moynihan",
        "pos": "phrase",
        "ipa": "/ˈdænjəl ˈpætrɪk ˈmɔɪnɪhæn/",
        "vi": "nghị sĩ Daniel Patrick Moynihan",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043130",
        "hw": "death adder",
        "pos": "phrase",
        "ipa": "/dɛθ ˈædər/",
        "vi": "loài rắn hổ tử thần cực độc Úc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043131",
        "hw": "dorsal vertebra",
        "pos": "phrase",
        "ipa": "/ˈdɔːrsl ˈvɜːrtəbrə/",
        "vi": "đốt sống ngực; đốt sống lưng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043132",
        "hw": "edible mussel",
        "pos": "phrase",
        "ipa": "/ˈɛdəbl ˈmʌsl/",
        "vi": "con vẹm đen ăn được; trai biển",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043133",
        "hw": "edward benjamin britten",
        "pos": "phrase",
        "ipa": "/ˈɛdwərd ˈbɛndʒəmɪn ˈbrɪtn/",
        "vi": "nhạc sĩ Edward Benjamin Britten",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043134",
        "hw": "elastic modulus",
        "pos": "phrase",
        "ipa": "/ɪˈlæstɪk ˈmɑːdʒələs/",
        "vi": "mô-đun đàn hồi Young vật lý liệu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043135",
        "hw": "elizabeth cady stanton",
        "pos": "phrase",
        "ipa": "/ɪˈlɪzəbəθ ˈkeɪdi ˈstæntn/",
        "vi": "nhà nữ quyền Elizabeth Cady Stanton",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043136",
        "hw": "elizabethan sonnet",
        "pos": "phrase",
        "ipa": "/ɪˌlɪzəˈbiːθən ˈsɑːnɪt/",
        "vi": "thể thơ son-nê thời Elizabeth",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043137",
        "hw": "esophageal smear",
        "pos": "phrase",
        "ipa": "/ɪˌsɑːfəˈdʒiːəl smɪər/",
        "vi": "mẫu quệt tế bào niêm mạc thực quản",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043138",
        "hw": "european bream",
        "pos": "phrase",
        "ipa": "/ˌjʊərəˈpiːən briːm/",
        "vi": "cá vền nước ngọt sông châu Âu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043139",
        "hw": "european sea bream",
        "pos": "phrase",
        "ipa": "/ˌjʊərəˈpiːən siː briːm/",
        "vi": "cá tráp biển bạc vùng châu Âu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043140",
        "hw": "exogenous obesity",
        "pos": "phrase",
        "ipa": "/ɛkˈsɑːdʒənəs oʊˈbiːsəti/",
        "vi": "chứng béo phì do ăn uống quá mức",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043141",
        "hw": "felix mendelssohn",
        "pos": "phrase",
        "ipa": "/ˈfeɪlɪks ˈmɛndəlsən/",
        "vi": "soạn giả Felix Mendelssohn",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043142",
        "hw": "fibonacci number",
        "pos": "phrase",
        "ipa": "/ˌfɪbəˈnɑːtʃi ˈnʌmbər/",
        "vi": "con số trong dãy số Fibonacci",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043143",
        "hw": "flame nettle",
        "pos": "phrase",
        "ipa": "/fleɪm ˈnɛtl/",
        "vi": "cây tía tô cảnh lá đỏ rực lửa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043144",
        "hw": "flanker back",
        "pos": "phrase",
        "ipa": "/ˈflæŋkər bæk/",
        "vi": "cầu thủ tiền vệ cánh bắt bóng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043145",
        "hw": "forehand stroke",
        "pos": "phrase",
        "ipa": "/ˈfɔːrhænd stroʊk/",
        "vi": "cú đánh bóng thuận tay quần vợt",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043146",
        "hw": "fortran program",
        "pos": "phrase",
        "ipa": "/ˈfɔːrtræn ˈproʊɡræm/",
        "vi": "chương trình mã nguồn FORTRAN",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043147",
        "hw": "genital wart",
        "pos": "phrase",
        "ipa": "/ˈdʒɛnɪtl wɔːrt/",
        "vi": "bệnh sùi mào gà; mụn cóc sinh dục",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043148",
        "hw": "genus aix",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs eɪks/",
        "vi": "chi uyên ương chim nước Aix",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043149",
        "hw": "genus pinus",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs ˈpaɪnəs/",
        "vi": "chi thực vật cây lá kim Thông",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043150",
        "hw": "giant armadillo",
        "pos": "phrase",
        "ipa": "/ˈdʒaɪənt ˌɑːrməˈdɪloʊ/",
        "vi": "loài tatu khổng lồ Nam Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043151",
        "hw": "goat herder",
        "pos": "phrase",
        "ipa": "/ɡoʊt ˈhɜːrdər/",
        "vi": "người chăn đàn dê đồng cỏ",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043152",
        "hw": "grape hyacinth",
        "pos": "phrase",
        "ipa": "/ɡreɪp ˈhaɪəsɪnθ/",
        "vi": "hoa dạ lan hương chùm quả nho",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043153",
        "hw": "grass bacillus",
        "pos": "phrase",
        "ipa": "/ɡræs bəˈsɪləs/",
        "vi": "trực khuẩn cỏ khô phân hủy xác cây",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043154",
        "hw": "gumbo soil",
        "pos": "phrase",
        "ipa": "/ˈɡʌmboʊ sɔɪl/",
        "vi": "loại đất sét đen dính gumbo",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043155",
        "hw": "gun moll",
        "pos": "phrase",
        "ipa": "/ɡʌn mɑːl/",
        "vi": "người tình của tên cướp xã hội đen",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043156",
        "hw": "harnessed antelope",
        "pos": "phrase",
        "ipa": "/ˈhɑːrnɪst ˈæntəloʊp/",
        "vi": "linh dương sọc vằn lưng châu Phi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043157",
        "hw": "hydroxyl group",
        "pos": "phrase",
        "ipa": "/haɪˈdrɑːksəl ɡruːp/",
        "vi": "nhóm chức hi-đrô-xin hóa học",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043158",
        "hw": "infantile fixation",
        "pos": "phrase",
        "ipa": "/ˈɪnfəntaɪl fɪkˈseɪʃən/",
        "vi": "chứng mặc cảm ám ảnh thời thơ ấu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043159",
        "hw": "ivor armstrong richards",
        "pos": "phrase",
        "ipa": "/ˈaɪvər ˈɑːrmstrɔːŋ ˈrɪtʃərdz/",
        "vi": "nhà phê bình I. A. Richards",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043160",
        "hw": "jack nicklaus",
        "pos": "phrase",
        "ipa": "/dʒæk ˈnɪkləs/",
        "vi": "huyền thoại golf Jack Nicklaus",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043161",
        "hw": "jean arp",
        "pos": "phrase",
        "ipa": "/ʒɑːn ɑːrp/",
        "vi": "nghệ sĩ điêu khắc Jean Arp",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043162",
        "hw": "john haldane",
        "pos": "phrase",
        "ipa": "/dʒɑːn ˈhɔːldeɪn/",
        "vi": "nhà khoa học John Haldane",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043163",
        "hw": "jose julian marti",
        "pos": "phrase",
        "ipa": "/hoʊˈzeɪ huːˈljɑːn mɑːrˈtiː/",
        "vi": "nhà văn Cuba José Julián Martí",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043164",
        "hw": "karl friedrich gauss",
        "pos": "phrase",
        "ipa": "/kɑːrl ˈfriːdrɪç ɡaʊs/",
        "vi": "nhà toán học Carl Friedrich Gauss",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043165",
        "hw": "klamath river",
        "pos": "phrase",
        "ipa": "/ˈklæməθ ˈrɪvər/",
        "vi": "dòng sông Klamath ở Oregon",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043166",
        "hw": "law of archimedes",
        "pos": "phrase",
        "ipa": "/lɔː əv ˌɑːrkɪˈmiːdiːz/",
        "vi": "định luật lực đẩy Ác-si-mét",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043167",
        "hw": "leger line",
        "pos": "phrase",
        "ipa": "/ˈlɛdʒər laɪn/",
        "vi": "dòng kẻ phụ trên khuông nhạc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043168",
        "hw": "lilian alicia marks",
        "pos": "phrase",
        "ipa": "/ˈlɪliən əˈlɪʃə mɑːrks/",
        "vi": "nghệ sĩ múa Dame Alicia Markova",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043169",
        "hw": "littoral zone",
        "pos": "phrase",
        "ipa": "/ˈlɪtərəl zoʊn/",
        "vi": "vùng ven bờ duyên hải biển",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043170",
        "hw": "macular area",
        "pos": "phrase",
        "ipa": "/ˈmækjələr ˈɛəriə/",
        "vi": "vùng điểm vàng võng mạc mắt",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043171",
        "hw": "milk adder",
        "pos": "phrase",
        "ipa": "/mɪlk ˈædər/",
        "vi": "loài rắn sữa sọc khoang vô hại",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043172",
        "hw": "moreton bay pine",
        "pos": "phrase",
        "ipa": "/ˈmɔːrtən beɪ paɪn/",
        "vi": "cây thông Moreton Bay xứ Úc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043173",
        "hw": "moss campion",
        "pos": "phrase",
        "ipa": "/mɔːs ˈkæmpiən/",
        "vi": "cây cúc campion mọc đệm rêu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043174",
        "hw": "mullah omar",
        "pos": "phrase",
        "ipa": "/ˈmʊlə ˈoʊmɑːr/",
        "vi": "thủ lĩnh Taliban Mullah Omar",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043175",
        "hw": "native fuchsia",
        "pos": "phrase",
        "ipa": "/ˈneɪtɪv ˈfjuːʃə/",
        "vi": "cây hoa vân anh bản địa Úc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043176",
        "hw": "nepalese rupee",
        "pos": "phrase",
        "ipa": "/ˌnɛpəˈliːz ruːˈpiː/",
        "vi": "đồng tiền rupee của Nepal",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043177",
        "hw": "nerve block anaesthesia",
        "pos": "phrase",
        "ipa": "/nɜːrv blɑːk ˌænəsˈθiːʒə/",
        "vi": "gây tê phong bế dây thần kinh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043178",
        "hw": "new ballgame",
        "pos": "phrase",
        "ipa": "/nuː ˈbɔːlɡeɪm/",
        "vi": "cục diện hoàn toàn mới mẻ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043179",
        "hw": "new caledonian yew",
        "pos": "phrase",
        "ipa": "/nuː ˌkælɪˈdoʊniən juː/",
        "vi": "cây thông đỏ đảo New Caledonia",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043180",
        "hw": "newtonian mechanics",
        "pos": "phrase",
        "ipa": "/njuːˈtoʊniən mɪˈkænɪks/",
        "vi": "cơ học cổ điển hệ Newton",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043181",
        "hw": "nicol prism",
        "pos": "phrase",
        "ipa": "/ˈnɪkəl ˈprɪzəm/",
        "vi": "lăng kính phân cực Nicol",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043182",
        "hw": "offset lithography",
        "pos": "phrase",
        "ipa": "/ˈɔːfsɛt lɪˈθɑːɡrəfi/",
        "vi": "công nghệ in ốp-sét thạch bản",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043183",
        "hw": "paleozoic era",
        "pos": "phrase",
        "ipa": "/ˌpeɪlioʊˈzoʊɪk ˈɪərə/",
        "vi": "đại Cổ sinh địa chất học",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043184",
        "hw": "pectoral medallion",
        "pos": "phrase",
        "ipa": "/ˈpɛktərəl məˈdæljən/",
        "vi": "tấm kỷ niệm chương đeo trước ngực",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043185",
        "hw": "pernicious anemia",
        "pos": "phrase",
        "ipa": "/pərˈnɪʃəs əˈniːmiə/",
        "vi": "bệnh thiếu máu ác tính Biermer",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043186",
        "hw": "phone tapper",
        "pos": "phrase",
        "ipa": "/foʊn ˈtæpər/",
        "vi": "kẻ nghe trộm đường dây điện thoại",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043187",
        "hw": "physiological sphincter",
        "pos": "phrase",
        "ipa": "/ˌfɪziəˈlɑːdʒɪkl ˈsfɪŋktər/",
        "vi": "cơ thắt sinh lý cơ học",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043188",
        "hw": "piping guan",
        "pos": "phrase",
        "ipa": "/ˈpaɪpɪŋ ɡwɑːn/",
        "vi": "loài chim guan hót tiếng sáo",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043189",
        "hw": "radical mastectomy",
        "pos": "phrase",
        "ipa": "/ˈrædɪkl mæˈstɛktəmi/",
        "vi": "phẫu thuật đoạn nhũ triệt căn",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043190",
        "hw": "requisition form",
        "pos": "phrase",
        "ipa": "/ˌrɛkwɪˈzɪʃən fɔːrm/",
        "vi": "mẫu phiếu đề xuất lĩnh vật tư",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043191",
        "hw": "rhea silvia",
        "pos": "phrase",
        "ipa": "/ˈriːə ˈsɪlviə/",
        "vi": "nàng trinh nữ Rhea Silvia La Mã",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043192",
        "hw": "richard haldane",
        "pos": "phrase",
        "ipa": "/ˈrɪtʃərd ˈhɔːldeɪn/",
        "vi": "chính khách Richard Haldane",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043193",
        "hw": "rip van winkle",
        "pos": "phrase",
        "ipa": "/rɪp væn ˈwɪŋkl/",
        "vi": "kẻ ngủ quên lạc hậu với thời đại",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043194",
        "hw": "rivet line",
        "pos": "phrase",
        "ipa": "/ˈrɪvɪt laɪn/",
        "vi": "hàng tán đinh đường đinh tán",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043195",
        "hw": "sea bream",
        "pos": "phrase",
        "ipa": "/siː briːm/",
        "vi": "các loài cá tráp sống ở biển",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043196",
        "hw": "showy sunflower",
        "pos": "phrase",
        "ipa": "/ˈʃoʊi ˈsʌnˌflaʊər/",
        "vi": "cây hoa hướng dương nở rực rỡ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043197",
        "hw": "sir james paget",
        "pos": "phrase",
        "ipa": "/sɜːr dʒeɪmz ˈpædʒɪt/",
        "vi": "bác sĩ phẫu thuật Sir James Paget",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043198",
        "hw": "slop basin",
        "pos": "phrase",
        "ipa": "/slɑːp ˈbeɪsn/",
        "vi": "bát đổ bã trà nước cặn trên bàn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043199",
        "hw": "slouch hat",
        "pos": "phrase",
        "ipa": "/slaʊtʃ hæt/",
        "vi": "chiếc mũ phớt mềm vành cụp xuống",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043200",
        "hw": "startle reaction",
        "pos": "phrase",
        "ipa": "/ˈstɑːrtl riˈækʃən/",
        "vi": "phản xạ giật mình do kích thích",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043201",
        "hw": "startle response",
        "pos": "phrase",
        "ipa": "/ˈstɑːrtl rɪˈspɑːns/",
        "vi": "đáp ứng giật nảy mình phản xạ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r07_raw_p2.json') as f:
    raw = json.load(f)

assert len(reviewed_items) == 100, f"Expected 100, got {len(reviewed_items)}"
assert len(reviewed_items) == len(raw)

for i, (rev, orig) in enumerate(zip(reviewed_items, raw)):
    assert rev["id"] == orig["id"], f"ID mismatch at {i}: {rev['id']} vs {orig['id']}"
    assert rev["hw"] == orig["hw"], f"HW mismatch at {i}: {rev['hw']} vs {orig['hw']}"
    assert len(rev["vi"]) <= 35, f"VI too long ({len(rev['vi'])}) at {i}: {rev['vi']}"
    assert rev["vi"].strip(), f"Empty VI at {i}"
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/"), f"Invalid IPA at {i}: {rev['ipa']}"
    assert rev["status"] == "reviewed"

with open('scratch/b29_r07_p2.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 7 Part 2 verified and written successfully.")
