import json

records = [
    ("082503", "rehanged", "verb", "/ˌriːˈhæŋd/", "đã treo lại (hành quyết, treo đồ)"),
    ("082504", "rehanging", "verb", "/ˌriːˈhæŋɪŋ/", "treo lại, mắc lên lại vị trí cũ"),
    ("082505", "rehangs", "verb", "/ˌriːˈhæŋz/", "treo lại (tranh ảnh, cửa, rèm)"),
    ("082506", "reharden", "verb", "/ˌriːˈhɑːrdən/", "tôi cứng lại (thép); làm cứng lại"),
    ("082507", "reharmonisation", "noun", "/ˌriːhɑːrmənaɪˈzeɪʃən/", "sự phối hòa âm lại (Anh)"),
    ("082508", "reharmonise", "verb", "/ˌriːˈhɑːrməˌnaɪz/", "hòa âm lại, phối khí lại (Anh)"),
    ("082509", "reharmonization", "noun", "/ˌriːhɑːrmənaɪˈzeɪʃən/", "sự phối hòa âm lại bản nhạc"),
    ("082510", "reharmonize", "verb", "/ˌriːˈhɑːrməˌnaɪz/", "hòa âm lại, phối khí lại bản nhạc"),
    ("082511", "rehashed", "verb", "/ˌriːˈhæʃt/", "đã xào nấu lại; bàn đi bàn lại"),
    ("082512", "rehashes", "verb", "/ˌriːˈhæʃɪz/", "xào nấu lại, lặp lại ý cũ nhàm chán"),
    ("082513", "rehashing", "verb", "/ˌriːˈhæʃɪŋ/", "xào nấu lại ý cũ; nhai lại chuyện"),
    ("082514", "reheard", "verb", "/ˌriːˈhɜːrd/", "đã nghe lại; đã tái thẩm vụ án"),
    ("082515", "rehearsed", "verb", "/rɪˈhɜːrst/", "đã diễn tập, đã tập dượt trước"),
    ("082516", "rehearses", "verb", "/rɪˈhɜːrsɪz/", "diễn tập, tập dượt trước; kể lể"),
    ("082517", "rehearsing", "verb", "/rɪˈhɜːrsɪŋ/", "diễn tập, tập dượt cho buổi diễn"),
    ("082518", "reheated", "verb", "/ˌriːˈhiːtɪd/", "đã hâm nóng lại (đồ ăn thức uống)"),
    ("082519", "reheater", "noun", "/ˌriːˈhiːtər/", "bộ quá nhiệt trung gian; lò hâm"),
    ("082520", "reheating", "verb", "/ˌriːˈhiːtɪŋ/", "hâm nóng lại, nung nóng trở lại"),
    ("082521", "reheats", "verb", "/ˌriːˈhiːts/", "hâm nóng lại, đun nóng trở lại"),
    ("082522", "reheel", "verb", "/ˌriːˈhiːl/", "đóng lại gót giày, thay gót mới"),
    ("082523", "rehumiliate", "verb", "/ˌriːhjuːˈmɪliˌeɪt/", "làm bẽ mặt, làm nhục lại lần nữa"),
    ("082524", "rehumiliated", "verb", "/ˌriːhjuːˈmɪliˌeɪtɪd/", "đã làm bẽ mặt, làm nhục lại"),
    ("082525", "rehumiliates", "verb", "/ˌriːhjuːˈmɪliˌeɪts/", "làm bẽ mặt, làm nhục thêm lần nữa"),
    ("082526", "rehumiliating", "verb", "/ˌriːhjuːˈmɪliˌeɪtɪŋ/", "làm bẽ mặt, hạ nhục lại lần nữa"),
    ("082527", "rehung", "verb", "/ˌriːˈhʌŋ/", "đã treo lại (tranh, cửa, chuông)"),
    ("082528", "rei", "noun", "/reɪ/", "đồng rây (tiền cổ Bồ Đào Nha)"),
    ("082529", "reiber", "noun", "/ˈraɪbər/", "tên họ Reiber (tiếng Đức-Anh)"),
    ("082530", "reibers", "noun", "/ˈraɪbərz/", "gia đình họ Reiber"),
    ("082531", "reichstag", "noun", "/ˈraɪkstɑːɡ/", "tòa nhà Quốc hội Đức Reichstag"),
    ("082532", "reificatory", "adj", "/ˌriːəfəˈkeɪtəri/", "mang tính vật hóa (triết học)"),
    ("082533", "reigle", "noun", "/ˈriːɡəl/", "đường rãnh dẫn hướng, hào rãnh (cổ)"),
    ("082534", "reigned", "verb", "/reɪnd/", "đã trị vì, thống trị; ngự trị"),
    ("082535", "reignition", "noun", "/ˌriːɪɡˈnɪʃən/", "sự đánh lửa lại, sự bùng cháy lại"),
    ("082536", "reigns", "verb", "/reɪnz/", "trị vì, cai trị; chiếm ưu thế"),
    ("082537", "reimbursable", "adj", "/ˌriːɪmˈbɜːrsəbəl/", "được hoàn trả chi phí, bồi hoàn lại"),
    ("082538", "reimbursed", "verb", "/ˌriːɪmˈbɜːrst/", "đã hoàn trả lại tiền chi tiêu"),
    ("082539", "reimburses", "verb", "/ˌriːɪmˈbɜːrsɪz/", "hoàn trả, bồi hoàn lại chi phí"),
    ("082540", "reimbursing", "verb", "/ˌriːɪmˈbɜːrsɪŋ/", "hoàn trả tiền, bồi hoàn chi phí"),
    ("082541", "reimport", "verb", "/ˌriːɪmˈpɔːrt/", "tái nhập khẩu hàng đã xuất đi"),
    ("082542", "reimportation", "noun", "/ˌriːɪmpɔːrˈteɪʃən/", "sự tái nhập khẩu hàng hóa"),
    ("082543", "reincarnated", "verb", "/ˌriːɪnˈkɑːrneɪtɪd/", "đã đầu thai, tái sinh kiếp khác"),
    ("082544", "reincarnates", "verb", "/ˌriːɪnˈkɑːrneɪts/", "đầu thai, tái sinh sang kiếp mới"),
    ("082545", "reincarnating", "verb", "/ˌriːɪnˈkɑːrneɪtɪŋ/", "đầu thai, hóa thân thành kiếp mới"),
    ("082546", "reincarnationism", "noun", "/ˌriːɪnkɑːrˈneɪʃəˌnɪzəm/", "thuyết luân hồi đầu thai"),
    ("082547", "reincorporate", "verb", "/ˌriːɪnˈkɔːrpəˌreɪt/", "tái sáp nhập, hợp nhất trở lại"),
    ("082548", "reincorporated", "verb", "/ˌriːɪnˈkɔːrpəˌreɪtɪd/", "đã tái sáp nhập, kết hợp trở lại"),
    ("082549", "reincorporates", "verb", "/ˌriːɪnˈkɔːrpəˌreɪts/", "tái sáp nhập, lồng ghép trở lại"),
    ("082550", "reincorporating", "verb", "/ˌriːɪnˈkɔːrpəˌreɪtɪŋ/", "tái sáp nhập, hợp nhất trở lại"),
    ("082551", "reincrease", "verb", "/ˌriːɪnˈkriːs/", "tăng trở lại, làm tăng thêm nữa"),
    ("082552", "reindeermoss", "noun", "/ˈreɪndɪrˌmɔːs/", "địa y tuần lộc (vùng đài nguyên)"),
    ("082553", "reinduce", "verb", "/ˌriːɪnˈduːs/", "lại xui khiến, gây cảm ứng lại"),
    ("082554", "reined", "verb", "/reɪnd/", "đã cầm cương, đã kìm giữ chặt"),
    ("082555", "reinforces", "verb", "/ˌriːɪnˈfɔːrsɪz/", "củng cố, gia cố, tăng cường lực"),
    ("082556", "reinforcing", "verb", "/ˌriːɪnˈfɔːrsɪŋ/", "củng cố, gia cố, tăng cường thêm"),
    ("082557", "reingratiate", "verb", "/ˌriːɪnˈɡreɪʃiˌeɪt/", "lấy lại cảm tình, lấy lòng trở lại"),
    ("082558", "reinhabit", "verb", "/ˌriːɪnˈhæbɪt/", "quay lại sinh sống, cư trú trở lại"),
    ("082559", "reinhabited", "verb", "/ˌriːɪnˈhæbɪtɪd/", "đã quay lại sinh sống, cư trú lại"),
    ("082560", "reinhabiting", "verb", "/ˌriːɪnˈhæbɪtɪŋ/", "quay lại định cư, cư trú trở lại"),
    ("082561", "reinhabits", "verb", "/ˌriːɪnˈhæbɪts/", "quay lại sinh sống ở nơi cũ"),
    ("082562", "reining", "verb", "/ˈreɪnɪŋ/", "kéo dây cương; kiềm chế, kìm hãm"),
    ("082563", "reinject", "verb", "/ˌriːɪnˈdʒɛkt/", "tiêm lại; bơm đưa trở lại vào"),
    ("082564", "reinless", "adj", "/ˈreɪnləs/", "không có dây cương; không kiềm chế"),
    ("082565", "reins", "verb", "/reɪnz/", "cầm cương, điều khiển; kiềm chế"),
    ("082566", "reinsert", "verb", "/ˌriːɪnˈsɜːrt/", "chèn lại, lắp gài trở lại vào"),
    ("082567", "reinserted", "verb", "/ˌriːɪnˈsɜːrtɪd/", "đã chèn lại, đã lồng gài trở lại"),
    ("082568", "reinserting", "verb", "/ˌriːɪnˈsɜːrtɪŋ/", "chèn lại, lắp đặt lại vào chỗ cũ"),
    ("082569", "reinserts", "verb", "/ˌriːɪnˈsɜːrts/", "chèn lại, đưa gài trở lại vào"),
    ("082570", "reinsman", "noun", "/ˈreɪnzmən/", "người đánh xe ngựa, tay đua xe ngựa"),
    ("082571", "reinspection", "noun", "/ˌriːɪnˈspɛkʃən/", "sự kiểm tra lại, sự thanh tra lại"),
    ("082572", "reinstalled", "verb", "/ˌriːɪnˈstɔːld/", "đã cài đặt lại; đã tái bổ nhiệm"),
    ("082573", "reinstalling", "verb", "/ˌriːɪnˈstɔːlɪŋ/", "cài đặt lại (phần mềm); lắp lại"),
    ("082574", "reinstated", "verb", "/ˌriːɪnˈsteɪtɪd/", "đã phục chức, đã khôi phục lại"),
    ("082575", "reinstates", "verb", "/ˌriːɪnˈsteɪts/", "phục chức, khôi phục lại như cũ"),
    ("082576", "reinstating", "verb", "/ˌriːɪnˈsteɪtɪŋ/", "phục chức, khôi phục hiệu lực cũ"),
    ("082577", "reintegrated", "verb", "/ˌriːˈɪntəˌɡreɪtɪd/", "đã tái hòa nhập, hợp nhất trở lại"),
    ("082578", "reintegrates", "verb", "/ˌriːˈɪntəˌɡreɪts/", "tái hòa nhập cộng đồng; hợp nhất"),
    ("082579", "reintegrating", "verb", "/ˌriːˈɪntəˌɡreɪtɪŋ/", "tái hòa nhập cộng đồng; hợp nhất"),
    ("082580", "reinter", "verb", "/ˌriːɪnˈtɜːr/", "cải táng, chôn cất lại hài cốt"),
    ("082581", "reintermediation", "noun", "/ˌriːɪntərˌmiːdiˈeɪʃən/", "sự tái xuất hiện khâu trung gian"),
    ("082582", "reinthrone", "verb", "/ˌriːɪnˈθroʊn/", "phục vị, đưa trở lại ngai vàng"),
    ("082583", "reintroduced", "verb", "/ˌriːɪntrəˈduːst/", "đã giới thiệu lại; đã thả về rừng"),
    ("082584", "reintroduces", "verb", "/ˌriːɪntrəˈduːsɪz/", "tái đưa vào; giới thiệu trở lại"),
    ("082585", "reintroducing", "verb", "/ˌriːɪntrəˈduːsɪŋ/", "tái đưa vào, thả loài về tự nhiên"),
    ("082586", "reinvasion", "noun", "/ˌriːɪnˈveɪʒən/", "cuộc tái xâm lược, sự xâm nhập lại"),
    ("082587", "reinvestigate", "verb", "/ˌriːɪnˈvɛstəˌɡeɪt/", "tái điều tra, điều tra lại vụ án"),
    ("082588", "reinvestment", "noun", "/ˌriːɪnˈvɛstmənt/", "sự tái đầu tư lợi nhuận thu được"),
    ("082589", "reissued", "verb", "/ˌriːˈɪʃuːd/", "đã tái bản, đã phát hành lại"),
    ("082590", "reissues", "verb", "/ˌriːˈɪʃuːz/", "tái bản, phát hành lại (sách, thẻ)"),
    ("082591", "reissuing", "verb", "/ˌriːˈɪʃuːɪŋ/", "tái bản, phát hành lại ấn phẩm cũ"),
    ("082592", "reiterated", "verb", "/riˈɪtəˌreɪtɪd/", "đã nhắc đi nhắc lại để nhấn mạnh"),
    ("082593", "reiterates", "verb", "/riˈɪtəˌreɪts/", "nhắc đi nhắc lại, khẳng định lại"),
    ("082594", "reiterating", "verb", "/riˈɪtəˌreɪtɪŋ/", "nhắc đi nhắc lại, lặp lại lần nữa"),
    ("082595", "reithrodontomys", "noun", "/ˌriːθroʊˈdɑːntəmɪs/", "chi chuột đồng gặt châu Mỹ"),
    ("082596", "reiver", "noun", "/ˈriːvər/", "kẻ cướp biên giới Scotland xưa"),
    ("082597", "rejectable", "adj", "/rɪˈdʒɛktəbəl/", "có thể bác bỏ, có thể loại bỏ"),
    ("082598", "rejectamenta", "noun", "/rɪˌdʒɛktəˈmɛntə/", "chất thải loại, phần bị gạt bỏ"),
    ("082599", "rejecting", "verb", "/rɪˈdʒɛktɪŋ/", "từ chối, bác bỏ, loại bỏ ra"),
    ("082600", "rejective", "adj", "/rɪˈdʒɛktɪv/", "có tính bài xích, hay khước từ"),
    ("082601", "rejects", "verb", "/rɪˈdʒɛkts/", "từ chối, bác bỏ, thải loại"),
    ("082602", "rejigged", "verb", "/ˌriːˈdʒɪɡd/", "đã sắp xếp lại, điều chỉnh lại máy"),
]

raw = json.load(open("scratch/b37_r06_raw_p1.json"))
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
with open("scratch/b37_r06_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r06_p1 saved OK")
