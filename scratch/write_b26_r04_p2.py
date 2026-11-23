import json

# Batch 26 Round 4 Part 2 (lex.en.200k.026602 to lex.en.200k.026701)
records = [
    {
        "id": "lex.en.200k.026602",
        "hw": "argentine monetary unit",
        "pos": "phrase",
        "ipa": "/ɑːr.dʒənˈtiːn ˈmɑː.nə.teri ˈjuː.nɪt/",
        "vi": "đơn vị tiền tệ Argentina",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026603",
        "hw": "asian influenza",
        "pos": "phrase",
        "ipa": "/ˈeɪ.ʒən ˌɪn.fluˈen.zə/",
        "vi": "bệnh cúm châu Á",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026604",
        "hw": "assemblies of god",
        "pos": "phrase",
        "ipa": "/əˈsem.bliz əv ɡɑːd/",
        "vi": "Hội thánh Đức Chúa Trời",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026605",
        "hw": "astronomical unit",
        "pos": "phrase",
        "ipa": "/ˌæs.trəˈnɑː.mɪ.kəl ˈjuː.nɪt/",
        "vi": "đơn vị thiên văn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026606",
        "hw": "atlas cedar",
        "pos": "phrase",
        "ipa": "/ˈæt.ləs ˈsiː.dɚ/",
        "vi": "cây tuyết tùng Atlas",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026607",
        "hw": "autograph album",
        "pos": "phrase",
        "ipa": "/ˈɔː.tə.ɡræf ˈæl.bəm/",
        "vi": "sổ lưu bút; tập chữ ký",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026608",
        "hw": "badger state",
        "pos": "phrase",
        "ipa": "/ˈbædʒ.ɚ steɪt/",
        "vi": "bang Wisconsin; biệt danh Badger",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026609",
        "hw": "ballroom dancing",
        "pos": "phrase",
        "ipa": "/ˈbɑːl.ruːm ˈdæn.sɪŋ/",
        "vi": "khiêu vũ; vũ điệu thính phòng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026610",
        "hw": "barred owl",
        "pos": "phrase",
        "ipa": "/bɑːrd aʊl/",
        "vi": "cú vằn; cú lông sọc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026611",
        "hw": "batting glove",
        "pos": "phrase",
        "ipa": "/ˈbæt̬.ɪŋ ɡlʌv/",
        "vi": "găng tay đánh bóng chày",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026612",
        "hw": "belgian congo",
        "pos": "phrase",
        "ipa": "/ˈbel.dʒən ˈkɑːŋ.ɡoʊ/",
        "vi": "Congo thuộc Bỉ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026613",
        "hw": "bermuda dollar",
        "pos": "phrase",
        "ipa": "/bɚˈmjuː.də ˈdɑː.lɚ/",
        "vi": "đô la Bermuda",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026614",
        "hw": "birch tree",
        "pos": "phrase",
        "ipa": "/bɝːtʃ triː/",
        "vi": "cây bạch dương",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026615",
        "hw": "body odor",
        "pos": "phrase",
        "ipa": "/ˈbɑː.di ˈoʊ.dɚ/",
        "vi": "mùi cơ thể; mùi hôi nách",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026616",
        "hw": "body stocking",
        "pos": "phrase",
        "ipa": "/ˈbɑː.di ˈstɑː.kɪŋ/",
        "vi": "áo liền quần ôm sát bó thân",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026617",
        "hw": "boiling water reactor",
        "pos": "phrase",
        "ipa": "/ˈbɔɪ.lɪŋ ˈwɑː.t̬ɚ riˈæk.tɚ/",
        "vi": "lò phản ứng nước sôi hạt nhân",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026618",
        "hw": "bone marrow",
        "pos": "phrase",
        "ipa": "/boʊn ˈmær.oʊ/",
        "vi": "tủy xương",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026619",
        "hw": "book of amos",
        "pos": "phrase",
        "ipa": "/bʊk əv ˈeɪ.məs/",
        "vi": "Sách A-mốt; sách tiên tri Amos",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026620",
        "hw": "book of jeremiah",
        "pos": "phrase",
        "ipa": "/bʊk əv ˌdʒer.əˈmaɪ.ə/",
        "vi": "Sách Giê-rê-mi; sách Kinh Thánh",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026621",
        "hw": "bottled gas",
        "pos": "phrase",
        "ipa": "/ˈbɑːt̬.əld ɡæs/",
        "vi": "khí hóa lỏng đóng bình; khí ga",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026622",
        "hw": "bricks and mortar",
        "pos": "phrase",
        "ipa": "/ˌbrɪks ən ˈmɔːr.t̬ɚ/",
        "vi": "gạch vữa; cửa hàng truyền thống",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026623",
        "hw": "bursting charge",
        "pos": "phrase",
        "ipa": "/ˈbɝː.stɪŋ tʃɑːrdʒ/",
        "vi": "liều thuốc nổ; khối nổ phá vỡ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026624",
        "hw": "calculus of variations",
        "pos": "phrase",
        "ipa": "/ˈkæl.kjə.ləs əv ˌver.iˈeɪ.ʃənz/",
        "vi": "phép tính biến phân",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026625",
        "hw": "canada wild rye",
        "pos": "phrase",
        "ipa": "/ˈkæn.ə.də waɪld raɪ/",
        "vi": "cỏ lúa mạch đen dại Canada",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026626",
        "hw": "cartridge holder",
        "pos": "phrase",
        "ipa": "/ˈkɑːr.trɪdʒ ˈhoʊl.dɚ/",
        "vi": "băng đạn; hộp chứa đạn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026627",
        "hw": "cd burner",
        "pos": "phrase",
        "ipa": "/ˌsiːˈdiː ˈbɝː.nɚ/",
        "vi": "ổ ghi đĩa CD; đầu ghi đĩa",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026628",
        "hw": "cling film",
        "pos": "phrase",
        "ipa": "/ˈklɪŋ fɪlm/",
        "vi": "màng bọc thực phẩm; màng nilon",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026629",
        "hw": "coaster wagon",
        "pos": "phrase",
        "ipa": "/ˈkoʊ.stɚ ˈwæɡ.ən/",
        "vi": "xe kéo bốn bánh cho trẻ em",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026630",
        "hw": "cocoa bean",
        "pos": "phrase",
        "ipa": "/ˈkoʊ.koʊ biːn/",
        "vi": "hạt ca cao",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026631",
        "hw": "colorado beetle",
        "pos": "phrase",
        "ipa": "/ˌkɑː.ləˈræd.oʊ ˈbiː.t̬əl/",
        "vi": "bọ cánh cứng khoai tây Colorado",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026632",
        "hw": "commencement day",
        "pos": "phrase",
        "ipa": "/kəˈmens.mənt deɪ/",
        "vi": "ngày lễ tốt nghiệp; ngày bế giảng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026633",
        "hw": "common barley",
        "pos": "phrase",
        "ipa": "/ˈkɑː.mən ˈbɑːr.li/",
        "vi": "lúa mạch thường; đại mạch",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026634",
        "hw": "constructive metabolism",
        "pos": "phrase",
        "ipa": "/kənˈstrʌk.tɪv məˈtæb.əl.ɪ.zəm/",
        "vi": "đồng hóa; quá trình tổng hợp chất",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026635",
        "hw": "cost ledger",
        "pos": "phrase",
        "ipa": "/kɔːst ˈledʒ.ɚ/",
        "vi": "sổ cái chi phí; sổ chi phí",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026636",
        "hw": "crocodile river",
        "pos": "phrase",
        "ipa": "/ˈkrɑː.kə.daɪl ˈrɪv.ɚ/",
        "vi": "sông Cá Sấu; sông Crocodile",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026637",
        "hw": "dead axle",
        "pos": "phrase",
        "ipa": "/ded ˈæk.səl/",
        "vi": "trục chết; trục bánh xe tĩnh",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026638",
        "hw": "desert pea",
        "pos": "phrase",
        "ipa": "/ˈdez.ɚt piː/",
        "vi": "cây đậu sa mạc hoa đỏ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026639",
        "hw": "disk cache",
        "pos": "phrase",
        "ipa": "/dɪsk kæʃ/",
        "vi": "bộ nhớ đệm đĩa",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026640",
        "hw": "dog paddle",
        "pos": "phrase",
        "ipa": "/dɑːɡ ˈpæd.əl/",
        "vi": "kiểu bơi chó",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026641",
        "hw": "ear fungus",
        "pos": "phrase",
        "ipa": "/ɪr ˈfʌŋ.ɡəs/",
        "vi": "mộc nhĩ; nấm mèo",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026642",
        "hw": "edible banana",
        "pos": "phrase",
        "ipa": "/ˈed.ə.bəl bəˈnæn.ə/",
        "vi": "chuối ăn quả; cây chuối ăn quả",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026643",
        "hw": "erie canal",
        "pos": "phrase",
        "ipa": "/ˈɪr.i kəˈnæl/",
        "vi": "kênh đào Erie",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026644",
        "hw": "ernest orlando lawrence",
        "pos": "phrase",
        "ipa": "/ˈɝː.nɪst ɔːrˈlæn.doʊ ˈlɔːr.əns/",
        "vi": "Ernest Lawrence; nhà vật lý Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026645",
        "hw": "european white birch",
        "pos": "phrase",
        "ipa": "/ˌjʊr.əˈpiː.ən waɪt bɝːtʃ/",
        "vi": "cây bạch dương trắng châu Âu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026646",
        "hw": "expressed almond oil",
        "pos": "phrase",
        "ipa": "/ɪkˈsprest ˈɑː.mənd ɔɪl/",
        "vi": "dầu hạnh nhân ép nguyên chất",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026647",
        "hw": "extend oneself",
        "pos": "phrase",
        "ipa": "/ɪkˈstend wʌnˈself/",
        "vi": "gắng hết sức; nỗ lực tối đa",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026648",
        "hw": "fairy lantern",
        "pos": "phrase",
        "ipa": "/ˈfer.i ˈlæn.tɚn/",
        "vi": "cây hoa đèn lồng; cỏ đèn tiên",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026649",
        "hw": "feather reed grass",
        "pos": "phrase",
        "ipa": "/ˈfeð.ɚ riːd ɡræs/",
        "vi": "cỏ sậy lông vũ; cỏ đuôi gà cảnh",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026650",
        "hw": "fibre bundle",
        "pos": "phrase",
        "ipa": "/ˈfaɪ.bɚ ˈbʌn.dəl/",
        "vi": "bó sợi; phân thớ toán học",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026651",
        "hw": "fielding average",
        "pos": "phrase",
        "ipa": "/ˈfiːl.dɪŋ ˈæv.ɚ.ɪdʒ/",
        "vi": "tỷ lệ phòng ngự trong bóng chày",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026652",
        "hw": "flag of truce",
        "pos": "phrase",
        "ipa": "/flæɡ əv truːs/",
        "vi": "cờ trắng đình chiến; cờ xin hàng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026653",
        "hw": "french loaf",
        "pos": "phrase",
        "ipa": "/frentʃ loʊf/",
        "vi": "bánh mì Pháp; bánh mì baguette",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026654",
        "hw": "gem cutter",
        "pos": "phrase",
        "ipa": "/dʒem ˈkʌt̬.ɚ/",
        "vi": "thợ cắt đá quý; thợ mài ngọc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026655",
        "hw": "genus melissa",
        "pos": "phrase",
        "ipa": "/ˈdʒiː.nəs məˈlɪs.ə/",
        "vi": "chi bạc hà chanh; chi Melissa",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026656",
        "hw": "genus vanilla",
        "pos": "phrase",
        "ipa": "/ˈdʒiː.nəs vàˈnɪl.ə/",
        "vi": "chi phong lan vani; chi Vanilla",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026657",
        "hw": "gill arch",
        "pos": "phrase",
        "ipa": "/ɡɪl ɑːrtʃ/",
        "vi": "cung mang cá; cung mang giải phẫu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026658",
        "hw": "glee club",
        "pos": "phrase",
        "ipa": "/ɡliː klʌb/",
        "vi": "câu lạc bộ hợp xướng học đường",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026659",
        "hw": "glory pea",
        "pos": "phrase",
        "ipa": "/ˈɡlɔːr.i piː/",
        "vi": "cây đậu vinh quang; hoa sa mạc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026660",
        "hw": "go ballistic",
        "pos": "phrase",
        "ipa": "/ɡoʊ bəˈlɪs.tɪk/",
        "vi": "nổi cơn thịnh nộ; giận phát điên",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026661",
        "hw": "golden parachute",
        "pos": "phrase",
        "ipa": "/ˌɡoʊl.dən ˈper.ə.ʃuːt/",
        "vi": "dù vàng; gói trợ cấp thôi việc lớn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026662",
        "hw": "granting immunity",
        "pos": "phrase",
        "ipa": "/ˈɡræn.tɪŋ ɪˈmjuː.nə.t̬i/",
        "vi": "trao quyền miễn trừ truy tố pháp lý",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026663",
        "hw": "grass pea",
        "pos": "phrase",
        "ipa": "/ɡræs piː/",
        "vi": "đậu cỏ; đậu hoa dại",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026664",
        "hw": "gravitational field",
        "pos": "phrase",
        "ipa": "/ˌɡræv.əˈteɪ.ʃən.əl fiːld/",
        "vi": "trường hấp dẫn; trường trọng lực",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026665",
        "hw": "gravitational force",
        "pos": "phrase",
        "ipa": "/ˌɡræv.əˈteɪ.ʃən.əl fɔːrs/",
        "vi": "lực hấp dẫn; lực trọng trường",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026666",
        "hw": "grazing fire",
        "pos": "phrase",
        "ipa": "/ˈɡreɪ.zɪŋ ˈfaɪr/",
        "vi": "hỏa lực bắn lướt sát mặt đất",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026667",
        "hw": "grazing land",
        "pos": "phrase",
        "ipa": "/ˈɡreɪ.zɪŋ lænd/",
        "vi": "đồng cỏ chăn thả gia súc; bãi cỏ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026668",
        "hw": "great ape",
        "pos": "phrase",
        "ipa": "/ɡreɪt eɪp/",
        "vi": "vượn người lớn; đại linh trưởng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026669",
        "hw": "helen keller",
        "pos": "phrase",
        "ipa": "/ˈhel.ən ˈkel.ɚ/",
        "vi": "Helen Keller; nữ văn sĩ mù điếc Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026670",
        "hw": "heroin addict",
        "pos": "phrase",
        "ipa": "/ˈher.oʊ.ɪn ˈæd.ɪkt/",
        "vi": "người nghiện ma túy heroin",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026671",
        "hw": "horn poppy",
        "pos": "phrase",
        "ipa": "/hɔːrn ˈpɑː.pi/",
        "vi": "cây anh túc sừng ven biển",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026672",
        "hw": "house sparrow",
        "pos": "phrase",
        "ipa": "/ˈhaʊs ˌsper.oʊ/",
        "vi": "chim sẻ nhà; chim sẻ thường",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026673",
        "hw": "inferior vocal cord",
        "pos": "phrase",
        "ipa": "/ɪnˈfɪr.i.ɚ ˈvoʊ.kəl kɔːrd/",
        "vi": "dây thanh âm dưới; dây thanh thật",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026674",
        "hw": "iron overload",
        "pos": "phrase",
        "ipa": "/ˈaɪ.ɚn ˌoʊ.vɚˈloʊd/",
        "vi": "ứ sắt; hội chứng quá tải sắt",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026675",
        "hw": "irrigation ditch",
        "pos": "phrase",
        "ipa": "/ˌɪr.əˈɡeɪ.ʃən dɪtʃ/",
        "vi": "mương tưới tiêu thủy lợi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026676",
        "hw": "judgement of dismissal",
        "pos": "phrase",
        "ipa": "/ˈdʒʌdʒ.mənt əv dɪsˈmɪs.əl/",
        "vi": "phán quyết bác đơn khởi kiện",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026677",
        "hw": "jury mast",
        "pos": "phrase",
        "ipa": "/ˈdʒʊr.i mæst/",
        "vi": "cột buồm tạm thời thay thế",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026678",
        "hw": "kangaroo apple",
        "pos": "phrase",
        "ipa": "/ˌkæŋ.ɡəˈruː ˈæp.əl/",
        "vi": "cây cà túi chuột Úc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026679",
        "hw": "kiss curl",
        "pos": "phrase",
        "ipa": "/ˈkɪs kɝːl/",
        "vi": "lọn tóc xoăn uốn trước trán",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026680",
        "hw": "kissing kin",
        "pos": "phrase",
        "ipa": "/ˈkɪs.ɪŋ kɪn/",
        "vi": "họ hàng thân thiết; bà con gần gũi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026681",
        "hw": "kite tail",
        "pos": "phrase",
        "ipa": "/kaɪt teɪl/",
        "vi": "đuôi diều giữ thăng bằng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026682",
        "hw": "ledger board",
        "pos": "phrase",
        "ipa": "/ˈledʒ.ɚ bɔːrd/",
        "vi": "thanh giằng ngang giàn giáo",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026683",
        "hw": "ledger paper",
        "pos": "phrase",
        "ipa": "/ˈledʒ.ɚ ˈpeɪ.pɚ/",
        "vi": "giấy kẻ ghi chép sổ cái",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026684",
        "hw": "leg curling",
        "pos": "phrase",
        "ipa": "/leɡ ˈkɝː.lɪŋ/",
        "vi": "bài tập cuốn chân tạ đùi sau",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026685",
        "hw": "little sparrow",
        "pos": "phrase",
        "ipa": "/ˈlɪt̬.əl ˈsper.oʊ/",
        "vi": "Chim sẻ nhỏ; biệt danh Édith Piaf",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026686",
        "hw": "locomotive engine",
        "pos": "phrase",
        "ipa": "/ˌloʊ.kəˈmoʊ.tɪv ˈen.dʒɪn/",
        "vi": "đầu máy xe lửa; đầu kéo tàu hỏa",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026687",
        "hw": "max ernst",
        "pos": "phrase",
        "ipa": "/mæks ˈɛərnst/",
        "vi": "Max Ernst; họa sĩ siêu thực Đức",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026688",
        "hw": "mineral tar",
        "pos": "phrase",
        "ipa": "/ˈmɪn.ɚ.əl tɑːr/",
        "vi": "hắc ín khoáng sản; nhựa đường mỏ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026689",
        "hw": "moth plant",
        "pos": "phrase",
        "ipa": "/mɑːθ plænt/",
        "vi": "hoa bướm đêm; cây cỏ dây leo",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026690",
        "hw": "mountain birch",
        "pos": "phrase",
        "ipa": "/ˈmaʊn.tən bɝːtʃ/",
        "vi": "bạch dương núi cao lá nhỏ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026691",
        "hw": "multiple regression",
        "pos": "phrase",
        "ipa": "/ˈmʌl.tə.pəl rɪˈɡreʃ.ən/",
        "vi": "hồi quy bội; phân tích đa biến",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026692",
        "hw": "mushroom anchor",
        "pos": "phrase",
        "ipa": "/ˈmʌʃ.ruːm ˈæŋ.kɚ/",
        "vi": "neo nấm giữ đáy bùn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026693",
        "hw": "nan river",
        "pos": "phrase",
        "ipa": "/næn ˈrɪv.ɚ/",
        "vi": "sông Nan ở miền bắc Thái Lan",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026694",
        "hw": "narcotics agent",
        "pos": "phrase",
        "ipa": "/nɑːrˈkɑː.tɪks ˈeɪ.dʒənt/",
        "vi": "đặc vụ phòng chống ma túy",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026695",
        "hw": "new world sparrow",
        "pos": "phrase",
        "ipa": "/nuː wɝːld ˈsper.oʊ/",
        "vi": "chim sẻ châu Mỹ; sẻ Tân thế giới",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026696",
        "hw": "nitrogen dioxide",
        "pos": "phrase",
        "ipa": "/ˈnaɪ.trə.dʒən daɪˈɑːk.saɪd/",
        "vi": "khí nitơ điôxit; khí NO₂",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026697",
        "hw": "nose flute",
        "pos": "phrase",
        "ipa": "/noʊz fluːt/",
        "vi": "sáo mũi; loại sáo thổi bằng mũi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026698",
        "hw": "notions counter",
        "pos": "phrase",
        "ipa": "/ˈnoʊ.ʃənz ˈkaʊn.tɚ/",
        "vi": "quầy bán phụ liệu may mặc kim chỉ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026699",
        "hw": "nuclear chemist",
        "pos": "phrase",
        "ipa": "/ˈnuː.kliː.ɚ ˈkem.ɪst/",
        "vi": "nhà hóa học hạt nhân",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026700",
        "hw": "obedience plant",
        "pos": "phrase",
        "ipa": "/oʊˈbiː.di.əns plænt/",
        "vi": "cây hoa vương miện ngoan ngoãn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026701",
        "hw": "oil refinery",
        "pos": "phrase",
        "ipa": "/ɔɪl rɪˈfaɪ.nɚ.i/",
        "vi": "nhà máy lọc dầu; xưởng lọc dầu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

# Validation
ALLOWED_POS = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
EXPECTED_KEYS = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(records) == 100, f"Expected 100 records, got {len(records)}"

for r in records:
    assert list(r.keys()) == EXPECTED_KEYS, f"Keys mismatch in {r['id']}"
    assert r['pos'] in ALLOWED_POS, f"Invalid POS {r['pos']} in {r['id']}"
    assert r['ipa'].startswith('/') and r['ipa'].endswith('/') and len(r['ipa']) > 2, f"Invalid IPA in {r['id']}"
    assert r['ipa'].count('/') == 2, f"IPA slashes count error in {r['id']}: {r['ipa']}"
    assert len(r['vi']) <= 35, f"VI too long ({len(r['vi'])} chars): {r['vi']} in {r['id']}"
    assert r['status'] == 'reviewed', f"Status not reviewed in {r['id']}"

with open('scratch/b26_r04_p2.json', 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print("Wrote scratch/b26_r04_p2.json successfully")
