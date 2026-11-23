import json

RECORDS = [
    ("083003", "reproductory", "adj", "/ˌriːprəˈdʌktəri/", "thuộc sinh sản; có khả năng sinh sản"[:35]),
    ("083004", "reprogram", "verb", "/ˌriːˈproʊɡræm/", "lập trình lại"),
    ("083005", "reprogrammed", "verb", "/ˌriːˈproʊɡræmd/", "đã lập trình lại"),
    ("083006", "reprogramming", "verb", "/ˌriːˈproʊɡræmɪŋ/", "đang lập trình lại"),
    ("083007", "reprograms", "verb", "/ˌriːˈproʊɡræmz/", "lập trình lại"),
    ("083008", "reprographic", "adj", "/ˌriːprəˈɡræfɪk/", "thuộc kỹ thuật sao chụp"),
    ("083009", "reprography", "noun", "/rɪˈprɑːɡrəfi/", "kỹ thuật sao chụp tài liệu"),
    ("083010", "reproportion", "verb", "/ˌriːprəˈpɔːrʃən/", "điều chỉnh lại tỷ lệ"),
    ("083011", "reproval", "noun", "/rɪˈpruːvəl/", "lời khiển trách; sự phê bình"),
    ("083012", "reproved", "verb", "/rɪˈpruːvd/", "đã khiển trách"),
    ("083013", "reprover", "noun", "/rɪˈpruːvər/", "người khiển trách; người phê bình"),
    ("083014", "reproves", "verb", "/rɪˈpruːvz/", "khiển trách"),
    ("083015", "reprovingly", "adv", "/rɪˈpruːvɪŋli/", "với vẻ khiển trách"),
    ("083016", "reps", "noun", "/rɛps/", "vải sọc gân; số lần lặp lại"),
    ("083017", "reptant", "adj", "/ˈrɛptənt/", "bò; trườn sát đất"),
    ("083018", "reptantia", "noun", "/rɛpˈtænʃə/", "phân bộ Giáp xác bò"),
    ("083019", "reptation", "noun", "/rɛpˈteɪʃən/", "chuyển động trườn; sự bò"),
    ("083020", "republicanise", "verb", "/rɪˈpʌblɪkəˌnaɪz/", "cộng hòa hóa"),
    ("083021", "republicanize", "verb", "/rɪˈpʌblɪkəˌnaɪz/", "cộng hòa hóa"),
    ("083022", "republics", "noun", "/rɪˈpʌblɪks/", "nước cộng hòa"),
    ("083023", "repudiated", "verb", "/rɪˈpjuːdiˌeɪtɪd/", "đã khước từ; đã phủ nhận"),
    ("083024", "repudiates", "verb", "/rɪˈpjuːdiˌeɪts/", "khước từ; phủ nhận"),
    ("083025", "repudiating", "verb", "/rɪˈpjuːdiˌeɪtɪŋ/", "đang khước từ; đang phủ nhận"),
    ("083026", "repudiative", "adj", "/rɪˈpjuːdiˌeɪtɪv/", "có tính bác bỏ; có tính chối bỏ"),
    ("083027", "repugn", "verb", "/rɪˈpjuːn/", "phản đối; chống đối"),
    ("083028", "repugnancy", "noun", "/rɪˈpʌɡnənsi/", "sự ghê tởm; mối ác cảm"),
    ("083029", "repulsed", "verb", "/rɪˈpʌlst/", "đã đẩy lui; đã đánh bật"),
    ("083030", "repulses", "verb", "/rɪˈpʌlsɪz/", "đẩy lui; đánh bật"),
    ("083031", "repulsing", "verb", "/rɪˈpʌlsɪŋ/", "đang đẩy lui; đang đánh bật"),
    ("083032", "repulsions", "noun", "/rɪˈpʌlʃənz/", "lực đẩy; sự ghê tởm"),
    ("083033", "repurchased", "verb", "/ˌriːˈpɜːrtʃəst/", "đã mua lại"),
    ("083034", "repurchases", "verb", "/ˌriːˈpɜːrtʃəsɪz/", "mua lại"),
    ("083035", "repurchasing", "verb", "/ˌriːˈpɜːrtʃəsɪŋ/", "đang mua lại"),
    ("083036", "reputed", "verb", "/rɪˈpjuːtɪd/", "được cho là; có tiếng là"),
    ("083037", "reputedless", "adj", "/rɪˈpjuːtɪdləs/", "không có tiếng tăm; vô danh"),
    ("083038", "reputes", "verb", "/rɪˈpjuːts/", "cho là; đánh giá là"),
    ("083039", "reputing", "verb", "/rɪˈpjuːtɪŋ/", "đang cho là; đang đánh giá"),
    ("083040", "requesting", "verb", "/rɪˈkwɛstɪŋ/", "đang yêu cầu; đang đề nghị"),
    ("083041", "requests", "verb", "/rɪˈkwɛsts/", "yêu cầu; thỉnh cầu"),
    ("083042", "requires", "verb", "/rɪˈkwaɪərz/", "đòi hỏi; yêu cầu"),
    ("083043", "requiring", "verb", "/rɪˈkwaɪərɪŋ/", "đang đòi hỏi; đang yêu cầu"),
    ("083044", "requisiteness", "noun", "/ˈrɛkwɪzɪtnəs/", "tính cần thiết; sự bắt buộc"),
    ("083045", "requisitioned", "verb", "/ˌrɛkwɪˈzɪʃənd/", "đã trưng dụng; đã yêu cầu"),
    ("083046", "requisitioning", "verb", "/ˌrɛkwɪˈzɪʃənɪŋ/", "đang trưng dụng; đang yêu cầu"),
    ("083047", "requited", "verb", "/rɪˈkwaɪtɪd/", "đã đền đáp"),
    ("083048", "requites", "verb", "/rɪˈkwaɪts/", "đền đáp"),
    ("083049", "requiting", "verb", "/rɪˈkwaɪtɪŋ/", "đang đền đáp"),
    ("083050", "reradiate", "verb", "/ˌriːˈreɪdiˌeɪt/", "phát xạ lại; bức xạ lại"),
    ("083051", "reran", "verb", "/ˌriːˈræn/", "đã chạy lại; đã chiếu lại"),
    ("083052", "rerebrace", "noun", "/ˈrɪrbreɪs/", "giáp bảo vệ cánh tay trên"),
    ("083053", "rerecording", "noun", "/ˌriːrɪˈkɔːrdɪŋ/", "sự ghi âm lại; bản thu lại"),
    ("083054", "reregistration", "noun", "/ˌriːˌrɛdʒɪˈstreɪʃən/", "sự đăng ký lại"),
    ("083055", "rerise", "verb", "/ˌriːˈraɪz/", "dậy lại; đứng lên lại"),
    ("083056", "rerolling", "noun", "/ˌriːˈroʊlɪŋ/", "sự cuộn lại; sự cán lại"),
    ("083057", "resail", "verb", "/ˌriːˈseɪl/", "lái thuyền về; ra khơi lại"),
    ("083058", "resaw", "verb", "/ˌriːˈsɔː/", "xẻ lại ván; cưa lại"),
    ("083059", "rescaled", "verb", "/ˌriːˈskeɪld/", "đã đổi tỷ lệ"),
    ("083060", "rescales", "verb", "/ˌriːˈskeɪlz/", "đổi tỷ lệ"),
    ("083061", "rescaling", "verb", "/ˌriːˈskeɪlɪŋ/", "đang đổi tỷ lệ"),
    ("083062", "rescindable", "adj", "/rɪˈsɪndəbəl/", "có thể hủy bỏ; có thể bãi bỏ"),
    ("083063", "rescissory", "adj", "/rɪˈsɪsəri/", "có tính hủy bỏ; thủ tiêu"),
    ("083064", "rescrape", "verb", "/ˌriːˈskreɪp/", "cạo lại; nạo lại"),
    ("083065", "rescreening", "noun", "/ˌriːˈskriːnɪŋ/", "sự sàng lại; sự chiếu lại"),
    ("083066", "rescribe", "verb", "/rɪˈskraɪb/", "viết lại; phúc đáp"),
    ("083067", "rescriptor", "noun", "/rɪˈskrɪptər/", "thuốc kháng HIV Rescriptor"),
    ("083068", "rescues", "verb", "/ˈrɛskjuːz/", "giải cứu; cứu thoát"),
    ("083069", "rescuing", "verb", "/ˈrɛskjuːɪŋ/", "đang giải cứu; đang cứu"),
    ("083070", "researched", "verb", "/rɪˈsɜːrtʃt/", "đã nghiên cứu"),
    ("083071", "researchers", "noun", "/rɪˈsɜːrtʃərz/", "nhà nghiên cứu"),
    ("083072", "researches", "verb", "/rɪˈsɜːrtʃɪz/", "nghiên cứu"),
    ("083073", "researching", "verb", "/rɪˈsɜːrtʃɪŋ/", "đang nghiên cứu"),
    ("083074", "resedaceae", "noun", "/ˌrɛsɪˈdeɪsiːˌiː/", "họ Mộc tê"),
    ("083075", "resemblances", "noun", "/rɪˈzɛmblənsɪz/", "sự giống nhau; nét tương đồng"),
    ("083076", "resented", "verb", "/rɪˈzɛntɪd/", "đã phẫn nộ; đã bực tức"),
    ("083077", "resentfulness", "noun", "/rɪˈzɛntfəlnəs/", "sự phẫn uất; nỗi hậm hực"),
    ("083078", "resenting", "verb", "/rɪˈzɛntɪŋ/", "đang phẫn nộ; đang bực tức"),
    ("083079", "resents", "verb", "/rɪˈzɛnts/", "phẫn nộ; bực tức"),
    ("083080", "reservations", "noun", "/ˌrɛzərˈveɪʃənz/", "sự đặt chỗ trước; sự dè dặt"),
    ("083081", "reservative", "adj", "/rɪˈzɜːrvətɪv/", "để bảo tồn; có tính giữ lại"),
    ("083082", "reservatory", "noun", "/rɪˈzɜːrvətɔːri/", "nơi bảo tồn; nơi cất giữ"),
    ("083083", "reservedness", "noun", "/rɪˈzɜːrvɪdnəs/", "sự dè dặt; tính kín đáo"),
    ("083084", "reserver", "noun", "/rɪˈzɜːrvər/", "người giữ lại; người đặt trước"),
    ("083085", "reserving", "verb", "/rɪˈzɜːrvɪŋ/", "đang giữ lại; đang đặt trước"),
    ("083086", "reservists", "noun", "/rɪˈzɜːrvɪsts/", "quân nhân dự bị"),
    ("083087", "reservoirs", "noun", "/ˈrɛzərˌvwɑːrz/", "hồ chứa nước; bể chứa"),
    ("083088", "resetter", "noun", "/ˌriːˈsɛtər/", "kẻ chứa chấp đồ ăn trộm"),
    ("083089", "resettles", "verb", "/ˌriːˈsɛtəlz/", "tái định cư; ổn định lại"),
    ("083090", "resettling", "verb", "/ˌriːˈsɛtlɪŋ/", "đang tái định cư; ổn định lại"),
    ("083091", "resew", "verb", "/ˌriːˈsoʊ/", "may lại; khâu lại"),
    ("083092", "reshaped", "verb", "/ˌriːˈʃeɪpt/", "đã định hình lại"),
    ("083093", "reshapes", "verb", "/ˌriːˈʃeɪps/", "định hình lại"),
    ("083094", "reshaping", "verb", "/ˌriːˈʃeɪpɪŋ/", "đang định hình lại"),
    ("083095", "resharpens", "verb", "/ˌriːˈʃɑːrpənz/", "mài sắc lại"),
    ("083096", "reshimmed", "verb", "/ˌriːˈʃɪmd/", "đã chêm lại; đã lót lại"),
    ("083097", "reshipped", "verb", "/ˌriːˈʃɪpt/", "đã chuyển tàu lại"),
    ("083098", "reshipping", "verb", "/ˌriːˈʃɪpɪŋ/", "đang chuyển tàu lại"),
    ("083099", "reships", "verb", "/ˌriːˈʃɪps/", "chuyển tàu lại"),
    ("083100", "resht", "noun", "/rɛʃt/", "thành phố Rasht ở Iran"),
    ("083101", "reshuffled", "verb", "/ˌriːˈʃʌfəld/", "đã cải tổ; đã xáo trộn lại"),
    ("083102", "reshuffles", "verb", "/ˌriːˈʃʌfəlz/", "cải tổ; xáo trộn lại"),
]

# Fix 083003 cleanly without slice cut
RECORDS[0] = ("083003", "reproductory", "adj", "/ˌriːprəˈdʌktəri/", "thuộc sinh sản; có khả năng sinh")
assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, r
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r07_raw_p1.json"))
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

json.dump(out, open("scratch/b37_r07_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b37_r07_p1 saved OK")
