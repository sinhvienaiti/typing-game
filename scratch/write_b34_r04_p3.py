import json

items = [
    ("066703", "white cohosh", "phrase", "/waɪt ˈkoʊhɒʃ/", "cây thiên ma trắng Bắc Mỹ"),
    ("066704", "abacas", "noun", "/ˈæbəkəz/", "cây chuối sợi lấy xơ làm dây"),
    ("066705", "abeles", "noun", "/əˈbiːlz/", "cây dương trắng lá bạc châu Âu"),
    ("066706", "abruptions", "noun", "/əˈbrʌpʃənz/", "sự đứt gãy đột ngột; bong nhau thai"),
    ("066707", "achaeans", "noun", "/əˈkiːənz/", "người Hy Lạp cổ vùng Achaea"),
    ("066708", "adads", "noun", "/əˈdɑːdz/", "thần bão tố Adad vùng Lưỡng Hà"),
    ("066709", "aerofoils", "noun", "/ˈɛərəˌfɔɪlz/", "cánh máy bay tạo lực nâng khí động"),
    ("066710", "aesirs", "noun", "/ˈeɪsɪərz/", "nhóm thần chính Aesir Bắc Âu"),
    ("066711", "alembics", "noun", "/əˈlɛmbɪks/", "bình chưng cất thủy tinh giả kim cổ"),
    ("066712", "alkyds", "noun", "/ˈælkɪdz/", "nhựa tổng hợp alkyd làm sơn phủ"),
    ("066713", "anencephalies", "noun", "/ˌænɛnˈsɛfəliz/", "dị tật bẩm sinh vô sọ thai nhi"),
    ("066714", "anunnakis", "noun", "/ˌɑːnʊˈnɑːkiz/", "nhóm thần cổ đại Anunnaki Lưỡng Hà"),
    ("066715", "apperceptions", "noun", "/ˌæpərˈsɛpʃənz/", "sự lĩnh hội dựa trên kinh nghiệm"),
    ("066716", "asystoles", "noun", "/eɪˈsɪstəliz/", "tình trạng tim ngừng đập hoàn toàn"),
    ("066717", "bennis", "noun", "/ˈbɛniz/", "cây vừng; hạt mè lấy dầu"),
    ("066718", "berberises", "noun", "/ˈbɜːrbərɪsɪz/", "cây hoàng liên gai chi Berberis"),
    ("066719", "bhangs", "noun", "/bæŋz/", "chế phẩm lá cần sa dùng ở Ấn Độ"),
    ("066720", "bioassayed", "verb", "/ˌbaɪoʊˈæseɪd/", "đã thử nghiệm định lượng sinh học"),
    ("066721", "bioassaying", "verb", "/ˌbaɪoʊˈæseɪɪŋ/", "đang định lượng hoạt tính sinh học"),
    ("066722", "bioassays", "noun", "/ˈbaɪoʊˌæseɪz/", "phép thử định lượng sinh học"),
    ("066723", "blowflies", "noun", "/ˈbloʊˌflaɪz/", "ruồi nhặng xanh đẻ dòi"),
    ("066724", "brownouts", "noun", "/ˈbraʊnˌaʊts/", "tình trạng sụt giảm điện áp cục bộ"),
    ("066725", "bruneians", "noun", "/bruːˈnaɪənz/", "người dân vương quốc Brunei"),
    ("066726", "bullfinches", "noun", "/ˈbʊlˌfɪntʃɪz/", "chim sẻ ức đỏ châu Âu"),
    ("066727", "campanulas", "noun", "/kæmˈpænjələz/", "hoa chuông thuộc chi Campanula"),
    ("066728", "capricci", "noun", "/kəˈpriːtʃi/", "tác phẩm âm nhạc tự do capriccio"),
    ("066729", "capriccios", "noun", "/kəˈpriːtʃoʊz/", "bản nhạc hoặc tranh kỳ hứng tự do"),
    ("066730", "chipewyans", "noun", "/ˌtʃɪpəˈwaɪənz/", "người bản địa Dene Chipewyan"),
    ("066731", "clawbacks", "noun", "/ˈklɔːˌbæks/", "điều khoản thu hồi tiền thưởng cũ"),
    ("066732", "coccis", "noun", "/ˈkɒksaɪ/", "vi khuẩn hình cầu; cầu khuẩn"),
    ("066733", "cockfights", "noun", "/ˈkɒkˌfaɪts/", "trò chọi gà đá gà độ"),
    ("066734", "coffeepots", "noun", "/ˈkɒfiˌpɒts/", "ấm pha và đựng cà phê nóng"),
    ("066735", "complines", "noun", "/ˈkɒmplɪnz/", "giờ kinh tối cuối ngày Công giáo"),
    ("066736", "conceptualisations", "noun", "/kənˌsɛptʃʊəlaɪˈzeɪʃənz/", "quá trình khái niệm hóa ý tưởng"),
    ("066737", "consignees", "noun", "/ˌkɒnsaɪˈniːz/", "người nhận hàng ghi trên vận đơn"),
    ("066738", "daybeds", "noun", "/ˈdeɪˌbɛdz/", "ghế dài ban ngày kiêm giường ngủ"),
    ("066739", "decipherments", "noun", "/dɪˈsaɪfərmənts/", "sự giải mã văn tự cổ hoặc mật mã"),
    ("066740", "deglazed", "verb", "/diːˈɡleɪzd/", "đã tráng chảo bằng rượu làm xốt"),
    ("066741", "deglazes", "verb", "/diːˈɡleɪzɪz/", "tráng chảo lấy cặn làm nước xốt"),
    ("066742", "deglazing", "verb", "/diːˈɡleɪzɪŋ/", "đang tráng chảo làm nước xốt"),
    ("066743", "destressed", "verb", "/diːˈstrɛst/", "đã giảm căng thẳng; tạo nét cũ mòn"),
    ("066744", "destresses", "verb", "/diːˈstrɛsɪz/", "thư giãn giảm stress; làm cũ đồ"),
    ("066745", "destressing", "verb", "/diːˈstrɛsɪŋ/", "đang giải tỏa căng thẳng tinh thần"),
    ("066746", "dewdrops", "noun", "/ˈdjuːˌdrɒps/", "giọt sương đọng trên lá sớm mai"),
    ("066747", "dichromates", "noun", "/daɪˈkroʊmeɪts/", "muối đicromat chất oxy hóa mạnh"),
    ("066748", "dilantins", "noun", "/daɪˈlæntɪnz/", "thuốc chống động kinh Dilantin"),
    ("066749", "donatuses", "noun", "/dəˈneɪtəsɪz/", "giám mục Donatus xứ Carthage"),
    ("066750", "donjons", "noun", "/ˈdɒndʒənz/", "tháp canh kiên cố chính của lâu đài"),
    ("066751", "dphils", "noun", "/ˌdiːˈfɪlz/", "học vị tiến sĩ triết học Oxford"),
    ("066752", "dromes", "noun", "/droʊmz/", "sân bay nhỏ; trường đua lòng chảo"),
    ("066753", "easterners", "noun", "/ˈiːstərnərz/", "người sinh sống ở vùng phía đông"),
    ("066754", "endoskeletons", "noun", "/ˌɛndoʊˈskɛlɪtənz/", "bộ xương nằm bên trong cơ thể"),
    ("066755", "firkins", "noun", "/ˈfɜːrkɪnz/", "thùng gỗ nhỏ 9 galông đựng bia bơ"),
    ("066756", "flittered", "verb", "/ˈflɪtərd/", "đã bay chập chờn thoăn thoắt"),
    ("066757", "flittering", "verb", "/ˈflɪtərɪŋ/", "đang bay chập chờn lướt nhanh"),
    ("066758", "flitters", "verb", "/ˈflɪtərz/", "bay lượn chập chờn thoăn thoắt"),
    ("066759", "floggers", "noun", "/ˈflɒɡərz/", "người đánh roi; kẻ buôn hàng lóng"),
    ("066760", "fontenoys", "noun", "/ˌfɒntəˈnɔɪz/", "trận đánh Fontenoy năm 1745"),
    ("066761", "fraternized", "verb", "/ˈfrætərˌnaɪzd/", "đã kết giao thân mật; giao lưu"),
    ("066762", "fraternizes", "verb", "/ˈfrætərˌnaɪzɪz/", "kết thân gần gũi với đối phương"),
    ("066763", "fraternizing", "verb", "/ˈfrætərˌnaɪzɪŋ/", "đang kết giao thân mật gắn bó"),
    ("066764", "gastrulations", "noun", "/ˌɡæstrəˈleɪʃənz/", "quá trình tạo phôi vị ở phôi thai"),
    ("066765", "gelts", "noun", "/ɡɛlts/", "tiền bạc (lóng gốc tiếng Yiddish)"),
    ("066766", "godparents", "noun", "/ˈɡɒdˌpɛərənts/", "cha mẹ đỡ đầu theo nghi thức"),
    ("066767", "goutier", "adj", "/ˈɡaʊtiər/", "mắc bệnh gút nặng hơn; sưng khớp"),
    ("066768", "goutiest", "adj", "/ˈɡaʊtiɪst/", "mắc bệnh gút nặng nhất"),
    ("066769", "grenadians", "noun", "/ɡrəˈneɪdiənz/", "người dân đảo quốc Grenada"),
    ("066770", "halicarnassuses", "noun", "/ˌhælɪkɑːrˈnæsəsɪz/", "thành cổ Halicarnassus Thổ Nhĩ Kỳ"),
    ("066771", "hasps", "noun", "/hæsps/", "bát khóa sắt gài chốt cửa hòm"),
    ("066772", "heavisides", "noun", "/ˈhɛvɪˌsaɪdz/", "nhà vật lý Anh Oliver Heaviside"),
    ("066773", "herpetologists", "noun", "/ˌhɜːrpɪˈtɒlədʒɪsts/", "nhà nghiên cứu bò sát và lưỡng cư"),
    ("066774", "hijazes", "noun", "/hɪˈdʒɑːzɪz/", "vùng lịch sử Hijaz Ả Rập Xê Út"),
    ("066775", "hosepipes", "noun", "/ˈhoʊzˌpaɪps/", "ống mềm vòi dẫn nước tưới cây"),
    ("066776", "humdingers", "noun", "/ˈhʌmˌdɪŋərz/", "người hoặc vật xuất sắc tuyệt vời"),
    ("066777", "identikits", "noun", "/aɪˈdɛntɪˌkɪts/", "bản vẽ phác họa chân dung nghi phạm"),
    ("066778", "imperfectives", "noun", "/ˌɪmpərˈfɛktɪvz/", "thể chưa hoàn thành của động từ"),
    ("066779", "indispositions", "noun", "/ˌɪndɪspəˈzɪʃənz/", "cơn khó ở nhẹ; sự không sẵn lòng"),
    ("066780", "inkblots", "noun", "/ˈɪŋkˌblɒts/", "vết mực loang trắc nghiệm tâm lý"),
    ("066781", "jespersens", "noun", "/ˈjɛspərsənz/", "nhà ngôn ngữ học Otto Jespersen"),
    ("066782", "kebs", "noun", "/kɛbz/", "thần đất Ai Cập cổ Keb (Geb)"),
    ("066783", "kirghizes", "noun", "/ˈkɪərɡɪzɪz/", "người dân tộc Kyrgyz Trung Á"),
    ("066784", "lachaises", "noun", "/ləˈʃɛzɪz/", "nhà điêu khắc Pháp Gaston Lachaise"),
    ("066785", "lamellas", "noun", "/ləˈmɛləz/", "phiến mỏng; lá mang của nấm"),
    ("066786", "leeuwenhoeks", "noun", "/ˈleɪvənˌhʊks/", "nhà kính hiển vi học Leeuwenhoek"),
    ("066787", "liquifies", "verb", "/ˈlɪkwɪˌfaɪz/", "làm tan chảy hóa thành chất lỏng"),
    ("066788", "liquifying", "verb", "/ˈlɪkwɪˌfaɪɪŋ/", "đang hóa lỏng chất rắn hoặc khí"),
    ("066789", "logier", "adj", "/ˈloʊɡiər/", "chậm chạp uể oải đờ đẫn hơn"),
    ("066790", "logiest", "adj", "/ˈloʊɡiɪst/", "chậm chạp uể oải đờ đẫn nhất"),
    ("066791", "lubbers", "noun", "/ˈlʌbərz/", "kẻ to lớn vụng về; thủy thủ mới"),
    ("066792", "malabos", "noun", "/məˈlɑːboʊz/", "thủ đô Malabo Guinea Xích Đạo"),
    ("066793", "manageresses", "noun", "/ˈmænɪdʒərɪsɪz/", "nữ quản lý khách sạn cửa hàng"),
    ("066794", "mergansers", "noun", "/mərˈɡænsərz/", "vịt mỏ cưa lặn bắt cá"),
    ("066795", "montrachets", "noun", "/ˌmɒntrəˈʃeɪz/", "rượu vang trắng Montrachet Pháp"),
    ("066796", "muhammadans", "noun", "/moʊˈhæmədənz/", "tín đồ Hồi giáo (cách gọi cũ)"),
    ("066797", "naiades", "noun", "/ˈnaɪədiːz/", "nữ thần suối; ấu trùng dưới nước"),
    ("066798", "naiads", "noun", "/ˈnaɪædz/", "nữ thần nước; ấu trùng thủy sinh"),
    ("066799", "nibblers", "noun", "/ˈnɪblərz/", "người hay gặm nhấm; kẻ cắn nhỏ"),
    ("066800", "numidias", "noun", "/njuːˈmɪdiəz/", "vương quốc cổ đại Numidia Bắc Phi"),
    ("066801", "officeholders", "noun", "/ˈɒfɪsˌhoʊldərz/", "công chức đang giữ chức vụ công"),
    ("066802", "okehs", "noun", "/oʊˈkeɪz/", "sự đồng ý phê chuẩn (biến thể)"),
]

with open("scratch/b34_r04_raw_p3.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS {pos} for {hw}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    inner = ipa[1:-1]
    assert inner and not inner.startswith(" ") and not inner.endswith(" "), f"Empty/space IPA: {hw} -> {ipa}"
    rec = dict(r)
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

with open("scratch/b34_r04_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r04_p3.json OK")
