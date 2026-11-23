import json
import re

# Batch 20 Round 5 Part 1 (097002 to 097101, 100 records)
# Fully manual cognitive translation & QA review

raw_file = "scratch/b20_r05_raw_p1.json"
out_file = "scratch/b20_r05_p1.json"

with open(raw_file, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100, f"Expected 100 records, got {len(raw_data)}"

reviewed = {
    "lex.en.100k.097002": ("oneirocriticism", "noun", "/oʊˌnaɪ.roʊˈkrɪt.ɪ.sɪ.zəm/", "thuật giải đoán giấc mộng"),
    "lex.en.100k.097003": ("oneirodynia", "noun", "/oʊˌnaɪ.roʊˈdɪn.i.ə/", "cơn ác mộng dữ dội khi ngủ"),
    "lex.en.100k.097004": ("oneirology", "noun", "/ˌoʊ.nɪˈrɑː.lə.dʒi/", "môn mộng học; nghiên cứu giấc mơ"),
    "lex.en.100k.097005": ("oneiromancer", "noun", "/oʊˈnaɪ.roʊˌmæn.sɚ/", "thầy bói mộng; người đoán giấc mơ"),
    "lex.en.100k.097006": ("oneiromancy", "noun", "/oʊˈnaɪ.roʊˌmæn.si/", "thuật bói mộng; chiêm tinh qua mơ"),
    "lex.en.100k.097007": ("onenesses", "noun", "/ˈwʌn.nəs.ɪz/", "sự đồng nhất; trạng thái duy nhất"),
    "lex.en.100k.097008": ("oner", "noun", "/ˈwʌn.ɚ/", "người độc nhất vô nhị; cú đòn mạnh"),
    "lex.en.100k.097009": ("onerously", "adv", "/ˈɑː.nɚ.əs.li/", "một cách nặng nề; khó nhọc"),
    "lex.en.100k.097010": ("onerousness", "noun", "/ˈɑː.nɚ.əs.nəs/", "tính chất nặng nề; gánh nặng khó"),
    "lex.en.100k.097011": ("onfall", "noun", "/ˈɑːn.fɑːl/", "sự tấn công bất ngờ; cơn bão tuyết"),
    "lex.en.100k.097012": ("onflow", "noun", "/ˈɑːn.floʊ/", "dòng chảy tới; sự dâng tràn tới"),
    "lex.en.100k.097013": ("ongoings", "noun", "/ˈɑːnˌɡoʊ.ɪŋz/", "các sự việc đang diễn ra; hành vi"),
    "lex.en.100k.097014": ("onhanger", "noun", "/ˈɑːnˌhæŋ.ɚ/", "kẻ bám đuôi; người ăn theo"),
    "lex.en.100k.097015": ("onhook", "adj", "/ˌɑːnˈhʊk/", "đã gác máy điện thoại"),
    "lex.en.100k.097016": ("onioned", "verb", "/ˈʌn.jənd/", "đã nêm hành tây; thêm hành"),
    "lex.en.100k.097017": ("onioning", "verb", "/ˈʌn.jən.ɪŋ/", "đang nêm hành; đang thêm củ hành"),
    "lex.en.100k.097018": ("onions", "noun", "/ˈʌn.jənz/", "những củ hành tây"),
    "lex.en.100k.097019": ("oniony", "adj", "/ˈʌn.jən.i/", "có mùi hành tây; vị nồng hành tây"),
    "lex.en.100k.097020": ("oniscidae", "noun", "/oʊˈnɪs.ɪ.diː/", "họ Mọt ẩm Oniscidae"),
    "lex.en.100k.097021": ("oniscus", "noun", "/oʊˈnɪs.kəs/", "chi mọt ẩm Oniscus"),
    "lex.en.100k.097022": ("onlay", "noun", "/ˈɑːn.leɪ/", "miếng trám mặt ngoài răng"),
    "lex.en.100k.097023": ("onliness", "noun", "/ˈoʊn.li.nəs/", "trạng thái duy nhất; tính cô độc"),
    "lex.en.100k.097024": ("onlooking", "adj", "/ˈɑːnˌlʊk.ɪŋ/", "đang đứng xem; đứng ngoài nhìn"),
    "lex.en.100k.097025": ("onobrychis", "noun", "/ˌɑː.noʊˈbraɪ.kɪs/", "chi cỏ Onobrychis họ đậu"),
    "lex.en.100k.097026": ("onocentaur", "noun", "/ˌɑː.noʊˈsen.tɔːr/", "quái vật mình người thân lừa"),
    "lex.en.100k.097027": ("onoclea", "noun", "/ˌɑː.noʊˈkliː.ə/", "chi dương xỉ nhạy cảm Onoclea"),
    "lex.en.100k.097028": ("onomancer", "noun", "/ˈɑː.noʊˌmæn.sɚ/", "thầy bói tên; người bói theo tên"),
    "lex.en.100k.097029": ("onomancy", "noun", "/ˈɑː.noʊˌmæn.si/", "thuật bói tên để đoán số mệnh"),
    "lex.en.100k.097030": ("onomatology", "noun", "/ˌɑː.noʊ.məˈtɑː.lə.dʒi/", "danh xưng học; môn nghiên cứu tên"),
    "lex.en.100k.097031": ("onomatomania", "noun", "/ˌɑː.noʊ.mæt̬.oʊˈmeɪ.ni.ə/", "chứng ám ảnh từ ngữ danh xưng"),
    "lex.en.100k.097032": ("onomatop", "noun", "/əˈnɑː.mə.toʊp/", "từ tượng thanh"),
    "lex.en.100k.097033": ("onomatope", "noun", "/əˈnɑː.mə.toʊp/", "từ ngữ tượng thanh"),
    "lex.en.100k.097034": ("onomatopoeical", "adj", "/ˌɑː.nəˌmæt̬.əˈpiː.ɪ.kəl/", "có tính chất tượng thanh"),
    "lex.en.100k.097035": ("onomatopolia", "noun", "/ˌɑː.noʊˌmæt̬.əˈpoʊ.li.ə/", "sự tạo ra từ tượng thanh"),
    "lex.en.100k.097036": ("onomatopy", "noun", "/ˌɑː.noʊˈmæt̬.ə.pi/", "phép tạo từ tượng thanh"),
    "lex.en.100k.097037": ("ononis", "noun", "/oʊˈnoʊ.nɪs/", "chi đậu Ononis; cây gai Ononis"),
    "lex.en.100k.097038": ("onopordon", "noun", "/ˌɑː.noʊˈpɔːr.dɑːn/", "chi kế bông Onopordum"),
    "lex.en.100k.097039": ("onopordum", "noun", "/ˌɑː.noʊˈpɔːr.dəm/", "chi kế bông Onopordum"),
    "lex.en.100k.097040": ("onosmodium", "noun", "/ˌɑː.noʊzˈmoʊ.di.əm/", "chi lưu ly Onosmodium Bắc Mỹ"),
    "lex.en.100k.097041": ("onrushing", "adj", "/ˈɑːnˌrʌʃ.ɪŋ/", "đang cuộn trào tới; lao xông tới"),
    "lex.en.100k.097042": ("ontic", "adj", "/ˈɑːn.tɪk/", "thuộc thực tại hiện sinh"),
    "lex.en.100k.097043": ("onto", "prep", "/ˈɑːn.tuː/", "lên trên; về phía trên"),
    "lex.en.100k.097044": ("ontogenetically", "adv", "/ˌɑːn.toʊ.dʒəˈnet̬.ɪ.kli/", "theo phương diện phát triển cá thể"),
    "lex.en.100k.097045": ("ontologist", "noun", "/ɑːnˈtɑː.lə.dʒɪst/", "nhà bản thể học"),
    "lex.en.100k.097046": ("onychia", "noun", "/oʊˈnɪk.i.ə/", "chứng viêm móng; sưng gốc móng"),
    "lex.en.100k.097047": ("onychium", "noun", "/oʊˈnɪk.i.əm/", "chi dương xỉ Onychium móng"),
    "lex.en.100k.097048": ("onychius", "noun", "/oʊˈnɪk.i.əs/", "đệm vuốt ở côn trùng"),
    "lex.en.100k.097049": ("onychogalea", "noun", "/ˌɑː.nɪ.koʊˈɡeɪ.li.ə/", "chi chuột túi có vuốt đuôi"),
    "lex.en.100k.097050": ("onychogenic", "adj", "/ˌɑː.nɪ.koʊˈdʒen.ɪk/", "tạo móng; phát triển móng"),
    "lex.en.100k.097051": ("onychoid", "adj", "/ˈɑː.nɪ.kɔɪd/", "có hình dạng giống cái móng"),
    "lex.en.100k.097052": ("onycholysis", "noun", "/ˌɑː.nɪˈkɑː.lə.sɪs/", "chứng bong móng; long móng"),
    "lex.en.100k.097053": ("onychomys", "noun", "/oʊˈnɪk.ə.mɪs/", "chi chuột ăn thịt Onychomys"),
    "lex.en.100k.097054": ("onychophora", "noun", "/ˌɑː.nɪˈkɑː.fɚ.ə/", "ngành giun nhung Onychophora"),
    "lex.en.100k.097055": ("onychophoran", "noun", "/ˌɑː.nɪˈkɑː.fɚ.ən/", "loài giun nhung có chân"),
    "lex.en.100k.097056": ("onychosis", "noun", "/ˌɑː.nɪˈkoʊ.sɪs/", "bệnh loạn dưỡng móng tay"),
    "lex.en.100k.097057": ("onymous", "adj", "/ˈɑː.nɪ.məs/", "có ghi rõ tên tác giả; hữu danh"),
    "lex.en.100k.097058": ("onymy", "noun", "/ˈɑː.nɪ.mi/", "hệ thống định danh; thuật ngữ"),
    "lex.en.100k.097059": ("onyxis", "noun", "/oʊˈnɪk.sɪs/", "chứng móng chọc thịt; mọc ngược"),
    "lex.en.100k.097060": ("oocarp", "noun", "/ˈoʊ.əˌkɑːrp/", "quả nang hình trứng"),
    "lex.en.100k.097061": ("oocentre", "noun", "/ˈoʊ.əˌsen.tɚ/", "thể trung tâm của tế bào trứng"),
    "lex.en.100k.097062": ("oocinet", "noun", "/ˈoʊ.ə.saɪˌnet/", "hợp tử động (trong sinh học)"),
    "lex.en.100k.097063": ("oocyst", "noun", "/ˈoʊ.əˌsɪst/", "kén hợp tử trứng ký sinh trùng"),
    "lex.en.100k.097064": ("oocysts", "noun", "/ˈoʊ.əˌsɪsts/", "các kén hợp tử ký sinh trùng"),
    "lex.en.100k.097065": ("ooecia", "noun", "/oʊˈiː.ʃi.ə/", "các túi ấp trứng của rêu biển"),
    "lex.en.100k.097066": ("ooecium", "noun", "/oʊˈiː.ʃi.əm/", "túi ấp trứng của sinh vật bọt"),
    "lex.en.100k.097067": ("oof", "noun", "/uːf/", "tiền bạc của cải; tiếng hự đau"),
    "lex.en.100k.097068": ("oofy", "adj", "/ˈuː.fi/", "giàu có xụ; lắm tiền nhiều của"),
    "lex.en.100k.097069": ("oogamete", "noun", "/ˌoʊ.ə.ɡəˈmiːt/", "giao tử cái; noãn cầu cái"),
    "lex.en.100k.097070": ("oogamous", "adj", "/oʊˈɑː.ɡə.məs/", "thuộc kiểu noãn giao"),
    "lex.en.100k.097071": ("oogenetic", "adj", "/ˌoʊ.ə.dʒəˈnet̬.ɪk/", "thuộc quá trình sinh trứng"),
    "lex.en.100k.097072": ("oogonial", "adj", "/ˌoʊ.əˈɡoʊ.ni.əl/", "thuộc noãn nguyên bào"),
    "lex.en.100k.097073": ("oogonium", "noun", "/ˌoʊ.əˈɡoʊ.ni.əm/", "noãn nguyên bào; túi noãn"),
    "lex.en.100k.097074": ("ooid", "adj", "/ˈoʊ.ɔɪd/", "có hình trứng; dạng quả trứng"),
    "lex.en.100k.097075": ("ookinesis", "noun", "/ˌoʊ.ə.kɪˈniː.sɪs/", "sự phân chia nhân của tế bào trứng"),
    "lex.en.100k.097076": ("oolite", "noun", "/ˈoʊ.əˌlaɪt/", "đá vôi trứng cá; oolit"),
    "lex.en.100k.097077": ("oolith", "noun", "/ˈoʊ.əˌlɪθ/", "hạt sỏi đá hình trứng cá"),
    "lex.en.100k.097078": ("oolitic", "adj", "/ˌoʊ.əˈlɪt̬.ɪk/", "thuộc kết cấu đá vôi trứng cá"),
    "lex.en.100k.097079": ("oological", "adj", "/ˌoʊ.əˈlɑː.dʒɪk.əl/", "thuộc ngành điểu noãn học"),
    "lex.en.100k.097080": ("oologist", "noun", "/oʊˈɑː.lə.dʒɪst/", "nhà nghiên cứu trứng chim"),
    "lex.en.100k.097081": ("oology", "noun", "/oʊˈɑː.lə.dʒi/", "điểu noãn học; nghiên cứu trứng"),
    "lex.en.100k.097082": ("oomycetes", "noun", "/ˌoʊ.ə.maɪˈsiː.tiːz/", "lớp nấm trứng Oomycetes"),
    "lex.en.100k.097083": ("oont", "noun", "/uːnt/", "con lạc đà (từ mượn Ấn Độ)"),
    "lex.en.100k.097084": ("oophore", "noun", "/ˈoʊ.əˌfɔːr/", "thể sinh noãn; buồng trứng"),
    "lex.en.100k.097085": ("oophoridium", "noun", "/ˌoʊ.ə.fəˈrɪd.i.əm/", "túi bào tử cái ở rêu"),
    "lex.en.100k.097086": ("oophoritis", "noun", "/ˌoʊ.ə.fəˈraɪ.t̬ɪs/", "chứng viêm buồng trứng"),
    "lex.en.100k.097087": ("oophoron", "noun", "/oʊˈɑː.fɚ.ɑːn/", "buồng trứng (giải phẫu y khoa)"),
    "lex.en.100k.097088": ("oophorosalpingectomy", "noun", "/ˌoʊ.ə.fɔː.roʊˌsæl.pɪnˈdʒek.tə.mi/", "cắt buồng trứng và vòi trứng"),
    "lex.en.100k.097089": ("oophyte", "noun", "/ˈoʊ.əˌfaɪt/", "thể giao tử sinh noãn"),
    "lex.en.100k.097090": ("oophytic", "adj", "/ˌoʊ.əˈfɪt̬.ɪk/", "thuộc thể giao tử sinh noãn"),
    "lex.en.100k.097091": ("ooplasm", "noun", "/ˈoʊ.əˌplæz.əm/", "noãn chất; tế bào chất của noãn"),
    "lex.en.100k.097092": ("ooplasmic", "adj", "/ˌoʊ.əˈplæz.mɪk/", "thuộc tế bào chất của noãn"),
    "lex.en.100k.097093": ("ooplast", "noun", "/ˈoʊ.əˌplæst/", "noãn cầu non; tế bào trứng sơ khai"),
    "lex.en.100k.097094": ("oops", "intj", "/uːps/", "úi chà; ôi chết rồi (lỡ tay)"),
    "lex.en.100k.097095": ("oosperm", "noun", "/ˈoʊ.əˌspɝːm/", "trứng đã thụ tinh; hợp tử noãn"),
    "lex.en.100k.097096": ("oosphere", "noun", "/ˈoʊ.əˌsfɪr/", "noãn cầu chưa thụ tinh"),
    "lex.en.100k.097097": ("oosporangium", "noun", "/ˌoʊ.ə.spəˈræn.dʒi.əm/", "túi sinh noãn bào tử"),
    "lex.en.100k.097098": ("oospore", "noun", "/ˈoʊ.əˌspɔːr/", "noãn bào tử; bào tử thụ tinh"),
    "lex.en.100k.097099": ("ootheca", "noun", "/ˌoʊ.əˈθiː.kə/", "ổ bọc trứng dán hoặc bọ ngựa"),
    "lex.en.100k.097100": ("oothecae", "noun", "/ˌoʊ.əˈθiː.siː/", "các ổ bọc trứng côn trùng"),
    "lex.en.100k.097101": ("oothecal", "adj", "/ˌoʊ.əˈθiː.kəl/", "thuộc ổ bọc trứng côn trùng"),
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
