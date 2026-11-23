# scratch/b18_r03_p3.py
# Batch 18 Round 3 Part 3: records 1200 - 1299 (IDs 086202 - 086301)
import json

data = [
    {
        "id": "lex.en.100k.086202",
        "hw": "implicating",
        "pos": "verb",
        "ipa": "/ˈɪmplɪkeɪtɪŋ/",
        "vi": "đang lôi kéo vào; đang dính líu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086203",
        "hw": "implicational",
        "pos": "adj",
        "ipa": "/ˌɪmplɪˈkeɪʃənəl/",
        "vi": "mang tính hàm ý; thuộc ngụ ý",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086204",
        "hw": "implicatively",
        "pos": "adv",
        "ipa": "/ˈɪmplɪkətɪvli/",
        "vi": "theo lối ngụ ý; mang tính hàm ẩn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086205",
        "hw": "implicatory",
        "pos": "adj",
        "ipa": "/ˈɪmplɪkətɔːri/",
        "vi": "có tính hàm ý; làm liên đới",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086206",
        "hw": "implicitness",
        "pos": "noun",
        "ipa": "/ɪmˈplɪsɪtnəs/",
        "vi": "tính hàm ẩn; sự ngầm hiểu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086207",
        "hw": "implicity",
        "pos": "noun",
        "ipa": "/ɪmˈplɪsɪti/",
        "vi": "tính hàm ẩn; sự ngấm ngầm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086208",
        "hw": "implied",
        "pos": "verb",
        "ipa": "/ɪmˈplaɪd/",
        "vi": "đã ngụ ý; đã hàm ý",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086209",
        "hw": "implies",
        "pos": "verb",
        "ipa": "/ɪmˈplaɪz/",
        "vi": "ngụ ý; bao hàm ngầm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086210",
        "hw": "implike",
        "pos": "adj",
        "ipa": "/ˈɪmplaɪk/",
        "vi": "tinh quái; nghịch như yêu tinh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086211",
        "hw": "imploded",
        "pos": "verb",
        "ipa": "/ɪmˈploʊdɪd/",
        "vi": "đã nổ ép vào trong; đã sụp đổ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086212",
        "hw": "implodes",
        "pos": "verb",
        "ipa": "/ɪmˈploʊdz/",
        "vi": "nổ sụp vào trong; sụp đổ nội tại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086213",
        "hw": "imploding",
        "pos": "verb",
        "ipa": "/ɪmˈploʊdɪŋ/",
        "vi": "đang nổ ép vào trong; đang sụp đổ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086214",
        "hw": "implorable",
        "pos": "adj",
        "ipa": "/ɪmˈplɔːrəbəl/",
        "vi": "có thể khẩn nài; có thể cầu xin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086215",
        "hw": "imploration",
        "pos": "noun",
        "ipa": "/ˌɪmpləˈreɪʃən/",
        "vi": "sự khẩn nài; lời van xin tha thiết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086216",
        "hw": "implorer",
        "pos": "noun",
        "ipa": "/ɪmˈplɔːrər/",
        "vi": "người khẩn nài; người van xin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086217",
        "hw": "imploringness",
        "pos": "noun",
        "ipa": "/ɪmˈplɔːrɪŋnəs/",
        "vi": "vẻ cầu khẩn; giọng điệu van xin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086218",
        "hw": "implosive",
        "pos": "adj",
        "ipa": "/ɪmˈploʊsɪv/",
        "vi": "nổ ép vào trong; hút vào (ngữ âm)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086219",
        "hw": "impluvium",
        "pos": "noun",
        "ipa": "/ɪmˈpluːviəm/",
        "vi": "bể hứng nước mưa (nhà La Mã cổ)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086220",
        "hw": "implying",
        "pos": "verb",
        "ipa": "/ɪmˈplaɪɪŋ/",
        "vi": "đang ngụ ý; mang ý tứ ngầm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086221",
        "hw": "impolicy",
        "pos": "noun",
        "ipa": "/ɪmˈpɑːləsi/",
        "vi": "chính sách dại dột; sự bất cập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086222",
        "hw": "impoliticly",
        "pos": "adv",
        "ipa": "/ɪmˈpɑːlətɪkli/",
        "vi": "một cách thiếu khôn ngoan; vụng về",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086223",
        "hw": "impoliticness",
        "pos": "noun",
        "ipa": "/ɪmˈpɑːlətɪknəs/",
        "vi": "sự thiếu khôn ngoan; tính dại dột",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086224",
        "hw": "imponderabilia",
        "pos": "noun",
        "ipa": "/ɪmˌpɑːndərəˈbɪliə/",
        "vi": "yếu tố khôn lường; điều vô hình",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086225",
        "hw": "imponderability",
        "pos": "noun",
        "ipa": "/ɪmˌpɑːndərəˈbɪləti/",
        "vi": "tính khôn lường; sự vô hình",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086226",
        "hw": "imponderableness",
        "pos": "noun",
        "ipa": "/ɪmˈpɑːndərəbəlnəs/",
        "vi": "tính chất khôn lường; tính mơ hồ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086227",
        "hw": "imponderably",
        "pos": "adv",
        "ipa": "/ɪmˈpɑːndərəbli/",
        "vi": "một cách khôn lường; khó ước đoán",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086228",
        "hw": "imponent",
        "pos": "adj",
        "ipa": "/ɪmˈpoʊnənt/",
        "vi": "giao nhiệm vụ; áp đặt bổn phận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086229",
        "hw": "importability",
        "pos": "noun",
        "ipa": "/ˌɪmpɔːrtəˈbɪləti/",
        "vi": "khả năng có thể nhập khẩu được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086230",
        "hw": "importable",
        "pos": "adj",
        "ipa": "/ɪmˈpɔːrtəbəl/",
        "vi": "có thể nhập khẩu; có thể mang vào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086231",
        "hw": "importee",
        "pos": "noun",
        "ipa": "/ˌɪmpɔːrˈtiː/",
        "vi": "hàng nhập khẩu; người được đưa vào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086232",
        "hw": "imports",
        "pos": "verb",
        "ipa": "/ɪmˈpɔːrts/",
        "vi": "nhập khẩu; mang ý nghĩa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086233",
        "hw": "importunateness",
        "pos": "noun",
        "ipa": "/ɪmˈpɔːrtʃənɪtnəs/",
        "vi": "sự quấy rầy; thói nài ép trơ trẽn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086234",
        "hw": "importuned",
        "pos": "verb",
        "ipa": "/ˌɪmpɔːrˈtjuːnd/",
        "vi": "đã nài nỉ; đã vòi vĩnh quấy rầy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086235",
        "hw": "importunely",
        "pos": "adv",
        "ipa": "/ɪmˈpɔːrtʃənɪtli/",
        "vi": "một cách dai dẳng; phiền toái",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086236",
        "hw": "importunes",
        "pos": "verb",
        "ipa": "/ˌɪmpɔːrˈtjuːnz/",
        "vi": "nài nỉ; van xin dai dẳng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086237",
        "hw": "importuning",
        "pos": "verb",
        "ipa": "/ˌɪmpɔːrˈtjuːnɪŋ/",
        "vi": "đang nài nỉ; đang van xin dai dẳng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086238",
        "hw": "imposable",
        "pos": "adj",
        "ipa": "/ɪmˈpoʊzəbəl/",
        "vi": "có thể áp đặt; có thể đánh thuế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086239",
        "hw": "imposer",
        "pos": "noun",
        "ipa": "/ɪmˈpoʊzər/",
        "vi": "người áp đặt; người đánh thuế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086240",
        "hw": "imposes",
        "pos": "verb",
        "ipa": "/ɪmˈpoʊzɪz/",
        "vi": "áp đặt; đánh thuế; bắt chịu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086241",
        "hw": "imposingness",
        "pos": "noun",
        "ipa": "/ɪmˈpoʊzɪŋnəs/",
        "vi": "vẻ oai nghiêm; sự hùng vĩ đường bệ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086242",
        "hw": "impossibilities",
        "pos": "noun",
        "ipa": "/ɪmˌpɑːsəˈbɪlɪtiz/",
        "vi": "những điều bất khả; việc không thể",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086243",
        "hw": "impossibleness",
        "pos": "noun",
        "ipa": "/ɪmˈpɑːsəbəlnəs/",
        "vi": "tính bất khả; tình trạng không thể",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086244",
        "hw": "imposthume",
        "pos": "noun",
        "ipa": "/ˈɪmpɑːstjuːm/",
        "vi": "ổ mủ; nhọt mủ sưng tấy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086245",
        "hw": "impostrous",
        "pos": "adj",
        "ipa": "/ɪmˈpɑːstrəs/",
        "vi": "lừa đảo; mang tính mạo danh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086246",
        "hw": "impostume",
        "pos": "noun",
        "ipa": "/ˈɪmpɑːstjuːm/",
        "vi": "ổ mủ; bọc mủ sưng tấy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086247",
        "hw": "impot",
        "pos": "noun",
        "ipa": "/ˈɪmpɑːt/",
        "vi": "bài phạt chép (ở trường học)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086248",
        "hw": "impotentness",
        "pos": "noun",
        "ipa": "/ˈɪmpətəntnəs/",
        "vi": "sự bất lực; tình trạng liệt dương",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086249",
        "hw": "impoundable",
        "pos": "adj",
        "ipa": "/ɪmˈpaʊndəbəl/",
        "vi": "có thể bị tịch thu; giam giữ được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086250",
        "hw": "impoundage",
        "pos": "noun",
        "ipa": "/ɪmˈpaʊndɪdʒ/",
        "vi": "sự tích nước hồ; sự tịch thu vật",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086251",
        "hw": "impounded",
        "pos": "verb",
        "ipa": "/ɪmˈpaʊndɪd/",
        "vi": "đã tịch thu; đã tạm giữ tang vật",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086252",
        "hw": "impounder",
        "pos": "noun",
        "ipa": "/ɪmˈpaʊndər/",
        "vi": "người tịch thu; nhân viên tạm giữ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086253",
        "hw": "impounds",
        "pos": "verb",
        "ipa": "/ɪmˈpaʊndz/",
        "vi": "tịch thu; tạm giữ; ngăn nước",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086254",
        "hw": "impoverishes",
        "pos": "verb",
        "ipa": "/ɪmˈpɑːvərɪʃɪz/",
        "vi": "làm nghèo nàn; làm kiệt quệ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086255",
        "hw": "impoverishing",
        "pos": "verb",
        "ipa": "/ɪmˈpɑːvərɪʃɪŋ/",
        "vi": "đang làm kiệt quệ; làm bần cùng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086256",
        "hw": "impracticableness",
        "pos": "noun",
        "ipa": "/ɪmˈpræktɪkəbəlnəs/",
        "vi": "tính không khả thi; khó thi hành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086257",
        "hw": "impracticably",
        "pos": "adv",
        "ipa": "/ɪmˈpræktɪkəbli/",
        "vi": "một cách không khả thi; khó làm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086258",
        "hw": "impractically",
        "pos": "adv",
        "ipa": "/ɪmˈpræktɪkli/",
        "vi": "một cách thiếu thực tế; viển vông",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086259",
        "hw": "imprecate",
        "pos": "verb",
        "ipa": "/ˈɪmprɪkeɪt/",
        "vi": "nguyền rủa; cầu điều gở xuống",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086260",
        "hw": "imprecatingly",
        "pos": "adv",
        "ipa": "/ˈɪmprɪkeɪtɪŋli/",
        "vi": "với giọng nguyền rủa; đầy oán hận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086261",
        "hw": "imprecator",
        "pos": "noun",
        "ipa": "/ˈɪmprɪkeɪtər/",
        "vi": "kẻ buông lời nguyền rủa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086262",
        "hw": "imprecatory",
        "pos": "adj",
        "ipa": "/ˈɪmprɪkətɔːri/",
        "vi": "mang tính nguyền rủa; chúc điều gở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086263",
        "hw": "impreciseness",
        "pos": "noun",
        "ipa": "/ˌɪmprɪˈsaɪsnəs/",
        "vi": "sự thiếu chuẩn xác; tính mơ hồ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086264",
        "hw": "imprecisions",
        "pos": "noun",
        "ipa": "/ˌɪmprɪˈsɪʒənz/",
        "vi": "những điểm thiếu chính xác",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086265",
        "hw": "impregnably",
        "pos": "adv",
        "ipa": "/ɪmˈprɛɡnəbli/",
        "vi": "một cách kiên cố; vững chắc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086266",
        "hw": "impregnant",
        "pos": "noun",
        "ipa": "/ɪmˈprɛɡnənt/",
        "vi": "chất làm thấm; chất tẩm ngấm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086267",
        "hw": "impregnated",
        "pos": "verb",
        "ipa": "/ɪmˈprɛɡneɪtɪd/",
        "vi": "đã thụ tinh; đã tẩm ướt đẫm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086268",
        "hw": "impregnates",
        "pos": "verb",
        "ipa": "/ɪmˈprɛɡneɪts/",
        "vi": "thụ tinh; tẩm ướt đẫm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086269",
        "hw": "impregnating",
        "pos": "verb",
        "ipa": "/ɪmˈprɛɡneɪtɪŋ/",
        "vi": "đang thụ tinh; đang làm ngấm sâu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086270",
        "hw": "impregnator",
        "pos": "noun",
        "ipa": "/ˈɪmprɛɡneɪtər/",
        "vi": "bình ngâm tẩm; tác nhân thụ thai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086271",
        "hw": "impremitive",
        "pos": "adj",
        "ipa": "/ɪmˈprɛmɪtɪv/",
        "vi": "không nguyên thủy; phái sinh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086272",
        "hw": "impresari",
        "pos": "noun",
        "ipa": "/ˌɪmprəˈsɑːri/",
        "vi": "các ông bầu sân khấu (số nhiều)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086273",
        "hw": "imprescribable",
        "pos": "adj",
        "ipa": "/ˌɪmprɪˈskraɪbəbəl/",
        "vi": "bất khả xâm phạm; không thể tước",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086274",
        "hw": "imprescriptibility",
        "pos": "noun",
        "ipa": "/ɪmprɪˌskrɪptəˈbɪlɪti/",
        "vi": "tính không thể mất theo thời hiệu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086275",
        "hw": "imprescriptible",
        "pos": "adj",
        "ipa": "/ˌɪmprɪˈskraɪbəbəl/",
        "vi": "không tiêu trừ theo luật định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086276",
        "hw": "impresses",
        "pos": "verb",
        "ipa": "/ɪmˈprɛsɪz/",
        "vi": "gây ấn tượng; khắc sâu; đóng dấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086277",
        "hw": "impressibility",
        "pos": "noun",
        "ipa": "/ɪmˌprɛsəˈbɪləti/",
        "vi": "tính dễ xúc cảm; dễ bị tác động",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086278",
        "hw": "impressible",
        "pos": "adj",
        "ipa": "/ɪmˈprɛsəbəl/",
        "vi": "dễ xúc động; dễ bị gây ấn tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086279",
        "hw": "impressibly",
        "pos": "adv",
        "ipa": "/ɪmˈprɛsəbli/",
        "vi": "một cách dễ cảm động; nhạy cảm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086280",
        "hw": "impressing",
        "pos": "verb",
        "ipa": "/ɪmˈprɛsɪŋ/",
        "vi": "đang gây ấn tượng; đang khắc sâu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086281",
        "hw": "impressionability",
        "pos": "noun",
        "ipa": "/ɪmˌprɛʃənəˈbɪləti/",
        "vi": "tính dễ bị ảnh hưởng; dễ uốn nắn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086282",
        "hw": "impressionableness",
        "pos": "noun",
        "ipa": "/ɪmˌprɛʃənəbəlnəs/",
        "vi": "tính dễ bị tiêm nhiễm ảnh hưởng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086283",
        "hw": "impressional",
        "pos": "adj",
        "ipa": "/ɪmˈprɛʃənəl/",
        "vi": "do ấn tượng; dựa trên cảm giác",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086284",
        "hw": "impressionary",
        "pos": "adj",
        "ipa": "/ɪmˈprɛʃənɛri/",
        "vi": "gợi ấn tượng; mang tính cảm xúc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086285",
        "hw": "impressionistically",
        "pos": "adv",
        "ipa": "/ɪmˌprɛʃəˈnɪstɪkli/",
        "vi": "theo phong cách ấn tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086286",
        "hw": "imprest",
        "pos": "noun",
        "ipa": "/ˈɪmprɛst/",
        "vi": "khoản tiền tạm ứng trước",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086287",
        "hw": "imprimis",
        "pos": "adv",
        "ipa": "/ɪmˈpraɪmɪs/",
        "vi": "trước hết; điều khoản đầu tiên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086288",
        "hw": "imprinted",
        "pos": "verb",
        "ipa": "/ɪmˈprɪntɪd/",
        "vi": "đã in dấu; đã khắc sâu trong óc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086289",
        "hw": "imprints",
        "pos": "verb",
        "ipa": "/ɪmˈprɪnts/",
        "vi": "in dấu; khắc sâu vào tâm trí",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086290",
        "hw": "imprisonable",
        "pos": "adj",
        "ipa": "/ɪmˈprɪzənəbəl/",
        "vi": "có thể bị phạt tù; đáng tống giam",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086291",
        "hw": "imprisoning",
        "pos": "verb",
        "ipa": "/ɪmˈprɪzənɪŋ/",
        "vi": "đang bỏ tù; đang giam giữ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086292",
        "hw": "imprisons",
        "pos": "verb",
        "ipa": "/ɪmˈprɪzənz/",
        "vi": "bỏ tù; tống giam; giam cầm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086293",
        "hw": "improbableness",
        "pos": "noun",
        "ipa": "/ɪmˈprɑːbəbəlnəs/",
        "vi": "tính khó xảy ra; sự khó tin",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086294",
        "hw": "improbity",
        "pos": "noun",
        "ipa": "/ɪmˈprɑːbəti/",
        "vi": "sự bất lương; thói bất chính",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086295",
        "hw": "improperness",
        "pos": "noun",
        "ipa": "/ɪmˈprɑːpərnəs/",
        "vi": "sự không phù hợp; tính khiếm nhã",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086296",
        "hw": "impropriate",
        "pos": "verb",
        "ipa": "/ɪmˈproʊprieɪt/",
        "vi": "thế tục hóa bổng lộc giáo hội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086297",
        "hw": "impropriation",
        "pos": "noun",
        "ipa": "/ɪmˌproʊpriˈeɪʃən/",
        "vi": "sự thế tục hóa bổng lộc nhà thờ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086298",
        "hw": "improvability",
        "pos": "noun",
        "ipa": "/ɪmˌpruːvəˈbɪləti/",
        "vi": "khả năng có thể cải thiện",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086299",
        "hw": "improvableness",
        "pos": "noun",
        "ipa": "/ɪmˈpruːvəbəlnəs/",
        "vi": "tính có thể cải tạo được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086300",
        "hw": "improvements",
        "pos": "noun",
        "ipa": "/ɪmˈpruːvmənts/",
        "vi": "những cải tiến; các sự tiến bộ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086301",
        "hw": "improves",
        "pos": "verb",
        "ipa": "/ɪmˈpruːvz/",
        "vi": "cải thiện; nâng cao chất lượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

if __name__ == "__main__":
    assert len(data) == 100, f"Expected 100, got {len(data)}"
    with open("scratch/b18_r03_raw_p3.json") as f:
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
    print("ALL 100 RECORDS IN ROUND 3 PART 3 VERIFIED SUCCESSFULLY!")
