import json

reviewed_items = [
    {
        "id": "lex.en.200k.043702",
        "hw": "wobblier",
        "pos": "adj",
        "ipa": "/ˈwɑːbliər/",
        "vi": "lung lay hơn; lắc lư hơn",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043703",
        "hw": "wobbliest",
        "pos": "adj",
        "ipa": "/ˈwɑːbliɪst/",
        "vi": "lung lay nhất; lắc lư nhất",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043704",
        "hw": "wraiths",
        "pos": "noun",
        "ipa": "/reɪθs/",
        "vi": "những bóng ma; linh hồn báo tử",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043705",
        "hw": "yangons",
        "pos": "noun",
        "ipa": "/jæŋˈɡoʊnz/",
        "vi": "các khu đô thị Yangon",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043706",
        "hw": "yews",
        "pos": "noun",
        "ipa": "/juːz/",
        "vi": "cây thủy tùng; cây du sam",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043707",
        "hw": "yugoslavs",
        "pos": "noun",
        "ipa": "/ˈjuːɡoʊslɑːvz/",
        "vi": "người Nam Tư; các công dân Nam Tư",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043708",
        "hw": "agua toad",
        "pos": "phrase",
        "ipa": "/ˈɑːɡwə toʊd/",
        "vi": "loài cóc mía khổng lồ Nam Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043709",
        "hw": "al qaida",
        "pos": "phrase",
        "ipa": "/æl ˈkaɪdə/",
        "vi": "tổ chức khủng bố Al-Qaeda",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043710",
        "hw": "american marten",
        "pos": "phrase",
        "ipa": "/əˈmɛrɪkən ˈmɑːrtn/",
        "vi": "loài chồn macten châu Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043711",
        "hw": "ammonium hydroxide",
        "pos": "phrase",
        "ipa": "/əˈmoʊniəm haɪˈdrɑːksaɪd/",
        "vi": "dung dịch amoni hydroxit",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043712",
        "hw": "anabolic steroid",
        "pos": "phrase",
        "ipa": "/ˌænəˈbɑːlɪk ˈstɪrɔɪd/",
        "vi": "chất kích thích tăng cơ bắp",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043713",
        "hw": "barium oxide",
        "pos": "phrase",
        "ipa": "/ˈbæriəm ˈɑːksaɪd/",
        "vi": "hợp chất bari oxit",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043714",
        "hw": "battle of verdun",
        "pos": "phrase",
        "ipa": "/ˈbætl əv vɛərˈdʌn/",
        "vi": "trận đánh Verdun thời Thế chiến I",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043715",
        "hw": "bayonne bridge",
        "pos": "phrase",
        "ipa": "/beɪˈoʊn brɪdʒ/",
        "vi": "cầu vòm thép Bayonne ở New York",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043716",
        "hw": "beatrice lillie",
        "pos": "phrase",
        "ipa": "/ˈbiːətrɪs ˈlɪli/",
        "vi": "nữ diễn viên hài Beatrice Lillie",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043717",
        "hw": "bilge pump",
        "pos": "phrase",
        "ipa": "/ˈbɪldʒ pʌmp/",
        "vi": "máy bơm hút nước đáy tàu thuyền",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043718",
        "hw": "binomial theorem",
        "pos": "phrase",
        "ipa": "/baɪˈnoʊmiəl ˈθiːərəm/",
        "vi": "định lý nhị thức Newton",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043719",
        "hw": "biotic community",
        "pos": "phrase",
        "ipa": "/baɪˈɑːtɪk kəˈmjuːnəti/",
        "vi": "quần xã sinh vật trong tự nhiên",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043720",
        "hw": "bulbous plant",
        "pos": "phrase",
        "ipa": "/ˈbʌlbəs plænt/",
        "vi": "loài cây thân hành dự trữ dưỡng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043721",
        "hw": "burr marigold",
        "pos": "phrase",
        "ipa": "/bɜːr ˈmærɪɡoʊld/",
        "vi": "cây quỷ châm thảo hoa cúc gai",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043722",
        "hw": "bush honeysuckle",
        "pos": "phrase",
        "ipa": "/bʊʃ ˈhʌnisʌkl/",
        "vi": "cây kim ngân bụi rậm hoa vàng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043723",
        "hw": "butternut tree",
        "pos": "phrase",
        "ipa": "/ˈbʌtərnʌt triː/",
        "vi": "cây óc chó trắng Bắc Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043724",
        "hw": "cabbage palmetto",
        "pos": "phrase",
        "ipa": "/ˈkæbɪdʒ pælˈmɛtoʊ/",
        "vi": "cây cọ bắp cải vùng Florida Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043725",
        "hw": "cardiac insufficiency",
        "pos": "phrase",
        "ipa": "/ˈkɑːrdiæk ˌɪnsəˈfɪʃənsi/",
        "vi": "chứng suy tim; thiểu năng cơ tim",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043726",
        "hw": "cardigan welsh corgi",
        "pos": "phrase",
        "ipa": "/ˈkɑːrdɪɡən wɛlʃ ˈkɔːrɡi/",
        "vi": "chó Corgi giống Cardigan xứ Wales",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043727",
        "hw": "cartridge extractor",
        "pos": "phrase",
        "ipa": "/ˈkɑːrtrɪdʒ ɪkˈstræktər/",
        "vi": "bộ phận móc văng vỏ đạn súng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043728",
        "hw": "charles liston",
        "pos": "phrase",
        "ipa": "/tʃɑːrlz ˈlɪstən/",
        "vi": "võ sĩ Sonny Liston quyền Anh Mỹ",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043729",
        "hw": "collapsible shelter",
        "pos": "phrase",
        "ipa": "/kəˈlæpsəbl ˈʃɛltər/",
        "vi": "lều bạt gấp gọn; chỗ trú di động",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043730",
        "hw": "computer filename",
        "pos": "phrase",
        "ipa": "/kəmˈpjuːtər ˈfaɪlneɪm/",
        "vi": "tên tập tin máy tính",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043731",
        "hw": "constant of gravitation",
        "pos": "phrase",
        "ipa": "/ˈkɑːnstənt əv ˌɡrævɪˈteɪʃən/",
        "vi": "hằng số vạn vật hấp dẫn Newton",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043732",
        "hw": "coronary occlusion",
        "pos": "phrase",
        "ipa": "/ˈkɔːrənɛri əˈkluːʒən/",
        "vi": "sự tắc nghẽn động mạch vành tim",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043733",
        "hw": "dishonorable discharge",
        "pos": "phrase",
        "ipa": "/dɪsˈɑːnərəbl ˈdɪstʃɑːrdʒ/",
        "vi": "lệnh tước quân tịch do tội nhục",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043734",
        "hw": "edgar degas",
        "pos": "phrase",
        "ipa": "/ˈɛdɡɑːr dəˈɡɑː/",
        "vi": "danh họa Edgar Degas người Pháp",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043735",
        "hw": "edmund halley",
        "pos": "phrase",
        "ipa": "/ˈɛdmənd ˈhæli/",
        "vi": "nhà thiên văn học Edmund Halley",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043736",
        "hw": "endemic typhus",
        "pos": "phrase",
        "ipa": "/ɛnˈdɛmɪk ˈtaɪfəs/",
        "vi": "bệnh sốt phát ban chuột địa phương",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043737",
        "hw": "european fly honeysuckle",
        "pos": "phrase",
        "ipa": "/ˌjʊərəˈpiːən flaɪ ˈhʌnisʌkl/",
        "vi": "cây kim ngân hoa quả đỏ châu Âu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043738",
        "hw": "evergreen huckleberry",
        "pos": "phrase",
        "ipa": "/ˈɛvərɡriːn ˈhʌklbɛri/",
        "vi": "cây việt quất thường xanh Bắc Mỹ",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043739",
        "hw": "fess up",
        "pos": "phrase",
        "ipa": "/fɛs ʌp/",
        "vi": "thú nhận; chịu nhận tội lỗi",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043740",
        "hw": "firmer chisel",
        "pos": "phrase",
        "ipa": "/ˈfɜːrmər ˈtʃɪzl/",
        "vi": "chiếc đục mộc lưỡi dày bản thẳng",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043741",
        "hw": "first baron beveridge",
        "pos": "phrase",
        "ipa": "/fɜːrst ˈbærən ˈbɛvərɪdʒ/",
        "vi": "huân tước William Beveridge Anh",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043742",
        "hw": "frederic francois chopin",
        "pos": "phrase",
        "ipa": "/frɛdəˈriːk frɑːnˈswɑː ʃoʊˈpæ̃/",
        "vi": "nhà soạn nhạc vĩ đại Chopin",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043743",
        "hw": "genus anas",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs ˈeɪnæs/",
        "vi": "chi vịt trời chim nước họ Vịt",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043744",
        "hw": "genus bacillus",
        "pos": "phrase",
        "ipa": "/ˈdʒiːnəs bəˈsɪləs/",
        "vi": "chi trực khuẩn hiếu khí Bacillus",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043745",
        "hw": "gianni versace",
        "pos": "phrase",
        "ipa": "/ˈdʒɑːni vərˈsɑːtʃi/",
        "vi": "nhà thiết kế thời trang Versace",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043746",
        "hw": "gilbert keith chesterton",
        "pos": "phrase",
        "ipa": "/ˈɡɪlbərt kiːθ ˈtʃɛstərtən/",
        "vi": "nhà văn G. K. Chesterton nước Anh",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043747",
        "hw": "glade fern",
        "pos": "phrase",
        "ipa": "/ɡleɪd fɜːrn/",
        "vi": "loài dương xỉ đồng cỏ ngập nước",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043748",
        "hw": "goofing off",
        "pos": "phrase",
        "ipa": "/ˈɡuːfɪŋ ɔːf/",
        "vi": "lêu lổng; lười biếng trốn việc",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043749",
        "hw": "gustav mahler",
        "pos": "phrase",
        "ipa": "/ˈɡʊstɑːv ˈmɑːlər/",
        "vi": "nhà soạn nhạc Gustav Mahler Áo",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043750",
        "hw": "hammerhead shark",
        "pos": "phrase",
        "ipa": "/ˈhæmərhɛd ʃɑːrk/",
        "vi": "cá mập đầu búa săn mồi đại dương",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043751",
        "hw": "jean baptiste racine",
        "pos": "phrase",
        "ipa": "/ʒɑ̃ː bɑːˈtiːst ræˈsiːn/",
        "vi": "nhà soạn kịch Jean Racine Pháp",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043752",
        "hw": "jeremy bentham",
        "pos": "phrase",
        "ipa": "/ˈdʒɛrəmi ˈbɛnθəm/",
        "vi": "triết gia vị lợi Jeremy Bentham",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043753",
        "hw": "john singleton copley",
        "pos": "phrase",
        "ipa": "/dʒɑːn ˈsɪŋɡltən ˈkɑːpli/",
        "vi": "họa sĩ Mỹ John Singleton Copley",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043754",
        "hw": "knee breeches",
        "pos": "phrase",
        "ipa": "/ˈniː brɪtʃɪz/",
        "vi": "quần lửng dài đến gối thời xưa",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043755",
        "hw": "kodiak bear",
        "pos": "phrase",
        "ipa": "/ˈkoʊdiæk bɛr/",
        "vi": "loài gấu nâu khổng lồ Kodiak",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043756",
        "hw": "kodiak island",
        "pos": "phrase",
        "ipa": "/ˈkoʊdiæk ˈaɪlənd/",
        "vi": "hòn đảo Kodiak lớn ngoài Alaska",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043757",
        "hw": "leeward side",
        "pos": "phrase",
        "ipa": "/ˈliːwərd saɪd/",
        "vi": "phía khuất gió; mặt tránh gió",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043758",
        "hw": "lentil plant",
        "pos": "phrase",
        "ipa": "/ˈlɛntl plænt/",
        "vi": "cây đậu lăng quả dẹt giàu đạm",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043759",
        "hw": "ludwig wittgenstein",
        "pos": "phrase",
        "ipa": "/ˈlʊdvɪɡ ˈvɪtɡənʃtaɪn/",
        "vi": "triết gia Ludwig Wittgenstein Áo",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043760",
        "hw": "magnesium bicarbonate",
        "pos": "phrase",
        "ipa": "/mæɡˈniːziəm baɪˈkɑːrbənət/",
        "vi": "hóa chất magie bicacbonat",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043761",
        "hw": "mark tobey",
        "pos": "phrase",
        "ipa": "/mɑːrk ˈtoʊbi/",
        "vi": "họa sĩ trừu tượng Mỹ Mark Tobey",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043762",
        "hw": "marten cat",
        "pos": "phrase",
        "ipa": "/ˈmɑːrtn kæt/",
        "vi": "chồn macten rừng thông Bắc Cực",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043763",
        "hw": "michel ney",
        "pos": "phrase",
        "ipa": "/miːˈʃɛl neɪ/",
        "vi": "thống chế quân đội Pháp Michel Ney",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043764",
        "hw": "mount vesuvius",
        "pos": "phrase",
        "ipa": "/maʊnt vəˈsuːviəs/",
        "vi": "núi lửa Vesuvius nổi tiếng ở Ý",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043765",
        "hw": "mud plantain",
        "pos": "phrase",
        "ipa": "/mʌd ˈplæntɪn/",
        "vi": "cây rau mác bùn; cây cỏ bùn mác",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043766",
        "hw": "narrow wale",
        "pos": "phrase",
        "ipa": "/ˈnæroʊ weɪl/",
        "vi": "chất liệu vải nhung gân hẹp tăm",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043767",
        "hw": "nettle rash",
        "pos": "phrase",
        "ipa": "/ˈnɛtl ræʃ/",
        "vi": "bệnh mề đay; chứng dị ứng mẩn ngứa",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043768",
        "hw": "new zealand honeysuckle",
        "pos": "phrase",
        "ipa": "/nuː ˈziːlənd ˈhʌnisʌkl/",
        "vi": "cây kim ngân hoa New Zealand",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043769",
        "hw": "nonverbal intelligence",
        "pos": "phrase",
        "ipa": "/nɑːnˈvɜːrbl ɪnˈtɛlɪdʒəns/",
        "vi": "trí thông minh phi ngôn ngữ",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043770",
        "hw": "northrop frye",
        "pos": "phrase",
        "ipa": "/ˈnɔːrθrəp fraɪ/",
        "vi": "nhà phê bình văn học Northrop Frye",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043771",
        "hw": "nuisance abatement",
        "pos": "phrase",
        "ipa": "/ˈnuːsns əˈbeɪtmənt/",
        "vi": "xử lý phiền toái; giải tỏa ô nhiễm",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043772",
        "hw": "ordovician period",
        "pos": "phrase",
        "ipa": "/ˌɔːrdəˈvɪʃən ˈpɪriəd/",
        "vi": "kỷ Ooc-đô-vic cổ sinh địa chất",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043773",
        "hw": "otter shrew",
        "pos": "phrase",
        "ipa": "/ˈɑːtər ʃruː/",
        "vi": "chuột chù rái cá bơi lội châu Phi",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043774",
        "hw": "pacific sardine",
        "pos": "phrase",
        "ipa": "/pəˈsɪfɪk sɑːrˈdiːn/",
        "vi": "loài cá mòi Thái Bình Dương",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043775",
        "hw": "pansy orchid",
        "pos": "phrase",
        "ipa": "/ˈpænzi ˈɔːrkɪd/",
        "vi": "loài lan păng-xê nhiều màu sắc",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043776",
        "hw": "past participle",
        "pos": "phrase",
        "ipa": "/pæst ˈpɑːrtɪsɪpl/",
        "vi": "quá khứ phân từ; động từ cột ba",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043777",
        "hw": "perfect participle",
        "pos": "phrase",
        "ipa": "/ˈpɜːrfɪkt ˈpɑːrtɪsɪpl/",
        "vi": "phân từ hoàn thành trong ngữ pháp",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043778",
        "hw": "phallic phase",
        "pos": "phrase",
        "ipa": "/ˈfælɪk feɪz/",
        "vi": "giai đoạn phát triển tâm tính dục",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043779",
        "hw": "phallic stage",
        "pos": "phrase",
        "ipa": "/ˈfælɪk steɪdʒ/",
        "vi": "thời kỳ phát triển tâm lý tính dục",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043780",
        "hw": "pina cloth",
        "pos": "phrase",
        "ipa": "/ˈpiːnjə klɔːθ/",
        "vi": "vải sợi tơ dứa piña Philippines",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043781",
        "hw": "pocketbook issue",
        "pos": "phrase",
        "ipa": "/ˈpɑːkɪtbʊk ˈɪʃuː/",
        "vi": "vấn đề kinh tế chi tiêu thiết yếu",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043782",
        "hw": "present participle",
        "pos": "phrase",
        "ipa": "/ˈprɛznt ˈpɑːrtɪsɪpl/",
        "vi": "hiện tại phân từ; dạng đuôi -ing",
        "cefr": "A2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043783",
        "hw": "quilting bee",
        "pos": "phrase",
        "ipa": "/ˈkwɪltɪŋ biː/",
        "vi": "buổi tụ họp may vá chăn bông",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043784",
        "hw": "reindeer lichen",
        "pos": "phrase",
        "ipa": "/ˈreɪndɪr ˈlaɪkən/",
        "vi": "địa y tuần lộc vùng đài nguyên",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043785",
        "hw": "rhone river",
        "pos": "phrase",
        "ipa": "/roʊn ˈrɪvər/",
        "vi": "dòng sông Rhône lớn ở Pháp Thụy Sĩ",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043786",
        "hw": "rhone wine",
        "pos": "phrase",
        "ipa": "/roʊn waɪn/",
        "vi": "rượu vang vùng sông Rhône ở Pháp",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043787",
        "hw": "richard phillips feynman",
        "pos": "phrase",
        "ipa": "/ˈrɪtʃərd ˈfɪlɪps ˈfaɪnmən/",
        "vi": "nhà vật lý hạt Richard Feynman",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043788",
        "hw": "riding breeches",
        "pos": "phrase",
        "ipa": "/ˈraɪdɪŋ brɪtʃɪz/",
        "vi": "chiếc quần chuyên dụng cưỡi ngựa",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043789",
        "hw": "rio nunez coffee",
        "pos": "phrase",
        "ipa": "/ˈriːoʊ ˈnuːnjɛz ˈkɔːfi/",
        "vi": "giống cà phê hoang dã Rio Nunez",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043790",
        "hw": "saint bede",
        "pos": "phrase",
        "ipa": "/seɪnt biːd/",
        "vi": "thánh Bede nhà sử học nước Anh",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043791",
        "hw": "sardine oil",
        "pos": "phrase",
        "ipa": "/sɑːrˈdiːn ɔɪl/",
        "vi": "dầu chiết xuất từ cá mòi tự nhiên",
        "cefr": "C1",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043792",
        "hw": "scuffle hoe",
        "pos": "phrase",
        "ipa": "/ˈskʌfl hoʊ/",
        "vi": "chiếc cuốc xới làm cỏ hai lưỡi đẩy",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043793",
        "hw": "sedimentation rate",
        "pos": "phrase",
        "ipa": "/ˌsɛdɪmɛnˈteɪʃən reɪt/",
        "vi": "tốc độ lắng hồng cầu trong y học",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043794",
        "hw": "snorkel diving",
        "pos": "phrase",
        "ipa": "/ˈsnɔːrkl ˈdaɪvɪŋ/",
        "vi": "môn lặn nông có ống thở trên biển",
        "cefr": "B1",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043795",
        "hw": "spiel off",
        "pos": "phrase",
        "ipa": "/ʃpiːl ɔːf/",
        "vi": "đọc vanh vách một tràng thuộc lòng",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043796",
        "hw": "stone marten",
        "pos": "phrase",
        "ipa": "/stoʊn ˈmɑːrtn/",
        "vi": "loài chồn đá chân sồi châu Âu",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043797",
        "hw": "thermonuclear bomb",
        "pos": "phrase",
        "ipa": "/ˌθɜːrmoʊˈnuːkliər bɑːm/",
        "vi": "bom khinh khí; quả bom nhiệt hạch",
        "cefr": "C1",
        "tier": "advanced",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043798",
        "hw": "to leeward",
        "pos": "phrase",
        "ipa": "/tuː ˈliːwərd/",
        "vi": "về phía khuất gió tàu thuyền",
        "cefr": "C2",
        "tier": "specialized",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043799",
        "hw": "wood shavings",
        "pos": "phrase",
        "ipa": "/wʊd ˈʃeɪvɪŋz/",
        "vi": "dăm bào gỗ tiện; phoi bào thợ mộc",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043800",
        "hw": "agnostics",
        "pos": "noun",
        "ipa": "/æɡˈnɑːstɪks/",
        "vi": "những người theo thuyết bất khả tri",
        "cefr": "B2",
        "tier": "general",
        "status": "reviewed",
        "notes": None
    },
    {
        "id": "lex.en.200k.043801",
        "hw": "algierses",
        "pos": "noun",
        "ipa": "/ælˈdʒɪrzɪz/",
        "vi": "các khu đô thị Algiers ở Algérie",
        "cefr": "C2",
        "tier": "rare",
        "status": "reviewed",
        "notes": None
    }
]

# Validation
with open('scratch/b29_r08_raw_p3.json') as f:
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

with open('scratch/b29_r08_p3.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 8 Part 3 verified and written successfully.")
