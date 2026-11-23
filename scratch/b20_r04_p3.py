import json
import re

# Batch 20 Round 4 Part 3 (096702 to 096801, 100 records)
# Fully manual cognitive translation & QA review

raw_file = "scratch/b20_r04_raw_p3.json"
out_file = "scratch/b20_r04_p3.json"

with open(raw_file, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100, f"Expected 100 records, got {len(raw_data)}"

reviewed = {
    "lex.en.100k.096702": ("oedematin", "noun", "/iːˈdem.ə.tɪn/", "chất oedematin; chất đệm nhân"),
    "lex.en.100k.096703": ("oedematose", "adj", "/ɪˈdem.ə.toʊs/", "phù thũng; sưng phù nề"),
    "lex.en.100k.096704": ("oedematous", "adj", "/ɪˈdem.ə.t̬əs/", "bị phù nề; phù thũng"),
    "lex.en.100k.096705": ("oedipal", "adj", "/ˈed.ə.pəl/", "thuộc mặc cảm Oedipus"),
    "lex.en.100k.096706": ("oedipally", "adv", "/ˈed.ə.pə.li/", "theo mặc cảm Oedipus"),
    "lex.en.100k.096707": ("oedogoniaceae", "noun", "/ˌiː.də.ɡoʊ.niˈeɪ.siː/", "họ Tảo sợi Oedogoniaceae"),
    "lex.en.100k.096708": ("oedogoniales", "noun", "/ˌiː.də.ɡoʊ.niˈeɪ.liːz/", "bộ Tảo sợi Oedogoniales"),
    "lex.en.100k.096709": ("oedogonium", "noun", "/ˌiː.dəˈɡoʊ.ni.əm/", "chi tảo sợi Oedogonium"),
    "lex.en.100k.096710": ("oeillade", "noun", "/eɪˈjɑːd/", "cái liếc mắt đưa tình; mắt đong đưa"),
    "lex.en.100k.096711": ("oelotrophic", "adj", "/ˌiː.loʊˈtrɑː.fɪk/", "dị hướng; tính không đẳng hướng"),
    "lex.en.100k.096712": ("oenanthic", "adj", "/iːˈnæn.θɪk/", "thuộc hương rượu vang"),
    "lex.en.100k.096713": ("oenanthylic", "adj", "/ˌiː.nænˈθɪl.ɪk/", "axit enanthic; thuộc enanthic"),
    "lex.en.100k.096714": ("oengus", "noun", "/ˈeɪŋ.ɡəs/", "thần tình yêu Oengus của Celt"),
    "lex.en.100k.096715": ("oenological", "adj", "/ˌiː.nəˈlɑː.dʒɪk.əl/", "thuộc khoa nghiên cứu rượu vang"),
    "lex.en.100k.096716": ("oenomania", "noun", "/ˌiː.noʊˈmeɪ.ni.ə/", "chứng cuồng rượu vang"),
    "lex.en.100k.096717": ("oenomel", "noun", "/ˈiː.nəˌmel/", "rượu vang pha mật ong"),
    "lex.en.100k.096718": ("oenophilist", "noun", "/iːˈnɑː.fə.lɪst/", "người sành rượu vang"),
    "lex.en.100k.096719": ("oesophageal", "adj", "/ɪˌsɑː.fəˈdʒiː.əl/", "thuộc thực quản"),
    "lex.en.100k.096720": ("oesophagi", "noun", "/ɪˈsɑː.fə.dʒaɪ/", "các ống thực quản"),
    "lex.en.100k.096721": ("oesophagitis", "noun", "/ɪˌsɑː.fəˈdʒaɪ.t̬ɪs/", "chứng viêm thực quản"),
    "lex.en.100k.096722": ("oesophagoscope", "noun", "/ɪˈsɑː.fə.ɡəˌskoʊp/", "ống soi thực quản"),
    "lex.en.100k.096723": ("oestrin", "noun", "/ˈes.trɪn/", "chất oestrin; hoóc-môn sinh dục"),
    "lex.en.100k.096724": ("oestriol", "noun", "/ˈes.tri.ɑːl/", "chất estriol; hoóc-môn estrogen"),
    "lex.en.100k.096725": ("oestrogenic", "adj", "/ˌes.trəˈdʒen.ɪk/", "thuộc estrogen; kích thích động dục"),
    "lex.en.100k.096726": ("oestrogenically", "adv", "/ˌes.trəˈdʒen.ɪ.kli/", "theo kiểu hoóc-môn estrogen"),
    "lex.en.100k.096727": ("oestrone", "noun", "/ˈes.troʊn/", "chất estrone; hoóc-môn estrogen"),
    "lex.en.100k.096728": ("oestrous", "adj", "/ˈes.trəs/", "đang động dục; thời kỳ động dục"),
    "lex.en.100k.096729": ("oestruation", "noun", "/ˌes.truˈeɪ.ʃən/", "sự động dục; thời kỳ động dục"),
    "lex.en.100k.096730": ("oestrum", "noun", "/ˈes.trəm/", "thời kỳ động dục; cơn hưng phấn"),
    "lex.en.100k.096731": ("of", "prep", "/əv/", "của; thuộc về; làm bằng; từ"),
    "lex.en.100k.096732": ("ofay", "noun", "/ˈoʊ.feɪ/", "người da trắng"),
    "lex.en.100k.096733": ("offed", "verb", "/ˈɔːft/", "đã giết chết; đã khử"),
    "lex.en.100k.096734": ("offenceless", "adj", "/əˈfens.ləs/", "vô hại; không xúc phạm ai"),
    "lex.en.100k.096735": ("offendedly", "adv", "/əˈfen.dɪd.li/", "với vẻ phật ý; đầy phật lòng"),
    "lex.en.100k.096736": ("offends", "verb", "/əˈfendz/", "xúc phạm; làm mếch lòng; phạm tội"),
    "lex.en.100k.096737": ("offenseless", "adj", "/əˈfens.ləs/", "vô hại; không làm ai phật lòng"),
    "lex.en.100k.096738": ("offensives", "noun", "/əˈfen.sɪvz/", "các cuộc tấn công; cuộc công kích"),
    "lex.en.100k.096739": ("offered", "verb", "/ˈɑː.fɚd/", "đã đề nghị; đã hiến tặng"),
    "lex.en.100k.096740": ("offers", "verb", "/ˈɑː.fɚz/", "đề nghị; mời mọc; cung cấp"),
    "lex.en.100k.096741": ("offhandedness", "noun", "/ˌɑːfˈhæn.dɪd.nəs/", "tính thiếu suy nghĩ; sự tùy tiện"),
    "lex.en.100k.096742": ("officers", "noun", "/ˈɑː.fə.sɚz/", "các viên chức; các sĩ quan"),
    "lex.en.100k.096743": ("offices", "noun", "/ˈɑː.fɪ.sɪz/", "các văn phòng; các chức vụ"),
    "lex.en.100k.096744": ("officialese", "noun", "/əˌfɪʃ.əlˈiːz/", "văn phong công chức; lời quan liêu"),
    "lex.en.100k.096745": ("officialise", "verb", "/əˈfɪʃ.əl.aɪz/", "chính thức hóa; công nhận"),
    "lex.en.100k.096746": ("officialism", "noun", "/əˈfɪʃ.əl.ɪ.zəm/", "thói quan liêu; sự vụ hình thức"),
    "lex.en.100k.096747": ("officialize", "verb", "/əˈfɪʃ.əl.aɪz/", "chính thức hóa; công nhận"),
    "lex.en.100k.096748": ("officiary", "adj", "/əˈfɪʃ.i.er.i/", "thuộc chức vụ; thuộc quan chức"),
    "lex.en.100k.096749": ("officiated", "verb", "/əˈfɪʃ.i.eɪ.t̬ɪd/", "đã chủ trì; đã điều hành buổi lễ"),
    "lex.en.100k.096750": ("officiates", "verb", "/əˈfɪʃ.i.eɪts/", "chủ trì; điều hành buổi lễ"),
    "lex.en.100k.096751": ("officiation", "noun", "/əˌfɪʃ.iˈeɪ.ʃən/", "sự chủ trì buổi lễ; làm trọng tài"),
    "lex.en.100k.096752": ("officinal", "adj", "/əˈfɪs.ɪ.nəl/", "dùng làm thuốc; theo dược điển"),
    "lex.en.100k.096753": ("officinally", "adv", "/əˈfɪs.ɪ.nə.li/", "theo phép dược điển; làm thuốc"),
    "lex.en.100k.096754": ("officiousness", "noun", "/əˈfɪʃ.əs.nəs/", "tính thích săm soi; sự lăng xăng"),
    "lex.en.100k.096755": ("offishly", "adv", "/ˈɑː.fɪʃ.li/", "một cách lạnh nhạt; xa cách"),
    "lex.en.100k.096756": ("offishness", "noun", "/ˈɑː.fɪʃ.nəs/", "sự lạnh nhạt; tính cách biệt"),
    "lex.en.100k.096757": ("offs", "verb", "/ˈɑːfs/", "giết; thủ tiêu (từ lóng)"),
    "lex.en.100k.096758": ("offsaddle", "verb", "/ˌɑːfˈsæd.əl/", "tháo yên ngựa; cởi bỏ yên cương"),
    "lex.en.100k.096759": ("offscourings", "noun", "/ˈɑːfˌskaʊ.rɪŋz/", "cặn bã xã hội; đồ rác rưởi"),
    "lex.en.100k.096760": ("offspur", "noun", "/ˈɑːf.spɝː/", "nhánh núi phụ; mỏm đồi rẽ ngang"),
    "lex.en.100k.096761": ("offtake", "noun", "/ˈɑːf.teɪk/", "sản lượng tiêu thụ; đường ống rẽ"),
    "lex.en.100k.096762": ("oflag", "noun", "/ˈoʊ.flæɡ/", "trại tù binh sĩ quan Đức"),
    "lex.en.100k.096763": ("oftenness", "noun", "/ˈɑːf.ən.nəs/", "tần suất diễn ra; tính thường xuyên"),
    "lex.en.100k.096764": ("ogalala", "noun", "/ˌoʊ.ɡəˈlɑː.lə/", "người Oglala; bộ tộc Da đỏ Oglala"),
    "lex.en.100k.096765": ("ogam", "noun", "/ˈɑː.ɡəm/", "chữ Ogam khắc đá cổ Celt"),
    "lex.en.100k.096766": ("ogcocephalidae", "noun", "/ˌɑːk.koʊ.səˈfæl.ɪ.diː/", "họ Cá dơi Ogcocephalidae"),
    "lex.en.100k.096767": ("ogham", "noun", "/ˈɑː.ɡəm/", "chữ Ogham khắc cổ Celt"),
    "lex.en.100k.096768": ("ogival", "adj", "/oʊˈdʒaɪ.vəl/", "có hình cung nhọn; dạng vòm nhọn"),
    "lex.en.100k.096769": ("ogler", "noun", "/ˈoʊ.ɡlɚ/", "kẻ liếc mắt đưa tình; người nhìn"),
    "lex.en.100k.096770": ("ogling", "noun", "/ˈoʊ.ɡlɪŋ/", "ánh mắt đưa tình; cái nhìn đắm"),
    "lex.en.100k.096771": ("ogreish", "adj", "/ˈoʊ.ɡɚ.ɪʃ/", "dữ tợn như yêu quái; hung bạo"),
    "lex.en.100k.096772": ("ogresses", "noun", "/ˈoʊ.ɡrəs.ɪz/", "các mụ chằn tinh; mụ dạ xoa"),
    "lex.en.100k.096773": ("ogrish", "adj", "/ˈoʊ.ɡrɪʃ/", "dữ tợn như chằn tinh; hung ác"),
    "lex.en.100k.096774": ("ohmage", "noun", "/ˈoʊ.mɪdʒ/", "điện trở tính bằng ôm"),
    "lex.en.100k.096775": ("ohmmeters", "noun", "/ˈoʊmˌmiː.t̬ɚz/", "các máy đo điện trở; ôm kế"),
    "lex.en.100k.096776": ("ohms", "noun", "/oʊmz/", "các đơn vị ôm (điện trở)"),
    "lex.en.100k.096777": ("ohnosecond", "noun", "/ˈoʊ.noʊˌsek.ənd/", "khoảnh khắc biết mình vừa sai lầm"),
    "lex.en.100k.096778": ("oho", "intj", "/oʊˈhoʊ/", "ồ hô; chà chà (tiếng thốt)"),
    "lex.en.100k.096779": ("ohv", "noun", "/ˌoʊ.eɪtʃˈviː/", "động cơ van trên đỉnh xilanh"),
    "lex.en.100k.096780": ("oidiophore", "noun", "/oʊˈɪd.i.oʊˌfɔːr/", "cuống sinh bào tử phấn"),
    "lex.en.100k.096781": ("oidiospore", "noun", "/oʊˈɪd.i.oʊˌspɔːr/", "bào tử phấn nấm mốc"),
    "lex.en.100k.096782": ("oidium", "noun", "/oʊˈɪd.i.əm/", "bào tử phấn; bệnh nấm phấn trắng"),
    "lex.en.100k.096783": ("oikoid", "noun", "/ˈɔɪ.kɔɪd/", "chất nền của hồng cầu"),
    "lex.en.100k.096784": ("oikological", "adj", "/ˌɔɪ.kəˈlɑː.dʒɪk.əl/", "thuộc sinh thái học gia đình"),
    "lex.en.100k.096785": ("oikology", "noun", "/ɔɪˈkɑː.lə.dʒi/", "khoa học quản trị gia đình"),
    "lex.en.100k.096786": ("oikoplast", "noun", "/ˈɔɪ.kə.plæst/", "tế bào biểu bì tiết màng nhầy"),
    "lex.en.100k.096787": ("oikos", "noun", "/ˈɔɪ.kɑːs/", "gia đình và điền trang Hy Lạp cổ"),
    "lex.en.100k.096788": ("oikosite", "noun", "/ˈɔɪ.kəˌsaɪt/", "sinh vật ký sinh cố định"),
    "lex.en.100k.096789": ("oilbird", "noun", "/ˈɔɪl.bɝːd/", "chim dầu Guácharo Nam Mỹ"),
    "lex.en.100k.096790": ("oilcake", "noun", "/ˈoil.keɪk/", "bánh bã ép dầu (cho gia súc)"),
    "lex.en.100k.096791": ("oilcan", "noun", "/ˈɔɪl.kæn/", "bình tra dầu; bình đựng dầu máy"),
    "lex.en.100k.096792": ("oilcans", "noun", "/ˈɔɪl.kænz/", "các bình tra dầu máy"),
    "lex.en.100k.096793": ("oildom", "noun", "/ˈɔɪl.dəm/", "giới công nghiệp dầu mỏ"),
    "lex.en.100k.096794": ("oilengine", "noun", "/ˈɔɪlˌen.dʒɪn/", "động cơ đốt dầu; máy chạy dầu"),
    "lex.en.100k.096795": ("oilers", "noun", "/ˈɔɪ.lɚz/", "thợ tra dầu; tàu chở dầu"),
    "lex.en.100k.096796": ("oilery", "noun", "/ˈɔɪ.lɚ.i/", "cửa hàng bán dầu; xưởng ép dầu"),
    "lex.en.100k.096797": ("oilfish", "noun", "/ˈɔɪl.fɪʃ/", "loài cá thu dầu Ruvettus"),
    "lex.en.100k.096798": ("oilily", "adv", "/ˈɔɪ.lɪ.li/", "một cách trơn nhờn; khéo nịnh"),
    "lex.en.100k.096799": ("oiling", "verb", "/ˈɔɪ.lɪŋ/", "đang tra dầu mỡ; bôi trơn"),
    "lex.en.100k.096800": ("oilmen", "noun", "/ˈɔɪl.men/", "những người kinh doanh dầu mỏ"),
    "lex.en.100k.096801": ("oilpaper", "noun", "/ˈɔɪlˌpeɪ.pɚ/", "giấy dầu chống thấm nước"),
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
