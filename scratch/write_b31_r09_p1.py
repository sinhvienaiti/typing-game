# -*- coding: utf-8 -*-
import json

part1_data = [
  {"id": "lex.en.200k.054002", "hw": "capra ibex", "pos": "phrase", "ipa": "/ˈkæprə ˈaɪbɛks/", "vi": "loài dê rừng núi Alps châu Âu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054003", "hw": "chamois cress", "pos": "phrase", "ipa": "/ˈʃæmwɑː krɛs/", "vi": "cây cải xoong núi đá hoa trắng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054004", "hw": "charles dillon stengel", "pos": "phrase", "ipa": "/tʃɑːrlz ˈdɪlən ˈstɛŋɡəl/", "vi": "huấn luyện viên Casey Stengel", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054005", "hw": "cheesed off", "pos": "adj", "ipa": "/tʃiːzd ɔːf/", "vi": "bực bội; tức giận chán ngấy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054006", "hw": "chocolate eclair", "pos": "phrase", "ipa": "/ˈtʃɔːklət eɪˈklɛər/", "vi": "bánh su kem phủ sô-cô-la Pháp", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054007", "hw": "chromatin granule", "pos": "phrase", "ipa": "/ˈkroʊmətɪn ˈɡrænjuːl/", "vi": "hạt chất nhiễm sắc nhân tế bào", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054008", "hw": "ciliary artery", "pos": "phrase", "ipa": "/ˈsɪliɛri ˈɑːrtəri/", "vi": "động mạch mi nuôi dưỡng mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054009", "hw": "cloven foot", "pos": "phrase", "ipa": "/ˌkloʊvən ˈfʊt/", "vi": "móng guốc chẻ đôi; móng quỷ dữ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054010", "hw": "crown vetch", "pos": "phrase", "ipa": "/kraʊn vɛtʃ/", "vi": "cỏ đậu vương miện chống xói mòn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054011", "hw": "dame edith sitwell", "pos": "phrase", "ipa": "/deɪm ˈiːdɪθ ˈsɪtwɛl/", "vi": "nữ thi sĩ Anh Dame Edith Sitwell", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054012", "hw": "daniel garrison brinton", "pos": "phrase", "ipa": "/ˈdænjəl ˈɡærɪsən ˈbrɪntən/", "vi": "nhà nhân chủng học Daniel Brinton", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054013", "hw": "debenture bond", "pos": "phrase", "ipa": "/dɪˈbɛntʃər bɑːnd/", "vi": "trái phiếu tín chấp không thế chấp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054014", "hw": "devil worshiper", "pos": "phrase", "ipa": "/ˈdɛvəl ˈwɜːrʃɪpər/", "vi": "người tôn sùng thờ phụng ác quỷ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054015", "hw": "diatomaceous earth", "pos": "phrase", "ipa": "/ˌdaɪətəˈmeɪʃəs ɜːrθ/", "vi": "đất tảo cát diatomit tự nhiên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054016", "hw": "emiliano zapata", "pos": "phrase", "ipa": "/ˌeɪmiːlˈjɑːnoʊ zəˈpɑːtə/", "vi": "lãnh tụ cách mạng Emiliano Zapata", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054017", "hw": "eusebius of caesarea", "pos": "phrase", "ipa": "/juːˈsiːbiəs əv ˌsɛzəˈriːə/", "vi": "sử gia giám mục Eusebius Caesarea", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054018", "hw": "figural blindness", "pos": "phrase", "ipa": "/ˈfɪɡjərəl ˈblaɪndnɪs/", "vi": "chứng mù nhận dạng hình khối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054019", "hw": "genus malus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈmeɪləs/", "vi": "chi Táo tây thực vật học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054020", "hw": "genus ruta", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈruːtə/", "vi": "chi cây Cửu lý hương Ruta", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054021", "hw": "genus samia", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈseɪmiə/", "vi": "chi bướm tằm hoang dại Samia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054022", "hw": "genus zea", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈziːə/", "vi": "chi Ngô lương thực ngô bắp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054023", "hw": "grass vetch", "pos": "phrase", "ipa": "/ɡræs vɛtʃ/", "vi": "loài cây đậu cỏ lá hẹp hoa đỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054024", "hw": "heat of solidification", "pos": "phrase", "ipa": "/hiːt əv səˌlɪdɪfɪˈkeɪʃən/", "vi": "nhiệt lượng đông đặc vật lý", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054025", "hw": "hereditary cerebellar ataxia", "pos": "phrase", "ipa": "/həˈrɛdɪtɛri ˌsɛrəˈbɛlər əˈtæksiə/", "vi": "thất điều tiểu não di truyền", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054026", "hw": "hero worshiper", "pos": "phrase", "ipa": "/ˈhɪəroʊ ˈwɜːrʃɪpər/", "vi": "người tôn sùng người hùng hết mực", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054027", "hw": "hugger mugger", "pos": "phrase", "ipa": "/ˈhʌɡər ˈmʌɡər/", "vi": "hành động lén lút; cảnh hỗn độn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054028", "hw": "hungarian goulash", "pos": "phrase", "ipa": "/hʌŋˈɡɛəriən ˈɡuːlæʃ/", "vi": "món súp bò hầm goulash Hungary", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054029", "hw": "icelandic krona", "pos": "phrase", "ipa": "/aɪsˈlændɪk ˈkroʊnə/", "vi": "đồng tiền króna của Iceland", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054030", "hw": "imogene coca", "pos": "phrase", "ipa": "/ˈɪmədʒiːn ˈkoʊkə/", "vi": "nữ diễn viên hài Imogene Coca", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054031", "hw": "inferior rectus", "pos": "phrase", "ipa": "/ɪnˈfɪəriər ˈrɛktəs/", "vi": "cơ thẳng dưới vận động mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054032", "hw": "inferior rectus muscle", "pos": "phrase", "ipa": "/ɪnˈfɪəriər ˈrɛktəs ˈmʌsəl/", "vi": "cơ thẳng dưới nhãn cầu mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054033", "hw": "intercostal muscle", "pos": "phrase", "ipa": "/ˌɪntərˈkɑːstəl ˈmʌsəl/", "vi": "cơ liên sườn giữa các xương sườn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054034", "hw": "karen horney", "pos": "phrase", "ipa": "/ˈkærən ˈhɔːrnaɪ/", "vi": "nhà phân tâm học nữ Karen Horney", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054035", "hw": "kasai river", "pos": "phrase", "ipa": "/kəˈsaɪ ˈrɪvər/", "vi": "dòng sông Kasai ở trung châu Phi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054036", "hw": "kura river", "pos": "phrase", "ipa": "/ˈkʊərə ˈrɪvər/", "vi": "dòng sông Kura vùng Kavkaz", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054037", "hw": "lateral rectus", "pos": "phrase", "ipa": "/ˈlætərəl ˈrɛktəs/", "vi": "cơ thẳng ngoài nhãn cầu mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054038", "hw": "lateral rectus muscle", "pos": "phrase", "ipa": "/ˈlætərəl ˈrɛktəs ˈmʌsəl/", "vi": "cơ thẳng ngoài vận động nhãn cầu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054039", "hw": "lexical disambiguation", "pos": "phrase", "ipa": "/ˈlɛksɪkəl ˌdɪsæmˌbɪɡjuˈeɪʃən/", "vi": "khử nhập nhằng nghĩa từ ngữ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054040", "hw": "linebacker blitzing", "pos": "phrase", "ipa": "/ˈlaɪnbækər ˈblɪtsɪŋ/", "vi": "đòn đột kích chớp nhoáng của hậu vệ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054041", "hw": "lupus erythematosus", "pos": "phrase", "ipa": "/ˈluːpəs ˌɛrɪˌθiːməˈtoʊsəs/", "vi": "bệnh tự miễn lupus ban đỏ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054042", "hw": "mackinaw blanket", "pos": "phrase", "ipa": "/ˈmækɪnɔː ˈblæŋkɪt/", "vi": "chăn len dày ấm họa tiết kẻ ca-rô", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054043", "hw": "marcus aurelius antoninus", "pos": "phrase", "ipa": "/ˈmɑːrkəs ɔːˈriːliəs ˌæntəˈnaɪnəs/", "vi": "hoàng đế La Mã Marcus Aurelius", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054044", "hw": "marquise de pompadour", "pos": "phrase", "ipa": "/mɑːrˈkiːz də ˈpɒmpədʊər/", "vi": "nữ Hầu tước phu nhân Pompadour", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054045", "hw": "matrilineal kin", "pos": "phrase", "ipa": "/ˌmætrɪˈlɪniəl kɪn/", "vi": "họ hàng thân tộc thuộc bên ngoại", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054046", "hw": "medullary ray", "pos": "phrase", "ipa": "/ˈmɛdəlɛri reɪ/", "vi": "tia tủy trong thân cây gỗ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054047", "hw": "mesenteric artery", "pos": "phrase", "ipa": "/ˌmɛzənˈtɛrɪk ˈɑːrtəri/", "vi": "động mạch mạc treo ruột bụng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054048", "hw": "mesenteric vein", "pos": "phrase", "ipa": "/ˌmɛzənˈtɛrɪk veɪn/", "vi": "tĩnh mạch mạc treo dẫn máu ruột", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054049", "hw": "milk vetch", "pos": "phrase", "ipa": "/mɪlk vɛtʃ/", "vi": "cây hoàng kỳ; cây đậu sữa dại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054050", "hw": "mot juste", "pos": "phrase", "ipa": "/ˌmoʊ ˈʒuːst/", "vi": "từ ngữ đắt giá; cách dùng từ chuẩn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054051", "hw": "multistage rocket", "pos": "phrase", "ipa": "/ˈmʌltisteɪdʒ ˈrɑːkɪt/", "vi": "tên lửa vũ trụ đẩy nhiều tầng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054052", "hw": "new world leishmaniasis", "pos": "phrase", "ipa": "/nuː wɜːrld ˌliːʃməˈnaɪəsɪs/", "vi": "bệnh nhiễm Leishmania châu Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054053", "hw": "nicolaus copernicus", "pos": "phrase", "ipa": "/ˌnɪkəˈleɪəs koʊˈpɜːrnɪkəs/", "vi": "nhà thiên văn Nicolaus Copernicus", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054054", "hw": "nooks and crannies", "pos": "phrase", "ipa": "/nʊks ænd ˈkræniz/", "vi": "từng ngóc ngách kẽ hở mọi nơi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054055", "hw": "old world leishmaniasis", "pos": "phrase", "ipa": "/oʊld wɜːrld ˌliːʃməˈnaɪəsɪs/", "vi": "bệnh leishmania ngoài da", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054056", "hw": "perennial ragweed", "pos": "phrase", "ipa": "/pəˈrɛniəl ˈræɡwiːd/", "vi": "cỏ phấn hương sống lâu năm dại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054057", "hw": "peruvian mastic tree", "pos": "phrase", "ipa": "/pəˈruːviən ˈmæstɪk triː/", "vi": "cây tiêu hồng Peru lấy nhựa thơm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054058", "hw": "piet mondrian", "pos": "phrase", "ipa": "/piːt ˈmɒndriɑːn/", "vi": "danh họa trừu tượng Piet Mondrian", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054059", "hw": "populus nigra", "pos": "phrase", "ipa": "/ˈpɒpjʊləs ˈnaɪɡrə/", "vi": "loài cây dương đen châu Âu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054060", "hw": "proscenium arch", "pos": "phrase", "ipa": "/proʊˈsiːniəm ɑːrtʃ/", "vi": "khung vòm ngăn sân khấu nhà hát", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054061", "hw": "purple milk vetch", "pos": "phrase", "ipa": "/ˈpɜːrpəl mɪlk vɛtʃ/", "vi": "cây hoàng kỳ hoa tím thảo dược", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054062", "hw": "ragweed pollen", "pos": "phrase", "ipa": "/ˈræɡwiːd ˈpɑːlən/", "vi": "phấn hoa cỏ phấn hương dị ứng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054063", "hw": "rectus inferior", "pos": "phrase", "ipa": "/ˈrɛktəs ɪnˈfɪəriər/", "vi": "cơ thẳng dưới nhãn cầu mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054064", "hw": "reverend dodgson", "pos": "phrase", "ipa": "/ˈrɛvərənd ˈdɑːdʒsən/", "vi": "mục sư Charles Dodgson tác giả", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054065", "hw": "river kasai", "pos": "phrase", "ipa": "/ˈrɪvər kəˈsaɪ/", "vi": "dòng sông Kasai miền trung châu Phi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054066", "hw": "robert edwin peary", "pos": "phrase", "ipa": "/ˈrɑːbərt ˈɛdwɪn ˈpɪəri/", "vi": "nhà thám hiểm Robert Edwin Peary", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054067", "hw": "sagebrush mariposa tulip", "pos": "phrase", "ipa": "/ˈseɪdʒbrʌʃ ˌmærɪˈpoʊsə ˈtuːlɪp/", "vi": "hoa huệ đồng cỏ mariposa tím", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054068", "hw": "samia cynthia", "pos": "phrase", "ipa": "/ˈseɪmiə ˈsɪnθiə/", "vi": "loài bướm đêm tằm cánh to", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054069", "hw": "scarlet pimpernel", "pos": "phrase", "ipa": "/ˈskɑːrlət ˈpɪmpərnɛl/", "vi": "cây an lạc hoa đỏ tươi nở rộ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054070", "hw": "sir alexander korda", "pos": "phrase", "ipa": "/sɜːr ˌælɪɡˈzændər ˈkɔːrdə/", "vi": "đạo diễn phim Sir Alexander Korda", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054071", "hw": "somatosensory system", "pos": "phrase", "ipa": "/soʊˌmætoʊˈsɛnsəri ˈsɪstəm/", "vi": "hệ thần kinh cảm giác thân thể", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054072", "hw": "spring vetch", "pos": "phrase", "ipa": "/sprɪŋ vɛtʃ/", "vi": "cây đậu tằm dại vụ xuân làm phân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054073", "hw": "sun worshiper", "pos": "phrase", "ipa": "/sʌn ˈwɜːrʃɪpər/", "vi": "người thờ mặt trời; người tắm nắng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054074", "hw": "superior rectus muscle", "pos": "phrase", "ipa": "/suːˈpɪəriər ˈrɛktəs ˈmʌsəl/", "vi": "cơ thẳng trên nhãn cầu mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054075", "hw": "sweet vetch", "pos": "phrase", "ipa": "/swiːt vɛtʃ/", "vi": "loài cây họ đậu rễ ngọt hoa đỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054076", "hw": "thomas babington macaulay", "pos": "phrase", "ipa": "/ˈtɑːməs ˈbæbɪŋtən məˈkɔːli/", "vi": "sử gia Thomas Babington Macaulay", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054077", "hw": "virginian sumac", "pos": "phrase", "ipa": "/vərˈdʒɪniən ˈsuːmæk/", "vi": "cây sơn thù du có lông Virginia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054078", "hw": "western tamarack", "pos": "phrase", "ipa": "/ˈwɛstərn ˈtæməræk/", "vi": "cây thông rụng lá phương Tây", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054079", "hw": "yellow oleander", "pos": "phrase", "ipa": "/ˈjɛloʊ ˌoʊliˈændər/", "vi": "cây trúc đào hoa vàng có độc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054080", "hw": "adenocarcinomata", "pos": "noun", "ipa": "/ˌædɪnoʊˌkɑːrsɪˈnoʊmətə/", "vi": "các khối ung thư biểu mô tuyến", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054081", "hw": "aedeses", "pos": "noun", "ipa": "/iːˈiːdiːzɪz/", "vi": "những con muỗi vằn Aedes", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054082", "hw": "angiotensins", "pos": "noun", "ipa": "/ˌændʒioʊˈtɛnsɪnz/", "vi": "các hormone co mạch angiotensin", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054083", "hw": "arcas", "pos": "noun", "ipa": "/ˈɑːrkəz/", "vi": "các loài sò thuộc chi sò lông Arca", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054084", "hw": "auteurs", "pos": "noun", "ipa": "/oʊˈtɜːrz/", "vi": "đạo diễn có phong cách riêng biệt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054085", "hw": "baggers", "pos": "noun", "ipa": "/ˈbæɡərz/", "vi": "nhân viên đóng gói hàng vào túi", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054086", "hw": "barmaids", "pos": "noun", "ipa": "/ˈbɑːrmeɪdz/", "vi": "những nữ nhân viên phục vụ quầy bar", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054087", "hw": "bedchambers", "pos": "noun", "ipa": "/ˈbɛdtʃeɪmbərz/", "vi": "các phòng ngủ riêng của quý tộc", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054088", "hw": "beelines", "pos": "noun", "ipa": "/ˈbiːlaɪnz/", "vi": "những đường bay thẳng tắp tới đích", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054089", "hw": "bifurcations", "pos": "noun", "ipa": "/ˌbaɪfərˈkeɪʃənz/", "vi": "những điểm ngã ba chia nhánh đôi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054090", "hw": "bluestones", "pos": "noun", "ipa": "/ˈbluːstoʊnz/", "vi": "đá sa thạch xám xanh; đá lam", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054091", "hw": "brattier", "pos": "adj", "ipa": "/ˈbrætiər/", "vi": "hỗn xược hư đốn hơn mè nheo hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054092", "hw": "brattiest", "pos": "adj", "ipa": "/ˈbrætiɪst/", "vi": "hỗn xược hư đốn nhất mè nheo nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054093", "hw": "broomsticks", "pos": "noun", "ipa": "/ˈbruːmstɪks/", "vi": "cán chổi quét; cán chổi phù thủy", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054094", "hw": "cakewalks", "pos": "noun", "ipa": "/ˈkeɪkwɔːks/", "vi": "việc dễ như trở bàn tay; điệu nhảy", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054095", "hw": "capitalisations", "pos": "noun", "ipa": "/ˌkæpɪtəlaɪˈzeɪʃənz/", "vi": "việc viết hoa; mức vốn hóa công ty", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054096", "hw": "carjackings", "pos": "noun", "ipa": "/ˈkɑːrdʒækɪŋz/", "vi": "vụ dùng vũ khí cướp xe trên đường", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054097", "hw": "clammier", "pos": "adj", "ipa": "/ˈklæmiər/", "vi": "ẩm ướt lành lạnh nhớp nháp hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054098", "hw": "clammiest", "pos": "adj", "ipa": "/ˈklæmiɪst/", "vi": "ẩm ướt nhớp nháp lạnh lẽo nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054099", "hw": "clydesdales", "pos": "noun", "ipa": "/ˈklaɪdzdeɪlz/", "vi": "giống ngựa thồ to lớn Clydesdale", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054100", "hw": "convolutions", "pos": "noun", "ipa": "/ˌkɑːnvəˈluːʃənz/", "vi": "nếp cuộn não; sự uốn lượn rối rắm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054101", "hw": "copilots", "pos": "noun", "ipa": "/ˈkoʊpaɪləts/", "vi": "các phi công lái phụ của máy bay", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part1_data) == 100, f"Length is {len(part1_data)}"

with open('scratch/b31_r09_raw_p1.json') as f:
    raw = json.load(f)

for i, (item, raw_item) in enumerate(zip(part1_data, raw)):
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

with open('scratch/b31_r09_p1.json', 'w', encoding='utf-8') as f:
    json.dump(part1_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 1")
