import json
import re

# Batch 20 Round 5 Part 3 (097202 to 097301, 100 records)
# Fully manual cognitive translation & QA review

raw_file = "scratch/b20_r05_raw_p3.json"
out_file = "scratch/b20_r05_p3.json"

with open(raw_file, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100, f"Expected 100 records, got {len(raw_data)}"

reviewed = {
    "lex.en.100k.097202": ("opisthorchiasis", "noun", "/ˌoʊ.pɪs.θɔːrˈkaɪ.ə.sɪs/", "bệnh nhiễm sán lá gan Opisthorchis"),
    "lex.en.100k.097203": ("opisthotic", "adj", "/ˌoʊ.pɪsˈθɑː.tɪk/", "thuộc xương tai sau"),
    "lex.en.100k.097204": ("opisthotonos", "noun", "/ˌoʊ.pɪsˈθɑː.tə.nəs/", "chứng ưỡn cong người do co giật"),
    "lex.en.100k.097205": ("opiumism", "noun", "/ˈoʊ.pi.ə.mɪ.zəm/", "chứng nghiện thuốc phiện; ngộ độc"),
    "lex.en.100k.097206": ("opiums", "noun", "/ˈoʊ.pi.əmz/", "các chế phẩm từ thuốc phiện"),
    "lex.en.100k.097207": ("opodeldoc", "noun", "/ˌɑː.pəˈdel.dɑːk/", "cao xoa bóp giảm đau opodeldoc"),
    "lex.en.100k.097208": ("opopanax", "noun", "/oʊˈpɑː.pə.næks/", "nhựa thơm ngọt opopanax"),
    "lex.en.100k.097209": ("opophilous", "adj", "/oʊˈpɑː.fə.ləs/", "ưa nhựa cây; sống nhờ nhựa cây"),
    "lex.en.100k.097210": ("opp", "adj", "/ɑːp/", "đối diện; ngược lại (viết tắt)"),
    "lex.en.100k.097211": ("oppidan", "noun", "/ˈɑː.pɪ.dən/", "học sinh ngoại trú ở trường Eton"),
    "lex.en.100k.097212": ("oppilate", "verb", "/ˈɑː.pəˌleɪt/", "làm tắc nghẽn; làm ứ tắc"),
    "lex.en.100k.097213": ("oppilation", "noun", "/ˌɑː.pəˈleɪ.ʃən/", "sự tắc nghẽn; tình trạng ứ tắc"),
    "lex.en.100k.097214": ("opponency", "noun", "/əˈpoʊ.nən.si/", "sự đối lập; tính chất đối kháng"),
    "lex.en.100k.097215": ("opponens", "noun", "/əˈpoʊ.nənz/", "cơ đối chiếu (ngón cái hoặc út)"),
    "lex.en.100k.097216": ("opportuneness", "noun", "/ˈɑː.pɚ.tuːn.nəs/", "tính đúng lúc; sự hợp thời điểm"),
    "lex.en.100k.097217": ("opposability", "noun", "/əˌpoʊ.zəˈbɪl.ə.t̬i/", "khả năng đối chiếu của ngón cái"),
    "lex.en.100k.097218": ("opposeless", "adj", "/əˈpoʊz.ləs/", "không thể chống lại; bất khả kháng"),
    "lex.en.100k.097219": ("opposes", "verb", "/əˈpoʊ.zɪz/", "chống đối; phản đối; đối kháng"),
    "lex.en.100k.097220": ("oppositeness", "noun", "/ˈɑː.pə.zɪt.nəs/", "tính đối diện; sự tương phản"),
    "lex.en.100k.097221": ("opposites", "noun", "/ˈɑː.pə.zɪts/", "những mặt đối lập; vật trái ngược"),
    "lex.en.100k.097222": ("oppositifoliate", "adj", "/əˌpɑː.zə.t̬əˈfoʊ.li.eɪt/", "có lá mọc đối xứng (thực vật)"),
    "lex.en.100k.097223": ("oppositifolious", "adj", "/əˌpɑː.zə.t̬əˈfoʊ.li.əs/", "có lá mọc đối xứng qua thân"),
    "lex.en.100k.097224": ("oppositional", "adj", "/ˌɑː.pəˈzɪʃ.ən.əl/", "mang tính chống đối; tính đối lập"),
    "lex.en.100k.097225": ("oppositionist", "noun", "/ˌɑː.pəˈzɪʃ.ən.ɪst/", "thành viên phe đối lập chính trị"),
    "lex.en.100k.097226": ("oppositive", "adj", "/əˈpɑː.zə.t̬ɪv/", "mang tính đối lập; tương phản"),
    "lex.en.100k.097227": ("oppresses", "verb", "/əˈpres.ɪz/", "áp bức; đè nặng; làm trĩu nặng"),
    "lex.en.100k.097228": ("oppressing", "verb", "/əˈpres.ɪŋ/", "đang áp bức; đang đè nặng tâm trí"),
    "lex.en.100k.097229": ("opprobriously", "adv", "/əˈproʊ.bri.əs.li/", "một cách sỉ nhục; đầy lăng mạ"),
    "lex.en.100k.097230": ("oppugn", "verb", "/əˈpjuːn/", "công kích; phản bác mạnh mẽ"),
    "lex.en.100k.097231": ("oppugnance", "noun", "/əˈpʌɡ.nəns/", "sự công kích; tinh thần phản kháng"),
    "lex.en.100k.097232": ("oppugnancy", "noun", "/əˈpʌɡ.nən.si/", "tính chất công kích; sự chống đối"),
    "lex.en.100k.097233": ("oppugnant", "adj", "/əˈpʌɡ.nənt/", "có tính công kích; mang phản kháng"),
    "lex.en.100k.097234": ("oppugnantion", "noun", "/ˌɑː.pəɡˈneɪ.ʃən/", "sự phản bác; hành động công kích"),
    "lex.en.100k.097235": ("opsimath", "noun", "/ˈɑːp.sɪ.mæθ/", "người về già mới bắt đầu học hành"),
    "lex.en.100k.097236": ("opsimathy", "noun", "/ɑːpˈsɪm.ə.θi/", "việc học hành khi đã về già"),
    "lex.en.100k.097237": ("opsonic", "adj", "/ɑːpˈsɑː.nɪk/", "thuộc opsonin; có tác dụng opsonin"),
    "lex.en.100k.097238": ("opsonification", "noun", "/ɑːpˌsɑː.nə.fəˈkeɪ.ʃən/", "quá trình opsonin hóa miễn dịch"),
    "lex.en.100k.097239": ("opsonify", "verb", "/ɑːpˈsɑː.nə.faɪ/", "làm cho bị opsonin hóa"),
    "lex.en.100k.097240": ("opsonin", "noun", "/ˈɑːp.sə.nɪn/", "kháng thể opsonin hỗ trợ thực bào"),
    "lex.en.100k.097241": ("opsonisation", "noun", "/ˌɑːp.sə.naɪˈzeɪ.ʃən/", "quá trình opsonin hóa tế bào"),
    "lex.en.100k.097242": ("opsonise", "verb", "/ˈɑːp.sə.naɪz/", "gắn opsonin; opsonin hóa vi khuẩn"),
    "lex.en.100k.097243": ("opsonization", "noun", "/ˌɑːp.sə.nəˈzeɪ.ʃən/", "hiện tượng opsonin hóa miễn dịch"),
    "lex.en.100k.097244": ("opsonize", "verb", "/ˈɑːp.sə.naɪz/", "gắn opsonin hỗ trợ thực bào"),
    "lex.en.100k.097245": ("optant", "noun", "/ˈɑːp.tənt/", "người chọn quốc tịch theo hiệp ước"),
    "lex.en.100k.097246": ("opted", "verb", "/ˈɑːp.tɪd/", "đã lựa chọn; đã quyết định chọn"),
    "lex.en.100k.097247": ("optez", "noun", "/ˈɑːp.tez/", "tiếng Optez (ngôn ngữ bản địa)"),
    "lex.en.100k.097248": ("opticator", "noun", "/ˈɑːp.tɪˌkeɪ.t̬ɚ/", "bộ chỉ thị quang học; dụng cụ ngắm"),
    "lex.en.100k.097249": ("opticist", "noun", "/ˈɑːp.tɪ.sɪst/", "chuyên gia quang học"),
    "lex.en.100k.097250": ("optimality", "noun", "/ˌɑːp.təˈmæl.ə.t̬i/", "tính tối ưu; trạng thái tối hảo"),
    "lex.en.100k.097251": ("optimate", "noun", "/ˈɑːp.tə.mət/", "tầng lớp quý tộc La Mã cổ đại"),
    "lex.en.100k.097252": ("optime", "noun", "/ˈɑːp.tɪ.mi/", "thí sinh đỗ hạng ưu toán Cambridge"),
    "lex.en.100k.097253": ("optimised", "verb", "/ˈɑːp.tə.maɪzd/", "đã tối ưu hóa; đã tinh chỉnh"),
    "lex.en.100k.097254": ("optimises", "verb", "/ˈɑːp.tə.maɪ.zɪz/", "tối ưu hóa; nâng cao hiệu suất"),
    "lex.en.100k.097255": ("optimising", "verb", "/ˈɑːp.tə.maɪ.zɪŋ/", "đang tối ưu hóa; tinh giản tối đa"),
    "lex.en.100k.097256": ("optimizer", "noun", "/ˈɑːp.tə.maɪ.zɚ/", "trình tối ưu hóa; bộ tinh chỉnh"),
    "lex.en.100k.097257": ("opting", "verb", "/ˈɑːp.tɪŋ/", "đang lựa chọn; đang quyết định chọn"),
    "lex.en.100k.097258": ("optocoel", "noun", "/ˈɑːp.təˌsiːl/", "khoang não thị giác (ở phôi thai)"),
    "lex.en.100k.097259": ("optoelectronics", "noun", "/ˌɑːp.toʊ.ɪˌlekˈtrɑː.nɪks/", "ngành quang điện tử học"),
    "lex.en.100k.097260": ("optogram", "noun", "/ˈɑːp.təˌɡræm/", "hình ảnh in trên võng mạc mắt"),
    "lex.en.100k.097261": ("optometer", "noun", "/ɑːpˈtɑː.mə.t̬ɚ/", "máy đo thị lực mắt; máy kiểm tra"),
    "lex.en.100k.097262": ("optometrists", "noun", "/ɑːpˈtɑː.mə.trɪsts/", "các chuyên viên đo khúc xạ mắt"),
    "lex.en.100k.097263": ("optophone", "noun", "/ˈɑːp.təˌfoʊn/", "máy quét chữ thành âm cho người mù"),
    "lex.en.100k.097264": ("opts", "verb", "/ɑːpts/", "lựa chọn; quyết định chọn"),
    "lex.en.100k.097265": ("opuntiales", "noun", "/oʊˌpʌn.ʃiˈeɪ.liːz/", "bộ Xương rồng Opuntiales"),
    "lex.en.100k.097266": ("opuscule", "noun", "/oʊˈpʌs.kjuːl/", "tác phẩm văn học nhỏ; tiểu phẩm"),
    "lex.en.100k.097267": ("ora", "noun", "/ˈɔːr.ə/", "các miệng; các lỗ mở giải phẫu"),
    "lex.en.100k.097268": ("orache", "noun", "/ˈɔːr.ətʃ/", "cây rau muối biển Atriplex"),
    "lex.en.100k.097269": ("oracularity", "noun", "/ɔːˌræk.jəˈler.ə.t̬i/", "tính chất sấm truyền; vẻ bí ẩn"),
    "lex.en.100k.097270": ("orad", "adv", "/ˈɔːr.æd/", "hướng về phía khoang miệng"),
    "lex.en.100k.097271": ("oradexon", "noun", "/ˌɔːr.əˈdek.sɑːn/", "thuốc dexamethasone kháng viêm"),
    "lex.en.100k.097272": ("orals", "noun", "/ˈɔːr.əlz/", "các kỳ thi vấn đáp; thuốc uống"),
    "lex.en.100k.097273": ("orangeness", "noun", "/ˈɔːr.ɪndʒ.nəs/", "sắc cam; màu da cam"),
    "lex.en.100k.097274": ("orangutang", "noun", "/ɔːˈræŋ.uːˌtæŋ/", "đười ươi Orangutan"),
    "lex.en.100k.097275": ("orangy", "adj", "/ˈɔːr.ɪn.dʒi/", "hơi có màu cam; phảng phất cam"),
    "lex.en.100k.097276": ("orasone", "noun", "/ˈɔːr.əˌsoʊn/", "thuốc prednisone kháng viêm"),
    "lex.en.100k.097277": ("orated", "verb", "/ɔːˈreɪ.t̬ɪd/", "đã diễn thuyết; đã thuyết giảng"),
    "lex.en.100k.097278": ("orates", "verb", "/ɔːˈreɪts/", "diễn thuyết; thuyết giảng hoa mỹ"),
    "lex.en.100k.097279": ("orating", "verb", "/ɔːˈreɪ.t̬ɪŋ/", "đang diễn thuyết; đang hùng biện"),
    "lex.en.100k.097280": ("oratorically", "adv", "/ˌɔːr.əˈtɔːr.ɪ.kli/", "theo phong cách tài hùng biện"),
    "lex.en.100k.097281": ("oratorise", "verb", "/ˈɔːr.ə.tə.raɪz/", "thuyết giảng hoa mỹ; khua môi mép"),
    "lex.en.100k.097282": ("oratorize", "verb", "/ˈɔːr.ə.tə.raɪz/", "thuyết giảng hoa mỹ; diễn thuyết"),
    "lex.en.100k.097283": ("oratress", "noun", "/ˈɔːr.ə.trəs/", "nữ diễn giả; nữ nhà hùng biện"),
    "lex.en.100k.097284": ("oratrix", "noun", "/ˈɔːr.ə.trɪks/", "nữ diễn giả; người nữ khởi kiện"),
    "lex.en.100k.097285": ("orbicularis", "noun", "/ˌɔːr.bɪk.jəˈler.ɪs/", "cơ vòng quanh mắt hoặc quanh miệng"),
    "lex.en.100k.097286": ("orbicularity", "noun", "/ˌɔːr.bɪk.jəˈler.ə.t̬i/", "tính chất tròn vo; dạng hình cầu"),
    "lex.en.100k.097287": ("orbiculate", "adj", "/ɔːrˈbɪk.jə.lət/", "có dạng hình tròn; dẹt tròn"),
    "lex.en.100k.097288": ("orbignya", "noun", "/ɔːrˈbɪn.jə/", "chi cọ dầu Babassu Orbignya"),
    "lex.en.100k.097289": ("orbitale", "noun", "/ˌɔːr.bɪˈteɪ.li/", "điểm thấp nhất bờ ổ mắt"),
    "lex.en.100k.097290": ("orbited", "verb", "/ˈɔːr.bɪ.t̬ɪd/", "đã bay quanh quỹ đạo; quay quanh"),
    "lex.en.100k.097291": ("orbiting", "verb", "/ˈɔːr.bɪ.t̬ɪŋ/", "đang bay quanh quỹ đạo; xoay quanh"),
    "lex.en.100k.097292": ("orbitomalar", "adj", "/ˌɔːr.bɪ.toʊˈmeɪ.lɚ/", "thuộc ổ mắt và xương gò má"),
    "lex.en.100k.097293": ("orbitonasal", "adj", "/ˌɔːr.bɪ.toʊˈneɪ.zəl/", "thuộc ổ mắt và khoang mũi"),
    "lex.en.100k.097294": ("orbits", "verb", "/ˈɔːr.bɪts/", "quay quanh quỹ đạo; di chuyển quanh"),
    "lex.en.100k.097295": ("orbitual", "adj", "/ɔːrˈbɪtʃ.u.əl/", "thuộc quỹ đạo mắt; thuộc đường quay"),
    "lex.en.100k.097296": ("orc", "noun", "/ɔːrk/", "quái vật orc; loài cá voi sát thủ"),
    "lex.en.100k.097297": ("orcadian", "noun", "/ɔːrˈkeɪ.di.ən/", "người dân quần đảo Orkney Scotland"),
    "lex.en.100k.097298": ("orch", "noun", "/ɔːrtʃ/", "dàn nhạc giao hưởng (viết tắt)"),
    "lex.en.100k.097299": ("orcharding", "noun", "/ˈɔːr.tʃɚ.dɪŋ/", "nghề trồng trọt vườn cây ăn quả"),
    "lex.en.100k.097300": ("orchardist", "noun", "/ˈɔːr.tʃɚ.dɪst/", "chủ trang trại vườn cây ăn quả"),
    "lex.en.100k.097301": ("orchardists", "noun", "/ˈɔːr.tʃɚ.dɪsts/", "các chủ trang trại cây ăn trái"),
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
