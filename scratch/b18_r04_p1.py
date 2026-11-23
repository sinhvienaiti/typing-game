# scratch/b18_r04_p1.py
# Batch 18 Round 4 Part 1: records 1500 - 1599 (IDs 086502 - 086601)
import json

data = [
    {
        "id": "lex.en.100k.086502",
        "hw": "incitingly",
        "pos": "adv",
        "ipa": "/ɪnˈsaɪtɪŋli/",
        "vi": "với giọng kích động; xúi giục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086503",
        "hw": "incitive",
        "pos": "adj",
        "ipa": "/ɪnˈsaɪtɪv/",
        "vi": "mang tính kích động; xúi giục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086504",
        "hw": "incivism",
        "pos": "noun",
        "ipa": "/ɪnˈsɪvɪzəm/",
        "vi": "sự thiếu ý thức công dân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086505",
        "hw": "inclemency",
        "pos": "noun",
        "ipa": "/ɪnˈklɛmənsi/",
        "vi": "sự khắc nghiệt; tính nghiệt ngã",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086506",
        "hw": "inclemently",
        "pos": "adv",
        "ipa": "/ɪnˈklɛməntli/",
        "vi": "một cách khắc nghiệt; gay gắt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086507",
        "hw": "inclementness",
        "pos": "noun",
        "ipa": "/ɪnˈklɛməntnəs/",
        "vi": "sự khắc nghiệt (thời tiết)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086508",
        "hw": "inclinable",
        "pos": "adj",
        "ipa": "/ɪnˈklaɪnəbəl/",
        "vi": "có chiều hướng; thiên về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086509",
        "hw": "inclinations",
        "pos": "noun",
        "ipa": "/ˌɪnkləˈneɪʃənz/",
        "vi": "những thiên hướng; các xu hướng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086510",
        "hw": "incliner",
        "pos": "noun",
        "ipa": "/ɪnˈklaɪnər/",
        "vi": "người cúi đầu; mặt nghiêng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086511",
        "hw": "inclines",
        "pos": "verb",
        "ipa": "/ɪnˈklaɪnz/",
        "vi": "nghiêng về; cúi đầu; thiên về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086512",
        "hw": "includable",
        "pos": "adj",
        "ipa": "/ɪnˈkluːdəbəl/",
        "vi": "có thể bao gồm; có thể gộp vào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086513",
        "hw": "includes",
        "pos": "verb",
        "ipa": "/ɪnˈkluːdz/",
        "vi": "bao gồm; bao hàm; tính cả",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086514",
        "hw": "includible",
        "pos": "adj",
        "ipa": "/ɪnˈkluːdəbəl/",
        "vi": "có thể tính vào; gồm vào được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086515",
        "hw": "including",
        "pos": "prep",
        "ipa": "/ɪnˈkluːdɪŋ/",
        "vi": "bao gồm; kể cả; tính cả",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086516",
        "hw": "inclusionary",
        "pos": "adj",
        "ipa": "/ɪnˈkluːʒənɛri/",
        "vi": "mang tính hòa nhập; bao hàm tất cả",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086517",
        "hw": "inclusively",
        "pos": "adv",
        "ipa": "/ɪnˈkluːsɪvli/",
        "vi": "tính gộp cả; bao hàm toàn bộ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086518",
        "hw": "inclusiveness",
        "pos": "noun",
        "ipa": "/ɪnˈkluːsɪvnəs/",
        "vi": "tính bao trùm; tính hòa nhập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086519",
        "hw": "incoagulability",
        "pos": "noun",
        "ipa": "/ɪnkoʊˌæɡjələˈbɪləti/",
        "vi": "tính không thể đông máu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086520",
        "hw": "incoagulable",
        "pos": "adj",
        "ipa": "/ˌɪnkoʊˈæɡjələbəl/",
        "vi": "không thể đông tụ; không vón cục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086521",
        "hw": "incoercible",
        "pos": "adj",
        "ipa": "/ˌɪnkoʊˈɜːrsəbəl/",
        "vi": "không thể ép buộc; không nén được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086522",
        "hw": "incog",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːɡ/",
        "vi": "ẩn danh; cải trang vi hành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086523",
        "hw": "incogitability",
        "pos": "noun",
        "ipa": "/ɪnˌkɑːdʒɪtəˈbɪləti/",
        "vi": "tính không thể suy tưởng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086524",
        "hw": "incogitable",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːdʒɪtəbəl/",
        "vi": "không thể tưởng tượng; khôn nghĩ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086525",
        "hw": "incogitant",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːdʒɪtənt/",
        "vi": "vô tâm; thiếu suy nghĩ chín chắn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086526",
        "hw": "incognita",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːɡnɪtə/",
        "vi": "ẩn danh (dùng cho phái nữ)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086527",
        "hw": "incognizable",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːɡnɪzəbəl/",
        "vi": "không thể nhận biết; khôn lường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086528",
        "hw": "incognizance",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːɡnɪzəns/",
        "vi": "sự không biết; sự không nhận thức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086529",
        "hw": "incognizant",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːɡnɪzənt/",
        "vi": "không nhận biết; không hay biết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086530",
        "hw": "incognoscible",
        "pos": "adj",
        "ipa": "/ˌɪnkɑːɡˈnɑːsəbəl/",
        "vi": "không thể nhận thức hay hiểu được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086531",
        "hw": "incoherentness",
        "pos": "noun",
        "ipa": "/ˌɪnkoʊˈhɪrəntnəs/",
        "vi": "tính rời rạc; sự thiếu mạch lạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086532",
        "hw": "incohesion",
        "pos": "noun",
        "ipa": "/ˌɪnkoʊˈhiːʒən/",
        "vi": "sự thiếu gắn kết; tính rời rạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086533",
        "hw": "incohesive",
        "pos": "adj",
        "ipa": "/ˌɪnkoʊˈhiːsɪv/",
        "vi": "rời rạc; thiếu tính gắn kết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086534",
        "hw": "incombustibility",
        "pos": "noun",
        "ipa": "/ˌɪnkəmˌbʌstəˈbɪləti/",
        "vi": "tính không cháy; tính chống cháy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086535",
        "hw": "incombustibleness",
        "pos": "noun",
        "ipa": "/ˌɪnkəmˈbʌstəbəlnəs/",
        "vi": "tính chất không bắt lửa; chống cháy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086536",
        "hw": "incombustibly",
        "pos": "adv",
        "ipa": "/ˌɪnkəmˈbʌstəbli/",
        "vi": "một cách không bắt lửa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086537",
        "hw": "incomeless",
        "pos": "adj",
        "ipa": "/ˈɪnkʌmləs/",
        "vi": "không có thu nhập; không có hoa lợi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086538",
        "hw": "incomer",
        "pos": "noun",
        "ipa": "/ˈɪnkʌmər/",
        "vi": "người mới đến; người nhập cư",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086539",
        "hw": "incomings",
        "pos": "noun",
        "ipa": "/ˈɪnkʌmɪŋz/",
        "vi": "các khoản thu nhập; tiền thu về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086540",
        "hw": "incommensurability",
        "pos": "noun",
        "ipa": "/ˌɪnkəmɛnʃərəˈbɪləti/",
        "vi": "tính bất khả ước; không cùng đơn vị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086541",
        "hw": "incommensurableness",
        "pos": "noun",
        "ipa": "/ˌɪnkəmˈɛnʃərəbəlnəs/",
        "vi": "tính không thể so sánh tương đương",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086542",
        "hw": "incommensurably",
        "pos": "adv",
        "ipa": "/ˌɪnkəmˈɛnʃərəbli/",
        "vi": "một cách không thể so sánh cùng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086543",
        "hw": "incommensurately",
        "pos": "adv",
        "ipa": "/ˌɪnkəˈmɛnʃərɪtli/",
        "vi": "một cách không tương xứng; cọc cạch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086544",
        "hw": "incommensurateness",
        "pos": "noun",
        "ipa": "/ˌɪnkəˈmɛnʃərɪtnəs/",
        "vi": "sự không tương xứng; tính lệch pha",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086545",
        "hw": "incommodate",
        "pos": "verb",
        "ipa": "/ɪnˈkɑːmədeɪt/",
        "vi": "làm phiền; gây phiền hà bất tiện",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086546",
        "hw": "incommode",
        "pos": "verb",
        "ipa": "/ˌɪnkəˈmoʊd/",
        "vi": "gây phiền phức; làm bất tiện",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086547",
        "hw": "incommoded",
        "pos": "verb",
        "ipa": "/ˌɪnkəˈmoʊdɪd/",
        "vi": "đã làm phiền; đã gây phiền toái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086548",
        "hw": "incommodes",
        "pos": "verb",
        "ipa": "/ˌɪnkəˈmoʊdz/",
        "vi": "làm phiền; gây phiền toái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086549",
        "hw": "incommoding",
        "pos": "verb",
        "ipa": "/ˌɪnkəˈmoʊdɪŋ/",
        "vi": "đang làm phiền; đang gây trở ngại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086550",
        "hw": "incommodious",
        "pos": "adj",
        "ipa": "/ˌɪnkəˈmoʊdiəs/",
        "vi": "chật chội; bất tiện khó chịu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086551",
        "hw": "incommodiously",
        "pos": "adv",
        "ipa": "/ˌɪnkəˈmoʊdiəsli/",
        "vi": "một cách bất tiện; chật chội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086552",
        "hw": "incommodiousness",
        "pos": "noun",
        "ipa": "/ˌɪnkəˈmoʊdiəsnəs/",
        "vi": "sự bất tiện; tình trạng chật chội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086553",
        "hw": "incommunicability",
        "pos": "noun",
        "ipa": "/ˌɪnkəˌmjuːnɪkəˈbɪləti/",
        "vi": "tính không thể truyền đạt chia sẻ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086554",
        "hw": "incommunicable",
        "pos": "adj",
        "ipa": "/ˌɪnkəˈmjuːnɪkəbəl/",
        "vi": "không thể giãi bày; khôn tả",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086555",
        "hw": "incommunicableness",
        "pos": "noun",
        "ipa": "/ˌɪnkəˈmjuːnɪkəbəlnəs/",
        "vi": "tính chất không thể giãi bày",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086556",
        "hw": "incommunicably",
        "pos": "adv",
        "ipa": "/ˌɪnkəˈmjuːnɪkəbli/",
        "vi": "đến mức không thể diễn đạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086557",
        "hw": "incommunicative",
        "pos": "adj",
        "ipa": "/ˌɪnkəˈmjuːnɪkətɪv/",
        "vi": "kín miệng; ít nói; không cởi mở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086558",
        "hw": "incommunicatively",
        "pos": "adv",
        "ipa": "/ˌɪnkəˈmjuːnɪkətɪvli/",
        "vi": "một cách khép kín; lầm lì",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086559",
        "hw": "incommunicativeness",
        "pos": "noun",
        "ipa": "/ˌɪnkəˈmjuːnɪkətɪvnəs/",
        "vi": "tính kín miệng; sự ít nói cởi mở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086560",
        "hw": "incommuntability",
        "pos": "noun",
        "ipa": "/ˌɪnkəmjuːntəˈbɪləti/",
        "vi": "tính không thể thay đổi thay thế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086561",
        "hw": "incommuntable",
        "pos": "adj",
        "ipa": "/ˌɪnkəˈmjuːntəbəl/",
        "vi": "không thể thay thế; bất biến",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086562",
        "hw": "incommutability",
        "pos": "noun",
        "ipa": "/ˌɪnkəˌmjuːtəˈbɪləti/",
        "vi": "tính không thể hoán đổi thay thế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086563",
        "hw": "incommutable",
        "pos": "adj",
        "ipa": "/ˌɪnkəˈmjuːtəbəl/",
        "vi": "không thể thay thế; bất di dịch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086564",
        "hw": "incommutableness",
        "pos": "noun",
        "ipa": "/ˌɪnkəˈmjuːtəbəlnəs/",
        "vi": "tính bất di bất dịch; không đổi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086565",
        "hw": "incommutably",
        "pos": "adv",
        "ipa": "/ˌɪnkəˈmjuːtəbli/",
        "vi": "một cách không thể thay đổi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086566",
        "hw": "incompact",
        "pos": "adj",
        "ipa": "/ˌɪnkəmˈpækt/",
        "vi": "rời rạc; không cô đọng; tơi xốp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086567",
        "hw": "incompactness",
        "pos": "noun",
        "ipa": "/ˌɪnkəmˈpæktnəs/",
        "vi": "tính rời rạc; độ tơi xốp lỏng lẻo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086568",
        "hw": "incomparability",
        "pos": "noun",
        "ipa": "/ɪnˌkɑːmpərəˈbɪləti/",
        "vi": "tính không thể sánh kịp; vô song",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086569",
        "hw": "incomparableness",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːmpərəbəlnəs/",
        "vi": "sự vô song; vẻ độc nhất vô nhị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086570",
        "hw": "incompatibleness",
        "pos": "noun",
        "ipa": "/ˌɪnkəmˈpætəbəlnəs/",
        "vi": "sự xung khắc; tính không dung hợp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086571",
        "hw": "incompatibly",
        "pos": "adv",
        "ipa": "/ˌɪnkəmˈpætəbli/",
        "vi": "một cách xung khắc; trái ngược nhau",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086572",
        "hw": "incompletenesses",
        "pos": "noun",
        "ipa": "/ˌɪnkəmˈpliːtnəsɪz/",
        "vi": "những chỗ dở dang; các điểm thiếu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086573",
        "hw": "incompletion",
        "pos": "noun",
        "ipa": "/ˌɪnkəmˈpliːʃən/",
        "vi": "tình trạng dở dang; chưa hoàn thành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086574",
        "hw": "incompliable",
        "pos": "adj",
        "ipa": "/ˌɪnkəmˈplaɪəbəl/",
        "vi": "không chiều theo; không phục tùng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086575",
        "hw": "incompliance",
        "pos": "noun",
        "ipa": "/ˌɪnkəmˈplaɪəns/",
        "vi": "sự bất tuân; tính không chịu thuận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086576",
        "hw": "incompliancy",
        "pos": "noun",
        "ipa": "/ˌɪnkəmˈplaɪənsi/",
        "vi": "sự ngang ngạnh; tính bất phục tùng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086577",
        "hw": "incompliant",
        "pos": "adj",
        "ipa": "/ˌɪnkəmˈplaɪənt/",
        "vi": "bất tuân; không chiều ý; bướng bỉnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086578",
        "hw": "incompliantly",
        "pos": "adv",
        "ipa": "/ˌɪnkəmˈplaɪəntli/",
        "vi": "một cách bất tuân; ngang ngạnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086579",
        "hw": "incomprehensibleness",
        "pos": "noun",
        "ipa": "/ɪnˌkɑːmprɪˈhɛnsəbəlnəs/",
        "vi": "tính chất khôn hiểu; sự bí hiểm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086580",
        "hw": "incomprehensibly",
        "pos": "adv",
        "ipa": "/ɪnˌkɑːmprɪˈhɛnsəbli/",
        "vi": "một cách khó hiểu; kỳ bí khôn lường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086581",
        "hw": "incomprehensive",
        "pos": "adj",
        "ipa": "/ˌɪnkɑːmprɪˈhɛnsɪv/",
        "vi": "không toàn diện; thiếu bao quát",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086582",
        "hw": "incomprehensively",
        "pos": "adv",
        "ipa": "/ˌɪnkɑːmprɪˈhɛnsɪvli/",
        "vi": "một cách không bao quát; chắp vá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086583",
        "hw": "incomprehensiveness",
        "pos": "noun",
        "ipa": "/ˌɪnkɑːmprɪˈhɛnsɪvnəs/",
        "vi": "sự thiếu bao quát; tính hạn hẹp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086584",
        "hw": "incomputability",
        "pos": "noun",
        "ipa": "/ɪnˌkɑːmpjətəˈbɪləti/",
        "vi": "tính không thể tính toán được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086585",
        "hw": "incomputable",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːmpjətəbəl/",
        "vi": "không thể đong đếm; vô số kể",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086586",
        "hw": "inconceivability",
        "pos": "noun",
        "ipa": "/ɪnkənˌsiːvəˈbɪləti/",
        "vi": "sự không thể tưởng tượng nổi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086587",
        "hw": "inconceivableness",
        "pos": "noun",
        "ipa": "/ɪnkənˈsiːvəbəlnəs/",
        "vi": "tính chất không thể ngờ tới",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086588",
        "hw": "inconclusiveness",
        "pos": "noun",
        "ipa": "/ˌɪnkənˈkluːsɪvnəs/",
        "vi": "tính không thuyết phục; mơ hồ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086589",
        "hw": "incondensability",
        "pos": "noun",
        "ipa": "/ˌɪnkənˌdɛnsəˈbɪləti/",
        "vi": "tính không thể ngưng tụ thành lỏng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086590",
        "hw": "incondensable",
        "pos": "adj",
        "ipa": "/ˌɪnkənˈdɛnsəbəl/",
        "vi": "không thể ngưng tụ (khí)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086591",
        "hw": "incondite",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːndɪt/",
        "vi": "thô kệch; vụng về; thiếu trau chuốt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086592",
        "hw": "inconditely",
        "pos": "adv",
        "ipa": "/ɪnˈkɑːndɪtli/",
        "vi": "một cách thô vụng; thiếu gọt giũa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086593",
        "hw": "inconformity",
        "pos": "noun",
        "ipa": "/ˌɪnkənˈfɔːrməti/",
        "vi": "sự không tuân phục; tính khác biệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086594",
        "hw": "incongruence",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːŋɡruəns/",
        "vi": "sự không tương thích; tính bất nhất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086595",
        "hw": "incongruently",
        "pos": "adv",
        "ipa": "/ɪnˈkɑːŋɡruəntli/",
        "vi": "một cách khập khiễng; bất nhất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086596",
        "hw": "incongruousness",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːŋɡruəsnəs/",
        "vi": "sự lạc lõng; tính cọc cạch phi lý",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086597",
        "hw": "inconnu",
        "pos": "noun",
        "ipa": "/ˌæŋkəˈnuː/",
        "vi": "người lạ mặt; cá hồi trắng inconnu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086598",
        "hw": "inconnus",
        "pos": "noun",
        "ipa": "/ˌæŋkəˈnuːz/",
        "vi": "những người lạ mặt; cá hồi trắng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086599",
        "hw": "inconquerable",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːŋkərəbəl/",
        "vi": "bất khả chiến bại; khôn khuất phục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086600",
        "hw": "inconsecutive",
        "pos": "adj",
        "ipa": "/ˌɪnkənˈsɛkjətɪv/",
        "vi": "không liên tiếp; rời rạc đứt quãng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086601",
        "hw": "inconsecutiveness",
        "pos": "noun",
        "ipa": "/ˌɪnkənˈsɛkjətɪvnəs/",
        "vi": "sự ngắt quãng; tính thiếu liên tục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

if __name__ == "__main__":
    assert len(data) == 100, f"Expected 100, got {len(data)}"
    with open("scratch/b18_r04_raw_p1.json") as f:
        raw = json.load(f)
    assert len(raw) == 100, f"Expected 100 raw, got {len(raw)}"
    for i in range(100):
        d = data[i]
        r = raw[i]
        assert d["id"] == r["id"], f"ID mismatch at {i}: {d['id']} vs {r['id']}"
        assert d["hw"] == r["hw"], f"HW mismatch at {i}: {d['hw']} vs {r['hw']}"
        assert d["cefr"] == r["cefr"], f"CEFR mismatch at {i}: {d['cefr']} vs {r['cefr']}"
        assert d["tier"] == r["tier"], f"TIER mismatch at {i}: {d['tier']} vs {r['tier']}"
        assert d["notes"] == r["notes"], f"NOTES mismatch at {i}: {d['notes']} vs {r['notes']}"
        assert d["status"] == "reviewed", f"Status not reviewed at {i}"
        assert d["ipa"].startswith("/") and d["ipa"].endswith("/") and d["ipa"].count("/") == 2, f"Bad IPA at {i}: {d['ipa']}"
        assert len(d["vi"]) <= 35, f"VI too long at {i} ({len(d['vi'])}): {d['vi']}"
        assert d["pos"] in ["noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"], f"Invalid pos at {i}: {d['pos']}"
    print("ALL 100 RECORDS IN ROUND 4 PART 1 VERIFIED SUCCESSFULLY!")
