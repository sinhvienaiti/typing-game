import json

records = [
    ("082303", "refines", "verb", "/rɪˈfaɪnz/", "tinh chế, lọc sạch; trau chuốt lại"),
    ("082304", "refinisher", "noun", "/ˌriːˈfɪnɪʃər/", "thợ phục chế đánh bóng đồ gỗ"),
    ("082305", "refits", "verb", "/ˌriːˈfɪts/", "tân trang sửa chữa đại tu (tàu)"),
    ("082306", "refitted", "verb", "/ˌriːˈfɪtɪd/", "đã tân trang, sửa chữa đại tu lại"),
    ("082307", "refitting", "verb", "/ˌriːˈfɪtɪŋ/", "tân trang, sửa chữa trang bị lại"),
    ("082308", "reflated", "verb", "/ˌriːˈfleɪtɪd/", "đã tái bơm lạm phát (kinh tế)"),
    ("082309", "reflates", "verb", "/ˌriːˈfleɪts/", "tái lạm phát kích thích kinh tế"),
    ("082310", "reflating", "verb", "/ˌriːˈfleɪtɪŋ/", "tái lạm phát, kích cầu tiền tệ"),
    ("082311", "reflationary", "adj", "/ˌriːˈfleɪʃəˌnɛri/", "nhằm tái lạm phát kích cầu"),
    ("082312", "reflectingly", "adv", "/rɪˈflɛktɪŋli/", "với vẻ trầm tư suy ngẫm sâu sắc"),
    ("082313", "reflectometers", "noun", "/ˌrɪflɛkˈtɑːmɪtərz/", "những máy đo hệ số phản xạ"),
    ("082314", "reflectorise", "verb", "/rɪˈflɛktəˌraɪz/", "gắn chất phản quang, tráng gương"),
    ("082315", "reflectorize", "verb", "/rɪˈflɛktəˌraɪz/", "gắn chất phản quang, tráng gương"),
    ("082316", "reflectors", "noun", "/rɪˈflɛktərz/", "tấm phản quang, gương phản xạ"),
    ("082317", "reflectoscope", "noun", "/rɪˈflɛktəˌskoʊp/", "máy dò khuyết tật kim loại siêu âm"),
    ("082318", "reflects", "verb", "/rɪˈflɛkts/", "phản chiếu, phản xạ; phản ánh lại"),
    ("082319", "reflet", "noun", "/rəˈfleɪ/", "lớp men ánh kim trên đồ gốm sứ"),
    ("082320", "reflexes", "noun", "/ˈriːflɛksɪz/", "các phản xạ tự nhiên của cơ thể"),
    ("082321", "reflexibility", "noun", "/rɪˌflɛksəˈbɪləti/", "tính chất có thể phản xạ tia sáng"),
    ("082322", "reflexible", "adj", "/rɪˈflɛksəbəl/", "có thể phản xạ, khúc xạ lại được"),
    ("082323", "reflexions", "noun", "/rɪˈflɛkʃənz/", "sự phản chiếu; suy tư (Anh)"),
    ("082324", "reflexiveness", "noun", "/rɪˈflɛksɪvnəs/", "tính phản thân, tính tự phản ánh"),
    ("082325", "reflexives", "noun", "/rɪˈflɛksɪvz/", "các đại từ phản thân (ngữ pháp)"),
    ("082326", "reflexly", "adv", "/ˈriːflɛksli/", "theo kiểu phản xạ vô điều kiện"),
    ("082327", "reflexogenic", "adj", "/rɪˌflɛksəˈdʒɛnɪk/", "kích thích gây ra phản xạ (sinh lý)"),
    ("082328", "reflexograph", "noun", "/rɪˈflɛksəˌɡræf/", "máy ghi đồ thị phản xạ (y học)"),
    ("082329", "reflexometer", "noun", "/ˌriːflɛkˈsɑːmɪtər/", "máy đo cường độ phản xạ cơ bắp"),
    ("082330", "reflorescence", "noun", "/ˌriːflɔːˈrɛsəns/", "sự nở hoa trở lại (vụ thứ hai)"),
    ("082331", "reflourish", "verb", "/ˌriːˈflɜːrɪʃ/", "hưng thịnh trở lại, nở rộ trở lại"),
    ("082332", "reflow", "verb", "/ˌriːˈfloʊ/", "chảy ngược lại; hàn chảy thiếc"),
    ("082333", "refluence", "noun", "/ˈrɛfluəns/", "dòng chảy ngược, thủy triều rút"),
    ("082334", "refluent", "adj", "/ˈrɛfluənt/", "chảy ngược lại, rút xuống"),
    ("082335", "refluxes", "noun", "/ˈriːflʌksɪz/", "hiện tượng trào ngược, chảy ngược"),
    ("082336", "refold", "verb", "/ˌriːˈfoʊld/", "gấp lại, xếp lại lần nữa"),
    ("082337", "refolded", "verb", "/ˌriːˈfoʊldɪd/", "đã gấp lại, đã cuộn gấp lại lần nữa"),
    ("082338", "refolding", "verb", "/ˌriːˈfoʊldɪŋ/", "gấp lại (protein, giấy) lần nữa"),
    ("082339", "refolds", "verb", "/ˌriːˈfoʊldz/", "gấp lại, cuộn gấp lại lần nữa"),
    ("082340", "refoliation", "noun", "/riˌfoʊliˈeɪʃən/", "sự đâm chồi ra lá trở lại"),
    ("082341", "refoot", "verb", "/ˌriːˈfʊt/", "thay phần bàn chân (tất, ủng cũ)"),
    ("082342", "reforested", "verb", "/ˌriːˈfɔːrɪstɪd/", "đã trồng lại rừng phủ xanh đồi trọc"),
    ("082343", "reforesting", "verb", "/ˌriːˈfɔːrɪstɪŋ/", "trồng lại rừng phủ xanh đất"),
    ("082344", "reforests", "verb", "/ˌriːˈfɔːrɪsts/", "trồng lại rừng phủ xanh đất trống"),
    ("082345", "reforged", "verb", "/ˌriːˈfɔːrdʒd/", "đã rèn đúc lại, tái tạo gắn kết lại"),
    ("082346", "reforges", "verb", "/ˌriːˈfɔːrdʒɪz/", "rèn lại (kim loại); tái lập quan hệ"),
    ("082347", "reforging", "verb", "/ˌriːˈfɔːrdʒɪŋ/", "rèn đúc lại; xây dựng lại bền chặt"),
    ("082348", "reformable", "adj", "/rɪˈfɔːrməbəl/", "có thể cải tạo, có thể cải cách"),
    ("082349", "reformers", "noun", "/rɪˈfɔːrmərz/", "những nhà cải cách, người đổi mới"),
    ("082350", "reforming", "verb", "/rɪˈfɔːrmɪŋ/", "cải cách, sửa đổi; hoàn lương"),
    ("082351", "reforms", "verb", "/rɪˈfɔːrmz/", "cải cách, cải thiện; hoàn lương"),
    ("082352", "refortified", "verb", "/ˌriːˈfɔːrtəˌfaɪd/", "đã củng cố lại công sự phòng thủ"),
    ("082353", "refortifies", "verb", "/ˌriːˈfɔːrtəˌfaɪz/", "gia cố phòng thủ, tăng cường"),
    ("082354", "refortify", "verb", "/ˌriːˈfɔːrtəˌfaɪ/", "gia cố phòng thủ, củng cố sức"),
    ("082355", "refortifying", "verb", "/ˌriːˈfɔːrtəˌfaɪɪŋ/", "củng cố công sự lại, tăng cường sức"),
    ("082356", "refound", "verb", "/ˌriːˈfaʊnd/", "tái lập, sáng lập lại; đúc lại"),
    ("082357", "refractable", "adj", "/rɪˈfræktəbəl/", "có thể bị khúc xạ (ánh sáng, sóng)"),
    ("082358", "refracted", "verb", "/rɪˈfræktɪd/", "đã khúc xạ (tia sáng qua lăng kính)"),
    ("082359", "refractile", "adj", "/rɪˈfræktəl/", "có khả năng khúc xạ ánh sáng"),
    ("082360", "refracting", "verb", "/rɪˈfræktɪŋ/", "khúc xạ, làm lệch tia sáng"),
    ("082361", "refractional", "adj", "/rɪˈfrækʃənəl/", "thuộc hiện tượng khúc xạ ánh sáng"),
    ("082362", "refractiveness", "noun", "/rɪˈfræktɪvnəs/", "tính khúc xạ, độ khúc xạ ánh sáng"),
    ("082363", "refractivity", "noun", "/ˌriːfrækˈtɪvəti/", "chiết suất, khả năng khúc xạ quang"),
    ("082364", "refractor", "noun", "/rɪˈfræktər/", "kính thiên văn khúc xạ"),
    ("082365", "refractors", "noun", "/rɪˈfræktərz/", "những kính thiên văn khúc xạ"),
    ("082366", "refracts", "verb", "/rɪˈfrækts/", "khúc xạ (tia sáng, sóng âm thanh)"),
    ("082367", "refracture", "verb", "/ˌriːˈfræktʃər/", "làm gãy lại (xương để nắn chỉnh, y)"),
    ("082368", "refrained", "verb", "/rɪˈfreɪnd/", "đã kiềm chế, đã kìm nén, tránh làm"),
    ("082369", "refraining", "verb", "/rɪˈfreɪnɪŋ/", "kiềm chế, kìm nén, tránh làm"),
    ("082370", "refrains", "verb", "/rɪˈfreɪnz/", "kiềm chế, nhịn không làm, kiêng cữ"),
    ("082371", "refrangible", "adj", "/rɪˈfrændʒəbəl/", "có thể khúc xạ (tia sáng, tia X)"),
    ("082372", "refreshen", "verb", "/rɪˈfrɛʃən/", "làm tươi mới, tiếp sinh lực"),
    ("082373", "refreshes", "verb", "/rɪˈfrɛʃɪz/", "làm tươi mới, sảng khoái; nạp lại"),
    ("082374", "refreshful", "adj", "/rɪˈfrɛʃfəl/", "tươi mát sảng khoái, tiếp sinh lực"),
    ("082375", "refreshfully", "adv", "/rɪˈfrɛʃfəli/", "một cách sảng khoái, mát mẻ dễ chịu"),
    ("082376", "refreshments", "noun", "/rɪˈfrɛʃmənts/", "đồ ăn nhẹ và nước giải khát"),
    ("082377", "refrigerates", "verb", "/rɪˈfrɪdʒəˌreɪts/", "làm lạnh, bảo quản lạnh"),
    ("082378", "refrigeratory", "noun", "/rɪˈfrɪdʒərəˌtɔːri/", "thiết bị làm lạnh, tủ ướp lạnh"),
    ("082379", "refringence", "noun", "/rɪˈfrɪndʒəns/", "tính khúc xạ, năng lực khúc xạ (lý)"),
    ("082380", "refringent", "adj", "/rɪˈfrɪndʒənt/", "có tính khúc xạ, chiết quang"),
    ("082381", "reft", "verb", "/rɛft/", "đã tước đoạt, đã cướp mất (thơ cổ)"),
    ("082382", "refueled", "verb", "/ˌriːˈfjuːəld/", "đã tiếp thêm nhiên liệu (xăng, dầu)"),
    ("082383", "refuels", "verb", "/ˌriːˈfjuːəlz/", "tiếp nhiên liệu lại, đổ thêm xăng"),
    ("082384", "refugence", "noun", "/rɪˈfʌldʒəns/", "ánh sáng rực rỡ chói lòa (lỗi viết)"),
    ("082385", "refugency", "noun", "/rɪˈfʌldʒənsi/", "sự chói sáng rực rỡ (lỗi viết)"),
    ("082386", "refulgence", "noun", "/rɪˈfʌldʒəns/", "ánh sáng rực rỡ, vẻ chói lòa"),
    ("082387", "refulgency", "noun", "/rɪˈfʌldʒənsi/", "vẻ chói sáng rực rỡ, sự lộng lẫy"),
    ("082388", "refundable", "adj", "/rɪˈfʌndəbəl/", "được hoàn trả lại tiền khi hủy bỏ"),
    ("082389", "refunded", "verb", "/rɪˈfʌndɪd/", "đã hoàn trả lại tiền cho khách hàng"),
    ("082390", "refunding", "verb", "/rɪˈfʌndɪŋ/", "hoàn trả tiền; tái cấp vốn"),
    ("082391", "refundment", "noun", "/rɪˈfʌndmənt/", "sự hoàn trả tiền lại (thuật ngữ cũ)"),
    ("082392", "refunds", "verb", "/rɪˈfʌndz/", "hoàn trả lại tiền, đền trả lại phí"),
    ("082393", "refurbished", "verb", "/ˌriːˈfɜːrbɪʃt/", "đã tân trang, sửa sang lại như mới"),
    ("082394", "refurbishes", "verb", "/ˌriːˈfɜːrbɪʃɪz/", "tân trang, sửa sang làm mới lại"),
    ("082395", "refurbishing", "verb", "/ˌriːˈfɜːrbɪʃɪŋ/", "tân trang, sửa chữa làm mới lại đồ"),
    ("082396", "refurnished", "verb", "/ˌriːˈfɜːrnɪʃt/", "đã trang bị lại nội thất mới"),
    ("082397", "refurnishes", "verb", "/ˌriːˈfɜːrnɪʃɪz/", "trang bị lại đồ nội thất mới"),
    ("082398", "refurnishing", "verb", "/ˌriːˈfɜːrnɪʃɪŋ/", "trang bị lại đồ đạc nội thất mới"),
    ("082399", "refusable", "adj", "/rɪˈfjuːzəbəl/", "có thể từ chối hoặc khước từ được"),
    ("082400", "refused", "verb", "/rɪˈfjuːzd/", "đã từ chối, đã khước từ yêu cầu"),
    ("082401", "refuses", "verb", "/rɪˈfjuːzɪz/", "từ chối, khước từ không chấp nhận"),
    ("082402", "refusing", "verb", "/rɪˈfjuːzɪŋ/", "từ chối, khước từ, không chịu làm"),
]

raw = json.load(open("scratch/b37_r05_raw_p4.json"))
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
with open("scratch/b37_r05_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r05_p4 saved OK")
