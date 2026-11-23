import json

RECORDS = [
    ("087703", "smothers", "verb", "/ˈsmʌðərz/", "làm ngạt thở; dập tắt; phủ kín"),
    ("087704", "smothery", "adj", "/ˈsmʌðəri/", "ngột ngạt khó thở; đầy khói bụi"),
    ("087705", "smoulderingly", "adv", "/ˈsmoʊldərɪŋli/", "âm ỉ cháy; chất chứa giận dữ"),
    ("087706", "smsgt", "noun", "/ˌɛsˌɛmˌɛsˈdʒiːtiː/", "thượng sĩ nhất không quân Mỹ"),
    ("087707", "smudged", "verb", "/smʌdʒd/", "đã làm nhòe mực; đã vấy vết bẩn"),
    ("087708", "smudges", "verb", "/ˈsmʌdʒɪz/", "làm nhòe nét; vấy vết bẩn"),
    ("087709", "smudginess", "noun", "/ˈsmʌdʒinəs/", "tình trạng nhòe nhoẹt lem bẩn"),
    ("087710", "smudging", "verb", "/ˈsmʌdʒɪŋ/", "đang làm nhòe; đang xông khói trừ tà"[:35]),
    ("087711", "smuggles", "verb", "/ˈsmʌɡəlz/", "buôn lậu; tuồn hàng lén lút"),
    ("087712", "smutch", "verb", "/smʌtʃ/", "bôi nhọ nhơ bẩn; làm lem bồ hóng"),
    ("087713", "smutchy", "adj", "/ˈsmʌtʃi/", "lem luốc bồ hóng; bẩn thỉu"),
    ("087714", "smuttily", "adv", "/ˈsmʌtɪli/", "thô tục dâm ô; lem bẩn bồ hóng"),
    ("087715", "smuttiness", "noun", "/ˈsmʌtinəs/", "tính tục tĩu; tình trạng bám muội"),
    ("087716", "smyrnium", "noun", "/ˈsmɜːrniəm/", "chi cây cần dại Smyrnium"),
    ("087717", "snackette", "noun", "/snæˈkɛt/", "quán ăn nhẹ nhỏ"),
    ("087718", "snaffled", "verb", "/ˈsnæfəld/", "đã cuỗm lấy; đã đóng hàm thiếc ngựa"[:35]),
    ("087719", "snaffles", "verb", "/ˈsnæfəlz/", "cuỗm lấy; thó mất; thắng dây cương"),
    ("087720", "snaffling", "verb", "/ˈsnæflɪŋ/", "đang cuỗm lấy; đang thó mất"),
    ("087721", "snagged", "verb", "/snæɡd/", "đã vướng mắc; đã rách toạc vì móc"),
    ("087722", "snagging", "verb", "/ˈsnæɡɪŋ/", "đang vướng mắc; đang sửa lỗi nhỏ"),
    ("087723", "snaggy", "adj", "/ˈsnæɡi/", "có nhiều cọc ngầm; nhiều mấu sắc"),
    ("087724", "snags", "verb", "/snæɡz/", "làm vướng rách; tóm nhanh được"),
    ("087725", "snailed", "verb", "/sneɪld/", "đã bò chậm như ốc sên; đi bắt ốc"),
    ("087726", "snailfish", "noun", "/ˈsneɪlˌfɪʃ/", "cá ốc biển sâu (họ Liparidae)"),
    ("087727", "snailflower", "noun", "/ˈsneɪlˌflaʊər/", "hoa đậu xoắn hình ốc"),
    ("087728", "snailing", "verb", "/ˈsneɪlɪŋ/", "đang bò chậm chạp; đang bắt ốc"),
    ("087729", "snaillery", "noun", "/ˈsneɪləri/", "trại nuôi ốc sên"),
    ("087730", "snaillike", "adj", "/ˈsneɪlˌlaɪk/", "chậm rì như ốc sên"),
    ("087731", "snails", "verb", "/sneɪlz/", "bò chậm như sên; bắt ốc sên"),
    ("087732", "snakeberry", "noun", "/ˈsneɪkˌbɛri/", "cây dâu rắn; cây nho độc châu Mỹ"),
    ("087733", "snakebird", "noun", "/ˈsneɪkˌbɜːrd/", "chim cổ rắn (chim điên điển)"),
    ("087734", "snakeblenny", "noun", "/ˈsneɪkˌblɛni/", "cá đạm bì thân mảnh dài"),
    ("087735", "snaked", "verb", "/sneɪkt/", "đã uốn lượn như rắn; kéo lê gỗ"),
    ("087736", "snakefish", "noun", "/ˈsneɪkˌfɪʃ/", "cá rắn biển; cá mối mình dài"),
    ("087737", "snakefly", "noun", "/ˈsneɪkˌflaɪ/", "côn trùng cổ dài giống rắn"),
    ("087738", "snakes", "verb", "/sneɪks/", "uốn khúc quanh co; lén lút luồn lách"[:35]),
    ("087739", "snakeskin", "noun", "/ˈsneɪkˌskɪn/", "da rắn thuộc; xác lột con rắn"),
    ("087740", "snakeskins", "noun", "/ˈsneɪkˌskɪnz/", "da rắn thuộc; xác rắn lột"),
    ("087741", "snakiness", "noun", "/ˈsneɪkinəs/", "tính quanh co xảo quyệt như rắn"),
    ("087742", "snaking", "verb", "/ˈsneɪkɪŋ/", "đang uốn lượn quanh co; kéo lê gỗ"),
    ("087743", "snakish", "adj", "/ˈsneɪkɪʃ/", "nham hiểm như rắn; uốn lượn"),
    ("087744", "snapback", "noun", "/ˈsnæpˌbæk/", "mũ lưỡi trai quai bấm sau; cú giật"[:35]),
    ("087745", "snapline", "noun", "/ˈsnæpˌlaɪn/", "dây bật mực đánh dấu đường thẳng"),
    ("087746", "snapped", "verb", "/snæpt/", "đã gãy phựt; đã nổi nóng quát; chụp"),
    ("087747", "snappily", "adv", "/ˈsnæpɪli/", "gọn gàng nhanh nhẹn; gắt gỏng"),
    ("087748", "snappiness", "noun", "/ˈsnæpinəs/", "sự nhanh nhẹn gọn; tính gắt gỏng"),
    ("087749", "snapping", "verb", "/ˈsnæpɪŋ/", "đang gãy phựt; đang đớp; đang chụp"),
    ("087750", "snappishly", "adv", "/ˈsnæpɪʃli/", "gắt gỏng; càu nhàu khó tính"),
    ("087751", "snappishness", "noun", "/ˈsnæpɪʃnəs/", "tính gắt gỏng hay cáu bẳn"),
    ("087752", "snaps", "verb", "/snæps/", "gãy gập; bật tách; quát nạt; chụp"),
    ("087753", "snapt", "verb", "/snæpt/", "đã gãy phựt; đã chộp nhanh (cổ)"),
    ("087754", "snapweed", "noun", "/ˈsnæpˌwiːd/", "cây bóng nước (hạt bật nổ)"),
    ("087755", "snared", "verb", "/snɛrd/", "đã đánh bẫy; đã giăng bẫy bắt"),
    ("087756", "snarer", "noun", "/ˈsnɛrər/", "người giăng bẫy; thợ đặt bẫy thú"),
    ("087757", "snares", "verb", "/snɛrz/", "đánh bẫy thú; giăng bẫy lừa"),
    ("087758", "snaring", "verb", "/ˈsnɛrɪŋ/", "đang đánh bẫy; đang giăng bẫy bắt"),
    ("087759", "snark", "noun", "/snɑːrk/", "lời châm chọc mỉa mai; quái vật ảo"),
    ("087760", "snarler", "noun", "/ˈsnɑːrlər/", "chó hay gầm gừ; người hay càu nhàu"),
    ("087761", "snarling", "verb", "/ˈsnɑːrlɪŋ/", "đang gầm gừ nhe răng; đang gắt gỏng"[:35]),
    ("087762", "snarls", "verb", "/snɑːrlz/", "gầm gừ; làm rối tung; quát tháo"),
    ("087763", "snatched", "verb", "/snætʃt/", "đã giật phăng; đã chộp vội lấy"),
    ("087764", "snatches", "verb", "/ˈsnætʃɪz/", "giật phăng lấy; chộp vội"),
    ("087765", "snatching", "verb", "/ˈsnætʃɪŋ/", "đang giật phăng; đang chộp vội lấy"),
    ("087766", "snatchy", "adj", "/ˈsnætʃi/", "đứt quãng từng hồi; không đều"),
    ("087767", "snazzily", "adv", "/ˈsnæzɪli/", "bảnh bao sành điệu; hợp mốt"),
    ("087768", "sneaked", "verb", "/sniːkt/", "đã lẻn đi rón rén; lén mang vào"),
    ("087769", "sneakers", "noun", "/ˈsniːkərz/", "giày thể thao đế mềm"),
    ("087770", "sneakingly", "adv", "/ˈsniːkɪŋli/", "lén lút; giấu giếm không lộ liễu"),
    ("087771", "sneaks", "verb", "/sniːks/", "lẻn đi rón rén; mách lẻo (Anh)"),
    ("087772", "sneck", "noun", "/snɛk/", "chốt then cửa; cái mũi (tiếng lóng)"),
    ("087773", "sneerer", "noun", "/ˈsnɪrər/", "kẻ hay cười khẩy chế nhạo"),
    ("087774", "sneezed", "verb", "/sniːzd/", "đã hắt hơi; đã hắt xì"),
    ("087775", "sneezes", "verb", "/ˈsniːzɪz/", "hắt hơi; hắt xì"),
    ("087776", "sneezeweed", "noun", "/ˈsniːzˌwiːd/", "cây cúc gây hắt hơi Helenium"),
    ("087777", "sneezewort", "noun", "/ˈsniːzˌwɜːrt/", "cây cỏ thi gây hắt hơi Achillea"),
    ("087778", "snell", "adj", "/snɛl/", "sắc sảo nhanh nhẹn; lạnh buốt (gió)"),
    ("087779", "snib", "noun", "/snɪb/", "chốt cài cửa sổ hay cửa ra vào"),
    ("087780", "snicked", "verb", "/snɪkt/", "đã khía vết nhỏ; đánh sượt bóng"),
    ("087781", "snickerer", "noun", "/ˈsnɪkərər/", "người cười khúc khích giễu cợt"),
    ("087782", "snickersnee", "noun", "/ˈsnɪkərˌsniː/", "dao găm lớn; cuộc đấu dao"),
    ("087783", "snicket", "noun", "/ˈsnɪkɪt/", "lối đi hẹp giữa hai bức tường (Anh)"),
    ("087784", "snicking", "verb", "/ˈsnɪkɪŋ/", "đang khía vết nhỏ; đánh sượt bóng"),
    ("087785", "snicks", "verb", "/snɪks/", "khía một vết nhỏ; đánh sượt mép gậy"[:35]),
    ("087786", "snideman", "noun", "/ˈsnaɪdmən/", "kẻ lưu hành tiền giả (lóng xưa)"),
    ("087787", "snideness", "noun", "/ˈsnaɪdnəs/", "thái độ mỉa mai chua cay; giả mạo"),
    ("087788", "snidesman", "noun", "/ˈsnaɪdzmən/", "kẻ lưu hành tiền giả (lóng xưa)"),
    ("087789", "sniffed", "verb", "/snɪft/", "đã khịt mũi; đã ngửi hít; bĩu môi"),
    ("087790", "sniffily", "adv", "/ˈsnɪfɪli/", "khinh khỉnh kênh kiệu; sụt sịt mũi"),
    ("087791", "sniffiness", "noun", "/ˈsnɪfinəs/", "thái độ khinh khỉnh; sự sụt sịt"),
    ("087792", "sniffing", "verb", "/ˈsnɪfɪŋ/", "đang khịt mũi; đang đánh hơi ngửi"),
    ("087793", "sniffish", "adj", "/ˈsnɪfɪʃ/", "khinh khỉnh; hay tỏ vẻ coi thường"),
    ("087794", "sniffishless", "noun", "/ˈsnɪfɪʃnəs/", "thái độ khinh khỉnh khó gần"),
    ("087795", "sniffishly", "adv", "/ˈsnɪfɪʃli/", "với vẻ khinh khỉnh kênh kiệu"),
    ("087796", "sniffled", "verb", "/ˈsnɪfəld/", "đã sụt sịt mũi; thút thít khóc"),
    ("087797", "sniffler", "noun", "/ˈsnɪflər/", "người hay khịt mũi sụt sịt"),
    ("087798", "sniffles", "verb", "/ˈsnɪfəlz/", "sụt sịt mũi; khóc thút thít"),
    ("087799", "sniffling", "verb", "/ˈsnɪflɪŋ/", "đang sụt sịt mũi; đang thút thít"),
    ("087800", "sniffs", "verb", "/snɪfs/", "khịt mũi; đánh hơi; khinh khỉnh"),
    ("087801", "snig", "verb", "/snɪɡ/", "kéo lê khúc gỗ; bắt lươn bằng mồi"),
    ("087802", "sniggered", "verb", "/ˈsnɪɡərd/", "đã cười khẩy chế nhạo"),
]

# Replace slices cleanly <= 35 chars
RECORDS[7] = ("087710", "smudging", "verb", "/ˈsmʌdʒɪŋ/", "đang làm nhòe; xông khói trừ tà")
RECORDS[15] = ("087718", "snaffled", "verb", "/ˈsnæfəld/", "đã cuỗm lấy; đã đóng hàm thiếc")
RECORDS[35] = ("087738", "snakes", "verb", "/sneɪks/", "uốn khúc quanh co; lén luồn lách")
RECORDS[41] = ("087744", "snapback", "noun", "/ˈsnæpˌbæk/", "mũ lưỡi trai quai bấm sau")
RECORDS[58] = ("087761", "snarling", "verb", "/ˈsnɑːrlɪŋ/", "đang gầm gừ nhe răng; gắt gỏng")
RECORDS[82] = ("087785", "snicks", "verb", "/snɪks/", "khía vết nhỏ; đánh sượt mép gậy")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r06_raw_p3.json"))
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

json.dump(out, open("scratch/b38_r06_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b38_r06_p3 saved OK")
