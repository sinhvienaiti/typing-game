import json

reviewed_records = [
    {
        "id": "lex.en.100k.082502",
        "hw": "grains",
        "pos": "noun",
        "ipa": "/ɡreɪnz/",
        "vi": "các hạt ngũ cốc; cây xiên cá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082503",
        "hw": "grallock",
        "pos": "noun",
        "ipa": "/ˈɡræl.ək/",
        "vi": "bộ lòng hươu nai; nội tạng hươu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082504",
        "hw": "gramarye",
        "pos": "noun",
        "ipa": "/ˈɡræm.ɚ.i/",
        "vi": "phép ma thuật; yêu thuật cổ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082505",
        "hw": "graminaceae",
        "pos": "noun",
        "ipa": "/ˌɡræm.ɪˈneɪ.siˌiː/",
        "vi": "họ hòa thảo; họ lúa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082506",
        "hw": "graminaceous",
        "pos": "adj",
        "ipa": "/ˌɡræm.ɪˈneɪ.ʃəs/",
        "vi": "thuộc họ hòa thảo; giống như cỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082507",
        "hw": "graminales",
        "pos": "noun",
        "ipa": "/ˌɡræm.ɪˈneɪ.liːz/",
        "vi": "bộ hòa thảo; bộ cỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082508",
        "hw": "gramineous",
        "pos": "adj",
        "ipa": "/ɡrəˈmɪn.i.əs/",
        "vi": "thuộc loài cỏ; giống như cỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082509",
        "hw": "gramineousness",
        "pos": "noun",
        "ipa": "/ɡrəˈmɪn.i.əs.nəs/",
        "vi": "đặc tính cỏ; tính chất như cỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082510",
        "hw": "graminifolious",
        "pos": "adj",
        "ipa": "/ˌɡræm.ɪ.nɪˈfoʊ.li.əs/",
        "vi": "có lá dạng cỏ; lá giống lá cỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082511",
        "hw": "graminivorous",
        "pos": "adj",
        "ipa": "/ˌɡræm.ɪˈnɪv.ɚ.əs/",
        "vi": "ăn cỏ; chuyên ăn cỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082512",
        "hw": "grammalogue",
        "pos": "noun",
        "ipa": "/ˈɡræm.ə.lɑːɡ/",
        "vi": "ký hiệu tốc ký; chữ tốc ký",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082513",
        "hw": "grammatic",
        "pos": "adj",
        "ipa": "/ɡrəˈmæt̬.ɪk/",
        "vi": "thuộc ngữ pháp; đúng ngữ pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082514",
        "hw": "grammaticality",
        "pos": "noun",
        "ipa": "/ɡrəˌmæt̬.əˈkæl.ə.ti/",
        "vi": "tính đúng ngữ pháp; tính ngữ pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082515",
        "hw": "grammaticism",
        "pos": "noun",
        "ipa": "/ɡrəˈmæt̬.ə.sɪz.əm/",
        "vi": "tính ngữ pháp; thói nề hà ngữ pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082516",
        "hw": "grammaticize",
        "pos": "verb",
        "ipa": "/ɡrəˈmæt̬.ə.saɪz/",
        "vi": "ngữ pháp hóa; chuẩn hóa ngữ pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082517",
        "hw": "grammatist",
        "pos": "noun",
        "ipa": "/ˈɡræm.ə.tɪst/",
        "vi": "thầy dạy ngữ pháp; nhà ngữ pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082518",
        "hw": "grammatite",
        "pos": "noun",
        "ipa": "/ˈɡræm.ə.taɪt/",
        "vi": "khoáng vật tremolit; grammatit",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082519",
        "hw": "grammatolatry",
        "pos": "noun",
        "ipa": "/ˌɡræm.əˈtɑː.lə.tri/",
        "vi": "sự sùng bái chữ nghĩa giáo điều",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082520",
        "hw": "grammatophyllum",
        "pos": "noun",
        "ipa": "/ˌɡræm.ə.toʊˈfɪl.əm/",
        "vi": "chi lan đại; phong lan khổng lồ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082521",
        "hw": "grammophone",
        "pos": "noun",
        "ipa": "/ˈɡræm.ə.foʊn/",
        "vi": "máy quay đĩa; máy hát đĩa than",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082522",
        "hw": "gramp",
        "pos": "noun",
        "ipa": "/ɡræmp/",
        "vi": "ông nội; ông ngoại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082523",
        "hw": "grampositive",
        "pos": "adj",
        "ipa": "/ˌɡræmˈpɑː.zə.t̬ɪv/",
        "vi": "dương tính Gram; gram dương",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082524",
        "hw": "grampuses",
        "pos": "noun",
        "ipa": "/ˈɡræm.pə.sɪz/",
        "vi": "các loài cá heo xám; cá voi sấm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082525",
        "hw": "grana",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.nə/",
        "vi": "các hạt lục lạp; phiến thylakoid",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082526",
        "hw": "granadillo",
        "pos": "noun",
        "ipa": "/ˌɡræn.əˈdɪl.oʊ/",
        "vi": "gỗ cẩm lai Nam Mỹ; cây chanh dây",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082527",
        "hw": "grandam",
        "pos": "noun",
        "ipa": "/ˈɡræn.dæm/",
        "vi": "bà nội; bà ngoại; bà lão",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082528",
        "hw": "granddads",
        "pos": "noun",
        "ipa": "/ˈɡræn.dædz/",
        "vi": "các người ông; các cụ ông",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082529",
        "hw": "grandiloquences",
        "pos": "noun",
        "ipa": "/ɡrænˈdɪl.ə.kwən.sɪz/",
        "vi": "những lời khoa trương kiểu cách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082530",
        "hw": "grandiloquently",
        "pos": "adv",
        "ipa": "/ɡrænˈdɪl.ə.kwənt.li/",
        "vi": "khoa trương; hùng hồn hoa mỹ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082531",
        "hw": "grandiloquous",
        "pos": "adj",
        "ipa": "/ɡrænˈdɪl.ə.kwəs/",
        "vi": "khoa trương; huênh hoang kiểu cách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082532",
        "hw": "grandioso",
        "pos": "adv",
        "ipa": "/ɡræn.diˈoʊ.soʊ/",
        "vi": "một cách hùng tráng; trang trọng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082533",
        "hw": "grandmamma",
        "pos": "noun",
        "ipa": "/ˈɡræn.mɑː.mɑː/",
        "vi": "bà nội; bà ngoại; bà kính yêu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082534",
        "hw": "grandmas",
        "pos": "noun",
        "ipa": "/ˈɡræn.mɑːz/",
        "vi": "các người bà; các cụ bà",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082535",
        "hw": "grandmotherly",
        "pos": "adj",
        "ipa": "/ˈɡrænˌmʌð.ɚ.li/",
        "vi": "như một người bà; hiền từ như bà",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082536",
        "hw": "grandpapa",
        "pos": "noun",
        "ipa": "/ˈɡræn.pəˌpɑː/",
        "vi": "ông nội; ông ngoại; ông kính yêu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082537",
        "hw": "grandparents",
        "pos": "noun",
        "ipa": "/ˈɡrændˌpɛr.ənts/",
        "vi": "ông bà; các vị ông bà",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082538",
        "hw": "grands",
        "pos": "noun",
        "ipa": "/ɡrændz/",
        "vi": "những cây đại dương cầm; ngàn đô",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082539",
        "hw": "grandsire",
        "pos": "noun",
        "ipa": "/ˈɡrændˌsaɪ.ɚ/",
        "vi": "ông tổ; cụ tổ; tổ phụ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082540",
        "hw": "grandstander",
        "pos": "noun",
        "ipa": "/ˈɡrændˌstæn.dɚ/",
        "vi": "kẻ thích thể hiện; người khoe mẽ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082541",
        "hw": "grangerism",
        "pos": "noun",
        "ipa": "/ˈɡreɪn.dʒɚˌɪz.əm/",
        "vi": "thói ghép thêm tranh minh họa sách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082542",
        "hw": "grangerize",
        "pos": "verb",
        "ipa": "/ˈɡreɪn.dʒɚ.aɪz/",
        "vi": "chèn thêm tranh minh họa vào sách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082543",
        "hw": "graniferous",
        "pos": "adj",
        "ipa": "/ɡrəˈnɪf.ɚ.əs/",
        "vi": "có hạt; sinh hạt; mang hạt ngũ cốc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082544",
        "hw": "graniform",
        "pos": "adj",
        "ipa": "/ˈɡræn.ə.fɔːrm/",
        "vi": "có hình hạt; dạng hạt ngũ cốc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082545",
        "hw": "granitelike",
        "pos": "adj",
        "ipa": "/ˈɡræn.ɪt.laɪk/",
        "vi": "cứng như đá granit; rắn như đá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082546",
        "hw": "graniteware",
        "pos": "noun",
        "ipa": "/ˈɡræn.ɪt.wɛər/",
        "vi": "đồ tráng men đốm xám kiểu granit",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082547",
        "hw": "granitite",
        "pos": "noun",
        "ipa": "/ˈɡræn.ə.taɪt/",
        "vi": "đá granitit; đá granit biotit",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082548",
        "hw": "granitoid",
        "pos": "adj",
        "ipa": "/ˈɡræn.ə.tɔɪd/",
        "vi": "dạng granit; tựa đá hoa cương",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082549",
        "hw": "granivorous",
        "pos": "adj",
        "ipa": "/ɡrəˈnɪv.ɚ.əs/",
        "vi": "ăn hạt; chuyên ăn ngũ cốc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082550",
        "hw": "granodiorite",
        "pos": "noun",
        "ipa": "/ˌɡræn.oʊˈdaɪ.ə.raɪt/",
        "vi": "đá granodiorit; đá hoa cương hoa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082551",
        "hw": "granolith",
        "pos": "noun",
        "ipa": "/ˈɡræn.ə.lɪθ/",
        "vi": "bê tông granit; đá nhân tạo granit",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082552",
        "hw": "granolithic",
        "pos": "adj",
        "ipa": "/ˌɡræn.əˈlɪθ.ɪk/",
        "vi": "thuộc bê tông granit nhân tạo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082553",
        "hw": "granoscaling",
        "pos": "noun",
        "ipa": "/ˌɡræn.oʊˈskeɪ.lɪŋ/",
        "vi": "sự phốt phát hóa bề mặt kim loại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082554",
        "hw": "granose",
        "pos": "adj",
        "ipa": "/ˈɡræn.oʊs/",
        "vi": "dạng chuỗi hạt; sần hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082555",
        "hw": "grantable",
        "pos": "adj",
        "ipa": "/ˈɡræn.t̬ə.bəl/",
        "vi": "có thể ban cấp; có thể chấp thuận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082556",
        "hw": "granting",
        "pos": "verb",
        "ipa": "/ˈɡræn.t̬ɪŋ/",
        "vi": "đang ban cấp; chấp thuận; cho phép",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082557",
        "hw": "grants",
        "pos": "verb",
        "ipa": "/ɡrænts/",
        "vi": "ban cấp; trao cho; chấp thuận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082558",
        "hw": "granularly",
        "pos": "adv",
        "ipa": "/ˈɡræn.jə.lɚ.li/",
        "vi": "thành dạng hạt; chi tiết từng phần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082559",
        "hw": "granulates",
        "pos": "verb",
        "ipa": "/ˈɡræn.jə.leɪts/",
        "vi": "tạo thành hạt; nghiền thành hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082560",
        "hw": "granulating",
        "pos": "verb",
        "ipa": "/ˈɡræn.jə.leɪ.tɪŋ/",
        "vi": "đang tạo hạt; làm thành hạt nhỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082561",
        "hw": "granulative",
        "pos": "adj",
        "ipa": "/ˈɡræn.jə.leɪ.t̬ɪv/",
        "vi": "tạo hạt mô hạt; làm thành hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082562",
        "hw": "granulator",
        "pos": "noun",
        "ipa": "/ˈɡræn.jə.leɪ.t̬ɚ/",
        "vi": "máy nghiền hạt; máy tạo hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082563",
        "hw": "granuliferous",
        "pos": "adj",
        "ipa": "/ˌɡræn.jəˈlɪf.ɚ.əs/",
        "vi": "chứa hạt nhỏ; có cấu trúc hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082564",
        "hw": "granulite",
        "pos": "noun",
        "ipa": "/ˈɡræn.jə.laɪt/",
        "vi": "đá granulit; đá biến chất hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082565",
        "hw": "granulitic",
        "pos": "adj",
        "ipa": "/ˌɡræn.jəˈlɪt̬.ɪk/",
        "vi": "thuộc đá granulit; có cấu trúc hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082566",
        "hw": "granulocytopenia",
        "pos": "noun",
        "ipa": "/ˌɡræn.jə.loʊˌsaɪ.toʊˈpiː.ni.ə/",
        "vi": "chứng giảm bạch cầu hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082567",
        "hw": "granulometry",
        "pos": "noun",
        "ipa": "/ˌɡræn.jəˈlɑː.mə.tri/",
        "vi": "phép đo cỡ hạt; phép phân tích hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082568",
        "hw": "granulous",
        "pos": "adj",
        "ipa": "/ˈɡræn.jə.ləs/",
        "vi": "có nhiều hạt nhỏ; lợn cợn hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082569",
        "hw": "grapefruits",
        "pos": "noun",
        "ipa": "/ˈɡreɪp.fruːts/",
        "vi": "các quả bưởi chùm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082570",
        "hw": "grapelike",
        "pos": "adj",
        "ipa": "/ˈɡreɪp.laɪk/",
        "vi": "dạng chùm nho; giống quả nho",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082571",
        "hw": "grapery",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.pɚ.i/",
        "vi": "nhà kính trồng nho; vườn nho",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082572",
        "hw": "graphed",
        "pos": "verb",
        "ipa": "/ɡræft/",
        "vi": "đã vẽ đồ thị; đã biểu diễn đồ thị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082573",
        "hw": "graphemic",
        "pos": "adj",
        "ipa": "/ɡræˈfiː.mɪk/",
        "vi": "thuộc chữ viết; thuộc tự vị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082574",
        "hw": "graphemics",
        "pos": "noun",
        "ipa": "/ɡræˈfiː.mɪks/",
        "vi": "nghiên cứu tự vị; tự vị học",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082575",
        "hw": "grapher",
        "pos": "noun",
        "ipa": "/ˈɡræf.ɚ/",
        "vi": "máy ghi tự động; máy vẽ đồ thị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082576",
        "hw": "graphicness",
        "pos": "noun",
        "ipa": "/ˈɡræf.ɪk.nəs/",
        "vi": "tính sinh động; tính trực quan",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082577",
        "hw": "graphing",
        "pos": "verb",
        "ipa": "/ˈɡræf.ɪŋ/",
        "vi": "đang vẽ đồ thị; biểu diễn đồ thị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082578",
        "hw": "graphitic",
        "pos": "adj",
        "ipa": "/ɡræˈfɪt̬.ɪk/",
        "vi": "thuộc than chì; chứa grafit",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082579",
        "hw": "graphitization",
        "pos": "noun",
        "ipa": "/ˌɡræf.ə.t̬əˈzeɪ.ʃən/",
        "vi": "sự grafit hóa; quá trình hóa chì",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082580",
        "hw": "graphitize",
        "pos": "verb",
        "ipa": "/ˈɡræf.ə.taɪz/",
        "vi": "grafit hóa; phủ lớp than chì",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082581",
        "hw": "graphological",
        "pos": "adj",
        "ipa": "/ˌɡræf.əˈlɑː.dʒɪ.kəl/",
        "vi": "thuộc thuật phân tích chữ viết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082582",
        "hw": "graphologists",
        "pos": "noun",
        "ipa": "/ɡræfˈɑː.lə.dʒɪsts/",
        "vi": "các chuyên gia phân tích chữ viết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082583",
        "hw": "graphospasm",
        "pos": "noun",
        "ipa": "/ˈɡræf.oʊˌspæz.əm/",
        "vi": "chứng chuột rút khi viết; vọp bẻ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082584",
        "hw": "graphs",
        "pos": "verb",
        "ipa": "/ɡræfs/",
        "vi": "vẽ đồ thị; biểu diễn trên đồ thị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082585",
        "hw": "grapo",
        "pos": "noun",
        "ipa": "/ˈɡræp.oʊ/",
        "vi": "củ từ tím; giống khoai mỡ caribe",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082586",
        "hw": "grappled",
        "pos": "verb",
        "ipa": "/ˈɡræp.əld/",
        "vi": "đã vật lộn; đã giằng co giải quyết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082587",
        "hw": "grapples",
        "pos": "verb",
        "ipa": "/ˈɡræp.əlz/",
        "vi": "vật lộn; giằng co; cố giải quyết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082588",
        "hw": "graptolite",
        "pos": "noun",
        "ipa": "/ˈɡræp.təˌlaɪt/",
        "vi": "hóa thạch bút đá; cổ sinh graptolit",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082589",
        "hw": "graptophyllum",
        "pos": "noun",
        "ipa": "/ˌɡræp.toʊˈfɪl.əm/",
        "vi": "chi cây lá màu; cây huyết hạnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082590",
        "hw": "grapy",
        "pos": "adj",
        "ipa": "/ˈɡreɪ.pi/",
        "vi": "có vị nho; thơm mùi nho; như nho",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082591",
        "hw": "graspingly",
        "pos": "adv",
        "ipa": "/ˈɡræs.pɪŋ.li/",
        "vi": "một cách tham lam; vồ vập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082592",
        "hw": "graspingness",
        "pos": "noun",
        "ipa": "/ˈɡræs.pɪŋ.nəs/",
        "vi": "tính tham lam; sự vơ vét hám lợi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082593",
        "hw": "graspless",
        "pos": "adj",
        "ipa": "/ˈɡræsp.ləs/",
        "vi": "không nắm giữ được; trơn tuột",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082594",
        "hw": "grassed",
        "pos": "verb",
        "ipa": "/ɡræst/",
        "vi": "đã trồng cỏ; đã tố cáo chỉ điểm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082595",
        "hw": "grasses",
        "pos": "verb",
        "ipa": "/ˈɡræs.ɪz/",
        "vi": "trồng cỏ phủ xanh; tố giác kẻ xấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082596",
        "hw": "grassfinch",
        "pos": "noun",
        "ipa": "/ˈɡræs.fɪntʃ/",
        "vi": "chim sẻ cỏ Úc; chim di thảo nguyên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082597",
        "hw": "grasshoppers",
        "pos": "noun",
        "ipa": "/ˈɡræsˌhɑː.pɚz/",
        "vi": "các con châu chấu; các con cào cào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082598",
        "hw": "grassiness",
        "pos": "noun",
        "ipa": "/ˈɡræs.i.nəs/",
        "vi": "tình trạng phủ đầy cỏ; mùi cỏ tươi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082599",
        "hw": "grassing",
        "pos": "verb",
        "ipa": "/ˈɡræs.ɪŋ/",
        "vi": "đang phủ cỏ; thả ăn cỏ; tố cáo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082600",
        "hw": "grassless",
        "pos": "adj",
        "ipa": "/ˈɡræs.ləs/",
        "vi": "không có cỏ; trơ trụi cằn cỗi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082601",
        "hw": "grasslike",
        "pos": "adj",
        "ipa": "/ˈɡræs.laɪk/",
        "vi": "giống như cỏ; tựa như lá cỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

# Validation
with open("scratch/b17_r06_raw_p1.json") as f:
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
