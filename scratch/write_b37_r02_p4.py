import json

records = [
    ("080803", "pyrrhonist", "noun", "/ˈpɪrənɪst/", "người theo thuyết hoài nghi Pyrrho"),
    ("080804", "pyrrhotine", "noun", "/ˈpɪrəˌtiːn/", "khoáng vật pyrotin (sunfua sắt)"),
    ("080805", "pyrrhula", "noun", "/ˈpɪrjələ/", "chi chim sẻ hồng (Pyrrhula)"),
    ("080806", "pyrrhuloxia", "noun", "/ˌpɪrjəˈlɑːksiə/", "chim giáo chủ sa mạc (Pyrrhuloxia)"),
    ("080807", "pyrrophyta", "noun", "/ˌpɪrəˈfaɪtə/", "ngành Tảo giáp hai roi (sinh học)"),
    ("080808", "pyrrosia", "noun", "/pɪˈroʊziə/", "chi dương xỉ thạch vi (Pyrrosia)"),
    ("080809", "pyrularia", "noun", "/ˌpɪrjəˈlɛriə/", "chi cây hạt dầu ký sinh Pyrularia"),
    ("080810", "pythagoreanism", "noun", "/pəˌθæɡəˈriːəˌnɪzəm/", "học thuyết triết học Pythagoras"),
    ("080811", "pythiaceae", "noun", "/ˌpɪθiˈeɪsiː/", "họ Nấm thối rễ Pythiaceae"),
    ("080812", "pythiad", "noun", "/ˈpɪθiˌæd/", "chu kỳ 4 năm giữa hai hội Pythian"),
    ("080813", "pythian", "adj", "/ˈpɪθiən/", "thuộc nữ tiên tri đền Delphi"),
    ("080814", "pythius", "noun", "/ˈpɪθiəs/", "danh hiệu thần Apollo (thần thoại)"),
    ("080815", "pythoness", "noun", "/ˈpaɪθənəs/", "nữ tiên tri đền Delphi; nữ phù thủy"),
    ("080816", "pythonidae", "noun", "/paɪˈθɑːnɪˌdiː/", "họ Trăn (bò sát không độc)"),
    ("080817", "pythoninae", "noun", "/ˌpaɪθəˈnaɪniː/", "phân họ Trăn (Pythoninae)"),
    ("080818", "pythonism", "noun", "/ˈpaɪθəˌnɪzəm/", "thuật bói toán tuyên sấm Delphi"),
    ("080819", "pyuria", "noun", "/paɪˈjʊriə/", "chứng đái ra mủ, mủ niệu (y học)"),
    ("080820", "pyxed", "verb", "/pɪkst/", "đã đặt mẫu tiền vào hòm kiểm định"),
    ("080821", "pyxes", "verb", "/ˈpɪksɪz/", "đặt mẫu tiền xu vào hòm kiểm định"),
    ("080822", "pyxidanthera", "noun", "/ˌpɪksɪdænˈθɪrə/", "chi cây rêu hoa Bắc Mỹ Pyxidanthera"),
    ("080823", "pyxidate", "adj", "/ˈpɪksəˌdeɪt/", "có quả nang mở nắp kiểu hộp"),
    ("080824", "pyxides", "noun", "/ˈpɪksəˌdiːz/", "các bình thánh lễ; các quả hộp"),
    ("080825", "pyxidia", "noun", "/pɪkˈsɪdiə/", "các quả nang nứt ngang có nắp"),
    ("080826", "pyxidium", "noun", "/pɪkˈsɪdiəm/", "quả nang nứt ngang có nắp đậy"),
    ("080827", "pyxie", "noun", "/ˈpɪksi/", "cây bụi nhỏ Pyxie (vùng đầm lầy)"),
    ("080828", "pyxing", "verb", "/ˈpɪksɪŋ/", "đặt mẫu tiền xu vào hòm kiểm định"),
    ("080829", "qabala", "noun", "/kəˈbɑːlə/", "thuyết thần bí Do Thái Kabbalah"),
    ("080830", "qabbala", "noun", "/kəˈbɑːlə/", "thuyết huyền bí Do Thái Kabbalah"),
    ("080831", "qabbalah", "noun", "/kəˈbɑːlə/", "thuyết thần bí Do Thái Kabbalah"),
    ("080832", "qaqortoq", "noun", "/ˈkɑːkɔːrˌtɑːk/", "thị trấn Qaqortoq ở nam Greenland"),
    ("080833", "qazaqstan", "noun", "/ˌkɑːzɑːkˈstɑːn/", "nước Kazakhstan (tên bản địa)"),
    ("080834", "qb", "noun", "/ˌkjuːˈbiː/", "tòa án Nữ hoàng (luật Anh)"),
    ("080835", "qbbasic", "noun", "/ˌkjuːbiːˈbeɪsɪk/", "ngôn ngữ lập trình QBasic (lỗi)"),
    ("080836", "qc", "noun", "/ˌkjuːˈsiː/", "luật sư hoàng gia (QC, viết tắt)"),
    ("080837", "qepiq", "noun", "/ˈkɛpɪk/", "đơn vị tiền xu qepik (Azerbaijan)"),
    ("080838", "qian", "noun", "/tʃjɛn/", "tiền đồng cổ Trung Hoa; họ Tiền"),
    ("080839", "qiangic", "noun", "/tʃiˈæŋɪk/", "nhóm ngôn ngữ Khương (Hán-Tạng)"),
    ("080840", "qic", "noun", "/ˌkjuːaɪˈsiː/", "băng từ lưu trữ chuẩn QIC (tin học)"),
    ("080841", "qindarka", "noun", "/kɪnˈdɑːrkə/", "đồng tiền xu qindarka (Albania)"),
    ("080842", "qintar", "noun", "/kɪnˈtɑːr/", "đồng tiền xu qintar (Albania)"),
    ("080843", "qoph", "noun", "/kɔːf/", "chữ cái thứ 19 tiếng Do Thái (Qoph)"),
    ("080844", "qr", "noun", "/ˌkjuːˈɑːr/", "một phần tư, quý (viết tắt)"),
    ("080845", "qt", "noun", "/kwɔːrt/", "đơn vị thể tích quart (viết tắt qt)"),
    ("080846", "qto", "noun", "/ˈkwɔːrtoʊ/", "khổ sách tư (quarto, viết tắt)"),
    ("080847", "qty", "noun", "/ˈkwɑːntəti/", "số lượng (quantity, viết tắt qty)"),
    ("080848", "qua", "conj", "/kweɪ/", "với tư cách là, trên cương vị là"),
    ("080849", "quacdragesima", "noun", "/ˌkwɑːdrəˈdʒɛsəmə/", "Chủ nhật đầu Mùa Chay (lỗi viết)"),
    ("080850", "quacdragesimal", "adj", "/ˌkwɑːdrəˈdʒɛsəməl/", "thuộc 40 ngày Mùa Chay (lỗi viết)"),
    ("080851", "quacked", "verb", "/kwækt/", "đã kêu cạp cạp; đã ba hoa khoác lác"),
    ("080852", "quackgrass", "noun", "/ˈkwækˌɡræs/", "cỏ gấu mì dại (Elymus repens)"),
    ("080853", "quacking", "verb", "/ˈkwækɪŋ/", "kêu cạp cạp (vịt); ba hoa khoác lác"),
    ("080854", "quackish", "adj", "/ˈkwækɪʃ/", "mang tính lang băm, lừa bịp y học"),
    ("080855", "quackle", "verb", "/ˈkwækəl/", "nghẹn thở; kêu cạp cạp khàn giọng"),
    ("080856", "quacks", "verb", "/kwæks/", "kêu cạp cạp (vịt); nói khoác lác"),
    ("080857", "quacksalver", "noun", "/ˈkwækˌsælvər/", "thầy thuốc lang băm, kẻ lừa đảo"),
    ("080858", "quacksalvers", "noun", "/ˈkwækˌsælvərz/", "những tên lang băm bán thuốc giả"),
    ("080859", "quadded", "adj", "/ˈkwɑːdɪd/", "gồm bốn sợi xoắn; chèn khoảng in"),
    ("080860", "quadragenarian", "adj", "/ˌkwɑːdrədʒəˈnɛriən/", "ở độ tuổi bốn mươi (40 đến 49 tuổi)"),
    ("080861", "quadragesima", "noun", "/ˌkwɑːdrəˈdʒɛsəmə/", "Chủ nhật đầu tiên của Mùa Chay"),
    ("080862", "quadragesimal", "adj", "/ˌkwɑːdrəˈdʒɛsəməl/", "thuộc bốn mươi ngày Mùa Chay"),
    ("080863", "quadrantal", "adj", "/kwɑːˈdræntəl/", "thuộc góc phần tư (toán, hàng hải)"),
    ("080864", "quadrantanopia", "noun", "/kwɑːˌdræntəˈnoʊpiə/", "chứng bán manh góc phần tư (y học)"),
    ("080865", "quadrants", "noun", "/ˈkwɑːdrənts/", "các cung phần tư; góc phần tư"),
    ("080866", "quadraphony", "noun", "/kwɑːˈdræfəni/", "hệ thống âm thanh bốn kênh độc lập"),
    ("080867", "quadrasonic", "adj", "/ˌkwɑːdrəˈsɑːnɪk/", "thuộc hệ thống âm thanh bốn kênh"),
    ("080868", "quadrat", "noun", "/ˈkwɑːdræt/", "ô vuông định lượng (sinh thái học)"),
    ("080869", "quadratron", "noun", "/ˈkwɑːdrəˌtrɑːn/", "đèn điện tử bốn cực (cũ)"),
    ("080870", "quadratures", "noun", "/ˈkwɑːdrətʃərz/", "phép cầu phương; vị trí góc vuông"),
    ("080871", "quadratus", "noun", "/kwɑːˈdreɪtəs/", "cơ vuông (giải phẫu học)"),
    ("080872", "quadrel", "noun", "/ˈkwɑːdrəl/", "viên gạch lát hình vuông, đá vuông"),
    ("080873", "quadrennial", "adj", "/kwɑːˈdrɛniəl/", "kéo dài 4 năm; 4 năm một lần"),
    ("080874", "quadrennium", "noun", "/kwɑːˈdrɛniəm/", "khoảng thời gian bốn năm"),
    ("080875", "quadricapsular", "adj", "/ˌkwɑːdrəˈkæpsələr/", "có bốn nang, có bốn bao (thực vật)"),
    ("080876", "quadricarpellary", "adj", "/ˌkwɑːdrəˈkɑːrpəˌlɛri/", "có bốn lá noãn (thực vật học)"),
    ("080877", "quadricentennial", "adj", "/ˌkwɑːdrəsɛnˈtɛniəl/", "thuộc lễ kỷ niệm 400 năm"),
    ("080878", "quadricentennials", "noun", "/ˌkwɑːdrəsɛnˈtɛniəlz/", "những lễ kỷ niệm 400 năm"),
    ("080879", "quadricorn", "noun", "/ˈkwɑːdrəˌkɔːrn/", "động vật có bốn sừng (động vật học)"),
    ("080880", "quadricornous", "adj", "/ˌkwɑːdrəˈkɔːrnəs/", "có bốn sừng (động vật học)"),
    ("080881", "quadricotyledonous", "adj", "/ˌkwɑːdrəˌkɑːtəlˈiːdənəs/", "có bốn lá mầm (thực vật học)"),
    ("080882", "quadricycle", "noun", "/ˈkwɑːdrəˌsaɪkəl/", "xe đạp bốn bánh (khung sơ khai)"),
    ("080883", "quadridentate", "adj", "/ˌkwɑːdrəˈdɛnteɪt/", "có bốn răng cưa (sinh học)"),
    ("080884", "quadrifarious", "adj", "/ˌkwɑːdrəˈfɛriəs/", "xếp thành bốn hàng dọc (lá, thân)"),
    ("080885", "quadrifid", "adj", "/ˈkwɑːdrəfɪd/", "chia làm bốn thùy sâu (thực vật)"),
    ("080886", "quadrifoil", "noun", "/ˈkwɑːdrəˌfɔɪl/", "cây cỏ bốn lá; hoa văn bốn cánh"),
    ("080887", "quadriga", "noun", "/kwɑːˈdraɪɡə/", "chiến xa bốn ngựa kéo (La Mã cổ)"),
    ("080888", "quadrigae", "noun", "/kwɑːˈdraɪdʒiː/", "các chiến xa bốn ngựa kéo (cổ đại)"),
    ("080889", "quadrigeminal", "adj", "/ˌkwɑːdrəˈdʒɛmənəl/", "gồm bốn phần giống nhau; sinh tư"),
    ("080890", "quadrilingual", "adj", "/ˌkwɑːdrəˈlɪŋɡwəl/", "thông thạo bốn thứ tiếng"),
    ("080891", "quadrillions", "noun", "/kwɑːˈdrɪljənz/", "hàng triệu tỷ (Mỹ), ngàn tỷ tỷ"),
    ("080892", "quadrillionth", "adj", "/kwɑːˈdrɪljənθ/", "thứ một triệu tỷ (10 mũ 15)"),
    ("080893", "quadrilobate", "adj", "/ˌkwɑːdrəˈloʊbeɪt/", "có bốn thùy (thực vật, sinh học)"),
    ("080894", "quadrilocular", "adj", "/ˌkwɑːdrəˈlɑːkjələr/", "có bốn ngăn, bốn ô (bầu nhụy)"),
    ("080895", "quadrimaculate", "adj", "/ˌkwɑːdrəˈmækjəlɪt/", "có bốn đốm màu (côn trùng học)"),
    ("080896", "quadrimanous", "adj", "/kwɑːˈdrɪmənəs/", "có bốn bàn tay cầm nắm"),
    ("080897", "quadrinate", "adj", "/ˈkwɑːdrəˌneɪt/", "có bốn lá chét mọc cùng cuống"),
    ("080898", "quadripara", "noun", "/kwɑːˈdrɪpərə/", "sản phụ sinh con lần thứ tư (y học)"),
    ("080899", "quadripennate", "adj", "/ˌkwɑːdrəˈpɛneɪt/", "có bốn cánh (côn trùng học)"),
    ("080900", "quadriphonic", "adj", "/ˌkwɑːdrəˈfɑːnɪk/", "thuộc hệ thống âm thanh bốn kênh"),
    ("080901", "quadriphyllous", "adj", "/ˌkwɑːdrəˈfɪləs/", "có bốn lá mọc vòng (thực vật)"),
    ("080902", "quadripinnate", "adj", "/ˌkwɑːdrəˈpɪneɪt/", "xẻ lông chim bốn lần (lá dương xỉ)"),
]

raw = json.load(open("scratch/b37_r02_raw_p4.json"))
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
with open("scratch/b37_r02_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r02_p4 saved OK")
