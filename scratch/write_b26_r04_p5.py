import json

# Batch 26 Round 4 Part 5 (lex.en.200k.026902 to lex.en.200k.027001)
records = [
    {
        "id": "lex.en.200k.026902",
        "hw": "jamaican cherry",
        "pos": "phrase",
        "ipa": "/dʒəˈmeɪ.kən ˈtʃer.i/",
        "vi": "cây trứng cá; anh đào Jamaica",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026903",
        "hw": "john mercer",
        "pos": "phrase",
        "ipa": "/dʒɑːn ˈmɝː.sɚ/",
        "vi": "John Mercer; nhà hóa học dệt may",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026904",
        "hw": "kangaroo bear",
        "pos": "phrase",
        "ipa": "/ˌkæŋ.ɡəˈruː ber/",
        "vi": "gấu túi koala nước Úc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026905",
        "hw": "lance corporal",
        "pos": "phrase",
        "ipa": "/ˌlæns ˈkɔːr.pɚ.əl/",
        "vi": "binh nhất; phó hạ sĩ quân đội",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026906",
        "hw": "leaf lettuce",
        "pos": "phrase",
        "ipa": "/liːf ˈlet̬.ɪs/",
        "vi": "xà lách lá mềm; xà lách mỡ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026907",
        "hw": "letter of jeremiah",
        "pos": "phrase",
        "ipa": "/ˈlet̬.ɚ əv ˌdʒer.əˈmaɪ.ə/",
        "vi": "Thư Giê-rê-mi; sách thứ kinh",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026908",
        "hw": "living accommodations",
        "pos": "phrase",
        "ipa": "/ˈlɪv.ɪŋ əˌkɑː.məˈdeɪ.ʃənz/",
        "vi": "chỗ ăn ở; tiện nghi sinh hoạt",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026909",
        "hw": "magnetic flux",
        "pos": "phrase",
        "ipa": "/mæɡˈnet̬.ɪk flʌks/",
        "vi": "từ thông qua tiết diện",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026910",
        "hw": "mandarin orange tree",
        "pos": "phrase",
        "ipa": "/ˈmæn.dɚ.ɪn ˈɔːr.ɪndʒ triː/",
        "vi": "cây quýt hồng; cây quýt đường",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026911",
        "hw": "mental exhaustion",
        "pos": "phrase",
        "ipa": "/ˈmen.t̬əl ɪɡˈzɑːs.tʃən/",
        "vi": "kiệt quệ tinh thần; suy nhược não",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026912",
        "hw": "mirror symmetry",
        "pos": "phrase",
        "ipa": "/ˈmɪr.ɚ ˈsɪm.ə.tri/",
        "vi": "đối xứng gương; tính chẵn lẻ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026913",
        "hw": "mixed nuisance",
        "pos": "phrase",
        "ipa": "/mɪkst ˈnuː.səns/",
        "vi": "phiền toái hỗn hợp công và tư",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026914",
        "hw": "mock turtle soup",
        "pos": "phrase",
        "ipa": "/mɑːk ˈtɝː.t̬əl suːp/",
        "vi": "súp thịt bê giả rùa",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026915",
        "hw": "musk rose",
        "pos": "phrase",
        "ipa": "/mʌsk roʊz/",
        "vi": "hoa hồng xạ hương trắng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026916",
        "hw": "mustard greens",
        "pos": "phrase",
        "ipa": "/ˈmʌs.tɚd ɡriːnz/",
        "vi": "rau cải xanh; cải cay",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026917",
        "hw": "neurological disorder",
        "pos": "phrase",
        "ipa": "/ˌnʊr.əˈlɑː.dʒɪ.kəl dɪsˈɔːr.dɚ/",
        "vi": "rối loạn chức năng hệ thần kinh",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026918",
        "hw": "norwegian lobster",
        "pos": "phrase",
        "ipa": "/nɔːrˈwiː.dʒən ˈlɑːb.stɚ/",
        "vi": "tôm hùm Na Uy gai nhỏ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026919",
        "hw": "orbital rotation",
        "pos": "phrase",
        "ipa": "/ˈɔːr.bə.t̬əl roʊˈteɪ.ʃən/",
        "vi": "chuyển động quay trên quỹ đạo",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026920",
        "hw": "panther lily",
        "pos": "phrase",
        "ipa": "/ˈpæn.θɚ ˈlɪl.i/",
        "vi": "hoa loa kèn đốm báo California",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026921",
        "hw": "parrot disease",
        "pos": "phrase",
        "ipa": "/ˈper.ət dɪˈziːz/",
        "vi": "bệnh vẹt lây sang người",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026922",
        "hw": "pea jacket",
        "pos": "phrase",
        "ipa": "/ˈpiː ˌdʒæk.ɪt/",
        "vi": "áo khoác len dày của thủy thủ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026923",
        "hw": "physiological psychology",
        "pos": "phrase",
        "ipa": "/ˌfɪz.i.əˈlɑː.dʒɪ.kəl saɪˈkɑː.lə.dʒi/",
        "vi": "tâm lý học sinh lý học",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026924",
        "hw": "pine bluff",
        "pos": "phrase",
        "ipa": "/paɪn blʌf/",
        "vi": "thành phố Pine Bluff bang Arkansas",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026925",
        "hw": "pink disease fungus",
        "pos": "phrase",
        "ipa": "/pɪŋk dɪˈziːz ˈfʌŋ.ɡəs/",
        "vi": "nấm mốc hồng gây bệnh nấm vỏ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026926",
        "hw": "pivot joint",
        "pos": "phrase",
        "ipa": "/ˈpɪv.ət dʒɔɪnt/",
        "vi": "khớp xoay trục xương",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026927",
        "hw": "placebo effect",
        "pos": "phrase",
        "ipa": "/pləˈsiː.boʊ ɪˌfekt/",
        "vi": "hiệu ứng giả dược chữa lành tâm lý",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026928",
        "hw": "plea bargaining",
        "pos": "phrase",
        "ipa": "/ˈpliː ˌbɑːr.ɡən.ɪŋ/",
        "vi": "thỏa thuận nhận tội giảm án",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026929",
        "hw": "pocket comb",
        "pos": "phrase",
        "ipa": "/ˈpɑː.kɪt koʊm/",
        "vi": "chiếc lược nhỏ bỏ túi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026930",
        "hw": "potato mosaic",
        "pos": "phrase",
        "ipa": "/pəˈteɪ.t̬oʊ moʊˈzeɪ.ɪk/",
        "vi": "bệnh virus khảm lá khoai tây",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026931",
        "hw": "preventive strike",
        "pos": "phrase",
        "ipa": "/prɪˈven.t̬ɪv straɪk/",
        "vi": "đòn tấn công phủ đầu phòng ngừa",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026932",
        "hw": "psychic phenomena",
        "pos": "phrase",
        "ipa": "/ˈsaɪ.kɪk fəˈnɑː.mə.nə/",
        "vi": "hiện tượng tâm linh huyền bí",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026933",
        "hw": "pulmonary reserve",
        "pos": "phrase",
        "ipa": "/ˈpʊl.mə.ner.i rɪˈzɝːv/",
        "vi": "dung lượng dự trữ hô hấp phổi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026934",
        "hw": "purple pea",
        "pos": "phrase",
        "ipa": "/ˈpɝː.pəl piː/",
        "vi": "cây đậu dại hoa tím Úc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026935",
        "hw": "quasi contract",
        "pos": "phrase",
        "ipa": "/ˌkweɪ.zaɪ ˈkɑːn.trækt/",
        "vi": "chuẩn hợp đồng nghĩa vụ luật định",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026936",
        "hw": "queen isabella",
        "pos": "phrase",
        "ipa": "/kwiːn ˌɪz.əˈbel.ə/",
        "vi": "Nữ hoàng Isabella xứ Tây Ban Nha",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026937",
        "hw": "radioactive decay",
        "pos": "phrase",
        "ipa": "/ˌreɪ.di.oʊˈæk.tɪv dɪˈkeɪ/",
        "vi": "quá trình phân rã phóng xạ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026938",
        "hw": "rain buckets",
        "pos": "phrase",
        "ipa": "/reɪn ˈbʌk.ɪts/",
        "vi": "mưa như trút nước; mưa tầm tã",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026939",
        "hw": "reap hook",
        "pos": "phrase",
        "ipa": "/riːp hʊk/",
        "vi": "lưỡi liềm gặt lúa; liềm cắt cỏ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026940",
        "hw": "red herring",
        "pos": "phrase",
        "ipa": "/ˌred ˈher.ɪŋ/",
        "vi": "hỏa mù đánh lạc hướng dư luận",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026941",
        "hw": "reef knot",
        "pos": "phrase",
        "ipa": "/riːf nɑːt/",
        "vi": "nút dẹt; nút buộc nối dây vuông",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026942",
        "hw": "religious trance",
        "pos": "phrase",
        "ipa": "/rɪˈlɪdʒ.əs træns/",
        "vi": "trạng thái xuất thần tôn giáo",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026943",
        "hw": "republic of liberia",
        "pos": "phrase",
        "ipa": "/rɪˈpʌb.lɪk əv laɪˈbɪr.i.ə/",
        "vi": "nước Cộng hòa Liberia Tây Phi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026944",
        "hw": "republic of lithuania",
        "pos": "phrase",
        "ipa": "/rɪˈpʌb.lɪk əv ˌlɪθ.uˈeɪ.ni.ə/",
        "vi": "nước Cộng hòa Lít-va Baltic",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026945",
        "hw": "residual soil",
        "pos": "phrase",
        "ipa": "/rɪˈzɪdʒ.u.əl sɔɪl/",
        "vi": "đất tàn dư phong hóa tại chỗ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026946",
        "hw": "rewrite man",
        "pos": "phrase",
        "ipa": "/ˈriː.raɪt mæn/",
        "vi": "biên tập viên phóng sự tòa soạn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026947",
        "hw": "robert tyre jones",
        "pos": "phrase",
        "ipa": "/ˈrɑː.bɚt taɪr dʒoʊnz/",
        "vi": "Bobby Jones; huyền thoại golf Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026948",
        "hw": "rock hopper",
        "pos": "phrase",
        "ipa": "/rɑːk ˈhɑː.pɚ/",
        "vi": "chim cánh cụt mào nhảy mỏm đá",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026949",
        "hw": "rope yarn",
        "pos": "phrase",
        "ipa": "/roʊp jɑːrn/",
        "vi": "sợi chỉ bện thành dây thừng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026950",
        "hw": "router plane",
        "pos": "phrase",
        "ipa": "/ˈraʊ.t̬ɚ pleɪn/",
        "vi": "bào đáy rãnh chìm nghề mộc",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026951",
        "hw": "roy chapman andrews",
        "pos": "phrase",
        "ipa": "/rɔɪ ˈtʃæp.mən ˈæn.druːz/",
        "vi": "Roy Andrews; nhà thám hiểm Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026952",
        "hw": "runaway robin",
        "pos": "phrase",
        "ipa": "/ˈrʌn.ə.weɪ ˈrɑː.bɪn/",
        "vi": "cây bạc hà bò dây leo dại",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026953",
        "hw": "scandinavian nation",
        "pos": "phrase",
        "ipa": "/ˌskæn.dəˈneɪ.vi.ən ˈneɪ.ʃən/",
        "vi": "quốc gia Bắc Âu vùng Scandinavia",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026954",
        "hw": "scissors grip",
        "pos": "phrase",
        "ipa": "/ˈsɪz.ɚz ɡrɪp/",
        "vi": "thế kẹp chân cắt kéo đấu vật",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026955",
        "hw": "sealing material",
        "pos": "phrase",
        "ipa": "/ˈsiː.lɪŋ məˈtɪr.i.əl/",
        "vi": "vật liệu trám kín chống thấm rò rỉ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026956",
        "hw": "seed beetle",
        "pos": "phrase",
        "ipa": "/siːd ˈbiː.t̬əl/",
        "vi": "mọt đục phá hạt giống cây",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026957",
        "hw": "sex chromosome",
        "pos": "phrase",
        "ipa": "/seks ˈkroʊ.mə.soʊm/",
        "vi": "nhiễm sắc thể giới tính X hoặc Y",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026958",
        "hw": "shoe repairing",
        "pos": "phrase",
        "ipa": "/ʃuː rɪˈper.ɪŋ/",
        "vi": "nghề đóng sửa giày dép da",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026959",
        "hw": "simulated military operation",
        "pos": "phrase",
        "ipa": "/ˈsɪm.jə.leɪ.t̬ɪd ˈmɪl.ə.ter.i ˌɑː.pəˈreɪ.ʃən/",
        "vi": "cuộc diễn tập quân sự giả định",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026960",
        "hw": "song sparrow",
        "pos": "phrase",
        "ipa": "/sɑːŋ ˈsper.oʊ/",
        "vi": "chim sẻ hót líu lo Bắc Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026961",
        "hw": "sorting algorithm",
        "pos": "phrase",
        "ipa": "/ˈsɔːr.tɪŋ ˈæl.ɡə.rɪð.əm/",
        "vi": "thuật toán sắp xếp dữ liệu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026962",
        "hw": "spaghetti junction",
        "pos": "phrase",
        "ipa": "/spəˈɡet.i ˈdʒʌŋk.ʃən/",
        "vi": "nút giao thông cầu vượt chằng chịt",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026963",
        "hw": "sparrow unit",
        "pos": "phrase",
        "ipa": "/ˈsper.oʊ ˈjuː.nɪt/",
        "vi": "đội du kích ám sát đô thị ngầm",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026964",
        "hw": "stealth fighter",
        "pos": "phrase",
        "ipa": "/steltθ ˈfaɪ.t̬ɚ/",
        "vi": "máy bay tiêm kích tàng hình radar",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026965",
        "hw": "stirred up",
        "pos": "phrase",
        "ipa": "/stɝːd ʌp/",
        "vi": "bị khuấy động; bị kích động",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026966",
        "hw": "straw mushroom",
        "pos": "phrase",
        "ipa": "/strɔː ˈmʌʃ.ruːm/",
        "vi": "nấm rơm tươi; nấm rơm ăn được",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026967",
        "hw": "striped bass",
        "pos": "phrase",
        "ipa": "/straɪpt bæs/",
        "vi": "cá vược sọc nước mặn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026968",
        "hw": "sweat duct",
        "pos": "phrase",
        "ipa": "/swet dʌkt/",
        "vi": "ống dẫn tuyến mồ hôi dưới da",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026969",
        "hw": "sweetness and light",
        "pos": "phrase",
        "ipa": "/ˈswiːt.nəs ən laɪt/",
        "vi": "thái độ hòa nhã êm đẹp vui vẻ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026970",
        "hw": "tally clerk",
        "pos": "phrase",
        "ipa": "/ˈtæl.i klɝːk/",
        "vi": "nhân viên kiểm đếm hàng bến bãi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026971",
        "hw": "tandem trailer",
        "pos": "phrase",
        "ipa": "/ˈtæn.dəm ˈtreɪ.lɚ/",
        "vi": "xe kéo rơ-moóc kép đôi hàng hóa",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026972",
        "hw": "territorial dominion",
        "pos": "phrase",
        "ipa": "/ˌter.əˈtɔːr.i.əl dəˈmɪn.jən/",
        "vi": "quyền cai quản lãnh thổ quốc gia",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026973",
        "hw": "theodore roosevelt",
        "pos": "phrase",
        "ipa": "/ˈθiː.ə.dɔːr ˈroʊ.zə.velt/",
        "vi": "Theodore Roosevelt; Tổng thống Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026974",
        "hw": "thermal equilibrium",
        "pos": "phrase",
        "ipa": "/ˈθɝː.məl ˌiː.kwəˈlɪb.ri.əm/",
        "vi": "trạng thái cân bằng nhiệt năng",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026975",
        "hw": "tidy sum",
        "pos": "phrase",
        "ipa": "/ˈtaɪ.di sʌm/",
        "vi": "khoản tiền lớn kha khá đáng kể",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026976",
        "hw": "true anomaly",
        "pos": "phrase",
        "ipa": "/truː əˈnɑː.mə.li/",
        "vi": "góc dị thường thực quỹ đạo",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026977",
        "hw": "true fir",
        "pos": "phrase",
        "ipa": "/truː fɝː/",
        "vi": "cây lãnh sam thật chi Abies",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026978",
        "hw": "true sparrow",
        "pos": "phrase",
        "ipa": "/truː ˈsper.oʊ/",
        "vi": "chim sẻ thật họ Passeridae",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026979",
        "hw": "unmarried man",
        "pos": "phrase",
        "ipa": "/ʌnˈmer.id mæn/",
        "vi": "người đàn ông độc thân chưa vợ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026980",
        "hw": "velvet worm",
        "pos": "phrase",
        "ipa": "/ˈvel.vɪt wɝːm/",
        "vi": "sâu nhung chân khớp Onychophora",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026981",
        "hw": "voltage regulator",
        "pos": "phrase",
        "ipa": "/ˈvoʊl.tɪdʒ ˈreɡ.jə.leɪ.t̬ɚ/",
        "vi": "bộ ổn định điện áp; máy ổn áp",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026982",
        "hw": "water ox",
        "pos": "phrase",
        "ipa": "/ˈwɑː.t̬ɚ ɑːks/",
        "vi": "con trâu nước châu Á",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026983",
        "hw": "weston cell",
        "pos": "phrase",
        "ipa": "/ˈwes.tən sel/",
        "vi": "pin chuẩn Weston tạo điện thế",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026984",
        "hw": "wheat gluten",
        "pos": "phrase",
        "ipa": "/wiːt ˈɡluː.tən/",
        "vi": "chất đạm gluten bột mì dẻo",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026985",
        "hw": "whisky neat",
        "pos": "phrase",
        "ipa": "/ˈwɪs.ki niːt/",
        "vi": "whisky nguyên chất không pha đá",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026986",
        "hw": "wine and dine",
        "pos": "phrase",
        "ipa": "/waɪn ən daɪn/",
        "vi": "chiêu đãi tiệc tùng rượu ngon",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026987",
        "hw": "yellow birch",
        "pos": "phrase",
        "ipa": "/ˈjel.oʊ bɝːtʃ/",
        "vi": "cây bạch dương vàng Bắc Mỹ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026988",
        "hw": "yorkshire pudding",
        "pos": "phrase",
        "ipa": "/ˈjɔːrk.ʃɚ ˈpʊd.ɪŋ/",
        "vi": "bánh nướng Yorkshire pudding Anh",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026989",
        "hw": "zen buddhist",
        "pos": "phrase",
        "ipa": "/zen ˈbʊd.ɪst/",
        "vi": "thiền sinh; tín đồ Thiền tông",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026990",
        "hw": "advisers",
        "pos": "noun",
        "ipa": "/ədˈvaɪ.zɚz/",
        "vi": "những người cố vấn; ban cố vấn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026991",
        "hw": "anatomies",
        "pos": "noun",
        "ipa": "/əˈnæt̬.ə.miz/",
        "vi": "những cấu trúc giải phẫu học",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026992",
        "hw": "automobiled",
        "pos": "verb",
        "ipa": "/ˈɑː.t̬ə.moʊ.biːld/",
        "vi": "đã di chuyển bằng xe ô tô hơi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026993",
        "hw": "automobiles",
        "pos": "noun",
        "ipa": "/ˈɑː.t̬ə.moʊ.biːlz/",
        "vi": "những chiếc xe hơi bốn bánh",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026994",
        "hw": "automobiling",
        "pos": "verb",
        "ipa": "/ˈɑː.t̬ə.moʊ.biːl.ɪŋ/",
        "vi": "việc lái xe ô tô; đi chơi xe hơi",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026995",
        "hw": "curtides",
        "pos": "noun",
        "ipa": "/ˈkɝː.tɪdz/",
        "vi": "những người thuộc dòng họ Curtis",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026996",
        "hw": "duller",
        "pos": "adj",
        "ipa": "/ˈdʌl.ɚ/",
        "vi": "cùn hơn; mờ nhạt chán ngắt hơn",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026997",
        "hw": "dullest",
        "pos": "adj",
        "ipa": "/ˈdʌl.ɪst/",
        "vi": "cùn nhất; chán ngắt nhạt nhẽo nhất",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026998",
        "hw": "grindings",
        "pos": "noun",
        "ipa": "/ˈɡraɪn.dɪŋz/",
        "vi": "mạt vụn nghiền; bã nghiền nhỏ",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.026999",
        "hw": "hobbies",
        "pos": "noun",
        "ipa": "/ˈhɑː.biz/",
        "vi": "những thú vui tiêu khiển; sở thích",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027000",
        "hw": "idols",
        "pos": "noun",
        "ipa": "/ˈaɪ.dəlz/",
        "vi": "các thần tượng; tượng thờ tôn kính",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.200k.027001",
        "hw": "modelings",
        "pos": "noun",
        "ipa": "/ˈmɑː.dəl.ɪŋz/",
        "vi": "các mô hình tạo dáng; tác phẩm mẫu",
        "cefr": "B2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

# Validation
ALLOWED_POS = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
EXPECTED_KEYS = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(records) == 100, f"Expected 100 records, got {len(records)}"

for r in records:
    assert list(r.keys()) == EXPECTED_KEYS, f"Keys mismatch in {r['id']}"
    assert r['pos'] in ALLOWED_POS, f"Invalid POS {r['pos']} in {r['id']}"
    assert r['ipa'].startswith('/') and r['ipa'].endswith('/') and len(r['ipa']) > 2, f"Invalid IPA in {r['id']}"
    assert r['ipa'].count('/') == 2, f"IPA slashes count error in {r['id']}: {r['ipa']}"
    assert len(r['vi']) <= 35, f"VI too long ({len(r['vi'])} chars): {r['vi']} in {r['id']}"
    assert r['status'] == 'reviewed', f"Status not reviewed in {r['id']}"

with open('scratch/b26_r04_p5.json', 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print("Wrote scratch/b26_r04_p5.json successfully")
