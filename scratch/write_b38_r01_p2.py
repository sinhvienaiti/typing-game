import json

RECORDS = [
    ("085103", "scalped", "verb", "/skælpt/", "đã lột da đầu; đã phe vé chợ đen"),
    ("085104", "scalpers", "noun", "/ˈskælpərz/", "người phe vé chợ đen; kẻ đầu cơ"),
    ("085105", "scalping", "verb", "/ˈskælpɪŋ/", "đang lột da đầu; đang lướt sóng"),
    ("085106", "scalpriform", "adj", "/ˈskælprɪˌfɔːrm/", "có hình lưỡi đục (răng cửa)"),
    ("085107", "scalps", "verb", "/skælps/", "lột da đầu; bán vé chợ đen"),
    ("085108", "scammony", "noun", "/ˈskæməni/", "cây bìm bìm tây Á làm thuốc tẩy"),
    ("085109", "scammonyroot", "noun", "/ˈskæməniˌruːt/", "rễ cây bìm bìm tây Á làm thuốc"),
    ("085110", "scampered", "verb", "/ˈskæmpərd/", "đã chạy vội; đã chạy lăng xăng"),
    ("085111", "scampering", "verb", "/ˈskæmpərɪŋ/", "đang chạy vội; đang chạy lăng xăng"),
    ("085112", "scampers", "verb", "/ˈskæmpərz/", "chạy vội; chạy nhảy lăng xăng"),
    ("085113", "scampish", "adj", "/ˈskæmpɪʃ/", "tinh ranh; láu cá; bất lương"),
    ("085114", "scampo", "noun", "/ˈskæmpoʊ/", "tôm hùm đất Na Uy; tôm scampi"),
    ("085115", "scandalisation", "noun", "/ˌskændəlaɪˈzeɪʃən/", "sự gây tai tiếng; nỗi công phẫn"),
    ("085116", "scandalised", "verb", "/ˈskændəˌlaɪzd/", "đã gây phẫn nộ; đã làm tai tiếng"),
    ("085117", "scandalises", "verb", "/ˈskændəˌlaɪzɪz/", "gây phẫn nộ; làm tai tiếng"),
    ("085118", "scandalising", "verb", "/ˈskændəˌlaɪzɪŋ/", "đang gây phẫn nộ; làm sốc"),
    ("085119", "scandalization", "noun", "/ˌskændəlaɪˈzeɪʃən/", "sự gây tai tiếng; nỗi công phẫn"),
    ("085120", "scandalized", "verb", "/ˈskændəˌlaɪzd/", "đã gây phẫn nộ; đã làm tai tiếng"),
    ("085121", "scandalizes", "verb", "/ˈskændəˌlaɪzɪz/", "gây phẫn nộ; làm tai tiếng"),
    ("085122", "scandalizing", "verb", "/ˈskændəˌlaɪzɪŋ/", "đang gây phẫn nộ; làm sốc"),
    ("085123", "scandalmonger", "noun", "/ˈskændəlˌmʌŋɡər/", "kẻ chuyên phao tin đồn thất thiệt"),
    ("085124", "scandalmongering", "adj", "/ˈskændəlˌmʌŋɡərɪŋ/", "hay phao tin đồn nhảm câu khách"),
    ("085125", "scandalousness", "noun", "/ˈskændələsnəs/", "tính chất tai tiếng; sự ô nhục"),
    ("085126", "scandent", "adj", "/ˈskændənt/", "mọc leo; có thân leo"),
    ("085127", "scandentia", "noun", "/skænˈdɛnʃə/", "bộ Đồi (Scandentia)"),
    ("085128", "scanned", "verb", "/skænd/", "đã quét; đã đọc lướt"),
    ("085129", "scans", "verb", "/skænz/", "quét ảnh; đọc lướt; kiểm tra nhịp"),
    ("085130", "scansores", "noun", "/skænˈsɔːriːz/", "nhóm chim leo trèo"),
    ("085131", "scansorial", "adj", "/skænˈsɔːriəl/", "thích nghi leo trèo (chim, thú)"),
    ("085132", "scanted", "verb", "/ˈskæntɪd/", "đã cắt xén; đã bớt xén ít ỏi"),
    ("085133", "scanties", "noun", "/ˈskæntiz/", "quần lót mỏng của phụ nữ"),
    ("085134", "scanting", "verb", "/ˈskæntɪŋ/", "đang cắt xén; đang tiết kiệm tằn tiện"),
    ("085135", "scantness", "noun", "/ˈskæntnəs/", "sự thiếu thốn; tình trạng ít ỏi"),
    ("085136", "scants", "verb", "/skænts/", "cắt xén; cung cấp thiếu thốn"),
    ("085137", "scapegoats", "noun", "/ˈskeɪpˌɡoʊts/", "vật tế thần; người gánh tội thay"),
    ("085138", "scapeless", "adj", "/ˈskeɪpləs/", "không có cuống hoa; không thân"),
    ("085139", "scapelike", "adj", "/ˈskeɪpˌlaɪk/", "giống cuống hoa; dạng trục"),
    ("085140", "scapha", "noun", "/ˈskeɪfə/", "rãnh vành tai ngoài"),
    ("085141", "scaphander", "noun", "/skəˈfændər/", "bộ đồ lặn có mũ chụp; chi ốc"),
    ("085142", "scaphiopus", "noun", "/skəˈfaɪəpəs/", "chi cóc chân xẻng Bắc Mỹ"),
    ("085143", "scaphium", "noun", "/ˈskeɪfiəm/", "cơ quan sinh dục bướm đực"),
    ("085144", "scaphocephaly", "noun", "/ˌskæfoʊˈsɛfəli/", "dị tật hộp sọ hình thuyền"),
    ("085145", "scaphognathite", "noun", "/skəˈfɑːɡnəˌθaɪt/", "tấm quạt nước mang giáp xác"),
    ("085146", "scaphopod", "noun", "/ˈskæfəˌpɑːd/", "động vật thân mềm vỏ ngà"),
    ("085147", "scaphopoda", "noun", "/skəˈfɑːpədə/", "lớp Vỏ ngà (Scaphopoda)"),
    ("085148", "scaphosepalum", "noun", "/ˌskæfoʊˈsɛpələm/", "chi phong lan Scaphosepalum"),
    ("085149", "scapose", "adj", "/ˈskeɪpoʊs/", "có cuống hoa mọc từ gốc"),
    ("085150", "scapulae", "noun", "/ˈskæpjəˌliː/", "xương bả vai"),
    ("085151", "scapulary", "noun", "/ˈskæpjəˌlɛri/", "áo choàng vai tu sĩ; băng đeo vai"),
    ("085152", "scapulohumeral", "adj", "/ˌskæpjəloʊˈhjuːmərəl/", "thuộc xương bả vai và cánh tay"),
    ("085153", "scarabaean", "noun", "/ˌskærəˈbiːən/", "bọ cánh cứng họ Bọ hung"),
    ("085154", "scarabaeid", "noun", "/ˌskærəˈbiːɪd/", "bọ hung"),
    ("085155", "scarabaeoid", "adj", "/ˌskærəˈbiːɔɪd/", "giống bọ hung"),
    ("085156", "scarabeiform", "adj", "/skəˈræbiɪˌfɔːrm/", "có hình dạng ấu trùng bọ hung"),
    ("085157", "scarabeus", "noun", "/ˌskærəˈbiːəs/", "bọ hung Ai Cập"),
    ("085158", "scarcement", "noun", "/ˈskɛrsmənt/", "bậc thềm thu hẹp của tường móng"),
    ("085159", "scarceness", "noun", "/ˈskɛrsnəs/", "sự khan hiếm; sự thiếu hụt"),
    ("085160", "scardinius", "noun", "/skɑːrˈdɪniəs/", "chi cá chép vây đỏ châu Âu"),
    ("085161", "scarecrowish", "adj", "/ˈskɛrˌkroʊɪʃ/", "gầy gò rách rưới như bù nhìn"),
    ("085162", "scarecrows", "noun", "/ˈskɛrˌkroʊz/", "bù nhìn đuổi chim"),
    ("085163", "scaremongering", "noun", "/ˈskɛrˌmʌŋɡərɪŋ/", "việc tung tin đồn gây hoang mang"),
    ("085164", "scares", "verb", "/skɛrz/", "làm sợ hãi; dọa nạt"),
    ("085165", "scarey", "adj", "/ˈskɛri/", "đáng sợ; dễ sợ"),
    ("085166", "scarfed", "verb", "/skɑːrft/", "đã quàng khăn; đã ăn ngấu nghiến"),
    ("085167", "scarfer", "noun", "/ˈskɑːrfər/", "máy vát mép mối nối gỗ"),
    ("085168", "scarfing", "verb", "/ˈskɑːrfɪŋ/", "đang quàng khăn; đang ghép vát"),
    ("085169", "scarfpin", "noun", "/ˈskɑːrfˌpɪn/", "trâm cài cà vạt"),
    ("085170", "scarfs", "verb", "/skɑːrfs/", "quàng khăn; ăn ngấu nghiến"),
    ("085171", "scaridae", "noun", "/ˈskærɪˌdiː/", "họ Cá mó (cá vẹt biển)"),
    ("085172", "scarification", "noun", "/ˌskærɪfɪˈkeɪʃən/", "sự rạch nông da; sự xới mặt đất"),
    ("085173", "scarificator", "noun", "/ˈskærɪfɪˌkeɪtər/", "dao rạch da giác hơi; máy xới đất"),
    ("085174", "scarified", "verb", "/ˈskærəˌfaɪd/", "đã rạch da; đã xới đất; làm sờn"),
    ("085175", "scarifier", "noun", "/ˈskærəˌfaɪər/", "máy cào cỏ; dao rạch da"),
    ("085176", "scarifies", "verb", "/ˈskærəˌfaɪz/", "rạch da; xới đất; đả kích gay gắt"),
    ("085177", "scarifying", "verb", "/ˈskærəˌfaɪɪŋ/", "đang rạch da; đang xới tơi đất"),
    ("085178", "scaring", "verb", "/ˈskɛrɪŋ/", "đang làm sợ hãi; đang hù dọa"),
    ("085179", "scarious", "adj", "/ˈskɛriəs/", "khô mỏng như màng giấy (lá bắc)"),
    ("085180", "scarped", "verb", "/skɑːrpt/", "đã vạt thành dốc đứng"),
    ("085181", "scarpered", "verb", "/ˈskɑːrpərd/", "đã cao chạy xa bay; bỏ trốn"),
    ("085182", "scarpering", "verb", "/ˈskɑːrpərɪŋ/", "đang bỏ chạy; đang tẩu thoát"),
    ("085183", "scarpers", "verb", "/ˈskɑːrpərz/", "bỏ chạy; chuồn mất"),
    ("085184", "scarph", "verb", "/skɑːrf/", "ghép vát mộng gỗ; ăn ngấu nghiến"),
    ("085185", "scarping", "verb", "/ˈskɑːrpɪŋ/", "đang vạt dốc đứng"),
    ("085186", "scarps", "verb", "/skɑːrps/", "vạt thành vách dốc đứng"),
    ("085187", "scarring", "verb", "/ˈskɑːrɪŋ/", "đang để lại sẹo; gây tổn thương"),
    ("085188", "scarry", "adj", "/ˈskɑːri/", "đầy vết sẹo; có sẹo"),
    ("085189", "scars", "verb", "/skɑːrz/", "để lại sẹo; gây chấn thương"),
    ("085190", "scartella", "noun", "/skɑːrˈtɛlə/", "chi cá mào gà Scartella"),
    ("085191", "scarus", "noun", "/ˈskɛrəs/", "chi cá vẹt biển Scarus"),
    ("085192", "scarves", "noun", "/skɑːrvz/", "khăn quàng cổ; khăn choàng"),
    ("085193", "scathed", "verb", "/skeɪðd/", "đã gây tổn hại; đã chỉ trích"),
    ("085194", "scatheless", "adj", "/ˈskeɪðləs/", "bình an vô sự; không bị tổn hại"),
    ("085195", "scatophagous", "adj", "/skəˈtɑːfəɡəs/", "ăn phân (côn trùng, động vật)"),
    ("085196", "scatophagy", "noun", "/skəˈtɑːfədʒi/", "tập tính ăn phân"),
    ("085197", "scats", "verb", "/skæts/", "hát ứng tác scat; xua đi nhanh"),
    ("085198", "scatted", "verb", "/ˈskætɪd/", "đã hát ứng tác scat; đã chạy biến"),
    ("085199", "scattergoad", "noun", "/ˈskætərˌɡʊd/", "kẻ tiêu xài hoang phí phung phí"),
    ("085200", "scattergram", "noun", "/ˈskætərˌɡræm/", "biểu đồ phân tán"),
    ("085201", "scattergrams", "noun", "/ˈskætərˌɡræmz/", "biểu đồ phân tán"),
    ("085202", "scatters", "verb", "/ˈskætərz/", "phân tán; rải rác; xua tan"),
]

# Shorten 085110, 085111, 085134 cleanly
RECORDS[7] = ("085110", "scampered", "verb", "/ˈskæmpərd/", "đã chạy vội; chạy lăng xăng")
RECORDS[8] = ("085111", "scampering", "verb", "/ˈskæmpərɪŋ/", "đang chạy vội; chạy lăng xăng")
RECORDS[31] = ("085134", "scanting", "verb", "/ˈskæntɪŋ/", "đang cắt xén; đang bớt xén")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r01_raw_p2.json"))
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

json.dump(out, open("scratch/b38_r01_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b38_r01_p2 saved OK")
