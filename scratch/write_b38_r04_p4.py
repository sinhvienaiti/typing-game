import json

RECORDS = [
    ("086803", "shovels", "verb", "/ˈʃʌvəlz/", "xúc bằng xẻng; hốt mạnh vào"),
    ("086804", "shover", "noun", "/ˈʃʌvər/", "người xô đẩy; dụng cụ đẩy"),
    ("086805", "shoves", "verb", "/ʃʌvz/", "xô đẩy mạnh; nhét bừa vào"),
    ("086806", "shoving", "verb", "/ˈʃʌvɪŋ/", "đang xô đẩy mạnh; đang nhét vào"),
    ("086807", "showed", "verb", "/ʃoʊd/", "đã cho xem; đã chỉ ra; thể hiện"),
    ("086808", "showered", "verb", "/ˈʃaʊərd/", "đã tắm vòi sen; đã trút mưa rào"),
    ("086809", "showeriness", "noun", "/ˈʃaʊərinəs/", "thời tiết hay có mưa rào"),
    ("086810", "showering", "verb", "/ˈʃaʊərɪŋ/", "đang tắm vòi sen; đang trút xuống"),
    ("086811", "showers", "verb", "/ˈʃaʊərz/", "tắm vòi sen; trút mưa rào; ban tặng"[:35]),
    ("086812", "showily", "adv", "/ˈʃoʊɪli/", "phô trương; sặc sỡ lòe loẹt"),
    ("086813", "shows", "verb", "/ʃoʊz/", "cho thấy; trình bày; biểu diễn"),
    ("086814", "shraga", "noun", "/ˈʃrɑːɡə/", "tên riêng nam Shraga"),
    ("086815", "shram", "verb", "/ʃræm/", "làm tê cóng vì gió lạnh"),
    ("086816", "shrank", "verb", "/ʃræŋk/", "đã co lại; đã thu nhỏ; lùi lại"),
    ("086817", "shredding", "noun", "/ˈʃrɛdɪŋ/", "việc xé nhỏ; việc hủy tài liệu"),
    ("086818", "shreddy", "adj", "/ˈʃrɛdi/", "bị xé tơi; rách thành từng mảnh"),
    ("086819", "shreds", "verb", "/ʃrɛdz/", "xé nhỏ; cắt sợi; hủy giấy vụn"),
    ("086820", "shrewed", "adj", "/ʃruːd/", "sắc sảo; khôn ngoan; tinh ranh"),
    ("086821", "shrewishly", "adv", "/ˈʃruːɪʃli/", "đanh đá; chua ngoa hay cằn nhằn"),
    ("086822", "shrewishness", "noun", "/ˈʃruːɪʃnəs/", "tính đanh đá chua ngoa"),
    ("086823", "shrewmouse", "noun", "/ˈʃruːˌmaʊs/", "chuột chù"),
    ("086824", "shrieks", "noun", "/ʃriːks/", "tiếng hét chói tai; tiếng la thé"),
    ("086825", "shrieval", "adj", "/ˈʃriːvəl/", "thuộc cảnh sát trưởng quận"),
    ("086826", "shrievalty", "noun", "/ˈʃriːvəlti/", "chức vụ cảnh sát trưởng quận"),
    ("086827", "shrikes", "noun", "/ʃraɪks/", "chim bách thanh"),
    ("086828", "shrilled", "verb", "/ʃrɪld/", "đã kêu the thé chói tai"),
    ("086829", "shrills", "verb", "/ʃrɪlz/", "kêu the thé; rít chói tai"),
    ("086830", "shrimped", "verb", "/ʃrɪmpt/", "đã đi đánh bắt tôm"),
    ("086831", "shrimpfish", "noun", "/ˈʃrɪmpˌfɪʃ/", "cá dao cạo bơi chúc đầu"),
    ("086832", "shrimping", "verb", "/ˈʃrɪmpɪŋ/", "đang đi đánh bắt tôm"),
    ("086833", "shrimps", "verb", "/ʃrɪmps/", "đánh bắt tôm"),
    ("086834", "shrinkages", "noun", "/ˈʃrɪŋkɪdʒɪz/", "độ co rút; sự hao hụt hàng hóa"),
    ("086835", "shrinks", "noun", "/ʃrɪŋks/", "bác sĩ tâm lý (lóng); sự co rút"),
    ("086836", "shrived", "verb", "/ʃraɪvd/", "đã giải tội cho (linh mục)"),
    ("086837", "shrivelling", "verb", "/ˈʃrɪvəlɪŋ/", "đang héo quắt; đang nhăn nheo lại"),
    ("086838", "shrivels", "verb", "/ˈʃrɪvəlz/", "héo quắt; nhăn nheo teo tóp"),
    ("086839", "shriven", "verb", "/ˈʃrɪvən/", "đã được giải tội xưng tội"),
    ("086840", "shrives", "verb", "/ʃraɪvz/", "nghe xưng tội và giải tội cho"),
    ("086841", "shriving", "verb", "/ˈʃraɪvɪŋ/", "đang nghe xưng tội và giải tội"),
    ("086842", "shroff", "noun", "/ʃrɑːf/", "người đổi tiền; người kiểm bạc"),
    ("086843", "shrouded", "verb", "/ˈʃraʊdɪd/", "đã bao phủ; đã quấn vải liệm"),
    ("086844", "shrouding", "verb", "/ˈʃraʊdɪŋ/", "đang bao phủ; đang quấn vải liệm"),
    ("086845", "shrouds", "verb", "/ʃraʊdz/", "bao phủ màn sương; quấn vải liệm"),
    ("086846", "shrove", "verb", "/ʃroʊv/", "đã nghe xưng tội và giải tội"),
    ("086847", "shrua", "noun", "/ʃrʌɡ/", "cái nhún vai"),
    ("086848", "shrublet", "noun", "/ˈʃrʌblət/", "cây bụi nhỏ; cây bụi thấp"),
    ("086849", "shrugged", "verb", "/ʃrʌɡd/", "đã nhún vai"),
    ("086850", "shrugging", "verb", "/ˈʃrʌɡɪŋ/", "đang nhún vai"),
    ("086851", "shrugs", "verb", "/ʃrʌɡz/", "nhún vai"),
    ("086852", "shrunk", "verb", "/ʃrʌŋk/", "đã co rút lại; đã teo nhỏ lại"),
    ("086853", "shtickl", "noun", "/ˈʃtɪkəl/", "một chút xíu; một mẩu nhỏ"),
    ("086854", "shtik", "noun", "/ʃtɪk/", "mánh hài quen; trò diễn đặc trưng"),
    ("086855", "shtikl", "noun", "/ˈʃtɪkəl/", "một chút xíu; một mẩu nhỏ"),
    ("086856", "shtup", "verb", "/ʃtʊp/", "quan hệ tình dục (tiếng lóng)"),
    ("086857", "shu", "noun", "/ʃuː/", "nhà Thục Hán; tiếng Trung vùng Thục"[:35]),
    ("086858", "shucked", "verb", "/ʃʌkt/", "đã bóc vỏ (bắp, hàu); đã lột áo"),
    ("086859", "shucker", "noun", "/ˈʃʌkər/", "máy bóc vỏ bắp; người tách vỏ hàu"),
    ("086860", "shucking", "verb", "/ˈʃʌkɪŋ/", "đang bóc vỏ bắp; đang tách vỏ hàu"),
    ("086861", "shuddered", "verb", "/ˈʃʌdərd/", "đã rùng mình; đã run lẩy bẩy"),
    ("086862", "shudderingly", "adv", "/ˈʃʌdərɪŋli/", "rùng mình kinh hãi; rùng rợn"),
    ("086863", "shudders", "verb", "/ˈʃʌdərz/", "rùng mình ớn lạnh; rung bần bật"),
    ("086864", "shuddery", "adj", "/ˈʃʌdəri/", "gây rùng mình; ớn lạnh rùng rợn"),
    ("086865", "shuffled", "verb", "/ˈʃʌfəld/", "đã xáo bài; đã lê bước; tráo đổi"),
    ("086866", "shuffles", "verb", "/ˈʃʌfəlz/", "xáo bài; lê bước chậm; tráo đổi"),
    ("086867", "shufflingly", "adv", "/ˈʃʌflɪŋli/", "lê bước kéo chân; quanh co mập mờ"),
    ("086868", "shufti", "noun", "/ˈʃʊfti/", "cái liếc nhìn nhanh (lóng Anh)"),
    ("086869", "shufty", "noun", "/ˈʃʊfti/", "cái nhìn thoáng qua"),
    ("086870", "shugenjas", "noun", "/ʃuːˈɡɛndʒəz/", "tu sĩ khổ hạnh núi Nhật Bản"),
    ("086871", "shuha", "adj", "/ˈʃuːhɑː/", "thuộc tông phái Thần đạo dân gian"),
    ("086872", "shumac", "noun", "/ˈʃuːˌmæk/", "cây sơn muối sumac"),
    ("086873", "shunless", "adj", "/ˈʃʌnləs/", "không thể né tránh được"),
    ("086874", "shunned", "verb", "/ʃʌnd/", "đã tránh xa; đã lảng tránh"),
    ("086875", "shuns", "verb", "/ʃʌnz/", "tránh xa; né tránh; xa lánh"),
    ("086876", "shunted", "verb", "/ˈʃʌntɪd/", "đã dồn toa tàu; đã gạt sang bên"),
    ("086877", "shunting", "verb", "/ˈʃʌntɪŋ/", "đang dồn toa; đang chuyển mạch"),
    ("086878", "shunts", "verb", "/ʃʌnts/", "dồn toa tàu; gạt sang; nối tắt"),
    ("086879", "shushed", "verb", "/ʃʌʃt/", "đã suỵt im lặng; đã làm dịu đi"),
    ("086880", "shushes", "verb", "/ˈʃʌʃɪz/", "suỵt ra hiệu im lặng"),
    ("086881", "shushing", "verb", "/ˈʃʌʃɪŋ/", "đang suỵt ra hiệu im lặng"),
    ("086882", "shuttering", "verb", "/ˈʃʌtərɪŋ/", "đang đóng cửa chớp; lắp ván khuôn"),
    ("086883", "shutterless", "adj", "/ˈʃʌtərləs/", "không có cửa chớp"),
    ("086884", "shutters", "verb", "/ˈʃʌtərz/", "đóng cửa chớp; đóng cửa ngừng bán"[:35]),
    ("086885", "shuttlebays", "noun", "/ˈʃʌtəlˌbeɪz/", "khoang đỗ tàu con thoi"),
    ("086886", "shuttlecocks", "noun", "/ˈʃʌtəlˌkɑːks/", "quả cầu lông"),
    ("086887", "shvantz", "noun", "/ʃvɑːnts/", "dương vật (lóng); kẻ vô dụng"),
    ("086888", "shyer", "noun", "/ˈʃaɪər/", "ngựa hay giật mình; người nhút nhát"[:35]),
    ("086889", "shying", "verb", "/ˈʃaɪɪŋ/", "đang giật mình né tránh; đang ném"),
    ("086890", "sialadenitis", "noun", "/ˌsaɪəlˌædəˈnaɪtɪs/", "viêm tuyến nước bọt"),
    ("086891", "sialia", "noun", "/saɪˈeɪliə/", "chi chim xanh Bắc Mỹ (Sialia)"),
    ("086892", "sialidae", "noun", "/saɪˈælɪˌdiː/", "họ côn trùng cánh lồi Sialidae"),
    ("086893", "sialis", "noun", "/ˈsaɪəlɪs/", "chi bọ bùn Sialis"),
    ("086894", "sialogogic", "adj", "/saɪˌæləˈɡɑːdʒɪk/", "kích thích tiết nước bọt"),
    ("086895", "sialogogue", "noun", "/saɪˈæləˌɡɑːɡ/", "thuốc kích thích tiết nước bọt"),
    ("086896", "sialoid", "adj", "/ˈsaɪəˌlɔɪd/", "giống nước bọt; dạng nước bọt"),
    ("086897", "sialolith", "noun", "/saɪˈæləˌlɪθ/", "sỏi tuyến nước bọt"),
    ("086898", "sibilance", "noun", "/ˈsɪbələns/", "tính chất âm xát xuýt"),
    ("086899", "sibilancy", "noun", "/ˈsɪbələnsi/", "tính chất âm xuýt; tiếng rít nhẹ"),
    ("086900", "sibilate", "verb", "/ˈsɪbəˌleɪt/", "phát âm thành âm xuýt"),
    ("086901", "sibilation", "noun", "/ˌsɪbəˈleɪʃən/", "tiếng xuýt; sự phát âm xuýt"),
    ("086902", "sibine", "noun", "/sɪˈbaɪniː/", "chi sâu bướm yên ngựa Sibine"),
]

# Remove slices cleanly <= 35 chars
RECORDS[8] = ("086811", "showers", "verb", "/ˈʃaʊərz/", "tắm vòi sen; trút mưa rào")
RECORDS[54] = ("086857", "shu", "noun", "/ʃuː/", "nước Thục Hán; tiếng vùng Thục")
RECORDS[81] = ("086884", "shutters", "verb", "/ˈʃʌtərz/", "đóng cửa chớp; đóng cửa tiệm")
RECORDS[85] = ("086888", "shyer", "noun", "/ˈʃaɪər/", "ngựa hay giật mình; người rụt rè")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r04_raw_p4.json"))
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

json.dump(out, open("scratch/b38_r04_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b38_r04_p4 saved OK")
