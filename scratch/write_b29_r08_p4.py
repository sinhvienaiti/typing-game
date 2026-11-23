import json

reviewed_items = [
    {
        "id": "lex.en.200k.043802",
        "hw": "amputations",
        "pos": "noun",
        "ipa": "/ˌæmpjʊˈteɪʃənz/",
        "vi": "các ca phẫu thuật cắt cụt chi",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043803",
        "hw": "aquinases",
        "pos": "noun",
        "ipa": "/əˈkwaɪnəsɪz/",
        "vi": "những người mang tên Aquinas",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043804",
        "hw": "axioms",
        "pos": "noun",
        "ipa": "/ˈæksiəmz/",
        "vi": "các tiên đề; chân lý tự hiển nhiên",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043805",
        "hw": "birthrights",
        "pos": "noun",
        "ipa": "/ˈbɜːrθraɪts/",
        "vi": "quyền thừa kế theo huyết thống",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043806",
        "hw": "blackboards",
        "pos": "noun",
        "ipa": "/ˈblækbɔːrdz/",
        "vi": "những chiếc bảng đen lớp học",
        "cefr": "A1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043807",
        "hw": "blackwaters",
        "pos": "noun",
        "ipa": "/ˈblækwɔːtərz/",
        "vi": "chứng sốt đái ra huyết cầu tố",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043808",
        "hw": "bystanders",
        "pos": "noun",
        "ipa": "/ˈbaɪstændərz/",
        "vi": "những người qua đường đứng xem",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043809",
        "hw": "catchments",
        "pos": "noun",
        "ipa": "/ˈkætʃmənts/",
        "vi": "lưu vực sông; khu vực gom nước",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043810",
        "hw": "chechens",
        "pos": "noun",
        "ipa": "/ˈtʃɛtʃənz/",
        "vi": "người Chechnya; cư dân Chechnya",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043811",
        "hw": "cleanlier",
        "pos": "adj",
        "ipa": "/ˈklɛnliər/",
        "vi": "ngăn nắp sạch sẽ hơn; vệ sinh hơn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043812",
        "hw": "cleanliest",
        "pos": "adj",
        "ipa": "/ˈklɛnliɪst/",
        "vi": "ngăn nắp sạch sẽ nhất; vệ sinh nhất",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043813",
        "hw": "crees",
        "pos": "noun",
        "ipa": "/kriːz/",
        "vi": "người thổ dân Cree bản địa Bắc Mỹ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043814",
        "hw": "crucifixes",
        "pos": "noun",
        "ipa": "/ˈkruːsəfɪksɪz/",
        "vi": "thánh giá có tượng Chúa chịu nạn",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043815",
        "hw": "diarrhoeas",
        "pos": "noun",
        "ipa": "/ˌdaɪəˈriːəz/",
        "vi": "các đợt tiêu chảy; bệnh tiêu chảy",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043816",
        "hw": "dieters",
        "pos": "noun",
        "ipa": "/ˈdaɪətərz/",
        "vi": "những người đang ăn kiêng giảm cân",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043817",
        "hw": "dissonances",
        "pos": "noun",
        "ipa": "/ˈdɪsənənsɪz/",
        "vi": "sự bất hòa; âm nghịch tai",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043818",
        "hw": "earthier",
        "pos": "adj",
        "ipa": "/ˈɜːrθiər/",
        "vi": "mộc mạc hơn; trần tục hơn",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043819",
        "hw": "earthiest",
        "pos": "adj",
        "ipa": "/ˈɜːrθiɪst/",
        "vi": "mộc mạc nhất; trần tục nhất",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043820",
        "hw": "equinoxes",
        "pos": "noun",
        "ipa": "/ˈiːkwənɑːksɪz/",
        "vi": "các điểm phân; ngày phân xuân thu",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043821",
        "hw": "eulogies",
        "pos": "noun",
        "ipa": "/ˈjuːlədʒiz/",
        "vi": "những bài điếu văn; lời ca ngợi",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043822",
        "hw": "flinderses",
        "pos": "noun",
        "ipa": "/ˈflɪndərzɪz/",
        "vi": "những người mang họ Flinders",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043823",
        "hw": "freshers",
        "pos": "noun",
        "ipa": "/ˈfrɛʃərz/",
        "vi": "sinh viên năm nhất mới nhập học",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043824",
        "hw": "gambias",
        "pos": "noun",
        "ipa": "/ˈɡæmbiəz/",
        "vi": "các vùng của đất nước Gambia",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043825",
        "hw": "gauls",
        "pos": "noun",
        "ipa": "/ɡɔːlz/",
        "vi": "người xứ Gaul cổ đại; người Gô-loa",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043826",
        "hw": "grenadas",
        "pos": "noun",
        "ipa": "/ɡrəˈneɪdəz/",
        "vi": "các khu vực của quốc đảo Grenada",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043827",
        "hw": "growers",
        "pos": "noun",
        "ipa": "/ˈɡroʊərz/",
        "vi": "người gieo trồng trọt nông nghiệp",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043828",
        "hw": "grunges",
        "pos": "noun",
        "ipa": "/ˈɡrʌndʒɪz/",
        "vi": "phong cách nhạc grunge; sự nhơ bẩn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043829",
        "hw": "iaeas",
        "pos": "noun",
        "ipa": "/ˌaɪ eɪ iː ˈeɪz/",
        "vi": "cơ quan IAEA nguyên tử quốc tế",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043830",
        "hw": "januses",
        "pos": "noun",
        "ipa": "/ˈdʒeɪnəsɪz/",
        "vi": "thần hai mặt Janus; kẻ hai mang",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043831",
        "hw": "jukeboxes",
        "pos": "noun",
        "ipa": "/ˈdʒuːkbɑːksɪz/",
        "vi": "máy hát đĩa tự động bỏ tiền xu",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043832",
        "hw": "jumpsuits",
        "pos": "noun",
        "ipa": "/ˈdʒʌmpsuːts/",
        "vi": "bộ quần áo liền thân jumpsuit",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043833",
        "hw": "kamis",
        "pos": "noun",
        "ipa": "/ˈkɑːmiz/",
        "vi": "thần linh kami trong Thần đạo Nhật",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043834",
        "hw": "markovs",
        "pos": "noun",
        "ipa": "/ˈmɑːrkɔːvz/",
        "vi": "những người mang họ Markov",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043835",
        "hw": "mertons",
        "pos": "noun",
        "ipa": "/ˈmɜːrtnz/",
        "vi": "những người mang họ Merton",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043836",
        "hw": "molotovs",
        "pos": "noun",
        "ipa": "/ˈmɑːlətɔːvz/",
        "vi": "những chai bom xăng Molotov",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043837",
        "hw": "monograms",
        "pos": "noun",
        "ipa": "/ˈmɑːnəɡræmz/",
        "vi": "chữ lồng tên; con dấu chữ lồng",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043838",
        "hw": "morays",
        "pos": "noun",
        "ipa": "/ˈmɔːreɪz/",
        "vi": "những con cá chình biển moray",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043839",
        "hw": "nachos",
        "pos": "noun",
        "ipa": "/ˈnɑːtʃoʊz/",
        "vi": "món bánh bắp giòn nacho Mexico",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043840",
        "hw": "nanotechnologies",
        "pos": "noun",
        "ipa": "/ˌnænoʊtɛkˈnɑːlədʒiz/",
        "vi": "các phân ngành công nghệ nano",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043841",
        "hw": "noblemen",
        "pos": "noun",
        "ipa": "/ˈnoʊblmən/",
        "vi": "các nhà quý tộc; bậc quý tộc nam",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043842",
        "hw": "optimists",
        "pos": "noun",
        "ipa": "/ˈɑːptəmɪsts/",
        "vi": "những người có tinh thần lạc quan",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043843",
        "hw": "osirises",
        "pos": "noun",
        "ipa": "/oʊˈsaɪrɪsɪz/",
        "vi": "thần Osiris cai quản cõi âm Ai Cập",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043844",
        "hw": "overlords",
        "pos": "noun",
        "ipa": "/ˈoʊvərlɔːrdz/",
        "vi": "chúa tể cai trị; bá chủ tối cao",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043845",
        "hw": "papacies",
        "pos": "noun",
        "ipa": "/ˈpeɪpəsiz/",
        "vi": "thời kỳ trị vì của các giáo hoàng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043846",
        "hw": "plancks",
        "pos": "noun",
        "ipa": "/plæŋks/",
        "vi": "những người mang họ Planck",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043847",
        "hw": "poodles",
        "pos": "noun",
        "ipa": "/ˈpuːdlz/",
        "vi": "giống chó săn vịt lông xoăn poodle",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043848",
        "hw": "roadblocks",
        "pos": "noun",
        "ipa": "/ˈroʊdblɑːks/",
        "vi": "chốt chặn đường sá; chướng ngại vật",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043849",
        "hw": "sabred",
        "pos": "verb",
        "ipa": "/ˈseɪbərd/",
        "vi": "đã chém bằng kiếm cong sabre",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043850",
        "hw": "sabres",
        "pos": "noun",
        "ipa": "/ˈseɪbərz/",
        "vi": "thanh kiếm cong kỵ binh sabre",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043851",
        "hw": "sabring",
        "pos": "verb",
        "ipa": "/ˈseɪbərɪŋ/",
        "vi": "đang chém bằng gươm cong kỵ binh",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043852",
        "hw": "sandboxes",
        "pos": "noun",
        "ipa": "/ˈsændbɑːksɪz/",
        "vi": "hố cát trẻ con; môi trường cô lập",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043853",
        "hw": "seagulls",
        "pos": "noun",
        "ipa": "/ˈsiːɡʌlz/",
        "vi": "những con chim mòng biển bắt cá",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043854",
        "hw": "shagging",
        "pos": "verb",
        "ipa": "/ˈʃæɡɪŋ/",
        "vi": "đang nhặt bóng tập; đang làm tình",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043855",
        "hw": "shags",
        "pos": "noun",
        "ipa": "/ʃæɡz/",
        "vi": "thảm sợi lông dày; chim cốc mào",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043856",
        "hw": "shifters",
        "pos": "noun",
        "ipa": "/ˈʃɪftərz/",
        "vi": "cần số xe cộ; người đổi ca làm",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043857",
        "hw": "shortfalls",
        "pos": "noun",
        "ipa": "/ˈʃɔːrtfɔːlz/",
        "vi": "các khoản thâm hụt; lượng thiếu hụt",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043858",
        "hw": "sichuans",
        "pos": "noun",
        "ipa": "/ˈsɪtʃwɑːnz/",
        "vi": "vùng Tứ Xuyên; món ăn vị Tứ Xuyên",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043859",
        "hw": "silos",
        "pos": "noun",
        "ipa": "/ˈsaɪloʊz/",
        "vi": "tháp chứa ngũ cốc; hầm tên lửa",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043860",
        "hw": "sions",
        "pos": "noun",
        "ipa": "/ˈsaɪənz/",
        "vi": "ngọn đồi thiêng Sion đất thánh",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043861",
        "hw": "streeps",
        "pos": "noun",
        "ipa": "/striːps/",
        "vi": "những người mang họ Streep",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043862",
        "hw": "styli",
        "pos": "noun",
        "ipa": "/ˈstaɪlaɪ/",
        "vi": "các đầu kim đĩa hát; bút cảm ứng số",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043863",
        "hw": "styluses",
        "pos": "noun",
        "ipa": "/ˈstaɪləsɪz/",
        "vi": "bút cảm ứng đồ họa; kim máy hát đĩa",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043864",
        "hw": "tailgated",
        "pos": "verb",
        "ipa": "/ˈteɪlɡeɪtɪd/",
        "vi": "đã bám sát đuôi xe phía trước",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043865",
        "hw": "tailgates",
        "pos": "noun",
        "ipa": "/ˈteɪlɡeɪts/",
        "vi": "cửa sau xe tải; cốp lật sau xe",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043866",
        "hw": "tailgating",
        "pos": "verb",
        "ipa": "/ˈteɪlɡeɪtɪŋ/",
        "vi": "việc lái xe bám sát đuôi xe trước",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043867",
        "hw": "tobins",
        "pos": "noun",
        "ipa": "/ˈtoʊbɪnz/",
        "vi": "những người mang họ Tobin",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043868",
        "hw": "trafalgars",
        "pos": "noun",
        "ipa": "/trəˈfælɡərz/",
        "vi": "các trận hải chiến mũi Trafalgar",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043869",
        "hw": "tuscans",
        "pos": "noun",
        "ipa": "/ˈtʌskənz/",
        "vi": "người vùng Tuscany miền trung Ý",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043870",
        "hw": "tutus",
        "pos": "noun",
        "ipa": "/ˈtuːtuːz/",
        "vi": "váy xòe ngắn của vũ công múa ba-lê",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043871",
        "hw": "usafs",
        "pos": "noun",
        "ipa": "/ˌjuː ɛs eɪ ˈɛfs/",
        "vi": "lực lượng Không quân Hoa Kỳ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043872",
        "hw": "vases",
        "pos": "noun",
        "ipa": "/ˈveɪsɪz/",
        "vi": "những chiếc bình hoa trang trí",
        "cefr": "A1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043873",
        "hw": "versaces",
        "pos": "noun",
        "ipa": "/vərˈsɑːtʃiz/",
        "vi": "mặt hàng thời trang cao cấp Versace",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043874",
        "hw": "zeds",
        "pos": "noun",
        "ipa": "/zɛdz/",
        "vi": "các chữ cái Z trong bảng mẫu tự Anh",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043875",
        "hw": "agape love",
        "pos": "phrase",
        "ipa": "/əˈɡɑːpeɪ lʌv/",
        "vi": "tình yêu thiêng liêng vô điều kiện",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043876",
        "hw": "anise plant",
        "pos": "phrase",
        "ipa": "/ˈænɪs plænt/",
        "vi": "cây tiểu hồi hương lấy hạt thơm",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043877",
        "hw": "anise tree",
        "pos": "phrase",
        "ipa": "/ˈænɪs triː/",
        "vi": "cây đại hồi thân gỗ cho hoa hồi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043878",
        "hw": "anne boleyn",
        "pos": "phrase",
        "ipa": "/æn ˈbʊlɪn/",
        "vi": "hoàng hậu Anne Boleyn nước Anh",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043879",
        "hw": "argonne forest",
        "pos": "phrase",
        "ipa": "/ɑːrˈɡɑːn ˈfɔːrɪst/",
        "vi": "chiến dịch rừng Argonne Thế chiến I",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043880",
        "hw": "ask jeeves",
        "pos": "phrase",
        "ipa": "/æsk ˈdʒiːvz/",
        "vi": "công cụ tìm kiếm Ask Jeeves đời đầu",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043881",
        "hw": "atlantic puffin",
        "pos": "phrase",
        "ipa": "/ətˈlæntɪk ˈpʌfɪn/",
        "vi": "loài hải âu rụt cổ Đại Tây Dương",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043882",
        "hw": "bahama grass",
        "pos": "phrase",
        "ipa": "/bəˈhɑːmə ɡræs/",
        "vi": "loài cỏ chỉ Bermuda xanh bò lan",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043883",
        "hw": "bahama islands",
        "pos": "phrase",
        "ipa": "/bəˈhɑːmə ˈaɪləndz/",
        "vi": "quần đảo Bahamas nhiệt đới Caribe",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043884",
        "hw": "balsam apple",
        "pos": "phrase",
        "ipa": "/ˈbɔːlsəm ˈæpl/",
        "vi": "cây mướp đắng gai quả vàng cam",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043885",
        "hw": "balsam family",
        "pos": "phrase",
        "ipa": "/ˈbɔːlsəm ˈfæməli/",
        "vi": "họ thực vật hoa bóng nước Balsam",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043886",
        "hw": "battle of ravenna",
        "pos": "phrase",
        "ipa": "/ˈbætl əv rəˈvɛnə/",
        "vi": "trận chiến khốc liệt Ravenna nước Ý",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043887",
        "hw": "bohr theory",
        "pos": "phrase",
        "ipa": "/bɔːr ˈθiːəri/",
        "vi": "thuyết lượng tử nguyên tử Bohr",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043888",
        "hw": "brown thrasher",
        "pos": "phrase",
        "ipa": "/braʊn ˈθræʃər/",
        "vi": "loài chim hoét nâu hót vang Bắc Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043889",
        "hw": "camber arch",
        "pos": "phrase",
        "ipa": "/ˈkæmbər ɑːrtʃ/",
        "vi": "kết cấu vòm uốn cong camber nhẹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043890",
        "hw": "canada balsam",
        "pos": "phrase",
        "ipa": "/ˈkænədə ˈbɔːlsəm/",
        "vi": "nhựa dầu linh sam thơm Canada",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043891",
        "hw": "carrion fungus",
        "pos": "phrase",
        "ipa": "/ˈkæriən ˈfʌŋɡəs/",
        "vi": "nấm thối mùi xác động vật bốc mùi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043892",
        "hw": "charles cornwallis",
        "pos": "phrase",
        "ipa": "/tʃɑːrlz kɔːrnˈwɑːlɪs/",
        "vi": "tướng Cornwallis của quân đội Anh",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043893",
        "hw": "chinese anise",
        "pos": "phrase",
        "ipa": "/ˌtʃaɪˈniːz ˈænɪs/",
        "vi": "cây đại hồi lấy gia vị hoa hồi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043894",
        "hw": "clam chowder",
        "pos": "phrase",
        "ipa": "/klæm ˈtʃaʊdər/",
        "vi": "món súp nghêu hầm kem béo ngậy",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043895",
        "hw": "conjugal family",
        "pos": "phrase",
        "ipa": "/ˈkɑːndʒʊɡl ˈfæməli/",
        "vi": "gia đình hạt nhân một vợ một chồng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043896",
        "hw": "conjugal right",
        "pos": "phrase",
        "ipa": "/ˈkɑːndʒʊɡl raɪt/",
        "vi": "quyền quan hệ gối chăn vợ chồng",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043897",
        "hw": "covalent bond",
        "pos": "phrase",
        "ipa": "/koʊˈveɪlənt bɑːnd/",
        "vi": "liên kết hóa học cộng hóa trị",
        "cefr": "B2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043898",
        "hw": "crawfish out",
        "pos": "phrase",
        "ipa": "/ˈkrɔːfɪʃ aʊt/",
        "vi": "rút lời cam kết; thoái thác bỏ cuộc",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043899",
        "hw": "david bushnell",
        "pos": "phrase",
        "ipa": "/ˈdeɪvɪd ˈbʊʃnəl/",
        "vi": "nhà chế tạo tàu ngầm lặn Bushnell",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043900",
        "hw": "distal muscular dystrophy",
        "pos": "phrase",
        "ipa": "/ˈdɪstl ˈmʌskjələr ˈdɪstrəfi/",
        "vi": "loạn dưỡng cơ ở ngọn chi xa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043901",
        "hw": "domestic prelate",
        "pos": "phrase",
        "ipa": "/dəˈmɛstɪk ˈprɛlət/",
        "vi": "giám mục danh dự tại tòa thánh",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r08_raw_p4.json') as f:
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

with open('scratch/b29_r08_p4.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 8 Part 4 verified and written successfully.")
