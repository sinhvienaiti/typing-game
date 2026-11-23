# -*- coding: utf-8 -*-
import json

part4_data = [
    {"id": "lex.en.200k.051302", "hw": "kaffir cat", "pos": "phrase", "ipa": "/ˈkæfər kæt/", "vi": "mèo rừng châu Phi hoang dã", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051303", "hw": "kaffir corn", "pos": "phrase", "ipa": "/ˈkæfər kɔːrn/", "vi": "cây lúa miến lương thực", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051304", "hw": "lake leman", "pos": "phrase", "ipa": "/leɪk ləˈmɑːn/", "vi": "hồ Léman; hồ Geneva Thụy Sĩ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051305", "hw": "marshall mcluhan", "pos": "phrase", "ipa": "/ˈmɑːrʃəl məkˈluːən/", "vi": "nhà lý luận Marshall McLuhan", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051306", "hw": "mass spectrograph", "pos": "phrase", "ipa": "/mæs ˈspɛktrəɡræf/", "vi": "máy ghi khối phổ thí nghiệm", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051307", "hw": "micrometer gauge", "pos": "phrase", "ipa": "/maɪˈkrɑːmətər ɡeɪdʒ/", "vi": "thước đo vi lượng panme cơ khí", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051308", "hw": "nathaniel currier", "pos": "phrase", "ipa": "/nəˈθænjəl ˈkɜːriər/", "vi": "nhà in tranh Nathaniel Currier", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051309", "hw": "nonfat dry milk", "pos": "phrase", "ipa": "/ˌnɑːnfæt draɪ mɪlk/", "vi": "sữa bột không béo; sữa gầy", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051310", "hw": "papuan monetary unit", "pos": "phrase", "ipa": "/ˈpæpjuən ˈmʌnɪtɛri ˈjuːnɪt/", "vi": "tiền tệ Papua New Guinea", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051311", "hw": "peloponnesian peninsula", "pos": "phrase", "ipa": "/ˌpɛləpəˈniːʒən pəˈnɪnsələ/", "vi": "bán đảo Peloponnese Hy Lạp", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051312", "hw": "pharyngeal recess", "pos": "phrase", "ipa": "/fəˈrɪndʒiəl ˈriːsɛs/", "vi": "ngách họng hầu giải phẫu", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051313", "hw": "pharyngeal reflex", "pos": "phrase", "ipa": "/fəˈrɪndʒiəl ˈriːflɛks/", "vi": "phản xạ nôn hầu họng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051314", "hw": "pinus nigra", "pos": "phrase", "ipa": "/ˈpaɪnəs ˈnaɪɡrə/", "vi": "loài thông đen châu Âu", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051315", "hw": "sandro botticelli", "pos": "phrase", "ipa": "/ˈsændroʊ ˌbɑːtɪˈtʃɛli/", "vi": "danh họa Sandro Botticelli", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051316", "hw": "sedge wren", "pos": "phrase", "ipa": "/sɛdʒ rɛn/", "vi": "chim hồng tước đầm lầy cói", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051317", "hw": "slender loris", "pos": "phrase", "ipa": "/ˈslɛndər ˈlɔːrɪs/", "vi": "loài cu li thon thả", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051318", "hw": "sound spectrograph", "pos": "phrase", "ipa": "/saʊnd ˈspɛktrəɡræf/", "vi": "máy ghi phổ âm thanh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051319", "hw": "susan brownell anthony", "pos": "phrase", "ipa": "/ˈsuːzən braʊˈnɛl ˈænθəni/", "vi": "nhà vận động nữ quyền Susan Anthony", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051320", "hw": "systematic desensitization", "pos": "phrase", "ipa": "/ˌsɪstəˈmætɪk diːˌsɛnsətəˈzeɪʃən/", "vi": "liệu pháp giải mẫn cảm hệ thống", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051321", "hw": "te deum", "pos": "phrase", "ipa": "/teɪ ˈdeɪəm/", "vi": "bài thánh ca tạ ơn Te Deum", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051322", "hw": "toboggan cap", "pos": "phrase", "ipa": "/təˈbɑːɡən kæp/", "vi": "mũ len trượt tuyết trùm tai", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051323", "hw": "tsung dao lee", "pos": "phrase", "ipa": "/tsʊŋ daʊ liː/", "vi": "nhà vật lý Lý Chính Đạo Nobel", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051324", "hw": "tuvalu dollar", "pos": "phrase", "ipa": "/tuːˈvɑːluː ˈdɑːlər/", "vi": "đồng đô la đảo quốc Tuvalu", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051325", "hw": "tyrant flycatcher", "pos": "phrase", "ipa": "/ˈtaɪrənt ˈflaɪkætʃər/", "vi": "họ chim đớp ruồi bạo chúa", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051326", "hw": "urinary hesitancy", "pos": "phrase", "ipa": "/ˈjʊrənɛri ˈhɛzətənsi/", "vi": "chứng khó tiểu ngập ngừng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051327", "hw": "walter mitty", "pos": "phrase", "ipa": "/ˈwɔːltər ˈmɪti/", "vi": "kẻ mơ mộng viển vông Mitty", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051328", "hw": "wild bergamot", "pos": "phrase", "ipa": "/waɪld ˈbɜːrɡəmɑːt/", "vi": "cây kinh giới dại thảo mộc", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051329", "hw": "aars", "pos": "noun", "ipa": "/ɑːrz/", "vi": "con sông Aar ở Thụy Sĩ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051330", "hw": "aires", "pos": "noun", "ipa": "/ɛərz/", "vi": "con sông Aire ở miền bắc nước Anh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051331", "hw": "albs", "pos": "noun", "ipa": "/ælbz/", "vi": "áo lễ dài trắng của linh mục", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051332", "hw": "algers", "pos": "noun", "ipa": "/ˈældʒərz/", "vi": "nhà văn Horatio Alger của Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051333", "hw": "anesthesiologists", "pos": "noun", "ipa": "/ˌænəsˌθiːziˈɑːlədʒɪsts/", "vi": "bác sĩ chuyên khoa gây mê hồi sức", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051334", "hw": "asimovs", "pos": "noun", "ipa": "/ˈæzɪmɔːvz/", "vi": "nhà văn khoa học Isaac Asimov", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051335", "hw": "aspirants", "pos": "noun", "ipa": "/əˈspaɪərənts/", "vi": "những người khát khao thăng tiến", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051336", "hw": "autocracies", "pos": "noun", "ipa": "/ɔːˈtɑːkrəsiz/", "vi": "các chế độ độc tài chuyên chế", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051337", "hw": "bassets", "pos": "noun", "ipa": "/ˈbæsɪts/", "vi": "các chú chó săn chân lùn basset", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051338", "hw": "bodices", "pos": "noun", "ipa": "/ˈbɑːdɪsɪz/", "vi": "phần thân áo trên phụ nữ cổ xưa", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051339", "hw": "bozos", "pos": "noun", "ipa": "/ˈboʊzoʊz/", "vi": "những gã ngốc nghếch dớ dẩn", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051340", "hw": "brainier", "pos": "adj", "ipa": "/ˈbreɪniər/", "vi": "thông minh hơn; sáng trí hơn", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051341", "hw": "brainiest", "pos": "adj", "ipa": "/ˈbreɪniɪst/", "vi": "thông minh nhất; sáng dạ nhất", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051342", "hw": "brens", "pos": "noun", "ipa": "/brɛnz/", "vi": "các khẩu trung liên súng Bren", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051343", "hw": "carbondales", "pos": "noun", "ipa": "/ˈkɑːrbəndeɪlz/", "vi": "các thành phố Carbondale nước Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051344", "hw": "chamomiles", "pos": "noun", "ipa": "/ˈkæməmaɪlz/", "vi": "hoa cúc La Mã thanh nhiệt", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051345", "hw": "clamored", "pos": "verb", "ipa": "/ˈklæmərd/", "vi": "đã la ó ầm ĩ; đã phản đối gay gắt", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051346", "hw": "clamors", "pos": "noun", "ipa": "/ˈklæmərz/", "vi": "tiếng la hét huyên náo; phản đối", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051347", "hw": "cognates", "pos": "noun", "ipa": "/ˈkɑːɡneɪts/", "vi": "các từ đồng căn; bà con cùng họ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051348", "hw": "contaminants", "pos": "noun", "ipa": "/kənˈtæmənənts/", "vi": "các chất gây ô nhiễm môi trường", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051349", "hw": "crevices", "pos": "noun", "ipa": "/ˈkrɛvɪsɪz/", "vi": "những khe nứt nhỏ; kẽ đá hẹp", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051350", "hw": "crewmen", "pos": "noun", "ipa": "/ˈkruːmən/", "vi": "các thuyền viên thủy thủ đoàn", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051351", "hw": "daises", "pos": "noun", "ipa": "/ˈdeɪɪsɪz/", "vi": "các bục danh dự; bục diễn thuyết", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051352", "hw": "defectors", "pos": "noun", "ipa": "/dɪˈfɛktərz/", "vi": "những kẻ phản bội đào tẩu", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051353", "hw": "denalis", "pos": "noun", "ipa": "/dɪˈnɑːliz/", "vi": "đỉnh núi tuyết cao Denali", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051354", "hw": "dmzes", "pos": "noun", "ipa": "/ˌdiː ɛm ˈzɛdz/", "vi": "các khu vực phi quân sự giới tuyến", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051355", "hw": "dollops", "pos": "noun", "ipa": "/ˈdɑːləps/", "vi": "các muỗng thức ăn đầy sệt", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051356", "hw": "donatellos", "pos": "noun", "ipa": "/ˌdɑːnəˈtɛloʊz/", "vi": "nhà điêu khắc Donatello Phục hưng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051357", "hw": "dongles", "pos": "noun", "ipa": "/ˈdɑːŋɡəlz/", "vi": "các thiết bị khóa bảo mật dongle", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051358", "hw": "dreadnoughts", "pos": "noun", "ipa": "/ˈdrɛdnɔːts/", "vi": "các thiết giáp hạm dreadnought", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051359", "hw": "esperantos", "pos": "noun", "ipa": "/ˌɛspəˈræntoʊz/", "vi": "ngôn ngữ quốc tế nhân tạo Esperanto", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051360", "hw": "farthings", "pos": "noun", "ipa": "/ˈfɑːrðɪŋz/", "vi": "đồng farthing xu nhỏ một phần tư", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051361", "hw": "forestalled", "pos": "verb", "ipa": "/fɔːrˈstɔːld/", "vi": "đã chặn trước; đã đón đầu ngăn ngừa", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051362", "hw": "forestalls", "pos": "verb", "ipa": "/fɔːrˈstɔːlz/", "vi": "hành động trước ngăn chặn", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051363", "hw": "goldeneyes", "pos": "noun", "ipa": "/ˈɡoʊldənaɪz/", "vi": "loài vịt lặn mắt vàng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051364", "hw": "goldilockses", "pos": "noun", "ipa": "/ˈɡoʊldilɑːksɪz/", "vi": "cây hoa cúc vàng; cô bé tóc vàng", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051365", "hw": "goldmines", "pos": "noun", "ipa": "/ˈɡoʊldmaɪnz/", "vi": "các mỏ khai thác vàng; mỏ tiền hời", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051366", "hw": "gorgons", "pos": "noun", "ipa": "/ˈɡɔːrɡənz/", "vi": "quái vật đầu rắn Gorgon thần thoại", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051367", "hw": "grises", "pos": "noun", "ipa": "/ˈɡriːsɪz/", "vi": "họa sĩ lập thể Juan Gris", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051368", "hw": "harpsichords", "pos": "noun", "ipa": "/ˈhɑːrpsɪkɔːrdz/", "vi": "các chiếc đàn harpsichord cổ điển", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051369", "hw": "hindenburgs", "pos": "noun", "ipa": "/ˈhɪndənbɜːrɡz/", "vi": "khinh khí cầu khổng lồ Hindenburg", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051370", "hw": "histograms", "pos": "noun", "ipa": "/ˈhɪstəɡræmz/", "vi": "các biểu đồ tần suất hình cột", "cefr": "b2", "tier": "specialized"},
    {"id": "lex.en.200k.051371", "hw": "hmos", "pos": "noun", "ipa": "/ˌeɪtʃ ɛm ˈoʊz/", "vi": "các tổ chức bảo hiểm y tế duy trì", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051372", "hw": "husains", "pos": "noun", "ipa": "/huːˈseɪnz/", "vi": "nhân vật Saddam Hussein của Iraq", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051373", "hw": "hutus", "pos": "noun", "ipa": "/ˈhuːtuːz/", "vi": "người sắc tộc Hutu ở Rwanda", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051374", "hw": "ibsens", "pos": "noun", "ipa": "/ˈɪbsənz/", "vi": "kịch tác gia Henrik Ibsen Na Uy", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051375", "hw": "insomniacs", "pos": "noun", "ipa": "/ɪnˈsɑːmniæks/", "vi": "những người mắc chứng mất ngủ đêm", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051376", "hw": "ionians", "pos": "noun", "ipa": "/aɪˈoʊniənz/", "vi": "người xứ Ionia Hy Lạp cổ đại", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051377", "hw": "irrelevances", "pos": "noun", "ipa": "/ɪˈrɛləvənsɪz/", "vi": "những điều không liên quan lạc đề", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051378", "hw": "javaneses", "pos": "noun", "ipa": "/ˌdʒɑːvəˈniːzɪz/", "vi": "người dân tộc Java Indonesia", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051379", "hw": "kerouacs", "pos": "noun", "ipa": "/ˈkɛruːæks/", "vi": "nhà văn Jack Kerouac thế hệ Beat", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051380", "hw": "libertarianisms", "pos": "noun", "ipa": "/ˌlɪbərˈtɛriənɪzəmz/", "vi": "chủ nghĩa tự do cá nhân triệt để", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051381", "hw": "lugers", "pos": "noun", "ipa": "/ˈluːɡərz/", "vi": "súng ngắn bán tự động Luger", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051382", "hw": "lyttons", "pos": "noun", "ipa": "/ˈlɪtənz/", "vi": "tác gia Edward Bulwer-Lytton", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051383", "hw": "maidenheads", "pos": "noun", "ipa": "/ˈmeɪdənhɛdz/", "vi": "màng trinh con gái; sự trinh bạch", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051384", "hw": "mammies", "pos": "noun", "ipa": "/ˈmæmiz/", "vi": "các vú em da đen; tiếng gọi mẹ yêu", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051385", "hw": "masques", "pos": "noun", "ipa": "/mæsks/", "vi": "dạ hội kịch đeo mặt nạ hóa trang", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051386", "hw": "masseuses", "pos": "noun", "ipa": "/mæˈsɜːz/", "vi": "các nữ kỹ thuật viên xoa bóp", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051387", "hw": "metronomes", "pos": "noun", "ipa": "/ˈmɛtrənoʊmz/", "vi": "các máy đập nhịp cơ học cho đàn", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051388", "hw": "minnows", "pos": "noun", "ipa": "/ˈmɪnoʊz/", "vi": "cá tuế nhỏ; người có vai vế mọn", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051389", "hw": "mitoses", "pos": "noun", "ipa": "/maɪˈtoʊsiːz/", "vi": "quá trình phân chia nguyên phân", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051390", "hw": "moonstones", "pos": "noun", "ipa": "/ˈmuːnstoʊnz/", "vi": "đá mặt trăng lung linh phát quang", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051391", "hw": "morels", "pos": "noun", "ipa": "/məˈrɛlz/", "vi": "các loại nấm bụng dê thơm ngon", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051392", "hw": "nogs", "pos": "noun", "ipa": "/nɑːɡz/", "vi": "chốt gỗ gắn tường; món rượu trứng", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051393", "hw": "noyeses", "pos": "noun", "ipa": "/ˈnɔɪzɪz/", "vi": "nhà thơ thi sĩ Alfred Noyes", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051394", "hw": "paintbrushes", "pos": "noun", "ipa": "/ˈpeɪntbrʌʃɪz/", "vi": "các cây cọ quét sơn; bút lông vẽ", "cefr": "b1", "tier": "general"},
    {"id": "lex.en.200k.051395", "hw": "pluckier", "pos": "adj", "ipa": "/ˈplʌkiər/", "vi": "can đảm hơn; kiên cường hơn", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051396", "hw": "pluckiest", "pos": "adj", "ipa": "/ˈplʌkiɪst/", "vi": "can đảm quả cảm nhất; gan dạ nhất", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051397", "hw": "queasier", "pos": "adj", "ipa": "/ˈkwiːziər/", "vi": "buồn nôn hơn; cảm thấy bồn chồn hơn", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051398", "hw": "queasiest", "pos": "adj", "ipa": "/ˈkwiːziɪst/", "vi": "buồn nôn nhất; cồn cào nhất", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051399", "hw": "quiches", "pos": "noun", "ipa": "/kiːʃɪz/", "vi": "các món bánh nướng mặn quiche Pháp", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051400", "hw": "rainstorms", "pos": "noun", "ipa": "/ˈreɪnstɔːrmz/", "vi": "các cơn giông bão mưa lớn dữ dội", "cefr": "b1", "tier": "general"},
    {"id": "lex.en.200k.051401", "hw": "rapprochements", "pos": "noun", "ipa": "/ræˌproʊʃˈmɑːnts/", "vi": "sự nối lại quan hệ thân thiện", "cefr": "c2", "tier": "general"}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
errors = []

for idx, item in enumerate(part4_data):
    # Length check
    if len(item['vi']) > 35:
        errors.append(f"Row {idx} {item['hw']} vi too long ({len(item['vi'])}): {item['vi']}")
    # Semicolon spacing
    if ';' in item['vi']:
        parts = item['vi'].split(';')
        for p in parts[1:]:
            if not p.startswith(' '):
                errors.append(f"Row {idx} {item['hw']} semicolon spacing error: {item['vi']}")
    # POS check
    if item['pos'] not in allowed_pos:
        errors.append(f"Row {idx} {item['hw']} invalid pos: {item['pos']}")
    # IPA check
    ipa = item['ipa']
    if ' ' not in item['hw']:
        if not (ipa.startswith('/') and ipa.endswith('/') and len(ipa) > 2):
            errors.append(f"Row {idx} {item['hw']} single word invalid ipa: {ipa}")
    else:
        if ipa != "" and not (ipa.startswith('/') and ipa.endswith('/')):
            errors.append(f"Row {idx} {item['hw']} phrase invalid ipa: {ipa}")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors:
        print("  -", e)
    exit(1)
else:
    # Set status and notes
    for item in part4_data:
        item['status'] = 'reviewed'
        item['notes'] = None
    
    with open('scratch/b31_r03_p4.json', 'w', encoding='utf-8') as f:
        json.dump(part4_data, f, ensure_ascii=False, indent=2)
    print("Validated and saved 100 items for Part 4")
