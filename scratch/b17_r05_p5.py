import json

reviewed_records = [
    {
        "id": "lex.en.100k.082402",
        "hw": "gosh",
        "pos": "intj",
        "ipa": "/ɡɑːʃ/",
        "vi": "chao ôi!; trời ơi!; úi chà",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082403",
        "hw": "goshaw",
        "pos": "noun",
        "ipa": "/ˈɡɑːs.hɔː/",
        "vi": "chim ưng ngỗng; chim ó",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082404",
        "hw": "gosmore",
        "pos": "noun",
        "ipa": "/ˈɡɑːs.mɔːr/",
        "vi": "cúc bồ công anh; rau bồ công anh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082405",
        "hw": "gospeler",
        "pos": "noun",
        "ipa": "/ˈɡɑː.spəl.ɚ/",
        "vi": "người truyền phúc âm; mục sư",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082406",
        "hw": "gospeller",
        "pos": "noun",
        "ipa": "/ˈɡɑː.spəl.ɚ/",
        "vi": "người truyền phúc âm; mục sư",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082407",
        "hw": "gosplan",
        "pos": "noun",
        "ipa": "/ˈɡɑːs.plæn/",
        "vi": "ủy ban kế hoạch nhà nước Liên Xô",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082408",
        "hw": "gospodar",
        "pos": "noun",
        "ipa": "/ɡəspəˈdɑːr/",
        "vi": "lãnh chúa; tổng đốc Walachia",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082409",
        "hw": "gospodars",
        "pos": "noun",
        "ipa": "/ɡəspəˈdɑːrz/",
        "vi": "các lãnh chúa; các tổng đốc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082410",
        "hw": "gossamery",
        "pos": "adj",
        "ipa": "/ˈɡɑː.sə.mɚ.i/",
        "vi": "mỏng nhẹ như tơ; thanh mảnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082411",
        "hw": "gossan",
        "pos": "noun",
        "ipa": "/ˈɡɑː.sən/",
        "vi": "mũ sắt; mạch quặng lộ rỉ sắt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082412",
        "hw": "gossanous",
        "pos": "adj",
        "ipa": "/ˈɡɑː.sə.nəs/",
        "vi": "thuộc mũ sắt; có mạch quặng rỉ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082413",
        "hw": "gossipmonger",
        "pos": "noun",
        "ipa": "/ˈɡɑː.sɪpˌmʌŋ.ɡɚ/",
        "vi": "kẻ ngồi lê đôi mách; kẻ mách lẻo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082414",
        "hw": "gossipmongering",
        "pos": "noun",
        "ipa": "/ˈɡɑː.sɪpˌmʌŋ.ɡɚ.ɪŋ/",
        "vi": "thói ngồi lê đôi mách; mách lẻo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082415",
        "hw": "gossipped",
        "pos": "verb",
        "ipa": "/ˈɡɑː.sɪpt/",
        "vi": "đã tán gẫu; đã ngồi lê đôi mách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082416",
        "hw": "gossipping",
        "pos": "verb",
        "ipa": "/ˈɡɑː.sɪp.ɪŋ/",
        "vi": "đang tán gẫu; ngồi lê đôi mách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082417",
        "hw": "gossipry",
        "pos": "noun",
        "ipa": "/ˈɡɑː.sɪp.ri/",
        "vi": "chuyện mách lẻo; sự tán gẫu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082418",
        "hw": "gossips",
        "pos": "verb",
        "ipa": "/ˈɡɑː.sɪps/",
        "vi": "tán gẫu; ngồi lê đôi mách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082419",
        "hw": "gossoon",
        "pos": "noun",
        "ipa": "/ɡəˈsuːn/",
        "vi": "cậu bé; chú bé; người hầu trai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082420",
        "hw": "got",
        "pos": "verb",
        "ipa": "/ɡɑːt/",
        "vi": "đã nhận được; đã có được; đã hiểu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082421",
        "hw": "gotcha",
        "pos": "noun",
        "ipa": "/ˈɡɑː.tʃə/",
        "vi": "cái bẫy bất ngờ; mánh khóe chơi xỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082422",
        "hw": "gothicism",
        "pos": "noun",
        "ipa": "/ˈɡɑː.θə.sɪz.əm/",
        "vi": "phong cách Goth; tinh thần Gothic",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082423",
        "hw": "gothicist",
        "pos": "noun",
        "ipa": "/ˈɡɑː.θə.sɪst/",
        "vi": "người theo phong cách Gothic",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082424",
        "hw": "gothicity",
        "pos": "noun",
        "ipa": "/ɡɑːˈθɪs.ə.ti/",
        "vi": "tính chất Gothic; nét Gothic",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082425",
        "hw": "gothite",
        "pos": "noun",
        "ipa": "/ˈɡoʊ.θaɪt/",
        "vi": "khoáng vật gơ-tit; quặng sắt nâu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082426",
        "hw": "gotta",
        "pos": "verb",
        "ipa": "/ˈɡɑː.t̬ə/",
        "vi": "phải; cần phải",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082427",
        "hw": "gotten",
        "pos": "verb",
        "ipa": "/ˈɡɑː.tən/",
        "vi": "đã nhận được; đã có được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082428",
        "hw": "gotterdammerung",
        "pos": "noun",
        "ipa": "/ˌɡɑː.tɚˈdæm.ɚ.ɪŋ/",
        "vi": "hoàng hôn chư thần; sự sụp đổ lớn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082429",
        "hw": "goud",
        "pos": "noun",
        "ipa": "/ɡaʊd/",
        "vi": "cây tùng lam; cây nhuộm vàng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082430",
        "hw": "goudron",
        "pos": "noun",
        "ipa": "/ɡuːˈdrɑːn/",
        "vi": "nhựa đường; hắc ín",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082431",
        "hw": "gouged",
        "pos": "verb",
        "ipa": "/ɡaʊdʒd/",
        "vi": "đã đục khoét; đã móc ra; đã ép giá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082432",
        "hw": "gouges",
        "pos": "verb",
        "ipa": "/ˈɡaʊ.dʒɪz/",
        "vi": "đục khoét; khoét lỗ; ép giá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082433",
        "hw": "gouging",
        "pos": "verb",
        "ipa": "/ˈɡaʊ.dʒɪŋ/",
        "vi": "đang đục khoét; móc ra; ép giá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082434",
        "hw": "goulashes",
        "pos": "noun",
        "ipa": "/ˈɡuː.lɑː.ʃɪz/",
        "vi": "các món thịt hầm goulash",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082435",
        "hw": "gourmandism",
        "pos": "noun",
        "ipa": "/ˈɡʊr.mən.dɪz.əm/",
        "vi": "thói phàm ăn; tính sành ăn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082436",
        "hw": "gourmandize",
        "pos": "verb",
        "ipa": "/ˈɡʊr.mən.daɪz/",
        "vi": "ăn uống vô độ; chén đẫy; ăn say mê",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082437",
        "hw": "gourmandizer",
        "pos": "noun",
        "ipa": "/ˈɡʊr.mən.daɪ.zɚ/",
        "vi": "kẻ phàm ăn; người sành ăn uống",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082438",
        "hw": "goutiness",
        "pos": "noun",
        "ipa": "/ˈɡaʊ.ti.nəs/",
        "vi": "tình trạng mắc bệnh gút; chứng gút",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082439",
        "hw": "goutwater",
        "pos": "noun",
        "ipa": "/ˈɡaʊtˌwɔː.t̬ɚ/",
        "vi": "nước mỏ chứa lưu huỳnh; nước sunfua",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082440",
        "hw": "governability",
        "pos": "noun",
        "ipa": "/ˌɡʌv.ɚ.nəˈbɪl.ə.ti/",
        "vi": "khả năng quản lý; tính dễ cai trị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082441",
        "hw": "governmentalism",
        "pos": "noun",
        "ipa": "/ˌɡʌv.ɚnˈmen.təlˌɪz.əm/",
        "vi": "chủ nghĩa chính phủ can thiệp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082442",
        "hw": "governmentalist",
        "pos": "noun",
        "ipa": "/ˌɡʌv.ɚnˈmen.təl.ɪst/",
        "vi": "người ủng hộ chính phủ can thiệp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082443",
        "hw": "governmentalize",
        "pos": "verb",
        "ipa": "/ˌɡʌv.ɚnˈmen.təl.aɪz/",
        "vi": "nhà nước hóa; chính phủ hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082444",
        "hw": "governments",
        "pos": "noun",
        "ipa": "/ˈɡʌv.ɚn.mənts/",
        "vi": "các chính phủ; các chính quyền",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082445",
        "hw": "governors",
        "pos": "noun",
        "ipa": "/ˈɡʌv.ɚ.nɚz/",
        "vi": "các thống đốc; các viên cai trị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082446",
        "hw": "governs",
        "pos": "verb",
        "ipa": "/ˈɡʌv.ɚnz/",
        "vi": "cai trị; quản lý; chi phối",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082447",
        "hw": "gowk",
        "pos": "noun",
        "ipa": "/ɡaʊk/",
        "vi": "chim cúc cu; kẻ ngốc nghếch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082448",
        "hw": "gowning",
        "pos": "verb",
        "ipa": "/ˈɡaʊ.nɪŋ/",
        "vi": "đang mặc áo choàng; mặc áo thụng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082449",
        "hw": "gowns",
        "pos": "verb",
        "ipa": "/ɡaʊnz/",
        "vi": "mặc áo choàng; mặc áo thụng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082450",
        "hw": "gownsman",
        "pos": "noun",
        "ipa": "/ˈɡaʊnz.mən/",
        "vi": "giáo sư đại học; luật sư; học giả",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082451",
        "hw": "grabbed",
        "pos": "verb",
        "ipa": "/ɡræbd/",
        "vi": "đã chộp lấy; đã vồ lấy; đã túm lấy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082452",
        "hw": "grabbing",
        "pos": "verb",
        "ipa": "/ˈɡræb.ɪŋ/",
        "vi": "đang chộp lấy; đang túm lấy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082453",
        "hw": "grabble",
        "pos": "verb",
        "ipa": "/ˈɡræb.əl/",
        "vi": "mò mẫm; sờ soạng tìm kiếm; bò toài",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082454",
        "hw": "grabbly",
        "pos": "adj",
        "ipa": "/ˈɡræb.li/",
        "vi": "ham vơ vét; tham lam vồ vập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082455",
        "hw": "graben",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.bən/",
        "vi": "địa hào; thung lũng kiến tạo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082456",
        "hw": "grabs",
        "pos": "verb",
        "ipa": "/ɡræbz/",
        "vi": "chộp lấy; vồ lấy; giật lấy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082457",
        "hw": "graced",
        "pos": "verb",
        "ipa": "/ɡreɪst/",
        "vi": "đã ban ơn; đã làm vinh dự cho",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082458",
        "hw": "gracelessness",
        "pos": "noun",
        "ipa": "/ˈɡreɪs.ləs.nəs/",
        "vi": "sự vụng về; sự thiếu duyên dáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082459",
        "hw": "graces",
        "pos": "verb",
        "ipa": "/ˈɡreɪ.sɪz/",
        "vi": "ban ơn; làm vẻ vang; tô điểm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082460",
        "hw": "gracilaria",
        "pos": "noun",
        "ipa": "/ˌɡræs.ɪˈlɛər.i.ə/",
        "vi": "chi rong câu; chi rau câu đỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082461",
        "hw": "gracilariid",
        "pos": "noun",
        "ipa": "/ˌɡræs.ɪ.ləˈraɪ.ɪd/",
        "vi": "ngài cánh hẹp; sâu đục lá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082462",
        "hw": "gracilariidae",
        "pos": "noun",
        "ipa": "/ˌɡræs.ɪ.ləˈraɪ.ə.diː/",
        "vi": "họ ngài cánh hẹp; họ bướm đục lá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082463",
        "hw": "gracilis",
        "pos": "noun",
        "ipa": "/ˈɡræs.ə.lɪs/",
        "vi": "cơ thon đùi; cơ thon",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082464",
        "hw": "gracility",
        "pos": "noun",
        "ipa": "/ɡrəˈsɪl.ə.ti/",
        "vi": "sự thanh mảnh; vẻ duyên dáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082465",
        "hw": "gracillariidae",
        "pos": "noun",
        "ipa": "/ˌɡræs.ɪ.ləˈraɪ.ə.diː/",
        "vi": "họ ngài cánh hẹp; họ bướm đục lá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082466",
        "hw": "gracing",
        "pos": "verb",
        "ipa": "/ˈɡreɪ.sɪŋ/",
        "vi": "đang tô điểm; làm vẻ vang; ban ơn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082467",
        "hw": "gracioso",
        "pos": "noun",
        "ipa": "/ɡrɑːˈsjoʊ.soʊ/",
        "vi": "nhân vật hề trong kịch Tây Ban Nha",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082468",
        "hw": "gracula",
        "pos": "noun",
        "ipa": "/ˈɡræk.jʊ.lə/",
        "vi": "chi chim yểng; chi chim nhồng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082469",
        "hw": "gradated",
        "pos": "verb",
        "ipa": "/ˈɡreɪ.deɪ.tɪd/",
        "vi": "đã chuyển tiếp dần; đã chia độ sắc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082470",
        "hw": "gradates",
        "pos": "verb",
        "ipa": "/ˈɡreɪ.deɪts/",
        "vi": "chuyển tiếp dần; biến thiên độ màu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082471",
        "hw": "gradating",
        "pos": "verb",
        "ipa": "/ˈɡreɪ.deɪ.tɪŋ/",
        "vi": "đang chuyển dần; hòa sắc biến thiên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082472",
        "hw": "gradationally",
        "pos": "adv",
        "ipa": "/ɡreɪˈdeɪ.ʃən.əl.i/",
        "vi": "theo từng mức; một cách chuyển dần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082473",
        "hw": "gradations",
        "pos": "noun",
        "ipa": "/ɡreɪˈdeɪ.ʃənz/",
        "vi": "các cấp bậc; các mức chuyển đổi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082474",
        "hw": "gradatory",
        "pos": "adj",
        "ipa": "/ˈɡræd.ə.tɔːr.i/",
        "vi": "từng bước một; có thứ bậc dần dần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082475",
        "hw": "gradebuilder",
        "pos": "noun",
        "ipa": "/ˈɡreɪdˌbɪl.dɚ/",
        "vi": "máy san ủi đất; máy san nền đường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082476",
        "hw": "grades",
        "pos": "verb",
        "ipa": "/ɡreɪdz/",
        "vi": "chấm điểm; xếp loại; phân hạng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082477",
        "hw": "gradienter",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.di.ən.tɚ/",
        "vi": "máy đo độ dốc; máy đo cao trình",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082478",
        "hw": "gradin",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.dɪn/",
        "vi": "bậc giật cấp; hàng ghế khán đài",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082479",
        "hw": "gradine",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.diːn/",
        "vi": "đục răng điêu khắc; bục bệ thờ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082480",
        "hw": "gradiometer",
        "pos": "noun",
        "ipa": "/ˌɡreɪ.diˈɑː.mɪ.t̬ɚ/",
        "vi": "máy đo građien; máy đo độ dốc từ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082481",
        "hw": "gradiometers",
        "pos": "noun",
        "ipa": "/ˌɡreɪ.diˈɑː.mɪ.t̬ɚz/",
        "vi": "các máy đo građien; máy đo độ dốc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082482",
        "hw": "gradology",
        "pos": "noun",
        "ipa": "/ɡreɪˈdɑː.lə.dʒi/",
        "vi": "khoa nghiên cứu quá trình phân cấp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082483",
        "hw": "gradualism",
        "pos": "noun",
        "ipa": "/ˈɡrædʒ.u.əlˌɪz.əm/",
        "vi": "chủ nghĩa tiệm tiến; tính dần dần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082484",
        "hw": "graduality",
        "pos": "noun",
        "ipa": "/ˌɡrædʒ.uˈæl.ə.ti/",
        "vi": "tính tiệm tiến; tính chất dần dần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082485",
        "hw": "gradualness",
        "pos": "noun",
        "ipa": "/ˈɡrædʒ.u.əl.nəs/",
        "vi": "tính từ từ; tính chất tiệm tiến",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082486",
        "hw": "graduates",
        "pos": "verb",
        "ipa": "/ˈɡrædʒ.u.eɪts/",
        "vi": "tốt nghiệp; phân cấp; chia độ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082487",
        "hw": "graduateship",
        "pos": "noun",
        "ipa": "/ˈɡrædʒ.u.ət.ʃɪp/",
        "vi": "tư cách người tốt nghiệp đại học",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082488",
        "hw": "graduating",
        "pos": "verb",
        "ipa": "/ˈɡrædʒ.u.eɪ.tɪŋ/",
        "vi": "đang tốt nghiệp; chia độ vạch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082489",
        "hw": "graduator",
        "pos": "noun",
        "ipa": "/ˈɡrædʒ.u.eɪ.t̬ɚ/",
        "vi": "dụng cụ khắc vạch; máy chia độ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082490",
        "hw": "gradus",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.dəs/",
        "vi": "từ điển thi luật La-tinh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082491",
        "hw": "graecism",
        "pos": "noun",
        "ipa": "/ˈɡriː.sɪz.əm/",
        "vi": "từ ngữ Hy Lạp; phong cách Hy Lạp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082492",
        "hw": "graecophile",
        "pos": "adj",
        "ipa": "/ˈɡriː.sə.faɪl/",
        "vi": "yêu Hy Lạp; chuộng văn hóa Hy Lạp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082493",
        "hw": "graecophilic",
        "pos": "adj",
        "ipa": "/ˌɡriː.səˈfɪl.ɪk/",
        "vi": "yêu Hy Lạp; chuộng văn hóa Hy Lạp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082494",
        "hw": "grafin",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.fɪn/",
        "vi": "nữ bá tước Đức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082495",
        "hw": "graftage",
        "pos": "noun",
        "ipa": "/ˈɡræf.tɪdʒ/",
        "vi": "kỹ thuật ghép cây; nghề ghép cành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082496",
        "hw": "grafted",
        "pos": "verb",
        "ipa": "/ˈɡræf.tɪd/",
        "vi": "đã cấy ghép mô; đã ghép cành cây",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082497",
        "hw": "grafter",
        "pos": "noun",
        "ipa": "/ˈɡræf.tɚ/",
        "vi": "dao ghép cây; kẻ nhận hối lộ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082498",
        "hw": "graftings",
        "pos": "noun",
        "ipa": "/ˈɡræf.tɪŋz/",
        "vi": "các mối cấy ghép; các chồi ghép",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082499",
        "hw": "grafts",
        "pos": "verb",
        "ipa": "/ɡræfts/",
        "vi": "ghép cành; cấy ghép mô; ăn hối lộ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082500",
        "hw": "grainer",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.nɚ/",
        "vi": "thợ tạo vân gỗ giả; dao cạo da",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082501",
        "hw": "grainfield",
        "pos": "noun",
        "ipa": "/ˈɡreɪn.fiːld/",
        "vi": "cánh đồng ngũ cốc; ruộng lúa mì",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

# Validation
with open("scratch/b17_r05_raw_p5.json") as f:
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

print("All 100 records in Part 5 verified successfully!")
