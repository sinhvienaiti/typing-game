import json

with open("scratch/b28_r01_raw_p2.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

edits = {
    "lex.en.200k.035103": {"vi": "chỗ ngồi bậc thang"},
    "lex.en.200k.035104": {"vi": "khớp khuỷu; khớp bẻ gập"},
    "lex.en.200k.035105": {"vi": "công tắc gạt; công tắc bập bênh"},
    "lex.en.200k.035106": {"vi": "mô hình thanh điệu; mẫu âm điệu"},
    "lex.en.200k.035114": {"vi": "ô kính cửa sổ; tấm kính cửa"},
    "lex.en.200k.035116": {"ipa": "/ˈwʊdwərdz/", "vi": "các nhân viên coi rừng"},
    "lex.en.200k.035117": {"ipa": "/ˌjuːɡoʊˈslɑːviəz/", "vi": "các nước Nam Tư cũ"},
    "lex.en.200k.035118": {"ipa": "/ˌeɪdiːeɪtʃˈdiːz/", "vi": "các chứng tăng động giảm chú ý"},
    "lex.en.200k.035119": {"ipa": "/əˈlɒnzoʊz/", "vi": "những người tên Alonso"},
    "lex.en.200k.035120": {"ipa": "/ˈænsɛstərz/", "vi": "tổ tiên; ông bà tổ tiên"},
    "lex.en.200k.035121": {"ipa": "/ˈɑːrbərz/", "vi": "giàn cây leo; bóng râm cây"},
    "lex.en.200k.035122": {"ipa": "/ˈæksəlz/", "vi": "các trục bánh xe"},
    "lex.en.200k.035123": {"ipa": "/ˈbreɪkaʊts/", "vi": "các vụ vượt ngục; sự bùng nổ"},
    "lex.en.200k.035124": {"ipa": "/ˈkætʃiər/", "vi": "bắt tai hơn; dễ nhớ hơn"},
    "lex.en.200k.035125": {"ipa": "/ˈkætʃiɪst/", "vi": "bắt tai nhất; dễ nhớ nhất"},
    "lex.en.200k.035126": {"ipa": "/ˌsiːbiːˈsiːz/", "vi": "xét nghiệm công thức máu toàn bộ"},
    "lex.en.200k.035127": {"ipa": "/ˌsɛrəˈmoʊniəlz/", "vi": "các nghi thức; nghi lễ"},
    "lex.en.200k.035128": {"ipa": "/tʃɛkt/", "vi": "đã kẻ ô carô; đã chi bằng séc"},
    "lex.en.200k.035129": {"ipa": "/tʃɛks/", "vi": "các tờ séc; chi phiếu ngân hàng"},
    "lex.en.200k.035130": {"ipa": "/tʃɛkɪŋ/", "vi": "tài khoản séc; việc ký séc"},
    "lex.en.200k.035131": {"ipa": "/ˈsɪskoʊz/", "vi": "các loài cá hồi trắng cisco"},
    "lex.en.200k.035132": {"ipa": "/ˈsɪskoʊz/", "vi": "các loài cá hồi trắng cisco"},
    "lex.en.200k.035133": {"ipa": "/klɪŋz/", "vi": "bám chặt; dính chặt", "pos": "verb"},
    "lex.en.200k.035134": {"ipa": "/ˌkoʊɪnˈsaɪdɪd/", "vi": "đã trùng khớp; xảy ra đồng thời"},
    "lex.en.200k.035135": {"ipa": "/ˌkoʊɪnˈsaɪdz/", "vi": "trùng khớp; xảy ra đồng thời"},
    "lex.en.200k.035136": {"ipa": "/ˈkɒvəntriz/", "vi": "tình trạng bị cô lập tẩy chay"},
    "lex.en.200k.035137": {"ipa": "/ˈkrɑːkədaɪlz/", "vi": "các con cá sấu"},
    "lex.en.200k.035138": {"ipa": "/kʌbd/", "vi": "đã sinh con non (thú hoang)"},
    "lex.en.200k.035139": {"ipa": "/ˈdɛrɪks/", "vi": "các giàn khoan dầu; cần cẩu tháp"},
    "lex.en.200k.035140": {"ipa": "/djʊˈrænts/", "vi": "những người họ Durant"},
    "lex.en.200k.035141": {"ipa": "/ɛlks/", "vi": "các con nai sừng tấm lớn"},
    "lex.en.200k.035142": {"ipa": "/ˈfɛləz/", "vi": "các anh bạn; những người anh em"},
    "lex.en.200k.035143": {"ipa": "/ˈɡɑːrdnərz/", "vi": "các người làm vườn"},
    "lex.en.200k.035144": {"ipa": "/ˈɡɪnɪsɪz/", "vi": "các ly bia đen Guinness"},
    "lex.en.200k.035145": {"ipa": "/ˈhoʊmstɛdɪd/", "vi": "đã khai hoang định cư"},
    "lex.en.200k.035146": {"ipa": "/ˈhoʊmstɛdɪŋ/", "vi": "việc khai hoang lập trại định cư"},
    "lex.en.200k.035147": {"ipa": "/ˈhoʊmstɛdz/", "vi": "các trang trại khẩn hoang"},
    "lex.en.200k.035148": {"ipa": "/hjuːz/", "vi": "các sắc thái màu sắc"},
    "lex.en.200k.035149": {"ipa": "/ˈaɪsɪŋz/", "vi": "lớp kem phủ bánh; sự đóng băng"},
    "lex.en.200k.035150": {"ipa": "/ˈɪntəlɛkts/", "vi": "trí tuệ; các bậc trí thức"},
    "lex.en.200k.035151": {"ipa": "/ˌɪzəˈbɛləz/", "vi": "những người tên Isabella"},
    "lex.en.200k.035152": {"ipa": "/dʒɪˈhɑːdz/", "vi": "các cuộc thánh chiến Hồi giáo"},
    "lex.en.200k.035153": {"ipa": "/ˈnɑːbɪŋ/", "vi": "chốt núm; mấu gồ tròn"},
    "lex.en.200k.035154": {"ipa": "/nɑːbz/", "vi": "các núm vặn; quả đấm cửa"},
    "lex.en.200k.035155": {"ipa": "/ləˈhɔːrz/", "vi": "những giống bồ câu Lahore"},
    "lex.en.200k.035156": {"ipa": "/ˈlɛdʒərz/", "vi": "các cuốn sổ cái kế toán"},
    "lex.en.200k.035157": {"ipa": "/ˈmɪmɪkt/", "vi": "đã bắt chước; đã nhại lại"},
    "lex.en.200k.035158": {"ipa": "/ˈmɪmɪkɪŋ/", "vi": "đang bắt chước; việc nhại lại"},
    "lex.en.200k.035159": {"ipa": "/ˈmɪmɪks/", "vi": "những người hay nhại; bắt chước"},
    "lex.en.200k.035160": {"ipa": "/ˈmjʊrəlz/", "vi": "các bức tranh tường lớn"},
    "lex.en.200k.035161": {"ipa": "/ˈmɜːrdɑːks/", "vi": "những người dòng họ Murdoch"},
    "lex.en.200k.035162": {"ipa": "/nænz/", "vi": "bà ngoại; bà nội; bánh mì naan"},
    "lex.en.200k.035163": {"ipa": "/ˈneɪzəlz/", "vi": "các âm mũi; xương mũi"},
    "lex.en.200k.035164": {"ipa": "/nɔːrˈθæmptənz/", "vi": "các vùng Northampton"},
    "lex.en.200k.035165": {"ipa": "/ˈoʊdɚz/", "vi": "các mùi hương; mùi vị"},
    "lex.en.200k.035166": {"ipa": "/ˈraɪks/", "vi": "các đế chế Đức"},
    "lex.en.200k.035167": {"ipa": "/ˌskændɪˈneɪviənz/", "vi": "người dân vùng Scandinavia"},
    "lex.en.200k.035168": {"ipa": "/ˈʃoʊdaʊnz/", "vi": "các cuộc đối đầu quyết định"},
    "lex.en.200k.035169": {"ipa": "/ˈsaɪdɪŋz/", "vi": "đường ray tránh; tấm ốp tường"},
    "lex.en.200k.035170": {"ipa": "/ˈskaɪlaɪnz/", "vi": "đường chân trời đô thị"},
    "lex.en.200k.035171": {"ipa": "/ˈstɑːkɪŋz/", "vi": "tất da chân dài; quần tất"},
    "lex.en.200k.035172": {"ipa": "/ˈswɪmɚz/", "vi": "các vận động viên bơi lội"},
    "lex.en.200k.035173": {"ipa": "/ˈtɛlɚz/", "vi": "giao dịch viên ngân hàng"},
    "lex.en.200k.035174": {"ipa": "/ˈtrænsɪz/", "vi": "trạng thái xuất thần; cơn mê"},
    "lex.en.200k.035175": {"ipa": "/ˈtrævəlɚz/", "vi": "những người đi du lịch; lữ khách"},
    "lex.en.200k.035176": {"ipa": "/ˈwɛbkæmz/", "vi": "các máy quay web; webcam"},
    "lex.en.200k.035177": {"ipa": "/wɛnz/", "vi": "các nang bã đậu dưới da"},
    "lex.en.200k.035178": {"ipa": "/ˈwɛstənz/", "vi": "những người họ Weston"},
    "lex.en.200k.035179": {"ipa": "/ˈzeɪviərz/", "vi": "những người tên Xavier"},
    "lex.en.200k.035180": {"vi": "cơn phân liệt cấp tính"},
    "lex.en.200k.035198": {"vi": "sản xuất hàng loạt; làm ra ồ ạt"}
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

with open("scratch/b28_r01_p2.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Part 2 reviewed successfully:", len(reviewed))
