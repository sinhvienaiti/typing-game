import json

reviewed_items = [
    {
        "id": "lex.en.200k.043502",
        "hw": "bolo tie",
        "pos": "phrase",
        "ipa": "/ˈboʊloʊ taɪ/",
        "vi": "cà vạt dây rút bolo miền Tây Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043503",
        "hw": "common plantain",
        "pos": "phrase",
        "ipa": "/ˈkɑːmən ˈplæntɪn/",
        "vi": "cây mã đề thảo dược quen thuộc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043504",
        "hw": "computed axial tomography",
        "pos": "phrase",
        "ipa": "/kəmˈpjuːtɪd ˈæksiəl təˈmɑːɡrəfi/",
        "vi": "kỹ thuật chụp cắt lớp vi tính CT",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043505",
        "hw": "conga line",
        "pos": "phrase",
        "ipa": "/ˈkɑːŋɡə laɪn/",
        "vi": "hàng người nối đuôi nhảy điệu conga",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043506",
        "hw": "congestive heart failure",
        "pos": "phrase",
        "ipa": "/kənˈdʒɛstɪv hɑːrt ˈfeɪljər/",
        "vi": "bệnh suy tim sung huyết mạn tính",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043507",
        "hw": "corona borealis",
        "pos": "phrase",
        "ipa": "/kəˈroʊnə ˌbɔːriˈælɪs/",
        "vi": "chòm sao Vương Miện Phương Bắc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043508",
        "hw": "creme de cacao",
        "pos": "phrase",
        "ipa": "/ˌkrɛm də kəˈkaʊ/",
        "vi": "rượu mùi vị sô-cô-la ca cao ngọt",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043509",
        "hw": "crystallized ginger",
        "pos": "phrase",
        "ipa": "/ˈkrɪstəlaɪzd ˈdʒɪndʒər/",
        "vi": "mứt gừng dẻo phủ đường kết tinh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043510",
        "hw": "de jure segregation",
        "pos": "phrase",
        "ipa": "/deɪ ˈdʒʊəri ˌsɛɡrɪˈɡeɪʃən/",
        "vi": "phân biệt chủng tộc theo luật định",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043511",
        "hw": "diurnal variation",
        "pos": "phrase",
        "ipa": "/daɪˈɜːrnl ˌvɛəriˈeɪʃən/",
        "vi": "sự biến thiên tuần hoàn trong ngày",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043512",
        "hw": "english plantain",
        "pos": "phrase",
        "ipa": "/ˈɪŋɡlɪʃ ˈplæntɪn/",
        "vi": "cây mã đề lá thon dài hoa trắng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043513",
        "hw": "eocene epoch",
        "pos": "phrase",
        "ipa": "/ˈiːəˌsiːn ˈɛpək/",
        "vi": "thế Thủy Tân; thế địa chất Eocen",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043514",
        "hw": "european honeysuckle",
        "pos": "phrase",
        "ipa": "/ˌjʊərəˈpiːən ˈhʌniˌsʌkl/",
        "vi": "cây kim ngân hoa châu Âu thơm",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043515",
        "hw": "ex tempore",
        "pos": "phrase",
        "ipa": "/ɛks ˈtɛmpəri/",
        "vi": "nói ứng khẩu; không soạn bài trước",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043516",
        "hw": "fal la",
        "pos": "phrase",
        "ipa": "/fæ lɑː/",
        "vi": "điệp khúc ca hát vui nhộn fal la",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043517",
        "hw": "femoral biceps",
        "pos": "phrase",
        "ipa": "/ˈfɛmərəl ˈbaɪsɛps/",
        "vi": "cơ nhị đầu đùi sau giải phẫu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043518",
        "hw": "fly honeysuckle",
        "pos": "phrase",
        "ipa": "/flaɪ ˈhʌniˌsʌkl/",
        "vi": "cây kim ngân ruồi mọc dại rừng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043519",
        "hw": "flying buttress",
        "pos": "phrase",
        "ipa": "/ˈflaɪɪŋ ˈbʌtrəs/",
        "vi": "trụ đỡ vòm bay kiến trúc Gothic",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043520",
        "hw": "francis of assisi",
        "pos": "phrase",
        "ipa": "/ˈfrænsɪs əv əˈsiːzi/",
        "vi": "Thánh Phanxicô thành Assisi",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043521",
        "hw": "francisco fernandez cordoba",
        "pos": "phrase",
        "ipa": "/frɑːnˈsiːskoʊ fɛrˈnɑːndɛz ˈkɔːrdəbə/",
        "vi": "nhà thám hiểm Francisco Córdoba",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043522",
        "hw": "french honeysuckle",
        "pos": "phrase",
        "ipa": "/frɛntʃ ˈhʌniˌsʌkl/",
        "vi": "cây kim ngân đậu vương hoa đỏ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043523",
        "hw": "freshwater mussel",
        "pos": "phrase",
        "ipa": "/ˈfrɛʃwɔːtər ˈmʌsl/",
        "vi": "loài trai sò nước ngọt sống đáy",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043524",
        "hw": "gravitation wave",
        "pos": "phrase",
        "ipa": "/ˌɡrævɪˈteɪʃən weɪv/",
        "vi": "sóng trọng lực; sóng hấp dẫn vũ trụ",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043525",
        "hw": "great australian bight",
        "pos": "phrase",
        "ipa": "/ɡreɪt ɔːˈstreɪliən baɪt/",
        "vi": "vịnh Đại Úc ở bờ nam biển khơi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043526",
        "hw": "hans adolf krebs",
        "pos": "phrase",
        "ipa": "/hɑːns ˈædɔːlf krɛbz/",
        "vi": "nhà sinh hóa Hans Adolf Krebs",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043527",
        "hw": "hans arp",
        "pos": "phrase",
        "ipa": "/hɑːns ɑːrp/",
        "vi": "nghệ sĩ điêu khắc họa sĩ Hans Arp",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043528",
        "hw": "hay bacillus",
        "pos": "phrase",
        "ipa": "/heɪ bəˈsɪləs/",
        "vi": "trực khuẩn cỏ khô hoại sinh đất",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043529",
        "hw": "hedge nettle",
        "pos": "phrase",
        "ipa": "/hɛdʒ ˈnɛtl/",
        "vi": "cây tầm ma hàng rào hoa tím dại",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043530",
        "hw": "honeysuckle family",
        "pos": "phrase",
        "ipa": "/ˈhʌniˌsʌkl ˈfæmɪli/",
        "vi": "họ thực vật hoa kim ngân dây leo",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043531",
        "hw": "horatio herbert kitchener",
        "pos": "phrase",
        "ipa": "/həˈreɪʃioʊ ˈhɜːrbərt ˈkɪtʃənər/",
        "vi": "thống chế Horatio H. Kitchener",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043532",
        "hw": "horseradish root",
        "pos": "phrase",
        "ipa": "/ˈhɔːrsrædɪʃ ruːt/",
        "vi": "củ cây cải ngựa cay nồng thơm",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043533",
        "hw": "horseradish sauce",
        "pos": "phrase",
        "ipa": "/ˈhɔːrsrædɪʃ sɔːs/",
        "vi": "nước sốt cải ngựa cay gắt béo",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043534",
        "hw": "hydroxyl ion",
        "pos": "phrase",
        "ipa": "/haɪˈdrɑːksəl ˈaɪən/",
        "vi": "anion bazơ hi-đrô-xin OH-",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043535",
        "hw": "indian mongoose",
        "pos": "phrase",
        "ipa": "/ˈɪndiən ˈmɑːŋɡuːs/",
        "vi": "loài cầy mangut xám ở Ấn Độ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043536",
        "hw": "indian plantain",
        "pos": "phrase",
        "ipa": "/ˈɪndiən ˈplæntɪn/",
        "vi": "cây mã đề dại thảo mộc Ấn Độ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043537",
        "hw": "isthmus of suez",
        "pos": "phrase",
        "ipa": "/ˈɪsməs əv suːˈɛz/",
        "vi": "eo đất nối lục địa Xuy-ê Suez",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043538",
        "hw": "italian honeysuckle",
        "pos": "phrase",
        "ipa": "/ɪˈtæljən ˈhʌniˌsʌkl/",
        "vi": "cây kim ngân hoa thơm nước Ý",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043539",
        "hw": "jan hus",
        "pos": "phrase",
        "ipa": "/jɑːn hʊs/",
        "vi": "nhà cải cách tôn giáo Jan Hus",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043540",
        "hw": "janis joplin",
        "pos": "phrase",
        "ipa": "/ˈdʒænɪs ˈdʒɑːplɪn/",
        "vi": "huyền thoại nhạc rock Janis Joplin",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043541",
        "hw": "japanese honeysuckle",
        "pos": "phrase",
        "ipa": "/ˌdʒæpəˈniːz ˈhʌniˌsʌkl/",
        "vi": "cây kim ngân hoa vàng Nhật Bản",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043542",
        "hw": "johann mendel",
        "pos": "phrase",
        "ipa": "/ˈjoʊhæn ˈmɛndl/",
        "vi": "nhà di truyền học Gregor Mendel",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043543",
        "hw": "john steinbeck",
        "pos": "phrase",
        "ipa": "/dʒɑːn ˈstaɪnbɛk/",
        "vi": "đại văn hào Mỹ John Steinbeck",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043544",
        "hw": "jupiter optimus maximus",
        "pos": "phrase",
        "ipa": "/ˈdʒuːpɪtər ˈɑːptɪməs ˈmæksɪməs/",
        "vi": "thần tối cao Jupiter Optimus La Mã",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043545",
        "hw": "justinian code",
        "pos": "phrase",
        "ipa": "/dʒʌˈstɪniən koʊd/",
        "vi": "Bộ luật La Mã cổ điển Justinian",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043546",
        "hw": "justinian the great",
        "pos": "phrase",
        "ipa": "/dʒʌˈstɪniən ðə ɡreɪt/",
        "vi": "Đại đế La Mã Justinian I",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043547",
        "hw": "keogh plan",
        "pos": "phrase",
        "ipa": "/ˈkiːoʊ plæn/",
        "vi": "chương trình hưu trí tự lập Keogh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043548",
        "hw": "kuan yin",
        "pos": "phrase",
        "ipa": "/ɡwɑːn jɪn/",
        "vi": "Phật Quan Thế Âm Bồ Tát từ bi",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043549",
        "hw": "law of gravitation",
        "pos": "phrase",
        "ipa": "/lɔː əv ˌɡrævɪˈteɪʃən/",
        "vi": "định luật vạn vật hấp dẫn Newton",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043550",
        "hw": "line squall",
        "pos": "phrase",
        "ipa": "/laɪn skwɔːl/",
        "vi": "đường gió lốc dông giật theo hàng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043551",
        "hw": "mantis prawn",
        "pos": "phrase",
        "ipa": "/ˈmæntɪs prɔːn/",
        "vi": "con tôm tích; tôm tít bề bề biển",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043552",
        "hw": "marsh harrier",
        "pos": "phrase",
        "ipa": "/mɑːrʃ ˈhæriər/",
        "vi": "loài diều hâu đầm lầy săn chuột",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043553",
        "hw": "mary magdalen",
        "pos": "phrase",
        "ipa": "/ˈmɛəri ˈmæɡdələn/",
        "vi": "Thánh nữ Maria Ma-đa-lê-na",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043554",
        "hw": "maurice ravel",
        "pos": "phrase",
        "ipa": "/moʊˈriːs rəˈvɛl/",
        "vi": "nhạc sĩ thiên tài Maurice Ravel",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043555",
        "hw": "metamorphic rock",
        "pos": "phrase",
        "ipa": "/ˌmɛtəˈmɔːrfɪk rɑːk/",
        "vi": "loại đá biến chất địa chất học",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043556",
        "hw": "myrtle warbler",
        "pos": "phrase",
        "ipa": "/ˈmɜːrtl ˈwɔːrblər/",
        "vi": "chim chích đầm lầy mông vàng sim",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043557",
        "hw": "newtonian telescope",
        "pos": "phrase",
        "ipa": "/njuːˈtoʊniən ˈtɛləskoʊp/",
        "vi": "kính thiên văn phản xạ của Newton",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043558",
        "hw": "occipital bone",
        "pos": "phrase",
        "ipa": "/ɑːkˈsɪpɪtl boʊn/",
        "vi": "xương chẩm nằm phía sau gáy sọ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043559",
        "hw": "omega centauri",
        "pos": "phrase",
        "ipa": "/oʊˈmeɪɡə sɛnˈtɔːraɪ/",
        "vi": "cụm sao cầu khổng lồ Omega Centauri",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043560",
        "hw": "ordinal number",
        "pos": "phrase",
        "ipa": "/ˈɔːrdənl ˈnʌmbər/",
        "vi": "số thứ tự trong toán học ngữ pháp",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043561",
        "hw": "oriental alabaster",
        "pos": "phrase",
        "ipa": "/ˌɔːriˈɛntl ˈæləbæstər/",
        "vi": "đá cẩm thạch thạch cao phương Đông",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043562",
        "hw": "palau islands",
        "pos": "phrase",
        "ipa": "/pəˈlaʊ ˈaɪləndz/",
        "vi": "quần đảo san hô nhiệt đới Palau",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043563",
        "hw": "parietal lobe",
        "pos": "phrase",
        "ipa": "/pəˈraɪətl loʊb/",
        "vi": "thùy đỉnh của vỏ não bán cầu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043564",
        "hw": "pea weevil",
        "pos": "phrase",
        "ipa": "/piː ˈwiːvɪl/",
        "vi": "con mọt đục khoét hạt đậu Hà Lan",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043565",
        "hw": "plantain family",
        "pos": "phrase",
        "ipa": "/ˈplæntɪn ˈfæmɪli/",
        "vi": "họ thực vật mã đề Plantaginaceae",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043566",
        "hw": "plantain tree",
        "pos": "phrase",
        "ipa": "/ˈplæntɪn triː/",
        "vi": "cây chuối lá; cây chuối nấu ăn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043567",
        "hw": "plasmid dna",
        "pos": "phrase",
        "ipa": "/ˈplæzmɪd ˌdiː ɛn ˈeɪ/",
        "vi": "phân tử ADN plasmid vi khuẩn",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043568",
        "hw": "potassium bicarbonate",
        "pos": "phrase",
        "ipa": "/pəˈtæsiəm baɪˌkɑːrbənət/",
        "vi": "muối kali bicacbonat phụ gia",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043569",
        "hw": "power pylon",
        "pos": "phrase",
        "ipa": "/ˈpaʊər ˈpaɪlɑːn/",
        "vi": "cột điện cao thế thép không rỉ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043570",
        "hw": "price gouging",
        "pos": "phrase",
        "ipa": "/praɪs ˈɡaʊdʒɪŋ/",
        "vi": "hành vi găm hàng đẩy giá chặt chém",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043571",
        "hw": "pro tempore",
        "pos": "phrase",
        "ipa": "/proʊ ˈtɛmpəri/",
        "vi": "đảm nhiệm tạm quyền; lâm thời",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043572",
        "hw": "pruning shears",
        "pos": "phrase",
        "ipa": "/ˈpruːnɪŋ ʃɪərz/",
        "vi": "kéo bấm tỉa cành cây làm vườn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043573",
        "hw": "pygmy sperm whale",
        "pos": "phrase",
        "ipa": "/ˈpɪɡmi spɜːrm weɪl/",
        "vi": "loài cá nhà táng nhỏ tí hon",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043574",
        "hw": "quirk moulding",
        "pos": "phrase",
        "ipa": "/kwɜːrk ˈmoʊldɪŋ/",
        "vi": "gờ chỉ kiến trúc có rãnh soi lõm",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043575",
        "hw": "reflexive pronoun",
        "pos": "phrase",
        "ipa": "/rɪˈflɛksɪv ˈproʊnaʊn/",
        "vi": "đại từ phản thân trong ngữ pháp",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043576",
        "hw": "republic of palau",
        "pos": "phrase",
        "ipa": "/rɪˈpʌblɪk əv pəˈlaʊ/",
        "vi": "quốc đảo Cộng hòa Palau Thái Bình",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043577",
        "hw": "saddle block anaesthesia",
        "pos": "phrase",
        "ipa": "/ˈsædl blɑːk ˌænəsˈθiːʒə/",
        "vi": "phương pháp gây tê kiểu yên ngựa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043578",
        "hw": "seychelles rupee",
        "pos": "phrase",
        "ipa": "/seɪˈʃɛlz ruːˈpiː/",
        "vi": "đồng rupee đảo quốc Seychelles",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043579",
        "hw": "signet ring",
        "pos": "phrase",
        "ipa": "/ˈsɪɡnɪt rɪŋ/",
        "vi": "chiếc nhẫn khắc con dấu đóng triện",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043580",
        "hw": "sir isaac pitman",
        "pos": "phrase",
        "ipa": "/sɜːr ˈaɪzək ˈpɪtmən/",
        "vi": "nhà phát minh tốc ký Isaac Pitman",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043581",
        "hw": "smooth hammerhead",
        "pos": "phrase",
        "ipa": "/smuːð ˈhæmərˌhɛd/",
        "vi": "cá mập đầu búa mắt trơn ăn thịt",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043582",
        "hw": "spherical trigonometry",
        "pos": "phrase",
        "ipa": "/ˈsfɛrɪkl ˌtrɪɡəˈnɑːmətri/",
        "vi": "lượng giác mặt cầu trong toán học",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043583",
        "hw": "squall line",
        "pos": "phrase",
        "ipa": "/skwɔːl laɪn/",
        "vi": "dải đường dông tố gió giật mạnh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043584",
        "hw": "squaw corn",
        "pos": "phrase",
        "ipa": "/skwɔː kɔːrn/",
        "vi": "giống ngô bắp hạt mềm bản địa Mỹ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043585",
        "hw": "squaw grass",
        "pos": "phrase",
        "ipa": "/skwɔː ɡræs/",
        "vi": "cỏ đuôi gấu trắng vùng núi cao",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043586",
        "hw": "squaw root",
        "pos": "phrase",
        "ipa": "/skwɔː ruːt/",
        "vi": "cây cỏ rễ củ ký sinh squaw root",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043587",
        "hw": "swot up",
        "pos": "phrase",
        "ipa": "/swɑːt ʌp/",
        "vi": "cày cuốc ôn thi; nhồi nhét chữ",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043588",
        "hw": "texas longhorn",
        "pos": "phrase",
        "ipa": "/ˈtɛksəs ˈlɔːŋhɔːrn/",
        "vi": "giống bò sừng dài bang Texas Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043589",
        "hw": "thar desert",
        "pos": "phrase",
        "ipa": "/tɑːr ˈdɛzərt/",
        "vi": "sa mạc cát Thar biên giới Ấn Độ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043590",
        "hw": "theory of gravitation",
        "pos": "phrase",
        "ipa": "/ˈθiːəri əv ˌɡrævɪˈteɪʃən/",
        "vi": "thuyết vạn vật hấp dẫn vật lý",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043591",
        "hw": "thermonuclear reaction",
        "pos": "phrase",
        "ipa": "/ˌθɜːrmoʊˈnuːkliər riˈækʃən/",
        "vi": "phản ứng nhiệt hạch tổng hợp hạt",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043592",
        "hw": "thomas alva edison",
        "pos": "phrase",
        "ipa": "/ˈtɑːməs ˈælvə ˈɛdɪsən/",
        "vi": "nhà phát minh Thomas Alva Edison",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043593",
        "hw": "toasting fork",
        "pos": "phrase",
        "ipa": "/ˈtoʊstɪŋ fɔːrk/",
        "vi": "dĩa dài nướng bánh mì xúc xích lò",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043594",
        "hw": "trumpeter swan",
        "pos": "phrase",
        "ipa": "/ˈtrʌmpɪtər swɑːn/",
        "vi": "chim thiên nga kèn lông trắng tinh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043595",
        "hw": "turkic language",
        "pos": "phrase",
        "ipa": "/ˈtɜːrkɪk ˈlæŋɡwɪdʒ/",
        "vi": "nhánh ngôn ngữ ngữ hệ Turk cổ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043596",
        "hw": "unsaturated fatty acid",
        "pos": "phrase",
        "ipa": "/ʌnˈsætʃəreɪtɪd ˈfæti ˈæsɪd/",
        "vi": "axit béo chưa bão hòa có lợi",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043597",
        "hw": "water plantain",
        "pos": "phrase",
        "ipa": "/ˈwɔːtər ˈplæntɪn/",
        "vi": "cây trạch tả mọc dưới đầm lầy",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043598",
        "hw": "webbing clothes moth",
        "pos": "phrase",
        "ipa": "/ˈwɛbɪŋ kloʊðz mɔːθ/",
        "vi": "sâu bướm ăn vải vóc quần áo len",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043599",
        "hw": "white honeysuckle",
        "pos": "phrase",
        "ipa": "/waɪt ˈhʌniˌsʌkl/",
        "vi": "hoa kim ngân trắng thơm ngào ngạt",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043600",
        "hw": "wide wale",
        "pos": "phrase",
        "ipa": "/waɪd weɪl/",
        "vi": "loại vải nhung có đường gân to bản",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043601",
        "hw": "william ralph inge",
        "pos": "phrase",
        "ipa": "/ˈwɪljəm rælf ɪndʒ/",
        "vi": "học giả giám mục William R. Inge",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r08_raw_p1.json') as f:
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

with open('scratch/b29_r08_p1.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 8 Part 1 verified and written successfully.")
