import json

records = [
    ("082203", "reduplicates", "verb", "/rɪˈduːpləˌkeɪts/", "lặp lại, láy âm; nhân đôi lên"),
    ("082204", "reduplicating", "verb", "/rɪˈduːpləˌkeɪtɪŋ/", "lặp lại, láy âm; nhân đôi lên"),
    ("082205", "reduplicative", "adj", "/rɪˈduːpləˌkeɪtɪv/", "có tính chất lặp lại, từ láy (ngữ)"),
    ("082206", "reduviid", "noun", "/rɪˈduːviˌɪd/", "bọ xít ăn sâu họ Reduviidae"),
    ("082207", "reduviidae", "noun", "/ˌrɛdjʊˈvaɪɪˌdiː/", "họ Bọ xít bắt mồi (Reduviidae)"),
    ("082208", "redwoods", "noun", "/ˈrɛdˌwʊdz/", "những cây gỗ đỏ khổng lồ Bắc Mỹ"),
    ("082209", "redye", "verb", "/ˌriːˈdaɪ/", "nhuộm lại màu khác"),
    ("082210", "redyed", "verb", "/ˌriːˈdaɪd/", "đã nhuộm lại màu mới"),
    ("082211", "redyeing", "verb", "/ˌriːˈdaɪɪŋ/", "nhuộm lại màu cho vải, tóc"),
    ("082212", "redyes", "verb", "/ˌriːˈdaɪz/", "nhuộm lại màu khác"),
    ("082213", "redying", "verb", "/ˌriːˈdaɪɪŋ/", "nhuộm lại màu mới (biến thể)"),
    ("082214", "ree", "adj", "/riː/", "ngà ngà say; điên cuồng (Scotland)"),
    ("082215", "reecho", "verb", "/ˌriːˈɛkoʊ/", "vang vọng lại nhiều lần"),
    ("082216", "reechoed", "verb", "/ˌriːˈɛkoʊd/", "đã vang vọng lại nhiều lần"),
    ("082217", "reechoes", "noun", "/ˌriːˈɛkoʊz/", "những tiếng vang vọng dội lại mãi"),
    ("082218", "reechoing", "adj", "/ˌriːˈɛkoʊɪŋ/", "vang vọng, dội âm lặp đi lặp lại"),
    ("082219", "reedbird", "noun", "/ˈriːdˌbɜːrd/", "chim sẻ đồng lúa Mỹ (bobolink)"),
    ("082220", "reedbuck", "noun", "/ˈriːdˌbʌk/", "linh dương đồng sậy châu Phi"),
    ("082221", "reedbucks", "noun", "/ˈriːdˌbʌks/", "những con linh dương đồng sậy"),
    ("082222", "reeded", "adj", "/ˈriːdɪd/", "lợp sậy; có gờ rãnh dọc (cột)"),
    ("082223", "reedify", "verb", "/riˈɛdəˌfaɪ/", "xây dựng lại, kiến thiết lại (cổ)"),
    ("082224", "reediness", "noun", "/ˈriːdinəs/", "giọng rè chói; dáng mảnh như sậy"),
    ("082225", "reeding", "noun", "/ˈriːdɪŋ/", "gờ nổi bán nguyệt; rãnh cạnh xu"),
    ("082226", "reedit", "verb", "/ˌriːˈɛdɪt/", "biên tập lại, tái bản có chỉnh sửa"),
    ("082227", "reedited", "verb", "/ˌriːˈɛdɪtɪd/", "đã biên tập lại, đã tái bản sửa"),
    ("082228", "reediting", "verb", "/ˌriːˈɛdɪtɪŋ/", "biên tập lại, hiệu đính tái bản"),
    ("082229", "reedits", "verb", "/ˌriːˈɛdɪts/", "biên tập lại, tái bản hiệu đính"),
    ("082230", "reedlike", "adj", "/ˈriːdˌlaɪk/", "mảnh dẻ thanh thoát như cây sậy"),
    ("082231", "reedmace", "noun", "/ˈriːdˌmeɪs/", "cây bồn bồn, cỏ nến (Typha)"),
    ("082232", "reeducate", "verb", "/ˌriːˈɛdʒəˌkeɪt/", "giáo dục lại, cải tạo lại, phục hồi"),
    ("082233", "reeducated", "verb", "/ˌriːˈɛdʒəˌkeɪtɪd/", "đã giáo dục lại, phục hồi chức năng"),
    ("082234", "reeducates", "verb", "/ˌriːˈɛdʒəˌkeɪts/", "giáo dục lại, đào tạo lại kỹ năng"),
    ("082235", "reeducating", "verb", "/ˌriːˈɛdʒəˌkeɪtɪŋ/", "giáo dục lại, rèn luyện phục hồi"),
    ("082236", "reeducation", "noun", "/ˌriːɛdʒəˈkeɪʃən/", "sự giáo dục lại; phục hồi chức năng"),
    ("082237", "reefed", "verb", "/riːft/", "đã thu bớt cánh buồm (hàng hải)"),
    ("082238", "reefing", "noun", "/ˈriːfɪŋ/", "kỹ thuật thu bớt cánh buồm"),
    ("082239", "reefs", "verb", "/riːfs/", "thu nhỏ cánh buồm khi có gió mạnh"),
    ("082240", "reefy", "adj", "/ˈriːfi/", "nhiều đá ngầm, nhiều rạn san hô"),
    ("082241", "reeked", "verb", "/riːkt/", "đã bốc mùi hôi nồng; đã bốc khói"),
    ("082242", "reeks", "verb", "/riːks/", "bốc mùi hôi nồng nặc; nồng nặc mùi"),
    ("082243", "reeky", "adj", "/ˈriːki/", "ám khói mù mịt; bốc mùi hôi nồng"),
    ("082244", "reelected", "verb", "/ˌriːɪˈlɛktɪd/", "đã tái đắc cử, được bầu lại"),
    ("082245", "reelecting", "verb", "/ˌriːɪˈlɛktɪŋ/", "tái bầu cử, bầu lại nhiệm kỳ mới"),
    ("082246", "reelects", "verb", "/ˌriːɪˈlɛkts/", "bầu lại, tái bầu cử vào chức vụ"),
    ("082247", "reeled", "verb", "/riːld/", "đã cuộn dây; đã đi loạng choạng"),
    ("082248", "reeligible", "adj", "/ˌriːˈɛlɪdʒəbəl/", "đủ điều kiện tái ứng cử (lỗi viết)"),
    ("082249", "reeling", "verb", "/ˈriːlɪŋ/", "cuộn dây; đi loạng choạng"),
    ("082250", "reelingly", "adv", "/ˈriːlɪŋli/", "loạng choạng, quay cuồng"),
    ("082251", "reels", "verb", "/riːlz/", "cuộn dây, quay guồng; lảo đảo"),
    ("082252", "reenforcement", "noun", "/ˌriːɪnˈfɔːrsmənt/", "sự tăng cường, quân tiếp viện"),
    ("082253", "reengage", "verb", "/ˌriːɪnˈɡeɪdʒ/", "tái gắn kết; tái giao chiến"),
    ("082254", "reengaged", "verb", "/ˌriːɪnˈɡeɪdʒd/", "đã tái gắn kết; đã đính hôn lại"),
    ("082255", "reengages", "verb", "/ˌriːɪnˈɡeɪdʒɪz/", "tái gắn kết; giao tranh lại"),
    ("082256", "reengaging", "verb", "/ˌriːɪnˈɡeɪdʒɪŋ/", "tái gắn kết, gài khớp lại; giao đấu"),
    ("082257", "reengine", "verb", "/ˌriːˈɛndʒɪn/", "thay động cơ mới (cho máy bay, tàu)"),
    ("082258", "reenkindle", "verb", "/ˌriːɪnˈkɪndəl/", "nhóm lại lửa, khơi dậy lại ngọn lửa"),
    ("082259", "reenter", "verb", "/ˌriːˈɛntər/", "tái nhập, đi vào lại; nhập lại"),
    ("082260", "reentered", "verb", "/ˌriːˈɛntərd/", "đã quay trở vào; đã nhập lại vào"),
    ("082261", "reentering", "verb", "/ˌriːˈɛntərɪŋ/", "quay trở vào lại; tái nhập"),
    ("082262", "reenters", "verb", "/ˌriːˈɛntərz/", "quay trở vào lại; tái gia nhập"),
    ("082263", "reeves", "noun", "/riːvz/", "chánh án địa hạt xưa; chim cái rẽ"),
    ("082264", "reexamined", "verb", "/ˌriːɪɡˈzæmɪnd/", "đã kiểm tra lại, đã xem xét lại"),
    ("082265", "reexamines", "verb", "/ˌriːɪɡˈzæmɪnz/", "kiểm tra lại, thẩm tra kỹ lại"),
    ("082266", "reexamining", "verb", "/ˌriːɪɡˈzæmɪnɪŋ/", "xem xét lại, tái kiểm định lại"),
    ("082267", "reexpands", "verb", "/ˌriːɪkˈspændz/", "mở rộng trở lại, giãn nở ra lại"),
    ("082268", "reexport", "verb", "/ˌriːɛkˈspɔːrt/", "tái xuất khẩu hàng hóa nhập vào"),
    ("082269", "reexportation", "noun", "/ˌriːɛkspɔːrˈteɪʃən/", "hoạt động tái xuất khẩu hàng hóa"),
    ("082270", "reexported", "verb", "/ˌriːɛkˈspɔːrtɪd/", "đã tái xuất khẩu hàng hóa ra ngoài"),
    ("082271", "reexporting", "verb", "/ˌriːɛkˈspɔːrtɪŋ/", "tái xuất khẩu hàng hóa đã nhập"),
    ("082272", "reexports", "verb", "/ˌriːɛkˈspɔːrts/", "tái xuất khẩu hàng hóa"),
    ("082273", "refabrication", "noun", "/ˌriːfæbrɪˈkeɪʃən/", "sự tái chế tạo, gia công lại"),
    ("082274", "refaced", "verb", "/ˌriːˈfeɪst/", "đã ốp mặt lại, làm mới bề mặt"),
    ("082275", "refaces", "verb", "/ˌriːˈfeɪsɪz/", "ốp lát bề mặt mới, mài phẳng mặt"),
    ("082276", "refacing", "verb", "/ˌriːˈfeɪsɪŋ/", "làm mới lớp bề mặt (tủ, tường)"),
    ("082277", "refactor", "verb", "/ˌriːˈfæktər/", "tái cấu trúc mã nguồn (tin học)"),
    ("082278", "refactored", "verb", "/ˌriːˈfæktərd/", "đã tái cấu trúc mã nguồn (tin học)"),
    ("082279", "refactoring", "verb", "/ˌriːˈfæktərɪŋ/", "tái cấu trúc mã nguồn (tin học)"),
    ("082280", "refactorings", "noun", "/ˌriːˈfæktərɪŋz/", "các bước tái cấu trúc mã nguồn"),
    ("082281", "refactors", "verb", "/ˌriːˈfæktərz/", "tái cấu trúc mã nguồn (tin học)"),
    ("082282", "refectioner", "noun", "/rɪˈfɛkʃənər/", "tu sĩ quản lý nhà ăn tu viện"),
    ("082283", "refectioners", "noun", "/rɪˈfɛkʃənərz/", "người phụ trách nhà ăn tu viện"),
    ("082284", "refective", "adj", "/rɪˈfɛktɪv/", "giúp hồi sức, bồi bổ sức lực"),
    ("082285", "referal", "noun", "/rɪˈfɜːrəl/", "sự giới thiệu, giấy chuyển viện"),
    ("082286", "refereed", "verb", "/ˌrɛfəˈriːd/", "đã làm trọng tài; đã thẩm định"),
    ("082287", "referees", "verb", "/ˌrɛfəˈriːz/", "làm trọng tài; thẩm định bài viết"),
    ("082288", "referenda", "noun", "/ˌrɛfəˈrɛndə/", "các cuộc trưng cầu dân ý"),
    ("082289", "referendums", "noun", "/ˌrɛfəˈrɛndəmz/", "các cuộc trưng cầu dân ý"),
    ("082290", "referred", "verb", "/rɪˈfɜːrd/", "đã nhắc đến; đã chuyển giới thiệu"),
    ("082291", "referring", "verb", "/rɪˈfɜːrɪŋ/", "nhắc đến, ám chỉ; chuyển giới thiệu"),
    ("082292", "refers", "verb", "/rɪˈfɜːrz/", "ám chỉ, đề cập đến; chuyển giao"),
    ("082293", "reffectingly", "adv", "/rɪˈflɛktɪŋli/", "suy tư, trầm ngâm (biến thể lỗi)"),
    ("082294", "reffection", "noun", "/rɪˈflɛkʃən/", "sự phản chiếu, suy ngẫm (lỗi viết)"),
    ("082295", "reffective", "adj", "/rɪˈflɛktɪv/", "phản chiếu; trầm tư (lỗi viết)"),
    ("082296", "reffector", "noun", "/rɪˈflɛktər/", "gương phản xạ (biến thể sai chữ)"),
    ("082297", "reffex", "noun", "/ˈriːflɛks/", "phản xạ; ánh phản chiếu (lỗi chữ)"),
    ("082298", "reffexibility", "noun", "/rɪˌflɛksəˈbɪləti/", "tính chất phản xạ được (lỗi chữ)"),
    ("082299", "reffexible", "adj", "/rɪˈflɛksəbəl/", "có thể phản xạ (biến thể lỗi)"),
    ("082300", "reffexive", "adj", "/rɪˈflɛksɪv/", "phản thân (ngữ pháp, lỗi viết)"),
    ("082301", "refinements", "noun", "/rɪˈfaɪnmənts/", "sự tinh chế; nét tinh tế thanh lịch"),
    ("082302", "refineries", "noun", "/rɪˈfaɪnəriz/", "những nhà máy lọc dầu, tinh chế"),
]

raw = json.load(open("scratch/b37_r05_raw_p3.json"))
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
with open("scratch/b37_r05_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r05_p3 saved OK")
