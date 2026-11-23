import json

records = [
    ("079503", "prolificness", "noun", "/prəˈlɪfɪknəs/", "sức sinh sản dồi dào, tính trù phú"),
    ("079504", "proligerous", "adj", "/proʊˈlɪdʒərəs/", "sinh sản, tạo phôi, đẻ con"),
    ("079505", "prolixities", "noun", "/proʊˈlɪksətiz/", "sự dài dòng, lời văn rườm rà"),
    ("079506", "prolixly", "adv", "/proʊˈlɪksli/", "một cách dài dòng, rườm rà"),
    ("079507", "prolixness", "noun", "/proʊˈlɪksnəs/", "tính dài dòng, sự rườm rà"),
    ("079508", "prolocutor", "noun", "/proʊˈlɑːkjətər/", "chủ tọa hội nghị; người phát ngôn"),
    ("079509", "prologise", "verb", "/ˈproʊləˌdʒaɪz/", "viết lời tựa, nói lời mở đầu (Anh)"),
    ("079510", "prologize", "verb", "/ˈproʊləˌdʒaɪz/", "viết lời tựa, nói lời mở đầu"),
    ("079511", "prologuize", "verb", "/ˈproʊləˌɡaɪz/", "viết lời tựa, đọc lời mở đầu"),
    ("079512", "prolongable", "adj", "/prəˈlɔːŋəbəl/", "có thể kéo dài, có thể gia hạn"),
    ("079513", "prolongate", "verb", "/proʊˈlɔːŋɡeɪt/", "kéo dài, nối dài, gia hạn"),
    ("079514", "prolongations", "noun", "/ˌproʊlɔːŋˈɡeɪʃənz/", "sự kéo dài, thời gian gia hạn"),
    ("079515", "prolonge", "noun", "/prəˈlɔːndʒ/", "dây kéo pháo (quân sự lịch sử)"),
    ("079516", "prolonger", "noun", "/prəˈlɔːŋər/", "người kéo dài; vật nối dài"),
    ("079517", "prolonging", "verb", "/prəˈlɔːŋɪŋ/", "kéo dài ra, nối dài, gia hạn"),
    ("079518", "prolongs", "verb", "/prəˈlɔːŋz/", "kéo dài ra, nối dài, gia hạn"),
    ("079519", "prolusion", "noun", "/proʊˈluːʒən/", "bài viết mở đầu; phần khởi động"),
    ("079520", "prolusory", "adj", "/proʊˈluːsəri/", "mở đầu, nhập đề, khởi động"),
    ("079521", "promenaded", "verb", "/ˌprɑːməˈneɪdɪd/", "đã đi dạo, đã tản bộ"),
    ("079522", "promenader", "noun", "/ˌprɑːməˈneɪdər/", "người đi dạo, khách tản bộ"),
    ("079523", "promenades", "verb", "/ˌprɑːməˈneɪdz/", "đi dạo, tản bộ, dạo chơi"),
    ("079524", "promenading", "verb", "/ˌprɑːməˈneɪdɪŋ/", "đi dạo, tản bộ, dạo chơi"),
    ("079525", "promerops", "noun", "/prəˈmɛrɑːps/", "chi chim hút mật đuôi dài"),
    ("079526", "promethean", "adj", "/prəˈmiːθiən/", "táo bạo, sáng tạo kiểu Prometheus"),
    ("079527", "prominency", "noun", "/ˈprɑːmənənsi/", "sự nổi bật, chỗ nhô cao (ít dùng)"),
    ("079528", "promiscuousness", "noun", "/prəˈmɪskjuəsnəs/", "tính bừa bãi, lối sống phóng túng"),
    ("079529", "promised", "verb", "/ˈprɑːmɪst/", "đã hứa, đã cam kết, hứa hẹn"),
    ("079530", "promiser", "noun", "/ˈprɑːmɪsər/", "người hứa, người cam kết"),
    ("079531", "promises", "verb", "/ˈprɑːmɪsɪz/", "hứa, cam kết, hứa hẹn"),
    ("079532", "promisorry", "adj", "/ˈprɑːmɪˌsɔːri/", "hứa hẹn; hẹn trả nợ (lỗi viết)"),
    ("079533", "promotability", "noun", "/prəˌmoʊtəˈbɪləti/", "khả năng được thăng tiến"),
    ("079534", "promotable", "adj", "/prəˈmoʊtəbəl/", "có thể thăng chức, quảng bá được"),
    ("079535", "promoted", "verb", "/prəˈmoʊtɪd/", "đã thăng chức; thúc đẩy, quảng bá"),
    ("079536", "promotes", "verb", "/prəˈmoʊts/", "thăng chức; thúc đẩy, quảng bá"),
    ("079537", "promoting", "verb", "/prəˈmoʊtɪŋ/", "thăng chức; thúc đẩy, quảng bá"),
    ("079538", "promotionally", "adv", "/prəˈmoʊʃənəli/", "nhằm quảng bá, mang tính khuyến mãi"),
    ("079539", "promotiveness", "noun", "/prəˈmoʊtɪvnəs/", "tính thúc đẩy, tính xúc tiến"),
    ("079540", "promptbook", "noun", "/ˈprɑːmptˌbʊk/", "sổ nhắc vở (sân khấu)"),
    ("079541", "prompted", "verb", "/ˈprɑːmptɪd/", "đã thúc đẩy, xui khiến; nhắc lời"),
    ("079542", "prompts", "verb", "/ˈprɑːmpts/", "thúc đẩy, gợi ý; nhắc lời diễn"),
    ("079543", "promulgates", "verb", "/ˈprɑːməlˌɡeɪts/", "ban bố, công bố; truyền bá"),
    ("079544", "promulgating", "verb", "/ˈprɑːməlˌɡeɪtɪŋ/", "ban bố, công bố; truyền bá"),
    ("079545", "promulgator", "noun", "/ˈprɑːməlˌɡeɪtər/", "người ban hành, người truyền bá"),
    ("079546", "promulge", "verb", "/proʊˈmʌldʒ/", "công bố, ban bố, ban hành (cổ)"),
    ("079547", "promycelium", "noun", "/ˌproʊmaɪˈsiːliəm/", "sợi nấm sơ sinh, đảm sơ (nấm)"),
    ("079548", "pronaos", "noun", "/proʊˈneɪɑːs/", "tiền sảnh đền thờ Hy Lạp cổ"),
    ("079549", "pronates", "verb", "/ˈproʊneɪts/", "lật sấp bàn tay hoặc bàn chân"),
    ("079550", "pronely", "adv", "/ˈproʊnli/", "nằm sấp, úp mặt xuống; dễ bị"),
    ("079551", "pronephric", "adj", "/proʊˈnɛfrɪk/", "thuộc tiền thận (phôi học)"),
    ("079552", "pronephros", "noun", "/proʊˈnɛfrəs/", "tiền thận (cơ quan bài tiết phôi)"),
    ("079553", "proneur", "noun", "/proʊˈnɜːr/", "người tán dương, người đề xướng"),
    ("079554", "prongbuck", "noun", "/ˈprɔːŋˌbʌk/", "linh dương sừng nhánh Bắc Mỹ"),
    ("079555", "prongy", "adj", "/ˈprɔːŋi/", "có nhánh nhọn, giống chĩa nĩa"),
    ("079556", "pronominally", "adv", "/proʊˈnɑːmənəli/", "như một đại từ (ngữ pháp)"),
    ("079557", "pronouncedly", "adv", "/prəˈnaʊnsɪdli/", "một cách rõ rệt, rõ ràng"),
    ("079558", "pronouncedness", "noun", "/prəˈnaʊnsɪdnəs/", "sự rõ rệt, tính nổi bật rõ ràng"),
    ("079559", "pronouncer", "noun", "/prəˈnaʊnsər/", "người phát âm; người tuyên án"),
    ("079560", "pronounces", "verb", "/prəˈnaʊnsɪz/", "phát âm; tuyên bố chính thức"),
    ("079561", "pronounciamento", "noun", "/prəˌnaʊnsiəˈmɛntoʊ/", "bản tuyên ngôn đảo chính"),
    ("079562", "pronounciation", "noun", "/prəˌnʌnsiˈeɪʃən/", "cách phát âm (lỗi chính tả)"),
    ("079563", "pronouncing", "verb", "/prəˈnaʊnsɪŋ/", "phát âm; tuyên bố chính thức"),
    ("079564", "pronuciation", "noun", "/prəˌnʌnsiˈeɪʃən/", "cách phát âm (lỗi chính tả)"),
    ("079565", "pronuclei", "noun", "/proʊˈnuːkliˌaɪ/", "các tiền nhân (tế bào sinh dục)"),
    ("079566", "pronucleus", "noun", "/proʊˈnuːkliəs/", "tiền nhân (tế bào sinh dục)"),
    ("079567", "pronuncial", "adj", "/prəˈnʌnʃəl/", "thuộc phát âm hoặc tuyên bố"),
    ("079568", "pronunciamento", "noun", "/prəˌnʌnsiəˈmɛntoʊ/", "bản tuyên ngôn, lời tuyên cáo"),
    ("079569", "pronunciational", "adj", "/prəˌnʌnsiˈeɪʃənəl/", "thuộc về cách phát âm"),
    ("079570", "pronunciations", "noun", "/prəˌnʌnsiˈeɪʃənz/", "những cách phát âm"),
    ("079571", "pronunciative", "adj", "/prəˈnʌnsiətɪv/", "thuộc phát âm; hay phán xét"),
    ("079572", "pronunciatory", "adj", "/prəˈnʌnsiəˌtɔːri/", "mang tính phát âm, tuyên bố"),
    ("079573", "proofing", "verb", "/ˈpruːfɪŋ/", "chống thấm; ủ bột; in thử kiểm tra"),
    ("079574", "proofless", "adj", "/ˈpruːfləs/", "không có bằng chứng, thiếu chứng cứ"),
    ("079575", "proofreads", "verb", "/ˈpruːfˌriːdz/", "đọc soát lỗi bản in, hiệu đính"),
    ("079576", "proofs", "verb", "/pruːfs/", "chống thấm; ủ bột; hiệu đính in thử"),
    ("079577", "propaedeutical", "adj", "/ˌproʊpiˈduːtɪkəl/", "dự bị, nhập môn, bước đầu"),
    ("079578", "propaedeutics", "noun", "/ˌproʊpiˈduːtɪks/", "môn nhập môn, kiến thức dự bị"),
    ("079579", "propagable", "adj", "/ˈprɑːpəɡəbəl/", "có thể nhân giống, truyền bá được"),
    ("079580", "propagandic", "adj", "/ˌprɑːpəˈɡændɪk/", "thuộc về tuyên truyền, cổ động"),
    ("079581", "propagandise", "verb", "/ˌprɑːpəˈɡænˌdaɪz/", "tuyên truyền, cổ động (Anh)"),
    ("079582", "propagandised", "verb", "/ˌprɑːpəˈɡænˌdaɪzd/", "đã tuyên truyền, đã cổ động (Anh)"),
    ("079583", "propagandises", "verb", "/ˌprɑːpəˈɡænˌdaɪzɪz/", "tuyên truyền, cổ động (Anh)"),
    ("079584", "propagandising", "verb", "/ˌprɑːpəˈɡænˌdaɪzɪŋ/", "tuyên truyền, cổ động (Anh)"),
    ("079585", "propagandism", "noun", "/ˌprɑːpəˈɡænˌdɪzəm/", "hoạt động tuyên truyền, cổ động"),
    ("079586", "propagandistically", "adv", "/ˌprɑːpəɡænˈdɪstɪkli/", "theo lối tuyên truyền, cổ động"),
    ("079587", "propagandized", "verb", "/ˌprɑːpəˈɡænˌdaɪzd/", "đã tuyên truyền, đã cổ động"),
    ("079588", "propagandizer", "noun", "/ˌprɑːpəˈɡænˌdaɪzər/", "tuyên truyền viên, người cổ động"),
    ("079589", "propagandizes", "verb", "/ˌprɑːpəˈɡænˌdaɪzɪz/", "tuyên truyền, cổ động tư tưởng"),
    ("079590", "propagandizing", "verb", "/ˌprɑːpəˈɡænˌdaɪzɪŋ/", "tuyên truyền, cổ động tư tưởng"),
    ("079591", "propagated", "verb", "/ˈprɑːpəˌɡeɪtɪd/", "đã nhân giống; đã lan truyền"),
    ("079592", "propagational", "adj", "/ˌprɑːpəˈɡeɪʃənəl/", "thuộc sự nhân giống, sự lan truyền"),
    ("079593", "propagations", "noun", "/ˌprɑːpəˈɡeɪʃənz/", "sự nhân giống; sự truyền sóng"),
    ("079594", "propagative", "adj", "/ˈprɑːpəˌɡeɪtɪv/", "có khả năng nhân giống, lan truyền"),
    ("079595", "propagule", "noun", "/ˈprɑːpəˌɡjuːl/", "chồi mầm sinh sản, cành giâm"),
    ("079596", "propagules", "noun", "/ˈprɑːpəˌɡjuːlz/", "các chồi mầm, đơn vị phát tán"),
    ("079597", "propagulum", "noun", "/proʊˈpæɡjələm/", "chồi mầm sinh sản (thực vật)"),
    ("079598", "propanal", "noun", "/ˈproʊpəˌnæl/", "hợp chất hữu cơ propanal (hóa học)"),
    ("079599", "propanamide", "noun", "/proʊˈpænəˌmaɪd/", "hợp chất propanamide (hóa học)"),
    ("079600", "propanolol", "noun", "/proʊˈprænəˌlɔːl/", "thuốc tim mạch propranolol"),
    ("079601", "propanone", "noun", "/ˈproʊpəˌnoʊn/", "dung môi propanone (axeton)"),
    ("079602", "proparoxytone", "noun", "/ˌproʊpærˈɑːksɪˌtoʊn/", "từ nhấn âm thứ ba từ cuối lên"),
]

raw = json.load(open("scratch/b36_r10_raw_p1.json"))
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
with open("scratch/b36_r10_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b36_r10_p1 saved OK")
