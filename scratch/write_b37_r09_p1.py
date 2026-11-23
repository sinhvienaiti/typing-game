import json

RECORDS = [
    ("084003", "roid", "noun", "/rɔɪd/", "thuốc steroid đồng hóa (lóng)"),
    ("084004", "roils", "verb", "/rɔɪlz/", "khuấy đục; làm bực mình"),
    ("084005", "roily", "adj", "/ˈrɔɪli/", "đục ngầu; bị khuấy đục"),
    ("084006", "roinek", "noun", "/ˈrɔɪnɛk/", "người Anh mới di cư đến Nam Phi"),
    ("084007", "roistered", "verb", "/ˈrɔɪstərd/", "đã tiệc tùng ồn ào; nô đùa ầm ĩ"),
    ("084008", "roisterer", "noun", "/ˈrɔɪstərər/", "kẻ tiệc tùng ồn ào; kẻ khoác lác"),
    ("084009", "roistering", "verb", "/ˈrɔɪstərɪŋ/", "đang tiệc tùng ồn ào"),
    ("084010", "roisterous", "adj", "/ˈrɔɪstərəs/", "ồn ào; hống hách"),
    ("084011", "roisters", "verb", "/ˈrɔɪstərz/", "tiệc tùng ồn ào; khoác lác"),
    ("084012", "rok", "noun", "/rɑːk/", "chim khổng lồ Roc trong truyền thuyết"[:35]),
    ("084013", "roke", "noun", "/roʊk/", "hơi sương; mạch quặng; bọt khí"),
    ("084014", "rollable", "adj", "/ˈroʊləbəl/", "có thể cuộn lại; có thể cán mỏng"),
    ("084015", "rollerblader", "noun", "/ˈroʊlərˌbleɪdər/", "người trượt giày patin một hàng"),
    ("084016", "rollercoaster", "noun", "/ˈroʊlərˌkoʊstər/", "tàu lượn siêu tốc"),
    ("084017", "rolley", "noun", "/ˈrɑːli/", "xe bò kéo bốn bánh"),
    ("084018", "rollick", "verb", "/ˈrɑːlɪk/", "nô đùa ầm ĩ; chạy nhảy vui vẻ"),
    ("084019", "rollickingly", "adv", "/ˈrɑːlɪkɪŋli/", "vui vẻ ồn ào; phóng khoáng"),
    ("084020", "rollmop", "noun", "/ˈroʊlˌmɑːp/", "phi lê cá trích cuộn ngâm giấm"),
    ("084021", "rollmops", "noun", "/ˈroʊlˌmɑːps/", "cá trích cuộn ngâm giấm"),
    ("084022", "rollout", "noun", "/ˈroʊlˌaʊt/", "sự ra mắt sản phẩm; đợt triển khai"),
    ("084023", "rolls", "verb", "/roʊlz/", "lăn; cuộn lại"),
    ("084024", "rolypoliness", "noun", "/ˌroʊliˈpoʊlinəs/", "vẻ tròn trịa mũm mĩm"),
    ("084025", "romaic", "adj", "/roʊˈmeɪɪk/", "thuộc tiếng Hy Lạp hiện đại"),
    ("084026", "romanal", "noun", "/ˈroʊməˌnæl/", "ngôn ngữ nhân tạo Romanal"),
    ("084027", "romanced", "verb", "/roʊˈmænst/", "đã tán tỉnh; đã lãng mạn hóa"),
    ("084028", "romancer", "noun", "/roʊˈmænsər/", "tác giả truyện kỳ ảo; kẻ tán tỉnh"),
    ("084029", "romances", "verb", "/roʊˈmænsɪz/", "tán tỉnh; thêu dệt lãng mạn"),
    ("084030", "romancing", "verb", "/roʊˈmænsɪŋ/", "đang tán tỉnh; đang lãng mạn hóa"),
    ("084031", "romanise", "verb", "/ˈroʊməˌnaɪz/", "La-tinh hóa chữ viết"),
    ("084032", "romanization", "noun", "/ˌroʊmənəˈzeɪʃən/", "sự La-tinh hóa chữ viết"),
    ("084033", "romano", "noun", "/roʊˈmɑːnoʊ/", "phô mai cứng Romano của Ý"),
    ("084034", "romanticised", "verb", "/roʊˈmæntəˌsaɪzd/", "đã lãng mạn hóa"),
    ("084035", "romanticises", "verb", "/roʊˈmæntəˌsaɪzɪz/", "lãng mạn hóa"),
    ("084036", "romanticising", "verb", "/roʊˈmæntəˌsaɪzɪŋ/", "đang lãng mạn hóa"),
    ("084037", "romanticistic", "adj", "/roʊˌmæntəˈsɪstɪk/", "thuộc chủ nghĩa lãng mạn"),
    ("084038", "romantics", "noun", "/roʊˈmæntɪks/", "người lãng mạn; nhà lãng mạn"),
    ("084039", "romewards", "adv", "/ˈroʊmwərdz/", "hướng về thành Rome"),
    ("084040", "rommany", "noun", "/ˈrɑːməni/", "người Di-gan; tiếng Romani"),
    ("084041", "romneya", "noun", "/rɑːmˈniːə/", "chi cây anh túc Matilija"),
    ("084042", "romped", "verb", "/rɑːmpt/", "đã nô đùa chạy nhảy"),
    ("084043", "rompers", "noun", "/ˈrɑːmpərz/", "quần yếm trẻ em; bộ đồ liền thân"),
    ("084044", "romping", "verb", "/ˈrɑːmpɪŋ/", "đang nô đùa chạy nhảy"),
    ("084045", "rompingly", "adv", "/ˈrɑːmpɪŋli/", "vui nhộn ồn ào"),
    ("084046", "rompish", "adj", "/ˈrɑːmpɪʃ/", "hiếu động; thích nô đùa ầm ĩ"),
    ("084047", "romps", "verb", "/rɑːmps/", "nô đùa chạy nhảy; thắng dễ dàng"),
    ("084048", "rompy", "adj", "/ˈrɑːmpi/", "thích nô đùa ầm ĩ"),
    ("084049", "ronan", "noun", "/ˈroʊnən/", "tên riêng nam Ronan"),
    ("084050", "rondache", "noun", "/rɑːnˈdɑːʃ/", "khiên tròn bộ binh thời xưa"),
    ("084051", "rondavel", "noun", "/rɑːnˈdɑːvəl/", "nhà tròn mái tranh Nam Phi"),
    ("084052", "rondelet", "noun", "/ˈrɑːndəlɪt/", "thể thơ Pháp rondelet"),
    ("084053", "rondure", "noun", "/ˈrɑːndʒər/", "dáng tròn; đường cong tròn"),
    ("084054", "roneograph", "noun", "/ˈroʊniəˌɡræf/", "máy in quay roneo"),
    ("084055", "rontgenogram", "noun", "/ˈrɛntɡənəˌɡræm/", "phim chụp X-quang"),
    ("084056", "roo", "noun", "/ruː/", "chuột túi kangaroo (cách gọi ngắn)"),
    ("084057", "roofage", "noun", "/ˈruːfɪdʒ/", "vật liệu lợp mái; mái nhà"),
    ("084058", "rooflight", "noun", "/ˈruːfˌlaɪt/", "cửa sổ trời trên mái"),
    ("084059", "roofrack", "noun", "/ˈruːfˌræk/", "giá chở đồ trên nóc ô tô"),
    ("084060", "roofs", "verb", "/ruːfs/", "lợp mái nhà"),
    ("084061", "roofslab", "noun", "/ˈruːfˌslæb/", "tấm đan lợp mái"),
    ("084062", "rooftree", "noun", "/ˈruːfˌtriː/", "đòn nóc; xà nóc mái nhà"),
    ("084063", "roofy", "noun", "/ˈruːfi/", "thuốc ngủ mạnh flunitrazepam"),
    ("084064", "rooinek", "noun", "/ˈrɔɪnɛk/", "người Anh mới di cư đến Nam Phi"),
    ("084065", "rooked", "verb", "/rʊkt/", "đã lừa bịp; đã chặt chém tiền"),
    ("084066", "rooker", "noun", "/ˈrʊkər/", "kẻ lừa đảo cờ bạc"),
    ("084067", "rookeries", "noun", "/ˈrʊkəriz/", "bãi sinh sản chim biển; khu ổ chuột"),
    ("084068", "rooking", "verb", "/ˈrʊkɪŋ/", "đang lừa bịp; đang chặt chém"),
    ("084069", "rooks", "verb", "/rʊks/", "lừa bịp; chặt chém tiền"),
    ("084070", "rooky", "noun", "/ˈrʊki/", "tân binh; người mới vào nghề"),
    ("084071", "roomed", "verb", "/ruːmd/", "đã ở trọ; đã thuê phòng"),
    ("084072", "roomily", "adv", "/ˈruːmɪli/", "rộng rãi; thoáng đãng"),
    ("084073", "rooming", "verb", "/ˈruːmɪŋ/", "đang ở trọ; đang thuê phòng"),
    ("084074", "roorback", "noun", "/ˈrʊrˌbæk/", "tin đồn thất thiệt bôi nhọ chính trị"),
    ("084075", "rooseveltian", "adj", "/ˌroʊzəˈvɛltiən/", "thuộc Tổng thống Roosevelt"),
    ("084076", "roosted", "verb", "/ˈruːstɪd/", "đã đậu ngủ (chim); đã nghỉ đêm"),
    ("084077", "roosting", "verb", "/ˈruːstɪŋ/", "đang đậu ngủ (chim)"),
    ("084078", "roosts", "verb", "/ruːsts/", "đậu ngủ trên cành (chim)"),
    ("084079", "rootage", "noun", "/ˈruːtɪdʒ/", "bộ rễ; sự bén rễ vững chắc"),
    ("084080", "rootbound", "adj", "/ˈruːtˌbaʊnd/", "bị bó rễ trong chậu"),
    ("084081", "rootle", "verb", "/ˈruːtəl/", "dũi đất bằng mõm; lục tìm"),
    ("084082", "rootlessness", "noun", "/ˈruːtləsnəs/", "tình trạng không cội rễ; bơ vơ"),
    ("084083", "rootlet", "noun", "/ˈruːtlɪt/", "rễ con; rễ phụ"),
    ("084084", "rootstalk", "noun", "/ˈruːtˌstɔːk/", "thân rễ; gốc ghép"),
    ("084085", "rooty", "adj", "/ˈruːti/", "nhiều rễ; giống rễ cây"),
    ("084086", "ropebark", "noun", "/ˈroʊpˌbɑːrk/", "cây vỏ dai làm dây thừng"),
    ("084087", "roped", "verb", "/roʊpt/", "đã trói bằng dây; đã quăng thòng lọng"),
    ("084088", "ropedancer", "noun", "/ˈroʊpˌdænsər/", "diễn viên xiếc đi trên dây"),
    ("084089", "ropemaker", "noun", "/ˈroʊpˌmeɪkər/", "thợ bện dây thừng"),
    ("084090", "ropemanship", "noun", "/ˈroʊpmənˌʃɪp/", "kỹ năng sử dụng dây leo núi"),
    ("084091", "ropes", "verb", "/roʊps/", "trói bằng dây; quăng dây bắt"),
    ("084092", "ropewalker", "noun", "/ˈroʊpˌwɔːkər/", "người đi thăng bằng trên dây"),
    ("084093", "rophy", "noun", "/ˈruːfi/", "thuốc mê mạnh flunitrazepam"),
    ("084094", "ropiness", "noun", "/ˈroʊpinəs/", "độ nhớt quánh; tính dai dính"),
    ("084095", "roquelaure", "noun", "/ˌrɑːkəˈlɔːr/", "áo choàng dài cổ điển đến gối"),
    ("084096", "roquet", "noun", "/roʊˈkeɪ/", "cú đánh bóng chạm bóng đối phương"),
    ("084097", "roridula", "noun", "/rəˈrɪdjələ/", "chi cây bắt mồi Roridula"),
    ("084098", "roridulaceae", "noun", "/rəˌrɪdjəˈleɪsiːˌiː/", "họ thực vật Roridulaceae"),
    ("084099", "rorippa", "noun", "/rəˈrɪpə/", "chi cải đất Rorippa"),
    ("084100", "roro", "noun", "/ˈroʊˌroʊ/", "tàu chở xe chạy thẳng (roll-on)"),
    ("084101", "rorty", "adj", "/ˈrɔːrti/", "vui nhộn; náo nhiệt; xôm tụ"),
    ("084102", "rosace", "noun", "/roʊˈzeɪs/", "cửa sổ hoa hồng (kiến trúc)"),
]

# Ensure 084012, 084074, 084087 are <= 35 cleanly
RECORDS[9] = ("084012", "rok", "noun", "/rɑːk/", "chim khổng lồ Roc thần thoại")
RECORDS[71] = ("084074", "roorback", "noun", "/ˈrʊrˌbæk/", "tin đồn thất thiệt bôi nhọ")
RECORDS[84] = ("084087", "roped", "verb", "/roʊpt/", "đã trói dây; đã quăng dây bắt")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r09_raw_p1.json"))
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

json.dump(out, open("scratch/b37_r09_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b37_r09_p1 saved OK")
