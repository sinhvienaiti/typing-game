import json

part2_data = [
  {"id": "lex.en.100k.096102", "hw": "northing", "pos": "noun", "ipa": "/ˈnɔːrðɪŋ/", "vi": "khoảng dời về hướng bắc; vĩ sai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096103", "hw": "northmost", "pos": "adj", "ipa": "/ˈnɔːrθmoʊst/", "vi": "xa nhất về phía bắc; cực bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096104", "hw": "norths", "pos": "noun", "ipa": "/nɔːrθs/", "vi": "các vùng phương bắc; các hướng bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096105", "hw": "northwardly", "pos": "adv", "ipa": "/ˈnɔːrθwɚdli/", "vi": "về hướng bắc; từ phương bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096106", "hw": "northwester", "pos": "noun", "ipa": "/ˌnɔːrθˈwɛstɚ/", "vi": "gió mạnh hướng tây bắc; bão tây bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096107", "hw": "northwestwardly", "pos": "adv", "ipa": "/ˌnɔːrθˈwɛstwɚdli/", "vi": "về phía tây bắc; theo hướng tây bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096108", "hw": "noruz", "pos": "noun", "ipa": "/noʊˈruːz/", "vi": "tết năm mới Ba Tư Nowruz", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096109", "hw": "norward", "pos": "adv", "ipa": "/ˈnɔːrwɚd/", "vi": "về hướng bắc; hướng lên bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096110", "hw": "norwards", "pos": "adv", "ipa": "/ˈnɔːrwɚdz/", "vi": "về phía bắc; hướng về phương bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096111", "hw": "norwegians", "pos": "noun", "ipa": "/nɔːrˈwiːdʒənz/", "vi": "những người Na Uy", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096112", "hw": "nos", "pos": "noun", "ipa": "/noʊz/", "vi": "những lời từ chối; phiếu chống", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096113", "hw": "nosebag", "pos": "noun", "ipa": "/ˈnoʊzbæɡ/", "vi": "túi thức ăn treo mũi ngựa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096114", "hw": "nosecount", "pos": "noun", "ipa": "/ˈnoʊzkaʊnt/", "vi": "sự đếm đầu người; kiểm phiếu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096115", "hw": "nosedived", "pos": "verb", "ipa": "/ˈnoʊzdaɪvd/", "vi": "lao đầu xuống dốc; sụt giảm mạnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096116", "hw": "nosedives", "pos": "verb", "ipa": "/ˈnoʊzdaɪvz/", "vi": "lao thẳng xuống dốc; giảm sút mạnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096117", "hw": "nosediving", "pos": "verb", "ipa": "/ˈnoʊzdaɪvɪŋ/", "vi": "lao dốc cắm đầu; sụt giảm thê thảm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096118", "hw": "nosepipe", "pos": "noun", "ipa": "/ˈnoʊzpaɪp/", "vi": "ống phun khí lò rèn; đầu vòi thổi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096119", "hw": "noser", "pos": "noun", "ipa": "/ˈnoʊzɚ/", "vi": "ngọn gió ngược thổi mạnh trực diện", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096120", "hw": "noserag", "pos": "noun", "ipa": "/ˈnoʊzræɡ/", "vi": "khăn mùi xoa hỉ mũi; khăn tay", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096121", "hw": "nosering", "pos": "noun", "ipa": "/ˈnoʊzrɪŋ/", "vi": "khuyên xỏ mũi; vòng xỏ mũi thú", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096122", "hw": "noses", "pos": "verb", "ipa": "/ˈnoʊzɪz/", "vi": "dò dẫm; len lỏi qua; ngửi tìm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096123", "hw": "nosewarmer", "pos": "noun", "ipa": "/ˈnoʊzwɔːrmɚ/", "vi": "tẩu thuốc ngắn cán", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096124", "hw": "nosher", "pos": "noun", "ipa": "/ˈnɑːʃɚ/", "vi": "người hay ăn vặt; người hảo ăn vặt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096125", "hw": "nosily", "pos": "adv", "ipa": "/ˈnoʊzɪli/", "vi": "một cách tò mò; thọc mạch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096126", "hw": "nosing", "pos": "noun", "ipa": "/ˈnoʊzɪŋ/", "vi": "mép gờ bậc cầu thang; sự dò mũi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096127", "hw": "nosohusial", "pos": "adj", "ipa": "/ˌnoʊsoʊˈhjuːziəl/", "vi": "thuộc chăm sóc y tế tại gia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096128", "hw": "nostocaceae", "pos": "noun", "ipa": "/ˌnɑːstəkˈeɪsiːiː/", "vi": "họ vi khuẩn lam Nostocaceae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096129", "hw": "notarial", "pos": "adj", "ipa": "/noʊˈtɛriəl/", "vi": "thuộc công chứng; được thị thực", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096130", "hw": "notarise", "pos": "verb", "ipa": "/ˈnoʊtəraɪz/", "vi": "công chứng; thị thực giấy tờ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096131", "hw": "notarized", "pos": "verb", "ipa": "/ˈnoʊtəraɪzd/", "vi": "đã công chứng; đã chứng thực", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096132", "hw": "notarizes", "pos": "verb", "ipa": "/ˈnoʊtəraɪzɪz/", "vi": "công chứng; xác nhận hợp lệ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096133", "hw": "notarizing", "pos": "verb", "ipa": "/ˈnoʊtəraɪzɪŋ/", "vi": "đang công chứng; chứng thực văn bản", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096134", "hw": "notaryship", "pos": "noun", "ipa": "/ˈnoʊtəriʃɪp/", "vi": "chức vị công chứng viên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096135", "hw": "notches", "pos": "verb", "ipa": "/ˈnɑːtʃɪz/", "vi": "khía rãnh; đạt được mục tiêu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096136", "hw": "notching", "pos": "verb", "ipa": "/ˈnɑːtʃɪŋ/", "vi": "khía rãnh; đạt được thắng lợi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096137", "hw": "notecase", "pos": "noun", "ipa": "/ˈnoʊtkeɪs/", "vi": "ví da đựng tiền giấy; ví bỏ túi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096138", "hw": "notecases", "pos": "noun", "ipa": "/ˈnoʊtkeɪsɪz/", "vi": "các ví đựng tiền giấy", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096139", "hw": "notechis", "pos": "noun", "ipa": "/ˈnoʊtəkɪs/", "vi": "chi rắn hổ Úc Notechis", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096140", "hw": "noteless", "pos": "adj", "ipa": "/ˈnoʊtləs/", "vi": "không được ai để ý; vô danh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096141", "hw": "notelet", "pos": "noun", "ipa": "/ˈnoʊtlət/", "vi": "tờ giấy ghi chú nhỏ; bức thư ngắn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096142", "hw": "notemigonus", "pos": "noun", "ipa": "/ˌnoʊtəmɪˈɡoʊnəs/", "vi": "chi cá tuế Notemigonus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096143", "hw": "notes", "pos": "verb", "ipa": "/noʊts/", "vi": "ghi nhận; chú ý tới", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096144", "hw": "nothosaur", "pos": "noun", "ipa": "/ˈnoʊθəsɔːr/", "vi": "loài bò sát biển cổ Nothosaur", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096145", "hw": "nothosauria", "pos": "noun", "ipa": "/ˌnoʊθəˈsɔːriə/", "vi": "phân bộ bò sát biển Nothosauria", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096146", "hw": "noticeability", "pos": "noun", "ipa": "/ˌnoʊtɪsəˈbɪləti/", "vi": "tính dễ nhận thấy; sự rõ nét", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096147", "hw": "noticeableness", "pos": "noun", "ipa": "/ˈnoʊtɪsəbəlnəs/", "vi": "sự dễ thấy; tính nổi bật rõ ràng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096148", "hw": "noticer", "pos": "noun", "ipa": "/ˈnoʊtɪsɚ/", "vi": "người tinh ý; người hay để ý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096149", "hw": "notices", "pos": "verb", "ipa": "/ˈnoʊtɪsɪz/", "vi": "để ý thấy; nhận biết; chú ý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096150", "hw": "noticing", "pos": "verb", "ipa": "/ˈnoʊtɪsɪŋ/", "vi": "nhận thấy; để mắt chú ý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096151", "hw": "notified", "pos": "verb", "ipa": "/ˈnoʊtəfaɪd/", "vi": "đã thông báo; đã gửi tin báo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096152", "hw": "notifies", "pos": "verb", "ipa": "/ˈnoʊtəfaɪz/", "vi": "thông báo; báo tin cho hay", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096153", "hw": "notifying", "pos": "verb", "ipa": "/ˈnoʊtəfaɪɪŋ/", "vi": "thông báo; gửi tin báo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096154", "hw": "noting", "pos": "verb", "ipa": "/ˈnoʊtɪŋ/", "vi": "ghi nhận; lưu tâm; chú thích", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096155", "hw": "notionalist", "pos": "noun", "ipa": "/ˈnoʊʃənəlɪst/", "vi": "kẻ hay hoang tưởng; nhà lý thuyết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096156", "hw": "notomys", "pos": "noun", "ipa": "/ˈnɑːtəmaɪs/", "vi": "chi chuột nhảy có túi Úc Notomys", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096157", "hw": "notonecta", "pos": "noun", "ipa": "/ˌnoʊtəˈnɛktə/", "vi": "chi bọ gạo bơi ngửa Notonecta", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096158", "hw": "notonectidae", "pos": "noun", "ipa": "/ˌnoʊtənɛkˈtɪdiː/", "vi": "họ bọ bơi ngửa Notonectidae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096159", "hw": "notophthalmus", "pos": "noun", "ipa": "/ˌnoʊtɑːfˈθælməs/", "vi": "chi kỳ giông Bắc Mỹ Notophthalmus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096160", "hw": "notornis", "pos": "noun", "ipa": "/noʊˈtɔːrnɪs/", "vi": "chim takahe New Zealand", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096161", "hw": "notoryctidae", "pos": "noun", "ipa": "/ˌnoʊtərɪkˈtɪdiː/", "vi": "họ chuột chũi có túi Notoryctidae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096162", "hw": "notoryctus", "pos": "noun", "ipa": "/ˌnoʊtəˈrɪktəs/", "vi": "chi chuột chũi có túi Notoryctus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096163", "hw": "notostraca", "pos": "noun", "ipa": "/noʊˈtɑːstrəkə/", "vi": "bộ tôm nòng nọc Notostraca", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096164", "hw": "noublemanly", "pos": "adv", "ipa": "/ˈnoʊbəlmənli/", "vi": "như một quý tộc; hào hiệp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096165", "hw": "nouns", "pos": "noun", "ipa": "/naʊnz/", "vi": "các danh từ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096166", "hw": "novae", "pos": "noun", "ipa": "/ˈnoʊviː/", "vi": "những tân tinh; sao mới bộc phát", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096167", "hw": "novator", "pos": "noun", "ipa": "/ˈnoʊveɪtɚ/", "vi": "người canh tân; nhà đổi mới", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096168", "hw": "novelese", "pos": "noun", "ipa": "/ˌnɑːvəlˈiːz/", "vi": "văn phong tiểu thuyết sến rẻ tiền", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096169", "hw": "novelise", "pos": "verb", "ipa": "/ˈnɑːvəlaɪz/", "vi": "tiểu thuyết hóa; phóng tác sách", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096170", "hw": "novelised", "pos": "verb", "ipa": "/ˈnɑːvəlaɪzd/", "vi": "đã tiểu thuyết hóa; đã phóng tác", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096171", "hw": "novelises", "pos": "verb", "ipa": "/ˈnɑːvəlaɪzɪz/", "vi": "tiểu thuyết hóa một tác phẩm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096172", "hw": "novelising", "pos": "verb", "ipa": "/ˈnɑːvəlaɪzɪŋ/", "vi": "tiểu thuyết hóa; phóng tác truyện", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096173", "hw": "novelistic", "pos": "adj", "ipa": "/ˌnɑːvəˈlɪstɪk/", "vi": "thuộc phong cách tiểu thuyết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096174", "hw": "novelists", "pos": "noun", "ipa": "/ˈnɑːvəlɪsts/", "vi": "các nhà viết tiểu thuyết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096175", "hw": "novelize", "pos": "verb", "ipa": "/ˈnɑːvəlaɪz/", "vi": "tiểu thuyết hóa kịch bản", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096176", "hw": "novelties", "pos": "noun", "ipa": "/ˈnɑːvəltiz/", "vi": "những món đồ mới lạ; sự tân kỳ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096177", "hw": "novennial", "pos": "adj", "ipa": "/noʊˈvɛniəl/", "vi": "định kỳ chín năm một lần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096178", "hw": "novercal", "pos": "adj", "ipa": "/noʊˈvɜːrkəl/", "vi": "thuộc mẹ kế; dì ghẻ cay nghiệt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096179", "hw": "novial", "pos": "noun", "ipa": "/ˈnoʊviəl/", "vi": "ngôn ngữ nhân tạo Novial", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096180", "hw": "noviceship", "pos": "noun", "ipa": "/ˈnɑːvəsʃɪp/", "vi": "thời kỳ tập sự; phẩm vị tập tu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096181", "hw": "noviciate", "pos": "noun", "ipa": "/noʊˈvɪʃiət/", "vi": "giai đoạn tập tu; nơi tập sự", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096182", "hw": "novillada", "pos": "noun", "ipa": "/ˌnoʊviːˈjɑːdə/", "vi": "trận đấu bò tơ Tây Ban Nha", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096183", "hw": "novillero", "pos": "noun", "ipa": "/ˌnoʊviːˈjɛroʊ/", "vi": "đấu sĩ đấu bò tơ tập sự", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096184", "hw": "novity", "pos": "noun", "ipa": "/ˈnɑːvəti/", "vi": "tính mới lạ; sự tân tiến cách tân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096185", "hw": "novobiocin", "pos": "noun", "ipa": "/ˌnoʊvoʊbaɪˈoʊsɪn/", "vi": "kháng sinh novobiocin trị khuẩn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096186", "hw": "nowaday", "pos": "adj", "ipa": "/ˈnaʊədeɪ/", "vi": "thời nay; ngày nay; hiện đại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096187", "hw": "noway", "pos": "adv", "ipa": "/ˈnoʊweɪ/", "vi": "hoàn toàn không; không đời nào", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096188", "hw": "noways", "pos": "adv", "ipa": "/ˈnoʊweɪz/", "vi": "tuyệt nhiên không; chẳng đời nào", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096189", "hw": "nowrooz", "pos": "noun", "ipa": "/noʊˈruːz/", "vi": "tết cổ truyền mừng xuân Nowruz", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096190", "hw": "noxiously", "pos": "adv", "ipa": "/ˈnɑːkʃəsli/", "vi": "một cách độc hại; nguy hại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096191", "hw": "noxiousness", "pos": "noun", "ipa": "/ˈnɑːkʃəsnəs/", "vi": "tính độc hại; sự nguy hại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096192", "hw": "nozzleman", "pos": "noun", "ipa": "/ˈnɑːzəlmən/", "vi": "thợ cầm vòi phun; lính cầm lăng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096193", "hw": "nozzles", "pos": "noun", "ipa": "/ˈnɑːzəlz/", "vi": "các đầu vòi phun; miệng ống xả", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096194", "hw": "npcs", "pos": "noun", "ipa": "/ˌɛnpiːˈsiːz/", "vi": "nhân vật không phải người chơi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096195", "hw": "nrm", "pos": "noun", "ipa": "/ˌɛnɑːrˈɛm/", "vi": "phong trào tôn giáo mới NRM", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096196", "hw": "nrna", "pos": "noun", "ipa": "/ˌɛnɑːrɛnˈeɪ/", "vi": "ARN nhân tế bào; nRNA sinh học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096197", "hw": "nrrowing", "pos": "noun", "ipa": "/ˈnɛroʊɪŋ/", "vi": "sự thu hẹp; sự thu hẹp ngữ nghĩa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096198", "hw": "nrti", "pos": "noun", "ipa": "/ˌɛnɑːrtiːˈaɪ/", "vi": "thuốc kháng virus ức chế men NRTI", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096199", "hw": "nsb", "pos": "noun", "ipa": "/ˌɛnɛsˈbiː/", "vi": "ngân hàng tiết kiệm quốc gia NSB", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096200", "hw": "nsfw", "pos": "adj", "ipa": "/ˌɛnɛsɛfˈdʌbəljuː/", "vi": "nội dung nhạy cảm; không phù hợp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096201", "hw": "nsfwer", "pos": "noun", "ipa": "/ˌɛnɛsɛfˈdʌbəljuːɚ/", "vi": "người chuyên đăng nội dung 18+", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
]

assert len(part2_data) == 100, f"Expected 100 items, got {len(part2_data)}"

valid_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

with open("scratch/b20_r03_raw_p2.json") as f:
    raw_p2 = json.load(f)

for i, (item, raw) in enumerate(zip(part2_data, raw_p2)):
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

with open("scratch/b20_r03_p2.json", "w") as f:
    json.dump(part2_data, f, ensure_ascii=False, indent=2)

print("Batch 20 Round 3 Part 2 validated and saved successfully!")
