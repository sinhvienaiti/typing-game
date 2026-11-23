# Cấu Trúc Dữ Liệu File Chủ Đề (`topics/<topic-id>.json`)

Mỗi file trong thư mục `content/english/topics-curated/topics/<topic-id>.json` đại diện cho một chủ đề từ vựng chuyên sâu và tích hợp đầy đủ câu ví dụ, âm vị học, cùng các đoạn văn luyện tập gõ & phát âm.

## 1. Cấu Trúc Tổng Thể

```json
{
  "topicId": "food.fruits",
  "group": "food-drink",
  "label": "Fruits",
  "labelVi": "Hoa quả & Trái cây",
  "descriptionVi": "Từ vựng về các loại hoa quả tươi, hương vị, cách thưởng thức và chọn mua trái cây.",
  "words": [
    {
      "lexemeId": "lex.en.100k.000123",
      "headword": "apple",
      "pos": "noun",
      "cefr": "A1",
      "ipaUs": "/ˈæp.əl/",
      "syllables": ["ap", "ple"],
      "stressedIndex": 0,
      "vi": "quả táo",
      "senseNote": "Trái cây tròn, vỏ đỏ/xanh, ăn giòn ngọt",
      "priority": "core",
      "examples": [
        {
          "en": "She eats a fresh red apple every morning.",
          "vi": "Cô ấy ăn một quả táo đỏ tươi mỗi sáng.",
          "ipaUs": "/ʃiː iːts ə freʃ red ˈæp.əl ˈev.ri ˈmɔːr.nɪŋ/",
          "stressWords": ["eats", "fresh", "red", "apple", "every", "morning"]
        }
      ]
    }
  ],
  "passages": [
    {
      "passageId": "PASSAGE_food.fruits_A1_01",
      "title": "A Morning at the Fresh Fruit Stall",
      "cefr": "A1",
      "wordCount": 268,
      "targetLexemeIds": [
        "lex.en.100k.000123"
      ],
      "text": "Morning begins early at the local open-air market...",
      "sentencePairs": [
        {
          "en": "Morning begins early at the local open-air market.",
          "vi": "Buổi sáng bắt đầu sớm tại khu chợ trời địa phương."
        }
      ],
      "pronunciationNotesVi": "Chú ý phát âm rõ âm chặn /p/ trong apple và âm đuôi /ts/ trong eats.",
      "comprehensionQuestions": [
        {
          "question": "What does the family buy first at the market?",
          "options": [
            "A basket of fresh apples",
            "A cup of cold milk",
            "A bag of rice",
            "A new hat"
          ],
          "answer": "A basket of fresh apples",
          "explanationVi": "Đoạn văn nêu rõ gia đình chọn mua một rổ táo tươi ngay khi bước vào sạp hoa quả."
        }
      ]
    }
  ]
}
```

## 2. Chi Tiết Các Trường Trong `words[]`
- `lexemeId`: Mã định danh thống nhất kế thừa từ kho gốc `lex.en.100k.xxxxxx` trong `qa-batches/`.
- `headword`: Từ tiếng Anh nguyên mẫu.
- `pos`: Từ loại chuẩn (`noun`, `verb`, `adj`, `adv`, `prep`, `phrase`...).
- `cefr`: Cấp độ khung tham chiếu Châu Âu (`A1`, `A2`, `B1`, `B2`).
- `ipaUs`: Phiên âm quốc tế chuẩn giọng Mỹ (US IPA) với dấu trọng âm `ˈ` chuẩn xác.
- `syllables`: Mảng phân tách các âm tiết để hỗ trợ luyện phát âm ngắt nhịp.
- `stressedIndex`: Vị trí chỉ mục (bắt đầu từ 0) của âm tiết mang trọng âm chính.
- `vi`: Nghĩa tiếng Việt cô đọng, tự nhiên và chính xác.
- `senseNote`: Ghi chú làm rõ nét nghĩa của từ trong ngữ cảnh chủ đề này (đặc biệt quan trọng với từ đa nghĩa).
- `priority`: `core` (từ trọng tâm, tần suất dùng cao) hoặc `support` (từ mở rộng, bổ trợ).
- `examples`: 1–2 câu áp dụng tự nhiên song ngữ `en`, `vi`, kèm `ipaUs` câu và `stressWords[]` các từ mang trọng âm ý nghĩa.

## 3. Chi Tiết Các Trường Trong `passages[]`
- `passageId`: Mã định danh đoạn văn theo mẫu `PASSAGE_<topic-id>_<cefr>_<số thứ tự>`.
- `title`: Tiêu đề bài đọc tiếng Anh.
- `cefr`: Cấp độ bài đọc, đồng nhất với các từ mục tiêu được gom cụm.
- `wordCount`: Số lượng từ thực tế của bài (chuẩn hóa trong khoảng ~250–350 từ).
- `targetLexemeIds`: Danh sách 10–15 `lexemeId` được lồng ghép mượt mà trong đoạn văn.
- `text`: Toàn văn đoạn văn chuẩn ngữ pháp, câu chuyện mạch lạc, phù hợp luyện gõ typing.
- `sentencePairs`: Mảng tách từng câu song ngữ Anh - Việt đối sánh trực quan.
- `pronunciationNotesVi`: Mẹo phát âm, nối âm hoặc lưu ý ngữ điệu tiếng Việt.
- `comprehensionQuestions`: 3–5 câu hỏi trắc nghiệm kiểm tra độ hiểu bài kèm đáp án và giải thích tiếng Việt.
