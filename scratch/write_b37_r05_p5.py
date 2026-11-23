import json

records = [
    ("082403", "refusion", "noun", "/ˌriːˈfjuːʒən/", "sự nấu chảy lại (kim loại)"),
    ("082404", "refutal", "noun", "/rɪˈfjuːtəl/", "sự bác bỏ, lập luận phản bác"),
    ("082405", "refutatory", "adj", "/rɪˈfjuːtəˌtɔːri/", "nhằm bác bỏ, mang tính phản bác"),
    ("082406", "refuted", "verb", "/rɪˈfjuːtɪd/", "đã bác bỏ, đã chứng minh là sai"),
    ("082407", "refuter", "noun", "/rɪˈfjuːtər/", "người bác bỏ, người phản bác lý lẽ"),
    ("082408", "refutes", "verb", "/rɪˈfjuːts/", "bác bỏ, phản bác, chứng minh sai"),
    ("082409", "refuting", "verb", "/rɪˈfjuːtɪŋ/", "bác bỏ, phản bác bằng lý lẽ sắc bén"),
    ("082410", "regained", "verb", "/rɪˈɡeɪnd/", "đã lấy lại được, đã giành lại được"),
    ("082411", "regains", "verb", "/rɪˈɡeɪnz/", "lấy lại, giành lại; hồi phục lại"),
    ("082412", "regalecidae", "noun", "/ˌrɛɡəˈliːsɪˌdiː/", "họ Cá mái chèo, cá hố rồng"),
    ("082413", "regaled", "verb", "/rɪˈɡeɪld/", "đã thết đãi; kể chuyện mua vui"),
    ("082414", "regalement", "noun", "/rɪˈɡeɪlmənt/", "tiệc thết đãi, sự chiêu đãi"),
    ("082415", "regales", "verb", "/rɪˈɡeɪlz/", "thết đãi linh đình; mua vui"),
    ("082416", "regaling", "verb", "/rɪˈɡeɪlɪŋ/", "thết đãi hậu hĩnh; kể mua vui"),
    ("082417", "regalism", "noun", "/ˈriːɡəˌlɪzəm/", "thuyết quyền tối thượng của nhà vua"),
    ("082418", "regalist", "noun", "/ˈriːɡəlɪst/", "người ủng hộ vương quyền giáo hội"),
    ("082419", "regality", "noun", "/rɪˈɡæləti/", "vương quyền, uy nghi bậc đế vương"),
    ("082420", "regardant", "adj", "/rɪˈɡɑːrdənt/", "ngoái đầu nhìn lại (huy hiệu)"),
    ("082421", "regarded", "verb", "/rɪˈɡɑːrdɪd/", "đã coi như, đánh giá; nhìn chăm chú"),
    ("082422", "regardful", "adj", "/rɪˈɡɑːrdfəl/", "kính cẩn, quan tâm chu đáo"),
    ("082423", "regarding", "prep", "/rɪˈɡɑːrdɪŋ/", "về việc, liên quan đến, đối với"),
    ("082424", "regards", "verb", "/rɪˈɡɑːrdz/", "coi là, xem như; quan tâm; nhìn kỹ"),
    ("082425", "regather", "verb", "/ˌriːˈɡæðər/", "tập hợp lại, gom tụ lại một chỗ"),
    ("082426", "regathered", "verb", "/ˌriːˈɡæðərd/", "đã tập hợp lại, lấy lại sức"),
    ("082427", "regathering", "verb", "/ˌriːˈɡæðərɪŋ/", "tập hợp lại, gom lại; thu hồi lực"),
    ("082428", "regathers", "verb", "/ˌriːˈɡæðərz/", "tập hợp lại, tụ họp lại đông đủ"),
    ("082429", "regd", "adj", "/ˈrɛdʒɪstərd/", "đã đăng ký chính thức (viết tắt)"),
    ("082430", "regelate", "verb", "/rɪˈdʒɛˌleɪt/", "tái đóng băng lại dưới áp suất"),
    ("082431", "regelation", "noun", "/ˌriːdʒəˈleɪʃən/", "hiện tượng tái đóng băng nước đá"),
    ("082432", "regenerated", "verb", "/rɪˈdʒɛnəˌreɪtɪd/", "đã tái sinh, tái tạo; cải tạo"),
    ("082433", "regenerates", "verb", "/rɪˈdʒɛnəˌreɪts/", "tái sinh, tái tạo; phục hồi"),
    ("082434", "regenerative", "adj", "/rɪˈdʒɛnərətɪv/", "có khả năng tái sinh, tái tạo"),
    ("082435", "regenerator", "noun", "/rɪˈdʒɛnəˌreɪtər/", "bộ tái sinh nhiệt (lò luyện thép)"),
    ("082436", "regenesis", "noun", "/ˌriːˈdʒɛnəsɪs/", "sự tái sinh, sự hồi sinh trở lại"),
    ("082437", "regentship", "noun", "/ˈriːdʒəntʃɪp/", "chức vụ nhiếp chính vương"),
    ("082438", "regerminate", "verb", "/ˌriːˈdʒɜːrməˌneɪt/", "nảy mầm trở lại, đâm chồi lại"),
    ("082439", "regermination", "noun", "/ˌriːdʒɜːrməˈneɪʃən/", "sự nảy mầm trở lại của hạt giống"),
    ("082440", "reget", "verb", "/ˌriːˈɡɛt/", "có được trở lại, lấy lại (hiếm)"),
    ("082441", "reggane", "noun", "/rəˈɡɑːn/", "thị trấn ốc đảo Reggane (Algeria)"),
    ("082442", "regicidal", "adj", "/ˌrɛdʒəˈsaɪdəl/", "thuộc tội giết vua (lịch sử)"),
    ("082443", "regiciders", "noun", "/ˈrɛdʒəˌsaɪdərz/", "những kẻ phạm tội ám sát nhà vua"),
    ("082444", "regie", "noun", "/reɪˈʒiː/", "chế độ độc quyền nhà nước; đạo diễn"),
    ("082445", "regild", "verb", "/ˌriːˈɡɪld/", "mạ vàng lại, thiếp vàng cho sáng"),
    ("082446", "regimentally", "adv", "/ˌrɛdʒəˈmɛntəli/", "theo quy củ trung đoàn quân đội"),
    ("082447", "regimenting", "verb", "/ˈrɛdʒəˌmɛntɪŋ/", "ép vào khuôn phép kỷ luật chặt chẽ"),
    ("082448", "regiments", "verb", "/ˈrɛdʒəˌmɛnts/", "quản lý chặt, gò vào khuôn khổ"),
    ("082449", "reginal", "adj", "/rɪˈdʒaɪnəl/", "thuộc nữ vương, ủng hộ nữ hoàng"),
    ("082450", "regionalise", "verb", "/ˈriːdʒənəˌlaɪz/", "khu vực hóa, phân vùng địa phương"),
    ("082451", "regionalist", "adj", "/ˈriːdʒənəlɪst/", "mang tính địa phương, phân vùng"),
    ("082452", "regionalists", "noun", "/ˈriːdʒənəlɪsts/", "người theo chủ nghĩa địa phương"),
    ("082453", "regionality", "noun", "/ˌriːdʒəˈnæləti/", "tính vùng miền, bản sắc địa phương"),
    ("082454", "regionalize", "verb", "/ˈriːdʒənəˌlaɪz/", "khu vực hóa, phân chia theo vùng"),
    ("082455", "registering", "verb", "/ˈrɛdʒɪstərɪŋ/", "đăng ký, ghi danh; biểu lộ"),
    ("082456", "registers", "verb", "/ˈrɛdʒɪstərz/", "đăng ký, ghi danh; ghi nhận"),
    ("082457", "registrarship", "noun", "/ˈrɛdʒɪstrɑːrˌʃɪp/", "chức trưởng phòng đào tạo, hộ tịch"),
    ("082458", "registrary", "noun", "/ˈrɛdʒɪstrəri/", "viên chức lưu trữ hồ sơ (Cambridge)"),
    ("082459", "reglaecus", "noun", "/ˌrɛɡəˈliːkəs/", "chi cá hố rồng (Regalecus)"),
    ("082460", "reglet", "noun", "/ˈrɛɡlɪt/", "nẹp gỗ chèn dòng chữ in; gờ phẳng"),
    ("082461", "regnal", "adj", "/ˈrɛɡnəl/", "thuộc triều đại trị vì của nhà vua"),
    ("082462", "regnancy", "noun", "/ˈrɛɡnənsi/", "sự trị vì, quyền cai trị tối cao"),
    ("082463", "regnellidium", "noun", "/ˌrɛɡnəˈlɪdiəm/", "chi dương xỉ nước hai lá (Nam Mỹ)"),
    ("082464", "regorge", "verb", "/rɪˈɡɔːrdʒ/", "nôn trớ ra; tràn ngược ra lại"),
    ("082465", "regosol", "noun", "/ˈrɛɡəˌsɔːl/", "đất regosol non kém phát triển"),
    ("082466", "regrant", "verb", "/ˌriːˈɡrænt/", "cấp lại (giấy phép, quyền lợi)"),
    ("082467", "regrate", "verb", "/rɪˈɡreɪt/", "đầu cơ thực phẩm bán giá cao"),
    ("082468", "regressand", "noun", "/ˈriːɡrɛsænd/", "biến phụ thuộc (thống kê hồi quy)"),
    ("082469", "regressed", "verb", "/rɪˈɡrɛst/", "đã thoái lui, thụt lùi về trước"),
    ("082470", "regresses", "verb", "/rɪˈɡrɛsɪz/", "thoái lui, thụt lùi; hồi quy (toán)"),
    ("082471", "regressing", "verb", "/rɪˈɡrɛsɪŋ/", "thoái lui, thụt lùi về giai đoạn cũ"),
    ("082472", "regressor", "noun", "/rɪˈɡrɛsər/", "biến độc lập giải thích (hồi quy)"),
    ("082473", "regretted", "verb", "/rɪˈɡrɛtɪd/", "đã hối tiếc, đã lấy làm tiếc"),
    ("082474", "regretting", "verb", "/rɪˈɡrɛtɪŋ/", "hối tiếc, ân hận, lấy làm tiếc"),
    ("082475", "regrouped", "verb", "/ˌriːˈɡruːpt/", "đã tập hợp lại, chấn chỉnh đội ngũ"),
    ("082476", "regrouping", "verb", "/ˌriːˈɡruːpɪŋ/", "tập hợp lại, sắp xếp lại đội hình"),
    ("082477", "regroups", "verb", "/ˌriːˈɡruːps/", "tập hợp lại, tái tổ chức lực lượng"),
    ("082478", "regt", "noun", "/ˈrɛdʒəmənt/", "trung đoàn quân đội (viết tắt)"),
    ("082479", "regulable", "adj", "/ˈrɛɡjələbəl/", "có thể điều chỉnh, chỉnh lý được"),
    ("082480", "regularised", "verb", "/ˈrɛɡjələˌraɪzd/", "đã hợp thức hóa, quy chuẩn (Anh)"),
    ("082481", "regularises", "verb", "/ˈrɛɡjələˌraɪzɪz/", "hợp thức hóa, quy chuẩn (Anh)"),
    ("082482", "regularising", "verb", "/ˈrɛɡjələˌraɪzɪŋ/", "hợp thức hóa, chuẩn hóa (Anh)"),
    ("082483", "regularities", "noun", "/ˌrɛɡjəˈlærətiz/", "tính đều đặn; quy luật ổn định"),
    ("082484", "regularized", "verb", "/ˈrɛɡjələˌraɪzd/", "đã hợp thức hóa, điều chỉnh đều"),
    ("082485", "regularizes", "verb", "/ˈrɛɡjələˌraɪzɪz/", "hợp thức hóa, đưa vào quy củ"),
    ("082486", "regularizing", "verb", "/ˈrɛɡjələˌraɪzɪŋ/", "hợp thức hóa, chuẩn hóa quy trình"),
    ("082487", "regulations", "noun", "/ˌrɛɡjəˈleɪʃənz/", "các quy định, quy chế, điều lệ"),
    ("082488", "regulators", "noun", "/ˈrɛɡjəˌleɪtərz/", "cơ quan quản lý; bộ điều chỉnh áp"),
    ("082489", "reguli", "noun", "/ˈrɛɡjəˌlaɪ/", "chim vàng anh mào lửa"),
    ("082490", "regur", "noun", "/ˈreɪɡʊr/", "đất sét đen trồng bông Ấn Độ"),
    ("082491", "regurgitant", "adj", "/rɪˈɡɜːrdʒɪtənt/", "trào ngược lên, ọc ra, chảy ngược"),
    ("082492", "regurgitated", "verb", "/rɪˈɡɜːrdʒəˌteɪtɪd/", "đã trào ngược; đã lặp lại máy móc"),
    ("082493", "regurgitates", "verb", "/rɪˈɡɜːrdʒəˌteɪts/", "trào ngược, nôn ra; lặp máy móc"),
    ("082494", "regurgitating", "verb", "/rɪˈɡɜːrdʒəˌteɪtɪŋ/", "trào ngược lên; lặp lại không hiểu"),
    ("082495", "rehab", "noun", "/ˈriːhæb/", "trung tâm cai nghiện; phục hồi"),
    ("082496", "rehabilitant", "noun", "/ˌriːəˈbɪlətənt/", "người đang tập phục hồi chức năng"),
    ("082497", "rehabilitated", "verb", "/ˌriːəˈbɪləˌteɪtɪd/", "đã phục hồi chức năng; minh oan"),
    ("082498", "rehabilitates", "verb", "/ˌriːəˈbɪləˌteɪts/", "phục hồi chức năng; cải tạo"),
    ("082499", "rehabilitating", "verb", "/ˌriːəˈbɪləˌteɪtɪŋ/", "phục hồi chức năng; khôi phục"),
    ("082500", "rehabs", "noun", "/ˈriːhæbz/", "các trại cai nghiện, cơ sở phục hồi"),
    ("082501", "rehandle", "verb", "/ˌriːˈhændəl/", "xử lý lại, làm lại; thay cán mới"),
    ("082502", "rehang", "verb", "/ˌriːˈhæŋ/", "treo lại (tranh, cửa, rèm)"),
]

raw = json.load(open("scratch/b37_r05_raw_p5.json"))
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
with open("scratch/b37_r05_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r05_p5 saved OK")
