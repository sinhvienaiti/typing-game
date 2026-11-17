import json

reviewed_items = [
    {
        "id": "lex.en.200k.043002",
        "hw": "thatch palm",
        "pos": "phrase",
        "ipa": "/θætʃ pɑːm/",
        "vi": "cây cọ lá dùng để lợp nhà",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043003",
        "hw": "thinning shears",
        "pos": "phrase",
        "ipa": "/ˈθɪnɪŋ ʃɪərz/",
        "vi": "kéo tỉa mỏng tóc chuyên dụng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043004",
        "hw": "thrush nightingale",
        "pos": "phrase",
        "ipa": "/θrʌʃ ˈnaɪtɪŋɡeɪl/",
        "vi": "chim họa mi hót họng trắng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043005",
        "hw": "triplet code",
        "pos": "phrase",
        "ipa": "/ˈtrɪplɪt koʊd/",
        "vi": "mã di truyền bộ ba bộ gen",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043006",
        "hw": "turkmen monetary unit",
        "pos": "phrase",
        "ipa": "/ˈtɜːrkmən ˈmʌnɪtɛri ˈjuːnɪt/",
        "vi": "đơn vị tiền tệ manat Turkmenistan",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043007",
        "hw": "ventricular aneurysm",
        "pos": "phrase",
        "ipa": "/vɛnˈtrɪkjələr ˈænjərɪzəm/",
        "vi": "chứng phình vách tâm thất tim",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043008",
        "hw": "white separatism",
        "pos": "phrase",
        "ipa": "/waɪt ˈsɛprətɪzəm/",
        "vi": "chủ nghĩa ly khai người da trắng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043009",
        "hw": "white snapdragon",
        "pos": "phrase",
        "ipa": "/waɪt ˈsnæpˌdræɡən/",
        "vi": "cây hoa mõm sói trắng dại",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043010",
        "hw": "wild snapdragon",
        "pos": "phrase",
        "ipa": "/waɪld ˈsnæpˌdræɡən/",
        "vi": "cây hoa mõm chó hoa dại vàng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043011",
        "hw": "yangtze river",
        "pos": "phrase",
        "ipa": "/ˈjæŋtsi ˈrɪvər/",
        "vi": "sông Dương Tử; Trường Giang",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043012",
        "hw": "yule log",
        "pos": "phrase",
        "ipa": "/juːl lɔːɡ/",
        "vi": "khúc gỗ bánh kem Giáng sinh",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043013",
        "hw": "almanacs",
        "pos": "noun",
        "ipa": "/ˈɔːlmənæks/",
        "vi": "những cuốn niên giám niên lịch",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043014",
        "hw": "analyzers",
        "pos": "noun",
        "ipa": "/ˈænəlaɪzərz/",
        "vi": "các máy phân tích dữ liệu kỹ thuật",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043015",
        "hw": "anesthetics",
        "pos": "noun",
        "ipa": "/ˌænəsˈθɛtɪks/",
        "vi": "các loại thuốc gây mê gây tê",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043016",
        "hw": "anglias",
        "pos": "noun",
        "ipa": "/ˈæŋɡliəz/",
        "vi": "các dòng xe Ford Anglia",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043017",
        "hw": "antioches",
        "pos": "noun",
        "ipa": "/ˈæntiˌɑːks/",
        "vi": "các thành phố cổ Antioch",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043018",
        "hw": "aquariuses",
        "pos": "noun",
        "ipa": "/əˈkwɛəriəsɪz/",
        "vi": "những người thuộc cung Bảo Bình",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043019",
        "hw": "ascots",
        "pos": "noun",
        "ipa": "/ˈæskəts/",
        "vi": "những chiếc khăn quàng cổ ascot",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043020",
        "hw": "beagles",
        "pos": "noun",
        "ipa": "/ˈbiːɡəlz/",
        "vi": "những chú chó săn thỏ giống Beagle",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043021",
        "hw": "capris",
        "pos": "noun",
        "ipa": "/kəˈpriːz/",
        "vi": "các kiểu quần lửng capri",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043022",
        "hw": "carthages",
        "pos": "noun",
        "ipa": "/ˈkɑːrθɪdʒɪz/",
        "vi": "các di tích thành cổ Carthage",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043023",
        "hw": "cauldrons",
        "pos": "noun",
        "ipa": "/ˈkɔːldrənz/",
        "vi": "những chiếc vạc lớn nấu kim loại",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043024",
        "hw": "chalets",
        "pos": "noun",
        "ipa": "/ʃæˈleɪz/",
        "vi": "những ngôi nhà gỗ vùng núi tuyết",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043025",
        "hw": "cleansers",
        "pos": "noun",
        "ipa": "/ˈklɛnzərz/",
        "vi": "các loại sữa rửa mặt; chất tẩy rửa",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043026",
        "hw": "clemenses",
        "pos": "noun",
        "ipa": "/ˈklɛmənsɪz/",
        "vi": "những người mang tên Clemens",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043027",
        "hw": "clippers",
        "pos": "noun",
        "ipa": "/ˈklɪpərz/",
        "vi": "những tông đơ cắt tóc; thuyền buồm",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043028",
        "hw": "coneys",
        "pos": "noun",
        "ipa": "/ˈkoʊniz/",
        "vi": "những con thỏ rừng châu Âu",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043029",
        "hw": "crts",
        "pos": "noun",
        "ipa": "/ˌsiː ɑːr ˈtiːz/",
        "vi": "các màn hình bóng đèn hình CRT",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043030",
        "hw": "deliberations",
        "pos": "noun",
        "ipa": "/dɪˌlɪbəˈreɪʃənz/",
        "vi": "những sự thảo luận cân nhắc kỹ",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043031",
        "hw": "dermatologists",
        "pos": "noun",
        "ipa": "/ˌdɜːrməˈtɑːlədʒɪsts/",
        "vi": "những bác sĩ chuyên khoa da liễu",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043032",
        "hw": "detonations",
        "pos": "noun",
        "ipa": "/ˌdɛtəˈneɪʃənz/",
        "vi": "những vụ nổ phá hủy dữ dội",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043033",
        "hw": "diodes",
        "pos": "noun",
        "ipa": "/ˈdaɪoʊdz/",
        "vi": "các bóng đi-ốt bán dẫn điện tử",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043034",
        "hw": "dixes",
        "pos": "noun",
        "ipa": "/ˈdɪksɪz/",
        "vi": "các nhà cải cách họ Dix",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043035",
        "hw": "downers",
        "pos": "noun",
        "ipa": "/ˈdaʊnərz/",
        "vi": "thuốc an thần gây ngủ; chuyện buồn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043036",
        "hw": "dreyfuses",
        "pos": "noun",
        "ipa": "/ˈdreɪfəsɪz/",
        "vi": "các nhân vật trong vụ án Dreyfus",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043037",
        "hw": "dutchmans",
        "pos": "noun",
        "ipa": "/ˈdʌtʃmənz/",
        "vi": "những người đàn ông Hà Lan",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043038",
        "hw": "endocrines",
        "pos": "noun",
        "ipa": "/ˈɛndoʊkrɪnz/",
        "vi": "các tuyến nội tiết trong cơ thể",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043039",
        "hw": "epis",
        "pos": "noun",
        "ipa": "/ˈɛpiz/",
        "vi": "các bút tiêm tự động epinephrine",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043040",
        "hw": "esters",
        "pos": "noun",
        "ipa": "/ˈɛstərz/",
        "vi": "các hợp chất hóa học este thơm",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043041",
        "hw": "fedoras",
        "pos": "noun",
        "ipa": "/fɪˈdɔːrəz/",
        "vi": "những chiếc mũ phớt rộng vành",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043042",
        "hw": "freys",
        "pos": "noun",
        "ipa": "/freɪz/",
        "vi": "các thành viên thuộc dòng họ Frey",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043043",
        "hw": "fuzzes",
        "pos": "noun",
        "ipa": "/ˈfʌzɪz/",
        "vi": "những lớp lông tơ mịn trên quả",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043044",
        "hw": "goodyears",
        "pos": "noun",
        "ipa": "/ˈɡʊdjɪərz/",
        "vi": "các lốp xe ô tô hãng Goodyear",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043045",
        "hw": "harlows",
        "pos": "noun",
        "ipa": "/ˈhɑːrloʊz/",
        "vi": "những người mang họ Harlow",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043046",
        "hw": "hearsts",
        "pos": "noun",
        "ipa": "/hɜːrsts/",
        "vi": "tập đoàn xuất bản gia đình Hearst",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043047",
        "hw": "horowitzes",
        "pos": "noun",
        "ipa": "/ˈhɔːrəwɪtsɪz/",
        "vi": "những nghệ sĩ piano họ Horowitz",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043048",
        "hw": "impalas",
        "pos": "noun",
        "ipa": "/ɪmˈpɑːləz/",
        "vi": "những con linh dương Impala đồng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043049",
        "hw": "irishmans",
        "pos": "noun",
        "ipa": "/ˈaɪrɪʃmənz/",
        "vi": "những người đàn ông Ireland",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043050",
        "hw": "islanders",
        "pos": "noun",
        "ipa": "/ˈaɪləndərz/",
        "vi": "những cư dân sinh sống trên đảo",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043051",
        "hw": "isms",
        "pos": "noun",
        "ipa": "/ˈɪzəmz/",
        "vi": "các học thuyết và trào lưu tư tưởng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043052",
        "hw": "lambdas",
        "pos": "noun",
        "ipa": "/ˈlæmdəz/",
        "vi": "những ký tự Hy Lạp lam-đa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043053",
        "hw": "leakier",
        "pos": "adj",
        "ipa": "/ˈliːkiər/",
        "vi": "dễ bị rò rỉ hơn; hở nước hơn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043054",
        "hw": "leakiest",
        "pos": "adj",
        "ipa": "/ˈliːkiəst/",
        "vi": "dễ bị rò rỉ nhất; hở nước nhất",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043055",
        "hw": "leicestershires",
        "pos": "noun",
        "ipa": "/ˈlɛstərʃɪərz/",
        "vi": "các vùng hạt Leicestershire Anh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043056",
        "hw": "letos",
        "pos": "noun",
        "ipa": "/ˈliːtoʊz/",
        "vi": "những hình tượng nữ thần Leto",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043057",
        "hw": "libidos",
        "pos": "noun",
        "ipa": "/lɪˈbiːdoʊz/",
        "vi": "các mức độ ham muốn dục vọng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043058",
        "hw": "lynchings",
        "pos": "noun",
        "ipa": "/ˈlɪntʃɪŋz/",
        "vi": "những vụ hành quyết kiểu lynch",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043059",
        "hw": "lynxes",
        "pos": "noun",
        "ipa": "/ˈlɪŋksɪz/",
        "vi": "những con mèo rừng linh miêu",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043060",
        "hw": "mahatmas",
        "pos": "noun",
        "ipa": "/məˈhɑːtməz/",
        "vi": "những bậc vĩ nhân tâm hồn cao cả",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043061",
        "hw": "mainstays",
        "pos": "noun",
        "ipa": "/ˈmeɪnsteɪz/",
        "vi": "những điểm tựa trụ cột then chốt",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043062",
        "hw": "mannequins",
        "pos": "noun",
        "ipa": "/ˈmænɪkɪnz/",
        "vi": "những con ma-nơ-canh trưng bày",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043063",
        "hw": "minivans",
        "pos": "noun",
        "ipa": "/ˈmɪnivænz/",
        "vi": "những chiếc xe ô tô chở khách nhỏ",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043064",
        "hw": "mistrusted",
        "pos": "verb",
        "ipa": "/mɪsˈtrʌstɪd/",
        "vi": "đã ngờ vực; không tin tưởng",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043065",
        "hw": "mistrusting",
        "pos": "verb",
        "ipa": "/mɪsˈtrʌstɪŋ/",
        "vi": "đang ngờ vực; hoài nghi lòng tin",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043066",
        "hw": "mistrusts",
        "pos": "noun",
        "ipa": "/mɪsˈtrʌsts/",
        "vi": "những mối nghi ngờ; ngờ vực",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043067",
        "hw": "monikers",
        "pos": "noun",
        "ipa": "/ˈmɑːnɪkərz/",
        "vi": "những biệt danh; tên hiệu đặt",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043068",
        "hw": "naves",
        "pos": "noun",
        "ipa": "/neɪvz/",
        "vi": "những gian chính giữa thánh đường",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043069",
        "hw": "nurembergs",
        "pos": "noun",
        "ipa": "/ˈnjʊərəmbɜːrɡz/",
        "vi": "các phiên tòa lịch sử Nuremberg",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043070",
        "hw": "pensacolas",
        "pos": "noun",
        "ipa": "/ˌpɛnsəˈkoʊləz/",
        "vi": "các căn cứ quân sự Pensacola",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043071",
        "hw": "polarities",
        "pos": "noun",
        "ipa": "/pəˈlærətiz/",
        "vi": "các cực tính; trạng thái đối cực",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043072",
        "hw": "profanities",
        "pos": "noun",
        "ipa": "/prəˈfænətiz/",
        "vi": "những lời chửi bới báng bổ thô tục",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043073",
        "hw": "reinvented",
        "pos": "verb",
        "ipa": "/ˌriːɪnˈvɛntɪd/",
        "vi": "đã tái tạo lại; làm mới hoàn toàn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043074",
        "hw": "reinventing",
        "pos": "verb",
        "ipa": "/ˌriːɪnˈvɛntɪŋ/",
        "vi": "đang tái tạo; đổi mới hoàn toàn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043075",
        "hw": "reinvents",
        "pos": "verb",
        "ipa": "/ˌriːɪnˈvɛnts/",
        "vi": "tái tạo sáng tạo lại diện mạo mới",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043076",
        "hw": "repatriations",
        "pos": "noun",
        "ipa": "/riːˌpætriˈeɪʃənz/",
        "vi": "các đợt hồi hương về nước định cư",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043077",
        "hw": "requiems",
        "pos": "noun",
        "ipa": "/ˈrɛkwiəmz/",
        "vi": "những bản thánh ca lễ cầu hồn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043078",
        "hw": "saris",
        "pos": "noun",
        "ipa": "/ˈsɑːriz/",
        "vi": "những bộ trang phục sari Ấn Độ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043079",
        "hw": "saucers",
        "pos": "noun",
        "ipa": "/ˈsɔːsərz/",
        "vi": "những chiếc đĩa nhỏ kê lót chén",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043080",
        "hw": "scrappier",
        "pos": "adj",
        "ipa": "/ˈskræpiər/",
        "vi": "hiếu chiến hơn; chắp vá vụn hơn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043081",
        "hw": "scrappiest",
        "pos": "adj",
        "ipa": "/ˈskræpiəst/",
        "vi": "hiếu chiến nhất; chắp vá nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043082",
        "hw": "spaniards",
        "pos": "noun",
        "ipa": "/ˈspænjərdz/",
        "vi": "những người dân Tây Ban Nha",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043083",
        "hw": "stimulants",
        "pos": "noun",
        "ipa": "/ˈstɪmjələnts/",
        "vi": "những chất kích thích thần kinh",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043084",
        "hw": "stricklands",
        "pos": "noun",
        "ipa": "/ˈstrɪkləndz/",
        "vi": "những người thuộc họ Strickland",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043085",
        "hw": "succumbed",
        "pos": "verb",
        "ipa": "/səˈkʌmd/",
        "vi": "đã đầu hàng; qua đời vì kiệt sức",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043086",
        "hw": "succumbing",
        "pos": "verb",
        "ipa": "/səˈkʌmɪŋ/",
        "vi": "đang khuất phục; ngã gục đầu hàng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043087",
        "hw": "succumbs",
        "pos": "verb",
        "ipa": "/səˈkʌmz/",
        "vi": "chịu khuất phục; đầu hàng trước",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043088",
        "hw": "suisses",
        "pos": "noun",
        "ipa": "/swiːsɪz/",
        "vi": "người Thụy Sĩ; ngân hàng Thụy Sĩ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043089",
        "hw": "susannas",
        "pos": "noun",
        "ipa": "/suːˈzænəz/",
        "vi": "những người mang tên Susanna",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043090",
        "hw": "talismans",
        "pos": "noun",
        "ipa": "/ˈtælɪsmənz/",
        "vi": "những lá bùa hộ mệnh may mắn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043091",
        "hw": "tortillas",
        "pos": "noun",
        "ipa": "/tɔːrˈtiːəz/",
        "vi": "những chiếc bánh ngô tortilla",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043092",
        "hw": "truffles",
        "pos": "noun",
        "ipa": "/ˈtrʌflz/",
        "vi": "những cây nấm củ truffle đắt đỏ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043093",
        "hw": "uncleaner",
        "pos": "adj",
        "ipa": "/ʌnˈkliːnər/",
        "vi": "kém vệ sinh hơn; ô uế bẩn thỉu hơn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043094",
        "hw": "uncleanest",
        "pos": "adj",
        "ipa": "/ʌnˈkliːnɪst/",
        "vi": "kém vệ sinh nhất; ô uế dơ bẩn nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043095",
        "hw": "valkyries",
        "pos": "noun",
        "ipa": "/vælˈkɪriz/",
        "vi": "những nữ thần chiến binh Valkyrie",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043096",
        "hw": "whiplashes",
        "pos": "noun",
        "ipa": "/ˈwɪplæʃɪz/",
        "vi": "những chấn thương gập cổ do va chạm",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043097",
        "hw": "wildcats",
        "pos": "noun",
        "ipa": "/ˈwaɪldkæts/",
        "vi": "mèo hoang dã; mỏ dầu khoan thăm dò",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043098",
        "hw": "wildcatted",
        "pos": "verb",
        "ipa": "/ˈwaɪldkætɪd/",
        "vi": "đã khoan thăm dò mỏ dầu rủi ro cao",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043099",
        "hw": "wildcatting",
        "pos": "verb",
        "ipa": "/ˈwaɪldkætɪŋ/",
        "vi": "đang khoan thăm dò dầu khí mạo hiểm",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043100",
        "hw": "absinthe oil",
        "pos": "phrase",
        "ipa": "/ˈæbsɪnθ ɔɪl/",
        "vi": "tinh dầu ngải tây nguyên chất",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043101",
        "hw": "accumulator register",
        "pos": "phrase",
        "ipa": "/əˈkjuːmjəleɪtər ˈrɛdʒɪstər/",
        "vi": "thanh ghi tích lũy bộ vi xử lý",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r07_raw_p1.json') as f:
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

with open('scratch/b29_r07_p1.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 7 Part 1 verified and written successfully.")
