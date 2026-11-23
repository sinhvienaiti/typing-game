# scratch/b18_r04_p3.py
# Batch 18 Round 4 Part 3: records 1700 - 1799 (IDs 086702 - 086801)
import json

data = [
    {
        "id": "lex.en.100k.086702",
        "hw": "incumbrance",
        "pos": "noun",
        "ipa": "/ɪnˈkʌmbrəns/",
        "vi": "vật ngáng trở; gánh nặng thế chấp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086703",
        "hw": "incunabula",
        "pos": "noun",
        "ipa": "/ˌɪŋkjəˈnæbjələ/",
        "vi": "sách in thời kỳ đầu; thuở sơ khai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086704",
        "hw": "incurability",
        "pos": "noun",
        "ipa": "/ɪnˌkjʊərəˈbɪləti/",
        "vi": "tính nan y; tính không chữa được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086705",
        "hw": "incurableness",
        "pos": "noun",
        "ipa": "/ɪnˈkjʊərəbəlnəs/",
        "vi": "tính chất nan y; sự bất trị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086706",
        "hw": "incuriosity",
        "pos": "noun",
        "ipa": "/ɪnˌkjʊəriˈɑːsəti/",
        "vi": "sự thiếu tò mò; tính thờ ơ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086707",
        "hw": "incuriously",
        "pos": "adv",
        "ipa": "/ɪnˈkjʊəriəsli/",
        "vi": "một cách thờ ơ; không chút tò mò",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086708",
        "hw": "incuriousness",
        "pos": "noun",
        "ipa": "/ɪnˈkjʊəriəsnəs/",
        "vi": "tính không tò mò; sự hờ hững",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086709",
        "hw": "incurred",
        "pos": "verb",
        "ipa": "/ɪnˈkɜːrd/",
        "vi": "đã gánh chịu; đã phát sinh nợ nần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086710",
        "hw": "incurrent",
        "pos": "adj",
        "ipa": "/ɪnˈkɜːrənt/",
        "vi": "chảy vào trong; dẫn nước vào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086711",
        "hw": "incurs",
        "pos": "verb",
        "ipa": "/ɪnˈkɜːrz/",
        "vi": "gánh chịu; chuốc lấy; phát sinh nợ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086712",
        "hw": "incursions",
        "pos": "noun",
        "ipa": "/ɪnˈkɜːrʒənz/",
        "vi": "những cuộc xâm lấn; sự đột nhập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086713",
        "hw": "incursive",
        "pos": "adj",
        "ipa": "/ɪnˈkɜːrsɪv/",
        "vi": "mang tính xâm nhập; tràn lấn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086714",
        "hw": "incurvate",
        "pos": "adj",
        "ipa": "/ˈɪnkɚveɪt/",
        "vi": "uốn cong vào trong; quặp vào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086715",
        "hw": "incurvation",
        "pos": "noun",
        "ipa": "/ˌɪnkɚˈveɪʃən/",
        "vi": "độ cong vào trong; sự uốn cong",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086716",
        "hw": "incurvature",
        "pos": "noun",
        "ipa": "/ɪnˈkɚvətʃər/",
        "vi": "đường cong vào phía trong",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086717",
        "hw": "incurve",
        "pos": "verb",
        "ipa": "/ɪnˈkɚv/",
        "vi": "uốn cong vào trong; bẻ quặp vào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086718",
        "hw": "incuse",
        "pos": "adj",
        "ipa": "/ɪnˈkjuːz/",
        "vi": "được đúc lõm; khắc chìm (tiền xu)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086719",
        "hw": "indeciduate",
        "pos": "adj",
        "ipa": "/ˌɪndɪˈsɪdʒuɪt/",
        "vi": "không có nhau rụng (động vật)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086720",
        "hw": "indeciduous",
        "pos": "adj",
        "ipa": "/ˌɪndɪˈsɪdʒuəs/",
        "vi": "không rụng lá; thường xanh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086721",
        "hw": "indecipherability",
        "pos": "noun",
        "ipa": "/ɪndɪˌsaɪfərəˈbɪləti/",
        "vi": "tính không thể giải mã đọc được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086722",
        "hw": "indecipherableness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈsaɪfərəbəlnəs/",
        "vi": "tình trạng chữ viết không thể đọc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086723",
        "hw": "indecipherably",
        "pos": "adv",
        "ipa": "/ˌɪndɪˈsaɪfərəbli/",
        "vi": "đến mức không thể giải mã đọc ra",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086724",
        "hw": "indecisions",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈsɪʒənz/",
        "vi": "những lúc do dự; sự ngập ngừng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086725",
        "hw": "indeclinable",
        "pos": "adj",
        "ipa": "/ˌɪndɪˈklaɪnəbəl/",
        "vi": "không biến cách (ngữ pháp)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086726",
        "hw": "indeclinableness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈklaɪnəbəlnəs/",
        "vi": "tính không biến cách trong ngữ pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086727",
        "hw": "indecomposability",
        "pos": "noun",
        "ipa": "/ɪndɪˌkɑːmpoʊzəˈbɪləti/",
        "vi": "tính không thể phân rã phân hủy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086728",
        "hw": "indecomposable",
        "pos": "adj",
        "ipa": "/ˌɪndikəmˈpoʊzəbəl/",
        "vi": "không thể phân hủy; không phân tách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086729",
        "hw": "indecomposableness",
        "pos": "noun",
        "ipa": "/ˌɪndikəmˈpoʊzəbəlnəs/",
        "vi": "tính không thể phân tách nhỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086730",
        "hw": "indecorously",
        "pos": "adv",
        "ipa": "/ɪnˈdɛkərəsli/",
        "vi": "một cách khiếm nhã; thiếu lịch sự",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086731",
        "hw": "indecorousness",
        "pos": "noun",
        "ipa": "/ɪnˈdɛkərəsnəs/",
        "vi": "sự khiếm nhã; thói thiếu đoan trang",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086732",
        "hw": "indecorum",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈkɔːrəm/",
        "vi": "hành vi khiếm nhã; sự bất lịch sự",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086733",
        "hw": "indefatigability",
        "pos": "noun",
        "ipa": "/ɪndɪˌfætɪɡəˈbɪləti/",
        "vi": "tính kiên cường không biết mệt mỏi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086734",
        "hw": "indefatigableness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈfætɪɡəbəlnəs/",
        "vi": "sự bền bỉ kiên trì dẻo dai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086735",
        "hw": "indefeasibility",
        "pos": "noun",
        "ipa": "/ɪndɪˌfiːzəˈbɪləti/",
        "vi": "tính không thể bị hủy bỏ vô hiệu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086736",
        "hw": "indefeasibleness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈfiːzəbəlnəs/",
        "vi": "tính bất khả hủy tiêu bãi bỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086737",
        "hw": "indefeasibly",
        "pos": "adv",
        "ipa": "/ˌɪndɪˈfiːzəbli/",
        "vi": "một cách không thể hủy bỏ được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086738",
        "hw": "indefectibility",
        "pos": "noun",
        "ipa": "/ɪndɪˌfɛktəˈbɪləti/",
        "vi": "tính không thể sai lầm; hoàn hảo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086739",
        "hw": "indefectible",
        "pos": "adj",
        "ipa": "/ˌɪndɪˈfɛktəbəl/",
        "vi": "không thể sai lầm; không suy suyển",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086740",
        "hw": "indefectibly",
        "pos": "adv",
        "ipa": "/ˌɪndɪˈfɛktəbli/",
        "vi": "một cách không tì vết sai lầm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086741",
        "hw": "indefensibility",
        "pos": "noun",
        "ipa": "/ɪndɪˌfɛnsəˈbɪləti/",
        "vi": "tính không thể biện hộ chống đỡ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086742",
        "hw": "indefensibleness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈfɛnsəbəlnəs/",
        "vi": "sự không thể bào chữa hay phòng thủ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086743",
        "hw": "indefensibly",
        "pos": "adv",
        "ipa": "/ˌɪndɪˈfɛnsəbli/",
        "vi": "một cách không thể bao biện được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086744",
        "hw": "indefinability",
        "pos": "noun",
        "ipa": "/ɪndɪˌfaɪnəˈbɪləti/",
        "vi": "tính không thể định nghĩa gọi tên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086745",
        "hw": "indefinably",
        "pos": "adv",
        "ipa": "/ˌɪndɪˈfaɪnəbli/",
        "vi": "một cách khó tả; mơ hồ khôn xiết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086746",
        "hw": "indefinitive",
        "pos": "adj",
        "ipa": "/ˌɪndɪˈfɪnətɪv/",
        "vi": "không dứt khoát; thiếu quyết đoán",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086747",
        "hw": "indefinitiveness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈfɪnətɪvnəs/",
        "vi": "tính chất không dứt khoát rõ ràng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086748",
        "hw": "indefinitude",
        "pos": "noun",
        "ipa": "/ɪnˈdɛfɪnɪtuːd/",
        "vi": "tính chất vô hạn; sự mơ hồ mập mờ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086749",
        "hw": "indefinity",
        "pos": "noun",
        "ipa": "/ɪnˈdɛfɪnəti/",
        "vi": "sự vô định; tính không xác định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086750",
        "hw": "indehiscence",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈhɪsəns/",
        "vi": "tính không tự mở nẻ (quả cây)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086751",
        "hw": "indeliberate",
        "pos": "adj",
        "ipa": "/ˌɪndɪˈlɪbərət/",
        "vi": "không cố ý; bột phát ngoài ý muốn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086752",
        "hw": "indeliberateness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈlɪbərətnəs/",
        "vi": "tính không suy tính trước; vô tình",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086753",
        "hw": "indeliberation",
        "pos": "noun",
        "ipa": "/ˌɪndɪˌlɪbəˈreɪʃən/",
        "vi": "sự thiếu cân nhắc; tính bốc đồng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086754",
        "hw": "indelibility",
        "pos": "noun",
        "ipa": "/ɪnˌdɛləˈbɪləti/",
        "vi": "tính không thể tẩy xóa phai mờ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086755",
        "hw": "indelibleness",
        "pos": "noun",
        "ipa": "/ɪnˈdɛləbəlnəs/",
        "vi": "sự không phai nhòa; nét khắc sâu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086756",
        "hw": "indelicately",
        "pos": "adv",
        "ipa": "/ɪnˈdɛlɪkətli/",
        "vi": "một cách thiếu tế nhị; vụng về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086757",
        "hw": "indelicateness",
        "pos": "noun",
        "ipa": "/ɪnˈdɛlɪkətnəs/",
        "vi": "sự thiếu tế nhị; tính khiếm nhã",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086758",
        "hw": "indemnified",
        "pos": "verb",
        "ipa": "/ɪnˈdɛmnɪfaɪd/",
        "vi": "đã bồi thường thiệt hại; bồi hoàn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086759",
        "hw": "indemnifier",
        "pos": "noun",
        "ipa": "/ɪnˈdɛmnɪfaɪər/",
        "vi": "người bồi thường; bên bồi hoàn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086760",
        "hw": "indemnifies",
        "pos": "verb",
        "ipa": "/ɪnˈdɛmnɪfaɪz/",
        "vi": "bồi thường thiệt hại; miễn trách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086761",
        "hw": "indemnifying",
        "pos": "verb",
        "ipa": "/ɪnˈdɛmnɪfaɪɪŋ/",
        "vi": "đang bồi thường; đang đền bù",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086762",
        "hw": "indemnitee",
        "pos": "noun",
        "ipa": "/ɪnˌdɛmnɪˈtiː/",
        "vi": "người được bồi thường đền bù",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086763",
        "hw": "indemnitor",
        "pos": "noun",
        "ipa": "/ɪnˈdɛmnɪtər/",
        "vi": "người chịu trách nhiệm bồi thường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086764",
        "hw": "indemonstrability",
        "pos": "noun",
        "ipa": "/ɪndɪˌmɑːnstrəˈbɪləti/",
        "vi": "tính không thể chứng minh được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086765",
        "hw": "indemonstrable",
        "pos": "adj",
        "ipa": "/ˌɪndɪˈmɑːnstrəbəl/",
        "vi": "không thể chứng minh được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086766",
        "hw": "indemonstrableness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈmɑːnstrəbəlnəs/",
        "vi": "tình trạng không thể chứng minh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086767",
        "hw": "indemonstrably",
        "pos": "adv",
        "ipa": "/ˌɪndɪˈmɑːnstrəbli/",
        "vi": "theo cách không thể chứng minh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086768",
        "hw": "indene",
        "pos": "noun",
        "ipa": "/ˈɪndiːn/",
        "vi": "hợp chất hidrocacbon inden (hóa)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086769",
        "hw": "indented",
        "pos": "verb",
        "ipa": "/ɪnˈdɛntɪd/",
        "vi": "đã thụt đầu dòng; đã làm mẻ mép",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086770",
        "hw": "indenting",
        "pos": "verb",
        "ipa": "/ɪnˈdɛntɪŋ/",
        "vi": "đang thụt lề đầu dòng; tạo khía",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086771",
        "hw": "indents",
        "pos": "verb",
        "ipa": "/ɪnˈdɛnts/",
        "vi": "thụt đầu dòng; làm mẻ mép; đặt hàng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086772",
        "hw": "indentureship",
        "pos": "noun",
        "ipa": "/ɪnˈdɛntʃərʃɪp/",
        "vi": "thời hạn học việc giao kèo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086773",
        "hw": "indepth",
        "pos": "adj",
        "ipa": "/ˈɪndɛpθ/",
        "vi": "chuyên sâu; toàn diện tường tận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086774",
        "hw": "indescribability",
        "pos": "noun",
        "ipa": "/ɪndɪˌskraɪbəˈbɪləti/",
        "vi": "tính không thể miêu tả xiết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086775",
        "hw": "indescribableness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈskraɪbəbəlnəs/",
        "vi": "sự không thể diễn tả bằng lời",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086776",
        "hw": "indestructibleness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈstrʌktəbəlnəs/",
        "vi": "tính không thể phá hủy tiêu diệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086777",
        "hw": "indestructibly",
        "pos": "adv",
        "ipa": "/ˌɪndɪˈstrʌktəbli/",
        "vi": "một cách không thể phá hủy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086778",
        "hw": "indetectability",
        "pos": "noun",
        "ipa": "/ˌɪndɪˌtɛktəˈbɪləti/",
        "vi": "tính không thể dò tìm phát hiện",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086779",
        "hw": "indetectable",
        "pos": "adj",
        "ipa": "/ˌɪndɪˈtɛktəbəl/",
        "vi": "không thể nhận biết hay phát hiện",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086780",
        "hw": "indeterminableness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈtɚmənəbəlnəs/",
        "vi": "tính không thể xác định rõ ràng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086781",
        "hw": "indeterminably",
        "pos": "adv",
        "ipa": "/ˌɪndɪˈtɚmənəbli/",
        "vi": "một cách không thể định rõ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086782",
        "hw": "indeterminately",
        "pos": "adv",
        "ipa": "/ˌɪndɪˈtɚmənətli/",
        "vi": "một cách vô định; không xác định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086783",
        "hw": "indeterminateness",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈtɚmənətnəs/",
        "vi": "tính bất định; sự mơ hồ không rõ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086784",
        "hw": "indetermination",
        "pos": "noun",
        "ipa": "/ˌɪndɪˌtɚmɪˈneɪʃən/",
        "vi": "sự thiếu quyết đoán; tính bất định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086785",
        "hw": "indeterminism",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈtɚmɪnɪzəm/",
        "vi": "thuyết bất định; thuyết vô định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086786",
        "hw": "indeterminist",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈtɚmɪnɪst/",
        "vi": "người theo thuyết bất định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086787",
        "hw": "indeterministic",
        "pos": "adj",
        "ipa": "/ˌɪndɪˌtɚmɪˈnɪstɪk/",
        "vi": "thuộc thuyết bất định phi tiền định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086788",
        "hw": "indexed",
        "pos": "verb",
        "ipa": "/ˈɪndɛkst/",
        "vi": "đã lập chỉ mục; đã đánh chỉ số",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086789",
        "hw": "indexes",
        "pos": "verb",
        "ipa": "/ˈɪndɛksɪz/",
        "vi": "lập chỉ mục; chỉ dẫn đánh dấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086790",
        "hw": "indexless",
        "pos": "adj",
        "ipa": "/ˈɪndɛksləs/",
        "vi": "không có bảng chỉ mục tra cứu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086791",
        "hw": "indianan",
        "pos": "noun",
        "ipa": "/ˌɪndiˈænən/",
        "vi": "người dân bang Indiana (Mỹ)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086792",
        "hw": "indicant",
        "pos": "noun",
        "ipa": "/ˈɪndɪkənt/",
        "vi": "chỉ dấu; triệu chứng chỉ thị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086793",
        "hw": "indicated",
        "pos": "verb",
        "ipa": "/ˈɪndɪkeɪtɪd/",
        "vi": "đã biểu thị; đã ngụ ý chứng tỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086794",
        "hw": "indicates",
        "pos": "verb",
        "ipa": "/ˈɪndɪkeɪts/",
        "vi": "chỉ ra; biểu thị; chứng tỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086795",
        "hw": "indicating",
        "pos": "verb",
        "ipa": "/ˈɪndɪkeɪtɪŋ/",
        "vi": "đang chỉ ra; đang biểu thị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086796",
        "hw": "indications",
        "pos": "noun",
        "ipa": "/ˌɪndɪˈkeɪʃənz/",
        "vi": "những dấu hiệu; các chỉ báo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086797",
        "hw": "indicatively",
        "pos": "adv",
        "ipa": "/ɪnˈdɪkətɪvli/",
        "vi": "mang tính biểu thị; ngụ ý chỉ ra",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086798",
        "hw": "indicatoridae",
        "pos": "noun",
        "ipa": "/ˌɪndɪkəˈtɔːrɪdiː/",
        "vi": "họ chim chỉ mật (điểu học)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086799",
        "hw": "indicatory",
        "pos": "adj",
        "ipa": "/ˈɪndɪkətɔːri/",
        "vi": "chỉ rõ; mang tính biểu thị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086800",
        "hw": "indices",
        "pos": "noun",
        "ipa": "/ˈɪndɪsiːz/",
        "vi": "các chỉ số; các bảng mục lục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086801",
        "hw": "indicia",
        "pos": "noun",
        "ipa": "/ɪnˈdɪʃiə/",
        "vi": "dấu bưu chính in sẵn; chỉ dấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

if __name__ == "__main__":
    assert len(data) == 100, f"Expected 100, got {len(data)}"
    with open("scratch/b18_r04_raw_p3.json") as f:
        raw = json.load(f)
    assert len(raw) == 100, f"Expected 100 raw, got {len(raw)}"
    for i in range(100):
        d = data[i]
        r = raw[i]
        assert d["id"] == r["id"], f"ID mismatch at {i}: {d['id']} vs {r['id']}"
        assert d["hw"] == r["hw"], f"HW mismatch at {i}: {d['hw']} vs {r['hw']}"
        assert d["cefr"] == r["cefr"], f"CEFR mismatch at {i}: {d['cefr']} vs {r['cefr']}"
        assert d["tier"] == r["tier"], f"TIER mismatch at {i}: {d['tier']} vs {r['tier']}"
        assert d["notes"] == r["notes"], f"NOTES mismatch at {i}: {d['notes']} vs {r['notes']}"
        assert d["status"] == "reviewed", f"Status not reviewed at {i}"
        assert d["ipa"].startswith("/") and d["ipa"].endswith("/") and d["ipa"].count("/") == 2, f"Bad IPA at {i}: {d['ipa']}"
        assert len(d["vi"]) <= 35, f"VI too long at {i} ({len(d['vi'])}): {d['vi']}"
        assert d["pos"] in ["noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"], f"Invalid pos at {i}: {d['pos']}"
    print("ALL 100 RECORDS IN ROUND 4 PART 3 VERIFIED SUCCESSFULLY!")
