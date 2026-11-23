import json

RECORDS = [
    ("086103", "sensationalized", "verb", "/sɛnˈseɪʃənəˌlaɪzd/", "đã giật gân hóa; đã thổi phồng"),
    ("086104", "sensationalizes", "verb", "/sɛnˈseɪʃənəˌlaɪzɪz/", "giật gân hóa; thổi phồng câu view"),
    ("086105", "sensationalizing", "verb", "/sɛnˈseɪʃənəˌlaɪzɪŋ/", "đang giật gân hóa; đang thổi phồng"),
    ("086106", "senses", "verb", "/ˈsɛnsɪz/", "cảm nhận thấy; đánh hơi thấy"),
    ("086107", "sensibilise", "verb", "/ˈsɛnsəbəˌlaɪz/", "làm nhạy cảm; nâng cao nhận thức"),
    ("086108", "sensibilization", "noun", "/ˌsɛnsəbələˈzeɪʃən/", "sự làm tăng độ nhạy cảm"),
    ("086109", "sensibilize", "verb", "/ˈsɛnsəbəˌlaɪz/", "làm nhạy cảm; nâng cao nhận thức"),
    ("086110", "sensibleness", "noun", "/ˈsɛnsəbəlnəs/", "sự hợp lý; tính sáng suốt thực tế"),
    ("086111", "sensify", "verb", "/ˈsɛnsəˌfaɪ/", "làm cho có cảm giác; nhạy cảm hóa"),
    ("086112", "sensitiser", "noun", "/ˈsɛnsɪˌtaɪzər/", "chất làm tăng độ nhạy"),
    ("086113", "sensitises", "verb", "/ˈsɛnsɪˌtaɪzɪz/", "làm nhạy cảm; nâng cao nhận thức"),
    ("086114", "sensitivenesses", "noun", "/ˈsɛnsɪtɪvnəsɪz/", "độ nhạy cảm; tính dễ bị tổn thương"),
    ("086115", "sensitives", "noun", "/ˈsɛnsɪtɪvz/", "người nhạy cảm; cây trinh nữ"),
    ("086116", "sensitivities", "noun", "/ˌsɛnsɪˈtɪvɪtiz/", "độ nhạy; sự nhạy cảm"),
    ("086117", "sensitizes", "verb", "/ˈsɛnsɪˌtaɪzɪz/", "làm nhạy cảm; gây mẫn cảm"),
    ("086118", "sensitometer", "noun", "/ˌsɛnsɪˈtɑːmɪtər/", "cảm quang kế; máy đo độ nhạy sáng"),
    ("086119", "sensitometry", "noun", "/ˌsɛnsɪˈtɑːmətri/", "phép đo độ nhạy phim ảnh"),
    ("086120", "sensoria", "noun", "/sɛnˈsɔːriə/", "vùng cảm giác não bộ; giác quan"),
    ("086121", "sensorimoror", "adj", "/ˌsɛnsəriˈmoʊtər/", "cảm giác và vận động"),
    ("086122", "sensualise", "verb", "/ˈsɛnʃuəˌlaɪz/", "nhấn mạnh nhục dục; gợi dục hóa"),
    ("086123", "sensualization", "noun", "/ˌsɛnʃuələˈzeɪʃən/", "sự nhục dục hóa; sự đam mê xác thịt"),
    ("086124", "sensualize", "verb", "/ˈsɛnʃuəˌlaɪz/", "nhục dục hóa; khiến đam mê xác thịt"),
    ("086125", "sensualness", "noun", "/ˈsɛnʃuəlnəs/", "tính gợi cảm xác thịt; sự nhục dục"),
    ("086126", "sentenced", "verb", "/ˈsɛntənst/", "đã tuyên án; đã kết án"),
    ("086127", "sentences", "verb", "/ˈsɛntənsɪz/", "tuyên án; kết án"),
    ("086128", "sentencing", "verb", "/ˈsɛntənsɪŋ/", "đang tuyên án; đang kết án"),
    ("086129", "sententia", "noun", "/sɛnˈtɛnʃə/", "câu danh ngôn; lời châm ngôn"),
    ("086130", "sententiousness", "noun", "/sɛnˈtɛnʃəsnəs/", "giọng điệu giáo huấn ra vẻ triết lý"),
    ("086131", "sentiency", "noun", "/ˈsɛnʃənsi/", "năng lực tri giác; khả năng cảm thụ"),
    ("086132", "sentimentalisation", "noun", "/ˌsɛntɪˌmɛntəlaɪˈzeɪʃən/", "sự đa cảm hóa; sự ủy mị hóa"),
    ("086133", "sentimentalise", "verb", "/ˌsɛntɪˈmɛntəˌlaɪz/", "ủy mị hóa; lãng mạn hóa sướt mướt"),
    ("086134", "sentimentalised", "verb", "/ˌsɛntɪˈmɛntəˌlaɪzd/", "đã ủy mị hóa; đã làm đa cảm"),
    ("086135", "sentimentalises", "verb", "/ˌsɛntɪˈmɛntəˌlaɪzɪz/", "ủy mị hóa; làm cho đa cảm"),
    ("086136", "sentimentalising", "verb", "/ˌsɛntɪˈmɛntəˌlaɪzɪŋ/", "đang ủy mị hóa; đang làm đa cảm"),
    ("086137", "sentimentalization", "noun", "/ˌsɛntɪˌmɛntələˈzeɪʃən/", "sự đa cảm hóa; sự ủy mị hóa"),
    ("086138", "sentimentalized", "verb", "/ˌsɛntɪˈmɛntəˌlaɪzd/", "đã ủy mị hóa; đã làm đa cảm"),
    ("086139", "sentimentalizes", "verb", "/ˌsɛntɪˈmɛntəˌlaɪzɪz/", "ủy mị hóa; làm cho đa cảm"),
    ("086140", "sentimentalizing", "verb", "/ˌsɛntɪˈmɛntəˌlaɪzɪŋ/", "đang ủy mị hóa; đang làm đa cảm"),
    ("086141", "sentimentise", "verb", "/ˈsɛntəˌmɛntaɪz/", "cư xử đa cảm; ủy mị"),
    ("086142", "sentimentize", "verb", "/ˈsɛntəˌmɛntaɪz/", "cư xử đa cảm; ủy mị"),
    ("086143", "sentiments", "noun", "/ˈsɛntəmənts/", "tình cảm; tâm tư; quan điểm"),
    ("086144", "sentries", "noun", "/ˈsɛntriz/", "lính gác; vọng gác"),
    ("086145", "seo", "noun", "/ˌɛsˌiːˈoʊ/", "tối ưu hóa công cụ tìm kiếm (SEO)"),
    ("086146", "sepaline", "adj", "/ˈsɛpəˌlaɪn/", "thuộc lá đài; giống lá đài"),
    ("086147", "sepaloid", "adj", "/ˈsɛpəˌlɔɪd/", "giống lá đài (hoa)"),
    ("086148", "separableness", "noun", "/ˈsɛpərəbəlnəs/", "tính có thể tách rời"),
    ("086149", "separably", "adv", "/ˈsɛpərəbli/", "có thể tách rời; riêng rẽ nhau"),
    ("086150", "separates", "verb", "/ˈsɛpəˌreɪts/", "tách rời; phân chia; ly thân"),
    ("086151", "separating", "verb", "/ˈsɛpəˌreɪtɪŋ/", "đang tách rời; đang phân chia"),
    ("086152", "separationism", "noun", "/ˌsɛpəˈreɪʃəˌnɪzəm/", "chủ nghĩa ly khai phân tách"),
    ("086153", "separationist", "noun", "/ˌsɛpəˈreɪʃənɪst/", "người theo chủ nghĩa ly khai"),
    ("086154", "separations", "noun", "/ˌsɛpəˈreɪʃənz/", "sự chia ly; sự tách rời; ly thân"),
    ("086155", "separatrix", "noun", "/ˌsɛpəˈreɪtrɪks/", "dấu phân cách; đường phân chia"),
    ("086156", "seperant", "noun", "/ˈsɛpərənt/", "chất tách lớp; tác nhân phân tách"),
    ("086157", "sepiabone", "noun", "/ˈsiːpiəˌboʊn/", "mai mực nang"),
    ("086158", "sepiidae", "noun", "/sɪˈpaɪɪˌdiː/", "họ Mực nang (Sepiidae)"),
    ("086159", "sepoy", "noun", "/ˈsiːpɔɪ/", "lính Ấn Độ dưới quyền thực dân Anh"),
    ("086160", "seps", "noun", "/sɛps/", "thằn lằn bóng chân ngắn; rắn độc"),
    ("086161", "septa", "noun", "/ˈsɛptə/", "vách ngăn (giải phẫu, thực vật)"),
    ("086162", "septan", "adj", "/ˈsɛptən/", "tái phát cách mỗi sáu ngày (sốt)"),
    ("086163", "septangle", "noun", "/ˈsɛptˌæŋɡəl/", "hình thất giác; hình bảy cạnh"),
    ("086164", "septation", "noun", "/sɛpˈteɪʃən/", "sự chia khoang bằng vách ngăn"),
    ("086165", "septectomy", "noun", "/sɛpˈtɛktəmi/", "phẫu thuật cắt vách ngăn mũi"),
    ("086166", "septembrist", "noun", "/sɛpˈtɛmbrɪst/", "người dự vụ thảm sát tháng 9 Pháp"),
    ("086167", "septempartite", "adj", "/ˌsɛptɛmˈpɑːrtaɪt/", "chia sâu thành bảy phần (lá)"),
    ("086168", "septenate", "adj", "/ˈsɛptəˌneɪt/", "xếp thành nhóm bảy; bảy lá chét"),
    ("086169", "septennate", "noun", "/sɛpˈtɛnət/", "nhiệm kỳ bảy năm; chu kỳ bảy năm"),
    ("086170", "septennial", "adj", "/sɛpˈtɛniəl/", "bảy năm một lần; kéo dài bảy năm"),
    ("086171", "septette", "noun", "/sɛpˈtɛt/", "nhóm bảy người; bản nhạc bảy bè"),
    ("086172", "septicaemic", "adj", "/ˌsɛptɪˈsiːmɪk/", "thuộc nhiễm trùng máu"),
    ("086173", "septicidal", "adj", "/ˌsɛptɪˈsaɪdəl/", "nứt tách dọc theo vách (quả nang)"),
    ("086174", "septiferous", "adj", "/sɛpˈtɪfərəs/", "có vách ngăn"),
    ("086175", "septifolious", "adj", "/ˌsɛptɪˈfoʊliəs/", "có bảy lá"),
    ("086176", "septifragal", "adj", "/sɛpˈtɪfrəɡəl/", "nứt tách lìa khỏi vách (quả)"),
    ("086177", "septilateral", "adj", "/ˌsɛptɪˈlætərəl/", "có bảy cạnh"),
    ("086178", "septillion", "num", "/sɛpˈtɪljən/", "một tỷ triệu tỷ (mười mũ 24)"),
    ("086179", "septimal", "adj", "/ˈsɛptɪməl/", "thuộc số bảy; chia theo bảy"),
    ("086180", "septimation", "noun", "/ˌsɛptɪˈmeɪʃən/", "sự trích lấy một phần bảy"),
    ("086181", "septobasidiaceae", "noun", "/ˌsɛptoʊbəˌsɪdiˈeɪsiːˌiː/", "họ Nấm ký sinh rệp sáp"),
    ("086182", "septobasidium", "noun", "/ˌsɛptoʊbəˈsɪdiəm/", "chi nấm ký sinh Septobasidium"),
    ("086183", "septrional", "adj", "/sɛpˈtɛntriənəl/", "thuộc phương Bắc"),
    ("086184", "septuagenary", "adj", "/ˌsɛptʃuəˈdʒɛnəri/", "ở tuổi bảy mươi; gồm bảy mươi"),
    ("086185", "sepulchred", "verb", "/ˈsɛpəlkərd/", "đã chôn cất trong lăng mộ"),
    ("086186", "sepulchres", "verb", "/ˈsɛpəlkərz/", "chôn cất vào lăng mộ"),
    ("086187", "sepulchring", "verb", "/ˈsɛpəlkərɪŋ/", "đang chôn cất trong lăng mộ"),
    ("086188", "sequacious", "adj", "/sɪˈkweɪʃəs/", "tuân theo mù quáng; mạch lạc"),
    ("086189", "sequacity", "noun", "/sɪˈkwæsɪti/", "tính phụ thuộc dễ bảo; tính dẻo"),
    ("086190", "sequalae", "noun", "/sɪˈkwiːliː/", "di chứng bệnh lý"),
    ("086191", "sequella", "noun", "/sɪˈkwɛlə/", "di chứng bệnh; hậu quả thứ phát"),
    ("086192", "sequenator", "noun", "/ˈsiːkwəˌneɪtər/", "máy giải trình tự axit amin"),
    ("086193", "sequenced", "adj", "/ˈsiːkwənst/", "đã giải trình tự; đã xếp theo thứ tự"[:35]),
    ("086194", "sequences", "noun", "/ˈsiːkwənsɪz/", "trình tự; dãy số; chuỗi cảnh phim"),
    ("086195", "sequencing", "noun", "/ˈsiːkwənsɪŋ/", "giải trình tự gen; sắp xếp trình tự"[:35]),
    ("086196", "sequentiality", "noun", "/sɪˌkwɛnʃiˈælɪti/", "tính tuần tự nối tiếp nhau"),
    ("086197", "sequestering", "verb", "/sɪˈkwɛstərɪŋ/", "đang cô lập; đang kê biên tài sản"),
    ("086198", "sequesters", "verb", "/sɪˈkwɛstərz/", "cô lập; kê biên tài sản tạm thời"),
    ("086199", "sequestra", "noun", "/sɪˈkwɛstrə/", "mảnh xương chết tách rời"),
    ("086200", "sequestrable", "adj", "/sɪˈkwɛstrəbəl/", "có thể kê biên tịch thu tạm thời"),
    ("086201", "sequestral", "adj", "/sɪˈkwɛstrəl/", "thuộc mảnh xương chết"),
    ("086202", "sequestrate", "verb", "/ˈsiːkwɪˌstreɪt/", "tịch thu tạm thời; cô lập"),
]

# Trim those longer than 35 cleanly
RECORDS[11] = ("086114", "sensitivenesses", "noun", "/ˈsɛnsɪtɪvnəsɪz/", "độ nhạy cảm; tính dễ tự ái")
RECORDS[21] = ("086124", "sensualize", "verb", "/ˈsɛnʃuəˌlaɪz/", "nhục dục hóa; gợi dục hóa")
RECORDS[27] = ("086130", "sententiousness", "noun", "/sɛnˈtɛnʃəsnəs/", "thói rao giảng đạo đức khô khan")
RECORDS[28] = ("086131", "sentiency", "noun", "/ˈsɛnʃənsi/", "năng lực tri giác; khả năng cảm nhận"[:35])
RECORDS[28] = ("086131", "sentiency", "noun", "/ˈsɛnʃənsi/", "năng lực tri giác; sự nhạy cảm")
RECORDS[31] = ("086134", "sentimentalised", "verb", "/ˌsɛntɪˈmɛntəˌlaɪzd/", "đã ủy mị hóa; đã làm đa cảm")
RECORDS[56] = ("086159", "sepoy", "noun", "/ˈsiːpɔɪ/", "lính Ấn Độ trong quân đội Anh xưa")
RECORDS[63] = ("086166", "septembrist", "noun", "/sɛpˈtɛmbrɪst/", "kẻ dự vụ thảm sát tháng 9 Pháp")
RECORDS[90] = ("086193", "sequenced", "adj", "/ˈsiːkwənst/", "đã giải trình tự; đã sắp thứ tự")
RECORDS[92] = ("086195", "sequencing", "noun", "/ˈsiːkwənsɪŋ/", "giải trình tự gen; lập trình tự")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r03_raw_p2.json"))
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

json.dump(out, open("scratch/b38_r03_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b38_r03_p2 saved OK")
