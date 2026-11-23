import json

records = [
    ("081003", "quartation", "noun", "/kwɔːrˈteɪʃən/", "phép hợp kim ba bạc một vàng"),
    ("081004", "quarterage", "noun", "/ˈkwɔːrtərɪdʒ/", "tiền trả hằng quý, phụ cấp quý"),
    ("081005", "quarterbell", "noun", "/ˈkwɔːrtərˌbɛl/", "chuông đồng hồ điểm mỗi 15 phút"),
    ("081006", "quartered", "verb", "/ˈkwɔːrtərd/", "đã chia làm bốn; đã đóng quân"),
    ("081007", "quarterlight", "noun", "/ˈkwɔːrtərˌlaɪt/", "cửa kính thông gió nhỏ bên cửa xe"),
    ("081008", "quartern", "noun", "/ˈkwɔːrtərn/", "đơn vị một phần tư (lít, cân Anh)"),
    ("081009", "quarternity", "noun", "/kwɔːrˈtɜːrnəti/", "nhóm bốn người; tứ vị nhất thể"),
    ("081010", "quarterstaves", "noun", "/ˈkwɔːrtərˌsteɪvz/", "những cây gậy chiến đấu dài bằng gỗ"),
    ("081011", "quartervine", "noun", "/ˈkwɔːrtərˌvaɪn/", "dây leo hoa kèn Bignonia Bắc Mỹ"),
    ("081012", "quartets", "noun", "/kwɔːrˈtɛts/", "nhóm tứ tấu; bản nhạc bốn người"),
    ("081013", "quartziferous", "adj", "/kwɔːrtˈsɪfərəs/", "chứa thạch anh (địa chất)"),
    ("081014", "quartzose", "adj", "/kwɔːrˈtsoʊs/", "giàu thạch anh, bằng thạch anh"),
    ("081015", "quartzous", "adj", "/ˈkwɔːrtsəs/", "chứa thạch anh, giống đá thạch anh"),
    ("081016", "quartzy", "adj", "/ˈkwɔːrtsi/", "có chứa thạch anh, giống thạch anh"),
    ("081017", "quasars", "noun", "/ˈkweɪzɑːrz/", "các chuẩn tinh phát xạ mạnh"),
    ("081018", "quashed", "verb", "/kwɑːʃt/", "đã hủy bỏ (phán quyết); đã dập tắt"),
    ("081019", "quashee", "noun", "/ˈkwɑːʃi/", "người da đen (cách gọi cũ)"),
    ("081020", "quashes", "verb", "/ˈkwɑːʃɪz/", "hủy bỏ (phán quyết); đàn áp dập tắt"),
    ("081021", "quashing", "verb", "/ˈkwɑːʃɪŋ/", "hủy bỏ (án); dập tắt cuộc nổi dậy"),
    ("081022", "quasihemidemisemiquaver", "noun", "/ˌkweɪzaɪˌhɛmiˌdɛmiˌsɛmiˈkweɪvər/", "nốt móc năm trong ký âm nhạc (Anh)"),
    ("081023", "quasihemidemisemiquavers", "noun", "/ˌkweɪzaɪˌhɛmiˌdɛmiˌsɛmiˈkweɪvərz/", "những nốt nhạc móc năm (Anh)"),
    ("081024", "quasimodo", "noun", "/ˌkwɑːzɪˈmoʊdoʊ/", "Chủ nhật thứ hai sau Lễ Phục sinh"),
    ("081025", "quass", "noun", "/kwɑːs/", "rượu lên men lúa mạch kvass (Nga)"),
    ("081026", "quassin", "noun", "/ˈkwɑːsɪn/", "chất đắng quassin (cây khổ mộc)"),
    ("081027", "quatercentenary", "noun", "/ˌkwætərsɛnˈtɛnəri/", "lễ kỷ niệm bốn trăm năm"),
    ("081028", "quatercentennial", "noun", "/ˌkwætərsɛnˈtɛniəl/", "lễ kỷ niệm bốn trăm năm"),
    ("081029", "quatern", "noun", "/ˈkwɔːtərn/", "bộ bốn, tập hợp gồm bốn phần"),
    ("081030", "quaternate", "adj", "/kwəˈtɜːrnət/", "xếp thành bộ bốn (lá mọc chụm bốn)"),
    ("081031", "quaternions", "noun", "/kwəˈtɜːrniənz/", "số siêu phức quaternion (toán học)"),
    ("081032", "quaternity", "noun", "/kwəˈtɜːrnəti/", "nhóm bốn người, bộ bốn thống nhất"),
    ("081033", "quaternization", "noun", "/kwəˌtɜːrnəˈzeɪʃən/", "phản ứng tạo muối amoni bậc bốn"),
    ("081034", "quatorzain", "noun", "/ˌkætərˈzeɪn/", "bài thơ mười bốn câu (dạng sonnet)"),
    ("081035", "quatrefoil", "noun", "/ˈkætrəˌfɔɪl/", "hoa văn hình cỏ bốn lá (kiến trúc)"),
    ("081036", "quatrocentist", "noun", "/ˌkwɑːtroʊˈtʃɛntɪst/", "nghệ sĩ Ý thế kỷ 15 (biến thể)"),
    ("081037", "quatrocento", "noun", "/ˌkwɑːtroʊˈtʃɛntoʊ/", "thế kỷ 15 văn nghệ Ý (biến thể)"),
    ("081038", "quattrocentist", "noun", "/ˌkwɑːtroʊˈtʃɛntɪst/", "nghệ sĩ Ý thời kỳ thế kỷ 15"),
    ("081039", "quavered", "verb", "/ˈkweɪvərd/", "đã run giọng, đã ngân rung âm thanh"),
    ("081040", "quaveringly", "adv", "/ˈkweɪvərɪŋli/", "với giọng run rẩy, ngân rung"),
    ("081041", "quavers", "verb", "/ˈkweɪvərz/", "run giọng, rung động, ngân rung"),
    ("081042", "quavery", "adj", "/ˈkweɪvəri/", "run rẩy, chao đảo, rung rung"),
    ("081043", "quayage", "noun", "/ˈkiːɪdʒ/", "phí neo đậu cầu cảng, bến tàu"),
    ("081044", "quayside", "noun", "/ˈkiːˌsaɪd/", "khu vực dọc theo bến tàu, cầu cảng"),
    ("081045", "quaysides", "noun", "/ˈkiːˌsaɪdz/", "những khu vực ven bến tàu, cầu cảng"),
    ("081046", "quean", "noun", "/kwiːn/", "cô gái lẳng lơ, đàn bà hư hỏng (cổ)"),
    ("081047", "queasily", "adv", "/ˈkwiːzəli/", "với cảm giác buồn nôn, khó chịu"),
    ("081048", "quebracho", "noun", "/keɪˈbrɑːtʃoʊ/", "cây gỗ cứng Nam Mỹ quebracho"),
    ("081049", "quechuan", "adj", "/ˈkɛtʃwən/", "thuộc dân tộc hoặc tiếng Quechua"),
    ("081050", "queendom", "noun", "/ˈkwiːndəm/", "vương quốc nữ hoàng; ngôi nữ hoàng"),
    ("081051", "queened", "verb", "/kwiːnd/", "đã phong hậu (cờ vua); đã làm dáng"),
    ("081052", "queenfish", "noun", "/ˈkwiːnˌfɪʃ/", "cá đù bạc (Seriphus politus)"),
    ("081053", "queenhood", "noun", "/ˈkwiːnˌhʊd/", "địa vị nữ hoàng, phẩm giá hoàng hậu"),
    ("081054", "queening", "verb", "/ˈkwiːnɪŋ/", "phong hậu (cờ vua); làm dáng"),
    ("081055", "queenlike", "adj", "/ˈkwiːnˌlaɪk/", "oai nghiêm quý phái như nữ hoàng"),
    ("081056", "queenliness", "noun", "/ˈkwiːnlinəs/", "vẻ uy nghi, phong thái bậc mẫu nghi"),
    ("081057", "queered", "verb", "/kwɪrd/", "đã làm hỏng, đã phá hỏng cơ hội"),
    ("081058", "queering", "verb", "/ˈkwɪrɪŋ/", "làm hỏng, phá bĩnh; nhìn góc queer"),
    ("081059", "queerish", "adj", "/ˈkwɪrɪʃ/", "hơi kỳ lạ, hơi quái dị, khang khác"),
    ("081060", "queers", "verb", "/kwɪrz/", "làm hỏng kế hoạch, phá bĩnh"),
    ("081061", "quells", "verb", "/kwɛlz/", "dập tắt, đàn áp; trấn an nỗi sợ"),
    ("081062", "quellung", "noun", "/ˈkwɛlʊŋ/", "phản ứng phồng vỏ vi khuẩn (y học)"),
    ("081063", "quenchable", "adj", "/ˈkwɛntʃəbəl/", "có thể dập tắt; có thể làm nguôi"),
    ("081064", "quencher", "noun", "/ˈkwɛntʃər/", "thức uống giải khát; chất dập tắt"),
    ("081065", "quenches", "verb", "/ˈkwɛntʃɪz/", "dập tắt (lửa); làm dịu cơn khát"),
    ("081066", "quenchless", "adj", "/ˈkwɛntʃləs/", "không thể dập tắt, khó nguôi"),
    ("081067", "quenelle", "noun", "/kəˈnɛl/", "viên chả cá hoặc thịt hấp kiểu Pháp"),
    ("081068", "quercitron", "noun", "/ˈkwɜːrsəˌtrɑːn/", "thuốc nhuộm vàng từ vỏ cây sồi đen"),
    ("081069", "querencias", "noun", "/kəˈrɛnsiəz/", "nơi thân thuộc tạo cảm giác an toàn"),
    ("081070", "querent", "noun", "/ˈkwɪrənt/", "người chất vấn; người đi xem bói"),
    ("081071", "queried", "verb", "/ˈkwɪrid/", "đã hỏi, đã nghi ngờ; đã truy vấn"),
    ("081072", "querier", "noun", "/ˈkwɪriər/", "người đặt câu hỏi, người chất vấn"),
    ("081073", "queries", "verb", "/ˈkwɪriz/", "hỏi, chất vấn, nghi ngờ; truy vấn"),
    ("081074", "querist", "noun", "/ˈkwɪrɪst/", "người đặt câu hỏi, người tìm hiểu"),
    ("081075", "querulously", "adv", "/ˈkwɛrələsli/", "với giọng càu nhàu, hay than phiền"),
    ("081076", "querulousness", "noun", "/ˈkwɛrələsnəs/", "tính hay càu nhàu, thói than phiền"),
    ("081077", "querying", "verb", "/ˈkwɪriɪŋ/", "hỏi, chất vấn, bày tỏ nghi vấn"),
    ("081078", "queso", "noun", "/ˈkeɪsoʊ/", "sốt phô mai đun chảy kiểu Mexico"),
    ("081079", "quested", "verb", "/ˈkwɛstɪd/", "đã tìm kiếm, đã truy tầm phiêu lưu"),
    ("081080", "questing", "verb", "/ˈkwɛstɪŋ/", "tìm kiếm, săn lùng, đi truy tầm"),
    ("081081", "questionary", "noun", "/ˈkwɛstʃəˌnɛri/", "bảng câu hỏi khảo sát (ít dùng)"),
    ("081082", "questioned", "verb", "/ˈkwɛstʃənd/", "đã hỏi, đã thẩm vấn; đã nghi ngờ"),
    ("081083", "questionless", "adj", "/ˈkwɛstʃənləs/", "không còn nghi ngờ gì, hiển nhiên"),
    ("081084", "questions", "noun", "/ˈkwɛstʃənz/", "các câu hỏi, vấn đề cần giải quyết"),
    ("081085", "questor", "noun", "/ˈkwɛstər/", "quan coi quốc khố La Mã; thủ quỹ"),
    ("081086", "questorship", "noun", "/ˈkwɛstərʃɪp/", "chức vụ quan coi quốc khố La Mã"),
    ("081087", "quests", "verb", "/kwɛsts/", "tìm kiếm, săn tìm, đi truy tầm"),
    ("081088", "quetch", "verb", "/kwɛtʃ/", "rên rỉ than phiền, cằn nhằn"),
    ("081089", "quethe", "verb", "/kwiːð/", "nói, tuyên bố (từ cổ rất hiếm)"),
    ("081090", "queued", "verb", "/kjuːd/", "đã xếp hàng chờ; đưa vào hàng đợi"),
    ("081091", "queuer", "noun", "/ˈkjuːər/", "người đang đứng xếp hàng chờ"),
    ("081092", "queues", "verb", "/kjuːz/", "xếp hàng chờ; đưa vào hàng đợi"),
    ("081093", "queuing", "verb", "/ˈkjuːɪŋ/", "xếp hàng chờ; xếp vào hàng đợi"),
    ("081094", "quiaquia", "noun", "/ˌkiːəˈkiːə/", "cá nục tròn Đại Tây Dương"),
    ("081095", "quibbled", "verb", "/ˈkwɪbəld/", "đã bắt bẻ vụn vặt, cãi chày cối"),
    ("081096", "quibbles", "verb", "/ˈkwɪbəlz/", "bắt bẻ vụn vặt, ngụy biện"),
    ("081097", "quibbling", "verb", "/ˈkwɪbəlɪŋ/", "bắt bẻ câu chữ, cãi vặt ngụy biện"),
    ("081098", "quickbasic", "noun", "/ˈkwɪkˌbeɪsɪk/", "ngôn ngữ lập trình QuickBASIC"),
    ("081099", "quickened", "verb", "/ˈkwɪkənd/", "đã tăng tốc; đã làm sống lại"),
    ("081100", "quickener", "noun", "/ˈkwɪkənər/", "chất xúc tiến, tác nhân kích thích"),
    ("081101", "quickens", "verb", "/ˈkwɪkənz/", "tăng tốc, đẩy nhanh; hồi sinh"),
    ("081102", "quicksanded", "adj", "/ˈkwɪkˌsændɪd/", "bị sa lầy vào bãi cát lún"),
]

raw = json.load(open("scratch/b37_r03_raw_p1.json"))
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
with open("scratch/b37_r03_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r03_p1 saved OK")
