import json

items = [
    ("073703", "padauks", "noun", "/pəˈdɔːks/", "cây giáng hương đỏ gỗ quý padauk"),
    ("073704", "paphiopedilums", "noun", "/ˌpæfioʊˈpɛdɪləmz/", "lan hài thuộc chi Paphiopedilum"),
    ("073705", "patternmakers", "noun", "/ˈpætərnˌmeɪkərz/", "thợ tạo khuôn mẫu đúc hoặc rập may"),
    ("073706", "peeresses", "noun", "/ˈpɪərɪsɪz/", "nữ quý tộc; phu nhân quý tộc Anh"),
    ("073707", "phalacrocoraxes", "noun", "/ˌfælækroʊˈkɔːræksɪz/", "chi Chim cốc biển (Phalacrocorax)"),
    ("073708", "philippopolises", "noun", "/ˌfɪlɪˈpɒpəlɪsɪz/", "thành phố Plovdiv cổ ở Bulgaria"),
    ("073709", "posterboards", "noun", "/ˈpoʊstərˌbɔːrdz/", "tấm bìa cứng dày làm áp phích bảng"),
    ("073710", "primalities", "noun", "/praɪˈmælɪtiz/", "tính nguyên tố của số (toán học)"),
    ("073711", "provokers", "noun", "/prəˈvoʊkərz/", "kẻ khiêu khích kích động gây sự"),
    ("073712", "punicas", "noun", "/ˈpjuːnɪkəz/", "chi Cây lựu ăn quả (Punica)"),
    ("073713", "quincentenaries", "noun", "/ˌkwɪnsɛnˈtɛnəriz/", "lễ kỷ niệm 500 năm (nửa thiên niên)"),
    ("073714", "radioprotections", "noun", "/ˌreɪdioʊprəˈtɛkʃənz/", "biện pháp bảo vệ chống bức xạ"),
    ("073715", "ratels", "noun", "/ˈreɪtəlz/", "lửng mật châu Phi gan dạ"),
    ("073716", "redeterminations", "noun", "/ˌriːdɪtɜːrmɪˈneɪʃənz/", "sự tái xác định lại kết quả mức"),
    ("073717", "riras", "noun", "/ˈriːrəz/", "nhóm vũ trang Real IRA (Ireland)"),
    ("073718", "royalisms", "noun", "/ˈrɔɪəˌlɪzəmz/", "chủ nghĩa bảo hoàng ủng hộ vua"),
    ("073719", "salaats", "noun", "/sɑːˈlɑːts/", "nghi lễ cầu nguyện Hồi giáo Salat"),
    ("073720", "sarcocystises", "noun", "/ˌsɑːrkoʊˈsɪstɪsɪz/", "chi Trùng bào tử ký sinh cơ"),
    ("073721", "sardinas", "noun", "/sɑːrˈdiːnəz/", "chi Cá mòi dầu châu Âu (Sardina)"),
    ("073722", "scabiosas", "noun", "/ˌskeɪbiˈoʊsəz/", "cây hoa nhím biển (chi Scabiosa)"),
    ("073723", "sceloporuses", "noun", "/sɪˈlɒpərəsɪz/", "thằn lằn gai chi Sceloporus"),
    ("073724", "schlemiels", "noun", "/ʃləˈmiːlz/", "kẻ ngốc nghếch vụng về hay gặp xui"),
    ("073725", "sclerotia", "noun", "/sklɪˈroʊʃə/", "hạch nấm (thể nghỉ cứng của nấm)"),
    ("073726", "sclerotiums", "noun", "/sklɪˈroʊʃəmz/", "hạch nấm (thể nghỉ cứng của nấm)"),
    ("073727", "seminomas", "noun", "/ˌsɛmɪˈnoʊməz/", "u ác tính tế bào mầm tinh hoàn"),
    ("073728", "shigellosises", "noun", "/ˌʃɪɡɛˈloʊsɪsɪz/", "bệnh lỵ trực khuẩn Shigella"),
    ("073729", "shrimpers", "noun", "/ˈʃrɪmpərz/", "tàu hoặc người đánh bắt tôm"),
    ("073730", "siliquae", "noun", "/ˈsɪlɪˌkwiː/", "quả cải giác dài (họ Cải)"),
    ("073731", "siliquas", "noun", "/ˈsɪlɪkwəz/", "quả cải giác dài (họ Cải)"),
    ("073732", "strelitzias", "noun", "/strɛˈlɪtsiəz/", "cây hoa thiên điểu (chuối pháo)"),
    ("073733", "substitutabilities", "noun", "/ˌsʌbstɪtjuːtəˈbɪlɪtiz/", "tính có thể thay thế được cho nhau"),
    ("073734", "sunbonnets", "noun", "/ˈsʌnˌbɒnɪts/", "mũ vải rộng vành buộc dây che nắng"),
    ("073735", "swearers", "noun", "/ˈswɛərərz/", "người hay chửi thề; người tuyên thệ"),
    ("073736", "takahes", "noun", "/ˈtɑːkəˌheɪz/", "chim takahe hiếm ở New Zealand"),
    ("073737", "technophiles", "noun", "/ˈtɛknəˌfaɪlz/", "người đam mê yêu thích công nghệ"),
    ("073738", "teletypewriters", "noun", "/ˌtɛlɪˈtaɪpˌraɪtərz/", "máy điện báo đánh chữ truyền tin"),
    ("073739", "tenosynovitides", "noun", "/ˌtɛnoʊsɪnəˈvaɪtɪdiːz/", "bệnh viêm bao gân (y học)"),
    ("073740", "thyrsi", "noun", "/ˈθɜːrsaɪ/", "cụm hoa chùy nhánh (thực vật học)"),
    ("073741", "thyrsuses", "noun", "/ˈθɜːrsəsɪz/", "cụm hoa chùy; gậy thông Dionysus"),
    ("073742", "torreyas", "noun", "/ˈtɔːriəz/", "cây thanh sam hạt nhục chi Torreya"),
    ("073743", "trituruses", "noun", "/ˈtrɪtjʊrəsɪz/", "chi Sa giông nước châu Âu Triturus"),
    ("073744", "vasoconstrictives", "noun", "/ˌveɪzoʊkənˈstrɪktɪvz/", "thuốc hoặc chất gây co mạch máu"),
    ("073745", "vasotecs", "noun", "/ˈveɪzoʊˌtɛks/", "thuốc hạ huyết áp enalapril Vasotec"),
    ("073746", "venographies", "noun", "/vɪˈnɒɡrəfiz/", "kỹ thuật chụp X-quang tĩnh mạch"),
    ("073747", "veronals", "noun", "/ˈvɛrənəlz/", "thuốc ngủ barbiturat Veronal (cũ)"),
    ("073748", "vesuvians", "noun", "/vɪˈsuːviənz/", "khoáng vật vesuvianit; que diêm gió"),
    ("073749", "vulvitises", "noun", "/vʌlˈvaɪtɪsɪz/", "bệnh viêm âm hộ (phụ khoa)"),
    ("073750", "wyclifs", "noun", "/ˈwɪklɪfs/", "nhà cải cách tôn giáo John Wycliffe"),
    ("073751", "yafos", "noun", "/ˈjɑːfoʊz/", "cảng cổ Jaffa (Yafo) ở Israel"),
    ("073752", "yokutses", "noun", "/ˈjoʊkʊtsɪz/", "người và tiếng Yokuts California"),
    ("073753", "agropyrons", "noun", "/ˌæɡrəˈpaɪrɒnz/", "chi Cỏ lúa mì dại (Agropyron)"),
    ("073754", "amazonas", "noun", "/ˌæməˈzoʊnəz/", "chi Vẹt xanh châu Mỹ (Amazona)"),
    ("073755", "archerfishes", "noun", "/ˈɑːrtʃərˌfɪʃɪz/", "cá mang rổ phun nước bắn côn trùng"),
    ("073756", "atrovents", "noun", "/ˈætrəvɛnts/", "thuốc giãn phế quản Atrovent"),
    ("073757", "batfishes", "noun", "/ˈbætˌfɪʃɪz/", "cá dơi biển dẹt hình đĩa"),
    ("073758", "bearwoods", "noun", "/ˈbɛərˌwʊdz/", "cây vỏ gấu cascara bờ tây Mỹ"),
    ("073759", "bhagas", "noun", "/ˈbɑːɡəz/", "thần tài lộc Bhaga Ấn Độ giáo"),
    ("073760", "biotypes", "noun", "/ˈbaɪoʊˌtaɪps/", "kiểu sinh học đồng nhất di truyền"),
    ("073761", "blackbucks", "noun", "/ˈblækˌbʌks/", "linh dương sừng xoắn đen Ấn Độ"),
    ("073762", "bodypainted", "verb", "/ˈbɒdiˌpeɪntɪd/", "đã vẽ nghệ thuật lên cơ thể"),
    ("073763", "bodypainting", "verb", "/ˈbɒdiˌpeɪntɪŋ/", "đang vẽ nghệ thuật lên cơ thể"),
    ("073764", "bodypaints", "verb", "/ˈbɒdiˌpeɪnts/", "vẽ nghệ thuật trực tiếp lên da"),
    ("073765", "brihaspatis", "noun", "/brɪˈhʌspətiz/", "hiền triết Brihaspati (sao Mộc)"),
    ("073766", "cajanuses", "noun", "/kəˈdʒeɪnəsɪz/", "chi Cây đậu triều đậu săng Cajanus"),
    ("073767", "canellas", "noun", "/kəˈnɛləz/", "vỏ quế trắng thơm vùng Caribe"),
    ("073768", "cataleptics", "noun", "/ˌkætəˈlɛptɪks/", "người mắc chứng giữ nguyên tư thế"),
    ("073769", "chlorambucils", "noun", "/klɔːrˈæmbjʊsɪlz/", "thuốc hóa trị bạch cầu chlorambucil"),
    ("073770", "clozarils", "noun", "/ˈklɒzərɪlz/", "thuốc trị tâm thần clozapine"),
    ("073771", "coamings", "noun", "/ˈkoʊmɪŋz/", "thành gờ chắn nước miệng hầm tàu"),
    ("073772", "communizations", "noun", "/ˌkɒmjʊnaɪˈzeɪʃənz/", "quá trình tập thể cộng sản hóa"),
    ("073773", "compulsivities", "noun", "/ˌkɒmpʌlˈsɪvɪtiz/", "tính cưỡng bức thôi thúc lặp lại"),
    ("073774", "continuants", "noun", "/kənˈtɪnjʊənts/", "âm liên tục kéo dài (ngữ âm học)"),
    ("073775", "costochondritises", "noun", "/ˌkɒstoʊkɒnˈdraɪtɪsɪz/", "bệnh viêm sụn khớp sườn-ức"),
    ("073776", "cottagers", "noun", "/ˈkɒtɪdʒərz/", "người sống trong nhà tranh thôn quê"),
    ("073777", "cryobiologies", "noun", "/ˌkraɪoʊbaɪˈɒlədʒiz/", "ngành sinh học nhiệt độ cực thấp"),
    ("073778", "crystallographers", "noun", "/ˌkrɪstəˈlɒɡrəfərz/", "nhà nghiên cứu tinh thể học"),
    ("073779", "cubituses", "noun", "/ˈkjuːbɪtəsɪz/", "khớp khuỷu tay; xương trụ (y học)"),
    ("073780", "cymries", "noun", "/ˈkɪmriz/", "người dân xứ Wales (biến thể)"),
    ("073781", "davyses", "noun", "/ˈdeɪvɪsɪz/", "nhà thám hiểm Bắc Cực John Davis"),
    ("073782", "decorticated", "verb", "/diːˈkɔːrtɪˌkeɪtɪd/", "đã bóc vỏ ngoài hoặc vỏ não"),
    ("073783", "decorticates", "verb", "/diːˈkɔːrtɪˌkeɪts/", "bóc tách lớp vỏ ngoài; cắt vỏ não"),
    ("073784", "decorticating", "verb", "/diːˈkɔːrtɪˌkeɪtɪŋ/", "đang bóc lớp vỏ; cắt vỏ cơ quan"),
    ("073785", "deoxyguanosines", "noun", "/diˌɒksiˈɡwɑːnəsiːnz/", "nucleoside deoxyguanosine (ADN)"),
    ("073786", "desorbed", "verb", "/diːˈzɔːrbd/", "đã giải hấp tách chất khỏi bề mặt"),
    ("073787", "desorbing", "verb", "/diːˈzɔːrbɪŋ/", "đang giải hấp khỏi bề mặt"),
    ("073788", "desorbs", "verb", "/diːˈzɔːrbz/", "giải hấp phóng thích khỏi bề mặt"),
    ("073789", "diaerses", "noun", "/daɪˈɛərɪsiːz/", "dấu hai chấm tách âm; sự tách âm"),
    ("073790", "diophantuses", "noun", "/ˌdaɪəˈfæntəsɪz/", "nhà toán học Hy Lạp Diophantus"),
    ("073791", "disfigurations", "noun", "/dɪsˌfɪɡjʊˈreɪʃənz/", "sự làm biến dạng hủy hoại dung mạo"),
    ("073792", "dysphasias", "noun", "/dɪsˈfeɪʒəz/", "chứng rối loạn ngôn ngữ do tổn não"),
    ("073793", "eddoes", "noun", "/ˈɛdoʊz/", "củ khoai sọ nhiệt đới eddo"),
    ("073794", "eddos", "noun", "/ˈɛdoʊz/", "củ khoai sọ nhiệt đới eddo"),
    ("073795", "eleocharises", "noun", "/ˌɛliəˈkɛərɪsɪz/", "chi Cỏ năn bộp (củ năng Eleocharis)"),
    ("073796", "elkhounds", "noun", "/ˈɛlkˌhaʊndz/", "chó săn nai sừng tấm Na Uy"),
    ("073797", "esakis", "noun", "/ɛˈsɑːkiz/", "nhà vật lý Nobel Nhật Leo Esaki"),
    ("073798", "eutherians", "noun", "/juːˈθɪəriənz/", "nhóm Thú có nhau thai hoàn chỉnh"),
    ("073799", "exteriorizations", "noun", "/ɪkˌstɪəriəraɪˈzeɪʃənz/", "sự biểu lộ bộc lộ ra bên ngoài"),
    ("073800", "fieldworkers", "noun", "/ˈfiːldˌwɜːrkərz/", "người điền dã; nhân viên thực địa"),
    ("073801", "fogies", "noun", "/ˈfoʊɡiz/", "người già bảo thủ cổ hủ lạc hậu"),
    ("073802", "gikuyus", "noun", "/ɡɪˈkuːjuːz/", "dân tộc và tiếng Kikuyu ở Kenya"),
]

with open("scratch/b35_r08_raw_p3.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS: {pos}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    assert not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"Space in IPA: {hw} -> {ipa}"
    out.append({**r, "pos": pos, "ipa": ipa, "vi": vi, "status": "reviewed"})

with open("scratch/b35_r08_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r08_p3.json OK")
