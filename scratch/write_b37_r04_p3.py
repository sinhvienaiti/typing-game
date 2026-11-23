import json

records = [
    ("081703", "reacception", "noun", "/ˌriːəkˈsɛpʃən/", "sự chấp nhận lại, sự đón nhận lại"),
    ("081704", "reaccustom", "verb", "/ˌriːəˈkʌstəm/", "tập làm quen lại từ đầu"),
    ("081705", "reached", "verb", "/riːtʃt/", "đã chạm tới; đã đạt được; liên lạc"),
    ("081706", "reaches", "verb", "/ˈriːtʃɪz/", "với tới, đạt đến; liên hệ với ai"),
    ("081707", "reachless", "adj", "/ˈriːtʃləs/", "không thể với tới, xa ngoài tầm với"),
    ("081708", "reacted", "verb", "/riˈæktɪd/", "đã phản ứng lại, đã phản hồi"),
    ("081709", "reacting", "verb", "/riˈæktɪŋ/", "phản ứng lại, đáp trả (hóa, tâm lý)"),
    ("081710", "reactionism", "noun", "/riˈækʃəˌnɪzəm/", "chủ nghĩa bảo thủ phản động"),
    ("081711", "reactionist", "adj", "/riˈækʃənɪst/", "mang tư tưởng bảo thủ chống đổi mới"),
    ("081712", "reactionless", "adj", "/riˈækʃənləs/", "không phản ứng, trơ (hóa, vật lý)"),
    ("081713", "reactions", "noun", "/riˈækʃənz/", "những phản ứng; phản ứng hóa học"),
    ("081714", "reactivates", "verb", "/riˈæktəˌveɪts/", "tái kích hoạt, hoạt hóa trở lại"),
    ("081715", "reactivating", "verb", "/riˈæktəˌveɪtɪŋ/", "tái kích hoạt, hoạt động trở lại"),
    ("081716", "reactivation", "noun", "/riˌæktəˈveɪʃən/", "sự tái kích hoạt, sự phục hồi"),
    ("081717", "reactivator", "noun", "/riˈæktəˌveɪtər/", "thiết bị hoặc chất tái kích hoạt"),
    ("081718", "reacts", "verb", "/riˈækts/", "phản ứng lại, phản hồi, tác dụng"),
    ("081719", "readably", "adv", "/ˈriːdəbli/", "một cách dễ đọc, rõ ràng mạch lạc"),
    ("081720", "readdress", "verb", "/ˌriːəˈdrɛs/", "ghi lại địa chỉ mới; xem xét lại"),
    ("081721", "readdressed", "verb", "/ˌriːəˈdrɛst/", "đã đổi địa chỉ gửi; giải quyết lại"),
    ("081722", "readdresses", "verb", "/ˌriːəˈdrɛsɪz/", "ghi lại địa chỉ gửi; xử lý lại"),
    ("081723", "readdressing", "verb", "/ˌriːəˈdrɛsɪŋ/", "ghi lại địa chỉ; xem xét giải quyết"),
    ("081724", "readerships", "noun", "/ˈriːdərˌʃɪps/", "lượng độc giả, các nhóm bạn đọc"),
    ("081725", "readied", "verb", "/ˈrɛdid/", "đã chuẩn bị sẵn sàng, đã sửa soạn"),
    ("081726", "readies", "verb", "/ˈrɛdiz/", "chuẩn bị sẵn sàng, sửa soạn chu đáo"),
    ("081727", "readjourn", "verb", "/ˌriːəˈdʒɜːrn/", "tạm hoãn lại lần nữa (phiên họp)"),
    ("081728", "readjusted", "verb", "/ˌriːəˈdʒʌstɪd/", "đã điều chỉnh lại, thích nghi lại"),
    ("081729", "readjusting", "verb", "/ˌriːəˈdʒʌstɪŋ/", "điều chỉnh lại, tái thích nghi"),
    ("081730", "readjusts", "verb", "/ˌriːəˈdʒʌsts/", "điều chỉnh lại, hiệu chỉnh lại"),
    ("081731", "readme", "noun", "/ˈriːdmiː/", "tệp hướng dẫn đi kèm phần mềm"),
    ("081732", "readmits", "verb", "/ˌriːədˈmɪts/", "cho nhập lại, nhận trở lại vào nhóm"),
    ("081733", "readmittance", "noun", "/ˌriːədˈmɪtəns/", "sự cho nhập lại, sự tái tiếp nhận"),
    ("081734", "readmitted", "verb", "/ˌriːədˈmɪtɪd/", "đã nhận lại, đã cho nhập viện lại"),
    ("081735", "readmitting", "verb", "/ˌriːədˈmɪtɪŋ/", "nhận trở lại, cho tái nhập viện"),
    ("081736", "readopt", "verb", "/ˌriːəˈdɑːpt/", "áp dụng lại; nhận nuôi lại"),
    ("081737", "readopted", "verb", "/ˌriːəˈdɑːptɪd/", "đã áp dụng lại, thông qua trở lại"),
    ("081738", "readopting", "verb", "/ˌriːəˈdɑːptɪŋ/", "áp dụng trở lại, chấp thuận lại"),
    ("081739", "readopts", "verb", "/ˌriːəˈdɑːpts/", "áp dụng trở lại, chấp thuận lại"),
    ("081740", "readorn", "verb", "/ˌriːəˈdɔːrn/", "trang hoàng lại, tô điểm lại"),
    ("081741", "reaffiliation", "noun", "/ˌriːəfɪliˈeɪʃən/", "sự tái gia nhập, kết nạp trở lại"),
    ("081742", "reaffirmed", "verb", "/ˌriːəˈfɜːrmd/", "đã tái khẳng định, xác nhận lại"),
    ("081743", "reaffirming", "verb", "/ˌriːəˈfɜːrmɪŋ/", "tái khẳng định, xác nhận lại"),
    ("081744", "reaffirms", "verb", "/ˌriːəˈfɜːrmz/", "tái khẳng định, xác nhận lại"),
    ("081745", "reafforest", "verb", "/ˌriːəˈfɔːrəst/", "trồng lại rừng (đất trọc bị phá)"),
    ("081746", "reafforestation", "noun", "/ˌriːəfɔːrəˈsteɪʃən/", "công cuộc tái trồng rừng phủ xanh"),
    ("081747", "reagency", "noun", "/riˈeɪdʒənsi/", "tác dụng phản ứng (hóa học, cũ)"),
    ("081748", "reagin", "noun", "/riˈeɪdʒɪn/", "kháng thể dị ứng IgE (miễn dịch)"),
    ("081749", "realia", "noun", "/riˈeɪliə/", "vật thật làm giáo cụ trực quan"),
    ("081750", "realigned", "verb", "/ˌriːəˈlaɪnd/", "đã căn chỉnh lại; sắp xếp hàng ngũ"),
    ("081751", "realigning", "verb", "/ˌriːəˈlaɪnɪŋ/", "căn chỉnh lại; tái cơ cấu liên minh"),
    ("081752", "realignment", "noun", "/ˌriːəˈlaɪnmənt/", "sự căn chỉnh lại; sự tái liên kết"),
    ("081753", "realigns", "verb", "/ˌriːəˈlaɪnz/", "căn chỉnh lại; tái sắp xếp vị thế"),
    ("081754", "realine", "verb", "/ˌriːəˈlaɪn/", "căn chỉnh lại, sắp xếp lại"),
    ("081755", "realises", "verb", "/ˈriːəˌlaɪzɪz/", "nhận ra, hiểu rõ; thực hiện (Anh)"),
    ("081756", "realising", "verb", "/ˈriːəˌlaɪzɪŋ/", "nhận ra, ý thức; thực hiện (Anh)"),
    ("081757", "realizability", "noun", "/ˌriːəlaɪzəˈbɪləti/", "tính khả thi, khả năng thực hiện"),
    ("081758", "realizations", "noun", "/ˌriːələˈzeɪʃənz/", "những sự nhận thức; việc thực hiện"),
    ("081759", "realizes", "verb", "/ˈriːəˌlaɪzɪz/", "nhận ra, ý thức được; thực hiện"),
    ("081760", "realizing", "verb", "/ˈriːəˌlaɪzɪŋ/", "nhận ra, thấu hiểu; biến thành thực"),
    ("081761", "reallot", "verb", "/ˌriːəˈlɑːt/", "phân bổ lại, chia phần lại"),
    ("081762", "reallotment", "noun", "/ˌriːəˈlɑːtmənt/", "sự phân bổ lại, sự tái chia phần"),
    ("081763", "realtime", "adj", "/ˈriːəlˌtaɪm/", "theo thời gian thực, tức thời"),
    ("081764", "reamed", "verb", "/riːmd/", "đã doa rộng lỗ; đã mắng té tát"),
    ("081765", "reamers", "noun", "/ˈriːmərz/", "mũi doa lỗ; dụng cụ vắt cam"),
    ("081766", "reamimate", "verb", "/riˈænəˌmeɪt/", "làm hồi sinh, khích lệ (biến thể)"),
    ("081767", "reamimation", "noun", "/riˌænəˈmeɪʃən/", "sự hồi sinh trở lại (biến thể lỗi)"),
    ("081768", "reaming", "verb", "/ˈriːmɪŋ/", "doa rộng lỗ; vắt kiệt; mắng xối xả"),
    ("081769", "reamkerti", "noun", "/riəmˈkɜːrti/", "sử thi Reamker của Campuchia"),
    ("081770", "reams", "verb", "/riːmz/", "doa rộng lỗ kim loại; mắng xối xả"),
    ("081771", "reannex", "verb", "/ˌriːəˈnɛks/", "tái sáp nhập (lãnh thổ trở lại)"),
    ("081772", "reaped", "verb", "/riːpt/", "đã gặt hái, thu hoạch; gặt kết quả"),
    ("081773", "reaping", "verb", "/ˈriːpɪŋ/", "gặt hái, thu hoạch; nhận hậu quả"),
    ("081774", "reapparel", "verb", "/ˌriːəˈpærəl/", "thay trang phục mới cho, mặc lại"),
    ("081775", "reappeared", "verb", "/ˌriːəˈpɪrd/", "đã xuất hiện trở lại, tái hiện"),
    ("081776", "reappearing", "verb", "/ˌriːəˈpɪrɪŋ/", "xuất hiện trở lại, tái xuất hiện"),
    ("081777", "reappears", "verb", "/ˌriːəˈpɪrz/", "xuất hiện trở lại, tái xuất hiện"),
    ("081778", "reapplication", "noun", "/ˌriːæplɪˈkeɪʃən/", "sự áp dụng lại; sự nộp đơn lại"),
    ("081779", "reappoint", "verb", "/ˌriːəˈpɔɪnt/", "tái bổ nhiệm chức vụ trở lại"),
    ("081780", "reappointed", "verb", "/ˌriːəˈpɔɪntɪd/", "đã tái bổ nhiệm chức vụ trở lại"),
    ("081781", "reappointing", "verb", "/ˌriːəˈpɔɪntɪŋ/", "tái bổ nhiệm, cử lại vào chức cũ"),
    ("081782", "reappointment", "noun", "/ˌriːəˈpɔɪntmənt/", "sự tái bổ nhiệm vào chức vụ cũ"),
    ("081783", "reappoints", "verb", "/ˌriːəˈpɔɪnts/", "tái bổ nhiệm, bổ nhiệm lại chức cũ"),
    ("081784", "reapportion", "verb", "/ˌriːəˈpɔːrʃən/", "phân chia lại (ghế, ngân quỹ)"),
    ("081785", "reaps", "verb", "/riːps/", "gặt hái, thu hoạch; gặt thành quả"),
    ("081786", "reared", "verb", "/rɪrd/", "đã nuôi nấng; đã chồm lên (ngựa)"),
    ("081787", "rearer", "noun", "/ˈrɪrər/", "người chăn nuôi gia súc, nuôi dạy"),
    ("081788", "rearmed", "verb", "/ˌriːˈɑːrmd/", "đã tái vũ trang, trang bị vũ khí"),
    ("081789", "rearming", "verb", "/ˌriːˈɑːrmɪŋ/", "tái vũ trang, trang bị lại khí tài"),
    ("081790", "rearms", "verb", "/ˌriːˈɑːrmz/", "tái vũ trang, cấp lại vũ khí"),
    ("081791", "rearranged", "verb", "/ˌriːəˈreɪndʒd/", "đã sắp xếp lại, đã bố trí lại"),
    ("081792", "rearranges", "verb", "/ˌriːəˈreɪndʒɪz/", "sắp xếp lại, bố trí lại trình tự"),
    ("081793", "rearranging", "verb", "/ˌriːəˈreɪndʒɪŋ/", "sắp xếp lại, tổ chức lại trật tự"),
    ("081794", "rearrangment", "noun", "/ˌriːəˈreɪndʒmənt/", "sự sắp xếp lại (biến thể sai chữ)"),
    ("081795", "rears", "verb", "/rɪrz/", "nuôi dưỡng; dựng lên; chồm hai chân"),
    ("081796", "reascend", "verb", "/ˌriːəˈsɛnd/", "trèo lên lại, thăng tiến trở lại"),
    ("081797", "reascended", "verb", "/ˌriːəˈsɛndɪd/", "đã trèo lên lại, đã bay vút lên lại"),
    ("081798", "reascending", "verb", "/ˌriːəˈsɛndɪŋ/", "leo lên lại, dâng cao trở lại"),
    ("081799", "reascends", "verb", "/ˌriːəˈsɛndz/", "leo lên lại, thăng tiến trở lại"),
    ("081800", "reasonings", "noun", "/ˈriːzənɪŋz/", "các lập luận, chuỗi suy luận logic"),
    ("081801", "reasonless", "adj", "/ˈriːzənləs/", "vô lý, thiếu lý trí, phi lý"),
    ("081802", "reasonnable", "adj", "/ˈriːzənəbəl/", "hợp lý, phải chăng (biến thể cổ)"),
]

raw = json.load(open("scratch/b37_r04_raw_p3.json"))
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
with open("scratch/b37_r04_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r04_p3 saved OK")
