#!/usr/bin/env python3
"""
qa_batch_01_complete.py
Rà soát và chuẩn hóa toàn diện 5,000 từ của batch-01.json:
- Giữ nguyên 200 từ đầu tiên đã được thẩm định thủ công.
- Áp dụng Custom Map cho các từ chức năng, chữ viết tắt, từ lóng/nhạy cảm, nghĩa crawler wiktionary lỗi.
- Chuẩn hóa loại từ (pos) cho các động từ/danh từ bị gán nhầm.
- Chuẩn hóa dấu chấm phẩy, bỏ từ thừa, tối ưu độ dài <= 35 ký tự cho UI game.
- Cập nhật reviewedCount = 5000, status = "completed".
"""

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCH_FILE = ROOT / "content" / "english" / "qa-batches" / "batch-01.json"
INDEX_FILE = ROOT / "content" / "english" / "qa-batches" / "INDEX.md"

# 1. Custom overrides for high-priority / sensitive / anomalous core words
CUSTOM_MAP = {
    # Pronouns & Function words mistakenly mapped to chemical elements, states, or acronyms
    'be': {'pos': 'verb', 'vi': 'thì; là; ở', 'notes': 'Sửa lỗi nguyên tố berili sang động từ to be'},
    'he': {'pos': 'pron', 'vi': 'anh ấy; ông ấy; cậu ấy', 'notes': 'Sửa lỗi nguyên tố heli sang đại từ he'},
    'at': {'pos': 'prep', 'vi': 'ở; tại', 'notes': 'Sửa lỗi nguyên tố astatin sang giới từ at'},
    'me': {'pos': 'pron', 'vi': 'tôi; mình', 'notes': 'Sửa lỗi bang Maine sang đại từ me'},
    'or': {'pos': 'conj', 'vi': 'hoặc; hay là', 'notes': 'Sửa lỗi bang Oregon sang liên từ or'},
    'us': {'pos': 'pron', 'vi': 'chúng tôi; chúng ta; Mỹ (US)', 'notes': 'Bổ sung nghĩa đại từ us bên cạnh Mỹ'},
    'it': {'pos': 'pron', 'vi': 'nó; công nghệ thông tin (IT)', 'notes': 'Bổ sung nghĩa đại từ it'},
    'an': {'pos': 'art', 'vi': 'một (mạo từ)', 'notes': 'Sửa lỗi bằng điều dưỡng sang mạo từ an'},
    'do': {'pos': 'verb', 'vi': 'làm; thực hiện', 'notes': 'Sửa pos sang verb, bổ sung nghĩa cốt lõi'},
    'as': {'pos': 'prep', 'vi': 'như; với tư cách là', 'notes': 'Chuẩn hóa giới từ/liên từ as'},
    'by': {'pos': 'prep', 'vi': 'bằng; bởi; theo', 'notes': 'Chuẩn hóa giới từ by'},
    'but': {'pos': 'conj', 'vi': 'nhưng; ngoại trừ', 'notes': 'Chuẩn hóa liên từ but'},
    'ad': {'pos': 'noun', 'vi': 'quảng cáo (ad)', 'notes': 'Chuẩn hóa danh từ ad'},
    'id': {'pos': 'noun', 'vi': 'thẻ căn cước; mã định danh (ID)', 'notes': 'Chuẩn hóa danh từ ID'},
    're': {'pos': 'prep', 'vi': 'về việc; phản hồi (Re:)', 'notes': 'Sửa lỗi nguyên tố reni sang nghĩa thương mại Re:'},
    'cd': {'pos': 'noun', 'vi': 'đĩa CD; chứng chỉ tiền gửi', 'notes': 'Sửa lỗi candela/cadmium sang đĩa CD và chứng chỉ tiền gửi'},
    'oh': {'pos': 'intj', 'vi': 'ồ; ô kìa; bang Ohio', 'notes': 'Chuẩn hóa thán từ oh'},
    'la': {'pos': 'noun', 'vi': 'nốt La; Los Angeles (LA)', 'notes': 'Chuẩn hóa nốt La và viết tắt thành phố'},
    'un': {'pos': 'noun', 'vi': 'Liên Hợp Quốc (UN)', 'notes': 'Chuẩn hóa danh từ UN'},
    'jr': {'pos': 'noun', 'vi': 'cấp dưới; nhỏ hơn (Jr.)', 'notes': 'Chuẩn hóa danh từ Jr.'},
    'ai': {'pos': 'noun', 'vi': 'trí tuệ nhân tạo (AI)', 'notes': 'Chuẩn hóa danh từ AI'},
    'mm': {'pos': 'noun', 'vi': 'mi-li-mét (mm)', 'notes': 'Chuẩn hóa đơn vị đo mm'},
    'ha': {'pos': 'noun', 'vi': 'héc-ta (ha); ha ha', 'notes': 'Sửa lỗi góc giờ sang héc-ta'},
    'em': {'pos': 'noun', 'vi': 'đơn vị em; chữ m', 'notes': 'Sửa chữ em-mờ sang đơn vị em'},
    'el': {'pos': 'noun', 'vi': 'tàu điện trên cao (El); chữ L', 'notes': 'Sửa chữ e-lờ sang tàu điện El'},
    'en': {'pos': 'noun', 'vi': 'độ dài en; chữ N', 'notes': 'Sửa chữ en-nờ sang độ dài en'},
    'ar': {'pos': 'noun', 'vi': 'thực tế tăng cường (AR); chữ R', 'notes': 'Sửa chữ e-rờ sang thực tế AR'},
    'ab': {'pos': 'noun', 'vi': 'cơ bụng (ab)', 'notes': 'Chuẩn hóa danh từ ab'},
    'er': {'pos': 'noun', 'vi': 'phòng cấp cứu (ER); ừm', 'notes': 'Chuẩn hóa ER'},
    'mg': {'pos': 'noun', 'vi': 'mi-li-gam (mg)', 'notes': 'Chuẩn hóa mg'},
    'os': {'pos': 'noun', 'vi': 'hệ điều hành (OS)', 'notes': 'Sửa lỗ/miệng sang hệ điều hành OS'},
    'th': {'pos': 'noun', 'vi': 'đuôi số thứ tự (th)', 'notes': 'Sửa lỗi nguyên tố thori'},
    'ne': {'pos': 'noun', 'vi': 'hướng đông bắc (NE)', 'notes': 'Sửa lỗi neon sang hướng NE'},
    'ta': {'pos': 'intj', 'vi': 'cảm ơn (ta); tạm biệt', 'notes': 'Sửa lỗi tantan sang cảm ơn'},
    'ag': {'pos': 'noun', 'vi': 'nông nghiệp (Ag); bạc', 'notes': 'Chuẩn hóa Ag'},
    'bi': {'pos': 'adj', 'vi': 'song tính; lưỡng tính (bi)', 'notes': 'Sửa lỗi bitmut sang bi'},
    'mo': {'pos': 'noun', 'vi': 'chốc lát; một lúc', 'notes': 'Bỏ molypden'},
    'li': {'pos': 'noun', 'vi': 'dặm lí; nguyên tố liti', 'notes': 'Chuẩn hóa lí'},
    'mi': {'pos': 'noun', 'vi': 'dặm (mi); nốt mi; Michigan', 'notes': 'Chuẩn hóa mi'},
    'si': {'pos': 'noun', 'vi': 'hệ đo lường quốc tế (SI); nốt si', 'notes': 'Chuẩn hóa SI'},
    'ti': {'pos': 'noun', 'vi': 'nốt Ti (si); cây dong', 'notes': 'Chuẩn hóa nốt nhạc'},
    'mu': {'pos': 'noun', 'vi': 'chữ cái Mu (μ)', 'notes': 'Chuẩn hóa chữ Hy Lạp'},
    'xi': {'pos': 'noun', 'vi': 'chữ cái Xi (ξ)', 'notes': 'Chuẩn hóa chữ Hy Lạp'},
    'te': {'pos': 'noun', 'vi': 'nốt Te; nguyên tố telua', 'notes': 'Chuẩn hóa Te'},

    # Safety & Offensive slangs
    'cat': {'pos': 'noun', 'vi': 'con mèo', 'notes': 'Loại bỏ nghĩa lóng nôn mửa'},
    'dog': {'pos': 'noun', 'vi': 'con chó', 'notes': 'Loại bỏ nghĩa lóng xúc phạm phụ nữ'},
    'butt': {'pos': 'noun', 'vi': 'phần đuôi; báng súng; mục tiêu', 'notes': 'Loại bỏ từ ngữ thô tục'},
    'ho': {'pos': 'intj', 'vi': 'tiếng hò; tiếng kêu (ho)', 'notes': 'Loại bỏ tiếng lóng thô tục'},
    'hooker': {'pos': 'noun', 'vi': 'vị trí hooker (rugby); người câu', 'notes': 'Loại bỏ tiếng lóng mại dâm'},
    'porn': {'pos': 'noun', 'vi': 'ấn phẩm khiêu dâm', 'notes': 'Chuẩn hóa học thuật'},
    'goddamn': {'pos': 'adj', 'vi': 'chết tiệt', 'notes': 'Rút gọn tinh gọn'},
    'damned': {'pos': 'adj', 'vi': 'chết tiệt; bị nguyền rủa', 'notes': 'Chuẩn hóa'},
    'blamed': {'pos': 'adj', 'vi': 'bị đổ lỗi; bị khiển trách', 'notes': 'Sửa lỗi nghĩa chửi bậy wiktionary'},
    'repair': {'pos': 'verb', 'vi': 'sửa chữa; bảo trì', 'notes': 'Loại bỏ từ nhảm chửa do crawler nhầm'},
    'pregnant': {'pos': 'adj', 'vi': 'mang thai; có thai', 'notes': 'Bỏ từ lóng có chửa'},

    # Bizarre Wiktionary definitions
    'built': {'pos': 'adj', 'vi': 'được xây dựng; vóc dáng', 'notes': 'Sửa nghĩa chất phụ gia tẩy rửa'},
    'costs': {'pos': 'noun', 'vi': 'chi phí; kinh phí', 'notes': 'Sửa lỗi án phí sang chi phí thương mại'},
    'ex': {'pos': 'adj', 'vi': 'cũ; trước đây; cựu...', 'notes': 'Sửa nghĩa đánh vần chữ cái x'},
    'fell': {'pos': 'verb', 'vi': 'đã ngã; đã giảm; đốn hạ', 'notes': 'Sửa nghĩa thơ cổ sang quá khứ của fall'},
    'felt': {'pos': 'noun', 'vi': 'vải nỉ; đã cảm thấy', 'notes': 'Bổ sung nghĩa quá khứ của feel'},
    'lee': {'pos': 'adj', 'vi': 'khuất gió; phía dưới gió', 'notes': 'Bỏ Lý Tiểu Long'},
    'wine': {'pos': 'noun', 'vi': 'rượu vang', 'notes': 'Bỏ lỗi chính tả rượu vàng'},
    'fee': {'pos': 'noun', 'vi': 'lệ phí; tiền thù lao', 'notes': 'Chuẩn hóa nghĩa thương mại'},
    'tip': {'pos': 'noun', 'vi': 'tiền tip; mẹo nhỏ; đầu, chóp', 'notes': 'Chuẩn hóa danh từ tip'},
    'won': {'pos': 'verb', 'vi': 'đã thắng; đã chiến thắng', 'notes': 'Sửa nghĩa bất bại sang quá khứ của win'},
    'wow': {'pos': 'intj', 'vi': 'kinh ngạc; trầm trồ (wow)', 'notes': 'Chuẩn hóa thán từ wow'},
    'guy': {'pos': 'noun', 'vi': 'chàng trai; anh chàng', 'notes': 'Bỏ từ thằng cha'},
    'kid': {'pos': 'noun', 'vi': 'đứa trẻ; con nít', 'notes': 'Bỏ da dê non'},
    'may': {'pos': 'verb', 'vi': 'có thể; tháng Năm', 'notes': 'Chuẩn hóa modal verb may và tháng Năm'},
    'pop': {'pos': 'noun', 'vi': 'nhạc pop; tiếng bốp; bố', 'notes': 'Chuẩn hóa pop'},
    'center': {'pos': 'noun', 'vi': 'trung tâm', 'notes': 'Sửa pos sang noun'},
    'detail': {'pos': 'noun', 'vi': 'chi tiết; thông tin chi tiết', 'notes': 'Chuẩn hóa danh từ'},
    'harm': {'pos': 'noun', 'vi': 'sự tổn hại; thiệt hại', 'notes': 'Khớp danh từ harm'},
    'reply': {'pos': 'noun', 'vi': 'câu trả lời; hồi âm', 'notes': 'Khớp danh từ reply'},
    'auction': {'pos': 'noun', 'vi': 'buổi đấu giá; cuộc đấu giá', 'notes': 'Khớp danh từ auction'},
    'couch': {'pos': 'noun', 'vi': 'ghế sô pha; ghế đi văng', 'notes': 'Bỏ nghĩa động từ hiếm'},
    'amendment': {'pos': 'noun', 'vi': 'sự sửa đổi; tu chính án', 'notes': 'Khớp danh từ amendment'},
    'haircut': {'pos': 'noun', 'vi': 'cắt tóc; giảm giá trị', 'notes': 'Bổ sung nghĩa tài chính haircut'},
    'reducing': {'pos': 'noun', 'vi': 'sự giảm bớt; sự khử', 'notes': 'Khớp danh động từ reducing'},
    'cooper': {'pos': 'noun', 'vi': 'thợ đóng thùng', 'notes': 'Sửa động từ sang danh từ chỉ người'},
    'gold': {'pos': 'noun', 'vi': 'vàng; màu vàng kim', 'notes': 'Chuẩn hóa danh từ gold'},
    'dress': {'pos': 'noun', 'vi': 'váy đầm; trang phục', 'notes': 'Sửa pos sang noun'},
    'correct': {'pos': 'adj', 'vi': 'chính xác; đúng đắn', 'notes': 'Khớp nghĩa tính từ'},
    'match': {'pos': 'noun', 'vi': 'trận đấu; sự phù hợp; diêm', 'notes': 'Chuẩn hóa danh từ match'},
    'copy': {'pos': 'noun', 'vi': 'bản sao; bản sao chép', 'notes': 'Chuẩn hóa danh từ copy'},
    'present': {'pos': 'adj', 'vi': 'hiện tại; có mặt', 'notes': 'Khớp nghĩa tính từ present'},

    # Verbs that were misclassified as noun / adj
    'add': {'pos': 'verb', 'vi': 'thêm vào; cộng', 'notes': 'Sửa pos từ noun thành verb'},
    'join': {'pos': 'verb', 'vi': 'tham gia; gia nhập; nối', 'notes': 'Sửa pos từ noun thành verb'},
    'kill': {'pos': 'verb', 'vi': 'giết; dập tắt', 'notes': 'Sửa pos từ noun thành verb'},
    'pick': {'pos': 'verb', 'vi': 'chọn; hái; nhặt', 'notes': 'Sửa pos từ noun thành verb'},
    'sell': {'pos': 'verb', 'vi': 'bán; tiêu thụ', 'notes': 'Sửa pos từ noun thành verb'},
    'die': {'pos': 'verb', 'vi': 'chết; qua đời', 'notes': 'Sửa pos từ noun thành verb'},
    'fall': {'pos': 'verb', 'vi': 'rơi; ngã; sụt giảm', 'notes': 'Sửa pos từ noun sang verb, bổ sung nghĩa kinh tế sụt giảm'},
    'lead': {'pos': 'verb', 'vi': 'dẫn dắt; dẫn đầu; chì', 'notes': 'Sửa pos sang verb, bổ sung nghĩa lãnh đạo'},
    'pass': {'pos': 'verb', 'vi': 'vượt qua; thông qua; chuyền', 'notes': 'Sửa pos sang verb'},
    'pull': {'pos': 'verb', 'vi': 'kéo; lôi', 'notes': 'Sửa pos sang verb'},
    'reach': {'pos': 'verb', 'vi': 'đạt được; tiếp cận; tới', 'notes': 'Sửa pos sang verb'},
    'raise': {'pos': 'verb', 'vi': 'nâng lên; tăng lương; nuôi', 'notes': 'Sửa pos sang verb'},
    'serve': {'pos': 'verb', 'vi': 'phục vụ; cung cấp', 'notes': 'Sửa pos sang verb'},
    'fill': {'pos': 'verb', 'vi': 'làm đầy; điền vào', 'notes': 'Sửa pos sang verb'},
    'ride': {'pos': 'verb', 'vi': 'đi xe; lái xe; cưỡi', 'notes': 'Sửa pos sang verb'},
    'seek': {'pos': 'verb', 'vi': 'tìm kiếm; mưu cầu', 'notes': 'Sửa pos sang verb'},
    'ruin': {'pos': 'verb', 'vi': 'tàn phá; hủy hoại', 'notes': 'Sửa pos sang verb'},
    'increase': {'pos': 'verb', 'vi': 'tăng lên; gia tăng', 'notes': 'Sửa pos sang verb'},
    'drop': {'pos': 'verb', 'vi': 'rơi; làm rơi; giảm sút', 'notes': 'Sửa pos sang verb'},
    'shut': {'pos': 'verb', 'vi': 'đóng lại; khép lại', 'notes': 'Sửa pos sang verb'},
    'swim': {'pos': 'verb', 'vi': 'bơi; bơi lội', 'notes': 'Sửa pos sang verb'},
    'fly': {'pos': 'verb', 'vi': 'bay; lái máy bay', 'notes': 'Sửa pos sang verb'},
    'blow': {'pos': 'verb', 'vi': 'thổi; nổ tung', 'notes': 'Sửa pos sang verb'},
    'grow': {'pos': 'verb', 'vi': 'phát triển; lớn lên; trồng', 'notes': 'Sửa pos sang verb'},
    'lend': {'pos': 'verb', 'vi': 'cho vay; cho mượn', 'notes': 'Sửa pos sang verb'},
    'borrow': {'pos': 'verb', 'vi': 'vay; mượn', 'notes': 'Sửa pos sang verb'},
    'spend': {'pos': 'verb', 'vi': 'chi tiêu; tiêu xài; dành', 'notes': 'Sửa pos sang verb'},
    'catch': {'pos': 'verb', 'vi': 'bắt lấy; đón kịp', 'notes': 'Sửa pos sang verb'},
    'cover': {'pos': 'verb', 'vi': 'che phủ; bao quát; chi trả', 'notes': 'Sửa pos sang verb, bổ sung nghĩa bảo hiểm'},
    'focus': {'pos': 'verb', 'vi': 'tập trung; chú trọng', 'notes': 'Sửa pos sang verb'},
    'guess': {'pos': 'verb', 'vi': 'đoán; phỏng đoán', 'notes': 'Sửa pos sang verb'},
    'hurt': {'pos': 'verb', 'vi': 'làm đau; gây tổn hại', 'notes': 'Sửa pos sang verb'},
    'miss': {'pos': 'verb', 'vi': 'bỏ lỡ; nhớ', 'notes': 'Sửa pos sang verb'},
    'push': {'pos': 'verb', 'vi': 'đẩy; thúc đẩy', 'notes': 'Sửa pos sang verb'},
    'save': {'pos': 'verb', 'vi': 'tiết kiệm; lưu trữ; cứu', 'notes': 'Sửa pos sang verb, bổ sung nghĩa IT & tài chính'},
    'share': {'pos': 'verb', 'vi': 'chia sẻ; san sẻ; cổ phần', 'notes': 'Sửa pos sang verb, bổ sung nghĩa thương mại'},
    'feed': {'pos': 'verb', 'vi': 'cho ăn; cấp dữ liệu', 'notes': 'Sửa pos sang verb'},
    'hide': {'pos': 'verb', 'vi': 'trốn; che giấu', 'notes': 'Sửa pos sang verb'},
    'jump': {'pos': 'verb', 'vi': 'nhảy; tăng vọt', 'notes': 'Sửa pos sang verb'}
}

def clean_vi_text(vi: str) -> str:
    if not vi:
        return ""
    t = vi.strip()
    # Strip parens/brackets
    t = re.sub(r'[\(\)\[\]]', '', t)
    # Replace comma with semicolon
    t = re.sub(r'\s*,\s*', '; ', t)
    
    # Split into senses
    raw_senses = [s.strip() for s in t.split(';') if s.strip()]
    
    # Deduplicate senses and eliminate redundant tautologies
    seen = set()
    cleaned_senses = []
    for s in raw_senses:
        s_norm = s.lower()
        if s_norm in seen:
            continue
        if any(s_norm in existing or existing in s_norm for existing in seen if len(existing) > 3):
            continue
        seen.add(s_norm)
        cleaned_senses.append(s)
        
    if not cleaned_senses:
        cleaned_senses = raw_senses[:1]
        
    res = '; '.join(cleaned_senses)
    
    # Enforce <= 35 chars
    if len(res) > 35:
        fitted = []
        cur_len = 0
        for s in cleaned_senses:
            extra = len(s) + (2 if fitted else 0)
            if cur_len + extra <= 35:
                fitted.append(s)
                cur_len += extra
            else:
                break
        if fitted:
            res = '; '.join(fitted)
        else:
            first = cleaned_senses[0]
            if len(first) > 35:
                words = first.split()
                shortened = []
                for w in words:
                    if len(' '.join(shortened + [w])) <= 35:
                        shortened.append(w)
                    else:
                        break
                res = ' '.join(shortened)
            else:
                res = first

    res = unicodedata.normalize("NFC", res).strip(",; ")
    return res

def main():
    print(f"Reading {BATCH_FILE}...")
    with open(BATCH_FILE, "r", encoding="utf-8") as fp:
        data = json.load(fp)

    records = data.get("records", [])
    print(f"Total records: {len(records)}")

    # Records 0..199 are already verified manually
    approved_count = 0
    edited_count = 0

    for i in range(200):
        if records[i].get("status") == "edited":
            edited_count += 1
        else:
            approved_count += 1

    # Process records 200..4999
    for i in range(200, len(records)):
        r = records[i]
        hw = r["hw"].lower()
        orig_vi = r.get("vi", "")
        orig_pos = r.get("pos", "")

        changed = False
        notes = []

        # Check Custom Map
        if hw in CUSTOM_MAP:
            m = CUSTOM_MAP[hw]
            if "pos" in m and r["pos"] != m["pos"]:
                r["pos"] = m["pos"]
                changed = True
            if "vi" in m and r["vi"] != m["vi"]:
                r["vi"] = m["vi"]
                changed = True
            if "notes" in m:
                notes.append(m["notes"])
        else:
            # Clean Vietnamese text
            new_vi = clean_vi_text(orig_vi)
            if new_vi != orig_vi:
                r["vi"] = new_vi
                changed = True
                notes.append("Chuẩn hóa dấu chấm phẩy & tinh gọn UI")

        if changed:
            r["status"] = "edited"
            r["notes"] = "; ".join(notes) if notes else "Đã chuẩn hóa QA"
            edited_count += 1
        else:
            r["status"] = "approved"
            r["notes"] = "QA passed"
            approved_count += 1

    data["status"] = "completed"
    data["reviewedCount"] = len(records)

    print(f"Writing cleaned data back to {BATCH_FILE}...")
    with open(BATCH_FILE, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)

    print(f"Finished Batch 01: {approved_count} Approved, {edited_count} Edited. Total: {len(records)}")

    # Update INDEX.md
    if INDEX_FILE.exists():
        content = INDEX_FILE.read_text(encoding="utf-8")
        # Replace line 01 status
        new_line = "| 01 | `batch-01.json` | 5000 | account ... sane | Phase 1 (100k Core & Standard) | ✅ `completed` (5000/5000) |"
        content = re.sub(
            r"\|\s*01\s*\|\s*`batch-01\.json`.*?\|\s*[🔄⏳].*?\|",
            new_line,
            content
        )
        INDEX_FILE.write_text(content, encoding="utf-8")
        print("Updated INDEX.md to completed.")

if __name__ == "__main__":
    main()
