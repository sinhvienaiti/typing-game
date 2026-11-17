import json

reviewed_items = [
    {
        "id": "lex.en.200k.043402",
        "hw": "coinages",
        "pos": "noun",
        "ipa": "/ˈkɔɪnɪdʒɪz/",
        "vi": "tiền đúc kim loại; việc tạo từ mới",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043403",
        "hw": "decadents",
        "pos": "noun",
        "ipa": "/ˈdɛkədənts/",
        "vi": "những kẻ đồi trụy sa đọa suy thoái",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043404",
        "hw": "decoyed",
        "pos": "verb",
        "ipa": "/dɪˈkɔɪd/",
        "vi": "đã dụ dỗ vào bẫy; đánh lừa",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043405",
        "hw": "decoying",
        "pos": "verb",
        "ipa": "/dɪˈkɔɪɪŋ/",
        "vi": "đang dụ vào tròng; gài bẫy lừa",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043406",
        "hw": "decoys",
        "pos": "noun",
        "ipa": "/ˈdiːkɔɪz/",
        "vi": "những con mồi nhử; chim mồi giả",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043407",
        "hw": "derivations",
        "pos": "noun",
        "ipa": "/ˌdɛrəˈveɪʃənz/",
        "vi": "nguồn gốc từ ngữ; sự dẫn xuất hóa",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043408",
        "hw": "dracos",
        "pos": "noun",
        "ipa": "/ˈdreɪkoʊz/",
        "vi": "các loài thằn lằn bay Draco rừng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043409",
        "hw": "emulations",
        "pos": "noun",
        "ipa": "/ˌɛmjuˈleɪʃənz/",
        "vi": "những phong trào thi đua phấn đấu",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043410",
        "hw": "escrows",
        "pos": "noun",
        "ipa": "/ˈɛskroʊz/",
        "vi": "các tài khoản ký quỹ trung gian",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043411",
        "hw": "fases",
        "pos": "noun",
        "ipa": "/ˈfæsɪz/",
        "vi": "các hội chứng ngộ độc rượu bào thai",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043412",
        "hw": "fayettevilles",
        "pos": "noun",
        "ipa": "/ˈfeɪətvɪlz/",
        "vi": "các thành phố địa danh Fayetteville",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043413",
        "hw": "federalists",
        "pos": "noun",
        "ipa": "/ˈfɛdərəˌlɪsts/",
        "vi": "những người theo phái liên bang",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043414",
        "hw": "femas",
        "pos": "noun",
        "ipa": "/ˈfiːməz/",
        "vi": "các đội cơ quan cứu trợ khẩn FEMA",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043415",
        "hw": "fixers",
        "pos": "noun",
        "ipa": "/ˈfɪksərz/",
        "vi": "những kẻ dàn xếp ngầm; thợ sửa chữa",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043416",
        "hw": "forayed",
        "pos": "verb",
        "ipa": "/fɔːˈreɪd/",
        "vi": "đã mở cuộc đột kích; thâm nhập",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043417",
        "hw": "foraying",
        "pos": "verb",
        "ipa": "/fɔːˈreɪɪŋ/",
        "vi": "đang đột kích; dấn thân thử sức",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043418",
        "hw": "forays",
        "pos": "noun",
        "ipa": "/ˈfɔːreɪz/",
        "vi": "cuộc đột kích; sự lấn sân ngành",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043419",
        "hw": "forfeitures",
        "pos": "noun",
        "ipa": "/ˈfɔːrfətʃərz/",
        "vi": "sự tịch thu tang vật; tài sản mất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043420",
        "hw": "friars",
        "pos": "noun",
        "ipa": "/ˈfraɪərz/",
        "vi": "những tu sĩ dòng hành khất tu trì",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043421",
        "hw": "fussier",
        "pos": "adj",
        "ipa": "/ˈfʌsiər/",
        "vi": "cầu kỳ kiểu cách hơn; khó tính hơn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043422",
        "hw": "fussiest",
        "pos": "adj",
        "ipa": "/ˈfʌsiəst/",
        "vi": "cầu kỳ nhất; khó tính khó chiều",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043423",
        "hw": "gnus",
        "pos": "noun",
        "ipa": "/nuːz/",
        "vi": "những con linh dương đầu bò hoang",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043424",
        "hw": "goodies",
        "pos": "noun",
        "ipa": "/ˈɡʊdiz/",
        "vi": "món ăn vặt thơm ngon; điều bổ ích",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043425",
        "hw": "grasslands",
        "pos": "noun",
        "ipa": "/ˈɡræslændz/",
        "vi": "những vùng thảo nguyên đồng cỏ rộng",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043426",
        "hw": "hajjes",
        "pos": "noun",
        "ipa": "/ˈhædʒɪz/",
        "vi": "các cuộc hành hương Hajj về Mecca",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043427",
        "hw": "hersheys",
        "pos": "noun",
        "ipa": "/ˈhɜːrʃiz/",
        "vi": "những thanh kẹo sô-cô-la Hershey",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043428",
        "hw": "hideouts",
        "pos": "noun",
        "ipa": "/ˈhaɪdaʊts/",
        "vi": "những nơi ẩn náu bí mật an toàn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043429",
        "hw": "hobbeses",
        "pos": "noun",
        "ipa": "/ˈhɑːbzɪz/",
        "vi": "tác phẩm triết học của nhà Hobbes",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043430",
        "hw": "hutches",
        "pos": "noun",
        "ipa": "/ˈhʌtʃɪz/",
        "vi": "những chiếc chuồng nuôi thỏ bằng gỗ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043431",
        "hw": "instalments",
        "pos": "noun",
        "ipa": "/ɪnˈstɔːlmənts/",
        "vi": "các khoản tiền trả góp định kỳ; kỳ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043432",
        "hw": "jetties",
        "pos": "noun",
        "ipa": "/ˈdʒɛtiz/",
        "vi": "những bờ kè đá chắn sóng; cầu tàu",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043433",
        "hw": "koalas",
        "pos": "noun",
        "ipa": "/koʊˈɑːləz/",
        "vi": "những chú gấu túi koala nước Úc",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043434",
        "hw": "koses",
        "pos": "noun",
        "ipa": "/ˈkoʊsɪz/",
        "vi": "những đơn vị đo chiều dài kos cổ Ấn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043435",
        "hw": "lorens",
        "pos": "noun",
        "ipa": "/ˈlɔːrənz/",
        "vi": "hình ảnh minh tinh Sophia Loren",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043436",
        "hw": "merles",
        "pos": "noun",
        "ipa": "/mɜːrlz/",
        "vi": "những con chim hoét đen châu Âu",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043437",
        "hw": "monochromes",
        "pos": "noun",
        "ipa": "/ˈmɑːnəˌkroʊmz/",
        "vi": "những bức ảnh tranh vẽ đơn sắc",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043438",
        "hw": "mortuaries",
        "pos": "noun",
        "ipa": "/ˈmɔːrtʃuɛriz/",
        "vi": "những nhà bảo quản thi hài nhà xác",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043439",
        "hw": "neumanns",
        "pos": "noun",
        "ipa": "/ˈnɔɪmənz/",
        "vi": "công trình của nhà toán học Neumann",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043440",
        "hw": "neurologists",
        "pos": "noun",
        "ipa": "/njʊˈrɑːlədʒɪsts/",
        "vi": "những bác sĩ chuyên khoa thần kinh",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043441",
        "hw": "nutmegs",
        "pos": "noun",
        "ipa": "/ˈnʌtmɛɡz/",
        "vi": "những hạt nhục đậu khấu làm gia vị",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043442",
        "hw": "obtuser",
        "pos": "adj",
        "ipa": "/əbˈtuːsər/",
        "vi": "đần độn chậm hiểu hơn; tù góc hơn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043443",
        "hw": "obtusest",
        "pos": "adj",
        "ipa": "/əbˈtuːsɪst/",
        "vi": "đần độn chậm hiểu nhất; tù nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043444",
        "hw": "particulates",
        "pos": "noun",
        "ipa": "/pɑːrˈtɪkjələts/",
        "vi": "các hạt bụi mịn lơ lửng không khí",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043445",
        "hw": "petals",
        "pos": "noun",
        "ipa": "/ˈpɛtlz/",
        "vi": "những cánh hoa mỏng manh khoe sắc",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043446",
        "hw": "pmses",
        "pos": "noun",
        "ipa": "/ˌpiː ɛm ˈɛsɪz/",
        "vi": "các cơn hội chứng tiền kinh nguyệt",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043447",
        "hw": "polygons",
        "pos": "noun",
        "ipa": "/ˈpɑːliɡɑːnz/",
        "vi": "hình đa giác trong hình học không",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043448",
        "hw": "provences",
        "pos": "noun",
        "ipa": "/prəˈvɑːnsɪz/",
        "vi": "phong cảnh vùng thảo mộc Provence",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043449",
        "hw": "purcells",
        "pos": "noun",
        "ipa": "/ˈpɜːrsəlz/",
        "vi": "những bản nhạc của Henry Purcell",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043450",
        "hw": "quartermasters",
        "pos": "noun",
        "ipa": "/ˈkwɔːrtərmæstərz/",
        "vi": "những sĩ quan hậu cần quân nhu",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043451",
        "hw": "rupees",
        "pos": "noun",
        "ipa": "/ruːˈpiːz/",
        "vi": "những đồng tiền rupee Ấn Độ, Nepal",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043452",
        "hw": "scrabbled",
        "pos": "verb",
        "ipa": "/ˈskræbld/",
        "vi": "đã cào bới loạn; mò mẫm tranh thủ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043453",
        "hw": "scrabbles",
        "pos": "noun",
        "ipa": "/ˈskræblz/",
        "vi": "các ván cờ chữ ghép từ Scrabble",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043454",
        "hw": "scrabbling",
        "pos": "verb",
        "ipa": "/ˈskræblɪŋ/",
        "vi": "đang cào cấu mò mẫm; lục lọi tìm",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043455",
        "hw": "seaboards",
        "pos": "noun",
        "ipa": "/ˈsiːbɔːrdz/",
        "vi": "những dải duyên hải ven biển dài",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043456",
        "hw": "shoddier",
        "pos": "adj",
        "ipa": "/ˈʃɑːdiər/",
        "vi": "chất lượng tồi tàn hơn; cẩu thả hơn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043457",
        "hw": "shoddiest",
        "pos": "adj",
        "ipa": "/ˈʃɑːdiɪst/",
        "vi": "chất lượng kém nhất; tệ hại nhất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043458",
        "hw": "shortstops",
        "pos": "noun",
        "ipa": "/ˈʃɔːrtstɑːps/",
        "vi": "những cầu thủ chặn ngắn bóng chày",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043459",
        "hw": "sleazier",
        "pos": "adj",
        "ipa": "/ˈsliːziər/",
        "vi": "nhơ nhớp bỉ ổi hơn; đồi bại hơn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043460",
        "hw": "sleaziest",
        "pos": "adj",
        "ipa": "/ˈsliːziəst/",
        "vi": "nhơ nhớp bỉ ổi nhất; đồi bại nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043461",
        "hw": "sociologists",
        "pos": "noun",
        "ipa": "/ˌsoʊsiˈɑːlədʒɪsts/",
        "vi": "những nhà nghiên cứu xã hội học",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043462",
        "hw": "squishier",
        "pos": "adj",
        "ipa": "/ˈskwɪʃiər/",
        "vi": "mềm nhũn ướt át hơn; dễ bẹp hơn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043463",
        "hw": "squishiest",
        "pos": "adj",
        "ipa": "/ˈskwɪʃiəst/",
        "vi": "mềm nhũn ướt át nhất; dễ bẹp nhất",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043464",
        "hw": "streetcars",
        "pos": "noun",
        "ipa": "/ˈstriːtkɑːrz/",
        "vi": "toa xe điện chạy trên ray đường",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043465",
        "hw": "stringers",
        "pos": "noun",
        "ipa": "/ˈstrɪŋərz/",
        "vi": "cộng tác viên báo chí; thanh xà dọc",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043466",
        "hw": "swamies",
        "pos": "noun",
        "ipa": "/ˈswɑːmiz/",
        "vi": "những bậc đạo sư tâm linh swami",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043467",
        "hw": "swamis",
        "pos": "noun",
        "ipa": "/ˈswɑːmiz/",
        "vi": "các vị đạo sư tu sĩ Ấn Độ giáo",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043468",
        "hw": "tahitis",
        "pos": "noun",
        "ipa": "/təˈhiːtiz/",
        "vi": "các hòn đảo nhiệt đới Tahiti",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043469",
        "hw": "tarantinos",
        "pos": "noun",
        "ipa": "/ˌtærənˈtiːnoʊz/",
        "vi": "các phong cách phim ảnh Tarantino",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043470",
        "hw": "tarmacked",
        "pos": "verb",
        "ipa": "/ˈtɑːrmækd/",
        "vi": "đã trải nhựa đường; rải thảm đá",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043471",
        "hw": "tarmacking",
        "pos": "verb",
        "ipa": "/ˈtɑːrmækɪŋ/",
        "vi": "đang trải thảm nhựa đường băng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043472",
        "hw": "tarmacs",
        "pos": "noun",
        "ipa": "/ˈtɑːrmæks/",
        "vi": "những đường băng sân bay trải nhựa",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043473",
        "hw": "troves",
        "pos": "noun",
        "ipa": "/troʊvz/",
        "vi": "những kho tàng tri thức; kho báu",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043474",
        "hw": "unpacking",
        "pos": "verb",
        "ipa": "/ʌnˈpækɪŋ/",
        "vi": "đang mở vali dỡ đồ; phân tích kỹ",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043475",
        "hw": "unpacks",
        "pos": "verb",
        "ipa": "/ʌnˈpæks/",
        "vi": "mở gói hàng; phân tích rành mạch",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043476",
        "hw": "wainwrights",
        "pos": "noun",
        "ipa": "/ˈweɪnraɪts/",
        "vi": "những người thợ đóng sửa xe ngựa",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043477",
        "hw": "wiltons",
        "pos": "noun",
        "ipa": "/ˈwɪltənz/",
        "vi": "các loại thảm dệt nhung Wilton",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043478",
        "hw": "winched",
        "pos": "verb",
        "ipa": "/wɪntʃt/",
        "vi": "đã dùng tời cơ học kéo lên cao",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043479",
        "hw": "winches",
        "pos": "noun",
        "ipa": "/ˈwɪntʃɪz/",
        "vi": "những chiếc máy tời cáp quay tay",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043480",
        "hw": "winching",
        "pos": "verb",
        "ipa": "/ˈwɪntʃɪŋ/",
        "vi": "đang vận hành kéo tời dây cáp",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043481",
        "hw": "workstations",
        "pos": "noun",
        "ipa": "/ˈwɜːrksteɪʃənz/",
        "vi": "các máy trạm; trạm làm việc lớn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043482",
        "hw": "yams",
        "pos": "noun",
        "ipa": "/jæmz/",
        "vi": "những củ mỡ; củ khoai từ dẻo bùi",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043483",
        "hw": "yolks",
        "pos": "noun",
        "ipa": "/joʊks/",
        "vi": "những lòng đỏ quả trứng gà vịt",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043484",
        "hw": "albert speer",
        "pos": "phrase",
        "ipa": "/ˈælbərt ʃpeɪr/",
        "vi": "kiến trúc sư Albert Speer Đức",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043485",
        "hw": "alexandre dumas",
        "pos": "phrase",
        "ipa": "/ˌælɪɡˈzændər duːˈmɑː/",
        "vi": "đại văn hào Alexandre Dumas cha",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043486",
        "hw": "alto saxophonist",
        "pos": "phrase",
        "ipa": "/ˈæltoʊ sækˈsɑːfənɪst/",
        "vi": "nghệ sĩ kèn xắc-xô-phôn alto",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043487",
        "hw": "american fly honeysuckle",
        "pos": "phrase",
        "ipa": "/əˈmɛrɪkən flaɪ ˈhʌniˌsʌkl/",
        "vi": "cây kim ngân ruồi Bắc Mỹ hoa vàng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043488",
        "hw": "anterior jugular vein",
        "pos": "phrase",
        "ipa": "/ænˈtɪəriər ˈdʒʌɡjələr veɪn/",
        "vi": "tĩnh mạch cảnh trước giải phẫu cổ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043489",
        "hw": "anton chekhov",
        "pos": "phrase",
        "ipa": "/ˈæntɑːn ˈtʃɛkɔːf/",
        "vi": "đại văn hào Nga Anton Chekhov",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043490",
        "hw": "apple dumpling",
        "pos": "phrase",
        "ipa": "/ˈæpl ˈdʌmplɪŋ/",
        "vi": "bánh táo bọc bột nướng giòn ngọt",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043491",
        "hw": "asbestos abatement",
        "pos": "phrase",
        "ipa": "/æsˈbɛstəs əˈbeɪtmənt/",
        "vi": "biện pháp xử lý giảm độc amiăng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043492",
        "hw": "australian honeysuckle",
        "pos": "phrase",
        "ipa": "/ɔːˈstreɪliən ˈhʌniˌsʌkl/",
        "vi": "cây hoa kim ngân bản địa nước Úc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043493",
        "hw": "baptismal name",
        "pos": "phrase",
        "ipa": "/bæpˈtɪzməl neɪm/",
        "vi": "tên thánh; tên đặt lúc rửa tội",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043494",
        "hw": "benjamin disraeli",
        "pos": "phrase",
        "ipa": "/ˈbɛndʒəmɪn dɪzˈreɪli/",
        "vi": "thủ tướng Benjamin Disraeli Anh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043495",
        "hw": "benthic division",
        "pos": "phrase",
        "ipa": "/ˈbɛnθɪk dɪˈvɪʒən/",
        "vi": "vùng phân bố sinh vật tầng đáy biển",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043496",
        "hw": "bilge water",
        "pos": "phrase",
        "ipa": "/bɪldʒ ˈwɔːtər/",
        "vi": "nước đọng hôi thối dưới đáy tàu",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043497",
        "hw": "bilge well",
        "pos": "phrase",
        "ipa": "/bɪldʒ wɛl/",
        "vi": "hố thu nước đáy tàu khoang máy",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043498",
        "hw": "biohazard suit",
        "pos": "phrase",
        "ipa": "/ˈbaɪoʊˌhæzərd suːt/",
        "vi": "bộ đồ bảo hộ chống nguy cơ sinh học",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043499",
        "hw": "bladder campion",
        "pos": "phrase",
        "ipa": "/ˈblædər ˈkæmpiən/",
        "vi": "cây cúc campion đài hoa phồng to",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043500",
        "hw": "bold fmri",
        "pos": "phrase",
        "ipa": "/boʊld ˌɛf ɛm ɑːr ˈaɪ/",
        "vi": "chụp cộng hưởng từ chức năng BOLD",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043501",
        "hw": "bolo knife",
        "pos": "phrase",
        "ipa": "/ˈboʊloʊ naɪf/",
        "vi": "con dao quắm cán gỗ phát cỏ bolo",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r07_raw_p5.json') as f:
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

with open('scratch/b29_r07_p5.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 7 Part 5 verified and written successfully.")
