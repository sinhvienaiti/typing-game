import json

reviewed_records = [
    {
        "id": "lex.en.100k.082802",
        "hw": "groundberry",
        "pos": "noun",
        "ipa": "/ˈɡraʊndˌbɛr.i/",
        "vi": "cây mộc mai lùn; quả mọng mọc bò",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082803",
        "hw": "grounded",
        "pos": "adj",
        "ipa": "/ˈɡraʊn.dɪd/",
        "vi": "nối đất; thực tế; bị cấm bay",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082804",
        "hw": "groundedly",
        "pos": "adv",
        "ipa": "/ˈɡraʊn.dɪd.li/",
        "vi": "có cơ sở vững chắc; chắc chắn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082805",
        "hw": "groundkeeper",
        "pos": "noun",
        "ipa": "/ˈɡraʊndˌkiː.pɚ/",
        "vi": "người chăm sóc sân cỏ; coi sân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082806",
        "hw": "groundlessly",
        "pos": "adv",
        "ipa": "/ˈɡraʊnd.ləs.li/",
        "vi": "một cách vô căn cứ; vô cớ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082807",
        "hw": "groundlessness",
        "pos": "noun",
        "ipa": "/ˈɡraʊnd.ləs.nəs/",
        "vi": "sự vô căn cứ; tính không cơ sở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082808",
        "hw": "groundlings",
        "pos": "noun",
        "ipa": "/ˈɡraʊnd.lɪŋz/",
        "vi": "khán giả bình dân; các loài cá đáy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082809",
        "hw": "groundloop",
        "pos": "noun",
        "ipa": "/ˈɡraʊndˌluːp/",
        "vi": "sự xoay ngoặt máy bay trên bộ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082810",
        "hw": "groundoak",
        "pos": "noun",
        "ipa": "/ˈɡraʊndˌoʊk/",
        "vi": "cây sồi lùn; cây thảo dâm bụt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082811",
        "hw": "groundsels",
        "pos": "noun",
        "ipa": "/ˈɡraʊnd.səlz/",
        "vi": "các cây cúc cối bồng; hoa senecio",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082812",
        "hw": "groundsheets",
        "pos": "noun",
        "ipa": "/ˈɡraʊndˌʃiːts/",
        "vi": "những tấm bạt lót lều cắm trại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082813",
        "hw": "groundsmen",
        "pos": "noun",
        "ipa": "/ˈɡraʊndz.mən/",
        "vi": "những người chăm sóc sân cỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082814",
        "hw": "groundworks",
        "pos": "noun",
        "ipa": "/ˈɡraʊnd.wɜːrks/",
        "vi": "các công việc nền tảng; cơ sở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082815",
        "hw": "groupment",
        "pos": "noun",
        "ipa": "/ˈɡruːp.mənt/",
        "vi": "sự tập hợp nhóm; đoàn thể",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082816",
        "hw": "groupoid",
        "pos": "noun",
        "ipa": "/ˈɡruː.pɔɪd/",
        "vi": "phỏng nhóm; cấu trúc groupoid",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082817",
        "hw": "groups",
        "pos": "verb",
        "ipa": "/ɡruːps/",
        "vi": "tập hợp thành nhóm; phân nhóm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082818",
        "hw": "grouseberry",
        "pos": "noun",
        "ipa": "/ˈɡraʊsˌbɛr.i/",
        "vi": "quả việt quất gà gô; cây nham lê",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082819",
        "hw": "groused",
        "pos": "verb",
        "ipa": "/ɡraʊst/",
        "vi": "đã càu nhàu; đã phàn nàn ca cẩm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082820",
        "hw": "grouser",
        "pos": "noun",
        "ipa": "/ˈɡraʊ.zɚ/",
        "vi": "kẻ hay càu nhàu; vấu xích bánh xe",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082821",
        "hw": "grouses",
        "pos": "noun",
        "ipa": "/ˈɡraʊ.sɪz/",
        "vi": "các con gà gô; những lời cằn nhằn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082822",
        "hw": "grousing",
        "pos": "verb",
        "ipa": "/ˈɡraʊ.zɪŋ/",
        "vi": "đang càu nhàu; cằn nhằn ca cẩm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082823",
        "hw": "grouted",
        "pos": "verb",
        "ipa": "/ˈɡraʊ.t̬ɪd/",
        "vi": "đã trát vữa xi măng; đã chà ron",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082824",
        "hw": "grouter",
        "pos": "noun",
        "ipa": "/ˈɡraʊ.t̬ɚ/",
        "vi": "máy bơm vữa; dụng cụ trát vữa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082825",
        "hw": "grouting",
        "pos": "verb",
        "ipa": "/ˈɡraʊ.t̬ɪŋ/",
        "vi": "đang trát vữa; bơm vữa chèn khe",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082826",
        "hw": "grouts",
        "pos": "verb",
        "ipa": "/ɡraʊts/",
        "vi": "trát vữa xi măng; chà ron gạch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082827",
        "hw": "grouty",
        "pos": "adj",
        "ipa": "/ˈɡraʊ.ti/",
        "vi": "cáu kỉnh; gắt gỏng; cặn bã",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082828",
        "hw": "groveler",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.və.lɚ/",
        "vi": "kẻ luồn cúi; người khúm núm bợ đỡ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082829",
        "hw": "grovelingly",
        "pos": "adv",
        "ipa": "/ˈɡrɑː.və.lɪŋ.li/",
        "vi": "quỵ lụy; khúm núm luồn cúi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082830",
        "hw": "grovelled",
        "pos": "verb",
        "ipa": "/ˈɡrɑː.vəld/",
        "vi": "đã phủ phục; đã quỵ lụy van xin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082831",
        "hw": "groveller",
        "pos": "noun",
        "ipa": "/ˈɡrɑː.və.lɚ/",
        "vi": "kẻ luồn cúi; người hạ mình van xin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082832",
        "hw": "grovels",
        "pos": "verb",
        "ipa": "/ˈɡrɑː.vəlz/",
        "vi": "phủ phục; khúm núm; luồn cúi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082833",
        "hw": "growingly",
        "pos": "adv",
        "ipa": "/ˈɡroʊ.ɪŋ.li/",
        "vi": "ngày càng tăng; ngày một rõ nét",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082834",
        "hw": "growled",
        "pos": "verb",
        "ipa": "/ɡraʊld/",
        "vi": "đã gầm gừ; đã càu nhàu giận dữ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082835",
        "hw": "growlers",
        "pos": "noun",
        "ipa": "/ˈɡraʊ.lɚz/",
        "vi": "tảng băng trôi nhỏ; bình bia lớn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082836",
        "hw": "growls",
        "pos": "verb",
        "ipa": "/ɡraʊlz/",
        "vi": "gầm gừ; càu nhàu; rền vang",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082837",
        "hw": "growly",
        "pos": "adj",
        "ipa": "/ˈɡraʊ.li/",
        "vi": "gầm gừ; ồm ồm gắt gỏng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082838",
        "hw": "growths",
        "pos": "noun",
        "ipa": "/ɡroʊθs/",
        "vi": "các khối u; các mức tăng trưởng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082839",
        "hw": "groyned",
        "pos": "adj",
        "ipa": "/ɡrɔɪnd/",
        "vi": "được gia cố bờ kè chắn sóng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082840",
        "hw": "groznyy",
        "pos": "noun",
        "ipa": "/ˈɡrɑːz.ni/",
        "vi": "thành phố Grozny của Chechnya",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082841",
        "hw": "grubbed",
        "pos": "verb",
        "ipa": "/ɡrʌbd/",
        "vi": "đã đào bới; đã nhổ rễ cây",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082842",
        "hw": "grubber",
        "pos": "noun",
        "ipa": "/ˈɡrʌb.ɚ/",
        "vi": "dụng cụ nhổ cỏ; cú đá bóng lăn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082843",
        "hw": "grubbily",
        "pos": "adv",
        "ipa": "/ˈɡrʌb.əl.i/",
        "vi": "một cách bẩn thỉu; lếch thếch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082844",
        "hw": "grubbiness",
        "pos": "noun",
        "ipa": "/ˈɡrʌb.i.nəs/",
        "vi": "tình trạng bẩn thỉu; sự lếch thếch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082845",
        "hw": "grubbing",
        "pos": "verb",
        "ipa": "/ˈɡrʌb.ɪŋ/",
        "vi": "đang đào bới; bứng rễ; tìm tòi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082846",
        "hw": "grubs",
        "pos": "verb",
        "ipa": "/ɡrʌbz/",
        "vi": "đào bới; nhổ rễ cây; lùng sục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082847",
        "hw": "grudged",
        "pos": "verb",
        "ipa": "/ɡrʌdʒd/",
        "vi": "đã ghen ghét; đã tiếc rẻ miệt thị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082848",
        "hw": "grudger",
        "pos": "noun",
        "ipa": "/ˈɡrʌdʒ.ɚ/",
        "vi": "người hay hậm hực; kẻ ganh tị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082849",
        "hw": "grudges",
        "pos": "verb",
        "ipa": "/ˈɡrʌdʒ.ɪz/",
        "vi": "hậm hực; ghen tị; tiếc rẻ cho đi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082850",
        "hw": "grue",
        "pos": "verb",
        "ipa": "/ɡruː/",
        "vi": "rùng mình run sợ; ớn lạnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082851",
        "hw": "gruffish",
        "pos": "adj",
        "ipa": "/ˈɡrʌf.ɪʃ/",
        "vi": "hơi cộc lốc; hơi thô lỗ gắt gỏng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082852",
        "hw": "gruffy",
        "pos": "adj",
        "ipa": "/ˈɡrʌf.i/",
        "vi": "thô kệch; cộc cằn khàn khàn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082853",
        "hw": "grugru",
        "pos": "noun",
        "ipa": "/ˈɡruː.ɡruː/",
        "vi": "cây cọ grugru; nhộng cọ nhiệt đới",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082854",
        "hw": "gruidae",
        "pos": "noun",
        "ipa": "/ˈɡruː.ɪˌdiː/",
        "vi": "họ sếu; họ chim sếu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082855",
        "hw": "gruiformes",
        "pos": "noun",
        "ipa": "/ɡruːˈɪ.fɔːr.miːz/",
        "vi": "bộ sếu; bộ chim sếu và gà nước",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082856",
        "hw": "grumbled",
        "pos": "verb",
        "ipa": "/ˈɡrʌm.bəld/",
        "vi": "đã lầm bầm; đã càu nhàu bất mãn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082857",
        "hw": "grumbles",
        "pos": "verb",
        "ipa": "/ˈɡrʌm.bəlz/",
        "vi": "lầm bầm phàn nàn; càu nhàu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082858",
        "hw": "grumblingly",
        "pos": "adv",
        "ipa": "/ˈɡrʌm.bəl.ɪŋ.li/",
        "vi": "càu nhàu gắt gỏng; lầm bầm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082859",
        "hw": "grumbly",
        "pos": "adj",
        "ipa": "/ˈɡrʌm.bli/",
        "vi": "hay càu nhàu; sôi bụng ùng ục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082860",
        "hw": "grume",
        "pos": "noun",
        "ipa": "/ɡruːm/",
        "vi": "cục máu đông; chất lỏng sệt quánh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082861",
        "hw": "grummet",
        "pos": "noun",
        "ipa": "/ˈɡrʌm.ɪt/",
        "vi": "vòng đệm dây; khoen kim loại xỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082862",
        "hw": "grumose",
        "pos": "adj",
        "ipa": "/ˈɡruː.moʊs/",
        "vi": "vón thành hạt; đông tụ dạng hạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082863",
        "hw": "grumous",
        "pos": "adj",
        "ipa": "/ˈɡruː.məs/",
        "vi": "vón cục; đông quánh đặc sệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082864",
        "hw": "grumpish",
        "pos": "adj",
        "ipa": "/ˈɡrʌm.pɪʃ/",
        "vi": "hay cáu bẳn; khó tính cộc cằn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082865",
        "hw": "grundyism",
        "pos": "noun",
        "ipa": "/ˈɡrʌn.diˌɪz.əm/",
        "vi": "tính câu nệ đạo đức; đạo đức giả",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082866",
        "hw": "grungily",
        "pos": "adv",
        "ipa": "/ˈɡrʌn.dʒəl.i/",
        "vi": "nhếch nhác; bẩn thỉu lùi xùi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082867",
        "hw": "grunted",
        "pos": "verb",
        "ipa": "/ˈɡrʌn.t̬ɪd/",
        "vi": "đã càu nhàu; đã phát tiếng ủn ỉn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082868",
        "hw": "grunting",
        "pos": "verb",
        "ipa": "/ˈɡrʌn.t̬ɪŋ/",
        "vi": "đang càu nhàu; rên rỉ ủn ỉn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082869",
        "hw": "gruntingly",
        "pos": "adv",
        "ipa": "/ˈɡrʌn.t̬ɪŋ.li/",
        "vi": "với tiếng ủn ỉn; càu nhàu gắt gỏng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082870",
        "hw": "gruntle",
        "pos": "verb",
        "ipa": "/ˈɡrʌn.təl/",
        "vi": "làm hài lòng; dỗ dành êm dịu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082871",
        "hw": "gruntled",
        "pos": "adj",
        "ipa": "/ˈɡrʌn.təld/",
        "vi": "vui lòng; thỏa mãn hài lòng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082872",
        "hw": "gruntling",
        "pos": "noun",
        "ipa": "/ˈɡrʌnt.lɪŋ/",
        "vi": "lợn con; chú heo sữa nhỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082873",
        "hw": "grunts",
        "pos": "verb",
        "ipa": "/ɡrʌnts/",
        "vi": "càu nhàu gầm gừ; kêu ủn ỉn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082874",
        "hw": "gryllidae",
        "pos": "noun",
        "ipa": "/ˈɡrɪl.ə.diː/",
        "vi": "họ dế mèn; họ dế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082875",
        "hw": "grysbok",
        "pos": "noun",
        "ipa": "/ˈɡreɪs.bɑːk/",
        "vi": "linh dương xám châu Phi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082876",
        "hw": "gt",
        "pos": "noun",
        "ipa": "/ˌdʒiːˈtiː/",
        "vi": "dòng xe thể thao đường trường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082877",
        "hw": "guacharo",
        "pos": "noun",
        "ipa": "/ˈɡwɑː.tʃə.roʊ/",
        "vi": "chim dầu Nam Mỹ; chim béo hang",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082878",
        "hw": "guaco",
        "pos": "noun",
        "ipa": "/ˈɡwɑː.koʊ/",
        "vi": "cây dây leo trị rắn cắn guaco",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082879",
        "hw": "guallatiri",
        "pos": "noun",
        "ipa": "/ɡwaɪ.əˈtɪr.i/",
        "vi": "núi lửa Guallatiri ở Chile",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082880",
        "hw": "guama",
        "pos": "noun",
        "ipa": "/ˈɡwɑː.mə/",
        "vi": "cây guama; cây đậu kem nhiệt đới",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082881",
        "hw": "guana",
        "pos": "noun",
        "ipa": "/ˈɡwɑː.nə/",
        "vi": "phân chim làm phân bón; kỳ nhông",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082882",
        "hw": "guanabana",
        "pos": "noun",
        "ipa": "/ɡwɑːˈnɑː.bə.nə/",
        "vi": "quả mãng cầu xiêm; quả na gai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082883",
        "hw": "guanabenz",
        "pos": "noun",
        "ipa": "/ˈɡwɑː.nə.bɛnz/",
        "vi": "thuốc hạ huyết áp guanabenz",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082884",
        "hw": "guanidine",
        "pos": "noun",
        "ipa": "/ˈɡwɑː.nəˌdiːn/",
        "vi": "hợp chất hữu cơ guanidin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082885",
        "hw": "guaniferous",
        "pos": "adj",
        "ipa": "/ˌɡwɑːˈnɪf.ɚ.əs/",
        "vi": "chứa phân chim; sinh phân guano",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082886",
        "hw": "guanophore",
        "pos": "noun",
        "ipa": "/ˈɡwɑː.noʊ.fɔːr/",
        "vi": "tế bào sắc tố ánh bạc guanin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082887",
        "hw": "guaranteed",
        "pos": "verb",
        "ipa": "/ˌɡɛr.ənˈtiːd/",
        "vi": "đã bảo đảm; đã cam đoan chắc chắn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082888",
        "hw": "guaranteeing",
        "pos": "verb",
        "ipa": "/ˌɡɛr.ənˈtiː.ɪŋ/",
        "vi": "đang cam kết; bảo đảm chất lượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082889",
        "hw": "guarantees",
        "pos": "verb",
        "ipa": "/ˌɡɛr.ənˈtiːz/",
        "vi": "bảo đảm; cam kết chắc chắn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082890",
        "hw": "guarapo",
        "pos": "noun",
        "ipa": "/ɡwɑːˈrɑː.poʊ/",
        "vi": "nước mía ép; rượu mía lên men",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082891",
        "hw": "guardedness",
        "pos": "noun",
        "ipa": "/ˈɡɑːr.dɪd.nəs/",
        "vi": "sự thận trọng; thái độ dè chừng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082892",
        "hw": "guarder",
        "pos": "noun",
        "ipa": "/ˈɡɑːr.dɚ/",
        "vi": "người canh giữ; lính canh phòng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082893",
        "hw": "guardhouses",
        "pos": "noun",
        "ipa": "/ˈɡɑːrdˌhaʊ.zɪz/",
        "vi": "các trạm gác binh; trại giam đồn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082894",
        "hw": "guardians",
        "pos": "noun",
        "ipa": "/ˈɡɑːr.di.ənz/",
        "vi": "những người bảo hộ; các giám hộ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082895",
        "hw": "guarding",
        "pos": "verb",
        "ipa": "/ˈɡɑːr.dɪŋ/",
        "vi": "đang canh gác; bảo vệ; trông coi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082896",
        "hw": "guardings",
        "pos": "noun",
        "ipa": "/ˈɡɑːr.dɪŋz/",
        "vi": "các bộ phận bảo hộ; tấm che chắn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082897",
        "hw": "guardless",
        "pos": "adj",
        "ipa": "/ˈɡɑːrd.ləs/",
        "vi": "không phòng vệ; không được canh giữ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082898",
        "hw": "guards",
        "pos": "verb",
        "ipa": "/ɡɑːrdz/",
        "vi": "canh giữ; bảo vệ; phòng bị chu đáo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082899",
        "hw": "guardsmen",
        "pos": "noun",
        "ipa": "/ˈɡɑːrdz.mən/",
        "vi": "những người lính cận vệ; vệ binh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082900",
        "hw": "guarnerius",
        "pos": "noun",
        "ipa": "/ɡwɑːrˈnɛər.i.əs/",
        "vi": "cây đàn vĩ cầm Guarneri cổ của Ý",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.082901",
        "hw": "gubernaculum",
        "pos": "noun",
        "ipa": "/ˌɡuː.bɚˈnæk.jʊ.ləm/",
        "vi": "dây kéo tinh hoàn; thể định hướng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

# Validation
with open("scratch/b17_r06_raw_p4.json") as f:
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

print("All 100 records in Part 4 verified successfully!")
