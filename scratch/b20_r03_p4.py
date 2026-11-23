import json

part4_data = [
  {"id": "lex.en.100k.096302", "hw": "nuzzling", "pos": "verb", "ipa": "/ˈnʌzəlɪŋ/", "vi": "dụi mũi âu yếm; nép sát vào", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096303", "hw": "nwbn", "pos": "noun", "ipa": "/ˌɛndʌbəljuːbaɪˈɛn/", "vi": "hướng tây bắc chế bắc NWbN", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096304", "hw": "nwbw", "pos": "noun", "ipa": "/ˌɛndʌbəljuːbaɪˈdʌbəljuː/", "vi": "hướng tây bắc chế tây NWbW", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096305", "hw": "nyamuragira", "pos": "noun", "ipa": "/njɑːˌmʊərəˈɡiːrə/", "vi": "núi lửa Nyamuragira ở Congo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096306", "hw": "nyamwezi", "pos": "noun", "ipa": "/njæmˈweɪzi/", "vi": "người Nyamwezi; tiếng Nyamwezi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096307", "hw": "nybble", "pos": "noun", "ipa": "/ˈnɪbəl/", "vi": "nửa byte; nhóm bốn bit dữ liệu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096308", "hw": "nyctaginaceae", "pos": "noun", "ipa": "/ˌnɪktədʒɪˈneɪsiːiː/", "vi": "họ hoa phấn Nyctaginaceae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096309", "hw": "nyctaginia", "pos": "noun", "ipa": "/ˌnɪktəˈdʒɪniə/", "vi": "chi hoa phấn đỏ Nyctaginia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096310", "hw": "nyctalope", "pos": "noun", "ipa": "/ˈnɪktəloʊp/", "vi": "người mắc chứng bệnh quáng gà", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096311", "hw": "nyctalopia", "pos": "noun", "ipa": "/ˌnɪktəˈloʊpiə/", "vi": "chứng quáng gà; mắt quáng gà", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096312", "hw": "nyctalopic", "pos": "adj", "ipa": "/ˌnɪktəˈloʊpɪk/", "vi": "thuộc chứng quáng gà; mắt quáng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096313", "hw": "nyctanassa", "pos": "noun", "ipa": "/ˌnɪktəˈnæsə/", "vi": "chi vạc đầu vàng Nyctanassa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096314", "hw": "nyctereutes", "pos": "noun", "ipa": "/ˌnɪktəˈruːtiːz/", "vi": "chi chó gấu mèo Nyctereutes", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096315", "hw": "nycticebus", "pos": "noun", "ipa": "/ˌnɪktɪˈsiːbəs/", "vi": "chi cu li chậm Nycticebus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096316", "hw": "nycticorax", "pos": "noun", "ipa": "/nɪkˈtɪkəræks/", "vi": "chi chim vạc Nycticorax", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096317", "hw": "nyctimene", "pos": "noun", "ipa": "/nɪkˈtɪmɪniː/", "vi": "chi dơi mũi ống Nyctimene", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096318", "hw": "nyctophile", "pos": "noun", "ipa": "/ˈnɪktəfaɪl/", "vi": "người yêu thích màn đêm bóng tối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096319", "hw": "nyctophobia", "pos": "noun", "ipa": "/ˌnɪktəˈfoʊbiə/", "vi": "chứng ám ảnh sợ bóng tối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096320", "hw": "nycturia", "pos": "noun", "ipa": "/nɪkˈtjʊriə/", "vi": "chứng tiểu đêm; tiểu tiện ban đêm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096321", "hw": "nydrazid", "pos": "noun", "ipa": "/ˈnaɪdrəzɪd/", "vi": "thuốc trị lao Nydrazid isoniazid", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096322", "hw": "nylghai", "pos": "noun", "ipa": "/ˈnɪlɡaɪ/", "vi": "loài linh dương bò lam Ấn Độ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096323", "hw": "nylghau", "pos": "noun", "ipa": "/ˈnɪlɡaʊ/", "vi": "linh dương lam Ấn Độ Boselaphus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096324", "hw": "nylonless", "pos": "adj", "ipa": "/ˈnaɪlɑːnləs/", "vi": "không chứa nilon; không mặc nilon", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096325", "hw": "nymphaeaceae", "pos": "noun", "ipa": "/ˌnɪmfiːˈeɪsiːiː/", "vi": "họ hoa súng Nymphaeaceae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096326", "hw": "nymphalid", "pos": "noun", "ipa": "/ˈnɪmfəlɪd/", "vi": "loài bướm giáp chân bốn ngón", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096327", "hw": "nymphalis", "pos": "noun", "ipa": "/nɪmˈfeɪlɪs/", "vi": "chi bướm giáp Nymphalis", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096328", "hw": "nymphean", "pos": "adj", "ipa": "/nɪmˈfiːən/", "vi": "thuộc nữ thần sông suối; kiều diễm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096329", "hw": "nymphets", "pos": "noun", "ipa": "/ˈnɪmfɪts/", "vi": "những thiếu nữ khêu gợi non nớt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096330", "hw": "nymphicus", "pos": "noun", "ipa": "/ˈnɪmfɪkəs/", "vi": "chi vẹt mào Úc Nymphicus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096331", "hw": "nympholepsy", "pos": "noun", "ipa": "/ˈnɪmfəlɛpsi/", "vi": "cơn cuồng si say đắm ảo tưởng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096332", "hw": "nympholept", "pos": "noun", "ipa": "/ˈnɪmfəlɛpt/", "vi": "kẻ si tình đắm đuối ảo mộng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096333", "hw": "nymphomaniacal", "pos": "adj", "ipa": "/ˌnɪmfəməˈnaɪəkəl/", "vi": "mắc chứng cuồng dâm nữ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096334", "hw": "nymphoses", "pos": "noun", "ipa": "/nɪmˈfoʊsiːz/", "vi": "các quá trình biến hóa nhộng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096335", "hw": "nymphosis", "pos": "noun", "ipa": "/nɪmˈfoʊsɪs/", "vi": "giai đoạn hóa nhộng; sự tạo kén", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096336", "hw": "nyssaceae", "pos": "noun", "ipa": "/nɪˈseɪsiːiː/", "vi": "họ thực vật Nyssaceae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096337", "hw": "nystan", "pos": "noun", "ipa": "/ˈnaɪstæn/", "vi": "thuốc kháng nấm Nystan nystatin", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096338", "hw": "nyuck", "pos": "intj", "ipa": "/njʌk/", "vi": "tiếng cười hỉ hả; ha ha", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096339", "hw": "oafishly", "pos": "adv", "ipa": "/ˈoʊfɪʃli/", "vi": "một cách ngốc nghếch thô lỗ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096340", "hw": "oafishness", "pos": "noun", "ipa": "/ˈoʊfɪʃnəs/", "vi": "tính ngốc nghếch; sự vụng về", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096341", "hw": "oakery", "pos": "noun", "ipa": "/ˈoʊkəri/", "vi": "rừng sồi bạt ngàn; vườn sồi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096342", "hw": "oaklet", "pos": "noun", "ipa": "/ˈoʊklət/", "vi": "cây sồi non nhỏ; chồi sồi non", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096343", "hw": "oakling", "pos": "noun", "ipa": "/ˈoʊklɪŋ/", "vi": "cây sồi non; mầm cây sồi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096344", "hw": "oaks", "pos": "noun", "ipa": "/oʊks/", "vi": "những cây gỗ sồi; đồ gỗ sồi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096345", "hw": "oaky", "pos": "adj", "ipa": "/ˈoʊki/", "vi": "có mùi gỗ sồi ủ rượu; cứng cáp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096346", "hw": "oarage", "pos": "noun", "ipa": "/ˈɔːrɪdʒ/", "vi": "dàn mái chèo; sự chèo thuyền", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096347", "hw": "oared", "pos": "adj", "ipa": "/ɔːrd/", "vi": "có trang bị mái chèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096348", "hw": "oarer", "pos": "noun", "ipa": "/ˈɔːrɚ/", "vi": "người chèo thuyền; tay chèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096349", "hw": "oaring", "pos": "verb", "ipa": "/ˈɔːrɪŋ/", "vi": "chèo thuyền; khua mái chèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096350", "hw": "oarium", "pos": "noun", "ipa": "/oʊˈɛriəm/", "vi": "buồng trứng sinh học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096351", "hw": "oarless", "pos": "adj", "ipa": "/ˈɔːrləs/", "vi": "không có mái chèo; thiếu chèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096352", "hw": "oarlock", "pos": "noun", "ipa": "/ˈɔːrlɑːk/", "vi": "cọc chèo thuyền; ngàm giữ chèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096353", "hw": "oars", "pos": "verb", "ipa": "/ɔːrz/", "vi": "khua mái chèo; rẽ nước chèo thuyền", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096354", "hw": "oarsmanship", "pos": "noun", "ipa": "/ˈɔːrzmənʃɪp/", "vi": "kỹ năng chèo thuyền; tài bơi chèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096355", "hw": "oarswoman", "pos": "noun", "ipa": "/ˈɔːrzˌwʊmən/", "vi": "nữ vận động viên chèo thuyền", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096356", "hw": "oary", "pos": "adj", "ipa": "/ˈɔːri/", "vi": "có dạng mái chèo; dùng làm chèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096357", "hw": "oasal", "pos": "adj", "ipa": "/oʊˈeɪsəl/", "vi": "thuộc ốc đảo xanh sa mạc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096358", "hw": "oases", "pos": "noun", "ipa": "/oʊˈeɪsiːz/", "vi": "những ốc đảo; nơi an lành màu mỡ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096359", "hw": "oatcakes", "pos": "noun", "ipa": "/ˈoʊtkeɪks/", "vi": "những chiếc bánh yến mạch nướng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096360", "hw": "oats", "pos": "noun", "ipa": "/oʊts/", "vi": "hạt yến mạch; cháo yến mạch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096361", "hw": "oau", "pos": "noun", "ipa": "/ˌoʊeɪˈjuː/", "vi": "tổ chức Thống nhất Châu Phi OAU", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096362", "hw": "oaves", "pos": "noun", "ipa": "/oʊvz/", "vi": "những kẻ đần độn vụng về", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096363", "hw": "obconic", "pos": "adj", "ipa": "/ɑːbˈkɑːnɪk/", "vi": "có hình nón ngược", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096364", "hw": "obconical", "pos": "adj", "ipa": "/ɑːbˈkɑːnɪkəl/", "vi": "có dạng hình nón ngược đỉnh dưới", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096365", "hw": "obcordate", "pos": "adj", "ipa": "/ɑːbˈkɔːrdeɪt/", "vi": "có hình trái tim ngược ngọn dưới", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096366", "hw": "obcurrent", "pos": "adj", "ipa": "/ɑːbˈkɜːrənt/", "vi": "chảy ngược chiều; giao nhau", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096367", "hw": "obduction", "pos": "noun", "ipa": "/ɑːbˈdʌkʃən/", "vi": "hiện tượng hút chìm trồi vỉa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096368", "hw": "obdurateness", "pos": "noun", "ipa": "/ˈɑːbdjʊrətnəs/", "vi": "sự ngoan cố; thái độ bướng bỉnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096369", "hw": "obe", "pos": "noun", "ipa": "/ˌoʊbiːˈiː/", "vi": "huân chương đế chế Anh OBE", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096370", "hw": "obeahman", "pos": "noun", "ipa": "/ˈoʊbiəmæn/", "vi": "pháp sư ma thuật Obeah Tây Ấn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096371", "hw": "obeche", "pos": "noun", "ipa": "/oʊˈbɛtʃi/", "vi": "gỗ obeche châu Phi làm đàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096372", "hw": "obechi", "pos": "noun", "ipa": "/oʊˈbɛtʃi/", "vi": "cây gỗ obechi Tây Phi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096373", "hw": "obediences", "pos": "noun", "ipa": "/oʊˈbiːdiənsɪz/", "vi": "sự phục tùng; các giáo quyền tu sĩ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096374", "hw": "obedientiary", "pos": "noun", "ipa": "/oʊˌbiːdiˈɛnʃieri/", "vi": "tu sĩ chấp hành sự vụ tu viện", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096375", "hw": "obeisant", "pos": "adj", "ipa": "/oʊˈbeɪsənt/", "vi": "cung kính; khúm núm cúi mình", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096376", "hw": "obeisantly", "pos": "adv", "ipa": "/oʊˈbeɪsəntli/", "vi": "một cách cung kính phục tùng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096377", "hw": "obeli", "pos": "noun", "ipa": "/ˈɑːbəlaɪ/", "vi": "các dấu gạch chữ thập obelus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096378", "hw": "obelion", "pos": "noun", "ipa": "/oʊˈbiːliən/", "vi": "điểm thóp trên khớp đỉnh trán", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096379", "hw": "obelise", "pos": "verb", "ipa": "/ˈɑːbəlaɪz/", "vi": "đánh dấu ôben nghi ngờ sai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096380", "hw": "obelisks", "pos": "noun", "ipa": "/ˈɑːbəlɪsks/", "vi": "những đài kỷ niệm hình tháp nhọn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096381", "hw": "obelize", "pos": "verb", "ipa": "/ˈɑːbəlaɪz/", "vi": "đánh dấu obelus nghi bản sai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096382", "hw": "obelus", "pos": "noun", "ipa": "/ˈɑːbələs/", "vi": "dấu obelus; ký hiệu chia trừ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096383", "hw": "oberson", "pos": "noun", "ipa": "/ˈoʊbərɑːn/", "vi": "vua tiên Oberon trong truyền thuyết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096384", "hw": "obeseness", "pos": "noun", "ipa": "/oʊˈbiːsnəs/", "vi": "tình trạng béo phì; sự thừa cân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096385", "hw": "obeyer", "pos": "noun", "ipa": "/oʊˈbeɪɚ/", "vi": "người biết vâng lời; kẻ tuân lệnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096386", "hw": "obihiro", "pos": "noun", "ipa": "/oʊbiːˈhɪəroʊ/", "vi": "thành phố Obihiro ở Hokkaido", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096387", "hw": "obiism", "pos": "noun", "ipa": "/ˈoʊbiɪzəm/", "vi": "tà thuật Obeah vùng Caribe", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096388", "hw": "obiit", "pos": "verb", "ipa": "/ˈoʊbiɪt/", "vi": "đã qua đời; đã tạ thế", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096389", "hw": "obiter", "pos": "adv", "ipa": "/ˈoʊbɪtɚ/", "vi": "nhân tiện; tiện thể nói qua", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096390", "hw": "obitual", "pos": "adj", "ipa": "/oʊˈbɪtʃuəl/", "vi": "thuộc ngày giỗ; liên quan tang lễ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096391", "hw": "obituaries", "pos": "noun", "ipa": "/oʊˈbɪtʃuɛriz/", "vi": "những bài cáo phó; mục tin buồn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096392", "hw": "obituarist", "pos": "noun", "ipa": "/oʊˈbɪtʃuərɪst/", "vi": "người chuyên viết cáo phó", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096393", "hw": "obj", "pos": "noun", "ipa": "/ˈɑːbdʒɛkt/", "vi": "đối tượng; bổ ngữ trong ngữ pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096394", "hw": "objected", "pos": "verb", "ipa": "/əbˈdʒɛktɪd/", "vi": "đã phản đối; đã khiếu nại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096395", "hw": "objectified", "pos": "verb", "ipa": "/əbˈdʒɛktɪfaɪd/", "vi": "đã vật hóa; đã cụ thể hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096396", "hw": "objectifies", "pos": "verb", "ipa": "/əbˈdʒɛktɪfaɪz/", "vi": "vật hóa; xem như đồ vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096397", "hw": "objectifying", "pos": "verb", "ipa": "/əbˈdʒɛktɪfaɪɪŋ/", "vi": "vật hóa; xem như đồ vật giải trí", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096398", "hw": "objecting", "pos": "verb", "ipa": "/əbˈdʒɛktɪŋ/", "vi": "lên tiếng phản đối; khiếu nại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096399", "hw": "objectionableness", "pos": "noun", "ipa": "/əbˈdʒɛkʃənəbəlnəs/", "vi": "sự đáng chê trách; tính khó chịu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096400", "hw": "objectise", "pos": "verb", "ipa": "/ˈɑːbdʒɪktaɪz/", "vi": "khách thể hóa; xem như đồ vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096401", "hw": "objectives", "pos": "noun", "ipa": "/əbˈdʒɛktɪvz/", "vi": "các mục tiêu; kính vật quang học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
]

assert len(part4_data) == 100, f"Expected 100 items, got {len(part4_data)}"

valid_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

with open("scratch/b20_r03_raw_p4.json") as f:
    raw_p4 = json.load(f)

for i, (item, raw) in enumerate(zip(part4_data, raw_p4)):
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

with open("scratch/b20_r03_p4.json", "w") as f:
    json.dump(part4_data, f, ensure_ascii=False, indent=2)

print("Batch 20 Round 3 Part 4 validated and saved successfully!")
