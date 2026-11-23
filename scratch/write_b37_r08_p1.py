import json

RECORDS = [
    ("083503", "reverser", "noun", "/rɪˈvɜːrsər/", "bộ đảo chiều; thiết bị đối chiếu"),
    ("083504", "reverses", "verb", "/rɪˈvɜːrsɪz/", "đảo ngược; lùi lại"),
    ("083505", "reversing", "verb", "/rɪˈvɜːrsɪŋ/", "đang đảo ngược; đang lùi lại"),
    ("083506", "reversional", "adj", "/rɪˈvɜːrʒənəl/", "thuộc quyền hoàn trả; quyền hồi quy"),
    ("083507", "reversioner", "noun", "/rɪˈvɜːrʒənər/", "người có quyền thừa kế hoàn lại"),
    ("083508", "reversionist", "noun", "/rɪˈvɜːrʒənɪst/", "người tái phạm; người muốn quay lại"),
    ("083509", "reversive", "adj", "/rɪˈvɜːrsɪv/", "có xu hướng quay ngược lại"),
    ("083510", "reverted", "verb", "/rɪˈvɜːrtɪd/", "đã quay trở lại; đã hoàn lại"),
    ("083511", "revertible", "adj", "/rɪˈvɜːrtəbəl/", "có thể hoàn lại; có thể trả lại"),
    ("083512", "reverts", "verb", "/rɪˈvɜːrts/", "quay trở lại; hoàn lại"),
    ("083513", "revet", "verb", "/rɪˈvɛt/", "xây kè chắn; lát đá ốp tường"),
    ("083514", "revetement", "noun", "/rɪˈvɛtmənt/", "tường chắn; lớp kè bảo vệ"),
    ("083515", "reviewal", "noun", "/rɪˈvjuːəl/", "sự xem xét lại; sự duyệt lại"),
    ("083516", "reviewed", "verb", "/rɪˈvjuːd/", "đã xem xét lại; đã đánh giá"),
    ("083517", "reviewers", "noun", "/rɪˈvjuːərz/", "người đánh giá; nhà phê bình"),
    ("083518", "reviewing", "verb", "/rɪˈvjuːɪŋ/", "đang xem xét lại; đang đánh giá"),
    ("083519", "reviews", "verb", "/rɪˈvjuːz/", "xem xét lại; đánh giá"),
    ("083520", "revilalize", "verb", "/ˌriːˈvaɪtəˌlaɪz/", "tiếp thêm sức sống; hồi sinh"),
    ("083521", "reviled", "verb", "/rɪˈvaɪld/", "đã chửi rủa; đã lăng mạ"),
    ("083522", "revilement", "noun", "/rɪˈvaɪlmənt/", "lời lăng mạ; sự chửi rủa"),
    ("083523", "reviler", "noun", "/rɪˈvaɪlər/", "kẻ chửi rủa; người mắng nhiếc"),
    ("083524", "reviles", "verb", "/rɪˈvaɪlz/", "chửi rủa; lăng mạ"),
    ("083525", "reviling", "verb", "/rɪˈvaɪlɪŋ/", "đang chửi rủa; đang lăng mạ"),
    ("083526", "revisable", "adj", "/rɪˈvaɪzəbəl/", "có thể sửa lại; xét lại được"),
    ("083527", "revisal", "noun", "/rɪˈvaɪzəl/", "sự sửa lại; sự hiệu đính"),
    ("083528", "revises", "verb", "/rɪˈvaɪzɪz/", "sửa lại; ôn tập lại"),
    ("083529", "revisional", "adj", "/rɪˈvɪʒənəl/", "thuộc sự xem xét lại; duyệt lại"),
    ("083530", "revisited", "verb", "/ˌriːˈvɪzɪtɪd/", "đã thăm lại; đã trở lại"),
    ("083531", "revisiting", "verb", "/ˌriːˈvɪzɪtɪŋ/", "đang thăm lại; đang trở lại"),
    ("083532", "revisits", "verb", "/ˌriːˈvɪzɪts/", "thăm lại; trở lại"),
    ("083533", "revisory", "adj", "/rɪˈvaɪzəri/", "để xem lại; có tính duyệt lại"),
    ("083534", "revitalises", "verb", "/ˌriːˈvaɪtəˌlaɪzɪz/", "hồi sinh; tiếp thêm sức sống"),
    ("083535", "revitalizes", "verb", "/ˌriːˈvaɪtəˌlaɪzɪz/", "hồi sinh; tiếp thêm sức sống"),
    ("083536", "revivalistic", "adj", "/rɪˌvaɪvəˈlɪstɪk/", "thuộc phong trào phục hưng"),
    ("083537", "revivals", "noun", "/rɪˈvaɪvəlz/", "sự phục hưng; sự hồi sinh"),
    ("083538", "reviver", "noun", "/rɪˈvaɪvər/", "người hồi sinh; chất phục hồi"),
    ("083539", "revives", "verb", "/rɪˈvaɪvz/", "hồi sinh; làm sống lại"),
    ("083540", "revivifier", "noun", "/rɪˈvɪvəˌfaɪər/", "chất phục hoạt; chất làm sống lại"),
    ("083541", "reviviscence", "noun", "/ˌrɛvɪˈvɪsəns/", "sự sống lại; sự phục hồi"),
    ("083542", "reviviscent", "adj", "/ˌrɛvɪˈvɪsənt/", "đang hồi sinh; sống lại"),
    ("083543", "revocability", "noun", "/ˌrɛvəkəˈbɪlɪti/", "tính có thể hủy bỏ"),
    ("083544", "revocatory", "adj", "/rɪˈvɑːkəˌtɔːri/", "có tính hủy bỏ; thu hồi"),
    ("083545", "revokable", "adj", "/rɪˈvoʊkəbəl/", "có thể hủy bỏ; có thể thu hồi"),
    ("083546", "revoked", "verb", "/rɪˈvoʊkt/", "đã thu hồi; đã hủy bỏ"),
    ("083547", "revokes", "verb", "/rɪˈvoʊks/", "thu hồi; hủy bỏ"),
    ("083548", "revoking", "verb", "/rɪˈvoʊkɪŋ/", "đang thu hồi; đang hủy bỏ"),
    ("083549", "revolted", "verb", "/rɪˈvoʊltɪd/", "đã nổi dậy; đã làm kinh tởm"),
    ("083550", "revolter", "noun", "/rɪˈvoʊltər/", "người nổi dậy; kẻ phản kháng"),
    ("083551", "revolts", "verb", "/rɪˈvoʊlts/", "nổi dậy; gây phẫn nộ"),
    ("083552", "revolute", "adj", "/ˈrɛvəˌluːt/", "cuốn mép ra ngoài (lá)"),
    ("083553", "revolutionised", "verb", "/ˌrɛvəˈluːʃəˌnaɪzd/", "đã cách mạng hóa"),
    ("083554", "revolutionises", "verb", "/ˌrɛvəˈluːʃəˌnaɪzɪz/", "cách mạng hóa"),
    ("083555", "revolutionising", "verb", "/ˌrɛvəˈluːʃəˌnaɪzɪŋ/", "đang cách mạng hóa"),
    ("083556", "revolutionism", "noun", "/ˌrɛvəˈluːʃəˌnɪzəm/", "chủ nghĩa cách mạng"),
    ("083557", "revolutionized", "verb", "/ˌrɛvəˈluːʃəˌnaɪzd/", "đã cách mạng hóa"),
    ("083558", "revolutionizes", "verb", "/ˌrɛvəˈluːʃəˌnaɪzɪz/", "cách mạng hóa"),
    ("083559", "revolutionizing", "verb", "/ˌrɛvəˈluːʃəˌnaɪzɪŋ/", "đang cách mạng hóa"),
    ("083560", "revolutions", "noun", "/ˌrɛvəˈluːʃənz/", "cuộc cách mạng; vòng quay"),
    ("083561", "revolves", "verb", "/rɪˈvɑːlvz/", "quay quanh; xoay quanh"),
    ("083562", "revolving", "verb", "/rɪˈvɑːlvɪŋ/", "đang quay quanh; đang xoay"),
    ("083563", "revs", "verb", "/rɛvz/", "tăng vòng tua máy; rồ ga"),
    ("083564", "revulsive", "adj", "/rɪˈvʌlsɪv/", "làm đổi hướng bệnh; gây ghê tởm"),
    ("083565", "revved", "verb", "/rɛvd/", "đã tăng vòng tua; đã rồ ga"),
    ("083566", "revving", "verb", "/ˈrɛvɪŋ/", "đang tăng vòng tua; đang rồ ga"),
    ("083567", "rewardable", "adj", "/rɪˈwɔːrdəbəl/", "đáng được khen thưởng"),
    ("083568", "rewarded", "verb", "/rɪˈwɔːrdɪd/", "đã khen thưởng; đã đền đáp"),
    ("083569", "rewarder", "noun", "/rɪˈwɔːrdər/", "người ban thưởng"),
    ("083570", "rewardful", "adj", "/rɪˈwɔːrdfəl/", "xứng đáng; mang lại phần thưởng"),
    ("083571", "rewardingly", "adv", "/rɪˈwɔːrdɪŋli/", "xứng đáng; mang lại kết quả tốt"),
    ("083572", "rewards", "verb", "/rɪˈwɔːrdz/", "khen thưởng; đền đáp"),
    ("083573", "rewash", "verb", "/ˌriːˈwɑːʃ/", "rửa lại; giặt lại"),
    ("083574", "rewashed", "verb", "/ˌriːˈwɑːʃt/", "đã rửa lại; đã giặt lại"),
    ("083575", "rewashes", "verb", "/ˌriːˈwɑːʃɪz/", "rửa lại; giặt lại"),
    ("083576", "rewashing", "verb", "/ˌriːˈwɑːʃɪŋ/", "đang rửa lại; đang giặt lại"),
    ("083577", "rewater", "noun", "/ˌriːˈwɔːtər/", "nước tái sử dụng"),
    ("083578", "rewinder", "noun", "/ˌriːˈwaɪndər/", "máy cuộn lại; bộ tua lại"),
    ("083579", "rewinders", "noun", "/ˌriːˈwaɪndərz/", "máy cuộn lại; bộ tua lại"),
    ("083580", "rewound", "verb", "/ˌriːˈwaʊnd/", "đã cuộn lại; đã lên dây lại"),
    ("083581", "rewritten", "verb", "/ˌriːˈrɪtən/", "đã viết lại; đã chép lại"),
    ("083582", "rewrote", "verb", "/ˌriːˈroʊt/", "đã viết lại; đã chép lại"),
    ("083583", "rfc", "noun", "/ˌɑːrˌɛfˈsiː/", "tài liệu chuẩn RFC"),
    ("083584", "rfna", "noun", "/ˌɑːrˌɛfˌɛnˈeɪ/", "axit nitric bốc khói đỏ (RFNA)"),
    ("083585", "rhabdoid", "noun", "/ˈræbdɔɪd/", "thể hình que"),
    ("083586", "rhabdoith", "noun", "/ˈræbdəˌlɪθ/", "sỏi hình que; viên đá vôi nhỏ"),
    ("083587", "rhabdomancer", "noun", "/ˈræbdəˌmænsər/", "người bói gậy; thầy dò mạch nước"),
    ("083588", "rhabdomancy", "noun", "/ˈræbdəˌmænsi/", "thuật bói gậy; phép dò mạch nước"),
    ("083589", "rhabdome", "noun", "/ˈræbdoʊm/", "thể que cảm quang mắt kép"),
    ("083590", "rhabdomere", "noun", "/ˈræbdəˌmɪr/", "tiểu thể que cảm quang"),
    ("083591", "rhabdomyoma", "noun", "/ˌræbdoʊmaɪˈoʊmə/", "u cơ vân lành tính"),
    ("083592", "rhabdosarcoma", "noun", "/ˌræbdoʊsɑːrˈkoʊmə/", "sarcoma cơ vân"),
    ("083593", "rhabdoviridae", "noun", "/ˌræbdoʊˈvɪrɪˌdiː/", "họ virus Rhabdoviridae"),
    ("083594", "rhabdovirus", "noun", "/ˌræbdoʊˈvaɪrəs/", "virus hình que (gây bệnh dại)"),
    ("083595", "rhagades", "noun", "/ˈræɡəˌdiːz/", "vết nứt kẽ da"),
    ("083596", "rhamnaceae", "noun", "/ræmˈneɪsiːˌiː/", "họ Táo ta (Rhamnaceae)"),
    ("083597", "rhamnaceous", "adj", "/ræmˈneɪʃəs/", "thuộc họ Táo ta"),
    ("083598", "rhamnales", "noun", "/ræmˈneɪliːz/", "bộ Táo ta (Rhamnales)"),
    ("083599", "rhaphe", "noun", "/ˈreɪfi/", "đường khâu; đường sống hạt"),
    ("083600", "rhapis", "noun", "/ˈreɪpɪs/", "chi Cọ trúc (Rhapis)"),
    ("083601", "rhapsode", "noun", "/ˈræpsoʊd/", "người ngâm sử thi Hy Lạp cổ"),
    ("083602", "rhapsodical", "adj", "/ræpˈsɑːdɪkəl/", "dạt dào cảm xúc; khoa trương"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r08_raw_p1.json"))
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

json.dump(out, open("scratch/b37_r08_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b37_r08_p1 saved OK")
