import json

rows = [
    ("076103", "philoprogenitive", "adj", "/ˌfɪloʊproʊˈdʒɛnɪtɪv/", "thương yêu con cái; sinh sản nhiều"),
    ("076104", "philoprogenitively", "adv", "/ˌfɪloʊproʊˈdʒɛnɪtɪvli/", "với lòng yêu thương con cái"),
    ("076105", "philoprogenitiveness", "noun", "/ˌfɪloʊproʊˈdʒɛnɪtɪvnəs/", "bản năng yêu con; tính sinh nhiều"),
    ("076106", "philosophies", "noun", "/fɪˈlɒsəfiz/", "triết học; các học thuyết triết lý"),
    ("076107", "philosophised", "verb", "/fɪˈlɒsəfaɪzd/", "đã triết lý, luận bàn triết học"),
    ("076108", "philosophiser", "noun", "/fɪˈlɒsəfaɪzər/", "người hay triết lý suông"),
    ("076109", "philosophises", "verb", "/fɪˈlɒsəfaɪzɪz/", "triết lý, luận bàn triết học"),
    ("076110", "philosophising", "verb", "/fɪˈlɒsəfaɪzɪŋ/", "triết lý, luận bàn triết học"),
    ("076111", "philosophism", "noun", "/fɪˈlɒsəfɪzəm/", "triết lý rởm, ngụy biện triết học"),
    ("076112", "philosophist", "noun", "/fɪˈlɒsəfɪst/", "nhà triết học giả hiệu, ngụy biện"),
    ("076113", "philosophized", "verb", "/fɪˈlɒsəfaɪzd/", "đã triết lý, luận bàn triết học"),
    ("076114", "philosophizer", "noun", "/fɪˈlɒsəfaɪzər/", "người hay triết lý suông"),
    ("076115", "philosophizes", "verb", "/fɪˈlɒsəfaɪzɪz/", "triết lý, luận bàn triết học"),
    ("076116", "philotechnic", "adj", "/ˌfɪloʊˈtɛknɪk/", "yêu thích kỹ thuật và thủ công"),
    ("076117", "philotechnical", "adj", "/ˌfɪloʊˈtɛknɪkəl/", "yêu thích kỹ thuật và thủ công"),
    ("076118", "philotherm", "noun", "/ˈfɪləθɜːrm/", "thực vật ưa nhiệt (nhiệt đới)"),
    ("076119", "philtrum", "noun", "/ˈfɪltrəm/", "rãnh nhân trung (giữa mũi và môi)"),
    ("076120", "phimoses", "noun", "/faɪˈmoʊsiːz/", "chứng hẹp bao quy đầu (y học)"),
    ("076121", "phintias", "noun", "/ˈfɪntiəs/", "nhân vật Phintias (Hy Lạp cổ)"),
    ("076122", "phishing", "noun", "/ˈfɪʃɪŋ/", "lừa đảo giả mạo đánh cắp dữ liệu"),
    ("076123", "phlebectomy", "noun", "/flɪˈbɛktəmi/", "phẫu thuật cắt bỏ giãn tĩnh mạch"),
    ("076124", "phlebitic", "adj", "/flɪˈbɪtɪk/", "bị viêm tĩnh mạch (y học)"),
    ("076125", "phlebodium", "noun", "/flɪˈboʊdiəm/", "chi dương xỉ rễ thỏ Phlebodium"),
    ("076126", "phlebogram", "noun", "/ˈflɛbəɡræm/", "đồ thị mạch tĩnh mạch (y học)"),
    ("076127", "phlebographic", "adj", "/ˌflɛbəˈɡræfɪk/", "thuộc chụp X-quang tĩnh mạch"),
    ("076128", "phlebography", "noun", "/flɪˈbɒɡrəfi/", "chụp X-quang tĩnh mạch (y học)"),
    ("076129", "phlebology", "noun", "/flɪˈbɒlədʒi/", "tĩnh mạch học (chuyên khoa y học)"),
    ("076130", "phlebosclerosic", "noun", "/ˌflɛboʊsklɪˈrɒsɪk/", "chứng xơ cứng thành tĩnh mạch"),
    ("076131", "phlebosclerotic", "adj", "/ˌflɛboʊskləˈrɒtɪk/", "thuộc chứng xơ cứng tĩnh mạch"),
    ("076132", "phlebothrombosis", "noun", "/ˌflɛboʊθrɒmˈboʊsɪs/", "huyết khối tĩnh mạch (y học)"),
    ("076133", "phlebotomic", "adj", "/ˌflɛbəˈtɒmɪk/", "thuộc thủ thuật trích máu tĩnh mạch"),
    ("076134", "phlebotomise", "verb", "/flɪˈbɒtəmaɪz/", "lấy máu tĩnh mạch; trích máu"),
    ("076135", "phlebotomize", "verb", "/flɪˈbɒtəmaɪz/", "lấy máu tĩnh mạch; trích máu"),
    ("076136", "phlebotomus", "noun", "/flɪˈbɒtəməs/", "chi muỗi cát truyền bệnh leishmania"),
    ("076137", "phlegmatical", "adj", "/flɛɡˈmætɪkəl/", "lãnh đạm, điềm tĩnh, thờ ơ"),
    ("076138", "phlegmatically", "adv", "/flɛɡˈmætɪkli/", "một cách lãnh đạm, điềm tĩnh"),
    ("076139", "phlegmon", "noun", "/ˈflɛɡmɒn/", "viêm tấy mô liên kết (y học)"),
    ("076140", "phlegmonic", "adj", "/flɛɡˈmɒnɪk/", "thuộc viêm tấy mô liên kết"),
    ("076141", "phlegmonous", "adj", "/ˈflɛɡmənəs/", "thuộc viêm tấy mô liên kết"),
    ("076142", "phleum", "noun", "/ˈfliːəm/", "chi cỏ đuôi mèo Phleum (Timothy)"),
    ("076143", "phloeodic", "adj", "/fliˈɒdɪk/", "có dạng mô bần, giống vỏ cây"),
    ("076144", "phloeum", "noun", "/ˈfliːəm/", "mô mạch rây (libe, thực vật học)"),
    ("076145", "phlogistic", "adj", "/floʊˈdʒɪstɪk/", "gây viêm; thuộc thuyết phlogiston"),
    ("076146", "phloic", "adj", "/ˈfloʊɪk/", "thuộc mạch rây, vỏ cây (libe)"),
    ("076147", "phlomis", "noun", "/ˈfloʊmɪs/", "chi cây hoa tai lừa (Phlomis)"),
    ("076148", "phlozirin", "noun", "/ˈfloʊzɪrɪn/", "chất đắng phlorizin (vỏ rễ táo)"),
    ("076149", "phlyctena", "noun", "/flɪkˈtiːnə/", "nốt phồng nước nhỏ (y học)"),
    ("076150", "phlyctenule", "noun", "/flɪkˈtɛnjuːl/", "nốt phồng rộp nhỏ trên kết mạc"),
    ("076151", "pho", "noun", "/foʊ/", "món phở (Việt Nam)"),
    ("076152", "phoanatory", "adj", "/ˈfoʊnətɔːri/", "thuộc sự phát âm (biến thể cũ)"),
    ("076153", "phobantropy", "noun", "/ˌfoʊbænˈθrɒpi/", "chứng sợ người, sợ đám đông"),
    ("076154", "phobophobia", "noun", "/ˌfoʊbəˈfoʊbiə/", "chứng sợ chính nỗi sợ hãi (tâm lý)"),
    ("076155", "phocidae", "noun", "/ˈfoʊsɪdiː/", "họ Hải cẩu thật (không tai ngoài)"),
    ("076156", "phocine", "adj", "/ˈfoʊsaɪn/", "thuộc loài hải cẩu"),
    ("076157", "phocomelia", "noun", "/ˌfɒkəˈmiːliə/", "dị tật chi ngắn như vây hải cẩu"),
    ("076158", "phoenicophorium", "noun", "/ˌfiːnɪkəˈfɔːriəm/", "cọ gai Seychelles (Phoenicophorium)"),
    ("076159", "phoenicopteridae", "noun", "/ˌfiːnɪkɒpˈtɛrɪdiː/", "họ Chim hồng hạc (Phoenicopteridae)"),
    ("076160", "phoeniculidae", "noun", "/ˌfiːnɪˈkjuːlɪdiː/", "họ Chim đầu rìu gỗ (Phoeniculidae)"),
    ("076161", "phoeniculus", "noun", "/fiˈnɪkjələs/", "chi chim đầu rìu gỗ (Phoeniculus)"),
    ("076162", "phoenicurus", "noun", "/ˌfiːnɪˈkjʊrəs/", "chi chim đuôi đỏ (Phoenicurus)"),
    ("076163", "pholadidae", "noun", "/foʊˈlædɪdiː/", "họ Ngao đục đá (Pholadidae)"),
    ("076164", "pholas", "noun", "/ˈfoʊləs/", "chi ngao đục đá (Pholas)"),
    ("076165", "pholidae", "noun", "/ˈfɒlɪdiː/", "họ Cá chạch biển gunnel (Pholidae)"),
    ("076166", "pholidota", "noun", "/ˌfɒlɪˈdoʊtə/", "bộ Tê tê; chi phong lan Pholidota"),
    ("076167", "pholiota", "noun", "/ˌfoʊliˈoʊtə/", "chi nấm trân châu gỗ (Pholiota)"),
    ("076168", "pholis", "noun", "/ˈfoʊlɪs/", "chi cá chạch biển gunnel (Pholis)"),
    ("076169", "pholistoma", "noun", "/ˌfoʊlɪˈstoʊmə/", "chi hoa ngũ tinh thảo Pholistoma"),
    ("076170", "phonascetics", "noun", "/ˌfoʊnəˈsɛtɪks/", "nghệ thuật luyện giọng hát, nói"),
    ("076171", "phonate", "verb", "/ˈfoʊneɪt/", "phát âm hữu thanh (thanh quản)"),
    ("076172", "phonatory", "adj", "/ˈfoʊnətɔːri/", "thuộc sự phát âm (cơ quan phát âm)"),
    ("076173", "phonautograph", "noun", "/foʊˈnɔːtəɡræf/", "máy ghi rung động sóng âm cổ"),
    ("076174", "phoned", "verb", "/foʊnd/", "đã gọi điện thoại"),
    ("076175", "phoneidoscope", "noun", "/foʊˈnaɪdəskoʊp/", "dụng cụ hiện hình sóng âm cổ"),
    ("076176", "phonematic", "adj", "/ˌfoʊnɪˈmætɪk/", "thuộc âm vị học"),
    ("076177", "phonemicist", "noun", "/fəˈniːmɪsɪst/", "nhà âm vị học"),
    ("076178", "phonemics", "noun", "/fəˈniːmɪks/", "âm vị học (ngôn ngữ học)"),
    ("076179", "phonendoscope", "noun", "/foʊˈnɛndəskoʊp/", "ống nghe khuếch đại âm cơ thể"),
    ("076180", "phones", "verb", "/foʊnz/", "gọi điện thoại"),
    ("076181", "phonetical", "adj", "/fəˈnɛtɪkəl/", "thuộc ngữ âm học"),
    ("076182", "phonetician", "noun", "/ˌfɒnɪˈtɪʃən/", "nhà ngữ âm học"),
    ("076183", "phoneticist", "noun", "/fəˈnɛtɪsɪst/", "nhà ngữ âm học"),
    ("076184", "phoneticize", "verb", "/fəˈnɛtɪsaɪz/", "phiên âm theo ngữ âm học"),
    ("076185", "phonetist", "noun", "/ˈfoʊnɪtɪst/", "nhà ngữ âm học"),
    ("076186", "phonically", "adv", "/ˈfɒnɪkli/", "theo cách phát âm, âm thanh"),
    ("076187", "phonily", "adv", "/ˈfoʊnɪli/", "một cách giả tạo, giả dối"),
    ("076188", "phoniness", "noun", "/ˈfoʊninəs/", "sự giả tạo, đồ giả dỏm"),
    ("076189", "phoning", "verb", "/ˈfoʊnɪŋ/", "gọi điện thoại"),
    ("076190", "phonofilm", "noun", "/ˈfoʊnəfɪlm/", "phim điện ảnh có âm thanh cổ"),
    ("076191", "phonogramic", "adj", "/ˌfoʊnəˈɡræmɪk/", "thuộc ký hiệu ghi âm, ghi âm lời"),
    ("076192", "phonogramically", "adv", "/ˌfoʊnəˈɡræmɪkli/", "theo cách ký hiệu ghi âm"),
    ("076193", "phonogrammic", "adj", "/ˌfoʊnəˈɡræmɪk/", "thuộc ký hiệu ghi âm"),
    ("076194", "phonogrammically", "adv", "/ˌfoʊnəˈɡræmɪkli/", "theo cách ký hiệu ghi âm"),
    ("076195", "phonographer", "noun", "/fəˈnɒɡrəfər/", "người viết tốc ký ngữ âm; ghi âm"),
    ("076196", "phonographic", "adj", "/ˌfoʊnəˈɡræfɪk/", "thuộc máy hát đĩa; tốc ký âm"),
    ("076197", "phonographically", "adv", "/ˌfoʊnəˈɡræfɪkli/", "bằng máy ghi âm; theo tốc ký âm"),
    ("076198", "phonographist", "noun", "/fəˈnɒɡrəfɪst/", "người viết tốc ký ngữ âm"),
    ("076199", "phonography", "noun", "/fəˈnɒɡrəfi/", "phép tốc ký âm; kỹ thuật ghi âm"),
    ("076200", "phonolite", "noun", "/ˈfoʊnəlaɪt/", "đá phún xuất phonolit (địa chất)"),
    ("076201", "phonolitic", "adj", "/ˌfoʊnəˈlɪtɪk/", "thuộc đá phonolit (địa chất)"),
    ("076202", "phonologic", "adj", "/ˌfɒnəˈlɒdʒɪk/", "thuộc âm vị học"),
]

with open("scratch/b36_r03_raw_p2.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r03_p2.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r03_p2 saved OK")
