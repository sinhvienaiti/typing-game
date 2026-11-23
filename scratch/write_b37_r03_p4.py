import json

records = [
    ("081303", "radiative", "adj", "/ˈreɪdiˌeɪtɪv/", "thuộc bức xạ, phát xạ nhiệt sáng"),
    ("081304", "radiators", "noun", "/ˈreɪdiˌeɪtərz/", "lò sưởi tản nhiệt; két nước làm mát"),
    ("081305", "radicalise", "verb", "/ˈrædɪkəˌlaɪz/", "cấp tiến hóa, cực đoan hóa (Anh)"),
    ("081306", "radicalised", "verb", "/ˈrædɪkəˌlaɪzd/", "đã cấp tiến hóa, cực đoan hóa (Anh)"),
    ("081307", "radicalises", "verb", "/ˈrædɪkəˌlaɪzɪz/", "cấp tiến hóa, cực đoan hóa (Anh)"),
    ("081308", "radicalising", "verb", "/ˈrædɪkəˌlaɪzɪŋ/", "cấp tiến hóa, cực đoan hóa (Anh)"),
    ("081309", "radicalized", "verb", "/ˈrædɪkəˌlaɪzd/", "đã cấp tiến hóa, đã cực đoan hóa"),
    ("081310", "radicalizes", "verb", "/ˈrædɪkəˌlaɪzɪz/", "cấp tiến hóa, đẩy tới cực đoan"),
    ("081311", "radicalizing", "verb", "/ˈrædɪkəˌlaɪzɪŋ/", "cấp tiến hóa, đẩy tới cực đoan"),
    ("081312", "radicallsm", "noun", "/ˈrædɪkəˌlɪzəm/", "chủ nghĩa cấp tiến (biến thể lỗi)"),
    ("081313", "radicand", "noun", "/ˈrædɪˌkænd/", "biểu thức dưới dấu căn (toán học)"),
    ("081314", "radicate", "verb", "/ˈrædɪˌkeɪt/", "bén rễ, mọc rễ sâu (thực vật học)"),
    ("081315", "radicel", "noun", "/ˈrædəˌsɛl/", "rễ con, nhánh rễ nhỏ (thực vật)"),
    ("081316", "radices", "noun", "/ˈrædɪˌsiːz/", "các rễ cây; cơ số; căn nguyên gốc"),
    ("081317", "radichio", "noun", "/rəˈdiːkioʊ/", "rau diếp xoăn tím Ý (radicchio)"),
    ("081318", "radicicolous", "adj", "/ˌrædɪˈsɪkələs/", "ký sinh ở rễ cây (nấm, côn trùng)"),
    ("081319", "radiciflorous", "adj", "/ˌrædɪsəˈflɔːrəs/", "ra hoa trực tiếp từ phần rễ cây"),
    ("081320", "radiciform", "adj", "/ˈrædɪsəˌfɔːrm/", "có hình dạng giống rễ cây"),
    ("081321", "radicular", "adj", "/rəˈdɪkjələr/", "thuộc chân răng; thuộc rễ thần kinh"),
    ("081322", "radicule", "noun", "/ˈrædɪˌkjuːl/", "rễ mầm, rễ con (biến thể)"),
    ("081323", "radiculitis", "noun", "/rəˌdɪkjəˈlaɪtɪs/", "chứng viêm rễ thần kinh (y học)"),
    ("081324", "radii", "noun", "/ˈreɪdiˌaɪ/", "các bán kính; các xương cẳng tay"),
    ("081325", "radiigera", "noun", "/ˌreɪdiˈɪdʒərə/", "chi nấm quả bóng sao (Radiigera)"),
    ("081326", "radioactivate", "verb", "/ˌreɪdioʊˈæktəˌveɪt/", "kích hoạt tính phóng xạ (vật lý)"),
    ("081327", "radioactivation", "noun", "/ˌreɪdioʊˌæktəˈveɪʃən/", "sự kích hoạt tính phóng xạ"),
    ("081328", "radioastronomy", "noun", "/ˌreɪdioʊəˈstrɑːnəmi/", "ngành thiên văn học vô tuyến"),
    ("081329", "radiobiologist", "noun", "/ˌreɪdioʊbaɪˈɑːlədʒɪst/", "nhà sinh học phóng xạ"),
    ("081330", "radiobox", "noun", "/ˈreɪdioʊˌbɑːks/", "nút chọn tròn giao diện (tin học)"),
    ("081331", "radiobroadcast", "verb", "/ˌreɪdioʊˈbrɔːdkæst/", "phát thanh qua sóng vô tuyến"),
    ("081332", "radiobroadcasting", "noun", "/ˌreɪdioʊˈbrɔːdkæstɪŋ/", "ngành phát thanh truyền thanh"),
    ("081333", "radiocast", "verb", "/ˈreɪdioʊˌkæst/", "phát thanh qua sóng vô tuyến"),
    ("081334", "radiochemist", "noun", "/ˌreɪdioʊˈkɛmɪst/", "nhà hóa học phóng xạ"),
    ("081335", "radiochlorine", "noun", "/ˌreɪdioʊˈklɔːriːn/", "đồng vị clo phóng xạ (hóa học)"),
    ("081336", "radiogenic", "adj", "/ˌreɪdioʊˈdʒɛnɪk/", "sinh ra từ phân rã phóng xạ"),
    ("081337", "radiogenimetry", "noun", "/ˌreɪdioʊdʒəˈnɪmətri/", "kỹ thuật tìm phương bằng vô tuyến"),
    ("081338", "radiogeniometer", "noun", "/ˌreɪdioʊˌdʒiːniˈɑːmɪtər/", "máy đo phương vị sóng vô tuyến"),
    ("081339", "radiographers", "noun", "/ˌreɪdiˈɑːɡrəfərz/", "các kỹ thuật viên chụp X-quang"),
    ("081340", "radioguidance", "noun", "/ˌreɪdioʊˈɡaɪdəns/", "sự dẫn đường bằng sóng vô tuyến"),
    ("081341", "radiohazard", "noun", "/ˌreɪdioʊˈhæzərd/", "mối nguy hiểm nhiễm bức xạ phóng xạ"),
    ("081342", "radiohouse", "noun", "/ˈreɪdioʊˌhaʊs/", "trạm thu phát vô tuyến, nhà đài"),
    ("081343", "radiolocate", "verb", "/ˌreɪdioʊˈloʊkeɪt/", "định vị mục tiêu bằng sóng radar"),
    ("081344", "radiolocated", "verb", "/ˌreɪdioʊˈloʊkeɪtɪd/", "đã định vị mục tiêu bằng radar"),
    ("081345", "radiolocator", "noun", "/ˌreɪdioʊˈloʊkeɪtər/", "máy radar định vị vô tuyến"),
    ("081346", "radiologists", "noun", "/ˌreɪdiˈɑːlədʒɪsts/", "các bác sĩ chẩn đoán hình ảnh"),
    ("081347", "radiolucency", "noun", "/ˌreɪdioʊˈluːsənsi/", "tính chất thấu tia X trên phim chụp"),
    ("081348", "radiolytic", "adj", "/ˌreɪdioʊˈlɪtɪk/", "thuộc sự phân ly bằng bức xạ"),
    ("081349", "radioman", "noun", "/ˈreɪdioʊˌmæn/", "nhân viên điện đài vô tuyến quân sự"),
    ("081350", "radiomaterial", "noun", "/ˌreɪdioʊməˈtɪriəl/", "vật liệu phát ra bức xạ phóng xạ"),
    ("081351", "radiometallography", "noun", "/ˌreɪdioʊˌmɛtəˈlɑːɡrəfi/", "kỹ thuật soi kim loại bằng tia X"),
    ("081352", "radiometallurgy", "noun", "/ˌreɪdioʊˈmɛtəˌlɜːrdʒi/", "ngành luyện kim xử lý chất phóng xạ"),
    ("081353", "radiometers", "noun", "/ˌreɪdiˈɑːmɪtərz/", "những máy đo cường độ bức xạ"),
    ("081354", "radiometric", "adj", "/ˌreɪdioʊˈmɛtrɪk/", "thuộc phép đo bức xạ, đồng vị"),
    ("081355", "radiometry", "noun", "/ˌreɪdiˈɑːmətri/", "phép đo bức xạ điện từ và phóng xạ"),
    ("081356", "radiomicrometer", "noun", "/ˌreɪdioʊmaɪˈkrɑːmɪtər/", "vi nhiệt kế đo bức xạ hồng ngoại"),
    ("081357", "radiomimetic", "adj", "/ˌreɪdioʊmɪˈmɛtɪk/", "gây tác dụng giống chiếu phóng xạ"),
    ("081358", "radionavigation", "noun", "/ˌreɪdioʊˌnævəˈɡeɪʃən/", "hệ thống dẫn đường bằng vô tuyến"),
    ("081359", "radionuclide", "noun", "/ˌreɪdioʊˈnuːklaɪd/", "đồng vị phóng xạ (vật lý hạt nhân)"),
    ("081360", "radiopacity", "noun", "/ˌreɪdioʊˈpæsəti/", "độ cản tia X (chẩn đoán hình ảnh)"),
    ("081361", "radiophare", "noun", "/ˈreɪdioʊˌfɛr/", "đèn hiệu vô tuyến hàng hải"),
    ("081362", "radiophony", "noun", "/ˌreɪdiˈɑːfəni/", "kỹ thuật truyền âm bằng bức xạ"),
    ("081363", "radiophosphorus", "noun", "/ˌreɪdioʊˈfɑːsfərəs/", "đồng vị phốt pho phóng xạ"),
    ("081364", "radiophoto", "noun", "/ˈreɪdioʊˌfoʊtoʊ/", "ảnh truyền qua sóng vô tuyến điện"),
    ("081365", "radiophotograph", "noun", "/ˌreɪdioʊˈfoʊtəˌɡræf/", "bức ảnh truyền bằng sóng vô tuyến"),
    ("081366", "radiophotography", "noun", "/ˌreɪdioʊfəˈtɑːɡrəfi/", "kỹ thuật truyền ảnh bằng vô tuyến"),
    ("081367", "radiophotoluminescence", "noun", "/ˌreɪdioʊˌfoʊtoʊluːməˈnɛsəns/", "hiện tượng phát quang sau chiếu xạ"),
    ("081368", "radiophototelegraphy", "noun", "/ˌreɪdioʊˌfoʊtoʊtəˈlɛɡrəfi/", "phép điện báo truyền ảnh vô tuyến"),
    ("081369", "radiophysics", "noun", "/ˌreɪdioʊˈfɪzɪks/", "vật lý vô tuyến và sóng điện từ"),
    ("081370", "radioprospecting", "noun", "/ˌreɪdioʊˈprɑːspɛktɪŋ/", "thăm dò khoáng sản bằng đo phóng xạ"),
    ("081371", "radioprotective", "adj", "/ˌreɪdioʊprəˈtɛktɪv/", "bảo vệ tế bào chống tác hại bức xạ"),
    ("081372", "radiopurity", "noun", "/ˌreɪdioʊˈpjʊrəti/", "độ tinh khiết phóng xạ (hóa học)"),
    ("081373", "radioreceiver", "noun", "/ˌreɪdioʊrɪˈsiːvər/", "máy thu thanh vô tuyến, máy radio"),
    ("081374", "radioresistant", "adj", "/ˌreɪdioʊrɪˈzɪstənt/", "có sức kháng chịu tia bức xạ cao"),
    ("081375", "radioscope", "noun", "/ˈreɪdiəˌskoʊp/", "máy soi huỳnh quang tia X, máy dò"),
    ("081376", "radioscopic", "adj", "/ˌreɪdiəˈskɑːpɪk/", "thuộc phép soi chiếu bằng tia X"),
    ("081377", "radioscopy", "noun", "/ˌreɪdiˈɑːskəpi/", "phép soi huỳnh quang tia X (y học)"),
    ("081378", "radiosight", "noun", "/ˈreɪdioʊˌsaɪt/", "kính ngắm định vị vô tuyến"),
    ("081379", "radiosignal", "noun", "/ˈreɪdioʊˌsɪɡnəl/", "tín hiệu sóng vô tuyến, radio"),
    ("081380", "radiosonde", "noun", "/ˈreɪdioʊˌsɑːnd/", "bóng thám không phát sóng radio"),
    ("081381", "radiosource", "noun", "/ˈreɪdioʊˌsɔːrs/", "nguồn phát sóng vô tuyến vũ trụ"),
    ("081382", "radiospectroscopy", "noun", "/ˌreɪdioʊspɛkˈtrɑːskəpi/", "phổ học sóng vô tuyến (vật lý)"),
    ("081383", "radiosusceptibility", "noun", "/ˌreɪdioʊsəˌsɛptəˈbɪləti/", "tính nhạy cảm với tia bức xạ"),
    ("081384", "radiosymmetrical", "adj", "/ˌreɪdioʊsɪˈmɛtrɪkəl/", "đối xứng tỏa tròn theo bán kính"),
    ("081385", "radiotechnics", "noun", "/ˌreɪdioʊˈtɛknɪks/", "kỹ thuật vô tuyến điện"),
    ("081386", "radiotelegram", "noun", "/ˌreɪdioʊˈtɛləˌɡræm/", "bức điện tín truyền qua vô tuyến"),
    ("081387", "radiotelephonic", "adj", "/ˌreɪdioʊˌtɛləˈfɑːnɪk/", "thuộc điện thoại vô tuyến"),
    ("081388", "radiotherapeutics", "noun", "/ˌreɪdioʊˌθɛrəˈpjuːtɪks/", "liệu pháp xạ trị điều trị ung thư"),
    ("081389", "radiotherapist", "noun", "/ˌreɪdioʊˈθɛrəpɪst/", "bác sĩ chuyên khoa xạ trị"),
    ("081390", "radiotherapists", "noun", "/ˌreɪdioʊˈθɛrəpɪsts/", "các bác sĩ chuyên khoa xạ trị"),
    ("081391", "radiothermics", "noun", "/ˌreɪdioʊˈθɜːrmɪks/", "kỹ thuật gia nhiệt sóng cao tần"),
    ("081392", "radiothorium", "noun", "/ˌreɪdioʊˈθɔːriəm/", "đồng vị phóng xạ thori-228"),
    ("081393", "radiotolerance", "noun", "/ˌreɪdioʊˈtɑːlərəns/", "khả năng dung nạp liều bức xạ"),
    ("081394", "radiotoxity", "noun", "/ˌreɪdioʊtɑːkˈsɪsəti/", "độc tính phóng xạ (biến thể)"),
    ("081395", "radiotracer", "noun", "/ˌreɪdioʊˈtreɪsər/", "chất đồng vị phóng xạ đánh dấu (y)"),
    ("081396", "radiotrician", "noun", "/ˌreɪdioʊˈtrɪʃən/", "kỹ thuật viên sửa máy vô tuyến"),
    ("081397", "radiotron", "noun", "/ˈreɪdiəˌtrɑːn/", "đèn điện tử chân không Radiotron"),
    ("081398", "radioulna", "noun", "/ˌreɪdioʊˈʌlnə/", "xương quay trụ hợp nhất (ếch, nhái)"),
    ("081399", "radioulnar", "adj", "/ˌreɪdioʊˈʌlnər/", "thuộc khớp xương quay và xương trụ"),
    ("081400", "radula", "noun", "/ˈrædʒələ/", "dải răng kitin nạo ăn (ốc)"),
    ("081401", "radyera", "noun", "/rəˈdjɪrə/", "chi cây bụi dâm bụt Úc Radyera"),
    ("081402", "raectance", "noun", "/riˈæktəns/", "điện kháng (biến thể sai chính tả)"),
]

raw = json.load(open("scratch/b37_r03_raw_p4.json"))
by_id = {f"lex.en.200k.{r[0]}": r for r in records}
out = []
for orig in raw:
    sid, hw, pos, ipa, vi = by_id[orig["id"]]
    assert orig["hw"] == hw, f"{orig['id']}: {orig['hw']} vs {hw}"
    assert 0 < len(vi) <= 35, f"{sid} {hw} len={len(vi)}: {vi}"
    assert "/" not in vi, f"{sid} {hw} slash in vi"
    assert ipa.count("/") == 2 and not ipa.startswith("/ ") and not ipa.endswith(" /"), f"{sid} {hw} bad ipa"
    orig["pos"] = pos
    orig["ipa"] = ipa
    orig["vi"] = vi
    orig["status"] = "reviewed"
    out.append(orig)

assert len(out) == 100
with open("scratch/b37_r03_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r03_p4 saved OK")
