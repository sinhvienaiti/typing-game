import json

rows = [
    ("077903", "polyphonously", "adv", "/pəˈlɪfənəsli/", "theo lối đa âm, phức điệu"),
    ("077904", "polyphyletic", "adj", "/ˌpɒlɪfaɪˈlɛtɪk/", "đa nguồn gốc (nhiều dòng tổ tiên)"),
    ("077905", "polyphyllous", "adj", "/ˌpɒlɪˈfɪləs/", "có nhiều lá đài hoặc nhiều lá"),
    ("077906", "polypi", "noun", "/ˈpɒlɪpaɪ/", "u lành polyp; cá thể thủy tức"),
    ("077907", "polypidom", "noun", "/pəˈlɪpɪdəm/", "bộ khung tập đoàn thủy tức, san hô"),
    ("077908", "polypite", "noun", "/ˈpɒlɪpaɪt/", "cá thể polyp trong tập đoàn san hô"),
    ("077909", "polyplacophora", "noun", "/ˌpɒlɪpləˈkɒfərə/", "lớp Song kinh (động vật thân mềm)"),
    ("077910", "polyplacophore", "noun", "/ˌpɒlɪˈplækəfɔːr/", "động vật thân mềm song kinh"),
    ("077911", "polyplanetic", "adj", "/ˌpɒlɪpləˈnɛtɪk/", "có nhiều giai đoạn bơi (bào tử)"),
    ("077912", "polyplast", "noun", "/ˈpɒlɪplæst/", "chất đa phân tử; tế bào đa dạng"),
    ("077913", "polyplastic", "adj", "/ˌpɒlɪˈplæstɪk/", "biến đổi nhiều dạng (sinh học)"),
    ("077914", "polyplicate", "adj", "/ˌpɒlɪˈplɪkɪt/", "có nhiều nếp gấp dọc"),
    ("077915", "polyploidigen", "noun", "/ˌpɒlɪˈplɔɪdɪdʒən/", "tác nhân gây đột biến đa bội"),
    ("077916", "polyploidization", "noun", "/ˌpɒlɪplɔɪdaɪˈzeɪʃən/", "quá trình đa bội hóa bộ NST"),
    ("077917", "polypnea", "noun", "/ˌpɒlɪpˈniːə/", "chứng thở nhanh và sâu (y học)"),
    ("077918", "polypod", "adj", "/ˈpɒlɪpɒd/", "có nhiều chân (chân khớp)"),
    ("077919", "polypodia", "noun", "/ˌpɒlɪˈpoʊdiə/", "dị tật thừa nhiều chân"),
    ("077920", "polypodiaceae", "noun", "/ˌpɒlɪpoʊdiˈeɪsiː/", "họ Dương xỉ (Polypodiaceae)"),
    ("077921", "polypodiales", "noun", "/ˌpɒlɪpoʊdiˈeɪliːz/", "bộ Dương xỉ (Polypodiales)"),
    ("077922", "polypody", "noun", "/ˈpɒlɪpədi/", "cây dương xỉ (chi Polypodium)"),
    ("077923", "polypoid", "adj", "/ˈpɒlɪpɔɪd/", "có dạng như khối polyp (y học)"),
    ("077924", "polyporaceae", "noun", "/ˌpɒlɪpəˈreɪsiː/", "họ Nấm lỗ (Polyporaceae)"),
    ("077925", "polypous", "adj", "/ˈpɒlɪpəs/", "thuộc hoặc có nhiều polyp (y học)"),
    ("077926", "polyprion", "noun", "/ˌpɒlɪˈpraɪɒn/", "chi cá mú đá biển sâu Polyprion"),
    ("077927", "polypropene", "noun", "/ˌpɒlɪˈproʊpiːn/", "nhựa polypropylen (nhựa PP)"),
    ("077928", "polypropenonitrile", "noun", "/ˌpɒlɪˌproʊpɪnoʊˈnaɪtrɪl/", "nhựa sợi tổng hợp polyacrylonitril"),
    ("077929", "polyptoton", "noun", "/pɒˈlɪptətɒn/", "phép lặp từ khác biến cách (tu từ)"),
    ("077930", "polypus", "noun", "/ˈpɒlɪpəs/", "u lành polyp niêm mạc (y học)"),
    ("077931", "polyrhizal", "adj", "/ˌpɒlɪˈraɪzəl/", "có nhiều rễ chùm (thực vật)"),
    ("077932", "polysaprobit", "adj", "/ˌpɒlɪˈsæprəbɪt/", "sinh vật sống ở nước rất ô nhiễm"),
    ("077933", "polysemant", "noun", "/ˈpɒlɪsɪˌmænt/", "từ đa nghĩa (ngôn ngữ học)"),
    ("077934", "polysemantic", "adj", "/ˌpɒlɪsɪˈmæntɪk/", "đa nghĩa, có nhiều nghĩa"),
    ("077935", "polysensivity", "noun", "/ˌpɒlɪsɛnˈsɪvɪti/", "tính nhạy cảm với nhiều kích thích"),
    ("077936", "polysepalous", "adj", "/ˌpɒlɪˈsɛpələs/", "có nhiều lá đài rời (hoa)"),
    ("077937", "polysiphonic", "adj", "/ˌpɒlɪsaɪˈfɒnɪk/", "có nhiều ống xifon dẫn (tảo đỏ)"),
    ("077938", "polysomaty", "noun", "/ˌpɒlɪˈsoʊməti/", "hiện tượng đa bội thân (tế bào)"),
    ("077939", "polysomic", "adj", "/ˌpɒlɪˈsoʊmɪk/", "đa nhiễm sắc thể (thừa NST)"),
    ("077940", "polysomy", "noun", "/ˈpɒlɪˌsoʊmi/", "tình trạng thừa nhiễm sắc thể"),
    ("077941", "polyspast", "noun", "/ˈpɒlɪspæst/", "hệ thống ròng rọc pa-lăng"),
    ("077942", "polyspermous", "adj", "/ˌpɒlɪˈspɜːrməs/", "nhiều hạt; đa tinh trùng thụ tinh"),
    ("077943", "polysporous", "adj", "/pɒˈlɪspərəs/", "tạo nhiều bào tử (nấm, vi sinh)"),
    ("077944", "polystelic", "adj", "/ˌpɒlɪˈstɛlɪk/", "có nhiều trung trụ dẫn (thực vật)"),
    ("077945", "polystome", "adj", "/ˈpɒlɪstoʊm/", "có nhiều giác bám (sán polystome)"),
    ("077946", "polysyllabically", "adv", "/ˌpɒlɪsɪˈlæbɪkli/", "bằng từ nhiều âm tiết"),
    ("077947", "polysyllable", "noun", "/ˈpɒlɪˌsɪləbəl/", "từ đa âm tiết (từ nhiều âm tiết)"),
    ("077948", "polysyllogisme", "noun", "/ˌpɒlɪˈsɪlədʒɪzəm/", "tam đoạn luận kép (logic học)"),
    ("077949", "polysymmetrical", "adj", "/ˌpɒlɪsɪˈmɛtrɪkəl/", "đối xứng theo nhiều mặt phẳng"),
    ("077950", "polysynaptic", "adj", "/ˌpɒlɪsɪˈnæptɪk/", "qua nhiều xináp thần kinh"),
    ("077951", "polysyndetic", "adj", "/ˌpɒlɪsɪnˈdɛtɪk/", "dùng phép lặp liên từ (tu từ)"),
    ("077952", "polysyndeton", "noun", "/ˌpɒlɪˈsɪndɪtɒn/", "phép lặp liên từ (tu từ học)"),
    ("077953", "polytarp", "noun", "/ˈpɒlɪtɑːrp/", "bạt nhựa polyetylen chống thấm"),
    ("077954", "polytarps", "noun", "/ˈpɒlɪtɑːrps/", "bạt nhựa polyetylen chống thấm"),
    ("077955", "polytene", "noun", "/ˈpɒlɪtiːn/", "nhiễm sắc thể khổng lồ đa sợi"),
    ("077956", "polythelia", "noun", "/ˌpɒlɪˈθiːliə/", "dị tật có nhiều núm vú (y học)"),
    ("077957", "polythen", "noun", "/ˈpɒlɪθiːn/", "nhựa polyetylen (PE)"),
    ("077958", "polytocous", "adj", "/pəˈlɪtəkəs/", "đẻ nhiều con hoặc nhiều trứng"),
    ("077959", "polytonal", "adj", "/ˌpɒlɪˈtoʊnəl/", "đa điệu tính (âm nhạc hiện đại)"),
    ("077960", "polytonalism", "noun", "/ˌpɒlɪˈtoʊnəlɪzəm/", "lối sáng tác đa điệu tính (nhạc)"),
    ("077961", "polytonality", "noun", "/ˌpɒlɪtoʊˈnælɪti/", "tính đa điệu (âm nhạc hiện đại)"),
    ("077962", "polytope", "noun", "/ˈpɒlɪtoʊp/", "đa diện nhiều chiều (pôlitôp)"),
    ("077963", "polytopic", "adj", "/ˌpɒlɪˈtɒpɪk/", "phân bố rộng ở nhiều vùng"),
    ("077964", "polytrichia", "noun", "/ˌpɒlɪˈtrɪkiə/", "chứng mọc rậm lông bất thường"),
    ("077965", "polytrichous", "adj", "/pəˈlɪtrɪkəs/", "rậm lông; nhiều tiên mao"),
    ("077966", "polytrophia", "noun", "/ˌpɒlɪˈtroʊfiə/", "tình trạng thừa dinh dưỡng (y học)"),
    ("077967", "polytrophic", "adj", "/ˌpɒlɪˈtrɒfɪk/", "ăn nhiều nguồn thức ăn khác nhau"),
    ("077968", "polytropic", "adj", "/ˌpɑːlɪˈtrɒpɪk/", "đa hướng; thụ phấn nhiều loài hoa"),
    ("077969", "polytype", "noun", "/ˈpɒlɪtaɪp/", "đa hình thái tinh thể (polytype)"),
    ("077970", "polytypic", "adj", "/ˌpɒlɪˈtɪpɪk/", "đa kiểu (gồm nhiều phân loài)"),
    ("077971", "polyurethan", "noun", "/ˌpɒlɪˈjʊərəθeɪn/", "nhựa polyuretan (PU)"),
    ("077972", "polyuric", "adj", "/ˌpɒlɪˈjʊrɪk/", "thuộc chứng tiểu nhiều (y học)"),
    ("077973", "polyvalence", "noun", "/ˌpɒlɪˈveɪləns/", "đa hóa trị; tính đa năng"),
    ("077974", "polyvalency", "noun", "/ˌpɒlɪˈveɪlənsi/", "đa hóa trị; tính đa năng"),
    ("077975", "polyvoltine", "adj", "/ˌpɒlɪˈvɒltiːn/", "sinh sản nhiều lứa trong một năm"),
    ("077976", "polyzoa", "noun", "/ˌpɒlɪˈzoʊə/", "ngành Động vật hình rêu (Bryozoa)"),
    ("077977", "polyzoan", "noun", "/ˌpɒlɪˈzoʊən/", "động vật hình rêu (ngành Bryozoa)"),
    ("077978", "polyzoarium", "noun", "/ˌpɒlɪzoʊˈɛriəm/", "khung tập đoàn động vật hình rêu"),
    ("077979", "polyzoic", "adj", "/ˌpɒlɪˈzoʊɪk/", "thuộc tập đoàn động vật hình rêu"),
    ("077980", "pomacanthus", "noun", "/ˌpoʊməˈkænθəs/", "chi cá tiên biển Pomacanthus"),
    ("077981", "pomace", "noun", "/ˈpʌmɪs/", "bã táo ép (hoặc bã trái cây ép)"),
    ("077982", "pomacentridae", "noun", "/ˌpoʊməˈsɛntrɪdiː/", "họ Cá thia rạn san hô"),
    ("077983", "pomacentrus", "noun", "/ˌpoʊməˈsɛntrəs/", "chi cá thia biển (Pomacentrus)"),
    ("077984", "pomaded", "adj", "/pəˈmeɪdɪd/", "được vuốt sáp thơm (tóc)"),
    ("077985", "pomader", "noun", "/ˈpɒmədər/", "viên hoặc túi nước hoa sáp thơm"),
    ("077986", "pomaderris", "noun", "/ˌpɒməˈdɛrɪs/", "chi cây bụi Pomaderris (Úc)"),
    ("077987", "pomades", "verb", "/pəˈmeɪdz/", "bôi sáp thơm (lên tóc)"),
    ("077988", "pomading", "verb", "/pəˈmeɪdɪŋ/", "bôi sáp thơm (lên tóc)"),
    ("077989", "pomatomidae", "noun", "/ˌpoʊməˈtɒmɪdiː/", "họ Cá trích xanh (Pomatomidae)"),
    ("077990", "pomatomus", "noun", "/poʊˈmætəməs/", "chi cá xanh bluefish (Pomatomus)"),
    ("077991", "pomatum", "noun", "/pəˈmeɪtəm/", "sáp thơm bôi tóc; thuốc mỡ (cổ)"),
    ("077992", "pomiculture", "noun", "/ˈpoʊmɪˌkʌltʃər/", "nghề trồng cây ăn quả"),
    ("077993", "pomiferous", "adj", "/poʊˈmɪfərəs/", "cho quả mọng dạng quả táo"),
    ("077994", "pomiform", "adj", "/ˈpoʊmɪfɔːrm/", "có hình dáng giống quả táo"),
    ("077995", "pommelled", "verb", "/ˈpʌməld/", "đã đấm túi bụi liên tiếp"),
    ("077996", "pommelling", "verb", "/ˈpʌməlɪŋ/", "đấm túi bụi liên tiếp"),
    ("077997", "pommels", "verb", "/ˈpʌməlz/", "đấm túi bụi liên tiếp"),
    ("077998", "pomodoro", "noun", "/ˌpɑːməˈdɔːroʊ/", "cà chua Ý dạng quả mận (pomodoro)"),
    ("077999", "pomodoros", "noun", "/ˌpɑːməˈdɔːroʊz/", "cà chua Ý dạng quả mận (pomodoro)"),
    ("078000", "pomolobus", "noun", "/pəˈmɒləbəs/", "chi cá trích sông Bắc Mỹ"),
    ("078001", "pomological", "adj", "/ˌpɒməˈlɒdʒɪkəl/", "thuộc ngành quả học (cây ăn quả)"),
    ("078002", "pomologically", "adv", "/ˌpɒməˈlɒdʒɪkli/", "về mặt khoa học cây ăn quả"),
]

with open("scratch/b36_r06_raw_p5.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r06_p5.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r06_p5 saved OK")
