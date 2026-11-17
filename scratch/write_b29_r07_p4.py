import json

reviewed_items = [
    {
        "id": "lex.en.200k.043302",
        "hw": "cardinal richelieu",
        "pos": "phrase",
        "ipa": "/ˈkɑːrdɪnl ˈrɪʃəljuː/",
        "vi": "Hồng y giáo chủ Richelieu Pháp",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043303",
        "hw": "carrion crow",
        "pos": "phrase",
        "ipa": "/ˈkæriən kroʊ/",
        "vi": "loài quạ đen ăn xác động vật",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043304",
        "hw": "casement window",
        "pos": "phrase",
        "ipa": "/ˈkeɪsmənt ˈwɪndoʊ/",
        "vi": "cửa sổ gắn bản lề mở ra ngoài",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043305",
        "hw": "cassava starch",
        "pos": "phrase",
        "ipa": "/kəˈsɑːvə stɑːrtʃ/",
        "vi": "tinh bột sắn; bột củ khoai mì",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043306",
        "hw": "caudal anesthesia",
        "pos": "phrase",
        "ipa": "/ˈkɔːdl ˌænəsˈθiːʒə/",
        "vi": "phương pháp gây tê vùng đuôi ngựa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043307",
        "hw": "charles augustus lindbergh",
        "pos": "phrase",
        "ipa": "/tʃɑːrlz ɔːˈɡʌstəs ˈlɪndbɜːrɡ/",
        "vi": "phi công Charles Lindbergh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043308",
        "hw": "claims adjuster",
        "pos": "phrase",
        "ipa": "/kleɪmz əˈdʒʌstər/",
        "vi": "giám định viên bồi thường bảo hiểm",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043309",
        "hw": "clara josephine schumann",
        "pos": "phrase",
        "ipa": "/ˈklɑːrə ˈdʒoʊzəfiːn ˈʃuːmɑːn/",
        "vi": "nghệ sĩ piano Clara Schumann",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043310",
        "hw": "coal scuttle",
        "pos": "phrase",
        "ipa": "/koʊl ˈskʌtl/",
        "vi": "thùng kim loại đựng than sưởi",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043311",
        "hw": "cognitive neuroscientist",
        "pos": "phrase",
        "ipa": "/ˈkɑːɡnətɪv ˈnjʊəroʊˌsaɪəntɪst/",
        "vi": "nhà khoa học thần kinh nhận thức",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043312",
        "hw": "cold gangrene",
        "pos": "phrase",
        "ipa": "/koʊld ˈɡæŋɡriːn/",
        "vi": "chứng hoại thư khô thiếu máu nuôi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043313",
        "hw": "common grape hyacinth",
        "pos": "phrase",
        "ipa": "/ˈkɑːmən ɡreɪp ˈhaɪəsɪnθ/",
        "vi": "hoa dạ lan hương quả nho tím biếc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043314",
        "hw": "cutaneous anthrax",
        "pos": "phrase",
        "ipa": "/kjuːˈteɪniəs ˈænθræks/",
        "vi": "bệnh than thể da do vi khuẩn",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043315",
        "hw": "de spinoza",
        "pos": "phrase",
        "ipa": "/də spɪˈnoʊzə/",
        "vi": "triết gia Baruch Spinoza Hà Lan",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043316",
        "hw": "dry gangrene",
        "pos": "phrase",
        "ipa": "/draɪ ˈɡæŋɡriːn/",
        "vi": "chứng hoại thư khô mô hoại tử",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043317",
        "hw": "elizabeth haldane",
        "pos": "phrase",
        "ipa": "/ɪˈlɪzəbəθ ˈhɔːldeɪn/",
        "vi": "tác giả Elizabeth Haldane",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043318",
        "hw": "extramarital sex",
        "pos": "phrase",
        "ipa": "/ˌɛkstrəˈmærɪtl sɛks/",
        "vi": "quan hệ tình dục ngoài giá thú",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043319",
        "hw": "fairy armadillo",
        "pos": "phrase",
        "ipa": "/ˈfɛəri ˌɑːrməˈdɪloʊ/",
        "vi": "loài tatu tiên hồng đào hang",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043320",
        "hw": "fete day",
        "pos": "phrase",
        "ipa": "/feɪt deɪ/",
        "vi": "ngày hội lễ hội kỷ niệm tưng bừng",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043321",
        "hw": "fibonacci sequence",
        "pos": "phrase",
        "ipa": "/ˌfɪbəˈnɑːtʃi ˈsiːkwəns/",
        "vi": "dãy số Fibonacci số học",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043322",
        "hw": "francis turner palgrave",
        "pos": "phrase",
        "ipa": "/ˈfrænsɪs ˈtɜːrnər ˈpælɡreɪv/",
        "vi": "nhà phê bình Francis Palgrave",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043323",
        "hw": "funeral pyre",
        "pos": "phrase",
        "ipa": "/ˈfjuːnərəl paɪər/",
        "vi": "giàn thiêu củi hỏa táng người chết",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043324",
        "hw": "gas gangrene",
        "pos": "phrase",
        "ipa": "/ɡæs ˈɡæŋɡriːn/",
        "vi": "chứng hoại thư sinh hơi kỵ khí",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043325",
        "hw": "genus poa",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs ˈpoʊə/",
        "vi": "chi thực vật cỏ hòa thảo Poa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043326",
        "hw": "giuseppe garibaldi",
        "pos": "phrase",
        "ipa": "/dʒuːˈzɛpi ˌɡærɪˈbɔːldi/",
        "vi": "vị anh hùng Giuseppe Garibaldi",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043327",
        "hw": "gregorian chant",
        "pos": "phrase",
        "ipa": "/ɡrɪˈɡɔːriən tʃænt/",
        "vi": "thánh ca bình ca Gregoriano cổ",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043328",
        "hw": "grope for",
        "pos": "phrase",
        "ipa": "/ɡroʊp fɔːr/",
        "vi": "mò mẫm tìm kiếm; dò dẫm trong tối",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043329",
        "hw": "harrier eagle",
        "pos": "phrase",
        "ipa": "/ˈhæriər ˈiːɡl/",
        "vi": "loài đại bàng săn rắn harrier",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043330",
        "hw": "hermit thrush",
        "pos": "phrase",
        "ipa": "/ˈhɜːrmɪt θrʌʃ/",
        "vi": "chim hoét ẩn sĩ giọng thánh thót",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043331",
        "hw": "herpes encephalitis",
        "pos": "phrase",
        "ipa": "/ˈhɜːrpiːz ɛnˌsɛfəˈlaɪtɪs/",
        "vi": "bệnh viêm não do virus herpes",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043332",
        "hw": "holy sepulchre",
        "pos": "phrase",
        "ipa": "/ˈhoʊli ˈsɛpəlkər/",
        "vi": "Nhà thờ Mộ Thánh Jerusalem",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043333",
        "hw": "horatio walpole",
        "pos": "phrase",
        "ipa": "/həˈreɪʃioʊ ˈwɔːlpoʊl/",
        "vi": "nhà văn Horatio Walpole",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043334",
        "hw": "hydrogen bromide",
        "pos": "phrase",
        "ipa": "/ˈhaɪdrədʒən ˈbroʊmaɪd/",
        "vi": "khí hydro bromua axit HBr",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043335",
        "hw": "hydroxyl radical",
        "pos": "phrase",
        "ipa": "/haɪˈdrɑːksəl ˈrædɪkl/",
        "vi": "gốc tự do hydroxyl phản ứng cao",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043336",
        "hw": "invasion of iwo",
        "pos": "phrase",
        "ipa": "/ɪnˈveɪʒən əv ˌiːwoʊ/",
        "vi": "chiến dịch đổ bộ đảo Iwo Jima",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043337",
        "hw": "jack william nicklaus",
        "pos": "phrase",
        "ipa": "/dʒæk ˈwɪljəm ˈnɪkləs/",
        "vi": "huyền thoại golf Jack Nicklaus",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043338",
        "hw": "john scott haldane",
        "pos": "phrase",
        "ipa": "/dʒɑːn skɑːt ˈhɔːldeɪn/",
        "vi": "nhà sinh lý học John S. Haldane",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043339",
        "hw": "joseph priestley",
        "pos": "phrase",
        "ipa": "/ˈdʒoʊzəf ˈpriːstli/",
        "vi": "nhà hóa học Joseph Priestley",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043340",
        "hw": "klamath falls",
        "pos": "phrase",
        "ipa": "/ˈklæməθ fɔːlz/",
        "vi": "thành phố thác Klamath Falls",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043341",
        "hw": "lake tanganyika",
        "pos": "phrase",
        "ipa": "/leɪk ˌtæŋɡənˈjiːkə/",
        "vi": "hồ nước ngọt sâu Tanganyika",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043342",
        "hw": "logarithmic scale",
        "pos": "phrase",
        "ipa": "/ˌlɑːɡəˈrɪðmɪk skeɪl/",
        "vi": "thang chia tỷ lệ logarit",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043343",
        "hw": "lower jawbone",
        "pos": "phrase",
        "ipa": "/ˈloʊər ˈdʒɔːboʊn/",
        "vi": "xương quai hàm dưới cơ thể",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043344",
        "hw": "mediterranean snapdragon",
        "pos": "phrase",
        "ipa": "/ˌmɛdətəˈreɪniən ˈsnæpˌdræɡən/",
        "vi": "hoa mõm sói Địa Trung Hải dại",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043345",
        "hw": "mesozoic era",
        "pos": "phrase",
        "ipa": "/ˌmɛzəˈzoʊɪk ˈɪərə/",
        "vi": "đại Trung sinh; thời đại khủng long",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043346",
        "hw": "mimosa bush",
        "pos": "phrase",
        "ipa": "/mɪˈmoʊsə bʊʃ/",
        "vi": "bụi cây hoa keo mimosa vàng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043347",
        "hw": "modified radical mastectomy",
        "pos": "phrase",
        "ipa": "/ˈmɑːdəfaɪd ˈrædɪkl mæˈstɛktəmi/",
        "vi": "cắt bỏ vú triệt căn biến đổi mới",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043348",
        "hw": "neva river",
        "pos": "phrase",
        "ipa": "/ˈneɪvə ˈrɪvər/",
        "vi": "dòng sông Neva chảy qua Nga",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043349",
        "hw": "old squaw",
        "pos": "phrase",
        "ipa": "/oʊld skwɔː/",
        "vi": "loài vịt biển đuôi dài bơi lặn",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043350",
        "hw": "ozark plateau",
        "pos": "phrase",
        "ipa": "/ˈoʊzɑːrk plæˈtoʊ/",
        "vi": "vùng cao nguyên Ozark núi đá",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043351",
        "hw": "pancho villa",
        "pos": "phrase",
        "ipa": "/ˈpɑːntʃoʊ ˈviːjə/",
        "vi": "nhà cách mạng Pancho Villa",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043352",
        "hw": "political commissar",
        "pos": "phrase",
        "ipa": "/pəˈlɪtɪkl ˈkɑːmɪsɑːr/",
        "vi": "chính ủy quân đội; chính trị viên",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043353",
        "hw": "potash alum",
        "pos": "phrase",
        "ipa": "/ˈpɑːtæʃ ˈæləm/",
        "vi": "phèn nhôm kali; phèn chua lọc nước",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043354",
        "hw": "potato wart fungus",
        "pos": "phrase",
        "ipa": "/pəˈteɪtoʊ wɔːrt ˈfʌŋɡəs/",
        "vi": "nấm gây bệnh sùi mào củ khoai tây",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043355",
        "hw": "practice bundling",
        "pos": "phrase",
        "ipa": "/ˈpræktɪs ˈbʌndlɪŋ/",
        "vi": "tục ngủ chung giường giữ gìn xưa",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043356",
        "hw": "prescriptive linguistics",
        "pos": "phrase",
        "ipa": "/prɪˈskrɪptɪv lɪŋˈɡwɪstɪks/",
        "vi": "ngôn ngữ học quy phạm chuẩn mực",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043357",
        "hw": "primus stove",
        "pos": "phrase",
        "ipa": "/ˈpraɪməs stoʊv/",
        "vi": "bếp dầu du lịch dã ngoại Primus",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043358",
        "hw": "protease inhibitor",
        "pos": "phrase",
        "ipa": "/ˈproʊtiˌeɪs ɪnˈhɪbɪtər/",
        "vi": "thuốc ức chế enzym men protease",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043359",
        "hw": "rebecca rolfe",
        "pos": "phrase",
        "ipa": "/rɪˈbɛkə rɑːlf/",
        "vi": "nàng Pocahontas Rebecca Rolfe",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043360",
        "hw": "richard feynman",
        "pos": "phrase",
        "ipa": "/ˈrɪtʃərd ˈfaɪnmən/",
        "vi": "nhà vật lý Richard Feynman tài ba",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043361",
        "hw": "scaly fern",
        "pos": "phrase",
        "ipa": "/ˈskeɪli fɜːrn/",
        "vi": "cây dương xỉ có vảy rỉ sắt",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043362",
        "hw": "scrub palmetto",
        "pos": "phrase",
        "ipa": "/skrʌb pælˈmɛtoʊ/",
        "vi": "cây cọ lùn bụi rậm mọc thấp",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043363",
        "hw": "selkirk mountains",
        "pos": "phrase",
        "ipa": "/ˈsɛlkɜːrk ˈmaʊntənz/",
        "vi": "dãy núi đá phủ tuyết Selkirk",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043364",
        "hw": "slop jar",
        "pos": "phrase",
        "ipa": "/slɑːp dʒɑːr/",
        "vi": "bô đựng nước tiểu nước thải xưa",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043365",
        "hw": "sonora lac",
        "pos": "phrase",
        "ipa": "/səˈnɔːrə læk/",
        "vi": "nhựa cánh kiến vùng Sonora",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043366",
        "hw": "spinal anaesthesia",
        "pos": "phrase",
        "ipa": "/ˈspaɪnl ˌænəsˈθiːʒə/",
        "vi": "phương pháp gây tê tủy sống y khoa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043367",
        "hw": "squaw man",
        "pos": "phrase",
        "ipa": "/skwɔː mæn/",
        "vi": "người da trắng lấy vợ bản địa Mỹ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043368",
        "hw": "squirting cucumber",
        "pos": "phrase",
        "ipa": "/ˈskwɜːrtɪŋ ˈkjuːkʌmbər/",
        "vi": "cây dưa chuột phun hạt khi chín",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043369",
        "hw": "striptease artist",
        "pos": "phrase",
        "ipa": "/ˈstrɪptiːz ˈɑːrtɪst/",
        "vi": "nghệ sĩ vũ công múa thoát y",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043370",
        "hw": "suckling reflex",
        "pos": "phrase",
        "ipa": "/ˈsʌklɪŋ ˈriːflɛks/",
        "vi": "phản xạ bú mẹ tự nhiên ở trẻ con",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043371",
        "hw": "tassel flower",
        "pos": "phrase",
        "ipa": "/ˈtæsl ˈflaʊər/",
        "vi": "hoa cúc tua đỏ; hoa đuôi sóc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043372",
        "hw": "thoracic aorta",
        "pos": "phrase",
        "ipa": "/θɔːˈræsɪk eɪˈɔːrtə/",
        "vi": "đoạn động mạch chủ ngực giải phẫu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043373",
        "hw": "tinned goods",
        "pos": "phrase",
        "ipa": "/tɪnd ɡʊdz/",
        "vi": "các loại hàng hóa đồ hộp kim loại",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043374",
        "hw": "tinned meat",
        "pos": "phrase",
        "ipa": "/tɪnd miːt/",
        "vi": "thịt hộp đóng hộp tiệt trùng",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043375",
        "hw": "upper jawbone",
        "pos": "phrase",
        "ipa": "/ˈʌpər ˈdʒɔːboʊn/",
        "vi": "xương hàm trên giải phẫu sọ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043376",
        "hw": "uruguayan peso",
        "pos": "phrase",
        "ipa": "/ˌjʊərəˈɡwaɪən ˈpeɪsoʊ/",
        "vi": "đồng peso tiền tệ Uruguay",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043377",
        "hw": "virginian stock",
        "pos": "phrase",
        "ipa": "/vərˈdʒɪniən stɑːk/",
        "vi": "cây hoa cúc dại bang Virginia",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043378",
        "hw": "webbing moth",
        "pos": "phrase",
        "ipa": "/ˈwɛbɪŋ mɔːθ/",
        "vi": "con sâu bướm cắn phá quần áo len",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043379",
        "hw": "werner karl heisenberg",
        "pos": "phrase",
        "ipa": "/ˈvɛrnər kɑːrl ˈhaɪzənbɜːrɡ/",
        "vi": "nhà vật lý Werner Heisenberg",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043380",
        "hw": "west berliner",
        "pos": "phrase",
        "ipa": "/wɛst ˌbɜːrlɪˈnər/",
        "vi": "người dân khu vực Tây Berlin",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043381",
        "hw": "west virginian",
        "pos": "phrase",
        "ipa": "/wɛst vərˈdʒɪniən/",
        "vi": "cư dân bang Tây Virginia nước Mỹ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043382",
        "hw": "william henry beveridge",
        "pos": "phrase",
        "ipa": "/ˈwɪljəm ˈhɛnri ˈbɛvərɪdʒ/",
        "vi": "kinh tế gia William Beveridge",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043383",
        "hw": "xerxes the great",
        "pos": "phrase",
        "ipa": "/ˈzɜːrksiːz ðə ɡreɪt/",
        "vi": "Hoàng đế Ba Tư Xerxes Đại đế",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043384",
        "hw": "young carnivore",
        "pos": "phrase",
        "ipa": "/jʌŋ ˈkɑːrnɪvɔːr/",
        "vi": "thú non của loài ăn thịt hoang dã",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043385",
        "hw": "accras",
        "pos": "noun",
        "ipa": "/əˈkrɑːz/",
        "vi": "các món bánh rán đậu cá chiên accra",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043386",
        "hw": "acquittals",
        "pos": "noun",
        "ipa": "/əˈkwɪtəlz/",
        "vi": "các phán quyết tuyên bố trắng án",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043387",
        "hw": "anvils",
        "pos": "noun",
        "ipa": "/ˈænvɪlz/",
        "vi": "những chiếc đe rèn kim loại nặng",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043388",
        "hw": "anzacs",
        "pos": "noun",
        "ipa": "/ˈænzæks/",
        "vi": "những người lính liên quân ANZAC",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043389",
        "hw": "argoses",
        "pos": "noun",
        "ipa": "/ˈɑːrɡəsɪz/",
        "vi": "các thành bang cổ đại Argos",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043390",
        "hw": "armaments",
        "pos": "noun",
        "ipa": "/ˈɑːrməmənts/",
        "vi": "các loại vũ khí khí tài quân sự",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043391",
        "hw": "bastilles",
        "pos": "noun",
        "ipa": "/bæˈstiːlz/",
        "vi": "những pháo đài ngục tối Bastille",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043392",
        "hw": "bloomfields",
        "pos": "noun",
        "ipa": "/ˈbluːmfiːldz/",
        "vi": "các khu định cư thị trấn Bloomfield",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043393",
        "hw": "buntings",
        "pos": "noun",
        "ipa": "/ˈbʌntɪŋz/",
        "vi": "dây cờ đuôi nheo trang trí; chim sẻ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043394",
        "hw": "caballed",
        "pos": "verb",
        "ipa": "/kəˈbæld/",
        "vi": "đã bí mật cấu kết mưu đồ phái",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043395",
        "hw": "caballing",
        "pos": "verb",
        "ipa": "/kəˈbælɪŋ/",
        "vi": "đang cấu kết bè cánh mưu toan ngầm",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043396",
        "hw": "cabals",
        "pos": "noun",
        "ipa": "/kəˈbælz/",
        "vi": "những phe cánh mưu đồ chính trị",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043397",
        "hw": "cadres",
        "pos": "noun",
        "ipa": "/ˈkædriz/",
        "vi": "những đội ngũ cán bộ nòng cốt",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043398",
        "hw": "campgrounds",
        "pos": "noun",
        "ipa": "/ˈkæmpɡraʊndz/",
        "vi": "những khu vực bãi cắm trại dã ngoại",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043399",
        "hw": "canaans",
        "pos": "noun",
        "ipa": "/ˈkeɪnənz/",
        "vi": "vùng đất hứa Ca-na-an trong Kinh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043400",
        "hw": "causeways",
        "pos": "noun",
        "ipa": "/ˈkɔːzweɪz/",
        "vi": "những con đường đắp cao vượt đầm",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043401",
        "hw": "cobs",
        "pos": "noun",
        "ipa": "/kɑːbz/",
        "vi": "những lõi bắp ngô; giống ngựa lùn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r07_raw_p4.json') as f:
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

with open('scratch/b29_r07_p4.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 7 Part 4 verified and written successfully.")
