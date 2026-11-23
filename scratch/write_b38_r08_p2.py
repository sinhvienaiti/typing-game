import json

RECORDS = [
    ("088603", "sphenogram", "noun", "/ˈsfiːnəˌɡræm/", "chữ viết hình nêm cổ đại"),
    ("088604", "sphenoidal", "adj", "/sfiˈnɔɪdəl/", "thuộc xương bướm (hộp sọ); hình nêm"),
    ("088605", "sphenopsida", "noun", "/sfɪˈnɑːpsɪdə/", "lớp Cỏ tháp bút (Sphenopsida)"),
    ("088606", "spheral", "adj", "/ˈsfɪrəl/", "hình cầu; đối xứng như thiên cầu"),
    ("088607", "sphericalness", "noun", "/ˈsfɛrɪkəlnəs/", "tính hình cầu; độ tròn đều ba chiều"),
    ("088608", "spherics", "noun", "/ˈsfɪrɪks/", "hình học và lượng giác mặt cầu"),
    ("088609", "spherocyte", "noun", "/ˈsfɪrəˌsaɪt/", "hồng cầu hình cầu (bệnh lý)"),
    ("088610", "spheroidization", "noun", "/ˌsfɪrɔɪdaɪˈzeɪʃən/", "quá trình ủ cầu hóa thép"),
    ("088611", "spherometer", "noun", "/sfɪˈrɑːmɪtər/", "dụng cụ đo độ cong mặt cầu"),
    ("088612", "spherometers", "noun", "/sfɪˈrɑːmɪtərz/", "dụng cụ đo độ cong mặt cầu"),
    ("088613", "spherula", "noun", "/ˈsfɛrjələ/", "hình cầu nhỏ; tiểu cầu"),
    ("088614", "spherular", "adj", "/ˈsfɛrjələr/", "có dạng hình cầu nhỏ"),
    ("088615", "spherulate", "adj", "/ˈsfɛrjəlɪt/", "phủ hạt tròn nhỏ; dạng tiểu cầu"),
    ("088616", "spherule", "noun", "/ˈsfɛruːl/", "hình cầu nhỏ; hạt vi cầu"),
    ("088617", "spherulite", "noun", "/ˈsfɛrjəˌlaɪt/", "tinh cầu bức xạ trong đá hay nhựa"),
    ("088618", "spherulitic", "adj", "/ˌsfɛrjəˈlɪtɪk/", "có cấu trúc tinh thể hình cầu"),
    ("088619", "sphery", "adj", "/ˈsfɪri/", "hình cầu tròn; thuộc thiên cầu"),
    ("088620", "sphincteral", "adj", "/sfɪŋkˈtɪrəl/", "thuộc cơ vòng; cơ thắt"),
    ("088621", "sphincterial", "adj", "/sfɪŋkˈtɪriəl/", "thuộc cơ vòng; cơ thắt"),
    ("088622", "sphincteric", "adj", "/sfɪŋkˈtɛrɪk/", "thuộc cơ vòng; cơ thắt"),
    ("088623", "sphinges", "noun", "/ˈsfɪndʒiːz/", "nhân sư Ai Cập; bướm đêm diều hâu"),
    ("088624", "sphingid", "noun", "/ˈsfɪŋɡɪd/", "bướm đêm diều hâu họ Sphingidae"),
    ("088625", "sphingine", "adj", "/ˈsfɪŋɡaɪn/", "giống nhân sư; thuộc bướm diều hâu"),
    ("088626", "sphragistics", "noun", "/sfrəˈdʒɪstɪks/", "ấn chương học (nghiên cứu con dấu)"),
    ("088627", "sphygmic", "adj", "/ˈsfɪɡmɪk/", "thuộc mạch đập; nhịp tim"),
    ("088628", "sphygmogram", "noun", "/ˈsfɪɡməˌɡræm/", "đồ thị ghi sóng mạch đập"),
    ("088629", "sphygmograph", "noun", "/ˈsfɪɡməˌɡræf/", "máy ghi đồ thị mạch đập"),
    ("088630", "sphygmographic", "adj", "/ˌsfɪɡməˈɡræfɪk/", "thuộc phép ghi mạch đập"),
    ("088631", "sphygmography", "noun", "/sfɪɡˈmɑːɡrəfi/", "phép ghi đồ thị mạch đập"),
    ("088632", "sphygmoid", "adj", "/ˈsfɪɡmɔɪd/", "giống nhịp đập của mạch máu"),
    ("088633", "sphygmology", "noun", "/sfɪɡˈmɑːlədʒi/", "mạch học (nghiên cứu mạch đập)"),
    ("088634", "sphygmometer", "noun", "/sfɪɡˈmɑːmɪtər/", "máy đo huyết áp và mạch đập"),
    ("088635", "sphygmophone", "noun", "/ˈsfɪɡməˌfoʊn/", "máy nghe âm thanh mạch đập"),
    ("088636", "sphygmoscope", "noun", "/ˈsfɪɡməˌskoʊp/", "dụng cụ quan sát dao động mạch"),
    ("088637", "sphygmus", "noun", "/ˈsfɪɡməs/", "nhịp mạch đập"),
    ("088638", "sphynx", "noun", "/sfɪŋks/", "tượng Nhân sư; giống mèo không lông"),
    ("088639", "sphyraena", "noun", "/sfɪˈriːnə/", "chi Cá nhồng biển (Sphyraena)"),
    ("088640", "sphyraenidae", "noun", "/sfɪˈrɛnɪˌdiː/", "họ Cá nhồng (Sphyraenidae)"),
    ("088641", "sphyrapicus", "noun", "/ˌsfɪrəˈpaɪkəs/", "chi chim gõ kiến hút nhựa cây"),
    ("088642", "sphyrna", "noun", "/ˈsfɜːrnə/", "chi Cá nhám búa (Sphyrna)"),
    ("088643", "sphyrnidae", "noun", "/ˈsfɜːrnɪˌdiː/", "họ Cá nhám búa (Sphyrnidae)"),
    ("088644", "spicate", "adj", "/ˈspaɪkeɪt/", "mọc thành cụm hoa dạng bông"),
    ("088645", "spicated", "adj", "/ˈspaɪkeɪtɪd/", "có cụm hoa dạng bông thóc"),
    ("088646", "spiceberry", "noun", "/ˈspaɪsˌbɛri/", "cây cơm nguội đỏ; cây lộc đề"),
    ("088647", "spiced", "verb", "/spaɪst/", "đã nêm gia vị; làm thêm hấp dẫn"),
    ("088648", "spicemill", "noun", "/ˈspaɪsˌmɪl/", "cối xay hạt tiêu và gia vị"),
    ("088649", "spicery", "noun", "/ˈspaɪsəri/", "gia vị thơm; mùi hương cay nồng"),
    ("088650", "spices", "verb", "/ˈspaɪsɪz/", "nêm gia vị; làm thêm phần thú vị"),
    ("088651", "spicily", "adv", "/ˈspaɪsɪli/", "cay nồng thơm; hơi khiêu khích"),
    ("088652", "spicing", "verb", "/ˈspaɪsɪŋ/", "đang nêm gia vị; làm thêm thú vị"),
    ("088653", "spicula", "noun", "/ˈspɪkjələ/", "gai xương nhỏ (bọt biển, san hô)"),
    ("088654", "spicular", "adj", "/ˈspɪkjələr/", "nhọn như gai nhỏ; có gai nhỏ"),
    ("088655", "spiculate", "adj", "/ˈspɪkjəˌleɪt/", "có gai nhọn nhỏ li ti"),
    ("088656", "spiculum", "noun", "/ˈspɪkjələm/", "gai nhỏ; kim xương bọt biển"),
    ("088657", "spiderflower", "noun", "/ˈspaɪdərˌflaʊər/", "hoa túy điệp (cây màn màn)"),
    ("088658", "spidergram", "noun", "/ˈspaɪdərˌɡræm/", "sơ đồ tư duy mạng nhện"),
    ("088659", "spiderlike", "adj", "/ˈspaɪdərˌlaɪk/", "giống con nhện; mảnh khảnh dài"),
    ("088660", "spiderly", "adj", "/ˈspaɪdərli/", "giống con nhện; có chân dài ngoẵng"),
    ("088661", "spiderman", "noun", "/ˈspaɪdərˌmæn/", "thợ leo giàn giáo cao; Người Nhện"),
    ("088662", "spiderwort", "noun", "/ˈspaɪdərˌwɜːrt/", "cây thài lài tím Tradescantia"),
    ("088663", "spied", "verb", "/spaɪd/", "đã làm gián điệp; đã thoáng thấy"),
    ("088664", "spiegeleisen", "noun", "/ˈspiːɡəlˌaɪzən/", "gang trắng giàu mangan (luyện thép)"),
    ("088665", "spieled", "verb", "/spiːld/", "đã ba hoa diễn thuyết quảng cáo"),
    ("088666", "spieling", "verb", "/ˈspiːlɪŋ/", "đang ba hoa diễn thuyết mời chào"),
    ("088667", "spiels", "verb", "/spiːlz/", "diễn thuyết ba hoa để quảng cáo"),
    ("088668", "spier", "noun", "/ˈspaɪər/", "người rình rập do thám; điệp viên"),
    ("088669", "spies", "noun", "/spaɪz/", "điệp viên; gián điệp"),
    ("088670", "spifflicate", "verb", "/ˈspɪflɪˌkeɪt/", "đánh nhừ tử; đánh choáng váng"),
    ("088671", "spifflication", "noun", "/ˌspɪflɪˈkeɪʃən/", "trận đòn nhừ tử; sự đè bẹp"),
    ("088672", "spiffling", "adj", "/ˈspɪflɪŋ/", "tuyệt vời; cừ khôi (từ cổ)"),
    ("088673", "spiflicate", "verb", "/ˈspɪflɪˌkeɪt/", "đánh nhừ tử; cho ăn đòn choáng váng"),
    ("088674", "spiflication", "noun", "/ˌspɪflɪˈkeɪʃən/", "trận đòn nhừ tử; sự đè bẹp"),
    ("088675", "spikefish", "noun", "/ˈspaɪkˌfɪʃ/", "cá bò gai nhọn họ Triacanthodidae"),
    ("088676", "spikelets", "noun", "/ˈspaɪkləts/", "gié hoa nhỏ (cỏ, lúa)"),
    ("088677", "spikelike", "adj", "/ˈspaɪkˌlaɪk/", "có hình dạng gai nhọn"),
    ("088678", "spikemoss", "noun", "/ˈspaɪkˌmɔːs/", "cây quyển bá (họ Selaginellaceae)"),
    ("088679", "spikes", "verb", "/spaɪks/", "tăng vọt đột biến; đóng đinh; pha"),
    ("088680", "spikewise", "adv", "/ˈspaɪkˌwaɪz/", "theo hình dạng mũi nhọn"),
    ("088681", "spiking", "verb", "/ˈspaɪkɪŋ/", "đang tăng vọt; đang lén pha thuốc"),
    ("088682", "spiling", "noun", "/ˈspaɪlɪŋ/", "hàng cọc cừ chống sạt hầm mỏ"),
    ("088683", "spilled", "verb", "/spɪld/", "đã làm đổ tràn; đã tiết lộ hết"),
    ("088684", "spillikin", "noun", "/ˈspɪlɪkɪn/", "que gỗ mỏng trong trò chơi rút que"),
    ("088685", "spillikins", "noun", "/ˈspɪlɪkɪnz/", "trò chơi rút que khéo tay"),
    ("088686", "spilling", "verb", "/ˈspɪlɪŋ/", "đang làm đổ tràn; đang tuôn ra"),
    ("088687", "spills", "verb", "/spɪlz/", "làm đổ tràn; tuôn trào; khai sạch"),
    ("088688", "spilogale", "noun", "/ˌspɪloʊˈɡeɪli/", "chi chồn hôi đốm Bắc Mỹ"),
    ("088689", "spiloma", "noun", "/spɪˈloʊmə/", "vết bớt sắc tố; nốt ruồi bẩm sinh"),
    ("088690", "spilt", "verb", "/spɪlt/", "đã làm đổ tràn; đã tuôn ra"),
    ("088691", "spilth", "noun", "/spɪlθ/", "phần chất lỏng bị đổ tràn ra ngoài"),
    ("088692", "spina", "noun", "/ˈspaɪnə/", "gai xương; dải phân cách trường đua"),
    ("088693", "spinaceous", "adj", "/spɪˈneɪʃəs/", "thuộc rau bina (cải bó xôi)"),
    ("088694", "spinacia", "noun", "/spɪˈneɪʃə/", "chi Cải bó xôi (Spinacia)"),
    ("088695", "spinage", "noun", "/ˈspɪnɪdʒ/", "rau chân vịt; cải bó xôi"),
    ("088696", "spinally", "adv", "/ˈspaɪnəli/", "dọc theo cột sống; vào tủy sống"),
    ("088697", "spinant", "noun", "/ˈspaɪnənt/", "chất kích thích phản xạ tủy sống"),
    ("088698", "spinate", "adj", "/ˈspaɪneɪt/", "có gai nhọn; dạng gai"),
    ("088699", "spination", "noun", "/spaɪˈneɪʃən/", "sự phân bố gai trên cơ thể"),
    ("088700", "spindleberry", "noun", "/ˈspɪndəlˌbɛri/", "cây thục lê hương Euonymus"),
    ("088701", "spindled", "verb", "/ˈspɪndəld/", "đã vươn thân mảnh khảnh cao vọt"),
    ("088702", "spindlelegs", "noun", "/ˈspɪndəlˌlɛɡz/", "người có đôi chân gầy khẳng khiu"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r08_raw_p2.json"))
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

json.dump(out, open("scratch/b38_r08_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b38_r08_p2 saved OK")
