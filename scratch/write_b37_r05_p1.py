import json

records = [
    ("082003", "recondense", "verb", "/ˌriːkənˈdɛns/", "ngưng tụ lại, cô đọng lại"),
    ("082004", "reconditeness", "noun", "/rɪˈkɑːndaɪtnəs/", "sự thâm thúy, tính uyên bác sâu xa"),
    ("082005", "reconfigure", "verb", "/ˌriːkənˈfɪɡjər/", "cấu hình lại, sắp xếp lại hệ thống"),
    ("082006", "reconnoitred", "verb", "/ˌrɛkəˈnɔɪtərd/", "đã trinh sát, đã do thám (Anh)"),
    ("082007", "reconnoitres", "verb", "/ˌrɛkəˈnɔɪtərz/", "trinh sát, do thám địa hình (Anh)"),
    ("082008", "reconquered", "verb", "/ˌriːˈkɑːŋkərd/", "đã tái chinh phục, đã thu hồi lại"),
    ("082009", "reconquering", "verb", "/ˌriːˈkɑːŋkərɪŋ/", "tái chinh phục, giành lại lãnh thổ"),
    ("082010", "reconquers", "verb", "/ˌriːˈkɑːŋkərz/", "tái chinh phục, chiếm lại lãnh thổ"),
    ("082011", "reconquest", "noun", "/ˌriːˈkɑːŋkwɛst/", "cuộc tái chinh phục, sự giành lại"),
    ("082012", "reconsecrate", "verb", "/ˌriːˈkɑːnsəˌkreɪt/", "tái thánh hiến, cung hiến lại"),
    ("082013", "reconsidered", "verb", "/ˌriːkənˈsɪdərd/", "đã xem xét lại, cân nhắc lại"),
    ("082014", "reconsidering", "verb", "/ˌriːkənˈsɪdərɪŋ/", "xem xét lại, cân nhắc lại"),
    ("082015", "reconsiders", "verb", "/ˌriːkənˈsɪdərz/", "xem xét lại, cân nhắc lại ý định"),
    ("082016", "reconsolidate", "verb", "/ˌriːkənˈsɑːlɪˌdeɪt/", "củng cố lại, hợp nhất trở lại"),
    ("082017", "reconstituent", "adj", "/ˌriːkənˈstɪtʃuənt/", "tái tạo mô; bồi bổ phục hồi sức"),
    ("082018", "reconstituted", "verb", "/ˌriːˈkɑːnstəˌtuːtɪd/", "đã tái cấu trúc; đã pha hoàn nguyên"),
    ("082019", "reconstitutes", "verb", "/ˌriːˈkɑːnstəˌtuːts/", "tái cấu trúc; pha hoàn nguyên"),
    ("082020", "reconstituting", "verb", "/ˌriːˈkɑːnstəˌtuːtɪŋ/", "tái cấu trúc; pha hoàn nguyên"),
    ("082021", "reconstitution", "noun", "/ˌriːkɑːnstəˈtuːʃən/", "sự tái cấu trúc; sự pha hoàn nguyên"),
    ("082022", "recontract", "verb", "/ˌriːˈkɑːntrækt/", "ký lại hợp đồng, tái giao kèo"),
    ("082023", "reconvened", "verb", "/ˌriːkənˈviːnd/", "đã triệu tập lại, họp lại"),
    ("082024", "reconvenes", "verb", "/ˌriːkənˈviːnz/", "triệu tập lại, họp trở lại"),
    ("082025", "reconvening", "verb", "/ˌriːkənˈviːnɪŋ/", "triệu tập lại, họp trở lại"),
    ("082026", "reconvention", "noun", "/ˌriːkənˈvɛnʃən/", "đơn phản tố (luật dân sự)"),
    ("082027", "reconversion", "noun", "/ˌriːkənˈvɜːrʒən/", "sự chuyển đổi trở lại thời bình"),
    ("082028", "reconverted", "verb", "/ˌriːkənˈvɜːrtɪd/", "đã chuyển đổi lại, đã cải đạo lại"),
    ("082029", "reconverting", "verb", "/ˌriːkənˈvɜːrtɪŋ/", "chuyển đổi trở lại mục đích cũ"),
    ("082030", "reconverts", "verb", "/ˌriːkənˈvɜːrts/", "chuyển đổi trở lại trạng thái cũ"),
    ("082031", "reconvey", "verb", "/ˌriːkənˈveɪ/", "chuyển nhượng lại tài sản (luật)"),
    ("082032", "reconveyance", "noun", "/ˌriːkənˈveɪəns/", "sự chuyển nhượng lại quyền sở hữu"),
    ("082033", "reconveyances", "noun", "/ˌriːkənˈveɪənsɪz/", "các chứng thư chuyển nhượng lại"),
    ("082034", "reconvict", "verb", "/ˌriːkənˈvɪkt/", "kết án lại, tuyên có tội lần nữa"),
    ("082035", "recooler", "noun", "/riˈkuːlər/", "bộ làm nguội lại, dàn làm lạnh phụ"),
    ("082036", "recopied", "verb", "/ˌriːˈkɑːpid/", "đã chép lại, đã sao chép lại"),
    ("082037", "recopies", "verb", "/ˌriːˈkɑːpiz/", "chép lại, sao chép lại lần nữa"),
    ("082038", "recopying", "verb", "/ˌriːˈkɑːpiɪŋ/", "chép lại, sao chép lại bản khác"),
    ("082039", "recordist", "noun", "/rɪˈkɔːrdɪst/", "kỹ sư thu âm, người ghi âm"),
    ("082040", "records", "verb", "/rɪˈkɔːrdz/", "ghi chép lại; ghi âm, ghi hình"),
    ("082041", "recordsman", "noun", "/ˈrɛkərdzmən/", "người giữ kỷ lục thể thao"),
    ("082042", "recork", "verb", "/ˌriːˈkɔːrk/", "đóng nút bần lại vào chai"),
    ("082043", "recounted", "verb", "/ˌriːˈkaʊntɪd/", "đã kiểm phiếu lại; đã kể lại"),
    ("082044", "recounts", "verb", "/ˌriːˈkaʊnts/", "kiểm đếm lại; thuật lại chi tiết"),
    ("082045", "recouped", "verb", "/rɪˈkuːpt/", "đã thu hồi vốn, gỡ gạc lại"),
    ("082046", "recouping", "verb", "/rɪˈkuːpɪŋ/", "thu hồi vốn, bù đắp thiệt hại"),
    ("082047", "recoupment", "noun", "/rɪˈkuːpmənt/", "sự thu hồi vốn, sự bù đắp tổn thất"),
    ("082048", "recoups", "verb", "/rɪˈkuːps/", "thu hồi lại vốn, bù đắp lại"),
    ("082049", "recoverer", "noun", "/rɪˈkʌvərər/", "người thu hồi, người phục hồi"),
    ("082050", "recoveries", "noun", "/rɪˈkʌvəriz/", "sự bình phục; các đợt thu hồi"),
    ("082051", "recovers", "verb", "/rɪˈkʌvərz/", "bình phục, hồi phục; thu hồi lại"),
    ("082052", "recreance", "noun", "/ˈrɛkriəns/", "tính hèn nhát, sự phản bội (cổ)"),
    ("082053", "recreancy", "noun", "/ˈrɛkriənsi/", "thói hèn nhát, sự bội tín (cổ)"),
    ("082054", "recreated", "verb", "/ˌriːkriˈeɪtɪd/", "đã tái tạo, dựng lại; giải trí"),
    ("082055", "recreates", "verb", "/ˌriːkriˈeɪts/", "tái tạo, dựng lại; tiêu khiển"),
    ("082056", "recreating", "verb", "/ˌriːkriˈeɪtɪŋ/", "tái tạo, tái hiện; nghỉ ngơi"),
    ("082057", "recreations", "noun", "/ˌrɛkriˈeɪʃənz/", "hoạt động giải trí, tiêu khiển"),
    ("082058", "recreative", "adj", "/ˈrɛkriˌeɪtɪv/", "mang tính giải trí, tiêu khiển"),
    ("082059", "recrement", "noun", "/ˈrɛkrəmənt/", "xỉ kim loại; dịch tiết tái hấp thu"),
    ("082060", "recriminate", "verb", "/rɪˈkrɪməˌneɪt/", "buộc tội lại, đổ lỗi trả đũa"),
    ("082061", "recriminated", "verb", "/rɪˈkrɪməˌneɪtɪd/", "đã buộc tội lại, đổ lỗi trả đũa"),
    ("082062", "recriminates", "verb", "/rɪˈkrɪməˌneɪts/", "buộc tội lại, đổ lỗi cho nhau"),
    ("082063", "recriminating", "verb", "/rɪˈkrɪməˌneɪtɪŋ/", "buộc tội lại, đổ lỗi trả đũa nhau"),
    ("082064", "recriminative", "adj", "/rɪˈkrɪməˌneɪtɪv/", "có tính buộc tội lại, đổ lỗi nhau"),
    ("082065", "recross", "verb", "/ˌriːˈkrɔːs/", "băng qua trở lại, vượt qua lại"),
    ("082066", "recrossed", "verb", "/ˌriːˈkrɔːst/", "đã băng qua trở lại phía bên kia"),
    ("082067", "recrosses", "verb", "/ˌriːˈkrɔːsɪz/", "băng qua trở lại phía bên kia"),
    ("082068", "recrossing", "verb", "/ˌriːˈkrɔːsɪŋ/", "băng qua trở lại sang bờ bên kia"),
    ("082069", "recrudesce", "verb", "/ˌriːkruːˈdɛs/", "tái phát trở lại (bệnh, bạo lực)"),
    ("082070", "recrudesced", "verb", "/ˌriːkruːˈdɛst/", "đã tái phát trở lại, bùng phát lại"),
    ("082071", "recrudescency", "noun", "/ˌriːkruːˈdɛsənsi/", "sự tái phát, sự bùng phát lại"),
    ("082072", "recrudescense", "noun", "/ˌriːkruːˈdɛsəns/", "sự tái phát lại (biến thể sai chữ)"),
    ("082073", "recrudescent", "adj", "/ˌriːkruːˈdɛsənt/", "tái phát lại, bùng phát trở lại"),
    ("082074", "recrudesces", "verb", "/ˌriːkruːˈdɛsɪz/", "tái phát lại, bùng lên trở lại"),
    ("082075", "recrudescing", "verb", "/ˌriːkruːˈdɛsɪŋ/", "tái phát trở lại, bùng phát lại"),
    ("082076", "recruital", "noun", "/rɪˈkruːtəl/", "sự tuyển mộ, sự chiêu sinh thêm"),
    ("082077", "recruited", "verb", "/rɪˈkruːtɪd/", "đã tuyển dụng; đã chiêu mộ quân"),
    ("082078", "recruiting", "verb", "/rɪˈkruːtɪŋ/", "tuyển dụng nhân sự; chiêu mộ"),
    ("082079", "recruitments", "noun", "/rɪˈkruːtmənts/", "các đợt tuyển dụng, chiêu mộ"),
    ("082080", "recruits", "verb", "/rɪˈkruːts/", "tuyển dụng, chiêu mộ, tuyển quân"),
    ("082081", "recrushing", "noun", "/riˈkrʌʃɪŋ/", "sự nghiền vụn lại (khoáng sản)"),
    ("082082", "recrystallization", "noun", "/riˌkrɪstələˈzeɪʃən/", "quá trình kết tinh lại (hóa học)"),
    ("082083", "recta", "noun", "/ˈrɛktə/", "các trực tràng, ruột thẳng"),
    ("082084", "rectangularity", "noun", "/rɛkˌtæŋɡjəˈlærəti/", "tính chất hình chữ nhật vuông góc"),
    ("082085", "rectifies", "verb", "/ˈrɛktəˌfaɪz/", "sửa chữa sai sót; chỉnh lưu dòng"),
    ("082086", "rectifying", "verb", "/ˈrɛktəˌfaɪɪŋ/", "sửa chữa sai sót; chỉnh lưu điện"),
    ("082087", "rectilineal", "adj", "/ˌrɛktəˈlɪniəl/", "thẳng tắp, gồm toàn đường thẳng"),
    ("082088", "rectilinearity", "noun", "/ˌrɛktəlɪniˈærəti/", "tính thẳng tắp, sự đi thẳng"),
    ("082089", "rectitis", "noun", "/rɛkˈtaɪtɪs/", "chứng viêm trực tràng (y học)"),
    ("082090", "rectocoele", "noun", "/ˈrɛktəˌsiːl/", "chứng sa trực tràng (Anh)"),
    ("082091", "rectoplasty", "noun", "/ˈrɛktəˌplæsti/", "phẫu thuật tạo hình trực tràng"),
    ("082092", "rectorial", "adj", "/rɛkˈtɔːriəl/", "thuộc hiệu trưởng; thuộc cha xứ"),
    ("082093", "rectories", "noun", "/ˈrɛktəriz/", "những nhà ở của mục sư giáo xứ"),
    ("082094", "rectoscope", "noun", "/ˈrɛktəˌskoʊp/", "ống nội soi trực tràng (y học)"),
    ("082095", "rectosigmoid", "adj", "/ˌrɛktoʊˈsɪɡmɔɪd/", "thuộc trực tràng và đại tràng sigma"),
    ("082096", "rectotomy", "noun", "/rɛkˈtɑːtəmi/", "phẫu thuật mở thông trực tràng"),
    ("082097", "recumb", "verb", "/rɪˈkʌm/", "nằm nghỉ ngả lưng, dựa vào (cổ)"),
    ("082098", "recumbency", "noun", "/rɪˈkʌmbənsi/", "tư thế nằm ngả lưng nghỉ ngơi"),
    ("082099", "recuperated", "verb", "/rɪˈkuːpəˌreɪtɪd/", "đã hồi phục sức khỏe, bình phục"),
    ("082100", "recuperates", "verb", "/rɪˈkuːpəˌreɪts/", "hồi phục sức khỏe; bù đắp tổn thất"),
    ("082101", "recuperating", "verb", "/rɪˈkuːpəˌreɪtɪŋ/", "hồi phục sức khỏe, dưỡng bệnh"),
    ("082102", "recuperator", "noun", "/rɪˈkuːpəˌreɪtər/", "bộ thu hồi nhiệt; lò hoàn nhiệt"),
]

raw = json.load(open("scratch/b37_r05_raw_p1.json"))
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
with open("scratch/b37_r05_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r05_p1 saved OK")
