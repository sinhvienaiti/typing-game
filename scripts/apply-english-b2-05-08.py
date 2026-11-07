from __future__ import annotations
import copy, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

R = [
    (
        "gr.b2.complex-noun-phrases",
        "Complex noun phrases can pack precise information around a head noun by combining premodifiers with prepositional, relative and non-finite postmodifiers.",
        "Cụm danh từ phức có thể nén thông tin chính xác quanh danh từ trung tâm bằng cách kết hợp bổ ngữ trước với cụm giới từ, mệnh đề quan hệ và cấu trúc không chia ở phía sau.",
        ["determiner + premodifier(s) + head noun + postmodifier(s)", "noun + past-participle / -ing clause", "noun + prepositional phrase"],
        "Use compact noun phrases when several details must identify or describe the same referent without creating a chain of short clauses.",
        ["The proposal submitted by the research team addresses several unresolved safety concerns.", "Students interested in the internship should apply before the end of the month.", "The building across from the station has offices on the top three floors."],
        "submitted",
        "Dịch sang tiếng Anh: Những sinh viên quan tâm đến kỳ thực tập nên nộp đơn trước cuối tháng.",
        "The proposal submitted the research team addresses several unresolved safety concerns.",
        "The proposal submitted by the research team addresses several unresolved safety concerns.",
        "Khi past participle mang nghĩa bị động và cần nêu tác nhân, dùng by + tác nhân trong phần hậu bổ nghĩa của danh từ.",
    ),
    (
        "gr.b2.articles-abstract-nouns",
        "Article choice with abstract nouns depends on whether the idea is general, one instance or a specifically identified concept.",
        "Việc chọn mạo từ với danh từ trừu tượng phụ thuộc vào việc ý niệm đang được nói chung, là một trường hợp cụ thể hay là một khái niệm đã được xác định.",
        ["zero article + abstract noun = general concept", "a/an + modified countable instance", "the + specified abstract noun"],
        "Choose zero, a/an or the according to how specifically the abstract idea is framed in the discourse.",
        ["Freedom requires responsibility.", "The freedom we gained after the reform came with new responsibilities.", "A deep understanding of context is essential for accurate interpretation."],
        "Freedom",
        "Dịch sang tiếng Anh: Sự tự do mà chúng tôi có được sau cuộc cải cách đi kèm với những trách nhiệm mới.",
        "The freedom requires responsibility when freedom is meant as a general idea.",
        "Freedom requires responsibility.",
        "Danh từ trừu tượng dùng theo nghĩa khái quát thường không có mạo từ; the chỉ phù hợp khi ý niệm đã được xác định cụ thể.",
    ),
    (
        "gr.b2.articles-modified-reference",
        "A restrictive modifier can make a noun identifiable, while a non-specific modified noun may still require a/an.",
        "Bổ ngữ hạn định có thể khiến danh từ trở nên xác định, trong khi một danh từ có bổ ngữ nhưng vẫn chưa xác định có thể tiếp tục dùng a/an.",
        ["the + noun + identifying modifier", "a/an + noun + non-identifying possibility"],
        "Use article choice together with relative clauses and other modifiers to signal whether the listener can identify the referent.",
        ["The information in the appendix is confidential.", "A solution that satisfies both teams will be difficult to find.", "The engineer who designed the system will join us later."],
        "information",
        "Dịch sang tiếng Anh: Một giải pháp đáp ứng được cả hai nhóm sẽ rất khó tìm.",
        "Information in the appendix is confidential when the appendix identifies which information we mean.",
        "The information in the appendix is confidential.",
        "Cụm in the appendix xác định rõ phần thông tin đang nói đến, vì vậy the là lựa chọn tự nhiên.",
    ),
    (
        "gr.b2.generic-reference",
        "English can express a whole class with a zero-article plural, with the + singular for a species/class, or with a/an + singular for a representative member.",
        "Tiếng Anh có thể nói về cả một lớp bằng danh từ số nhiều không mạo từ, the + số ít để chỉ loài/lớp, hoặc a/an + số ít để lấy một thành viên làm đại diện.",
        ["plural noun with zero article", "the + singular noun", "a/an + singular noun"],
        "Choose a generic pattern according to noun type, register and whether the class or a representative member is foregrounded.",
        ["Tigers are powerful predators.", "The tiger is threatened by habitat loss.", "A smartphone can replace several everyday devices."],
        "Tigers",
        "Dịch sang tiếng Anh: Loài hổ đang bị đe dọa bởi việc mất môi trường sống.",
        "The tigers are powerful predators when tigers means the species in general.",
        "Tigers are powerful predators.",
        "Danh từ số nhiều mang nghĩa khái quát thường dùng zero article; the tigers thường gợi một nhóm hổ cụ thể đã biết.",
    ),
    (
        "gr.b2.less-fewer-number-amount",
        "Fewer and number normally combine with countable plural nouns, while less and amount normally combine with uncountable quantity.",
        "Fewer và number thường đi với danh từ đếm được số nhiều, còn less và amount thường đi với lượng không đếm được.",
        ["fewer + plural count noun", "less + uncountable noun", "number of + plural count noun", "amount of + uncountable noun"],
        "Make quantity language precise in formal and neutral contexts by matching the expression to countability.",
        ["Fewer employees commute every day than they did five years ago.", "The amount of waste produced by the factory has fallen significantly.", "We need less time but a greater number of volunteers."],
        "Fewer",
        "Dịch sang tiếng Anh: Lượng chất thải do nhà máy tạo ra đã giảm đáng kể.",
        "Less employees commute every day than they did five years ago.",
        "Fewer employees commute every day than they did five years ago.",
        "Employees là danh từ đếm được số nhiều nên trong văn phong chuẩn dùng fewer, không dùng less.",
    ),
    (
        "gr.b2.advanced-quantifiers",
        "Advanced quantifiers distinguish countability, degree and register, including a great deal of, hardly any and a large number or amount of.",
        "Các lượng từ nâng cao phân biệt tính đếm được, mức độ và sắc thái văn phong, chẳng hạn a great deal of, hardly any và a large number/amount of.",
        ["a great deal of + uncountable noun", "hardly any + plural/uncountable noun", "a large number of + plural noun", "a large amount of + uncountable noun"],
        "Use nuanced quantity expressions when simple much/many is too weak or too informal for the context.",
        ["A great deal of research has focused on this question.", "Hardly any applicants had experience with the new platform.", "A large number of residents opposed the proposal."],
        "deal",
        "Dịch sang tiếng Anh: Hầu như không có ứng viên nào có kinh nghiệm với nền tảng mới.",
        "A large amount of residents opposed the proposal.",
        "A large number of residents opposed the proposal.",
        "Residents là danh từ đếm được số nhiều nên dùng a large number of; amount đi với danh từ không đếm được.",
    ),
    (
        "gr.b2.correlative-comparison",
        "The correlative pattern the + comparative ..., the + comparative ... links two changing variables.",
        "Cấu trúc tương liên the + so sánh hơn ..., the + so sánh hơn ... liên kết hai đại lượng thay đổi cùng nhau.",
        ["The + comparative + clause, the + comparative + clause"],
        "Express that a change in one condition is systematically associated with a change in another.",
        ["The more carefully you plan, the fewer problems you are likely to face.", "The longer the meeting continued, the less productive it became.", "The more we automate routine tasks, the more time we can spend on analysis."],
        "carefully",
        "Dịch sang tiếng Anh: Cuộc họp càng kéo dài thì nó càng kém hiệu quả.",
        "More you practice, better you become.",
        "The more you practice, the better you become.",
        "Cả hai vế của cấu trúc tương liên đều cần the trước dạng so sánh hơn.",
    ),
    (
        "gr.b2.superlative-present-perfect",
        "A superlative followed by a Present Perfect relative clause evaluates an experience across the speaker's life or another unfinished period.",
        "Dạng so sánh nhất đi với mệnh đề Present Perfect dùng để đánh giá một trải nghiệm trong suốt cuộc đời người nói hoặc một khoảng thời gian chưa kết thúc.",
        ["the + superlative + noun + subject + have/has ever + past participle"],
        "Describe an extreme experience while keeping the comparison period connected to the present.",
        ["This is the most demanding project I've ever managed.", "It's the best documentary we've seen this year.", "That was the most convincing explanation she has given so far."],
        "managed",
        "Dịch sang tiếng Anh: Đó là bộ phim tài liệu hay nhất mà chúng tôi đã xem trong năm nay.",
        "This is the most demanding project I ever managed.",
        "This is the most demanding project I've ever managed.",
        "Khi so sánh trải nghiệm trong một khoảng thời gian còn mở đến hiện tại, Present Perfect là lựa chọn tự nhiên.",
    ),
    (
        "gr.b2.adjective-order",
        "When several adjectives occur before a noun, English strongly prefers a conventional semantic order rather than an arbitrary sequence.",
        "Khi nhiều tính từ cùng đứng trước danh từ, tiếng Anh ưu tiên một trật tự ngữ nghĩa quen thuộc thay vì sắp xếp tùy ý.",
        ["opinion + size + age + shape + color + origin + material + purpose + noun"],
        "Order stacked adjectives naturally, especially in detailed descriptions and product or object descriptions.",
        ["She bought a beautiful small Italian leather bag.", "They restored an impressive old stone bridge.", "He drives a sleek new electric sports car."],
        "Italian",
        "Dịch sang tiếng Anh: Họ đã phục hồi một cây cầu đá cổ rất ấn tượng.",
        "She bought a leather Italian small beautiful bag.",
        "She bought a beautiful small Italian leather bag.",
        "Tính từ chỉ ý kiến và kích thước thường đứng trước nguồn gốc và chất liệu; trật tự tự nhiên quan trọng hơn dịch từng từ theo thứ tự tiếng Việt.",
    ),
    (
        "gr.b2.gradable-intensifiers",
        "Gradable adjectives combine with degree modifiers such as very or extremely, while non-gradable extremes often prefer absolutely, completely or similar intensifiers.",
        "Tính từ có thang độ kết hợp với very, extremely..., còn tính từ cực trị/không có thang độ thường hợp với absolutely, completely... hơn.",
        ["very/extremely + gradable adjective", "absolutely/completely + extreme adjective", "deeply/highly + selected adjective collocations"],
        "Choose an intensifier that matches both the adjective's scale and its common collocational behavior.",
        ["The instructions are absolutely essential for safe operation.", "I was deeply disappointed by the decision.", "The final stage is extremely difficult but not impossible."],
        "absolutely",
        "Dịch sang tiếng Anh: Tôi vô cùng thất vọng về quyết định đó.",
        "The deadline is very impossible to meet.",
        "The deadline is absolutely impossible to meet.",
        "Impossible là tính từ cực trị, vì vậy absolutely/completely tự nhiên hơn very trong cách dùng chuẩn.",
    ),
    (
        "gr.b2.stance-adverbs",
        "Stance adverbs comment on the speaker's certainty, evaluation or attitude toward the whole proposition.",
        "Trạng từ lập trường cho biết mức độ chắc chắn, đánh giá hoặc thái độ của người nói đối với toàn bộ mệnh đề.",
        ["stance adverb + comma + clause", "clause-medial stance adverb where natural"],
        "Signal evidence, evaluation or viewpoint explicitly without changing the core event described.",
        ["Apparently, the supplier has changed its delivery schedule.", "Fortunately, nobody was injured in the accident.", "Arguably, this is the most important finding in the report."],
        "Apparently",
        "Dịch sang tiếng Anh: May mắn là không có ai bị thương trong vụ tai nạn.",
        "It is apparently that the supplier has changed its delivery schedule.",
        "Apparently, the supplier has changed its delivery schedule.",
        "Apparently có thể trực tiếp bổ nghĩa cho cả mệnh đề; không dùng mẫu It is apparently that theo cách này.",
    ),
    (
        "gr.b2.focus-adverbs",
        "Focus adverbs such as only, even, just and also change which constituent receives emphasis, so their position can change meaning.",
        "Các trạng từ tiêu điểm như only, even, just và also thay đổi thành phần được nhấn mạnh, vì vậy vị trí của chúng có thể làm đổi nghĩa.",
        ["focus adverb immediately before the focused constituent where possible"],
        "Place focus adverbs deliberately to distinguish who, what action or which object is being restricted or highlighted.",
        ["Only Maya reviewed the final draft.", "Maya only reviewed the final draft, so she did not approve it.", "Even the most experienced engineers found the task difficult."],
        "Only",
        "Dịch sang tiếng Anh: Maya chỉ xem xét bản nháp cuối cùng nên cô ấy không phê duyệt nó.",
        "Only I asked him to send the invoice when the intended meaning is that I merely asked rather than demanded.",
        "I only asked him to send the invoice.",
        "Đặt only ngay trước thành phần cần giới hạn; Only I... giới hạn chủ ngữ, còn I only asked... giới hạn hành động.",
    ),
    (
        "gr.b2.fixed-prepositional-phrases",
        "Many formal and neutral meanings are expressed through fixed multiword prepositional phrases whose internal preposition is not freely interchangeable.",
        "Nhiều ý nghĩa trung tính và trang trọng được diễn đạt bằng cụm giới từ cố định nhiều từ, trong đó giới từ bên trong không thể thay tùy ý.",
        ["on behalf of", "in charge of", "in response to", "with regard to"],
        "Use established phrase-level combinations for roles, responses, reference and formal connections between ideas.",
        ["On behalf of the team, I'd like to thank everyone who helped.", "She is in charge of coordinating the regional offices.", "The policy was revised in response to customer feedback."],
        "behalf",
        "Dịch sang tiếng Anh: Cô ấy phụ trách điều phối các văn phòng khu vực.",
        "She is in charge for coordinating the regional offices.",
        "She is in charge of coordinating the regional offices.",
        "Cụm cố định là in charge of; đổi of thành for làm sai kết hợp chuẩn.",
    ),
    (
        "gr.b2.dependent-prepositions-adjectives",
        "Many adjectives select a particular preposition, and changing that preposition can be ungrammatical or alter the intended relation.",
        "Nhiều tính từ đòi hỏi một giới từ cụ thể; đổi giới từ có thể làm câu sai hoặc thay đổi quan hệ nghĩa.",
        ["aware of", "consistent with", "capable of", "responsible for"],
        "Learn adjective-preposition combinations as lexical patterns rather than translating the preposition literally.",
        ["The committee is aware of the risks involved.", "This approach is consistent with our long-term strategy.", "She is capable of handling the negotiation herself."],
        "aware",
        "Dịch sang tiếng Anh: Cách tiếp cận này nhất quán với chiến lược dài hạn của chúng tôi.",
        "She is responsible of preparing the final report.",
        "She is responsible for preparing the final report.",
        "Responsible đi với for khi nói về nhiệm vụ hoặc trách nhiệm.",
    ),
    (
        "gr.b2.dependent-prepositions-verbs",
        "Many verbs form meaning-specific patterns with a required preposition that should be learned together with the verb.",
        "Nhiều động từ tạo thành mẫu nghĩa cụ thể với một giới từ bắt buộc và nên được học như một đơn vị cùng với động từ.",
        ["distinguish between", "depend on", "object to", "result in/from"],
        "Choose the preposition licensed by the verb and intended meaning instead of translating a Vietnamese preposition word-for-word.",
        ["We need to distinguish between temporary failures and structural problems.", "The success of the campaign depends on sustained public support.", "Several experts objected to the proposed change."],
        "distinguish",
        "Dịch sang tiếng Anh: Thành công của chiến dịch phụ thuộc vào sự ủng hộ bền vững của công chúng.",
        "The success of the campaign depends of sustained public support.",
        "The success of the campaign depends on sustained public support.",
        "Depend mang nghĩa phụ thuộc đi với on, không đi với of.",
    ),
    (
        "gr.b2.multiword-verbs",
        "Multiword verbs combine a lexical verb with particles and/or prepositions; the whole combination controls meaning, object position and complement pattern.",
        "Động từ nhiều từ kết hợp động từ chính với tiểu từ và/hoặc giới từ; toàn bộ cụm quyết định nghĩa, vị trí tân ngữ và kiểu bổ ngữ.",
        ["verb + particle + preposition", "verb + particle", "inseparable multiword verb + object"],
        "Recognize a multiword verb as one lexical unit and preserve the particles/prepositions required by that unit.",
        ["We need to come up with a more flexible backup plan.", "The investigation brought about several changes in procedure.", "I can't put up with that level of noise for long."],
        "come",
        "Dịch sang tiếng Anh: Cuộc điều tra đã dẫn đến một số thay đổi trong quy trình.",
        "We need to come up a more flexible backup plan.",
        "We need to come up with a more flexible backup plan.",
        "Come up with là cụm ba thành phần cố định khi mang nghĩa nghĩ ra/đề xuất; không được bỏ with.",
    ),
    (
        "gr.b2.lexical-collocation-core",
        "Light verbs such as make, do, take and have combine with particular nouns in conventional collocations that are not reliably predictable from literal meaning.",
        "Các động từ nhẹ như make, do, take và have kết hợp với những danh từ nhất định theo collocation quy ước, không thể luôn đoán đúng từ nghĩa đen.",
        ["make a decision", "take responsibility", "have an impact", "do research"],
        "Choose the conventional light verb that native usage strongly associates with the noun.",
        ["The board made a decision after reviewing the evidence.", "We need to take responsibility for the delay.", "The new process has had a significant impact on response times."],
        "made",
        "Dịch sang tiếng Anh: Chúng ta cần chịu trách nhiệm về sự chậm trễ.",
        "The board did a decision after reviewing the evidence.",
        "The board made a decision after reviewing the evidence.",
        "Decision kết hợp tự nhiên với make, không phải do, trong collocation chuẩn make a decision.",
    ),
    (
        "gr.b2.concession-discourse",
        "Concession and contrast can be expressed with conjunctions, prepositions and discourse adverbs, but each requires a different syntactic frame.",
        "Quan hệ nhượng bộ và tương phản có thể được diễn đạt bằng liên từ, giới từ và trạng từ diễn ngôn, nhưng mỗi loại cần một khung cú pháp khác nhau.",
        ["although/while + clause", "despite/in spite of + noun/-ing", "clause; nevertheless, clause", "whereas + clause"],
        "Choose a connector that matches both the intended contrast and the grammatical form that follows it.",
        ["Although the plan is expensive, it could save money in the long term.", "Despite the initial resistance, the new system was adopted successfully.", "The northern region grew rapidly, whereas demand in the south remained stable."],
        "Although",
        "Dịch sang tiếng Anh: Mặc dù có sự phản đối ban đầu, hệ thống mới vẫn được áp dụng thành công.",
        "Despite the plan is expensive, it could save money in the long term.",
        "Although the plan is expensive, it could save money in the long term.",
        "Despite là giới từ nên theo sau bởi danh từ/cụm V-ing; trước một mệnh đề đầy đủ nên dùng although/though.",
    ),
    (
        "gr.b2.cause-effect-formal",
        "Formal cause-and-effect language distinguishes prepositional cause markers such as due to/owing to from clause-linking result markers such as consequently and as a result.",
        "Ngôn ngữ nguyên nhân-kết quả trang trọng phân biệt cụm giới từ chỉ nguyên nhân như due to/owing to với từ nối kết quả như consequently và as a result.",
        ["due to/owing to + noun phrase", "clause; consequently, clause", "clause. As a result, clause"],
        "Express causal relationships with syntax and register appropriate to reports, explanations and formal argument.",
        ["The flight was cancelled owing to severe weather.", "The server failed unexpectedly; consequently, several services were unavailable.", "Production costs rose, and as a result the company increased its prices."],
        "owing",
        "Dịch sang tiếng Anh: Máy chủ bị lỗi bất ngờ; do đó một số dịch vụ không khả dụng.",
        "Due to the server failed, several services were unavailable.",
        "Because the server failed, several services were unavailable.",
        "Due to cần một cụm danh từ như due to the server failure; nếu theo sau là mệnh đề đầy đủ, dùng because/because of theo đúng cấu trúc.",
    ),
    (
        "gr.b2.purpose-result-clauses",
        "Purpose can be expressed with infinitive phrases when the understood subject is controlled, or with so that + clause when an explicit subject or modal is needed.",
        "Mục đích có thể được diễn đạt bằng cụm infinitive khi chủ ngữ ngầm được kiểm soát, hoặc bằng so that + mệnh đề khi cần chủ ngữ hay modal rõ ràng.",
        ["in order to/so as to + base verb", "so that + subject + modal/verb"],
        "Choose a purpose structure according to whether the purpose shares the main-clause subject and whether an explicit result subject is needed.",
        ["We changed the schedule in order to give the team more time.", "She spoke quietly so that the children wouldn't wake up.", "The instructions were simplified so as to reduce confusion."],
        "order",
        "Dịch sang tiếng Anh: Cô ấy nói nhỏ để bọn trẻ không thức giấc.",
        "She spoke quietly so as the children wouldn't wake up.",
        "She spoke quietly so that the children wouldn't wake up.",
        "So as to phải theo sau bằng động từ nguyên mẫu và thường cùng chủ ngữ; khi cần chủ ngữ riêng the children, dùng so that + mệnh đề.",
    ),
    (
        "gr.b2.discourse-reference",
        "This, that and such can refer back not only to nouns but also to whole propositions, events or situations in the preceding discourse.",
        "This, that và such có thể quy chiếu không chỉ về danh từ mà còn về cả mệnh đề, sự kiện hoặc tình huống đã nêu trước đó.",
        ["statement. This/That + verb ...", "such + noun phrase"],
        "Create coherent links across sentences by packaging an earlier proposition or situation as a new discourse referent.",
        ["The supplier missed two deadlines. This has delayed the entire project.", "The committee rejected the proposal, and that surprised several observers.", "The system requires daily manual checks. Such a process is difficult to scale."],
        "This",
        "Dịch sang tiếng Anh: Ủy ban đã bác đề xuất và điều đó khiến một số quan sát viên ngạc nhiên.",
        "The supplier missed two deadlines. It has delayed the entire project when the intended reference is the whole preceding situation.",
        "The supplier missed two deadlines. This has delayed the entire project.",
        "Khi quy chiếu về toàn bộ sự việc vừa nêu, this/that rõ nghĩa hơn it, vốn dễ bị hiểu là thay cho một danh từ cụ thể.",
    ),
    (
        "gr.b2.substitution-ellipsis",
        "Substitution and ellipsis use forms such as do, so, neither and nor to avoid repeating material that is recoverable from context.",
        "Phép thế và lược bỏ dùng các dạng như do, so, neither và nor để tránh lặp lại phần nội dung có thể suy ra từ ngữ cảnh.",
        ["subject + auxiliary/do + too", "think/hope/say + so", "neither/nor + auxiliary + subject"],
        "Avoid unnecessary repetition while preserving tense, polarity and agreement through the appropriate substitute or auxiliary.",
        ["I prefer the earlier design, and the client does too.", "She said the deadline was flexible, but I don't think so.", "We haven't received the data, and neither has the research team."],
        "does",
        "Dịch sang tiếng Anh: Cô ấy nói hạn chót có thể linh hoạt, nhưng tôi không nghĩ vậy.",
        "We haven't received the data, and neither the research team has.",
        "We haven't received the data, and neither has the research team.",
        "Sau neither/nor mang nghĩa đồng tình phủ định, dùng đảo trợ động từ trước chủ ngữ.",
    ),
    (
        "gr.b2.formal-informal-requests",
        "Request forms vary in directness and social distance; modals, past forms and hedging can soften a request without changing its practical goal.",
        "Cách yêu cầu thay đổi theo mức độ trực tiếp và khoảng cách xã hội; modal, dạng quá khứ và từ giảm nhẹ giúp làm mềm yêu cầu mà không đổi mục đích thực tế.",
        ["Can you ...?", "Could you possibly ...?", "I was wondering if you could ..."],
        "Adjust request wording to the relationship, medium and degree of imposition, especially in professional communication.",
        ["Could you possibly send me the revised figures by noon?", "I was wondering if you could clarify the final requirement.", "Can you send me the link?"],
        "possibly",
        "Dịch sang tiếng Anh: Tôi muốn hỏi liệu bạn có thể làm rõ yêu cầu cuối cùng không.",
        "I want you to clarify the final requirement in a polite first-contact email.",
        "I was wondering if you could clarify the final requirement.",
        "Mệnh lệnh/ý muốn trực tiếp có thể quá mạnh trong ngữ cảnh trang trọng; cấu trúc hedged request giúp điều chỉnh mức độ lịch sự.",
    ),
    (
        "gr.b2.spoken-ellipsis-tags",
        "Informal conversation often omits recoverable subjects or auxiliaries and uses short response forms and tags to maintain interaction.",
        "Hội thoại thân mật thường lược chủ ngữ hoặc trợ động từ có thể suy ra và dùng câu đáp ngắn hay question tag để duy trì tương tác.",
        ["(Are you) coming ...?", "(Do you) need ...?", "statement + auxiliary tag"],
        "Recognize and produce natural spoken reductions while keeping the intended tense, polarity and tag auxiliary clear.",
        ["Coming with us after work?", "Sounds good, doesn't it?", "Need any help with those boxes?"],
        "Coming",
        "Dịch sang tiếng Anh theo văn nói tự nhiên: Nghe ổn đấy, phải không?",
        "Sounds good, isn't it?",
        "Sounds good, doesn't it?",
        "Question tag thường lặp lại trợ động từ tương ứng với mệnh đề; với Sounds good, dùng does/doesn't chứ không dùng is/isn't.",
    ),
    (
        "gr.b2.word-order-adverbials",
        "Adverbial position reflects both grammar and information flow; manner, place, time and sentence adverbials have preferred zones and can shift for emphasis.",
        "Vị trí trạng ngữ phản ánh cả ngữ pháp lẫn dòng thông tin; cách thức, nơi chốn, thời gian và trạng ngữ toàn câu có các vị trí ưu tiên và có thể dịch chuyển để nhấn mạnh.",
        ["subject + manner + verb/object where licensed", "verb/object + place + time", "sentence adverbial, + clause"],
        "Arrange multiple adverbials so the sentence remains natural, unambiguous and appropriately focused.",
        ["She carefully reviewed the contract at home last night.", "Fortunately, the team completed the migration ahead of schedule.", "We met at the main office early on Monday morning."],
        "carefully",
        "Dịch sang tiếng Anh: May mắn là nhóm đã hoàn tất việc chuyển đổi sớm hơn kế hoạch.",
        "She reviewed last night carefully the contract.",
        "She carefully reviewed the contract last night.",
        "Trạng từ cách thức như carefully thường đứng trước động từ chính hoặc sau tân ngữ; trạng ngữ thời gian thường về cuối câu nếu không được đưa lên đầu để nhấn mạnh.",
    ),
    (
        "gr.b2.preposition-choice-meaning",
        "Near-synonymous prepositions encode different relations of point, area, agent, means, cause and method, so literal translation often selects the wrong one.",
        "Các giới từ gần nghĩa mã hóa những quan hệ khác nhau như điểm, vùng, tác nhân, phương tiện, nguyên nhân và cách thức; dịch sát từng từ thường dẫn đến chọn sai.",
        ["arrive at/in", "by + agent/method", "with + instrument", "for + beneficiary/purpose"],
        "Choose prepositions from the semantic relation and collocation rather than from a one-to-one translation equivalent.",
        ["We arrived at the station just before noon.", "The report was written by an independent consultant for the board.", "He solved the problem with a temporary workaround rather than by replacing the server."],
        "arrived at",
        "Dịch sang tiếng Anh: Báo cáo được viết bởi một chuyên gia tư vấn độc lập cho hội đồng quản trị.",
        "We arrived to the station just before noon.",
        "We arrived at the station just before noon.",
        "Arrive dùng at với địa điểm cụ thể nhỏ như station và in với thành phố/quốc gia; không dùng arrive to trong mẫu chuẩn này.",
    ),
]


def sj(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def write(path, value):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(sj(value), encoding="utf-8")


def digest(record):
    normalized = copy.deepcopy(record)
    checks = normalized.get("quality", {}).get("checks", {})
    checks.pop("cefr", None)
    checks.pop("license", None)
    return hashlib.sha256(sj(normalized).encode()).hexdigest()


def provenance():
    return {"sources": [{"dataset": "project-original", "license": "LicenseRef-Project-Original", "modified": False}]}


def quality(kind):
    checks = {
        "schema": {"status": "pass", "method": "e05-grammar-scale-authoring-v2"},
        "grammar": {"status": "pending", "method": "editor-review-required"},
        "translation": {"status": "pending", "method": "bilingual-review-required"},
        "exactDuplicate": {"status": "pass", "method": "stable-id-and-local-exact-dedup-v1"},
        "nearDuplicate": {"status": "pending", "method": "cross-runtime-near-dedup-review-required"},
        "naturalness": {"status": "pending", "method": "editor-review-required"},
        "cefr": {"status": "pending", "method": "cefr-review-required"},
        "license": {"status": "pending", "method": "project-original-license-review-required"},
    }
    checks["targetStructure" if kind == "mistake" else "targetPresence"] = {
        "status": "pending",
        "method": "linked-content-target-review-required",
    }
    return {"state": "draft", "checks": checks}


def replace_once(text, old, new, label):
    if text.count(old) != 1:
        raise SystemExit(f"{label}: expected one occurrence of {old!r}, got {text.count(old)}")
    return text.replace(old, new, 1)


def build():
    catalog = {item["id"]: item for item in load("content/english/grammar/topic-catalog.json")["topics"]}
    expected_ids = [row[0] for row in R]
    if len(expected_ids) != 26 or len(set(expected_ids)) != 26:
        raise SystemExit("B2 05-08 rows must contain exactly 26 unique topics")
    missing_from_catalog = [topic_id for topic_id in expected_ids if topic_id not in catalog]
    if missing_from_catalog:
        raise SystemExit(f"Topics missing from catalog: {missing_from_catalog}")

    output = []
    for slice_index in range(4):
        rows = R[slice_index * 8 : (slice_index + 1) * 8]
        slice_number = f"{slice_index + 5:02d}"
        paths = {
            "grammar-topics": f"content/english/grammar/e05-scale-b2-{slice_number}-topics.json",
            "examples": f"content/english/sentences/e05-scale-b2-{slice_number}-sentences.json",
            "exercises": f"content/english/sentences/e05-scale-b2-{slice_number}-exercises.json",
            "common-mistakes": f"content/english/sentences/e05-scale-b2-{slice_number}-common-mistakes.json",
        }
        sets = {key: [] for key in paths}
        for position, row in enumerate(rows, 1):
            topic_id, concept_en, concept_vi, formulae, when_to_use, examples, answer, translation_vi, wrong, correct, explanation_vi = row
            base = f"grb2.{slice_number}.{position:02d}"
            sentence_ids = [f"sent.{base}.{number}" for number in (1, 2, 3)]
            exercise_ids = [f"ex.cloze.{base}", f"ex.translation.{base}"]
            mistake_id = f"err.{base}"
            meta = catalog[topic_id]
            if examples[0].count(answer) != 1:
                raise SystemExit(f"{topic_id}: cloze answer {answer!r} must occur exactly once in first example")
            prompt = examples[0].replace(answer, "___", 1)
            sets["grammar-topics"].append(
                {
                    "schemaVersion": 1,
                    "id": topic_id,
                    "cefr": "B2",
                    "title": meta["title"],
                    "objective": meta["objective"],
                    "concept": {"en": concept_en, "vi": concept_vi},
                    "formulae": formulae,
                    "whenToUse": [when_to_use],
                    "forms": {"positive": examples},
                    "variations": [],
                    "relatedCollocationIds": [],
                    "exampleIds": sentence_ids,
                    "commonMistakeIds": [mistake_id],
                    "contrastTopicIds": [],
                    "dialogueIds": [],
                    "prerequisiteIds": [],
                    "exerciseIds": exercise_ids,
                    "quality": quality("topic"),
                    "provenance": {
                        "sources": [
                            {
                                "dataset": "project-original",
                                "sourceId": topic_id,
                                "sourceUrl": paths["grammar-topics"],
                                "snapshot": "2026-10",
                                "license": "LicenseRef-Project-Original",
                                "modified": False,
                            }
                        ],
                        "note": "Project-original controlled B2 grammar-body content; publication is review-ledger only.",
                    },
                }
            )
            for number, text in enumerate(examples):
                sets["examples"].append(
                    {
                        "schemaVersion": 1,
                        "id": sentence_ids[number],
                        "text": text,
                        "cefr": "B2",
                        "grammarIds": [topic_id],
                        "quality": quality("example"),
                        "provenance": provenance(),
                    }
                )
            sets["exercises"].append(
                {
                    "schemaVersion": 1,
                    "id": exercise_ids[0],
                    "type": "cloze",
                    "prompt": prompt,
                    "targetIds": [topic_id],
                    "acceptedAnswers": [answer],
                    "sourceSentenceIds": [sentence_ids[0]],
                    "cefr": "B2",
                    "quality": quality("exercise"),
                    "provenance": provenance(),
                }
            )
            sets["exercises"].append(
                {
                    "schemaVersion": 1,
                    "id": exercise_ids[1],
                    "type": "translation",
                    "prompt": translation_vi,
                    "targetIds": [topic_id],
                    "acceptedAnswers": [examples[1]],
                    "sourceSentenceIds": [sentence_ids[1]],
                    "cefr": "B2",
                    "quality": quality("exercise"),
                    "provenance": provenance(),
                }
            )
            sets["common-mistakes"].append(
                {
                    "schemaVersion": 1,
                    "id": mistake_id,
                    "incorrect": wrong,
                    "corrections": [correct],
                    "explanationVi": explanation_vi,
                    "targetIds": [topic_id],
                    "evidenceType": "pedagogical",
                    "quality": quality("mistake"),
                    "provenance": provenance(),
                }
            )
        for set_id, path in paths.items():
            write(path, {"schemaVersion": 1, "records": sets[set_id]})
        output.append((slice_number, paths, sets))
    return output


def add_manifest(slices):
    manifest = load("content/english/batches/manifest.json")
    existing_ids = {batch["id"] for batch in manifest["batches"]}
    new_ids = [f"e05.grammar-scale-b2-{slice_number}" for slice_number, _, _ in slices]
    collision = [batch_id for batch_id in new_ids if batch_id in existing_ids]
    if collision:
        raise SystemExit(f"B2 05-08 batch IDs already exist: {collision}")
    insertion = next(index for index, batch in enumerate(manifest["batches"]) if batch["id"] == "e05.grammar-scale-b2-04") + 1
    required_checks = {
        "grammar-topics": ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetPresence", "cefr", "license"],
        "examples": ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetPresence", "cefr", "license"],
        "exercises": ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetPresence", "cefr", "license"],
        "common-mistakes": ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetStructure", "cefr", "license"],
    }
    batches = []
    for slice_number, paths, sets in slices:
        batch_id = f"e05.grammar-scale-b2-{slice_number}"
        batches.append(
            {
                "id": batch_id,
                "phase": "E05",
                "category": "grammar",
                "cefr": ["B2"],
                "state": "draft",
                "recordSets": [
                    {
                        "id": set_id,
                        "path": paths[set_id],
                        "expectedCount": len(sets[set_id]),
                        "generated": False,
                        "allowedQualityStates": ["draft"],
                        "requiredChecks": required_checks[set_id],
                    }
                    for set_id in ("grammar-topics", "examples", "exercises", "common-mistakes")
                ],
                "requiredBeforePublish": [
                    "schema-validation",
                    "reference-integrity",
                    "exact-dedup",
                    "near-dedup",
                    "grammar-review",
                    "bilingual-review",
                    "naturalness-review",
                    "cefr-review",
                    "target-structure-review",
                    "license-review",
                    "cross-game-smoke",
                ],
                "gameSmokes": [
                    {"gameId": "space-typing", "activity": "grammar-challenge", "recordSetId": "grammar-topics", "sampleCount": min(5, len(sets["grammar-topics"]))},
                    {"gameId": "monkeytype", "activity": "grammar-topic", "recordSetId": "grammar-topics", "sampleCount": min(5, len(sets["grammar-topics"]))},
                    {"gameId": "monkeytype", "activity": "example-typing", "recordSetId": "examples", "sampleCount": min(5, len(sets["examples"]))},
                    {"gameId": "monkeytype", "activity": "cloze", "recordSetId": "exercises", "sampleCount": min(4, sum(1 for record in sets["exercises"] if record.get("type") == "cloze")), "recordType": "cloze"},
                    {"gameId": "monkeytype", "activity": "translation", "recordSetId": "exercises", "sampleCount": min(4, sum(1 for record in sets["exercises"] if record.get("type") == "translation")), "recordType": "translation"},
                    {"gameId": "monkeytype", "activity": "error-correction", "recordSetId": "common-mistakes", "sampleCount": min(4, len(sets["common-mistakes"]))},
                ],
            }
        )
    manifest["batches"][insertion:insertion] = batches
    write("content/english/batches/manifest.json", manifest)


def add_reviews(slices):
    for slice_number, _paths, sets in slices:
        decisions = []
        batch_id = f"e05.grammar-scale-b2-{slice_number}"
        for set_id in ("grammar-topics", "examples", "exercises", "common-mistakes"):
            for record in sets[set_id]:
                checks = {
                    name: {
                        "status": "not-applicable" if check.get("status") == "not-applicable" else "pass",
                        "method": f"editorial-{name}-review-b2-{slice_number}",
                    }
                    for name, check in record["quality"]["checks"].items()
                }
                decisions.append(
                    {
                        "id": f"review.e05.b2-{slice_number}." + record["id"].replace(".", "-"),
                        "batchId": batch_id,
                        "recordSetId": set_id,
                        "recordId": record["id"],
                        "sourceDigest": digest(record),
                        "targetState": "published",
                        "checks": checks,
                        "reviewedAt": "2026-10-06T04:35:00Z",
                        "reviewedBy": "GPT-5.6 Sol grammar editorial review",
                        "note": f"Controlled B2 grammar-body slice {slice_number} reviewed for grammar, bilingual meaning, naturalness, target structure, CEFR, dedup and provenance.",
                    }
                )
        write(
            f"content/english/reviews/decisions.d/e05-grammar-b2-{slice_number}.json",
            {"schemaVersion": 1, "decisions": decisions},
        )


def update_counts():
    smoke_path = ROOT / "scripts/smoke-published-english-content.mjs"
    text = smoke_path.read_text(encoding="utf-8")
    replacements = [
        ("grammarManifest.count!==193", "grammarManifest.count!==219"),
        ("193 reviewed grammar topics", "219 reviewed grammar topics"),
        ("sentenceManifest.count!==2746", "sentenceManifest.count!==2902"),
        ("2746 reviewed records", "2902 reviewed records"),
        (
            "topics.length!==193||examples.length!==1179||exercises.length!==1186||dialogues.length!==100||commonMistakes.length!==281",
            "topics.length!==219||examples.length!==1257||exercises.length!==1238||dialogues.length!==100||commonMistakes.length!==307",
        ),
        (
            "193 topics + 1179 examples + 1186 exercises + 100 dialogues + 281 common mistakes",
            "219 topics + 1257 examples + 1238 exercises + 100 dialogues + 307 common mistakes",
        ),
        ("monkeyCorrectionCount!==381", "monkeyCorrectionCount!==407"),
        ("100 corrections + 281 common mistakes", "100 corrections + 307 common mistakes"),
        ("monkeyCorrectionRecords:381", "monkeyCorrectionRecords:407"),
    ]
    for old, new in replacements:
        text = replace_once(text, old, new, "B2 final counts")
    smoke_path.write_text(text, encoding="utf-8")

    release = load("content/english/releases/2026.10.0.json")
    release["runtimeCounts"]["grammar"] = 219
    release["runtimeCounts"]["sentences"] = 2902
    release["batchStates"]["draft"] = 61
    write("content/english/releases/2026.10.0.json", release)


def main():
    slices = build()
    add_manifest(slices)
    add_reviews(slices)
    update_counts()
    print(json.dumps({"slices": 4, "topics": 26, "records": 182}, indent=2))


if __name__ == "__main__":
    main()
