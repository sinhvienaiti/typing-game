import json

rows = [
    ("075803", "peskily", "adv", "/ˈpɛskɪli/", "một cách phiền toái, quấy rầy"),
    ("075804", "peskiness", "noun", "/ˈpɛskinəs/", "tính hay quấy rầy, phiền toái"),
    ("075805", "pessimal", "adj", "/ˈpɛsɪməl/", "bất lợi nhất, tồi tệ nhất"),
    ("075806", "pessimum", "adj", "/ˈpɛsɪməm/", "điều kiện bất lợi nhất (sinh thái)"),
    ("075807", "pesterer", "noun", "/ˈpɛstərər/", "người quấy rầy; kẻ làm phiền"),
    ("075808", "pesthole", "noun", "/ˈpɛstˌhoʊl/", "ổ dịch bệnh; nơi ô uế chứa bệnh"),
    ("075809", "pesthouse", "noun", "/ˈpɛstˌhaʊs/", "viện cách ly bệnh truyền nhiễm"),
    ("075810", "pesticidal", "adj", "/ˌpɛstɪˈsaɪdəl/", "có tác dụng trừ sâu, diệt cỏ hại"),
    ("075811", "pestiferously", "adv", "/pɛˈstɪfərəsli/", "độc hại; gây khó chịu phiền toái"),
    ("075812", "pestiferousness", "noun", "/pɛˈstɪfərəsnəs/", "tính chất độc hại, gây dịch bệnh"),
    ("075813", "pestilentially", "adv", "/ˌpɛstɪˈlɛnʃəli/", "mang mầm dịch bệnh; tai hại"),
    ("075814", "pestled", "verb", "/ˈpɛsəld/", "đã giã nhuyễn bằng chày cối"),
    ("075815", "pestles", "verb", "/ˈpɛsəlz/", "giã nhuyễn bằng chày cối"),
    ("075816", "pestling", "verb", "/ˈpɛsəlɪŋ/", "giã nhuyễn bằng chày cối"),
    ("075817", "pestology", "noun", "/pɛˈstɒlədʒi/", "khoa học nghiên cứu sinh vật hại"),
    ("075818", "petabit", "noun", "/ˈpɛtəbɪt/", "đơn vị dữ liệu petabit (Pb)"),
    ("075819", "petaliferous", "adj", "/ˌpɛtəˈlɪfərəs/", "có mang cánh hoa (thực vật)"),
    ("075820", "petaliform", "adj", "/pɪˈtælɪfɔːrm/", "có hình dạng cánh hoa (thực vật)"),
    ("075821", "petalike", "adj", "/ˈpɛtəlˌlaɪk/", "giống như cánh hoa"),
    ("075822", "petalles", "adj", "/ˈpɛtəlləs/", "không có cánh hoa (biến thể cũ)"),
    ("075823", "petalless", "adj", "/ˈpɛtəlləs/", "không có cánh hoa (thực vật)"),
    ("075824", "petallike", "adj", "/ˈpɛtəlˌlaɪk/", "giống như cánh hoa"),
    ("075825", "petalody", "noun", "/ˈpɛtələdi/", "sự biến bộ phận hoa thành cánh"),
    ("075826", "petalous", "adj", "/ˈpɛtələs/", "có cánh hoa (thực vật)"),
    ("075827", "petary", "noun", "/ˈpiːtəri/", "bãi khai thác than bùn"),
    ("075828", "petases", "noun", "/ˈpɛtˌeɪsɪz/", "enzym phân hủy nhựa PETase"),
    ("075829", "petasi", "noun", "/ˈpɛtəsaɪ/", "mũ rộng vành có cánh (Hy Lạp cổ)"),
    ("075830", "petasites", "noun", "/ˌpɛtəˈsaɪtiːz/", "chi cây chân voi (Petasites)"),
    ("075831", "petasus", "noun", "/ˈpɛtəsəs/", "mũ rộng vành có cánh (Hy Lạp cổ)"),
    ("075832", "petaurist", "noun", "/ˈpɛtɔːrɪst/", "sóc bay lớn; thú túi bay Petaurus"),
    ("075833", "petaurista", "noun", "/ˌpɛtɔːˈrɪstə/", "chi sóc bay khổng lồ châu Á"),
    ("075834", "petauristidae", "noun", "/ˌpɛtɔːˈrɪstɪdiː/", "họ Thú túi bay Petauridae"),
    ("075835", "petaurus", "noun", "/pɪˈtɔːrəs/", "chi thú túi bay Úc (Petaurus)"),
    ("075836", "petchary", "noun", "/ˈpɛtʃəri/", "chim đớp ruồi kingbird (Tây Ấn)"),
    ("075837", "petechiae", "noun", "/pəˈtiːkiːiː/", "chấm xuất huyết dưới da (y học)"),
    ("075838", "petechial", "adj", "/pəˈtiːkiəl/", "thuộc đốm xuất huyết dưới da"),
    ("075839", "petered", "verb", "/ˈpiːtərd/", "đã cạn dần, yếu dần, tắt dần"),
    ("075840", "petering", "verb", "/ˈpiːtərɪŋ/", "cạn dần, yếu dần, tắt dần"),
    ("075841", "peters", "verb", "/ˈpiːtərz/", "cạn dần, yếu dần, tắt dần"),
    ("075842", "petersham", "noun", "/ˈpiːtərʃəm/", "vải dạ dày; dây lưng váy petersham"),
    ("075843", "petiolate", "adj", "/ˈpɛtioʊlɪt/", "có cuống lá (thực vật học)"),
    ("075844", "petiolated", "adj", "/ˈpɛtioʊleɪtɪd/", "có cuống lá (thực vật học)"),
    ("075845", "petioled", "adj", "/ˈpɛtioʊld/", "có cuống lá (thực vật học)"),
    ("075846", "petiolule", "noun", "/ˈpɛtioʊljuːl/", "cuống lá chét (thực vật học)"),
    ("075847", "petiteness", "noun", "/pəˈtiːtnəs/", "vẻ nhỏ nhắn, xinh xắn; sự nhỏ bé"),
    ("075848", "petitionary", "adj", "/pəˈtɪʃənəri/", "mang tính thỉnh cầu, kiến nghị"),
    ("075849", "petitioned", "verb", "/pəˈtɪʃənd/", "đã thỉnh cầu, gửi đơn kiến nghị"),
    ("075850", "petitioning", "verb", "/pəˈtɪʃənɪŋ/", "thỉnh cầu, gửi đơn kiến nghị"),
    ("075851", "petitions", "verb", "/pəˈtɪʃənz/", "thỉnh cầu, gửi đơn kiến nghị"),
    ("075852", "petong", "noun", "/pəˈtɒŋ/", "hợp kim đồng trắng (paktong)"),
    ("075853", "petplay", "noun", "/ˈpɛtpleɪ/", "trò đóng vai thú cưng (nhập vai)"),
    ("075854", "petrescence", "noun", "/pɪˈtrɛsəns/", "quá trình hóa đá, hóa thạch"),
    ("075855", "petrescent", "adj", "/pɪˈtrɛsənt/", "đang hóa đá, chuyển thành đá"),
    ("075856", "petrine", "adj", "/ˈpiːtraɪn/", "thuộc Thánh Phê-rô (Tông đồ Peter)"),
    ("075857", "petrissage", "noun", "/ˌpɛtrɪˈsɑːʒ/", "kỹ thuật xoa bóp nhào cơ (massage)"),
    ("075858", "petrochemicals", "noun", "/ˌpɛtroʊˈkɛmɪkəlz/", "hóa chất dầu mỏ (sản phẩm hóa dầu)"),
    ("075859", "petrochemistry", "noun", "/ˌpɛtroʊˈkɛmɪstri/", "ngành hóa dầu; hóa học dầu mỏ"),
    ("075860", "petrocoptis", "noun", "/ˌpɛtrəˈkɒptɪs/", "chi hoa đá Petrocoptis (châu Âu)"),
    ("075861", "petrodollar", "noun", "/ˈpɛtroʊˌdɑːlər/", "đô la dầu mỏ (doanh thu dầu thô)"),
    ("075862", "petrofabric", "adj", "/ˌpɛtroʊˈfæbrɪk/", "kiến trúc thạch học đá biến chất"),
    ("075863", "petrofabrics", "noun", "/ˌpɛtroʊˈfæbrɪks/", "ngành thạch học kiến trúc"),
    ("075864", "petrogale", "noun", "/pɪˈtrɒɡəli/", "chi chuột túi núi đá (Petrogale)"),
    ("075865", "petrogenesis", "noun", "/ˌpɛtroʊˈdʒɛnɪsɪs/", "quá trình hình thành đá (địa chất)"),
    ("075866", "petrogenetic", "adj", "/ˌpɛtroʊdʒəˈnɛtɪk/", "thuộc sự hình thành đá (địa chất)"),
    ("075867", "petroglyphic", "adj", "/ˌpɛtrəˈɡlɪfɪk/", "thuộc hình chạm khắc trên đá cổ"),
    ("075868", "petrograph", "noun", "/ˈpɛtrəɡræf/", "hình vẽ hoặc chữ khắc trên đá"),
    ("075869", "petrographer", "noun", "/pɪˈtrɒɡrəfər/", "nhà thạch học mô tả đá"),
    ("075870", "petrographic", "adj", "/ˌpɛtrəˈɡræfɪk/", "thuộc thạch học mô tả đá"),
    ("075871", "petrographical", "adj", "/ˌpɛtrəˈɡræfɪkəl/", "thuộc thạch học mô tả đá"),
    ("075872", "petrographically", "adv", "/ˌpɛtrəˈɡræfɪkli/", "về mặt thạch học mô tả"),
    ("075873", "petrography", "noun", "/pɪˈtrɒɡrəfi/", "thạch học mô tả (phân loại đá)"),
    ("075874", "petroil", "noun", "/ˈpɛtrɔɪl/", "nhiên liệu xăng pha nhớt (2 kỳ)"),
    ("075875", "petroleur", "noun", "/ˌpɛtrəˈlɜːr/", "kẻ phóng hỏa bằng dầu lửa (cổ)"),
    ("075876", "petrolic", "adj", "/pɪˈtrɒlɪk/", "thuộc dầu mỏ, xăng dầu"),
    ("075877", "petroliferous", "adj", "/ˌpɛtrəˈlɪfərəs/", "chứa dầu mỏ, giàu dầu khí"),
    ("075878", "petrolith", "noun", "/ˈpɛtrəlɪθ/", "đá thấm dầu; tầng đá dầu"),
    ("075879", "petrologic", "adj", "/ˌpɛtrəˈlɒdʒɪk/", "thuộc thạch học (nguồn gốc đá)"),
    ("075880", "petrological", "adj", "/ˌpɛtrəˈlɒdʒɪkəl/", "thuộc thạch học (nguồn gốc đá)"),
    ("075881", "petrologically", "adv", "/ˌpɛtrəˈlɒdʒɪkli/", "theo quan điểm thạch học"),
    ("075882", "petrologist", "noun", "/pɪˈtrɒlədʒɪst/", "nhà thạch học (nghiên cứu đá)"),
    ("075883", "petromyzon", "noun", "/ˌpɛtroʊˈmaɪzɒn/", "chi cá mút đá biển (Petromyzon)"),
    ("075884", "petromyzoniformes", "noun", "/ˌpɛtroʊmaɪˌzɒnɪˈfɔːrmiːz/", "bộ Cá mút đá"),
    ("075885", "petromyzontidae", "noun", "/ˌpɛtroʊmaɪˈzɒntɪdiː/", "họ Cá mút đá (Petromyzontidae)"),
    ("075886", "petrophilous", "adj", "/pɪˈtrɒfɪləs/", "ưa sống trên đá (sinh vật)"),
    ("075887", "petrophyte", "noun", "/ˈpɛtrəfaɪt/", "thực vật mọc bám trên đá"),
    ("075888", "petrosal", "adj", "/pɪˈtroʊsəl/", "thuộc xương đá (xương thái dương)"),
    ("075889", "petroselinum", "noun", "/ˌpɛtrəˈsiːlɪnəm/", "chi rau mùi tây (Petroselinum)"),
    ("075890", "pets", "verb", "/pɛts/", "vuốt ve, âu yếm, cưng nựng"),
    ("075891", "petted", "verb", "/ˈpɛtɪd/", "đã vuốt ve, âu yếm, cưng nựng"),
    ("075892", "petteria", "noun", "/pəˈtɪriə/", "chi đậu vàng Dalmatia (Petteria)"),
    ("075893", "petticoated", "adj", "/ˈpɛtɪˌkoʊtɪd/", "mặc váy lót; nữ tính yếu ớt"),
    ("075894", "pettifogged", "verb", "/ˈpɛtɪfɒɡd/", "đã bới móc cãi vặt (luật sư tồi)"),
    ("075895", "pettifogger", "noun", "/ˈpɛtɪˌfɒɡər/", "luật sư cãi vặt kiếm ăn; kẻ bới móc"),
    ("075896", "pettifoggers", "noun", "/ˈpɛtɪˌfɒɡərz/", "luật sư cãi vặt; kẻ bới móc"),
    ("075897", "pettifoggery", "noun", "/ˈpɛtɪˌfɒɡəri/", "trò cãi cùn bới móc vặt vãnh"),
    ("075898", "pettifogging", "verb", "/ˈpɛtɪˌfɒɡɪŋ/", "bới móc cãi vặt; hành nghề lặt vặt"),
    ("075899", "pettifogs", "verb", "/ˈpɛtɪfɒɡz/", "bới móc cãi vặt; hành nghề lặt vặt"),
    ("075900", "pettily", "adv", "/ˈpɛtɪli/", "một cách nhỏ mọn, ích kỷ, vụn vặt"),
    ("075901", "pettioes", "noun", "/ˈpɛtɪtoʊz/", "chân giò lợn (nấu ăn, từ cổ)"),
    ("075902", "pettish", "adj", "/ˈpɛtɪʃ/", "cáu kỉnh, hay dỗi, dễ bực mình"),
]

with open("scratch/b36_r02_raw_p4.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

assert len(raw) == len(rows) == 100
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, rows):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} vs {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} vs {hw}"
    assert len(vi) <= 35, f"vi too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.count("/") == 2 and not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"bad ipa: {hw} -> {ipa}"
    r["pos"] = pos
    r["ipa"] = ipa
    r["vi"] = vi
    r["status"] = "reviewed"
    out.append(r)

with open("scratch/b36_r02_p4.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r02_p4 saved OK")
