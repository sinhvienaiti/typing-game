import json

RECORDS = [
    ("084903", "sarcology", "noun", "/sɑːrˈkɑːlədʒi/", "khoa học về mô mềm cơ thể"),
    ("084904", "sarcolyte", "noun", "/ˈsɑːrkəˌlaɪt/", "tế bào phân mảnh cơ"),
    ("084905", "sarcomata", "noun", "/sɑːrˈkoʊmətə/", "khối u ác tính mô liên kết"),
    ("084906", "sarcomatoid", "adj", "/sɑːrˈkoʊməˌtɔɪd/", "dạng sarcoma; giống u mô liên kết"),
    ("084907", "sarcomatosis", "noun", "/ˌsɑːrkoʊməˈtoʊsɪs/", "bệnh sarcoma lan tỏa"),
    ("084908", "sarcomatous", "adj", "/sɑːrˈkoʊmətəs/", "thuộc khối u sarcoma"),
    ("084909", "sarcophages", "noun", "/sɑːrˈkɑːfədʒɪz/", "quan tài đá chạm khắc cổ"),
    ("084910", "sarcophagi", "noun", "/sɑːrˈkɑːfəˌɡaɪ/", "quan tài đá chạm khắc cổ"),
    ("084911", "sarcophagous", "adj", "/sɑːrˈkɑːfəɡəs/", "ăn thịt"),
    ("084912", "sarcophagy", "noun", "/sɑːrˈkɑːfədʒi/", "tập tính ăn thịt"),
    ("084913", "sarcophilus", "noun", "/sɑːrˈkɑːfɪləs/", "chi thú ăn thịt quỷ Tasmania"),
    ("084914", "sarcoplasm", "noun", "/ˈsɑːrkəˌplæzəm/", "tương cơ; bào tương tế bào cơ"),
    ("084915", "sarcoplast", "noun", "/ˈsɑːrkəˌplæst/", "nguyên bào cơ; hạt tạo cơ"),
    ("084916", "sarcoptid", "noun", "/sɑːrˈkɑːptɪd/", "con cái ghẻ; mạt ký sinh"),
    ("084917", "sarcoptidae", "noun", "/sɑːrˈkɑːptɪˌdiː/", "họ Cái ghẻ (Sarcoptidae)"),
    ("084918", "sarcorhamphus", "noun", "/ˌsɑːrkəˈræmfəs/", "chi Kền kền vua châu Mỹ"),
    ("084919", "sarcoscyphaceae", "noun", "/ˌsɑːrkəˌsaɪˈfeɪsiːˌiː/", "họ Nấm chén đỏ"),
    ("084920", "sarcosoma", "noun", "/ˌsɑːrkəˈsoʊmə/", "chi nấm túi Sarcosoma; phần thịt"),
    ("084921", "sarcosomal", "adj", "/ˌsɑːrkəˈsoʊməl/", "thuộc ty thể tế bào cơ"),
    ("084922", "sarcosomataceae", "noun", "/ˌsɑːrkəˌsoʊməˈteɪsiːˌiː/", "họ nấm túi Sarcosomataceae"),
    ("084923", "sarcosome", "noun", "/ˈsɑːrkəˌsoʊm/", "ty thể tế bào cơ"),
    ("084924", "sarcosomes", "noun", "/ˈsɑːrkəˌsoʊmz/", "ty thể tế bào cơ"),
    ("084925", "sarcosperm", "noun", "/ˈsɑːrkəˌspɜːrm/", "vỏ hạt nạc; phần thịt hạt"),
    ("084926", "sarcosporidia", "noun", "/ˌsɑːrkoʊspəˈrɪdiə/", "bộ Trùng bào tử ký sinh cơ"),
    ("084927", "sarcosporidian", "noun", "/ˌsɑːrkoʊspəˈrɪdiən/", "trùng bào tử ký sinh cơ"),
    ("084928", "sarcostemma", "noun", "/ˌsɑːrkəˈstɛmə/", "chi Dây sữa (Sarcostemma)"),
    ("084929", "sarcostyle", "noun", "/ˈsɑːrkəˌstaɪl/", "tơ cơ; sợi cơ"),
    ("084930", "sarcotesta", "noun", "/ˌsɑːrkəˈtɛstə/", "vỏ hạt nạc (hạt lựu, bạch quả)"),
    ("084931", "sarcous", "adj", "/ˈsɑːrkəs/", "thuộc mô cơ; bằng thịt"),
    ("084932", "sardinops", "noun", "/ˈsɑːrdɪnɑːps/", "chi cá mòi Thái Bình Dương"),
    ("084933", "sardius", "noun", "/ˈsɑːrdiəs/", "đá mã não đỏ sardius"),
    ("084934", "sardonicisms", "noun", "/sɑːrˈdɑːnɪˌsɪzəmz/", "lời nói mỉa mai cay độc"),
    ("084935", "sarge", "noun", "/sɑːrdʒ/", "trung sĩ (cách gọi thân mật)"),
    ("084936", "sarissa", "noun", "/səˈrɪsə/", "ngọn giáo dài quân Macedonia cổ"),
    ("084937", "sarissae", "noun", "/səˈrɪsiː/", "ngọn giáo dài quân Macedonia cổ"),
    ("084938", "sark", "noun", "/sɑːrk/", "áo sơ mi; áo lót (tiếng Scotland)"),
    ("084939", "sarky", "adj", "/ˈsɑːrki/", "châm chọc; mỉa mai chua cay"),
    ("084940", "sarmenta", "noun", "/sɑːrˈmɛntə/", "thân bò; nhánh bò lan"),
    ("084941", "sarmentaceous", "adj", "/ˌsɑːrmənˈteɪʃəs/", "có thân bò; mọc cành vươn dài"),
    ("084942", "sarmentose", "adj", "/ˌsɑːrmənˈtoʊs/", "có nhiều nhánh bò lan"),
    ("084943", "sarmentous", "adj", "/sɑːrˈmɛntəs/", "có nhiều nhánh bò lan"),
    ("084944", "sarmentum", "noun", "/sɑːrˈmɛntəm/", "thân bò; cành bò dài (thực vật)"),
    ("084945", "sarnie", "noun", "/ˈsɑːrni/", "bánh mì kẹp sandwich (lóng Anh)"),
    ("084946", "sarongs", "noun", "/səˈrɔːŋz/", "váy quấn xà rông"),
    ("084947", "sarpanitu", "noun", "/sɑːrpəˈniːtuː/", "nữ thần Sarpanitu (Babylon)"),
    ("084948", "sarraceniaceae", "noun", "/ˌsærəsɪniˈeɪsiːˌiː/", "họ Cây bình bắt mồi Bắc Mỹ"),
    ("084949", "sarraceniales", "noun", "/ˌsærəsɪniˈeɪliːz/", "bộ Cây nắp ấm cũ"),
    ("084950", "sarrusphore", "noun", "/səˈruːsəˌfoʊn/", "kèn gỗ đồng sarrusophone"),
    ("084951", "sarsen", "noun", "/ˈsɑːrsən/", "tảng đá sa thạch cổ (Stonehenge)"),
    ("084952", "sarsenet", "noun", "/ˈsɑːrsənɪt/", "vải lụa dệt mỏng mịn"),
    ("084953", "sartorii", "noun", "/sɑːrˈtɔːriˌaɪ/", "cơ may (ở đùi)"),
    ("084954", "sassaby", "noun", "/ˈsæsəbi/", "linh dương sừng cong tsessebe"),
    ("084955", "sassed", "verb", "/sæst/", "đã trả lời hỗn láo; đã cãi láo"),
    ("084956", "sasses", "verb", "/ˈsæsɪz/", "nói hỗn láo; cãi láo"),
    ("084957", "satang", "noun", "/səˈtɑːŋ/", "đơn vị tiền xu satang Thái Lan"),
    ("084958", "satanically", "adv", "/səˈtænɪkli/", "độc ác như quỷ; tà ác quỷ quyệt"),
    ("084959", "satanology", "noun", "/ˌseɪtəˈnɑːlədʒi/", "nghiên cứu về quỷ Satan"),
    ("084960", "satanophobia", "noun", "/ˌseɪtənəˈfoʊbiə/", "chứng sợ quỷ Satan"),
    ("084961", "sated", "verb", "/ˈseɪtɪd/", "đã làm thỏa mãn; đã ăn no nê"),
    ("084962", "satellites", "noun", "/ˈsætəˌlaɪts/", "vệ tinh nhân tạo; vệ tinh tự nhiên"[:35]),
    ("084963", "sates", "verb", "/seɪts/", "làm thỏa mãn hoàn toàn; làm no nê"[:35]),
    ("084964", "satiability", "noun", "/ˌseɪʃəˈbɪlɪti/", "tính có thể thỏa mãn được"),
    ("084965", "satiable", "adj", "/ˈseɪʃəbəl/", "có thể làm thỏa mãn; làm no được"),
    ("084966", "satiates", "verb", "/ˈseɪʃiˌeɪts/", "làm thỏa mãn; làm no chán"),
    ("084967", "satiating", "verb", "/ˈseɪʃiˌeɪtɪŋ/", "đang làm thỏa mãn; đang làm no"),
    ("084968", "satined", "verb", "/ˈsætənd/", "đã đánh bóng mịn như sa-tanh"),
    ("084969", "satinet", "noun", "/ˌsætɪˈnɛt/", "vải giả lụa sa-tanh"),
    ("084970", "satinette", "noun", "/ˌsætɪˈnɛt/", "vải giả sa-tanh; giống bồ câu"),
    ("084971", "sating", "verb", "/ˈseɪtɪŋ/", "đang làm thỏa mãn; đang làm no"),
    ("084972", "satining", "verb", "/ˈsætənɪŋ/", "đang đánh bóng mịn như sa-tanh"),
    ("084973", "satinleaf", "noun", "/ˈsætənˌliːf/", "cây vú sữa lá vàng đồng"),
    ("084974", "satinpod", "noun", "/ˈsætənˌpɑːd/", "cây hoa đồng tiền bạc Lunaria"),
    ("084975", "satins", "verb", "/ˈsætənz/", "đánh bóng mịn như lụa sa-tanh"),
    ("084976", "satirised", "verb", "/ˈsætəˌraɪzd/", "đã châm biếm; đã đả kích"),
    ("084977", "satirises", "verb", "/ˈsætəˌraɪzɪz/", "châm biếm; đả kích"),
    ("084978", "satirising", "verb", "/ˈsætəˌraɪzɪŋ/", "đang châm biếm; đang đả kích"),
    ("084979", "satirists", "noun", "/ˈsætərɪsts/", "nhà văn châm biếm; người trào phúng"[:35]),
    ("084980", "satirized", "verb", "/ˈsætəˌraɪzd/", "đã châm biếm; đã đả kích"),
    ("084981", "satirizes", "verb", "/ˈsætəˌraɪzɪz/", "châm biếm; đả kích"),
    ("084982", "satirizing", "verb", "/ˈsætəˌraɪzɪŋ/", "đang châm biếm; đang đả kích"),
    ("084983", "satisfactions", "noun", "/ˌsætɪsˈfækʃənz/", "sự hài lòng; điều thỏa mãn"),
    ("084984", "satisfactoriness", "noun", "/ˌsætɪsˈfæktərinəs/", "tính thỏa đáng; sự đáp ứng tốt"),
    ("084985", "satisfiability", "noun", "/ˌsætɪsfaɪəˈbɪlɪti/", "tính thỏa mãn được (lôgic học)"),
    ("084986", "satisfice", "verb", "/ˈsætɪsˌfaɪs/", "chấp nhận phương án đủ tốt"),
    ("084987", "satisfier", "noun", "/ˈsætɪsˌfaɪər/", "yếu tố mang lại sự hài lòng"),
    ("084988", "satisfies", "verb", "/ˈsætɪsˌfaɪz/", "làm hài lòng; đáp ứng đầy đủ"),
    ("084989", "satisfise", "verb", "/ˈsætɪsˌfaɪs/", "chấp nhận phương án đủ tốt"),
    ("084990", "satoshi", "noun", "/səˈtoʊʃi/", "đơn vị Bitcoin nhỏ nhất; tên Nhật"),
    ("084991", "satrapy", "noun", "/ˈseɪtrəpi/", "chức tổng đốc Ba Tư cổ"),
    ("084992", "saturability", "noun", "/ˌsætʃərəˈbɪlɪti/", "tính có thể bão hòa"),
    ("084993", "saturable", "adj", "/ˈsætʃərəbəl/", "có thể bão hòa được"),
    ("084994", "saturant", "noun", "/ˈsætʃərənt/", "chất làm bão hòa; chất tẩm đẫm"),
    ("084995", "saturates", "verb", "/ˈsætʃəˌreɪts/", "làm bão hòa; thấm đẫm"),
    ("084996", "saturating", "verb", "/ˈsætʃəˌreɪtɪŋ/", "đang làm bão hòa; đang thấm đẫm"),
    ("084997", "saturator", "noun", "/ˈsætʃəˌreɪtər/", "thiết bị bão hòa khí; máy bão hòa"[:35]),
    ("084998", "satureia", "noun", "/ˌsætʃəˈriːə/", "chi cây húng bạc hà Satureja"),
    ("084999", "satureja", "noun", "/səˈtjʊriːdʒə/", "chi cây rau thơm Satureja"),
    ("085000", "saturnian", "adj", "/səˈtɜːrniən/", "thuộc sao Thổ; thuộc thần Saturn"),
    ("085001", "saturnic", "adj", "/səˈtɜːrnɪk/", "thuộc nhiễm độc chì; nặng nề u ám"),
    ("085002", "saturniid", "noun", "/səˈtɜːrniˌɪd/", "bướm đêm khổng lồ họ Saturniidae"),
]

# Clean 084962, 084963, 084979, 084997 without slices
RECORDS[59] = ("084962", "satellites", "noun", "/ˈsætəˌlaɪts/", "vệ tinh nhân tạo; vệ tinh")
RECORDS[60] = ("084963", "sates", "verb", "/seɪts/", "làm thỏa mãn; làm no nê")
RECORDS[76] = ("084979", "satirists", "noun", "/ˈsætərɪsts/", "nhà văn châm biếm; nhà trào phúng")
RECORDS[94] = ("084997", "saturator", "noun", "/ˈsætʃəˌreɪtər/", "thiết bị bão hòa; máy bão hòa")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r10_raw_p5.json"))
by_id = {r["id"].split(".")[-1]: r for r in raw}
out = []
for sid, hw, pos, ipa, vi in RECORDS:
    rec = dict(by_id[sid])
    assert rec["hw"] == hw, (sid, hw, rec["hw"])
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

json.dump(out, open("scratch/b37_r10_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b37_r10_p5 saved OK")
