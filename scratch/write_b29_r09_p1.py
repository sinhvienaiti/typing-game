import json

reviewed_items = [
    {
        "id": "lex.en.200k.044002",
        "hw": "eurasiae",
        "pos": "noun",
        "ipa": "/jʊəˈreɪʒə/",
        "vi": "đại lục Á-Âu; vùng Âu-Á",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044003",
        "hw": "expats",
        "pos": "noun",
        "ipa": "/ˈɛkspæts/",
        "vi": "kiều dân; người định cư nước ngoài",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044004",
        "hw": "eyelids",
        "pos": "noun",
        "ipa": "/ˈaɪlɪdz/",
        "vi": "những mí mắt; mi mắt trên dưới",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044005",
        "hw": "financiers",
        "pos": "noun",
        "ipa": "/ˌfɪnənˈsɪrz/",
        "vi": "chuyên gia tài chính; nhà tài phiệt",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044006",
        "hw": "ftps",
        "pos": "noun",
        "ipa": "/ˌɛf tiː ˈpiːz/",
        "vi": "giao thức truyền tệp tin mạng máy",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044007",
        "hw": "gangstas",
        "pos": "noun",
        "ipa": "/ˈɡæŋstəz/",
        "vi": "dân giang hồ đường phố; dân anh chị",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044008",
        "hw": "hindrances",
        "pos": "noun",
        "ipa": "/ˈhɪndrənsɪz/",
        "vi": "những chướng ngại; vật cản trở lại",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044009",
        "hw": "hulas",
        "pos": "noun",
        "ipa": "/ˈhuːləz/",
        "vi": "các điệu múa hula truyền thống đảo",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044010",
        "hw": "huxleys",
        "pos": "noun",
        "ipa": "/ˈhʌksliz/",
        "vi": "những người mang họ Huxley",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044011",
        "hw": "immunizations",
        "pos": "noun",
        "ipa": "/ˌɪmjʊnəˈzeɪʃənz/",
        "vi": "các đợt tiêm chủng tạo miễn dịch",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044012",
        "hw": "incas",
        "pos": "noun",
        "ipa": "/ˈɪŋkəz/",
        "vi": "người Inca; các vị hoàng đế Inca",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044013",
        "hw": "innovators",
        "pos": "noun",
        "ipa": "/ˈɪnəveɪtərz/",
        "vi": "những nhà đổi mới sáng tạo tài năng",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044014",
        "hw": "intermissions",
        "pos": "noun",
        "ipa": "/ˌɪntərˈmɪʃənz/",
        "vi": "giờ nghỉ giải lao giữa buổi diễn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044015",
        "hw": "landlines",
        "pos": "noun",
        "ipa": "/ˈlændlaɪnz/",
        "vi": "những chiếc điện thoại cố định bàn",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044016",
        "hw": "liberians",
        "pos": "noun",
        "ipa": "/laɪˈbɪriənz/",
        "vi": "người Liberia; cư dân nước Liberia",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044017",
        "hw": "lingoes",
        "pos": "noun",
        "ipa": "/ˈlɪŋɡoʊz/",
        "vi": "tiếng lóng biệt ngữ chuyên ngành",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044018",
        "hw": "lohans",
        "pos": "noun",
        "ipa": "/ˈloʊhænz/",
        "vi": "những người họ Lohan; tượng La Hán",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044019",
        "hw": "marlins",
        "pos": "noun",
        "ipa": "/ˈmɑːrlɪnz/",
        "vi": "những con cá cờ mũi kiếm đại dương",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044020",
        "hw": "matrons",
        "pos": "noun",
        "ipa": "/ˈmeɪtrənz/",
        "vi": "phụ nữ có tuổi; nữ quản lý ký túc",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044021",
        "hw": "meatier",
        "pos": "adj",
        "ipa": "/ˈmiːtiər/",
        "vi": "nhiều thịt hơn; sâu sắc phong phú",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044022",
        "hw": "meatiest",
        "pos": "adj",
        "ipa": "/ˈmiːtiɪst/",
        "vi": "nhiều thịt nhất; sâu sắc nhất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044023",
        "hw": "mouthfuls",
        "pos": "noun",
        "ipa": "/ˈmaʊθfʊlz/",
        "vi": "những miếng ngậm đầy miệng; hớp đầy",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044024",
        "hw": "neoliberals",
        "pos": "noun",
        "ipa": "/ˌniːoʊˈlɪbərəlz/",
        "vi": "những người theo phái tân tự do",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044025",
        "hw": "oateses",
        "pos": "noun",
        "ipa": "/ˈoʊtsɪz/",
        "vi": "những người mang họ Oates",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044026",
        "hw": "outflows",
        "pos": "noun",
        "ipa": "/ˈaʊtfloʊz/",
        "vi": "dòng chảy ra ngoài; luồng tiền ra",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044027",
        "hw": "outperformed",
        "pos": "verb",
        "ipa": "/ˌaʊtpərˈfɔːrmd/",
        "vi": "đã thể hiện vượt trội; làm tốt hơn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044028",
        "hw": "outperforming",
        "pos": "verb",
        "ipa": "/ˌaʊtpərˈfɔːrmɪŋ/",
        "vi": "đang làm tốt hơn; vượt trội hơn hẳn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044029",
        "hw": "outperforms",
        "pos": "verb",
        "ipa": "/ˌaʊtpərˈfɔːrmz/",
        "vi": "làm tốt hơn; vượt trội hơn hẳn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044030",
        "hw": "overtures",
        "pos": "noun",
        "ipa": "/ˈoʊvərtʃʊrz/",
        "vi": "khúc dạo đầu; lời gợi ý làm quen",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044031",
        "hw": "parrs",
        "pos": "noun",
        "ipa": "/pɑːrz/",
        "vi": "cá hồi chấm con thời kỳ lớn nhanh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044032",
        "hw": "pepperonis",
        "pos": "noun",
        "ipa": "/ˌpɛpəˈroʊniz/",
        "vi": "xúc xích bò lợn cay pepperoni Ý",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044033",
        "hw": "peses",
        "pos": "noun",
        "ipa": "/ˈpiːziːz/",
        "vi": "bàn chân động vật; bàn chân người",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044034",
        "hw": "pleistocenes",
        "pos": "noun",
        "ipa": "/ˈplaɪstəsiːnz/",
        "vi": "các thời kỳ thuộc thế Canh Tân",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044035",
        "hw": "poxes",
        "pos": "noun",
        "ipa": "/ˈpɑːksɪz/",
        "vi": "các chứng bệnh phát ban đậu mùa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044036",
        "hw": "pretenses",
        "pos": "noun",
        "ipa": "/prɪˈtɛnsɪz/",
        "vi": "thái độ giả dối; sự làm bộ làm tịch",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044037",
        "hw": "puritans",
        "pos": "noun",
        "ipa": "/ˈpjʊrɪtənz/",
        "vi": "người theo phái Thanh giáo khắt khe",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044038",
        "hw": "quarts",
        "pos": "noun",
        "ipa": "/kwɔːrts/",
        "vi": "các đơn vị thể tích quart nước Mỹ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044039",
        "hw": "rabbles",
        "pos": "noun",
        "ipa": "/ˈræblz/",
        "vi": "đám đông dân đen hỗn loạn bát nháo",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044040",
        "hw": "raisins",
        "pos": "noun",
        "ipa": "/ˈreɪznz/",
        "vi": "những chùm nho khô sấy ngọt lịm",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044041",
        "hw": "redeemers",
        "pos": "noun",
        "ipa": "/rɪˈdiːmərz/",
        "vi": "người chuộc tội; đấng cứu thế",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044042",
        "hw": "rhapsodies",
        "pos": "noun",
        "ipa": "/ˈræpsədiz/",
        "vi": "bản cuồng tưởng khúc; lời khen ngợi",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044043",
        "hw": "rheas",
        "pos": "noun",
        "ipa": "/ˈriːəz/",
        "vi": "nữ thần Rhea; chim đà điểu Nam Mỹ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044044",
        "hw": "rousseaus",
        "pos": "noun",
        "ipa": "/ruːˈsoʊz/",
        "vi": "những người mang họ Rousseau",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044045",
        "hw": "ruddier",
        "pos": "adj",
        "ipa": "/ˈrʌdiər/",
        "vi": "hồng hào khỏe mạnh hơn; đỏ au hơn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044046",
        "hw": "ruddiest",
        "pos": "adj",
        "ipa": "/ˈrʌdiɪst/",
        "vi": "hồng hào khỏe mạnh nhất; đỏ au nhất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044047",
        "hw": "runes",
        "pos": "noun",
        "ipa": "/ruːnz/",
        "vi": "ký tự chữ rune cổ; mật mã phù phép",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044048",
        "hw": "sahibs",
        "pos": "noun",
        "ipa": "/ˈsɑːhɪbz/",
        "vi": "ông chủ; các ngài da trắng ở Ấn Độ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044049",
        "hw": "schisms",
        "pos": "noun",
        "ipa": "/ˈskɪzəmz/",
        "vi": "sự phân liệt giáo phái; sự ly giáo",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044050",
        "hw": "seers",
        "pos": "noun",
        "ipa": "/ˈsiːərz/",
        "vi": "nhà thấu thị; tiên tri thấy trước",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044051",
        "hw": "sewards",
        "pos": "noun",
        "ipa": "/ˈsuːərdz/",
        "vi": "những người mang họ Seward",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044052",
        "hw": "shippers",
        "pos": "noun",
        "ipa": "/ˈʃɪpərz/",
        "vi": "chủ hàng hóa; bên giao vận hàng gửi",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044053",
        "hw": "snappier",
        "pos": "adj",
        "ipa": "/ˈsnæpiər/",
        "vi": "linh hoạt hơn; dễ cáu kỉnh hơn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044054",
        "hw": "snappiest",
        "pos": "adj",
        "ipa": "/ˈsnæpiɪst/",
        "vi": "nhanh nhẹn linh hoạt nhất; gắt nhất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044055",
        "hw": "snowboarded",
        "pos": "verb",
        "ipa": "/ˈsnoʊbɔːrdɪd/",
        "vi": "đã trượt ván tuyết trên dốc núi",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044056",
        "hw": "snowboards",
        "pos": "noun",
        "ipa": "/ˈsnoʊbɔːrdz/",
        "vi": "những tấm ván trượt trên tuyết",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044057",
        "hw": "solitaires",
        "pos": "noun",
        "ipa": "/ˈsɑːlətɛrz/",
        "vi": "nhẫn đính một hột ngọc; trò xếp bài",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044058",
        "hw": "spiegels",
        "pos": "noun",
        "ipa": "/ˈʃpiːɡəlz/",
        "vi": "loại gang kính spiegel luyện thép",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044059",
        "hw": "stanzas",
        "pos": "noun",
        "ipa": "/ˈstænzəz/",
        "vi": "các khổ thơ; đoạn thơ bốn câu mẫu",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044060",
        "hw": "stipends",
        "pos": "noun",
        "ipa": "/ˈstaɪpɛndz/",
        "vi": "tiền trợ cấp sinh hoạt; lương tu sĩ",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044061",
        "hw": "tecs",
        "pos": "noun",
        "ipa": "/tɛks/",
        "vi": "các thám tử tư điều tra vụ việc",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044062",
        "hw": "titties",
        "pos": "noun",
        "ipa": "/ˈtɪtiz/",
        "vi": "bộ ngực phụ nữ; đôi gò bồng đảo",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044063",
        "hw": "tsked",
        "pos": "verb",
        "ipa": "/tɪkst/",
        "vi": "đã chép miệng tặc lưỡi bực mình",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044064",
        "hw": "tsking",
        "pos": "verb",
        "ipa": "/ˈtɪksɪŋ/",
        "vi": "đang tặc lưỡi chép miệng chán nản",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044065",
        "hw": "tsks",
        "pos": "verb",
        "ipa": "/tɪks/",
        "vi": "chép miệng tặc lưỡi tỏ ý chê bai",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044066",
        "hw": "ukuleles",
        "pos": "noun",
        "ipa": "/ˌjuːkəˈleɪliz/",
        "vi": "những chiếc đàn ukulele bốn dây nhỏ",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044067",
        "hw": "umps",
        "pos": "noun",
        "ipa": "/ʌmps/",
        "vi": "các trọng tài điều khiển bóng chày",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044068",
        "hw": "uranuses",
        "pos": "noun",
        "ipa": "/ˈjʊərənəsɪz/",
        "vi": "thần Uranus; hành tinh Thiên Vương",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044069",
        "hw": "yetis",
        "pos": "noun",
        "ipa": "/ˈjɛtiz/",
        "vi": "người tuyết quái vật ở Himalaya",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044070",
        "hw": "acetic acid",
        "pos": "phrase",
        "ipa": "/əˈsiːtɪk ˈæsɪd/",
        "vi": "axit axetic trong giấm ăn hằng ngày",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044071",
        "hw": "acetyl chloride",
        "pos": "phrase",
        "ipa": "/ˈæsətɪl ˈklɔːraɪd/",
        "vi": "hợp chất hóa học axetyl clorua",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044072",
        "hw": "afro hairdo",
        "pos": "phrase",
        "ipa": "/ˈæfroʊ ˈhɛrduː/",
        "vi": "kiểu tóc xù afro của người da đen",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044073",
        "hw": "alfalfa sprout",
        "pos": "phrase",
        "ipa": "/ælˈfælfə spraʊt/",
        "vi": "mầm cỏ linh lăng thanh mát ăn kèm",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044074",
        "hw": "anise seed",
        "pos": "phrase",
        "ipa": "/ˈænɪs siːd/",
        "vi": "hạt tiểu hồi dùng làm gia vị nêm",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044075",
        "hw": "ansar al islam",
        "pos": "phrase",
        "ipa": "/ˌænsɑːr æl ɪsˈlɑːm/",
        "vi": "nhóm du kích Ansar al-Islam",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044076",
        "hw": "apneas",
        "pos": "noun",
        "ipa": "/ˈæpniəz/",
        "vi": "chứng ngừng thở từng cơn khi ngủ",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044077",
        "hw": "armpits",
        "pos": "noun",
        "ipa": "/ˈɑːrmpɪts/",
        "vi": "hố nách dưới cánh tay người",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044078",
        "hw": "asls",
        "pos": "noun",
        "ipa": "/ˌeɪ ɛs ˈɛlz/",
        "vi": "ngôn ngữ ký hiệu ASL của nước Mỹ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044079",
        "hw": "austerest",
        "pos": "adj",
        "ipa": "/ɔːˈstɪrɪst/",
        "vi": "khắt khe nhất; mộc mạc đạm bạc nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044080",
        "hw": "backers",
        "pos": "noun",
        "ipa": "/ˈbækərz/",
        "vi": "người ủng hộ; nhà tài trợ vốn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044081",
        "hw": "bailiffs",
        "pos": "noun",
        "ipa": "/ˈbeɪlɪfs/",
        "vi": "thừa phát lại tòa án; viên cảnh lại",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044082",
        "hw": "baptismal font",
        "pos": "phrase",
        "ipa": "/bæpˈtɪzməl fɑːnt/",
        "vi": "chậu đá chứa nước rửa tội nhà thờ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044083",
        "hw": "beckman thermometer",
        "pos": "phrase",
        "ipa": "/ˈbɛkmən θərˈmɑːmɪtər/",
        "vi": "nhiệt kế hiệu ứng vi sai Beckman",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044084",
        "hw": "benedict de spinoza",
        "pos": "phrase",
        "ipa": "/ˈbɛnədɪkt də spɪˈnoʊzə/",
        "vi": "triết gia Benedict Spinoza Hà Lan",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044085",
        "hw": "bergmans",
        "pos": "noun",
        "ipa": "/ˈbɜːrɡmənz/",
        "vi": "những người mang họ Bergman",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044086",
        "hw": "bermuda chub",
        "pos": "phrase",
        "ipa": "/bərˈmjuːdə tʃʌb/",
        "vi": "loài cá chép biển Bermuda chub",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044087",
        "hw": "black mamba",
        "pos": "phrase",
        "ipa": "/blæk ˈmɑːmbə/",
        "vi": "loài rắn mamba đen cực độc châu Phi",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044088",
        "hw": "blockages",
        "pos": "noun",
        "ipa": "/ˈblɑːkɪdʒɪz/",
        "vi": "chứng tắc nghẽn; chỗ tắc mạch máu",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044089",
        "hw": "bola tie",
        "pos": "phrase",
        "ipa": "/ˈboʊlə taɪ/",
        "vi": "dây cà vạt cài mạ bạc bolo cao bồi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044090",
        "hw": "book of nehemiah",
        "pos": "phrase",
        "ipa": "/bʊk əv ˌniːəˈmaɪə/",
        "vi": "cuốn sách Nê-hê-mi trong Kinh Thánh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044091",
        "hw": "bristle fern",
        "pos": "phrase",
        "ipa": "/ˈbrɪsl fɜːrn/",
        "vi": "loài dương xỉ có lông cứng nhỏ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044092",
        "hw": "buoyed",
        "pos": "verb",
        "ipa": "/bʊɪd/",
        "vi": "đã nâng đỡ tinh thần; làm nổi lên",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044093",
        "hw": "buoying",
        "pos": "verb",
        "ipa": "/ˈbuːiɪŋ/",
        "vi": "làm nổi bập bềnh; nâng đỡ tinh thần",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044094",
        "hw": "buoys",
        "pos": "noun",
        "ipa": "/buːiz/",
        "vi": "chiếc phao tiêu báo hiệu trên biển",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044095",
        "hw": "burkina faso franc",
        "pos": "phrase",
        "ipa": "/bʊrˈkiːnə ˈfɑːsoʊ fræŋk/",
        "vi": "đồng tiền franc tại Burkina Faso",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044096",
        "hw": "campaigners",
        "pos": "noun",
        "ipa": "/kæmˈpeɪnərz/",
        "vi": "người tham gia vận động tranh cử",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044097",
        "hw": "candlestick tulip",
        "pos": "phrase",
        "ipa": "/ˈkændlstɪk ˈtuːlɪp/",
        "vi": "hoa tulip hình chân nến duyên dáng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044098",
        "hw": "cavernous sinus",
        "pos": "phrase",
        "ipa": "/ˈkævərnəs ˈsaɪnəs/",
        "vi": "xoang tĩnh mạch hang đáy hộp sọ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044099",
        "hw": "chalices",
        "pos": "noun",
        "ipa": "/ˈtʃælɪsɪz/",
        "vi": "những chiếc chén thánh uống rượu lễ",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044100",
        "hw": "chromatic aberration",
        "pos": "phrase",
        "ipa": "/kroʊˈmætɪk ˌæbəˈreɪʃən/",
        "vi": "hiện tượng quang sai sắc thấu kính",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.044101",
        "hw": "cine projector",
        "pos": "phrase",
        "ipa": "/ˈsɪni prəˈdʒɛktər/",
        "vi": "máy chiếu phim nhựa rạp chiếu bóng",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r09_raw_p1.json') as f:
    raw = json.load(f)

assert len(reviewed_items) == 100, f"Expected 100 items, got {len(reviewed_items)}"
assert len(raw) == 100, f"Expected 100 raw items, got {len(raw)}"

valid_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}

for i, (rev, orig) in enumerate(zip(reviewed_items, raw)):
    assert rev["id"] == orig["id"], f"ID mismatch at {i}: {rev['id']} vs {orig['id']}"
    assert rev["hw"] == orig["hw"], f"HW mismatch at {i}: {rev['hw']} vs {orig['hw']}"
    assert rev["pos"] in valid_pos, f"Invalid POS at {i}: {rev['pos']}"
    assert len(rev["vi"]) <= 35, f"VI too long ({len(rev['vi'])}) at {i}: {rev['vi']}"
    assert rev["status"] == "reviewed", f"Invalid status at {i}"
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/"), f"Invalid IPA at {i}: {rev['ipa']}"
    assert rev["ipa"].count("/") == 2, f"IPA slashes count != 2 at {i}: {rev['ipa']}"

with open('scratch/b29_r09_p1.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 9 Part 1 verified and written successfully.")
