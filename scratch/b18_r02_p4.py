# scratch/b18_r02_p4.py
# Batch 18 Round 2 Part 4: records 800 - 899 (IDs 085802 - 085901)
import json

data = [
    {
        "id": "lex.en.100k.085802",
        "hw": "ileal",
        "pos": "adj",
        "ipa": "/ˈɪliəl/",
        "vi": "(thuộc) hồi tràng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085803",
        "hw": "ileitis",
        "pos": "noun",
        "ipa": "/ˌɪliˈaɪtɪs/",
        "vi": "viêm hồi tràng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085804",
        "hw": "ileocecal",
        "pos": "adj",
        "ipa": "/ˌɪlioʊˈsiːkəl/",
        "vi": "(thuộc) hồi manh tràng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085805",
        "hw": "iles",
        "pos": "noun",
        "ipa": "/aɪlz/",
        "vi": "nếp gấp; vạt áo (dạng số nhiều)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085806",
        "hw": "ilia",
        "pos": "noun",
        "ipa": "/ˈɪliə/",
        "vi": "xương cánh chậu (số nhiều)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085807",
        "hw": "ilka",
        "pos": "adj",
        "ipa": "/ˈɪlkə/",
        "vi": "mỗi; từng (phương ngữ)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085808",
        "hw": "illampu",
        "pos": "noun",
        "ipa": "/iːˈjɑːmpuː/",
        "vi": "núi Illampu (Bolivia)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085809",
        "hw": "illation",
        "pos": "noun",
        "ipa": "/ɪˈleɪʃən/",
        "vi": "sự suy luận; kết luận rút ra",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085810",
        "hw": "illatively",
        "pos": "adv",
        "ipa": "/ˈɪlətɪvli/",
        "vi": "theo lối suy luận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085811",
        "hw": "illaudable",
        "pos": "adj",
        "ipa": "/ɪˈlɔːdəbəl/",
        "vi": "không đáng khen; đáng chê trách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085812",
        "hw": "illecebrum",
        "pos": "noun",
        "ipa": "/ɪˈlɛsəbrəm/",
        "vi": "chi cẩm chướng dại (thực vật)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085813",
        "hw": "illegalisation",
        "pos": "noun",
        "ipa": "/ɪˌliːɡəlaɪˈzeɪʃən/",
        "vi": "sự bất hợp pháp hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085814",
        "hw": "illegalise",
        "pos": "verb",
        "ipa": "/ɪˈliːɡəlaɪz/",
        "vi": "bất hợp pháp hóa; đặt ngoài luật",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085815",
        "hw": "illegalization",
        "pos": "noun",
        "ipa": "/ɪˌliːɡələˈzeɪʃən/",
        "vi": "sự bất hợp pháp hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085816",
        "hw": "illegalize",
        "pos": "verb",
        "ipa": "/ɪˈliːɡəlaɪz/",
        "vi": "bất hợp pháp hóa; đặt ngoài luật",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085817",
        "hw": "illegatity",
        "pos": "noun",
        "ipa": "/ˌɪlɪˈɡætɪti/",
        "vi": "sự bất hợp pháp; tính trái luật",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085818",
        "hw": "illegatization",
        "pos": "noun",
        "ipa": "/ɪˌlɛɡətɪˈzeɪʃən/",
        "vi": "sự làm thành không hợp pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085819",
        "hw": "illegibleness",
        "pos": "noun",
        "ipa": "/ɪˈlɛdʒəbəlnəs/",
        "vi": "sự khó đọc; tính khó đọc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085820",
        "hw": "illegitimateness",
        "pos": "noun",
        "ipa": "/ˌɪlɪˈdʒɪtəmətnəs/",
        "vi": "sự bất hợp pháp; tính ngoài giá thú",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085821",
        "hw": "illegitimation",
        "pos": "noun",
        "ipa": "/ɪˌlɛdʒɪtɪˈmeɪʃən/",
        "vi": "sự tuyên bố bất hợp pháp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085822",
        "hw": "illiberalise",
        "pos": "verb",
        "ipa": "/ɪˈlɪbərəlaɪz/",
        "vi": "làm cho hẹp hòi; hạn chế tự do",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085823",
        "hw": "illiberalism",
        "pos": "noun",
        "ipa": "/ɪˈlɪbərəˌlɪzəm/",
        "vi": "chủ nghĩa phi tự do; tính hẹp hòi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085824",
        "hw": "illiberality",
        "pos": "noun",
        "ipa": "/ˌɪlɪbəˈræləti/",
        "vi": "tính hẹp hòi; sự thiếu tự do",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085825",
        "hw": "illiberalize",
        "pos": "verb",
        "ipa": "/ɪˈlɪbərəlaɪz/",
        "vi": "làm cho hẹp hòi; hạn chế tự do",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085826",
        "hw": "illiberally",
        "pos": "adv",
        "ipa": "/ɪˈlɪbərəli/",
        "vi": "một cách hẹp hòi; thiếu tự do",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085827",
        "hw": "illiberalness",
        "pos": "noun",
        "ipa": "/ɪˈlɪbərəlnəs/",
        "vi": "tính hẹp hòi; tính cố chấp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085828",
        "hw": "illicitness",
        "pos": "noun",
        "ipa": "/ɪˈlɪsɪtnəs/",
        "vi": "tính bất hợp pháp; sự trái phép",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085829",
        "hw": "illicium",
        "pos": "noun",
        "ipa": "/ɪˈlɪsiəm/",
        "vi": "chi đại hồi; chi hồi (thực vật)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085830",
        "hw": "illimani",
        "pos": "noun",
        "ipa": "/iːjiˈmɑːni/",
        "vi": "núi Illimani (Bolivia)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085831",
        "hw": "illimitability",
        "pos": "noun",
        "ipa": "/ɪˌlɪmɪtəˈbɪlɪti/",
        "vi": "tính vô hạn; tính vô biên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085832",
        "hw": "illimitableness",
        "pos": "noun",
        "ipa": "/ɪˈlɪmɪtəbəlnəs/",
        "vi": "sự vô hạn; tính vô biên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085833",
        "hw": "illimitably",
        "pos": "adv",
        "ipa": "/ɪˈlɪmɪtəbli/",
        "vi": "một cách vô hạn; vô biên",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085834",
        "hw": "illinium",
        "pos": "noun",
        "ipa": "/ɪˈlɪniəm/",
        "vi": "nguyên tố illinium (cũ)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085835",
        "hw": "illiquid",
        "pos": "adj",
        "ipa": "/ɪˈlɪkwɪd/",
        "vi": "kém thanh khoản; khó đổi ra tiền",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085836",
        "hw": "illiquidity",
        "pos": "noun",
        "ipa": "/ˌɪlɪˈkwɪdɪti/",
        "vi": "tính kém thanh khoản (tài chính)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085837",
        "hw": "illiterately",
        "pos": "adv",
        "ipa": "/ɪˈlɪtərɪtli/",
        "vi": "một cách mù chữ; dốt nát",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085838",
        "hw": "illiterateness",
        "pos": "noun",
        "ipa": "/ɪˈlɪtərɪtnəs/",
        "vi": "nạn mù chữ; sự thất học",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085839",
        "hw": "illnesses",
        "pos": "noun",
        "ipa": "/ˈɪlnəsɪz/",
        "vi": "các căn bệnh; các chứng bệnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085840",
        "hw": "illogicalness",
        "pos": "noun",
        "ipa": "/ɪˈlɑːdʒɪkəlnəs/",
        "vi": "tính phi lô-gíc; sự vô lý",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085841",
        "hw": "illuminability",
        "pos": "noun",
        "ipa": "/ɪˌluːmɪnəˈbɪlɪti/",
        "vi": "khả năng có thể chiếu sáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085842",
        "hw": "illuminable",
        "pos": "adj",
        "ipa": "/ɪˈluːmɪnəbəl/",
        "vi": "có thể chiếu sáng; có thể soi tỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085843",
        "hw": "illuminati",
        "pos": "noun",
        "ipa": "/ɪˌluːmɪˈnɑːti/",
        "vi": "hội Khai sáng; giới tinh hoa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085844",
        "hw": "illuminatingly",
        "pos": "adv",
        "ipa": "/ɪˈluːmɪneɪtɪŋli/",
        "vi": "một cách sáng tỏ; có tính khai sáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085845",
        "hw": "illuminative",
        "pos": "adj",
        "ipa": "/ɪˈluːmɪneɪtɪv/",
        "vi": "chiếu sáng; mang tính soi sáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085846",
        "hw": "illuminator",
        "pos": "noun",
        "ipa": "/ɪˈluːmɪneɪtər/",
        "vi": "nguồn chiếu sáng; đèn chiếu sáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085847",
        "hw": "illumined",
        "pos": "verb",
        "ipa": "/ɪˈluːmɪnd/",
        "vi": "đã soi sáng; đã rọi sáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085848",
        "hw": "illumines",
        "pos": "verb",
        "ipa": "/ɪˈluːmɪnz/",
        "vi": "soi sáng; rọi sáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085849",
        "hw": "illumining",
        "pos": "verb",
        "ipa": "/ɪˈluːmɪnɪŋ/",
        "vi": "đang soi sáng; đang rọi sáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085850",
        "hw": "illuminist",
        "pos": "noun",
        "ipa": "/ɪˈluːmɪnɪst/",
        "vi": "người theo phái Khai sáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085851",
        "hw": "illuministic",
        "pos": "adj",
        "ipa": "/ɪˌluːmɪˈnɪstɪk/",
        "vi": "(thuộc) phái Khai sáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085852",
        "hw": "illuminometer",
        "pos": "noun",
        "ipa": "/ˌɪluːmɪˈnɑːmɪtər/",
        "vi": "dụng cụ đo độ rọi sáng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085853",
        "hw": "illuory",
        "pos": "noun",
        "ipa": "/ɪˈluːsəri/",
        "vi": "ảo tưởng; điều không thực tế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085854",
        "hw": "illusional",
        "pos": "adj",
        "ipa": "/ɪˈluːʒənəl/",
        "vi": "thuộc ảo tưởng; hoang tưởng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085855",
        "hw": "illusionism",
        "pos": "noun",
        "ipa": "/ɪˈluːʒənɪzəm/",
        "vi": "chủ nghĩa ảo thị; nghệ thuật ảo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085856",
        "hw": "illusionistic",
        "pos": "adj",
        "ipa": "/ɪˌluːʒəˈnɪstɪk/",
        "vi": "tạo ảo thị giác; gợi ảo giác",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085857",
        "hw": "illusionistically",
        "pos": "adv",
        "ipa": "/ɪˌluːʒəˈnɪstɪkli/",
        "vi": "theo lối tạo ảo thị giác",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085858",
        "hw": "illusionless",
        "pos": "adj",
        "ipa": "/ɪˈluːʒənləs/",
        "vi": "không ảo tưởng; thực tế tỉnh táo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085859",
        "hw": "illusions",
        "pos": "noun",
        "ipa": "/ɪˈluːʒənz/",
        "vi": "những ảo tưởng; các ảo giác",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085860",
        "hw": "illusively",
        "pos": "adv",
        "ipa": "/ɪˈluːsɪvli/",
        "vi": "một cách ảo tưởng; giả tạo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085861",
        "hw": "illusiveness",
        "pos": "noun",
        "ipa": "/ɪˈluːsɪvnəs/",
        "vi": "tính chất ảo tưởng; tính hư ảo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085862",
        "hw": "illustratable",
        "pos": "adj",
        "ipa": "/ˈɪləstreɪtəbəl/",
        "vi": "có thể minh họa; có thể làm rõ ý",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085863",
        "hw": "illustrated",
        "pos": "verb",
        "ipa": "/ˈɪləstreɪtɪd/",
        "vi": "đã minh họa; đã làm sáng tỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085864",
        "hw": "illustrates",
        "pos": "verb",
        "ipa": "/ˈɪləstreɪts/",
        "vi": "minh họa; làm sáng tỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085865",
        "hw": "illustrating",
        "pos": "verb",
        "ipa": "/ˈɪləstreɪtɪŋ/",
        "vi": "đang minh họa; đang làm sáng tỏ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085866",
        "hw": "illustrational",
        "pos": "adj",
        "ipa": "/ˌɪləˈstreɪʃənəl/",
        "vi": "thuộc sự minh họa; dùng để minh họa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085867",
        "hw": "illustratively",
        "pos": "adv",
        "ipa": "/ɪˈlʌstrətɪvli/",
        "vi": "để minh họa; nhằm giải thích",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085868",
        "hw": "illustriously",
        "pos": "adv",
        "ipa": "/ɪˈlʌstriəsli/",
        "vi": "một cách lừng lẫy; hiển hách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085869",
        "hw": "illustriousness",
        "pos": "noun",
        "ipa": "/ɪˈlʌstriəsnəs/",
        "vi": "sự lừng lẫy; danh tiếng hiển hách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085870",
        "hw": "illuvia",
        "pos": "noun",
        "ipa": "/ɪˈluːviə/",
        "vi": "chất tích tụ tầng đất (số nhiều)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085871",
        "hw": "illuvial",
        "pos": "adj",
        "ipa": "/ɪˈluːviəl/",
        "vi": "(thuộc) tầng tích tụ; bồi tích",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085872",
        "hw": "illuviation",
        "pos": "noun",
        "ipa": "/ɪˌluːviˈeɪʃən/",
        "vi": "quá trình tích tụ khoáng vào đất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085873",
        "hw": "illuvium",
        "pos": "noun",
        "ipa": "/ɪˈluːviəm/",
        "vi": "vật liệu tích tụ tầng B (đất)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085874",
        "hw": "illy",
        "pos": "adj",
        "ipa": "/ˈɪli/",
        "vi": "ốm yếu; khó ở; tồi tệ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085875",
        "hw": "ilosone",
        "pos": "noun",
        "ipa": "/ˈaɪləsoʊn/",
        "vi": "thuốc kháng sinh Ilosone",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085876",
        "hw": "ilxx",
        "pos": "num",
        "ipa": "/ˌsɪksti ˈnaɪn/",
        "vi": "sáu mươi chín (số La Mã)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085877",
        "hw": "ilxxx",
        "pos": "num",
        "ipa": "/ˌsɛvənti ˈnaɪn/",
        "vi": "bảy mươi chín (số La Mã)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085878",
        "hw": "imageable",
        "pos": "adj",
        "ipa": "/ˈɪmɪdʒəbəl/",
        "vi": "dễ tạo hình tượng; dễ hình dung",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085879",
        "hw": "imaged",
        "pos": "verb",
        "ipa": "/ˈɪmɪdʒd/",
        "vi": "đã khắc họa; đã mường tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085880",
        "hw": "imageless",
        "pos": "adj",
        "ipa": "/ˈɪmɪdʒləs/",
        "vi": "không có hình ảnh; vô tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085881",
        "hw": "imager",
        "pos": "noun",
        "ipa": "/ˈɪmɪdʒər/",
        "vi": "thiết bị tạo ảnh; người tạo hình",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085882",
        "hw": "images",
        "pos": "verb",
        "ipa": "/ˈɪmɪdʒɪz/",
        "vi": "khắc họa; hình dung trong trí",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085883",
        "hw": "imaginability",
        "pos": "noun",
        "ipa": "/ɪˌmædʒɪnəˈbɪlɪti/",
        "vi": "khả năng có thể tưởng tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085884",
        "hw": "imaginableness",
        "pos": "noun",
        "ipa": "/ɪˈmædʒɪnəbəlnəs/",
        "vi": "tính có thể hình dung được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085885",
        "hw": "imaginably",
        "pos": "adv",
        "ipa": "/ɪˈmædʒɪnəbli/",
        "vi": "có thể tưởng tượng được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085886",
        "hw": "imaginal",
        "pos": "adj",
        "ipa": "/ɪˈmædʒɪnəl/",
        "vi": "(thuộc) thành trùng (côn trùng)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085887",
        "hw": "imaginaria",
        "pos": "noun",
        "ipa": "/ˌɪmədʒɪˈnɛriə/",
        "vi": "thế giới tưởng tượng (số nhiều)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085888",
        "hw": "imaginarily",
        "pos": "adv",
        "ipa": "/ɪˈmædʒɪnərəli/",
        "vi": "một cách tưởng tượng; trong hư cấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085889",
        "hw": "imaginariness",
        "pos": "noun",
        "ipa": "/ɪˈmædʒɪnərinəs/",
        "vi": "tính chất ảo tưởng; tính hư cấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085890",
        "hw": "imaginational",
        "pos": "adj",
        "ipa": "/ɪˌmædʒɪˈneɪʃənəl/",
        "vi": "(thuộc) trí tưởng tượng; hư cấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085891",
        "hw": "imaginations",
        "pos": "noun",
        "ipa": "/ɪˌmædʒəˈneɪʃənz/",
        "vi": "những trí tưởng tượng; sự hư cấu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085892",
        "hw": "imaginativeness",
        "pos": "noun",
        "ipa": "/ɪˈmædʒɪnətɪvnəs/",
        "vi": "óc giàu tưởng tượng; sự sáng tạo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085893",
        "hw": "imagined",
        "pos": "verb",
        "ipa": "/ɪˈmædʒɪnd/",
        "vi": "đã tưởng tượng; đã hình dung",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085894",
        "hw": "imaginer",
        "pos": "noun",
        "ipa": "/ɪˈmædʒɪnər/",
        "vi": "người tưởng tượng; người mộng tưởng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085895",
        "hw": "imagines",
        "pos": "verb",
        "ipa": "/ɪˈmædʒɪnz/",
        "vi": "tưởng tượng; hình dung trong trí",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085896",
        "hw": "imagining",
        "pos": "verb",
        "ipa": "/ɪˈmædʒɪnɪŋ/",
        "vi": "đang tưởng tượng; đang mường tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085897",
        "hw": "imagisms",
        "pos": "noun",
        "ipa": "/ˈɪmɪdʒɪzəmz/",
        "vi": "các trào lưu thơ hình tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085898",
        "hw": "imagist",
        "pos": "noun",
        "ipa": "/ˈɪmɪdʒɪst/",
        "vi": "nhà thơ phái hình tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085899",
        "hw": "imagistic",
        "pos": "adj",
        "ipa": "/ˌɪmɪˈdʒɪstɪk/",
        "vi": "thuộc chủ nghĩa thơ hình tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085900",
        "hw": "imagistically",
        "pos": "adv",
        "ipa": "/ˌɪmɪˈdʒɪstɪkli/",
        "vi": "theo lối thơ hình tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085901",
        "hw": "imagists",
        "pos": "noun",
        "ipa": "/ˈɪmɪdʒɪsts/",
        "vi": "các nhà thơ phái hình tượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

if __name__ == "__main__":
    assert len(data) == 100, f"Expected 100, got {len(data)}"
    with open("scratch/b18_r02_raw_p4.json") as f:
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
    print("ALL 100 RECORDS IN PART 4 VERIFIED SUCCESSFULLY!")
