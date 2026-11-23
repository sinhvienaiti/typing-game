import json

records = [
    ("081803", "reasonning", "noun", "/ˈriːzənɪŋ/", "sự suy luận, lý lẽ (lỗi viết)"),
    ("081804", "reasons", "verb", "/ˈriːzənz/", "suy luận, lập luận, thuyết phục"),
    ("081805", "reassail", "verb", "/ˌriːəˈseɪl/", "tấn công lại, công kích lần nữa"),
    ("081806", "reassembled", "verb", "/ˌriːəˈsɛmbəld/", "đã lắp ráp lại, đã tập hợp lại"),
    ("081807", "reassembles", "verb", "/ˌriːəˈsɛmbəlz/", "lắp ráp lại (máy); tập hợp lại"),
    ("081808", "reassembling", "verb", "/ˌriːəˈsɛmblɪŋ/", "lắp ráp lại; tập hợp lại đông đủ"),
    ("081809", "reasserted", "verb", "/ˌriːəˈsɜːrtɪd/", "đã khẳng định lại, đòi lại quyền"),
    ("081810", "reasserting", "verb", "/ˌriːəˈsɜːrtɪŋ/", "khẳng định lại dứt khoát; tái lập"),
    ("081811", "reasserts", "verb", "/ˌriːəˈsɜːrts/", "khẳng định lại, bảo vệ lại quyền"),
    ("081812", "reassessed", "verb", "/ˌriːəˈsɛst/", "đã đánh giá lại, định giá lại"),
    ("081813", "reassesses", "verb", "/ˌriːəˈsɛsɪz/", "đánh giá lại, xem xét lại mức độ"),
    ("081814", "reassessing", "verb", "/ˌriːəˈsɛsɪŋ/", "đánh giá lại, thẩm định lại"),
    ("081815", "reassume", "verb", "/ˌriːəˈsuːm/", "đảm nhận lại; khoác lại vẻ ngoài"),
    ("081816", "reassures", "verb", "/ˌriːəˈʃʊrz/", "trấn an, làm yên lòng, cam đoan lại"),
    ("081817", "reattatch", "verb", "/ˌriːəˈtætʃ/", "gắn lại, nối lại (lỗi viết)"),
    ("081818", "reattempt", "verb", "/ˌriːəˈtɛmpt/", "thử lại lần nữa, cố gắng lại"),
    ("081819", "reattempted", "verb", "/ˌriːəˈtɛmptɪd/", "đã thử lại lần nữa, đã nỗ lực lại"),
    ("081820", "reattempting", "verb", "/ˌriːəˈtɛmptɪŋ/", "thử lại lần nữa, thực hiện lại"),
    ("081821", "reattempts", "verb", "/ˌriːəˈtɛmpts/", "thử lại lần nữa, cố gắng lại"),
    ("081822", "reattribute", "verb", "/ˌriːəˈtrɪbjuːt/", "quy cho tác giả khác, gán nguồn lại"),
    ("081823", "reaumur", "noun", "/ˈreɪəˌmjʊr/", "nhiệt giai Réaumur (đóng băng 0-80)"),
    ("081824", "reawakened", "verb", "/ˌriːəˈweɪkənd/", "đã thức tỉnh lại, khơi dậy lại"),
    ("081825", "reawakening", "verb", "/ˌriːəˈweɪkənɪŋ/", "đánh thức lại, khơi dậy cảm xúc"),
    ("081826", "reawakens", "verb", "/ˌriːəˈweɪkənz/", "thức tỉnh trở lại, khơi dậy lại"),
    ("081827", "rebake", "verb", "/riˈbeɪk/", "nướng lại (bánh), nung lại (gạch)"),
    ("081828", "reballasting", "noun", "/riˈbælʌstɪŋ/", "sự rải lại đá dăm đường ray"),
    ("081829", "rebaptise", "verb", "/riˈbæpˌtaɪz/", "rửa tội lại; đặt tên mới (Anh)"),
    ("081830", "rebaptism", "noun", "/riˈbæpˌtɪzəm/", "lễ rửa tội lại; sự đặt lại tên mới"),
    ("081831", "rebaptize", "verb", "/riˈbæpˌtaɪz/", "rửa tội lại; đặt lại tên mới cho"),
    ("081832", "rebarbarise", "verb", "/riˈbɑːrbəˌraɪz/", "đưa trở lại thời mông muội (Anh)"),
    ("081833", "rebarbarize", "verb", "/riˈbɑːrbəˌraɪz/", "làm trở nên dã man man rợ trở lại"),
    ("081834", "rebarbative", "adj", "/rɪˈbɑːrbətɪv/", "gây khó chịu, thô lỗ phản cảm"),
    ("081835", "rebated", "verb", "/ˈriːbeɪtɪd/", "đã chiết khấu, đã hoàn tiền lại"),
    ("081836", "rebates", "verb", "/ˈriːbeɪts/", "chiết khấu, giảm giá hoàn tiền"),
    ("081837", "rebating", "verb", "/ˈriːbeɪtɪŋ/", "chiết khấu, hoàn trả lại một phần"),
    ("081838", "rebato", "noun", "/rəˈbɑːtoʊ/", "cổ áo ren dựng cao thế kỷ 17"),
    ("081839", "rebbe", "noun", "/ˈrɛbi/", "vị thầy tinh thần Do Thái giáo"),
    ("081840", "rebec", "noun", "/ˈriːbɛk/", "đàn vĩ cầm cổ ba dây thời Trung cổ"),
    ("081841", "rebeck", "noun", "/ˈriːbɛk/", "đàn vĩ cầm ba dây (biến thể cổ)"),
    ("081842", "rebelled", "verb", "/rɪˈbɛld/", "đã nổi loạn, đã nổi dậy chống đối"),
    ("081843", "rebelling", "verb", "/rɪˈbɛlɪŋ/", "nổi loạn, nổi dậy, phản kháng mạnh"),
    ("081844", "rebellow", "verb", "/riˈbɛloʊ/", "gầm vang dội lại (tiếng bò, sấm)"),
    ("081845", "rebels", "verb", "/rɪˈbɛlz/", "nổi loạn, nổi dậy; chống đối lại"),
    ("081846", "rebidding", "noun", "/riˈbɪdɪŋ/", "sự đấu thầu lại, sự bỏ giá lại"),
    ("081847", "rebinding", "noun", "/riˈbaɪndɪŋ/", "việc đóng gáy sách lại; sự bó lại"),
    ("081848", "reblossom", "verb", "/riˈblɑːsəm/", "nở hoa trở lại (cây cối, hy vọng)"),
    ("081849", "reboant", "adj", "/rɪˈboʊənt/", "vang vọng ầm ĩ, rền vang (thơ cổ)"),
    ("081850", "reboisement", "noun", "/riˈbwɑːzmənt/", "sự trồng lại rừng (thuật ngữ cũ)"),
    ("081851", "rebore", "verb", "/riˈbɔːr/", "doa lại xi-lanh động cơ (cơ khí)"),
    ("081852", "reboxetine", "noun", "/riˈbɑːksətiːn/", "thuốc chống trầm cảm reboxetine"),
    ("081853", "rebroadcasting", "noun", "/ˌriːˈbrɔːdkæstɪŋ/", "việc phát sóng lại, tiếp sóng"),
    ("081854", "rebuffed", "verb", "/rɪˈbʌft/", "đã khước từ phũ phàng, đẩy lùi"),
    ("081855", "rebuffing", "verb", "/rɪˈbʌfɪŋ/", "khước từ phũ phàng, bác bỏ thẳng"),
    ("081856", "rebuffs", "verb", "/rɪˈbʌfs/", "khước từ phũ phàng, gạt phăng"),
    ("081857", "rebuilded", "verb", "/ˌriːˈbɪldɪd/", "đã xây dựng lại (dạng không chuẩn)"),
    ("081858", "rebuilt", "verb", "/ˌriːˈbɪlt/", "đã xây dựng lại, đã tái thiết"),
    ("081859", "rebuked", "verb", "/rɪˈbjuːkt/", "đã khiển trách, đã quở mắng"),
    ("081860", "rebuker", "noun", "/rɪˈbjuːkər/", "người khiển trách, người quở trách"),
    ("081861", "rebukes", "verb", "/rɪˈbjuːks/", "khiển trách, quở mắng nghiêm khắc"),
    ("081862", "rebuking", "verb", "/rɪˈbjuːkɪŋ/", "khiển trách, quở mắng, phê bình"),
    ("081863", "rebukingly", "adv", "/rɪˈbjuːkɪŋli/", "với giọng khiển trách, quở mắng"),
    ("081864", "reburied", "verb", "/riˈbɛrid/", "đã cải táng, đã chôn cất lại"),
    ("081865", "reburies", "verb", "/riˈbɛriz/", "cải táng, bốc mộ chôn cất lại"),
    ("081866", "reburying", "noun", "/riˈbɛriɪŋ/", "việc cải táng, sự chôn cất lại"),
    ("081867", "rebutment", "noun", "/rɪˈbʌtmənt/", "sự bác bỏ, lập luận phản bác"),
    ("081868", "rebuts", "verb", "/rɪˈbʌts/", "bác bỏ, phản bác bằng chứng cứ"),
    ("081869", "rebutted", "verb", "/rɪˈbʌtɪd/", "đã bác bỏ, đã phản bác chứng cứ"),
    ("081870", "rebutter", "noun", "/rɪˈbʌtər/", "lời phản bác; người bác bỏ"),
    ("081871", "rebutting", "verb", "/rɪˈbʌtɪŋ/", "bác bỏ, phản bác lập luận"),
    ("081872", "rec", "noun", "/rɛk/", "sự giải trí; sự ghi hình (viết tắt)"),
    ("081873", "recalcitrancy", "noun", "/rɪˈkælsətrənsi/", "tính bướng bỉnh ngoan cố, khó bảo"),
    ("081874", "recalcitrate", "verb", "/rɪˈkælsəˌtreɪt/", "chống đối kịch liệt, bướng bỉnh"),
    ("081875", "recalcitration", "noun", "/rɪˌkælsəˈtreɪʃən/", "sự phản kháng ngoan cố, cãi lại"),
    ("081876", "recalesce", "verb", "/ˌriːkəˈlɛs/", "tái phát sáng khi thép nguội dần"),
    ("081877", "recalescence", "noun", "/ˌriːkəˈlɛsəns/", "hiện tượng thép đỏ sáng khi nguội"),
    ("081878", "recalescent", "adj", "/ˌriːkəˈlɛsənt/", "tái phát sáng khi thép nguội"),
    ("081879", "recalibration", "noun", "/ˌriːkæləˈbreɪʃən/", "sự hiệu chuẩn lại, điều chỉnh lại"),
    ("081880", "recalking", "noun", "/riˈkɔːkɪŋ/", "sự xảm trét lại khe ván tàu thuyền"),
    ("081881", "recallable", "adj", "/rɪˈkɔːləbəl/", "có thể triệu hồi, thu hồi lại"),
    ("081882", "recalled", "verb", "/rɪˈkɔːld/", "đã nhớ lại; đã thu hồi, triệu hồi"),
    ("081883", "recalling", "verb", "/rɪˈkɔːlɪŋ/", "nhớ lại, hồi tưởng; triệu hồi"),
    ("081884", "recalls", "verb", "/rɪˈkɔːlz/", "nhớ lại, gợi nhớ; thu hồi sản phẩm"),
    ("081885", "recapitulative", "adj", "/ˌriːkəˈpɪtʃəˌleɪtɪv/", "tóm tắt lại; lặp lại tiến hóa"),
    ("081886", "recapped", "verb", "/ˈriːkæpt/", "đã tóm tắt lại; đã đắp lại lốp xe"),
    ("081887", "recapping", "verb", "/ˈriːkæpɪŋ/", "tóm tắt lại ngắn gọn; đắp lại lốp"),
    ("081888", "recaps", "verb", "/ˈriːkæps/", "tóm tắt điểm chính; đắp lại lốp xe"),
    ("081889", "recaptured", "verb", "/ˌriːˈkæptʃərd/", "đã chiếm lại, bắt giữ lại"),
    ("081890", "recaptures", "verb", "/ˌriːˈkæptʃərz/", "chiếm lại, bắt lại; tái hiện lại"),
    ("081891", "recapturing", "verb", "/ˌriːˈkæptʃərɪŋ/", "chiếm lại, bắt lại; tái hiện lại"),
    ("081892", "reccy", "noun", "/ˈrɛki/", "cuộc trinh sát thực địa (lóng Anh)"),
    ("081893", "receded", "verb", "/rɪˈsiːdɪd/", "đã lùi lại, đã rút xuống, mờ dần"),
    ("081894", "recedes", "verb", "/rɪˈsiːdz/", "lùi lại, rút xuống; giảm bớt dần"),
    ("081895", "receipted", "verb", "/rɪˈsiːtɪd/", "đã ký nhận thanh toán (biên lai)"),
    ("081896", "receipter", "noun", "/rɪˈsiːtər/", "người ký biên nhận bảo lãnh tài sản"),
    ("081897", "receipting", "verb", "/rɪˈsiːtɪŋ/", "ký xác nhận thu tiền biên lai"),
    ("081898", "receives", "verb", "/rɪˈsiːvz/", "nhận, tiếp nhận; tiếp đón, đón tiếp"),
    ("081899", "receiving", "verb", "/rɪˈsiːvɪŋ/", "nhận, tiếp nhận; tiếp đón; bắt bóng"),
    ("081900", "recense", "verb", "/rɪˈsɛns/", "hiệu đính chỉnh lý lại bản văn cổ"),
    ("081901", "recension", "noun", "/rɪˈsɛnʃən/", "bản hiệu đính; sự duyệt lại"),
    ("081902", "recentness", "noun", "/ˈriːsəntnəs/", "tính mới mẻ, thời gian mới gần đây"),
]

raw = json.load(open("scratch/b37_r04_raw_p4.json"))
by_id = {f"lex.en.200k.{r[0]}": r for r in records}
out = []
for orig in raw:
    sid, hw, pos, ipa, vi = by_id[orig["id"]]
    assert orig["hw"] == hw, f"{orig['id']}: {orig['hw']} vs {hw}"
    assert 0 < len(vi) <= 35, f"{sid} {hw} len={len(vi)}: {vi}"
    assert "/" not in vi, f"{sid} {hw} slash in vi"
    assert ipa.count("/") == 2 and not ipa.startswith("/ ") and not ipa.endswith(" /"), f"{sid} {hw} bad ipa"
    orig["pos"] = pos
    orig["ipa"] = ipa
    orig["vi"] = vi
    orig["status"] = "reviewed"
    out.append(orig)

assert len(out) == 100
with open("scratch/b37_r04_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r04_p4 saved OK")
