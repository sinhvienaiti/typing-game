import json

records = [
    ("082803", "renegading", "verb", "/ˈrɛnəˌɡeɪdɪŋ/", "phản bội, đào ngũ theo phe đối địch"),
    ("082804", "renegation", "noun", "/ˌrɛnəˈɡeɪʃən/", "sự chối bỏ, sự bội tín bội ước"),
    ("082805", "renegociate", "verb", "/ˌriːnɪˈɡoʊʃiˌeɪt/", "đàm phán lại (biến thể sai chữ)"),
    ("082806", "renegotiable", "adj", "/ˌriːnɪˈɡoʊʃəbəl/", "có thể đàm phán thương lượng lại"),
    ("082807", "renegotiated", "verb", "/ˌriːnɪˈɡoʊʃiˌeɪtɪd/", "đã đàm phán lại, thương lượng lại"),
    ("082808", "renegotiates", "verb", "/ˌriːnɪˈɡoʊʃiˌeɪts/", "đàm phán lại, thương lượng lại"),
    ("082809", "renegotiating", "verb", "/ˌriːnɪˈɡoʊʃiˌeɪtɪŋ/", "đàm phán lại, thương lượng lại"),
    ("082810", "renegue", "verb", "/rɪˈniːɡ/", "thất hứa, nuốt lời; đánh sai bài"),
    ("082811", "renes", "noun", "/ˈriːniːz/", "hai quả thận (giải phẫu học Latin)"),
    ("082812", "renest", "verb", "/ˌriːˈnɛst/", "làm lại tổ mới (chim làm tổ)"),
    ("082813", "renewals", "noun", "/rɪˈnuːəlz/", "sự gia hạn; sự phục hồi đổi mới"),
    ("082814", "renews", "verb", "/rɪˈnuːz/", "gia hạn (hợp đồng); làm mới lại"),
    ("082815", "reniculus", "noun", "/rəˈnɪkjələs/", "tiểu thùy thận (giải phẫu học)"),
    ("082816", "renipericardial", "adj", "/ˌrɛnəˌpɛrɪˈkɑːrdiəl/", "thuộc thận và màng ngoài tim"),
    ("082817", "reniportal", "adj", "/ˌrɛnəˈpɔːrtəl/", "thuộc tĩnh mạch cửa thận (sinh lý)"),
    ("082818", "renitence", "noun", "/ˈrɛnɪtəns/", "tính kháng cự đàn hồi; sự ngoan cố"),
    ("082819", "renitency", "noun", "/ˈrɛnɪtənsi/", "lực cản đàn hồi; sự cự tuyệt bướng"),
    ("082820", "renitent", "adj", "/ˈrɛnɪtənt/", "chống đối bướng bỉnh; đàn hồi"),
    ("082821", "rennin", "noun", "/ˈrɛnɪn/", "enzym rennin đông sữa làm phô mai"),
    ("082822", "renominate", "verb", "/ˌriːˈnɑːməˌneɪt/", "tái đề cử (ứng viên); đặt tên mới"),
    ("082823", "renominated", "verb", "/ˌriːˈnɑːməˌneɪtɪd/", "đã tái đề cử vào nhiệm kỳ tiếp theo"),
    ("082824", "renominates", "verb", "/ˌriːˈnɑːməˌneɪts/", "tái đề cử vào vị trí ứng cử"),
    ("082825", "renominating", "verb", "/ˌriːˈnɑːməˌneɪtɪŋ/", "tái đề cử, giới thiệu lại ứng viên"),
    ("082826", "renormalise", "verb", "/riˈnɔːrməˌlaɪz/", "tái chuẩn hóa, bình thường (Anh)"),
    ("082827", "renormalize", "verb", "/riˈnɔːrməˌlaɪz/", "tái chuẩn hóa, bình thường hóa"),
    ("082828", "renouncer", "noun", "/rɪˈnaʊnsər/", "người từ bỏ quyền, người khước từ"),
    ("082829", "renounces", "verb", "/rɪˈnaʊnsɪz/", "từ bỏ, tuyên bố khước từ, cắt đứt"),
    ("082830", "renouncing", "verb", "/rɪˈnaʊnsɪŋ/", "từ bỏ quyền lợi, khước từ, cắt đứt"),
    ("082831", "renovated", "verb", "/ˈrɛnəˌveɪtɪd/", "đã cải tạo, đã sửa sang tân trang"),
    ("082832", "renovates", "verb", "/ˈrɛnəˌveɪts/", "cải tạo, sửa chữa nâng cấp mới"),
    ("082833", "renovating", "verb", "/ˈrɛnəˌveɪtɪŋ/", "cải tạo, sửa sang tân trang lại nhà"),
    ("082834", "renovations", "noun", "/ˌrɛnəˈveɪʃənz/", "những công trình cải tạo, tu sửa"),
    ("082835", "rensselaerite", "noun", "/ˌrɛnsəˈlɛraɪt/", "khoáng vật hoạt thạch rensselaerite"),
    ("082836", "rentability", "noun", "/ˌrɛntəˈbɪləti/", "khả năng sinh lời; cho thuê được"),
    ("082837", "rente", "noun", "/rɑːnt/", "tiền lãi trái phiếu chính phủ Pháp"),
    ("082838", "rentiers", "noun", "/rɑːnˈtjɛrz/", "những người sống bằng lợi tức"),
    ("082839", "renule", "noun", "/ˈrɛnjuːl/", "tiểu thận, thùy thận nhỏ"),
    ("082840", "renumber", "verb", "/ˌriːˈnʌmbər/", "đánh số thứ tự lại (trang, nhà)"),
    ("082841", "renumbered", "verb", "/ˌriːˈnʌmbərd/", "đã đánh lại số thứ tự mới"),
    ("082842", "renumbering", "verb", "/ˌriːˈnʌmbərɪŋ/", "đánh lại số thứ tự cho danh sách"),
    ("082843", "renumbers", "verb", "/ˌriːˈnʌmbərz/", "đánh số thứ tự lại cho đúng"),
    ("082844", "renunciant", "adj", "/rɪˈnʌnsiənt/", "từ bỏ dục vọng thế tục; khước từ"),
    ("082845", "renunciative", "adj", "/rɪˈnʌnsiətɪv/", "mang tính từ bỏ, khước từ quyền lợi"),
    ("082846", "renunciatory", "adj", "/rɪˈnʌnsiəˌtɔːri/", "nhằm từ bỏ, thể hiện sự khước từ"),
    ("082847", "reoccupation", "noun", "/riˌɑːkjəˈpeɪʃən/", "sự tái chiếm đóng; sự ở lại nhà cũ"),
    ("082848", "reoccupied", "verb", "/riˈɑːkjəˌpaɪd/", "đã tái chiếm đóng; đã dọn về ở lại"),
    ("082849", "reoccupies", "verb", "/riˈɑːkjəˌpaɪz/", "tái chiếm đóng; quay lại sử dụng"),
    ("082850", "reoccupy", "verb", "/riˈɑːkjəˌpaɪ/", "tái chiếm đóng; quay lại cư ngụ"),
    ("082851", "reoccupying", "verb", "/riˈɑːkjəˌpaɪɪŋ/", "tái chiếm giữ; quay lại nơi ở cũ"),
    ("082852", "reoder", "verb", "/ˌriːˈɔːrdər/", "đặt hàng lại; sắp xếp lại (lỗi)"),
    ("082853", "reopened", "verb", "/ˌriːˈoʊpənd/", "đã mở cửa trở lại; đã tái điều tra"),
    ("082854", "reopening", "verb", "/ˌriːˈoʊpənɪŋ/", "mở cửa lại; mở lại hồ sơ điều tra"),
    ("082855", "reopens", "verb", "/ˌriːˈoʊpənz/", "mở cửa trở lại, hoạt động lại"),
    ("082856", "reordered", "verb", "/ˌriːˈɔːrdərd/", "đã đặt hàng lại; đã sắp xếp lại"),
    ("082857", "reorders", "verb", "/ˌriːˈɔːrdərz/", "đặt mua lại; sắp xếp lại thứ tự"),
    ("082858", "reorganises", "verb", "/ˌriːˈɔːrɡəˌnaɪzɪz/", "tái cơ cấu, tổ chức lại (Anh)"),
    ("082859", "reorganising", "verb", "/ˌriːˈɔːrɡəˌnaɪzɪŋ/", "tái cơ cấu, sắp xếp lại (Anh)"),
    ("082860", "reorganizes", "verb", "/ˌriːˈɔːrɡəˌnaɪzɪz/", "tái cơ cấu, tổ chức sắp xếp lại"),
    ("082861", "reorganizing", "verb", "/ˌriːˈɔːrɡəˌnaɪzɪŋ/", "tái cơ cấu, tổ chức lại bộ máy"),
    ("082862", "reoriented", "verb", "/ˌriːˈɔːriɛntɪd/", "đã định hướng lại, chuyển hướng lại"),
    ("082863", "reorienting", "verb", "/ˌriːˈɔːriɛntɪŋ/", "định hướng lại, điều chỉnh hướng"),
    ("082864", "reorients", "verb", "/ˌriːˈɔːriɛnts/", "định hướng lại, chỉnh hướng lại"),
    ("082865", "reoviridae", "noun", "/ˌriːoʊˈvaɪrəˌdiː/", "họ Vi-rút Reoviridae (gây sốt)"),
    ("082866", "repace", "verb", "/ˌriːˈpeɪs/", "bước đi bách bộ qua lại lần nữa"),
    ("082867", "repacify", "verb", "/ˌriːˈpæsəˌfaɪ/", "lập lại hòa bình, bình định trở lại"),
    ("082868", "repack", "verb", "/ˌriːˈpæk/", "đóng gói lại, xếp hành lý lại"),
    ("082869", "repackage", "verb", "/ˌriːˈpækɪdʒ/", "đóng gói lại bao bì; trình bày lại"),
    ("082870", "repacking", "verb", "/ˌriːˈpækɪŋ/", "đóng gói lại, sắp xếp bao bì lại"),
    ("082871", "repacks", "verb", "/ˌriːˈpæks/", "đóng gói lại, xếp hành lý lại"),
    ("082872", "repagination", "noun", "/ˌriːpædʒəˈneɪʃən/", "việc đánh lại số trang sách (in ấn)"),
    ("082873", "repaid", "verb", "/rɪˈpeɪd/", "đã trả lại nợ; đã đền đáp công ơn"),
    ("082874", "repainted", "verb", "/ˌriːˈpeɪntɪd/", "đã sơn lại lớp sơn mới"),
    ("082875", "repainting", "verb", "/ˌriːˈpeɪntɪŋ/", "sơn sửa lại, quét sơn mới lại"),
    ("082876", "repaints", "verb", "/ˌriːˈpeɪnts/", "sơn lại màu mới (tường, xe, tranh)"),
    ("082877", "repairable", "adj", "/rɪˈpɛrəbəl/", "có thể sửa chữa, tu sửa lại được"),
    ("082878", "repaired", "verb", "/rɪˈpɛrd/", "đã sửa chữa, đã khắc phục hư hỏng"),
    ("082879", "repairing", "verb", "/rɪˈpɛrɪŋ/", "sửa chữa, tu sửa, khắc phục hỏng"),
    ("082880", "repairment", "noun", "/rɪˈpɛrmənt/", "việc sửa chữa, sự tu bổ lại (hiếm)"),
    ("082881", "repairs", "verb", "/rɪˈpɛrz/", "sửa chữa, tu bổ; lui tới chốn nào"),
    ("082882", "repairwoman", "noun", "/rɪˈpɛrˌwʊmən/", "nữ thợ sửa chữa máy móc thiết bị"),
    ("082883", "repairwomen", "noun", "/rɪˈpɛrˌwɪmɪn/", "những nữ thợ sửa chữa kỹ thuật"),
    ("082884", "repand", "adj", "/rɪˈpænd/", "có mép lá hơi lượn sóng (thực vật)"),
    ("082885", "repaper", "verb", "/ˌriːˈpeɪpər/", "dán lại giấy dán tường mới"),
    ("082886", "reparability", "noun", "/ˌrɛpərəˈbɪləti/", "tính có thể sửa chữa hoặc đền bù"),
    ("082887", "reparations", "noun", "/ˌrɛpəˈreɪʃənz/", "tiền bồi thường chiến tranh, đền bù"),
    ("082888", "reparative", "adj", "/rɪˈpærətɪv/", "nhằm bồi thường, giúp hồi phục sửa"),
    ("082889", "repartition", "verb", "/ˌriːpɑːrˈtɪʃən/", "phân chia lại, chia lại ranh giới"),
    ("082890", "repartitioned", "verb", "/ˌriːpɑːrˈtɪʃənd/", "đã chia tách lại, phân chia lại"),
    ("082891", "repartitioning", "verb", "/ˌriːpɑːrˈtɪʃənɪŋ/", "phân vùng lại (ổ đĩa); chia lại đất"),
    ("082892", "repass", "verb", "/ˌriːˈpæs/", "đi ngang qua lại trên đường về"),
    ("082893", "repatriated", "verb", "/ˌriːˈpeɪtriˌeɪtɪd/", "đã hồi hương; đã chuyển vốn về"),
    ("082894", "repatriates", "verb", "/ˌriːˈpeɪtriˌeɪts/", "hồi hương; chuyển tiền về nước"),
    ("082895", "repatriating", "verb", "/ˌriːˈpeɪtriˌeɪtɪŋ/", "đưa hồi hương; chuyển lợi nhuận về"),
    ("082896", "repealable", "adj", "/rɪˈpiːləbəl/", "có thể bãi bỏ, hủy bỏ (đạo luật)"),
    ("082897", "repealing", "verb", "/rɪˈpiːlɪŋ/", "bãi bỏ, hủy bỏ (đạo luật, quy định)"),
    ("082898", "repeals", "verb", "/rɪˈpiːlz/", "bãi bỏ, hủy bỏ (đạo luật cũ)"),
    ("082899", "repeaters", "noun", "/rɪˈpiːtərz/", "bộ chuyển tiếp; súng liên thanh"),
    ("082900", "repeats", "verb", "/rɪˈpiːts/", "lặp lại, nhắc lại; học lại lớp"),
    ("082901", "repelled", "verb", "/rɪˈpɛld/", "đã đẩy lùi (địch); làm kinh tởm"),
    ("082902", "repellently", "adv", "/rɪˈpɛləntli/", "một cách ghê tởm, đáng kinh sợ"),
]

raw = json.load(open("scratch/b37_r06_raw_p4.json"))
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
with open("scratch/b37_r06_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r06_p4 saved OK")
