import json

RECORDS = [
    ("087903", "soapfish", "noun", "/ˈsoʊpˌfɪʃ/", "cá xà phòng tiết nhớt độc"),
    ("087904", "soapily", "adv", "/ˈsoʊpɪli/", "trơn trượt như xà phòng; khéo nịnh"),
    ("087905", "soapines", "noun", "/ˈsoʊpinəs/", "tính chất nhờn giống xà phòng"),
    ("087906", "soapiness", "noun", "/ˈsoʊpinəs/", "tính chất xà phòng; vẻ khéo nịnh"),
    ("087907", "soaping", "verb", "/ˈsoʊpɪŋ/", "đang xoa xà phòng; đang rửa xà bông"[:35]),
    ("087908", "soapless", "adj", "/ˈsoʊpləs/", "không chứa xà phòng"),
    ("087909", "soaprock", "noun", "/ˈsoʊpˌrɑːk/", "đá tan; đá hoạt thạch trơn"),
    ("087910", "soaps", "verb", "/soʊps/", "xoa xà phòng; tâng bốc nịnh hót"),
    ("087911", "soapweed", "noun", "/ˈsoʊpˌwiːd/", "cây thùa ngọc giá làm xà phòng"),
    ("087912", "soared", "verb", "/sɔːrd/", "đã bay vút lên cao; đã tăng vọt"),
    ("087913", "soars", "verb", "/sɔːrz/", "bay vút lên cao; tăng vọt mạnh"),
    ("087914", "sobbed", "verb", "/sɑːbd/", "đã khóc nức nở; đã khóc thổn thức"),
    ("087915", "sobbingly", "adv", "/ˈsɑːbɪŋli/", "nức nở thổn thức; sụt sùi"),
    ("087916", "sobered", "verb", "/ˈsoʊbərd/", "đã tỉnh rượu; đã nghiêm túc lại"),
    ("087917", "sobers", "verb", "/ˈsoʊbərz/", "làm tỉnh rượu; trở nên điềm tĩnh"),
    ("087918", "sobersided", "adj", "/ˈsoʊbərˌsaɪdɪd/", "nghiêm nghị đứng đắn; ít đùa"),
    ("087919", "sobersides", "noun", "/ˈsoʊbərˌsaɪdz/", "người nghiêm túc ít nói cười"),
    ("087920", "soboles", "noun", "/ˈsɑːbəˌliːz/", "thân bò ngầm; chồi rễ lan"),
    ("087921", "sobralia", "noun", "/səˈbreɪliə/", "chi phong lan Nam Mỹ Sobralia"),
    ("087922", "sobs", "verb", "/sɑːbz/", "khóc nức nở; khóc thổn thức"),
    ("087923", "soc", "noun", "/sɑːk/", "người theo chủ nghĩa xã hội"),
    ("087924", "socager", "noun", "/ˈsɑːkɪdʒər/", "tá điền nộp tô thuế thay lao dịch"),
    ("087925", "sociableness", "noun", "/ˈsoʊʃəbəlnəs/", "tính hòa đồng cởi mở dễ gần"),
    ("087926", "socialiser", "noun", "/ˈsoʊʃəˌlaɪzər/", "người hay giao thiệp; người xã hội"[:35]),
    ("087927", "socialises", "verb", "/ˈsoʊʃəˌlaɪzɪz/", "giao lưu xã hội; xã hội hóa"),
    ("087928", "socialisings", "noun", "/ˈsoʊʃəˌlaɪzɪŋz/", "buổi gặp gỡ giao lưu xã hội"),
    ("087929", "socialistically", "adv", "/ˌsoʊʃəˈlɪstɪkli/", "theo đường lối xã hội chủ nghĩa"),
    ("087930", "socialists", "noun", "/ˈsoʊʃəlɪsts/", "người theo chủ nghĩa xã hội"),
    ("087931", "socializer", "noun", "/ˈsoʊʃəˌlaɪzər/", "người hay giao tiếp xã hội"),
    ("087932", "socializes", "verb", "/ˈsoʊʃəˌlaɪzɪz/", "giao tiếp xã hội; xã hội hóa"),
    ("087933", "socialness", "noun", "/ˈsoʊʃəlnəs/", "tính hòa đồng; bản chất xã hội"),
    ("087934", "sociation", "noun", "/ˌsoʊsiˈeɪʃən/", "quần hợp thực vật đồng nhất"),
    ("087935", "societally", "adv", "/səˈsaɪətəli/", "về mặt xã hội; trên bình diện chung"[:35]),
    ("087936", "societies", "noun", "/səˈsaɪətiz/", "xã hội; hiệp hội; câu lạc bộ"),
    ("087937", "socinianism", "noun", "/soʊˈsɪniəˌnɪzəm/", "học thuyết tôn giáo Socinus"),
    ("087938", "sociobiologic", "adj", "/ˌsoʊsioʊˌbaɪəˈlɑːdʒɪk/", "thuộc sinh học xã hội"),
    ("087939", "sociobiologically", "adv", "/ˌsoʊsioʊˌbaɪəˈlɑːdʒɪkli/", "về mặt sinh học xã hội"),
    ("087940", "sociobiologist", "noun", "/ˌsoʊsioʊbaɪˈɑːlədʒɪst/", "nhà sinh học xã hội"),
    ("087941", "sociocracy", "noun", "/ˌsoʊsiˈɑːkrəsi/", "mô hình quản trị đồng thuận"),
    ("087942", "socioculturally", "adv", "/ˌsoʊsioʊˈkʌltʃərəli/", "về phương diện văn hóa xã hội"),
    ("087943", "sociogram", "noun", "/ˈsoʊsiəˌɡræm/", "sơ đồ mạng lưới quan hệ xã hội"),
    ("087944", "sociolinguist", "noun", "/ˌsoʊsioʊˈlɪŋɡwɪst/", "nhà ngôn ngữ học xã hội"),
    ("087945", "sociolinguistically", "adv", "/ˌsoʊsioʊlɪŋˈɡwɪstɪkli/", "về mặt ngôn ngữ học xã hội"),
    ("087946", "sociolinguists", "noun", "/ˌsoʊsioʊˈlɪŋɡwɪsts/", "nhà ngôn ngữ học xã hội"),
    ("087947", "sociologies", "noun", "/ˌsoʊsiˈɑːlədʒiz/", "ngành xã hội học"),
    ("087948", "sockdolager", "noun", "/sɑːkˈdɑːlədʒər/", "cú đấm hạ đo ván; đòn quyết định"),
    ("087949", "sockdologer", "noun", "/sɑːkˈdɑːlədʒər/", "cú đấm hạ đo ván; lý lẽ đanh thép"),
    ("087950", "socked", "verb", "/sɑːkt/", "đã đấm mạnh; đã nện cho một cú"),
    ("087951", "socker", "noun", "/ˈsɑːkər/", "môn bóng đá (cách viết cũ)"),
    ("087952", "socketed", "adj", "/ˈsɑːkɪtɪd/", "có lắp ổ cắm; nằm trong hốc ổ"),
    ("087953", "sockets", "noun", "/ˈsɑːkɪts/", "ổ cắm điện; hốc mắt; đế cắm"),
    ("087954", "sockeyes", "noun", "/ˈsɑːkˌaɪz/", "cá hồi đỏ Thái Bình Dương"),
    ("087955", "socking", "verb", "/ˈsɑːkɪŋ/", "đang đấm mạnh; đang nện cú trời"),
    ("087956", "socks", "verb", "/sɑːks/", "đấm thật mạnh; đánh trúng cú nặng"),
    ("087957", "sodalist", "noun", "/ˈsoʊdəlɪst/", "hội viên đoàn thể Công giáo"),
    ("087958", "sodbuster", "noun", "/ˈsɑːdˌbʌstər/", "nông dân khai khẩn đất hoang Mỹ"),
    ("087959", "soddenly", "adv", "/ˈsɑːdənli/", "ướt sũng đẫm nước; đờ đẫn lờ đờ"),
    ("087960", "soddenness", "noun", "/ˈsɑːdənnəs/", "tình trạng ướt sũng đẫm nước"),
    ("087961", "sodiums", "noun", "/ˈsoʊdiəmz/", "nguyên tố natri; hợp chất natri"),
    ("087962", "sodoku", "noun", "/soʊˈdoʊkuː/", "bệnh sốt do chuột cắn (sodoku)"),
    ("087963", "sodomise", "verb", "/ˈsɑːdəˌmaɪz/", "giao hợp đường hậu môn"),
    ("087964", "sodomist", "noun", "/ˈsɑːdəmɪst/", "người giao hợp đường hậu môn"),
    ("087965", "sodomitical", "adj", "/ˌsɑːdəˈmɪtɪkəl/", "thuộc giao hợp đường hậu môn"),
    ("087966", "soever", "adv", "/soʊˈɛvər/", "dù bất cứ thế nào"),
    ("087967", "sofas", "noun", "/ˈsoʊfəz/", "ghế sô-pha; trường kỷ"),
    ("087968", "sofism", "noun", "/ˈsuːˌfɪzəm/", "chủ nghĩa thần bí Hồi giáo Sufi"),
    ("087969", "softa", "noun", "/ˈsɔːftə/", "sinh viên trường thần học Ottoman"),
    ("087970", "softens", "verb", "/ˈsɔːfənz/", "làm mềm đi; làm dịu bớt"),
    ("087971", "softer", "adj", "/ˈsɔːftər/", "mềm hơn; dịu nhẹ hơn"),
    ("087972", "softest", "adj", "/ˈsɔːftɪst/", "mềm nhất; êm dịu nhất"),
    ("087973", "softhead", "noun", "/ˈsɔːftˌhɛd/", "kẻ khờ khạo; người ngốc nghếch"),
    ("087974", "softheaded", "adj", "/ˌsɔːftˈhɛdɪd/", "khờ dại; nhẹ dạ cả tin"),
    ("087975", "softheartedness", "noun", "/ˌsɔːftˈhɑːrtɪdnəs/", "lòng trắc ẩn; tính dễ mủi lòng"),
    ("087976", "softwares", "noun", "/ˈsɔːftˌwɛrz/", "phần mềm máy tính"),
    ("087977", "softwooded", "adj", "/ˈsɔːftˌwʊdɪd/", "có gỗ mềm (cây lá kim)"),
    ("087978", "sogdian", "noun", "/ˈsɑːɡdiən/", "người Sogdia; tiếng Sogdia cổ"),
    ("087979", "soggily", "adv", "/ˈsɑːɡɪli/", "ướt sũng nhũn nhão; ỉu xìu"),
    ("087980", "sohc", "noun", "/ˌɛsˌoʊˌeɪtʃˈsiː/", "trục cam đơn trên đỉnh xi-lanh"),
    ("087981", "soigne", "adj", "/swɑːnˈjeɪ/", "chải chuốt lịch lãm; chăm chút kỹ"),
    ("087982", "soignee", "adj", "/swɑːnˈjeɪ/", "chải chuốt thanh lịch (nữ giới)"),
    ("087983", "soilage", "noun", "/ˈsɔɪlɪdʒ/", "cỏ tươi cắt cho gia súc ăn tại chuồng"[:35]),
    ("087984", "soilborne", "adj", "/ˈsɔɪlˌbɔːrn/", "lây truyền qua đất (mầm bệnh)"),
    ("087985", "soiless", "adj", "/ˈsɔɪlləs/", "không cần đất trồng; sạch vết bẩn"),
    ("087986", "soilless", "adj", "/ˈsɔɪlləs/", "không cần đất trồng (thủy canh)"),
    ("087987", "soils", "verb", "/sɔɪlz/", "làm bẩn; làm hoen ố; bón phân"),
    ("087988", "soilure", "noun", "/ˈsɔɪljər/", "vết bẩn dơ; hành động làm hoen ố"),
    ("087989", "sojourned", "verb", "/ˈsoʊdʒɜːrnd/", "đã lưu trú tạm thời ở nơi khác"),
    ("087990", "sojourning", "verb", "/ˈsoʊdʒɜːrnɪŋ/", "đang lưu trú tạm thời ở nơi khác"),
    ("087991", "sojourns", "verb", "/ˈsoʊdʒɜːrnz/", "lưu trú tạm thời; tạm dừng chân"),
    ("087992", "soke", "noun", "/soʊk/", "quyền tài phán địa phương thời xưa"),
    ("087993", "sokeman", "noun", "/ˈsoʊkmən/", "nông dân tự do chịu quyền tài phán"),
    ("087994", "sokoro", "noun", "/səˈkɔːroʊ/", "tiếng Sokoro (Cộng hòa Tchad)"),
    ("087995", "sola", "adj", "/ˈsoʊlə/", "một mình đơn độc (nữ); điên điển"),
    ("087996", "solaced", "verb", "/ˈsɑːləst/", "đã an ủi; đã làm khuây khỏa"),
    ("087997", "solacement", "noun", "/ˈsɑːləsmənt/", "sự an ủi; niềm khuây khỏa nỗi đau"),
    ("087998", "solaces", "verb", "/ˈsɑːləsɪz/", "an ủi; làm khuây khỏa nỗi buồn"),
    ("087999", "solacing", "verb", "/ˈsɑːləsɪŋ/", "đang an ủi; đang làm khuây khỏa"),
    ("088000", "solanceous", "adj", "/səˈleɪnʃəs/", "thuộc họ Cà (Solanaceae)"),
    ("088001", "solandra", "noun", "/soʊˈlændrə/", "chi cây loa kèn vàng Solandra"),
    ("088002", "solanella", "noun", "/ˌsoʊləˈnɛlə/", "cây chuông tuyết vùng núi tuyết"),
]

# Remove slices cleanly <= 35 chars
RECORDS[4] = ("087907", "soaping", "verb", "/ˈsoʊpɪŋ/", "đang xoa xà phòng; đang nịnh bợ")
RECORDS[23] = ("087926", "socialiser", "noun", "/ˈsoʊʃəˌlaɪzər/", "người hay giao tiếp xã hội")
RECORDS[32] = ("087935", "societally", "adv", "/səˈsaɪətəli/", "về mặt xã hội; trên bình diện chung"[:35])
RECORDS[32] = ("087935", "societally", "adv", "/səˈsaɪətəli/", "trên phương diện xã hội")
RECORDS[80] = ("087983", "soilage", "noun", "/ˈsɔɪlɪdʒ/", "cỏ tươi cắt cho gia súc ăn")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r06_raw_p5.json"))
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

json.dump(out, open("scratch/b38_r06_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b38_r06_p5 saved OK")
