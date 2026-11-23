import json

items = [
    ("067003", "strads", "noun", "/strædz/", "đàn vĩ cầm danh tiếng Stradivarius"),
    ("067004", "streambeds", "noun", "/ˈstriːmˌbɛdz/", "lòng suối; đáy dòng chảy sông suối"),
    ("067005", "supertankers", "noun", "/ˈsuːpərˌtæŋkərz/", "siêu tàu chở dầu trọng tải khổng lồ"),
    ("067006", "sweetpeas", "noun", "/ˈswiːtˌpiːz/", "cây hoa đậu thơm leo màu sắc"),
    ("067007", "teakettles", "noun", "/ˈtiːˌkɛtəlz/", "ấm đun nước sôi có quai vòi"),
    ("067008", "tontines", "noun", "/ˈtɒnˌtiːnz/", "quỹ góp vốn tontine hưởng chung"),
    ("067009", "trenchers", "noun", "/ˈtrɛntʃərz/", "thớt gỗ dọn ăn; người đào hào rãnh"),
    ("067010", "triamcinolones", "noun", "/ˌtraɪæmˈsɪnəloʊnz/", "thuốc kháng viêm corticoid bôi da"),
    ("067011", "trichotillomanias", "noun", "/ˌtrɪkəˌtɪləˈmeɪniəz/", "hội chứng tự bứt nhổ tóc bệnh lý"),
    ("067012", "triticums", "noun", "/ˈtrɪtɪkəmz/", "cây lúa mì thuộc chi Triticum"),
    ("067013", "tsugas", "noun", "/ˈtsuːɡəz/", "cây thông độc cần thuộc chi Tsuga"),
    ("067014", "turkomans", "noun", "/ˈtɜːrkəmənz/", "người dân tộc Turkmen Trung Á"),
    ("067015", "variorums", "noun", "/ˌvɛəriˈɔːrəmz/", "ấn bản sách kèm chú giải tổng hợp"),
    ("067016", "vitalisms", "noun", "/ˈvaɪtəˌlɪzəmz/", "thuyết sinh lực luận triết sinh học"),
    ("067017", "wastrels", "noun", "/ˈweɪstrəlz/", "kẻ ăn chơi hoang phí vô dụng"),
    ("067018", "weighbridges", "noun", "/ˈweɪˌbrɪdʒɪz/", "trạm cân xe tải trọng lượng lớn"),
    ("067019", "whapped", "verb", "/wæpt/", "đã đánh đập hoặc vỗ thật mạnh"),
    ("067020", "whapping", "verb", "/ˈwæpɪŋ/", "đang đập mạnh; cú đánh nảy lửa"),
    ("067021", "whaps", "verb", "/wæps/", "đánh đập hoặc va đập kêu bộp"),
    ("067022", "yobos", "noun", "/ˈjoʊboʊz/", "tên côn đồ lưu manh du côn (Anh)"),
    ("067023", "adductions", "noun", "/əˈdʌkʃənz/", "cử động khép chi vào trục cơ thể"),
    ("067024", "advertorials", "noun", "/ˌædvərˈtɔːriəlz/", "bài quảng cáo viết kiểu bài báo"),
    ("067025", "airwaves", "noun", "/ˈɛərˌweɪvz/", "sóng phát thanh và truyền hình"),
    ("067026", "atriplex mexicana", "phrase", "/ˈætrɪplɛks ˌmɛksɪˈkeɪnə/", "cây rau muối nguồn gốc Mexico"),
    ("067027", "bandoliers", "noun", "/ˌbændəˈlɪərz/", "dây đai đeo đạn vắt chéo qua vai"),
    ("067028", "barbados maidenhair", "phrase", "/bɑːrˈbeɪdɒs ˈmeɪdənˌhɛər/", "dương xỉ tóc thần nữ Barbados"),
    ("067029", "bascules", "noun", "/ˈbæskjuːlz/", "cầu mở nâng nhịp đối trọng"),
    ("067030", "battle of solferino", "phrase", "/ˈbætəl əv ˌsɒlfəˈriːnoʊ/", "trận đánh Solferino năm 1859 ở Ý"),
    ("067031", "bedfellows", "noun", "/ˈbɛdˌfɛloʊz/", "bạn ngủ chung; đồng minh bất đắc dĩ"),
    ("067032", "bedsteads", "noun", "/ˈbɛdˌstɛdz/", "khung sườn giường ngủ bằng gỗ sắt"),
    ("067033", "bermuda maidenhair", "phrase", "/bərˈmjuːdə ˈmeɪdənˌhɛər/", "dương xỉ tóc thần nữ Bermuda"),
    ("067034", "bespeaking", "verb", "/bɪˈspiːkɪŋ/", "đang biểu thị dấu hiệu; đặt trước"),
    ("067035", "bespeaks", "verb", "/bɪˈspiːks/", "chứng tỏ; báo hiệu trước điều gì"),
    ("067036", "booted armillaria", "phrase", "/ˈbuːtɪd ˌɑːrmɪˈlɛəriə/", "nấm mật ong có vòng cổ Armillaria"),
    ("067037", "boulles", "noun", "/buːlz/", "đồ gỗ khảm đồng đồi mồi Boulle"),
    ("067038", "brassica oleracea botrytis", "phrase", "/ˈbræsɪkə ˌɒləˈreɪsiə bɒˈtraɪtɪs/", "cây cải bông trắng; súp lơ trắng"),
    ("067039", "brown lacewing", "phrase", "/braʊn ˈleɪsˌwɪŋ/", "côn trùng cánh ren nâu ăn rệp"),
    ("067040", "brueghels", "noun", "/ˈbrɔɪɡəlz/", "danh họa Hà Lan Pieter Bruegel"),
    ("067041", "brunns", "noun", "/brʊnz/", "nhà toán học Đức Hermann Brunn"),
    ("067042", "calcanei", "noun", "/kælˈkeɪniaɪ/", "xương gót chân ở bàn chân"),
    ("067043", "calcaneuses", "noun", "/kælˈkeɪniəsɪz/", "xương gót nâng đỡ phần sau bàn chân"),
    ("067044", "caloosahatchee canal", "phrase", "/kəˌluːsəˈhætʃi kəˈnæl/", "kênh đào Caloosahatchee ở Florida"),
    ("067045", "caloosahatchee river", "phrase", "/kəˌluːsəˈhætʃi ˈrɪvər/", "sông Caloosahatchee ở Florida Mỹ"),
    ("067046", "carcases", "noun", "/ˈkɑːrkəsɪz/", "xác động vật chết; bộ khung sườn"),
    ("067047", "cardioids", "noun", "/ˈkɑːrdiˌɔɪdz/", "đường cong toán học hình trái tim"),
    ("067048", "carica papaya", "phrase", "/ˈkærɪkə pəˈpaɪə/", "cây đu đủ trồng lấy quả ăn"),
    ("067049", "catalpa speciosa", "phrase", "/kəˈtælpə ˌspiːʃiˈoʊsə/", "cây gỗ catalpa hoa trắng Bắc Mỹ"),
    ("067050", "cecropia moth", "phrase", "/sɪˈkroʊpiə mɒθ/", "ngài đêm khổng lồ cecropia Bắc Mỹ"),
    ("067051", "centromeres", "noun", "/ˈsɛntrəˌmɪərz/", "tâm động của nhiễm sắc thể"),
    ("067052", "climbing maidenhair", "phrase", "/ˈklaɪmɪŋ ˈmeɪdənˌhɛər/", "cây dương xỉ dây leo Bắc Mỹ"),
    ("067053", "common maidenhair", "phrase", "/ˈkɒmən ˈmeɪdənˌhɛər/", "cây dương xỉ ráng đuôi chồn thường"),
    ("067054", "common osier", "phrase", "/ˈkɒmən ˈoʊʒər/", "cây liễu mềm đan giỏ châu Âu"),
    ("067055", "conceptualised", "verb", "/kənˈsɛptʃʊəˌlaɪzd/", "đã hình thành khái niệm ý tưởng"),
    ("067056", "conceptualises", "verb", "/kənˈsɛptʃʊəˌlaɪzɪz/", "hình thành khái niệm lý thuyết"),
    ("067057", "conceptualising", "verb", "/kənˈsɛptʃʊəˌlaɪzɪŋ/", "đang hình thành khái niệm ý tưởng"),
    ("067058", "confabulations", "noun", "/kənˌfæbjəˈleɪʃənz/", "cuộc trò chuyện; chứng bịa chuyện"),
    ("067059", "corylus americana", "phrase", "/ˈkɒrɪləs əˌmɛrɪˈkeɪnə/", "cây hạt phỉ hoang dã Bắc Mỹ"),
    ("067060", "culiacans", "noun", "/ˌkuːliəˈkɑːnz/", "thành phố Culiacán tây bắc Mexico"),
    ("067061", "cupbearers", "noun", "/ˈkʌpˌbɛərərz/", "người hầu rót rượu cho vua chúa"),
    ("067062", "curcuma longa", "phrase", "/ˈkɜːrkjʊmə ˈlɒŋɡə/", "cây nghệ vàng trồng lấy củ gia vị"),
    ("067063", "curtilages", "noun", "/ˈkɜːrtəlɪdʒɪz/", "khuôn viên sân vườn bao quanh nhà"),
    ("067064", "cycad family", "phrase", "/ˈsaɪkæd ˈfæməli/", "họ Tuế thực vật hạt trần cổ đại"),
    ("067065", "cyperus longus", "phrase", "/saɪˈpɪərəs ˈlɒŋɡəs/", "cây cói thơm mọc vùng đầm lầy"),
    ("067066", "dashikis", "noun", "/dɑːˈʃiːkiz/", "áo thụng sặc sỡ truyền thống Phi"),
    ("067067", "diagnosticians", "noun", "/ˌdaɪəɡnɒˈstɪʃənz/", "chuyên gia chẩn đoán bệnh hoặc lỗi"),
    ("067068", "dichroisms", "noun", "/ˈdaɪkroʊˌɪzəmz/", "hiện tượng lưỡng sắc tinh thể"),
    ("067069", "dobriches", "noun", "/ˈdɒbrɪtʃɪz/", "thành phố Dobrich ở Bulgaria"),
    ("067070", "drumlins", "noun", "/ˈdrʌmlɪnz/", "gò đồi thuôn do băng hà bồi tụ"),
    ("067071", "dysmenorrheas", "noun", "/ˌdɪsmɛnəˈriːəz/", "chứng đau bụng kinh dữ dội"),
    ("067072", "edirnes", "noun", "/ɛˈdɪərneɪz/", "thành phố Edirne ở Thổ Nhĩ Kỳ"),
    ("067073", "emancipators", "noun", "/ɪˈmænsɪˌpeɪtərz/", "người giải phóng nô lệ hoặc áp bức"),
    ("067074", "emmentals", "noun", "/ˈɛməntɑːlz/", "phô mai lỗ tròn Emmental Thụy Sĩ"),
    ("067075", "enchiridia", "noun", "/ˌɛŋkaɪˈrɪdiə/", "sách cẩm nang hướng dẫn bỏ túi"),
    ("067076", "enchiridions", "noun", "/ˌɛŋkaɪˈrɪdiənz/", "sổ tay triết lý hoặc cẩm nang nhỏ"),
    ("067077", "eosinophils", "noun", "/ˌiːəˈsɪnəfɪlz/", "bạch cầu ái toan chống ký sinh"),
    ("067078", "fadeouts", "noun", "/ˈfeɪdˌaʊts/", "hiệu ứng tối mờ dần cuối cảnh phim"),
    ("067079", "family compositae", "phrase", "/ˈfæməli kəmˈpɒzɪtiː/", "họ Cúc thực vật có hoa lớn nhất"),
    ("067080", "flocs", "noun", "/flɒks/", "cụm bông kết tụ lơ lửng trong dịch"),
    ("067081", "folliculitides", "noun", "/fɒˌlɪkjʊˈlaɪtɪdiːz/", "bệnh viêm nang lông trên da"),
    ("067082", "fringed loosestrife", "phrase", "/frɪndʒd ˈluːsˌstraɪf/", "cây trân châu vàng tua mép lá"),
    ("067083", "genus batis", "phrase", "/ˈdʒiːnəs ˈbeɪtɪs/", "chi cây muối mặn ven biển Batis"),
    ("067084", "genus cecropia", "phrase", "/ˈdʒiːnəs sɪˈkroʊpiə/", "chi cây gỗ kèn Cecropia"),
    ("067085", "genus cupressus", "phrase", "/ˈdʒiːnəs kjuːˈprɛsəs/", "chi cây hoàng đàn bách Cupressus"),
    ("067086", "genus dioscorea", "phrase", "/ˈdʒiːnəs ˌdaɪəˈskɔːriə/", "chi củ mài khoai mỡ Dioscorea"),
    ("067087", "genus eupatorium", "phrase", "/ˈdʒiːnəs ˌjuːpəˈtɔːriəm/", "chi cây cỏ lào trạch lan Eupatorium"),
    ("067088", "genus fragaria", "phrase", "/ˈdʒiːnəs frəˈɡɛəriə/", "chi cây dâu tây quả đỏ Fragaria"),
    ("067089", "genus gypsophila", "phrase", "/ˈdʒiːnəs dʒɪpˈsɒfɪlə/", "chi hoa bi chấm trắng Gypsophila"),
    ("067090", "genus smilax", "phrase", "/ˈdʒiːnəs ˈsmaɪlæks/", "chi cây khúc khắc kim cang Smilax"),
    ("067091", "genus teredo", "phrase", "/ˈdʒiːnəs təˈriːdoʊ/", "chi con hà ăn gỗ tàu biển Teredo"),
    ("067092", "genus trichomonas", "phrase", "/ˈdʒiːnəs ˌtrɪkəˈmoʊnəs/", "chi trùng roi ký sinh Trichomonas"),
    ("067093", "genus tyto", "phrase", "/ˈdʒiːnəs ˈtaɪtoʊ/", "chi chim cú lợn mặt tim Tyto"),
    ("067094", "glyceraldehydes", "noun", "/ˌɡlɪsəˈrældɪhaɪdz/", "đường đơn ba cacbon glyxeralđehit"),
    ("067095", "golden maidenhair", "phrase", "/ˈɡoʊldən ˈmeɪdənˌhɛər/", "rêu mũ lông vàng golden maidenhair"),
    ("067096", "green lacewing", "phrase", "/ɡriːn ˈleɪsˌwɪŋ/", "côn trùng cánh ren xanh có ích"),
    ("067097", "griots", "noun", "/ˈɡriːoʊz/", "nghệ nhân kể sử truyền miệng Phi"),
    ("067098", "gulf of akaba", "phrase", "/ɡʌlf əv ˈækəbə/", "vịnh Aqaba trên Biển Đỏ"),
    ("067099", "hadean time", "phrase", "/heɪˈdiːən taɪm/", "liên đại Hỏa Thành sơ khai Trái Đất"),
    ("067100", "handbaskets", "noun", "/ˈhændˌbæskɪts/", "giỏ mây xách tay đựng đồ"),
    ("067101", "helpmates", "noun", "/ˈhɛlpˌmeɪts/", "người bạn đời giúp đỡ đồng hành"),
    ("067102", "hepaticas", "noun", "/hɪˈpætɪkəz/", "hoa gan; cây thảo dược hepatica"),
]

with open("scratch/b34_r05_raw_p1.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS {pos} for {hw}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    inner = ipa[1:-1]
    assert inner and not inner.startswith(" ") and not inner.endswith(" "), f"Empty/space IPA: {hw} -> {ipa}"
    rec = dict(r)
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

with open("scratch/b34_r05_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r05_p1.json OK")
