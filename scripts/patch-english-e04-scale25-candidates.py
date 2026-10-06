#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts/apply-english-e04-focused-scale-25.py"

REPLACEMENTS = {
    '("exercise discretion", "verb + noun", "vận dụng quyền cân nhắc để đưa ra quyết định phù hợp theo hoàn cảnh", "C1")':
        '("articulate a position", "verb + noun", "trình bày rõ ràng quan điểm hoặc lập trường về một vấn đề", "C1")',
    '("exercise caution", "verb + noun", "hành động thận trọng để hạn chế rủi ro hoặc sai sót", "B2")':
        '("clarify expectations", "verb + noun", "làm rõ những điều được mong đợi về kết quả, trách nhiệm hoặc hành vi", "B2")',
    '("pose a threat", "verb + noun", "tạo ra mối đe dọa hoặc nguy cơ đáng kể", "B2")':
        '("define parameters", "verb + noun", "xác định các giới hạn hoặc điều kiện chính của một kế hoạch hay quá trình", "C1")',
    '("raise objections", "verb + noun", "nêu ra những phản đối đối với một đề xuất hoặc quyết định", "B2")':
        '("delineate responsibilities", "verb + noun", "phân định rõ trách nhiệm giữa các cá nhân hoặc đơn vị", "C1")',
    '("reach consensus", "verb + noun", "đạt được sự đồng thuận giữa các bên", "B2")':
        '("coordinate efforts", "verb + noun", "phối hợp các nỗ lực của nhiều bên để đạt một mục tiêu chung", "B2")',
    '("draw a distinction", "verb + noun", "chỉ ra sự khác biệt rõ ràng giữa hai khái niệm hoặc trường hợp", "C1")':
        '("pool expertise", "verb + noun", "kết hợp chuyên môn của nhiều người hoặc tổ chức để xử lý một nhiệm vụ", "C1")',
    '("secure funding", "verb + noun", "đảm bảo có được nguồn kinh phí cần thiết", "B2")':
        '("prioritize investment", "verb + noun", "ưu tiên nguồn đầu tư cho những lĩnh vực hoặc mục tiêu quan trọng hơn", "C1")',
    '("mitigate risk", "verb + noun", "giảm mức độ hoặc tác động của rủi ro", "B2")':
        '("reduce exposure", "verb + noun", "giảm mức độ tiếp xúc hoặc phụ thuộc vào một nguồn rủi ro", "C1")',
    '("impose restrictions", "verb + noun", "áp đặt các hạn chế đối với hoạt động hoặc hành vi", "B2")':
        '("reinforce safeguards", "verb + noun", "tăng cường các biện pháp bảo vệ nhằm ngăn ngừa rủi ro hoặc sai phạm", "C1")',
}

text = TARGET.read_text(encoding="utf-8")
changed = []
for old, new in REPLACEMENTS.items():
    if old in text:
        if text.count(old) != 1:
            raise RuntimeError(f"replacement source is not unique: {old}")
        text = text.replace(old, new, 1)
        changed.append(new.split('"', 2)[1])
    elif new not in text:
        raise RuntimeError(f"neither old nor replacement candidate exists: {old}")

TARGET.write_text(text, encoding="utf-8")
print({"patched": changed, "count": len(changed)})
