import json
import re

# Batch 20 Round 5 Part 2 (097102 to 097201, 100 records)
# Fully manual cognitive translation & QA review

raw_file = "scratch/b20_r05_raw_p2.json"
out_file = "scratch/b20_r05_p2.json"

with open(raw_file, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100, f"Expected 100 records, got {len(raw_data)}"

reviewed = {
    "lex.en.100k.097102": ("ootid", "noun", "/ˈoʊ.ə.tɪd/", "noãn tử; tế bào trứng chín"),
    "lex.en.100k.097103": ("ootocoid", "adj", "/oʊˈɑː.təˌkɔɪd/", "sinh con kèm túi noãn; noãn thai"),
    "lex.en.100k.097104": ("ootocous", "adj", "/oʊˈɑː.tə.kəs/", "đẻ trứng; sinh sản bằng trứng"),
    "lex.en.100k.097105": ("ootype", "noun", "/ˈoʊ.əˌtaɪp/", "thất noãn (ở giun sán)"),
    "lex.en.100k.097106": ("oozed", "verb", "/uːzd/", "đã rỉ ra; đã ứa ra; đã rỉ nước"),
    "lex.en.100k.097107": ("oozes", "verb", "/ˈuː.zɪz/", "rỉ ra; ứa ra; rỉ dịch"),
    "lex.en.100k.097108": ("ooziness", "noun", "/ˈuː.zi.nəs/", "sự rỉ nước; tính lầy lội bùn"),
    "lex.en.100k.097109": ("oozoite", "noun", "/oʊˈɑː.zəˌwaɪt/", "cá thể sinh sản hữu tính"),
    "lex.en.100k.097110": ("oozooid", "noun", "/oʊˈɑː.zəˌwɔɪd/", "cá thể noãn sinh (động vật bọt)"),
    "lex.en.100k.097111": ("op", "noun", "/ɑːp/", "cuộc mổ; chiến dịch (viết tắt)"),
    "lex.en.100k.097112": ("opacify", "verb", "/oʊˈpæs.ə.faɪ/", "làm mờ đục; làm mất độ trong"),
    "lex.en.100k.097113": ("opalesce", "verb", "/ˌoʊ.pəˈles/", "ánh lên sắc ngọc mắt mèo"),
    "lex.en.100k.097114": ("opalesque", "adj", "/ˌoʊ.pəˈlesk/", "óng ánh như ngọc mắt mèo"),
    "lex.en.100k.097115": ("opalise", "verb", "/ˈoʊ.pə.laɪz/", "hóa ngọc opal; làm óng ánh"),
    "lex.en.100k.097116": ("opalize", "verb", "/ˈoʊ.pə.laɪz/", "hóa ngọc opal; làm óng ánh"),
    "lex.en.100k.097117": ("opaques", "noun", "/oʊˈpeɪks/", "vật thể mờ đục; chất chắn sáng"),
    "lex.en.100k.097118": ("ope", "verb", "/oʊp/", "mở ra (dạng thơ cổ của open)"),
    "lex.en.100k.097119": ("oped", "verb", "/oʊpt/", "đã mở ra (dạng thơ cổ)"),
    "lex.en.100k.097120": ("openable", "adj", "/ˈoʊ.pən.ə.bəl/", "có thể mở được; có nắp mở"),
    "lex.en.100k.097121": ("openbill", "noun", "/ˈoʊ.pənˌbɪl/", "cò nhạn; cò mỏ hở Anastomus"),
    "lex.en.100k.097122": ("opencut", "adj", "/ˈoʊ.pənˌkʌt/", "khai thác mỏ lộ thiên"),
    "lex.en.100k.097123": ("openhanded", "adj", "/ˌoʊ.pənˈhæn.dɪd/", "rộng rãi; hào phóng; độ lượng"),
    "lex.en.100k.097124": ("openhandedness", "noun", "/ˌoʊ.pənˈhæn.dɪd.nəs/", "tính rộng lượng; sự hào phóng"),
    "lex.en.100k.097125": ("openmouthed", "adj", "/ˌoʊ.pənˈmaʊðd/", "há hốc mồm ngạc nhiên; sửng sốt"),
    "lex.en.100k.097126": ("opens", "verb", "/ˈoʊ.pənz/", "mở ra; khai trương; bắt đầu"),
    "lex.en.100k.097127": ("opepe", "noun", "/oʊˈpeɪ.peɪ/", "cây gỗ bilinga Opepe châu Phi"),
    "lex.en.100k.097128": ("operability", "noun", "/ˌɑː.pɚ.əˈbɪl.ə.t̬i/", "khả năng mổ được; tính khả thi"),
    "lex.en.100k.097129": ("operagoer", "noun", "/ˈɑː.prəˌɡoʊ.ɚ/", "người thường đi xem opera"),
    "lex.en.100k.097130": ("operants", "noun", "/ˈɑː.pɚ.ənts/", "phản xạ có điều kiện hành vi"),
    "lex.en.100k.097131": ("operationalism", "noun", "/ˌɑː.pɚˈeɪ.ʃən.əl.ɪ.zəm/", "chủ nghĩa thao tác luận"),
    "lex.en.100k.097132": ("operationalist", "noun", "/ˌɑː.pɚˈeɪ.ʃən.əl.ɪst/", "người theo chủ nghĩa thao tác"),
    "lex.en.100k.097133": ("operationalize", "verb", "/ˌɑː.pɚˈeɪ.ʃən.əl.aɪz/", "thao tác hóa; cụ thể hóa"),
    "lex.en.100k.097134": ("operatise", "verb", "/ˈɑː.pɚ.ə.taɪz/", "chuyển soạn thành nhạc kịch"),
    "lex.en.100k.097135": ("operatize", "verb", "/ˈɑː.pɚ.ə.taɪz/", "chuyển soạn thành nhạc kịch opera"),
    "lex.en.100k.097136": ("opercula", "noun", "/oʊˈpɝː.kjə.lə/", "các nắp mang cá; vảy nắp vỏ ốc"),
    "lex.en.100k.097137": ("opercular", "adj", "/oʊˈpɝː.kjə.lɚ/", "thuộc nắp mang cá; thuộc nắp vảy"),
    "lex.en.100k.097138": ("operculated", "adj", "/oʊˈpɝː.kjə.leɪ.t̬ɪd/", "có nắp đậy; có vảy nắp đậy"),
    "lex.en.100k.097139": ("operculation", "noun", "/oʊˌpɝː.kjəˈleɪ.ʃən/", "sự hình thành nắp mang; nắp đậy"),
    "lex.en.100k.097140": ("operculiform", "adj", "/oʊˈpɝː.kjə.ləˌfɔːrm/", "có hình dạng chiếc nắp đậy"),
    "lex.en.100k.097141": ("operculigenous", "adj", "/oʊˌpɝː.kjəˈlɪdʒ.ə.nəs/", "sinh ra nắp đậy (thực vật)"),
    "lex.en.100k.097142": ("operettist", "noun", "/ˌɑː.pəˈret̬.ɪst/", "nhà soạn nhạc kịch ngắn operet"),
    "lex.en.100k.097143": ("operose", "adj", "/ˈɑː.pɚ.oʊs/", "tốn nhiều công phu; vất vả"),
    "lex.en.100k.097144": ("operoseness", "noun", "/ˈɑː.pɚ.oʊs.nəs/", "tính chất tốn nhiều công sức"),
    "lex.en.100k.097145": ("opes", "verb", "/oʊps/", "mở ra (dạng thơ cổ ngôi 3)"),
    "lex.en.100k.097146": ("opheodrys", "noun", "/oʊˈfiː.oʊ.drɪs/", "chi rắn lục Opheodrys Bắc Mỹ"),
    "lex.en.100k.097147": ("ophidiidae", "noun", "/ˌoʊ.fɪˈdaɪ.ɪ.diː/", "họ cá chồn Ophidiidae"),
    "lex.en.100k.097148": ("ophidism", "noun", "/ˈoʊ.fɪ.dɪ.zəm/", "chứng trúng độc nọc độc rắn"),
    "lex.en.100k.097149": ("ophiocephalous", "adj", "/ˌoʊ.fi.oʊˈsef.ə.ləs/", "có hình dạng đầu giống rắn"),
    "lex.en.100k.097150": ("ophiodon", "noun", "/ˌoʊ.fiˈoʊ.dɑːn/", "chi cá răng rắn Ophiodon"),
    "lex.en.100k.097151": ("ophiodontidae", "noun", "/ˌoʊ.fi.oʊˈdɑːn.tə.diː/", "họ cá linh Ophiodontidae"),
    "lex.en.100k.097152": ("ophioglossaceae", "noun", "/ˌoʊ.fi.oʊ.ɡlɑːˈseɪ.siː/", "họ dương xỉ Lưỡi rắn"),
    "lex.en.100k.097153": ("ophioglossales", "noun", "/ˌoʊ.fi.oʊ.ɡlɑːˈseɪ.liːz/", "bộ dương xỉ Lưỡi rắn"),
    "lex.en.100k.097154": ("ophioglossum", "noun", "/ˌoʊ.fi.oʊˈɡlɑː.səm/", "chi dương xỉ Lưỡi rắn"),
    "lex.en.100k.097155": ("ophiolater", "noun", "/ˌoʊ.fiˈɑː.lə.tɚ/", "người tôn sùng thờ cúng loài rắn"),
    "lex.en.100k.097156": ("ophiolatrous", "adj", "/ˌoʊ.fiˈɑː.lə.trəs/", "thuộc tín ngưỡng sùng bái rắn"),
    "lex.en.100k.097157": ("ophiolatry", "noun", "/ˌoʊ.fiˈɑː.lə.tri/", "tục sùng bái loài rắn"),
    "lex.en.100k.097158": ("ophiologic", "adj", "/ˌoʊ.fi.əˈlɑː.dʒɪk/", "thuộc khoa nghiên cứu loài rắn"),
    "lex.en.100k.097159": ("ophiological", "adj", "/ˌoʊ.fi.əˈlɑː.dʒɪk.əl/", "thuộc môn nghiên cứu loài rắn"),
    "lex.en.100k.097160": ("ophiologist", "noun", "/ˌoʊ.fiˈɑː.lə.dʒɪst/", "nhà nghiên cứu về loài rắn"),
    "lex.en.100k.097161": ("ophiology", "noun", "/ˌoʊ.fiˈɑː.lə.dʒi/", "khoa nghiên cứu chuyên về loài rắn"),
    "lex.en.100k.097162": ("ophiomorphous", "adj", "/ˌoʊ.fi.oʊˈmɔːr.fəs/", "có dạng uốn lượn giống loài rắn"),
    "lex.en.100k.097163": ("ophiophagous", "adj", "/ˌoʊ.fiˈɑː.fə.ɡəs/", "chuyên ăn thịt các loài rắn"),
    "lex.en.100k.097164": ("ophiophagus", "noun", "/ˌoʊ.fiˈɑː.fə.ɡəs/", "chi rắn hổ mang chúa"),
    "lex.en.100k.097165": ("ophisaurus", "noun", "/ˌoʊ.fɪˈsɔːr.əs/", "chi thằn lằn không chân"),
    "lex.en.100k.097166": ("ophite", "noun", "/ˈoʊ.faɪt/", "đá ofit; tín đồ phái thờ rắn"),
    "lex.en.100k.097167": ("ophitic", "adj", "/oʊˈfɪt̬.ɪk/", "có cấu trúc tinh thể đá ofit"),
    "lex.en.100k.097168": ("ophitism", "noun", "/ˈoʊ.fɪ.tɪ.zəm/", "giáo phái thờ rắn Ophites"),
    "lex.en.100k.097169": ("ophiurida", "noun", "/ˌoʊ.fiˈjʊər.ɪ.də/", "bộ Sao biển đuôi rắn Ophiurida"),
    "lex.en.100k.097170": ("ophiuroid", "adj", "/ˌoʊ.fiˈjʊər.ɔɪd/", "thuộc lớp sao biển đuôi rắn"),
    "lex.en.100k.097171": ("ophiuroidea", "noun", "/ˌoʊ.fi.jʊˈrɔɪ.di.ə/", "lớp Sao biển đuôi rắn"),
    "lex.en.100k.097172": ("ophryon", "noun", "/ˈɑː.fri.ɑːn/", "điểm trán giữa hai lông mày"),
    "lex.en.100k.097173": ("ophthalmectomy", "noun", "/ˌɑːf.θælˈmek.tə.mi/", "phẫu thuật khoét bỏ nhãn cầu mắt"),
    "lex.en.100k.097174": ("ophthalmitis", "noun", "/ˌɑːf.θælˈmaɪ.t̬ɪs/", "chứng viêm toàn bộ nhãn cầu"),
    "lex.en.100k.097175": ("ophthalmocele", "noun", "/ɑːfˈθæl.məˌsiːl/", "chứng lồi nhãn cầu mắt"),
    "lex.en.100k.097176": ("ophthalmogyric", "adj", "/ˌɑːf.θæl.moʊˈdʒaɪ.rɪk/", "làm vận nhãn; làm đảo mắt"),
    "lex.en.100k.097177": ("ophthalmological", "adj", "/ˌɑːf.θæl.məˈlɑː.dʒɪk.əl/", "thuộc chuyên khoa nhãn khoa"),
    "lex.en.100k.097178": ("ophthalmoscopic", "adj", "/ˌɑːf.θæl.məˈskɑː.pɪk/", "thuộc kỹ thuật soi đáy mắt"),
    "lex.en.100k.097179": ("ophthalmotomy", "noun", "/ˌɑːf.θælˈmɑː.tə.mi/", "thủ thuật rạch mở nhãn cầu mắt"),
    "lex.en.100k.097180": ("opined", "verb", "/oʊˈpaɪnd/", "đã phát biểu ý kiến; đã cho rằng"),
    "lex.en.100k.097181": ("opines", "verb", "/oʊˈpaɪnz/", "phát biểu ý kiến; cho rằng"),
    "lex.en.100k.097182": ("oping", "verb", "/ˈoʊ.pɪŋ/", "đang mở ra (dạng thơ cổ)"),
    "lex.en.100k.097183": ("opining", "verb", "/oʊˈpaɪ.nɪŋ/", "đang bày tỏ quan điểm; nhận định"),
    "lex.en.100k.097184": ("opinionable", "adj", "/əˈpɪn.jən.ə.bəl/", "có thể gây tranh cãi ý kiến"),
    "lex.en.100k.097185": ("opinionatedness", "noun", "/əˈpɪn.jə.neɪ.t̬ɪd.nəs/", "tính bảo thủ; sự độc đoán ý kiến"),
    "lex.en.100k.097186": ("opinionative", "adj", "/əˈpɪn.jə.neɪ.t̬ɪv/", "ngoan cố; khăng khăng ý mình"),
    "lex.en.100k.097187": ("opinionatively", "adv", "/əˈpɪn.jə.neɪ.t̬ɪv.li/", "một cách ngoan cố; độc đoán"),
    "lex.en.100k.097188": ("opinionativeness", "noun", "/əˈpɪn.jə.neɪ.t̬ɪv.nəs/", "thói ngoan cố cố chấp ý kiến"),
    "lex.en.100k.097189": ("opinionist", "noun", "/əˈpɪn.jən.ɪst/", "người cố chấp bảo thủ quan điểm"),
    "lex.en.100k.097190": ("opioid", "noun", "/ˈoʊ.pi.ɔɪd/", "chất giảm đau opioid; thuốc opioid"),
    "lex.en.100k.097191": ("opioids", "noun", "/ˈoʊ.pi.ɔɪdz/", "các thuốc giảm đau nhóm opioid"),
    "lex.en.100k.097192": ("opisometer", "noun", "/ˌɑː.pəˈsɑː.mə.t̬ɚ/", "dụng cụ đo độ dài đường cong"),
    "lex.en.100k.097193": ("opisthbranch", "noun", "/oʊˈpɪs.θə.bræŋk/", "động vật thân mềm mang sau"),
    "lex.en.100k.097194": ("opisthobranchia", "noun", "/oʊˌpɪs.θoʊˈbræŋ.ki.ə/", "phân lớp thân mềm mang sau"),
    "lex.en.100k.097195": ("opisthocomidae", "noun", "/oʊˌpɪs.θəˈkɑː.mɪ.diː/", "họ chim hoatzin Opisthocomidae"),
    "lex.en.100k.097196": ("opisthocomus", "noun", "/oʊˌpɪsˈθɑː.kə.məs/", "chi chim hoatzin Opisthocomus"),
    "lex.en.100k.097197": ("opisthodome", "noun", "/oʊˈpɪs.θə.doʊm/", "hậu sảnh đền thờ Hy Lạp cổ"),
    "lex.en.100k.097198": ("opisthoglypha", "noun", "/ˌoʊ.pɪsˈθɑː.ɡlə.fə/", "nhóm rắn có răng nanh sau"),
    "lex.en.100k.097199": ("opisthognathidae", "noun", "/ˌoʊ.pɪs.θɑːɡˈnæθ.ɪ.diː/", "họ cá hàm Opisthognathidae"),
    "lex.en.100k.097200": ("opisthognathous", "adj", "/ˌoʊ.pɪsˈθɑːɡ.nə.θəs/", "có hàm dưới thụt sâu vào trong"),
    "lex.en.100k.097201": ("opisthograph", "noun", "/oʊˈpɪs.θə.ɡræf/", "bản thảo cổ viết trên cả hai mặt"),
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
