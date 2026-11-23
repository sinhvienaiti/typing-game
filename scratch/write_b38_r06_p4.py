import json

RECORDS = [
    ("087803", "sniggerer", "noun", "/ˈsnɪɡərər/", "người cười khẩy chế nhạo"),
    ("087804", "sniggering", "verb", "/ˈsnɪɡərɪŋ/", "đang cười khẩy chế nhạo"),
    ("087805", "sniggers", "noun", "/ˈsnɪɡərz/", "tiếng cười khẩy chế nhạo"),
    ("087806", "sniggle", "verb", "/ˈsnɪɡəl/", "câu lươn trong hang bằng mồi"),
    ("087807", "sniped", "verb", "/snaɪpt/", "đã bắn tỉa; đã chỉ trích lén"),
    ("087808", "snipefish", "noun", "/ˈsnaɪpˌfɪʃ/", "cá mỏ nhọn biển (họ Macroramphosidae)"[:35]),
    ("087809", "snipers", "noun", "/ˈsnaɪpərz/", "lính bắn tỉa; tay súng ngắm"),
    ("087810", "snipes", "verb", "/snaɪps/", "bắn tỉa; chỉ trích ngấm ngầm"),
    ("087811", "sniping", "verb", "/ˈsnaɪpɪŋ/", "đang bắn tỉa; đang công kích lén"),
    ("087812", "snipped", "verb", "/snɪpt/", "đã cắt tỉa nhanh bằng kéo"),
    ("087813", "snipper", "noun", "/ˈsnɪpər/", "thợ cắt xén; cái kéo nhỏ cắt cành"),
    ("087814", "snippers", "noun", "/ˈsnɪpərz/", "kéo cắt kim loại hay cắt cành"),
    ("087815", "snippety", "adj", "/ˈsnɪpɪti/", "rời rạc vụn vặt; xấc xược châm chọc"[:35]),
    ("087816", "snippiness", "noun", "/ˈsnɪpinəs/", "thái độ xấc xược cộc cằn"),
    ("087817", "snippy", "adj", "/ˈsnɪpi/", "cộc cằn khó chịu; cắt xén vụn vặt"),
    ("087818", "snipy", "adj", "/ˈsnaɪpi/", "nhọn dài như mỏ chim dẽ giun"),
    ("087819", "snitcher", "noun", "/ˈsnɪtʃər/", "kẻ mách lẻo chỉ điểm; tên trộm vặt"),
    ("087820", "sniveler", "noun", "/ˈsnɪvələr/", "người hay khóc lóc than vãn"),
    ("087821", "snivelled", "verb", "/ˈsnɪvəld/", "đã sụt sịt khóc lóc; rên rỉ than"),
    ("087822", "sniveller", "noun", "/ˈsnɪvələr/", "người hay than vãn nhõng nhẽo"),
    ("087823", "snivelling", "verb", "/ˈsnɪvəlɪŋ/", "đang sụt sịt khóc lóc; than vãn"),
    ("087824", "snivels", "verb", "/ˈsnɪvəlz/", "sụt sịt khóc lóc; than vãn giả vờ"),
    ("087825", "snobberies", "noun", "/ˈsnɑːbəriz/", "thói hợm hĩnh trưởng giả"),
    ("087826", "snobbishnesses", "noun", "/ˈsnɑːbɪʃnəsɪz/", "tính hợm hĩnh khinh người"),
    ("087827", "snobbism", "noun", "/ˈsnɑːˌbɪzəm/", "thói hợm hĩnh trọng giàu khinh nghèo"[:35]),
    ("087828", "snobocracies", "noun", "/snɑːˈbɑːkrəsiz/", "giới trưởng giả hợm hĩnh cầm quyền"[:35]),
    ("087829", "snobocracy", "noun", "/snɑːˈbɑːkrəsi/", "chính quyền trưởng giả hợm hĩnh"),
    ("087830", "snobol", "noun", "/ˈsnoʊˌbɑːl/", "ngôn ngữ lập trình SNOBOL"),
    ("087831", "snogged", "verb", "/snɑːɡd/", "đã hôn môi nồng nhiệt (lóng Anh)"),
    ("087832", "snogs", "verb", "/snɑːɡz/", "hôn môi nồng nhiệt (lóng Anh)"),
    ("087833", "snookered", "verb", "/ˈsnʊkərd/", "đã bị đẩy vào thế bí tiến thoái"),
    ("087834", "snookering", "verb", "/ˈsnʊkərɪŋ/", "đang đẩy đối thủ vào thế bí"),
    ("087835", "snookers", "verb", "/ˈsnʊkərz/", "đẩy vào thế bí khó xoay xở"),
    ("087836", "snooped", "verb", "/snuːpt/", "đã rình mò xoi mói chuyện riêng"),
    ("087837", "snoopiness", "noun", "/ˈsnuːpinəs/", "tính tò mò hay xoi mói"),
    ("087838", "snooping", "verb", "/ˈsnuːpɪŋ/", "đang rình mò xoi mói bí mật"),
    ("087839", "snoops", "verb", "/snuːps/", "rình mò; xoi mói chuyện người khác"[:35]),
    ("087840", "snootily", "adv", "/ˈsnuːtɪli/", "kênh kiệu; ra vẻ khinh người"),
    ("087841", "snootiness", "noun", "/ˈsnuːtinəs/", "thái độ kênh kiệu hợm hĩnh"),
    ("087842", "snoozed", "verb", "/snuːzd/", "đã ngủ gật; đã chợp mắt ngắn"),
    ("087843", "snoozes", "verb", "/ˈsnuːzɪz/", "ngủ gật; chợp mắt nghỉ ngơi"),
    ("087844", "snoozing", "verb", "/ˈsnuːzɪŋ/", "đang ngủ gật; đang chợp mắt ngắn"),
    ("087845", "snored", "verb", "/snɔːrd/", "đã ngủ ngáy khò khò"),
    ("087846", "snores", "verb", "/snɔːrz/", "ngủ ngáy"),
    ("087847", "snorted", "verb", "/ˈsnɔːrtɪd/", "đã khịt mũi khinh bỉ; hít chất"),
    ("087848", "snorts", "verb", "/snɔːrts/", "khịt mũi tỏ thái độ; hít bằng mũi"),
    ("087849", "snorty", "adj", "/ˈsnɔːrti/", "hay gắt gỏng cáu kỉnh; khinh khỉnh"),
    ("087850", "snottiness", "noun", "/ˈsnɑːtinəs/", "thái độ xấc xược; tình trạng sổ mũi"[:35]),
    ("087851", "snouted", "adj", "/ˈsnaʊtɪd/", "có mõm dài; có vòng mũi (lợn)"),
    ("087852", "snouty", "adj", "/ˈsnaʊti/", "có mũi dài giống mõm; xấc xược"),
    ("087853", "snowballed", "verb", "/ˈsnoʊˌbɔːld/", "đã tăng nhanh như quả cầu tuyết"),
    ("087854", "snowballing", "verb", "/ˈsnoʊˌbɔːlɪŋ/", "đang tăng nhanh theo cấp số nhân"),
    ("087855", "snowballs", "verb", "/ˈsnoʊˌbɔːlz/", "tăng vọt nhanh; ném bóng tuyết"),
    ("087856", "snowbells", "noun", "/ˈsnoʊˌbɛlz/", "cây hoa chuông tuyết Styrax"),
    ("087857", "snowblind", "adj", "/ˈsnoʊˌblaɪnd/", "bị lòa mắt tạm thời vì ánh tuyết"),
    ("087858", "snowblindness", "noun", "/ˈsnoʊˌblaɪndnəs/", "chứng mù lòa tạm thời do tuyết"),
    ("087859", "snowdropper", "noun", "/ˈsnoʊˌdrɑːpər/", "kẻ trộm quần áo phơi trên dây (Úc)"[:35]),
    ("087860", "snowdrops", "noun", "/ˈsnoʊˌdrɑːps/", "hoa giọt tuyết báo xuân"),
    ("087861", "snowed", "verb", "/snoʊd/", "đã có tuyết rơi; đã lừa khéo"),
    ("087862", "snowfalls", "noun", "/ˈsnoʊˌfɔːlz/", "trận tuyết rơi; lượng tuyết rơi"),
    ("087863", "snowglobe", "noun", "/ˈsnoʊˌɡloʊb/", "quả cầu tuyết thủy tinh trang trí"),
    ("087864", "snowglobes", "noun", "/ˈsnoʊˌɡloʊbz/", "quả cầu tuyết thủy tinh trang trí"),
    ("087865", "snowily", "adv", "/ˈsnoʊɪli/", "trắng xóa như tuyết; đầy tuyết"),
    ("087866", "snowiness", "noun", "/ˈsnoʊinəs/", "tình trạng phủ đầy tuyết trắng"),
    ("087867", "snowinesses", "noun", "/ˈsnoʊinəsɪz/", "vẻ trắng muốt như tuyết"),
    ("087868", "snowing", "verb", "/ˈsnoʊɪŋ/", "đang có tuyết rơi"),
    ("087869", "snowless", "adj", "/ˈsnoʊləs/", "không có tuyết rơi"),
    ("087870", "snowline", "noun", "/ˈsnoʊˌlaɪn/", "đường ranh giới tuyết vĩnh cửu"),
    ("087871", "snowlines", "noun", "/ˈsnoʊˌlaɪnz/", "đường ranh giới tuyết vĩnh cửu"),
    ("087872", "snowmen", "noun", "/ˈsnoʊˌmɛn/", "người tuyết đắp chơi"),
    ("087873", "snows", "verb", "/snoʊz/", "có tuyết rơi; phủ tuyết; lừa khéo"),
    ("087874", "snowstorms", "noun", "/ˈsnoʊˌstɔːrmz/", "bão tuyết"),
    ("087875", "snr", "noun", "/ˌɛsˌɛnˈɑːr/", "tỷ số tín hiệu trên nhiễu; người lớn"[:35]),
    ("087876", "snubbed", "verb", "/snʌbd/", "đã phớt lờ hắt hủi; đã buộc dây"),
    ("087877", "snubber", "noun", "/ˈsnʌbər/", "bộ giảm chấn; mạch dập xung"),
    ("087878", "snubbing", "verb", "/ˈsnʌbɪŋ/", "đang phớt lờ hắt hủi; đang kìm lại"),
    ("087879", "snubbingly", "adv", "/ˈsnʌbɪŋli/", "lạnh nhạt phớt lờ; cắt ngang"),
    ("087880", "snubs", "verb", "/snʌbz/", "phớt lờ lạnh nhạt; hắt hủi ai"),
    ("087881", "snuffed", "verb", "/snʌft/", "đã tắt ngấm (nến); đã hít thuốc"),
    ("087882", "snuffiness", "noun", "/ˈsnʌfinəs/", "tính chất như thuốc lá hít; cáu"),
    ("087883", "snuffing", "verb", "/ˈsnʌfɪŋ/", "đang dập tắt nến; đang hít mạnh"),
    ("087884", "snuffingly", "adv", "/ˈsnʌfɪŋli/", "giọng nghẹt mũi; hít khịt mũi"),
    ("087885", "snuffled", "verb", "/ˈsnʌfəld/", "đã khụt khịt mũi; nói giọng mũi"),
    ("087886", "snuffler", "noun", "/ˈsnʌflər/", "người thở khụt khịt mũi"),
    ("087887", "snuffles", "verb", "/ˈsnʌfəlz/", "khụt khịt mũi; nói giọng nghẹt mũi"),
    ("087888", "snuffly", "adj", "/ˈsnʌfli/", "hay khụt khịt mũi; nghẹt mũi"),
    ("087889", "snuffs", "verb", "/snʌfs/", "dập tắt ngọn nến; hít thuốc bột"),
    ("087890", "snuffy", "adj", "/ˈsnʌfi/", "vấy thuốc hít; màu nâu thuốc hít"),
    ("087891", "snugged", "verb", "/snʌɡd/", "đã nằm cuộn ấm áp; chằng buộc gọn"),
    ("087892", "snuggeries", "noun", "/ˈsnʌɡəriz/", "góc phòng nhỏ ấm cúng riêng tư"),
    ("087893", "snuggery", "noun", "/ˈsnʌɡəri/", "căn phòng nhỏ ấm cúng; xó riêng"),
    ("087894", "snugging", "verb", "/ˈsnʌɡɪŋ/", "đang thu mình ấm áp; đang thu gọn"),
    ("087895", "snuggles", "verb", "/ˈsnʌɡəlz/", "rúc vào ôm ấp ấm áp"),
    ("087896", "snugs", "verb", "/snʌɡz/", "thu mình ấm áp; buộc chặt gọn gàng"),
    ("087897", "soakage", "noun", "/ˈsoʊkɪdʒ/", "sự ngâm ướt; lượng nước thấm vào"),
    ("087898", "soaks", "verb", "/soʊks/", "ngâm nước; thấm đẫm; uống say mèm"),
    ("087899", "soapberry", "noun", "/ˈsoʊpˌbɛri/", "cây bồ hòn; quả bồ hòn"),
    ("087900", "soapdisk", "noun", "/ˈsoʊpˌdɪsk/", "đĩa đựng bánh xà phòng"),
    ("087901", "soapdisks", "noun", "/ˈsoʊpˌdɪsks/", "đĩa đựng bánh xà phòng"),
    ("087902", "soaped", "verb", "/soʊpt/", "đã xoa xà phòng; đã gội xà phòng"),
]

# Replace all slices cleanly <= 35 chars
RECORDS[5] = ("087808", "snipefish", "noun", "/ˈsnaɪpˌfɪʃ/", "cá mỏ nhọn biển Macroramphosus")
RECORDS[12] = ("087815", "snippety", "adj", "/ˈsnɪpɪti/", "rời rạc vụn vặt; xấc xược châm biếm"[:35])
RECORDS[12] = ("087815", "snippety", "adj", "/ˈsnɪpɪti/", "rời rạc vụn vặt; xấc xược")
RECORDS[24] = ("087827", "snobbism", "noun", "/ˈsnɑːˌbɪzəm/", "thói hợm hĩnh khinh người")
RECORDS[25] = ("087828", "snobocracies", "noun", "/snɑːˈbɑːkrəsiz/", "giới trưởng giả hợm hĩnh cầm quyền"[:35])
RECORDS[25] = ("087828", "snobocracies", "noun", "/snɑːˈbɑːkrəsiz/", "chế độ giới trưởng giả hợm hĩnh")
RECORDS[36] = ("087839", "snoops", "verb", "/snuːps/", "rình mò; xoi mói chuyện riêng")
RECORDS[47] = ("087850", "snottiness", "noun", "/ˈsnɑːtinəs/", "thái độ xấc xược; sự sổ mũi")
RECORDS[56] = ("087859", "snowdropper", "noun", "/ˈsnoʊˌdrɑːpər/", "kẻ trộm quần áo phơi trên dây")
RECORDS[72] = ("087875", "snr", "noun", "/ˌɛsˌɛnˈɑːr/", "tỷ số tín hiệu nhiễu; người cha")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r06_raw_p4.json"))
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

json.dump(out, open("scratch/b38_r06_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b38_r06_p4 saved OK")
