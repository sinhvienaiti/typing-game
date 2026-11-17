import json

reviewed_items = [
    {
        "id": "lex.en.200k.042902",
        "hw": "alpine salamander",
        "pos": "phrase",
        "ipa": "/ˈælpaɪn ˈsæləˌmændər/",
        "vi": "loài kỳ giông đen vùng núi Alps",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042903",
        "hw": "ambrose everett burnside",
        "pos": "phrase",
        "ipa": "/ˈæmbroʊz ˈɛvərɪt ˈbɜːrnˌsaɪd/",
        "vi": "tướng Ambrose Everett Burnside",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042904",
        "hw": "american shrew mole",
        "pos": "phrase",
        "ipa": "/əˈmɛrɪkən ʃruː moʊl/",
        "vi": "chuột chũi chuột chù Bắc Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042905",
        "hw": "atlantic halibut",
        "pos": "phrase",
        "ipa": "/ætˈlæntɪk ˈhælɪbət/",
        "vi": "cá bơn lớn biển Đại Tây Dương",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042906",
        "hw": "australian nettle tree",
        "pos": "phrase",
        "ipa": "/ɔːˈstreɪliən ˈnɛtl triː/",
        "vi": "cây tầm ma lá độc khổng lồ Úc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042907",
        "hw": "azure aster",
        "pos": "phrase",
        "ipa": "/ˈæʒər ˈæstər/",
        "vi": "hoa cúc tây cánh xanh lơ biếc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042908",
        "hw": "bladder sphincter",
        "pos": "phrase",
        "ipa": "/ˈblædər ˈsfɪŋktər/",
        "vi": "cơ vòng thắt cổ bàng quang",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042909",
        "hw": "bog aster",
        "pos": "phrase",
        "ipa": "/bɑːɡ ˈæstər/",
        "vi": "cây hoa cúc tây đầm lầy dại",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042910",
        "hw": "bull nettle",
        "pos": "phrase",
        "ipa": "/bʊl ˈnɛtl/",
        "vi": "cây tầm ma gai lớn có gai độc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042911",
        "hw": "calcium bicarbonate",
        "pos": "phrase",
        "ipa": "/ˈkælsiəm baɪˌkɑːrbənət/",
        "vi": "muối canxi bicacbonat hóa học",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042912",
        "hw": "carnation family",
        "pos": "phrase",
        "ipa": "/kɑːrˈneɪʃən ˈfæmɪli/",
        "vi": "họ thực vật hoa cẩm chướng rừng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042913",
        "hw": "carrion flower",
        "pos": "phrase",
        "ipa": "/ˈkæriən ˈflaʊər/",
        "vi": "hoa xác thối tỏa mùi rữa",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042914",
        "hw": "cervical plexus",
        "pos": "phrase",
        "ipa": "/ˈsɜːrvɪkl ˈplɛksəs/",
        "vi": "đám rối thần kinh vùng cổ gáy",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042915",
        "hw": "child molester",
        "pos": "phrase",
        "ipa": "/tʃaɪld məˈlɛstər/",
        "vi": "kẻ lạm dụng xâm hại trẻ em",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042916",
        "hw": "chili con carne",
        "pos": "phrase",
        "ipa": "/ˈtʃɪli kɑːn ˈkɑːrni/",
        "vi": "món hầm ớt thịt bò bằm cay xé",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042917",
        "hw": "circus acrobat",
        "pos": "phrase",
        "ipa": "/ˈsɜːrkəs ˈækrəbæt/",
        "vi": "nghệ sĩ xiếc nhào lộn điêu luyện",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042918",
        "hw": "convergent thinker",
        "pos": "phrase",
        "ipa": "/kənˈvɜːrdʒənt ˈθɪŋkər/",
        "vi": "người có lối tư duy hội tụ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042919",
        "hw": "corkscrew flower",
        "pos": "phrase",
        "ipa": "/ˈkɔːrkskruː ˈflaʊər/",
        "vi": "cây hoa ốc xoắn hình xoắn ốc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042920",
        "hw": "crew neckline",
        "pos": "phrase",
        "ipa": "/kruː ˈnɛklaɪn/",
        "vi": "kiểu đường viền cổ áo tròn ôm",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042921",
        "hw": "croquet ball",
        "pos": "phrase",
        "ipa": "/kroʊˈkeɪ bɔːl/",
        "vi": "quả bóng gỗ chơi môn croquet",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042922",
        "hw": "croquet equipment",
        "pos": "phrase",
        "ipa": "/kroʊˈkeɪ ɪˈkwɪpmənt/",
        "vi": "bộ dụng cụ thi đấu bóng vồ croquet",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042923",
        "hw": "devil nettle",
        "pos": "phrase",
        "ipa": "/ˈdɛvl ˈnɛtl/",
        "vi": "cây tầm ma độc lá nhọn gai quỷ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042924",
        "hw": "dissociative disorder",
        "pos": "phrase",
        "ipa": "/dɪˈsoʊʃieɪtɪv dɪsˈɔːrdər/",
        "vi": "chứng rối loạn tâm thần phân ly",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042925",
        "hw": "diverging lens",
        "pos": "phrase",
        "ipa": "/daɪˈvɜːrdʒɪŋ lɛnz/",
        "vi": "thấu kính quang học phân kỳ",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042926",
        "hw": "edward thatch",
        "pos": "phrase",
        "ipa": "/ˈɛdwərd θætʃ/",
        "vi": "hải tặc râu đen Edward Thatch",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042927",
        "hw": "eugene victor debs",
        "pos": "phrase",
        "ipa": "/juːˈdʒiːn ˈvɪktər dɛbz/",
        "vi": "nhà hoạt động Eugene V. Debs",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042928",
        "hw": "exclusionary rule",
        "pos": "phrase",
        "ipa": "/ɪkˈskluːʒənɛri ruːl/",
        "vi": "quy tắc bác bỏ chứng cứ sai luật",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042929",
        "hw": "fen orchid",
        "pos": "phrase",
        "ipa": "/fɛn ˈɔːrkɪd/",
        "vi": "hoa phong lan mọc đầm than bùn",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042930",
        "hw": "ferdinand magellan",
        "pos": "phrase",
        "ipa": "/ˈfɜːrdɪnænd məˈdʒɛlən/",
        "vi": "nhà thám hiểm Ferdinand Magellan",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042931",
        "hw": "folic acid",
        "pos": "phrase",
        "ipa": "/ˌfoʊlɪk ˈæsɪd/",
        "vi": "axit folic; vitamin B9 hòa tan",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042932",
        "hw": "forehand drive",
        "pos": "phrase",
        "ipa": "/ˈfɔːrhænd draɪv/",
        "vi": "cú vụt bóng thuận tay uy lực",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042933",
        "hw": "forehand shot",
        "pos": "phrase",
        "ipa": "/ˈfɔːrhænd ʃɑːt/",
        "vi": "cú đánh trả bóng bằng tay thuận",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042934",
        "hw": "foucault pendulum",
        "pos": "phrase",
        "ipa": "/fuːˈkoʊ ˈpɛndʒələm/",
        "vi": "con lắc Foucault đo Trái Đất quay",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042935",
        "hw": "gabon franc",
        "pos": "phrase",
        "ipa": "/ɡæˈbɔːn fræŋk/",
        "vi": "đồng tiền phrăng nước Gabon",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042936",
        "hw": "genus agave",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs əˈɡɑːvi/",
        "vi": "chi thực vật thùa Agave mọng nước",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042937",
        "hw": "genus iguana",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs ɪˈɡwɑːnə/",
        "vi": "chi cự đà Nam Mỹ Iguana",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042938",
        "hw": "genus proteus",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs ˈproʊtiəs/",
        "vi": "chi kỳ giông mù hang động Proteus",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042939",
        "hw": "glandular plague",
        "pos": "phrase",
        "ipa": "/ˈɡlændʒələr pleɪɡ/",
        "vi": "bệnh dịch hạch thể sưng hạch",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042940",
        "hw": "gregorian telescope",
        "pos": "phrase",
        "ipa": "/ɡrɪˈɡɔːriən ˈtɛləskoʊp/",
        "vi": "kính thiên văn phản xạ Gregory",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042941",
        "hw": "gunnery sergeant",
        "pos": "phrase",
        "ipa": "/ˈɡʌnəri ˈsɑːrdʒənt/",
        "vi": "trung sĩ nhất pháo binh lục chiến",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042942",
        "hw": "gustav ludwig hertz",
        "pos": "phrase",
        "ipa": "/ˈɡʊstɑːf ˈlʊdvɪç hɛərts/",
        "vi": "nhà vật lý Gustav Ludwig Hertz",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042943",
        "hw": "guy fawkes",
        "pos": "phrase",
        "ipa": "/ɡaɪ fɔːks/",
        "vi": "nhân vật lịch sử Guy Fawkes",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042944",
        "hw": "guy fawkes day",
        "pos": "phrase",
        "ipa": "/ɡaɪ fɔːks deɪ/",
        "vi": "ngày lễ đốt pháo Guy Fawkes",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042945",
        "hw": "guy fawkes night",
        "pos": "phrase",
        "ipa": "/ɡaɪ fɔːks naɪt/",
        "vi": "đêm đốt lửa mừng Guy Fawkes",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042946",
        "hw": "harlequin opal",
        "pos": "phrase",
        "ipa": "/ˈhɑːrləkwɪn ˈoʊpl/",
        "vi": "ngọc mắt mèo opal đa sắc hoa văn",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042947",
        "hw": "hdl cholesterol",
        "pos": "phrase",
        "ipa": "/ˌeɪtʃ diː ˈɛl kəˈlɛstərɔːl/",
        "vi": "cholesterol tỷ trọng cao có lợi",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042948",
        "hw": "himalaya mountains",
        "pos": "phrase",
        "ipa": "/ˌhɪməˈleɪə ˈmaʊntənz/",
        "vi": "dãy núi hùng vĩ Himalaya",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042949",
        "hw": "huckleberry finn",
        "pos": "phrase",
        "ipa": "/ˈhʌklbɛri fɪn/",
        "vi": "nhân vật cậu bé Huckleberry Finn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042950",
        "hw": "huntingdon elm",
        "pos": "phrase",
        "ipa": "/ˈhʌntɪŋdən ɛlm/",
        "vi": "cây du lai Huntingdon tán rộng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042951",
        "hw": "idiot savant",
        "pos": "phrase",
        "ipa": "/ˌɪdiət sæˈvɑːnt/",
        "vi": "bác học thiểu năng có thiên tài",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042952",
        "hw": "ignatius of loyola",
        "pos": "phrase",
        "ipa": "/ɪɡˈneɪʃəs əv lɔɪˈoʊlə/",
        "vi": "Thánh I-nhã vùng Loyola",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042953",
        "hw": "in utero",
        "pos": "phrase",
        "ipa": "/ɪn ˈjuːtəroʊ/",
        "vi": "ở trong tử cung; trong bào thai",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042954",
        "hw": "interagency support",
        "pos": "phrase",
        "ipa": "/ˌɪntərˈeɪdʒənsi səˈpɔːrt/",
        "vi": "hỗ trợ phối hợp liên cơ quan",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042955",
        "hw": "lateral ventricle",
        "pos": "phrase",
        "ipa": "/ˈlætərəl ˈvɛntrɪkl/",
        "vi": "não thất bên ở bán cầu đại não",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042956",
        "hw": "lop off",
        "pos": "phrase",
        "ipa": "/lɑːp ɔːf/",
        "vi": "chặt đứt lìa cành; cắt phăng đi",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042957",
        "hw": "marcel proust",
        "pos": "phrase",
        "ipa": "/mɑːrˈsɛl pruːst/",
        "vi": "nhà văn đại tài Marcel Proust",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042958",
        "hw": "marconi rig",
        "pos": "phrase",
        "ipa": "/mɑːrˈkoʊni rɪɡ/",
        "vi": "kiểu giàn buồm tam giác Marconi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042959",
        "hw": "masked shrew",
        "pos": "phrase",
        "ipa": "/mæskt ʃruː/",
        "vi": "loài chuột chù có đốm mặt nạ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042960",
        "hw": "mesquite gum",
        "pos": "phrase",
        "ipa": "/mɛsˈkit ɡʌm/",
        "vi": "chất gôm dẻo từ cây mesquite",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042961",
        "hw": "mew gull",
        "pos": "phrase",
        "ipa": "/mjuː ɡʌl/",
        "vi": "chim mòng biển hoa mew ven bờ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042962",
        "hw": "mussel shrimp",
        "pos": "phrase",
        "ipa": "/ˈmʌsl ʃrɪmp/",
        "vi": "loài tôm nhỏ giáp xác hai mảnh vỏ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042963",
        "hw": "mutton snapper",
        "pos": "phrase",
        "ipa": "/ˈmʌtn ˈsnæpər/",
        "vi": "cá hồng mutton vây đuôi hồng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042964",
        "hw": "nitric bacterium",
        "pos": "phrase",
        "ipa": "/ˈnaɪtrɪk bækˈtɪəriəm/",
        "vi": "vi khuẩn nitrat hóa đất phì nhiêu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042965",
        "hw": "nitrous bacterium",
        "pos": "phrase",
        "ipa": "/ˈnaɪtrəs bækˈtɪəriəm/",
        "vi": "vi khuẩn nitrit hóa chuyển hóa đạm",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042966",
        "hw": "northern harrier",
        "pos": "phrase",
        "ipa": "/ˈnɔːrðərn ˈhæriər/",
        "vi": "chim ưng cánh dài miền bắc săn mồi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042967",
        "hw": "oat cell carcinoma",
        "pos": "phrase",
        "ipa": "/oʊt sɛl ˌkɑːrsɪˈnoʊmə/",
        "vi": "ung thư biểu mô phổi tế bào nhỏ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042968",
        "hw": "origination fee",
        "pos": "phrase",
        "ipa": "/əˌrɪdʒəˈneɪʃən fiː/",
        "vi": "phí thẩm định mở hồ sơ vay vốn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042969",
        "hw": "pacific halibut",
        "pos": "phrase",
        "ipa": "/pəˈsɪfɪk ˈhælɪbət/",
        "vi": "loài cá bơn Thái Bình Dương lớn",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042970",
        "hw": "painted nettle",
        "pos": "phrase",
        "ipa": "/ˈpeɪntɪd ˈnɛtl/",
        "vi": "cây tía tô cảnh nhiều lá màu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042971",
        "hw": "paraffin wax",
        "pos": "phrase",
        "ipa": "/ˈpærəfɪn wæks/",
        "vi": "sáp nến parafin công nghiệp",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042972",
        "hw": "pelvic girdle",
        "pos": "phrase",
        "ipa": "/ˈpɛlvɪk ˈɡɜːrdl/",
        "vi": "vòng xương đai chậu xương chậu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042973",
        "hw": "plate tectonics",
        "pos": "phrase",
        "ipa": "/pleɪt tɛkˈtɑːnɪks/",
        "vi": "thuyết kiến tạo mảng địa chất",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042974",
        "hw": "pole vaulting",
        "pos": "phrase",
        "ipa": "/poʊl ˈvɔːltɪŋ/",
        "vi": "môn thể thao điền kinh nhảy sào",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042975",
        "hw": "prefrontal lobe",
        "pos": "phrase",
        "ipa": "/priːˈfrʌntl loʊb/",
        "vi": "vùng thùy tiền trán vỏ não",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042976",
        "hw": "pulmonary embolism",
        "pos": "phrase",
        "ipa": "/ˈpʊlmənɛri ˈɛmbəlɪzəm/",
        "vi": "chứng tắc mạch máu màng phổi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042977",
        "hw": "purplish pink",
        "pos": "phrase",
        "ipa": "/ˈpɜːrplɪʃ pɪŋk/",
        "vi": "màu hồng ánh tím phớt biếc",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042978",
        "hw": "pyramidal tract",
        "pos": "phrase",
        "ipa": "/pɪˈræmɪdl trækt/",
        "vi": "bó tháp dẫn truyền vận động não",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042979",
        "hw": "refractory anemia",
        "pos": "phrase",
        "ipa": "/rɪˈfræktəri əˈniːmiə/",
        "vi": "chứng thiếu máu dai dẳng kháng trị",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042980",
        "hw": "roman nettle",
        "pos": "phrase",
        "ipa": "/ˈroʊmən ˈnɛtl/",
        "vi": "cây tầm ma La Mã có gai chích đau",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042981",
        "hw": "rorschach test",
        "pos": "phrase",
        "ipa": "/ˈrɔːrʃɑːk tɛst/",
        "vi": "trắc nghiệm tâm lý mực Rorschach",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042982",
        "hw": "salvadoran capital",
        "pos": "phrase",
        "ipa": "/ˌsælvəˈdɔːriən ˈkæpɪtl/",
        "vi": "thủ đô San Salvador ở Trung Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042983",
        "hw": "scotch marigold",
        "pos": "phrase",
        "ipa": "/skɑːtʃ ˈmærɪɡoʊld/",
        "vi": "cây hoa cúc vạn thọ cam Scotland",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042984",
        "hw": "sea chub",
        "pos": "phrase",
        "ipa": "/siː tʃʌb/",
        "vi": "loài cá mè biển ăn rong tảo rạn",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042985",
        "hw": "shari river",
        "pos": "phrase",
        "ipa": "/ˈʃɑːri ˈrɪvər/",
        "vi": "dòng sông ngòi Chari miền Trung Phi",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042986",
        "hw": "shock absorber",
        "pos": "phrase",
        "ipa": "/ʃɑːk əbˈzɔːrbər/",
        "vi": "bộ phận giảm xóc giảm chấn xe cộ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042987",
        "hw": "shrew mole",
        "pos": "phrase",
        "ipa": "/ʃruː moʊl/",
        "vi": "chuột chũi chuột chù nhỏ đào hang",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042988",
        "hw": "silurian period",
        "pos": "phrase",
        "ipa": "/sɪˈljʊəriən ˈpɪəriəd/",
        "vi": "kỷ Silur; kỷ địa chất Silurian",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042989",
        "hw": "silver bromide",
        "pos": "phrase",
        "ipa": "/ˈsɪlvər ˈbroʊmaɪd/",
        "vi": "muối bạc bromua trong tráng phim",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042990",
        "hw": "simple mastectomy",
        "pos": "phrase",
        "ipa": "/ˈsɪmpl mæˈstɛktəmi/",
        "vi": "phẫu thuật cắt bỏ vú đơn thuần",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042991",
        "hw": "skeet shooting",
        "pos": "phrase",
        "ipa": "/skiːt ˈʃuːtɪŋ/",
        "vi": "môn thể thao bắn đĩa bay skeet",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042992",
        "hw": "slender salamander",
        "pos": "phrase",
        "ipa": "/ˈslɛndər ˈsæləˌmændər/",
        "vi": "loài kỳ giông thân mảnh khảnh dại",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042993",
        "hw": "slop chest",
        "pos": "phrase",
        "ipa": "/slɑːp tʃɛst/",
        "vi": "kho đồ dùng quân nhu cho thủy thủ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042994",
        "hw": "snake charmer",
        "pos": "phrase",
        "ipa": "/sneɪk ˈtʃɑːrmər/",
        "vi": "nghệ sĩ biểu diễn thôi miên rắn",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042995",
        "hw": "sodium bicarbonate",
        "pos": "phrase",
        "ipa": "/ˈsoʊdiəm baɪˈkɑːrbənət/",
        "vi": "muối natri bicacbonat; baking soda",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042996",
        "hw": "squash rackets",
        "pos": "phrase",
        "ipa": "/skwɑːʃ ˈrækɪts/",
        "vi": "môn thể thao bóng quần trong nhà",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042997",
        "hw": "stiletto heel",
        "pos": "phrase",
        "ipa": "/stɪˈlɛtoʊ hiːl/",
        "vi": "giày cao gót nhọn hoắt stiletto",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042998",
        "hw": "sump pump",
        "pos": "phrase",
        "ipa": "/sʌmp pʌmp/",
        "vi": "máy bơm hút nước ngập hố ga móng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.042999",
        "hw": "swiss chard",
        "pos": "phrase",
        "ipa": "/swɪs tʃɑːrd/",
        "vi": "rau cải cầu vồng Thụy Sĩ giòn ngọt",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043000",
        "hw": "tanzanian monetary unit",
        "pos": "phrase",
        "ipa": "/ˌtænzəˈniːən ˈmʌnɪtɛri ˈjuːnɪt/",
        "vi": "đơn vị tiền shilling của Tanzania",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043001",
        "hw": "texas armadillo",
        "pos": "phrase",
        "ipa": "/ˈtɛksəs ˌɑːrməˈdɪloʊ/",
        "vi": "con tatu chín đai sống ở bang Texas",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r06_raw_p5.json') as f:
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

with open('scratch/b29_r06_p5.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 6 Part 5 verified and written successfully.")
