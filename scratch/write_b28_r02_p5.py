import json

with open("scratch/b28_r02_raw_p5.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

edits = {
    "lex.en.200k.035902": {"ipa": "/ˈlɒks/", "vi": "các hồ nước sâu ở Scotland"},
    "lex.en.200k.035903": {"ipa": "/ˈloʊʃənz/", "vi": "kem dưỡng da; dung dịch xoa"},
    "lex.en.200k.035904": {"ipa": "/ˈluːθərənz/", "vi": "các tín đồ giáo hội Luther"},
    "lex.en.200k.035905": {"ipa": "/ˈmɑːrəz/", "vi": "loài thú mara; ma vương"},
    "lex.en.200k.035906": {"ipa": "/mɑːrˈkiːzɪz/", "vi": "các hầu tước; ngọc thoi"},
    "lex.en.200k.035907": {"ipa": "/ˈnaɪdʒərz/", "vi": "vùng sông Niger; nước Niger"},
    "lex.en.200k.035908": {"ipa": "/ˈnɪpəlz/", "vi": "núm vú; đầu vòi ren nối"},
    "lex.en.200k.035909": {"ipa": "/ˌɛnɑːrˈeɪz/", "vi": "Hiệp hội Súng trường Quốc gia Mỹ"},
    "lex.en.200k.035910": {"ipa": "/ˌɛnˈviːz/", "vi": "tiểu bang Nevada (NV)"},
    "lex.en.200k.035911": {"ipa": "/ˌpæsəˈdiːnəz/", "vi": "các thành phố Pasadena"},
    "lex.en.200k.035912": {"ipa": "/ˈpɪnəkəlz/", "vi": "đỉnh cao chót vót; tháp nhọn"},
    "lex.en.200k.035913": {"ipa": "/ˈprɑːmptɪŋz/", "vi": "sự xui khiến; lời gợi nhắc"},
    "lex.en.200k.035914": {"ipa": "/ˈsaɪz/", "vi": "đơn vị áp suất psi; chữ psi"},
    "lex.en.200k.035915": {"ipa": "/ˈreɪsɚz/", "vi": "các tay đua; xe đua; ngựa đua"},
    "lex.en.200k.035916": {"ipa": "/ˈreɪdiəlz/", "vi": "lốp xe radial bố tỏa tròn"},
    "lex.en.200k.035917": {"ipa": "/rɪˈkɑːnəsənsɪz/", "vi": "các đợt trinh sát quân sự"},
    "lex.en.200k.035918": {"ipa": "/ˈriːdʒənts/", "vi": "quan nhiếp chính; ủy viên quản trị"},
    "lex.en.200k.035919": {"ipa": "/rɛnˈdɪʃənz/", "vi": "các bản diễn tấu; bản thể hiện"},
    "lex.en.200k.035920": {"ipa": "/ˈroʊdsaɪdz/", "vi": "hai bên vệ đường; lề đường"},
    "lex.en.200k.035921": {"ipa": "/səˈskætʃəwɑːnz/", "vi": "tỉnh Saskatchewan"},
    "lex.en.200k.035922": {"ipa": "/ˌsɛkrəˈtɛriəts/", "vi": "các ban thư ký; văn phòng thư ký"},
    "lex.en.200k.035923": {"ipa": "/ˈʃeɪkiər/", "vi": "run rẩy hơn; kém vững hơn"},
    "lex.en.200k.035924": {"ipa": "/ˈʃeɪkiɪst/", "vi": "run rẩy nhất; bấp bênh nhất"},
    "lex.en.200k.035925": {"ipa": "/saɪˈbɪriəz/", "vi": "vùng đất hoang lạnh Siberia"},
    "lex.en.200k.035926": {"ipa": "/ˈsaɪnaɪz/", "vi": "vùng bán đảo Sinai"},
    "lex.en.200k.035927": {"ipa": "/ˈstɔːkərz/", "vi": "những kẻ rình rập quấy rối"},
    "lex.en.200k.035928": {"ipa": "/ˈstætʃərz/", "vi": "tầm vóc; uy tín; vóc dáng"},
    "lex.en.200k.035929": {"ipa": "/ˈstaʊtər/", "vi": "đậm người hơn; mập mạp hơn"},
    "lex.en.200k.035930": {"ipa": "/ˈstaʊtɪst/", "vi": "đậm người nhất; kiên cường nhất"},
    "lex.en.200k.035931": {"ipa": "/staʊts/", "vi": "các loại bia đen nặng độ"},
    "lex.en.200k.035932": {"ipa": "/ˈstrɪpərz/", "vi": "vũ nữ thoát y; chất tẩy sơn"},
    "lex.en.200k.035933": {"ipa": "/ˈsɪnəɡɔːɡz/", "vi": "các giáo đường Do Thái"},
    "lex.en.200k.035934": {"ipa": "/ʌnˈiːziər/", "vi": "bất an hơn; lo âu hơn"},
    "lex.en.200k.035935": {"ipa": "/ʌnˈiːziɪst/", "vi": "bất an nhất; lo âu nhất"},
    "lex.en.200k.035936": {"ipa": "/ˌjuːɛsdiːˈeɪz/", "vi": "Bộ Nông nghiệp Hoa Kỳ (USDA)"},
    "lex.en.200k.035937": {"ipa": "/ˈvɛriənsɪz/", "vi": "phương sai; sự bất đồng ý kiến"},
    "lex.en.200k.035938": {"ipa": "/ˈwɑːliz/", "vi": "những kẻ ngốc nghếch vụng về"},
    "lex.en.200k.035939": {"ipa": "/ˈweɪvlɛŋθs/", "vi": "các bước sóng ánh sáng"},
    "lex.en.200k.035940": {"ipa": "/ˈwɜːrkloʊdz/", "vi": "khối lượng công việc cần làm"},
    "lex.en.200k.035954": {"vi": "che khuất; xóa sạch khỏi trí nhớ"},
    "lex.en.200k.035970": {"vi": "ngã bệnh; suy sụp sức khỏe"},
    "lex.en.200k.035983": {"vi": "mối quan hệ tín thác ủy thác"}
}

reviewed = []
for item in raw:
    item_id = item["id"]
    if item_id in edits:
        for k, v in edits[item_id].items():
            item[k] = v
    item["status"] = "reviewed"
    assert len(item["vi"]) <= 35, f"Length > 35 at {item_id}: {item['vi']}"
    if item["pos"] != "phrase":
        assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2, f"Bad IPA at {item['hw']}: {item['ipa']}"
    reviewed.append(item)

with open("scratch/b28_r02_p5.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Batch 28 Round 2 Part 5 reviewed successfully:", len(reviewed))
