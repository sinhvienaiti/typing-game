# -*- coding: utf-8 -*-
import json

part3_data = [
  {"id": "lex.en.200k.054702", "hw": "revaluations", "pos": "noun", "ipa": "/ˌriːvæljuˈeɪʃənz/", "vi": "sự đánh giá lại; nâng giá tiền tệ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054703", "hw": "rosaleses", "pos": "noun", "ipa": "/roʊˈzeɪliːzɪz/", "vi": "các loài thực vật bộ Hoa hồng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054704", "hw": "rufs", "pos": "noun", "ipa": "/ɑːr-juː-ɛfs/", "vi": "Mặt trận Thống nhất Cách mạng RUF", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054705", "hw": "salutations", "pos": "noun", "ipa": "/ˌsæljʊˈteɪʃənz/", "vi": "lời chào hỏi; câu mở đầu thư", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054706", "hw": "sappers", "pos": "noun", "ipa": "/ˈsæpərz/", "vi": "những người lính công binh đào hầm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054707", "hw": "screwballs", "pos": "noun", "ipa": "/ˈskruːbɔːlz/", "vi": "những kẻ lập dị; cú ném bóng xoáy", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054708", "hw": "settees", "pos": "noun", "ipa": "/sɛˈtiːz/", "vi": "những chiếc ghế xô pha dài nhỏ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054709", "hw": "shylocks", "pos": "noun", "ipa": "/ˈʃaɪlɑːks/", "vi": "những kẻ cho vay nặng lãi tàn nhẫn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054710", "hw": "sidons", "pos": "noun", "ipa": "/ˈsaɪdənz/", "vi": "thành phố cổ Sidon của Phoenicia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054711", "hw": "sikorskies", "pos": "noun", "ipa": "/sɪˈkɔːrskiz/", "vi": "máy bay trực thăng Sikorsky", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054712", "hw": "skimmers", "pos": "noun", "ipa": "/ˈskɪmərz/", "vi": "muôi vớt bọt; thiết bị trộm thẻ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054713", "hw": "speechwriters", "pos": "noun", "ipa": "/ˈspiːtʃraɪtərz/", "vi": "những người chuyên viết diễn văn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054714", "hw": "spillages", "pos": "noun", "ipa": "/ˈspɪlɪdʒɪz/", "vi": "lượng chất lỏng bị tràn đổ ra", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054715", "hw": "spiritualists", "pos": "noun", "ipa": "/ˈspɪrɪtʃuəlɪsts/", "vi": "những người theo thuyết thông linh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054716", "hw": "stalinisms", "pos": "noun", "ipa": "/ˈstɑːlɪnɪzəmz/", "vi": "các chính sách chủ nghĩa Stalin", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054717", "hw": "stirrups", "pos": "noun", "ipa": "/ˈstɜːrəps/", "vi": "bàn đạp yên ngựa; xương bàn đạp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054718", "hw": "suvas", "pos": "noun", "ipa": "/ˈsuːvəz/", "vi": "thành phố Suva thủ đô của Fiji", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054719", "hw": "tawdrier", "pos": "adj", "ipa": "/ˈtɔːdriər/", "vi": "lòe loẹt hơn; rẻ tiền hơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054720", "hw": "tawdriest", "pos": "adj", "ipa": "/ˈtɔːdriɪst/", "vi": "lòe loẹt nhất; rẻ tiền nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054721", "hw": "transoms", "pos": "noun", "ipa": "/ˈtrænsəmz/", "vi": "thanh ngang cửa; ô thoáng trên cửa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054722", "hw": "twiggier", "pos": "adj", "ipa": "/ˈtwɪɡiər/", "vi": "gầy guộc hơn; nhiều cành nhánh hơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054723", "hw": "twiggiest", "pos": "adj", "ipa": "/ˈtwɪɡiɪst/", "vi": "gầy guộc nhất; nhiều nhánh nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054724", "hw": "updikes", "pos": "noun", "ipa": "/ˈʌpdaɪks/", "vi": "nhà văn Mỹ John Updike", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054725", "hw": "vilified", "pos": "verb", "ipa": "/ˈvɪlɪfaɪd/", "vi": "đã phỉ báng; đã bôi nhọ thanh danh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054726", "hw": "vilifies", "pos": "verb", "ipa": "/ˈvɪlɪfaɪz/", "vi": "phỉ báng; bôi nhọ thanh danh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054727", "hw": "vilifying", "pos": "verb", "ipa": "/ˈvɪlɪfaɪɪŋ/", "vi": "đang phỉ báng; đang bôi nhọ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054728", "hw": "weightlifters", "pos": "noun", "ipa": "/ˈweɪtlɪftərz/", "vi": "các vận động viên cử tạ thi đấu", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054729", "hw": "amaryllis family", "pos": "phrase", "ipa": "/ˌæməˈrɪlɪs ˈfæmɪli/", "vi": "họ thực vật hoa loa kèn thủy tiên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054730", "hw": "american gentian", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈdʒɛnʃən/", "vi": "cây long đởm hoa xanh Bắc Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054731", "hw": "arthur laffer", "pos": "phrase", "ipa": "/ˈɑːrθər ˈlæfər/", "vi": "nhà kinh tế học Arthur Laffer", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054732", "hw": "balsam woolly aphid", "pos": "phrase", "ipa": "/ˈbɔːlsəm ˈwʊli ˈeɪfɪd/", "vi": "rệp sáp trắng hại cây linh sam", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054733", "hw": "blind gentian", "pos": "phrase", "ipa": "/blaɪnd ˈdʒɛnʃən/", "vi": "loài long đởm hoa không nở", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054734", "hw": "bottle gentian", "pos": "phrase", "ipa": "/ˈbɑːtəl ˈdʒɛnʃən/", "vi": "cây hoa long đởm hình chai búp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054735", "hw": "caisson disease", "pos": "phrase", "ipa": "/ˈkeɪsən dɪˈziːz/", "vi": "bệnh giảm áp ở thợ lặn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054736", "hw": "cheviot hills", "pos": "phrase", "ipa": "/ˈtʃiːviət hɪlz/", "vi": "dãy đồi Cheviot biên giới Anh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054737", "hw": "closed gentian", "pos": "phrase", "ipa": "/kloʊzd ˈdʒɛnʃən/", "vi": "cây hoa long đởm cánh khép kín", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054738", "hw": "common camas", "pos": "phrase", "ipa": "/ˈkɑːmən ˈkæməs/", "vi": "cây hoa huệ tây dại hoa xanh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054739", "hw": "contractile organ", "pos": "phrase", "ipa": "/kənˈtræktəl ˈɔːrɡən//", "vi": "cơ quan có khả năng co rút", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054740", "hw": "copernican system", "pos": "phrase", "ipa": "/koʊˈpɜːrnɪkən ˈsɪstəm/", "vi": "thuyết nhật tâm của Copernicus", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054741", "hw": "cottontail rabbit", "pos": "phrase", "ipa": "/ˈkɑːtənteɪl ˈræbɪt/", "vi": "loài thỏ đuôi bông Bắc Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054742", "hw": "death camas", "pos": "phrase", "ipa": "/dɛθ ˈkæməs/", "vi": "cây hoa tử huệ có độc chết người", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054743", "hw": "feliz lusitania", "pos": "phrase", "ipa": "/feɪˈliːz ˌluːsɪˈteɪniə/", "vi": "pháo đài lịch sử Feliz Lusitania", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054744", "hw": "foist off", "pos": "phrase", "ipa": "/fɔɪst ɔːf/", "vi": "lừa gạt tống khứ đồ giả cho ai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054745", "hw": "gentian family", "pos": "phrase", "ipa": "/ˈdʒɛnʃən ˈfæmɪli/", "vi": "họ thực vật Long đởm thảo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054746", "hw": "genus astragalus", "pos": "phrase", "ipa": "/ˈdʒiːnəs æˈstræɡələs/", "vi": "chi cây Hoàng kỳ thảo dược", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054747", "hw": "genus datura", "pos": "phrase", "ipa": "/ˈdʒiːnəs dəˈtʊərə/", "vi": "chi thực vật Cà độc dược", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054748", "hw": "genus euphorbia", "pos": "phrase", "ipa": "/ˈdʒiːnəs juːˈfɔːrbiə/", "vi": "chi Đại kích có nhựa mủ trắng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054749", "hw": "genus phytophthora", "pos": "phrase", "ipa": "/ˈdʒiːnəs faɪˈtɑːfθərə/", "vi": "chi nấm mốc nước hại rễ thực vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054750", "hw": "genus sida", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈsaɪdə/", "vi": "chi Bông vàng; chi Ké hoa đào", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054751", "hw": "genus vitis", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈvaɪtɪs/", "vi": "chi Nho thuộc họ Nho leo giàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054752", "hw": "georges braque", "pos": "phrase", "ipa": "/ʒɔːrʒ bræk/", "vi": "danh họa Georges Braque Pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054753", "hw": "great yellow gentian", "pos": "phrase", "ipa": "/ɡreɪt ˈjɛloʊ ˈdʒɛnʃən/", "vi": "cây hoa long đởm vàng vùng núi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054754", "hw": "green gentian", "pos": "phrase", "ipa": "/ɡriːn ˈdʒɛnʃən/", "vi": "cây long đởm hoa đài xanh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054755", "hw": "hank panky", "pos": "phrase", "ipa": "/ˈhæŋki ˈpæŋki/", "vi": "trò mờ ám gian lận; chim chuột", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054756", "hw": "hieronymus bosch", "pos": "phrase", "ipa": "/haɪˈrɑːnɪməs bɒʃ/", "vi": "danh họa Hà Lan Hieronymus Bosch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054757", "hw": "hoary plantain", "pos": "phrase", "ipa": "/ˈhɔːri ˈplæntɪn/", "vi": "cây mã đề có lông trắng nhung", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054758", "hw": "horse gentian", "pos": "phrase", "ipa": "/hɔːrs ˈdʒɛnʃən/", "vi": "cây rễ sốt hoa sốt họ Kim ngân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054759", "hw": "horseshoe vetch", "pos": "phrase", "ipa": "/ˈhɔːrsʃuː vɛtʃ/", "vi": "cỏ móng ngựa hoa vàng đậu thức ăn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054760", "hw": "intervertebral disk", "pos": "phrase", "ipa": "/ˌɪntərˈvɜːrtɪbrəl dɪsk/", "vi": "đĩa đệm nằm giữa các đốt sống", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054761", "hw": "intervertebral vein", "pos": "phrase", "ipa": "/ˌɪntərˈvɜːrtɪbrəl veɪn/", "vi": "tĩnh mạch gian đốt sống lưng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054762", "hw": "ionospheric wave", "pos": "phrase", "ipa": "/aɪˌɑːnəˈsfɪrɪk weɪv/", "vi": "sóng vô tuyến phản xạ tầng điện ly", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054763", "hw": "jacques offenbach", "pos": "phrase", "ipa": "/ʒɑːk ˈɔːfənbɑːk/", "vi": "nhà soạn nhạc Jacques Offenbach", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054764", "hw": "jaggery palm", "pos": "phrase", "ipa": "/ˈdʒæɡəri pɑːm/", "vi": "cây thốt nốt nấu đường jaggery", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054765", "hw": "lactase deficiency", "pos": "phrase", "ipa": "/ˈlækteɪs dɪˈfɪʃənsi/", "vi": "chứng thiếu hụt men tiêu lactaza", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054766", "hw": "laffer curve", "pos": "phrase", "ipa": "/ˈlæfər kɜːrv/", "vi": "đường cong Laffer trong thuế khóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054767", "hw": "leishmaniasis americana", "pos": "phrase", "ipa": "/ˌliːʃməˈnaɪəsɪs əˌmɛrɪˈkɑːnə/", "vi": "bệnh trùng roi Leishmania châu Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054768", "hw": "livingroom set", "pos": "phrase", "ipa": "/ˈlɪvɪŋruːm sɛt/", "vi": "bộ bàn ghế sô pha phòng khách", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054769", "hw": "livingroom suite", "pos": "phrase", "ipa": "/ˈlɪvɪŋruːm swiːt/", "vi": "bộ nội thất bàn ghế phòng khách", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054770", "hw": "lut desert", "pos": "phrase", "ipa": "/lʊt ˈdɛzərt/", "vi": "sa mạc Lut cực nóng ở Iran", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054771", "hw": "magnetic monopole", "pos": "phrase", "ipa": "/mæɡˈnɛtɪk ˈmɑːnəpoʊl/", "vi": "đơn cực từ giả định trong vật lý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054772", "hw": "mauritian monetary unit", "pos": "phrase", "ipa": "/məˈrɪʃən ˈmɑːnɪtɛri ˈjuːnɪt/", "vi": "đơn vị tiền tệ của đảo Mauritius", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054773", "hw": "medullary sheath", "pos": "phrase", "ipa": "/ˈmɛdəlɛri ʃiːθ/", "vi": "bao myelin bảo vệ sợi thần kinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054774", "hw": "metacarpal bone", "pos": "phrase", "ipa": "/ˌmɛtəˈkɑːrpəl boʊn/", "vi": "xương bàn tay nối các ngón tay", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054775", "hw": "mountain skink", "pos": "phrase", "ipa": "/ˈmaʊntɪn skɪŋk/", "vi": "loài thằn lằn bóng sống trên núi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054776", "hw": "niccolo machiavelli", "pos": "phrase", "ipa": "/ˌnɪkəloʊ ˌmækiəˈvɛli/", "vi": "nhà tư tưởng Niccolò Machiavelli", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054777", "hw": "nonparametric statistics", "pos": "phrase", "ipa": "/ˌnɑːnpærəˈmɛtrɪk stəˈtɪstɪks/", "vi": "thống kê phi tham số trong toán", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054778", "hw": "northern dune tansy", "pos": "phrase", "ipa": "/ˈnɔːrðərn djuːn ˈtænzi/", "vi": "cúc thơm mọc cồn cát phương bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054779", "hw": "oedipal complex", "pos": "phrase", "ipa": "/ˈɛdɪpəl ˈkɑːmplɛks/", "vi": "phức cảm Oedipus trong tâm lý học", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054780", "hw": "oven stuffer", "pos": "phrase", "ipa": "/ˈʌvən ˈstʌfər/", "vi": "gà lớn nuôi béo để quay lò nướng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054781", "hw": "patellar reflex", "pos": "phrase", "ipa": "/pəˈtɛlər ˈriːflɛks/", "vi": "phản xạ gân xương bánh chè", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054782", "hw": "peptic ulcer", "pos": "phrase", "ipa": "/ˈpɛptɪk ˈʌlsər/", "vi": "chứng loét dạ dày tá tràng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054783", "hw": "pericardial space", "pos": "phrase", "ipa": "/ˌpɛrɪˈkɑːrdiəl speɪs/", "vi": "khoang màng ngoài tim", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054784", "hw": "pious platitude", "pos": "phrase", "ipa": "/ˈpaɪəs ˈplætɪtuːd/", "vi": "lời đạo đức sáo rỗng; giả nhân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054785", "hw": "regius professor", "pos": "phrase", "ipa": "/ˈriːdʒiəs prəˈfɛsər/", "vi": "giáo sư hoàng gia bổ nhiệm Anh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054786", "hw": "sandor kellner", "pos": "phrase", "ipa": "/ˈʃɑːndɔːr ˈkɛlnər/", "vi": "đạo diễn Alexander Korda Hungary", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054787", "hw": "seigneur de bayard", "pos": "phrase", "ipa": "/sɛnˈjɜːr də baɪˈɑːrd/", "vi": "hiệp sĩ Pierre Terrail de Bayard", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054788", "hw": "sense tagger", "pos": "phrase", "ipa": "/sɛns ˈtæɡər/", "vi": "bộ gán nhãn ngữ nghĩa từ vựng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054789", "hw": "subclinical absence", "pos": "phrase", "ipa": "/sʌbˈklɪnɪkəl ˈæbsəns/", "vi": "cơn vắng ý thức cận lâm sàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054790", "hw": "tableau vivant", "pos": "phrase", "ipa": "/tæbˈloʊ viːˈvɑ̃ː/", "vi": "hoạt cảnh người đóng bất động", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054791", "hw": "terra incognita", "pos": "phrase", "ipa": "/ˈtɛrə ɪnˈkɑːɡnɪtə/", "vi": "vùng đất chưa biết; cõi vô định", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054792", "hw": "tickler file", "pos": "phrase", "ipa": "/ˈtɪklər faɪl/", "vi": "tập hồ sơ nhắc việc theo ngày", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054793", "hw": "transylvanian alps", "pos": "phrase", "ipa": "/ˌtrænsɪlˈveɪniən ælps/", "vi": "dãy An-pơ Transilvania Rumani", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054794", "hw": "trimmer joist", "pos": "phrase", "ipa": "/ˈtrɪmər dʒɔɪst/", "vi": "dầm bo mép khung sàn công trình", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054795", "hw": "vitus bering", "pos": "phrase", "ipa": "/ˈvaɪtəs ˈbɪərɪŋ/", "vi": "nhà thám hiểm biển Vitus Bering", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054796", "hw": "western skink", "pos": "phrase", "ipa": "/ˈwɛstərn skɪŋk/", "vi": "loài thằn lằn bóng miền tây", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054797", "hw": "white camas", "pos": "phrase", "ipa": "/waɪt ˈkæməs/", "vi": "cây tử huệ hoa trắng có độc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054798", "hw": "willa cather", "pos": "phrase", "ipa": "/ˈwɪlə ˈkæðər/", "vi": "nữ nhà văn Mỹ Willa Cather", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054799", "hw": "yagi aerial", "pos": "phrase", "ipa": "/ˈjɑːɡi ˈɛəriəl/", "vi": "ăng-ten định hướng dải sóng Yagi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054800", "hw": "yellow twining snapdragon", "pos": "phrase", "ipa": "/ˈjɛloʊ ˈtwaɪnɪŋ ˈsnæpˌdræɡən/", "vi": "cây mõm chó leo hoa vàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054801", "hw": "achesons", "pos": "noun", "ipa": "/ˈeɪtʃɪsənz/", "vi": "Ngoại trưởng Mỹ Dean Acheson", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part3_data) == 100, f"Length is {len(part3_data)}"

with open('scratch/b31_r10_raw_p3.json') as f:
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

with open('scratch/b31_r10_p3.json', 'w', encoding='utf-8') as f:
    json.dump(part3_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 3")
