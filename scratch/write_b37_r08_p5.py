import json

RECORDS = [
    ("083903", "riveret", "noun", "/ˈrɪvərɪt/", "con sông nhỏ; dòng suối"),
    ("083904", "riverine", "adj", "/ˈrɪvəˌraɪn/", "thuộc sông ngòi; ven sông"),
    ("083905", "riverman", "noun", "/ˈrɪvərmən/", "người làm nghề trên sông"),
    ("083906", "rivery", "adj", "/ˈrɪvəri/", "có nhiều sông; như dòng sông"),
    ("083907", "rives", "verb", "/raɪvz/", "xé toạc; chẻ vỡ"),
    ("083908", "riveted", "verb", "/ˈrɪvɪtɪd/", "đã tán đinh; đã bị cuốn hút"),
    ("083909", "rivets", "verb", "/ˈrɪvɪts/", "tán đinh; thu hút chặt"),
    ("083910", "rivetter", "noun", "/ˈrɪvɪtər/", "thợ tán đinh; máy tán đinh"),
    ("083911", "rivina", "noun", "/rɪˈvaɪnə/", "chi cây mồng tơi leo Rivina"),
    ("083912", "riving", "verb", "/ˈraɪvɪŋ/", "đang xé toạc; đang chẻ ra"),
    ("083913", "rivose", "adj", "/ˈraɪvoʊs/", "có rãnh ngoằn ngoèo"),
    ("083914", "rivulus", "noun", "/ˈrɪvjələs/", "chi cá killi Rivulus"),
    ("083915", "rizz", "noun", "/rɪz/", "sức hút quyến rũ; duyên tán tỉnh"),
    ("083916", "rly", "noun", "/ˈreɪlˌweɪ/", "đường sắt (viết tắt)"),
    ("083917", "rm", "noun", "/ˌɑːrˈɛm/", "Thủy quân lục chiến Hoàng gia Anh"),
    ("083918", "roadability", "noun", "/ˌroʊdəˈbɪlɪti/", "khả năng bám đường của xe"),
    ("083919", "roadbook", "noun", "/ˈroʊdˌbʊk/", "sổ chỉ dẫn lộ trình đua xe"),
    ("083920", "roadie", "noun", "/ˈroʊdi/", "nhân viên kỹ thuật đi lưu diễn"),
    ("083921", "roadleveller", "noun", "/ˈroʊdˌlɛvələr/", "xe san lấp mặt đường"),
    ("083922", "roadmap", "noun", "/ˈroʊdˌmæp/", "lộ trình kế hoạch; bản đồ đường"),
    ("083923", "roadworthy", "adj", "/ˈroʊdˌwɜːrði/", "đủ tiêu chuẩn an toàn lưu thông"),
    ("083924", "roak", "noun", "/roʊk/", "sương mù nhẹ; khói bốc"),
    ("083925", "roamed", "verb", "/roʊmd/", "đã đi lang thang; đã rong ruổi"),
    ("083926", "roaming", "verb", "/ˈroʊmɪŋ/", "đang lang thang; chuyển vùng"),
    ("083927", "roams", "verb", "/roʊmz/", "đi lang thang; rong ruổi"),
    ("083928", "roared", "verb", "/rɔːrd/", "đã gầm vang; đã rống lên"),
    ("083929", "roars", "verb", "/rɔːrz/", "gầm vang; rống lên"),
    ("083930", "roasts", "verb", "/roʊsts/", "nướng; rang; châm biếm"),
    ("083931", "robbed", "verb", "/rɑːbd/", "đã cướp; đã tước đoạt"),
    ("083932", "robbers", "noun", "/ˈrɑːbərz/", "tên cướp; kẻ trộm"),
    ("083933", "robbing", "verb", "/ˈrɑːbɪŋ/", "đang cướp; đang tước đoạt"),
    ("083934", "robes", "verb", "/roʊbz/", "mặc áo choàng; khoác lên"),
    ("083935", "robing", "verb", "/ˈroʊbɪŋ/", "đang mặc áo choàng"),
    ("083936", "roborant", "adj", "/ˈrɑːbərənt/", "bồi bổ; tăng cường sinh lực"),
    ("083937", "robotaxi", "noun", "/ˈroʊboʊˌtæksi/", "taxi tự lái"),
    ("083938", "robotize", "verb", "/ˈroʊbəˌtaɪz/", "tự động hóa bằng rô-bốt"),
    ("083939", "robotized", "verb", "/ˈroʊbəˌtaɪzd/", "đã tự động hóa bằng rô-bốt"),
    ("083940", "robotizes", "verb", "/ˈroʊbəˌtaɪzɪz/", "tự động hóa bằng rô-bốt"),
    ("083941", "robotizing", "verb", "/ˈroʊbəˌtaɪzɪŋ/", "đang tự động hóa bằng rô-bốt"),
    ("083942", "robotlike", "adj", "/ˈroʊbɑːtˌlaɪk/", "máy móc như rô-bốt; vô cảm"),
    ("083943", "robs", "verb", "/rɑːbz/", "cướp; tước đoạt"),
    ("083944", "roburite", "noun", "/ˈrɑːbjəˌraɪt/", "thuốc nổ an toàn roburit"),
    ("083945", "robustious", "adj", "/rəˈbʌstʃəs/", "ầm ĩ; ngang ngạnh; vạm vỡ"),
    ("083946", "robustnesses", "noun", "/roʊˈbʌstnəsɪz/", "tính vững chắc; sự khỏe mạnh"),
    ("083947", "rocaille", "noun", "/rəˈkaɪ/", "hoa văn trang trí vỏ sò đá"),
    ("083948", "rocambole", "noun", "/ˈrɑːkəmˌboʊl/", "hành tăm châu Âu; tỏi tây dại"),
    ("083949", "roccella", "noun", "/rɑːˈsɛlə/", "chi địa y nhuộm Roccella"),
    ("083950", "roccellaceae", "noun", "/ˌrɑːsəˈleɪsiːˌiː/", "họ địa y Roccellaceae"),
    ("083951", "roccus", "noun", "/ˈrɑːkəs/", "chi cá vược Roccus"),
    ("083952", "rocephin", "noun", "/rəˈsɛfɪn/", "thuốc kháng sinh Rocephin"),
    ("083953", "rochet", "noun", "/ˈrɑːtʃɪt/", "áo lễ trắng của giám mục"),
    ("083954", "rockability", "noun", "/ˌrɑːkəˈbɪlɪti/", "nhạc rockabilly; độ lắc lư"),
    ("083955", "rockchuck", "noun", "/ˈrɑːkˌtʃʌk/", "sóc macmot bụng vàng vùng đá"),
    ("083956", "rockclimbing", "noun", "/ˈrɑːkˌklaɪmɪŋ/", "môn leo vách đá"),
    ("083957", "rockcress", "noun", "/ˈrɑːkˌkrɛs/", "cây cải đá"),
    ("083958", "rocked", "verb", "/rɑːkt/", "đã đung đưa; đã làm rung chuyển"),
    ("083959", "rocketeer", "noun", "/ˌrɑːkəˈtɪr/", "kỹ sư tên lửa; người phóng tên lửa"),
    ("083960", "rocketeers", "noun", "/ˌrɑːkəˈtɪrz/", "kỹ sư tên lửa"),
    ("083961", "rocketer", "noun", "/ˈrɑːkɪtər/", "chim trĩ bay vọt thẳng lên"),
    ("083962", "rockfoil", "noun", "/ˈrɑːkˌfɔɪl/", "cây tai hổ mọc trên đá"),
    ("083963", "rockhead", "noun", "/ˈrɑːkˌhɛd/", "tầng đá gốc cứng phía trên"),
    ("083964", "rockhole", "noun", "/ˈrɑːkˌhoʊl/", "hốc đá tự nhiên chứa nước"),
    ("083965", "rockily", "adv", "/ˈrɑːkɪli/", "chao đảo; không vững chắc"),
    ("083966", "rockiness", "noun", "/ˈrɑːkinəs/", "tình trạng nhiều đá; sự chao đảo"),
    ("083967", "rocking", "verb", "/ˈrɑːkɪŋ/", "đang đung đưa; đang rung chuyển"),
    ("083968", "rocks", "verb", "/rɑːks/", "đung đưa; làm rung chuyển"),
    ("083969", "rockweed", "noun", "/ˈrɑːkˌwiːd/", "rong nâu mọc bám đá biển"),
    ("083970", "rocroi", "noun", "/roʊˈkrwɑː/", "trận chiến Rocroi"),
    ("083971", "roddin", "noun", "/ˈrɑːdɪn/", "lối mòn hẹp (phương ngữ Scotland)"),
    ("083972", "rodenticide", "noun", "/roʊˈdɛntəˌsaɪd/", "thuốc diệt loài gặm nhấm"),
    ("083973", "rodhos", "noun", "/ˈroʊdoʊs/", "đảo Rhodes (Hy Lạp)"),
    ("083974", "rodlike", "adj", "/ˈrɑːdˌlaɪk/", "hình que; dạng thanh"),
    ("083975", "rodman", "noun", "/ˈrɑːdmən/", "người cầm mia đo đạc; người câu cá"),
    ("083976", "rodolia", "noun", "/roʊˈdoʊliə/", "chi bọ rùa Rodolia"),
    ("083977", "rodomontade", "noun", "/ˌrɑːdəmɑːnˈteɪd/", "lời khoác lác huênh hoang"),
    ("083978", "rodster", "noun", "/ˈrɑːdstər/", "người câu cá bằng cần"),
    ("083979", "roebucks", "noun", "/ˈroʊˌbʌks/", "hoẵng đực châu Âu"),
    ("083980", "roentgenium", "noun", "/ˌrɛntˈɡɛniəm/", "nguyên tố hóa học roentgeni"),
    ("083981", "roentgenization", "noun", "/ˌrɛntɡənəˈzeɪʃən/", "sự chiếu tia X"),
    ("083982", "roentgenogram", "noun", "/ˈrɛntɡənəˌɡræm/", "phim chụp X-quang"),
    ("083983", "roentgenograph", "noun", "/ˈrɛntɡənəˌɡræf/", "ảnh chụp tia X"),
    ("083984", "roentgenographic", "adj", "/ˌrɛntɡənəˈɡræfɪk/", "thuộc chụp X-quang"),
    ("083985", "roentgenography", "noun", "/ˌrɛntɡəˈnɑːɡrəfi/", "kỹ thuật chụp X-quang"),
    ("083986", "roentgenologist", "noun", "/ˌrɛntɡəˈnɑːlədʒɪst/", "bác sĩ chẩn đoán X-quang"),
    ("083987", "roentgenologists", "noun", "/ˌrɛntɡəˈnɑːlədʒɪsts/", "bác sĩ chẩn đoán X-quang"),
    ("083988", "roentgenology", "noun", "/ˌrɛntɡəˈnɑːlədʒi/", "khoa học tia X; X-quang học"),
    ("083989", "roentgenometer", "noun", "/ˌrɛntɡəˈnɑːmɪtər/", "liều lượng kế tia X"),
    ("083990", "roentgenoscope", "noun", "/rɛntˈɡɛnəˌskoʊp/", "máy chiếu X-quang huỳnh quang"),
    ("083991", "roentgenoscopic", "adj", "/ˌrɛntɡənəˈskɑːpɪk/", "thuộc soi X-quang"),
    ("083992", "roentgenoscopy", "noun", "/ˌrɛntɡəˈnɑːskəpi/", "phép soi chiếu tia X"),
    ("083993", "roentgenotherapy", "noun", "/ˌrɛntɡənoʊˈθɛrəpi/", "liệu pháp xạ trị tia X"),
    ("083994", "rofecoxib", "noun", "/ˌroʊfəˈkɑːksɪb/", "thuốc kháng viêm rofecoxib"),
    ("083995", "rogations", "noun", "/roʊˈɡeɪʃənz/", "kinh cầu nguyện khẩn xin mùa màng"),
    ("083996", "rogatory", "adj", "/ˈrɑːɡəˌtɔːri/", "yêu cầu ủy thác thẩm tra"),
    ("083997", "roger", "intj", "/ˈrɑːdʒər/", "đã rõ (tín hiệu vô tuyến)"),
    ("083998", "rogered", "verb", "/ˈrɑːdʒərd/", "đã xác nhận đã rõ (vô tuyến)"),
    ("083999", "rogering", "verb", "/ˈrɑːdʒərɪŋ/", "đang xác nhận đã rõ (vô tuyến)"),
    ("084000", "rogorist", "noun", "/ˈrɪɡərɪst/", "người theo chủ nghĩa khắc khổ"),
    ("084001", "roguishness", "noun", "/ˈroʊɡɪʃnəs/", "tính tinh nghịch; vẻ láu cá"),
    ("084002", "rohan", "noun", "/ˈroʊhɑːn/", "cây gỗ đỏ Ấn Độ rohan"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r08_raw_p5.json"))
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

json.dump(out, open("scratch/b37_r08_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b37_r08_p5 saved OK")
