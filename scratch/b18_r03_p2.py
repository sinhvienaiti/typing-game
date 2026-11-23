# scratch/b18_r03_p2.py
# Batch 18 Round 3 Part 2: records 1100 - 1199 (IDs 086102 - 086201)
import json

data = [
    {
        "id": "lex.en.100k.086102",
        "hw": "impendency",
        "pos": "noun",
        "ipa": "/ɪmˈpɛndənsi/",
        "vi": "sự sắp xảy ra; mối nguy cận kề",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086103",
        "hw": "impendent",
        "pos": "adj",
        "ipa": "/ɪmˈpɛndənt/",
        "vi": "sắp xảy ra; lơ lửng đe dọa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086104",
        "hw": "impends",
        "pos": "verb",
        "ipa": "/ɪmˈpɛndz/",
        "vi": "sắp xảy ra; lơ lửng đe dọa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086105",
        "hw": "impenetrableness",
        "pos": "noun",
        "ipa": "/ɪmˈpɛnɪtrəbəlnəs/",
        "vi": "tính không thể xuyên qua; khó hiểu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086106",
        "hw": "impenetrably",
        "pos": "adv",
        "ipa": "/ɪmˈpɛnɪtrəbli/",
        "vi": "một cách không thể xuyên thấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086107",
        "hw": "impenetrate",
        "pos": "verb",
        "ipa": "/ɪmˈpɛnɪtreɪt/",
        "vi": "xuyên qua; thâm nhập sâu vào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086108",
        "hw": "impenitence",
        "pos": "noun",
        "ipa": "/ɪmˈpɛnɪtəns/",
        "vi": "sự không ăn năn; tính ngoan cố",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086109",
        "hw": "impenitency",
        "pos": "noun",
        "ipa": "/ɪmˈpɛnɪtənsi/",
        "vi": "tính không hối hận; sự ngoan cố",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086110",
        "hw": "impenitently",
        "pos": "adv",
        "ipa": "/ɪmˈpɛnɪtəntli/",
        "vi": "một cách ngoan cố; không ăn năn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086111",
        "hw": "impenitentness",
        "pos": "noun",
        "ipa": "/ɪmˈpɛnɪtəntnəs/",
        "vi": "sự không hối cải; tính ngoan cố",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086112",
        "hw": "impennate",
        "pos": "adj",
        "ipa": "/ɪmˈpɛneɪt/",
        "vi": "không có cánh bay (loài chim)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086113",
        "hw": "imperatival",
        "pos": "adj",
        "ipa": "/ɪmˌpɛrəˈtaɪvəl/",
        "vi": "(thuộc) thức mệnh lệnh (ngữ pháp)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086114",
        "hw": "imperativeness",
        "pos": "noun",
        "ipa": "/ɪmˈpɛrətɪvnəs/",
        "vi": "tính cấp bách; tính khẩn thiết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086115",
        "hw": "imperatives",
        "pos": "noun",
        "ipa": "/ɪmˈpɛrətɪvz/",
        "vi": "những yêu cầu cấp thiết; câu lệnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086116",
        "hw": "imperator",
        "pos": "noun",
        "ipa": "/ˌɪmpəˈreɪtər/",
        "vi": "thống soái; hoàng đế La Mã",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086117",
        "hw": "imperatorial",
        "pos": "adj",
        "ipa": "/ˌɪmpərəˈtɔːriəl/",
        "vi": "(thuộc) hoàng đế; thống soái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086118",
        "hw": "imperceptibility",
        "pos": "noun",
        "ipa": "/ɪmˌpɚˌsɛptəˈbɪlɪti/",
        "vi": "tính không thể cảm nhận được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086119",
        "hw": "imperceptibleness",
        "pos": "noun",
        "ipa": "/ɪmˌpɚˌsɛptəbəlnəs/",
        "vi": "tính không thể nhận thấy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086120",
        "hw": "imperception",
        "pos": "noun",
        "ipa": "/ˌɪmpɚˈsɛpʃən/",
        "vi": "sự thiếu nhạy cảm; kém nhận thức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086121",
        "hw": "imperceptive",
        "pos": "adj",
        "ipa": "/ˌɪmpɚˈsɛptɪv/",
        "vi": "thiếu nhạy bén; kém nhận thức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086122",
        "hw": "imperceptiveness",
        "pos": "noun",
        "ipa": "/ˌɪmpɚˈsɛptɪvnəs/",
        "vi": "sự thiếu nhạy bén; kém tinh tế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086123",
        "hw": "imperceptivity",
        "pos": "noun",
        "ipa": "/ˌɪmpɚsɛpˈtɪvɪti/",
        "vi": "tính thiếu nhạy bén; kém tinh ý",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086124",
        "hw": "impercipience",
        "pos": "noun",
        "ipa": "/ˌɪmpɚˈsɪpiəns/",
        "vi": "sự kém nhạy bén; thiếu cảm nhận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086125",
        "hw": "impercipient",
        "pos": "adj",
        "ipa": "/ˌɪmpɚˈsɪpiənt/",
        "vi": "kém nhạy bén; khó nhận thức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086126",
        "hw": "imperence",
        "pos": "noun",
        "ipa": "/ˈɪmpərəns/",
        "vi": "thói trơ tráo; tính vô liêm sỉ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086127",
        "hw": "imperfectibility",
        "pos": "noun",
        "ipa": "/ɪmˌpɚfɛktəˈbɪlɪti/",
        "vi": "tính không thể đạt tới hoàn hảo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086128",
        "hw": "imperfectible",
        "pos": "adj",
        "ipa": "/ˌɪmpɚˈfɛktəbəl/",
        "vi": "không thể hoàn thiện tuyệt đối",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086129",
        "hw": "imperfections",
        "pos": "noun",
        "ipa": "/ˌɪmpɚˈfɛkʃənz/",
        "vi": "những khiếm khuyết; các vết lỗi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086130",
        "hw": "imperfectness",
        "pos": "noun",
        "ipa": "/ɪmˈpɚfɪktnəs/",
        "vi": "tính khiếm khuyết; sự bất toàn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086131",
        "hw": "imperforation",
        "pos": "noun",
        "ipa": "/ɪmˌpɚfəˈreɪʃən/",
        "vi": "chứng tịt lỗ bẩm sinh (y học)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086132",
        "hw": "imperialisation",
        "pos": "noun",
        "ipa": "/ɪmˌpɪriəlaɪˈzeɪʃən/",
        "vi": "sự đế quốc hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086133",
        "hw": "imperialise",
        "pos": "verb",
        "ipa": "/ɪmˈpɪriəlaɪz/",
        "vi": "đế quốc hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086134",
        "hw": "imperialisms",
        "pos": "noun",
        "ipa": "/ɪmˈpɪriəlɪzəmz/",
        "vi": "các chính sách đế quốc chủ nghĩa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086135",
        "hw": "imperialistically",
        "pos": "adv",
        "ipa": "/ɪmˌpɪriəˈlɪstɪkli/",
        "vi": "theo kiểu đế quốc chủ nghĩa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086136",
        "hw": "imperialization",
        "pos": "noun",
        "ipa": "/ɪmˌpɪriələˈzeɪʃən/",
        "vi": "sự đế quốc hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086137",
        "hw": "imperialize",
        "pos": "verb",
        "ipa": "/ɪmˈpɪriəlaɪz/",
        "vi": "đế quốc hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086138",
        "hw": "imperialness",
        "pos": "noun",
        "ipa": "/ɪmˈpɪriəlnəs/",
        "vi": "phong thái hoàng gia; vẻ uy nghiêm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086139",
        "hw": "imperilings",
        "pos": "noun",
        "ipa": "/ɪmˈpɛrəlɪŋz/",
        "vi": "những hành động gây hiểm nguy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086140",
        "hw": "imperilled",
        "pos": "verb",
        "ipa": "/ɪmˈpɛrəld/",
        "vi": "đã đẩy vào cảnh hiểm nghèo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086141",
        "hw": "imperilling",
        "pos": "verb",
        "ipa": "/ɪmˈpɛrəlɪŋ/",
        "vi": "đang đẩy vào thế hiểm nghèo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086142",
        "hw": "imperilment",
        "pos": "noun",
        "ipa": "/ɪmˈpɛrəlmənt/",
        "vi": "sự đẩy vào thế hiểm nguy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086143",
        "hw": "imperils",
        "pos": "verb",
        "ipa": "/ɪmˈpɛrəlz/",
        "vi": "đẩy vào cảnh hiểm nguy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086144",
        "hw": "imperishability",
        "pos": "noun",
        "ipa": "/ɪmˌpɛrɪʃəˈbɪlɪti/",
        "vi": "tính không hư nát; sự bất diệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086145",
        "hw": "imperishableness",
        "pos": "noun",
        "ipa": "/ɪmˈpɛrɪʃəbəlnəs/",
        "vi": "tính bất hoại; sự trường cửu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086146",
        "hw": "imperishably",
        "pos": "adv",
        "ipa": "/ɪmˈpɛrɪʃəbli/",
        "vi": "một cách bất diệt; muôn thuở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086147",
        "hw": "imperishingness",
        "pos": "noun",
        "ipa": "/ɪmˈpɛrɪʃɪŋnəs/",
        "vi": "tính không tàn lụi; sự bất hoại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086148",
        "hw": "impermanency",
        "pos": "noun",
        "ipa": "/ɪmˈpɚmənənsi/",
        "vi": "tính vô thường; sự tạm bợ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086149",
        "hw": "impermeableness",
        "pos": "noun",
        "ipa": "/ɪmˈpɚmiəbəlnəs/",
        "vi": "tính không thấm qua được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086150",
        "hw": "impermeably",
        "pos": "adv",
        "ipa": "/ɪmˈpɚmiəbli/",
        "vi": "một cách không thấm nước",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086151",
        "hw": "impermissibilities",
        "pos": "noun",
        "ipa": "/ɪmpɚˌmɪsəˈbɪlɪtiz/",
        "vi": "những điều cấm; sự không được phép",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086152",
        "hw": "impermissibility",
        "pos": "noun",
        "ipa": "/ɪmpɚˌmɪsəˈbɪlɪti/",
        "vi": "tính không được phép; điều cấm kỵ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086153",
        "hw": "imperscriptible",
        "pos": "adj",
        "ipa": "/ɪmpɚˈskrɪptəbəl/",
        "vi": "bất thành văn; không ghi chép lại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086154",
        "hw": "impersonalisation",
        "pos": "noun",
        "ipa": "/ɪmˌpɚsənəlaɪˈzeɪʃən/",
        "vi": "sự phi nhân tính hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086155",
        "hw": "impersonalise",
        "pos": "verb",
        "ipa": "/ɪmˈpɚsənəlaɪz/",
        "vi": "phi nhân tính hóa; làm mất cá tính",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086156",
        "hw": "impersonalism",
        "pos": "noun",
        "ipa": "/ɪmˈpɚsənəlɪzəm/",
        "vi": "chủ nghĩa phi cá nhân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086157",
        "hw": "impersonality",
        "pos": "noun",
        "ipa": "/ˌɪmpˌɜːrsənˈæləti/",
        "vi": "tính khách quan; sự thiếu cá tính",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086158",
        "hw": "impersonalization",
        "pos": "noun",
        "ipa": "/ɪmˌpɚsənələˈzeɪʃən/",
        "vi": "sự phi nhân tính hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086159",
        "hw": "impersonalize",
        "pos": "verb",
        "ipa": "/ɪmˈpɚsənəlaɪz/",
        "vi": "phi nhân tính hóa; tước bỏ cá tính",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086160",
        "hw": "impersonated",
        "pos": "verb",
        "ipa": "/ˌɪmpˈɜːrsənˌeɪtɪd/",
        "vi": "đã giả mạo; đã đóng giả",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086161",
        "hw": "impersonates",
        "pos": "verb",
        "ipa": "/ˌɪmpˈɜːrsənˌeɪts/",
        "vi": "giả mạo; đóng vai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086162",
        "hw": "impersonating",
        "pos": "verb",
        "ipa": "/ˌɪmpˈɜːrsənˌeɪtɪŋ/",
        "vi": "đang giả mạo; đang đóng vai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086163",
        "hw": "impersonative",
        "pos": "adj",
        "ipa": "/ɪmˈpɚsənətɪv/",
        "vi": "mang tính nhân cách hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086164",
        "hw": "impersonify",
        "pos": "verb",
        "ipa": "/ɪmpɚˈsɑːnəfaɪ/",
        "vi": "nhân cách hóa; là hiện thân của",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086165",
        "hw": "impertinences",
        "pos": "noun",
        "ipa": "/ɪmˈpɚtnənsɪz/",
        "vi": "những lời xấc xược; điều xấc láo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086166",
        "hw": "impertinency",
        "pos": "noun",
        "ipa": "/ɪmˈpɚtnənsi/",
        "vi": "sự láo xược; tính xấc láo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086167",
        "hw": "impertinentness",
        "pos": "noun",
        "ipa": "/ɪmˈpɚtnəntnəs/",
        "vi": "sự vô lễ; tính xấc xược",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086168",
        "hw": "imperturbableness",
        "pos": "noun",
        "ipa": "/ɪmpɚˈtɚbəbəlnəs/",
        "vi": "sự điềm nhiên; tính bình thản",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086169",
        "hw": "imperturbably",
        "pos": "adv",
        "ipa": "/ɪmpɚˈtɚbəbli/",
        "vi": "một cách điềm tĩnh; thản nhiên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086170",
        "hw": "imperturbation",
        "pos": "noun",
        "ipa": "/ˌɪmpɚtɚˈbeɪʃən/",
        "vi": "sự điềm tĩnh; tâm bất biến",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086171",
        "hw": "imperviable",
        "pos": "adj",
        "ipa": "/ɪmˈpɚviəbəl/",
        "vi": "không xuyên qua được; miễn nhiễm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086172",
        "hw": "imperviously",
        "pos": "adv",
        "ipa": "/ɪmˈpɚviəsli/",
        "vi": "một cách trơ lì; không lay chuyển",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086173",
        "hw": "impetiginous",
        "pos": "adj",
        "ipa": "/ˌɪmpɪˈtɪdʒɪnəs/",
        "vi": "(thuộc) bệnh chốc lở ngoài da",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086174",
        "hw": "impetrate",
        "pos": "verb",
        "ipa": "/ˈɪmpɪtreɪt/",
        "vi": "khẩn cầu; nài xin được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086175",
        "hw": "impetration",
        "pos": "noun",
        "ipa": "/ˌɪmpɪˈtreɪʃən/",
        "vi": "sự khẩn nài; lời cầu xin đạt được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086176",
        "hw": "impetrative",
        "pos": "adj",
        "ipa": "/ˈɪmpɪtreɪtɪv/",
        "vi": "mang tính khẩn cầu; nài xin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086177",
        "hw": "impetrator",
        "pos": "noun",
        "ipa": "/ˈɪmpɪtreɪtər/",
        "vi": "người khẩn cầu; người nài xin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086178",
        "hw": "imphees",
        "pos": "noun",
        "ipa": "/ɪmˈfiːz/",
        "vi": "các giống mía miến đường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086179",
        "hw": "impieties",
        "pos": "noun",
        "ipa": "/ɪmˈpaɪətiz/",
        "vi": "những hành vi bất kính; điều vô đạo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086180",
        "hw": "impiousness",
        "pos": "noun",
        "ipa": "/ˈɪmpiəsnəs/",
        "vi": "sự bất kính thần thánh; sự vô đạo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086181",
        "hw": "impishness",
        "pos": "noun",
        "ipa": "/ˈɪmpɪʃnəs/",
        "vi": "tính tinh nghịch; thói ranh mãnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086182",
        "hw": "impiteous",
        "pos": "adj",
        "ipa": "/ɪmˈpɪtiəs/",
        "vi": "nhẫn tâm; không thương xót",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086183",
        "hw": "implacability",
        "pos": "noun",
        "ipa": "/ɪmˌplækəˈbɪlɪti/",
        "vi": "tính không thể xoa dịu; sự sắt đá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086184",
        "hw": "implacableness",
        "pos": "noun",
        "ipa": "/ɪmˈplækəbəlnəs/",
        "vi": "sự không khoan nhượng; sự sắt đá",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086185",
        "hw": "implacably",
        "pos": "adv",
        "ipa": "/ɪmˈplækəbli/",
        "vi": "một cách kiên quyết không nguôi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086186",
        "hw": "implacental",
        "pos": "adj",
        "ipa": "/ˌɪmpləˈsɛntəl/",
        "vi": "không có nhau thai (động vật)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086187",
        "hw": "implacentate",
        "pos": "adj",
        "ipa": "/ˌɪmpləˈsɛnteɪt/",
        "vi": "thuộc loài không nhau thai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086188",
        "hw": "implantable",
        "pos": "adj",
        "ipa": "/ˈɪmplˌæntəbəl/",
        "vi": "có thể cấy ghép vào cơ thể",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086189",
        "hw": "implanting",
        "pos": "verb",
        "ipa": "/ˌɪmplˈæntɪŋ/",
        "vi": "đang cấy ghép; đang khắc sâu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086190",
        "hw": "implants",
        "pos": "verb",
        "ipa": "/ˌɪmplˈænts/",
        "vi": "cấy ghép; khắc sâu vào tâm trí",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086191",
        "hw": "implausibleness",
        "pos": "noun",
        "ipa": "/ɪmˈplɔːzəbəlnəs/",
        "vi": "sự khó tin; tính khó xảy ra",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086192",
        "hw": "implead",
        "pos": "verb",
        "ipa": "/ɪmˈpliːd/",
        "vi": "khởi tố kiện tụng; đưa ra tòa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086193",
        "hw": "impleadable",
        "pos": "adj",
        "ipa": "/ɪmˈpliːdəbəl/",
        "vi": "có thể bị khởi kiện; truy cứu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086194",
        "hw": "impledge",
        "pos": "verb",
        "ipa": "/ɪmˈplɛdʒ/",
        "vi": "cầm cố; đem gán nợ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086195",
        "hw": "implemental",
        "pos": "adj",
        "ipa": "/ˌɪmpləˈmɛntəl/",
        "vi": "làm công cụ; đóng vai trò hỗ trợ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086196",
        "hw": "implementary",
        "pos": "adj",
        "ipa": "/ˌɪmpləˈmɛntəri/",
        "vi": "phục vụ thi hành; làm phương tiện",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086197",
        "hw": "implementer",
        "pos": "noun",
        "ipa": "/ˈɪmpləmɛntər/",
        "vi": "người thực hiện; bên triển khai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086198",
        "hw": "implementing",
        "pos": "verb",
        "ipa": "/ˈɪmpləmˌɛntɪŋ/",
        "vi": "đang thực thi; đang triển khai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086199",
        "hw": "implements",
        "pos": "verb",
        "ipa": "/ˈɪmpləmənts/",
        "vi": "thực hiện; thi hành; triển khai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086200",
        "hw": "impletion",
        "pos": "noun",
        "ipa": "/ɪmˈpliːʃən/",
        "vi": "sự làm cho tràn đầy; trạng thái đầy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086201",
        "hw": "implicates",
        "pos": "verb",
        "ipa": "/ˈɪmplɪkˌeɪts/",
        "vi": "lôi kéo vào; làm dính líu đến",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

if __name__ == "__main__":
    assert len(data) == 100, f"Expected 100, got {len(data)}"
    with open("scratch/b18_r03_raw_p2.json") as f:
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
    print("ALL 100 RECORDS IN ROUND 3 PART 2 VERIFIED SUCCESSFULLY!")
