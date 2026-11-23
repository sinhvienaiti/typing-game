import json

reviewed_records = [
    {
        "id": "lex.en.100k.082902",
        "hw": "guddle",
        "pos": "verb",
        "ipa": "/ˈɡʌd.əl/",
        "vi": "bắt cá bằng tay; làm lộn xộn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082903",
        "hw": "guelma",
        "pos": "noun",
        "ipa": "/ɡwɛlˈmɑː/",
        "vi": "thành phố Guelma ở Algérie",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082904",
        "hw": "guereza",
        "pos": "noun",
        "ipa": "/ɡwəˈreɪ.zə/",
        "vi": "khỉ colobus guereza đen trắng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082905",
        "hw": "gueridon",
        "pos": "noun",
        "ipa": "/ˌɡɛr.ɪˈdɑːn/",
        "vi": "bàn tròn nhỏ ba chân; xe phục vụ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082906",
        "hw": "guessed",
        "pos": "verb",
        "ipa": "/ɡɛst/",
        "vi": "đã phỏng đoán; đã đoán chừng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082907",
        "hw": "guesses",
        "pos": "verb",
        "ipa": "/ˈɡɛs.ɪz/",
        "vi": "phỏng đoán; đoán chừng; ước lượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082908",
        "hw": "guesthouses",
        "pos": "noun",
        "ipa": "/ˈɡɛstˌhaʊ.zɪz/",
        "vi": "các nhà khách; các nhà trọ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082909",
        "hw": "guestship",
        "pos": "noun",
        "ipa": "/ˈɡɛst.ʃɪp/",
        "vi": "tư cách người khách; vị thế khách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082910",
        "hw": "guestwise",
        "pos": "adv",
        "ipa": "/ˈɡɛst.waɪz/",
        "vi": "như một vị khách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082911",
        "hw": "guestworker",
        "pos": "noun",
        "ipa": "/ˈɡɛstˌwɜːr.kɚ/",
        "vi": "lao động nhập cư tạm thời",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082912",
        "hw": "guevina",
        "pos": "noun",
        "ipa": "/ɡwəˈviː.nə/",
        "vi": "cây phỉ Chile; chi cây guevina",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082913",
        "hw": "gug",
        "pos": "noun",
        "ipa": "/ɡʌɡ/",
        "vi": "đường dốc tời quặng mỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082914",
        "hw": "guggle",
        "pos": "verb",
        "ipa": "/ˈɡʌɡ.əl/",
        "vi": "chảy ọc ọc; sôi ùng ục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082915",
        "hw": "guib",
        "pos": "noun",
        "ipa": "/ɡiːb/",
        "vi": "linh dương guib châu Phi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082916",
        "hw": "guichet",
        "pos": "noun",
        "ipa": "/ɡiːˈʃeɪ/",
        "vi": "ô cửa bán vé; quầy giao dịch nhỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082917",
        "hw": "guidable",
        "pos": "adj",
        "ipa": "/ˈɡaɪ.də.bəl/",
        "vi": "có thể dẫn đường; dễ định hướng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082918",
        "hw": "guidances",
        "pos": "noun",
        "ipa": "/ˈɡaɪ.dəns.ɪz/",
        "vi": "các văn bản hướng dẫn; sự chỉ dẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082919",
        "hw": "guideless",
        "pos": "adj",
        "ipa": "/ˈɡaɪd.ləs/",
        "vi": "không có người dẫn đường; bơ vơ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082920",
        "hw": "guidelines",
        "pos": "noun",
        "ipa": "/ˈɡaɪdˌlaɪnz/",
        "vi": "các đường lối chỉ đạo; hướng dẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082921",
        "hw": "guideposts",
        "pos": "noun",
        "ipa": "/ˈɡaɪdˌpoʊsts/",
        "vi": "các cột chỉ đường; kim chỉ nam",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082922",
        "hw": "guider",
        "pos": "noun",
        "ipa": "/ˈɡaɪ.dɚ/",
        "vi": "người hướng dẫn; thanh định hướng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082923",
        "hw": "guides",
        "pos": "verb",
        "ipa": "/ɡaɪdz/",
        "vi": "hướng dẫn; dẫn đường; định hướng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082924",
        "hw": "guideway",
        "pos": "noun",
        "ipa": "/ˈɡaɪdˌweɪ/",
        "vi": "đường ray dẫn hướng; rãnh dẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082925",
        "hw": "guideword",
        "pos": "noun",
        "ipa": "/ˈɡaɪdˌwɜːrd/",
        "vi": "từ chỉ mục đầu trang từ điển",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082926",
        "hw": "guidon",
        "pos": "noun",
        "ipa": "/ˈɡaɪ.dən/",
        "vi": "cờ hiệu kỵ binh; cờ tiểu đội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082927",
        "hw": "guidwillie",
        "pos": "adj",
        "ipa": "/ɡɪdˈwɪl.i/",
        "vi": "nồng hậu; hiếu khách; thân tình",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082928",
        "hw": "guildsman",
        "pos": "noun",
        "ipa": "/ˈɡɪldz.mən/",
        "vi": "thành viên bang hội; thợ hội quán",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082929",
        "hw": "guilefully",
        "pos": "adv",
        "ipa": "/ˈɡaɪl.fəl.i/",
        "vi": "một cách quỷ quyệt; xảo quyệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082930",
        "hw": "guilefulness",
        "pos": "noun",
        "ipa": "/ˈɡaɪl.fəl.nəs/",
        "vi": "tính gian trá; sự xảo quyệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082931",
        "hw": "guilelessly",
        "pos": "adv",
        "ipa": "/ˈɡaɪl.ləs.li/",
        "vi": "thật thà chất phác; ngây thơ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082932",
        "hw": "guilelessness",
        "pos": "noun",
        "ipa": "/ˈɡaɪl.ləs.nəs/",
        "vi": "tính chất phác; lòng chân thật",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082933",
        "hw": "guilery",
        "pos": "noun",
        "ipa": "/ˈɡaɪ.lɚ.i/",
        "vi": "trò lừa dối; hành vi quỷ quyệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082934",
        "hw": "guillemet",
        "pos": "noun",
        "ipa": "/ˌɡiː.əˈmeɪ/",
        "vi": "dấu ngoặc kép kiểu Pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082935",
        "hw": "guillemets",
        "pos": "noun",
        "ipa": "/ˌɡiː.əˈmeɪz/",
        "vi": "các dấu ngoặc kép kiểu Pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082936",
        "hw": "guillemots",
        "pos": "noun",
        "ipa": "/ˈɡɪl.ə.mɑːts/",
        "vi": "những con chim uria; chim cưu biển",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082937",
        "hw": "guillotined",
        "pos": "verb",
        "ipa": "/ˈɡɪl.ə.tiːnd/",
        "vi": "đã xử trảm bằng máy chém; xén giấy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082938",
        "hw": "guillotines",
        "pos": "verb",
        "ipa": "/ˈɡɪl.ə.tiːnz/",
        "vi": "chém đầu bằng máy chém; cắt xén",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082939",
        "hw": "guillotining",
        "pos": "verb",
        "ipa": "/ˈɡɪl.ə.tiː.nɪŋ/",
        "vi": "đang chém đầu; cắt xén bằng máy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082940",
        "hw": "guilotine",
        "pos": "noun",
        "ipa": "/ˈɡɪl.ə.tiːn/",
        "vi": "máy chém; máy xén tài liệu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082941",
        "hw": "guiltlessly",
        "pos": "adv",
        "ipa": "/ˈɡɪlt.ləs.li/",
        "vi": "vô tội; một cách trong sạch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082942",
        "hw": "guiltlessness",
        "pos": "noun",
        "ipa": "/ˈɡɪlt.ləs.nəs/",
        "vi": "sự vô tội; tính vô can trong sạch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082943",
        "hw": "guimpe",
        "pos": "noun",
        "ipa": "/ɡæmp/",
        "vi": "áo lót cổ cao; khăn trùm đầu nữ tu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082944",
        "hw": "guitarfish",
        "pos": "noun",
        "ipa": "/ɡɪˈtɑːr.fɪʃ/",
        "vi": "cá giống; cá đuối guitar",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082945",
        "hw": "gujerat",
        "pos": "noun",
        "ipa": "/ˌɡʊdʒ.əˈrɑːt/",
        "vi": "bang Gujarat của Ấn Độ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082946",
        "hw": "gujerati",
        "pos": "noun",
        "ipa": "/ˌɡʊdʒ.əˈrɑː.ti/",
        "vi": "tiếng Gujarati; người dân Gujarat",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082947",
        "hw": "gular",
        "pos": "adj",
        "ipa": "/ˈɡjuː.lɚ/",
        "vi": "thuộc yết hầu; thuộc vùng cổ họng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082948",
        "hw": "gules",
        "pos": "adj",
        "ipa": "/ɡjuːlz/",
        "vi": "màu đỏ tươi huy hiệu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082949",
        "hw": "gulfweed",
        "pos": "noun",
        "ipa": "/ˈɡʌlf.wiːd/",
        "vi": "rong mơ; rong biển sargassum",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082950",
        "hw": "gulfy",
        "pos": "adj",
        "ipa": "/ˈɡʌl.fi/",
        "vi": "nhiều xoáy nước; sâu thẳm hiểm trở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082951",
        "hw": "guller",
        "pos": "noun",
        "ipa": "/ˈɡʌl.ɚ/",
        "vi": "kẻ lừa gạt; kẻ lừa đảo bịp bợm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082952",
        "hw": "gulleries",
        "pos": "noun",
        "ipa": "/ˈɡʌl.ɚ.iz/",
        "vi": "nơi mòng biển đẻ; các trò lừa bịp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082953",
        "hw": "gullery",
        "pos": "noun",
        "ipa": "/ˈɡʌl.ɚ.i/",
        "vi": "trò lừa gạt; nơi chim mòng biển đẻ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082954",
        "hw": "gullibly",
        "pos": "adv",
        "ipa": "/ˈɡʌl.ə.bli/",
        "vi": "một cách khờ dại; cả tin ngây thơ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082955",
        "hw": "gulls",
        "pos": "noun",
        "ipa": "/ɡʌlz/",
        "vi": "chim mòng biển; những kẻ cả tin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082956",
        "hw": "gulosity",
        "pos": "noun",
        "ipa": "/ɡjuːˈlɑː.sə.ti/",
        "vi": "thói phàm ăn; tật háu ăn tham uống",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082957",
        "hw": "gulped",
        "pos": "verb",
        "ipa": "/ɡʌlpt/",
        "vi": "đã nuốt ực; đã hớp vội vàng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082958",
        "hw": "gulpingly",
        "pos": "adv",
        "ipa": "/ˈɡʌl.pɪŋ.li/",
        "vi": "nuốt ừng ực; hổn hển nuốt nghẹn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082959",
        "hw": "gulps",
        "pos": "verb",
        "ipa": "/ɡʌlps/",
        "vi": "nuốt chửng; nuốt ực; hớp từng ngụm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082960",
        "hw": "gumboil",
        "pos": "noun",
        "ipa": "/ˈɡʌmˌbɔɪl/",
        "vi": "áp-xe chân răng; mụn nhọt ở nướu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082961",
        "hw": "gumboot",
        "pos": "noun",
        "ipa": "/ˈɡʌm.buːt/",
        "vi": "ủng cao su chống nước; ủng đi mưa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082962",
        "hw": "gumby",
        "pos": "noun",
        "ipa": "/ˈɡʌm.bi/",
        "vi": "trống goombay châu Phi; gõ găm-bi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082963",
        "hw": "gummer",
        "pos": "noun",
        "ipa": "/ˈɡʌm.ɚ/",
        "vi": "người móm; máy bấm răng cưa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082964",
        "hw": "gummiferous",
        "pos": "adj",
        "ipa": "/ɡʌˈmɪf.ɚ.əs/",
        "vi": "tiết ra gôm; sinh chất nhựa dẻo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082965",
        "hw": "gumminess",
        "pos": "noun",
        "ipa": "/ˈɡʌm.i.nəs/",
        "vi": "độ dính bết; tính kết dính như gôm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082966",
        "hw": "gummite",
        "pos": "noun",
        "ipa": "/ˈɡʌm.aɪt/",
        "vi": "khoáng vật gummit; quặng urani",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082967",
        "hw": "gummosis",
        "pos": "noun",
        "ipa": "/ɡʌˈmoʊ.sɪs/",
        "vi": "bệnh chảy mủ gôm ở cây thân gỗ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082968",
        "hw": "gumptious",
        "pos": "adj",
        "ipa": "/ˈɡʌmp.ʃəs/",
        "vi": "tháo vát; khôn ngoan mưu trí",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082969",
        "hw": "gums",
        "pos": "verb",
        "ipa": "/ɡʌmz/",
        "vi": "dán bằng keo gôm; nhai bằng nướu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082970",
        "hw": "gumshield",
        "pos": "noun",
        "ipa": "/ˈɡʌm.ʃiːld/",
        "vi": "miếng bảo vệ hàm; máng ngậm răng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082971",
        "hw": "gumweed",
        "pos": "noun",
        "ipa": "/ˈɡʌm.wiːd/",
        "vi": "cây cúc nhựa; thảo dược gumweed",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082972",
        "hw": "gumwood",
        "pos": "noun",
        "ipa": "/ˈɡʌm.wʊd/",
        "vi": "gỗ cây bạch đàn; gỗ cây nhựa gôm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082973",
        "hw": "gunfighter",
        "pos": "noun",
        "ipa": "/ˈɡʌnˌfaɪ.t̬ɚ/",
        "vi": "tay súng miền Tây; kẻ bắn súng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082974",
        "hw": "gunge",
        "pos": "noun",
        "ipa": "/ɡʌndʒ/",
        "vi": "chất nhầy nhụa; chất sền sệt bẩn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082975",
        "hw": "gungho",
        "pos": "adj",
        "ipa": "/ˌɡʌŋˈhoʊ/",
        "vi": "hăng say nhiệt tình; sốt sắng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082976",
        "hw": "gungy",
        "pos": "adj",
        "ipa": "/ˈɡʌn.dʒi/",
        "vi": "nhầy nhụa dính nhớp; bẩn thỉu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082977",
        "hw": "gunlock",
        "pos": "noun",
        "ipa": "/ˈɡʌn.lɑːk/",
        "vi": "khóa nòng súng; bộ điểm hỏa súng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082978",
        "hw": "gunmen",
        "pos": "noun",
        "ipa": "/ˈɡʌn.mən/",
        "vi": "những tay súng; toán cướp có súng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082979",
        "hw": "gunned",
        "pos": "verb",
        "ipa": "/ɡʌnd/",
        "vi": "đã rồ ga phóng nhanh; đã bắn súng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082980",
        "hw": "gunneries",
        "pos": "noun",
        "ipa": "/ˈɡʌn.ɚ.iz/",
        "vi": "ngành pháo binh; thuật bắn pháo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082981",
        "hw": "gunners",
        "pos": "noun",
        "ipa": "/ˈɡʌn.ɚz/",
        "vi": "các pháo thủ; những tay súng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082982",
        "hw": "gunning",
        "pos": "verb",
        "ipa": "/ˈɡʌn.ɪŋ/",
        "vi": "đang rồ ga xe; săn bắn; tìm diệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082983",
        "hw": "gunnysack",
        "pos": "noun",
        "ipa": "/ˈɡʌn.iˌsæk/",
        "vi": "bao tải gai; bao bố thô dệt đay",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082984",
        "hw": "gunpowders",
        "pos": "noun",
        "ipa": "/ˈɡʌnˌpaʊ.dɚz/",
        "vi": "các loại thuốc súng nổ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082985",
        "hw": "gunroom",
        "pos": "noun",
        "ipa": "/ˈɡʌn.ruːm/",
        "vi": "phòng chứa súng; phòng sĩ quan trẻ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082986",
        "hw": "guns",
        "pos": "verb",
        "ipa": "/ɡʌnz/",
        "vi": "nhấn ga rồ máy; bắn súng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082987",
        "hw": "gunshots",
        "pos": "noun",
        "ipa": "/ˈɡʌn.ʃɑːts/",
        "vi": "những tiếng súng nổ; phát đạn bắn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082988",
        "hw": "gunstick",
        "pos": "noun",
        "ipa": "/ˈɡʌn.stɪk/",
        "vi": "cây thông nòng súng; que nhồi đạn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082989",
        "hw": "gunzeled",
        "pos": "verb",
        "ipa": "/ˈɡʌn.zəld/",
        "vi": "đã say mê xe lửa; đã làm tay sai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082990",
        "hw": "guorthegein",
        "pos": "noun",
        "ipa": "/ˌvɔːr.tɪˈɡɜːrn/",
        "vi": "vua Vortigern trong huyền sử Anh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082991",
        "hw": "guqin",
        "pos": "noun",
        "ipa": "/ɡuːˈtʃiːn/",
        "vi": "đàn cổ cầm bảy dây của Trung Quốc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082992",
        "hw": "gurgitation",
        "pos": "noun",
        "ipa": "/ˌɡɜːr.dʒɪˈteɪ.ʃən/",
        "vi": "sự sôi sùng sục; chuyển động ọc ọc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082993",
        "hw": "gurgled",
        "pos": "verb",
        "ipa": "/ˈɡɜːr.ɡəld/",
        "vi": "đã chảy ọc ọc; đã róc rách reo vui",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082994",
        "hw": "gurgles",
        "pos": "verb",
        "ipa": "/ˈɡɜːr.ɡəlz/",
        "vi": "chảy róc rách; kêu ọc ọc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082995",
        "hw": "gurgling",
        "pos": "verb",
        "ipa": "/ˈɡɜːr.ɡəl.ɪŋ/",
        "vi": "đang chảy ọc ọc; róc rách róc rách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082996",
        "hw": "gurglingly",
        "pos": "adv",
        "ipa": "/ˈɡɜːr.ɡəl.ɪŋ.li/",
        "vi": "róc rách ọc ọc; một cách vui sướng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082997",
        "hw": "gurnet",
        "pos": "noun",
        "ipa": "/ˈɡɜːr.nɪt/",
        "vi": "cá chào mào biển; cá thiết giáp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082998",
        "hw": "gushed",
        "pos": "verb",
        "ipa": "/ɡʌʃt/",
        "vi": "đã phun trào mạnh; đã khen nức nở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082999",
        "hw": "gushes",
        "pos": "verb",
        "ipa": "/ˈɡʌʃ.ɪz/",
        "vi": "phun trào ào ạt; khen lấy khen để",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083000",
        "hw": "gushily",
        "pos": "adv",
        "ipa": "/ˈɡʌʃ.əl.i/",
        "vi": "vồn vã thái quá; nức nở sướt mướt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.083001",
        "hw": "gushiness",
        "pos": "noun",
        "ipa": "/ˈɡʌʃ.i.nəs/",
        "vi": "sự vồn vã quá mức; thói sướt mướt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

# Validation
with open("scratch/b17_r06_raw_p5.json") as f:
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
