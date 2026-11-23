import json

reviewed_records = [
    {
        "id": "lex.en.100k.082602",
        "hw": "grated",
        "pos": "verb",
        "ipa": "/ˈɡreɪ.t̬ɪd/",
        "vi": "đã nạo vụn; đã nghiến ken két",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082603",
        "hw": "grates",
        "pos": "verb",
        "ipa": "/ɡreɪts/",
        "vi": "nạo vụn; mài nhỏ; kêu ken két",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082604",
        "hw": "gratifications",
        "pos": "noun",
        "ipa": "/ˌɡræt̬.ə.fəˈkeɪ.ʃənz/",
        "vi": "sự thỏa mãn; những niềm hài lòng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082605",
        "hw": "gratifier",
        "pos": "noun",
        "ipa": "/ˈɡræt̬.ə.faɪ.ɚ/",
        "vi": "người làm vừa lòng; điều thỏa lòng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082606",
        "hw": "gratifies",
        "pos": "verb",
        "ipa": "/ˈɡræt̬.ə.faɪz/",
        "vi": "làm hài lòng; làm thỏa mãn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082607",
        "hw": "gratin",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.tæn/",
        "vi": "món đút lò phủ phô mai vụn bánh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082608",
        "hw": "gratings",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.t̬ɪŋz/",
        "vi": "các tấm vỉ sắt; tiếng ken két",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082609",
        "hw": "gratuitousness",
        "pos": "noun",
        "ipa": "/ɡrəˈtuː.ə.t̬əs.nəs/",
        "vi": "tính không căn cứ; sự cho không",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082610",
        "hw": "gratulatory",
        "pos": "adj",
        "ipa": "/ˈɡrætʃ.ə.lə.tɔːr.i/",
        "vi": "chúc mừng; biểu lộ niềm vui mừng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082611",
        "hw": "gravamen",
        "pos": "noun",
        "ipa": "/ɡrəˈveɪ.mən/",
        "vi": "điểm mấu chốt của lời khiếu nại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082612",
        "hw": "graved",
        "pos": "verb",
        "ipa": "/ɡreɪvd/",
        "vi": "đã khắc sâu; đã cạo sạch đáy tàu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082613",
        "hw": "graveless",
        "pos": "adj",
        "ipa": "/ˈɡreɪv.ləs/",
        "vi": "không mồ mả; không được chôn cất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082614",
        "hw": "gravelled",
        "pos": "verb",
        "ipa": "/ˈɡræv.əld/",
        "vi": "đã rải sỏi; đã làm bối rối",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082615",
        "hw": "gravelling",
        "pos": "verb",
        "ipa": "/ˈɡræv.əl.ɪŋ/",
        "vi": "đang rải sỏi; làm bối rối",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082616",
        "hw": "gravels",
        "pos": "verb",
        "ipa": "/ˈɡræv.əlz/",
        "vi": "rải sỏi lên; làm lúng túng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082617",
        "hw": "gravelweed",
        "pos": "noun",
        "ipa": "/ˈɡræv.əl.wiːd/",
        "vi": "cây thạch hương; cỏ rễ sỏi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082618",
        "hw": "graverobber",
        "pos": "noun",
        "ipa": "/ˈɡreɪvˌrɑː.bɚ/",
        "vi": "kẻ trộm mộ; kẻ đào trộm tử thi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082619",
        "hw": "gravers",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.vɚz/",
        "vi": "những dao chạm khắc; thợ chạm trổ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082620",
        "hw": "gravidation",
        "pos": "noun",
        "ipa": "/ˌɡræv.əˈdeɪ.ʃən/",
        "vi": "sự thụ thai; sự mang thai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082621",
        "hw": "gravidity",
        "pos": "noun",
        "ipa": "/ɡrəˈvɪd.ə.ti/",
        "vi": "thai kỳ; tình trạng mang thai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082622",
        "hw": "gravidly",
        "pos": "adv",
        "ipa": "/ˈɡræv.ɪd.li/",
        "vi": "nặng nề; một cách trĩu nặng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082623",
        "hw": "gravidness",
        "pos": "noun",
        "ipa": "/ˈɡræv.ɪd.nəs/",
        "vi": "tình trạng mang thai; sự nặng trĩu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082624",
        "hw": "graving",
        "pos": "verb",
        "ipa": "/ˈɡreɪ.vɪŋ/",
        "vi": "đang khắc chạm; cạo sạch đáy tàu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082625",
        "hw": "gravitant",
        "pos": "adj",
        "ipa": "/ˈɡræv.ɪ.tənt/",
        "vi": "hướng trọng lực; hút theo trọng lực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082626",
        "hw": "gravitated",
        "pos": "verb",
        "ipa": "/ˈɡræv.ə.teɪ.t̬ɪd/",
        "vi": "đã hướng về; đã bị thu hút về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082627",
        "hw": "gravitater",
        "pos": "noun",
        "ipa": "/ˈɡræv.ə.teɪ.t̬ɚ/",
        "vi": "vật bị hút về; người hướng về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082628",
        "hw": "gravitates",
        "pos": "verb",
        "ipa": "/ˈɡræv.ə.teɪts/",
        "vi": "hướng về; bị cuốn hút về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082629",
        "hw": "gravitatinal",
        "pos": "adj",
        "ipa": "/ˌɡræv.ɪˈteɪ.ʃən.əl/",
        "vi": "thuộc trọng lực; do hấp dẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082630",
        "hw": "gravitating",
        "pos": "verb",
        "ipa": "/ˈɡræv.ə.teɪ.t̬ɪŋ/",
        "vi": "đang hướng về; bị cuốn hút về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082631",
        "hw": "gravitative",
        "pos": "adj",
        "ipa": "/ˈɡræv.ə.teɪ.t̬ɪv/",
        "vi": "do trọng lực tác động; hút hấp dẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082632",
        "hw": "gravities",
        "pos": "noun",
        "ipa": "/ˈɡræv.ə.t̬iz/",
        "vi": "các tỷ trọng; mức độ trầm trọng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082633",
        "hw": "grawlix",
        "pos": "noun",
        "ipa": "/ˈɡrɔː.lɪks/",
        "vi": "chuỗi ký tự thay tiếng chửi thề",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082634",
        "hw": "grawlixes",
        "pos": "noun",
        "ipa": "/ˈɡrɔː.lɪk.sɪz/",
        "vi": "các chuỗi ký tự thay tiếng chửi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082635",
        "hw": "grayback",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.bæk/",
        "vi": "chim dẽ xám; lính phe miền Nam",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082636",
        "hw": "grayens",
        "pos": "verb",
        "ipa": "/ˈɡreɪ.ənz/",
        "vi": "hóa bạc; ngả sang màu xám",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082637",
        "hw": "grayhen",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.hɛn/",
        "vi": "gà gô đen mái; gà gô xám",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082638",
        "hw": "graylag",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.læɡ/",
        "vi": "ngỗng trời xám; ngỗng xám châu Âu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082639",
        "hw": "grayling",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.lɪŋ/",
        "vi": "cá hồi nước ngọt xám; bướm xám",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082640",
        "hw": "grayly",
        "pos": "adv",
        "ipa": "/ˈɡreɪ.li/",
        "vi": "với sắc xám ảm đạm; xám xịt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082641",
        "hw": "grazable",
        "pos": "adj",
        "ipa": "/ˈɡreɪ.zə.bəl/",
        "vi": "thích hợp chăn thả; gặm cỏ được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082642",
        "hw": "grazeable",
        "pos": "adj",
        "ipa": "/ˈɡreɪ.zə.bəl/",
        "vi": "thích hợp chăn thả; gặm cỏ được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082643",
        "hw": "grazer",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.zɚ/",
        "vi": "động vật gặm cỏ; thú ăn cỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082644",
        "hw": "grazes",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.zɪz/",
        "vi": "các vết sầy xước; các cánh đồng cỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082645",
        "hw": "graziery",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.zɪ.ri/",
        "vi": "nghề chăn nuôi gia súc; bãi chăn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082646",
        "hw": "greaseless",
        "pos": "adj",
        "ipa": "/ˈɡriːs.ləs/",
        "vi": "không nhờn; không dính dầu mỡ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082647",
        "hw": "greasers",
        "pos": "noun",
        "ipa": "/ˈɡriː.zɚz/",
        "vi": "những thợ tra dầu mỡ máy móc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082648",
        "hw": "greases",
        "pos": "verb",
        "ipa": "/ˈɡriː.sɪz/",
        "vi": "bôi mỡ nhờn; tra dầu bôi trơn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082649",
        "hw": "greasily",
        "pos": "adv",
        "ipa": "/ˈɡriː.səl.i/",
        "vi": "dính nhiều dầu mỡ; bóng nhờn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082650",
        "hw": "greasing",
        "pos": "verb",
        "ipa": "/ˈɡriː.sɪŋ/",
        "vi": "đang bôi mỡ; tra dầu; hối lộ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082651",
        "hw": "greaten",
        "pos": "verb",
        "ipa": "/ˈɡreɪ.tən/",
        "vi": "làm lớn mạnh; khuếch trương",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082652",
        "hw": "greathearted",
        "pos": "adj",
        "ipa": "/ˌɡreɪtˈhɑːr.t̬ɪd/",
        "vi": "hào hiệp độ lượng; quả cảm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082653",
        "hw": "grecism",
        "pos": "noun",
        "ipa": "/ˈɡriː.sɪz.əm/",
        "vi": "tinh thần Hy Lạp; từ ngữ Hy Lạp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082654",
        "hw": "grecize",
        "pos": "verb",
        "ipa": "/ˈɡriː.saɪz/",
        "vi": "Hy Lạp hóa; mô phỏng lối Hy Lạp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082655",
        "hw": "grecolatry",
        "pos": "noun",
        "ipa": "/ɡriːˈkɑː.lə.tri/",
        "vi": "sự sùng bái văn hóa Hy Lạp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082656",
        "hw": "greegree",
        "pos": "noun",
        "ipa": "/ˈɡriː.ɡriː/",
        "vi": "bùa hộ mệnh châu Phi; bùa may mắn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082657",
        "hw": "greenbottle",
        "pos": "noun",
        "ipa": "/ˈɡriːnˌbɑː.t̬əl/",
        "vi": "nhặng xanh; ruồi nhặng xanh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082658",
        "hw": "greened",
        "pos": "verb",
        "ipa": "/ɡriːnd/",
        "vi": "đã phủ xanh; đã làm cho xanh tươi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082659",
        "hw": "greener",
        "pos": "noun",
        "ipa": "/ˈɡriː.nɚ/",
        "vi": "người mới vào nghề; lính mới tò te",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082660",
        "hw": "greeneries",
        "pos": "noun",
        "ipa": "/ˈɡriː.nɚ.iz/",
        "vi": "những mảng cây xanh; thảm thực vật",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082661",
        "hw": "greeneye",
        "pos": "noun",
        "ipa": "/ˈɡriːn.aɪ/",
        "vi": "cá mắt lục biển sâu; cá mắt xanh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082662",
        "hw": "greenfinch",
        "pos": "noun",
        "ipa": "/ˈɡriːn.fɪntʃ/",
        "vi": "chim sẻ lục; chim sẻ ngô xanh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082663",
        "hw": "greenflies",
        "pos": "noun",
        "ipa": "/ˈɡriːn.flaɪz/",
        "vi": "những con rệp vừng xanh; rệp cây",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082664",
        "hw": "greengrocers",
        "pos": "noun",
        "ipa": "/ˈɡriːnˌɡroʊ.sɚz/",
        "vi": "những người bán rau quả tươi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082665",
        "hw": "greengrocery",
        "pos": "noun",
        "ipa": "/ˈɡriːnˌɡroʊ.sɚ.i/",
        "vi": "cửa hàng rau quả; rau củ tươi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082666",
        "hw": "greenhood",
        "pos": "noun",
        "ipa": "/ˈɡriːn.hʊd/",
        "vi": "lan mũ xanh Úc; lan đầu chim",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082667",
        "hw": "greenhorns",
        "pos": "noun",
        "ipa": "/ˈɡriːnˌhɔːrnz/",
        "vi": "những tay mơ; lính mới tò te",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082668",
        "hw": "greenhouses",
        "pos": "noun",
        "ipa": "/ˈɡriːnˌhaʊ.zɪz/",
        "vi": "các nhà kính trồng cây",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082669",
        "hw": "greenishness",
        "pos": "noun",
        "ipa": "/ˈɡriː.nɪʃ.nəs/",
        "vi": "sắc hơi lục; ánh xanh lá mờ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082670",
        "hw": "greenleaved",
        "pos": "adj",
        "ipa": "/ˈɡriːnˌliːvd/",
        "vi": "có lá xanh tươi; tán lá xanh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082671",
        "hw": "greenlight",
        "pos": "verb",
        "ipa": "/ˈɡriːn.laɪt/",
        "vi": "bật đèn xanh; phê chuẩn dự án",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082672",
        "hw": "greenling",
        "pos": "noun",
        "ipa": "/ˈɡriːn.lɪŋ/",
        "vi": "cá lục sáu vạch; cá lục bờ đá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082673",
        "hw": "greenlinnet",
        "pos": "noun",
        "ipa": "/ˈɡriːnˌlɪn.ɪt/",
        "vi": "chim sẻ lục châu Âu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082674",
        "hw": "greenockite",
        "pos": "noun",
        "ipa": "/ˈɡriː.nə.kaɪt/",
        "vi": "khoáng vật greenockit; quặng cadmi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082675",
        "hw": "greensick",
        "pos": "adj",
        "ipa": "/ˈɡriːn.sɪk/",
        "vi": "mắc chứng thiếu máu da xanh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082676",
        "hw": "greensickness",
        "pos": "noun",
        "ipa": "/ˈɡriːnˌsɪk.nəs/",
        "vi": "chứng thiếu máu xanh thiếu nữ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082677",
        "hw": "greenstone",
        "pos": "noun",
        "ipa": "/ˈɡriːn.stoʊn/",
        "vi": "đá phiến xanh; ngọc bích nephrit",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082678",
        "hw": "greenstuff",
        "pos": "noun",
        "ipa": "/ˈɡriːnˌstʌf/",
        "vi": "rau xanh các loại; cây cỏ xanh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082679",
        "hw": "greentech",
        "pos": "noun",
        "ipa": "/ˈɡriːn.tek/",
        "vi": "công nghệ xanh bảo vệ môi trường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082680",
        "hw": "greenwash",
        "pos": "noun",
        "ipa": "/ˈɡriːn.wɑːʃ/",
        "vi": "sự tẩy xanh môi trường giả tạo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082681",
        "hw": "greenweed",
        "pos": "noun",
        "ipa": "/ˈɡriːn.wiːd/",
        "vi": "cây kim tước nhuộm vàng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082682",
        "hw": "greenwing",
        "pos": "noun",
        "ipa": "/ˈɡriːn.wɪŋ/",
        "vi": "vịt mòng két cánh xanh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082683",
        "hw": "greeny",
        "pos": "adj",
        "ipa": "/ˈɡriː.ni/",
        "vi": "hơi ngả màu xanh lục; hơi xanh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082684",
        "hw": "greenyard",
        "pos": "noun",
        "ipa": "/ˈɡriːn.jɑːrd/",
        "vi": "bãi nhốt súc vật đi lạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082685",
        "hw": "greeted",
        "pos": "verb",
        "ipa": "/ˈɡriː.t̬ɪd/",
        "vi": "đã chào đón; đã đón tiếp niềm nở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082686",
        "hw": "greets",
        "pos": "verb",
        "ipa": "/ɡriːts/",
        "vi": "chào hỏi; đón tiếp; mở lời chào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082687",
        "hw": "gregarine",
        "pos": "noun",
        "ipa": "/ˈɡrɛɡ.ə.raɪn/",
        "vi": "trùng gregarin ký sinh ruột",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082688",
        "hw": "gregarinida",
        "pos": "noun",
        "ipa": "/ˌɡrɛɡ.əˈrɪn.ə.də/",
        "vi": "bộ trùng bào tử gregarin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082689",
        "hw": "grege",
        "pos": "noun",
        "ipa": "/ɡreɪʒ/",
        "vi": "tơ sống chưa tẩy; màu be xám",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082690",
        "hw": "grew",
        "pos": "verb",
        "ipa": "/ɡruː/",
        "vi": "đã lớn lên; đã phát triển; đã mọc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082691",
        "hw": "grewsome",
        "pos": "adj",
        "ipa": "/ˈɡruː.səm/",
        "vi": "ghê rợn; kinh khủng; rùng rợn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082692",
        "hw": "greycing",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.sɪŋ/",
        "vi": "cuộc săn đuổi bằng chó săn thỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082693",
        "hw": "greyhen",
        "pos": "noun",
        "ipa": "/ˈɡreɪ.hɛn/",
        "vi": "gà gô đen mái; gà rừng xám mái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082694",
        "hw": "greyly",
        "pos": "adv",
        "ipa": "/ˈɡreɪ.li/",
        "vi": "một cách ảm đạm; xám xịt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082695",
        "hw": "grias",
        "pos": "noun",
        "ipa": "/ˈɡraɪ.əs/",
        "vi": "chi cây lê cơm cháy; cây grias",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082696",
        "hw": "gridder",
        "pos": "noun",
        "ipa": "/ˈɡrɪd.ɚ/",
        "vi": "cầu thủ bóng bầu dục Mỹ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082697",
        "hw": "griddlecake",
        "pos": "noun",
        "ipa": "/ˈɡrɪd.əl.keɪk/",
        "vi": "bánh kếp nướng chảo; bánh rán vỉ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082698",
        "hw": "gride",
        "pos": "noun",
        "ipa": "/ɡraɪd/",
        "vi": "tiếng ken két sắt đá; tiếng cọ xát",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082699",
        "hw": "griefless",
        "pos": "adj",
        "ipa": "/ˈɡriːf.ləs/",
        "vi": "không đau khổ; không phiền muộn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082700",
        "hw": "griest",
        "pos": "noun",
        "ipa": "/ɡriːst/",
        "vi": "mẻ thóc xay bột; ngũ cốc nghiền",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082701",
        "hw": "grieved",
        "pos": "verb",
        "ipa": "/ɡriːvd/",
        "vi": "đã đau buồn; đã thương xót vô hạn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

# Validation
with open("scratch/b17_r06_raw_p2.json") as f:
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

print("All 100 records in Part 2 verified successfully!")
