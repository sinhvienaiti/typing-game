import json

rows = [
    ("075603", "peristaltically", "adv", "/ˌpɛrɪˈstæltɪkli/", "bằng nhu động (ống tiêu hóa)"),
    ("075604", "peristediinae", "noun", "/ˌpɛrɪstɪˈdaɪɪniː/", "phân họ Cá chào mào giáp"),
    ("075605", "peristedion", "noun", "/ˌpɛrɪˈstiːdiɒn/", "chi cá chào mào giáp Peristedion"),
    ("075606", "peristomal", "adj", "/ˌpɛrɪˈstoʊməl/", "thuộc miệng bào tử; quanh miệng"),
    ("075607", "peristomes", "noun", "/ˈpɛrɪstoʊmz/", "miệng bào tử; vành quanh miệng"),
    ("075608", "peristylar", "adj", "/ˌpɛrɪˈstaɪlər/", "có hàng cột bao quanh sân trong"),
    ("075609", "perithecia", "noun", "/ˌpɛrɪˈθiːʃə/", "thể bình chứa túi bào tử (nấm)"),
    ("075610", "perithecial", "adj", "/ˌpɛrɪˈθiːʃəl/", "thuộc thể bình bào tử (nấm)"),
    ("075611", "perithecium", "noun", "/ˌpɛrɪˈθiːʃiəm/", "thể bình chứa túi bào tử (nấm)"),
    ("075612", "perithelial", "adj", "/ˌpɛrɪˈθiːliəl/", "thuộc lớp mô quanh mạch máu nhỏ"),
    ("075613", "perithelium", "noun", "/ˌpɛrɪˈθiːliəm/", "mô liên kết quanh mao mạch"),
    ("075614", "peritonaeum", "noun", "/ˌpɛrɪtəˈniːəm/", "màng bụng, phúc mạc (giải phẫu)"),
    ("075615", "peritonea", "noun", "/ˌpɛrɪtəˈniːə/", "màng bụng, phúc mạc (giải phẫu)"),
    ("075616", "peritoneally", "adv", "/ˌpɛrɪtəˈniːəli/", "qua đường màng bụng (phúc mạc)"),
    ("075617", "peritoneums", "noun", "/ˌpɛrɪtəˈniːəmz/", "màng bụng, phúc mạc (giải phẫu)"),
    ("075618", "peritrate", "noun", "/ˈpɛrɪtreɪt/", "thuốc giãn mạch vành Peritrate"),
    ("075619", "peritrichous", "adj", "/pəˈrɪtrɪkəs/", "có tiên mao mọc khắp bề mặt"),
    ("075620", "periwigged", "adj", "/ˈpɛrɪwɪɡd/", "đội bộ tóc giả dài cổ điển"),
    ("075621", "perjured", "verb", "/ˈpɜːrdʒərd/", "đã khai man trước tòa"),
    ("075622", "perjurers", "noun", "/ˈpɜːrdʒərərz/", "kẻ khai man trước tòa"),
    ("075623", "perjures", "verb", "/ˈpɜːrdʒərz/", "khai man trước tòa"),
    ("075624", "perjuries", "noun", "/ˈpɜːrdʒəriz/", "tội khai man (lời thề dối)"),
    ("075625", "perjuring", "verb", "/ˈpɜːrdʒərɪŋ/", "khai man trước tòa"),
    ("075626", "perjurious", "adj", "/pərˈdʒʊriəs/", "mang tính khai man, bội thề"),
    ("075627", "perjuriously", "adv", "/pərˈdʒʊriəsli/", "theo cách khai man, bội thề"),
    ("075628", "perked", "verb", "/pɜːrkt/", "đã ngẩng lên; pha cà phê lọc"),
    ("075629", "perkily", "adv", "/ˈpɜːrkɪli/", "một cách hoạt bát, lanh lợi"),
    ("075630", "perking", "verb", "/ˈpɜːrkɪŋ/", "ngẩng đầu lên; pha cà phê lọc"),
    ("075631", "perks", "verb", "/pɜːrks/", "ngẩng lên; hồi tỉnh; pha cà phê"),
    ("075632", "perlacous", "adj", "/pɜːrˈleɪʃəs/", "óng ánh như ngọc trai"),
    ("075633", "perleche", "noun", "/pɛrˈlɛʃ/", "chứng chốc mép, nứt khóe miệng"),
    ("075634", "perlemoen", "noun", "/ˈpɛrləmuːn/", "bào ngư Nam Phi (perlemoen)"),
    ("075635", "perlite", "noun", "/ˈpɜːrlaɪt/", "đá thủy tinh núi lửa perlit"),
    ("075636", "perlitic", "adj", "/pərˈlɪtɪk/", "thuộc đá trân châu perlit"),
    ("075637", "permagrins", "noun", "/ˈpɜːrməɡrɪnz/", "nụ cười gượng cứng đơ thường trực"),
    ("075638", "permalink", "noun", "/ˈpɜːrməlɪŋk/", "liên kết cố định vĩnh viễn (web)"),
    ("075639", "permanentness", "noun", "/ˈpɜːrmənəntnəs/", "tính vĩnh viễn, lâu dài"),
    ("075640", "permanganic", "adj", "/ˌpɜːrmæŋˈɡænɪk/", "thuộc axit pemanganic (hóa học)"),
    ("075641", "permeableness", "noun", "/ˈpɜːrmiəbəlnəs/", "tính thấm qua được (màng, đá)"),
    ("075642", "permeably", "adv", "/ˈpɜːrmiəbli/", "có thể thấm qua được"),
    ("075643", "permeance", "noun", "/ˈpɜːrmiəns/", "độ dẫn từ; độ thấm khí (vật lý)"),
    ("075644", "permease", "noun", "/ˈpɜːrmieɪs/", "enzym vận chuyển qua màng tế bào"),
    ("075645", "permeated", "verb", "/ˈpɜːrmiˌeɪtɪd/", "đã thấm qua, lan tỏa khắp"),
    ("075646", "permeates", "verb", "/ˈpɜːrmiˌeɪts/", "thấm qua, lan tỏa khắp"),
    ("075647", "permeative", "adj", "/ˈpɜːrmiətɪv/", "có tính lan tỏa, thấm khắp"),
    ("075648", "permic", "noun", "/ˈpɜːrmɪk/", "nhóm ngôn ngữ Permi; kỷ Pecmi"),
    ("075649", "permineralization", "noun", "/pərˌmɪnərəlaɪˈzeɪʃən/", "quá trình khoáng hóa hóa thạch"),
    ("075650", "permineralizations", "noun", "/pərˌmɪnərəlaɪˈzeɪʃənz/", "quá trình khoáng hóa hóa thạch"),
    ("075651", "permiscible", "adj", "/pərˈmɪsɪbəl/", "có thể trộn lẫn được với nhau"),
    ("075652", "permissibilities", "noun", "/pərˌmɪsəˈbɪlɪtiz/", "tính có thể cho phép, chấp nhận"),
    ("075653", "permissibleness", "noun", "/pərˈmɪsɪbəlnəs/", "tính có thể cho phép được"),
    ("075654", "permissions", "noun", "/pərˈmɪʃənz/", "sự cho phép; quyền hạn, giấy phép"),
    ("075655", "permits", "verb", "/pərˈmɪts/", "cho phép, chấp thuận"),
    ("075656", "permittance", "noun", "/pərˈmɪtəns/", "độ điện dung; sự cho phép (cổ)"),
    ("075657", "permitted", "verb", "/pərˈmɪtɪd/", "đã cho phép, chấp thuận"),
    ("075658", "permitter", "noun", "/pərˈmɪtər/", "người cấp phép, người cho phép"),
    ("075659", "permitting", "verb", "/pərˈmɪtɪŋ/", "cho phép, chấp thuận"),
    ("075660", "permittivity", "noun", "/ˌpɜːrmɪˈtɪvɪti/", "hằng số điện môi tuyệt đối"),
    ("075661", "permutability", "noun", "/pərˌmjuːtəˈbɪlɪti/", "tính có thể hoán vị, đổi chỗ"),
    ("075662", "permutable", "adj", "/pərˈmjuːtəbəl/", "có thể hoán vị, thay đổi thứ tự"),
    ("075663", "permutableness", "noun", "/pərˈmjuːtəbəlnəs/", "tính có thể hoán vị, đổi chỗ"),
    ("075664", "permutably", "adv", "/pərˈmjuːtəbli/", "có thể hoán vị cho nhau được"),
    ("075665", "permutational", "adj", "/ˌpɜːrmjʊˈteɪʃənəl/", "thuộc phép hoán vị (toán học)"),
    ("075666", "pern", "noun", "/pɜːrn/", "chim ó ăn ong (diều hâu ăn ong)"),
    ("075667", "perniciousness", "noun", "/pərˈnɪʃəsnəs/", "tính thâm độc, nguy hại khôn lường"),
    ("075668", "pernio", "noun", "/ˈpɜːrnioʊ/", "chứng cước da do lạnh (y học)"),
    ("075669", "pernis", "noun", "/ˈpɜːrnɪs/", "chi chim ó ăn ong (Pernis)"),
    ("075670", "pernoctation", "noun", "/ˌpɜːrnɒkˈteɪʃən/", "sự thức suốt đêm (cầu nguyện)"),
    ("075671", "pernorate", "verb", "/pərˈnɔːreɪt/", "kết luận bài diễn văn (biến thể)"),
    ("075672", "pernoration", "noun", "/ˌpɜːrnəˈreɪʃən/", "đoạn kết bài diễn văn (biến thể)"),
    ("075673", "perodicticus", "noun", "/ˌpɛroʊˈdɪktɪkəs/", "chi cu li potto châu Phi"),
    ("075674", "peroneous", "noun", "/ˌpɛrəˈniːəs/", "cơ mác (biến thể của peroneus)"),
    ("075675", "peronosporaceae", "noun", "/ˌpɛrənɒspəˈreɪsiː/", "họ Nấm sương mai (thực vật)"),
    ("075676", "peronosporales", "noun", "/ˌpɛrənɒspəˈreɪliːz/", "bộ Nấm sương mai (Peronosporales)"),
    ("075677", "perorate", "verb", "/ˈpɛrəreɪt/", "diễn thuyết hùng hồn; kết luận"),
    ("075678", "peroretion", "noun", "/ˌpɛrəˈreɪʃən/", "đoạn kết diễn văn (biến thể cũ)"),
    ("075679", "peroxided", "verb", "/pəˈrɒksaɪdɪd/", "đã tẩy trắng bằng ôxy già"),
    ("075680", "peroxides", "noun", "/pəˈrɒksaɪdz/", "hợp chất peroxit; ôxy già"),
    ("075681", "peroxidic", "adj", "/ˌpɛrɒkˈsɪdɪk/", "thuộc hợp chất peroxit"),
    ("075682", "peroxiding", "verb", "/pəˈrɒksaɪdɪŋ/", "tẩy trắng bằng ôxy già"),
    ("075683", "peroxyde", "noun", "/pəˈrɒksaɪd/", "peroxit (cách viết cũ)"),
    ("075684", "perpend", "verb", "/pərˈpɛnd/", "cân nhắc kỹ; viên gạch liên kết"),
    ("075685", "perpetrated", "verb", "/ˈpɜːrpɪˌtreɪtɪd/", "đã gây ra (tội ác, hành vi xấu)"),
    ("075686", "perpetrates", "verb", "/ˈpɜːrpɪˌtreɪts/", "gây ra (tội ác, hành vi xấu)"),
    ("075687", "perpetrating", "verb", "/ˈpɜːrpɪˌtreɪtɪŋ/", "gây ra (tội ác, hành vi xấu)"),
    ("075688", "perpetuance", "noun", "/pərˈpɛtʃuəns/", "sự duy trì lâu dài, vĩnh viễn"),
    ("075689", "perpetuated", "verb", "/pərˈpɛtʃueɪtɪd/", "đã duy trì vĩnh viễn, lưu truyền"),
    ("075690", "perpetuates", "verb", "/pərˈpɛtʃueɪts/", "duy trì vĩnh viễn, lưu truyền mãi"),
    ("075691", "perpetuating", "verb", "/pərˈpɛtʃueɪtɪŋ/", "duy trì vĩnh viễn, lưu truyền mãi"),
    ("075692", "perpetuator", "noun", "/pərˈpɛtʃueɪtər/", "người duy trì, người lưu truyền"),
    ("075693", "perplexedly", "adv", "/pərˈplɛksɪdli/", "một cách bối rối, lúng túng"),
    ("075694", "perplexes", "verb", "/pərˈplɛksɪz/", "làm bối rối, làm rối trí"),
    ("075695", "perplexingly", "adv", "/pərˈplɛksɪŋli/", "một cách gây bối rối, khó hiểu"),
    ("075696", "perquisition", "noun", "/ˌpɜːrkwɪˈzɪʃən/", "sự tra xét, khám soát tỉ mỉ"),
    ("075697", "perron", "noun", "/ˈpɛrən/", "bậc thềm đá ngoài cửa lớn"),
    ("075698", "pers", "noun", "/pɜːrs/", "viết tắt của person (ngôi, người)"),
    ("075699", "perse", "adj", "/pɜːrs/", "màu xanh lam đậm (xanh xám cổ)"),
    ("075700", "persecuted", "verb", "/ˈpɜːrsɪˌkjuːtɪd/", "đã ngược đãi, bức hại"),
    ("075701", "persecutes", "verb", "/ˈpɜːrsɪˌkjuːts/", "ngược đãi, bức hại"),
    ("075702", "persecuting", "verb", "/ˈpɜːrsɪˌkjuːtɪŋ/", "ngược đãi, bức hại"),
]

with open("scratch/b36_r02_raw_p2.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r02_p2.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r02_p2 saved OK")
