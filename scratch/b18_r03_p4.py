# scratch/b18_r03_p4.py
# Batch 18 Round 3 Part 4: records 1300 - 1399 (IDs 086302 - 086401)
import json

data = [
    {
        "id": "lex.en.100k.086302",
        "hw": "improvisational",
        "pos": "adj",
        "ipa": "/ˌɪmprɑːvɪˈzeɪʃənəl/",
        "vi": "(thuộc) sự ứng biến; ngẫu hứng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086303",
        "hw": "improvisator",
        "pos": "noun",
        "ipa": "/ˌɪmprəvɪˈzeɪtər/",
        "vi": "người ứng khẩu; người ứng tác",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086304",
        "hw": "improvisatory",
        "pos": "adj",
        "ipa": "/ˌɪmprəvɪzəˈtɔːri/",
        "vi": "có tính ứng biến; ngẫu hứng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086305",
        "hw": "improviser",
        "pos": "noun",
        "ipa": "/ˈɪmprəvaɪzər/",
        "vi": "người giỏi ứng biến; người ứng tác",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086306",
        "hw": "improvises",
        "pos": "verb",
        "ipa": "/ˈɪmprəvaɪzɪz/",
        "vi": "ứng biến; ứng tác ngẫu hứng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086307",
        "hw": "improvising",
        "pos": "verb",
        "ipa": "/ˈɪmprəvaɪzɪŋ/",
        "vi": "đang ứng biến; đang ứng tác",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086308",
        "hw": "improvize",
        "pos": "verb",
        "ipa": "/ˈɪmprəvaɪz/",
        "vi": "ứng biến; ứng tác (biến thể chữ)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086309",
        "hw": "imprudences",
        "pos": "noun",
        "ipa": "/ɪmˈpruːdənsɪz/",
        "vi": "những hành động thiếu thận trọng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086310",
        "hw": "imprudency",
        "pos": "noun",
        "ipa": "/ɪmˈpruːdənsi/",
        "vi": "sự bất cẩn; tính thiếu thận trọng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086311",
        "hw": "imprudentness",
        "pos": "noun",
        "ipa": "/ɪmˈpruːdəntnəs/",
        "vi": "sự thiếu thận trọng; sự khinh suất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086312",
        "hw": "impudentness",
        "pos": "noun",
        "ipa": "/ˈɪmpjədəntnəs/",
        "vi": "tính trơ trẽn; sự xấc xược",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086313",
        "hw": "impudicity",
        "pos": "noun",
        "ipa": "/ˌɪmpjəˈdɪsəti/",
        "vi": "thói dâm ô; sự vô liêm sỉ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086314",
        "hw": "impugnability",
        "pos": "noun",
        "ipa": "/ɪmˌpjuːnəˈbɪləti/",
        "vi": "tính có thể bị bài bác phản đối",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086315",
        "hw": "impugnable",
        "pos": "adj",
        "ipa": "/ɪmˈpjuːnəbəl/",
        "vi": "có thể bị bác bỏ; đáng nghi vấn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086316",
        "hw": "impugned",
        "pos": "verb",
        "ipa": "/ɪmˈpjuːnd/",
        "vi": "đã bài bác; đã công kích phủ nhận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086317",
        "hw": "impugner",
        "pos": "noun",
        "ipa": "/ɪmˈpjuːnər/",
        "vi": "người bài bác; kẻ công kích",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086318",
        "hw": "impugning",
        "pos": "verb",
        "ipa": "/ɪmˈpjuːnɪŋ/",
        "vi": "đang bài bác; đang công kích",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086319",
        "hw": "impugnment",
        "pos": "noun",
        "ipa": "/ɪmˈpjuːnmənt/",
        "vi": "sự bài bác; lời công kích nghi vấn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086320",
        "hw": "impugns",
        "pos": "verb",
        "ipa": "/ɪmˈpjuːnz/",
        "vi": "bài bác; công kích; nghi vấn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086321",
        "hw": "impuissance",
        "pos": "noun",
        "ipa": "/ɪmˈpwɪsəns/",
        "vi": "sự bất lực; sự suy yếu thế lực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086322",
        "hw": "impuissances",
        "pos": "noun",
        "ipa": "/ɪmˈpwɪsənsɪz/",
        "vi": "các tình trạng bất lực; sự yếu kém",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086323",
        "hw": "impuissant",
        "pos": "adj",
        "ipa": "/ɪmˈpwɪsənt/",
        "vi": "bất lực; yếu ớt; không có quyền uy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086324",
        "hw": "impulsivity",
        "pos": "noun",
        "ipa": "/ˌɪmpəlˈsɪvəti/",
        "vi": "tính bốc đồng; tính bộc phát",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086325",
        "hw": "impultative",
        "pos": "adj",
        "ipa": "/ɪmˈpʌltətɪv/",
        "vi": "mang tính quy kết; đổ trách nhiệm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086326",
        "hw": "impultativeness",
        "pos": "noun",
        "ipa": "/ɪmˈpʌltətɪvnəs/",
        "vi": "tính chất quy kết; sự đổ tội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086327",
        "hw": "impurely",
        "pos": "adv",
        "ipa": "/ɪmˈpjʊərli/",
        "vi": "một cách không trong sạch; nhơ bẩn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086328",
        "hw": "impureness",
        "pos": "noun",
        "ipa": "/ɪmˈpjʊərnəs/",
        "vi": "sự không thanh khiết; tính vẩn đục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086329",
        "hw": "imputability",
        "pos": "noun",
        "ipa": "/ɪmˌpjuːtəˈbɪləti/",
        "vi": "khả năng có thể quy trách nhiệm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086330",
        "hw": "imputableness",
        "pos": "noun",
        "ipa": "/ɪmˈpjuːtəbəlnəs/",
        "vi": "tính có thể quy lỗi; trách nhiệm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086331",
        "hw": "imputably",
        "pos": "adv",
        "ipa": "/ɪmˈpjuːtəbli/",
        "vi": "một cách có thể quy trách nhiệm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086332",
        "hw": "imputative",
        "pos": "adj",
        "ipa": "/ɪmˈpjuːtətɪv/",
        "vi": "có tính quy kết; mang tính gán tội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086333",
        "hw": "imputatively",
        "pos": "adv",
        "ipa": "/ɪmˈpjuːtətɪvli/",
        "vi": "theo cách quy gán trách nhiệm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086334",
        "hw": "imputativeness",
        "pos": "noun",
        "ipa": "/ɪmˈpjuːtətɪvnəs/",
        "vi": "tính quy gán; sự đổ trách nhiệm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086335",
        "hw": "imputed",
        "pos": "verb",
        "ipa": "/ɪmˈpjuːtɪd/",
        "vi": "đã quy cho; đã gán trách nhiệm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086336",
        "hw": "imputes",
        "pos": "verb",
        "ipa": "/ɪmˈpjuːts/",
        "vi": "quy cho; gán trách nhiệm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086337",
        "hw": "imputing",
        "pos": "verb",
        "ipa": "/ɪmˈpjuːtɪŋ/",
        "vi": "đang quy cho; đang gán lỗi lầm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086338",
        "hw": "imputrescible",
        "pos": "adj",
        "ipa": "/ˌɪmpjuːˈtrɛsəbəl/",
        "vi": "không thể mục nát; khó thối rữa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086339",
        "hw": "imsouane",
        "pos": "noun",
        "ipa": "/ɪmˈsuːæn/",
        "vi": "thị trấn Imsouane (Ma-rốc)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086340",
        "hw": "inabilities",
        "pos": "noun",
        "ipa": "/ˌɪnəˈbɪlətiz/",
        "vi": "những sự bất lực; các thiếu sót",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086341",
        "hw": "inaccessibleness",
        "pos": "noun",
        "ipa": "/ˌɪnækˈsɛsəbəlnəs/",
        "vi": "sự khó tiếp cận; tính bất khả xâm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086342",
        "hw": "inaccessibly",
        "pos": "adv",
        "ipa": "/ˌɪnækˈsɛsəbli/",
        "vi": "một cách khó tiếp cận; xa xôi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086343",
        "hw": "inaccuracies",
        "pos": "noun",
        "ipa": "/ɪnˈækjərəsiz/",
        "vi": "những điểm sai sót; lỗi sai lệch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086344",
        "hw": "inaccurateness",
        "pos": "noun",
        "ipa": "/ɪnˈækjərɪtnəs/",
        "vi": "tính không chính xác; sự sai lệch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086345",
        "hw": "inachis",
        "pos": "noun",
        "ipa": "/ˈɪnəkɪs/",
        "vi": "chi bướm công Inachis (sinh học)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086346",
        "hw": "inactivated",
        "pos": "verb",
        "ipa": "/ɪnˈæktɪveɪtɪd/",
        "vi": "đã vô hiệu hóa; đã giải ngũ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086347",
        "hw": "inactivates",
        "pos": "verb",
        "ipa": "/ɪnˈæktɪveɪts/",
        "vi": "vô hiệu hóa; làm ngưng hoạt động",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086348",
        "hw": "inactivating",
        "pos": "verb",
        "ipa": "/ɪnˈæktɪveɪtɪŋ/",
        "vi": "đang vô hiệu hóa; đang giải ngũ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086349",
        "hw": "inactively",
        "pos": "adv",
        "ipa": "/ɪnˈæktɪvli/",
        "vi": "một cách thụ động; không hoạt động",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086350",
        "hw": "inactiveness",
        "pos": "noun",
        "ipa": "/ɪnˈæktɪvnəs/",
        "vi": "tình trạng bất hoạt; sự thụ động",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086351",
        "hw": "inadaptability",
        "pos": "noun",
        "ipa": "/ˌɪnədæptəˈbɪləti/",
        "vi": "tính không thể thích nghi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086352",
        "hw": "inadaptable",
        "pos": "adj",
        "ipa": "/ˌɪnəˈdæptəbəl/",
        "vi": "không thể thích nghi; khó hòa nhập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086353",
        "hw": "inadequacies",
        "pos": "noun",
        "ipa": "/ɪnˈædɪkwəsiz/",
        "vi": "những điểm thiếu sót; bất cập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086354",
        "hw": "inadequateness",
        "pos": "noun",
        "ipa": "/ɪnˈædɪkwɪtnəs/",
        "vi": "sự không thỏa đáng; sự thiếu thốn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086355",
        "hw": "inadhesive",
        "pos": "adj",
        "ipa": "/ˌɪnədˈhiːsɪv/",
        "vi": "không dính; không bám dính",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086356",
        "hw": "inadmissibilities",
        "pos": "noun",
        "ipa": "/ˌɪnədmɪsəˈbɪlətiz/",
        "vi": "các điều không thể chấp nhận được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086357",
        "hw": "inadmissibly",
        "pos": "adv",
        "ipa": "/ˌɪnədˈmɪsəbli/",
        "vi": "một cách không thể chấp nhận được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086358",
        "hw": "inadvertency",
        "pos": "noun",
        "ipa": "/ˌɪnədˈvɚtənsi/",
        "vi": "sự vô ý; tính sơ suất sơ ý",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086359",
        "hw": "inadvisability",
        "pos": "noun",
        "ipa": "/ˌɪnədˌvaɪzəˈbɪləti/",
        "vi": "sự không nên làm; tính dại dột",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086360",
        "hw": "inadvisableness",
        "pos": "noun",
        "ipa": "/ˌɪnədˈvaɪzəbəlnəs/",
        "vi": "sự không nên làm; tính bất khả thi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086361",
        "hw": "inadvisably",
        "pos": "adv",
        "ipa": "/ˌɪnədˈvaɪzəbli/",
        "vi": "một cách không nên; dại dột",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086362",
        "hw": "inaesthetic",
        "pos": "adj",
        "ipa": "/ˌɪnɛsˈθɛtɪk/",
        "vi": "thiếu thẩm mỹ; phản thẩm mỹ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086363",
        "hw": "inalienability",
        "pos": "noun",
        "ipa": "/ɪnˌeɪliənəˈbɪləti/",
        "vi": "tính không thể chuyển nhượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086364",
        "hw": "inalienableness",
        "pos": "noun",
        "ipa": "/ɪnˈeɪliənəbəlnəs/",
        "vi": "tính bất khả chuyển nhượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086365",
        "hw": "inalterability",
        "pos": "noun",
        "ipa": "/ɪnˌɔːltərəˈbɪləti/",
        "vi": "tính không thể thay đổi; bất biến",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086366",
        "hw": "inalterable",
        "pos": "adj",
        "ipa": "/ɪnˈɔːltərəbəl/",
        "vi": "không thể thay đổi; bất di bất dịch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086367",
        "hw": "inalterableness",
        "pos": "noun",
        "ipa": "/ɪnˈɔːltərəbəlnəs/",
        "vi": "sự bất biến; tính cố định mãi mãi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086368",
        "hw": "inalterably",
        "pos": "adv",
        "ipa": "/ɪnˈɔːltərəbli/",
        "vi": "một cách bất biến; không đổi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086369",
        "hw": "inamorato",
        "pos": "noun",
        "ipa": "/ɪˌnæməˈrɑːtoʊ/",
        "vi": "người tình nam; tình nhân nam",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086370",
        "hw": "inanimately",
        "pos": "adv",
        "ipa": "/ɪnˈænəmɪtli/",
        "vi": "một cách vô tri vô giác; đờ đẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086371",
        "hw": "inanimateness",
        "pos": "noun",
        "ipa": "/ɪnˈænəmɪtnəs/",
        "vi": "tính vô tri; trạng thái không hồn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086372",
        "hw": "inanimation",
        "pos": "noun",
        "ipa": "/ɪnˌænəˈmeɪʃən/",
        "vi": "sự thiếu sinh khí; vẻ đờ đẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086373",
        "hw": "inanities",
        "pos": "noun",
        "ipa": "/ɪnˈænətiz/",
        "vi": "những chuyện vô bổ; lời nhảm nhí",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086374",
        "hw": "inanition",
        "pos": "noun",
        "ipa": "/ˌɪnəˈnɪʃən/",
        "vi": "sự kiệt sức do đói khát suy nhược",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086375",
        "hw": "inappeasable",
        "pos": "adj",
        "ipa": "/ˌɪnəˈpiːzəbəl/",
        "vi": "không thể xoa dịu; khôn nguôi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086376",
        "hw": "inappetence",
        "pos": "noun",
        "ipa": "/ɪnˈæpɪtəns/",
        "vi": "chứng chán ăn; sự không muốn ăn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086377",
        "hw": "inappetency",
        "pos": "noun",
        "ipa": "/ɪnˈæpɪtənsi/",
        "vi": "chứng mất cảm giác thèm ăn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086378",
        "hw": "inapplicableness",
        "pos": "noun",
        "ipa": "/ɪnˈæplɪkəbəlnəs/",
        "vi": "tính không thể áp dụng được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086379",
        "hw": "inapplicably",
        "pos": "adv",
        "ipa": "/ɪnˈæplɪkəbli/",
        "vi": "một cách không thể áp dụng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086380",
        "hw": "inappositely",
        "pos": "adv",
        "ipa": "/ɪnˈæpəzɪtli/",
        "vi": "một cách không thích hợp; lạc lõng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086381",
        "hw": "inappositeness",
        "pos": "noun",
        "ipa": "/ɪnˈæpəzɪtnəs/",
        "vi": "sự không thích đáng; không ăn nhập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086382",
        "hw": "inappreciable",
        "pos": "adj",
        "ipa": "/ˌɪnəˈpriːʃəbəl/",
        "vi": "không đáng kể; quá nhỏ khó thấy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086383",
        "hw": "inappreciably",
        "pos": "adv",
        "ipa": "/ˌɪnəˈpriːʃəbli/",
        "vi": "một cách không đáng kể; rất ít",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086384",
        "hw": "inappreciation",
        "pos": "noun",
        "ipa": "/ˌɪnəˌpriːʃiˈeɪʃən/",
        "vi": "sự không nhận biết giá trị; vô ơn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086385",
        "hw": "inappreciative",
        "pos": "adj",
        "ipa": "/ˌɪnəˈpriːʃiətɪv/",
        "vi": "thiếu trân trọng; không biết ơn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086386",
        "hw": "inappreciatively",
        "pos": "adv",
        "ipa": "/ˌɪnəˈpriːʃiətɪvli/",
        "vi": "một cách thiếu trân trọng; thờ ơ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086387",
        "hw": "inappreciativeness",
        "pos": "noun",
        "ipa": "/ˌɪnəˈpriːʃiətɪvnəs/",
        "vi": "sự thiếu đánh giá cao; sự thờ ơ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086388",
        "hw": "inapprehensible",
        "pos": "adj",
        "ipa": "/ˌɪnæprɪˈhɛnsəbəl/",
        "vi": "không thể lĩnh hội; khó hiểu thấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086389",
        "hw": "inapprehension",
        "pos": "noun",
        "ipa": "/ˌɪnæprɪˈhɛnʃən/",
        "vi": "sự không hiểu thấu; sự chậm hiểu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086390",
        "hw": "inapprehensive",
        "pos": "adj",
        "ipa": "/ˌɪnæprɪˈhɛnsɪv/",
        "vi": "chậm hiểu; không hề âu lo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086391",
        "hw": "inapprehensiveness",
        "pos": "noun",
        "ipa": "/ˌɪnæprɪˈhɛnsɪvnəs/",
        "vi": "sự kém hiểu biết; không chút lo âu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086392",
        "hw": "inapproachability",
        "pos": "noun",
        "ipa": "/ˌɪnəˌproʊtʃəˈbɪləti/",
        "vi": "tính khó gần; sự khó tiếp cận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086393",
        "hw": "inapproachable",
        "pos": "adj",
        "ipa": "/ˌɪnəˈproʊtʃəbəl/",
        "vi": "khó gần gũi; không thể tới gần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086394",
        "hw": "inapproachably",
        "pos": "adv",
        "ipa": "/ˌɪnəˈproʊtʃəbli/",
        "vi": "một cách khó gần; xa cách kiêu kỳ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086395",
        "hw": "inaptitude",
        "pos": "noun",
        "ipa": "/ɪnˈæptɪtuːd/",
        "vi": "sự bất tài; tính thiếu khả năng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086396",
        "hw": "inaptitudes",
        "pos": "noun",
        "ipa": "/ɪnˈæptɪtuːdz/",
        "vi": "những mặt bất tài; điểm thiếu hụt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086397",
        "hw": "inaptly",
        "pos": "adv",
        "ipa": "/ɪnˈæptli/",
        "vi": "một cách không phù hợp; vụng về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086398",
        "hw": "inaptness",
        "pos": "noun",
        "ipa": "/ɪnˈæptnəs/",
        "vi": "sự không thích hợp; tính vụng về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086399",
        "hw": "inarch",
        "pos": "verb",
        "ipa": "/ɪnˈɑːrtʃ/",
        "vi": "ghép cành áp (kỹ thuật ghép cây)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086400",
        "hw": "inarm",
        "pos": "verb",
        "ipa": "/ɪnˈɑːrm/",
        "vi": "ôm chặt trong tay; ôm ghì",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086401",
        "hw": "inartful",
        "pos": "adj",
        "ipa": "/ɪnˈɑːrtfəl/",
        "vi": "vụng về; chất phác mộc mạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

if __name__ == "__main__":
    assert len(data) == 100, f"Expected 100, got {len(data)}"
    with open("scratch/b18_r03_raw_p4.json") as f:
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
    print("ALL 100 RECORDS IN ROUND 3 PART 4 VERIFIED SUCCESSFULLY!")
