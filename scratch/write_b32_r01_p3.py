# -*- coding: utf-8 -*-
import json

part3_data = [
  {"id": "lex.en.200k.055202", "hw": "punics", "pos": "noun", "ipa": "/ˈpjuːnɪks/", "vi": "tiếng Punic và người Carthage cổ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055203", "hw": "reinvigorates", "pos": "verb", "ipa": "/ˌriːɪnˈvɪɡəreɪts/", "vi": "tiếp thêm sinh lực; làm hồi sinh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055204", "hw": "reinvigorating", "pos": "verb", "ipa": "/ˌriːɪnˈvɪɡəreɪtɪŋ/", "vi": "đang tiếp thêm sinh lực mới", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055205", "hw": "reuptakes", "pos": "noun", "ipa": "/riːˈʌpteɪks/", "vi": "sự tái hấp thu chất dẫn truyền", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055206", "hw": "santees", "pos": "noun", "ipa": "/sænˈtiːz/", "vi": "người Santee Dakota da đỏ Bắc Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055207", "hw": "satanists", "pos": "noun", "ipa": "/ˈseɪtənɪsts/", "vi": "những người theo giáo phái Satan", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055208", "hw": "seraphs", "pos": "noun", "ipa": "/ˈsɛrəfs/", "vi": "thiên thần luyến thần sáu cánh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055209", "hw": "serfs", "pos": "noun", "ipa": "/sɜːrfs/", "vi": "nông nô thời phong kiến xưa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055210", "hw": "shishas", "pos": "noun", "ipa": "/ˈʃiːʃəz/", "vi": "bình hút thuốc lào shisha Ả Rập", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055211", "hw": "shostakoviches", "pos": "noun", "ipa": "/ˌʃɒstəˈkoʊvɪtʃɪz/", "vi": "nhà soạn nhạc Dmitri Shostakovich", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055212", "hw": "similes", "pos": "noun", "ipa": "/ˈsɪməliz/", "vi": "các phép so sánh trong văn chương", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055213", "hw": "sitars", "pos": "noun", "ipa": "/sɪˈtɑːrz/", "vi": "đàn sitar dây dài truyền thống Ấn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055214", "hw": "slushier", "pos": "adj", "ipa": "/ˈslʌʃiər/", "vi": "lầy lội tuyết tan hơn; sướt mướt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055215", "hw": "slushiest", "pos": "adj", "ipa": "/ˈslʌʃiɪst/", "vi": "lầy lội tuyết tan nhất; ướt át", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055216", "hw": "snowshoeing", "pos": "verb", "ipa": "/ˈsnoʊʃuːɪŋ/", "vi": "đang đi bộ trên tuyết bằng vợt", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055217", "hw": "snowshoes", "pos": "noun", "ipa": "/ˈsnoʊʃuːz/", "vi": "những chiếc vợt đi trên tuyết", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055218", "hw": "stillbirths", "pos": "noun", "ipa": "/ˈstɪlbɜːrθs/", "vi": "các ca thai chết lưu trong bụng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055219", "hw": "stressors", "pos": "noun", "ipa": "/ˈstrɛsərz/", "vi": "các tác nhân gây căng thẳng tâm lý", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055220", "hw": "striatums", "pos": "noun", "ipa": "/straɪˈeɪtəmz/", "vi": "thể vân trong nhân nền của não", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055221", "hw": "sufisms", "pos": "noun", "ipa": "/ˈsuːfɪzəmz/", "vi": "chủ nghĩa thần bí Sufi Hồi giáo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055222", "hw": "sultanas", "pos": "noun", "ipa": "/sʌlˈtɑːnəz/", "vi": "nho khô vàng không hạt; hoàng hậu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055223", "hw": "svrs", "pos": "noun", "ipa": "/ˌɛs.viːˈɑːrz/", "vi": "Cơ quan Tình báo Đối ngoại Nga SVR", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055224", "hw": "switchblades", "pos": "noun", "ipa": "/ˈswɪtʃbleɪdz/", "vi": "những con dao bấm lò xo bật nhanh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055225", "hw": "trespassers", "pos": "noun", "ipa": "/ˈtrɛspəsərz/", "vi": "những kẻ xâm phạm đất tư trái phép", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055226", "hw": "truisms", "pos": "noun", "ipa": "/ˈtruːɪzəmz/", "vi": "những chân lý hiển nhiên rõ ràng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055227", "hw": "trumbos", "pos": "noun", "ipa": "/ˈtrʌmboʊz/", "vi": "nhà biên kịch Dalton Trumbo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055228", "hw": "vallettas", "pos": "noun", "ipa": "/vəˈlɛtəz/", "vi": "thành phố Valletta thủ đô Malta", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055229", "hw": "varuses", "pos": "noun", "ipa": "/ˈvɛərəsɪz/", "vi": "chứng dị tật vẹo trong bàn chân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055230", "hw": "vulgates", "pos": "noun", "ipa": "/ˈvʌlɡeɪts/", "vi": "bản dịch Kinh Thánh tiếng Latinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055231", "hw": "wagoners", "pos": "noun", "ipa": "/ˈwæɡənərz/", "vi": "những người lái xe ngựa chở hàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055232", "hw": "yazoos", "pos": "noun", "ipa": "/ˈjæzuːz/", "vi": "dòng sông Yazoo ở bang Mississippi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055233", "hw": "zachariases", "pos": "noun", "ipa": "/ˌzækəˈraɪəsɪz/", "vi": "ngôn sứ Zacharias trong Kinh Thánh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055234", "hw": "zestier", "pos": "adj", "ipa": "/ˈzɛstiər/", "vi": "đậm đà hơn; hăng say hứng thú hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055235", "hw": "zestiest", "pos": "adj", "ipa": "/ˈzɛstiɪst/", "vi": "đậm đà nhất; hứng khởi nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055236", "hw": "zunis", "pos": "noun", "ipa": "/ˈzuːnjiz/", "vi": "người da đỏ Zuni ở New Mexico", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055237", "hw": "alpha methyl dopa", "pos": "phrase", "ipa": "/ˈælfə ˈmɛθəl ˈdoʊpə/", "vi": "thuốc hạ huyết áp methyldopa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055238", "hw": "amicus curiae", "pos": "phrase", "ipa": "/əˈmiːkəs ˈkjʊriiː/", "vi": "người bạn của tòa án tư vấn luật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055239", "hw": "amicus curiae brief", "pos": "phrase", "ipa": "/əˈmiːkəs ˈkjʊriiː briːf/", "vi": "văn bản ý kiến tư vấn của tòa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055240", "hw": "antimalarial drug", "pos": "phrase", "ipa": "/ˌæntiməˈlɛəriəl drʌɡ/", "vi": "thuốc đặc trị phòng bệnh sốt rét", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055241", "hw": "antonius stradivarius", "pos": "phrase", "ipa": "/ænˈtoʊniəs ˌstrædɪˈvɛəriəs/", "vi": "nghệ nhân làm đàn Stradivarius", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055242", "hw": "arthur edwin kennelly", "pos": "phrase", "ipa": "/ˈɑːrθər ˈɛdwɪn ˈkɛnəli/", "vi": "kỹ sư điện Arthur Edwin Kennelly", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055243", "hw": "augustinian hermits", "pos": "phrase", "ipa": "/ɔːɡʌˈstɪniən ˈhɜːrmɪts/", "vi": "các tu sĩ dòng ẩn tu Augustinô", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055244", "hw": "bakke decision", "pos": "phrase", "ipa": "/ˈbɑːki dɪˈsɪʒən/", "vi": "phán quyết tuyển sinh Bakke", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055245", "hw": "battle of zama", "pos": "phrase", "ipa": "/ˈbætəl əv ˈzɑːmə/", "vi": "trận chiến lịch sử Zama Bắc Phi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055246", "hw": "beef stroganoff", "pos": "phrase", "ipa": "/biːf ˈstrɔːɡənɔːf/", "vi": "món thịt bò xào sốt Stroganoff", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055247", "hw": "begonia rex", "pos": "phrase", "ipa": "/bɪˈɡoʊniə rɛks/", "vi": "cây thu hải đường lá hoa văn Rex", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055248", "hw": "bullhead catfish", "pos": "phrase", "ipa": "/ˈbʊlhɛd ˈkætfɪʃ/", "vi": "loài cá nheo đầu bẹt nước ngọt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055249", "hw": "camillo golgi", "pos": "phrase", "ipa": "/kəˈmiːloʊ ˈɡɔːldʒi/", "vi": "bác sĩ Nobel Y học Camillo Golgi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055250", "hw": "cephalic index", "pos": "phrase", "ipa": "/sɪˈfælɪk ˈɪndɛks/", "vi": "chỉ số hình thái sọ đầu người", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055251", "hw": "civet cat", "pos": "phrase", "ipa": "/ˈsɪvɪt kæt/", "vi": "loài cầy hương; cầy đốm châu Á", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055252", "hw": "classical haemophilia", "pos": "phrase", "ipa": "/ˈklæsɪkəl ˌhiːməˈfɪliə/", "vi": "bệnh ưa chảy máu cổ điển dạng A", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055253", "hw": "cyclic neutropenia", "pos": "phrase", "ipa": "/ˈsaɪklɪk ˌnuːtrəˈpiːniə/", "vi": "giảm bạch cầu đa nhân có chu kỳ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055254", "hw": "disseminated lupus erythematosus", "pos": "phrase", "ipa": "/dɪˈsɛmɪneɪtɪd ˈluːpəs ˌɛrɪˌθiːməˈtoʊsəs/", "vi": "bệnh lupus ban đỏ rải rác hệ thống", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055255", "hw": "dowsing rod", "pos": "phrase", "ipa": "/ˈdaʊzɪŋ rɑːd/", "vi": "que dò tìm mạch nước ngầm kim loại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055256", "hw": "duodenal smear", "pos": "phrase", "ipa": "/ˌdjuːəˈdiːnəl smɪər/", "vi": "mẫu phết tế bào dịch tá tràng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055257", "hw": "eared grebe", "pos": "phrase", "ipa": "/ɪərd ɡriːb/", "vi": "loài chim lặn có chỏm lông tai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055258", "hw": "entrenching tool", "pos": "phrase", "ipa": "/ɪnˈtrɛntʃɪŋ tuːl/", "vi": "xẻng bộ binh đào công sự gấp gọn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055259", "hw": "eugene paul wigner", "pos": "phrase", "ipa": "/juːˈdʒiːn pɔːl ˈwɪɡnər/", "vi": "nhà vật lý Nobel Eugene Wigner", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055260", "hw": "eugene wigner", "pos": "phrase", "ipa": "/juːˈdʒiːn ˈwɪɡnər/", "vi": "nhà vật lý lý thuyết Eugene Wigner", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055261", "hw": "fettuccine alfredo", "pos": "phrase", "ipa": "/ˌfɛtʊˈtʃiːni ælˈfreɪdoʊ/", "vi": "mì dẹt sốt bơ kem béo Alfredo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055262", "hw": "gas maser", "pos": "phrase", "ipa": "/ɡæs ˈmeɪzər/", "vi": "thiết bị maser kích thích bằng khí", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055263", "hw": "genus amanita", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌæməˈnaɪtə/", "vi": "chi nấm tán độc Amanita rừng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055264", "hw": "genus begonia", "pos": "phrase", "ipa": "/ˈdʒiːnəs bɪˈɡoʊniə/", "vi": "chi cây hoa Thu hải đường", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055265", "hw": "glutathione peroxidase", "pos": "phrase", "ipa": "/ˌɡluːtəˈθaɪoʊn pəˈrɑːksɪdeɪs/", "vi": "men chống oxy hóa glutathione", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055266", "hw": "haemorrhagic fever", "pos": "phrase", "ipa": "/ˌhɛməˈrædʒɪk ˈfiːvər/", "vi": "bệnh sốt xuất huyết truyền nhiễm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055267", "hw": "haemorrhagic stroke", "pos": "phrase", "ipa": "/ˌhɛməˈrædʒɪk stroʊk/", "vi": "tai biến đột quỵ xuất huyết não", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055268", "hw": "hans albrecht bethe", "pos": "phrase", "ipa": "/hæns ˈælbrɛkt ˈbeɪtə/", "vi": "nhà vật lý Nobel Hans Bethe", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055269", "hw": "heinrich von kleist", "pos": "phrase", "ipa": "/ˈhaɪnrɪç fɔn klaɪst/", "vi": "nhà thơ Đức Heinrich von Kleist", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055270", "hw": "herbert marcuse", "pos": "phrase", "ipa": "/ˈhɜːrbərt mɑːrˈkuːzə/", "vi": "triết gia Herbert Marcuse Đức", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055271", "hw": "horseradish peroxidase", "pos": "phrase", "ipa": "/ˈhɔːrsrædɪʃ pəˈrɑːksɪdeɪs/", "vi": "men peroxidase từ củ cải ngựa HRP", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055272", "hw": "isthmian games", "pos": "phrase", "ipa": "/ˈɪsmiən ɡeɪmz/", "vi": "đại hội thể thao Isthmia Hy Lạp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055273", "hw": "japanese poinsettia", "pos": "phrase", "ipa": "/ˌdʒæpəˈniːz pɔɪnˈsɛtiə/", "vi": "cây trạng nguyên Nhật Bản lá đỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055274", "hw": "jewelled headdress", "pos": "phrase", "ipa": "/ˈdʒuːəld ˈhɛddrɛs/", "vi": "vương miện khăn đội đầu nạm ngọc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055275", "hw": "kidney begonia", "pos": "phrase", "ipa": "/ˈkɪdni bɪˈɡoʊniə/", "vi": "cây thu hải đường lá hình quả thận", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055276", "hw": "kingwood tree", "pos": "phrase", "ipa": "/ˈkɪŋwʊd triː/", "vi": "cây gỗ cẩm lai cẩm chỉ quý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055277", "hw": "kudu lily", "pos": "phrase", "ipa": "/ˈkuːduː ˈlɪli/", "vi": "loài hoa huệ kudu sứ sa mạc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055278", "hw": "kudzu vine", "pos": "phrase", "ipa": "/ˈkʊdzuː vaɪn/", "vi": "dây sắn dây củ ngọt leo giàn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055279", "hw": "lacrimal apparatus", "pos": "phrase", "ipa": "/ˈlækrɪməl ˌæpəˈrætəs/", "vi": "hệ thống tuyến tiết và dẫn lệ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055280", "hw": "lacrimal artery", "pos": "phrase", "ipa": "/ˈlækrɪməl ˈɑːrtəri/", "vi": "động mạch tuyến lệ ở mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055281", "hw": "lacrimal sac", "pos": "phrase", "ipa": "/ˈlækrɪməl sæk/", "vi": "túi lệ chứa nước mắt ở hốc mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055282", "hw": "lacrimal vein", "pos": "phrase", "ipa": "/ˈlækrɪməl veɪn/", "vi": "tĩnh mạch tuyến lệ của mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055283", "hw": "large civet", "pos": "phrase", "ipa": "/lɑːrdʒ ˈsɪvɪt/", "vi": "loài cầy hương lớn Ấn Độ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055284", "hw": "lassa fever", "pos": "phrase", "ipa": "/ˈlæsə ˈfiːvər/", "vi": "bệnh sốt xuất huyết Lassa virus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055285", "hw": "lassa virus", "pos": "phrase", "ipa": "/ˈlæsə ˈvaɪrəs/", "vi": "vi-rút Lassa gây sốt xuất huyết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055286", "hw": "litter lout", "pos": "phrase", "ipa": "/ˈlɪtər laʊt/", "vi": "kẻ thiếu ý thức vứt rác bừa bãi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055287", "hw": "malayan tapir", "pos": "phrase", "ipa": "/məˈleɪən ˈteɪpər/", "vi": "loài heo vòi lông khoang Mã Lai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055288", "hw": "marquesas islands", "pos": "phrase", "ipa": "/mɑːrˈkeɪsəs ˈaɪləndz/", "vi": "quần đảo Marquesas Thái Bình Dương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055289", "hw": "merce cunningham", "pos": "phrase", "ipa": "/mɜːrs ˈkʌnɪŋhæm/", "vi": "biên đạo múa Merce Cunningham", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055290", "hw": "nares deep", "pos": "phrase", "ipa": "/nɛərz diːp/", "vi": "vực sâu thẳm Nares ở Đại Tây Dương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055291", "hw": "nonparametric statistic", "pos": "phrase", "ipa": "/ˌnɑːnpærəˈmɛtrɪk stəˈtɪstɪk/", "vi": "thống kê phi tham số kiểm định", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055292", "hw": "nucleon number", "pos": "phrase", "ipa": "/ˈnuːkliɑːn ˈnʌmbər/", "vi": "số khối nucleon trong hạt nhân", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055293", "hw": "octal digit", "pos": "phrase", "ipa": "/ˈɑːktəl ˈdɪdʒɪt/", "vi": "chữ số hệ bát phân từ 0 đến 7", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055294", "hw": "oesophageal veins", "pos": "phrase", "ipa": "/ɪˌsɑːfəˈdʒiːəl veɪnz/", "vi": "các tĩnh mạch thực quản dẫn máu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055295", "hw": "opencast mining", "pos": "phrase", "ipa": "/ˈoʊpənkæst ˈmaɪnɪŋ/", "vi": "việc khai thác mỏ lộ thiên", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055296", "hw": "palm civet", "pos": "phrase", "ipa": "/pɑːm ˈsɪvɪt/", "vi": "loài cầy vòi hương ăn quả cọ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055297", "hw": "pelham grenville wodehouse", "pos": "phrase", "ipa": "/ˈpɛləm ˈɡrɛnvɪl ˈwʊdhaʊs/", "vi": "nhà văn hài P. G. Wodehouse", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055298", "hw": "perineal artery", "pos": "phrase", "ipa": "/ˌpɛrɪˈniːəl ˈɑːrtəri/", "vi": "động mạch đáy chậu cung cấp máu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055299", "hw": "phlox bifida", "pos": "phrase", "ipa": "/flɑːks ˈbɪfɪdə/", "vi": "cây hoa giáp trúc đào cánh chẻ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055300", "hw": "poinsettia strain", "pos": "phrase", "ipa": "/pɔɪnˈsɛtiə streɪn/", "vi": "chủng vi-rút trên cây trạng nguyên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055301", "hw": "polyhedral angle", "pos": "phrase", "ipa": "/ˌpɑːliˈhiːdrəl ˈæŋɡəl/", "vi": "góc đa diện tạo bởi các mặt phẳng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part3_data) == 100, f"Length is {len(part3_data)}"

with open('scratch/b32_r01_raw_p3.json') as f:
    raw = json.load(f)

for i, (item, raw_item) in enumerate(zip(part3_data, raw)):
    assert item['id'] == raw_item['id'], f"ID mismatch at {i}: {item['id']} vs {raw_item['id']}"
    assert item['hw'] == raw_item['hw'], f"HW mismatch at {i}: {item['hw']} vs {raw_item['hw']}"
    assert list(item.keys()) == expected_keys, f"Keys mismatch at {i}: {list(item.keys())}"
    assert item['pos'] in allowed_pos, f"pos invalid at {i}: {item['pos']}"
    assert len(item['vi']) <= 35, f"vi too long ({len(item['vi'])} chars) at {i}: {item['vi']}"
    assert item['status'] == 'reviewed'
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and len(item['ipa']) > 2, f"invalid ipa at {i}: {item['ipa']}"
    if ';' in item['vi']:
        for seg in item['vi'].split(';')[1:]:
            assert seg.startswith(' '), f"missing space after semicolon at {i}: {item['vi']}"

with open('scratch/b32_r01_p3.json', 'w', encoding='utf-8') as f:
    json.dump(part3_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 3")
