import json

with open("scratch/b28_r01_raw_p1.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

# QA adjustments
edits = {
    "lex.en.200k.035010": {"ipa": "/ˈdʒækpɑːts/", "vi": "các giải độc đắc; tiền thưởng lớn"},
    "lex.en.200k.035012": {"vi": "que hương; nhang thơm"},
    "lex.en.200k.035013": {"ipa": "/dʒʊˈræsɪks/", "vi": "các tầng kỷ Jura; đá kỷ Jura"},
    "lex.en.200k.035015": {"vi": "cá đù trắng lớn; cá whiting vua"},
    "lex.en.200k.035018": {"vi": "kính nhiều lớp; kính an toàn"},
    "lex.en.200k.035020": {"ipa": "/laɪˈbɪriəz/", "vi": "các giống cà phê Liberia"},
    "lex.en.200k.035021": {"ipa": "/ˌlɪθuˈeɪniəz/", "vi": "các cộng đồng người Litva"},
    "lex.en.200k.035022": {"ipa": "/ˈliːtərz/", "vi": "các lít; những lít"},
    "lex.en.200k.035024": {"ipa": "/ˌloʊkəˈmoʊtɪvz/", "vi": "các đầu máy xe lửa"},
    "lex.en.200k.035025": {"ipa": "/ˈlɔːŋɪŋz/", "vi": "những nỗi khao khát; niềm ước mong"},
    "lex.en.200k.035031": {"ipa": "/ˈmɑːntrəz/", "vi": "các câu thần chú; câu chân ngôn"},
    "lex.en.200k.035032": {"ipa": "/mɑːrˈsɛld/", "vi": "đã uốn tóc lượn sóng"},
    "lex.en.200k.035033": {"ipa": "/mɑːrˈsɛlɪŋ/", "vi": "việc uốn tóc lượn sóng"},
    "lex.en.200k.035034": {"ipa": "/mɑːrˈsɛld/", "vi": "đã uốn tóc lượn sóng"},
    "lex.en.200k.035035": {"ipa": "/mɑːrˈsɛlɪŋ/", "vi": "việc uốn tóc lượn sóng"},
    "lex.en.200k.035036": {"ipa": "/ˈmeɪsəz/", "vi": "các ngọn núi mặt bàn"},
    "lex.en.200k.035037": {"ipa": "/ˈmaɪkrəskoʊps/", "vi": "các kính hiển vi"},
    "lex.en.200k.035039": {"ipa": "/ˈmɪlkiər/", "vi": "đục như sữa hơn; trắng đục hơn"},
    "lex.en.200k.035040": {"ipa": "/ˈmɪlkiɪst/", "vi": "đục như sữa nhất; trắng đục nhất"},
    "lex.en.200k.035043": {"ipa": "/ˈmɪksərz/", "vi": "các máy trộn; buổi tiệc giao lưu"},
    "lex.en.200k.035045": {"ipa": "/ˌɛmˈviːz/", "vi": "các đơn vị milivôn (mV)"},
    "lex.en.200k.035047": {"ipa": "/ˈnuːsənsɪz/", "vi": "các mối phiền toái; người quấy rầy"},
    "lex.en.200k.035050": {"ipa": "/ˈaʊtɪŋz/", "vi": "các chuyến dã ngoại; cuộc dạo chơi"},
    "lex.en.200k.035055": {"ipa": "/ˈpeɪtʃɛks/", "vi": "các séc tiền lương; phiếu lương"},
    "lex.en.200k.035057": {"vi": "thành viên bồi thẩm đoàn sơ thẩm"},
    "lex.en.200k.035059": {"ipa": "/ˈpɪlɡrəmɪdʒɪz/", "vi": "các cuộc hành hương"},
    "lex.en.200k.035066": {"ipa": "/prɪˈvɛntɪvz/", "vi": "các biện pháp phòng; thuốc ngừa"},
    "lex.en.200k.035067": {"vi": "kháng nguyên tuyến tiền liệt (PSA)"},
    "lex.en.200k.035071": {"ipa": "/rædz/", "vi": "các đơn vị rad; góc radian"},
    "lex.en.200k.035073": {"ipa": "/rɪˈɡrɛʃənz/", "vi": "sự thụt lùi; các phép hồi quy"},
    "lex.en.200k.035074": {"vi": "người bị khai trừ tôn giáo"},
    "lex.en.200k.035079": {"ipa": "/ˈruːtərz/", "vi": "các bộ định tuyến; máy phay mộng"},
    "lex.en.200k.035080": {"ipa": "/ˈsæbəθs/", "vi": "các ngày Sa-bát; ngày nghỉ lễ"},
    "lex.en.200k.035086": {"ipa": "/ˈʃʌvəld/", "vi": "đã xúc bằng xẻng"},
    "lex.en.200k.035087": {"ipa": "/ˈʃʌvəlɪŋ/", "vi": "đang xúc bằng xẻng"},
    "lex.en.200k.035088": {"vi": "muối nở; natri bicacbonat"},
    "lex.en.200k.035093": {"vi": "hệ thống liên kết đòn lái"},
    "lex.en.200k.035098": {"ipa": "/ˈsɜːrneɪmz/", "vi": "các họ; những họ"},
    "lex.en.200k.035100": {"ipa": "/taɪz/", "vi": "các dân tộc ngữ hệ Thái"}
}

reviewed = []
for item in raw:
    item_id = item["id"]
    if item_id in edits:
        for k, v in edits[item_id].items():
            item[k] = v
    item["status"] = "reviewed"
    # Ensure length <= 35
    assert len(item["vi"]) <= 35, f"Length > 35 at {item_id}: {item['vi']}"
    # Ensure ipa valid
    if item["pos"] != "phrase":
        assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2, f"Bad IPA at {item['hw']}: {item['ipa']}"
    reviewed.append(item)

with open("scratch/b28_r01_p1.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Part 1 reviewed successfully:", len(reviewed))
