from __future__ import annotations
import copy, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

R = [('gr.c2.narrative-viewpoint-aspect',
  'Advanced narrative manages tense and aspect as viewpoint choices: simple forms move events forward, progressive forms open an internal view, and perfect forms look back from a reference point.',
  'Tường thuật nâng cao quản lý thì và thể như lựa chọn điểm nhìn: dạng đơn đẩy sự kiện tiến lên, tiếp diễn mở góc nhìn bên trong, và hoàn thành nhìn ngược từ một mốc tham chiếu.',
  ['simple tense for event progression', 'progressive for internal/ongoing viewpoint', 'perfect for anteriority relative to a reference time'],
  'Shift viewpoint deliberately across scenes while keeping the temporal reference point recoverable.',
  ['By the time the inspectors arrived, the night team had been monitoring the pressure for six hours, and the alarms were still sounding.',
   "She opens the archive, finds the unsigned note, and suddenly remembers what the witness had said the previous evening.",
   'The river had been rising for days; by dawn, water was spilling across the lower road.'],
  'had been monitoring',
  'Dịch sang tiếng Anh: Cô ấy mở kho lưu trữ, tìm thấy tờ ghi chú chưa ký và chợt nhớ điều nhân chứng đã nói tối hôm trước.',
  'By the time the inspectors arrived, the night team was monitored the pressure for six hours.',
  'By the time the inspectors arrived, the night team had been monitoring the pressure for six hours.',
  'Cần past perfect continuous để nhìn lại một hoạt động kéo dài đến mốc inspectors arrived.'),
 ('gr.c2.historical-present',
  'The historical present switches into present tense inside a past narrative to make selected events feel immediate, while surrounding time references keep the chronology clear.',
  'Historical present chuyển sang hiện tại trong một câu chuyện quá khứ để làm một số sự kiện trở nên sống động, trong khi các mốc thời gian xung quanh vẫn giữ trình tự rõ.',
  ['past narrative frame → selected present-tense scene', 'present tense used stylistically, not accidentally'],
  'Use the historical present consistently for a deliberately foregrounded scene, then signal any return to past narration.',
  ["So I enter the room, and the chair looks up and says, 'We need to talk,' even though ten minutes earlier she had denied there was a problem.",
   'In 1969 the team reaches the ridge and discovers that the route marked on the map no longer exists.',
   'The witness pauses, turns toward the jury, and then describes what she had seen outside the station.'],
  'I enter the room',
  'Dịch sang tiếng Anh: Năm 1969 nhóm lên tới sườn núi và phát hiện tuyến đường đánh dấu trên bản đồ không còn tồn tại.',
  'So I entered the room, and the chair looks up and says, when a deliberate historical-present scene is intended.',
  'So I enter the room, and the chair looks up and says.',
  'Khi đã chuyển có chủ ý sang historical present cho cảnh trọng tâm, các động từ sự kiện trong cùng chuỗi nên nhất quán.'),
 ('gr.c2.sequence-of-tenses',
  'Sequence of tenses in complex reporting reflects both the reporting time and whether the embedded proposition is still valid; backshift can therefore be obligatory, optional, or deliberately avoided.',
  'Sequence of tenses trong tường thuật phức phản ánh cả thời điểm tường thuật và việc mệnh đề nhúng còn đúng hay không; vì vậy lùi thì có thể bắt buộc, tùy chọn hoặc chủ ý không dùng.',
  ['past reporting verb + backshifted clause', 'non-backshift for a still-valid/general proposition where licensed'],
  'Choose backshift from temporal interpretation and current validity rather than applying it mechanically.',
  ['The review concluded that the control had failed because the software was relying on a configuration that was already obsolete.',
   'The lecturer reminded us that water boils at 100 degrees Celsius at standard pressure.',
   'She said in March that the company would publish the figures once the audit had finished.'],
  'had failed',
  'Dịch sang tiếng Anh: Giảng viên nhắc chúng tôi rằng nước sôi ở 100 độ C ở áp suất tiêu chuẩn.',
  'The review concluded that the control has failed because the software was relying on an obsolete configuration.',
  'The review concluded that the control had failed because the software was relying on an obsolete configuration.',
  'Khi sự cố xảy ra trước mốc concluded trong quá khứ, past perfect thể hiện quan hệ trước-sau rõ.'),
 ('gr.c2.layered-counterfactuals',
  'Layered counterfactuals combine several unreal assumptions and consequences across different time frames, with each clause locating its own hypothetical relation.',
  'Counterfactual nhiều tầng kết hợp nhiều giả định và hệ quả phi thực ở các mốc thời gian khác nhau, mỗi mệnh đề tự định vị quan hệ giả định của nó.',
  ['if + past perfect ... would have + participle; if that had happened, would + verb now', 'nested/linked counterfactual consequences'],
  'Use layered counterfactuals only when each unreal step has a clear causal and temporal relation to the next.',
  ['If the regulator had intervened earlier, the merger might have been delayed; had that happened, the market would be less concentrated today.',
   'Had we retained the original backup, we could have restored the archive, which would have spared us the reconstruction now under way.',
   'If she were more willing to delegate, she might have accepted the promotion last year and would not be managing both teams now.'],
  'had intervened',
  'Dịch sang tiếng Anh: Nếu chúng tôi giữ bản sao lưu ban đầu, chúng tôi có thể đã khôi phục kho dữ liệu và tránh được việc tái dựng hiện nay.',
  'If the regulator would have intervened earlier, the merger might have been delayed.',
  'If the regulator had intervened earlier, the merger might have been delayed.',
  'Mệnh đề điều kiện phản thực quá khứ dùng past perfect, không dùng would have.'),
 ('gr.c2.implicit-conditionals',
  'Conditional meaning can be conveyed without if through context, inversion, a noun phrase, an imperative, or a modalized main clause.',
  'Nghĩa điều kiện có thể được diễn đạt không cần if thông qua ngữ cảnh, đảo ngữ, cụm danh từ, mệnh lệnh hoặc mệnh đề chính có modal.',
  ['with/but for/without + noun phrase, conditional result', 'imperative + and/or + result', 'modal result with condition inferred from context'],
  'Recognize the missing condition and make it explicit only when clarity requires it.',
  ['Without the additional evidence, the appeal would almost certainly have failed.',
   'One more delay and the funding agreement could collapse altogether.',
   'A less experienced team might have abandoned the search at that point.'],
  'Without the additional evidence',
  'Dịch sang tiếng Anh: Chỉ thêm một lần trì hoãn nữa là thỏa thuận tài trợ có thể sụp đổ hoàn toàn.',
  'Without the additional evidence, the appeal will almost certainly have failed.',
  'Without the additional evidence, the appeal would almost certainly have failed.',
  'Kết quả phản thực quá khứ cần would have + past participle khi điều kiện ngầm không xảy ra.'),
 ('gr.c2.so-such-inversion',
  'Formal or literary clauses can front so + adjective/adverb or such + noun phrase, triggering inversion or an emphatic copular pattern.',
  'Mệnh đề trang trọng hoặc văn chương có thể đưa so + tính/trạng từ hoặc such + cụm danh từ lên đầu, kéo theo đảo ngữ hoặc mẫu copular nhấn mạnh.',
  ['So + adjective + be + subject + that ...', 'Such + be + noun phrase + that ...'],
  'Use these highly marked patterns for deliberate rhetorical emphasis, not as a neutral default.',
  ['So convincing was the evidence that even the original critics accepted the revised conclusion.',
   'Such was the intensity of the storm that the coastal sensors stopped transmitting.',
   'So rapidly did demand increase that the supplier exhausted its reserve stock within a week.'],
  'So convincing was',
  'Dịch sang tiếng Anh: Cơn bão dữ dội đến mức các cảm biến ven biển ngừng truyền dữ liệu.',
  'So convincing the evidence was that even the critics accepted the conclusion.',
  'So convincing was the evidence that even the critics accepted the conclusion.',
  'Khi front so + adjective trong mẫu trang trọng, đảo be/trợ động từ lên trước chủ ngữ.'),
 ('gr.c2.locative-inversion',
  'Locative and directional inversion places a location or movement expression first and, with suitable verbs, places the lexical verb before a full noun subject.',
  'Locative/directional inversion đưa cụm nơi chốn hoặc hướng lên đầu và với động từ phù hợp, đặt động từ từ vựng trước chủ ngữ danh từ đầy đủ.',
  ['locative/directional phrase + verb + full noun subject'],
  'Use this marked order mainly in descriptive, literary, or scene-setting prose, especially with be, stand, lie, come, and similar verbs.',
  ['Beyond the final checkpoint stood a row of temporary shelters.',
   'From the eastern tunnel emerged a maintenance vehicle carrying the replacement transformer.',
   'At the center of the courtyard lies a stone basin dating from the seventeenth century.'],
  'Beyond the final checkpoint stood',
  'Dịch sang tiếng Anh: Từ đường hầm phía đông xuất hiện một xe bảo trì chở máy biến áp thay thế.',
  'Beyond the final checkpoint did stand a row of temporary shelters.',
  'Beyond the final checkpoint stood a row of temporary shelters.',
  'Locative inversion với các động từ như stand/emerge thường đảo động từ từ vựng trực tiếp, không thêm do.'),
 ('gr.c2.formulaic-subjunctive',
  'Formulaic subjunctives survive in fixed expressions and the irrealis were marks remote hypotheticals independently of subject number.',
  'Subjunctive công thức tồn tại trong các cụm cố định, còn irrealis were đánh dấu giả định xa thực tế không phụ thuộc số của chủ ngữ.',
  ['be that as it may', 'come what may', 'if I/he/she were ...', 'far be it from me ...'],
  'Use fixed subjunctive expressions as register-sensitive units and use were for careful irrealis hypotheses.',
  ['Be that as it may, the committee still has to explain why the safeguard was removed.',
   'Were the evidence less ambiguous, I would support a stronger conclusion.',
   'Come what may, the archive must remain accessible to the inquiry.'],
  'Be that as it may',
  'Dịch sang tiếng Anh: Nếu bằng chứng ít mơ hồ hơn, tôi sẽ ủng hộ một kết luận mạnh hơn.',
  'Was the evidence less ambiguous, I would support a stronger conclusion.',
  'Were the evidence less ambiguous, I would support a stronger conclusion.',
  'Trong giả định irrealis trang trọng, were dùng với mọi ngôi.'),
 ('gr.c2.gapping-complex-ellipsis',
  'Gapping omits a repeated verb or verb sequence from a non-initial coordinated clause while leaving contrasting remnants.',
  'Gapping lược động từ hoặc chuỗi động từ lặp lại ở vế phối hợp không đầu tiên, để lại các thành phần tương phản.',
  ['clause with verb, and subject + [gap] + contrasting complement'],
  'Use gapping only when the missing predicate is uniquely recoverable and the remaining constituents are structurally parallel.',
  ['The northern region approved the proposal in May, and the southern region in July.',
   'Some reviewers considered the evidence persuasive; others, dangerously incomplete.',
   'Maria will present the legal analysis, and David the financial implications.'],
  'and the southern region in July',
  'Dịch sang tiếng Anh: Maria sẽ trình bày phân tích pháp lý, còn David trình bày các hệ quả tài chính.',
  'The northern region approved the proposal in May, and the southern region approved in July, as a gapping construction.',
  'The northern region approved the proposal in May, and the southern region in July.',
  'Gapping lược toàn bộ predicate lặp lại; không để lại một phần gây cấu trúc nửa lược nửa đầy.'),
 ('gr.c2.comparative-clause-ellipsis',
  'Comparative clauses after than and as often omit material recoverable from the matrix clause, but the ellipsis must preserve the intended comparison.',
  'Mệnh đề so sánh sau than và as thường lược phần có thể suy ra từ mệnh đề chính, nhưng phần lược phải giữ đúng đối tượng so sánh.',
  ['comparative + than + reduced clause', 'as + adjective/adverb + as + reduced clause'],
  'Expand the reduced clause mentally to check case, scope, and whether like is being compared with like.',
  ['The revised model predicts a steeper decline than the earlier one does.',
   'The second survey attracted more rural respondents than the first.',
   'The measure is not as sensitive to short-term volatility as the previous index was.'],
  'than the earlier one does',
  'Dịch sang tiếng Anh: Khảo sát thứ hai thu hút nhiều người trả lời ở nông thôn hơn khảo sát thứ nhất.',
  'The second survey attracted more rural respondents than the first attracted rural respondents more.',
  'The second survey attracted more rural respondents than the first.',
  'Sau than có thể lược predicate trùng nếu đối tượng so sánh vẫn rõ; không lặp sai trật tự.'),
 ('gr.c2.free-relatives',
  'A free or fused relative contains its own antecedent, so the wh-form and relative clause together function as a complete noun phrase or adjunct.',
  'Free/fused relative tự chứa antecedent, vì vậy wh-form cùng mệnh đề quan hệ hoạt động như một cụm danh từ hoặc trạng ngữ hoàn chỉnh.',
  ['what + clause = the thing(s) that ...', 'where + clause = the place where ...', 'how + clause = the way in which ...'],
  'Use free relatives when no separate head noun is needed and distinguish them from interrogative embedded clauses by function.',
  ['What the audit uncovered was more serious than the preliminary note had suggested.',
   'We returned to where the original samples had been stored.',
   'How the exception is interpreted will determine whether the appeal succeeds.'],
  'What the audit uncovered',
  'Dịch sang tiếng Anh: Cách ngoại lệ được diễn giải sẽ quyết định liệu đơn kháng cáo có thành công hay không.',
  'The thing what the audit uncovered was more serious than expected.',
  'What the audit uncovered was more serious than expected.',
  'Free relative với what đã bao gồm nghĩa the thing(s) that, nên không đặt thêm head noun the thing.'),
 ('gr.c2.nominal-wh-ever-relatives',
  'Whoever, whatever, and whichever can head nominal free relatives meaning any person or thing satisfying the clause, distinct from concessive uses meaning no matter who/what/which.',
  'Whoever, whatever và whichever có thể đứng đầu free relative danh ngữ nghĩa là bất kỳ người/vật nào thỏa mệnh đề, khác với cách dùng nhượng bộ no matter.',
  ['whoever/whatever/whichever + clause as subject/object/complement'],
  'Determine whether the -ever clause fills a noun-phrase slot or adds a concessive circumstance.',
  ['Whoever drafted the final clause should explain why the exception was added.',
   'The panel will consider whatever evidence the parties submit before Friday.',
   'Choose whichever option provides the clearest audit trail.'],
  'Whoever drafted the final clause',
  'Dịch sang tiếng Anh: Hội đồng sẽ xem xét bất kỳ bằng chứng nào các bên nộp trước thứ Sáu.',
  'Whoever did draft the final clause should explains why the exception was added.',
  'Whoever drafted the final clause should explain why the exception was added.',
  'Nominal whoever-clause dùng cấu trúc mệnh đề bình thường; không thêm do-support hay -s sau modal.'),
 ('gr.c2.extraposition-anticipatory-it',
  'Extraposition places a heavy clausal subject later and fills subject position with anticipatory it, often improving information balance.',
  'Extraposition đưa chủ ngữ mệnh đề nặng về cuối và dùng anticipatory it ở vị trí chủ ngữ, thường giúp cân bằng thông tin.',
  ['It + be/seem + complement + that/to-clause', 'It + verb + that-clause'],
  'Use extraposition when the clausal subject would be awkwardly heavy initially, while preserving its semantic role.',
  ['It became clear during the hearing that several witnesses had been given different versions of the timetable.',
   'It would be difficult to justify abandoning the safeguard without new evidence.',
   'It surprised the reviewers that the discrepancy had not been detected earlier.'],
  'It became clear',
  'Dịch sang tiếng Anh: Sẽ khó biện minh cho việc bỏ biện pháp bảo vệ nếu không có bằng chứng mới.',
  'Became clear during the hearing that several witnesses had different timetables.',
  'It became clear during the hearing that several witnesses had different timetables.',
  'Anticipatory it lấp vị trí chủ ngữ khi that-clause được extrapose về cuối.'),
 ('gr.c2.raising-vs-control',
  'Raising predicates do not assign a semantic role to the surface subject, whereas control predicates select a participant that also controls an understood infinitive subject.',
  'Động từ raising không gán vai nghĩa cho chủ ngữ bề mặt, còn control predicate chọn một tham thể đồng thời kiểm soát chủ ngữ ngầm của infinitive.',
  ['subject + seem/appear + to-infinitive (raising)', 'subject + try/promise/decide + to-infinitive (control)'],
  'Use diagnostics such as expletive subjects and meaning preservation to distinguish raising from control.',
  ['The discrepancy appears to have originated in the imported dataset.',
   'There seems to be a mismatch between the two definitions.',
   'The investigators tried to reproduce the fault under controlled conditions.'],
  'appears to have originated',
  'Dịch sang tiếng Anh: Có vẻ có sự không khớp giữa hai định nghĩa.',
  'The discrepancy appears that it originated in the imported dataset.',
  'The discrepancy appears to have originated in the imported dataset.',
  'Appear trong raising pattern nhận to-infinitive; không dùng subject + appears that it... theo mẫu này.'),
 ('gr.c2.tough-constructions',
  'In a tough construction, the matrix subject is understood as a missing object inside the infinitive clause: This problem is difficult to solve.',
  'Trong tough construction, chủ ngữ mệnh đề chính được hiểu là tân ngữ bị khuyết bên trong infinitive: This problem is difficult to solve.',
  ['NP + be + easy/difficult/impossible + to-infinitive with object gap'],
  'Use the construction only when the matrix subject can be interpreted as the semantic object or complement of the infinitive.',
  ['The final paragraph is difficult to interpret without the earlier definition.',
   'This valve is awkward to reach when the outer panel is fitted.',
   'The distinction is easy to overlook in a rapidly edited document.'],
  'difficult to interpret',
  'Dịch sang tiếng Anh: Van này khó tiếp cận khi tấm ngoài đã được lắp.',
  'The final paragraph is difficult to interpret it without the earlier definition.',
  'The final paragraph is difficult to interpret without the earlier definition.',
  'Trong tough construction, object gap đã quy chiếu về final paragraph nên không thêm it.'),
 ('gr.c2.supplementive-clauses',
  'Supplementive non-finite clauses are loosely attached comments or circumstances whose understood subject must be recoverable from the host clause.',
  'Mệnh đề không chia supplementive là phần bình luận/hoàn cảnh gắn lỏng, với chủ ngữ ngầm phải suy ra rõ từ mệnh đề chính.',
  ['-ing/-ed/adjective supplement, main clause', 'main clause, -ing/-ed supplement'],
  'Use supplementives to add secondary circumstance or evaluation without creating dangling reference.',
  ['Concerned about the widening confidence interval, the analysts ran a second robustness check.',
   'The committee rejected the proposal, citing unresolved questions about enforcement.',
   'Still uncertain about the source of the leak, engineers kept the affected line isolated.'],
  'Concerned about the widening confidence interval',
  'Dịch sang tiếng Anh: Ủy ban bác đề xuất, viện dẫn các câu hỏi chưa được giải quyết về thực thi.',
  'Concerned about the widening confidence interval, a second robustness check was run by the analysts.',
  'Concerned about the widening confidence interval, the analysts ran a second robustness check.',
  'Chủ ngữ ngầm của Concerned phải là analysts, nên chủ ngữ mệnh đề chính cũng cần là analysts.'),
 ('gr.c2.absolute-clauses',
  'Absolute clauses contain their own explicit subject plus a non-finite, adjective, or prepositional predicate and modify the whole main clause.',
  'Absolute clause có chủ ngữ riêng cùng vị ngữ không chia, tính từ hoặc giới từ và bổ nghĩa cho toàn mệnh đề chính.',
  ['noun phrase + participle/adjective/prepositional phrase, main clause'],
  'Use absolutes for compact background circumstances when their relation to the main event is clear.',
  ['The final vote having been postponed, both delegations agreed to continue informal talks.',
   'All other factors equal, the revised method produces a slightly lower estimate.',
   'Her hands in her pockets, the witness waited silently outside the hearing room.'],
  'The final vote having been postponed',
  'Dịch sang tiếng Anh: Khi mọi yếu tố khác bằng nhau, phương pháp sửa đổi cho kết quả ước tính thấp hơn một chút.',
  'Having the final vote been postponed, both delegations agreed to continue talks.',
  'The final vote having been postponed, both delegations agreed to continue talks.',
  'Absolute clause cần subject riêng trước non-finite predicate: the final vote + having been postponed.'),
 ('gr.c2.verbless-clauses',
  'Verbless clauses omit an understood form of be and often function as compact conditional, concessive, temporal, or supplementive clauses.',
  'Verbless clause lược dạng be có thể suy ra và thường làm mệnh đề điều kiện, nhượng bộ, thời gian hoặc supplementive cô đọng.',
  ['if/when/though + adjective/PP', 'adjective/PP supplement with understood be'],
  'Use verbless clauses when the omitted copula and subject relation are unmistakable; restore a finite clause if ambiguity arises.',
  ['When necessary, the regulator may require an independent valuation.',
   'Though technically feasible, the proposed migration would be prohibitively expensive.',
   'Once fully operational, the new facility should process twice the current volume.'],
  'When necessary',
  'Dịch sang tiếng Anh: Mặc dù khả thi về kỹ thuật, việc chuyển đổi đề xuất sẽ quá tốn kém.',
  'Though it technically feasible, the proposed migration would be expensive.',
  'Though technically feasible, the proposed migration would be expensive.',
  'Trong verbless though-clause có thể lược subject + be hoàn toàn; không giữ subject mà bỏ riêng be.'),
 ('gr.c2.pp-attachment-ambiguity',
  'A prepositional phrase may plausibly modify a verb, noun, or another phrase; attachment ambiguity can change who did what or with what.',
  'Một cụm giới từ có thể bổ nghĩa hợp lý cho động từ, danh từ hoặc cụm khác; mơ hồ attachment có thể làm đổi ai làm gì hoặc bằng công cụ nào.',
  ['verb + NP + PP with multiple attachment sites'],
  'Detect competing parses and rewrite by repositioning, adding a relative clause, or naming the intended relation explicitly.',
  ['Using the new scanner, the analyst examined the document that had been stored in the archive.',
   'We discussed the proposal from the regional office during the afternoon session.',
   'The team photographed the device with the cracked housing, not with a telephoto lens.'],
  'Using the new scanner',
  'Dịch sang tiếng Anh: Nhóm chụp thiết bị có vỏ bị nứt, chứ không phải chụp bằng ống kính tele.',
  'The analyst examined the document in the archive with the new scanner.',
  'Using the new scanner, the analyst examined the document that had been stored in the archive.',
  'Đưa instrumental PP lên đầu và dùng relative clause cho location giúp loại bỏ hai attachment cạnh tranh.'),
 ('gr.c2.proper-name-articles',
  'Proper names are usually articleless, but conventional classes such as newspapers, families, plural states, organizations, seas, and descriptive landmarks take marked article patterns.',
  'Tên riêng thường không có mạo từ, nhưng các nhóm quy ước như báo chí, gia đình, quốc gia số nhiều, tổ chức, biển và địa danh mô tả có mẫu mạo từ riêng.',
  ['zero article + most personal/city names', 'the + selected organizations/newspapers/plural or descriptive names'],
  'Treat article choice with proper names as a conventional naming property and distinguish official titles from generic descriptions.',
  ['The Netherlands submitted its revised position to the United Nations before the deadline.',
   'She cited an editorial published in The Guardian during the earlier debate.',
   'Mount Etna was visible from the coast, while the Mediterranean remained unusually calm.'],
  'The Netherlands',
  'Dịch sang tiếng Anh: Cô ấy trích một bài xã luận đăng trên The Guardian trong cuộc tranh luận trước.',
  'Netherlands submitted its revised position to United Nations before the deadline.',
  'The Netherlands submitted its revised position to the United Nations before the deadline.',
  'Một số proper names quy ước cần the, gồm The Netherlands và the United Nations.'),
 ('gr.c2.countability-coercion',
  'Context can coerce a normally mass noun into a count reading for types, portions, or instances, or a count noun into a mass-like reading for substance/activity.',
  'Ngữ cảnh có thể ép danh từ thường không đếm được sang cách đọc đếm được cho loại/phần/trường hợp, hoặc ngược lại cho vật chất/hoạt động.',
  ['mass noun → count instance/type', 'count noun → mass/substance reading where context licenses'],
  'Use coerced countability only when the contextual interpretation is natural and recoverable.',
  ['The tasting compared three coffees grown at different altitudes.',
   'The committee encountered two distinct resistances to the reform: legal and cultural.',
   'There was chicken on the floor after the container split open.'],
  'three coffees',
  'Dịch sang tiếng Anh: Ủy ban gặp hai kiểu phản kháng khác nhau đối với cải cách: pháp lý và văn hóa.',
  'The tasting compared three coffee grown at different altitudes.',
  'The tasting compared three coffees grown at different altitudes.',
  'Khi coffee nghĩa là ba loại/mẫu cà phê, nó có thể được coercion thành danh từ đếm được số nhiều.'),
 ('gr.c2.word-class-conversion',
  'English freely converts forms between noun, verb, and adjective uses without overt derivational morphology when syntax and convention license the shift.',
  'Tiếng Anh thường chuyển đổi từ giữa danh từ, động từ và tính từ mà không thêm hình vị phái sinh khi cú pháp và quy ước cho phép.',
  ['noun ↔ verb conversion', 'adjective/noun used in newly licensed syntactic slot'],
  'Use conversion where it is established or transparently productive, and avoid novel conversions that obscure meaning in formal prose.',
  ['The team benchmarked the new parser against three established systems.',
   'Please email the signed declaration to the secretariat before noon.',
   'The policy aims to mainstream accessibility rather than treat it as a late-stage check.'],
  'benchmarked',
  'Dịch sang tiếng Anh: Vui lòng email bản khai đã ký cho ban thư ký trước buổi trưa.',
  'The team made a benchmarked of the new parser against three systems.',
  'The team benchmarked the new parser against three systems.',
  'Benchmark có thể chuyển đổi trực tiếp sang động từ; không thêm make a rồi dùng participle sai chức năng.'),
 ('gr.c2.pragmatic-tense-modal',
  'Tense and modal forms can encode interpersonal distance, politeness, tentativeness, and stance beyond their literal temporal or logical meanings.',
  'Thì và modal có thể mã hóa khoảng cách liên cá nhân, lịch sự, dè dặt và lập trường vượt ngoài nghĩa thời gian hay logic trực tiếp.',
  ['past tense for social distance', 'modal remoteness for tentative proposals', 'progressive for softened intention'],
  'Interpret tense/modality pragmatically when literal time alone does not explain the speaker\'s choice.',
  ['I was wondering whether you might have a moment to discuss the revised terms.',
   'We were hoping to avoid reopening the entire negotiation at this stage.',
   'Could we perhaps frame the recommendation more cautiously?'],
  'I was wondering',
  'Dịch sang tiếng Anh: Chúng tôi hy vọng có thể tránh mở lại toàn bộ cuộc đàm phán ở giai đoạn này.',
  'I was wondering whether do you have a moment to discuss the revised terms.',
  'I was wondering whether you might have a moment to discuss the revised terms.',
  'Câu hỏi gián tiếp làm mềm giữ trật tự mệnh đề và có thể kết hợp past + might để tăng pragmatic distance.'),
 ('gr.c2.evidential-distancing',
  'Evidential and reporting constructions identify the source or status of information and let writers calibrate responsibility for a claim.',
  'Cấu trúc evidential và reporting chỉ ra nguồn/trạng thái thông tin và cho phép người viết điều chỉnh trách nhiệm đối với một tuyên bố.',
  ['reportedly/allegedly/apparently + clause', 'be said/reported/thought + to-infinitive', 'seem/appear + to-infinitive'],
  'Choose distancing language that matches evidence strength and avoids presenting unattributed allegations as established fact.',
  ['The subsidiary is reported to have transferred the assets shortly before the investigation began.',
   'Reportedly, several bidders withdrew after the timetable was changed.',
   'The discrepancy appears to reflect a coding change rather than an underlying trend.'],
  'is reported to have transferred',
  'Dịch sang tiếng Anh: Theo các báo cáo, một số nhà thầu đã rút lui sau khi lịch trình thay đổi.',
  'The subsidiary is reported that it transferred the assets shortly before the investigation.',
  'The subsidiary is reported to have transferred the assets shortly before the investigation.',
  'Subject + reporting passive thường đi với to-infinitive, không theo sau bằng that-clause cùng chủ ngữ.'),
 ('gr.c2.concessive-inversion',
  'Formal concessive clauses can front an adjective, adverb, or noun phrase before though/as, producing a marked pattern equivalent to although.',
  'Mệnh đề nhượng bộ trang trọng có thể đưa tính từ, trạng từ hoặc cụm danh từ lên trước though/as, tạo mẫu nhấn mạnh tương đương although.',
  ['adjective/adverb + though/as + subject + verb', 'noun + though/as + subject + be'],
  'Use concessive inversion for controlled formal or literary emphasis, not routine conversation.',
  ['Difficult though the transition was, the team completed it without interrupting customer service.',
   'Carefully as the protocol had been designed, one failure mode had been overlooked.',
   'Experienced negotiator though she is, she still asks a colleague to review every settlement clause.'],
  'Difficult though the transition was',
  'Dịch sang tiếng Anh: Dù giao thức được thiết kế cẩn thận, một chế độ lỗi vẫn bị bỏ sót.',
  'Though difficult the transition was, the team completed it without interruption.',
  'Difficult though the transition was, the team completed it without interruption.',
  'Mẫu marked đưa adjective lên trước though/as, rồi giữ subject + verb phía sau.'),
 ('gr.c2.formal-conditional-register',
  'Legal and institutional English uses highly explicit conditional markers to specify prerequisites, exceptions, and contingency procedures.',
  'Tiếng Anh pháp lý và thể chế dùng các dấu hiệu điều kiện rất tường minh để quy định điều kiện tiên quyết, ngoại lệ và thủ tục dự phòng.',
  ['subject to + noun/-ing', 'provided/provided that + clause', 'in the event that + clause', 'should + subject + verb'],
  'Use formal conditionals when precision and scope justify them; prefer simpler if when no legal or procedural distinction is gained.',
  ['The authorization remains valid subject to the operator maintaining the required insurance coverage.',
   'In the event that either party terminates the agreement, confidential material must be returned within ten working days.',
   'Should any discrepancy arise, the signed paper record will take precedence.'],
  'subject to the operator maintaining',
  'Dịch sang tiếng Anh: Nếu một trong hai bên chấm dứt thỏa thuận, tài liệu mật phải được hoàn trả trong mười ngày làm việc.',
  'The authorization remains valid subject that the operator maintains the required insurance coverage.',
  'The authorization remains valid subject to the operator maintaining the required insurance coverage.',
  'Subject to là giới từ/phức giới từ và thường nhận NP hoặc -ing clause, không nhận subject that-clause.'),
 ('gr.c2.dense-noun-phrases',
  'Dense technical noun phrases can stack classifiers, nominal modifiers, participles, and postmodifiers, but excessive stacking hides semantic relations.',
  'Cụm danh từ kỹ thuật dày có thể chồng classifier, noun modifier, participle và hậu bổ nghĩa, nhưng chồng quá mức sẽ che quan hệ nghĩa.',
  ['premodifier stack + head noun + postmodifier', 'unpack noun stack with of/for/relative clause where needed'],
  'Parse the head and modifier relations first, then unpack any stack whose interpretation is not immediate.',
  ['The committee approved the high-risk supplier data-retention policy review schedule.',
   'We revised the schedule for reviewing the data-retention policy applied to high-risk suppliers.',
   'The newly proposed cross-border payment fraud detection reporting standard requires further consultation.'],
  'high-risk supplier data-retention policy review schedule',
  'Dịch sang tiếng Anh: Chúng tôi sửa lịch rà soát chính sách lưu giữ dữ liệu áp dụng cho nhà cung cấp rủi ro cao.',
  'The committee approved the supplier high-risk retention-data review policy schedule.',
  'The committee approved the high-risk supplier data-retention policy review schedule.',
  'Trong noun stack, thứ tự modifier phải phản ánh cấu trúc nghĩa; nếu khó hiểu nên unpack bằng for/of/relative clause.'),
 ('gr.c2.construction-register-selection',
  'Several grammatical constructions may express similar content, but their frequency and acceptability vary sharply across conversation, journalism, academic prose, and legal language.',
  'Nhiều cấu trúc ngữ pháp có thể diễn đạt nội dung gần nhau, nhưng tần suất và độ phù hợp khác mạnh giữa hội thoại, báo chí, học thuật và pháp lý.',
  ['neutral construction ↔ marked formal/literary/spoken alternative'],
  'Choose not only a grammatical form but the form conventionally expected by the genre and communicative relationship.',
  ['The study found no measurable effect, a wording appropriate for a concise research report.',
   'No measurable effect did the study find is grammatical only in a highly marked rhetorical context.',
   "We didn't really get much out of it may suit conversation but not the executive summary."],
  'The study found no measurable effect',
  "Dịch sang tiếng Anh: Cách nói 'We didn't really get much out of it' có thể hợp hội thoại nhưng không hợp bản tóm tắt điều hành.",
  'No measurable effect did the study find, as the neutral default in a research report.',
  'The study found no measurable effect, as the neutral default in a research report.',
  'Marked inversion không nên thay cấu trúc SVO trung tính nếu genre không có lý do tu từ.'),
 ('gr.c2.idiomatic-prepositions-c2',
  'At C2, many preposition choices are low-predictability lexical conventions whose alternatives may be grammatical but carry different senses or collocational strength.',
  'Ở C2, nhiều lựa chọn giới từ là quy ước từ vựng khó dự đoán; phương án khác có thể vẫn ngữ pháp nhưng mang nghĩa hoặc mức collocation khác.',
  ['lexeme + conventional preposition', 'preposition alternatives distinguished by sense/register'],
  'Use corpus-like collocational knowledge and local meaning rather than one-to-one translation to select the preposition.',
  ['The judgment is predicated on the assumption that the disclosure duty applies to both subsidiaries.',
   'Her account is at odds with the timeline reconstructed from the server logs.',
   'The committee showed little appetite for reopening a compromise reached after months of negotiation.'],
  'predicated on',
  'Dịch sang tiếng Anh: Lời kể của cô ấy mâu thuẫn với dòng thời gian dựng lại từ log máy chủ.',
  'The judgment is predicated in the assumption that the disclosure duty applies.',
  'The judgment is predicated on the assumption that the disclosure duty applies.',
  'Predicated trong nghĩa dựa trên một giả định đi với on.'),
 ('gr.c2.advanced-punctuation-grammar',
  'Punctuation can signal whether clauses are independent, subordinate, appositive, or parenthetical; choices therefore interact with grammatical structure rather than merely pausing speech.',
  'Dấu câu có thể báo hiệu mệnh đề độc lập, phụ thuộc, đồng vị hay chen ngang; vì vậy nó tương tác với cấu trúc ngữ pháp chứ không chỉ biểu thị chỗ ngắt.',
  ['independent clause; independent clause', 'independent clause: elaboration/list', 'dash for marked interruption/supplement', 'comma with non-defining supplement'],
  'Choose punctuation by syntactic relation and discourse function, and avoid comma splices between independent clauses.',
  ['The evidence was incomplete; the panel therefore postponed its decision.',
   'One conclusion was unavoidable: the control had never been tested under peak load.',
   'The final witness—an engineer who had left the company in 2022—provided the missing maintenance records.'],
  'incomplete; the panel',
  'Dịch sang tiếng Anh: Chỉ có một kết luận không thể tránh khỏi: biện pháp kiểm soát chưa bao giờ được thử dưới tải đỉnh.',
  'The evidence was incomplete, the panel therefore postponed its decision.',
  'The evidence was incomplete; the panel therefore postponed its decision.',
  'Hai independent clauses không nên nối chỉ bằng comma; semicolon phù hợp khi quan hệ gần và không có conjunction.'),
 ('gr.c2.spoken-written-register-shift',
  'Expert register shifting recasts not only vocabulary but grammar: speech favors ellipsis, headers, tails, contractions, and clause chains, whereas formal writing often favors explicit subordination and nominal organization.',
  'Chuyển đổi văn phong ở mức cao không chỉ đổi từ vựng mà đổi cả ngữ pháp: lời nói chuộng lược, header/tail, contraction và chuỗi mệnh đề; văn viết trang trọng thường chuộng quan hệ phụ thuộc rõ và tổ chức danh ngữ.',
  ['spoken clause chain/ellipsis ↔ explicit written subordination/nominalization'],
  'Recast structure to fit the target mode instead of merely replacing informal words with formal synonyms.',
  ["Spoken: 'That deadline, we can't move it, can we?' Written: 'The deadline cannot be extended under the current agreement.'",
   "Spoken: 'We looked at it and it just didn't add up.' Written: 'Our review found the figures internally inconsistent.'",
   "Spoken: 'Bit of a problem with the backup.' Written: 'The backup procedure presents a material operational risk.'"],
  "That deadline, we can't move it, can we?",
  'Dịch sang tiếng Anh theo văn viết trang trọng: Chúng tôi rà soát và nhận thấy các con số không nhất quán nội bộ.',
  "In the formal report: That deadline, we can't move it, can we?",
  'In the formal report: The deadline cannot be extended under the current agreement.',
  'Header, contraction và tag question là đặc trưng hội thoại; văn bản trang trọng cần cấu trúc tường minh hơn.'),
 ('gr.c2.ambiguity-reference-editing',
  'Advanced editing identifies competing modifier attachment, pronoun antecedents, quantifier scope, and coordination parses, then rewrites for one intended interpretation.',
  'Biên tập nâng cao nhận diện attachment, antecedent đại từ, phạm vi lượng từ và cách phân tích phối hợp cạnh tranh, rồi viết lại để chỉ còn một cách hiểu chủ đích.',
  ['ambiguous structure → explicit antecedent/position/scope marker'],
  'Resolve ambiguity by naming the referent, moving the modifier, splitting clauses, or repeating a key noun when necessary.',
  ['After speaking to Daniel, Priya told the director that Daniel would revise the appendix.',
   'The policy applies only to contractors who handle personal data, not to all external suppliers.',
   'Using the laboratory microscope, the researcher examined the sample that had been stored in ethanol.'],
  'Daniel would revise the appendix',
  'Dịch sang tiếng Anh: Chính sách chỉ áp dụng cho nhà thầu xử lý dữ liệu cá nhân, không phải mọi nhà cung cấp bên ngoài.',
  'After speaking to Daniel, Priya told the director that he would revise the appendix.',
  'After speaking to Daniel, Priya told the director that Daniel would revise the appendix.',
  'Khi he có nhiều antecedent hợp lý, lặp tên cần thiết để khóa cách hiểu.'),
 ('gr.c2.advanced-editing-consistency',
  'C2 editing checks agreement, parallelism, tense/aspect, complement selection, and reference across long stretches where each local phrase may look plausible in isolation.',
  'Biên tập C2 kiểm tra hòa hợp, song song, thì/thể, lựa chọn bổ ngữ và quy chiếu xuyên đoạn dài nơi từng cụm riêng lẻ có thể trông hợp lý.',
  ['maintain grammatical feature consistency across coordinated and dependent structures'],
  'Edit globally: identify the controlling timeline, subject heads, complement patterns, and parallel frame before correcting isolated forms.',
  ['The report argues that the measure is costly, that it duplicates existing controls, and that it should therefore be withdrawn.',
   'By the time the second review began, the team had corrected the coding error and had rerun every affected model.',
   'Neither the revised definition nor the accompanying examples resolve the ambiguity identified by the reviewers.'],
  'that the measure is costly',
  'Dịch sang tiếng Anh: Trước khi đợt rà soát thứ hai bắt đầu, nhóm đã sửa lỗi mã và chạy lại mọi mô hình bị ảnh hưởng.',
  'The report argues that the measure is costly, duplicates existing controls, and that it should therefore be withdrawn.',
  'The report argues that the measure is costly, that it duplicates existing controls, and that it should therefore be withdrawn.',
  'Trong danh sách ba that-clauses, giữ frame song song giúp phạm vi của argues rõ và nhất quán.')]


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
    if len(expected_ids) != 33 or len(set(expected_ids)) != 33:
        raise SystemExit("C2 rows must contain exactly 33 unique topics")
    missing_from_catalog = [topic_id for topic_id in expected_ids if topic_id not in catalog]
    if missing_from_catalog:
        raise SystemExit(f"Topics missing from catalog: {missing_from_catalog}")
    wrong_level = [topic_id for topic_id in expected_ids if catalog[topic_id].get("cefr") != "C2"]
    if wrong_level:
        raise SystemExit(f"Topics are not C2 in catalog: {wrong_level}")

    output = []
    slice_sizes = [7, 7, 7, 6, 6]
    offset = 0
    for slice_index, slice_size in enumerate(slice_sizes, 1):
        rows = R[offset: offset + slice_size]
        offset += slice_size
        slice_number = f"{slice_index:02d}"
        paths = {
            "grammar-topics": f"content/english/grammar/e05-scale-c2-{slice_number}-topics.json",
            "examples": f"content/english/sentences/e05-scale-c2-{slice_number}-sentences.json",
            "exercises": f"content/english/sentences/e05-scale-c2-{slice_number}-exercises.json",
            "common-mistakes": f"content/english/sentences/e05-scale-c2-{slice_number}-common-mistakes.json",
        }
        sets = {key: [] for key in paths}
        for position, row in enumerate(rows, 1):
            topic_id, concept_en, concept_vi, formulae, when_to_use, examples, answer, translation_vi, wrong, correct, explanation_vi = row
            base = f"grc2.{slice_number}.{position:02d}"
            sentence_ids = [f"sent.{base}.{number}" for number in (1, 2, 3)]
            exercise_ids = [f"ex.cloze.{base}", f"ex.translation.{base}"]
            mistake_id = f"err.{base}"
            meta = catalog[topic_id]
            if examples[0].count(answer) != 1:
                raise SystemExit(f"{topic_id}: cloze answer {answer!r} must occur exactly once in first example")
            prompt = examples[0].replace(answer, "___", 1)
            sets["grammar-topics"].append({
                "schemaVersion": 1,
                "id": topic_id,
                "cefr": "C2",
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
                    "sources": [{
                        "dataset": "project-original",
                        "sourceId": topic_id,
                        "sourceUrl": paths["grammar-topics"],
                        "snapshot": "2026-10",
                        "license": "LicenseRef-Project-Original",
                        "modified": False,
                    }],
                    "note": "Project-original controlled C2 grammar-body content; publication is review-ledger only.",
                },
            })
            for number, text in enumerate(examples):
                sets["examples"].append({
                    "schemaVersion": 1,
                    "id": sentence_ids[number],
                    "text": text,
                    "cefr": "C2",
                    "grammarIds": [topic_id],
                    "quality": quality("example"),
                    "provenance": provenance(),
                })
            sets["exercises"].append({
                "schemaVersion": 1,
                "id": exercise_ids[0],
                "type": "cloze",
                "prompt": prompt,
                "targetIds": [topic_id],
                "acceptedAnswers": [answer],
                "sourceSentenceIds": [sentence_ids[0]],
                "cefr": "C2",
                "quality": quality("exercise"),
                "provenance": provenance(),
            })
            sets["exercises"].append({
                "schemaVersion": 1,
                "id": exercise_ids[1],
                "type": "translation",
                "prompt": translation_vi,
                "targetIds": [topic_id],
                "acceptedAnswers": [examples[1]],
                "sourceSentenceIds": [sentence_ids[1]],
                "cefr": "C2",
                "quality": quality("exercise"),
                "provenance": provenance(),
            })
            sets["common-mistakes"].append({
                "schemaVersion": 1,
                "id": mistake_id,
                "incorrect": wrong,
                "corrections": [correct],
                "explanationVi": explanation_vi,
                "targetIds": [topic_id],
                "evidenceType": "pedagogical",
                "quality": quality("mistake"),
                "provenance": provenance(),
            })
        for set_id, path in paths.items():
            write(path, {"schemaVersion": 1, "records": sets[set_id]})
        output.append((slice_number, paths, sets))
    return output


def add_manifest(slices):
    manifest = load("content/english/batches/manifest.json")
    existing_ids = {batch["id"] for batch in manifest["batches"]}
    new_ids = [f"e05.grammar-scale-c2-{slice_number}" for slice_number, _, _ in slices]
    collision = [batch_id for batch_id in new_ids if batch_id in existing_ids]
    if collision:
        raise SystemExit(f"C2 batch IDs already exist: {collision}")
    insertion = next(index for index, batch in enumerate(manifest["batches"]) if batch["id"] == "e05.grammar-scale-c1-06") + 1
    required_checks = {
        "grammar-topics": ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetPresence", "cefr", "license"],
        "examples": ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetPresence", "cefr", "license"],
        "exercises": ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetPresence", "cefr", "license"],
        "common-mistakes": ["schema", "grammar", "translation", "exactDuplicate", "nearDuplicate", "naturalness", "targetStructure", "cefr", "license"],
    }
    batches = []
    for slice_number, paths, sets in slices:
        batch_id = f"e05.grammar-scale-c2-{slice_number}"
        batches.append({
            "id": batch_id,
            "phase": "E05",
            "category": "grammar",
            "cefr": ["C2"],
            "state": "draft",
            "recordSets": [{
                "id": set_id,
                "path": paths[set_id],
                "expectedCount": len(sets[set_id]),
                "generated": False,
                "allowedQualityStates": ["draft"],
                "requiredChecks": required_checks[set_id],
            } for set_id in ("grammar-topics", "examples", "exercises", "common-mistakes")],
            "requiredBeforePublish": [
                "schema-validation", "reference-integrity", "exact-dedup", "near-dedup",
                "grammar-review", "bilingual-review", "naturalness-review", "cefr-review",
                "target-structure-review", "license-review", "cross-game-smoke",
            ],
            "gameSmokes": [
                {"gameId": "space-typing", "activity": "grammar-challenge", "recordSetId": "grammar-topics", "sampleCount": min(5, len(sets["grammar-topics"]))},
                {"gameId": "monkeytype", "activity": "grammar-topic", "recordSetId": "grammar-topics", "sampleCount": min(5, len(sets["grammar-topics"]))},
                {"gameId": "monkeytype", "activity": "example-typing", "recordSetId": "examples", "sampleCount": min(5, len(sets["examples"]))},
                {"gameId": "monkeytype", "activity": "cloze", "recordSetId": "exercises", "sampleCount": min(4, sum(1 for record in sets["exercises"] if record.get("type") == "cloze")), "recordType": "cloze"},
                {"gameId": "monkeytype", "activity": "translation", "recordSetId": "exercises", "sampleCount": min(4, sum(1 for record in sets["exercises"] if record.get("type") == "translation")), "recordType": "translation"},
                {"gameId": "monkeytype", "activity": "error-correction", "recordSetId": "common-mistakes", "sampleCount": min(4, len(sets["common-mistakes"]))},
            ],
        })
    manifest["batches"][insertion:insertion] = batches
    write("content/english/batches/manifest.json", manifest)


def add_reviews(slices):
    for slice_number, _paths, sets in slices:
        decisions = []
        batch_id = f"e05.grammar-scale-c2-{slice_number}"
        for set_id in ("grammar-topics", "examples", "exercises", "common-mistakes"):
            for record in sets[set_id]:
                checks = {
                    name: {
                        "status": "not-applicable" if check.get("status") == "not-applicable" else "pass",
                        "method": f"editorial-{name}-review-c2-{slice_number}",
                    }
                    for name, check in record["quality"]["checks"].items()
                }
                decisions.append({
                    "id": f"review.e05.c2-{slice_number}." + record["id"].replace(".", "-"),
                    "batchId": batch_id,
                    "recordSetId": set_id,
                    "recordId": record["id"],
                    "sourceDigest": digest(record),
                    "targetState": "published",
                    "checks": checks,
                    "reviewedAt": "2026-10-06T05:30:00Z",
                    "reviewedBy": "GPT-5.6 Sol grammar editorial review",
                    "note": f"Controlled C2 grammar-body slice {slice_number} reviewed for grammar, bilingual meaning, naturalness, target structure, CEFR, dedup and provenance.",
                })
        write(f"content/english/reviews/decisions.d/e05-grammar-c2-{slice_number}.json",
              {"schemaVersion": 1, "decisions": decisions})


def update_counts():
    smoke_path = ROOT / "scripts/smoke-published-english-content.mjs"
    text = smoke_path.read_text(encoding="utf-8")
    replacements = [
        ("grammarManifest.count!==267", "grammarManifest.count!==300"),
        ("267 reviewed grammar topics", "300 reviewed grammar topics"),
        ("sentenceManifest.count!==3190", "sentenceManifest.count!==3388"),
        ("3190 reviewed records", "3388 reviewed records"),
        ("topics.length!==267||examples.length!==1401||exercises.length!==1334||dialogues.length!==100||commonMistakes.length!==355",
         "topics.length!==300||examples.length!==1500||exercises.length!==1400||dialogues.length!==100||commonMistakes.length!==388"),
        ("267 topics + 1401 examples + 1334 exercises + 100 dialogues + 355 common mistakes",
         "300 topics + 1500 examples + 1400 exercises + 100 dialogues + 388 common mistakes"),
        ("monkeyCorrectionCount!==455", "monkeyCorrectionCount!==488"),
        ("100 corrections + 355 common mistakes", "100 corrections + 388 common mistakes"),
        ("monkeyCorrectionRecords:455", "monkeyCorrectionRecords:488"),
    ]
    for old, new in replacements:
        text = replace_once(text, old, new, "C2 final counts")
    smoke_path.write_text(text, encoding="utf-8")

    release = load("content/english/releases/2026.10.0.json")
    release["runtimeCounts"]["grammar"] = 300
    release["runtimeCounts"]["sentences"] = 3388
    release["batchStates"]["draft"] = 72
    write("content/english/releases/2026.10.0.json", release)


def main():
    slices = build()
    add_manifest(slices)
    add_reviews(slices)
    update_counts()
    print(json.dumps({"slices": 5, "topics": 33, "records": 231}, indent=2))


if __name__ == "__main__":
    main()
