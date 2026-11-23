# scratch/b18_r04_p2.py
# Batch 18 Round 4 Part 2: records 1600 - 1699 (IDs 086602 - 086701)
import json

data = [
    {
        "id": "lex.en.100k.086602",
        "hw": "inconsequence",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːnsəkwəns/",
        "vi": "tính chất không quan trọng; vụn vặt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086603",
        "hw": "inconsequences",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːnsəkwənsɪz/",
        "vi": "những chuyện vụn vặt; điều phi lý",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086604",
        "hw": "inconsequent",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːnsəkwənt/",
        "vi": "không quan trọng; thiếu mạch lạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086605",
        "hw": "inconsequentia",
        "pos": "noun",
        "ipa": "/ˌɪnkɑːnsəˈkwɛnʃiə/",
        "vi": "những điều vô lý vụn vặt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086606",
        "hw": "inconsequentiality",
        "pos": "noun",
        "ipa": "/ɪnˌkɑːnsəˌkwɛnʃiˈæləti/",
        "vi": "tính vụn vặt; sự không quan trọng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086607",
        "hw": "inconsequently",
        "pos": "adv",
        "ipa": "/ɪnˈkɑːnsəkwəntli/",
        "vi": "một cách rời rạc; thiếu liên kết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086608",
        "hw": "inconsequentness",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːnsəkwəntnəs/",
        "vi": "tính rời rạc; sự thiếu mạch lạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086609",
        "hw": "inconsiderableness",
        "pos": "noun",
        "ipa": "/ˌɪnkənˈsɪdərəbəlnəs/",
        "vi": "tính không đáng kể; sự nhỏ nhặt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086610",
        "hw": "inconsiderably",
        "pos": "adv",
        "ipa": "/ˌɪnkənˈsɪdərəbli/",
        "vi": "một cách không đáng kể; rất ít",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086611",
        "hw": "inconsiderateness",
        "pos": "noun",
        "ipa": "/ˌɪnkənˈsɪdərɪtnəs/",
        "vi": "sự vô tâm; tính thiếu chu đáo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086612",
        "hw": "inconsistence",
        "pos": "noun",
        "ipa": "/ˌɪnkənˈsɪstəns/",
        "vi": "sự bất nhất; tính mâu thuẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086613",
        "hw": "inconsolability",
        "pos": "noun",
        "ipa": "/ɪnkənˌsoʊləˈbɪləti/",
        "vi": "nỗi đau khôn nguôi; sự sầu thảm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086614",
        "hw": "inconsolableness",
        "pos": "noun",
        "ipa": "/ɪnkənˈsoʊləbəlnəs/",
        "vi": "nỗi buồn không thể nguôi ngoai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086615",
        "hw": "inconsolably",
        "pos": "adv",
        "ipa": "/ɪnkənˈsoʊləbli/",
        "vi": "một cách khôn nguôi; thảm thiết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086616",
        "hw": "inconsonance",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːnsənəns/",
        "vi": "sự chối tai; tính không hòa hợp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086617",
        "hw": "inconsonant",
        "pos": "adj",
        "ipa": "/ɪnˈkɑːnsənənt/",
        "vi": "chói tai; không hòa hợp; trái ngược",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086618",
        "hw": "inconsonantly",
        "pos": "adv",
        "ipa": "/ɪnˈkɑːnsənəntli/",
        "vi": "một cách chói tai; không ăn khớp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086619",
        "hw": "inconspicuousness",
        "pos": "noun",
        "ipa": "/ˌɪnkənˈspɪkjuəsnəs/",
        "vi": "tính kín đáo; sự khó nhận thấy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086620",
        "hw": "inconstantly",
        "pos": "adv",
        "ipa": "/ɪnˈkɑːnstəntli/",
        "vi": "một cách hay thay đổi; thất thường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086621",
        "hw": "inconsumable",
        "pos": "adj",
        "ipa": "/ˌɪnkənˈsuːməbəl/",
        "vi": "không thể tiêu thụ; không cháy hết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086622",
        "hw": "inconsumably",
        "pos": "adv",
        "ipa": "/ˌɪnkənˈsuːməbli/",
        "vi": "đến mức không thể tiêu hao hết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086623",
        "hw": "incontestability",
        "pos": "noun",
        "ipa": "/ɪnkənˌtɛstəˈbɪləti/",
        "vi": "tính không thể chối cãi; rành rành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086624",
        "hw": "incontestableness",
        "pos": "noun",
        "ipa": "/ɪnkənˈtɛstəbəlnəs/",
        "vi": "sự hiển nhiên không thể bàn cãi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086625",
        "hw": "incontestably",
        "pos": "adv",
        "ipa": "/ɪnkənˈtɛstəbli/",
        "vi": "một cách không thể chối cãi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086626",
        "hw": "incontestible",
        "pos": "adj",
        "ipa": "/ˌɪnkənˈtɛstəbəl/",
        "vi": "không thể tranh cãi; hiển nhiên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086627",
        "hw": "incontinences",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːntɪnənsɪz/",
        "vi": "các chứng mất tự chủ; sự dâm bôn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086628",
        "hw": "incontinency",
        "pos": "noun",
        "ipa": "/ɪnˈkɑːntɪnənsi/",
        "vi": "chứng tiểu tiện không tự chủ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086629",
        "hw": "incontinently",
        "pos": "adv",
        "ipa": "/ɪnˈkɑːntɪnəntli/",
        "vi": "không kìm nén được; ngay lập tức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086630",
        "hw": "incontrollable",
        "pos": "adj",
        "ipa": "/ˌɪnkənˈtroʊləbəl/",
        "vi": "không thể kiểm soát; không kiềm chế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086631",
        "hw": "incontrovertibility",
        "pos": "noun",
        "ipa": "/ɪnˌkɑːntrəˌvɚtəˈbɪləti/",
        "vi": "tính không thể phủ nhận bàn cãi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086632",
        "hw": "incontrovertibleness",
        "pos": "noun",
        "ipa": "/ɪnˌkɑːntrəˈvɚtəbəlnəs/",
        "vi": "tính xác thực không thể bác bỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086633",
        "hw": "inconvenienced",
        "pos": "verb",
        "ipa": "/ˌɪnkənˈviːniənst/",
        "vi": "đã làm phiền; đã gây phiền toái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086634",
        "hw": "inconveniences",
        "pos": "verb",
        "ipa": "/ˌɪnkənˈviːniənsɪz/",
        "vi": "làm phiền; gây phiền toái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086635",
        "hw": "inconveniencing",
        "pos": "verb",
        "ipa": "/ˌɪnkənˈviːniənsɪŋ/",
        "vi": "đang làm phiền; đang gây bất tiện",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086636",
        "hw": "inconveniency",
        "pos": "noun",
        "ipa": "/ˌɪnkənˈviːniənsi/",
        "vi": "sự bất tiện; sự phiền phức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086637",
        "hw": "inconvertibility",
        "pos": "noun",
        "ipa": "/ɪnkənˌvɚtəˈbɪləti/",
        "vi": "tính không thể chuyển đổi tiền tệ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086638",
        "hw": "inconvertibleness",
        "pos": "noun",
        "ipa": "/ɪnkənˈvɚtəbəlnəs/",
        "vi": "tình trạng không thể quy đổi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086639",
        "hw": "inconvertibly",
        "pos": "adv",
        "ipa": "/ɪnkənˈvɚtəbli/",
        "vi": "theo cách không thể chuyển đổi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086640",
        "hw": "inconvincible",
        "pos": "adj",
        "ipa": "/ˌɪnkənˈvɪnsəbəl/",
        "vi": "không thể thuyết phục; ngoan cố",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086641",
        "hw": "incoordinate",
        "pos": "adj",
        "ipa": "/ˌɪnkoʊˈɔːrdənɪt/",
        "vi": "thiếu phối hợp; vụng về mất đồng bộ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086642",
        "hw": "incoordinately",
        "pos": "adv",
        "ipa": "/ˌɪnkoʊˈɔːrdənɪtli/",
        "vi": "một cách thiếu phối hợp; rời rạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086643",
        "hw": "incorporable",
        "pos": "adj",
        "ipa": "/ɪnˈkɔːrpərəbəl/",
        "vi": "có thể sáp nhập; hợp nhất được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086644",
        "hw": "incorporatedness",
        "pos": "noun",
        "ipa": "/ɪnˈkɔːrpəreɪtɪdnəs/",
        "vi": "tư cách pháp nhân; sự hợp nhất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086645",
        "hw": "incorporates",
        "pos": "verb",
        "ipa": "/ɪnˈkɔːrpəreɪts/",
        "vi": "kết hợp; sáp nhập; hợp thành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086646",
        "hw": "incorporating",
        "pos": "verb",
        "ipa": "/ɪnˈkɔːrpəreɪtɪŋ/",
        "vi": "đang kết hợp; đang sáp nhập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086647",
        "hw": "incorporative",
        "pos": "adj",
        "ipa": "/ɪnˈkɔːrpəreɪtɪv/",
        "vi": "mang tính sáp nhập; hợp nhất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086648",
        "hw": "incorporator",
        "pos": "noun",
        "ipa": "/ɪnˈkɔːrpəreɪtər/",
        "vi": "người sáng lập công ty cổ phần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086649",
        "hw": "incorporeality",
        "pos": "noun",
        "ipa": "/ɪnkɔːrˌpɔːriˈæləti/",
        "vi": "tính phi vật thể; sự vô hình",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086650",
        "hw": "incorporeally",
        "pos": "adv",
        "ipa": "/ˌɪnkɔːrˈpɔːriəli/",
        "vi": "một cách phi vật chất; vô hình",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086651",
        "hw": "incorporeity",
        "pos": "noun",
        "ipa": "/ˌɪnkɔːrpəˈriːəti/",
        "vi": "tính chất phi vật chất; sự vô thể",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086652",
        "hw": "incorrigibility",
        "pos": "noun",
        "ipa": "/ɪnˌkɔːrɪdʒəˈbɪləti/",
        "vi": "tính hết thuốc chữa; thói bất trị",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086653",
        "hw": "incorrigibleness",
        "pos": "noun",
        "ipa": "/ɪnˈkɔːrɪdʒəbəlnəs/",
        "vi": "sự bất trị; tính không thể uốn nắn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086654",
        "hw": "incorrodable",
        "pos": "adj",
        "ipa": "/ˌɪnkəˈroʊdəbəl/",
        "vi": "không thể bị ăn mòn; chống gỉ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086655",
        "hw": "incorrodible",
        "pos": "adj",
        "ipa": "/ˌɪnkəˈroʊdəbəl/",
        "vi": "không bị gỉ sét; không bị ăn mòn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086656",
        "hw": "incorrosible",
        "pos": "adj",
        "ipa": "/ˌɪnkəˈroʊsəbəl/",
        "vi": "không bị ăn mòn; kháng gỉ sét",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086657",
        "hw": "incorrupted",
        "pos": "adj",
        "ipa": "/ˌɪnkəˈrʌptɪd/",
        "vi": "trong sạch; không bị vấy bẩn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086658",
        "hw": "incorruptibleness",
        "pos": "noun",
        "ipa": "/ˌɪnkəˈrʌptəbəlnəs/",
        "vi": "tính thanh liêm; sự bất hoại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086659",
        "hw": "incorruptibly",
        "pos": "adv",
        "ipa": "/ˌɪnkəˈrʌptəbli/",
        "vi": "một cách liêm khiết; chí công vô tư",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086660",
        "hw": "incorruptly",
        "pos": "adv",
        "ipa": "/ˌɪnkəˈrʌptli/",
        "vi": "một cách trong sạch; liêm khiết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086661",
        "hw": "incorruptness",
        "pos": "noun",
        "ipa": "/ˌɪnkəˈrʌptnəs/",
        "vi": "sự liêm khiết; tính chính trực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086662",
        "hw": "incrassate",
        "pos": "adj",
        "ipa": "/ɪnˈkræseɪt/",
        "vi": "dày cộm lên; phình to (sinh học)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086663",
        "hw": "increasable",
        "pos": "adj",
        "ipa": "/ɪnˈkriːsəbəl/",
        "vi": "có thể gia tăng; có thể tăng thêm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086664",
        "hw": "increaser",
        "pos": "noun",
        "ipa": "/ɪnˈkriːsər/",
        "vi": "ống nối tăng kích cỡ; bộ khuếch đại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086665",
        "hw": "increases",
        "pos": "verb",
        "ipa": "/ɪnˈkriːsɪz/",
        "vi": "tăng lên; gia tăng; phát triển",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086666",
        "hw": "incredibleness",
        "pos": "noun",
        "ipa": "/ɪnˈkrɛdəbəlnəs/",
        "vi": "tính khó tin; sự phi thường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086667",
        "hw": "incredulousness",
        "pos": "noun",
        "ipa": "/ɪnˈkrɛdʒələsnəs/",
        "vi": "sự hoài nghi; vẻ ngờ vực không tin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086668",
        "hw": "incrementally",
        "pos": "adv",
        "ipa": "/ˌɪŋkrəˈmɛntəli/",
        "vi": "từng bước một; tăng dần từng nấc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086669",
        "hw": "incretion",
        "pos": "noun",
        "ipa": "/ɪnˈkriːʃən/",
        "vi": "chất nội tiết; sự tiết trong",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086670",
        "hw": "incretology",
        "pos": "noun",
        "ipa": "/ˌɪnkrɪˈtɑːlədʒi/",
        "vi": "khoa nội tiết học",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086671",
        "hw": "incriminated",
        "pos": "verb",
        "ipa": "/ɪnˈkrɪməneɪtɪd/",
        "vi": "đã buộc tội; đã làm vướng tội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086672",
        "hw": "incriminates",
        "pos": "verb",
        "ipa": "/ɪnˈkrɪməneɪts/",
        "vi": "buộc tội; làm liên lụy vướng tội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086673",
        "hw": "incriminatingly",
        "pos": "adv",
        "ipa": "/ɪnˈkrɪməneɪtɪŋli/",
        "vi": "với tính chất quy tội; tố cáo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086674",
        "hw": "incriminator",
        "pos": "noun",
        "ipa": "/ɪnˈkrɪməneɪtər/",
        "vi": "người tố giác; người buộc tội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086675",
        "hw": "incrust",
        "pos": "verb",
        "ipa": "/ɪnˈkrʌst/",
        "vi": "đóng vảy; dát khảm bề mặt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086676",
        "hw": "incubated",
        "pos": "verb",
        "ipa": "/ˈɪŋkjəbeɪtɪd/",
        "vi": "đã ấp trứng; đã nuôi cấy vi khuẩn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086677",
        "hw": "incubates",
        "pos": "verb",
        "ipa": "/ˈɪŋkjəbeɪts/",
        "vi": "ấp trứng; ủ bệnh; nuôi cấy mẫu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086678",
        "hw": "incubating",
        "pos": "verb",
        "ipa": "/ˈɪŋkjəbeɪtɪŋ/",
        "vi": "đang ấp trứng; đang thời kỳ ủ bệnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086679",
        "hw": "incubational",
        "pos": "adj",
        "ipa": "/ˌɪŋkjəˈbeɪʃənəl/",
        "vi": "(thuộc) kỳ ủ bệnh; sự ấp trứng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086680",
        "hw": "incubative",
        "pos": "adj",
        "ipa": "/ˈɪŋkjəbeɪtɪv/",
        "vi": "đang trong giai đoạn ủ bệnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086681",
        "hw": "incubatory",
        "pos": "adj",
        "ipa": "/ˈɪŋkjəbətɔːri/",
        "vi": "dùng để ấp trứng; phục vụ ủ ấm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086682",
        "hw": "incubi",
        "pos": "noun",
        "ipa": "/ˈɪŋkjəbaɪ/",
        "vi": "ác quỷ bóng đè; các cơn ác mộng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086683",
        "hw": "inculcated",
        "pos": "verb",
        "ipa": "/ˈɪnkʌlkeɪtɪd/",
        "vi": "đã khắc sâu; đã truyền thụ giáo dục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086684",
        "hw": "inculcates",
        "pos": "verb",
        "ipa": "/ˈɪnkʌlkeɪts/",
        "vi": "khắc sâu vào trí; truyền dạy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086685",
        "hw": "inculcating",
        "pos": "verb",
        "ipa": "/ˈɪnkʌlkeɪtɪŋ/",
        "vi": "đang khắc sâu; đang truyền dạy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086686",
        "hw": "inculcative",
        "pos": "adj",
        "ipa": "/ɪnˈkʌlkətɪv/",
        "vi": "nhằm khắc sâu; mang tính răn dạy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086687",
        "hw": "inculcator",
        "pos": "noun",
        "ipa": "/ˈɪnkʌlkeɪtər/",
        "vi": "người truyền dạy; người giáo dục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086688",
        "hw": "inculcatory",
        "pos": "adj",
        "ipa": "/ɪnˈkʌlkətɔːri/",
        "vi": "nhằm khắc sâu; rèn luyện giáo dục",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086689",
        "hw": "inculpability",
        "pos": "noun",
        "ipa": "/ɪnˌkʌlpəˈbɪləti/",
        "vi": "sự vô tội; tình trạng không có lỗi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086690",
        "hw": "inculpable",
        "pos": "adj",
        "ipa": "/ɪnˈkʌlpəbəl/",
        "vi": "vô tội; không vướng tì vết sai lầm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086691",
        "hw": "inculpableness",
        "pos": "noun",
        "ipa": "/ɪnˈkʌlpəbəlnəs/",
        "vi": "tính chất trong sạch; sự vô tội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086692",
        "hw": "inculpate",
        "pos": "verb",
        "ipa": "/ˈɪnkʌlpeɪt/",
        "vi": "buộc tội; quy trách nhiệm phạm tội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086693",
        "hw": "inculpated",
        "pos": "verb",
        "ipa": "/ˈɪnkʌlpeɪtɪd/",
        "vi": "đã buộc tội; đã tố cáo vướng tội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086694",
        "hw": "inculpates",
        "pos": "verb",
        "ipa": "/ˈɪnkʌlpeɪts/",
        "vi": "buộc tội; tố cáo dính líu phạm pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086695",
        "hw": "inculpating",
        "pos": "verb",
        "ipa": "/ˈɪnkʌlpeɪtɪŋ/",
        "vi": "đang buộc tội; đang quy trách nhiệm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086696",
        "hw": "inculpation",
        "pos": "noun",
        "ipa": "/ˌɪnkʌlˈpeɪʃən/",
        "vi": "sự buộc tội; lời cáo buộc dính líu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086697",
        "hw": "inculpative",
        "pos": "adj",
        "ipa": "/ɪnˈkʌlpətɪv/",
        "vi": "mang tính buộc tội; quy trách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086698",
        "hw": "incult",
        "pos": "adj",
        "ipa": "/ɪnˈkʌlt/",
        "vi": "hoang vu; không canh tác; thô kệch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086699",
        "hw": "incumbently",
        "pos": "adv",
        "ipa": "/ɪnˈkʌmbəntli/",
        "vi": "dưới tư cách đương nhiệm chức vụ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086700",
        "hw": "incumbents",
        "pos": "noun",
        "ipa": "/ɪnˈkʌmbənts/",
        "vi": "những người đương nhiệm chức vụ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086701",
        "hw": "incumber",
        "pos": "verb",
        "ipa": "/ɪnˈkʌmbər/",
        "vi": "làm vướng víu; gây trở ngại nặng nề",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

if __name__ == "__main__":
    assert len(data) == 100, f"Expected 100, got {len(data)}"
    with open("scratch/b18_r04_raw_p2.json") as f:
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
    print("ALL 100 RECORDS IN ROUND 4 PART 2 VERIFIED SUCCESSFULLY!")
