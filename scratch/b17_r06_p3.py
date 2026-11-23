import json

reviewed_records = [
    {
        "id": "lex.en.100k.082702",
        "hw": "grieves",
        "pos": "verb",
        "ipa": "/ɡriːvz/",
        "vi": "đau buồn; thương xót; sầu não",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082703",
        "hw": "grievingly",
        "pos": "adv",
        "ipa": "/ˈɡriː.vɪŋ.li/",
        "vi": "một cách đau buồn; xót xa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082704",
        "hw": "grievousness",
        "pos": "noun",
        "ipa": "/ˈɡriː.vəs.nəs/",
        "vi": "tính nghiêm trọng; nỗi đau đớn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082705",
        "hw": "griff",
        "pos": "noun",
        "ipa": "/ɡrɪf/",
        "vi": "người mới đến Ấn Độ; tin tức ngầm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082706",
        "hw": "griffonage",
        "pos": "noun",
        "ipa": "/ˌɡrɪf.əˈnɑːʒ/",
        "vi": "chữ viết nghệch ngoạc; nét nguệch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082707",
        "hw": "grig",
        "pos": "noun",
        "ipa": "/ɡrɪɡ/",
        "vi": "lươn nhỏ; con dế; người vui vẻ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082708",
        "hw": "grillage",
        "pos": "noun",
        "ipa": "/ˈɡrɪl.ɪdʒ/",
        "vi": "hệ dầm móng; giàn dầm chịu lực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082709",
        "hw": "grillroom",
        "pos": "noun",
        "ipa": "/ˈɡrɪl.ruːm/",
        "vi": "quán đồ nướng; nhà hàng nướng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082710",
        "hw": "grills",
        "pos": "verb",
        "ipa": "/ɡrɪlz/",
        "vi": "nướng vỉ; tra khảo dồn dập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082711",
        "hw": "grilse",
        "pos": "noun",
        "ipa": "/ɡrɪls/",
        "vi": "cá hồi non một năm tuổi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082712",
        "hw": "grimaced",
        "pos": "verb",
        "ipa": "/ˈɡrɪm.əst/",
        "vi": "đã nhăn mặt; đã làm mặt méo mó",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082713",
        "hw": "grimacer",
        "pos": "noun",
        "ipa": "/ˈɡrɪm.ə.sɚ/",
        "vi": "người hay nhăn nhó; kẻ làm mặt xấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082714",
        "hw": "grimaces",
        "pos": "noun",
        "ipa": "/ˈɡrɪm.ə.sɪz/",
        "vi": "những vẻ nhăn nhó; nét mặt méo mó",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082715",
        "hw": "grimacier",
        "pos": "noun",
        "ipa": "/ˌɡrɪm.əˈsjeɪ/",
        "vi": "kẻ hay nhăn nhó; người làm bộ dạng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082716",
        "hw": "grimacing",
        "pos": "verb",
        "ipa": "/ˈɡrɪm.ə.sɪŋ/",
        "vi": "đang nhăn mặt; nhăn nhó khó chịu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082717",
        "hw": "grimalkin",
        "pos": "noun",
        "ipa": "/ɡrɪˈmæl.kɪn/",
        "vi": "mèo cái già; mụ già ác nghiệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082718",
        "hw": "grimed",
        "pos": "verb",
        "ipa": "/ɡraɪmd/",
        "vi": "đã làm bám bẩn; cáu ghét đầy bụi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082719",
        "hw": "grimes",
        "pos": "verb",
        "ipa": "/ɡraɪmz/",
        "vi": "làm bám bụi bẩn; làm dính cáu bẩn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082720",
        "hw": "grimily",
        "pos": "adv",
        "ipa": "/ˈɡraɪ.məl.i/",
        "vi": "một cách lem luốc; dơ dáy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082721",
        "hw": "griminess",
        "pos": "noun",
        "ipa": "/ˈɡraɪ.mi.nəs/",
        "vi": "tình trạng cáu bẩn; sự lem luốc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082722",
        "hw": "griming",
        "pos": "verb",
        "ipa": "/ˈɡraɪ.mɪŋ/",
        "vi": "đang làm bám bẩn; phủ lớp cáu bẩn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082723",
        "hw": "grindability",
        "pos": "noun",
        "ipa": "/ˌɡraɪn.dəˈbɪl.ə.ti/",
        "vi": "khả năng nghiền nhỏ; độ dễ mài mòn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082724",
        "hw": "grindelia",
        "pos": "noun",
        "ipa": "/ɡrɪnˈdiː.li.ə/",
        "vi": "chi cúc nhựa; cây grindelia",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082725",
        "hw": "grinders",
        "pos": "noun",
        "ipa": "/ˈɡraɪn.dɚz/",
        "vi": "các máy nghiền; các răng hàm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082726",
        "hw": "grindery",
        "pos": "noun",
        "ipa": "/ˈɡraɪn.dɚ.i/",
        "vi": "đồ nghề đóng giày; dụng cụ thợ giày",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082727",
        "hw": "grindingly",
        "pos": "adv",
        "ipa": "/ˈɡraɪn.dɪŋ.li/",
        "vi": "nghiến ken két; nặng nề khốc liệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082728",
        "hw": "grinds",
        "pos": "noun",
        "ipa": "/ɡraɪndz/",
        "vi": "những công việc cực nhọc; bã cà phê",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082729",
        "hw": "grinned",
        "pos": "verb",
        "ipa": "/ɡrɪnd/",
        "vi": "đã cười toe toét; đã nhoẻn cười",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082730",
        "hw": "grinningly",
        "pos": "adv",
        "ipa": "/ˈɡrɪn.ɪŋ.li/",
        "vi": "một cách toe toét; cười toe toét",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082731",
        "hw": "grins",
        "pos": "verb",
        "ipa": "/ɡrɪnz/",
        "vi": "cười toe toét; nhoẻn miệng cười",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082732",
        "hw": "griper",
        "pos": "noun",
        "ipa": "/ˈɡraɪ.pɚ/",
        "vi": "kẻ hay cằn nhằn; người hay phàn nàn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082733",
        "hw": "gripped",
        "pos": "verb",
        "ipa": "/ɡrɪpt/",
        "vi": "đã nắm chặt; đã cuốn hút mãnh liệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082734",
        "hw": "gripper",
        "pos": "noun",
        "ipa": "/ˈɡrɪp.ɚ/",
        "vi": "bộ kẹp; càng kẹp cơ khí; tay gắp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082735",
        "hw": "grippes",
        "pos": "noun",
        "ipa": "/ɡrɪps/",
        "vi": "các đợt cúm mùa; bệnh cảm cúm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082736",
        "hw": "grippingly",
        "pos": "adv",
        "ipa": "/ˈɡrɪp.ɪŋ.li/",
        "vi": "một cách lôi cuốn; đầy hấp dẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082737",
        "hw": "grippy",
        "pos": "adj",
        "ipa": "/ˈɡrɪp.i/",
        "vi": "bám chắc; dính chặt; có độ ma sát",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082738",
        "hw": "grips",
        "pos": "verb",
        "ipa": "/ɡrɪps/",
        "vi": "nắm chặt; kẹp chặt; lôi cuốn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082739",
        "hw": "gripsack",
        "pos": "noun",
        "ipa": "/ˈɡrɪp.sæk/",
        "vi": "túi xách du lịch; vali nhỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082740",
        "hw": "griqua",
        "pos": "noun",
        "ipa": "/ˈɡriː.kwə/",
        "vi": "người Griqua; tộc người lai Nam Phi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082741",
        "hw": "griselinia",
        "pos": "noun",
        "ipa": "/ˌɡrɪs.əˈlɪn.i.ə/",
        "vi": "chi cây thường xanh Griselinia",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082742",
        "hw": "griseous",
        "pos": "adj",
        "ipa": "/ˈɡrɪz.i.əs/",
        "vi": "có màu xám tro; màu lam xám",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082743",
        "hw": "grisette",
        "pos": "noun",
        "ipa": "/ɡrɪˈzɛt/",
        "vi": "cô thợ may Pháp; cô gái lao động",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082744",
        "hw": "griskin",
        "pos": "noun",
        "ipa": "/ˈɡrɪs.kɪn/",
        "vi": "thịt thăn lợn; miếng nạc lưng lợn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082745",
        "hw": "grisliness",
        "pos": "noun",
        "ipa": "/ˈɡrɪz.li.nəs/",
        "vi": "tính rùng rợn; nỗi ghê sợ hãi hùng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082746",
        "hw": "grison",
        "pos": "noun",
        "ipa": "/ˈɡraɪ.sən/",
        "vi": "chồn grison; loài chồn Nam Mỹ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082747",
        "hw": "grissino",
        "pos": "noun",
        "ipa": "/ɡrɪˈsiː.noʊ/",
        "vi": "que bánh mì giòn Ý; que bánh mì",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082748",
        "hw": "gristliness",
        "pos": "noun",
        "ipa": "/ˈɡrɪs.li.nəs/",
        "vi": "tình trạng nhiều sụn; độ gân guốc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082749",
        "hw": "gritrock",
        "pos": "noun",
        "ipa": "/ˈɡrɪt.rɑːk/",
        "vi": "đá sa thạch hạt thô; đá sạn kết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082750",
        "hw": "gritstones",
        "pos": "noun",
        "ipa": "/ˈɡrɪtˌstoʊnz/",
        "vi": "các khối đá sa thạch thô",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082751",
        "hw": "grittily",
        "pos": "adv",
        "ipa": "/ˈɡrɪt̬.əl.i/",
        "vi": "với sự can trường; lạo xạo có sạn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082752",
        "hw": "grittiness",
        "pos": "noun",
        "ipa": "/ˈɡrɪt̬.i.nəs/",
        "vi": "tính có sạn; sự kiên cường góc cạnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082753",
        "hw": "grivet",
        "pos": "noun",
        "ipa": "/ˈɡrɪv.ɪt/",
        "vi": "khỉ grivet châu Phi; khỉ lục xám",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082754",
        "hw": "grizzles",
        "pos": "verb",
        "ipa": "/ˈɡrɪz.əlz/",
        "vi": "cằn nhằn; mè nheo; ngả màu xám bạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082755",
        "hw": "grizzling",
        "pos": "verb",
        "ipa": "/ˈɡrɪz.əl.ɪŋ/",
        "vi": "đang cằn nhằn; mè nheo; hóa hoa râm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082756",
        "hw": "groak",
        "pos": "verb",
        "ipa": "/ɡroʊk/",
        "vi": "nhìn thèm thuồng người khác ăn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082757",
        "hw": "groaned",
        "pos": "verb",
        "ipa": "/ɡroʊnd/",
        "vi": "đã rên rỉ; đã kêu than đau đớn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082758",
        "hw": "groaning",
        "pos": "adj",
        "ipa": "/ˈɡroʊ.nɪŋ/",
        "vi": "rên rỉ than van; kĩu kịt trĩu nặng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082759",
        "hw": "groaningly",
        "pos": "adv",
        "ipa": "/ˈɡroʊ.nɪŋ.li/",
        "vi": "với tiếng rên rỉ; thở than ai oán",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082760",
        "hw": "groans",
        "pos": "verb",
        "ipa": "/ɡroʊnz/",
        "vi": "rên rỉ; thở than; kêu cót két",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082761",
        "hw": "grobian",
        "pos": "noun",
        "ipa": "/ˈɡroʊ.bi.ən/",
        "vi": "kẻ thô lỗ vụng về; người cục cằn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082762",
        "hw": "groceries",
        "pos": "noun",
        "ipa": "/ˈɡroʊ.sɚ.iz/",
        "vi": "hàng tạp hóa; đồ nhu yếu phẩm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082763",
        "hw": "grocers",
        "pos": "noun",
        "ipa": "/ˈɡroʊ.sɚz/",
        "vi": "những người bán hàng tạp hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082764",
        "hw": "groceteria",
        "pos": "noun",
        "ipa": "/ˌɡroʊ.səˈtɛər.i.ə/",
        "vi": "cửa hàng tạp hóa tự phục vụ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082765",
        "hw": "groenendael",
        "pos": "noun",
        "ipa": "/ˈɡruːn.ən.dɑːl/",
        "vi": "chó chăn cừu Groenendael của Bỉ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082766",
        "hw": "groenlandia",
        "pos": "noun",
        "ipa": "/ˌɡruːnˈlæn.di.ə/",
        "vi": "chi rong ráng nước ngọt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082767",
        "hw": "groggery",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.ɡɚ.i/",
        "vi": "quán rượu bình dân; tiệm rượu tồi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082768",
        "hw": "groggily",
        "pos": "adv",
        "ipa": "/ˈɡrɑː.ɡəl.i/",
        "vi": "chếnh choáng; lảo đảo loạng choạng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082769",
        "hw": "grogram",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.ɡrəm/",
        "vi": "vải grogram sợi thô dệt len tơ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082770",
        "hw": "groined",
        "pos": "adj",
        "ipa": "/ɡrɔɪnd/",
        "vi": "có vòm chéo góc; có múi vòm giao",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082771",
        "hw": "groining",
        "pos": "noun",
        "ipa": "/ˈɡrɔɪ.nɪŋ/",
        "vi": "kết cấu múi vòm giao; gờ vòm cong",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082772",
        "hw": "groins",
        "pos": "noun",
        "ipa": "/ɡrɔɪnz/",
        "vi": "các vùng háng; các bờ kè chắn sóng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082773",
        "hw": "gromet",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.mɪt/",
        "vi": "vòng dây đệm; khoen xỏ dây kim loại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082774",
        "hw": "gromwell",
        "pos": "noun",
        "ipa": "/ˈɡrɑːm.wɛl/",
        "vi": "cây tử thảo; thảo dược gromwell",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082775",
        "hw": "gronland",
        "pos": "noun",
        "ipa": "/ˈɡrɑːn.lənd/",
        "vi": "đảo Greenland; xứ Băng Đảo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082776",
        "hw": "groomer",
        "pos": "noun",
        "ipa": "/ˈɡruː.mɚ/",
        "vi": "thợ làm đẹp thú cưng; máy san tuyết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082777",
        "hw": "grooms",
        "pos": "verb",
        "ipa": "/ɡruːmz/",
        "vi": "chải lông thú; đào tạo rèn giũa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082778",
        "hw": "grooveability",
        "pos": "noun",
        "ipa": "/ˌɡruː.vəˈbɪl.ə.ti/",
        "vi": "khả năng tạo rãnh; độ dễ xẻ rãnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082779",
        "hw": "grooves",
        "pos": "verb",
        "ipa": "/ɡruːvz/",
        "vi": "xẻ rãnh; tạo khe; phiêu theo nhạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082780",
        "hw": "grooviness",
        "pos": "noun",
        "ipa": "/ˈɡruː.vi.nəs/",
        "vi": "nét thời thượng; vẻ sành điệu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082781",
        "hw": "groped",
        "pos": "verb",
        "ipa": "/ɡroʊpt/",
        "vi": "đã mò mẫm; đã sờ soạng tìm kiếm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082782",
        "hw": "groper",
        "pos": "noun",
        "ipa": "/ˈɡroʊ.pɚ/",
        "vi": "kẻ sờ soạng quấy rối; loài cá mú",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082783",
        "hw": "gropes",
        "pos": "verb",
        "ipa": "/ɡroʊps/",
        "vi": "mò mẫm tìm đường; sờ soạng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082784",
        "hw": "gropingly",
        "pos": "adv",
        "ipa": "/ˈɡroʊ.pɪŋ.li/",
        "vi": "một cách dò dẫm; mò mẫm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082785",
        "hw": "gros",
        "pos": "adj",
        "ipa": "/ɡroʊ/",
        "vi": "dày dặn; thô sợi; lớn bản",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082786",
        "hw": "grossbeak",
        "pos": "noun",
        "ipa": "/ˈɡroʊs.biːk/",
        "vi": "chim mỏ to; chim sẻ mỏ lớn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082787",
        "hw": "grossed",
        "pos": "verb",
        "ipa": "/ɡroʊst/",
        "vi": "đã thu tổng cộng; đã làm kinh tởm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082788",
        "hw": "grosses",
        "pos": "verb",
        "ipa": "/ˈɡroʊ.sɪz/",
        "vi": "thu tổng doanh thu; làm kinh tởm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082789",
        "hw": "grossing",
        "pos": "verb",
        "ipa": "/ˈɡroʊ.sɪŋ/",
        "vi": "đang thu tổng cộng; làm buồn nôn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082790",
        "hw": "grossulariaceae",
        "pos": "noun",
        "ipa": "/ˌɡrɑː.səˌlɛr.iˈeɪ.siˌiː/",
        "vi": "họ phúc bồn tử; họ lý chua",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082791",
        "hw": "grossularite",
        "pos": "noun",
        "ipa": "/ˈɡrɑːs.jə.ləˌraɪt/",
        "vi": "khoáng vật ngọc thạch lựu lục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082792",
        "hw": "grote",
        "pos": "noun",
        "ipa": "/ɡroʊt/",
        "vi": "đồng groat cổ; đồng bốn xu Anh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082793",
        "hw": "grotesquery",
        "pos": "noun",
        "ipa": "/ɡroʊˈtɛsk.ɚ.i/",
        "vi": "sự kỳ dị dị hợm; nét quái đản",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082794",
        "hw": "grottiness",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.ti.nəs/",
        "vi": "sự nhếch nhác; vẻ tồi tàn bẩn thỉu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082795",
        "hw": "grottoes",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.toʊz/",
        "vi": "những hang động nhân tạo; động nhỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082796",
        "hw": "grouched",
        "pos": "verb",
        "ipa": "/ɡraʊtʃt/",
        "vi": "đã càu nhàu; đã cằn nhằn cúp mặt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082797",
        "hw": "grouches",
        "pos": "verb",
        "ipa": "/ˈɡraʊ.tʃɪz/",
        "vi": "càu nhàu gắt gỏng; cằn nhằn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082798",
        "hw": "grouchily",
        "pos": "adv",
        "ipa": "/ˈɡraʊ.tʃəl.i/",
        "vi": "một cách gắt gỏng; càu nhàu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082799",
        "hw": "grouchiness",
        "pos": "noun",
        "ipa": "/ˈɡraʊ.tʃi.nəs/",
        "vi": "tính gắt gỏng; thói càu nhàu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082800",
        "hw": "grouching",
        "pos": "verb",
        "ipa": "/ˈɡraʊ.tʃɪŋ/",
        "vi": "đang càu nhàu gắt gỏng; cằn nhằn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082801",
        "hw": "groundage",
        "pos": "noun",
        "ipa": "/ˈɡraʊn.dɪdʒ/",
        "vi": "thuế cắm neo cảng; phí neo đậu tàu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

# Validation
with open("scratch/b17_r06_raw_p3.json") as f:
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

print("All 100 records in Part 3 verified successfully!")
