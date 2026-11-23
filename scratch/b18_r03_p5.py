# scratch/b18_r03_p5.py
# Batch 18 Round 3 Part 5: records 1400 - 1499 (IDs 086402 - 086501)
import json

data = [
    {
        "id": "lex.en.100k.086402",
        "hw": "inarticulacy",
        "pos": "noun",
        "ipa": "/ˌɪnɑːrˈtɪkjələsi/",
        "vi": "tính ấp úng; sự nói năng không rõ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086403",
        "hw": "inarticulateness",
        "pos": "noun",
        "ipa": "/ˌɪnɑːrˈtɪkjələtnəs/",
        "vi": "sự ấp úng; tính khó diễn đạt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086404",
        "hw": "inartificial",
        "pos": "adj",
        "ipa": "/ˌɪnˌɑːrtəˈfɪʃəl/",
        "vi": "tự nhiên; mộc mạc; không giả tạo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086405",
        "hw": "inartificiality",
        "pos": "noun",
        "ipa": "/ˌɪnˌɑːrtəfɪʃiˈæləti/",
        "vi": "tính chất tự nhiên; sự mộc mạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086406",
        "hw": "inartificially",
        "pos": "adv",
        "ipa": "/ˌɪnˌɑːrtəˈfɪʃəli/",
        "vi": "một cách tự nhiên; mộc mạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086407",
        "hw": "inartificialness",
        "pos": "noun",
        "ipa": "/ˌɪnˌɑːrtəˈfɪʃəlnəs/",
        "vi": "tính tự nhiên; sự chân phương",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086408",
        "hw": "inartistical",
        "pos": "adj",
        "ipa": "/ˌɪnɑːrˈtɪstɪkəl/",
        "vi": "thiếu nghệ thuật; không mỹ quan",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086409",
        "hw": "inartistically",
        "pos": "adv",
        "ipa": "/ˌɪnɑːrˈtɪstɪkli/",
        "vi": "một cách vụng về thiếu thẩm mỹ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086410",
        "hw": "inasmuch",
        "pos": "conj",
        "ipa": "/ɪnəzˈmʌtʃ/",
        "vi": "bởi vì; xét thấy rằng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086411",
        "hw": "inattentions",
        "pos": "noun",
        "ipa": "/ˌɪnəˈtɛnʃənz/",
        "vi": "những lúc lơ đãng; các sơ suất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086412",
        "hw": "inattentively",
        "pos": "adv",
        "ipa": "/ˌɪnəˈtɛntɪvli/",
        "vi": "một cách lơ đãng; thiếu tập trung",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086413",
        "hw": "inaudibility",
        "pos": "noun",
        "ipa": "/ɪnˌɔːdəˈbɪləti/",
        "vi": "tính không thể nghe thấy được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086414",
        "hw": "inaudibleness",
        "pos": "noun",
        "ipa": "/ɪnˈɔːdəbəlnəs/",
        "vi": "sự không nghe thấy; sự im ắng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086415",
        "hw": "inaugurally",
        "pos": "adv",
        "ipa": "/ɪnˈɔːɡjərəli/",
        "vi": "dưới hình thức mở màn khánh thành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086416",
        "hw": "inaugurated",
        "pos": "verb",
        "ipa": "/ɪnˈɔːɡjəreɪtɪd/",
        "vi": "đã khai mạc; đã nhậm chức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086417",
        "hw": "inaugurates",
        "pos": "verb",
        "ipa": "/ɪnˈɔːɡjəreɪts/",
        "vi": "khai mạc; làm lễ nhậm chức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086418",
        "hw": "inaugurating",
        "pos": "verb",
        "ipa": "/ɪnˈɔːɡjəreɪtɪŋ/",
        "vi": "đang khai mạc; đang khánh thành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086419",
        "hw": "inaugurator",
        "pos": "noun",
        "ipa": "/ɪnˈɔːɡjəreɪtər/",
        "vi": "người khai mạc; người khởi xướng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086420",
        "hw": "inauguratory",
        "pos": "adj",
        "ipa": "/ɪnˈɔːɡjərətɔːri/",
        "vi": "thuộc lễ nhậm chức; khai mạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086421",
        "hw": "inauspiciousness",
        "pos": "noun",
        "ipa": "/ˌɪnɔːˈspɪʃəsnəs/",
        "vi": "điềm gở; sự không may mắn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086422",
        "hw": "inauthenticity",
        "pos": "noun",
        "ipa": "/ˌɪnɔːθɛnˈtɪsəti/",
        "vi": "tính giả tạo; sự thiếu chân thực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086423",
        "hw": "inbeing",
        "pos": "noun",
        "ipa": "/ˈɪnˌbiːɪŋ/",
        "vi": "bản chất nội tại; cốt lõi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086424",
        "hw": "inbox",
        "pos": "noun",
        "ipa": "/ˈɪnbɑːks/",
        "vi": "hộp thư đến; hòm thư tiếp nhận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086425",
        "hw": "inbreathe",
        "pos": "verb",
        "ipa": "/ɪnˈbriːð/",
        "vi": "hít vào; truyền cảm hứng vào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086426",
        "hw": "inbreed",
        "pos": "verb",
        "ipa": "/ˈɪnbriːd/",
        "vi": "giao phối cận huyết; lai cận huyết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086427",
        "hw": "inbye",
        "pos": "adj",
        "ipa": "/ˈɪnbaɪ/",
        "vi": "ở sâu trong hầm mỏ; góc hầm lò",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086428",
        "hw": "incalculability",
        "pos": "noun",
        "ipa": "/ɪnˌkælkjələˈbɪləti/",
        "vi": "tính khôn lường; sự vô số kể",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086429",
        "hw": "incalculableness",
        "pos": "noun",
        "ipa": "/ɪnˈkælkjələbəlnəs/",
        "vi": "tính không thể đo đếm tính toán",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086430",
        "hw": "incalculably",
        "pos": "adv",
        "ipa": "/ɪnˈkælkjələbli/",
        "vi": "vô số kể; khôn lường xiết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086431",
        "hw": "incalescence",
        "pos": "noun",
        "ipa": "/ˌɪnkəˈlɛsəns/",
        "vi": "sự nóng dần lên; độ ấm tăng dần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086432",
        "hw": "incandesce",
        "pos": "verb",
        "ipa": "/ˌɪnkænˈdɛs/",
        "vi": "phát sáng rực; nóng đỏ rực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086433",
        "hw": "incandescently",
        "pos": "adv",
        "ipa": "/ˌɪnkænˈdɛsəntli/",
        "vi": "một cách sáng rực; chói lòa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086434",
        "hw": "incantational",
        "pos": "adj",
        "ipa": "/ˌɪnkænˈteɪʃənəl/",
        "vi": "(thuộc) câu thần chú; phù chú",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086435",
        "hw": "incantatory",
        "pos": "adj",
        "ipa": "/ɪnˈkæntətɔːri/",
        "vi": "mang tính phù chú; như niệm chú",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086436",
        "hw": "incapableness",
        "pos": "noun",
        "ipa": "/ɪnˈkeɪpəbəlnəs/",
        "vi": "sự bất tài; tính không có năng lực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086437",
        "hw": "incapably",
        "pos": "adv",
        "ipa": "/ɪnˈkeɪpəbli/",
        "vi": "một cách bất lực; thiếu khả năng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086438",
        "hw": "incapacious",
        "pos": "adj",
        "ipa": "/ˌɪnkəˈpeɪʃəs/",
        "vi": "chật hẹp; dung tích nhỏ hẹp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086439",
        "hw": "incapaciousness",
        "pos": "noun",
        "ipa": "/ˌɪnkəˈpeɪʃəsnəs/",
        "vi": "sự chật chội; dung tích quá hẹp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086440",
        "hw": "incapacitates",
        "pos": "verb",
        "ipa": "/ˌɪnkəˈpæsɪteɪts/",
        "vi": "làm mất năng lực; làm tàn phế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086441",
        "hw": "incapacitation",
        "pos": "noun",
        "ipa": "/ˌɪnkəˌpæsɪˈteɪʃən/",
        "vi": "sự làm mất khả năng; sự tước quyền",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086442",
        "hw": "incarcerated",
        "pos": "verb",
        "ipa": "/ɪnˈkɑːrsəreɪtɪd/",
        "vi": "đã tống giam; đã bỏ tù",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086443",
        "hw": "incarcerates",
        "pos": "verb",
        "ipa": "/ɪnˈkɑːrsəreɪts/",
        "vi": "tống giam; bỏ tù; giam hãm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086444",
        "hw": "incarcerating",
        "pos": "verb",
        "ipa": "/ɪnˈkɑːrsəreɪtɪŋ/",
        "vi": "đang tống giam; đang giam giữ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086445",
        "hw": "incarcerator",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːrsəreɪtər/",
        "vi": "kẻ tống giam; người giam giữ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086446",
        "hw": "incarnadined",
        "pos": "verb",
        "ipa": "/ɪnˈkɑːrnədaɪnd/",
        "vi": "đã nhuộm đỏ màu thịt; nhuộm đỏ máu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086447",
        "hw": "incarnadines",
        "pos": "verb",
        "ipa": "/ɪnˈkɑːrnədaɪnz/",
        "vi": "nhuộm đỏ như máu; làm ửng hồng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086448",
        "hw": "incarnadining",
        "pos": "verb",
        "ipa": "/ɪnˈkɑːrnədaɪnɪŋ/",
        "vi": "đang nhuộm đỏ như máu tươi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086449",
        "hw": "incarnated",
        "pos": "verb",
        "ipa": "/ˈɪnkɑːrneɪtɪd/",
        "vi": "đã hiện thân; đã hóa thân thành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086450",
        "hw": "incarnates",
        "pos": "verb",
        "ipa": "/ˈɪnkɑːrneɪts/",
        "vi": "hiện thân; là hóa thân của",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086451",
        "hw": "incarnating",
        "pos": "verb",
        "ipa": "/ˈɪnkɑːrneɪtɪŋ/",
        "vi": "đang hiện thân; đang hóa thân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086452",
        "hw": "incarnational",
        "pos": "adj",
        "ipa": "/ˌɪnkɑːrˈneɪʃənəl/",
        "vi": "(thuộc) sự nhập thể; hiện thân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086453",
        "hw": "incarnations",
        "pos": "noun",
        "ipa": "/ˌɪnkɑːrˈneɪʃənz/",
        "vi": "những kiếp luân hồi; các hóa thân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086454",
        "hw": "incarnator",
        "pos": "noun",
        "ipa": "/ˈɪnkɑːrneɪtər/",
        "vi": "đấng hiện thân; người làm hóa thân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086455",
        "hw": "incasement",
        "pos": "noun",
        "ipa": "/ɪnˈkeɪsmənt/",
        "vi": "sự bọc kín; sự cho vào hộp đựng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086456",
        "hw": "incaution",
        "pos": "noun",
        "ipa": "/ɪnˈkɔːʃən/",
        "vi": "sự thiếu thận trọng; sự khinh suất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086457",
        "hw": "incautiousness",
        "pos": "noun",
        "ipa": "/ɪnˈkɔːʃəsnəs/",
        "vi": "tính bất cẩn; sự thiếu thận trọng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086458",
        "hw": "incendiarism",
        "pos": "noun",
        "ipa": "/ɪnˈsɛndiərɪzəm/",
        "vi": "tội cố ý phóng hỏa; sự đốt nhà",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086459",
        "hw": "incensation",
        "pos": "noun",
        "ipa": "/ˌɪnsɛnˈseɪʃən/",
        "vi": "nghi thức xông trầm; dâng hương",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086460",
        "hw": "incenses",
        "pos": "verb",
        "ipa": "/ɪnˈsɛnsɪz/",
        "vi": "làm giận điên lên; dâng hương",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086461",
        "hw": "incensing",
        "pos": "verb",
        "ipa": "/ɪnˈsɛnsɪŋ/",
        "vi": "đang làm nổi giận; đang xông hương",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086462",
        "hw": "incenter",
        "pos": "noun",
        "ipa": "/ˈɪnˌsɛntər/",
        "vi": "tâm đường tròn nội tiếp (toán học)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086463",
        "hw": "incentre",
        "pos": "noun",
        "ipa": "/ˈɪnˌsɛntər/",
        "vi": "tâm đường tròn nội tiếp tam giác",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086464",
        "hw": "incept",
        "pos": "verb",
        "ipa": "/ɪnˈsɛpt/",
        "vi": "tiếp nhận; khởi xướng; bắt đầu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086465",
        "hw": "inceptor",
        "pos": "noun",
        "ipa": "/ɪnˈsɛptər/",
        "vi": "người khởi xướng; tân sinh viên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086466",
        "hw": "inceptors",
        "pos": "noun",
        "ipa": "/ɪnˈsɛptərz/",
        "vi": "những người khởi xướng; tân tú tài",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086467",
        "hw": "incertain",
        "pos": "adj",
        "ipa": "/ɪnˈsɜːrtn/",
        "vi": "không chắc chắn; ngờ vực bất định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086468",
        "hw": "incertitudes",
        "pos": "noun",
        "ipa": "/ɪnˈsɜːrtɪtuːdz/",
        "vi": "những nỗi bấp bênh; điều hoài nghi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086469",
        "hw": "incessancy",
        "pos": "noun",
        "ipa": "/ɪnˈsɛsənsi/",
        "vi": "tính liên miên; sự không dứt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086470",
        "hw": "incessantness",
        "pos": "noun",
        "ipa": "/ɪnˈsɛsəntnəs/",
        "vi": "sự không ngừng nghỉ; tính liên tục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086471",
        "hw": "incestuousness",
        "pos": "noun",
        "ipa": "/ɪnˈsɛstʃuəsnəs/",
        "vi": "tính chất loạn luân; sự loạn luân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086472",
        "hw": "inched",
        "pos": "verb",
        "ipa": "/ɪntʃt/",
        "vi": "đã nhích từng chút; đã tiến chậm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086473",
        "hw": "inches",
        "pos": "verb",
        "ipa": "/ˈɪntʃɪz/",
        "vi": "nhích từng bước nhỏ; tiến dần dần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086474",
        "hw": "inching",
        "pos": "verb",
        "ipa": "/ˈɪntʃɪŋ/",
        "vi": "đang nhích từng chút một",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086475",
        "hw": "inchmeal",
        "pos": "adv",
        "ipa": "/ˈɪntʃmiːl/",
        "vi": "từng chút một; dần dà từng li",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086476",
        "hw": "inchoated",
        "pos": "verb",
        "ipa": "/ˈɪnkoʊeɪtɪd/",
        "vi": "đã mới manh nha; đã vừa khởi sự",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086477",
        "hw": "inchoately",
        "pos": "adv",
        "ipa": "/ˈɪnkoʊətli/",
        "vi": "một cách sơ khai; chớm nở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086478",
        "hw": "inchoateness",
        "pos": "noun",
        "ipa": "/ˈɪnkoʊətnəs/",
        "vi": "trạng thái manh nha; tính sơ khai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086479",
        "hw": "inchoates",
        "pos": "verb",
        "ipa": "/ˈɪnkoʊeɪts/",
        "vi": "khởi sự; mới manh nha hình thành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086480",
        "hw": "inchoating",
        "pos": "verb",
        "ipa": "/ˈɪnkoʊeɪtɪŋ/",
        "vi": "đang manh nha; đang chớm nở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086481",
        "hw": "inchoation",
        "pos": "noun",
        "ipa": "/ˌɪnkoʊˈeɪʃən/",
        "vi": "sự khởi xướng; giai đoạn manh nha",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086482",
        "hw": "inchoatively",
        "pos": "adv",
        "ipa": "/ɪnˈkoʊətɪvli/",
        "vi": "mang tính khởi phát hành động",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086483",
        "hw": "incidentalness",
        "pos": "noun",
        "ipa": "/ˌɪnsɪˈdɛntəlnəs/",
        "vi": "tính thứ yếu; tính phụ ngẫu nhiên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086484",
        "hw": "incidentless",
        "pos": "adj",
        "ipa": "/ˈɪnsɪdəntləs/",
        "vi": "bình yên vô sự; không có sự cố",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086485",
        "hw": "incienso",
        "pos": "noun",
        "ipa": "/ɪnˈsjɛnsoʊ/",
        "vi": "cây bụi hương incienso (sa mạc)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086486",
        "hw": "incinerated",
        "pos": "verb",
        "ipa": "/ɪnˈsɪnəreɪtɪd/",
        "vi": "đã thiêu hủy; đã đốt thành tro",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086487",
        "hw": "incinerates",
        "pos": "verb",
        "ipa": "/ɪnˈsɪnəreɪts/",
        "vi": "thiêu hủy; đốt thành tro bụi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086488",
        "hw": "incinerating",
        "pos": "verb",
        "ipa": "/ɪnˈsɪnəreɪtɪŋ/",
        "vi": "đang thiêu hủy; đang đốt thành tro",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086489",
        "hw": "incipience",
        "pos": "noun",
        "ipa": "/ɪnˈsɪpiəns/",
        "vi": "sự bắt đầu manh nha; lúc chớm nở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086490",
        "hw": "incipiency",
        "pos": "noun",
        "ipa": "/ɪnˈsɪpiənsi/",
        "vi": "thời kỳ chớm nở; lúc mới bắt đầu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086491",
        "hw": "incipiently",
        "pos": "adv",
        "ipa": "/ɪnˈsɪpiəntli/",
        "vi": "lúc mới chớm phát; lúc ban đầu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086492",
        "hw": "incipit",
        "pos": "noun",
        "ipa": "/ˈɪnsɪpɪt/",
        "vi": "những từ mở đầu bản thảo cổ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086493",
        "hw": "incises",
        "pos": "verb",
        "ipa": "/ɪnˈsaɪzɪz/",
        "vi": "khắc sâu; rạch đường cắt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086494",
        "hw": "incising",
        "pos": "verb",
        "ipa": "/ɪnˈsaɪzɪŋ/",
        "vi": "đang chạm khắc; đang rạch mổ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086495",
        "hw": "incisura",
        "pos": "noun",
        "ipa": "/ˌɪnsɪˈsjʊərə/",
        "vi": "khuyết lõm; vết khía (giải phẫu)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086496",
        "hw": "incisure",
        "pos": "noun",
        "ipa": "/ɪnˈsɪʒər/",
        "vi": "vết khía lõm; đường rãnh sâu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086497",
        "hw": "incitant",
        "pos": "noun",
        "ipa": "/ɪnˈsaɪtənt/",
        "vi": "chất kích thích; động lực thúc đẩy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086498",
        "hw": "incitation",
        "pos": "noun",
        "ipa": "/ˌɪnsaɪˈteɪʃən/",
        "vi": "sự kích động; hành vi xúi giục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086499",
        "hw": "incited",
        "pos": "verb",
        "ipa": "/ɪnˈsaɪtɪd/",
        "vi": "đã xúi giục; đã kích động bạo lực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086500",
        "hw": "incites",
        "pos": "verb",
        "ipa": "/ɪnˈsaɪts/",
        "vi": "xúi giục; kích động nổi loạn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086501",
        "hw": "inciting",
        "pos": "verb",
        "ipa": "/ɪnˈsaɪtɪŋ/",
        "vi": "đang xúi giục; đang kích động",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

if __name__ == "__main__":
    assert len(data) == 100, f"Expected 100, got {len(data)}"
    with open("scratch/b18_r03_raw_p5.json") as f:
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
    print("ALL 100 RECORDS IN ROUND 3 PART 5 VERIFIED SUCCESSFULLY!")
