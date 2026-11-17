import json

reviewed_items = [
    {
        "id": "lex.en.200k.042802",
        "hw": "bustiest",
        "pos": "adj",
        "ipa": "/ˈbʌstiəst/",
        "vi": "có vòng một đẫy đà nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042803",
        "hw": "callouses",
        "pos": "verb",
        "ipa": "/ˈkæləsɪz/",
        "vi": "làm cho chai sần; chai sạn đi",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042804",
        "hw": "callousing",
        "pos": "verb",
        "ipa": "/ˈkæləsɪŋ/",
        "vi": "đang làm cho chai sần, chai sạn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042805",
        "hw": "cantoneses",
        "pos": "noun",
        "ipa": "/ˌkæntəˈniːzɪz/",
        "vi": "những người nói tiếng Quảng Đông",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042806",
        "hw": "casablancas",
        "pos": "noun",
        "ipa": "/ˌkæsəˈblæŋkəz/",
        "vi": "các thành phố Casablanca",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042807",
        "hw": "casseroles",
        "pos": "noun",
        "ipa": "/ˈkæsəroʊlz/",
        "vi": "những món thịt hầm đút lò",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042808",
        "hw": "coons",
        "pos": "noun",
        "ipa": "/kuːnz/",
        "vi": "những con gấu trúc bắc Mỹ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042809",
        "hw": "cubicles",
        "pos": "noun",
        "ipa": "/ˈkjuːbɪklz/",
        "vi": "các khoang làm việc văn phòng",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042810",
        "hw": "daintier",
        "pos": "adj",
        "ipa": "/ˈdeɪntiər/",
        "vi": "xinh xắn hơn; thanh nhã hơn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042811",
        "hw": "dainties",
        "pos": "noun",
        "ipa": "/ˈdeɪntiz/",
        "vi": "những món sơn hào hải vị ngon",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042812",
        "hw": "daintiest",
        "pos": "adj",
        "ipa": "/ˈdeɪntiəst/",
        "vi": "xinh xắn nhất; thanh nhã nhất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042813",
        "hw": "devis",
        "pos": "noun",
        "ipa": "/ˈdeɪviːz/",
        "vi": "các hiện thân của nữ thần Devi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042814",
        "hw": "dietriches",
        "pos": "noun",
        "ipa": "/ˈdiːtrɪkɪz/",
        "vi": "các nhân vật mang tên Dietrich",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042815",
        "hw": "dilutions",
        "pos": "noun",
        "ipa": "/daɪˈluːʃənz/",
        "vi": "các độ pha loãng dung dịch",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042816",
        "hw": "drugstores",
        "pos": "noun",
        "ipa": "/ˈdrʌɡstɔːrz/",
        "vi": "những tiệm thuốc tây; hiệu thuốc",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042817",
        "hw": "ejections",
        "pos": "noun",
        "ipa": "/ɪˈdʒɛkʃənz/",
        "vi": "các sự tống khứ; việc phóng ra",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042818",
        "hw": "electrolytes",
        "pos": "noun",
        "ipa": "/ɪˈlɛktrəlaɪts/",
        "vi": "các chất điện giải sinh hóa",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042819",
        "hw": "elitists",
        "pos": "noun",
        "ipa": "/eɪˈliːtɪsts/",
        "vi": "những người theo phái tinh hoa",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042820",
        "hw": "equines",
        "pos": "noun",
        "ipa": "/ˈiːkwaɪnz/",
        "vi": "các động vật thuộc họ ngựa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042821",
        "hw": "faucets",
        "pos": "noun",
        "ipa": "/ˈfɔːsɪts/",
        "vi": "những chiếc vòi nước máy",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042822",
        "hw": "fausts",
        "pos": "noun",
        "ipa": "/faʊsts/",
        "vi": "những bi kịch kịch bản Faust",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042823",
        "hw": "fdrs",
        "pos": "noun",
        "ipa": "/ˌɛf diː ˈɑːrz/",
        "vi": "các tài liệu tổng thống FDR",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042824",
        "hw": "feistier",
        "pos": "adj",
        "ipa": "/ˈfaɪstiər/",
        "vi": "gan dạ hiếu chiến hơn; hăng hơn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042825",
        "hw": "feistiest",
        "pos": "adj",
        "ipa": "/ˈfaɪstiəst/",
        "vi": "gan dạ hiếu chiến nhất; hăng nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042826",
        "hw": "finked",
        "pos": "verb",
        "ipa": "/fɪŋkt/",
        "vi": "đã mật báo; đã đâm sau lưng",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042827",
        "hw": "finking",
        "pos": "verb",
        "ipa": "/ˈfɪŋkɪŋ/",
        "vi": "đang mật báo; đâm sau lưng",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042828",
        "hw": "finks",
        "pos": "noun",
        "ipa": "/fɪŋks/",
        "vi": "những kẻ phản bội điểm chỉ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042829",
        "hw": "footholds",
        "pos": "noun",
        "ipa": "/ˈfʊthoʊldz/",
        "vi": "những chỗ đặt chân; bàn đạp đứng",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042830",
        "hw": "forbiddings",
        "pos": "noun",
        "ipa": "/fərˈbɪdɪŋz/",
        "vi": "những lời răn cấm ngăn trở",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042831",
        "hw": "fouriers",
        "pos": "noun",
        "ipa": "/ˈfʊrieɪz/",
        "vi": "các phép biến đổi toán học Fourier",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042832",
        "hw": "frauen",
        "pos": "noun",
        "ipa": "/ˈfraʊən/",
        "vi": "những người phụ nữ Đức",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042833",
        "hw": "fraus",
        "pos": "noun",
        "ipa": "/fraʊz/",
        "vi": "những bà phu nhân người Đức",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042834",
        "hw": "ghastlier",
        "pos": "adj",
        "ipa": "/ˈɡæstliər/",
        "vi": "rùng rợn hơn; ghê rợn hơn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042835",
        "hw": "ghastliest",
        "pos": "adj",
        "ipa": "/ˈɡæstliəst/",
        "vi": "rùng rợn nhất; kinh khủng nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042836",
        "hw": "gias",
        "pos": "noun",
        "ipa": "/ˌdʒiː aɪ ˈeɪz/",
        "vi": "các viện giám định đá quý GIA",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042837",
        "hw": "hairlines",
        "pos": "noun",
        "ipa": "/ˈhɛrlaɪnz/",
        "vi": "những đường chân tóc trán",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042838",
        "hw": "handsets",
        "pos": "noun",
        "ipa": "/ˈhændsɛts/",
        "vi": "những thiết bị tay nghe cầm tay",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042839",
        "hw": "heiresses",
        "pos": "noun",
        "ipa": "/ˈɛrəsɪz/",
        "vi": "những cô tiểu thư nữ thừa kế",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042840",
        "hw": "hhses",
        "pos": "noun",
        "ipa": "/ˌeɪtʃ eɪtʃ ˈɛsɪz/",
        "vi": "các văn phòng Bộ Y tế Mỹ HHS",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042841",
        "hw": "holsters",
        "pos": "noun",
        "ipa": "/ˈhoʊlstərz/",
        "vi": "những bao da đựng súng ngắn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042842",
        "hw": "huntsvilles",
        "pos": "noun",
        "ipa": "/ˈhʌntsvɪlz/",
        "vi": "các địa danh thành phố Huntsville",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042843",
        "hw": "issuers",
        "pos": "noun",
        "ipa": "/ˈɪʃuərz/",
        "vi": "các tổ chức phát hành chứng khoán",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042844",
        "hw": "kegs",
        "pos": "noun",
        "ipa": "/kɛɡz/",
        "vi": "những thùng chứa bia kim loại",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042845",
        "hw": "kissingers",
        "pos": "noun",
        "ipa": "/ˈkɪsɪndʒərz/",
        "vi": "các phân tích ngoại giao Kissinger",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042846",
        "hw": "lancets",
        "pos": "noun",
        "ipa": "/ˈlænsɪts/",
        "vi": "những lưỡi dao chích y tế nhọn",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042847",
        "hw": "landfalls",
        "pos": "noun",
        "ipa": "/ˈlændfɔːlz/",
        "vi": "những lần bão đổ bộ vào bờ biển",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042848",
        "hw": "lawmakers",
        "pos": "noun",
        "ipa": "/ˈlɔːmeɪkərz/",
        "vi": "những nhà làm luật lập pháp",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042849",
        "hw": "leningrads",
        "pos": "noun",
        "ipa": "/ˈlɛnɪnɡrædz/",
        "vi": "các di tích lịch sử Leningrad",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042850",
        "hw": "lerners",
        "pos": "noun",
        "ipa": "/ˈlɜːrnərz/",
        "vi": "những người mang họ Lerner",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042851",
        "hw": "lifeguards",
        "pos": "noun",
        "ipa": "/ˈlaɪfɡɑːrdz/",
        "vi": "những nhân viên cứu hộ bãi biển",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042852",
        "hw": "limericks",
        "pos": "noun",
        "ipa": "/ˈlɪmərɪks/",
        "vi": "những bài thơ năm câu hài hước",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042853",
        "hw": "lolitas",
        "pos": "noun",
        "ipa": "/loʊˈliːtəz/",
        "vi": "những phong cách thời trang Lolita",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042854",
        "hw": "loners",
        "pos": "noun",
        "ipa": "/ˈloʊnərz/",
        "vi": "những người ưa sống thu mình",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042855",
        "hw": "loyolas",
        "pos": "noun",
        "ipa": "/lɔɪˈoʊləz/",
        "vi": "các trường viện Dòng Tên Loyola",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042856",
        "hw": "mcmasters",
        "pos": "noun",
        "ipa": "/məkˈmæstərz/",
        "vi": "những người mang họ McMaster",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042857",
        "hw": "moguls",
        "pos": "noun",
        "ipa": "/ˈmoʊɡəlz/",
        "vi": "những ông trùm tài phiệt lớn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042858",
        "hw": "monets",
        "pos": "noun",
        "ipa": "/moʊˈneɪz/",
        "vi": "các kiệt tác danh họa Claude Monet",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042859",
        "hw": "morphed",
        "pos": "verb",
        "ipa": "/mɔːrft/",
        "vi": "đã biến hóa hình dạng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042860",
        "hw": "morphs",
        "pos": "verb",
        "ipa": "/mɔːrfs/",
        "vi": "biến đổi dần về hình thái",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042861",
        "hw": "musas",
        "pos": "noun",
        "ipa": "/ˈmjuːsəz/",
        "vi": "các loài thực vật thuộc chi chuối",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042862",
        "hw": "nimbler",
        "pos": "adj",
        "ipa": "/ˈnɪmblər/",
        "vi": "nhanh nhẹn hơn; hoạt bát hơn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042863",
        "hw": "nimblest",
        "pos": "adj",
        "ipa": "/ˈnɪmblɪst/",
        "vi": "nhanh nhẹn nhất; lanh lợi nhất",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042864",
        "hw": "nomads",
        "pos": "noun",
        "ipa": "/ˈnoʊmædz/",
        "vi": "những người dân sống du mục",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042865",
        "hw": "nrcs",
        "pos": "noun",
        "ipa": "/ˌɛn ɑːr ˈsiːz/",
        "vi": "các ủy ban điều tiết hạt nhân NRC",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042866",
        "hw": "pathfinders",
        "pos": "noun",
        "ipa": "/ˈpæθfaɪndərz/",
        "vi": "những người khai phá mở đường",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042867",
        "hw": "pediatricians",
        "pos": "noun",
        "ipa": "/ˌpiːdiəˈtrɪʃənz/",
        "vi": "những bác sĩ chuyên khoa nhi",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042868",
        "hw": "pembrokes",
        "pos": "noun",
        "ipa": "/ˈpɛmbroʊks/",
        "vi": "những giống chó corgi Pembroke",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042869",
        "hw": "penchants",
        "pos": "noun",
        "ipa": "/ˈpɛntʃənts/",
        "vi": "những thiên hướng sở thích riêng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042870",
        "hw": "ponytails",
        "pos": "noun",
        "ipa": "/ˈpoʊniteɪlz/",
        "vi": "những mái tóc cột đuôi ngựa",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042871",
        "hw": "poplars",
        "pos": "noun",
        "ipa": "/ˈpɑːplərz/",
        "vi": "những hàng cây thân gỗ bạch dương",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042872",
        "hw": "quorums",
        "pos": "noun",
        "ipa": "/ˈkwɔːrəmz/",
        "vi": "các túc số đại biểu tối thiểu",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042873",
        "hw": "rascals",
        "pos": "noun",
        "ipa": "/ˈræsklz/",
        "vi": "những kẻ ranh ma; đứa nghịch ngợm",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042874",
        "hw": "revues",
        "pos": "noun",
        "ipa": "/rɪˈvjuːz/",
        "vi": "những buổi biểu diễn kịch tạp kỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042875",
        "hw": "rigors",
        "pos": "noun",
        "ipa": "/ˈrɪɡərz/",
        "vi": "những nỗi gian khổ; tính khắt khe",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042876",
        "hw": "roanokes",
        "pos": "noun",
        "ipa": "/ˈroʊənoʊks/",
        "vi": "các khu định cư đảo Roanoke",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042877",
        "hw": "ropers",
        "pos": "noun",
        "ipa": "/ˈroʊpərz/",
        "vi": "những tay cao bồi quăng thòng lọng",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042878",
        "hw": "scotsmans",
        "pos": "noun",
        "ipa": "/ˈskɑːtsmənz/",
        "vi": "những người đàn ông Scotland",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042879",
        "hw": "seatbelts",
        "pos": "noun",
        "ipa": "/ˈsiːtbɛlts/",
        "vi": "những sợi dây đai an toàn xe",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042880",
        "hw": "shanks",
        "pos": "noun",
        "ipa": "/ʃæŋks/",
        "vi": "những khúc thịt bắp chân ống cẳng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042881",
        "hw": "shortlisted",
        "pos": "verb",
        "ipa": "/ˈʃɔːrtlɪstɪd/",
        "vi": "đã chọn lọc vào danh sách rút gọn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042882",
        "hw": "shortlisting",
        "pos": "verb",
        "ipa": "/ˈʃɔːrtlɪstɪŋ/",
        "vi": "đang chọn lọc vào danh sách rút gọn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042883",
        "hw": "shortlists",
        "pos": "noun",
        "ipa": "/ˈʃɔːrtlɪsts/",
        "vi": "các bảng danh sách ứng viên rút gọn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042884",
        "hw": "sidebars",
        "pos": "noun",
        "ipa": "/ˈsaɪdbɑːrz/",
        "vi": "những thanh cạnh bên lề trang web",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042885",
        "hw": "sociopaths",
        "pos": "noun",
        "ipa": "/ˈsoʊsiəpæθs/",
        "vi": "những kẻ có tâm lý chống xã hội",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042886",
        "hw": "spocks",
        "pos": "noun",
        "ipa": "/spɑːks/",
        "vi": "các nhân vật thuyền phó Spock",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042887",
        "hw": "squeakier",
        "pos": "adj",
        "ipa": "/ˈskwiːkiər/",
        "vi": "phát tiếng kẽo kẹt chói tai hơn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042888",
        "hw": "squeakiest",
        "pos": "adj",
        "ipa": "/ˈskwiːkiəst/",
        "vi": "phát tiếng kẽo kẹt chói tai nhất",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042889",
        "hw": "steamships",
        "pos": "noun",
        "ipa": "/ˈstiːmʃɪps/",
        "vi": "những con tàu thủy hơi nước lớn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042890",
        "hw": "telecasts",
        "pos": "noun",
        "ipa": "/ˈtɛlɪkæsts/",
        "vi": "những chương trình phát sóng TV",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042891",
        "hw": "testimonials",
        "pos": "noun",
        "ipa": "/ˌtɛstəˈmoʊniəlz/",
        "vi": "những lời chứng thực khen ngợi",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042892",
        "hw": "toners",
        "pos": "noun",
        "ipa": "/ˈtoʊnərz/",
        "vi": "hộp mực in máy; nước hoa hồng da",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042893",
        "hw": "trashier",
        "pos": "adj",
        "ipa": "/ˈtræʃiər/",
        "vi": "kém chất lượng hơn; tồi tàn hơn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042894",
        "hw": "trashiest",
        "pos": "adj",
        "ipa": "/ˈtræʃiəst/",
        "vi": "kém chất lượng nhất; tồi tàn nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042895",
        "hw": "trimesters",
        "pos": "noun",
        "ipa": "/traɪˈmɛstərz/",
        "vi": "các kỳ ba tháng thai kỳ; học kỳ ba",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042896",
        "hw": "tullies",
        "pos": "noun",
        "ipa": "/ˈtʌliz/",
        "vi": "các thành viên gia tộc Tully",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042897",
        "hw": "unholier",
        "pos": "adj",
        "ipa": "/ʌnˈhoʊliər/",
        "vi": "tội lỗi đồi bại hơn; kém thiêng hơn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042898",
        "hw": "unholiest",
        "pos": "adj",
        "ipa": "/ʌnˈhoʊliəst/",
        "vi": "tội lỗi nhất; bất kính thiêng nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042899",
        "hw": "virgos",
        "pos": "noun",
        "ipa": "/ˈvɜːrɡoʊz/",
        "vi": "những người thuộc chòm sao Xử Nữ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042900",
        "hw": "yiddishes",
        "pos": "noun",
        "ipa": "/ˈjɪdɪʃɪz/",
        "vi": "các ngôn ngữ tiếng Do Thái Yiddish",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042901",
        "hw": "acceptor rna",
        "pos": "phrase",
        "ipa": "/ækˈsɛptər ˌɑːr ɛn ˈeɪ/",
        "vi": "ARN vận chuyển tiếp nhận axit amin",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r06_raw_p4.json') as f:
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

with open('scratch/b29_r06_p4.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 6 Part 4 verified and written successfully.")
