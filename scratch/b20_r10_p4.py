import json

# Manual QA review for Batch 20 Round 10 Part 4 (099802 to 099901)
part4_data = [
  {"id": "lex.en.100k.099802", "hw": "pats", "pos": "verb", "ipa": "/pæts/", "vi": "vỗ nhẹ; xoa nhẹ", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099803", "hw": "patted", "pos": "verb", "ipa": "/ˈpætɪd/", "vi": "đã vỗ nhẹ; đã vỗ về", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099804", "hw": "pattered", "pos": "verb", "ipa": "/ˈpætərd/", "vi": "đã rơi lộp độp; đã bước rộn rã", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099805", "hw": "patterer", "pos": "noun", "ipa": "/ˈpætərər/", "vi": "người rao bán liến thoắng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099806", "hw": "pattering", "pos": "noun", "ipa": "/ˈpætərɪŋ/", "vi": "tiếng rơi lộp độp; bước thoăn thoắt", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099807", "hw": "patternable", "pos": "adj", "ipa": "/ˈpætərnəbəl/", "vi": "có thể mô phỏng theo mẫu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099808", "hw": "patterning", "pos": "noun", "ipa": "/ˈpætərnɪŋ/", "vi": "cách bố trí hoa văn họa tiết", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099809", "hw": "patterns", "pos": "noun", "ipa": "/ˈpætərnz/", "vi": "các hoa văn; các khuôn mẫu định sẵn", "cefr": "A2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099810", "hw": "patters", "pos": "verb", "ipa": "/ˈpætərz/", "vi": "rơi lộp độp; nói liến thoắng", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099811", "hw": "patting", "pos": "noun", "ipa": "/ˈpætɪŋ/", "vi": "động tác vỗ nhẹ; cử chỉ vuốt ve", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099812", "hw": "pattypan", "pos": "noun", "ipa": "/ˈpætipæn/", "vi": "khuôn bánh nhỏ; quả bí đĩa bay", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099813", "hw": "patulent", "pos": "adj", "ipa": "/ˈpætʃʊlənt/", "vi": "xòe rộng ra; nở rộng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099814", "hw": "patulous", "pos": "adj", "ipa": "/ˈpætʃʊləs/", "vi": "xòe rộng; vươn cành tỏa rộng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099815", "hw": "patulously", "pos": "adv", "ipa": "/ˈpætʃʊləsli/", "vi": "theo dạng xòe rộng tỏa ra", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099816", "hw": "patulousness", "pos": "noun", "ipa": "/ˈpætʃʊləsnəs/", "vi": "tình trạng xòe rộng; sự mở rộng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099817", "hw": "patwin", "pos": "noun", "ipa": "/ˈpætwɪn/", "vi": "người bản xứ Patwin (California)", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099818", "hw": "pauchiness", "pos": "noun", "ipa": "/ˈpɔːtʃinəs/", "vi": "tình trạng bụng béo phệ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099819", "hw": "pauciflorous", "pos": "adj", "ipa": "/ˌpɔːsɪˈflɔːrəs/", "vi": "ít hoa; hoa mọc thưa thớt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099820", "hw": "paucifoliate", "pos": "adj", "ipa": "/ˌpɔːsɪˈfoʊliɪt/", "vi": "ít lá; cành thưa lá", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099821", "hw": "paucilocular", "pos": "adj", "ipa": "/ˌpɔːsɪˈlɑːkjələr/", "vi": "có ít ngăn; có vài khoang nhỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099822", "hw": "paucinervate", "pos": "adj", "ipa": "/ˌpɔːsɪˈnɜːrveɪt/", "vi": "gân lá thưa thớt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099823", "hw": "paunched", "pos": "adj", "ipa": "/pɔːntʃt/", "vi": "có bụng phệ; to bụng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099824", "hw": "paunches", "pos": "noun", "ipa": "/ˈpɔːntʃɪz/", "vi": "các bụng phệ; dạ cỏ động vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099825", "hw": "paunchiness", "pos": "noun", "ipa": "/ˈpɔːntʃinəs/", "vi": "tình trạng béo bụng phệ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099826", "hw": "paunching", "pos": "noun", "ipa": "/ˈpɔːntʃɪŋ/", "vi": "việc mổ bụng bỏ ruột súc vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099827", "hw": "pauperisation", "pos": "noun", "ipa": "/ˌpɔːpəraɪˈzeɪʃən/", "vi": "sự bần cùng hóa tầng lớp nghèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099828", "hw": "pauperise", "pos": "verb", "ipa": "/ˈpɔːpəraɪz/", "vi": "bần cùng hóa; làm cho khánh kiệt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099829", "hw": "pauperised", "pos": "adj", "ipa": "/ˈpɔːpəraɪzd/", "vi": "bị bần cùng hóa; kiệt quệ cơ hàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099830", "hw": "pauperises", "pos": "verb", "ipa": "/ˈpɔːpəraɪzɪz/", "vi": "bần cùng hóa; làm cho kiệt quệ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099831", "hw": "pauperising", "pos": "verb", "ipa": "/ˈpɔːpəraɪzɪŋ/", "vi": "đang bần cùng hóa dân nghèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099832", "hw": "pauperize", "pos": "verb", "ipa": "/ˈpɔːpəraɪz/", "vi": "bần cùng hóa; làm cho khánh kiệt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099833", "hw": "pauperized", "pos": "adj", "ipa": "/ˈpɔːpəraɪzd/", "vi": "bị bần cùng hóa; khánh kiệt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099834", "hw": "pauperizes", "pos": "verb", "ipa": "/ˈpɔːpəraɪzɪz/", "vi": "bần cùng hóa; đẩy vào cảnh nghèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099835", "hw": "pauperizing", "pos": "verb", "ipa": "/ˈpɔːpəraɪzɪŋ/", "vi": "đang đẩy vào cảnh bần cùng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099836", "hw": "pauropoda", "pos": "noun", "ipa": "/pɔːˈrɒpədə/", "vi": "lớp động vật chân ít Pauropoda", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099837", "hw": "paused", "pos": "verb", "ipa": "/pɔːzd/", "vi": "đã tạm dừng; đã ngập ngừng", "cefr": "A2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099838", "hw": "pauses", "pos": "noun", "ipa": "/ˈpɔːzɪz/", "vi": "các quãng ngắt nghỉ; chỗ tạm dừng", "cefr": "A2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099839", "hw": "pausing", "pos": "noun", "ipa": "/ˈpɔːzɪŋ/", "vi": "sự tạm ngưng; thái độ ngập ngừng", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099840", "hw": "pavage", "pos": "noun", "ipa": "/ˈpeɪvɪdʒ/", "vi": "thuế lát đường; phí tu bổ đường", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099841", "hw": "paver", "pos": "noun", "ipa": "/ˈpeɪvər/", "vi": "thợ lát đường; máy lát mặt đường", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099842", "hw": "paves", "pos": "verb", "ipa": "/peɪvz/", "vi": "lát đá; mở đường dẫn lối", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099843", "hw": "pavingstone", "pos": "noun", "ipa": "/ˈpeɪvɪŋstoʊn/", "vi": "phiến đá lát đường", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099844", "hw": "pavingstones", "pos": "noun", "ipa": "/ˈpeɪvɪŋstoʊnz/", "vi": "các phiến đá lát mặt đường", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099845", "hw": "pavior", "pos": "noun", "ipa": "/ˈpeɪvjər/", "vi": "thợ lát vỉa hè; phiến đá lát hè", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099846", "hw": "paviour", "pos": "noun", "ipa": "/ˈpeɪvjər/", "vi": "thợ lát vỉa hè; phiến đá lát hè", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099847", "hw": "pavise", "pos": "noun", "ipa": "/ˈpævɪs/", "vi": "khiên lớn che thân của xạ thủ nỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099848", "hw": "pavonine", "pos": "adj", "ipa": "/ˈpævənaɪn/", "vi": "óng ánh rực rỡ như đuôi chim công", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099849", "hw": "pawed", "pos": "verb", "ipa": "/pɔːd/", "vi": "đã cào móng vuốt; đã sờ soạng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099850", "hw": "pawer", "pos": "noun", "ipa": "/ˈpɔːər/", "vi": "kẻ hay sờ mó thô lỗ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099851", "hw": "pawing", "pos": "noun", "ipa": "/ˈpɔːɪŋ/", "vi": "hành động cào vuốt; việc dẫm móng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099852", "hw": "pawkily", "pos": "adv", "ipa": "/ˈpɔːkɪli/", "vi": "một cách láu lỉnh dí dỏm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099853", "hw": "pawkiness", "pos": "noun", "ipa": "/ˈpɔːkɪnəs/", "vi": "tính láu lỉnh dí dỏm sâu sắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099854", "hw": "pawky", "pos": "adj", "ipa": "/ˈpɔːki/", "vi": "dí dỏm kín đáo; láu lỉnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099855", "hw": "pawnable", "pos": "adj", "ipa": "/ˈpɔːnəbəl/", "vi": "có thể đem thế chấp cầm đồ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099856", "hw": "pawnage", "pos": "noun", "ipa": "/ˈpɔːnɪdʒ/", "vi": "việc cầm đồ thế chấp tài sản", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099857", "hw": "pawnbroking", "pos": "noun", "ipa": "/ˈpɔːnˌbroʊkɪŋ/", "vi": "nghề kinh doanh tiệm cầm đồ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099858", "hw": "pawned", "pos": "verb", "ipa": "/pɔːnd/", "vi": "đã đem cầm đồ; đã thế chấp", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099859", "hw": "pawner", "pos": "noun", "ipa": "/ˈpɔːnər/", "vi": "người đem tài sản đi cầm đồ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099860", "hw": "pawning", "pos": "noun", "ipa": "/ˈpɔːnɪŋ/", "vi": "việc cầm đồ; hành vi thế chấp", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099861", "hw": "pawns", "pos": "noun", "ipa": "/pɔːnz/", "vi": "các quân tốt cờ vua; vật thế chấp", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099862", "hw": "paws", "pos": "noun", "ipa": "/pɔːz/", "vi": "các bàn chân có vuốt vuốt thú", "cefr": "A2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099863", "hw": "paxto", "pos": "noun", "ipa": "/ˈpæʃtoʊ/", "vi": "tiếng Pashto (Afghanistan)", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099864", "hw": "payadores", "pos": "noun", "ipa": "/ˌpaɪəˈdɔːreɪz/", "vi": "các nhạc sĩ hát đối dân gian Gaucho", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099865", "hw": "payena", "pos": "noun", "ipa": "/pəˈjiːnə/", "vi": "chi cây cao su nhựa Payena", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099866", "hw": "payloads", "pos": "noun", "ipa": "/ˈpeɪloʊdz/", "vi": "các tải trọng hữu ích vận chuyển", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099867", "hw": "payments", "pos": "noun", "ipa": "/ˈpeɪmənts/", "vi": "các khoản thanh toán; số tiền trả", "cefr": "A2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099868", "hw": "paynim", "pos": "noun", "ipa": "/ˈpeɪnɪm/", "vi": "người ngoại giáo thời Thập Tự Chinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099869", "hw": "paysage", "pos": "noun", "ipa": "/peɪˈiːzɑːʒ/", "vi": "bức tranh phong cảnh miền quê", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099870", "hw": "paysheet", "pos": "noun", "ipa": "/ˈpeɪʃiːt/", "vi": "bảng chi trả lương nhân viên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099871", "hw": "pbit", "pos": "noun", "ipa": "/ˈpiːbɪt/", "vi": "đơn vị đo petabit", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099872", "hw": "pde", "pos": "noun", "ipa": "/ˌpiːdiːˈiː/", "vi": "phương trình đạo hàm riêng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099873", "hw": "pdflp", "pos": "noun", "ipa": "/ˌpiːdiːɛfɛlˈpiː/", "vi": "Mặt trận DC Giải phóng Palestine", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099874", "hw": "pdi", "pos": "noun", "ipa": "/ˌpiːdiːˈaɪ/", "vi": "quy trình kiểm định trước giao xe", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099875", "hw": "pdsa", "pos": "noun", "ipa": "/ˌpiːdiːɛsˈeɪ/", "vi": "hội bảo trợ y tế động vật PDSA", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099876", "hw": "pdt", "pos": "noun", "ipa": "/ˌpiːdiːˈtiː/", "vi": "giờ mùa hè Thái Bình Dương PDT", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099877", "hw": "peaceableness", "pos": "noun", "ipa": "/ˈpiːsəbəlnəs/", "vi": "tính yêu chuộng hòa bình ôn nhu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099878", "hw": "peacemaking", "pos": "noun", "ipa": "/ˈpiːsˌmeɪkɪŋ/", "vi": "sự kiến tạo hòa bình; hòa giải", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099879", "hw": "peachick", "pos": "noun", "ipa": "/ˈpiːtʃɪk/", "vi": "chim công non", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099880", "hw": "peachiness", "pos": "noun", "ipa": "/ˈpiːtʃinəs/", "vi": "vẻ tươi tắn hồng hào như đào", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099881", "hw": "peachwood", "pos": "noun", "ipa": "/ˈpiːtʃwʊd/", "vi": "gỗ cây vang nhuộm màu đỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099882", "hw": "peacockery", "pos": "noun", "ipa": "/ˈpiːkɑːkəri/", "vi": "thói khoe khoang lòe loẹt vênh váo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099883", "hw": "peafowls", "pos": "noun", "ipa": "/ˈpiːfaʊlz/", "vi": "các loài chim công", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099884", "hw": "peag", "pos": "noun", "ipa": "/piːɡ/", "vi": "chuỗi hạt vỏ sò tiền wampum", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099885", "hw": "peahens", "pos": "noun", "ipa": "/ˈpiːhɛnz/", "vi": "các con chim công mái", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099886", "hw": "peaker", "pos": "noun", "ipa": "/ˈpiːkər/", "vi": "nhà máy điện chạy phụ tải đỉnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099887", "hw": "peaking", "pos": "verb", "ipa": "/ˈpiːkɪŋ/", "vi": "đang chạm mức đỉnh điểm", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099888", "hw": "peakish", "pos": "adj", "ipa": "/ˈpiːkɪʃ/", "vi": "trông hơi xanh xao gầy yếu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099889", "hw": "peaks", "pos": "noun", "ipa": "/piːks/", "vi": "các đỉnh chóp nhọn; các đỉnh núi", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099890", "hw": "pealed", "pos": "verb", "ipa": "/piːld/", "vi": "đã vang rền; đã gióng hồi chuông", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099891", "hw": "peals", "pos": "noun", "ipa": "/piːlz/", "vi": "các hồi chuông ngân; tràng cười rộ", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099892", "hw": "pearlaceous", "pos": "adj", "ipa": "/pɜːrˈleɪʃəs/", "vi": "óng ánh như ngọc trai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099893", "hw": "pearlbarley", "pos": "noun", "ipa": "/ˈpɜːrlˌbɑːrli/", "vi": "hạt đại mạch ngọc trai tròn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099894", "hw": "pearled", "pos": "adj", "ipa": "/pɜːrld/", "vi": "được cẩn ngọc trai; lóng lánh sương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099895", "hw": "pearlfish", "pos": "noun", "ipa": "/ˈpɜːrlfɪʃ/", "vi": "loài cá ngọc trai sống ký sinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099896", "hw": "pearlies", "pos": "noun", "ipa": "/ˈpɜːrliz/", "vi": "bộ áo đính hàng cúc khuy xà cừ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099897", "hw": "pearliness", "pos": "noun", "ipa": "/ˈpɜːrlinəs/", "vi": "vẻ óng ánh trắng ngà như xà cừ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099898", "hw": "pearling", "pos": "noun", "ipa": "/ˈpɜːrlɪŋ/", "vi": "nghề lặn bắt tìm ngọc trai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099899", "hw": "pearls", "pos": "noun", "ipa": "/pɜːrlz/", "vi": "các viên ngọc trai quý giá", "cefr": "A2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099900", "hw": "pearlweed", "pos": "noun", "ipa": "/ˈpɜːrlwiːd/", "vi": "cây cỏ cúc ngọc Sagina", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099901", "hw": "pearlwort", "pos": "noun", "ipa": "/ˈpɜːrlwɜːrt/", "vi": "cây cỏ cúc ngọc Sagina", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
raw_items = json.load(open('scratch/b20_r10_raw_p4.json', 'r', encoding='utf-8'))
assert len(part4_data) == 100
assert len(raw_items) == 100

for i, item in enumerate(part4_data):
    raw = raw_items[i]
    assert item["id"] == raw["id"], f"ID mismatch at {i}: {item['id']} vs {raw['id']}"
    assert item["hw"] == raw["hw"], f"HW mismatch at {i}: {item['hw']} vs {raw['hw']}"
    assert len(item["vi"]) <= 35, f"vi too long at {i} ({item['hw']}): {item['vi']} ({len(item['vi'])} chars)"
    assert item["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num"], f"Invalid pos at {i}: {item['pos']}"
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert item["status"] == "reviewed"
    item["cefr"] = raw.get("cefr", "C2")
    item["tier"] = raw.get("tier", "expanded")
    item["notes"] = raw.get("notes", "")

with open('scratch/b20_r10_p4.json', 'w', encoding='utf-8') as f:
    json.dump(part4_data, f, ensure_ascii=False, indent=2)

print("b20_r10_p4.json created successfully and validated!")
