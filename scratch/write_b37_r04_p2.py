import json

records = [
    ("081603", "rassling", "noun", "/ˈræslɪŋ/", "môn đấu vật (phương ngữ Mỹ)"),
    ("081604", "rasterize", "verb", "/ˈræstəˌraɪz/", "chuyển ảnh đồ họa thành điểm ảnh"),
    ("081605", "ratability", "noun", "/ˌreɪtəˈbɪləti/", "tình trạng thuộc diện chịu thuế"),
    ("081606", "ratables", "noun", "/ˈreɪtəbəlz/", "bất động sản thuộc diện chịu thuế"),
    ("081607", "ratafee", "noun", "/ˌrætəˈfiː/", "rượu mùi vị hạnh nhân (biến thể)"),
    ("081608", "ratafia", "noun", "/ˌrætəˈfiːə/", "rượu mùi hạnh nhân; bánh hạnh nhân"),
    ("081609", "ratal", "noun", "/ˈreɪtəl/", "mức định giá tài sản tính thuế"),
    ("081610", "ratanakiri", "noun", "/ˌrɑːtənɑːkɪˈriː/", "tỉnh Ratanakiri (Campuchia)"),
    ("081611", "ratatat", "noun", "/ˌrætəˈtæt/", "tiếng gõ cửa dồn dập cọc cọc"),
    ("081612", "ratbag", "noun", "/ˈrætbæɡ/", "gã đểu cáng, kẻ khó ưa (lóng Úc)"),
    ("081613", "ratcheted", "verb", "/ˈrætʃətɪd/", "đã tăng từng nấc; đã vặn bánh cóc"),
    ("081614", "ratcheting", "verb", "/ˈrætʃətɪŋ/", "tăng dần từng nấc; vặn bánh cóc"),
    ("081615", "ratchets", "verb", "/ˈrætʃəts/", "tăng dần từng nấc; siết bánh cóc"),
    ("081616", "rateability", "noun", "/ˌreɪtəˈbɪləti/", "tính chịu thuế tài sản (biến thể)"),
    ("081617", "rateables", "noun", "/ˈreɪtəbəlz/", "những tài sản chịu thuế địa phương"),
    ("081618", "rated", "verb", "/ˈreɪtɪd/", "đã đánh giá, xếp hạng; đã định mức"),
    ("081619", "ratemeter", "noun", "/ˈreɪtˌmiːtər/", "máy đo tốc độ xung đếm phóng xạ"),
    ("081620", "rater", "noun", "/ˈreɪtər/", "người đánh giá xếp hạng; người mắng"),
    ("081621", "ratfink", "noun", "/ˈrætˌfɪŋk/", "kẻ chỉ điểm, tên mật báo hèn hạ"),
    ("081622", "ratfinking", "verb", "/ˈrætˌfɪŋkɪŋ/", "mật báo, chỉ điểm phản bội bạn bè"),
    ("081623", "rath", "adj", "/ræθ/", "sớm, chín sớm (thơ ca cổ)"),
    ("081624", "rathe", "adj", "/reɪð/", "nở sớm, chín sớm trước mùa (cổ)"),
    ("081625", "ratherish", "adv", "/ˈræðərɪʃ/", "hơi hơi, phần nào (khẩu ngữ)"),
    ("081626", "ratibida", "noun", "/rəˈtɪbɪdə/", "chi hoa cúc nón đồng cỏ (Ratibida)"),
    ("081627", "raticide", "noun", "/ˈrætəˌsaɪd/", "thuốc diệt chuột; kẻ giết chuột"),
    ("081628", "ratifier", "noun", "/ˈrætəˌfaɪər/", "người phê chuẩn, người chuẩn y"),
    ("081629", "ratin", "noun", "/ˈrætɪn/", "thuốc diệt chuột (thuật ngữ cũ)"),
    ("081630", "ratine", "noun", "/ˌrætəˈneɪ/", "vải len dệt xoắn xù bề mặt (ratine)"),
    ("081631", "ratiocinate", "verb", "/ˌrætiˈɑːsəˌneɪt/", "suy luận logic, lập luận chặt chẽ"),
    ("081632", "ratiocinated", "verb", "/ˌrætiˈɑːsəˌneɪtɪd/", "đã suy luận logic có hệ thống"),
    ("081633", "ratiocinates", "verb", "/ˌrætiˈɑːsəˌneɪts/", "suy luận logic, lý luận có hệ thống"),
    ("081634", "ratiocinating", "verb", "/ˌrætiˈɑːsəˌneɪtɪŋ/", "suy luận logic, lập luận chặt chẽ"),
    ("081635", "ratiocinations", "noun", "/ˌrætiˌɑːsəˈneɪʃənz/", "những quá trình suy luận logic"),
    ("081636", "ratiocinative", "adj", "/ˌrætiˈɑːsənətɪv/", "dựa trên suy luận logic chặt chẽ"),
    ("081637", "ratiocinator", "noun", "/ˌrætiˈɑːsəˌneɪtər/", "người giỏi suy luận logic"),
    ("081638", "rationalizations", "noun", "/ˌræʃənələˈzeɪʃənz/", "sự hợp lý hóa; lý lẽ biện minh"),
    ("081639", "rationalness", "noun", "/ˈræʃənəlnəs/", "tính hợp lý, sự có lý sáng suốt"),
    ("081640", "rationals", "noun", "/ˈræʃənəlz/", "số hữu tỷ; quần dài thể thao nữ xưa"),
    ("081641", "rations", "verb", "/ˈræʃənz/", "phân phát khẩu phần, định suất"),
    ("081642", "ratitae", "noun", "/ˈrætəˌtiː/", "nhóm chim chạy không bay (đà điểu)"),
    ("081643", "ratlike", "adj", "/ˈrætˌlaɪk/", "giống chuột; xảo quyệt lén lút"),
    ("081644", "ratlin", "noun", "/ˈrætlɪn/", "bậc thang dây trên cột buồm tàu"),
    ("081645", "ratline", "noun", "/ˈrætlɪn/", "dây ngang làm thang leo cột buồm"),
    ("081646", "ratling", "noun", "/ˈrætlɪŋ/", "bậc thang dây cột buồm (biến thể)"),
    ("081647", "rato", "noun", "/ˈrɑːtoʊ/", "tên lửa trợ phóng máy bay cất cánh"),
    ("081648", "ratoon", "verb", "/rəˈtuːn/", "mọc chồi mới từ gốc (mía, dứa)"),
    ("081649", "ratos", "noun", "/ˈrɑːtoʊz/", "các tên lửa trợ phóng RATO"),
    ("081650", "rats", "verb", "/ræts/", "bắt chuột; phản bội, tố giác"),
    ("081651", "ratsbane", "noun", "/ˈrætsˌbeɪn/", "thuốc diệt chuột; thạch tín"),
    ("081652", "ratsnake", "noun", "/ˈrætˌsneɪk/", "rắn ráo săn chuột (họ Rắn nước)"),
    ("081653", "ratted", "verb", "/ˈrætɪd/", "đã bắt chuột; đã phản bội, tố giác"),
    ("081654", "ratteen", "noun", "/ræˈtiːn/", "vải len dày dệt chéo (ratteen)"),
    ("081655", "ratten", "verb", "/ˈrætən/", "phá hoại máy móc ép đình công"),
    ("081656", "rattlebox", "noun", "/ˈrætəlˌbɑːks/", "cây lục lạc; kẻ lắm mồm"),
    ("081657", "rattlebrained", "adj", "/ˈrætəlˌbreɪnd/", "đầu óc rỗng tuếch, ngớ ngẩn"),
    ("081658", "rattlepated", "adj", "/ˈrætəlˌpeɪtɪd/", "nông cạn, ba hoa, thiếu suy nghĩ"),
    ("081659", "rattles", "verb", "/ˈrætəlz/", "kêu lạch cạch; làm mất bình tĩnh"),
    ("081660", "raudixin", "noun", "/rɔːˈdɪksɪn/", "thuốc hạ huyết áp từ rễ ba gạc"),
    ("081661", "raut", "noun", "/raʊt/", "lệnh hành quân (từ quân sự cũ)"),
    ("081662", "rauvolfia", "noun", "/raʊˈwʊlfiə/", "chi cây Ba gạc (dược liệu)"),
    ("081663", "rauwolfia", "noun", "/raʊˈwʊlfiə/", "cây Ba gạc (chi Rauvolfia)"),
    ("081664", "ravages", "verb", "/ˈrævɪdʒɪz/", "tàn phá, hủy hoại nặng nề"),
    ("081665", "raved", "verb", "/reɪvd/", "đã nói sảng; đã khen nức nở"),
    ("081666", "ravehook", "noun", "/ˈreɪvˌhʊk/", "dụng cụ móc cạy xảm gỗ vỏ tàu"),
    ("081667", "ravelin", "noun", "/ˈrævəlɪn/", "pháo đài tam giác ngoài hào thành"),
    ("081668", "ravelled", "verb", "/ˈrævəld/", "đã gỡ rối; đã tước sợi; làm rối"),
    ("081669", "ravelling", "noun", "/ˈrævəlɪŋ/", "sợi chỉ tước ra từ mép vải"),
    ("081670", "ravels", "verb", "/ˈrævəlz/", "làm rối tung; tước sợi; gỡ nút rối"),
    ("081671", "ravenala", "noun", "/ˌrævəˈnɑːlə/", "cây chuối rẻ quạt (Ravenala)"),
    ("081672", "ravened", "verb", "/ˈrævənd/", "đã ăn ngấu nghiến; đã cướp bóc"),
    ("081673", "ravenousness", "noun", "/ˈrævənəsnəs/", "cơn đói cồn cào, sự tham lam vô độ"),
    ("081674", "ravens", "verb", "/ˈrævənz/", "ăn ngấu nghiến; lùng sục cướp phá"),
    ("081675", "raves", "verb", "/reɪvz/", "nói sảng, gào thét; khen hết lời"),
    ("081676", "ravigote", "noun", "/ˌrævɪˈɡoʊt/", "nước sốt thảo mộc chua cay Pháp"),
    ("081677", "ravigotte", "noun", "/ˌrævɪˈɡoʊt/", "nước sốt thảo mộc ravigote Pháp"),
    ("081678", "ravin", "noun", "/ˈrævɪn/", "sự cướp bóc; con mồi săn bắt được"),
    ("081679", "ravingly", "adv", "/ˈreɪvɪŋli/", "một cách điên cuồng, nói sảng dại"),
    ("081680", "ravished", "verb", "/ˈrævɪʃt/", "đã làm say mê; đã cưỡng bức"),
    ("081681", "ravisher", "noun", "/ˈrævɪʃər/", "kẻ cưỡng hiếp; kẻ cướp đoạt"),
    ("081682", "rawish", "adj", "/ˈrɔːɪʃ/", "hơi sống sượng; hơi buốt ẩm ướt"),
    ("081683", "rawlplug", "noun", "/ˈrɔːlˌplʌɡ/", "tắc kê nhựa nở đóng tường bắt vít"),
    ("081684", "rawly", "adv", "/ˈrɔːli/", "mộc mạc sống sượng; non nớt vụng về"),
    ("081685", "rayah", "noun", "/ˈrɑːjə/", "thần dân ngoài Hồi giáo (Ottoman)"),
    ("081686", "rayed", "adj", "/reɪd/", "có tia tỏa ra; có hoa cánh tỏa tia"),
    ("081687", "raying", "noun", "/ˈreɪɪŋ/", "sự chiếu xạ, sự phát tia sáng"),
    ("081688", "rayless", "adj", "/ˈreɪləs/", "không có tia sáng; mù mịt tối tăm"),
    ("081689", "rayne", "noun", "/reɪn/", "cơn mưa, trận mưa (cách viết cổ)"),
    ("081690", "rayonnant", "adj", "/ˌreɪəˈnɑːnt/", "tỏa tia; phong cách Gothic rực rỡ"),
    ("081691", "razbliuto", "noun", "/ˌræzbliˈjuːtoʊ/", "nỗi buồn man mác nhớ người từng yêu"),
    ("081692", "razes", "verb", "/ˈreɪzɪz/", "san phẳng, phá hủy hoàn toàn"),
    ("081693", "razmataz", "noun", "/ˈræzməˌtæz/", "trò phô trương hoa mỹ lòe loẹt"),
    ("081694", "razoo", "noun", "/rəˈzuː/", "đồng xu nhỏ mọn (không đáng một xu)"),
    ("081695", "razzed", "verb", "/ræzd/", "đã chế giễu, đã huýt sáo la ó"),
    ("081696", "razzes", "verb", "/ˈræzɪz/", "chế giễu, la ó trêu chọc (khẩu ngữ)"),
    ("081697", "razzia", "noun", "/ˈrætsiə/", "cuộc đột kích cướp bóc, càn quét"),
    ("081698", "rc", "noun", "/ˌɑːrˈsiː/", "Hội Chữ thập đỏ; Công giáo La Mã"),
    ("081699", "reabsorbed", "verb", "/ˌriːəbˈzɔːrbd/", "đã tái hấp thu, đã thu hút trở lại"),
    ("081700", "reabsorbing", "verb", "/ˌriːəbˈzɔːrbɪŋ/", "tái hấp thu, hút trở lại"),
    ("081701", "reabsorbs", "verb", "/ˌriːəbˈzɔːrbz/", "tái hấp thu, hấp thu trở lại"),
    ("081702", "reaccept", "verb", "/ˌriːəkˈsɛpt/", "chấp nhận lại, thu nhận trở lại"),
]

raw = json.load(open("scratch/b37_r04_raw_p2.json"))
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
with open("scratch/b37_r04_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r04_p2 saved OK")
