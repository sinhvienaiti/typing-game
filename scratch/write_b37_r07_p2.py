import json

RECORDS = [
    ("083103", "resided", "verb", "/rɪˈzaɪdɪd/", "đã cư trú; đã sinh sống"),
    ("083104", "residentiary", "adj", "/ˌrɛzɪˈdɛnʃəri/", "có nơi ở chính thức; thường trú"),
    ("083105", "resider", "noun", "/rɪˈzaɪdər/", "người cư trú; cư dân"),
    ("083106", "resides", "verb", "/rɪˈzaɪdz/", "cư trú; sinh sống"),
    ("083107", "residing", "verb", "/rɪˈzaɪdɪŋ/", "đang cư trú; đang sinh sống"),
    ("083108", "residua", "noun", "/rɪˈzɪdʒuə/", "phần dư; cặn bã"),
    ("083109", "residuate", "verb", "/rɪˈzɪdʒuˌeɪt/", "xác định phần dư"),
    ("083110", "residuation", "noun", "/rɪˌzɪdʒuˈeɪʃən/", "sự xác định phần dư"),
    ("083111", "resift", "verb", "/ˌriːˈsɪft/", "rây lại; sàng lại"),
    ("083112", "resignations", "noun", "/ˌrɛzɪɡˈneɪʃənz/", "đơn từ chức; sự cam chịu"),
    ("083113", "resigned", "verb", "/rɪˈzaɪnd/", "đã từ chức; đã cam chịu"),
    ("083114", "resignee", "noun", "/ˌrɛzɪɡˈniː/", "người được nhượng quyền"),
    ("083115", "resigning", "verb", "/rɪˈzaɪnɪŋ/", "đang từ chức"),
    ("083116", "resigns", "verb", "/rɪˈzaɪnz/", "từ chức"),
    ("083117", "resilifer", "noun", "/rɪˈsɪlɪfər/", "mấu bản lề sừng (nhuyễn thể)"),
    ("083118", "resilium", "noun", "/rɪˈsɪliəm/", "dây chằng bản lề vỏ hai mảnh"),
    ("083119", "resilver", "verb", "/ˌriːˈsɪlvər/", "tráng bạc lại"),
    ("083120", "resinaceous", "adj", "/ˌrɛzɪˈneɪʃəs/", "có nhựa; giống nhựa cây"),
    ("083121", "resinated", "adj", "/ˈrɛzɪˌneɪtɪd/", "tẩm nhựa; có vị nhựa"),
    ("083122", "resiniferous", "adj", "/ˌrɛzɪˈnɪfərəs/", "tiết ra nhựa; sinh nhựa"),
    ("083123", "resinification", "noun", "/rɪˌzɪnɪfɪˈkeɪʃən/", "sự hóa nhựa; sự tạo nhựa"),
    ("083124", "resinify", "verb", "/rɪˈzɪnɪˌfaɪ/", "làm thành nhựa; hóa nhựa"),
    ("083125", "resinlike", "adj", "/ˈrɛzɪnˌlaɪk/", "giống nhựa cây"),
    ("083126", "resinoid", "noun", "/ˈrɛzɪˌnɔɪd/", "chất dạng nhựa; nhựa tổng hợp"),
    ("083127", "resiny", "adj", "/ˈrɛzɪni/", "có nhựa; dính như nhựa"),
    ("083128", "resipiscence", "noun", "/ˌrɛsɪˈpɪsəns/", "sự hồi tâm; sự hối cải"),
    ("083129", "resistances", "noun", "/rɪˈzɪstənsɪz/", "sự kháng cự; điện trở"),
    ("083130", "resisted", "verb", "/rɪˈzɪstɪd/", "đã chống cự; đã kháng cự"),
    ("083131", "resistibility", "noun", "/rɪˌzɪstəˈbɪlɪti/", "tính có thể chống lại"),
    ("083132", "resisting", "verb", "/rɪˈzɪstɪŋ/", "đang chống cự; đang kháng cự"),
    ("083133", "resistless", "adj", "/rɪˈzɪstləs/", "không thể cưỡng lại"),
    ("083134", "resistors", "noun", "/rɪˈzɪstərz/", "điện trở"),
    ("083135", "resists", "verb", "/rɪˈzɪsts/", "chống cự; kháng cự"),
    ("083136", "resituates", "verb", "/ˌriːˈsɪtʃuˌeɪts/", "đặt lại vị trí"),
    ("083137", "resmudge", "verb", "/ˌriːˈsmʌdʒ/", "làm nhòe lại; làm bẩn lại"),
    ("083138", "resold", "verb", "/ˌriːˈsoʊld/", "đã bán lại"),
    ("083139", "resoled", "verb", "/ˌriːˈsoʊld/", "đã thay đế giày"),
    ("083140", "resoles", "verb", "/ˌriːˈsoʊlz/", "thay đế giày"),
    ("083141", "resolidification", "noun", "/ˌriːsəˌlɪdɪfɪˈkeɪʃən/", "sự hóa rắn trở lại"),
    ("083142", "resoling", "verb", "/ˌriːˈsoʊlɪŋ/", "đang thay đế giày"),
    ("083143", "resolubility", "noun", "/rɪˌzɑːljəˈbɪlɪti/", "tính phân giải được"),
    ("083144", "resoluble", "adj", "/rɪˈzɑːljəbəl/", "có thể phân giải; giải quyết được"),
    ("083145", "resolutions", "noun", "/ˌrɛzəˈluːʃənz/", "nghị quyết; độ phân giải"),
    ("083146", "resolutive", "adj", "/rɪˈzɑːljətɪv/", "để phân giải; giúp tan"),
    ("083147", "resolvability", "noun", "/rɪˌzɑːlvəˈbɪlɪti/", "tính giải quyết được; độ phân giải"),
    ("083148", "resolver", "noun", "/rɪˈzɑːlvər/", "người giải quyết; bộ phân giải"),
    ("083149", "resolves", "verb", "/rɪˈzɑːlvz/", "giải quyết; quyết tâm"),
    ("083150", "resonantly", "adv", "/ˈrɛzənəntli/", "vang dội; vang vọng"),
    ("083151", "resonated", "verb", "/ˈrɛzəˌneɪtɪd/", "đã cộng hưởng; đã vang vọng"),
    ("083152", "resonates", "verb", "/ˈrɛzəˌneɪts/", "cộng hưởng; vang vọng"),
    ("083153", "resonators", "noun", "/ˈrɛzəˌneɪtərz/", "bộ cộng hưởng"),
    ("083154", "resorcinolphthalein", "noun", "/rɪˌzɔːrsɪnɒlˈθæliˌɪn/", "hợp chất huỳnh quang"),
    ("083155", "resorted", "verb", "/rɪˈzɔːrtɪd/", "đã phải dùng đến; thường lui tới"),
    ("083156", "resorting", "verb", "/rɪˈzɔːrtɪŋ/", "đang dùng đến; đang lui tới"),
    ("083157", "resorts", "verb", "/rɪˈzɔːrts/", "dùng đến; lui tới"),
    ("083158", "resourceless", "adj", "/rɪˈsɔːrsləs/", "thiếu tài nguyên; bất lực"),
    ("083159", "resourcelessness", "noun", "/rɪˈsɔːrsləsnəs/", "tình trạng thiếu phương kế"),
    ("083160", "resovable", "adj", "/rɪˈzɑːlvəbəl/", "có thể giải quyết"),
    ("083161", "respecful", "adj", "/rɪˈspɛktfəl/", "tỏ vẻ tôn trọng; lễ phép"),
    ("083162", "respecfully", "adv", "/rɪˈspɛktfəli/", "với vẻ tôn trọng; lễ phép"),
    ("083163", "respecting", "verb", "/rɪˈspɛktɪŋ/", "đang tôn trọng"),
    ("083164", "respectlessness", "noun", "/rɪˈspɛktləsnəs/", "sự thiếu tôn trọng"),
    ("083165", "respectworthy", "adj", "/rɪˈspɛktˌwɜːrði/", "đáng kính trọng"),
    ("083166", "respell", "verb", "/ˌriːˈspɛl/", "đánh vần lại"),
    ("083167", "respelled", "verb", "/ˌriːˈspɛld/", "đã đánh vần lại"),
    ("083168", "respelling", "verb", "/ˌriːˈspɛlɪŋ/", "đang đánh vần lại"),
    ("083169", "respells", "verb", "/ˌriːˈspɛlz/", "đánh vần lại"),
    ("083170", "respelt", "verb", "/ˌriːˈspɛlt/", "đã đánh vần lại"),
    ("083171", "respirability", "noun", "/rɪˌspaɪrəˈbɪlɪti/", "tính thở được; khả năng hô hấp"),
    ("083172", "respirable", "adj", "/ˈrɛspərəbəl/", "có thể thở được; hít thở được"),
    ("083173", "respiratorium", "noun", "/ˌrɛspɪrəˈtɔːriəm/", "cơ quan hô hấp; mang (cá)"),
    ("083174", "respirators", "noun", "/ˈrɛspəˌreɪtərz/", "mặt nạ phòng độc; máy thở"),
    ("083175", "respirometer", "noun", "/ˌrɛspəˈrɑːmɪtər/", "hô hấp kế"),
    ("083176", "resplend", "verb", "/rɪˈsplɛnd/", "tỏa sáng rực rỡ"),
    ("083177", "resplendency", "noun", "/rɪˈsplɛndənsi/", "sự rực rỡ; vẻ lộng lẫy"),
    ("083178", "responded", "verb", "/rɪˈspɑːndɪd/", "đã phản hồi; đã đáp lại"),
    ("083179", "responding", "verb", "/rɪˈspɑːndɪŋ/", "đang phản hồi; đang đáp lại"),
    ("083180", "responds", "verb", "/rɪˈspɑːndz/", "phản hồi; đáp lại"),
    ("083181", "responsibilities", "noun", "/rɪˌspɑːnsəˈbɪlɪtiz/", "trách nhiệm; bổn phận"),
    ("083182", "responsibleness", "noun", "/rɪˈspɑːnsəbəlnəs/", "tính có trách nhiệm"),
    ("083183", "responsions", "noun", "/rɪˈspɑːnʃənz/", "kỳ thi đầu vào Oxford xưa"),
    ("083184", "responsively", "adv", "/rɪˈspɑːnsɪvli/", "nhiệt tình đáp ứng; nhạy bén"),
    ("083185", "responsor", "noun", "/rɪˈspɑːnsər/", "bộ đáp tín hiệu"),
    ("083186", "responsory", "noun", "/rɪˈspɑːnsəri/", "bài thánh ca đối đáp"),
    ("083187", "responsum", "noun", "/rɪˈspɑːnsəm/", "phán quyết luật Do Thái"),
    ("083188", "respray", "verb", "/ˌriːˈspreɪ/", "phun lại; sơn lại"),
    ("083189", "restage", "verb", "/ˌriːˈsteɪdʒ/", "dàn dựng lại"),
    ("083190", "restake", "verb", "/ˌriːˈsteɪk/", "cắm cọc lại; làm mềm lại da"),
    ("083191", "restarted", "verb", "/ˌriːˈstɑːrtɪd/", "đã khởi động lại"),
    ("083192", "restarting", "verb", "/ˌriːˈstɑːrtɪŋ/", "đang khởi động lại"),
    ("083193", "restarts", "verb", "/ˌriːˈstɑːrts/", "khởi động lại"),
    ("083194", "restauranter", "noun", "/ˌrɛstəˈrɑːntər/", "chủ nhà hàng"),
    ("083195", "restauranteur", "noun", "/ˌrɛstərənˈtɜːr/", "chủ nhà hàng; người mở nhà hàng"),
    ("083196", "restharrow", "noun", "/ˈrɛstˌhæroʊ/", "cây cỏ bướm gai"),
    ("083197", "resthome", "noun", "/ˈrɛstˌhoʊm/", "nhà dưỡng lão; nhà điều dưỡng"),
    ("083198", "restibilis", "noun", "/rɪˈstɪbɪlɪs/", "cây trồng nhiều vụ liên tiếp"),
    ("083199", "restibrachium", "noun", "/ˌrɛstɪˈbreɪkiəm/", "cuống tiểu não dưới"),
    ("083200", "restif", "adj", "/ˈrɛstɪf/", "bồn chồn; bất kham"),
    ("083201", "restiform", "adj", "/ˈrɛstɪfɔːrm/", "dạng thừng; hình dây thừng"),
    ("083202", "resting", "verb", "/ˈrɛstɪŋ/", "đang nghỉ ngơi"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r07_raw_p2.json"))
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

json.dump(out, open("scratch/b37_r07_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b37_r07_p2 saved OK")
