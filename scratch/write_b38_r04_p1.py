import json

RECORDS = [
    ("086503", "sharecrop", "verb", "/ˈʃɛrˌkrɑːp/", "lĩnh canh; cấy rẽ chia hoa lợi"),
    ("086504", "sharecropped", "verb", "/ˈʃɛrˌkrɑːpt/", "đã lĩnh canh; đã cấy rẽ chia phần"),
    ("086505", "sharecroppers", "noun", "/ˈʃɛrˌkrɑːpərz/", "tá điền cấy rẽ; nông dân lĩnh canh"[:35]),
    ("086506", "sharecropping", "verb", "/ˈʃɛrˌkrɑːpɪŋ/", "đang lĩnh canh; đang cấy rẽ"),
    ("086507", "sharecrops", "verb", "/ˈʃɛrˌkrɑːps/", "lĩnh canh; cấy rẽ chia hoa lợi"),
    ("086508", "shareholders", "noun", "/ˈʃɛrˌhoʊldərz/", "cổ đông"),
    ("086509", "shareowner", "noun", "/ˈʃɛrˌoʊnər/", "cổ đông; người sở hữu cổ phần"),
    ("086510", "shareowners", "noun", "/ˈʃɛrˌoʊnərz/", "cổ đông; người sở hữu cổ phần"),
    ("086511", "sharepusher", "noun", "/ˈʃɛrˌpʊʃər/", "kẻ môi giới bán cổ phiếu ma"),
    ("086512", "sharepushers", "noun", "/ˈʃɛrˌpʊʃərz/", "kẻ lừa bán cổ phiếu ma"),
    ("086513", "sharers", "noun", "/ˈʃɛrərz/", "người chia sẻ; người dùng chung"),
    ("086514", "shares", "noun", "/ʃɛrz/", "cổ phần; phần chia sẻ"),
    ("086515", "sharked", "verb", "/ʃɑːrkt/", "đã lừa đảo kiếm chác"),
    ("086516", "sharking", "verb", "/ˈʃɑːrkɪŋ/", "đang lừa đảo kiếm chác; săn cá mập"[:35]),
    ("086517", "sharks", "verb", "/ʃɑːrks/", "lừa đảo kiếm chác; săn cá mập"),
    ("086518", "sharkskins", "noun", "/ˈʃɑːrkˌskɪnz/", "da cá mập; vải dệt bóng sharkskin"[:35]),
    ("086519", "sharksucker", "noun", "/ˈʃɑːrkˌsʌkər/", "cá ép bám theo cá mập"),
    ("086520", "sharpeners", "noun", "/ˈʃɑːrpənərz/", "đồ gọt bút chì; đá mài dao"),
    ("086521", "sharpening", "verb", "/ˈʃɑːrpənɪŋ/", "đang mài sắc; đang vót nhọn"),
    ("086522", "sharpens", "verb", "/ˈʃɑːrpənz/", "mài sắc; vót nhọn; làm sắc bén"),
    ("086523", "sharpish", "adj", "/ˈʃɑːrpɪʃ/", "hơi sắc bén; hơi gay gắt; hơi lạnh"),
    ("086524", "sharpnel", "noun", "/ˈʃræpnəl/", "mảnh đạn pháo; đạn trái phá"),
    ("086525", "sharpnesses", "noun", "/ˈʃɑːrpnəsɪz/", "độ sắc bén; sự gay gắt"),
    ("086526", "sharps", "noun", "/ʃɑːrps/", "nốt thăng; cám thô; kim nhọn"),
    ("086527", "sharpshoot", "verb", "/ˈʃɑːrpˌʃuːt/", "bắn tỉa chính xác"),
    ("086528", "sharpshooters", "noun", "/ˈʃɑːrpˌʃuːtərz/", "lính bắn tỉa; tay súng thiện xạ"),
    ("086529", "shashlik", "noun", "/ˈʃɑːʃlɪk/", "thịt xiên nướng kiểu Kavkaz"),
    ("086530", "shastan", "noun", "/ˈʃæstən/", "ngữ hệ Shasta (bản địa Bắc Mỹ)"),
    ("086531", "shaster", "noun", "/ˈʃɑːstər/", "kinh điển giáo huấn Ấn Độ giáo"),
    ("086532", "shastra", "noun", "/ˈʃɑːstrə/", "kinh luận giáo huấn Ấn Độ giáo"),
    ("086533", "shatters", "verb", "/ˈʃætərz/", "đập vỡ tan tành; làm tiêu tan"),
    ("086534", "shattery", "adj", "/ˈʃætəri/", "giòn dễ vỡ tan; lỏng lẻo"),
    ("086535", "shaveling", "noun", "/ˈʃeɪvlɪŋ/", "tu sĩ cạo đầu (hàm ý giễu cợt)"),
    ("086536", "shavers", "noun", "/ˈʃeɪvərz/", "máy cạo râu; cậu nhóc tinh nghịch"[:35]),
    ("086537", "shaves", "verb", "/ʃeɪvz/", "cạo râu; gọt mỏng; sượt qua"),
    ("086538", "shavetail", "noun", "/ˈʃeɪvˌteɪl/", "thiếu úy mới ra trường; la non"),
    ("086539", "shavetails", "noun", "/ˈʃeɪvˌteɪlz/", "thiếu úy mới; la mới huấn luyện"),
    ("086540", "shavous", "noun", "/ʃəˈvuːoʊs/", "lễ Ngũ Tuần Do Thái Shavuot"),
    ("086541", "shavuoth", "noun", "/ʃəˈvuːoʊθ/", "lễ Ngũ Tuần Do Thái Shavuot"),
    ("086542", "shawls", "noun", "/ʃɔːlz/", "khăn choàng vai"),
    ("086543", "shawms", "noun", "/ʃɔːmz/", "kèn dăm đôi thời Trung cổ"),
    ("086544", "she", "pron", "/ʃiː/", "cô ấy; chị ấy; bà ấy; con cái"),
    ("086545", "shea", "noun", "/ʃeɪ/", "cây hạt mỡ châu Phi"),
    ("086546", "sheading", "noun", "/ˈʃiːdɪŋ/", "khu hành chính (đảo Man)"),
    ("086547", "sheaflike", "adj", "/ˈʃiːfˌlaɪk/", "có hình dạng bó lúa"),
    ("086548", "sheafy", "adj", "/ˈʃiːfi/", "được bó thành lượm; giống bó lúa"),
    ("086549", "shearers", "noun", "/ˈʃɪrərz/", "thợ xén lông cừu; thợ cắt tôn"),
    ("086550", "shearling", "noun", "/ˈʃɪrlɪŋ/", "cừu non vừa xén lông lần đầu"),
    ("086551", "sheartail", "noun", "/ˈʃɪrˌteɪl/", "chim ruồi đuôi kéo"),
    ("086552", "sheartails", "noun", "/ˈʃɪrˌteɪlz/", "chim ruồi đuôi kéo"),
    ("086553", "shearwaters", "noun", "/ˈʃɪrˌwɔːtərz/", "chim hải âu rẽ sóng"),
    ("086554", "sheatfish", "noun", "/ˈʃiːtˌfɪʃ/", "cá nheo lớn châu Âu"),
    ("086555", "sheathes", "verb", "/ʃiːðz/", "tra vào bao; bọc lớp bảo vệ"),
    ("086556", "sheathless", "adj", "/ˈʃiːθləs/", "không có vỏ bao; trần trụi"),
    ("086557", "sheaths", "noun", "/ʃiːðz/", "bao kiếm; vỏ bọc bảo vệ; bao quy"),
    ("086558", "sheathwinged", "adj", "/ˈʃiːθˌwɪŋd/", "có cánh cứng (bọ cánh cứng)"),
    ("086559", "sheathy", "adj", "/ˈʃiːθi/", "có dạng bao bọc; giống vỏ bao"),
    ("086560", "sheave", "noun", "/ʃiːv/", "bánh ròng rọc có rãnh"),
    ("086561", "sheaves", "noun", "/ʃiːvz/", "bó lúa; xấp giấy; bánh ròng rọc"),
    ("086562", "shebat", "noun", "/ʃəˈvɑːt/", "tháng thứ năm lịch Do Thái"),
    ("086563", "shebook", "noun", "/tʃɪˈbuːk/", "tẩu thuốc cán dài kiểu Thổ Nhĩ Kỳ"),
    ("086564", "shebooks", "noun", "/tʃɪˈbuːks/", "tẩu thuốc cán dài Thổ Nhĩ Kỳ"),
    ("086565", "sheboyganites", "noun", "/ʃɪˈbɔɪɡəˌnaɪts/", "cư dân thành phố Sheboygan (Mỹ)"),
    ("086566", "shedders", "noun", "/ˈʃɛdərz/", "cua sắp lột vỏ; động vật lột xác"),
    ("086567", "sheepcote", "noun", "/ˈʃiːpˌkoʊt/", "chuồng cừu; ràn cừu"),
    ("086568", "sheepishness", "noun", "/ˈʃiːpɪʃnəs/", "vẻ bẽn lẽn; sự ngượng ngùng"),
    ("086569", "sheeplike", "adj", "/ˈʃiːpˌlaɪk/", "khờ khạo hiền lành như cừu"),
    ("086570", "sheepmen", "noun", "/ˈʃiːpmən/", "người chăn nuôi cừu"),
    ("086571", "sheeprun", "noun", "/ˈʃiːpˌrʌn/", "đồng cỏ rộng chăn thả cừu"),
    ("086572", "sheepshank", "noun", "/ˈʃiːpˌʃæŋk/", "nút thắt rút ngắn dây thừng"),
    ("086573", "sheepshearing", "noun", "/ˈʃiːpˌʃɪrɪŋ/", "việc xén lông cừu; mùa xén lông"),
    ("086574", "sheepskins", "noun", "/ˈʃiːpˌskɪnz/", "da cừu thuộc; bằng tốt nghiệp"),
    ("086575", "sheepwalk", "noun", "/ˈʃiːpˌwɔːk/", "bãi chăn thả cừu rộng lớn"),
    ("086576", "sheered", "verb", "/ʃɪrd/", "đã chuyển hướng đột ngột"),
    ("086577", "sheering", "verb", "/ˈʃɪrɪŋ/", "đang chuyển hướng đột ngột"),
    ("086578", "sheers", "verb", "/ʃɪrz/", "chuyển hướng đột ngột; chệch hướng"[:35]),
    ("086579", "sheeted", "verb", "/ˈʃiːtɪd/", "đã phủ khăn trải; đổ xối xả"),
    ("086580", "sheeter", "noun", "/ˈʃiːtər/", "máy cắt giấy thành từng tờ tấm"),
    ("086581", "sheetlike", "adj", "/ˈʃiːtˌlaɪk/", "mỏng phẳng dạng tấm lá"),
    ("086582", "sheets", "verb", "/ʃiːts/", "phủ tấm trải; đổ mưa như trút"),
    ("086583", "shegetz", "noun", "/ˈʃeɪɡəts/", "thanh niên ngoại đạo (tiếng Yiddish)"[:35]),
    ("086584", "shegoat", "noun", "/ˈʃiːˌɡoʊt/", "con dê cái"),
    ("086585", "shegoats", "noun", "/ˈʃiːˌɡoʊts/", "con dê cái"),
    ("086586", "sheikdom", "noun", "/ˈʃiːkdəm/", "tiểu quốc của tù trưởng Ả Rập"),
    ("086587", "sheila", "noun", "/ˈʃiːlə/", "cô gái trẻ (tiếng lóng Úc); tên nữ"[:35]),
    ("086588", "shekaree", "noun", "/ʃɪˈkɑːri/", "thợ săn chuyên nghiệp (Ấn Độ)"),
    ("086589", "shekarry", "noun", "/ʃɪˈkɑːri/", "thợ săn chuyên nghiệp (Ấn Độ)"),
    ("086590", "shelfful", "noun", "/ˈʃɛlfˌfʊl/", "đầy một ngăn kệ"),
    ("086591", "shelflike", "adj", "/ˈʃɛlfˌlaɪk/", "có dạng giống cái kệ; nhô ra"),
    ("086592", "shelfy", "adj", "/ˈʃɛlfi/", "có nhiều bãi cạn đá ngầm"),
    ("086593", "shellack", "verb", "/ʃəˈlæk/", "quét sơn cánh kiến; đánh bại áp đảo"[:35]),
    ("086594", "shellacking", "noun", "/ʃəˈlækɪŋ/", "trận thua thảm hại; trận đòn nhừ tử"[:35]),
    ("086595", "shellback", "noun", "/ˈʃɛlˌbæk/", "thủy thủ lão luyện vượt xích đạo"),
    ("086596", "shellbark", "noun", "/ˈʃɛlˌbɑːrk/", "cây hồ đào vỏ bong mảng"),
    ("086597", "shellflower", "noun", "/ˈʃɛlˌflaʊər/", "hoa riềng ấm Alpinia; cây rùa mai"),
    ("086598", "shellproof", "adj", "/ˈʃɛlˌpruːf/", "chống được đạn pháo và bom nổ"),
    ("086599", "shells", "noun", "/ʃɛlz/", "vỏ sò; vỏ đạn pháo; thân tàu đua"),
    ("086600", "shelly", "adj", "/ˈʃɛli/", "nhiều vỏ sò ốc; có mai cứng"),
    ("086601", "shelta", "noun", "/ˈʃɛltə/", "tiếng Shelta của dân du mục Ireland"[:35]),
    ("086602", "shelterbelt", "noun", "/ˈʃɛltərˌbɛlt/", "dải rừng phòng hộ chắn gió"),
]

# Cleanly replace slice expressions without slicing
RECORDS[2] = ("086505", "sharecroppers", "noun", "/ˈʃɛrˌkrɑːpərz/", "tá điền cấy rẽ; nông dân thuê đất")
RECORDS[13] = ("086516", "sharking", "verb", "/ˈʃɑːrkɪŋ/", "đang lừa đảo kiếm chác")
RECORDS[15] = ("086518", "sharkskins", "noun", "/ˈʃɑːrkˌskɪnz/", "da cá mập; vải dệt bóng mịn")
RECORDS[33] = ("086536", "shavers", "noun", "/ˈʃeɪvərz/", "máy cạo râu; cậu bé ranh mãnh")
RECORDS[75] = ("086578", "sheers", "verb", "/ʃɪrz/", "chuyển hướng đột ngột")
RECORDS[80] = ("086583", "shegetz", "noun", "/ˈʃeɪɡəts/", "thanh niên ngoại đạo (Do Thái)")
RECORDS[84] = ("086587", "sheila", "noun", "/ˈʃiːlə/", "cô gái trẻ (lóng Úc); tên Sheila")
RECORDS[90] = ("086593", "shellack", "verb", "/ʃəˈlæk/", "quét sơn cánh kiến; thắng áp đảo")
RECORDS[91] = ("086594", "shellacking", "noun", "/ʃəˈlækɪŋ/", "trận thua thảm; trận đòn nhừ tử")
RECORDS[98] = ("086601", "shelta", "noun", "/ˈʃɛltə/", "tiếng Shelta (du mục Ireland)")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r04_raw_p1.json"))
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

json.dump(out, open("scratch/b38_r04_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b38_r04_p1 saved OK")
