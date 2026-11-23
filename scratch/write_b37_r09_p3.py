import json

RECORDS = [
    ("084203", "rowelled", "verb", "/ˈraʊəld/", "đã thúc cựa ngựa bánh xe"),
    ("084204", "rowelling", "verb", "/ˈraʊəlɪŋ/", "đang thúc cựa ngựa bánh xe"),
    ("084205", "rowels", "verb", "/ˈraʊəlz/", "thúc cựa ngựa bánh xe"),
    ("084206", "rowlock", "noun", "/ˈrɑːlək/", "cọc chèo; móc giữ mái chèo"),
    ("084207", "rows", "verb", "/roʊz/", "chèo thuyền; cãi cọ"),
    ("084208", "royalistic", "adj", "/ˌrɔɪəˈlɪstɪk/", "theo phái bảo hoàng"),
    ("084209", "royalists", "noun", "/ˈrɔɪəlɪsts/", "người theo phái bảo hoàng"),
    ("084210", "royalties", "noun", "/ˈrɔɪəltiz/", "tiền bản quyền; hoàng tộc"),
    ("084211", "royer", "noun", "/ˈrɔɪər/", "máy đánh tơi cát đúc"),
    ("084212", "roystonea", "noun", "/ˌrɔɪˈstoʊniə/", "chi Cau vua (Roystonea)"),
    ("084213", "rozzer", "noun", "/ˈrɑːzər/", "cảnh sát (từ lóng Anh)"),
    ("084214", "rp", "noun", "/ˌɑːrˈpiː/", "giọng Anh chuẩn (RP)"),
    ("084215", "rpi", "noun", "/ˌɑːrˌpiːˈaɪ/", "chỉ số giá bán lẻ (RPI)"),
    ("084216", "rrp", "noun", "/ˌɑːrˌɑːrˈpiː/", "giá bán lẻ đề xuất"),
    ("084217", "rsa", "noun", "/ˌɑːrˌɛsˈeɪ/", "Cộng hòa Nam Phi; thuật toán RSA"),
    ("084218", "rsc", "noun", "/ˌɑːrˌɛsˈsiː/", "Đoàn kịch Hoàng gia Shakespeare"),
    ("084219", "rsm", "noun", "/ˌɑːrˌɛsˈɛm/", "thượng sĩ nhất trung đoàn"),
    ("084220", "rspb", "noun", "/ˌɑːrˌɛsˌpiːˈbiː/", "Hội Hoàng gia Bảo vệ Chim"),
    ("084221", "rspca", "noun", "/ˌɑːrˌɛsˌpiːˌsiːˈeɪ/", "Hội Bảo vệ Động vật Hoàng gia"),
    ("084222", "rsv", "noun", "/ˌɑːrˌɛsˈviː/", "virus hợp bào hô hấp (RSV)"),
    ("084223", "rtlt", "noun", "/ˌɑːrˌtiːˌɛlˈtiː/", "độ trễ khứ hồi tín hiệu"),
    ("084224", "ruandan", "adj", "/ruˈɑːndən/", "thuộc nước Rwanda"),
    ("084225", "rubaiyat", "noun", "/ˌruːbaɪˈjɑːt/", "thể thơ tứ tuyệt Ba Tư"),
    ("084226", "rubasse", "noun", "/ruːˈbæs/", "thạch anh nhuộm đỏ hồng ngọc"),
    ("084227", "rubbed", "verb", "/rʌbd/", "đã chà xát; đã xoa bóp"),
    ("084228", "rubberise", "verb", "/ˈrʌbəˌraɪz/", "tráng cao su; bọc cao su"),
    ("084229", "rubberised", "verb", "/ˈrʌbəˌraɪzd/", "đã tráng cao su; đã bọc cao su"),
    ("084230", "rubberises", "verb", "/ˈrʌbəˌraɪzɪz/", "tráng cao su; bọc cao su"),
    ("084231", "rubberising", "verb", "/ˈrʌbəˌraɪzɪŋ/", "đang tráng cao su; đang bọc cao su"),
    ("084232", "rubberize", "verb", "/ˈrʌbəˌraɪz/", "tráng cao su; bọc cao su"),
    ("084233", "rubberized", "verb", "/ˈrʌbəˌraɪzd/", "đã tráng cao su; đã bọc cao su"),
    ("084234", "rubberizes", "verb", "/ˈrʌbəˌraɪzɪz/", "tráng cao su; bọc cao su"),
    ("084235", "rubberizing", "verb", "/ˈrʌbəˌraɪzɪŋ/", "đang tráng cao su; đang bọc cao su"),
    ("084236", "rubberlike", "adj", "/ˈrʌbərˌlaɪk/", "giống cao su; đàn hồi như cao su"),
    ("084237", "rubbernecker", "noun", "/ˈrʌbərˌnɛkər/", "kẻ tò mò nghển cổ nhìn ngó"),
    ("084238", "rubbly", "adj", "/ˈrʌbli/", "đầy gạch đá vụn; lởm chởm đá"),
    ("084239", "rubefacient", "noun", "/ˌruːbɪˈfeɪʃənt/", "thuốc bôi làm đỏ da giảm đau"),
    ("084240", "rubefaction", "noun", "/ˌruːbɪˈfækʃən/", "sự sung huyết làm đỏ da"),
    ("084241", "rubefy", "verb", "/ˈruːbəˌfaɪ/", "làm đỏ da; gây sung huyết da"),
    ("084242", "rubescent", "adj", "/ruːˈbɛsənt/", "ửng đỏ; trở nên đỏ"),
    ("084243", "rubiaceous", "adj", "/ˌruːbiˈeɪʃəs/", "thuộc họ Cà phê (Rubiaceae)"),
    ("084244", "rubican", "adj", "/ˈruːbɪkən/", "có lông nâu lốm đốm trắng (ngựa)"),
    ("084245", "rubicelle", "noun", "/ˈruːbɪˌsɛl/", "đá quý spinel màu vàng cam đỏ"),
    ("084246", "rubicundity", "noun", "/ˌruːbɪˈkʌndɪti/", "vẻ hồng hào đỏ đắn"),
    ("084247", "rubied", "adj", "/ˈruːbid/", "đỏ thắm như hồng ngọc"),
    ("084248", "rubies", "noun", "/ˈruːbiz/", "đá hồng ngọc; ngọc rubi"),
    ("084249", "rubify", "verb", "/ˈruːbəˌfaɪ/", "nhuộm đỏ thắm như hồng ngọc"),
    ("084250", "rubiginous", "adj", "/ruːˈbɪdʒənəs/", "có màu gỉ sắt; màu nâu đỏ"),
    ("084251", "rubious", "adj", "/ˈruːbiəs/", "có màu đỏ thắm như hồng ngọc"),
    ("084252", "rubor", "noun", "/ˈruːbɔːr/", "sự ửng đỏ vùng viêm"),
    ("084253", "rubricate", "verb", "/ˈruːbrɪˌkeɪt/", "viết mực đỏ; sắp xếp đề mục"),
    ("084254", "rubrician", "noun", "/ruːˈbrɪʃən/", "học giả am hiểu nghi lễ phụng vụ"),
    ("084255", "rubricist", "noun", "/ˈruːbrɪsɪst/", "người am hiểu quy định phụng vụ"),
    ("084256", "rubs", "verb", "/rʌbz/", "chà xát; xoa bóp; cọ vào"),
    ("084257", "rubying", "verb", "/ˈruːbiɪŋ/", "đang nhuộm đỏ hồng ngọc"),
    ("084258", "ruc", "noun", "/ˌɑːrˌjuːˈsiː/", "Sở Cảnh sát Hoàng gia Ulster"),
    ("084259", "rucervus", "noun", "/ruːˈsɜːrvəs/", "chi Hươu đầm lầy Rucervus"),
    ("084260", "ruche", "noun", "/ruːʃ/", "dải vải xếp nếp trang trí"),
    ("084261", "ruched", "adj", "/ruːʃt/", "có xếp nếp bèo nhún"),
    ("084262", "ruching", "noun", "/ˈruːʃɪŋ/", "dải trang trí xếp nếp nhún"),
    ("084263", "rucked", "verb", "/rʌkt/", "đã nhăn dúm; đã tụ tập thành đám"),
    ("084264", "rucking", "verb", "/ˈrʌkɪŋ/", "đang nhăn dúm; đang xô đẩy"),
    ("084265", "rucks", "verb", "/rʌks/", "làm nhăn dúm; xô đẩy tranh bóng"),
    ("084266", "rucksacks", "noun", "/ˈrʌkˌsæks/", "ba lô đeo vai"),
    ("084267", "ruction", "noun", "/ˈrʌkʃən/", "cuộc cãi vã ồn ào; sự náo loạn"),
    ("084268", "rudapithecus", "noun", "/ˌruːdəpɪˈθiːkəs/", "chi vượn cổ Rudapithecus"),
    ("084269", "rudderfish", "noun", "/ˈrʌdərˌfɪʃ/", "cá cam bơi theo đuôi tàu"),
    ("084270", "rudderpost", "noun", "/ˈrʌdərˌpoʊst/", "trụ đỡ bánh lái tàu"),
    ("084271", "rudderstock", "noun", "/ˈrʌdərˌstɑːk/", "trục bánh lái tàu thủy"),
    ("084272", "ruddied", "verb", "/ˈrʌdid/", "đã làm ửng hồng; đã nhuộm đỏ"),
    ("084273", "ruddies", "verb", "/ˈrʌdiz/", "làm ửng hồng; nhuộm đỏ"),
    ("084274", "ruddily", "adv", "/ˈrʌdɪli/", "hồng hào khỏe mạnh"),
    ("084275", "ruddiness", "noun", "/ˈrʌdinəs/", "vẻ mặt hồng hào khỏe mạnh"),
    ("084276", "ruddles", "noun", "/ˈrʌdəlz/", "đất son đỏ; cúc vạn thọ đồng"),
    ("084277", "ruddock", "noun", "/ˈrʌdək/", "chim cổ đỏ châu Âu"),
    ("084278", "ruddying", "verb", "/ˈrʌdiɪŋ/", "đang làm ửng hồng"),
    ("084279", "ruderal", "adj", "/ˈruːdərəl/", "mọc ở bãi rác hay nơi đổ nát"),
    ("084280", "rudimental", "adj", "/ˌruːdəˈmɛntəl/", "sơ đẳng; bước đầu; thô sơ"),
    ("084281", "rued", "verb", "/ruːd/", "đã hối tiếc; đã ân hận"),
    ("084282", "ruefescence", "noun", "/ruːˈfɛsəns/", "sự ngả màu nâu đỏ"),
    ("084283", "ruefescent", "adj", "/ruːˈfɛsənt/", "ngả màu đỏ hồng"),
    ("084284", "ruefulness", "noun", "/ˈruːfəlnəs/", "vẻ ân hận; nỗi sầu muộn"),
    ("084285", "rues", "verb", "/ruːz/", "hối tiếc; ân hận"),
    ("084286", "ruffed", "adj", "/rʌft/", "có diềm lông cổ xù"),
    ("084287", "ruffianish", "adj", "/ˈrʌfiənɪʃ/", "côn đồ; hung hãn"),
    ("084288", "ruffianism", "noun", "/ˈrʌfiəˌnɪzəm/", "hành vi côn đồ bạo lực"),
    ("084289", "ruffianly", "adj", "/ˈrʌfiənli/", "côn đồ; hung bạo"),
    ("084290", "ruffing", "verb", "/ˈrʌfɪŋ/", "đang đánh bài trùm"),
    ("084291", "ruffler", "noun", "/ˈrʌflər/", "kẻ ngạo mạn; chân vịt nhún bèo"),
    ("084292", "ruffles", "verb", "/ˈrʌfəlz/", "làm rối; làm xù lông; làm phật ý"),
    ("084293", "ruffling", "verb", "/ˈrʌflɪŋ/", "đang làm rối; đang làm phật ý"),
    ("084294", "ruffs", "verb", "/rʌfs/", "đánh bài trùm; xù lông cổ"),
    ("084295", "rufous", "adj", "/ˈruːfəs/", "đỏ hung; nâu đỏ"),
    ("084296", "rugae", "noun", "/ˈruːdʒiː/", "nếp nhăn niêm mạc"),
    ("084297", "rugal", "adj", "/ˈruːɡəl/", "thuộc nếp nhăn niêm mạc"),
    ("084298", "rugate", "adj", "/ˈruːɡeɪt/", "có nếp nhăn"),
    ("084299", "ruggedisation", "noun", "/ˌrʌɡɪdaɪˈzeɪʃən/", "sự gia cố chịu va đập"),
    ("084300", "ruggedise", "verb", "/ˈrʌɡɪˌdaɪz/", "gia cố cho bền chắc"),
    ("084301", "ruggedization", "noun", "/ˌrʌɡɪdaɪˈzeɪʃən/", "sự gia cố chịu va đập"),
    ("084302", "ruggedize", "verb", "/ˈrʌɡɪˌdaɪz/", "gia cố cho bền chắc"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r09_raw_p3.json"))
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

json.dump(out, open("scratch/b37_r09_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b37_r09_p3 saved OK")
