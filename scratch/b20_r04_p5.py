import json
import re

# Batch 20 Round 4 Part 5 (096902 to 097001, 100 records)
# Fully manual cognitive translation & QA review

raw_file = "scratch/b20_r04_raw_p5.json"
out_file = "scratch/b20_r04_p5.json"

with open(raw_file, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100, f"Expected 100 records, got {len(raw_data)}"

reviewed = {
    "lex.en.100k.096902": ("olivet", "noun", "/ˈɑː.lɪ.vɪt/", "khuy áo nhỏ hình quả ô-liu"),
    "lex.en.100k.096903": ("olivette", "noun", "/ˌɑː.lɪˈvet/", "hạt khuy hình quả ô-liu; đèn rọi"),
    "lex.en.100k.096904": ("olivin", "noun", "/ˈɑː.lə.vɪn/", "khoáng vật olivin (silicat)"),
    "lex.en.100k.096905": ("olivinic", "adj", "/ˌɑː.ləˈvɪn.ɪk/", "thuộc khoáng vật olivin"),
    "lex.en.100k.096906": ("ollari", "noun", "/ˈɑː.lə.ri/", "tiếng Ollari (ngữ hệ Dravida)"),
    "lex.en.100k.096907": ("om", "noun", "/oʊm/", "từ Om; Huân chương Công trạng"),
    "lex.en.100k.096908": ("omadhaun", "noun", "/ˈɑː.mə.hɔːn/", "kẻ ngốc nghếch; gã khờ Ái Nhĩ Lan"),
    "lex.en.100k.096909": ("omasum", "noun", "/oʊˈmeɪ.səm/", "dạ lá sách (dạ dày thú nhai lại)"),
    "lex.en.100k.096910": ("omayyad", "noun", "/uːˈmaɪ.jæd/", "triều đại Hồi giáo Umayyad"),
    "lex.en.100k.096911": ("ombilic", "adj", "/ˈɑːm.bɪ.lɪk/", "thuộc lỗ gốc cuống lông chim"),
    "lex.en.100k.096912": ("ombratropism", "noun", "/ˌɑːm.brəˈtroʊ.pɪ.zəm/", "tính hướng mưa (ở thực vật)"),
    "lex.en.100k.096913": ("ombre", "noun", "/ˈɑːm.bɚ/", "bài ombre; hiệu ứng chuyển màu"),
    "lex.en.100k.096914": ("ombrology", "noun", "/ɑːmˈbrɑː.lə.dʒi/", "khoa nghiên cứu lượng mưa"),
    "lex.en.100k.096915": ("ombrometer", "noun", "/ɑːmˈbrɑː.mə.t̬ɚ/", "vũ kế; máy đo lượng mưa"),
    "lex.en.100k.096916": ("ombrophil", "adj", "/ˈɑːm.brə.fɪl/", "ưa mưa; thích nghi vùng mưa nhiều"),
    "lex.en.100k.096917": ("ombrophile", "noun", "/ˈɑːm.brə.faɪl/", "cây ưa mưa; thực vật vùng mưa nhiều"),
    "lex.en.100k.096918": ("ombrophobe", "noun", "/ˈɑːm.brə.foʊb/", "cây sợ mưa; thực vật kỵ mưa"),
    "lex.en.100k.096919": ("ombu", "noun", "/ɔːmˈbuː/", "cây ombu thảo nguyên Nam Mỹ"),
    "lex.en.100k.096920": ("ombudsmen", "noun", "/ˈɑːm.bʊdz.mən/", "các thanh tra viên nhân dân"),
    "lex.en.100k.096921": ("omelettes", "noun", "/ˈɑːm.ləts/", "các món trứng cuộn rán; ốp-lết"),
    "lex.en.100k.096922": ("omened", "adj", "/ˈoʊ.mənd/", "có điềm báo trước; báo trước điềm"),
    "lex.en.100k.096923": ("omenta", "noun", "/oʊˈmen.tə/", "các mạc nối ruột màng bụng"),
    "lex.en.100k.096924": ("omental", "adj", "/oʊˈmen.t̬əl/", "thuộc mạc nối dạ dày ruột"),
    "lex.en.100k.096925": ("omer", "noun", "/ˈoʊ.mɚ/", "đơn vị đo omer của Do Thái cổ"),
    "lex.en.100k.096926": ("omg", "intj", "/ˌoʊ.emˈdʒiː/", "trời ơi; ôi chúa ơi (viết tắt)"),
    "lex.en.100k.096927": ("omissible", "adj", "/oʊˈmɪs.ə.bəl/", "có thể bỏ qua; có thể lược bỏ"),
    "lex.en.100k.096928": ("omissive", "adj", "/oʊˈmɪs.ɪv/", "có tính bỏ sót; dễ sao lãng"),
    "lex.en.100k.096929": ("omits", "verb", "/oʊˈmɪts/", "bỏ sót; bỏ quên; lược bỏ"),
    "lex.en.100k.096930": ("omittance", "noun", "/oʊˈmɪt.əns/", "sự bỏ qua; sự sao lãng tạm thời"),
    "lex.en.100k.096931": ("omitted", "verb", "/oʊˈmɪt̬.ɪd/", "đã bỏ qua; đã lược bớt"),
    "lex.en.100k.096932": ("omitting", "verb", "/oʊˈmɪt̬.ɪŋ/", "đang bỏ sót; đang lược bỏ"),
    "lex.en.100k.096933": ("omlet", "noun", "/ˈɑːm.lət/", "món trứng cuộn (cách viết cổ)"),
    "lex.en.100k.096934": ("ommachromes", "noun", "/ˈɑː.mə.kroʊmz/", "các sắc tố mắt côn trùng"),
    "lex.en.100k.096935": ("ommastrephes", "noun", "/ˌɑː.məˈstref.iːz/", "chi mực ống Ommastrephes"),
    "lex.en.100k.096936": ("ommateum", "noun", "/ˌɑː.məˈtiː.əm/", "mắt kép ở chân khớp"),
    "lex.en.100k.096937": ("ommatidial", "adj", "/ˌɑː.məˈtɪd.i.əl/", "thuộc mắt con trong mắt kép"),
    "lex.en.100k.096938": ("ommatidium", "noun", "/ˌɑː.məˈtɪd.i.əm/", "mắt con (đơn vị của mắt kép)"),
    "lex.en.100k.096939": ("ommatophore", "noun", "/oʊˈmæt̬.əˌfɔːr/", "cuống mắt ở ốc sên"),
    "lex.en.100k.096940": ("ommatophorous", "adj", "/ˌɑː.məˈtɑː.fɚ.əs/", "có mang cuống mắt"),
    "lex.en.100k.096941": ("ommiad", "noun", "/uːˈmaɪ.jæd/", "nhà Umayyad (cách viết khác)"),
    "lex.en.100k.096942": ("omnibuses", "noun", "/ˈɑːm.nɪ.bʌs.ɪz/", "các xe buýt; các tập sách tuyển tập"),
    "lex.en.100k.096943": ("omnicompetence", "noun", "/ˌɑːm.nɪˈkɑːm.pə.təns/", "năng lực hoặc thẩm quyền toàn phần"),
    "lex.en.100k.096944": ("omnicompetent", "adj", "/ˌɑːm.nɪˈkɑːm.pə.tənt/", "có năng lực và quyền hạn toàn diện"),
    "lex.en.100k.096945": ("omnifarious", "adj", "/ˌɑːm.nɪˈfer.i.əs/", "thuộc đủ mọi loại; muôn vẻ"),
    "lex.en.100k.096946": ("omniferous", "adj", "/ɑːmˈnɪf.ɚ.əs/", "sinh ra đủ mọi thứ; sinh muôn loài"),
    "lex.en.100k.096947": ("omnific", "adj", "/ɑːmˈnɪf.ɪk/", "sáng tạo ra muôn loài; vạn năng"),
    "lex.en.100k.096948": ("omnificent", "adj", "/ɑːmˈnɪf.ə.sənt/", "có quyền năng sáng tạo muôn vật"),
    "lex.en.100k.096949": ("omniform", "adj", "/ˈɑːm.nɪ.fɔːrm/", "có đủ mọi hình dạng; muôn hình"),
    "lex.en.100k.096950": ("omniformity", "noun", "/ˌɑːm.nɪˈfɔːr.mə.t̬i/", "tính muôn hình vạn trạng"),
    "lex.en.100k.096951": ("omnigenous", "adj", "/ɑːmˈnɪdʒ.ə.nəs/", "gồm đủ mọi chủng loại"),
    "lex.en.100k.096952": ("omnipercipience", "noun", "/ˌɑːm.nɪ.pɚˈsɪp.i.əns/", "khả năng thấu suốt vạn vật"),
    "lex.en.100k.096953": ("omnipotency", "noun", "/ɑːmˈnɪp.ə.tən.si/", "quyền năng vô hạn; sự toàn năng"),
    "lex.en.100k.096954": ("omnirange", "noun", "/ˈɑːm.nɪˌreɪndʒ/", "đài vô tuyến dẫn đường đa hướng"),
    "lex.en.100k.096955": ("omnivorousness", "noun", "/ɑːmˈnɪv.ɚ.əs.nəs/", "tính ăn tạp; sự ham đọc đủ thứ"),
    "lex.en.100k.096956": ("omomyid", "noun", "/oʊˈmɑː.mi.ɪd/", "linh trưởng hóa thạch Omomyidae"),
    "lex.en.100k.096957": ("omophagia", "noun", "/ˌoʊ.moʊˈfeɪ.dʒə/", "tục ăn thịt sống trong tế lễ"),
    "lex.en.100k.096958": ("omophagic", "adj", "/ˌoʊ.moʊˈfædʒ.ɪk/", "thuộc tục ăn thịt sống"),
    "lex.en.100k.096959": ("omophagist", "noun", "/oʊˈmɑː.fə.dʒɪst/", "người có tục ăn thịt sống"),
    "lex.en.100k.096960": ("omophagous", "adj", "/oʊˈmɑː.fə.ɡəs/", "có thói quen ăn thịt sống"),
    "lex.en.100k.096961": ("omophalocele", "noun", "/ˌɑːm.fə.loʊˈsiːl/", "tật thoát vị rốn bẩm sinh"),
    "lex.en.100k.096962": ("omophalotomy", "noun", "/ˌɑːm.fəˈlɑː.tə.mi/", "thủ thuật cắt dây rốn sơ sinh"),
    "lex.en.100k.096963": ("omoplate", "noun", "/ˈoʊ.məˌpleɪt/", "xương bả vai (giải phẫu)"),
    "lex.en.100k.096964": ("omotic", "adj", "/oʊˈmɑː.tɪk/", "thuộc nhóm ngôn ngữ Omotic"),
    "lex.en.100k.096965": ("omotocia", "noun", "/ˌoʊ.moʊˈtoʊ.ʃi.ə/", "chứng sinh non; đẻ non"),
    "lex.en.100k.096966": ("omphalic", "adj", "/ɑːmˈfæl.ɪk/", "thuộc về rốn; liên quan đến rốn"),
    "lex.en.100k.096967": ("omphalodium", "noun", "/ˌɑːm.fəˈloʊ.di.əm/", "vết sẹo rốn trên hạt cây"),
    "lex.en.100k.096968": ("omphalogenesis", "noun", "/ˌɑːm.fə.loʊˈdʒen.ə.sɪs/", "sự hình thành rốn phôi thai"),
    "lex.en.100k.096969": ("omphaloid", "adj", "/ˈɑːm.fə.lɔɪd/", "có hình dạng giống cái rốn"),
    "lex.en.100k.096970": ("omphaloidium", "noun", "/ˌɑːm.fəˈlɔɪ.di.əm/", "vết rốn nhỏ trên vỏ hạt giống"),
    "lex.en.100k.096971": ("omphalomesenteric", "adj", "/ˌɑːm.fə.loʊˌmez.ənˈter.ɪk/", "thuộc cuống rốn và mạc treo"),
    "lex.en.100k.096972": ("omphaloskepsis", "noun", "/ˌɑːm.fə.loʊˈskep.sɪs/", "sự ngắm rốn suy tưởng; chiêm nghiệm"),
    "lex.en.100k.096973": ("omphalotomy", "noun", "/ˌɑːm.fəˈlɑː.tə.mi/", "thủ thuật cắt dây rốn"),
    "lex.en.100k.096974": ("omphalotus", "noun", "/ˌɑːm.fəˈloʊ.təs/", "chi nấm phát quang Omphalotus"),
    "lex.en.100k.096975": ("omphalus", "noun", "/ˈɑːm.fə.ləs/", "rốn; tâm điểm trung tâm"),
    "lex.en.100k.096976": ("onagraceae", "noun", "/ˌɑː.nəˈɡreɪ.siː/", "họ Rau dừa nước Onagraceae"),
    "lex.en.100k.096977": ("onagraceous", "adj", "/ˌɑː.nəˈɡreɪ.ʃəs/", "thuộc họ Rau dừa nước"),
    "lex.en.100k.096978": ("onagri", "noun", "/ˈɑː.nə.ɡraɪ/", "các con lừa hoang Onager"),
    "lex.en.100k.096979": ("onanist", "noun", "/ˈoʊ.nə.nɪst/", "người thủ dâm; xuất tinh ngoài"),
    "lex.en.100k.096980": ("onanistic", "adj", "/ˌoʊ.nəˈnɪs.tɪk/", "thuộc hành vi thủ dâm"),
    "lex.en.100k.096981": ("oncer", "noun", "/ˈwʌn.sɚ/", "việc chỉ làm một lần; tờ một bảng"),
    "lex.en.100k.096982": ("onchocercosis", "noun", "/ˌɑːŋ.koʊ.sɝːˈkoʊ.sɪs/", "bệnh giun chỉ Onchocerca"),
    "lex.en.100k.096983": ("onchosphere", "noun", "/ˈɑːŋ.kəˌsfɪr/", "ấu trùng có móc sán dây"),
    "lex.en.100k.096984": ("oncogenesis", "noun", "/ˌɑːŋ.koʊˈdʒen.ə.sɪs/", "quá trình sinh u; sinh ung thư"),
    "lex.en.100k.096985": ("oncogenic", "adj", "/ˌɑːŋ.koʊˈdʒen.ɪk/", "có khả năng gây khối u ung thư"),
    "lex.en.100k.096986": ("oncogenicity", "noun", "/ˌɑːŋ.koʊ.dʒəˈnɪs.ə.t̬i/", "khả năng sinh khối u ung thư"),
    "lex.en.100k.096987": ("oncogenous", "adj", "/ɑːŋˈkɑː.dʒə.nəs/", "gây u; phát sinh khối u bướu"),
    "lex.en.100k.096988": ("oncosis", "noun", "/ɑːŋˈkoʊ.sɪs/", "sự phồng to tế bào hoại tử; u"),
    "lex.en.100k.096989": ("oncosphere", "noun", "/ˈɑːŋ.kəˌsfɪr/", "ấu trùng sáu móc của sán dây"),
    "lex.en.100k.096990": ("oncospore", "noun", "/ˈɑːŋ.kəˌspɔːr/", "bào tử mang móc bám"),
    "lex.en.100k.096991": ("oncotomy", "noun", "/ɑːŋˈkɑː.tə.mi/", "phẫu thuật mở khối u bướu"),
    "lex.en.100k.096992": ("oncovin", "noun", "/ˈɑːŋ.koʊˌvɪn/", "thuốc vincristine chống ung thư"),
    "lex.en.100k.096993": ("ondatra", "noun", "/ɑːnˈdæt.rə/", "chi chuột hương Bắc Mỹ Ondatra"),
    "lex.en.100k.096994": ("ondograph", "noun", "/ˈɑːn.dəˌɡræf/", "máy tự ghi dạng sóng điện"),
    "lex.en.100k.096995": ("ondographs", "noun", "/ˈɑːn.dəˌɡræfs/", "các máy tự ghi dạng sóng điện"),
    "lex.en.100k.096996": ("ondometer", "noun", "/ɑːnˈdɑː.mə.t̬ɚ/", "dụng cụ đo bước sóng điện từ"),
    "lex.en.100k.096997": ("ondoscope", "noun", "/ˈɑːn.dəˌskoʊp/", "máy chỉ thị sóng điện từ"),
    "lex.en.100k.096998": ("onefold", "adj", "/ˈwʌn.foʊld/", "đơn nhất; chỉ một phần; giản đơn"),
    "lex.en.100k.096999": ("oneirism", "noun", "/oʊˈnaɪ.rɪ.zəm/", "ảo mộng khi thức; trạng thái mơ"),
    "lex.en.100k.097000": ("oneirocritic", "noun", "/oʊˌnaɪ.roʊˈkrɪt.ɪk/", "người giải mộng; người đoán giấc mơ"),
    "lex.en.100k.097001": ("oneirocritical", "adj", "/oʊˌnaɪ.roʊˈkrɪt̬.ɪ.kəl/", "thuộc thuật giải đoán giấc mơ"),
}

VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

processed = []
for item in raw_data:
    item_id = item["id"]
    assert item_id in reviewed, f"Missing id: {item_id}"
    hw, pos, ipa, vi = reviewed[item_id]
    
    assert hw == item["hw"], f"HW mismatch: {hw} vs {item['hw']}"
    assert pos in VALID_POS, f"Invalid POS: {pos}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Invalid IPA: {ipa}"
    assert len(vi) <= 35, f"Vietnamese text too long ({len(vi)} chars): '{vi}'"
    assert not re.search(r"(Số nhiều của|Xem|Dạng|Viết tắt|Động từ chia|%%)", vi), f"Crawler artifact in vi: '{vi}'"

    new_item = {
        "id": item["id"],
        "hw": item["hw"],
        "pos": pos,
        "ipa": ipa,
        "vi": vi,
        "cefr": item["cefr"],
        "tier": item["tier"],
        "status": "reviewed",
        "notes": item["notes"],
    }
    processed.append(new_item)

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(processed, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(processed)} items to {out_file}")
