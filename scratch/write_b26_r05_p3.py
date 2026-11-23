import json

# Batch 26 Round 5 Part 3 (lex.en.200k.027202 to lex.en.200k.027301)
records = [
    {
        "id": "lex.en.200k.027202",
        "hw": "noahs",
        "pos": "noun",
        "ipa": "/ˈnoʊ.əz/",
        "vi": "những người tên Noah",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027203",
        "hw": "norms",
        "pos": "noun",
        "ipa": "/nɔːrmz/",
        "vi": "các chuẩn mực; quy phạm xã hội",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027204",
        "hw": "occupying",
        "pos": "verb",
        "ipa": "/ˈɑː.kjə.paɪ.ɪŋ/",
        "vi": "đang chiếm đóng; đang bận rộn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027205",
        "hw": "pacs",
        "pos": "noun",
        "ipa": "/pæks/",
        "vi": "các ủy ban hành động chính trị",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027206",
        "hw": "perths",
        "pos": "noun",
        "ipa": "/pɝːθs/",
        "vi": "những nơi tên Perth",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027207",
        "hw": "pistolled",
        "pos": "verb",
        "ipa": "/ˈpɪs.təld/",
        "vi": "đã bắn chết bằng súng ngắn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027208",
        "hw": "pistolling",
        "pos": "verb",
        "ipa": "/ˈpɪs.təl.ɪŋ/",
        "vi": "việc bắn bằng súng ngắn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027209",
        "hw": "pistols",
        "pos": "noun",
        "ipa": "/ˈpɪs.təlz/",
        "vi": "những khẩu súng ngắn lục",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027210",
        "hw": "printers",
        "pos": "noun",
        "ipa": "/ˈprɪn.t̬ɚz/",
        "vi": "các máy in ấn; những người thợ in",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027211",
        "hw": "reunions",
        "pos": "noun",
        "ipa": "/riːˈjuː.njənz/",
        "vi": "các cuộc hội ngộ; buổi họp mặt",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027212",
        "hw": "sanctuaries",
        "pos": "noun",
        "ipa": "/ˈsæŋk.tʃu.er.iz/",
        "vi": "khu bảo tồn thiên nhiên; nơi ẩn náu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027213",
        "hw": "satans",
        "pos": "noun",
        "ipa": "/ˈseɪ.tənz/",
        "vi": "những kẻ ác độc quỷ Sa-tăng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027214",
        "hw": "seouls",
        "pos": "noun",
        "ipa": "/soʊlz/",
        "vi": "những nơi tên Seoul",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027215",
        "hw": "sieges",
        "pos": "noun",
        "ipa": "/ˈsiː.dʒɪz/",
        "vi": "các cuộc bao vây hãm thành",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027216",
        "hw": "soundtracks",
        "pos": "noun",
        "ipa": "/ˈsaʊnd.træks/",
        "vi": "các bản nhạc phim ghi âm",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027217",
        "hw": "spines",
        "pos": "noun",
        "ipa": "/spaɪnz/",
        "vi": "các cột sống; gai góc trên thân",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027218",
        "hw": "sullivans",
        "pos": "noun",
        "ipa": "/ˈsʌl.ə.vənz/",
        "vi": "những người mang họ Sullivan",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027219",
        "hw": "tenures",
        "pos": "noun",
        "ipa": "/ˈten.jɚz/",
        "vi": "nhiệm kỳ; quyền sử dụng đất",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027220",
        "hw": "tenuring",
        "pos": "verb",
        "ipa": "/ˈten.jɚ.ɪŋ/",
        "vi": "việc trao biên chế vĩnh viễn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027221",
        "hw": "textures",
        "pos": "noun",
        "ipa": "/ˈteks.tʃɚz/",
        "vi": "các kết cấu bề mặt; chất liệu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027222",
        "hw": "treasurers",
        "pos": "noun",
        "ipa": "/ˈtreʒ.ɚ.ɚz/",
        "vi": "những người thủ quỹ; thủ kho",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027223",
        "hw": "triangles",
        "pos": "noun",
        "ipa": "/ˈtraɪ.æŋ.ɡəlz/",
        "vi": "các hình tam giác; kẻ ba góc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027224",
        "hw": "unclearer",
        "pos": "adj",
        "ipa": "/ʌnˈklɪr.ɚ/",
        "vi": "mờ mịt hơn; không rõ ràng hơn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027225",
        "hw": "unclearest",
        "pos": "adj",
        "ipa": "/ʌnˈklɪr.ɪst/",
        "vi": "mơ hồ nhất; không rõ ràng nhất",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027226",
        "hw": "venezuelas",
        "pos": "noun",
        "ipa": "/ˌven.əˈzweɪ.ləz/",
        "vi": "những nơi tên Venezuela",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027227",
        "hw": "venices",
        "pos": "noun",
        "ipa": "/ˈven.ɪs.ɪz/",
        "vi": "những nơi tên Venice",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027228",
        "hw": "adobe brick",
        "pos": "phrase",
        "ipa": "/əˈdoʊ.bi brɪk/",
        "vi": "gạch bùn phơi khô tự nhiên",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027229",
        "hw": "alex haley",
        "pos": "phrase",
        "ipa": "/ˈæl.ɪks ˈheɪ.li/",
        "vi": "Alex Haley; nhà văn viết Cội Rễ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027230",
        "hw": "american gray birch",
        "pos": "phrase",
        "ipa": "/əˈmer.ɪ.kən ɡreɪ bɝːtʃ/",
        "vi": "cây bạch dương xám Bắc Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027231",
        "hw": "american grey birch",
        "pos": "phrase",
        "ipa": "/əˈmer.ɪ.kən ɡreɪ bɝːtʃ/",
        "vi": "cây bạch dương xám Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027232",
        "hw": "apache devil dance",
        "pos": "phrase",
        "ipa": "/əˈpætʃ.i ˈdev.əl dæns/",
        "vi": "điệu múa trừ quỷ người Apache",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027233",
        "hw": "apostle paul",
        "pos": "phrase",
        "ipa": "/əˈpɑː.səl pɔːl/",
        "vi": "Thánh Tông đồ Phao-lô",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027234",
        "hw": "arctic poppy",
        "pos": "phrase",
        "ipa": "/ˈɑːrk.tɪk ˈpɑː.pi/",
        "vi": "hoa anh túc vàng Bắc Cực",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027235",
        "hw": "at variance",
        "pos": "phrase",
        "ipa": "/æt ˈver.i.əns/",
        "vi": "xung đột; không hòa hợp với",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027236",
        "hw": "australian chestnut",
        "pos": "phrase",
        "ipa": "/ɑːˈstreɪl.jən ˈtʃes.nʌt/",
        "vi": "cây dẻ hoa đỏ nước Úc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027237",
        "hw": "bear paw",
        "pos": "phrase",
        "ipa": "/ber pɑː/",
        "vi": "bánh sừng bò hình móng gấu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027238",
        "hw": "bedford cord",
        "pos": "phrase",
        "ipa": "/ˈbed.fɚd kɔːrd/",
        "vi": "vải sợi gân dọc Bedford",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027239",
        "hw": "belly flop",
        "pos": "phrase",
        "ipa": "/ˈbel.i flɑːp/",
        "vi": "cú nhảy bổ bụng xuống nước",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027240",
        "hw": "belt buckle",
        "pos": "phrase",
        "ipa": "/belt ˈbʌk.əl/",
        "vi": "mặt khóa dây thắt lưng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027241",
        "hw": "billie the kid",
        "pos": "phrase",
        "ipa": "/ˈbɪl.i ðə kɪd/",
        "vi": "Billy the Kid; tướng cướp miền Tây",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027242",
        "hw": "bitter almond",
        "pos": "phrase",
        "ipa": "/ˈbɪt̬.ɚ ˈɑː.mənd/",
        "vi": "hạt hạnh nhân đắng hoang dã",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027243",
        "hw": "black lotion",
        "pos": "phrase",
        "ipa": "/blæk ˈloʊ.ʃən/",
        "vi": "dung dịch calomen trị giang mai",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027244",
        "hw": "black racer",
        "pos": "phrase",
        "ipa": "/blæk ˈreɪ.sɚ/",
        "vi": "rắn roi đen Bắc Mỹ không độc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027245",
        "hw": "body lotion",
        "pos": "phrase",
        "ipa": "/ˈbɑː.di ˌloʊ.ʃən/",
        "vi": "sữa dưỡng thể toàn thân da mềm",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027246",
        "hw": "bunk down",
        "pos": "phrase",
        "ipa": "/bʌŋk daʊn/",
        "vi": "ngủ tạm trên giường hẹp",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027247",
        "hw": "bunk off",
        "pos": "phrase",
        "ipa": "/bʌŋk ɔːf/",
        "vi": "trốn học; cúp việc không phép",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027248",
        "hw": "capital of belarus",
        "pos": "phrase",
        "ipa": "/ˈkæp.ə.t̬əl əv ˌbel.əˈruːs/",
        "vi": "thủ đô Minsk của Belarus",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027249",
        "hw": "cartridge brass",
        "pos": "phrase",
        "ipa": "/ˈkɑːr.trɪdʒ bræs/",
        "vi": "đồng thau dập vỏ đạn súng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027250",
        "hw": "celestial pole",
        "pos": "phrase",
        "ipa": "/səˈles.tʃəl poʊl/",
        "vi": "thiên cực Bắc hoặc Nam",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027251",
        "hw": "chicken kiev",
        "pos": "phrase",
        "ipa": "/ˌtʃɪk.ɪn ˈkiː.ef/",
        "vi": "món ức gà cuộn bơ chiên Kiev",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027252",
        "hw": "chicken stew",
        "pos": "phrase",
        "ipa": "/ˈtʃɪk.ɪn stuː/",
        "vi": "món thịt gà hầm củ quả",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027253",
        "hw": "chimney swift",
        "pos": "phrase",
        "ipa": "/ˈtʃɪm.ni swɪft/",
        "vi": "chim yến làm tổ ống khói",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027254",
        "hw": "chinese chestnut",
        "pos": "phrase",
        "ipa": "/ˌtʃaɪˈniːz ˈtʃes.nʌt/",
        "vi": "cây dẻ thơm Trung Quốc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027255",
        "hw": "cider mill",
        "pos": "phrase",
        "ipa": "/ˈsaɪ.dɚ mɪl/",
        "vi": "xưởng ép táo làm nước ép rượu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027256",
        "hw": "cigar lighter",
        "pos": "phrase",
        "ipa": "/sɪˈɡɑːr ˌlaɪ.t̬ɚ/",
        "vi": "bật lửa châm xì gà chuyên dụng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027257",
        "hw": "clamp down",
        "pos": "phrase",
        "ipa": "/klæmp daʊn/",
        "vi": "siết chặt kỷ luật; đàn áp mạnh",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027258",
        "hw": "cleanup position",
        "pos": "phrase",
        "ipa": "/ˈkliːn.ʌp pəˌzɪʃ.ən/",
        "vi": "vị trí đánh bóng thứ tư trận đấu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027259",
        "hw": "commencement exercise",
        "pos": "phrase",
        "ipa": "/kəˈmens.mənt ˈek.sɚ.saɪz/",
        "vi": "nghi thức lễ trao bằng tốt nghiệp",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027260",
        "hw": "common thorn apple",
        "pos": "phrase",
        "ipa": "/ˈkɑː.mən θɔːrn ˈæp.əl/",
        "vi": "cây cà độc dược gai thông thường",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027261",
        "hw": "compression fracture",
        "pos": "phrase",
        "ipa": "/kəmˈpreʃ.ən ˈfræk.tʃɚ/",
        "vi": "gãy lún thân đốt sống do nén",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027262",
        "hw": "concrete mixer",
        "pos": "phrase",
        "ipa": "/ˈkɑːŋ.kriːt ˌmɪk.sɚ/",
        "vi": "máy trộn bê tông xây dựng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027263",
        "hw": "conditional probability",
        "pos": "phrase",
        "ipa": "/kənˈdɪʃ.ən.əl ˌprɑː.bəˈbɪl.ə.t̬i/",
        "vi": "xác suất có điều kiện toán học",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027264",
        "hw": "continental glacier",
        "pos": "phrase",
        "ipa": "/ˌkɑːn.tənˈen.t̬əl ˈɡleɪ.ʃɚ/",
        "vi": "sông băng lục địa khổng lồ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027265",
        "hw": "crocodile tears",
        "pos": "phrase",
        "ipa": "/ˌkrɑː.kə.daɪl ˈtɪrz/",
        "vi": "nước mắt cá sấu; khóc giả tạo",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027266",
        "hw": "cross of lorraine",
        "pos": "phrase",
        "ipa": "/krɑːs əv ləˈreɪn/",
        "vi": "thánh giá hai thanh ngang Lorraine",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027267",
        "hw": "delusional disorder",
        "pos": "phrase",
        "ipa": "/dɪˈluː.ʒən.əl dɪsˈɔːr.dɚ/",
        "vi": "chứng rối loạn tâm thần hoang tưởng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027268",
        "hw": "descriptive grammar",
        "pos": "phrase",
        "ipa": "/dɪˈskrɪp.tɪv ˈɡræm.ɚ/",
        "vi": "ngữ pháp miêu tả thực tế",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027269",
        "hw": "dialog box",
        "pos": "phrase",
        "ipa": "/ˈdaɪ.ə.lɑːɡ bɑːks/",
        "vi": "hộp thoại thông báo trên máy tính",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027270",
        "hw": "displaced fracture",
        "pos": "phrase",
        "ipa": "/dɪˈspleɪst ˈfræk.tʃɚ/",
        "vi": "gãy xương có di lệch khớp xương",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027271",
        "hw": "dna fingerprint",
        "pos": "phrase",
        "ipa": "/ˌdiː.enˈeɪ ˈfɪŋ.ɡɚ.prɪnt/",
        "vi": "dấu vân tay ADN định danh cá thể",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027272",
        "hw": "dwarf iris",
        "pos": "phrase",
        "ipa": "/dwɔːrf ˈaɪ.rɪs/",
        "vi": "cây hoa diên vĩ lùn vùng núi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027273",
        "hw": "ecclesiastical province",
        "pos": "phrase",
        "ipa": "/ɪˌkliː.ziˈæs.tɪk ˈprɑː.vɪns/",
        "vi": "giáo tỉnh thuộc giáo phận quản hạt",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027274",
        "hw": "edward teller",
        "pos": "phrase",
        "ipa": "/ˈed.wɚd ˈtel.ɚ/",
        "vi": "Edward Teller; cha đẻ bom khinh khí",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027275",
        "hw": "edward weston",
        "pos": "phrase",
        "ipa": "/ˈed.wɚd ˈwes.tən/",
        "vi": "Edward Weston; nhiếp ảnh gia Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027276",
        "hw": "english cavalry saddle",
        "pos": "phrase",
        "ipa": "/ˈɪŋ.ɡlɪʃ ˈkæv.əl.ri ˈsæd.əl/",
        "vi": "yên kỵ binh kiểu quân đội Anh",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027277",
        "hw": "espionage agent",
        "pos": "phrase",
        "ipa": "/ˈes.pi.ə.nɑːʒ ˈeɪ.dʒənt/",
        "vi": "điệp viên tình báo gián điệp ngầm",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027278",
        "hw": "european chestnut",
        "pos": "phrase",
        "ipa": "/ˌjʊr.əˈpiː.ən ˈtʃes.nʌt/",
        "vi": "cây dẻ châu Âu cho hạt bùi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027279",
        "hw": "european silver fir",
        "pos": "phrase",
        "ipa": "/ˌjʊr.əˈpiː.ən ˌsɪl.vɚ ˈfɝː/",
        "vi": "cây linh sam bạc trắng châu Âu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027280",
        "hw": "ezra pound",
        "pos": "phrase",
        "ipa": "/ˈez.rə paʊnd/",
        "vi": "Ezra Pound; nhà thơ hiện đại Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027281",
        "hw": "favourable reception",
        "pos": "phrase",
        "ipa": "/ˈfeɪ.vɚ.ə.bəl rɪˈsep.ʃən/",
        "vi": "sự đón nhận nồng nhiệt nhiệt tình",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027282",
        "hw": "fingerprint expert",
        "pos": "phrase",
        "ipa": "/ˈfɪŋ.ɡɚ.prɪnt ˈek.spɝːt/",
        "vi": "chuyên viên giám định dấu vân tay",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027283",
        "hw": "freshwater bass",
        "pos": "phrase",
        "ipa": "/ˈfreʃˌwɑː.t̬ɚ bæs/",
        "vi": "cá vược nước ngọt ao hồ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027284",
        "hw": "funnel shape",
        "pos": "phrase",
        "ipa": "/ˈfʌn.əl ʃeɪp/",
        "vi": "hình phễu thon dài ở đáy",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027285",
        "hw": "funnel web",
        "pos": "phrase",
        "ipa": "/ˈfʌn.əl web/",
        "vi": "mạng nhện hình ống phễu bẫy mồi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027286",
        "hw": "genital system",
        "pos": "phrase",
        "ipa": "/ˈdʒen.ə.t̬əl ˈsɪs.təm/",
        "vi": "hệ sinh dục cơ quan sinh sản",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027287",
        "hw": "genus python",
        "pos": "phrase",
        "ipa": "/ˈdʒiː.nəs ˈpaɪ.θɑːn/",
        "vi": "chi trăn khổng lồ bò sát",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027288",
        "hw": "giant fir",
        "pos": "phrase",
        "ipa": "/ˈdʒaɪ.ənt fɝː/",
        "vi": "cây linh sam khổng lồ Tây Bắc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027289",
        "hw": "graphical record",
        "pos": "phrase",
        "ipa": "/ˈɡræf.ɪ.kəl ˈrek.ɚd/",
        "vi": "bản ghi dạng đồ thị hình ảnh",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027290",
        "hw": "gravitational constant",
        "pos": "phrase",
        "ipa": "/ˌɡræv.əˈteɪ.ʃən.əl ˈkɑːn.stənt/",
        "vi": "hằng số hấp dẫn vạn vật G",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027291",
        "hw": "gravy boat",
        "pos": "phrase",
        "ipa": "/ˈɡreɪ.vi boʊt/",
        "vi": "thuyền rót nước sốt bàn tiệc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027292",
        "hw": "gray birch",
        "pos": "phrase",
        "ipa": "/ɡreɪ bɝːtʃ/",
        "vi": "cây bạch dương xám vỏ trắng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027293",
        "hw": "great grey kangaroo",
        "pos": "phrase",
        "ipa": "/ɡreɪt ɡreɪ ˌkæŋ.ɡəˈruː/",
        "vi": "chuột túi xám miền đông nước Úc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027294",
        "hw": "guy of burgundy",
        "pos": "phrase",
        "ipa": "/ɡaɪ əv ˈbɝː.ɡən.di/",
        "vi": "Giáo hoàng Callixtus Đệ Nhị",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027295",
        "hw": "hand lotion",
        "pos": "phrase",
        "ipa": "/ˈhænd ˌloʊ.ʃən/",
        "vi": "kem dưỡng ẩm thoa da tay mịn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027296",
        "hw": "hereditary pattern",
        "pos": "phrase",
        "ipa": "/həˈred.ə.ter.i ˈpæt̬.ɚn/",
        "vi": "kiểu quy luật di truyền sinh học",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027297",
        "hw": "immersion foot",
        "pos": "phrase",
        "ipa": "/ɪˈmɝː.ʒən fʊt/",
        "vi": "bệnh bàn chân ngâm nước lạnh sưng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027298",
        "hw": "implicit in",
        "pos": "phrase",
        "ipa": "/ɪmˈplɪs.ɪt ɪn/",
        "vi": "tiềm tàng trong; ngấm ngầm trong",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027299",
        "hw": "ink cartridge",
        "pos": "phrase",
        "ipa": "/ˈɪŋk ˌkɑːr.trɪdʒ/",
        "vi": "hộp mực thay thế máy in",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027300",
        "hw": "interim overhaul",
        "pos": "phrase",
        "ipa": "/ˈɪn.t̬ɚ.ɪm ˈoʊ.vɚ.hɑːl/",
        "vi": "đợt trung tu bảo dưỡng máy móc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027301",
        "hw": "internal auditor",
        "pos": "phrase",
        "ipa": "/ɪnˈtɝː.nəl ˈɑː.də.t̬ɚ/",
        "vi": "chuyên viên kiểm toán nội bộ",
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

with open('scratch/b26_r05_p3.json', 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print("Wrote scratch/b26_r05_p3.json successfully")
