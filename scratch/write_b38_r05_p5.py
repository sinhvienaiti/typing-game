import json

RECORDS = [
    ("087403", "slaughterous", "adj", "/ˈslɔːtərəs/", "đẫm máu; khát máu tàn sát"),
    ("087404", "slaughterously", "adv", "/ˈslɔːtərəsli/", "tàn khốc đẫm máu"),
    ("087405", "slaughters", "verb", "/ˈslɔːtərz/", "giết mổ; tàn sát; đánh bại thảm"),
    ("087406", "slaved", "verb", "/sleɪvd/", "đã làm việc quần quật như nô lệ"),
    ("087407", "slaveless", "adj", "/ˈsleɪvləs/", "không có nô lệ"),
    ("087408", "slavelike", "adj", "/ˈsleɪvˌlaɪk/", "khúm núm hèn hạ như nô lệ"),
    ("087409", "slavered", "verb", "/ˈslævərd/", "đã chảy nước dãi; đã nịnh bợ"),
    ("087410", "slaverer", "noun", "/ˈslævərər/", "người hay chảy dãi; kẻ nịnh bợ"),
    ("087411", "slavering", "verb", "/ˈslævərɪŋ/", "đang chảy nước dãi; đang nịnh hót"),
    ("087412", "slavers", "verb", "/ˈslævərz/", "chảy nước dãi; thèm nhỏ dãi"),
    ("087413", "slaves", "verb", "/sleɪvz/", "làm lụng cật lực như nô lệ"),
    ("087414", "slavicist", "noun", "/ˈslɑːvɪsɪst/", "học giả ngôn ngữ văn học Slav"),
    ("087415", "slaving", "verb", "/ˈsleɪvɪŋ/", "đang làm việc quần quật vất vả"),
    ("087416", "slavishness", "noun", "/ˈsleɪvɪʃnəs/", "tính nô lệ; thói bắt chước mù quáng"[:35]),
    ("087417", "slavism", "noun", "/ˈslɑːvɪzəm/", "tinh thần liên kết các dân tộc Slav"[:35]),
    ("087418", "slavocracy", "noun", "/sleɪˈvɑːkrəsi/", "tầng lớp chủ nô cầm quyền"),
    ("087419", "slavonian", "adj", "/sləˈvoʊniən/", "thuộc vùng Slavonia (Croatia)"),
    ("087420", "slavonise", "verb", "/ˈslævəˌnaɪz/", "Slav hóa"),
    ("087421", "slavonize", "verb", "/ˈslævəˌnaɪz/", "Slav hóa"),
    ("087422", "slavophil", "adj", "/ˈslævəˌfaɪl/", "thân các dân tộc Slav"),
    ("087423", "slavophile", "adj", "/ˈslævəˌfaɪl/", "thân và ngưỡng mộ văn hóa Slav"),
    ("087424", "slavophobe", "adj", "/ˈslævəˌfoʊb/", "bài xích người Slav"),
    ("087425", "slayers", "noun", "/ˈsleɪərz/", "kẻ sát nhân; người tiêu diệt"),
    ("087426", "slbm", "noun", "/ˌɛsˌɛlˌbiːˈɛm/", "tên lửa đạn đạo phóng từ tàu ngầm"),
    ("087427", "sld", "noun", "/ˌɛsˌɛlˈdiː/", "Đảng Tự do Dân chủ Xã hội"),
    ("087428", "sleazily", "adv", "/ˈsliːzɪli/", "nhớp nhúa; đê tiện; tồi tàn"),
    ("087429", "sledded", "verb", "/ˈslɛdɪd/", "đã đi xe trượt tuyết; chở xe trượt"[:35]),
    ("087430", "sledder", "noun", "/ˈslɛdər/", "người lái xe trượt tuyết"),
    ("087431", "sledged", "verb", "/slɛdʒd/", "đã đi xe trượt tuyết; chế giễu"),
    ("087432", "sledges", "verb", "/ˈslɛdʒɪz/", "trượt tuyết; nói kháy chọc tức"),
    ("087433", "sledging", "verb", "/ˈslɛdʒɪŋ/", "đang trượt tuyết; khiêu khích"),
    ("087434", "sleds", "verb", "/slɛdz/", "đi xe trượt tuyết; chở bằng xe trượt"[:35]),
    ("087435", "sleeker", "noun", "/ˈsliːkər/", "dụng cụ vuốt láng da hay khuôn đúc"[:35]),
    ("087436", "sleekily", "adv", "/ˈsliːkɪli/", "bóng mượt; khéo léo trơn tru"),
    ("087437", "sleeking", "verb", "/ˈsliːkɪŋ/", "đang vuốt cho bóng mượt"),
    ("087438", "sleeks", "verb", "/sliːks/", "vuốt cho bóng mượt"),
    ("087439", "sleeky", "adj", "/ˈsliːki/", "bóng mượt; khéo nịnh bợ ngọt xớt"),
    ("087440", "sleeplessly", "adv", "/ˈsliːpləsli/", "trằn trọc mất ngủ; không ngừng nghỉ"[:35]),
    ("087441", "sleepyheaded", "adj", "/ˈsliːpiˌhɛdɪd/", "ngái ngủ; hay buồn ngủ lờ đờ"),
    ("087442", "sleeted", "verb", "/ˈsliːtɪd/", "đã đổ mưa tuyết lẫn đá"),
    ("087443", "sleetiness", "noun", "/ˈsliːtinəs/", "tình trạng mưa tuyết ẩm ướt"),
    ("087444", "sleeting", "verb", "/ˈsliːtɪŋ/", "đang đổ mưa tuyết lẫn đá"),
    ("087445", "sleets", "verb", "/sliːts/", "đổ mưa tuyết lẫn mưa đá"),
    ("087446", "sleeves", "noun", "/sliːvz/", "tay áo; bìa đĩa nhạc; ống lót"),
    ("087447", "sleeving", "noun", "/ˈsliːvɪŋ/", "ống bọc cách điện; ống lót"),
    ("087448", "sleighed", "verb", "/sleɪd/", "đã đi xe trượt tuyết ngựa kéo"),
    ("087449", "sleighing", "verb", "/ˈsleɪɪŋ/", "đang đi xe trượt tuyết ngựa kéo"),
    ("087450", "sleighings", "noun", "/ˈsleɪɪŋz/", "chuyến đi chơi xe trượt tuyết"),
    ("087451", "sleighs", "verb", "/sleɪz/", "đi xe trượt tuyết ngựa kéo"),
    ("087452", "sleights", "noun", "/slaɪts/", "trò ảo thuật khéo tay; mánh khóe"),
    ("087453", "slenderise", "verb", "/ˈslɛndəˌraɪz/", "làm cho thon gọn mảnh mai"),
    ("087454", "slenderised", "verb", "/ˈslɛndəˌraɪzd/", "đã làm thon gọn mảnh mai"),
    ("087455", "slenderises", "verb", "/ˈslɛndəˌraɪzɪz/", "làm cho thon gọn mảnh mai"),
    ("087456", "slenderising", "verb", "/ˈslɛndəˌraɪzɪŋ/", "đang làm thon gọn mảnh mai"),
    ("087457", "slenderize", "verb", "/ˈslɛndəˌraɪz/", "làm cho thon gọn mảnh mai"),
    ("087458", "slenderized", "verb", "/ˈslɛndəˌraɪzd/", "đã làm thon gọn mảnh mai"),
    ("087459", "slenderizes", "verb", "/ˈslɛndəˌraɪzɪz/", "làm cho thon gọn mảnh mai"),
    ("087460", "slenderizing", "verb", "/ˈslɛndəˌraɪzɪŋ/", "đang làm thon gọn mảnh mai"),
    ("087461", "slept", "verb", "/slɛpt/", "đã ngủ"),
    ("087462", "sleuthhound", "noun", "/ˈsluːθˌhaʊnd/", "chó săn tìm dấu vết; thám tử"),
    ("087463", "slewness", "noun", "/ˈsluːnəs/", "độ nghiêng lệch; tình trạng xoay xéo"[:35]),
    ("087464", "slezsko", "noun", "/ˈslɛskoʊ/", "vùng Silesia (tiếng Séc)"),
    ("087465", "slices", "verb", "/ˈslaɪsɪz/", "cắt lát mỏng; đánh bóng xoáy lệch"),
    ("087466", "slickenside", "noun", "/ˈslɪkənˌsaɪd/", "mặt trượt đứt gãy nhẵn bóng"),
    ("087467", "slickensided", "adj", "/ˈslɪkənˌsaɪdɪd/", "có mặt trượt địa chất nhẵn bóng"),
    ("087468", "slicking", "verb", "/ˈslɪkɪŋ/", "đang vuốt bóng; đang làm trơn tru"),
    ("087469", "slicks", "verb", "/slɪks/", "vuốt bóng mượt; làm trơn láng"),
    ("087470", "slid", "verb", "/slɪd/", "đã trượt; đã lướt nhẹ"),
    ("087471", "slides", "verb", "/slaɪdz/", "trượt; lướt nhẹ; tụt xuống"),
    ("087472", "slideway", "noun", "/ˈslaɪdˌweɪ/", "đường trượt dẫn hướng máy móc"),
    ("087473", "slighted", "verb", "/ˈslaɪtɪd/", "đã coi thường; đã hắt hủi lạnh nhạt"[:35]),
    ("087474", "slightingly", "adv", "/ˈslaɪtɪŋli/", "với vẻ khinh thường lạnh nhạt"),
    ("087475", "slights", "verb", "/slaɪts/", "coi thường; hắt hủi; phá pháo đài"),
    ("087476", "slily", "adv", "/ˈslaɪli/", "ranh mãnh; kín đáo tinh ranh"),
    ("087477", "sliminess", "noun", "/ˈslaɪminəs/", "tính nhầy nhụa nhớp nháp; sự nịnh"),
    ("087478", "slimly", "adv", "/ˈslɪmli/", "mảnh khảnh thon thả; ít ỏi mong manh"[:35]),
    ("087479", "slimmed", "verb", "/slɪmd/", "đã giảm cân cho thon gọn"),
    ("087480", "slimmer", "noun", "/ˈslɪmər/", "người đang ăn kiêng giảm cân"),
    ("087481", "slimming", "verb", "/ˈslɪmɪŋ/", "đang ăn kiêng giảm cân cho gọn"),
    ("087482", "slimmish", "adj", "/ˈslɪmɪʃ/", "hơi mảnh khảnh; hơi gầy gầy"),
    ("087483", "slims", "verb", "/slɪmz/", "làm thon gọn; ăn kiêng giảm cân"),
    ("087484", "slimsy", "adj", "/ˈslɪmzi/", "mỏng manh; ọp ẹp kém bền"),
    ("087485", "slingbacks", "noun", "/ˈslɪŋˌbæks/", "giày hở gót có quai hậu"),
    ("087486", "slings", "noun", "/slɪŋz/", "ná thun; dây treo băng bó tay"),
    ("087487", "slingshots", "noun", "/ˈslɪŋˌʃɑːts/", "ná cao su bắn đạn"),
    ("087488", "slinkily", "adv", "/ˈslɪŋkɪli/", "uyển chuyển lén lút; bó sát gợi cảm"[:35]),
    ("087489", "slinkiness", "noun", "/ˈslɪŋkinəs/", "dáng vẻ uyển chuyển bó sát"),
    ("087490", "slinky", "adj", "/ˈslɪŋki/", "uyển chuyển lả lướt; ôm sát người"),
    ("087491", "slinkys", "noun", "/ˈslɪŋkiz/", "đồ chơi lò xo Slinky"),
    ("087492", "slipover", "noun", "/ˈslɪpˌoʊvər/", "áo len chui đầu không cúc"),
    ("087493", "slipped", "verb", "/slɪpt/", "đã trượt chân; đã lẻn đi; đã tuột"),
    ("087494", "slipperily", "adv", "/ˈslɪpərɪli/", "trơn trượt; khôn lỏi khó nắm bắt"),
    ("087495", "slippering", "noun", "/ˈslɪpərɪŋ/", "trận đòn đánh bằng dép"),
    ("087496", "slipperings", "noun", "/ˈslɪpərɪŋz/", "trận đòn đánh bằng dép"),
    ("087497", "slipperwort", "noun", "/ˈslɪpərˌwɜːrt/", "cây hoa hài tiên Calceolaria"),
    ("087498", "slips", "verb", "/slɪps/", "trượt chân; lẻn đi; lỡ lời"),
    ("087499", "slipsheet", "noun", "/ˈslɪpˌʃiːt/", "tờ giấy lót chống lem mực in"),
    ("087500", "slipshoe", "noun", "/ˈslɪpˌʃuː/", "dép lê; giày sục dễ xỏ"),
    ("087501", "slipslop", "noun", "/ˈslɪpˌslɑːp/", "chuyện nhạt nhẽo; văn phong cẩu thả"[:35]),
    ("087502", "slipstick", "noun", "/ˈslɪpˌstɪk/", "thước tính lô-ga (lóng)"),
]

# Remove all slices cleanly <= 35 chars
RECORDS[13] = ("087416", "slavishness", "noun", "/ˈsleɪvɪʃnəs/", "tính nô lệ; sự bắt chước mù quáng")
RECORDS[14] = ("087417", "slavism", "noun", "/ˈslɑːvɪzəm/", "chủ nghĩa liên kết các dân tộc Slav"[:35])
RECORDS[14] = ("087417", "slavism", "noun", "/ˈslɑːvɪzəm/", "chủ nghĩa liên Slav")
RECORDS[26] = ("087429", "sledded", "verb", "/ˈslɛdɪd/", "đã đi xe trượt tuyết")
RECORDS[31] = ("087434", "sleds", "verb", "/slɛdz/", "đi xe trượt tuyết")
RECORDS[32] = ("087435", "sleeker", "noun", "/ˈsliːkər/", "dụng cụ vuốt láng da thuộc")
RECORDS[37] = ("087440", "sleeplessly", "adv", "/ˈsliːpləsli/", "trằn trọc mất ngủ; không ngừng")
RECORDS[60] = ("087463", "slewness", "noun", "/ˈsluːnəs/", "độ nghiêng lệch; độ xoay xéo")
RECORDS[70] = ("087473", "slighted", "verb", "/ˈslaɪtɪd/", "đã coi thường; đã hắt hủi lạnh nhạt"[:35])
RECORDS[70] = ("087473", "slighted", "verb", "/ˈslaɪtɪd/", "đã coi thường; đã hắt hủi")
RECORDS[75] = ("087478", "slimly", "adv", "/ˈslɪmli/", "mảnh khảnh thon thả; ít ỏi")
RECORDS[85] = ("087488", "slinkily", "adv", "/ˈslɪŋkɪli/", "uyển chuyển lả lướt; bó sát người")
RECORDS[98] = ("087501", "slipslop", "noun", "/ˈslɪpˌslɑːp/", "chuyện nhạt nhẽo; văn cẩu thả")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r05_raw_p5.json"))
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

json.dump(out, open("scratch/b38_r05_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b38_r05_p5 saved OK")
