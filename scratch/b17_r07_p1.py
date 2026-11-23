import json

reviewed_records = [
    {
        "id": "lex.en.100k.083002",
        "hw": "gushingly",
        "pos": "adv",
        "ipa": "/ˈɡʌʃ.ɪŋ.li/",
        "vi": "một cách vồn vã; tuôn trào nức nở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083003",
        "hw": "gusseted",
        "pos": "adj",
        "ipa": "/ˈɡʌs.ɪ.tɪd/",
        "vi": "có miếng đệm gia cố; có con đỉa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083004",
        "hw": "gussets",
        "pos": "noun",
        "ipa": "/ˈɡʌs.ɪts/",
        "vi": "các miếng đệm gia cố; góc chèn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083005",
        "hw": "gustable",
        "pos": "adj",
        "ipa": "/ˈɡʌs.tə.bəl/",
        "vi": "ngon miệng; có thể nếm được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083006",
        "hw": "gustative",
        "pos": "adj",
        "ipa": "/ˈɡʌs.tə.tɪv/",
        "vi": "thuộc vị giác; liên quan đến nếm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083007",
        "hw": "gustatorial",
        "pos": "adj",
        "ipa": "/ˌɡʌs.təˈtɔːr.i.əl/",
        "vi": "thuộc vị giác; thưởng thức món ăn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083008",
        "hw": "gustatorily",
        "pos": "adv",
        "ipa": "/ˈɡʌs.tə.tɔːr.əl.i/",
        "vi": "về mặt vị giác; theo cảm nhận nếm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083009",
        "hw": "gusted",
        "pos": "verb",
        "ipa": "/ˈɡʌs.tɪd/",
        "vi": "đã thổi từng cơn; gió rít từng đợt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083010",
        "hw": "gustily",
        "pos": "adv",
        "ipa": "/ˈɡʌs.təl.i/",
        "vi": "theo từng cơn gió; nồng nhiệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083011",
        "hw": "gustiness",
        "pos": "noun",
        "ipa": "/ˈɡʌs.ti.nəs/",
        "vi": "tình trạng gió giật; tính dông gió",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083012",
        "hw": "gusting",
        "pos": "verb",
        "ipa": "/ˈɡʌs.tɪŋ/",
        "vi": "đang thổi từng cơn gió mạnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083013",
        "hw": "gusts",
        "pos": "verb",
        "ipa": "/ɡʌsts/",
        "vi": "thổi thành từng cơn gió mạnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083014",
        "hw": "gutierrezia",
        "pos": "noun",
        "ipa": "/ɡuːˌtiː.ɛˈreɪ.zi.ə/",
        "vi": "chi cúc rắn; cây cỏ gutierrezia",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083015",
        "hw": "gutlessness",
        "pos": "noun",
        "ipa": "/ˈɡʌt.ləs.nəs/",
        "vi": "sự nhu nhược; tính hèn nhát",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083016",
        "hw": "gutsily",
        "pos": "adv",
        "ipa": "/ˈɡʌt.səl.i/",
        "vi": "một cách gan góc; quả cảm bạo dạn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083017",
        "hw": "gutsiness",
        "pos": "noun",
        "ipa": "/ˈɡʌt.si.nəs/",
        "vi": "sự can đảm gan góc; tính bạo dạn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083018",
        "hw": "guttae",
        "pos": "noun",
        "ipa": "/ˈɡʌt.iː/",
        "vi": "các giọt trang trí trên gờ chỉ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083019",
        "hw": "guttate",
        "pos": "adj",
        "ipa": "/ˈɡʌt.eɪt/",
        "vi": "có đốm hình giọt nước; lốm đốm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083020",
        "hw": "guttation",
        "pos": "noun",
        "ipa": "/ɡʌˈteɪ.ʃən/",
        "vi": "hiện tượng ứ giọt nước ở lá cây",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083021",
        "hw": "gutted",
        "pos": "verb",
        "ipa": "/ˈɡʌt.ɪd/",
        "vi": "đã mổ ruột; đã thiêu rụi ruột",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083022",
        "hw": "guttered",
        "pos": "verb",
        "ipa": "/ˈɡʌt.ɚd/",
        "vi": "đã chảy thành rãnh; chập chờn lụi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083023",
        "hw": "guttering",
        "pos": "verb",
        "ipa": "/ˈɡʌt.ɚ.ɪŋ/",
        "vi": "đang chảy rãnh; chập chờn sắp tắt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083024",
        "hw": "gutters",
        "pos": "verb",
        "ipa": "/ˈɡʌt.ɚz/",
        "vi": "chảy thành rãnh nước; cháy leo lét",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083025",
        "hw": "guttersnipish",
        "pos": "adj",
        "ipa": "/ˈɡʌt.ɚˌsnaɪ.pɪʃ/",
        "vi": "nhếch nhác đầu đường xó chợ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083026",
        "hw": "gutterway",
        "pos": "noun",
        "ipa": "/ˈɡʌt.ɚ.weɪ/",
        "vi": "máng xối thoát nước; rãnh tiêu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083027",
        "hw": "guttiferae",
        "pos": "noun",
        "ipa": "/ɡʌˈtɪf.ɚ.iː/",
        "vi": "họ bứa; họ măng cụt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083028",
        "hw": "guttiferales",
        "pos": "noun",
        "ipa": "/ɡʌˌtɪf.ɚˈeɪ.liːz/",
        "vi": "bộ bứa; bộ măng cụt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083029",
        "hw": "guttiform",
        "pos": "adj",
        "ipa": "/ˈɡʌt.ə.fɔːrm/",
        "vi": "có hình giọt nước; dạng giọt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083030",
        "hw": "gutting",
        "pos": "verb",
        "ipa": "/ˈɡʌt.ɪŋ/",
        "vi": "đang mổ ruột; vét sạch bên trong",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083031",
        "hw": "guttle",
        "pos": "verb",
        "ipa": "/ˈɡʌt.əl/",
        "vi": "ăn uống phàm phu; ngấu nghiến",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083032",
        "hw": "guttler",
        "pos": "noun",
        "ipa": "/ˈɡʌt.lɚ/",
        "vi": "kẻ ăn uống vô độ; kẻ phàm ăn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083033",
        "hw": "guttula",
        "pos": "noun",
        "ipa": "/ˈɡʌt.jʊ.lə/",
        "vi": "giọt dầu li ti; giọt nhỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083034",
        "hw": "guttulate",
        "pos": "adj",
        "ipa": "/ˈɡʌt.jʊ.leɪt/",
        "vi": "chứa các giọt dầu nhỏ; có đốm giọt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083035",
        "hw": "guttulose",
        "pos": "adj",
        "ipa": "/ˈɡʌt.jʊ.loʊs/",
        "vi": "chứa nhiều giọt nhỏ; lấm tấm giọt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083036",
        "hw": "gutturalism",
        "pos": "noun",
        "ipa": "/ˈɡʌt.ɚ.əlˌɪz.əm/",
        "vi": "đặc tính âm họng; giọng cuống họng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083037",
        "hw": "gutturality",
        "pos": "noun",
        "ipa": "/ˌɡʌt.ɚˈæl.ə.ti/",
        "vi": "tính chất âm hầu; âm giọng cổ họng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083038",
        "hw": "gutturalize",
        "pos": "verb",
        "ipa": "/ˈɡʌt.ɚ.əl.aɪz/",
        "vi": "phát âm từ cuống họng; họng hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083039",
        "hw": "gutturally",
        "pos": "adv",
        "ipa": "/ˈɡʌt.ɚ.əl.i/",
        "vi": "từ sâu cuống họng; khàn đặc nghẹn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083040",
        "hw": "guv",
        "pos": "noun",
        "ipa": "/ɡʌv/",
        "vi": "ông chủ; thưa sếp; thưa ngài",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083041",
        "hw": "guzzled",
        "pos": "verb",
        "ipa": "/ˈɡʌz.əld/",
        "vi": "đã nốc cạn; đã uống ừng ực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083042",
        "hw": "guzzles",
        "pos": "verb",
        "ipa": "/ˈɡʌz.əlz/",
        "vi": "nốc cạn; uống ừng ực; ngốn ngấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083043",
        "hw": "gyatt",
        "pos": "noun",
        "ipa": "/ɡjɑːt/",
        "vi": "mông to nở nang; đường cong gợi cảm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083044",
        "hw": "gyatts",
        "pos": "noun",
        "ipa": "/ɡjɑːts/",
        "vi": "những cặp mông đẫy đà gợi cảm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083045",
        "hw": "gybed",
        "pos": "verb",
        "ipa": "/dʒaɪbd/",
        "vi": "đã xoay đổi buồm theo hướng gió",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083046",
        "hw": "gybes",
        "pos": "verb",
        "ipa": "/dʒaɪbz/",
        "vi": "chuyển hướng buồm; xoay buồm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083047",
        "hw": "gybing",
        "pos": "verb",
        "ipa": "/ˈdʒaɪ.bɪŋ/",
        "vi": "đang chuyển hướng buồm theo gió",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083048",
        "hw": "gyle",
        "pos": "noun",
        "ipa": "/ɡaɪl/",
        "vi": "mẻ bia ủ; thùng lên men bia",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083049",
        "hw": "gymnadenia",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.nəˈdiː.ni.ə/",
        "vi": "chi lan thơm Gymnadenia",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083050",
        "hw": "gymnadeniopsis",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.nəˌdiː.niˈɑːp.sɪs/",
        "vi": "chi phong lan Gymnadeniopsis",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083051",
        "hw": "gymnasia",
        "pos": "noun",
        "ipa": "/dʒɪmˈneɪ.zi.ə/",
        "vi": "các phòng tập gym; trường trung học",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083052",
        "hw": "gymnastically",
        "pos": "adv",
        "ipa": "/dʒɪmˈnæs.tɪ.kəl.i/",
        "vi": "về mặt thể dục dụng cụ; uốn dẻo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083053",
        "hw": "gymnasts",
        "pos": "noun",
        "ipa": "/ˈdʒɪm.næsts/",
        "vi": "các vận động viên thể dục dụng cụ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083054",
        "hw": "gymnelis",
        "pos": "noun",
        "ipa": "/dʒɪmˈnɛl.ɪs/",
        "vi": "chi cá nheo biển Gymnelis",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083055",
        "hw": "gymnocalycium",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.noʊ.kəˈlɪs.i.əm/",
        "vi": "chi xương rồng cằm Gymnocalycium",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083056",
        "hw": "gymnocarpic",
        "pos": "adj",
        "ipa": "/ˌdʒɪm.noʊˈkɑːr.pɪk/",
        "vi": "có thể quả trần; quả lộ ngoài",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083057",
        "hw": "gymnocarpium",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.noʊˈkɑːr.pi.əm/",
        "vi": "chi dương xỉ sồi Gymnocarpium",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083058",
        "hw": "gymnocladus",
        "pos": "noun",
        "ipa": "/dʒɪmˈnɑːk.lə.dəs/",
        "vi": "cây cà phê Kentucky; chi gỗ trần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083059",
        "hw": "gymnocyte",
        "pos": "noun",
        "ipa": "/ˈdʒɪm.noʊ.saɪt/",
        "vi": "tế bào trần không có màng bọc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083060",
        "hw": "gymnogenous",
        "pos": "adj",
        "ipa": "/dʒɪmˈnɑː.dʒə.nəs/",
        "vi": "trơ trụi khi mới nở; chim non trần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083061",
        "hw": "gymnogyps",
        "pos": "noun",
        "ipa": "/ˈdʒɪm.noʊ.dʒɪps/",
        "vi": "chi kền kền khoang cổ California",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083062",
        "hw": "gymnomycota",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.noʊ.maɪˈkoʊ.tə/",
        "vi": "ngành nấm nhầy trần Gymnomycota",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083063",
        "hw": "gymnophiona",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.noʊˈfaɪ.ə.nə/",
        "vi": "bộ giun lưỡng cư; bộ không chân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083064",
        "hw": "gymnophobia",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.nəˈfoʊ.bi.ə/",
        "vi": "hội chứng sợ khỏa thân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083065",
        "hw": "gymnopilus",
        "pos": "noun",
        "ipa": "/ˌdʒɪmˈnɑː.pə.ləs/",
        "vi": "chi nấm tán Gymnopilus",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083066",
        "hw": "gymnoplast",
        "pos": "noun",
        "ipa": "/ˈdʒɪm.noʊ.plæst/",
        "vi": "khối nguyên sinh chất trần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083067",
        "hw": "gymnorhina",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.nəˈraɪ.nə/",
        "vi": "chi chim đồ gốm Úc; chim quạ Úc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083068",
        "hw": "gymnosophical",
        "pos": "adj",
        "ipa": "/ˌdʒɪm.nəˈsɑː.fɪ.kəl/",
        "vi": "thuộc phái triết gia khỏa thân Ấn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083069",
        "hw": "gymnosophist",
        "pos": "noun",
        "ipa": "/dʒɪmˈnɑː.sə.fɪst/",
        "vi": "nhà hiền triết khỏa thân Ấn Độ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083070",
        "hw": "gymnosophy",
        "pos": "noun",
        "ipa": "/dʒɪmˈnɑː.sə.fi/",
        "vi": "triết lý tu khổ hạnh khỏa thân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083071",
        "hw": "gymnospermae",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.noʊˈspɜːr.miː/",
        "vi": "ngành thực vật hạt trần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083072",
        "hw": "gymnospermophyta",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.noʊˌspɜːr.məˈfaɪ.tə/",
        "vi": "ngành thực vật có hạt trần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083073",
        "hw": "gymnospermous",
        "pos": "adj",
        "ipa": "/ˌdʒɪm.noʊˈspɜːr.məs/",
        "vi": "thuộc loài thực vật hạt trần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083074",
        "hw": "gymnosperms",
        "pos": "noun",
        "ipa": "/ˈdʒɪm.noʊˌspɜːrmz/",
        "vi": "các loài cây hạt trần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083075",
        "hw": "gymnosporangium",
        "pos": "noun",
        "ipa": "/ˌdʒɪm.noʊ.spəˈræn.dʒi.əm/",
        "vi": "chi nấm gỉ sắt Gymnosporangium",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083076",
        "hw": "gymnospore",
        "pos": "noun",
        "ipa": "/ˈdʒɪm.noʊ.spɔːr/",
        "vi": "bào tử trần không màng bọc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083077",
        "hw": "gymnura",
        "pos": "noun",
        "ipa": "/dʒɪmˈnjʊər.ə/",
        "vi": "chi cá đuối bướm Gymnura",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083078",
        "hw": "gymslip",
        "pos": "noun",
        "ipa": "/ˈdʒɪm.slɪp/",
        "vi": "váy yếm đồng phục nữ sinh Anh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083079",
        "hw": "gynaeceum",
        "pos": "noun",
        "ipa": "/ˌdʒaɪ.nəˈsiː.əm/",
        "vi": "khuê phòng phụ nữ; bộ nhụy hoa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083080",
        "hw": "gynaecium",
        "pos": "noun",
        "ipa": "/ˌdʒaɪˈniː.si.əm/",
        "vi": "bộ nhụy hoa; cơ quan sinh sản cái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083081",
        "hw": "gynaecoid",
        "pos": "noun",
        "ipa": "/ˈɡaɪ.nəˌkɔɪd/",
        "vi": "kiến thợ đẻ trứng; dạng giống cái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083082",
        "hw": "gynaeolatry",
        "pos": "noun",
        "ipa": "/ˌdʒaɪ.niːˈɑː.lə.tri/",
        "vi": "sự tôn sùng phụ nữ quá mức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083083",
        "hw": "gynandromorph",
        "pos": "noun",
        "ipa": "/dʒaɪˈnæn.droʊˌmɔːrf/",
        "vi": "cá thể nửa đực nửa cái lưỡng phái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083084",
        "hw": "gynandromorphic",
        "pos": "adj",
        "ipa": "/dʒaɪˌnæn.droʊˈmɔːr.fɪk/",
        "vi": "mang đặc điểm nửa đực nửa cái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083085",
        "hw": "gynandromorphism",
        "pos": "noun",
        "ipa": "/dʒaɪˌnæn.droʊˈmɔːr.fɪz.əm/",
        "vi": "hiện tượng nửa đực nửa cái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083086",
        "hw": "gynandromorphous",
        "pos": "adj",
        "ipa": "/dʒaɪˌnæn.droʊˈmɔːr.fəs/",
        "vi": "thuộc thể dị dạng nửa đực nửa cái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083087",
        "hw": "gynandrophore",
        "pos": "noun",
        "ipa": "/dʒaɪˈnæn.drə.fɔːr/",
        "vi": "cuống nhị nhụy chung",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083088",
        "hw": "gynandrous",
        "pos": "adj",
        "ipa": "/dʒaɪˈnæn.drəs/",
        "vi": "có nhị và nhụy dính liền",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083089",
        "hw": "gynantherous",
        "pos": "adj",
        "ipa": "/ˌdʒaɪˈnæn.θɚ.əs/",
        "vi": "có nhị thoái hóa thành nhụy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083090",
        "hw": "gynanthropia",
        "pos": "noun",
        "ipa": "/ˌdʒaɪ.nænˈθroʊ.pi.ə/",
        "vi": "chứng nữ mang đặc tính nam",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083091",
        "hw": "gynarchy",
        "pos": "noun",
        "ipa": "/ˈdʒaɪ.nɑːr.ki/",
        "vi": "chế độ phụ nữ cầm quyền",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083092",
        "hw": "gynecocracy",
        "pos": "noun",
        "ipa": "/ˌdʒaɪ.nəˈkɑː.krə.si/",
        "vi": "chế độ nữ quyền thống trị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083093",
        "hw": "gyneolatry",
        "pos": "noun",
        "ipa": "/ˌdʒaɪ.niˈɑː.lə.tri/",
        "vi": "sự sùng bái tôn thờ phụ nữ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083094",
        "hw": "gynne",
        "pos": "noun",
        "ipa": "/ɡwɪn/",
        "vi": "nàng Nell Gwynne lịch sử",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083095",
        "hw": "gynobase",
        "pos": "noun",
        "ipa": "/ˈdʒaɪ.noʊ.beɪs/",
        "vi": "đế bầu nhụy phình to; đế nhụy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083096",
        "hw": "gynogenesis",
        "pos": "noun",
        "ipa": "/ˌdʒaɪ.noʊˈdʒɛn.ə.sɪs/",
        "vi": "sinh sản đơn tính cái noãn sào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083097",
        "hw": "gynophobia",
        "pos": "noun",
        "ipa": "/ˌdʒaɪ.nəˈfoʊ.bi.ə/",
        "vi": "hội chứng sợ phụ nữ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083098",
        "hw": "gynophore",
        "pos": "noun",
        "ipa": "/ˈdʒaɪ.nə.fɔːr/",
        "vi": "cuống nhụy hoa; chân bầu nhụy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083099",
        "hw": "gynosphinx",
        "pos": "noun",
        "ipa": "/ˈdʒaɪ.noʊ.sfɪŋks/",
        "vi": "nhân sư đầu phụ nữ mình sư tử",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083100",
        "hw": "gynostegium",
        "pos": "noun",
        "ipa": "/ˌdʒaɪ.noʊˈstiː.dʒi.əm/",
        "vi": "màng bọc dính nhị nhụy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083101",
        "hw": "gynura",
        "pos": "noun",
        "ipa": "/dʒaɪˈnjʊər.ə/",
        "vi": "chi cây bầu đất; cây lá nhung tím",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

# Validation
with open("scratch/b17_r07_raw_p1.json") as f:
    raw = json.load(f)

assert len(reviewed_records) == 100, f"Expected 100, got {len(reviewed_records)}"
assert len(raw) == 100, f"Expected 100 raw, got {len(raw)}"

for i, (rev, orig) in enumerate(zip(reviewed_records, raw)):
    assert rev["id"] == orig["id"], f"ID mismatch at {i}: {rev['id']} != {orig['id']}"
    assert rev["hw"] == orig["hw"], f"HW mismatch at {i}: {rev['hw']} != {orig['hw']}"
    assert rev["cefr"] == orig["cefr"], f"CEFR mismatch at {i}"
    assert rev["tier"] == orig["tier"], f"Tier mismatch at {i}"
    assert rev["notes"] == orig["notes"], f"Notes mismatch at {i}"
    assert rev["status"] == "reviewed", f"Status must be 'reviewed' at {i}"
    assert rev["vi"], f"vi is empty at {i}"
    assert len(rev["vi"]) <= 35, f"vi too long ({len(rev['vi'])} > 35) at {i}: {rev['vi']}"
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and len(rev["ipa"]) > 2, f"Invalid IPA at {i}: {rev['ipa']}"
    assert rev["ipa"].count("/") == 2, f"IPA slashes count != 2 at {i}: {rev['ipa']}"
    assert not rev["ipa"].startswith("/ ") and not rev["ipa"].endswith(" /"), f"Boundary spaces in IPA at {i}: {rev['ipa']}"
    assert rev["pos"] in ["noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"], f"Invalid pos at {i}: {rev['pos']}"

print("All 100 records in Part 1 verified successfully!")
