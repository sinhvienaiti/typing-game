import json

part5_data = [
  {"id": "lex.en.100k.096402", "hw": "objectivise", "pos": "verb", "ipa": "/əbˈdʒɛktɪvaɪz/", "vi": "khách quan hóa; cụ thể hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096403", "hw": "objectivism", "pos": "noun", "ipa": "/əbˈdʒɛktɪvɪzəm/", "vi": "chủ nghĩa khách quan Ayn Rand", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096404", "hw": "objectivize", "pos": "verb", "ipa": "/əbˈdʒɛktɪvaɪz/", "vi": "khách quan hóa; cụ thể hóa ý niệm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096405", "hw": "objectize", "pos": "verb", "ipa": "/ˈɑːbdʒɪktaɪz/", "vi": "khách thể hóa; xem như đối tượng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096406", "hw": "objectless", "pos": "adj", "ipa": "/ˈɑːbdʒɪktləs/", "vi": "không có mục đích; không đối tượng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096407", "hw": "objects", "pos": "verb", "ipa": "/əbˈdʒɛkts/", "vi": "phản đối; bất đồng ý kiến", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096408", "hw": "objurgate", "pos": "verb", "ipa": "/ˈɑːbdʒɚɡeɪt/", "vi": "khiển trách nặng nề; mắng mỏ gắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096409", "hw": "objurgated", "pos": "verb", "ipa": "/ˈɑːbdʒɚɡeɪtɪd/", "vi": "đã khiển trách gay gắt; đã mắng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096410", "hw": "objurgates", "pos": "verb", "ipa": "/ˈɑːbdʒɚɡeɪts/", "vi": "khiển trách gay gắt; mắng nhiếc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096411", "hw": "objurgating", "pos": "verb", "ipa": "/ˈɑːbdʒɚɡeɪtɪŋ/", "vi": "khiển trách nặng nề; mắng gay gắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096412", "hw": "objurgation", "pos": "noun", "ipa": "/ˌɑːbdʒɚˈɡeɪʃən/", "vi": "lời khiển trách nặng; sự quở trách", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096413", "hw": "objurgatory", "pos": "adj", "ipa": "/ˈɑːbdʒɚɡətɔːri/", "vi": "có tính khiển trách gay gắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096414", "hw": "oblast", "pos": "noun", "ipa": "/ˈɑːblæst/", "vi": "tỉnh; đơn vị hành chính tỉnh ở Nga", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096415", "hw": "oblational", "pos": "adj", "ipa": "/oʊˈbleɪʃənəl/", "vi": "thuộc của lễ dâng tế; lễ tạ ơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096416", "hw": "oblatory", "pos": "adj", "ipa": "/ˈɑːblətɔːri/", "vi": "dùng làm của lễ tế; hiến tế", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096417", "hw": "obligates", "pos": "verb", "ipa": "/ˈɑːblɪɡeɪts/", "vi": "bắt buộc; ép buộc phải thi hành", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096418", "hw": "obligating", "pos": "verb", "ipa": "/ˈɑːblɪɡeɪtɪŋ/", "vi": "bắt buộc; giao trách nhiệm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096419", "hw": "obligational", "pos": "adj", "ipa": "/ˌɑːblɪˈɡeɪʃənəl/", "vi": "thuộc nghĩa vụ ràng buộc; pháp lý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096420", "hw": "obligations", "pos": "noun", "ipa": "/ˌɑːblɪˈɡeɪʃənz/", "vi": "các nghĩa vụ; những bổn phận", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096421", "hw": "obligatorisch", "pos": "adj", "ipa": "/ɔbliɡaˈtoːʁɪʃ/", "vi": "mang tính bắt buộc theo luật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096422", "hw": "obligee", "pos": "noun", "ipa": "/ˌɑːblɪˈdʒiː/", "vi": "người có quyền đòi nợ nghĩa vụ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096423", "hw": "obligement", "pos": "noun", "ipa": "/əˈblaɪdʒmənt/", "vi": "ân huệ làm ơn; nghĩa vụ ràng buộc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096424", "hw": "obliger", "pos": "noun", "ipa": "/əˈblaɪdʒɚ/", "vi": "người làm ơn; người giúp đỡ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096425", "hw": "obliges", "pos": "verb", "ipa": "/əblˈaɪdʒɪz/", "vi": "bắt buộc; làm ơn giúp đỡ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096426", "hw": "obligingness", "pos": "noun", "ipa": "/əˈblaɪdʒɪŋnəs/", "vi": "tính hay giúp đỡ; sự sốt sắng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096427", "hw": "obligor", "pos": "noun", "ipa": "/ˌɑːblɪˈɡɔːr/", "vi": "bên có nghĩa vụ; người mang nợ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096428", "hw": "obliquation", "pos": "noun", "ipa": "/ˌɑːblɪˈkweɪʃən/", "vi": "độ nghiêng; sự đi lệch hướng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096429", "hw": "obliqueness", "pos": "noun", "ipa": "/əˈbliːknəs/", "vi": "tính xiên chéo; tính quanh co", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096430", "hw": "obliquitous", "pos": "adj", "ipa": "/əˈblɪkwɪtəs/", "vi": "nghiêng lệch; quanh co dối trá", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096431", "hw": "obliterable", "pos": "adj", "ipa": "/əˈblɪtərəbəl/", "vi": "có thể xóa sạch; có thể hủy bỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096432", "hw": "obliterates", "pos": "verb", "ipa": "/əblˈɪtəreɪts/", "vi": "xóa sạch dấu vết; tiêu diệt sạch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096433", "hw": "obliterating", "pos": "verb", "ipa": "/əblˈɪtəreɪtɪŋ/", "vi": "xóa sạch hoàn toàn; phá hủy sạch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096434", "hw": "obliterative", "pos": "adj", "ipa": "/əˈblɪtəreɪtɪv/", "vi": "có tính xóa sạch; gây bít mạch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096435", "hw": "obliviously", "pos": "adv", "ipa": "/əˈblɪviəsli/", "vi": "một cách thờ ơ vô tâm; không để ý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096436", "hw": "oblongish", "pos": "adj", "ipa": "/ˈɑːblɔːŋɪʃ/", "vi": "hơi thuôn dài; hơi giống chữ nhật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096437", "hw": "oblongly", "pos": "adv", "ipa": "/ˈɑːblɔːŋli/", "vi": "theo hình chữ nhật; có dạng thuôn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096438", "hw": "oblongness", "pos": "noun", "ipa": "/ˈɑːblɔːŋnəs/", "vi": "dạng thuôn dài; tính hình chữ nhật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096439", "hw": "obmutescence", "pos": "noun", "ipa": "/ˌɑːbmjuːˈtɛsəns/", "vi": "sự câm lặng cố ý; thái độ nín thinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096440", "hw": "obmutescent", "pos": "adj", "ipa": "/ˌɑːbmjuːˈtɛsənt/", "vi": "câm nín; cố giữ im lặng tuyệt đối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096441", "hw": "obnubilate", "pos": "verb", "ipa": "/ɑːbˈnuːbəleɪt/", "vi": "làm u ám; che mờ suy nghĩ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096442", "hw": "obnubilation", "pos": "noun", "ipa": "/ɑːbˌnuːbəˈleɪʃən/", "vi": "sự che mờ mịt; đầu óc u ám", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096443", "hw": "obol", "pos": "noun", "ipa": "/ˈoʊbɑːl/", "vi": "đồng obol bạc Hy Lạp cổ đại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096444", "hw": "obolus", "pos": "noun", "ipa": "/ˈɑːbələs/", "vi": "đồng xu obolus trả tiền đò Styx", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096445", "hw": "obovoid", "pos": "adj", "ipa": "/ɑːbˈoʊvɔɪd/", "vi": "có dạng hình quả trứng ngược", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096446", "hw": "obpyramidal", "pos": "adj", "ipa": "/ˌɑːbpɪˈræmɪdəl/", "vi": "có dạng hình tháp chóp ngược", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096447", "hw": "obpyriform", "pos": "adj", "ipa": "/ˌɑːbˈpɪrəfɔːrm/", "vi": "có dạng hình quả lê ngược", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096448", "hw": "obscurant", "pos": "noun", "ipa": "/ˈɑːbskjʊrənt/", "vi": "người theo chủ nghĩa ngu dân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096449", "hw": "obscurantic", "pos": "adj", "ipa": "/ˌɑːbskjʊˈræntɪk/", "vi": "thuộc chủ nghĩa ngu dân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096450", "hw": "obscuration", "pos": "noun", "ipa": "/ˌɑːbskjʊˈreɪʃən/", "vi": "sự che tối mịt; hiện tượng lu mờ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096451", "hw": "obscured", "pos": "verb", "ipa": "/əbˈskjʊrd/", "vi": "đã che khuất; làm mờ tầm nhìn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096452", "hw": "obscureness", "pos": "noun", "ipa": "/əbˈskjʊrnəs/", "vi": "sự tối tăm u ẩn; cảnh vô danh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096453", "hw": "obscures", "pos": "verb", "ipa": "/əbˈskjʊrz/", "vi": "che khuất; làm mờ mịt; làm lu mờ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096454", "hw": "obscuring", "pos": "verb", "ipa": "/əbˈskjʊrɪŋ/", "vi": "che khuất; làm lu mờ; làm mù mịt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096455", "hw": "obsecration", "pos": "noun", "ipa": "/ˌɑːbsəˈkreɪʃən/", "vi": "lời cầu xin tha thiết; sự khẩn cầu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096456", "hw": "obsequial", "pos": "adj", "ipa": "/əbˈsiːkwiəl/", "vi": "thuộc lễ tang; nghi thức đám tang", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096457", "hw": "obsequies", "pos": "noun", "ipa": "/ˈɑːbsəkwiz/", "vi": "những nghi lễ mai táng; tang lễ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096458", "hw": "obsequy", "pos": "noun", "ipa": "/ˈɑːbsəkwi/", "vi": "lễ an táng; nghi thức đám ma", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096459", "hw": "observability", "pos": "noun", "ipa": "/əbˌzɜːrvəˈbɪləti/", "vi": "khả năng quan sát được; giám sát", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096460", "hw": "observances", "pos": "noun", "ipa": "/əbˈzɜːrvənsɪz/", "vi": "sự tuân thủ; các nghi thức lễ tiết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096461", "hw": "observancy", "pos": "noun", "ipa": "/əbˈzɜːrvənsi/", "vi": "sự cẩn trọng tuân thủ quy tắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096462", "hw": "observantly", "pos": "adv", "ipa": "/əbˈzɜːrvəntli/", "vi": "một cách tinh ý; rất chăm chú", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096463", "hw": "observations", "pos": "noun", "ipa": "/ˌɑːbzɚˈveɪʃənz/", "vi": "những quan sát; nhận xét nhận định", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096464", "hw": "observers", "pos": "noun", "ipa": "/əbˈzɜːrvɚz/", "vi": "những quan sát viên; người theo dõi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096465", "hw": "observes", "pos": "verb", "ipa": "/əbˈzɜːrvz/", "vi": "quan sát; theo dõi; tuân thủ luật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096466", "hw": "observingly", "pos": "adv", "ipa": "/əbˈzɜːrvɪŋli/", "vi": "một cách tinh ý; quan sát kỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096467", "hw": "obsesses", "pos": "verb", "ipa": "/əbˈsɛsɪz/", "vi": "ám ảnh tâm trí; trăn trở", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096468", "hw": "obsessing", "pos": "verb", "ipa": "/əbˈsɛsɪŋ/", "vi": "ám ảnh thường trực; vướng bận lòng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096469", "hw": "obsessionally", "pos": "adv", "ipa": "/əbˈsɛʃənəli/", "vi": "một cách ám ảnh cưỡng chế", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096470", "hw": "obsessivity", "pos": "noun", "ipa": "/ˌɑːbsɛˈsɪvəti/", "vi": "tính ám ảnh; xu hướng ám ảnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096471", "hw": "obsidianal", "pos": "adj", "ipa": "/əbˈsɪdiənəl/", "vi": "thuộc cuộc vây hãm; hãm thành", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096472", "hw": "obsolesce", "pos": "verb", "ipa": "/ˌɑːbsəˈlɛs/", "vi": "dần trở nên lỗi thời; mai một dần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096473", "hw": "obsolescently", "pos": "adv", "ipa": "/ˌɑːbsəˈlɛsəntli/", "vi": "một cách dần lỗi thời; thoái trào", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096474", "hw": "obsolescentness", "pos": "noun", "ipa": "/ˌɑːbsəˈlɛsəntnəs/", "vi": "tình trạng đang dần thoái trào", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096475", "hw": "obsoleteness", "pos": "noun", "ipa": "/ˌɑːbsəˈliːtnəs/", "vi": "tính lỗi thời; sự lạc hậu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096476", "hw": "obsoletism", "pos": "noun", "ipa": "/ˈɑːbsəliːtɪzəm/", "vi": "từ ngữ cổ lỗi thời; thói dùng cổ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096477", "hw": "obstinateness", "pos": "noun", "ipa": "/ˈɑːbstɪnətnəs/", "vi": "tính bướng bỉnh; sự ngoan cố", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096478", "hw": "obstipant", "pos": "noun", "ipa": "/ˈɑːbstɪpənt/", "vi": "thuốc cầm tiêu chảy; thuốc trị lỏng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096479", "hw": "obstipate", "pos": "verb", "ipa": "/ˈɑːbstɪpeɪt/", "vi": "làm táo bón nặng; gây tắc ruột", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096480", "hw": "obstipation", "pos": "noun", "ipa": "/ˌɑːbstɪˈpeɪʃən/", "vi": "chứng táo bón nặng do tắc ruột", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096481", "hw": "obstreperously", "pos": "adv", "ipa": "/əbˈstrɛpərəsli/", "vi": "một cách ngỗ ngược om sòm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096482", "hw": "obstreperousness", "pos": "noun", "ipa": "/əbˈstrɛpərəsnəs/", "vi": "sự ngỗ ngược; thói hung hăng om sòm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096483", "hw": "obstructer", "pos": "noun", "ipa": "/əbˈstrʌktɚ/", "vi": "người cản trở; kẻ gây tắc nghẽn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096484", "hw": "obstructing", "pos": "verb", "ipa": "/əbˈstrʌktɪŋ/", "vi": "cản trở; gây tắc nghẽn; chắn ngang", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096485", "hw": "obstructively", "pos": "adv", "ipa": "/əbˈstrʌktɪvli/", "vi": "với ý đồ cản trở gây khó khăn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096486", "hw": "obstructiveness", "pos": "noun", "ipa": "/əbˈstrʌktɪvnəs/", "vi": "tính thích gây cản trở bế tắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096487", "hw": "obstructor", "pos": "noun", "ipa": "/əbˈstrʌktɚ/", "vi": "vật cản trở; người ngăn trở", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096488", "hw": "obstructs", "pos": "verb", "ipa": "/əbˈstrʌkts/", "vi": "cản trở; gây nghẽn; bịt kín lối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096489", "hw": "obtained", "pos": "verb", "ipa": "/əbˈteɪnd/", "vi": "đã giành được; đã lấy được giấy tờ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096490", "hw": "obtainer", "pos": "noun", "ipa": "/əbˈteɪnɚ/", "vi": "người thu nhận; người đạt được", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096491", "hw": "obtaining", "pos": "verb", "ipa": "/əbˈteɪnɪŋ/", "vi": "đạt được; thu thập; đang thịnh hành", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096492", "hw": "obtains", "pos": "verb", "ipa": "/əbˈteɪnz/", "vi": "đạt được; hiện hành; giữ nguyên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096493", "hw": "obtect", "pos": "adj", "ipa": "/ɑːbˈtɛkt/", "vi": "có màng vỏ bọc bảo vệ quanh nhộng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096494", "hw": "obtected", "pos": "adj", "ipa": "/ɑːbˈtɛktɪd/", "vi": "được bao bọc màng nhộng kín", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096495", "hw": "obtention", "pos": "noun", "ipa": "/əbˈtɛnʃən/", "vi": "sự thu được; việc xin cấp phép được", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096496", "hw": "obtest", "pos": "verb", "ipa": "/ɑːbˈtɛst/", "vi": "tha thiết van xin; khẩn cầu thề bồi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096497", "hw": "obtestation", "pos": "noun", "ipa": "/ˌɑːbtɛˈsteɪʃən/", "vi": "lời khẩn cầu tha thiết thề bồi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096498", "hw": "obtruder", "pos": "noun", "ipa": "/əbˈtruːdɚ/", "vi": "kẻ thích can dự đường đột", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096499", "hw": "obtruncate", "pos": "verb", "ipa": "/ɑːbˈtrʌŋkeɪt/", "vi": "chặt cụt ngọn cây; đốn ngọn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096500", "hw": "obtrusion", "pos": "noun", "ipa": "/əbˈtruːʒən/", "vi": "sự đường đột can thiệp; xông xáo ép", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096501", "hw": "obtrusiveness", "pos": "noun", "ipa": "/əbˈtruːsɪvnəs/", "vi": "sự lộ liễu phô trương; thói sỗ sàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
]

assert len(part5_data) == 100, f"Expected 100 items, got {len(part5_data)}"

valid_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

with open("scratch/b20_r03_raw_p5.json") as f:
    raw_p5 = json.load(f)

for i, (item, raw) in enumerate(zip(part5_data, raw_p5)):
    assert item["id"] == raw["id"], f"ID mismatch at {i}: {item['id']} vs {raw['id']}"
    assert item["hw"] == raw["hw"], f"HW mismatch at {i}: {item['hw']} vs {raw['hw']}"
    assert item["pos"] in valid_pos, f"Invalid POS at {i}: {item['pos']}"
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/"), f"Invalid IPA slashes at {i}: {item['ipa']}"
    assert item["ipa"].count("/") == 2, f"IPA does not have exactly 2 slashes at {i}: {item['ipa']}"
    assert not item["ipa"].startswith("/ ") and not item["ipa"].endswith(" /"), f"IPA boundary spaces at {i}: {item['ipa']}"
    assert len(item["vi"]) <= 35, f"vi too long at {i} ({item['hw']}): {item['vi']} (len={len(item['vi'])})"
    assert len(item["vi"]) > 0, f"Empty vi at {i}"
    assert not any(art in item["vi"] for art in ["Số nhiều", "Xem ", "Dạng ", "Viết tắt", "Động từ chia", "%%"]), f"Crawler artifact in vi at {i}: {item['vi']}"
    assert item["status"] == "reviewed", f"Status not reviewed at {i}"

with open("scratch/b20_r03_p5.json", "w") as f:
    json.dump(part5_data, f, ensure_ascii=False, indent=2)

print("Batch 20 Round 3 Part 5 validated and saved successfully!")
