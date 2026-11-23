import json

RECORDS = [
    ("088203", "sopranists", "noun", "/səˈprɑːnɪsts/", "nam ca sĩ hát giọng nữ cao"),
    ("088204", "sora", "noun", "/ˈsɔːrə/", "chim gà nước nhỏ Bắc Mỹ"),
    ("088205", "sorachi", "noun", "/sɔːˈrɑːtʃi/", "phó tỉnh Sorachi (Hokkaido, Nhật)"),
    ("088206", "sorbefacient", "adj", "/ˌsɔːrbəˈfeɪʃənt/", "thúc đẩy sự hấp thu"),
    ("088207", "sorbic", "adj", "/ˈsɔːrbɪk/", "thuộc axit sorbic bảo quản"),
    ("088208", "sorbitol", "noun", "/ˈsɔːrbəˌtɔːl/", "chất tạo ngọt sorbitol"),
    ("088209", "sorbtion", "noun", "/ˈsɔːrpʃən/", "sự hấp phụ; quá trình hút bám"),
    ("088210", "sorcererous", "adj", "/ˈsɔːrsərəs/", "thuộc phép thuật phù thủy; ma mị"),
    ("088211", "sorcerers", "noun", "/ˈsɔːrsərərz/", "phù thủy; thầy pháp nam"),
    ("088212", "sorceresses", "noun", "/ˈsɔːrsərəsɪz/", "nữ phù thủy; bà đồng phép thuật"),
    ("088213", "sorceries", "noun", "/ˈsɔːrsəriz/", "phép thuật phù thủy; yêu thuật"),
    ("088214", "sorcerise", "verb", "/ˈsɔːrsəˌraɪz/", "yểm bùa mê; dùng ma thuật biến hóa"[:35]),
    ("088215", "sorcerize", "verb", "/ˈsɔːrsəˌraɪz/", "yểm bùa mê; dùng ma thuật biến hóa"[:35]),
    ("088216", "sordidly", "adv", "/ˈsɔːrdɪdli/", "bẩn thỉu nhớp nhúa; hèn hạ ti tiện"[:35]),
    ("088217", "sordine", "noun", "/sɔːrˈdiːn/", "ống hãm tiếng nhạc cụ đồng hay dây"[:35]),
    ("088218", "sordino", "noun", "/sɔːrˈdiːnoʊ/", "bộ giảm thanh nhạc cụ dây hay kèn"),
    ("088219", "soredial", "adj", "/səˈriːdiəl/", "thuộc ổ bào tử phấn địa y"),
    ("088220", "soredium", "noun", "/səˈriːdiəm/", "cụm sinh sản phấn ở địa y"),
    ("088221", "sorehead", "noun", "/ˈsɔːrˌhɛd/", "kẻ cay cú bất mãn hay hậm hực"),
    ("088222", "sorel", "noun", "/ˈsɔːrəl/", "hươu đực ba tuổi; màu hạt dẻ nhạt"),
    ("088223", "sorenesses", "noun", "/ˈsɔːrnəsɪz/", "cơn đau nhức; nỗi tự ái bực bội"),
    ("088224", "sorgho", "noun", "/ˈsɔːrɡoʊ/", "cây cao lương ngọt lấy mật"),
    ("088225", "sorgo", "noun", "/ˈsɔːrɡoʊ/", "cây cao lương ngọt lấy mật"),
    ("088226", "sori", "noun", "/ˈsɔːraɪ/", "ổ túi bào tử dưới lá dương xỉ"),
    ("088227", "soricidae", "noun", "/səˈrɪsɪˌdiː/", "họ Chuột chù (Soricidae)"),
    ("088228", "soricine", "adj", "/ˈsɔːrɪˌsaɪn/", "thuộc họ Chuột chù; giống chuột chù"[:35]),
    ("088229", "sorites", "noun", "/səˈraɪtiːz/", "tam đoạn luận nối tiếp; nghịch lý"),
    ("088230", "soritical", "adj", "/səˈrɪtɪkəl/", "thuộc tam đoạn luận dây chuyền"),
    ("088231", "sorn", "verb", "/sɔːrn/", "ăn bám chực chờ (tiếng Scotland)"),
    ("088232", "sorner", "noun", "/ˈsɔːrnər/", "kẻ ăn chực nằm vạ (Scotland)"),
    ("088233", "soroptimist", "noun", "/səˈrɑːptəmɪst/", "hội viên hội phụ nữ Soroptimist"),
    ("088234", "sororate", "noun", "/ˈsɔːrəˌreɪt/", "tục lấy chị em gái của vợ đã mất"),
    ("088235", "sororicide", "noun", "/səˈrɔːrəˌsaɪd/", "tội giết chị em gái ruột"),
    ("088236", "sorosis", "noun", "/səˈroʊsɪs/", "quả phức (quả dứa, dâu); hội nữ"),
    ("088237", "sorra", "adv", "/ˈsɑːrə/", "không hề; chẳng có (tiếng Ireland)"),
    ("088238", "sorrily", "adv", "/ˈsɔːrəli/", "thảm hại; đáng thương; xoàng xĩnh"),
    ("088239", "sorriness", "noun", "/ˈsɔːrinəs/", "vẻ tồi tàn đáng thương"),
    ("088240", "sorrowed", "verb", "/ˈsɑːroʊd/", "đã đau buồn; đã thương tiếc"),
    ("088241", "sorrower", "noun", "/ˈsɑːroʊər/", "người đang sầu thảm đau buồn"),
    ("088242", "sorrowfulness", "noun", "/ˈsɑːroʊfəlnəs/", "nỗi buồn rầu sầu thảm"),
    ("088243", "sorrows", "verb", "/ˈsɑːroʊz/", "đau buồn; sầu muộn thương tiếc"),
    ("088244", "sortable", "adj", "/ˈsɔːrtəbəl/", "có thể sắp xếp phân loại được"),
    ("088245", "sortilege", "noun", "/ˈsɔːrtɪlɪdʒ/", "thuật bói thẻ xin xăm; ma thuật"),
    ("088246", "sorts", "verb", "/sɔːrts/", "phân loại; sắp xếp theo thứ tự"),
    ("088247", "sorus", "noun", "/ˈsɔːrəs/", "ổ túi bào tử (dương xỉ, nấm)"),
    ("088248", "sosalist", "noun", "/ˈsoʊdəlɪst/", "hội viên đoàn thể tôn giáo"),
    ("088249", "sotelo", "noun", "/soʊˈtɛloʊ/", "tên họ Tây Ban Nha Sotelo"),
    ("088250", "soteriologic", "adj", "/soʊˌtɪriəˈlɑːdʒɪk/", "thuộc thần học cứu rỗi"),
    ("088251", "sothic", "adj", "/ˈsɑːθɪk/", "thuộc sao Thiên Lang (Ai Cập cổ)"),
    ("088252", "sottish", "adj", "/ˈsɑːtɪʃ/", "say xỉn đờ đẫn; nghiện rượu chè"),
    ("088253", "sottishly", "adv", "/ˈsɑːtɪʃli/", "say xỉn đờ đẫn; nghiện ngập"),
    ("088254", "sottishness", "noun", "/ˈsɑːtɪʃnəs/", "tình trạng say xỉn ngu muội"),
    ("088255", "souari", "noun", "/ˈswaːri/", "cây gỗ cứng hạt béo souari Nam Mỹ"),
    ("088256", "soubisse", "noun", "/suːˈbiːz/", "nước xốt kem hành tây kiểu Pháp"),
    ("088257", "soucar", "noun", "/saʊˈkɑːr/", "chủ ngân hàng Ấn Độ truyền thống"),
    ("088258", "soufflot", "noun", "/suːˈfloʊ/", "kiến trúc sư Pháp J.-G. Soufflot"),
    ("088259", "soughed", "verb", "/saʊd/", "đã thổi rì rào vi vu (gió, cây)"),
    ("088260", "soughing", "adj", "/ˈsaʊɪŋ/", "thổi vi vu; rì rào êm ả"),
    ("088261", "soughingly", "adv", "/ˈsaʊɪŋli/", "rì rào vi vu theo gió"),
    ("088262", "soughs", "verb", "/saʊz/", "thổi vi vu; kêu rì rào nhẹ"),
    ("088263", "soulfuls", "noun", "/ˈsoʊlfəlz/", "cảm xúc sâu lắng (âm nhạc soul)"),
    ("088264", "soullessly", "adv", "/ˈsoʊlləsli/", "vô hồn; lạnh lẽo máy móc nhạt nhẽo"[:35]),
    ("088265", "soullessness", "noun", "/ˈsoʊlləsnəs/", "sự vô hồn lạnh lẽo; tính nhạt nhẽo"),
    ("088266", "soulsful", "adj", "/ˈsoʊlfəl/", "tràn đầy cảm xúc sâu lắng"),
    ("088267", "soundable", "adj", "/ˈsaʊndəbəl/", "có thể đo độ sâu; có thể dò xét"),
    ("088268", "sounded", "verb", "/ˈsaʊndɪd/", "đã phát âm thanh; nghe có vẻ; dò"),
    ("088269", "soundlessness", "noun", "/ˈsaʊndləsnəs/", "sự tĩnh lặng tuyệt đối không tiếng"),
    ("088270", "sounds", "noun", "/saʊndz/", "âm thanh; tiếng động; eo biển"),
    ("088271", "souped", "verb", "/suːpt/", "đã độ động cơ cho mạnh hơn"),
    ("088272", "soupfin", "noun", "/ˈsuːpˌfɪn/", "cá mập vây nấu súp Galeorhinus"),
    ("088273", "soupiness", "noun", "/ˈsuːpinəs/", "độ sệt loãng như súp; tính sến sẩm"[:35]),
    ("088274", "souping", "verb", "/ˈsuːpɪŋ/", "đang độ động cơ; sụp đổ"),
    ("088275", "soups", "verb", "/suːps/", "nâng cấp động cơ cho khỏe hơn"),
    ("088276", "soupson", "noun", "/suːpˈsɔːn/", "một chút xíu; một thoáng (tiếng Pháp)"[:35]),
    ("088277", "soupspoon", "noun", "/ˈsuːpˌspuːn/", "thìa lòng sâu ăn súp"),
    ("088278", "sourball", "noun", "/ˈsaʊərˌbɔːl/", "kẹo cứng vị chua hình viên tròn"),
    ("088279", "sourdine", "noun", "/sʊrˈdiːn/", "bộ phận giảm âm thanh nhạc cụ"),
    ("088280", "sourish", "adj", "/ˈsaʊərɪʃ/", "hơi chua; chua chua"),
    ("088281", "sournesses", "noun", "/ˈsaʊərnəsɪz/", "vị chua; thái độ cáu kỉnh gắt gỏng"[:35]),
    ("088282", "sours", "verb", "/ˈsaʊərz/", "làm chua; khiến cay đắng rạn nứt"),
    ("088283", "souschef", "noun", "/ˈsuːˌʃɛf/", "bếp phó trong nhà hàng"),
    ("088284", "souses", "verb", "/ˈsaʊsɪz/", "ngâm giấm; dội ướt sũng; uống say"),
    ("088285", "sousing", "noun", "/ˈsaʊsɪŋ/", "sự dội ướt sũng; trận mưa như trút"),
    ("088286", "souslik", "noun", "/ˈsuːslɪk/", "sóc đất Á-Âu"),
    ("088287", "soutache", "noun", "/suːˈtæʃ/", "dây bện dẹt trang trí viền áo"),
    ("088288", "souteneur", "noun", "/ˌsuːtəˈnɜːr/", "kẻ môi giới mại dâm (từ Pháp)"),
    ("088289", "souter", "noun", "/ˈsuːtər/", "thợ đóng giày (phương ngữ Scotland)"),
    ("088290", "souterrain", "noun", "/ˈsuːtəˌreɪn/", "hầm ngầm đá thời tiền sử"),
    ("088291", "southeaster", "noun", "/ˌsaʊθˈiːstər/", "gió mạnh hay bão thổi hướng đông nam"[:35]),
    ("088292", "southeastwardly", "adv", "/ˌsaʊθˈiːstwərdli/", "theo hướng đông nam"),
    ("088293", "southeastwards", "adv", "/ˌsaʊθˈiːstwərdz/", "về phía đông nam"),
    ("088294", "southernise", "verb", "/ˈsʌðərˌnaɪz/", "mang phong cách miền Nam hóa"),
    ("088295", "southernism", "noun", "/ˈsʌðərˌnɪzəm/", "lối nói đặc trưng miền Nam Mỹ"),
    ("088296", "southernize", "verb", "/ˈsʌðərˌnaɪz/", "mang phong cách miền Nam hóa"),
    ("088297", "southernizm", "noun", "/ˈsʌðərˌnɪzəm/", "cách nói đặc trưng miền Nam Mỹ"),
    ("088298", "southernness", "noun", "/ˈsʌðərnnəs/", "đặc tính phương Nam"),
    ("088299", "southing", "noun", "/ˈsaʊðɪŋ/", "sự dịch chuyển về hướng nam"),
    ("088300", "southron", "noun", "/ˈsʌðrən/", "người Anh (cách gọi từ Scotland)"),
    ("088301", "southwardly", "adj", "/ˈsaʊθwərdli/", "hướng về phía nam; từ hướng nam"),
    ("088302", "southwester", "noun", "/ˌsaʊθˈwɛstər/", "gió tây nam; mũ đi biển chống mưa"),
]

# Remove slices cleanly <= 35 chars
RECORDS[11] = ("088214", "sorcerise", "verb", "/ˈsɔːrsəˌraɪz/", "yểm bùa mê; dùng ma thuật")
RECORDS[12] = ("088215", "sorcerize", "verb", "/ˈsɔːrsəˌraɪz/", "yểm bùa mê; dùng ma thuật")
RECORDS[13] = ("088216", "sordidly", "adv", "/ˈsɔːrdɪdli/", "bẩn thỉu nhớp nhúa; hèn hạ")
RECORDS[14] = ("088217", "sordine", "noun", "/sɔːrˈdiːn/", "ống hãm tiếng nhạc cụ")
RECORDS[25] = ("088228", "soricine", "adj", "/ˈsɔːrɪˌsaɪn/", "thuộc họ Chuột chù")
RECORDS[61] = ("088264", "soullessly", "adv", "/ˈsoʊlləsli/", "vô hồn; lạnh lẽo máy móc")
RECORDS[70] = ("088273", "soupiness", "noun", "/ˈsuːpinəs/", "độ sệt loãng như súp; vẻ sến")
RECORDS[73] = ("088276", "soupson", "noun", "/suːpˈsɔːn/", "một chút xíu; một thoáng")
RECORDS[78] = ("088281", "sournesses", "noun", "/ˈsaʊərnəsɪz/", "vị chua; tính cáu kỉnh gắt gỏng")
RECORDS[88] = ("088291", "southeaster", "noun", "/ˌsaʊθˈiːstər/", "gió hay bão thổi từ hướng đông nam")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r07_raw_p3.json"))
by_id = {r["id"].split(".")[-1]: r for r in raw}
out = []
for sid, hw, pos, ipa, vi in RECORDS:
    rec = dict(by_id[sid])
    assert rec["hw"] == hw, (sid, hw, rec["hw"])
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

json.dump(out, open("scratch/b38_r07_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b38_r07_p3 saved OK")
