import json

records = [
    ("082903", "repeller", "noun", "/rɪˈpɛlər/", "người xua đuổi; chất xua côn trùng"),
    ("082904", "repellingly", "adv", "/rɪˈpɛlɪŋli/", "một cách ghê tởm, đáng kinh tởm"),
    ("082905", "repels", "verb", "/rɪˈpɛlz/", "đẩy lùi (tấn công); đẩy nhau"),
    ("082906", "repentantly", "adv", "/rɪˈpɛntəntli/", "với vẻ ăn năn, hối hận sâu sắc"),
    ("082907", "repented", "verb", "/rɪˈpɛntɪd/", "đã ăn năn hối cải, đã hối hận"),
    ("082908", "repenting", "verb", "/rɪˈpɛntɪŋ/", "ăn năn hối cải, hối hận về lỗi lầm"),
    ("082909", "repents", "verb", "/rɪˈpɛnts/", "ăn năn hối cải, hối hận sâu sắc"),
    ("082910", "repeople", "verb", "/ˌriːˈpiːpəl/", "tái lập dân cư vào vùng đất hoang"),
    ("082911", "repercuss", "verb", "/ˌriːpərˈkʌs/", "dội âm trở lại; gây ra hệ lụy"),
    ("082912", "reperuse", "verb", "/ˌriːpəˈruːz/", "đọc kỹ lại lần nữa (văn bản)"),
    ("082913", "repetitions", "noun", "/ˌrɛpəˈtɪʃənz/", "những sự lặp lại; hiệp tập (thể)"),
    ("082914", "repetitiously", "adv", "/ˌrɛpəˈtɪʃəsli/", "một cách lặp đi lặp lại nhàm chán"),
    ("082915", "repetitiousness", "noun", "/ˌrɛpəˈtɪʃəsnəs/", "tính lặp đi lặp lại dài dòng chán"),
    ("082916", "rephrased", "verb", "/ˌriːˈfreɪzd/", "đã diễn đạt lại bằng từ ngữ khác"),
    ("082917", "rephrases", "verb", "/ˌriːˈfreɪzɪz/", "diễn đạt lại câu chữ cho rõ hơn"),
    ("082918", "repiece", "verb", "/ˌriːˈpiːs/", "ghép nối lại các mảnh rời rạc"),
    ("082919", "repined", "verb", "/rɪˈpaɪnd/", "đã than vãn rầu rĩ, tỏ ra bất mãn"),
    ("082920", "repines", "verb", "/rɪˈpaɪnz/", "than vãn, sầu não bất mãn (văn)"),
    ("082921", "repining", "verb", "/rɪˈpaɪnɪŋ/", "than vãn buồn rầu, ca thán số phận"),
    ("082922", "repla", "noun", "/ˈrɛplə/", "các vách giả trong quả cải (sinh)"),
    ("082923", "replaceability", "noun", "/rɪˌpleɪsəˈbɪləti/", "tính có thể thay thế được"),
    ("082924", "replaced", "verb", "/rɪˈpleɪst/", "đã thay thế; đã đặt lại về chỗ cũ"),
    ("082925", "replacements", "noun", "/rɪˈpleɪsmənts/", "sự thay thế; linh kiện, người thế"),
    ("082926", "replacer", "noun", "/rɪˈpleɪsər/", "người thay thế; vật phẩm thay thế"),
    ("082927", "replaces", "verb", "/rɪˈpleɪsɪz/", "thay thế cho; đặt trả về vị trí cũ"),
    ("082928", "replantation", "noun", "/ˌriːplænˈteɪʃən/", "phẫu thuật nối lại bộ phận (y học)"),
    ("082929", "replate", "verb", "/ˌriːˈpleɪt/", "mạ lại kim loại; đổi bản kẽm in"),
    ("082930", "replenished", "verb", "/rɪˈplɛnɪʃt/", "đã bổ sung đầy đủ lại kho dự trữ"),
    ("082931", "replenisher", "noun", "/rɪˈplɛnɪʃər/", "dung dịch bổ sung; người tiếp tế"),
    ("082932", "replenishes", "verb", "/rɪˈplɛnɪʃɪz/", "bổ sung, làm đầy lại phần đã dùng"),
    ("082933", "replenishing", "verb", "/rɪˈplɛnɪʃɪŋ/", "bổ sung đầy lại, tiếp tế thêm"),
    ("082934", "replicant", "noun", "/ˈrɛplɪkənt/", "người nhân bản sinh học"),
    ("082935", "replied", "verb", "/rɪˈplaɪd/", "đã trả lời, đã đáp lại thư từ"),
    ("082936", "replies", "verb", "/rɪˈplaɪz/", "trả lời, hồi âm, đối đáp lại"),
    ("082937", "replum", "noun", "/ˈrɛpləm/", "vách giả quả cải (thực vật học)"),
    ("082938", "replying", "verb", "/rɪˈplaɪɪŋ/", "trả lời, đáp lại, phản hồi ý kiến"),
    ("082939", "repoint", "verb", "/ˌriːˈpɔɪnt/", "trát lại mạch vữa tường gạch; chuốt"),
    ("082940", "repolarization", "noun", "/riˌpoʊlərəˈzeɪʃən/", "sự tái phân cực (màng tế bào)"),
    ("082941", "repolish", "verb", "/ˌriːˈpɑːlɪʃ/", "đánh bóng lại; trau chuốt lại văn"),
    ("082942", "repopulate", "verb", "/ˌriːˈpɑːpjəˌleɪt/", "tái tạo dân số, phục hồi quần thể"),
    ("082943", "repopulated", "verb", "/ˌriːˈpɑːpjəˌleɪtɪd/", "đã tái sinh dân cư, khôi phục đàn"),
    ("082944", "repopulates", "verb", "/ˌriːˈpɑːpjəˌleɪts/", "tái tạo dân cư, phục hồi quần thể"),
    ("082945", "repopulating", "verb", "/ˌriːˈpɑːpjəˌleɪtɪŋ/", "tái tạo dân số, khôi phục quần thể"),
    ("082946", "repopulation", "noun", "/ˌriːpɑːpjəˈleɪʃən/", "sự phục hồi dân số hoặc quần thể"),
    ("082947", "reportorial", "adj", "/ˌrɛpərˈtɔːriəl/", "thuộc phóng viên, thuộc nghề báo"),
    ("082948", "reports", "noun", "/rɪˈpɔːrts/", "các bản báo cáo; tin đồn; tiếng nổ"),
    ("082949", "reposal", "noun", "/rɪˈpoʊzəl/", "sự đặt niềm tin; sự nghỉ ngơi (cổ)"),
    ("082950", "reposed", "verb", "/rɪˈpoʊzd/", "đã nghỉ ngơi, an nghỉ; đặt tin cậy"),
    ("082951", "reposeful", "adj", "/rɪˈpoʊzfəl/", "thanh bình, yên ả, êm đềm thư thái"),
    ("082952", "reposefulness", "noun", "/rɪˈpoʊzfəlnəs/", "trạng thái thanh thản yên bình"),
    ("082953", "reposes", "verb", "/rɪˈpoʊzɪz/", "nghỉ ngơi; nằm yên; đặt lòng tin"),
    ("082954", "reposing", "verb", "/rɪˈpoʊzɪŋ/", "nghỉ ngơi thư giãn; đặt niềm tin"),
    ("082955", "reposit", "verb", "/rɪˈpɑːzɪt/", "cất giữ, lưu trữ nơi an toàn (cổ)"),
    ("082956", "repositing", "noun", "/rɪˈpɑːzɪtɪŋ/", "sự cất giữ trong kho lưu trữ"),
    ("082957", "repossessed", "verb", "/ˌriːpəˈzɛst/", "đã thu hồi tài sản thế chấp (nợ)"),
    ("082958", "repossesses", "verb", "/ˌriːpəˈzɛsɪz/", "thu hồi lại tài sản khi quá hạn nợ"),
    ("082959", "repossessing", "verb", "/ˌriːpəˈzɛsɪŋ/", "thu hồi lại tài sản (xe, nhà nợ)"),
    ("082960", "reprehended", "verb", "/ˌrɛprɪˈhɛndɪd/", "đã khiển trách, đã quở mắng nghiêm"),
    ("082961", "reprehending", "verb", "/ˌrɛprɪˈhɛndɪŋ/", "khiển trách, chỉ trích, phê phán"),
    ("082962", "reprehends", "verb", "/ˌrɛprɪˈhɛndz/", "khiển trách, quở mắng nghiêm khắc"),
    ("082963", "reprehensibility", "noun", "/ˌrɛprɪhɛnsəˈbɪləti/", "tính đáng khiển trách, đáng lên án"),
    ("082964", "reprehension", "noun", "/ˌrɛprɪˈhɛnʃən/", "lời khiển trách, sự quở trách nặng"),
    ("082965", "reprehensively", "adv", "/ˌrɛprɪˈhɛnsɪvli/", "với giọng khiển trách, chê trách"),
    ("082966", "representations", "noun", "/ˌrɛprɪzɛnˈteɪʃənz/", "sự đại diện; hình ảnh; trình bày"),
    ("082967", "representatives", "noun", "/ˌrɛprɪˈzɛntətɪvz/", "những người đại diện; hạ nghị sĩ"),
    ("082968", "representer", "noun", "/ˌrɛprɪˈzɛntər/", "người đại diện, người trình bày"),
    ("082969", "representing", "verb", "/ˌrɛprɪˈzɛntɪŋ/", "đại diện cho; tượng trưng; mô tả"),
    ("082970", "represents", "verb", "/ˌrɛprɪˈzɛnts/", "đại diện cho; biểu thị, tượng trưng"),
    ("082971", "represser", "noun", "/rɪˈprɛsər/", "kẻ đàn áp; gen ức chế (sinh học)"),
    ("082972", "represses", "verb", "/rɪˈprɛsɪz/", "đàn áp (bạo loạn); kìm nén cảm xúc"),
    ("082973", "repressible", "adj", "/rɪˈprɛsəbəl/", "có thể kìm nén; có thể dẹp yên"),
    ("082974", "repressively", "adv", "/rɪˈprɛsɪvli/", "theo lối đàn áp, kìm kẹp gắt gao"),
    ("082975", "repressiveness", "noun", "/rɪˈprɛsɪvnəs/", "tính chất đàn áp, sự kìm kẹp tự do"),
    ("082976", "reprieved", "verb", "/rɪˈpriːvd/", "đã hoãn thi hành án; cho khuây khỏa"),
    ("082977", "reprieves", "verb", "/rɪˈpriːvz/", "hoãn thi hành án; giải thoát tạm"),
    ("082978", "reprieving", "verb", "/rɪˈpriːvɪŋ/", "hoãn thi hành án; tạm cứu vãn nguy"),
    ("082979", "reprimanded", "verb", "/ˈrɛprəˌmændɪd/", "đã khiển trách chính thức"),
    ("082980", "reprimanding", "verb", "/ˈrɛprəˌmændɪŋ/", "khiển trách, quở trách nghiêm khắc"),
    ("082981", "reprimands", "verb", "/ˈrɛprəˌmændz/", "khiển trách, quở trách chính thức"),
    ("082982", "reprinted", "verb", "/ˌriːˈprɪntɪd/", "đã in lại, đã tái bản sách báo"),
    ("082983", "reprints", "verb", "/ˌriːˈprɪnts/", "in lại, tái bản (sách, bài báo)"),
    ("082984", "reprize", "verb", "/rɪˈpraɪz/", "diễn lại, lặp lại đoạn nhạc điệp"),
    ("082985", "reproachable", "adj", "/rɪˈproʊtʃəbəl/", "đáng trách móc, đáng bị chê trách"),
    ("082986", "reproached", "verb", "/rɪˈproʊtʃt/", "đã trách móc, đã khiển trách nhẹ"),
    ("082987", "reproacher", "noun", "/rɪˈproʊtʃər/", "người hay trách móc, chỉ trích"),
    ("082988", "reproaches", "verb", "/rɪˈproʊtʃɪz/", "trách móc, chê trách, chỉ trích"),
    ("082989", "reproachfulness", "noun", "/rɪˈproʊtʃfəlnəs/", "vẻ trách móc, thái độ oán trách"),
    ("082990", "reproaching", "verb", "/rɪˈproʊtʃɪŋ/", "trách móc, chê trách nhẹ nhàng"),
    ("082991", "reproachless", "adj", "/rɪˈproʊtʃləs/", "không chê trách vào đâu được"),
    ("082992", "reprobative", "adj", "/ˈrɛprəˌbeɪtɪv/", "khiển trách gay gắt, lên án nặng"),
    ("082993", "reprobatory", "adj", "/ˈrɛprəbəˌtɔːri/", "lên án gay gắt, quở trách mạnh mẽ"),
    ("082994", "reprocessed", "verb", "/ˌriːˈprɑːsɛst/", "đã tái chế, xử lý lại (nhiên liệu)"),
    ("082995", "reprocesses", "verb", "/ˌriːˈprɑːsɛsɪz/", "tái chế, xử lý lại chất thải hạt"),
    ("082996", "reprocessing", "verb", "/ˌriːˈprɑːsɛsɪŋ/", "tái chế, xử lý lại để tận dụng"),
    ("082997", "reproduced", "verb", "/ˌriːprəˈduːst/", "đã tái tạo, sao chép; đã sinh sản"),
    ("082998", "reproduces", "verb", "/ˌriːprəˈduːsɪz/", "tái tạo, sao chép; sinh sản nòi"),
    ("082999", "reproducing", "verb", "/ˌriːprəˈduːsɪŋ/", "tái tạo, sao chép; sinh sản truyền"),
    ("083000", "reproductions", "noun", "/ˌriːprəˈdʌkʃənz/", "bản sao chép; quá trình sinh sản"),
    ("083001", "reproductiveness", "noun", "/ˌriːprəˈdʌktɪvnəs/", "khả năng sinh sản, tính tái tạo"),
    ("083002", "reproductor", "noun", "/ˌriːprəˈdʌktər/", "máy sao chép thẻ đục lỗ (cũ)"),
]

raw = json.load(open("scratch/b37_r06_raw_p5.json"))
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
with open("scratch/b37_r06_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r06_p5 saved OK")
