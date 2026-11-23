import json

records = [
    ("080003", "prudences", "noun", "/ˈpruːdənsɪz/", "những sự thận trọng, khôn ngoan"),
    ("080004", "prudentially", "adv", "/pruːˈdɛnʃəli/", "một cách thận trọng, khôn ngoan"),
    ("080005", "prudishly", "adv", "/ˈpruːdɪʃli/", "một cách quá giữ kẽ, e dè giả tạo"),
    ("080006", "pruinose", "adj", "/ˈpruːɪˌnoʊs/", "có phủ lớp phấn trắng (thực vật)"),
    ("080007", "prumnopitys", "noun", "/ˌpruːmnoʊˈpɪtɪs/", "chi thông đất Prumnopitys"),
    ("080008", "pruned", "verb", "/pruːnd/", "đã cắt tỉa cành; đã cắt giảm bớt"),
    ("080009", "prunellidae", "noun", "/pruːˈnɛlɪˌdiː/", "họ chim chích dậu (Prunellidae)"),
    ("080010", "prunello", "noun", "/pruːˈnɛloʊ/", "mận khô gọt vỏ; vải len mỏng (cổ)"),
    ("080011", "prunes", "verb", "/pruːnz/", "cắt tỉa (cành); cắt giảm (chi phí)"),
    ("080012", "pruniform", "adj", "/ˈpruːnɪˌfɔːrm/", "có hình dạng giống quả mận"),
    ("080013", "pruriency", "noun", "/ˈprʊriənsi/", "tính hiếu sắc, thói dâm dục"),
    ("080014", "pruriently", "adv", "/ˈprʊriəntli/", "một cách hiếu sắc, dâm dục"),
    ("080015", "pruriginous", "adj", "/prʊˈrɪdʒənəs/", "mắc chứng ngứa sần; gây ngứa ngáy"),
    ("080016", "pruritic", "adj", "/prʊˈrɪtɪk/", "gây ngứa, thuộc chứng ngứa (y học)"),
    ("080017", "prussianise", "verb", "/ˈprʌʃəˌnaɪz/", "Phổ hóa, áp đặt kỷ luật kiểu Phổ"),
    ("080018", "prussianism", "noun", "/ˈprʌʃəˌnɪzəm/", "chủ nghĩa quân phiệt kiểu Phổ"),
    ("080019", "prussianize", "verb", "/ˈprʌʃəˌnaɪz/", "Phổ hóa, áp đặt kỷ luật kiểu Phổ"),
    ("080020", "prussic", "adj", "/ˈprʌsɪk/", "thuộc axit pruxic (cyanua)"),
    ("080021", "pryer", "noun", "/ˈpraɪər/", "người tò mò, kẻ hay tọc mạch"),
    ("080022", "pryingly", "adv", "/ˈpraɪɪŋli/", "với vẻ tò mò, tọc mạch xoi mói"),
    ("080023", "psalmodic", "adj", "/sælˈmɑːdɪk/", "thuộc nghệ thuật hát thánh vịnh"),
    ("080024", "psalmodist", "noun", "/ˈsɑːlmədɪst/", "người hát thánh vịnh"),
    ("080025", "psalmodize", "verb", "/ˈsɑːlməˌdaɪz/", "hát thánh vịnh, ngâm thánh ca"),
    ("080026", "psaltriparus", "noun", "/ˌsɔːltrɪˈpɛrəs/", "chi chim sẻ bụi Bắc Mỹ"),
    ("080027", "psammoma", "noun", "/sæˈmoʊmə/", "u thể cát, u màng não dạng cát"),
    ("080028", "psammon", "noun", "/ˈsæmɑːn/", "quần xã sinh vật sống trong cát"),
    ("080029", "psammona", "noun", "/sæˈmoʊnə/", "các quần xã sinh vật sống trong cát"),
    ("080030", "psammophilous", "adj", "/sæˈmɑːfələs/", "ưa cát, thích sống trên đất cát"),
    ("080031", "psammophyte", "noun", "/ˈsæməˌfaɪt/", "thực vật ưa cát, cây mọc trên cát"),
    ("080032", "psammosere", "noun", "/ˈsæməˌsɪr/", "diễn thế thực vật trên cồn cát"),
    ("080033", "psellism", "noun", "/ˈsɛlˌɪzəm/", "chứng nói lắp, tật nói ngọng"),
    ("080034", "psellismus", "noun", "/sɛˈlɪzməs/", "chứng nói lắp, tật nói ngọng"),
    ("080035", "psenes", "noun", "/ˈsiːniːz/", "chi cá trôi dạt đại dương (Psenes)"),
    ("080036", "psephite", "noun", "/ˈsiːfaɪt/", "đá mảnh thô, đá cuội kết (địa chất)"),
    ("080037", "psephological", "adj", "/ˌsiːfəˈlɑːdʒɪkəl/", "thuộc khoa nghiên cứu bầu cử"),
    ("080038", "psephologists", "noun", "/siːˈfɑːlədʒɪsts/", "các nhà nghiên cứu bầu cử"),
    ("080039", "psephology", "noun", "/siːˈfɑːlədʒi/", "khoa học nghiên cứu bầu cử"),
    ("080040", "psephurus", "noun", "/sɪˈfjʊrəs/", "chi cá tầm thìa Trung Quốc"),
    ("080041", "psetta", "noun", "/ˈsɛtə/", "chi cá bơn lớn châu Âu (Psetta)"),
    ("080042", "psettichthys", "noun", "/sɛˈtɪkθɪs/", "chi cá bơn cát Thái Bình Dương"),
    ("080043", "pseudacris", "noun", "/suːˈdækrɪs/", "chi ếch cây đồng ca Bắc Mỹ"),
    ("080044", "pseudaletia", "noun", "/ˌsuːdəˈliːʃə/", "chi bướm sâu keo (Pseudaletia)"),
    ("080045", "pseudaxis", "noun", "/suːˈdæksɪs/", "trục giả (cành hợp trục, thực vật)"),
    ("080046", "pseudechis", "noun", "/suːˈdɛkɪs/", "chi rắn đen độc Úc (Pseudechis)"),
    ("080047", "pseudemys", "noun", "/suːˈdɛmɪs/", "chi rùa sông Bắc Mỹ (Pseudemys)"),
    ("080048", "pseudepigraphy", "noun", "/ˌsuːdɪˈpɪɡrəfi/", "hành vi giả danh tác giả kinh điển"),
    ("080049", "pseudepisematic", "adj", "/ˌsuːdɛpɪsɪˈmætɪk/", "có màu sắc ngụy trang lừa mồi"),
    ("080050", "pseudoallele", "noun", "/ˌsuːdoʊəˈliːl/", "alen giả (di truyền học)"),
    ("080051", "pseudoallelic", "adj", "/ˌsuːdoʊəˈliːlɪk/", "thuộc alen giả (di truyền học)"),
    ("080052", "pseudoallelism", "noun", "/ˌsuːdoʊəˈliːlˌɪzəm/", "hiện tượng alen giả (di truyền)"),
    ("080053", "pseudoalveolar", "adj", "/ˌsuːdoʊælˈviːələr/", "có dạng phế nang giả (giải phẫu)"),
    ("080054", "pseudoamitosis", "noun", "/ˌsuːdoʊæmaɪˈtoʊsɪs/", "hiện tượng trực phân giả (tế bào)"),
    ("080055", "pseudoanalytic", "adj", "/ˌsuːdoʊænəˈlɪtɪk/", "giả giải tích (toán học)"),
    ("080056", "pseudoangiocarpic", "adj", "/ˌsuːdoʊˌændʒioʊˈkɑːrpɪk/", "có thể quả kín giả (nấm học)"),
    ("080057", "pseudoaposematic", "adj", "/ˌsuːdoʊˌæpəsɪˈmætɪk/", "bắt chước màu cảnh báo (sinh học)"),
    ("080058", "pseudoaquatic", "adj", "/ˌsuːdoʊəˈkwɑːtɪk/", "ưa đất ẩm ướt, bán thủy sinh"),
    ("080059", "pseudoaxile", "adj", "/ˌsuːdoʊˈæksəl/", "thuộc trục giả (thực vật học)"),
    ("080060", "pseudobasidum", "noun", "/ˌsuːdoʊbəˈsɪdiəm/", "đảm vách dày, đảm giả (nấm)"),
    ("080061", "pseudobivalent", "adj", "/ˌsuːdoʊbaɪˈveɪlənt/", "có cặp nhiễm sắc thể giả"),
    ("080062", "pseudobombax", "noun", "/ˌsuːdoʊˈbɑːmbæks/", "chi cây gạo giả (Pseudobombax)"),
    ("080063", "pseudobrachium", "noun", "/ˌsuːdoʊˈbreɪkiəm/", "vây ngực giả dạng chi (cá)"),
    ("080064", "pseudobranch", "noun", "/ˈsuːdoʊˌbræŋk/", "mang giả (bộ phận hô hấp phụ cá)"),
    ("080065", "pseudobulbous", "adj", "/ˌsuːdoʊˈbʌlbəs/", "có thân giả hành (họ Lan)"),
    ("080066", "pseudobuld", "noun", "/ˈsuːdoʊˌbʌlb/", "thân giả hành (biến thể sai chữ)"),
    ("080067", "pseudocapsule", "noun", "/ˌsuːdoʊˈkæpsəl/", "bao giả (bọc khối u, y học)"),
    ("080068", "pseudocardia", "noun", "/ˌsuːdoʊˈkɑːrdiə/", "tim giả (mạch co bóp ở côn trùng)"),
    ("080069", "pseudocarp", "noun", "/ˈsuːdoʊˌkɑːrp/", "quả giả (như táo tây, dâu tây)"),
    ("080070", "pseudocarpous", "adj", "/ˌsuːdoʊˈkɑːrpəs/", "có dạng quả giả (thực vật)"),
    ("080071", "pseudocellular", "adj", "/ˌsuːdoʊˈsɛljələr/", "giống cấu trúc tế bào, giả tế bào"),
    ("080072", "pseudocellus", "noun", "/ˌsuːdoʊˈsɛləs/", "mắt đơn giả (ở bọ đuôi bật)"),
    ("080073", "pseudochrysalis", "noun", "/ˌsuːdoʊˈkrɪsəlɪs/", "nhộng giả (ấu trùng côn trùng)"),
    ("080074", "pseudococcidae", "noun", "/ˌsuːdoʊˈkɑːksɪˌdiː/", "họ Rệp sáp (Pseudococcidae)"),
    ("080075", "pseudocoel", "noun", "/ˈsuːdoʊˌsiːl/", "thể xoang giả (động vật giun tròn)"),
    ("080076", "pseudocoelomate", "adj", "/ˌsuːdoʊˈsiːləˌmeɪt/", "có thể xoang giả (động vật học)"),
    ("080077", "pseudocolumella", "noun", "/ˌsuːdoʊˌkɑːljəˈmɛlə/", "trụ giả (nấm nhầy, san hô)"),
    ("080078", "pseudocolus", "noun", "/ˌsuːdoʊˈkoʊləs/", "chi nấm mực thối (Pseudocolus)"),
    ("080079", "pseudoconch", "noun", "/ˈsuːdoʊˌkɑːŋk/", "vỏ xoắn giả (giải phẫu mũi bò sát)"),
    ("080080", "pseudocone", "noun", "/ˈsuːdoʊˌkoʊn/", "nón thủy tinh giả (mắt côn trùng)"),
    ("080081", "pseudoconformal", "adj", "/ˌsuːdoʊkənˈfɔːrməl/", "giả bảo giác (hình học vi phân)"),
    ("080082", "pseudoconidium", "noun", "/ˌsuːdoʊkəˈnɪdiəm/", "bào tử đính giả (nấm học)"),
    ("080083", "pseudoconjugation", "noun", "/ˌsuːdoʊˌkɑːndʒəˈɡeɪʃən/", "sự tiếp hợp giả (sinh vật đơn bào)"),
    ("080084", "pseudocycloidal", "adj", "/ˌsuːdoʊsaɪˈklɔɪdəl/", "có dạng đường xicloit giả (toán)"),
    ("080085", "pseudocyesis", "noun", "/ˌsuːdoʊsaɪˈiːsɪs/", "chứng mang thai giả (tâm lý)"),
    ("080086", "pseudocyst", "noun", "/ˈsuːdoʊˌsɪst/", "nang giả (y học, sinh vật học)"),
    ("080087", "pseudoderm", "noun", "/ˈsuːdoʊˌdɜːrm/", "lớp vỏ giả (bọt biển)"),
    ("080088", "pseudodominance", "noun", "/ˌsuːdoʊˈdɑːmənəns/", "tính trội giả (di truyền học)"),
    ("080089", "pseudodont", "adj", "/ˈsuːdoʊˌdɑːnt/", "có răng giả bằng chất sừng"),
    ("080090", "pseudoepiphyte", "noun", "/ˌsuːdoʊˈɛpəˌfaɪt/", "thực vật biểu sinh giả (dây leo)"),
    ("080091", "pseudofossil", "noun", "/ˈsuːdoʊˌfɑːsəl/", "hóa thạch giả (khoáng vật tự nhiên)"),
    ("080092", "pseudogamic", "adj", "/ˌsuːdoʊˈɡæmɪk/", "thuộc sự thụ tinh giả (thực vật)"),
    ("080093", "pseudogap", "noun", "/ˈsuːdoʊˌɡæp/", "vùng giả khe năng lượng (vật lý)"),
    ("080094", "pseudogaps", "noun", "/ˈsuːdoʊˌɡæps/", "các vùng giả khe năng lượng"),
    ("080095", "pseudogaster", "noun", "/ˈsuːdoʊˌɡæstər/", "khoang tiêu hóa giả (bọt biển)"),
    ("080096", "pseudogastreula", "noun", "/ˌsuːdoʊˈɡæstrələ/", "phôi vị giả (biến thể sai chữ)"),
    ("080097", "pseudograph", "noun", "/ˈsuːdoʊˌɡræf/", "tác phẩm giả mạo tên tác giả"),
    ("080098", "pseudohallucination", "noun", "/ˌsuːdoʊhəˌluːsəˈneɪʃən/", "ảo giác giả (tâm thần học)"),
    ("080099", "pseudohermaphrodite", "adj", "/ˌsuːdoʊhɜːrˈmæfrəˌdaɪt/", "lưỡng tính giả (y học)"),
    ("080100", "pseudohermaphroditic", "adj", "/ˌsuːdoʊhɜːrˌmæfrəˈdɪtɪk/", "thuộc chứng lưỡng tính giả"),
    ("080101", "pseudohermaphroditism", "noun", "/ˌsuːdoʊhɜːrˈmæfrədaɪˌtɪzəm/", "chứng lưỡng tính giả (y học)"),
    ("080102", "pseudohypoparathyroidism", "noun", "/ˌsuːdoʊˌhaɪpoʊˌpɛrəˈθaɪrɔɪˌdɪzəm/", "bệnh giả suy tuyến cận giáp"),
]

raw = json.load(open("scratch/b37_r01_raw_p1.json"))
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
with open("scratch/b37_r01_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r01_p1 saved OK")
