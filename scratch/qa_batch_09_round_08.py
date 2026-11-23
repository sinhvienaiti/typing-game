# Batch 09 Round 8 Manual QA overrides (records 3500-3999, IDs 043502-044001)
import json

OVERRIDES_PART1 = {
    "lex.en.100k.043502": {
        "hw": "castanea",
        "pos": "noun",
        "vi": "chi cây dẻ hạt Castanea dẻ gai",
        "ipa": "/kæˈsteɪniə/"
    },
    "lex.en.100k.043503": {
        "hw": "cauterization",
        "pos": "noun",
        "vi": "thủ thuật đốt mô cầm máu khử khuẩn",
        "ipa": "/ˌkɔːtərəˈzeɪʃən/"
    },
    "lex.en.100k.043504": {
        "hw": "ceramicist",
        "pos": "noun",
        "vi": "nghệ nhân gốm sứ mỹ nghệ",
        "ipa": "/səˈræmɪsɪst/"
    },
    "lex.en.100k.043505": {
        "hw": "charolais",
        "pos": "noun",
        "vi": "giống bò thịt Charolais Pháp",
        "ipa": "/ˈʃærəleɪ/"
    },
    "lex.en.100k.043506": {
        "hw": "chthonic",
        "pos": "adj",
        "vi": "thuộc lòng đất; thuộc âm phủ",
        "ipa": "/ˈθɑːnɪk/"
    },
    "lex.en.100k.043507": {
        "hw": "clubby",
        "pos": "adj",
        "vi": "thân mật nội bộ; khép kín bè phái",
        "ipa": "/ˈklʌbi/"
    },
    "lex.en.100k.043508": {
        "hw": "cockamamie",
        "pos": "adj",
        "vi": "lố bịch quái đản; ngớ ngẩn khó tin",
        "ipa": "/ˈkɑːkəmeɪmi/"
    },
    "lex.en.100k.043509": {
        "hw": "coeducation",
        "pos": "noun",
        "vi": "nền giáo dục chung nam và nữ",
        "ipa": "/ˌkoʊɛdʒəˈkeɪʃən/"
    },
    "lex.en.100k.043510": {
        "hw": "coffea",
        "pos": "noun",
        "vi": "chi cây cà phê hạt Coffea",
        "ipa": "/ˈkɑːfiə/"
    },
    "lex.en.100k.043511": {
        "hw": "comradery",
        "pos": "noun",
        "vi": "tình đồng đội gắn bó keo sơn",
        "ipa": "/ˌkɑːmˈrædəri/"
    },
    "lex.en.100k.043512": {
        "hw": "concupiscence",
        "pos": "noun",
        "vi": "dục vọng nhục dục xác thịt",
        "ipa": "/kɑːnˈkjuːpɪsəns/"
    },
    "lex.en.100k.043513": {
        "hw": "condemnatory",
        "pos": "adj",
        "vi": "mang tính lên án; kết tội chỉ trích",
        "ipa": "/kənˈdɛmnətɔːri/"
    },
    "lex.en.100k.043514": {
        "hw": "contradistinction",
        "pos": "noun",
        "vi": "sự đối lập tương phản rõ rệt",
        "ipa": "/ˌkɑːntrədɪˈstɪŋkʃən/"
    },
    "lex.en.100k.043515": {
        "hw": "copt",
        "pos": "noun",
        "vi": "người Cơ Đốc Copt Ai Cập cổ",
        "ipa": "/kɑːpt/"
    },
    "lex.en.100k.043516": {
        "hw": "cotyledon",
        "pos": "noun",
        "vi": "lá mầm đầu tiên của hạt phôi",
        "ipa": "/ˌkɑːtəˈliːdən/"
    },
    "lex.en.100k.043517": {
        "hw": "crudity",
        "pos": "noun",
        "vi": "tính chất thô thiển; sự sơ sài",
        "ipa": "/ˈkruːdəti/"
    },
    "lex.en.100k.043518": {
        "hw": "dabbler",
        "pos": "noun",
        "vi": "người học đòi; kẻ làm việc tài tử",
        "ipa": "/ˈdæblɚ/"
    },
    "lex.en.100k.043519": {
        "hw": "dagestani",
        "pos": "noun",
        "vi": "người dân vùng Dagestan Kavkaz",
        "ipa": "/ˌdæɡɪˈstæni/"
    },
    "lex.en.100k.043520": {
        "hw": "debauch",
        "pos": "noun",
        "vi": "cuộc chè chén trụy lạc say sưa",
        "ipa": "/dɪˈbɔːtʃ/"
    },
    "lex.en.100k.043521": {
        "hw": "debilitate",
        "pos": "verb",
        "vi": "làm suy yếu; làm kiệt quệ cơ thể",
        "ipa": "/dɪˈbɪlɪteɪt/"
    },
    "lex.en.100k.043522": {
        "hw": "decapod",
        "pos": "noun",
        "vi": "giáp xác mười chân như tôm cua",
        "ipa": "/ˈdɛkəpɑːd/"
    },
    "lex.en.100k.043523": {
        "hw": "dejectedly",
        "pos": "adv",
        "vi": "một cách chán nản ủ rũ rầu rĩ",
        "ipa": "/dɪˈdʒɛktɪdli/"
    },
    "lex.en.100k.043524": {
        "hw": "demonstratively",
        "pos": "adv",
        "vi": "một cách biểu cảm sôi nổi bộc lộ",
        "ipa": "/dɪˈmɑːnstrətɪvli/"
    },
    "lex.en.100k.043525": {
        "hw": "deportee",
        "pos": "noun",
        "vi": "người bị trục xuất đuổi khỏi nước",
        "ipa": "/ˌdiːpɔːrˈtiː/"
    },
    "lex.en.100k.043526": {
        "hw": "diltiazem",
        "pos": "noun",
        "vi": "thuốc hạ huyết áp diltiazem tim",
        "ipa": "/dɪlˈtaɪəzɛm/"
    },
    "lex.en.100k.043527": {
        "hw": "dolorous",
        "pos": "adj",
        "vi": "đau thương bi ai; buồn rầu sầu muộn",
        "ipa": "/ˈdoʊlərəs/"
    },
    "lex.en.100k.043528": {
        "hw": "dragger",
        "pos": "noun",
        "vi": "tàu kéo lưới cào vét đáy biển",
        "ipa": "/ˈdræɡɚ/"
    },
    "lex.en.100k.043529": {
        "hw": "dramatise",
        "pos": "verb",
        "vi": "chuyển thể kịch; làm trầm trọng hóa",
        "ipa": "/ˈdræmətaɪz/"
    },
    "lex.en.100k.043530": {
        "hw": "dreadlock",
        "pos": "noun",
        "vi": "bím tóc tết bện thừng dreadlocks",
        "ipa": "/ˈdrɛdlɑːk/"
    },
    "lex.en.100k.043531": {
        "hw": "dreadnaught",
        "pos": "noun",
        "vi": "thiết giáp hạm bọc thép cổ điển",
        "ipa": "/ˈdrɛdnɔːt/"
    },
    "lex.en.100k.043532": {
        "hw": "embezzler",
        "pos": "noun",
        "vi": "kẻ tham ô biển thủ công quỹ",
        "ipa": "/ɪmˈbɛzlɚ/"
    },
    "lex.en.100k.043533": {
        "hw": "enceinte",
        "pos": "adj",
        "vi": "đang mang thai; có bầu có thai",
        "ipa": "/ɑːnˈsæ̃t/"
    },
    "lex.en.100k.043534": {
        "hw": "epicyclic",
        "pos": "adj",
        "vi": "thuộc bánh răng hành tinh luân hồi",
        "ipa": "/ˌɛpɪˈsaɪklɪk/"
    },
    "lex.en.100k.043535": {
        "hw": "equipage",
        "pos": "noun",
        "vi": "cỗ xe ngựa lộng lẫy; đoàn tùy tùng",
        "ipa": "/ˈɛkwəpɪdʒ/"
    },
    "lex.en.100k.043536": {
        "hw": "eutrophic",
        "pos": "adj",
        "vi": "giàu dưỡng chất phú dưỡng mặt nước",
        "ipa": "/juːˈtroʊfɪk/"
    },
    "lex.en.100k.043537": {
        "hw": "expiate",
        "pos": "verb",
        "vi": "chuộc lỗi lầm; đền bù tội lỗi",
        "ipa": "/ˈɛkspieɪt/"
    },
    "lex.en.100k.043538": {
        "hw": "farad",
        "pos": "noun",
        "vi": "đơn vị đo điện dung fara",
        "ipa": "/ˈfæræd/"
    },
    "lex.en.100k.043539": {
        "hw": "finiteness",
        "pos": "noun",
        "vi": "tính chất hữu hạn có giới hạn",
        "ipa": "/ˈfaɪnaɪtnəs/"
    },
    "lex.en.100k.043540": {
        "hw": "fireclay",
        "pos": "noun",
        "vi": "đất sét chịu lửa làm gạch lò nung",
        "ipa": "/ˈfaɪərkleɪ/"
    },
    "lex.en.100k.043541": {
        "hw": "flippancy",
        "pos": "noun",
        "vi": "thái độ cợt nhả thiếu nghiêm túc",
        "ipa": "/ˈflɪpənsi/"
    },
    "lex.en.100k.043542": {
        "hw": "forthrightness",
        "pos": "noun",
        "vi": "tính bộc trực cương trực thẳng thắn",
        "ipa": "/ˈfɔːrθˌraɪtnəs/"
    },
    "lex.en.100k.043543": {
        "hw": "fulminant",
        "pos": "adj",
        "vi": "bùng phát cấp tính dữ dội bệnh học",
        "ipa": "/ˈfʌlmɪnənt/"
    },
    "lex.en.100k.043544": {
        "hw": "galangal",
        "pos": "noun",
        "vi": "củ riềng gia vị ấm vị cay",
        "ipa": "/ˈɡæləŋɡæl/"
    },
    "lex.en.100k.043545": {
        "hw": "gamin",
        "pos": "noun",
        "vi": "trẻ bụi đời lang thang đường phố",
        "ipa": "/ɡæˈmæ̃/"
    },
    "lex.en.100k.043546": {
        "hw": "gastrin",
        "pos": "noun",
        "vi": "hoóc-môn kích tiết axit dịch vị",
        "ipa": "/ˈɡæstrɪn/"
    },
    "lex.en.100k.043547": {
        "hw": "genu",
        "pos": "noun",
        "vi": "đầu gối; đoạn gập khúc khuỷu",
        "ipa": "/ˈdʒɛnuː/"
    },
    "lex.en.100k.043548": {
        "hw": "gestate",
        "pos": "verb",
        "vi": "mang thai ấp ủ; nung nấu ý tưởng",
        "ipa": "/ˈdʒɛsteɪt/"
    },
    "lex.en.100k.043549": {
        "hw": "godlessness",
        "pos": "noun",
        "vi": "sự vô thần; thói vô đạo đức",
        "ipa": "/ˈɡɑːdləsnəs/"
    },
    "lex.en.100k.043550": {
        "hw": "hargeisa",
        "pos": "noun",
        "vi": "thành phố lớn Hargeisa Somaliland",
        "ipa": "/hɑːrˈɡeɪsə/"
    },
    "lex.en.100k.043551": {
        "hw": "hassam",
        "pos": "noun",
        "vi": "họa sĩ Childe Hassam Mỹ",
        "ipa": "/ˈhæsəm/"
    },
    "lex.en.100k.043552": {
        "hw": "hauteur",
        "pos": "noun",
        "vi": "thái độ kiêu căng ngạo mạn",
        "ipa": "/oʊˈtɝː/"
    },
    "lex.en.100k.043553": {
        "hw": "haycock",
        "pos": "noun",
        "vi": "đống cỏ khô vun hình nón nhỏ",
        "ipa": "/ˈheɪkɑːk/"
    },
    "lex.en.100k.043554": {
        "hw": "heming",
        "pos": "noun",
        "vi": "viền lai áo; nếp gấp may viền",
        "ipa": "/ˈhɛmɪŋ/"
    },
    "lex.en.100k.043555": {
        "hw": "hesperides",
        "pos": "noun",
        "vi": "các tiên nữ canh vườn táo vàng",
        "ipa": "/hɛˈspɛrɪdiːz/"
    },
    "lex.en.100k.043556": {
        "hw": "heterodoxy",
        "pos": "noun",
        "vi": "quan điểm dị giáo không chính thống",
        "ipa": "/ˈhɛtərədɑːksi/"
    },
    "lex.en.100k.043557": {
        "hw": "hindoo",
        "pos": "adj",
        "vi": "thuộc Ấn Độ giáo Hindu",
        "ipa": "/ˈhɪnduː/"
    },
    "lex.en.100k.043558": {
        "hw": "hollo",
        "pos": "noun",
        "vi": "tiếng la hét gọi to từ xa",
        "ipa": "/ˈhɑːloʊ/"
    },
    "lex.en.100k.043559": {
        "hw": "hornswoggle",
        "pos": "verb",
        "vi": "lừa phỉnh gạt gẫm mánh khóe",
        "ipa": "/ˈhɔːrnˌswɑːɡəl/"
    },
    "lex.en.100k.043560": {
        "hw": "hourlong",
        "pos": "adj",
        "vi": "kéo dài trọn vẹn một giờ đồng hồ",
        "ipa": "/ˈaʊərlɔːŋ/"
    },
    "lex.en.100k.043561": {
        "hw": "hudud",
        "pos": "noun",
        "vi": "các hình phạt theo luật Sharia Hồi",
        "ipa": "/hʊˈduːd/"
    },
    "lex.en.100k.043562": {
        "hw": "hussite",
        "pos": "noun",
        "vi": "tín đồ phái cải cách Jan Hus",
        "ipa": "/ˈhʌsaɪt/"
    },
    "lex.en.100k.043563": {
        "hw": "ichor",
        "pos": "noun",
        "vi": "dòng máu bất tử của thần linh",
        "ipa": "/ˈaɪkɔːr/"
    },
    "lex.en.100k.043564": {
        "hw": "inosine",
        "pos": "noun",
        "vi": "hợp chất inosine trung gian tế bào",
        "ipa": "/ˈɪnəsiːn/"
    },
    "lex.en.100k.043565": {
        "hw": "karaites",
        "pos": "noun",
        "vi": "phái Do Thái giáo theo Kinh Torah",
        "ipa": "/ˈkærəaɪts/"
    },
    "lex.en.100k.043566": {
        "hw": "khoisan",
        "pos": "noun",
        "vi": "người hoặc ngữ tộc Khoisan Nam Phi",
        "ipa": "/ˈkɔɪsɑːn/"
    },
    "lex.en.100k.043567": {
        "hw": "killdeer",
        "pos": "noun",
        "vi": "chim choi choi killdeer châu Mỹ",
        "ipa": "/ˈkɪldɪr/"
    },
    "lex.en.100k.043568": {
        "hw": "koinonia",
        "pos": "noun",
        "vi": "sự hiệp thông trong Ki-tô giáo",
        "ipa": "/ˌkɔɪnoʊˈniːə/"
    },
    "lex.en.100k.043569": {
        "hw": "lexicographic",
        "pos": "adj",
        "vi": "thuộc việc biên soạn từ điển học",
        "ipa": "/ˌlɛksɪkəˈɡræfɪk/"
    },
    "lex.en.100k.043570": {
        "hw": "lifehack",
        "pos": "verb",
        "vi": "dùng mẹo vặt tiết kiệm thời gian",
        "ipa": "/ˈlaɪfhæk/"
    },
    "lex.en.100k.043571": {
        "hw": "lour",
        "pos": "verb",
        "vi": "nhìn trừng trừng đe dọa; trời u ám",
        "ipa": "/laʊɚ/"
    },
    "lex.en.100k.043572": {
        "hw": "macromolecule",
        "pos": "noun",
        "vi": "đại phân tử polyme sinh học lớn",
        "ipa": "/ˌmækroʊˈmɑːlɪkjuːl/"
    },
    "lex.en.100k.043573": {
        "hw": "mandrill",
        "pos": "noun",
        "vi": "loài khỉ mặt sặc sỡ Mandrill",
        "ipa": "/ˈmændrɪl/"
    },
    "lex.en.100k.043574": {
        "hw": "melanocyte",
        "pos": "noun",
        "vi": "tế bào hắc tố sinh sắc tố da",
        "ipa": "/məˈlænəsaɪt/"
    },
    "lex.en.100k.043575": {
        "hw": "monetarism",
        "pos": "noun",
        "vi": "chủ nghĩa trọng tiền tệ kinh tế",
        "ipa": "/ˈmɑːnɪtərɪzəm/"
    },
    "lex.en.100k.043576": {
        "hw": "monistic",
        "pos": "adj",
        "vi": "thuộc thuyết nhất nguyên luận triết",
        "ipa": "/moʊˈnɪstɪk/"
    },
    "lex.en.100k.043577": {
        "hw": "narrowboat",
        "pos": "noun",
        "vi": "thuyền hẹp đi kênh rạch nước Anh",
        "ipa": "/ˈnæroʊboʊt/"
    },
    "lex.en.100k.043578": {
        "hw": "naze",
        "pos": "noun",
        "vi": "mũi đất nhô ra biển vách đá",
        "ipa": "/neɪz/"
    },
    "lex.en.100k.043579": {
        "hw": "nearsightedness",
        "pos": "noun",
        "vi": "tật cận thị mắt nhìn xa mờ",
        "ipa": "/ˌnɪrˈsaɪtɪdnəs/"
    },
    "lex.en.100k.043580": {
        "hw": "nicety",
        "pos": "noun",
        "vi": "chi tiết tinh tế; phép xã giao nhỏ",
        "ipa": "/ˈnaɪsəti/"
    },
    "lex.en.100k.043581": {
        "hw": "nimbleness",
        "pos": "noun",
        "vi": "sự nhanh nhẹn hoạt bát thoăn thoắt",
        "ipa": "/ˈnɪmbəlnəs/"
    },
    "lex.en.100k.043582": {
        "hw": "nonrenewable",
        "pos": "adj",
        "vi": "không thể tái tạo cạn kiệt dần",
        "ipa": "/ˌnɑːnrɪˈnuːəbəl/"
    },
    "lex.en.100k.043583": {
        "hw": "oarsman",
        "pos": "noun",
        "vi": "tay chèo thuyền thể thao bắt cá",
        "ipa": "/ˈɔːrzmən/"
    },
    "lex.en.100k.043584": {
        "hw": "oast",
        "pos": "noun",
        "vi": "lò sấy khô hoa bia làm bia",
        "ipa": "/oʊst/"
    },
    "lex.en.100k.043585": {
        "hw": "oleoresin",
        "pos": "noun",
        "vi": "hỗn hợp nhựa dầu tự nhiên",
        "ipa": "/ˌoʊlioʊˈrɛzɪn/"
    },
    "lex.en.100k.043586": {
        "hw": "orchiectomy",
        "pos": "noun",
        "vi": "phẫu thuật cắt bỏ tinh hoàn y khoa",
        "ipa": "/ˌɔːrkiˈɛktəmi/"
    },
    "lex.en.100k.043587": {
        "hw": "overleaf",
        "pos": "adv",
        "vi": "ở mặt sau trang giấy; trang kế",
        "ipa": "/ˌoʊvɚˈliːf/"
    },
    "lex.en.100k.043588": {
        "hw": "padrone",
        "pos": "noun",
        "vi": "ông chủ cai thầu; chủ nhà trọ Ý",
        "ipa": "/pəˈdroʊneɪ/"
    },
    "lex.en.100k.043589": {
        "hw": "pasch",
        "pos": "noun",
        "vi": "Lễ Vượt Qua của người Do Thái",
        "ipa": "/pæsk/"
    },
    "lex.en.100k.043590": {
        "hw": "pemphigus",
        "pos": "noun",
        "vi": "bệnh bọng nước tự miễn pemphigus",
        "ipa": "/ˈpɛmfɪɡəs/"
    },
    "lex.en.100k.043591": {
        "hw": "penetrable",
        "pos": "adj",
        "vi": "có thể xuyên qua thấm qua được",
        "ipa": "/ˈpɛnɪtrəbəl/"
    },
    "lex.en.100k.043592": {
        "hw": "peremptorily",
        "pos": "adv",
        "vi": "một cách độc đoán dứt khoát",
        "ipa": "/pəˈrɛmptərəli/"
    },
    "lex.en.100k.043593": {
        "hw": "periphrastic",
        "pos": "adj",
        "vi": "dài dòng vòng vo theo lối gián tiếp",
        "ipa": "/ˌpɛrɪˈfræstɪk/"
    },
    "lex.en.100k.043594": {
        "hw": "perspicacious",
        "pos": "adj",
        "vi": "sáng suốt sâu sắc có óc nhận xét",
        "ipa": "/ˌpɝːspɪˈkeɪʃəs/"
    },
    "lex.en.100k.043595": {
        "hw": "petulantly",
        "pos": "adv",
        "vi": "một cách hờn dỗi cáu kỉnh",
        "ipa": "/ˈpɛtʃələntli/"
    },
    "lex.en.100k.043596": {
        "hw": "phanerozoic",
        "pos": "noun",
        "vi": "đại Hiển sinh trong địa chất học",
        "ipa": "/ˌfænərəˈzoʊɪk/"
    },
    "lex.en.100k.043597": {
        "hw": "philatelist",
        "pos": "noun",
        "vi": "người sưu tầm tem bưu chính",
        "ipa": "/fɪˈlætəlɪst/"
    },
    "lex.en.100k.043598": {
        "hw": "photocell",
        "pos": "noun",
        "vi": "tế bào quang điện cảm biến ánh sáng",
        "ipa": "/ˈfoʊtoʊsɛl/"
    },
    "lex.en.100k.043599": {
        "hw": "pictograph",
        "pos": "noun",
        "vi": "chữ tượng hình; biểu đồ tranh ảnh",
        "ipa": "/ˈpɪktəɡræf/"
    },
    "lex.en.100k.043600": {
        "hw": "pommy",
        "pos": "noun",
        "vi": "người Anh từ lóng của người Úc",
        "ipa": "/ˈpɑːmi/"
    },
    "lex.en.100k.043601": {
        "hw": "positioner",
        "pos": "noun",
        "vi": "bộ định vị thiết bị đặt vị trí",
        "ipa": "/pəˈzɪʃənɚ/"
    }
}

OVERRIDES_PART2 = {
    "lex.en.100k.043602": {
        "hw": "potbellied",
        "pos": "adj",
        "vi": "bụng bự phệ bụng; tròn ủng",
        "ipa": "/ˈpɑːtˌbɛlid/"
    },
    "lex.en.100k.043603": {
        "hw": "preparative",
        "pos": "adj",
        "vi": "có tính chuẩn bị dự bị sẵn sàng",
        "ipa": "/prɪˈpærətɪv/"
    },
    "lex.en.100k.043604": {
        "hw": "prickling",
        "pos": "noun",
        "vi": "cảm giác râm ran như kim châm",
        "ipa": "/ˈprɪklɪŋ/"
    },
    "lex.en.100k.043605": {
        "hw": "promiscuously",
        "pos": "adv",
        "vi": "một cách bừa bãi lăng nhăng hỗn độn",
        "ipa": "/prəˈmɪskjuəsli/"
    },
    "lex.en.100k.043606": {
        "hw": "railroader",
        "pos": "noun",
        "vi": "nhân viên ngành đường sắt xe lửa",
        "ipa": "/ˈreɪlˌroʊdɚ/"
    },
    "lex.en.100k.043607": {
        "hw": "recusant",
        "pos": "adj",
        "vi": "bất phục tùng quốc giáo Anh",
        "ipa": "/ˈrɛkjəzənt/"
    },
    "lex.en.100k.043608": {
        "hw": "redshank",
        "pos": "noun",
        "vi": "loài chim choắt chân đỏ ven bờ",
        "ipa": "/ˈrɛdʃæŋk/"
    },
    "lex.en.100k.043609": {
        "hw": "reflexed",
        "pos": "adj",
        "vi": "uốn cong quặp ngược xuống",
        "ipa": "/rɪˈflɛkst/"
    },
    "lex.en.100k.043610": {
        "hw": "reverberant",
        "pos": "adj",
        "vi": "vang dội âm vang dội lại",
        "ipa": "/rɪˈvɝːbərənt/"
    },
    "lex.en.100k.043611": {
        "hw": "rostand",
        "pos": "noun",
        "vi": "nhà viết kịch Edmond Rostand Pháp",
        "ipa": "/rɔːˈstɑːn/"
    },
    "lex.en.100k.043612": {
        "hw": "rotenone",
        "pos": "noun",
        "vi": "chất trừ sâu tự nhiên rotenone",
        "ipa": "/ˈroʊtənoʊn/"
    },
    "lex.en.100k.043613": {
        "hw": "sabaton",
        "pos": "noun",
        "vi": "giáp sắt bảo vệ bàn chân kỵ sĩ",
        "ipa": "/ˈsæbətɑːn/"
    },
    "lex.en.100k.043614": {
        "hw": "salesgirl",
        "pos": "noun",
        "vi": "nữ nhân viên bán hàng cửa tiệm",
        "ipa": "/ˈseɪlzɡɝːl/"
    },
    "lex.en.100k.043615": {
        "hw": "schonberg",
        "pos": "noun",
        "vi": "nhà soạn nhạc Arnold Schoenberg Áo",
        "ipa": "/ˈʃøːnbɛrk/"
    },
    "lex.en.100k.043616": {
        "hw": "seclude",
        "pos": "verb",
        "vi": "tách biệt cô lập khỏi bên ngoài",
        "ipa": "/sɪˈkluːd/"
    },
    "lex.en.100k.043617": {
        "hw": "sensitised",
        "pos": "adj",
        "vi": "được làm cho nhạy cảm; mẫn cảm",
        "ipa": "/ˈsɛnsɪtaɪzd/"
    },
    "lex.en.100k.043618": {
        "hw": "sexpot",
        "pos": "noun",
        "vi": "phụ nữ cực kỳ quyến rũ gợi tình",
        "ipa": "/ˈsɛkspɑːt/"
    },
    "lex.en.100k.043619": {
        "hw": "shoveler",
        "pos": "noun",
        "vi": "người xúc xẻng; loài vịt mỏ thìa",
        "ipa": "/ˈʃʌvəlɚ/"
    },
    "lex.en.100k.043620": {
        "hw": "silenus",
        "pos": "noun",
        "vi": "thần đồng hành say xỉn Silenus",
        "ipa": "/saɪˈliːnəs/"
    },
    "lex.en.100k.043621": {
        "hw": "skanda",
        "pos": "noun",
        "vi": "thần chiến tranh Skanda Ấn Độ giáo",
        "ipa": "/ˈskʌndə/"
    },
    "lex.en.100k.043622": {
        "hw": "sourpuss",
        "pos": "noun",
        "vi": "kẻ hay càu nhàu cau có gắt gỏng",
        "ipa": "/ˈsaʊərpʊs/"
    },
    "lex.en.100k.043623": {
        "hw": "spallation",
        "pos": "noun",
        "vi": "sự vỡ vụn hạt nhân tán xạ phân mảnh",
        "ipa": "/spɔːˈleɪʃən/"
    },
    "lex.en.100k.043624": {
        "hw": "sporulation",
        "pos": "noun",
        "vi": "quá trình hình thành bào tử",
        "ipa": "/ˌspɔːrjəˈleɪʃən/"
    },
    "lex.en.100k.043625": {
        "hw": "staleness",
        "pos": "noun",
        "vi": "sự ôi thiu; tính cũ kỹ nhàm chán",
        "ipa": "/ˈsteɪlnəs/"
    },
    "lex.en.100k.043626": {
        "hw": "suasion",
        "pos": "noun",
        "vi": "sự khuyên nhủ thuyết phục êm dịu",
        "ipa": "/ˈsweɪʒən/"
    },
    "lex.en.100k.043627": {
        "hw": "suburbanite",
        "pos": "noun",
        "vi": "cư dân sống tại khu ngoại ô",
        "ipa": "/səˈbɝːbənaɪt/"
    },
    "lex.en.100k.043628": {
        "hw": "succotash",
        "pos": "noun",
        "vi": "món ngô xào đậu succotash Mỹ",
        "ipa": "/ˈsʌkətæʃ/"
    },
    "lex.en.100k.043629": {
        "hw": "sumptuary",
        "pos": "adj",
        "vi": "nhằm hạn chế chi tiêu xa hoa",
        "ipa": "/ˈsʌmptʃuɛri/"
    },
    "lex.en.100k.043630": {
        "hw": "sweatband",
        "pos": "noun",
        "vi": "băng thun đeo trán thấm mồ hôi",
        "ipa": "/ˈswɛtbænd/"
    },
    "lex.en.100k.043631": {
        "hw": "tamarindo",
        "pos": "noun",
        "vi": "nước giải khát quả me nhiệt đới",
        "ipa": "/ˌtæməˈrɪndoʊ/"
    },
    "lex.en.100k.043632": {
        "hw": "taxus",
        "pos": "noun",
        "vi": "chi cây thông đỏ Taxus lấy gỗ quý",
        "ipa": "/ˈtæksəs/"
    },
    "lex.en.100k.043633": {
        "hw": "terete",
        "pos": "adj",
        "vi": "có thân hình trụ tròn nhẵn thon",
        "ipa": "/təˈriːt/"
    },
    "lex.en.100k.043634": {
        "hw": "threepence",
        "pos": "noun",
        "vi": "đồng tiền xu ba xu cũ của Anh",
        "ipa": "/ˈθrɪpəns/"
    },
    "lex.en.100k.043635": {
        "hw": "threescore",
        "pos": "num",
        "vi": "sáu mươi; ba lần hai mươi; 60",
        "ipa": "/ˈθriːskɔːr/"
    },
    "lex.en.100k.043636": {
        "hw": "thrombolytic",
        "pos": "noun",
        "vi": "thuốc làm tan huyết khối đông",
        "ipa": "/ˌθrɑːmboʊˈlɪtɪk/"
    },
    "lex.en.100k.043637": {
        "hw": "tike",
        "pos": "noun",
        "vi": "đứa bé hiếu động; cậu nhóc nghịch",
        "ipa": "/taɪk/"
    },
    "lex.en.100k.043638": {
        "hw": "tinpot",
        "pos": "adj",
        "vi": "tầm thường xoàng xĩnh quyền rơm",
        "ipa": "/ˈtɪnpɑːt/"
    },
    "lex.en.100k.043639": {
        "hw": "triskelion",
        "pos": "noun",
        "vi": "biểu tượng ba chân uốn cong tỏa ra",
        "ipa": "/traɪˈskɛliən/"
    },
    "lex.en.100k.043640": {
        "hw": "typewriting",
        "pos": "noun",
        "vi": "kỹ thuật đánh máy; bản thảo máy",
        "ipa": "/ˈtaɪpˌraɪtɪŋ/"
    },
    "lex.en.100k.043641": {
        "hw": "ubiquinone",
        "pos": "noun",
        "vi": "coenzym Q10 bổ trợ tế bào",
        "ipa": "/juːˈbɪkwɪnoʊn/"
    },
    "lex.en.100k.043642": {
        "hw": "uncaused",
        "pos": "adj",
        "vi": "tự nhiên không bởi nguyên nhân nào",
        "ipa": "/ʌnˈkɔːzd/"
    },
    "lex.en.100k.043643": {
        "hw": "uncial",
        "pos": "adj",
        "vi": "viết theo kiểu chữ in hoa tròn cổ",
        "ipa": "/ˈʌnʃəl/"
    },
    "lex.en.100k.043644": {
        "hw": "undependable",
        "pos": "adj",
        "vi": "thất thường không đáng tin cậy",
        "ipa": "/ˌʌndɪˈpɛndəbəl/"
    },
    "lex.en.100k.043645": {
        "hw": "undereducated",
        "pos": "adj",
        "vi": "thất học; học vấn không đầy đủ",
        "ipa": "/ˌʌndɚˈɛdʒəkeɪtɪd/"
    },
    "lex.en.100k.043646": {
        "hw": "undershot",
        "pos": "adj",
        "vi": "có hàm dưới nhô ra phía trước",
        "ipa": "/ˈʌndɚʃɑːt/"
    },
    "lex.en.100k.043647": {
        "hw": "unengaged",
        "pos": "adj",
        "vi": "rảnh rỗi thanh thản; chưa đính hôn",
        "ipa": "/ˌʌnɪnˈɡeɪdʒd/"
    },
    "lex.en.100k.043648": {
        "hw": "unio",
        "pos": "noun",
        "vi": "chi trai sông nước ngọt Unio",
        "ipa": "/ˈjuːnioʊ/"
    },
    "lex.en.100k.043649": {
        "hw": "unreasoning",
        "pos": "adj",
        "vi": "mù quáng không nghe theo lý trí",
        "ipa": "/ʌnˈriːzənɪŋ/"
    },
    "lex.en.100k.043650": {
        "hw": "unremarked",
        "pos": "adj",
        "vi": "không được để ý; không ai nhắc tới",
        "ipa": "/ˌʌnrɪˈmɑːrkt/"
    },
    "lex.en.100k.043651": {
        "hw": "unshared",
        "pos": "adj",
        "vi": "không chia sẻ cùng ai; sở hữu riêng",
        "ipa": "/ʌnˈʃɛrd/"
    },
    "lex.en.100k.043652": {
        "hw": "untracked",
        "pos": "adj",
        "vi": "chưa có dấu chân người khai phá",
        "ipa": "/ʌnˈtrækt/"
    },
    "lex.en.100k.043653": {
        "hw": "untrammelled",
        "pos": "adj",
        "vi": "không bị ràng buộc kiềm tỏa tự do",
        "ipa": "/ʌnˈtræməld/"
    },
    "lex.en.100k.043654": {
        "hw": "usurer",
        "pos": "noun",
        "vi": "kẻ cho vay nặng lãi bóc lột",
        "ipa": "/ˈjuːʒərɚ/"
    },
    "lex.en.100k.043655": {
        "hw": "vaginitis",
        "pos": "noun",
        "vi": "chứng viêm nhiễm niêm mạc âm đạo",
        "ipa": "/ˌvædʒəˈnaɪtɪs/"
    },
    "lex.en.100k.043656": {
        "hw": "variate",
        "pos": "noun",
        "vi": "biến số ngẫu nhiên trong thống kê",
        "ipa": "/ˈvɛriət/"
    },
    "lex.en.100k.043657": {
        "hw": "ventilatory",
        "pos": "adj",
        "vi": "thuộc chức năng thông khí hô hấp",
        "ipa": "/ˈvɛntɪlətɔːri/"
    },
    "lex.en.100k.043658": {
        "hw": "walloons",
        "pos": "noun",
        "vi": "người Walloon vùng nam nước Bỉ",
        "ipa": "/wɑːˈluːnz/"
    },
    "lex.en.100k.043659": {
        "hw": "washtub",
        "pos": "noun",
        "vi": "chậu giặt giũ đồ bằng kim loại gỗ",
        "ipa": "/ˈwɑːʃtʌb/"
    },
    "lex.en.100k.043660": {
        "hw": "widgeon",
        "pos": "noun",
        "vi": "vịt đầu hung hoang dã wigeon",
        "ipa": "/ˈwɪdʒən/"
    },
    "lex.en.100k.043661": {
        "hw": "wimple",
        "pos": "noun",
        "vi": "khăn trùm đầu cổ của nữ tu sĩ xưa",
        "ipa": "/ˈwɪmpəl/"
    },
    "lex.en.100k.043662": {
        "hw": "yakut",
        "pos": "noun",
        "vi": "người hoặc tiếng Yakut Siberia",
        "ipa": "/jəˈkʊt/"
    },
    "lex.en.100k.043663": {
        "hw": "abadan",
        "pos": "noun",
        "vi": "thành phố cảng Abadan của Iran",
        "ipa": "/ˌɑːbɑːˈdɑːn/"
    },
    "lex.en.100k.043664": {
        "hw": "abrade",
        "pos": "verb",
        "vi": "mài mòn bề mặt; làm trầy xước da",
        "ipa": "/əˈbreɪd/"
    },
    "lex.en.100k.043665": {
        "hw": "acrolein",
        "pos": "noun",
        "vi": "chất lỏng độc bay hơi acrolein",
        "ipa": "/əˈkroʊliɪn/"
    },
    "lex.en.100k.043666": {
        "hw": "addle",
        "pos": "verb",
        "vi": "làm rối trí mù mẫm; làm trứng ung",
        "ipa": "/ˈædəl/"
    },
    "lex.en.100k.043667": {
        "hw": "aerialist",
        "pos": "noun",
        "vi": "diễn viên xiếc đu dây nhào lộn cao",
        "ipa": "/ˈɛriəlɪst/"
    },
    "lex.en.100k.043668": {
        "hw": "airburst",
        "pos": "noun",
        "vi": "vụ nổ bom đạn pháo trên không trung",
        "ipa": "/ˈɛrbɝːst/"
    },
    "lex.en.100k.043669": {
        "hw": "alnico",
        "pos": "noun",
        "vi": "hợp kim từ vĩnh cửu alnico",
        "ipa": "/ˈælnɪkoʊ/"
    },
    "lex.en.100k.043670": {
        "hw": "anthropometry",
        "pos": "noun",
        "vi": "nhân trắc học đo kích thước người",
        "ipa": "/ˌænθrəˈpɑːmətri/"
    },
    "lex.en.100k.043671": {
        "hw": "anticyclone",
        "pos": "noun",
        "vi": "xoáy nghịch khí áp cao trời quang",
        "ipa": "/ˌæntiˈsaɪkloʊn/"
    },
    "lex.en.100k.043672": {
        "hw": "aquitania",
        "pos": "noun",
        "vi": "vùng Aquitaine lịch sử Pháp",
        "ipa": "/ˌækwɪˈteɪniə/"
    },
    "lex.en.100k.043673": {
        "hw": "armiger",
        "pos": "noun",
        "vi": "người có quyền mang huy hiệu quý",
        "ipa": "/ˈɑːrmɪdʒɚ/"
    },
    "lex.en.100k.043674": {
        "hw": "arrogate",
        "pos": "verb",
        "vi": "tự tiện chiếm quyền trái phép",
        "ipa": "/ˈærəɡeɪt/"
    },
    "lex.en.100k.043675": {
        "hw": "assayer",
        "pos": "noun",
        "vi": "người phân tích giám định quặng",
        "ipa": "/æˈseɪɚ/"
    },
    "lex.en.100k.043676": {
        "hw": "bachelorhood",
        "pos": "noun",
        "vi": "thời kỳ độc thân của người đàn ông",
        "ipa": "/ˈbætʃəlɚhʊd/"
    },
    "lex.en.100k.043677": {
        "hw": "bagful",
        "pos": "noun",
        "vi": "một túi đầy vật phẩm; lượng đầy túi",
        "ipa": "/ˈbæɡfʊl/"
    },
    "lex.en.100k.043678": {
        "hw": "baseness",
        "pos": "noun",
        "vi": "sự hèn hạ đê tiện vô liêm sỉ",
        "ipa": "/ˈbeɪsnəs/"
    },
    "lex.en.100k.043679": {
        "hw": "bitingly",
        "pos": "adv",
        "vi": "một cách sâu cay chua chát buốt giá",
        "ipa": "/ˈbaɪtɪŋli/"
    },
    "lex.en.100k.043680": {
        "hw": "blackleg",
        "pos": "noun",
        "vi": "kẻ phá đám bãi công; bệnh súc vật",
        "ipa": "/ˈblæklɛɡ/"
    },
    "lex.en.100k.043681": {
        "hw": "bookclub",
        "pos": "noun",
        "vi": "câu lạc bộ người yêu sách đọc sách",
        "ipa": "/ˈbʊkklʌb/"
    },
    "lex.en.100k.043682": {
        "hw": "brumaire",
        "pos": "noun",
        "vi": "tháng Sương mù lịch cộng hòa Pháp",
        "ipa": "/bryˈmɛr/"
    },
    "lex.en.100k.043683": {
        "hw": "caboodle",
        "pos": "noun",
        "vi": "toàn bộ tất cả mớ đồ lũ người",
        "ipa": "/kəˈbuːdəl/"
    },
    "lex.en.100k.043684": {
        "hw": "canape",
        "pos": "noun",
        "vi": "bánh mì nhỏ khai vị phết bơ sốt",
        "ipa": "/ˈkænəpeɪ/"
    },
    "lex.en.100k.043685": {
        "hw": "candelabrum",
        "pos": "noun",
        "vi": "chân nến nhiều nhánh lớn sang trọng",
        "ipa": "/ˌkændəˈlɑːbrəm/"
    },
    "lex.en.100k.043686": {
        "hw": "caryatid",
        "pos": "noun",
        "vi": "cột đá tạc tượng phụ nữ Hy Lạp",
        "ipa": "/ˌkæriˈætɪd/"
    },
    "lex.en.100k.043687": {
        "hw": "cautiousness",
        "pos": "noun",
        "vi": "sự cẩn trọng dè dặt tính thận trọng",
        "ipa": "/ˈkɔːʃəsnəs/"
    },
    "lex.en.100k.043688": {
        "hw": "centrex",
        "pos": "noun",
        "vi": "tổng đài điện thoại cơ quan",
        "ipa": "/ˈsɛntrɛks/"
    },
    "lex.en.100k.043689": {
        "hw": "chicot",
        "pos": "noun",
        "vi": "cây cà phê Kentucky gãy ngọn",
        "ipa": "/ʃiːˈkoʊ/"
    },
    "lex.en.100k.043690": {
        "hw": "circumstantially",
        "pos": "adv",
        "vi": "theo chứng cứ gián tiếp hoàn cảnh",
        "ipa": "/ˌsɝːkəmˈstænʃəli/"
    },
    "lex.en.100k.043691": {
        "hw": "clathrate",
        "pos": "adj",
        "vi": "có cấu trúc mạng tinh thể bọc lồng",
        "ipa": "/ˈklæθreɪt/"
    },
    "lex.en.100k.043692": {
        "hw": "claver",
        "pos": "verb",
        "vi": "nói chuyện phiếm; buôn chuyện",
        "ipa": "/ˈkleɪvɚ/"
    },
    "lex.en.100k.043693": {
        "hw": "clomipramine",
        "pos": "noun",
        "vi": "thuốc chống trầm cảm clomipramine",
        "ipa": "/kloʊˈmɪprəmiːn/"
    },
    "lex.en.100k.043694": {
        "hw": "clubroom",
        "pos": "noun",
        "vi": "phòng sinh hoạt chung câu lạc bộ",
        "ipa": "/ˈklʌbruːm/"
    },
    "lex.en.100k.043695": {
        "hw": "collagenase",
        "pos": "noun",
        "vi": "men phân giải sợi collagenase",
        "ipa": "/kəˈlædʒəneɪs/"
    },
    "lex.en.100k.043696": {
        "hw": "concatenate",
        "pos": "verb",
        "vi": "nối các chuỗi lại với nhau chuỗi",
        "ipa": "/kənˈkætəneɪt/"
    },
    "lex.en.100k.043697": {
        "hw": "consanguineous",
        "pos": "adj",
        "vi": "có quan hệ cận huyết thống",
        "ipa": "/ˌkɑːnsæŋˈɡwɪniəs/"
    },
    "lex.en.100k.043698": {
        "hw": "contrariwise",
        "pos": "adv",
        "vi": "ngược lại; trái lại hoàn toàn",
        "ipa": "/ˌkɑːntrəriwaɪz/"
    },
    "lex.en.100k.043699": {
        "hw": "conventionality",
        "pos": "noun",
        "vi": "tính sáo mòn quy ước xã hội",
        "ipa": "/kənˌvɛnʃəˈnæləti/"
    },
    "lex.en.100k.043700": {
        "hw": "corduroys",
        "pos": "noun",
        "vi": "quần may bằng vải nhung kẻ gân sọc",
        "ipa": "/ˈkɔːrdərɔɪz/"
    },
    "lex.en.100k.043701": {
        "hw": "countercurrent",
        "pos": "noun",
        "vi": "dòng nước chảy ngược ngược chiều",
        "ipa": "/ˈkaʊntɚˌkɝːənt/"
    }
}

OVERRIDES_PART3 = {
    "lex.en.100k.043702": {
        "hw": "cowbird",
        "pos": "noun",
        "vi": "loài chim sáo bò đẻ trứng nhờ tổ",
        "ipa": "/ˈkaʊbɝːd/"
    },
    "lex.en.100k.043703": {
        "hw": "cowslip",
        "pos": "noun",
        "vi": "hoa anh thảo dại màu vàng thơm",
        "ipa": "/ˈkaʊslɪp/"
    },
    "lex.en.100k.043704": {
        "hw": "cufflink",
        "pos": "noun",
        "vi": "khuy măng-sét cài cổ tay áo sơ mi",
        "ipa": "/ˈkʌflɪŋk/"
    },
    "lex.en.100k.043705": {
        "hw": "dadaism",
        "pos": "noun",
        "vi": "trường phái nghệ thuật Da-đa",
        "ipa": "/ˈdɑːdɑːɪzəm/"
    },
    "lex.en.100k.043706": {
        "hw": "decidua",
        "pos": "noun",
        "vi": "màng rụng nội mạc tử cung khi thai",
        "ipa": "/dɪˈsɪdʒuə/"
    },
    "lex.en.100k.043707": {
        "hw": "declamatory",
        "pos": "adj",
        "vi": "hùng hồn đao to búa lớn khoa trương",
        "ipa": "/dɪˈklæmətɔːri/"
    },
    "lex.en.100k.043708": {
        "hw": "defroster",
        "pos": "noun",
        "vi": "bộ phận sấy kính rã đông tuyết đá",
        "ipa": "/diːˈfrɔːstɚ/"
    },
    "lex.en.100k.043709": {
        "hw": "desalinization",
        "pos": "noun",
        "vi": "sự khử muối; việc lọc nước biển",
        "ipa": "/diːˌsælɪnɪˈzeɪʃən/"
    },
    "lex.en.100k.043710": {
        "hw": "descender",
        "pos": "noun",
        "vi": "phần chân chữ thò xuống dưới dòng",
        "ipa": "/dɪˈsɛndɚ/"
    },
    "lex.en.100k.043711": {
        "hw": "devilry",
        "pos": "noun",
        "vi": "hành vi quỷ quyệt; trò nghịch ác",
        "ipa": "/ˈdɛvəlri/"
    },
    "lex.en.100k.043712": {
        "hw": "dextral",
        "pos": "adj",
        "vi": "thuận tay phải; xoắn theo bên phải",
        "ipa": "/ˈdɛkstrəl/"
    },
    "lex.en.100k.043713": {
        "hw": "dimity",
        "pos": "noun",
        "vi": "vải sợi bông mỏng dệt vân sọc nổi",
        "ipa": "/ˈdɪmɪti/"
    },
    "lex.en.100k.043714": {
        "hw": "diplopia",
        "pos": "noun",
        "vi": "chứng song thị nhìn một hóa hai vật",
        "ipa": "/dɪˈploʊpiə/"
    },
    "lex.en.100k.043715": {
        "hw": "discreditable",
        "pos": "adj",
        "vi": "mang tiếng xấu; làm tổn hại uy tín",
        "ipa": "/dɪsˈkrɛdɪtəbəl/"
    },
    "lex.en.100k.043716": {
        "hw": "disillusioning",
        "pos": "adj",
        "vi": "làm cho vỡ mộng tan biến ảo tưởng",
        "ipa": "/ˌdɪsɪˈluːʒənɪŋ/"
    },
    "lex.en.100k.043717": {
        "hw": "disorganisation",
        "pos": "noun",
        "vi": "sự vô tổ chức mất trật tự hỗn loạn",
        "ipa": "/dɪsˌɔːrɡənəˈzeɪʃən/"
    },
    "lex.en.100k.043718": {
        "hw": "drosera",
        "pos": "noun",
        "vi": "chi cây gọng vó bắt ruồi ăn sâu bọ",
        "ipa": "/ˈdrɑːsərə/"
    },
    "lex.en.100k.043719": {
        "hw": "drupe",
        "pos": "noun",
        "vi": "quả hạch có nhân cứng bên trong",
        "ipa": "/druːp/"
    },
    "lex.en.100k.043720": {
        "hw": "duckbill",
        "pos": "adj",
        "vi": "có hình dạng mỏ vịt dẹp phẳng",
        "ipa": "/ˈdʌkbɪl/"
    },
    "lex.en.100k.043721": {
        "hw": "duple",
        "pos": "adj",
        "vi": "nhịp đôi hai phách; gồm hai phần",
        "ipa": "/ˈduːpəl/"
    },
    "lex.en.100k.043722": {
        "hw": "ebonite",
        "pos": "noun",
        "vi": "cao su cứng lưu hóa cách điện",
        "ipa": "/ˈɛbənaɪt/"
    },
    "lex.en.100k.043723": {
        "hw": "endogamy",
        "pos": "noun",
        "vi": "tục nội hôn kết hôn trong thị tộc",
        "ipa": "/ɛnˈdɑːɡəmi/"
    },
    "lex.en.100k.043724": {
        "hw": "endogenously",
        "pos": "adv",
        "vi": "nội sinh; bắt nguồn từ bên trong",
        "ipa": "/ɛnˈdɑːdʒənəsli/"
    },
    "lex.en.100k.043725": {
        "hw": "epilator",
        "pos": "noun",
        "vi": "máy nhổ lông cá nhân tiện dụng",
        "ipa": "/ˈɛpəleɪtɚ/"
    },
    "lex.en.100k.043726": {
        "hw": "eschaton",
        "pos": "noun",
        "vi": "ngày tận thế chung cuộc nhân loại",
        "ipa": "/ˈɛskətɑːn/"
    },
    "lex.en.100k.043727": {
        "hw": "finitude",
        "pos": "noun",
        "vi": "tính chất hữu hạn có biên giới dừng",
        "ipa": "/ˈfɪnɪtuːd/"
    },
    "lex.en.100k.043728": {
        "hw": "floatplane",
        "pos": "noun",
        "vi": "thủy phi cơ hạ cánh trên phao nước",
        "ipa": "/ˈfloʊtpleɪn/"
    },
    "lex.en.100k.043729": {
        "hw": "footplate",
        "pos": "noun",
        "vi": "sàn đứng lái của người lái tàu hỏa",
        "ipa": "/ˈfʊtpleɪt/"
    },
    "lex.en.100k.043730": {
        "hw": "forewarn",
        "pos": "verb",
        "vi": "cảnh báo trước điều nguy hiểm",
        "ipa": "/fɔːrˈwɔːrn/"
    },
    "lex.en.100k.043731": {
        "hw": "fringilla",
        "pos": "noun",
        "vi": "chi chim sẻ cúc Fringilla hót hay",
        "ipa": "/frɪnˈdʒɪlə/"
    },
    "lex.en.100k.043732": {
        "hw": "gamow",
        "pos": "noun",
        "vi": "nhà vật lý George Gamow thuyết nổ",
        "ipa": "/ˈɡeɪmɑːv/"
    },
    "lex.en.100k.043733": {
        "hw": "gatecrasher",
        "pos": "noun",
        "vi": "kẻ đến dự tiệc không mời mà đến",
        "ipa": "/ˈɡeɪtˌkræʃɚ/"
    },
    "lex.en.100k.043734": {
        "hw": "geniculate",
        "pos": "adj",
        "vi": "gập góc nhọn cong như đầu gối",
        "ipa": "/dʒəˈnɪkjələt/"
    },
    "lex.en.100k.043735": {
        "hw": "gerontologist",
        "pos": "noun",
        "vi": "chuyên gia nghiên cứu lão khoa già",
        "ipa": "/ˌdʒɛrənˈtɑːlədʒɪst/"
    },
    "lex.en.100k.043736": {
        "hw": "gofer",
        "pos": "noun",
        "vi": "người chuyên chạy việc vặt lon ton",
        "ipa": "/ˈɡoʊfɚ/"
    },
    "lex.en.100k.043737": {
        "hw": "greenroom",
        "pos": "noun",
        "vi": "phòng nghỉ diễn viên hậu trường",
        "ipa": "/ˈɡriːnruːm/"
    },
    "lex.en.100k.043738": {
        "hw": "halothane",
        "pos": "noun",
        "vi": "thuốc mê đường hô hấp halothane",
        "ipa": "/ˈhæləθeɪn/"
    },
    "lex.en.100k.043739": {
        "hw": "harakiri",
        "pos": "noun",
        "vi": "nghi thức mổ bụng tự sát võ sĩ",
        "ipa": "/ˌhærəˈkɪri/"
    },
    "lex.en.100k.043740": {
        "hw": "harridan",
        "pos": "noun",
        "vi": "mụ đàn bà đanh đá chanh chua già",
        "ipa": "/ˈhærɪdən/"
    },
    "lex.en.100k.043741": {
        "hw": "hindlimb",
        "pos": "noun",
        "vi": "chi sau; chân sau của động vật",
        "ipa": "/ˈhaɪndlɪm/"
    },
    "lex.en.100k.043742": {
        "hw": "homoeroticism",
        "pos": "noun",
        "vi": "tình cảm đồng tính luyến ái dục",
        "ipa": "/ˌhoʊmoʊɪˈrɑːtɪsɪzəm/"
    },
    "lex.en.100k.043743": {
        "hw": "horseflesh",
        "pos": "noun",
        "vi": "thịt ngựa; các đặc điểm loài ngựa",
        "ipa": "/ˈhɔːrsflɛʃ/"
    },
    "lex.en.100k.043744": {
        "hw": "hydrophobia",
        "pos": "noun",
        "vi": "chứng sợ nước do mắc bệnh dại",
        "ipa": "/ˌhaɪdrəˈfoʊbiə/"
    },
    "lex.en.100k.043745": {
        "hw": "incontrovertibly",
        "pos": "adv",
        "vi": "một cách hiển nhiên không thể cãi",
        "ipa": "/ˌɪnkɑːntrəˈvɝːtəbli/"
    },
    "lex.en.100k.043746": {
        "hw": "introit",
        "pos": "noun",
        "vi": "bài thánh ca mở đầu thánh lễ",
        "ipa": "/ˈɪntroʊɪt/"
    },
    "lex.en.100k.043747": {
        "hw": "ipomoea",
        "pos": "noun",
        "vi": "chi bìm bìm khoai lang hoa kèn",
        "ipa": "/ˌɪpəˈmiːə/"
    },
    "lex.en.100k.043748": {
        "hw": "irredentist",
        "pos": "noun",
        "vi": "người đòi thu hồi lãnh thổ lịch sử",
        "ipa": "/ˌɪrɪˈdɛntɪst/"
    },
    "lex.en.100k.043749": {
        "hw": "irremediable",
        "pos": "adj",
        "vi": "vô phương cứu vãn không thể sửa",
        "ipa": "/ˌɪrɪˈmiːdiəbəl/"
    },
    "lex.en.100k.043750": {
        "hw": "irreversibility",
        "pos": "noun",
        "vi": "tính không thể đảo ngược hoàn lại",
        "ipa": "/ˌɪrɪˌvɝːsəˈbɪləti/"
    },
    "lex.en.100k.043751": {
        "hw": "isinglass",
        "pos": "noun",
        "vi": "chất keo làm từ bong bóng cá",
        "ipa": "/ˈaɪzɪŋɡlæs/"
    },
    "lex.en.100k.043752": {
        "hw": "ivry",
        "pos": "noun",
        "vi": "trận chiến Ivry nổi tiếng lịch sử",
        "ipa": "/iːˈvriː/"
    },
    "lex.en.100k.043753": {
        "hw": "jotun",
        "pos": "noun",
        "vi": "người khổng lồ thần thoại Bắc Âu",
        "ipa": "/ˈjoʊtʊn/"
    },
    "lex.en.100k.043754": {
        "hw": "juncus",
        "pos": "noun",
        "vi": "chi cây cỏ bấc đèn đầm lầy Juncus",
        "ipa": "/ˈdʒʌŋkəs/"
    },
    "lex.en.100k.043755": {
        "hw": "khalifah",
        "pos": "noun",
        "vi": "vị thủ lĩnh khalip thế giới Hồi",
        "ipa": "/kəˈliːfə/"
    },
    "lex.en.100k.043756": {
        "hw": "killifish",
        "pos": "noun",
        "vi": "loài cá killi nhỏ nước ngọt",
        "ipa": "/ˈkɪlɪfɪʃ/"
    },
    "lex.en.100k.043757": {
        "hw": "lamarckian",
        "pos": "adj",
        "vi": "thuộc học thuyết tiến hóa Lamarck",
        "ipa": "/ləˈmɑːrkiən/"
    },
    "lex.en.100k.043758": {
        "hw": "layabout",
        "pos": "noun",
        "vi": "kẻ lười nhác ăn không ngồi rồi",
        "ipa": "/ˈleɪəbaʊt/"
    },
    "lex.en.100k.043759": {
        "hw": "lieutenancy",
        "pos": "noun",
        "vi": "cấp bậc trung úy; chức phó chỉ huy",
        "ipa": "/luːˈtɛnənsi/"
    },
    "lex.en.100k.043760": {
        "hw": "limburger",
        "pos": "noun",
        "vi": "phô mai mềm mùi nồng Limburger",
        "ipa": "/ˈlɪmbɝːɡɚ/"
    },
    "lex.en.100k.043761": {
        "hw": "limbus",
        "pos": "noun",
        "vi": "vùng rìa giáp ranh giác mạc mắt",
        "ipa": "/ˈlɪmbəs/"
    },
    "lex.en.100k.043762": {
        "hw": "liposome",
        "pos": "noun",
        "vi": "túi hạt nano hình cầu liposome",
        "ipa": "/ˈlɪpəsoʊm/"
    },
    "lex.en.100k.043763": {
        "hw": "lordosis",
        "pos": "noun",
        "vi": "chứng ưỡn cong cột sống thắt lưng",
        "ipa": "/lɔːrˈdoʊsɪs/"
    },
    "lex.en.100k.043764": {
        "hw": "madrona",
        "pos": "noun",
        "vi": "cây dâu rừng dại madrona vỏ đỏ",
        "ipa": "/məˈdroʊnjə/"
    },
    "lex.en.100k.043765": {
        "hw": "mandatorily",
        "pos": "adv",
        "vi": "một cách bắt buộc theo luật định",
        "ipa": "/ˈmændətɔːrəli/"
    },
    "lex.en.100k.043766": {
        "hw": "mapmaking",
        "pos": "noun",
        "vi": "nghề vẽ bản đồ địa lý bản đồ học",
        "ipa": "/ˈmæpˌmeɪkɪŋ/"
    },
    "lex.en.100k.043767": {
        "hw": "masculinization",
        "pos": "noun",
        "vi": "quá trình nam tính hóa ngoại hình",
        "ipa": "/ˌmæskjələnəˈzeɪʃən/"
    },
    "lex.en.100k.043768": {
        "hw": "mcguffey",
        "pos": "noun",
        "vi": "nhà sư phạm William McGuffey",
        "ipa": "/məˈɡʌfi/"
    },
    "lex.en.100k.043769": {
        "hw": "meerschaum",
        "pos": "noun",
        "vi": "khoáng sét sepiolit tạc tẩu thuốc",
        "ipa": "/ˈmɪrʃəm/"
    },
    "lex.en.100k.043770": {
        "hw": "menotti",
        "pos": "noun",
        "vi": "nhà soạn kịch Gian Carlo Menotti",
        "ipa": "/məˈnɑːti/"
    },
    "lex.en.100k.043771": {
        "hw": "menshevik",
        "pos": "noun",
        "vi": "đảng viên phái Menshevik ở Nga",
        "ipa": "/ˈmɛnʃəvɪk/"
    },
    "lex.en.100k.043772": {
        "hw": "microcosmic",
        "pos": "adj",
        "vi": "thuộc về thế giới thu nhỏ vi mô",
        "ipa": "/ˌmaɪkrəˈkɑːzmɪk/"
    },
    "lex.en.100k.043773": {
        "hw": "mko",
        "pos": "noun",
        "vi": "tổ chức Mojahedin-e-Khalq",
        "ipa": "/ˌɛm.keɪˈoʊ/"
    },
    "lex.en.100k.043774": {
        "hw": "monoecious",
        "pos": "adj",
        "vi": "đồng chu; hoa đực cái cùng cây",
        "ipa": "/məˈniːʃəs/"
    },
    "lex.en.100k.043775": {
        "hw": "monthlong",
        "pos": "adj",
        "vi": "kéo dài trọn một tháng trời",
        "ipa": "/ˈmʌnθlɔːŋ/"
    },
    "lex.en.100k.043776": {
        "hw": "multiprocessing",
        "pos": "noun",
        "vi": "công nghệ đa xử lý dữ liệu",
        "ipa": "/ˌmʌltiˈprɑːsɛsɪŋ/"
    },
    "lex.en.100k.043777": {
        "hw": "nephron",
        "pos": "noun",
        "vi": "đơn vị cấu tạo chức năng thận",
        "ipa": "/ˈnɛfrɑːn/"
    },
    "lex.en.100k.043778": {
        "hw": "neutralisation",
        "pos": "noun",
        "vi": "phản ứng trung hòa axit bazơ",
        "ipa": "/ˌnuːtrələˈzeɪʃən/"
    },
    "lex.en.100k.043779": {
        "hw": "ngb",
        "pos": "noun",
        "vi": "Cục Vệ binh Quốc gia Hoa Kỳ NGB",
        "ipa": "/ˌɛn.dʒiːˈbiː/"
    },
    "lex.en.100k.043780": {
        "hw": "nilotic",
        "pos": "adj",
        "vi": "thuộc lưu vực hoặc ngữ hệ sông Nin",
        "ipa": "/naɪˈlɑːtɪk/"
    },
    "lex.en.100k.043781": {
        "hw": "nonviable",
        "pos": "adj",
        "vi": "không có khả năng sống sót sinh tồn",
        "ipa": "/ˌnɑːnˈvaɪəbəl/"
    },
    "lex.en.100k.043782": {
        "hw": "numidian",
        "pos": "adj",
        "vi": "thuộc vương quốc Numidia Bắc Phi",
        "ipa": "/nuːˈmɪdiən/"
    },
    "lex.en.100k.043783": {
        "hw": "oafish",
        "pos": "adj",
        "vi": "cục mịch ngớ ngẩn lóng ngóng vụng",
        "ipa": "/ˈoʊfɪʃ/"
    },
    "lex.en.100k.043784": {
        "hw": "obsessiveness",
        "pos": "noun",
        "vi": "tính chất hay bị ám ảnh bận tâm",
        "ipa": "/əbˈsɛsɪvnəs/"
    },
    "lex.en.100k.043785": {
        "hw": "ohioan",
        "pos": "noun",
        "vi": "người dân sinh sống ở bang Ohio Mỹ",
        "ipa": "/oʊˈhaɪoʊən/"
    },
    "lex.en.100k.043786": {
        "hw": "oiliness",
        "pos": "noun",
        "vi": "tính nhờn dầu; vẻ tâng bốc nịnh nọt",
        "ipa": "/ˈɔɪlinəs/"
    },
    "lex.en.100k.043787": {
        "hw": "otolaryngologist",
        "pos": "noun",
        "vi": "bác sĩ chuyên khoa tai mũi họng",
        "ipa": "/ˌoʊtoʊˌlærɪŋˈɡɑːlədʒɪst/"
    },
    "lex.en.100k.043788": {
        "hw": "overexertion",
        "pos": "noun",
        "vi": "sự làm việc quá sức kiệt lực",
        "ipa": "/ˌoʊvɚrɪɡˈzɝːʃən/"
    },
    "lex.en.100k.043789": {
        "hw": "oxalis",
        "pos": "noun",
        "vi": "chi cây chua me đất lá khế Oxalis",
        "ipa": "/ˈɑːksəlɪs/"
    },
    "lex.en.100k.043790": {
        "hw": "papaver",
        "pos": "noun",
        "vi": "chi cây thuốc phiện anh túc hoa",
        "ipa": "/pəˈpeɪvɚ/"
    },
    "lex.en.100k.043791": {
        "hw": "patroller",
        "pos": "noun",
        "vi": "người tuần tra; nhân viên tuần tra",
        "ipa": "/pəˈtroʊlɚ/"
    },
    "lex.en.100k.043792": {
        "hw": "pentose",
        "pos": "noun",
        "vi": "đường đơn năm nguyên tử cacbon",
        "ipa": "/ˈpɛntoʊs/"
    },
    "lex.en.100k.043793": {
        "hw": "periodontics",
        "pos": "noun",
        "vi": "chuyên khoa chữa bệnh nha chu răng",
        "ipa": "/ˌpɛriəˈdɑːntɪks/"
    },
    "lex.en.100k.043794": {
        "hw": "phragmites",
        "pos": "noun",
        "vi": "chi cây sậy đầm lầy Phragmites",
        "ipa": "/fræɡˈmaɪtiːz/"
    },
    "lex.en.100k.043795": {
        "hw": "phyllo",
        "pos": "noun",
        "vi": "lá bột mỏng nướng bánh Hy Lạp",
        "ipa": "/ˈfiːloʊ/"
    },
    "lex.en.100k.043796": {
        "hw": "pictographic",
        "pos": "adj",
        "vi": "thuộc ký tự chữ viết tượng hình",
        "ipa": "/ˌpɪktəˈɡræfɪk/"
    },
    "lex.en.100k.043797": {
        "hw": "pilothouse",
        "pos": "noun",
        "vi": "buồng lái tàu trên boong hoa tiêu",
        "ipa": "/ˈpaɪləthaʊs/"
    },
    "lex.en.100k.043798": {
        "hw": "polychaete",
        "pos": "noun",
        "vi": "loài giun nhiều tơ sống đáy biển",
        "ipa": "/ˈpɑːlikiːt/"
    },
    "lex.en.100k.043799": {
        "hw": "prancer",
        "pos": "noun",
        "vi": "ngựa nhún nhảy phóng chân phi nhanh",
        "ipa": "/ˈprænsɚ/"
    },
    "lex.en.100k.043800": {
        "hw": "proselyte",
        "pos": "noun",
        "vi": "người mới cải sang tôn giáo khác",
        "ipa": "/ˈprɑːsəlaɪt/"
    },
    "lex.en.100k.043801": {
        "hw": "prosthodontics",
        "pos": "noun",
        "vi": "khoa phục hình làm răng giả thẩm mỹ",
        "ipa": "/ˌprɑːsθəˈdɑːntɪks/"
    }
}

OVERRIDES_PART4 = {
    "lex.en.100k.043802": {
        "hw": "protegee",
        "pos": "noun",
        "vi": "cô gái được nâng đỡ dìu dắt",
        "ipa": "/ˈproʊtəʒeɪ/"
    },
    "lex.en.100k.043803": {
        "hw": "pulmonic",
        "pos": "adj",
        "vi": "thuộc phổi; âm phụ âm bật phổi",
        "ipa": "/pʊlˈmɑːnɪk/"
    },
    "lex.en.100k.043804": {
        "hw": "pustule",
        "pos": "noun",
        "vi": "mụn mủ sưng đỏ viêm nhiễm trên da",
        "ipa": "/ˈpʌstʃuːl/"
    },
    "lex.en.100k.043805": {
        "hw": "quat",
        "pos": "noun",
        "vi": "mụt nhọt nhỏ; lá cây nhai khat",
        "ipa": "/kwɑːt/"
    },
    "lex.en.100k.043806": {
        "hw": "quattrocento",
        "pos": "noun",
        "vi": "nghệ thuật Phục hưng thế kỷ 15 Ý",
        "ipa": "/ˌkwɑːtroʊˈtʃɛntoʊ/"
    },
    "lex.en.100k.043807": {
        "hw": "queenly",
        "pos": "adj",
        "vi": "uy nghi đường bệ như một nữ hoàng",
        "ipa": "/ˈkwiːnli/"
    },
    "lex.en.100k.043808": {
        "hw": "rearmost",
        "pos": "adj",
        "vi": "ở tận cùng phía sau cùng hàng ngũ",
        "ipa": "/ˈrɪrmoʊst/"
    },
    "lex.en.100k.043809": {
        "hw": "refloat",
        "pos": "verb",
        "vi": "làm nổi lại tàu mắc cạn; trục vớt",
        "ipa": "/riːˈfloʊt/"
    },
    "lex.en.100k.043810": {
        "hw": "rehear",
        "pos": "verb",
        "vi": "xét xử lại phiên tòa phúc thẩm",
        "ipa": "/riːˈhɪr/"
    },
    "lex.en.100k.043811": {
        "hw": "riyal",
        "pos": "noun",
        "vi": "đồng tiền riyal của Ả Rập Xê Út",
        "ipa": "/rɪˈjɑːl/"
    },
    "lex.en.100k.043812": {
        "hw": "rosaceae",
        "pos": "noun",
        "vi": "họ Hoa hồng thực vật hạt kín",
        "ipa": "/roʊˈzeɪsiiː/"
    },
    "lex.en.100k.043813": {
        "hw": "rottenness",
        "pos": "noun",
        "vi": "tình trạng thối rữa mục nát tha hóa",
        "ipa": "/ˈrɑːtənnəs/"
    },
    "lex.en.100k.043814": {
        "hw": "sangoma",
        "pos": "noun",
        "vi": "thầy lang truyền thống người Zulu",
        "ipa": "/sæŋˈɡoʊmə/"
    },
    "lex.en.100k.043815": {
        "hw": "sarda",
        "pos": "noun",
        "vi": "chi cá ngừ sọc dưa bonito Sarda",
        "ipa": "/ˈsɑːrdə/"
    },
    "lex.en.100k.043816": {
        "hw": "scaramouche",
        "pos": "noun",
        "vi": "nhân vật hề ba hoa khoác lác kịch",
        "ipa": "/ˌskærəˈmuːʃ/"
    },
    "lex.en.100k.043817": {
        "hw": "schoolchild",
        "pos": "noun",
        "vi": "học sinh lứa tuổi tiểu học",
        "ipa": "/ˈskuːlˌtʃaɪld/"
    },
    "lex.en.100k.043818": {
        "hw": "scilla",
        "pos": "noun",
        "vi": "chi hoa lan chuông xanh Scilla củ",
        "ipa": "/ˈsɪlə/"
    },
    "lex.en.100k.043819": {
        "hw": "sesamoid",
        "pos": "noun",
        "vi": "xương vừng nằm trong gân cơ gối",
        "ipa": "/ˈsɛsəmɔɪd/"
    },
    "lex.en.100k.043820": {
        "hw": "shako",
        "pos": "noun",
        "vi": "mũ kê-pi quân đội dáng trụ lông",
        "ipa": "/ˈʃækoʊ/"
    },
    "lex.en.100k.043821": {
        "hw": "shamisen",
        "pos": "noun",
        "vi": "đàn ba dây samisen truyền thống",
        "ipa": "/ˈʃæmɪsɛn/"
    },
    "lex.en.100k.043822": {
        "hw": "sibylline",
        "pos": "adj",
        "vi": "bí ẩn khó hiểu như lời sấm truyền",
        "ipa": "/ˈsɪbəlaɪn/"
    },
    "lex.en.100k.043823": {
        "hw": "sightsee",
        "pos": "verb",
        "vi": "đi tham quan du lịch danh lam",
        "ipa": "/ˈsaɪtsiː/"
    },
    "lex.en.100k.043824": {
        "hw": "siwan",
        "pos": "noun",
        "vi": "tháng Siwan thứ ba lịch Do Thái",
        "ipa": "/sɪˈvɑːn/"
    },
    "lex.en.100k.043825": {
        "hw": "solanaceae",
        "pos": "noun",
        "vi": "họ Cà Solanaceae khoai tây cà chua",
        "ipa": "/ˌsoʊləˈneɪsiiː/"
    },
    "lex.en.100k.043826": {
        "hw": "sorrowfully",
        "pos": "adv",
        "vi": "một cách sầu muộn đau buồn",
        "ipa": "/ˈsɑːroʊfəli/"
    },
    "lex.en.100k.043827": {
        "hw": "sorrowing",
        "pos": "adj",
        "vi": "đau đớn buồn thương tang tóc",
        "ipa": "/ˈsɑːroʊɪŋ/"
    },
    "lex.en.100k.043828": {
        "hw": "spacefaring",
        "pos": "noun",
        "vi": "hoạt động du hành không gian vũ trụ",
        "ipa": "/ˈspeɪsˌfɛrɪŋ/"
    },
    "lex.en.100k.043829": {
        "hw": "spacy",
        "pos": "adj",
        "vi": "lơ mơ ngơ ngác mất tập trung",
        "ipa": "/ˈspeɪsi/"
    },
    "lex.en.100k.043830": {
        "hw": "spartina",
        "pos": "noun",
        "vi": "chi cỏ chịu mặn Spartina bãi bồi",
        "ipa": "/spɑːrˈtaɪnə/"
    },
    "lex.en.100k.043831": {
        "hw": "spasmodically",
        "pos": "adv",
        "vi": "theo từng cơn co giật đứt quãng",
        "ipa": "/spæzˈmɑːdɪkli/"
    },
    "lex.en.100k.043832": {
        "hw": "spindrift",
        "pos": "noun",
        "vi": "bụi bọt nước biển bị gió cuốn bay",
        "ipa": "/ˈspɪndrɪft/"
    },
    "lex.en.100k.043833": {
        "hw": "spoonbill",
        "pos": "noun",
        "vi": "loài chim cò mỏ thìa xúc mồi",
        "ipa": "/ˈspuːnbɪl/"
    },
    "lex.en.100k.043834": {
        "hw": "stippled",
        "pos": "adj",
        "vi": "có đốm chấm lấm tấm hoa rải rác",
        "ipa": "/ˈstɪpəld/"
    },
    "lex.en.100k.043835": {
        "hw": "strophe",
        "pos": "noun",
        "vi": "khổ thơ ca tụng trong thi ca cổ",
        "ipa": "/ˈstroʊfi/"
    },
    "lex.en.100k.043836": {
        "hw": "succinylcholine",
        "pos": "noun",
        "vi": "thuốc giãn cơ succinylcholine mổ",
        "ipa": "/ˌsʌksɪnəlˈkoʊliːn/"
    },
    "lex.en.100k.043837": {
        "hw": "sulfonylurea",
        "pos": "noun",
        "vi": "thuốc trị tiểu đường sulfonylurea",
        "ipa": "/ˌsʌlfənɪlˈjʊriə/"
    },
    "lex.en.100k.043838": {
        "hw": "supremacism",
        "pos": "noun",
        "vi": "chủ nghĩa phân biệt thượng đẳng sắc",
        "ipa": "/səˈprɛməsɪzəm/"
    },
    "lex.en.100k.043839": {
        "hw": "syzygy",
        "pos": "noun",
        "vi": "hiện tượng thẳng hàng ba thiên thể",
        "ipa": "/ˈsɪzɪdʒi/"
    },
    "lex.en.100k.043840": {
        "hw": "tammuz",
        "pos": "noun",
        "vi": "tháng Tammuz lịch Do Thái",
        "ipa": "/tɑːˈmuːz/"
    },
    "lex.en.100k.043841": {
        "hw": "temazepam",
        "pos": "noun",
        "vi": "thuốc an thần mất ngủ temazepam",
        "ipa": "/təˈmæzəpæm/"
    },
    "lex.en.100k.043842": {
        "hw": "thebe",
        "pos": "noun",
        "vi": "đồng xu thebe của Botswana",
        "ipa": "/ˈteɪbeɪ/"
    },
    "lex.en.100k.043843": {
        "hw": "thyroidectomy",
        "pos": "noun",
        "vi": "phẫu thuật cắt bỏ tuyến giáp",
        "ipa": "/ˌθaɪrɔɪˈdɛktəmi/"
    },
    "lex.en.100k.043844": {
        "hw": "tilia",
        "pos": "noun",
        "vi": "chi cây đoạn Tilia gỗ làm đàn",
        "ipa": "/ˈtɪliə/"
    },
    "lex.en.100k.043845": {
        "hw": "titillated",
        "pos": "adj",
        "vi": "cảm thấy phấn khích thích thú nhẹ",
        "ipa": "/ˈtɪtəleɪtɪd/"
    },
    "lex.en.100k.043846": {
        "hw": "tranquilliser",
        "pos": "noun",
        "vi": "thuốc an thần giảm căng thẳng lo âu",
        "ipa": "/ˈtræŋkwəlaɪzɚ/"
    },
    "lex.en.100k.043847": {
        "hw": "translocate",
        "pos": "verb",
        "vi": "di dời vị trí; chuyển đoạn gen",
        "ipa": "/trænzˈloʊkeɪt/"
    },
    "lex.en.100k.043848": {
        "hw": "tropopause",
        "pos": "noun",
        "vi": "đỉnh tầng đối lưu giáp bình lưu",
        "ipa": "/ˈtroʊpəpɔːz/"
    },
    "lex.en.100k.043849": {
        "hw": "tuneless",
        "pos": "adj",
        "vi": "chát chúa vô điệu mất giai điệu",
        "ipa": "/ˈtuːnləs/"
    },
    "lex.en.100k.043850": {
        "hw": "undreamed",
        "pos": "adj",
        "vi": "ngoài sức tưởng tượng không ngờ",
        "ipa": "/ʌnˈdriːmd/"
    },
    "lex.en.100k.043851": {
        "hw": "ungodliness",
        "pos": "noun",
        "vi": "tội lỗi bất kính; tính vô đạo đức",
        "ipa": "/ʌnˈɡɑːdlinəs/"
    },
    "lex.en.100k.043852": {
        "hw": "unimodal",
        "pos": "adj",
        "vi": "có một đỉnh mốt duy nhất biểu đồ",
        "ipa": "/ˌjuːnɪˈmoʊdəl/"
    },
    "lex.en.100k.043853": {
        "hw": "uninfluenced",
        "pos": "adj",
        "vi": "không bị lung lay tác động chi phối",
        "ipa": "/ˌʌnˈɪnfluənst/"
    },
    "lex.en.100k.043854": {
        "hw": "unreflective",
        "pos": "adj",
        "vi": "nông nổi thiếu suy ngẫm chín chắn",
        "ipa": "/ˌʌnrɪˈflɛktɪv/"
    },
    "lex.en.100k.043855": {
        "hw": "unsurpassable",
        "pos": "adj",
        "vi": "vô song không ai có thể vượt qua",
        "ipa": "/ˌʌnsɚˈpæsəbəl/"
    },
    "lex.en.100k.043856": {
        "hw": "untrusting",
        "pos": "adj",
        "vi": "hay ngờ vực ngờ nghệch không tin",
        "ipa": "/ʌnˈtrʌstɪŋ/"
    },
    "lex.en.100k.043857": {
        "hw": "vicariate",
        "pos": "noun",
        "vi": "giáo hạt đại diện tông tòa phụ cận",
        "ipa": "/vaɪˈkɛriət/"
    },
    "lex.en.100k.043858": {
        "hw": "vioxx",
        "pos": "noun",
        "vi": "thuốc kháng viêm giảm đau Vioxx",
        "ipa": "/ˈvaɪɑːks/"
    },
    "lex.en.100k.043859": {
        "hw": "vocalic",
        "pos": "adj",
        "vi": "thuộc nguyên âm; có tính nguyên âm",
        "ipa": "/voʊˈkælɪk/"
    },
    "lex.en.100k.043860": {
        "hw": "voiceprint",
        "pos": "noun",
        "vi": "phổ âm giọng nói nhận dạng người",
        "ipa": "/ˈvɔɪsprɪnt/"
    },
    "lex.en.100k.043861": {
        "hw": "waxen",
        "pos": "adj",
        "vi": "làm bằng sáp; tái nhợt như sáp",
        "ipa": "/ˈwæksən/"
    },
    "lex.en.100k.043862": {
        "hw": "winckelmann",
        "pos": "noun",
        "vi": "nhà khảo cổ học Johann Winckelmann",
        "ipa": "/ˈvɪŋkəlmɑːn/"
    },
    "lex.en.100k.043863": {
        "hw": "yeshivah",
        "pos": "noun",
        "vi": "trường kinh thánh Do Thái giáo",
        "ipa": "/jəˈʃiːvə/"
    },
    "lex.en.100k.043864": {
        "hw": "zukerman",
        "pos": "noun",
        "vi": "nghệ sĩ vĩ cầm Pinchas Zukerman",
        "ipa": "/ˈzʊkɚmən/"
    },
    "lex.en.100k.043865": {
        "hw": "acetabular",
        "pos": "adj",
        "vi": "thuộc hõm cối xương chậu hông",
        "ipa": "/ˌæsɪˈtæbjəlɚ/"
    },
    "lex.en.100k.043866": {
        "hw": "achondroplasia",
        "pos": "noun",
        "vi": "chứng loạn sản sụn gây người lùn",
        "ipa": "/eɪˌkɑːndroʊˈpleɪʒiə/"
    },
    "lex.en.100k.043867": {
        "hw": "aconitum",
        "pos": "noun",
        "vi": "chi cây phụ tử ô đầu kịch độc",
        "ipa": "/ˌækəˈnaɪtəm/"
    },
    "lex.en.100k.043868": {
        "hw": "acrophobia",
        "pos": "noun",
        "vi": "nỗi sợ hãi chứng sợ độ cao",
        "ipa": "/ˌækrəˈfoʊbiə/"
    },
    "lex.en.100k.043869": {
        "hw": "adduce",
        "pos": "verb",
        "vi": "đưa ra dẫn chứng viện lẽ xác đáng",
        "ipa": "/əˈduːs/"
    },
    "lex.en.100k.043870": {
        "hw": "adnate",
        "pos": "adj",
        "vi": "dính liền thân với nhau thực vật",
        "ipa": "/ˈædneɪt/"
    },
    "lex.en.100k.043871": {
        "hw": "adrenocortical",
        "pos": "adj",
        "vi": "thuộc lớp vỏ tuyến thượng thận",
        "ipa": "/əˌdriːnoʊˈkɔːrtɪkəl/"
    },
    "lex.en.100k.043872": {
        "hw": "affably",
        "pos": "adv",
        "vi": "một cách nhã nhặn niềm nở cởi mở",
        "ipa": "/ˈæfəbli/"
    },
    "lex.en.100k.043873": {
        "hw": "agapanthus",
        "pos": "noun",
        "vi": "cây thanh anh bách hợp châu Phi",
        "ipa": "/ˌæɡəˈpænθəs/"
    },
    "lex.en.100k.043874": {
        "hw": "aluminate",
        "pos": "noun",
        "vi": "muối nhôm aluminat trong hóa học",
        "ipa": "/əˈluːmɪneɪt/"
    },
    "lex.en.100k.043875": {
        "hw": "americanize",
        "pos": "verb",
        "vi": "Mỹ hóa phong cách lối sống văn hóa",
        "ipa": "/əˈmɛrɪkənaɪz/"
    },
    "lex.en.100k.043876": {
        "hw": "anachronistically",
        "pos": "adv",
        "vi": "một cách sai thời đại lỗi thời",
        "ipa": "/əˌnækrəˈnɪstɪkli/"
    },
    "lex.en.100k.043877": {
        "hw": "anosmia",
        "pos": "noun",
        "vi": "chứng mất khứu giác điếc mũi",
        "ipa": "/ænˈɑːzmiə/"
    },
    "lex.en.100k.043878": {
        "hw": "approachability",
        "pos": "noun",
        "vi": "tính cách cởi mở thân thiện dễ gần",
        "ipa": "/əˌproʊtʃəˈbɪləti/"
    },
    "lex.en.100k.043879": {
        "hw": "aspirator",
        "pos": "noun",
        "vi": "ống hút dịch; máy hút thông xoang",
        "ipa": "/ˈæspəreɪtɚ/"
    },
    "lex.en.100k.043880": {
        "hw": "auspiciously",
        "pos": "adv",
        "vi": "một cách hanh thông tốt lành may",
        "ipa": "/ɔːˈspɪʃəsli/"
    },
    "lex.en.100k.043881": {
        "hw": "aweigh",
        "pos": "adj",
        "vi": "vừa được nhổ khỏi đáy biển mỏ neo",
        "ipa": "/əˈweɪ/"
    },
    "lex.en.100k.043882": {
        "hw": "balas",
        "pos": "noun",
        "vi": "đá spinel đỏ balas giả hồng ngọc",
        "ipa": "/ˈbæləs/"
    },
    "lex.en.100k.043883": {
        "hw": "berried",
        "pos": "adj",
        "vi": "sai trĩu quả mọng nhiều quả mọng",
        "ipa": "/ˈbɛrid/"
    },
    "lex.en.100k.043884": {
        "hw": "bindweed",
        "pos": "noun",
        "vi": "cỏ bìm bìm dại leo quấn hại mùa",
        "ipa": "/ˈbaɪndwiːd/"
    },
    "lex.en.100k.043885": {
        "hw": "bootmaker",
        "pos": "noun",
        "vi": "thợ thủ công đóng ủng đóng giày da",
        "ipa": "/ˈbuːtˌmeɪkɚ/"
    },
    "lex.en.100k.043886": {
        "hw": "boutonniere",
        "pos": "noun",
        "vi": "bông hoa cài ve áo comple chú rể",
        "ipa": "/ˌbuːtəˈnjɛr/"
    },
    "lex.en.100k.043887": {
        "hw": "bunkum",
        "pos": "noun",
        "vi": "chuyện ba hoa tào lao nhảm nhí",
        "ipa": "/ˈbʌŋkəm/"
    },
    "lex.en.100k.043888": {
        "hw": "burnable",
        "pos": "adj",
        "vi": "có thể bén lửa đốt cháy được",
        "ipa": "/ˈbɝːnəbəl/"
    },
    "lex.en.100k.043889": {
        "hw": "bvd",
        "pos": "noun",
        "vi": "nhãn hiệu quần áo lót nam BVD",
        "ipa": "/ˌbiː.viːˈdiː/"
    },
    "lex.en.100k.043890": {
        "hw": "carborundum",
        "pos": "noun",
        "vi": "bột mài cacborunđum silic carbide",
        "ipa": "/ˌkɑːrbəˈrʌndəm/"
    },
    "lex.en.100k.043891": {
        "hw": "carnauba",
        "pos": "noun",
        "vi": "sáp lá cọ carnauba bóng xe",
        "ipa": "/kɑːrˈnɔːbə/"
    },
    "lex.en.100k.043892": {
        "hw": "cashbox",
        "pos": "noun",
        "vi": "hộp sắt khóa an toàn đựng tiền",
        "ipa": "/ˈkæʃbɑːks/"
    },
    "lex.en.100k.043893": {
        "hw": "castrato",
        "pos": "noun",
        "vi": "nam ca sĩ bị thiến giữ giọng cao",
        "ipa": "/kæˈstrɑːtoʊ/"
    },
    "lex.en.100k.043894": {
        "hw": "catholicity",
        "pos": "noun",
        "vi": "tính bao quát toàn diện độ lượng",
        "ipa": "/ˌkæθəˈlɪsəti/"
    },
    "lex.en.100k.043895": {
        "hw": "chador",
        "pos": "noun",
        "vi": "áo choàng dài trùm đầu phụ nữ Hồi",
        "ipa": "/ˈtʃɑːdɔːr/"
    },
    "lex.en.100k.043896": {
        "hw": "changan",
        "pos": "noun",
        "vi": "cố đô Trường An cổ của Trung Hoa",
        "ipa": "/ˈtʃɑːŋˈɑːn/"
    },
    "lex.en.100k.043897": {
        "hw": "chiasm",
        "pos": "noun",
        "vi": "vùng bắt chéo dây thần kinh",
        "ipa": "/ˈkaɪæzəm/"
    },
    "lex.en.100k.043898": {
        "hw": "collaborationist",
        "pos": "noun",
        "vi": "kẻ bắt tay với quân chiếm đóng",
        "ipa": "/kəˌlæbəˈreɪʃənɪst/"
    },
    "lex.en.100k.043899": {
        "hw": "comfortingly",
        "pos": "adv",
        "vi": "một cách ấm áp xoa dịu an ủi",
        "ipa": "/ˈkʌmfɚtɪŋli/"
    },
    "lex.en.100k.043900": {
        "hw": "conjuror",
        "pos": "noun",
        "vi": "nhà ảo thuật tài ba; thầy phù thủy",
        "ipa": "/ˈkɑːndʒɚrɚ/"
    },
    "lex.en.100k.043901": {
        "hw": "contrastingly",
        "pos": "adv",
        "vi": "một cách tương phản đối lập rõ rệt",
        "ipa": "/kənˈtræstɪŋli/"
    }
}

OVERRIDES_PART5 = {
    "lex.en.100k.043902": {
        "hw": "corrida",
        "pos": "noun",
        "vi": "trận đấu bò tót Tây Ban Nha",
        "ipa": "/kəˈriːdə/"
    },
    "lex.en.100k.043903": {
        "hw": "counterespionage",
        "pos": "noun",
        "vi": "hoạt động phản gián tình báo",
        "ipa": "/ˌkaʊntɚˈɛspiənɑːʒ/"
    },
    "lex.en.100k.043904": {
        "hw": "cryptogram",
        "pos": "noun",
        "vi": "bản văn kiện viết bằng mật mã",
        "ipa": "/ˈkrɪptəɡræm/"
    },
    "lex.en.100k.043905": {
        "hw": "culotte",
        "pos": "noun",
        "vi": "quần giả váy culotte ống rộng",
        "ipa": "/kjuːˈlɑːt/"
    },
    "lex.en.100k.043906": {
        "hw": "cynosure",
        "pos": "noun",
        "vi": "tâm điểm của mọi sự chú ý",
        "ipa": "/ˈsaɪnəʃʊr/"
    },
    "lex.en.100k.043907": {
        "hw": "czestochowa",
        "pos": "noun",
        "vi": "thành phố thánh địa Częstochowa",
        "ipa": "/ˌtʃɛstəˈhoʊvə/"
    },
    "lex.en.100k.043908": {
        "hw": "dapsone",
        "pos": "noun",
        "vi": "thuốc kháng sinh dapsone trị phong",
        "ipa": "/ˈdæpsoʊn/"
    },
    "lex.en.100k.043909": {
        "hw": "debilitation",
        "pos": "noun",
        "vi": "sự suy nhược kiệt quệ sức lực",
        "ipa": "/dɪˌbɪlɪˈteɪʃən/"
    },
    "lex.en.100k.043910": {
        "hw": "dermabrasion",
        "pos": "noun",
        "vi": "thủ thuật mài mòn sẹo tái tạo da",
        "ipa": "/ˌdɝːməˈbreɪʒən/"
    },
    "lex.en.100k.043911": {
        "hw": "deviousness",
        "pos": "noun",
        "vi": "tính quanh co lắt léo xảo quyệt",
        "ipa": "/ˈdiːviəsnəs/"
    },
    "lex.en.100k.043912": {
        "hw": "diastole",
        "pos": "noun",
        "vi": "giai đoạn giãn tim tâm trương",
        "ipa": "/daɪˈæstəli/"
    },
    "lex.en.100k.043913": {
        "hw": "digitalisation",
        "pos": "noun",
        "vi": "liệu trình dùng thuốc digitalis",
        "ipa": "/ˌdɪdʒɪtələˈzeɪʃən/"
    },
    "lex.en.100k.043914": {
        "hw": "disbar",
        "pos": "verb",
        "vi": "tước quyền hành nghề luật sư",
        "ipa": "/dɪsˈbɑːr/"
    },
    "lex.en.100k.043915": {
        "hw": "discoid",
        "pos": "adj",
        "vi": "có hình dạng đĩa tròn dẹt mỏng",
        "ipa": "/ˈdɪskɔɪd/"
    },
    "lex.en.100k.043916": {
        "hw": "diverticulum",
        "pos": "noun",
        "vi": "túi thừa bất thường ở thành ruột",
        "ipa": "/ˌdaɪvɚˈtɪkjələm/"
    },
    "lex.en.100k.043917": {
        "hw": "dodder",
        "pos": "noun",
        "vi": "dây tơ hồng sống ký sinh hút chất",
        "ipa": "/ˈdɑːdɚ/"
    },
    "lex.en.100k.043918": {
        "hw": "dorsiflexion",
        "pos": "noun",
        "vi": "động tác gập mu chân mu bàn tay",
        "ipa": "/ˌdɔːrsɪˈflɛkʃən/"
    },
    "lex.en.100k.043919": {
        "hw": "doubloon",
        "pos": "noun",
        "vi": "đồng tiền vàng đúp-lông Tây Ban Nha",
        "ipa": "/dʌˈbluːn/"
    },
    "lex.en.100k.043920": {
        "hw": "doyenne",
        "pos": "noun",
        "vi": "nữ lão thành đức cao vọng trọng",
        "ipa": "/dɔɪˈɛn/"
    },
    "lex.en.100k.043921": {
        "hw": "eaglet",
        "pos": "noun",
        "vi": "chim đại bàng con mới nở",
        "ipa": "/ˈiːɡlɪt/"
    },
    "lex.en.100k.043922": {
        "hw": "encumber",
        "pos": "verb",
        "vi": "làm vướng víu nặng nề gánh nặng",
        "ipa": "/ɪnˈkʌmbɚ/"
    },
    "lex.en.100k.043923": {
        "hw": "ennoble",
        "pos": "verb",
        "vi": "phong tước quý tộc; tôn vinh",
        "ipa": "/ɪˈnoʊbəl/"
    },
    "lex.en.100k.043924": {
        "hw": "entailment",
        "pos": "noun",
        "vi": "hệ quả tất yếu logic suy ra",
        "ipa": "/ɪnˈteɪlmənt/"
    },
    "lex.en.100k.043925": {
        "hw": "eulogize",
        "pos": "verb",
        "vi": "ca ngợi tán dương ca tụng công đức",
        "ipa": "/ˈjuːlədʒaɪz/"
    },
    "lex.en.100k.043926": {
        "hw": "eumenes",
        "pos": "noun",
        "vi": "chi tò vò đất xây tổ eumenes",
        "ipa": "/ˈjuːməniːz/"
    },
    "lex.en.100k.043927": {
        "hw": "exponentiation",
        "pos": "noun",
        "vi": "phép tính lũy thừa nâng lên số mũ",
        "ipa": "/ɛkˌspoʊnɛnʃiˈeɪʃən/"
    },
    "lex.en.100k.043928": {
        "hw": "fatback",
        "pos": "noun",
        "vi": "mảng mỡ lưng lợn ướp muối rán giòn",
        "ipa": "/ˈfætbæk/"
    },
    "lex.en.100k.043929": {
        "hw": "fiducial",
        "pos": "adj",
        "vi": "dùng làm mốc đo đạc tin cậy chuẩn",
        "ipa": "/fɪˈduːʃəl/"
    },
    "lex.en.100k.043930": {
        "hw": "frigidity",
        "pos": "noun",
        "vi": "chứng lãnh cảm; sự lạnh lùng",
        "ipa": "/frɪˈdʒɪdəti/"
    },
    "lex.en.100k.043931": {
        "hw": "frisia",
        "pos": "noun",
        "vi": "vùng Frisia duyên hải biển Bắc Âu",
        "ipa": "/ˈfriːʒiə/"
    },
    "lex.en.100k.043932": {
        "hw": "fula",
        "pos": "noun",
        "vi": "người hoặc ngôn ngữ Fula Tây Phi",
        "ipa": "/ˈfuːlə/"
    },
    "lex.en.100k.043933": {
        "hw": "furl",
        "pos": "verb",
        "vi": "cuộn chặt xếp gọn cánh buồm chiếc ô",
        "ipa": "/fɝːl/"
    },
    "lex.en.100k.043934": {
        "hw": "genetical",
        "pos": "adj",
        "vi": "thuộc nguồn gốc di truyền học gen",
        "ipa": "/dʒəˈnɛtɪkəl/"
    },
    "lex.en.100k.043935": {
        "hw": "geomancy",
        "pos": "noun",
        "vi": "thuật xem phong thủy địa lý đất cát",
        "ipa": "/ˈdʒiːəmænsi/"
    },
    "lex.en.100k.043936": {
        "hw": "germicidal",
        "pos": "adj",
        "vi": "có tính sát trùng diệt vi khuẩn",
        "ipa": "/ˌdʒɝːmɪˈsaɪdəl/"
    },
    "lex.en.100k.043937": {
        "hw": "gluey",
        "pos": "adj",
        "vi": "nhơn nhớt dính quánh như keo dán",
        "ipa": "/ˈɡluːi/"
    },
    "lex.en.100k.043938": {
        "hw": "hamsun",
        "pos": "noun",
        "vi": "nhà văn Knut Hamsun đạt giải Nobel",
        "ipa": "/ˈhɑːmsʊn/"
    },
    "lex.en.100k.043939": {
        "hw": "homophonic",
        "pos": "adj",
        "vi": "từ đồng âm; phức điệu chủ âm",
        "ipa": "/ˌhɑːməˈfɑːnɪk/"
    },
    "lex.en.100k.043940": {
        "hw": "hyla",
        "pos": "noun",
        "vi": "chi nhái bén leo cây Hyla da xanh",
        "ipa": "/ˈhaɪlə/"
    },
    "lex.en.100k.043941": {
        "hw": "ilx",
        "pos": "num",
        "vi": "năm mươi chín; 59",
        "ipa": "/ˌaɪ.ɛlˈɛks/"
    },
    "lex.en.100k.043942": {
        "hw": "indri",
        "pos": "noun",
        "vi": "loài vượn cáo lớn không đuôi Indri",
        "ipa": "/ˈɪndri/"
    },
    "lex.en.100k.043943": {
        "hw": "ironworker",
        "pos": "noun",
        "vi": "thợ lắp ráp kết cấu dầm sắt thép",
        "ipa": "/ˈaɪɚnˌwɝːkɚ/"
    },
    "lex.en.100k.043944": {
        "hw": "jabiru",
        "pos": "noun",
        "vi": "loài cò đầu đen khổng lồ Jabiru",
        "ipa": "/ˌdʒæbəˈruː/"
    },
    "lex.en.100k.043945": {
        "hw": "jauntily",
        "pos": "adv",
        "vi": "một cách nhí nhảnh tự tin yêu đời",
        "ipa": "/ˈdʒɔːntəli/"
    },
    "lex.en.100k.043946": {
        "hw": "jook",
        "pos": "noun",
        "vi": "món cháo gạo trắng nhừ Quảng Đông",
        "ipa": "/dʒʊk/"
    },
    "lex.en.100k.043947": {
        "hw": "kach",
        "pos": "noun",
        "vi": "đảng cánh hữu Kach cực đoan Israel",
        "ipa": "/kɑːx/"
    },
    "lex.en.100k.043948": {
        "hw": "kittiwake",
        "pos": "noun",
        "vi": "mòng biển móng ngắn Kittiwake",
        "ipa": "/ˈkɪtɪweɪk/"
    },
    "lex.en.100k.043949": {
        "hw": "larix",
        "pos": "noun",
        "vi": "chi cây thông rụng lá Larix tuyết",
        "ipa": "/ˈlærɪks/"
    },
    "lex.en.100k.043950": {
        "hw": "leanness",
        "pos": "noun",
        "vi": "độ nạc của thịt; vẻ thanh mảnh gầy",
        "ipa": "/ˈliːnnəs/"
    },
    "lex.en.100k.043951": {
        "hw": "lesvos",
        "pos": "noun",
        "vi": "hòn đảo du lịch Lesbos của Hy Lạp",
        "ipa": "/ˈlɛzbɑːs/"
    },
    "lex.en.100k.043952": {
        "hw": "lexicographical",
        "pos": "adj",
        "vi": "thuộc lĩnh vực biên soạn từ điển",
        "ipa": "/ˌlɛksɪkəˈɡræfɪkəl/"
    },
    "lex.en.100k.043953": {
        "hw": "libration",
        "pos": "noun",
        "vi": "sự lắc lư quang sai Mặt Trăng",
        "ipa": "/laɪˈbreɪʃən/"
    },
    "lex.en.100k.043954": {
        "hw": "lunate",
        "pos": "adj",
        "vi": "có hình dạng vầng trăng khuyết liềm",
        "ipa": "/ˈluːneɪt/"
    },
    "lex.en.100k.043955": {
        "hw": "manipulable",
        "pos": "adj",
        "vi": "dễ thao túng; dễ điều khiển nắn bóp",
        "ipa": "/məˈnɪpjələbəl/"
    },
    "lex.en.100k.043956": {
        "hw": "matricide",
        "pos": "noun",
        "vi": "tội ác giết mẹ đẻ; kẻ sát hại mẹ",
        "ipa": "/ˈmætrɪsaɪd/"
    },
    "lex.en.100k.043957": {
        "hw": "megalith",
        "pos": "noun",
        "vi": "khối cự thạch công trình đá tảng cổ",
        "ipa": "/ˈmɛɡəlɪθ/"
    },
    "lex.en.100k.043958": {
        "hw": "metazoan",
        "pos": "noun",
        "vi": "động vật đa bào có mô chuyên biệt",
        "ipa": "/ˌmɛtəˈzoʊən/"
    },
    "lex.en.100k.043959": {
        "hw": "mikvah",
        "pos": "noun",
        "vi": "bể nước thanh tẩy nghi lễ Do Thái",
        "ipa": "/ˈmɪkvə/"
    },
    "lex.en.100k.043960": {
        "hw": "miscalculate",
        "pos": "verb",
        "vi": "tính toán sai lầm; nhận định nhầm",
        "ipa": "/mɪsˈkælkjəleɪt/"
    },
    "lex.en.100k.043961": {
        "hw": "mmpi",
        "pos": "noun",
        "vi": "trắc nghiệm đo nhân cách MMPI chuẩn",
        "ipa": "/ˌɛm.ɛm.piːˈaɪ/"
    },
    "lex.en.100k.043962": {
        "hw": "moong",
        "pos": "noun",
        "vi": "hạt đậu xanh bóc vỏ món Ấn Độ",
        "ipa": "/muːŋ/"
    },
    "lex.en.100k.043963": {
        "hw": "mountebank",
        "pos": "noun",
        "vi": "kẻ bịp bợm ba hoa; thầy lang băm",
        "ipa": "/ˈmaʊntɪbæŋk/"
    },
    "lex.en.100k.043964": {
        "hw": "mullioned",
        "pos": "adj",
        "vi": "có song đứng chia ô cửa sổ",
        "ipa": "/ˈmʌljənd/"
    },
    "lex.en.100k.043965": {
        "hw": "mussorgsky",
        "pos": "noun",
        "vi": "nhà soạn nhạc Modest Mussorgsky Nga",
        "ipa": "/ˈmʊsɔːrɡski/"
    },
    "lex.en.100k.043966": {
        "hw": "mustela",
        "pos": "noun",
        "vi": "chi chồn Mustela thân dài săn mồi",
        "ipa": "/mjuːˈstiːlə/"
    },
    "lex.en.100k.043967": {
        "hw": "myoclonus",
        "pos": "noun",
        "vi": "chứng co giật cơ đột ngột ngắn ngủi",
        "ipa": "/maɪˈɑːklənəs/"
    },
    "lex.en.100k.043968": {
        "hw": "nabob",
        "pos": "noun",
        "vi": "quan chức giàu có phô trương",
        "ipa": "/ˈneɪbɑːb/"
    },
    "lex.en.100k.043969": {
        "hw": "nacre",
        "pos": "noun",
        "vi": "lớp xà cừ óng ánh vỏ ốc ngọc trai",
        "ipa": "/ˈneɪkɚ/"
    },
    "lex.en.100k.043970": {
        "hw": "namer",
        "pos": "noun",
        "vi": "người đặt tên định danh sự vật",
        "ipa": "/ˈneɪmɚ/"
    },
    "lex.en.100k.043971": {
        "hw": "nibelung",
        "pos": "noun",
        "vi": "tộc người lùn giữ kho báu Nibelung",
        "ipa": "/ˈniːbəlʊŋ/"
    },
    "lex.en.100k.043972": {
        "hw": "noisome",
        "pos": "adj",
        "vi": "hôi thối nồng nặc; độc hại khó chịu",
        "ipa": "/ˈnɔɪsəm/"
    },
    "lex.en.100k.043973": {
        "hw": "notate",
        "pos": "verb",
        "vi": "ghi chép bằng nốt nhạc ký âm",
        "ipa": "/ˈnoʊteɪt/"
    },
    "lex.en.100k.043974": {
        "hw": "outfox",
        "pos": "verb",
        "vi": "dùng mưu khôn ngoan lừa đối thủ",
        "ipa": "/aʊtˈfɑːks/"
    },
    "lex.en.100k.043975": {
        "hw": "overenthusiastic",
        "pos": "adj",
        "vi": "hào hứng thái quá; quá nồng nhiệt",
        "ipa": "/ˌoʊvɚrɪnˌθuːziˈæstɪk/"
    },
    "lex.en.100k.043976": {
        "hw": "ovine",
        "pos": "adj",
        "vi": "thuộc loài cừu; nhút nhát như cừu",
        "ipa": "/ˈoʊvaɪn/"
    },
    "lex.en.100k.043977": {
        "hw": "paraboloid",
        "pos": "noun",
        "vi": "mặt cong paraboloit trong hình học",
        "ipa": "/pəˈræbəlɔɪd/"
    },
    "lex.en.100k.043978": {
        "hw": "parky",
        "pos": "adj",
        "vi": "lạnh buốt giá; có sương giá",
        "ipa": "/ˈpɑːrki/"
    },
    "lex.en.100k.043979": {
        "hw": "paternally",
        "pos": "adv",
        "vi": "một cách ân cần nhân hậu như cha",
        "ipa": "/pəˈtɝːnəli/"
    },
    "lex.en.100k.043980": {
        "hw": "penology",
        "pos": "noun",
        "vi": "khoa nghiên cứu hình phạt và nhà tù",
        "ipa": "/piːˈnɑːlədʒi/"
    },
    "lex.en.100k.043981": {
        "hw": "persnickety",
        "pos": "adj",
        "vi": "kỹ tính soi mói vặt vãnh khắt khe",
        "ipa": "/pɚˈsnɪkəti/"
    },
    "lex.en.100k.043982": {
        "hw": "phenylketonuria",
        "pos": "noun",
        "vi": "rối loạn chuyển hóa bẩm sinh PKU",
        "ipa": "/ˌfɛnɪlˌkiːtəˈnjʊriə/"
    },
    "lex.en.100k.043983": {
        "hw": "pictorially",
        "pos": "adv",
        "vi": "bằng hình ảnh qua tranh minh họa",
        "ipa": "/pɪkˈtɔːriəli/"
    },
    "lex.en.100k.043984": {
        "hw": "plasm",
        "pos": "noun",
        "vi": "nguyên sinh chất tế bào",
        "ipa": "/ˈplæzəm/"
    },
    "lex.en.100k.043985": {
        "hw": "poaceae",
        "pos": "noun",
        "vi": "họ Hòa thảo họ Lúa ngũ cốc",
        "ipa": "/poʊˈeɪsiiː/"
    },
    "lex.en.100k.043986": {
        "hw": "pouched",
        "pos": "adj",
        "vi": "có túi ấp con loài thú có túi",
        "ipa": "/paʊtʃt/"
    },
    "lex.en.100k.043987": {
        "hw": "practicability",
        "pos": "noun",
        "vi": "tính khả thi trong thực tiễn",
        "ipa": "/ˌpræktɪkəˈbɪləti/"
    },
    "lex.en.100k.043988": {
        "hw": "predetermine",
        "pos": "verb",
        "vi": "quyết định sắp đặt định trước",
        "ipa": "/ˌpriːdɪˈtɝːmɪn/"
    },
    "lex.en.100k.043989": {
        "hw": "priggish",
        "pos": "adj",
        "vi": "làm bộ đạo đức giả tự phụ tự mãn",
        "ipa": "/ˈprɪɡɪʃ/"
    },
    "lex.en.100k.043990": {
        "hw": "probabilistically",
        "pos": "adv",
        "vi": "theo lý thuyết xác suất ngẫu nhiên",
        "ipa": "/ˌprɑːbəbəˈlɪstɪkli/"
    },
    "lex.en.100k.043991": {
        "hw": "professionalisation",
        "pos": "noun",
        "vi": "quá trình chuyên nghiệp hóa ngành",
        "ipa": "/prəˌfɛʃənələˈzeɪʃən/"
    },
    "lex.en.100k.043992": {
        "hw": "prohibitory",
        "pos": "adj",
        "vi": "mang tính ngăn cấm; giá cấm cửa",
        "ipa": "/proʊˈhɪbətɔːri/"
    },
    "lex.en.100k.043993": {
        "hw": "promethium",
        "pos": "noun",
        "vi": "nguyên tố phóng xạ đất hiếm promêti",
        "ipa": "/prəˈmiːθiəm/"
    },
    "lex.en.100k.043994": {
        "hw": "proneness",
        "pos": "noun",
        "vi": "khuynh hướng dễ mắc thói quen xấu",
        "ipa": "/ˈproʊnnəs/"
    },
    "lex.en.100k.043995": {
        "hw": "punctum",
        "pos": "noun",
        "vi": "điểm nhỏ giải phẫu học; huyệt",
        "ipa": "/ˈpʌŋktəm/"
    },
    "lex.en.100k.043996": {
        "hw": "radome",
        "pos": "noun",
        "vi": "vỏ vòm chụp bảo vệ ăng-ten ra-đa",
        "ipa": "/ˈreɪdoʊm/"
    },
    "lex.en.100k.043997": {
        "hw": "reabsorb",
        "pos": "verb",
        "vi": "tái hấp thu chất lỏng vào cơ thể",
        "ipa": "/ˌriːəbˈzɔːrb/"
    },
    "lex.en.100k.043998": {
        "hw": "robitussin",
        "pos": "noun",
        "vi": "thuốc si-rô giảm ho Robitussin",
        "ipa": "/ˌroʊbɪˈtʌsɪn/"
    },
    "lex.en.100k.043999": {
        "hw": "roustabout",
        "pos": "noun",
        "vi": "lao động chân tay giàn khoan dầu",
        "ipa": "/ˈraʊstəbaʊt/"
    },
    "lex.en.100k.044000": {
        "hw": "saleslady",
        "pos": "noun",
        "vi": "nữ nhân viên bán hàng chu đáo",
        "ipa": "/ˈseɪlzˌleɪdi/"
    },
    "lex.en.100k.044001": {
        "hw": "salsify",
        "pos": "noun",
        "vi": "cây cúc dê lấy củ rễ salsify ăn",
        "ipa": "/ˈsælsəfi/"
    }
}

ALL_OVERRIDES = {}
ALL_OVERRIDES.update(OVERRIDES_PART1)
ALL_OVERRIDES.update(OVERRIDES_PART2)
ALL_OVERRIDES.update(OVERRIDES_PART3)
ALL_OVERRIDES.update(OVERRIDES_PART4)
ALL_OVERRIDES.update(OVERRIDES_PART5)

print(f"Total overrides loaded: {len(ALL_OVERRIDES)}")

# Validate all overrides
VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}
errors = []

for rec_id, ov in ALL_OVERRIDES.items():
    if len(ov["vi"]) > 35:
        errors.append(f"{rec_id}: vi length {len(ov['vi'])} > 35: '{ov['vi']}'")
    if ov["pos"] not in VALID_POS:
        errors.append(f"{rec_id}: invalid pos '{ov['pos']}'")
    if not (ov["ipa"].startswith("/") and ov["ipa"].endswith("/")):
        errors.append(f"{rec_id}: invalid ipa: '{ov['ipa']}'")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for err in errors[:20]:
        print(f"  {err}")
    raise SystemExit(1)

# Apply to batch-09.json
BATCH_FILE = "content/english/qa-batches/batch-09.json"
with open(BATCH_FILE, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

records = batch_data["records"]
applied_count = 0

for i in range(3500, 4000):
    r = records[i]
    r_id = r["id"]
    if r_id in ALL_OVERRIDES:
        ov = ALL_OVERRIDES[r_id]
        if r["hw"].lower() != ov["hw"].lower():
            print(f"Mismatch at index {i}: record hw '{r['hw']}' vs override hw '{ov['hw']}'")
            raise SystemExit(1)
        r["pos"] = ov["pos"]
        r["vi"] = ov["vi"]
        r["ipa"] = ov["ipa"]
        applied_count += 1
    else:
        print(f"Missing override for record index {i}: {r_id} {r['hw']}")
        raise SystemExit(1)

print(f"Successfully applied {applied_count} overrides to records 3500-3999.")

# Update reviewedCount
batch_data["reviewedCount"] = 4000
batch_data["status"] = "in_progress"

with open(BATCH_FILE, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Batch 09 updated: reviewedCount is now 4000.")
