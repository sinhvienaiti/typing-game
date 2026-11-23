import json

RECORDS = [
    ("088803", "spleenwort", "noun", "/ˈspliːnˌwɜːrt/", "cây dương xỉ tổ chim Asplenium"),
    ("088804", "spleeny", "adj", "/ˈspliːni/", "u uất cáu kỉnh; hay bực dọc"),
    ("088805", "splenalgia", "noun", "/splɪˈnældʒə/", "chứng đau vùng lá lách"),
    ("088806", "splenalgic", "adj", "/splɪˈnældʒɪk/", "thuộc đau vùng lá lách"),
    ("088807", "splendent", "adj", "/ˈsplɛndənt/", "rực rỡ chói lọi; sáng lóng lánh"),
    ("088808", "splendorous", "adj", "/ˈsplɛndərəs/", "tráng lệ huy hoàng; rực rỡ"),
    ("088809", "splendourous", "adj", "/ˈsplɛndərəs/", "tráng lệ huy hoàng; rực rỡ"),
    ("088810", "splenectomized", "adj", "/splɪˈnɛktəˌmaɪzd/", "đã phẫu thuật cắt bỏ lá lách"),
    ("088811", "splenetical", "adj", "/splɪˈnɛtɪkəl/", "thuộc lá lách; hay cáu gắt u uất"),
    ("088812", "splenetically", "adv", "/splɪˈnɛtɪkli/", "gắt gỏng cay nghiệt; u uất"),
    ("088813", "splenial", "adj", "/ˈspliːniəl/", "thuộc cơ gối cổ; có dạng nẹp"),
    ("088814", "splenii", "noun", "/ˈspliːniˌaɪ/", "cơ gối đầu cổ (giải phẫu)"),
    ("088815", "splenitic", "adj", "/splɪˈnɪtɪk/", "viêm lá lách; hay cáu kỉnh"),
    ("088816", "splenitis", "noun", "/splɪˈnaɪtɪs/", "bệnh viêm lá lách"),
    ("088817", "splenitive", "adj", "/ˈsplɛnətɪv/", "dễ nổi nóng; bồng bột cáu gắt"),
    ("088818", "splenius", "noun", "/ˈspliːniəs/", "cơ gối đầu cổ (giải phẫu)"),
    ("088819", "splenization", "noun", "/ˌsplɛnəˈzeɪʃən/", "sự sung huyết phổi giống mô lách"),
    ("088820", "splenocyte", "noun", "/ˈsplɛnəˌsaɪt/", "tế bào lách; bạch cầu đơn nhân"),
    ("088821", "splenography", "noun", "/splɪˈnɑːɡrəfi/", "kỹ thuật chụp X-quang lá lách"),
    ("088822", "splenoid", "adj", "/ˈspliːnɔɪd/", "giống mô lá lách"),
    ("088823", "splenology", "noun", "/splɪˈnɑːlədʒi/", "khoa học nghiên cứu về lá lách"),
    ("088824", "splenopathy", "noun", "/splɪˈnɑːpəθi/", "bệnh lý ở lá lách"),
    ("088825", "splenotomy", "noun", "/splɪˈnɑːtəmi/", "phẫu thuật rạch mở lá lách"),
    ("088826", "spliced", "verb", "/splaɪst/", "đã ghép nối dây cáp; đã cắt ghép"),
    ("088827", "splices", "verb", "/ˈsplaɪsɪz/", "ghép nối đầu dây; cắt ghép gen"),
    ("088828", "splining", "noun", "/ˈsplaɪnɪŋ/", "gia công cắt rãnh then hoa trục"),
    ("088829", "splinted", "verb", "/ˈsplɪntɪd/", "đã nẹp cố định xương gãy"),
    ("088830", "splintered", "verb", "/ˈsplɪntərd/", "đã vỡ vụn thành mảnh; chia rẽ"),
    ("088831", "splinterless", "adj", "/ˈsplɪntərləs/", "không vỡ văng mảnh sắc; chống vỡ"),
    ("088832", "splinterproof", "adj", "/ˈsplɪntərˌpruːf/", "chống vỡ bắn mảnh sắc nhọn"),
    ("088833", "splinting", "verb", "/ˈsplɪntɪŋ/", "đang bó nẹp cố định xương gãy"),
    ("088834", "splints", "verb", "/splɪnts/", "bó nẹp cố định xương bị gãy"),
    ("088835", "splipy", "adj", "/ˈslɪpi/", "trơn trượt; khôn lỏi nhanh nhẹn"),
    ("088836", "spliting", "adj", "/ˈsplɪtɪŋ/", "đau như búa bổ; vỡ òa (cười)"),
    ("088837", "splitsaw", "noun", "/ˈsplɪtˌsɔː/", "máy cưa xẻ dọc gỗ"),
    ("088838", "splittable", "adj", "/ˈsplɪtəbəl/", "có thể tách đôi hay chẻ ra được"),
    ("088839", "splittism", "noun", "/ˈsplɪtˌɪzəm/", "chủ nghĩa bè phái; sự chia rẽ"),
    ("088840", "splitworm", "noun", "/ˈsplɪtˌwɜːrm/", "sâu đục lá khoai tây và thuốc lá"),
    ("088841", "splotches", "verb", "/ˈsplɑːtʃɪz/", "làm vấy đốm lem nhem"),
    ("088842", "splotching", "verb", "/ˈsplɑːtʃɪŋ/", "đang làm vấy đốm lem nhem"),
    ("088843", "splotchy", "adj", "/ˈsplɑːtʃi/", "lem nhem loang lổ nhiều vết đốm"),
    ("088844", "splurged", "verb", "/splɜːrdʒd/", "đã vung tiền chi tiêu xả láng"),
    ("088845", "splurges", "verb", "/ˈsplɜːrdʒɪz/", "vung tiền chi tiêu hoang phí"),
    ("088846", "splurging", "verb", "/ˈsplɜːrdʒɪŋ/", "đang vung tiền chi tiêu xả láng"),
    ("088847", "spluttered", "verb", "/ˈsplʌtərd/", "đã nói lắp bắp; đã nổ lách tách"),
    ("088848", "splutterer", "noun", "/ˈsplʌtərər/", "người nói lắp bắp ấp úng"),
    ("088849", "spluttering", "verb", "/ˈsplʌtərɪŋ/", "đang nói lắp bắp; nổ lách tách"),
    ("088850", "splutters", "verb", "/ˈsplʌtərz/", "nói lắp bắp văng nước; lách tách"),
    ("088851", "spoffish", "adj", "/ˈspɑːfɪʃ/", "lăng xăng bận rộn một cách ồn ào"),
    ("088852", "spoilable", "adj", "/ˈspɔɪləbəl/", "dễ hư hỏng; dễ bị ôi thiu"),
    ("088853", "spoilation", "noun", "/ˌspɔɪˈleɪʃən/", "sự cướp phá tước đoạt"),
    ("088854", "spoils", "verb", "/spɔɪlz/", "làm hư hỏng; chiều hư; ôi thiu"),
    ("088855", "spoilsman", "noun", "/ˈspɔɪlzmən/", "chính khách chia chác bổng lộc phe"[:35]),
    ("088856", "spokeshave", "noun", "/ˈspoʊkˌʃeɪv/", "bào hai tay cầm dùng gọt cong"),
    ("088857", "spokeshaves", "noun", "/ˈspoʊkˌʃeɪvz/", "bào hai tay cầm gọt bề mặt cong"),
    ("088858", "spokewise", "adv", "/ˈspoʊkˌwaɪz/", "tỏa tròn đều như nan hoa bánh xe"),
    ("088859", "spoliate", "verb", "/ˈspoʊliˌeɪt/", "cướp bóc; tước đoạt; phá hủy"),
    ("088860", "spoliator", "noun", "/ˈspoʊliˌeɪtər/", "kẻ cướp bóc tước đoạt; kẻ phá hoại"[:35]),
    ("088861", "spoliatory", "adj", "/ˈspoʊliəˌtɔːri/", "có tính chất cướp đoạt bóc lột"),
    ("088862", "spondaic", "adj", "/spɑːnˈdeɪɪk/", "thuộc nhịp thơ hai âm tiết nặng"),
    ("088863", "spondaical", "adj", "/spɑːnˈdeɪɪkəl/", "theo nhịp hai âm tiết nhấn mạnh"),
    ("088864", "spondaise", "verb", "/ˈspɑːndaɪz/", "chuyển thành nhịp thơ hai âm nhấn"),
    ("088865", "spondaize", "verb", "/ˈspɑːndaɪz/", "chuyển thành nhịp thơ hai âm nhấn"),
    ("088866", "spondias", "noun", "/ˈspɑːndiəs/", "chi Cây cóc; cây dâu da xoan"),
    ("088867", "spondilus", "noun", "/ˈspɑːndɪləs/", "đốt sống; sò gai biển Spondylus"),
    ("088868", "spondulicks", "noun", "/spɑːnˈduːlɪks/", "tiền bạc (tiếng lóng cổ Mỹ)"),
    ("088869", "spondyl", "noun", "/ˈspɑːndɪl/", "đốt sống"),
    ("088870", "spondylarthritis", "noun", "/ˌspɑːndɪloʊɑːrˈθraɪtɪs/", "viêm khớp cột sống"),
    ("088871", "spondyle", "noun", "/ˈspɑːndɪl/", "đốt sống"),
    ("088872", "spondyloarthropathies", "noun", "/ˌspɑːndɪloʊɑːrˈθrɑːpəθiz/", "bệnh lý khớp cột sống"),
    ("088873", "spondyloarthropathy", "noun", "/ˌspɑːndɪloʊɑːrˈθrɑːpəθi/", "bệnh lý khớp cột sống"),
    ("088874", "spondylotherapeutics", "noun", "/ˌspɑːndɪloʊˌθɛrəˈpjuːtɪks/", "phép chữa trị bệnh cột sống"),
    ("088875", "spondylotherapy", "noun", "/ˌspɑːndɪloʊˈθɛrəpi/", "liệu pháp điều trị cột sống"),
    ("088876", "spondylous", "adj", "/ˈspɑːndɪləs/", "thuộc đốt sống"),
    ("088877", "sponged", "verb", "/spʌndʒd/", "đã lau bằng bọt biển; đã ăn chực"),
    ("088878", "spongefly", "noun", "/ˈspʌndʒˌflaɪ/", "bọ cánh gân sống ký sinh bọt biển"),
    ("088879", "spongelike", "adj", "/ˈspʌndʒˌlaɪk/", "mềm xốp thấm nước như bọt biển"),
    ("088880", "spongeous", "adj", "/ˈspʌndʒəs/", "xốp mềm nhiều lỗ như bọt biển"),
    ("088881", "sponges", "verb", "/ˈspʌndʒɪz/", "lau bằng bọt biển; sống ăn bám"),
    ("088882", "spongiform", "adj", "/ˈspʌndʒɪˌfɔːrm/", "dạng xốp giống bọt biển (bệnh não)"),
    ("088883", "spongillafly", "noun", "/spʌnˈdʒɪləˌflaɪ/", "bọ cánh gân ký sinh bọt biển ngọt"),
    ("088884", "spongin", "noun", "/ˈspʌndʒɪn/", "chất protein sừng tạo khung bọt biển"[:35]),
    ("088885", "sponging", "verb", "/ˈspʌndʒɪŋ/", "đang lau bọt biển; đang ăn chực"),
    ("088886", "spongioblast", "noun", "/ˈspʌndʒioʊˌblæst/", "nguyên bào thần kinh đệm"),
    ("088887", "spongioblastoma", "noun", "/ˌspʌndʒioʊblæˈstoʊmə/", "u nguyên bào thần kinh đệm"),
    ("088888", "sponsion", "noun", "/ˈspɑːnʃən/", "cam kết bảo lãnh nhân danh quốc gia"[:35]),
    ("088889", "sponson", "noun", "/ˈspɑːnsən/", "cánh phao hông tàu thủy hay máy bay"[:35]),
    ("088890", "sponsorial", "adj", "/spɑːnˈsɔːriəl/", "thuộc nhà tài trợ hay người bảo trợ"[:35]),
    ("088891", "sponsors", "noun", "/ˈspɑːnsərz/", "nhà tài trợ; người bảo trợ"),
    ("088892", "spontaneousness", "noun", "/spɑːnˈteɪniəsnəs/", "tính tự phát; sự hồn nhiên"),
    ("088893", "spontoon", "noun", "/spɑːnˈtuːn/", "ngọn giáo ngắn của sĩ quan bộ binh"),
    ("088894", "spontoons", "noun", "/spɑːnˈtuːnz/", "ngọn giáo ngắn sĩ quan xưa"),
    ("088895", "spoofed", "verb", "/spuːft/", "đã nhại hài hước; đã giả mạo"),
    ("088896", "spoofer", "noun", "/ˈspuːfər/", "người nhại giễu; kẻ giả mạo lừa"),
    ("088897", "spoofing", "verb", "/ˈspuːfɪŋ/", "đang nhại hài; đang giả mạo dữ liệu"[:35]),
    ("088898", "spoofs", "verb", "/spuːfs/", "nhại hài hước; giả mạo đánh lừa"),
    ("088899", "spookier", "adj", "/ˈspuːkiər/", "rùng rợn hơn; ma quái hơn"),
    ("088900", "spookiest", "adj", "/ˈspuːkiɪst/", "rùng rợn nhất; ma quái nhất"),
    ("088901", "spookiness", "noun", "/ˈspuːkinəs/", "vẻ rùng rợn ma quái kỳ bí"),
    ("088902", "spookish", "adj", "/ˈspuːkɪʃ/", "hơi ma quái rùng rợn; nhát như ma"),
]

# Remove all slices cleanly <= 35 chars
RECORDS[52] = ("088855", "spoilsman", "noun", "/ˈspɔɪlzmən/", "chính khách chia chác bổng lộc")
RECORDS[57] = ("088860", "spoliator", "noun", "/ˈspoʊliˌeɪtər/", "kẻ cướp bóc; kẻ phá hoại tài sản")
RECORDS[81] = ("088884", "spongin", "noun", "/ˈspʌndʒɪn/", "protein sừng tạo khung bọt biển")
RECORDS[85] = ("088888", "sponsion", "noun", "/ˈspɑːnʃən/", "lời cam kết bảo lãnh quốc tế")
RECORDS[86] = ("088889", "sponson", "noun", "/ˈspɑːnsən/", "cánh phao thăng bằng mạn tàu")
RECORDS[87] = ("088890", "sponsorial", "adj", "/spɑːnˈsɔːriəl/", "thuộc nhà tài trợ; bảo trợ")
RECORDS[94] = ("088897", "spoofing", "verb", "/ˈspuːfɪŋ/", "đang nhại hài; đang giả mạo tin")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r08_raw_p4.json"))
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

json.dump(out, open("scratch/b38_r08_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b38_r08_p4 saved OK")
