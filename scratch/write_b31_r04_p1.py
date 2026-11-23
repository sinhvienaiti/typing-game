# -*- coding: utf-8 -*-
import json

part1_data = [
    {"id": "lex.en.200k.051502", "hw": "white bryony", "pos": "phrase", "ipa": "/waɪt ˈbraɪəni/", "vi": "dây củ khúc khắc trắng leo", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051503", "hw": "woolly aphid", "pos": "phrase", "ipa": "/ˈwʊli ˈeɪfɪd/", "vi": "loài rệp sáp bông trắng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051504", "hw": "woolly apple aphid", "pos": "phrase", "ipa": "/ˈwʊli ˈæpəl ˈeɪfɪd/", "vi": "rệp sáp xơ trắng hại táo", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051505", "hw": "altoonas", "pos": "noun", "ipa": "/ælˈtuːnəz/", "vi": "thành phố Altoona ở Pennsylvania", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051506", "hw": "antlers", "pos": "noun", "ipa": "/ˈæntlərz/", "vi": "các nhánh gạc hươu nai", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051507", "hw": "arbs", "pos": "noun", "ipa": "/ɑːrbz/", "vi": "người kinh doanh chênh lệch giá", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051508", "hw": "arrangers", "pos": "noun", "ipa": "/əˈreɪndʒərz/", "vi": "người phối khí; người thu xếp", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051509", "hw": "ayurvedas", "pos": "noun", "ipa": "/ˌɑːjʊərˈveɪdəz/", "vi": "hệ thống y học cổ truyền Ayurveda", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051510", "hw": "babars", "pos": "noun", "ipa": "/ˈbɑːbɑːrz/", "vi": "chú voi hoạt hình Babar nước Pháp", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051511", "hw": "barakas", "pos": "noun", "ipa": "/bəˈrɑːkəz/", "vi": "ân sủng phước lành Baraka Hồi giáo", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051512", "hw": "barbaries", "pos": "noun", "ipa": "/ˈbɑːrbəriz/", "vi": "vùng bờ biển Barbary ở Bắc Phi", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051513", "hw": "baudelaires", "pos": "noun", "ipa": "/ˈboʊdəlɛərz/", "vi": "thi phẩm của Charles Baudelaire", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051514", "hw": "bellinis", "pos": "noun", "ipa": "/bɛˈliːniz/", "vi": "món cocktail Bellini rượu đào", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051515", "hw": "beveled", "pos": "verb", "ipa": "/ˈbɛvəld/", "vi": "đã vát nghiêng góc mép", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051516", "hw": "beveling", "pos": "verb", "ipa": "/ˈbɛvəlɪŋ/", "vi": "đang vát nghiêng cạnh mép", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051517", "hw": "bookmakers", "pos": "noun", "ipa": "/ˈbʊkmeɪkərz/", "vi": "những nhà cái cá cược thể thao", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051518", "hw": "brezhnevs", "pos": "noun", "ipa": "/ˈbrɛʒnɛvz/", "vi": "lãnh đạo Leonid Brezhnev Liên Xô", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051519", "hw": "brogans", "pos": "noun", "ipa": "/ˈbroʊɡənz/", "vi": "các đôi giày da thô cổ cao", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051520", "hw": "bunyans", "pos": "noun", "ipa": "/ˈbʌnjənz/", "vi": "nhà văn John Bunyan nước Anh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051521", "hw": "businesspeoples", "pos": "noun", "ipa": "/ˈbɪznəspiːpəlz/", "vi": "các giới doanh nhân thương trường", "cefr": "b1", "tier": "general"},
    {"id": "lex.en.200k.051522", "hw": "cacophonies", "pos": "noun", "ipa": "/kæˈkɑːfəniz/", "vi": "những tạp âm chói tai hỗn loạn", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051523", "hw": "caligulas", "pos": "noun", "ipa": "/kəˈlɪɡjələz/", "vi": "hoàng đế bạo chúa Caligula La Mã", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051524", "hw": "collations", "pos": "noun", "ipa": "/kəˈleɪʃənz/", "vi": "bữa ăn nhẹ; sự đối chiếu văn bản", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051525", "hw": "confucianisms", "pos": "noun", "ipa": "/kənˈfjuːʃənɪzəmz/", "vi": "các tư tưởng Nho giáo Khổng giáo", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051526", "hw": "connectednesses", "pos": "noun", "ipa": "/kəˈnɛktɪdnəsɪz/", "vi": "sự liên kết gắn bó chặt chẽ", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051527", "hw": "conservators", "pos": "noun", "ipa": "/kənˈsɜːrvətərz/", "vi": "chuyên viên bảo tồn; người giám hộ", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051528", "hw": "coveys", "pos": "noun", "ipa": "/ˈkʌviz/", "vi": "các đàn chim cút; nhóm nhỏ bè bạn", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051529", "hw": "denunciations", "pos": "noun", "ipa": "/dɪˌnʌnsiˈeɪʃənz/", "vi": "những lời tố cáo công khai; lên án", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051530", "hw": "diuretics", "pos": "noun", "ipa": "/ˌdaɪjʊˈrɛtɪks/", "vi": "các loại thuốc lợi tiểu y khoa", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051531", "hw": "doppelgangers", "pos": "noun", "ipa": "/ˈdɑːpəlɡæŋərz/", "vi": "bản sao song trùng ma quái bí ẩn", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051532", "hw": "drawbridges", "pos": "noun", "ipa": "/ˈdrɔːbrɪdʒɪz/", "vi": "các cây cầu cất nâng mở qua sông", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051533", "hw": "edps", "pos": "noun", "ipa": "/ˌiː diː ˈpiːz/", "vi": "hệ thống xử lý dữ liệu điện tử", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051534", "hw": "effectors", "pos": "noun", "ipa": "/ɪˈfɛktərz/", "vi": "cơ quan phản ứng; phân tử tác động", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051535", "hw": "encapsulations", "pos": "noun", "ipa": "/ɪnˌkæpsəˈleɪʃənz/", "vi": "tính đóng gói dữ liệu; sự bao bọc", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051536", "hw": "etiologies", "pos": "noun", "ipa": "/ˌiːtiˈɑːlədʒiz/", "vi": "nguyên nhân học; căn nguyên bệnh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051537", "hw": "expediencies", "pos": "noun", "ipa": "/ɪkˈspiːdiənsiz/", "vi": "tính thực dụng vụ lợi; kế tạm bợ", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051538", "hw": "eyesores", "pos": "noun", "ipa": "/ˈaɪsɔːrz/", "vi": "vật chướng mắt; cảnh tượng khó coi", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051539", "hw": "foreshores", "pos": "noun", "ipa": "/ˈfɔːrʃɔːrz/", "vi": "bãi triều ven bờ; dải mép sóng bờ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051540", "hw": "gawains", "pos": "noun", "ipa": "/ɡəˈweɪnz/", "vi": "hiệp sĩ Gawain Bàn Tròn Arthur", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051541", "hw": "gizmos", "pos": "noun", "ipa": "/ˈɡɪzmoʊz/", "vi": "các đồ tiện ích nhỏ; máy móc nhỏ", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051542", "hw": "glycines", "pos": "noun", "ipa": "/ˈɡlaɪsiːnz/", "vi": "các phân tử axit amin glyxin", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051543", "hw": "groggier", "pos": "adj", "ipa": "/ˈɡrɑːɡiər/", "vi": "lảo đảo hơn; choáng váng hơn", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051544", "hw": "groggiest", "pos": "adj", "ipa": "/ˈɡrɑːɡiɪst/", "vi": "lảo đảo nhất; choáng váng nhất", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051545", "hw": "guavas", "pos": "noun", "ipa": "/ˈɡwɑːvəz/", "vi": "các quả ổi; cây ổi ăn trái", "cefr": "b1", "tier": "general"},
    {"id": "lex.en.200k.051546", "hw": "guineans", "pos": "noun", "ipa": "/ˈɡɪniənz/", "vi": "người dân nước Guinea châu Phi", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051547", "hw": "gwynns", "pos": "noun", "ipa": "/ɡwɪnz/", "vi": "nữ diễn viên kịch Nell Gwyn ở Anh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051548", "hw": "gwyns", "pos": "noun", "ipa": "/ɡwɪnz/", "vi": "thần âm phủ Celtic; thần thoại Gwyn", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051549", "hw": "habsburgs", "pos": "noun", "ipa": "/ˈhæpsbɜːrɡz/", "vi": "hoàng tộc đế vương Habsburg châu Âu", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051550", "hw": "hematomas", "pos": "noun", "ipa": "/ˌhiːməˈtoʊməz/", "vi": "các khối máu tụ dưới da sưng tấy", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051551", "hw": "hematomata", "pos": "noun", "ipa": "/ˌhiːməˈtɑːmətə/", "vi": "các khối tụ máu bầm trong mô cơ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051552", "hw": "hoyles", "pos": "noun", "ipa": "/hɔɪlz/", "vi": "nhà vật lý thiên văn Fred Hoyle", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051553", "hw": "iges", "pos": "noun", "ipa": "/ˌaɪ dʒiː ˈiːz/", "vi": "kháng thể globulin miễn dịch IgE", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051554", "hw": "indiscretions", "pos": "noun", "ipa": "/ˌɪndɪˈskrɛʃənz/", "vi": "sự thiếu thận trọng; việc sơ suất", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051555", "hw": "ingas", "pos": "noun", "ipa": "/ˈɪŋɡəz/", "vi": "chi cây họ đậu Inga vùng nhiệt đới", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051556", "hw": "jailers", "pos": "noun", "ipa": "/ˈdʒeɪlərz/", "vi": "các viên cai ngục; người coi tù", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051557", "hw": "kerbs", "pos": "noun", "ipa": "/kɜːrbz/", "vi": "mép vỉa hè; mép lề đường lát đá", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051558", "hw": "luxemburgs", "pos": "noun", "ipa": "/ˈlʌksəmbɜːrɡz/", "vi": "nhà cách mạng Rosa Luxemburg", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051559", "hw": "lyres", "pos": "noun", "ipa": "/ˈlaɪərz/", "vi": "các cây đàn lia cổ đại Hy Lạp", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051560", "hw": "materialists", "pos": "noun", "ipa": "/məˈtɪəriəlɪsts/", "vi": "người duy vật; người sống thực dụng", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051561", "hw": "mccauleys", "pos": "noun", "ipa": "/məˈkɔːliz/", "vi": "nữ anh hùng Mary McCauley Cách mạng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051562", "hw": "micronesias", "pos": "noun", "ipa": "/ˌmaɪkroʊˈniːʒəz/", "vi": "quần đảo Micronesia Thái Bình Dương", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051563", "hw": "miris", "pos": "noun", "ipa": "/ˈmɪriz/", "vi": "người bộ tộc Mishing Miri ở Ấn Độ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051564", "hw": "miros", "pos": "noun", "ipa": "/ˈmiːroʊz/", "vi": "họa sĩ siêu thực Joan Miró", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051565", "hw": "miscalculations", "pos": "noun", "ipa": "/mɪsˌkælkjuˈleɪʃənz/", "vi": "những sai sót do tính toán nhầm lẫn", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051566", "hw": "mongered", "pos": "verb", "ipa": "/ˈmʌŋɡərd/", "vi": "đã bán dạo; đã gieo rắc điều xấu", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051567", "hw": "montpeliers", "pos": "noun", "ipa": "/mɑːntˈpiːljərz/", "vi": "thủ phủ Montpelier bang Vermont", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051568", "hw": "musings", "pos": "noun", "ipa": "/ˈmjuːzɪŋz/", "vi": "những suy nghĩ trầm tư; suy tưởng", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051569", "hw": "narcs", "pos": "noun", "ipa": "/nɑːrks/", "vi": "cảnh sát chống ma túy; kẻ điểm chỉ", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051570", "hw": "natchezes", "pos": "noun", "ipa": "/ˈnætʃɪzɪz/", "vi": "thổ dân Natchez; thành phố Natchez", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051571", "hw": "neurobiologies", "pos": "noun", "ipa": "/ˌnʊroʊbaɪˈɑːlədʒiz/", "vi": "các ngành sinh học thần kinh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051572", "hw": "nitrides", "pos": "noun", "ipa": "/ˈnaɪtraɪdz/", "vi": "các hợp chất hóa học nitrua", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051573", "hw": "norepinephrines", "pos": "noun", "ipa": "/ˌnɔːrˌɛpəˈnɛfrɪnz/", "vi": "hoóc-môn noradrenalin thần kinh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051574", "hw": "nuffields", "pos": "noun", "ipa": "/ˈnʌfiːldz/", "vi": "nhà công nghiệp huân tước Nuffield", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051575", "hw": "obverses", "pos": "noun", "ipa": "/ˈɑːbvɜːrsɪz/", "vi": "mặt ngửa đồng xu; mặt đối lập", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051576", "hw": "offings", "pos": "noun", "ipa": "/ˈɔːfɪŋz/", "vi": "vùng biển khơi xa bờ; tương lai gần", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051577", "hw": "offstages", "pos": "noun", "ipa": "/ˈɔːfsteɪdʒɪz/", "vi": "khu hậu trường sau sân khấu kịch", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051578", "hw": "okas", "pos": "noun", "ipa": "/ˈoʊkəz/", "vi": "củ chua oka Nam Mỹ; đơn vị đo oka", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051579", "hw": "parleyed", "pos": "verb", "ipa": "/ˈpɑːrlid/", "vi": "đã thương lượng; đàm phán ngưng bắn", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051580", "hw": "parleying", "pos": "verb", "ipa": "/ˈpɑːrliɪŋ/", "vi": "đang đàm phán; đang thương lượng", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051581", "hw": "parleys", "pos": "noun", "ipa": "/ˈpɑːrliz/", "vi": "các cuộc đàm phán thỏa hiệp", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051582", "hw": "pavlovs", "pos": "noun", "ipa": "/ˈpævlɔːvz/", "vi": "nhà sinh lý học Ivan Pavlov phản xạ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051583", "hw": "persephones", "pos": "noun", "ipa": "/pərˈsɛfəniz/", "vi": "nữ thần mùa xuân Persephone âm phủ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051584", "hw": "phses", "pos": "noun", "ipa": "/ˌpiː eɪtʃ ˈɛsɪz/", "vi": "Cơ quan Y tế Công cộng Hoa Kỳ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051585", "hw": "pithier", "pos": "adj", "ipa": "/ˈpɪθiər/", "vi": "ngắn gọn súc tích hơn; cô đọng hơn", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051586", "hw": "pithiest", "pos": "adj", "ipa": "/ˈpɪθiɪst/", "vi": "súc tích nhất; sâu sắc cô đọng nhất", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051587", "hw": "pittances", "pos": "noun", "ipa": "/ˈpɪtənsɪz/", "vi": "món tiền còm; đồng lương ít ỏi", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051588", "hw": "placentals", "pos": "noun", "ipa": "/pləˈsɛntəlz/", "vi": "động vật có nhau thai nuôi dưỡng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051589", "hw": "puccinis", "pos": "noun", "ipa": "/pʊˈtʃiːniz/", "vi": "nhà soạn nhạc opera Giacomo Puccini", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051590", "hw": "pullovers", "pos": "noun", "ipa": "/ˈpʊloʊvərz/", "vi": "áo len chui đầu dài tay", "cefr": "a2", "tier": "general"},
    {"id": "lex.en.200k.051591", "hw": "reassessments", "pos": "noun", "ipa": "/ˌriːəˈsɛsmənts/", "vi": "các đợt thẩm định và đánh giá lại", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051592", "hw": "registrants", "pos": "noun", "ipa": "/ˈrɛdʒɪstrənts/", "vi": "những người nộp đơn đăng ký dự thi", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051593", "hw": "rositas", "pos": "noun", "ipa": "/roʊˈziːtəz/", "vi": "cây hoa râm bụt thảo mộc Rosita", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051594", "hw": "sashimis", "pos": "noun", "ipa": "/sæˈʃiːmiz/", "vi": "các món gỏi cá sống sashimi Nhật", "cefr": "b1", "tier": "general"},
    {"id": "lex.en.200k.051595", "hw": "sceptres", "pos": "noun", "ipa": "/ˈsɛptərz/", "vi": "các vương trượng quyền uy của vua", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051596", "hw": "segways", "pos": "noun", "ipa": "/ˈsɛɡweɪz/", "vi": "xe hai bánh tự cân bằng Segway", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051597", "hw": "selangors", "pos": "noun", "ipa": "/səˈlæŋɡɔːrz/", "vi": "bang công nghiệp Selangor Malaysia", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051598", "hw": "senores", "pos": "noun", "ipa": "/sɛnˈjɔːreɪz/", "vi": "các quý ông trong tiếng Tây Ban Nha", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051599", "hw": "senors", "pos": "noun", "ipa": "/sɛnˈjɔːrz/", "vi": "các quý ông lịch thiệp Tây Ban Nha", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051600", "hw": "servicemen", "pos": "noun", "ipa": "/ˈsɜːrvɪsmən/", "vi": "các quân nhân; binh sĩ quân đội", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051601", "hw": "silversteins", "pos": "noun", "ipa": "/ˈsɪlvərstiːnz/", "vi": "nhà thơ thiếu nhi Shel Silverstein", "cefr": "c2", "tier": "specialized"}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
errors = []

for idx, item in enumerate(part1_data):
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
    for item in part1_data:
        item['status'] = 'reviewed'
        item['notes'] = None
    
    with open('scratch/b31_r04_p1.json', 'w', encoding='utf-8') as f:
        json.dump(part1_data, f, ensure_ascii=False, indent=2)
    print("Validated and saved 100 items for Part 1")
