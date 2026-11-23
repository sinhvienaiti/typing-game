import json

records = [
    ("080403", "pulverisation", "noun", "/ˌpʌlvərəˈzeɪʃən/", "sự nghiền nát, sự tán thành bột"),
    ("080404", "pulverises", "verb", "/ˈpʌlvəˌraɪzɪz/", "nghiền nát, tán bột; đánh bại (Anh)"),
    ("080405", "pulverising", "verb", "/ˈpʌlvəˌraɪzɪŋ/", "nghiền nát, tán bột; đánh bại (Anh)"),
    ("080406", "pulverizable", "adj", "/ˈpʌlvəˌraɪzəbəl/", "có thể nghiền nhỏ, tán bột được"),
    ("080407", "pulverizator", "noun", "/ˈpʌlvəˌreɪtər/", "máy phun sương; máy nghiền bột"),
    ("080408", "pulverizer", "noun", "/ˈpʌlvəˌraɪzər/", "máy nghiền bột mịn; bình xịt bụi"),
    ("080409", "pulverizes", "verb", "/ˈpʌlvəˌraɪzɪz/", "nghiền nát thành bột; đánh tan tác"),
    ("080410", "pulverizing", "verb", "/ˈpʌlvəˌraɪzɪŋ/", "nghiền nát thành bột; đánh tan tác"),
    ("080411", "pulverous", "adj", "/ˈpʌlvərəs/", "có dạng bột mịn, vụn như bụi"),
    ("080412", "pulverulence", "noun", "/ˌpʌlvəˈruːləns/", "trạng thái vụn bụi; lớp phấn mịn"),
    ("080413", "pulverulent", "adj", "/ˌpʌlvəˈruːlənt/", "dạng bụi mịn; phủ phấn trắng"),
    ("080414", "pulvillar", "adj", "/pʌlˈvɪlər/", "thuộc đệm bàn chân (côn trùng)"),
    ("080415", "pulvilli", "noun", "/pʌlˈvɪlaɪ/", "các đệm bám chân (côn trùng học)"),
    ("080416", "pulvilliform", "adj", "/pʌlˈvɪləˌfɔːrm/", "có dạng đệm bám chân (côn trùng)"),
    ("080417", "pulvillus", "noun", "/pʌlˈvɪləs/", "đệm bám ở cuối chân côn trùng"),
    ("080418", "pulvinate", "adj", "/ˈpʌlvəˌneɪt/", "hình gối phồng (thực vật học)"),
    ("080419", "pulvinated", "adj", "/ˈpʌlvəˌneɪtɪd/", "có dạng phồng hình gối (cột trụ)"),
    ("080420", "pulvinus", "noun", "/pʌlˈvaɪnəs/", "thể gối cuống lá (thực vật học)"),
    ("080421", "pulviplume", "noun", "/ˈpʌlvəˌpluːm/", "lông phấn (ở chim diệc, vẹt)"),
    ("080422", "pumelo", "noun", "/ˈpʌməloʊ/", "cây bưởi, quả bưởi (biến thể)"),
    ("080423", "pumiceous", "adj", "/pjʊˈmɪʃəs/", "thuộc đá bọt, xốp như đá bọt"),
    ("080424", "pumicer", "noun", "/ˈpʌmɪsər/", "người đánh bóng bằng đá bọt"),
    ("080425", "pumiciform", "adj", "/pjʊˈmɪsəˌfɔːrm/", "có cấu trúc xốp như đá bọt"),
    ("080426", "pummeling", "noun", "/ˈpʌməlɪŋ/", "trận đòn nhừ tử, cú đấm liên tiếp"),
    ("080427", "pummelled", "verb", "/ˈpʌməld/", "đã đấm thùm thụp, đánh liên tiếp"),
    ("080428", "pummelling", "verb", "/ˈpʌməlɪŋ/", "đấm thùm thụp, nện liên tiếp (Anh)"),
    ("080429", "pummelo", "noun", "/ˈpʌməloʊ/", "cây bưởi, quả bưởi (bưởi ta)"),
    ("080430", "pummels", "verb", "/ˈpʌməlz/", "đấm thùm thụp, giáng đòn liên tiếp"),
    ("080431", "pumpability", "noun", "/ˌpʌmpəˈbɪləti/", "khả năng bơm được (chất lỏng)"),
    ("080432", "pumpage", "noun", "/ˈpʌmpɪdʒ/", "lượng chất lỏng bơm được; phí bơm"),
    ("080433", "pumper", "noun", "/ˈpʌmpər/", "xe cứu hỏa bơm nước; công nhân bơm"),
    ("080434", "pumping", "verb", "/ˈpʌmpɪŋ/", "bơm; dò hỏi khéo; đập thình thịch"),
    ("080435", "pumpkins", "noun", "/ˈpʌmpkɪnz/", "những quả bí ngô, quả bí đỏ"),
    ("080436", "pumps", "verb", "/pʌmps/", "bơm (nước, hơi); dò hỏi moi tin"),
    ("080437", "pumpship", "verb", "/ˈpʌmpˌʃɪp/", "tiểu tiện, đi tiểu (lóng hàng hải)"),
    ("080438", "puna", "noun", "/ˈpuːnə/", "cao nguyên lạnh puna; say độ cao"),
    ("080439", "punaluan", "adj", "/ˌpuːnəˈluːən/", "thuộc chế độ quần hôn cổ Hawaii"),
    ("080440", "punchayet", "noun", "/pʌnˈtʃaɪət/", "hội đồng trưởng lão làng (Ấn Độ)"),
    ("080441", "punchball", "noun", "/ˈpʌntʃˌbɔːl/", "bóng đấm tập quyền Anh"),
    ("080442", "punchboard", "noun", "/ˈpʌntʃˌbɔːrd/", "bảng đục lỗ chơi xổ số trúng thưởng"),
    ("080443", "punched", "verb", "/pʌntʃt/", "đã đấm, đã thoi; đã bấm lỗ, đục lỗ"),
    ("080444", "puncheon", "noun", "/ˈpʌntʃən/", "cọc chống; thùng rượu lớn; cái đục"),
    ("080445", "punchers", "noun", "/ˈpʌntʃərz/", "máy đột lỗ; người chăn bò miền Tây"),
    ("080446", "punches", "verb", "/ˈpʌntʃɪz/", "đấm, thoi; bấm lỗ, đột lỗ"),
    ("080447", "punchily", "adv", "/ˈpʌntʃəli/", "một cách mạnh mẽ, súc tích gọn gàng"),
    ("080448", "punchinello", "noun", "/ˌpʌntʃəˈnɛloʊ/", "nhân vật hề Punch; người mập lùn"),
    ("080449", "punchiness", "noun", "/ˈpʌntʃinəs/", "tính mạnh mẽ, súc tích; choáng váng"),
    ("080450", "punching", "verb", "/ˈpʌntʃɪŋ/", "đấm, tung cú đấm; bấm lỗ, đục lỗ"),
    ("080451", "punchless", "adj", "/ˈpʌntʃləs/", "thiếu lực, yếu ớt, kém thuyết phục"),
    ("080452", "punchy", "adj", "/ˈpʌntʃi/", "súc tích, sắc bén; hơi choáng váng"),
    ("080453", "puncta", "noun", "/ˈpʌŋktə/", "các điểm chấm, lỗ nhỏ (giải phẫu)"),
    ("080454", "punctate", "adj", "/ˈpʌŋkteɪt/", "có chấm nhỏ, lấm tấm (sinh học)"),
    ("080455", "punctation", "noun", "/pʌŋkˈteɪʃən/", "sự có đốm chấm nhỏ (sinh học)"),
    ("080456", "punctator", "noun", "/pʌŋkˈteɪtər/", "người chấm thanh âm kinh Do Thái"),
    ("080457", "puncticulate", "adj", "/pʌŋkˈtɪkjəlɪt/", "có chấm cực nhỏ li ti (sinh học)"),
    ("080458", "punctiform", "adj", "/ˈpʌŋktɪˌfɔːrm/", "có dạng chấm nhỏ (vi khuẩn học)"),
    ("080459", "punctilio", "noun", "/pʌŋkˈtɪlioʊ/", "chi tiết cầu kỳ trong nghi thức"),
    ("080460", "punctiliousness", "noun", "/pʌŋkˈtɪliəsnəs/", "tính tỉ mỉ, sự câu nệ nghi thức"),
    ("080461", "punctualities", "noun", "/ˌpʌŋktʃuˈælətiz/", "tính đúng giờ, sự chuẩn giờ"),
    ("080462", "punctuative", "adj", "/ˈpʌŋktʃuətɪv/", "để chấm câu, thuộc dấu chấm câu"),
    ("080463", "punctuator", "noun", "/ˈpʌŋktʃuˌeɪtər/", "người chấm câu; bộ chèn dấu câu"),
    ("080464", "punctule", "noun", "/ˈpʌŋktjuːl/", "chấm nhỏ li ti, lỗ nhỏ (sinh học)"),
    ("080465", "puncturable", "adj", "/ˈpʌŋktʃərəbəl/", "có thể đâm thủng, chọc thủng được"),
    ("080466", "punctureless", "adj", "/ˈpʌŋktʃərləs/", "không bị thủng, chống đâm thủng"),
    ("080467", "punctures", "verb", "/ˈpʌŋktʃərz/", "đâm thủng, chọc thủng; làm xẹp lốp"),
    ("080468", "puncturing", "verb", "/ˈpʌŋktʃərɪŋ/", "đâm thủng, chọc thủng, làm tiêu tan"),
    ("080469", "pundits", "noun", "/ˈpʌndɪts/", "chuyên gia, nhà bình luận uy tín"),
    ("080470", "pungapung", "noun", "/pʊŋɡəˈpʊŋɡ/", "cây khoai nưa (Amorphophallus)"),
    ("080471", "punicaceae", "noun", "/ˌpjuːnɪˈkeɪsiː/", "họ Lựu (thực vật học)"),
    ("080472", "puniceous", "adj", "/pjuːˈnɪʃəs/", "có màu đỏ tía, đỏ thẫm như hạt lựu"),
    ("080473", "punily", "adv", "/ˈpjuːnɪli/", "một cách nhỏ bé, yếu ớt, tầm thường"),
    ("080474", "puniness", "noun", "/ˈpjuːninəs/", "vẻ nhỏ bé yếu ớt, sự tầm thường"),
    ("080475", "punishability", "noun", "/ˌpʌnɪʃəˈbɪləti/", "tính có thể bị trừng phạt (luật)"),
    ("080476", "punisher", "noun", "/ˈpʌnɪʃər/", "người trừng phạt, người trừng trị"),
    ("080477", "punishes", "verb", "/ˈpʌnɪʃɪz/", "trừng phạt, trừng trị; làm hao tổn"),
    ("080478", "punishments", "noun", "/ˈpʌnɪʃmənts/", "các hình phạt, sự trừng phạt"),
    ("080479", "punitiveness", "noun", "/ˈpjuːnətɪvnəs/", "tính chất trừng phạt, nghiêm khắc"),
    ("080480", "punitorily", "adv", "/ˈpjuːnəˌtɔːrəli/", "nhằm mục đích trừng phạt"),
    ("080481", "punitory", "adj", "/ˈpjuːnəˌtɔːri/", "nhằm trừng phạt, mang tính phạt"),
    ("080482", "punka", "noun", "/ˈpʌŋkə/", "quạt trần kéo dây kiểu Ấn Độ"),
    ("080483", "punker", "noun", "/ˈpʌŋkər/", "tín đồ nhạc punk; gỗ mục mồi lửa"),
    ("080484", "punkey", "noun", "/ˈpʌŋki/", "con muỗi mắt đốt buốt (Bắc Mỹ)"),
    ("080485", "punkie", "noun", "/ˈpʌŋki/", "con muỗi mắt, dĩn hút máu"),
    ("080486", "punned", "verb", "/pʌnd/", "đã chơi chữ, đã nói lái"),
    ("080487", "punner", "noun", "/ˈpʌnər/", "người hay chơi chữ; cái đầm đất"),
    ("080488", "punnets", "noun", "/ˈpʌnɪts/", "những rổ nhỏ đựng dâu quả (Anh)"),
    ("080489", "punningly", "adv", "/ˈpʌnɪŋli/", "theo lối chơi chữ, bông đùa"),
    ("080490", "puns", "verb", "/pʌnz/", "chơi chữ, nói lái để gây cười"),
    ("080491", "puntation", "noun", "/pʌnˈteɪʃən/", "tình trạng có các đốm chấm nhỏ"),
    ("080492", "punted", "verb", "/ˈpʌntɪd/", "đã đá bóng sống; đã đẩy sào thuyền"),
    ("080493", "punts", "verb", "/pʌnts/", "đá bóng sống; chống sào đẩy thuyền"),
    ("080494", "pupae", "noun", "/ˈpjuːpiː/", "những con nhộng (côn trùng)"),
    ("080495", "pupated", "verb", "/ˈpjuːpeɪtɪd/", "đã hóa nhộng (sâu bướm)"),
    ("080496", "pupates", "verb", "/ˈpjuːpeɪts/", "hóa nhộng, đóng kén thành nhộng"),
    ("080497", "pupating", "verb", "/ˈpjuːpeɪtɪŋ/", "hóa nhộng, đóng kén thành nhộng"),
    ("080498", "pupation", "noun", "/pjuːˈpeɪʃən/", "quá trình hóa nhộng (côn trùng)"),
    ("080499", "pupiform", "adj", "/ˈpjuːpəˌfɔːrm/", "có hình dạng con nhộng"),
    ("080500", "pupilage", "noun", "/ˈpjuːpəlɪdʒ/", "tuổi vị thành niên; thời học việc"),
    ("080501", "pupilarity", "noun", "/ˌpjuːpəˈlærəti/", "tuổi vị thành niên (luật Scotland)"),
    ("080502", "pupilary", "adj", "/ˈpjuːpəˌlɛri/", "thuộc con ngươi mắt; thuộc học trò"),
]

raw = json.load(open("scratch/b37_r01_raw_p5.json"))
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
with open("scratch/b37_r01_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r01_p5 saved OK")
