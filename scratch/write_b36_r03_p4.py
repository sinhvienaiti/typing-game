import json

rows = [
    ("076303", "photogram", "noun", "/ˈfoʊtəɡræm/", "ảnh trắc quang; ảnh chụp trực tiếp"),
    ("076304", "photogrammeter", "noun", "/ˌfoʊtəˈɡræmɪtər/", "máy trắc quang ảnh (đo ảnh)"),
    ("076305", "photogrammetry", "noun", "/ˌfoʊtəˈɡræmɪtri/", "phép đo ảnh (trắc quang ảnh)"),
    ("076306", "photographable", "adj", "/ˌfoʊtəˈɡræfəbəl/", "có thể chụp ảnh được"),
    ("076307", "photographers", "noun", "/fəˈtɑːɡrəfərz/", "nhiếp ảnh gia; thợ chụp ảnh"),
    ("076308", "photographies", "noun", "/fəˈtɒɡrəfiz/", "nghệ thuật hoặc ngành nhiếp ảnh"),
    ("076309", "photoheliograph", "noun", "/ˌfoʊtoʊˈhiːlioʊɡræf/", "kính thiên văn chụp Mặt Trời"),
    ("076310", "photoinactivation", "noun", "/ˌfoʊtoʊɪnˌæktɪˈveɪʃən/", "sự bất hoạt hóa do ánh sáng"),
    ("076311", "photoinduced", "adj", "/ˌfoʊtoʊɪnˈdjuːst/", "được kích hoạt bởi ánh sáng"),
    ("076312", "photoing", "verb", "/ˈfoʊtoʊɪŋ/", "chụp ảnh, chụp hình"),
    ("076313", "photoionization", "noun", "/ˌfoʊtoʊˌaɪənaɪˈzeɪʃən/", "sự quang ion hóa (vật lý)"),
    ("076314", "photokinesis", "noun", "/ˌfoʊtoʊkɪˈniːsɪs/", "tính quang động (sinh vật học)"),
    ("076315", "photolitgraphy", "noun", "/ˌfoʊtoʊlɪˈθɒɡrəfi/", "kỹ thuật in thạch bản ảnh"),
    ("076316", "photolithograph", "noun", "/ˌfoʊtoʊˈlɪθəɡræf/", "bản in thạch bản ảnh"),
    ("076317", "photolithographer", "noun", "/ˌfoʊtoʊlɪˈθɒɡrəfər/", "thợ in thạch bản ảnh"),
    ("076318", "photoluminescence", "noun", "/ˌfoʊtoʊˌluːmɪˈnɛsəns/", "sự quang phát quang (vật lý)"),
    ("076319", "photolysis", "noun", "/foʊˈtɒlɪsɪs/", "sự quang phân (hóa học, sinh học)"),
    ("076320", "photolytic", "adj", "/ˌfoʊtəˈlɪtɪk/", "thuộc sự quang phân"),
    ("076321", "photolytically", "adv", "/ˌfoʊtəˈlɪtɪkli/", "bằng phương pháp quang phân"),
    ("076322", "photomacrography", "noun", "/ˌfoʊtoʊməˈkrɒɡrəfi/", "chụp ảnh cận cảnh phóng đại lớn"),
    ("076323", "photomagnetic", "adj", "/ˌfoʊtoʊmæɡˈnɛtɪk/", "thuộc hiệu ứng quang từ"),
    ("076324", "photomap", "noun", "/ˈfoʊtoʊˌmæp/", "bản đồ ghép từ không ảnh"),
    ("076325", "photomechanics", "noun", "/ˌfoʊtoʊmɪˈkænɪks/", "kỹ thuật chế bản in quang cơ"),
    ("076326", "photometers", "noun", "/foʊˈtɒmɪtərz/", "máy đo cường độ sáng (quang kế)"),
    ("076327", "photometrical", "adj", "/ˌfoʊtəˈmɛtrɪkəl/", "thuộc phép đo ánh sáng (trắc quang)"),
    ("076328", "photometrically", "adv", "/ˌfoʊtəˈmɛtrɪkli/", "bằng phương pháp trắc quang"),
    ("076329", "photometrician", "noun", "/ˌfoʊtoʊmɪˈtrɪʃən/", "chuyên gia đo trắc quang"),
    ("076330", "photometrist", "noun", "/foʊˈtɒmɪtrɪst/", "chuyên gia đo trắc quang"),
    ("076331", "photomicrographer", "noun", "/ˌfoʊtoʊmaɪˈkrɒɡrəfər/", "người chụp ảnh qua kính hiển vi"),
    ("076332", "photomicrographic", "adj", "/ˌfoʊtoʊˌmaɪkrəˈɡræfɪk/", "thuộc chụp ảnh qua kính hiển vi"),
    ("076333", "photomicrography", "noun", "/ˌfoʊtoʊmaɪˈkrɒɡrəfi/", "kỹ thuật chụp ảnh kính hiển vi"),
    ("076334", "photomicroscope", "noun", "/ˌfoʊtoʊˈmaɪkrəskoʊp/", "kính hiển vi gắn máy chụp ảnh"),
    ("076335", "photomorphs", "noun", "/ˈfoʊtəmɔːrfs/", "cơ thể biến thái theo ánh sáng"),
    ("076336", "photomosaic", "noun", "/ˌfoʊtoʊmoʊˈzeɪɪk/", "ảnh ghép toàn cảnh từ nhiều ảnh"),
    ("076337", "photomultiplier", "noun", "/ˌfoʊtoʊˈmʌltɪˌplaɪər/", "ống nhân quang điện (vật lý)"),
    ("076338", "photonastic", "adj", "/ˌfoʊtoʊˈnæstɪk/", "thuộc ứng động ánh sáng (thực vật)"),
    ("076339", "photonegative", "adj", "/ˌfoʊtoʊˈnɛɡətɪv/", "tránh ánh sáng; mang tính quang âm"),
    ("076340", "photoneutron", "noun", "/ˌfoʊtoʊˈnuːtrɒn/", "nơtron sinh ra do quang hạt nhân"),
    ("076341", "photonic", "adj", "/foʊˈtɒnɪk/", "thuộc photon, quang tử học"),
    ("076342", "photonuclear", "adj", "/ˌfoʊtoʊˈnuːkliər/", "thuộc phản ứng quang hạt nhân"),
    ("076343", "photoperiod", "noun", "/ˌfoʊtoʊˈpɪriəd/", "quang chu kỳ (độ dài ngày đêm)"),
    ("076344", "photophase", "noun", "/ˈfoʊtəfeɪz/", "pha sáng (quá trình quang hợp)"),
    ("076345", "photophilic", "adj", "/ˌfoʊtəˈfɪlɪk/", "ưa ánh sáng (sinh vật)"),
    ("076346", "photophobic", "adj", "/ˌfoʊtəˈfoʊbɪk/", "sợ ánh sáng, tránh ánh sáng"),
    ("076347", "photophone", "noun", "/ˈfoʊtəfoʊn/", "máy truyền âm bằng tia sáng"),
    ("076348", "photophore", "noun", "/ˈfoʊtəfɔːr/", "cơ quan phát sáng (ở cá, mực)"),
    ("076349", "photophoresis", "noun", "/ˌfoʊtoʊfəˈriːsɪs/", "hiện tượng quang chuyển hạt"),
    ("076350", "photopia", "noun", "/foʊˈtoʊpiə/", "thị giác ban ngày (vùng sáng rõ)"),
    ("076351", "photopigment", "noun", "/ˌfoʊtoʊˈpɪɡmənt/", "sắc tố cảm quang (trong võng mạc)"),
    ("076352", "photoplay", "noun", "/ˈfoʊtoʊˌpleɪ/", "phim điện ảnh; kịch bản phim câm"),
    ("076353", "photopositive", "adj", "/ˌfoʊtoʊˈpɒzɪtɪv/", "hướng về phía ánh sáng; quang dương"),
    ("076354", "photoprint", "noun", "/ˈfoʊtoʊˌprɪnt/", "bản in ảnh; bản sao rọi xanh"),
    ("076355", "photoproduct", "noun", "/ˌfoʊtoʊˈprɒdʌkt/", "sản phẩm của phản ứng quang hóa"),
    ("076356", "photoproducts", "noun", "/ˌfoʊtoʊˈprɒdʌkts/", "sản phẩm của phản ứng quang hóa"),
    ("076357", "photoreaction", "noun", "/ˌfoʊtoʊriˈækʃən/", "phản ứng quang hóa"),
    ("076358", "photoreactivation", "noun", "/ˌfoʊtoʊriˌæktɪˈveɪʃən/", "sự phục hồi DNA nhờ ánh sáng"),
    ("076359", "photoreception", "noun", "/ˌfoʊtoʊrɪˈsɛpʃən/", "sự cảm nhận ánh sáng (thị giác)"),
    ("076360", "photoreceptor", "noun", "/ˌfoʊtoʊrɪˈsɛptər/", "tế bào thụ cảm ánh sáng"),
    ("076361", "photoreconnaissance", "noun", "/ˌfoʊtoʊrɪˈkɒnəsəns/", "trinh sát bằng chụp ảnh hàng không"),
    ("076362", "photoreduction", "noun", "/ˌfoʊtoʊrɪˈdʌkʃən/", "sự quang khử (hóa học)"),
    ("076363", "photoresistance", "noun", "/ˌfoʊtoʊrɪˈzɪstəns/", "tính quang trở; điện trở quang"),
    ("076364", "photoresistor", "noun", "/ˌfoʊtoʊrɪˈzɪstər/", "linh kiện quang trở (LDR)"),
    ("076365", "photorespiration", "noun", "/ˌfoʊtoʊˌrɛspəˈreɪʃən/", "hô hấp sáng (sinh lý thực vật)"),
    ("076366", "photoretinitis", "noun", "/ˌfoʊtoʊˌrɛtɪˈnaɪtɪs/", "viêm võng mạc do ánh nắng chói"),
    ("076367", "photos", "verb", "/ˈfoʊtoʊz/", "chụp ảnh, chụp hình"),
    ("076368", "photosensitise", "verb", "/ˌfoʊtoʊˈsɛnsɪtaɪz/", "gây mẫn cảm ánh sáng; nhạy sáng"),
    ("076369", "photosensitivities", "noun", "/ˌfoʊtoʊˌsɛnsɪˈtɪvɪtiz/", "độ nhạy sáng; sự dị ứng ánh sáng"),
    ("076370", "photosensitize", "verb", "/ˌfoʊtoʊˈsɛnsɪtaɪz/", "gây mẫn cảm ánh sáng; nhạy sáng"),
    ("076371", "photoshops", "verb", "/ˈfoʊtoʊˌʃɑːps/", "chỉnh sửa ảnh bằng Photoshop"),
    ("076372", "photospheres", "noun", "/ˈfoʊtəsfɪrz/", "quang cầu (lớp khí quyển Mặt Trời)"),
    ("076373", "photospheric", "adj", "/ˌfoʊtəˈsfɪrɪk/", "thuộc quang cầu Mặt Trời"),
    ("076374", "photostage", "noun", "/ˈfoʊtoʊsteɪdʒ/", "giai đoạn cần ánh sáng (thực vật)"),
    ("076375", "photosurface", "noun", "/ˌfoʊtoʊˈsɜːrfɪs/", "bề mặt nhạy sáng, quang điện"),
    ("076376", "photosynthesise", "verb", "/ˌfoʊtoʊˈsɪnθəsaɪz/", "quang hợp (thực vật)"),
    ("076377", "photosynthesize", "verb", "/ˌfoʊtoʊˈsɪnθəsaɪz/", "quang hợp (thực vật)"),
    ("076378", "photosynthesized", "verb", "/ˌfoʊtoʊˈsɪnθəsaɪzd/", "đã quang hợp (thực vật)"),
    ("076379", "photosynthesizes", "verb", "/ˌfoʊtoʊˈsɪnθəsaɪzɪz/", "quang hợp (thực vật)"),
    ("076380", "photosynthesizing", "verb", "/ˌfoʊtoʊˈsɪnθəsaɪzɪŋ/", "quang hợp (thực vật)"),
    ("076381", "photosynthetically", "adv", "/ˌfoʊtoʊsɪnˈθɛtɪkli/", "bằng quá trình quang hợp"),
    ("076382", "phototactic", "adj", "/ˌfoʊtəˈtæktɪk/", "có tính hướng sáng (di chuyển)"),
    ("076383", "phototaxis", "noun", "/ˌfoʊtoʊˈtæksɪs/", "tính hướng sáng (di chuyển)"),
    ("076384", "phototelegraphy", "noun", "/ˌfoʊtoʊtɪˈlɛɡrəfi/", "kỹ thuật truyền ảnh điện báo từ xa"),
    ("076385", "phototherapeutic", "adj", "/ˌfoʊtoʊˌθɛrəˈpjuːtɪk/", "thuộc liệu pháp ánh sáng (y học)"),
    ("076386", "phototonus", "noun", "/ˌfoʊtəˈtoʊnəs/", "trạng thái nhạy cảm ánh sáng (cây)"),
    ("076387", "phototopography", "noun", "/ˌfoʊtoʊtəˈpɒɡrəfi/", "phép trắc địa bằng không ảnh"),
    ("076388", "phototrophic", "adj", "/ˌfoʊtəˈtrɒfɪk/", "quang dưỡng (dùng năng lượng sáng)"),
    ("076389", "phototrophy", "noun", "/foʊˈtɒtrəfi/", "sự quang dưỡng (sinh vật học)"),
    ("076390", "phototube", "noun", "/ˈfoʊtoʊtuːb/", "ống đèn quang điện chân không"),
    ("076391", "phototype", "noun", "/ˈfoʊtətaɪp/", "bản kẽm in ảnh; bản in chụp"),
    ("076392", "photovaristor", "noun", "/ˌfoʊtoʊvəˈrɪstər/", "linh kiện varistor quang điện"),
    ("076393", "photovision", "noun", "/ˈfoʊtoʊˌvɪʒən/", "truyền hình (cách gọi cũ)"),
    ("076394", "photozincography", "noun", "/ˌfoʊtoʊzɪŋˈkɒɡrəfi/", "kỹ thuật in bản kẽm quang hóa"),
    ("076395", "phoxinus", "noun", "/ˈfɒksɪnəs/", "chi cá tuế suối Âu-Á (Phoxinus)"),
    ("076396", "phragma", "noun", "/ˈfræɡmə/", "vách ngăn, màng ngăn (sinh học)"),
    ("076397", "phragmacone", "noun", "/ˈfræɡməkoʊn/", "vỏ ngăn hình nón mực hóa thạch"),
    ("076398", "phragmipedium", "noun", "/ˌfræɡmɪˈpiːdiəm/", "chi lan hài Nam Mỹ Phragmipedium"),
    ("076399", "phragmocone", "noun", "/ˈfræɡməkoʊn/", "vỏ ngăn hình nón mực hóa thạch"),
    ("076400", "phragmoplast", "noun", "/ˈfræɡmoʊplæst/", "thể vách ngăn (phân bào thực vật)"),
    ("076401", "phragmosome", "noun", "/ˈfræɡmoʊsoʊm/", "thể đĩa vách (phân bào thực vật)"),
    ("076402", "phrasally", "adv", "/ˈfreɪzəli/", "theo lối thành ngữ, cụm từ"),
]

with open("scratch/b36_r03_raw_p4.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

assert len(raw) == len(rows) == 100
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, rows):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} vs {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} vs {hw}"
    assert len(vi) <= 35, f"vi too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.count("/") == 2 and not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"bad ipa: {hw} -> {ipa}"
    r["pos"] = pos
    r["ipa"] = ipa
    r["vi"] = vi
    r["status"] = "reviewed"
    out.append(r)

with open("scratch/b36_r03_p4.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r03_p4 saved OK")
