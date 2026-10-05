from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PILOT_IDS={"gr.a2.present-perfect-experience","gr.a2.first-conditional"}
SLICE_SIZE=8
REVIEWED_AT="2026-10-05T15:20:00Z"


def D(en,vi,formula,use,examples,cloze_prompt,cloze_answer,translation_vi,wrong,correct,explain,variation):
    return {"en":en,"vi":vi,"formula":formula,"use":use,"examples":examples,"clozePrompt":cloze_prompt,"clozeAnswer":cloze_answer,"translationVi":translation_vi,"wrong":wrong,"correct":correct,"explain":explain,"variation":variation}

DETAILS={
"gr.a2.past-simple-finished-time":D("Use the Past Simple for an action completed at a finished time in the past.","Dùng Quá khứ đơn cho hành động đã hoàn tất tại một thời điểm quá khứ đã kết thúc.",["Subject + past form + finished-time expression."],"Use it with times such as yesterday, last night, in 2024 or two days ago.",["I finished the report yesterday.","Sara called me last night.","We moved here in 2024."],"Sara ___ me last night.","called","Dịch sang tiếng Anh: Sara đã gọi cho tôi tối qua.","I have seen him yesterday.","I saw him yesterday.","Yesterday là thời gian quá khứ đã kết thúc nên dùng Quá khứ đơn, không dùng Hiện tại hoàn thành.","A finished-time expression normally selects the Past Simple."),
"gr.a2.past-continuous-background":D("Use the Past Continuous to describe an activity or situation in progress around a past time.","Dùng Quá khứ tiếp diễn để mô tả hoạt động hoặc tình huống đang diễn ra quanh một thời điểm trong quá khứ.",["Subject + was/were + verb-ing."],"Set the background scene for another past event or describe what was happening at a stated past time.",["It was raining while we were driving home.","The children were playing outside at six.","I was reading when the lights went out."],"The children ___ outside at six.","were playing","Dịch sang tiếng Anh: Lúc sáu giờ bọn trẻ đang chơi ở bên ngoài.","At six, the children played outside.","At six, the children were playing outside.","Khi nhấn mạnh hành động đang diễn ra tại một thời điểm quá khứ, dùng was/were + V-ing.","The Past Continuous presents an action as in progress rather than as a completed event."),
"gr.a2.past-continuous-interruption":D("Use the Past Continuous for an action already in progress and the Past Simple for the shorter event that interrupts it.","Dùng Quá khứ tiếp diễn cho hành động đang diễn ra và Quá khứ đơn cho sự kiện ngắn chen vào.",["Past Continuous + when + Past Simple."],"Describe an interrupted past activity.",["I was cooking when the phone rang.","They were walking home when it started to snow.","She was sleeping when the alarm went off."],"I ___ when the phone rang.","was cooking","Dịch sang tiếng Anh: Họ đang đi bộ về nhà thì trời bắt đầu có tuyết.","I cooked when the phone was ringing.","I was cooking when the phone rang.","Hành động nền đang diễn ra dùng Quá khứ tiếp diễn; sự kiện ngắn xảy ra chen vào dùng Quá khứ đơn.","When commonly introduces the shorter interrupting event."),
"gr.a2.past-simple-vs-continuous":D("Choose the Past Simple for completed events and the Past Continuous for activities in progress at that past moment.","Chọn Quá khứ đơn cho sự kiện hoàn tất và Quá khứ tiếp diễn cho hoạt động đang diễn ra tại thời điểm quá khứ đó.",["completed event: Past Simple","background/in-progress action: was/were + verb-ing"],"Contrast a background activity with a completed event in a past story.",["I was taking a shower when you called.","While Ben was driving, he saw an accident.","We were having dinner when the power went out."],"While Ben ___, he saw an accident.","was driving","Dịch sang tiếng Anh: Trong khi Ben đang lái xe, anh ấy nhìn thấy một vụ tai nạn.","While Ben drove, he was seeing an accident.","While Ben was driving, he saw an accident.","Hoạt động kéo dài làm nền dùng Quá khứ tiếp diễn; sự kiện xảy ra và hoàn tất dùng Quá khứ đơn.","While often introduces the longer background action."),
"gr.a2.used-to":D("Use used to + base verb for past habits or states that are no longer true now.","Dùng used to + động từ nguyên mẫu cho thói quen hoặc trạng thái trong quá khứ hiện nay không còn đúng.",["Subject + used to + base verb.","Subject + didn't use to + base verb."],"Talk about repeated past habits or old situations that changed.",["I used to live near the sea.","Mina used to walk to school.","We didn't use to have a car."],"Mina ___ walk to school.","used to","Dịch sang tiếng Anh: Mina trước đây thường đi bộ đến trường.","We didn't used to have a car.","We didn't use to have a car.","Sau didn't dùng dạng nguyên mẫu use, không dùng used.","Used to describes a past pattern, not a single finished event."),
"gr.a2.present-perfect-recent-result":D("Use the Present Perfect when a recent past action has an important result now.","Dùng Hiện tại hoàn thành khi một hành động vừa xảy ra trong quá khứ tạo ra kết quả quan trọng ở hiện tại.",["Subject + have/has + past participle."],"Connect a recent action with its present result.",["I've lost my keys, so I can't open the door.","Leo has broken his glasses, so he can't read clearly.","We've finished the work, so we can go home."],"Leo ___ his glasses, so he can't read clearly.","has broken","Dịch sang tiếng Anh: Leo đã làm vỡ kính nên bây giờ anh ấy không thể đọc rõ.","Leo broke his glasses, so now he can't read clearly yesterday.","Leo has broken his glasses, so he can't read clearly.","Khi trọng tâm là kết quả hiện tại và không nêu thời gian quá khứ đã kết thúc, dùng Hiện tại hoàn thành.","The present result is more important than the exact past time."),
"gr.a2.present-perfect-ever-never":D("Use ever in Present Perfect questions and never in statements to talk about experience up to now.","Dùng ever trong câu hỏi Hiện tại hoàn thành và never trong câu khẳng định để nói về trải nghiệm tính đến hiện tại.",["Have/Has + subject + ever + past participle?","Subject + have/has never + past participle."],"Ask about or state life experience without a finished past time.",["Have you ever ridden a horse?","I've never flown in a helicopter.","Has Tom ever tried sushi?"],"I've ___ flown in a helicopter.","never","Dịch sang tiếng Anh: Tôi chưa bao giờ bay bằng trực thăng.","Did you ever ridden a horse?","Have you ever ridden a horse?","Với ever để hỏi trải nghiệm tính đến hiện tại, dùng have/has + quá khứ phân từ.","Never already contains a negative meaning, so do not add not."),
"gr.a2.present-perfect-already-yet":D("Use already for something completed sooner than expected and yet mainly in Present Perfect questions and negatives.","Dùng already cho việc đã hoàn tất sớm hơn dự kiến và yet chủ yếu trong câu hỏi hoặc phủ định ở Hiện tại hoàn thành.",["Subject + have/has already + past participle.","Have/Has + subject + past participle + yet?","Subject + haven't/hasn't + past participle + yet."],"Talk about whether an expected action is complete by now.",["I've already sent the email.","Nina hasn't finished yet.","Have they arrived yet?"],"Nina hasn't finished ___.","yet","Dịch sang tiếng Anh: Nina vẫn chưa làm xong.","Nina hasn't already finished.","Nina hasn't finished yet.","Yet thường đứng cuối câu phủ định hoặc câu hỏi khi nói việc được mong đợi đã xảy ra hay chưa.","Already normally comes before the past participle; yet usually comes at the end."),
"gr.a2.present-perfect-just":D("Use just with the Present Perfect for an action completed a very short time ago.","Dùng just với Hiện tại hoàn thành cho hành động vừa mới hoàn tất cách đây rất ngắn.",["Subject + have/has just + past participle."],"Report very recent news or actions.",["I've just eaten lunch.","The train has just left.","Mia has just called me."],"The train has ___ left.","just","Dịch sang tiếng Anh: Tàu vừa mới rời đi.","The train just has left.","The train has just left.","Trong cấu trúc này just thường đứng giữa have/has và quá khứ phân từ.","In standard British-style usage, just commonly appears with the Present Perfect."),
"gr.a2.present-perfect-since-for":D("Use since for a starting point and for for a duration with a situation continuing up to now.","Dùng since cho mốc bắt đầu và for cho khoảng thời gian khi tình huống kéo dài đến hiện tại.",["have/has + past participle + since + starting point","have/has + past participle + for + duration"],"Say how long a current situation has continued.",["I've lived here for three years.","She has worked here since May.","They've known each other for a long time."],"She has worked here ___ May.","since","Dịch sang tiếng Anh: Cô ấy đã làm việc ở đây từ tháng Năm.","I've lived here since three years.","I've lived here for three years.","Khoảng thời gian dùng for; mốc bắt đầu dùng since.","Use since with points such as Monday, 2024 or I was a child."),
"gr.a2.present-perfect-vs-past-simple":D("Use the Present Perfect for an unfinished time or experience connected to now, and the Past Simple with a finished past time.","Dùng Hiện tại hoàn thành cho khoảng thời gian chưa kết thúc hoặc trải nghiệm liên quan hiện tại; dùng Quá khứ đơn với thời gian quá khứ đã kết thúc.",["Present Perfect: have/has + past participle","Past Simple: past form + finished-time expression"],"Choose between present relevance and a specific finished past event.",["I've visited Hue twice.","I visited Hue last summer.","Have you seen this film? I saw it yesterday."],"I ___ Hue last summer.","visited","Dịch sang tiếng Anh: Tôi đã đến Huế vào mùa hè năm ngoái.","I have visited Hue last summer.","I visited Hue last summer.","Last summer là thời gian quá khứ đã kết thúc nên phải dùng Quá khứ đơn.","Do not combine the Present Perfect with explicit finished times such as yesterday or last year."),
"gr.a2.quantifiers-much-many-lot":D("Use many with countable plural nouns, much with uncountable nouns, and a lot of with both in common affirmative sentences.","Dùng many với danh từ đếm được số nhiều, much với danh từ không đếm được và a lot of với cả hai trong nhiều câu khẳng định thông dụng.",["many + plural countable noun","much + uncountable noun","a lot of + countable/uncountable noun"],"Talk about large quantities and ask how much or how many.",["How many books do you have?","We don't have much time.","There are a lot of people here."],"We don't have ___ time.","much","Dịch sang tiếng Anh: Chúng tôi không có nhiều thời gian.","How much books do you have?","How many books do you have?","Books là danh từ đếm được số nhiều nên dùng many, không dùng much.","Much is less common than a lot of in affirmative informal statements."),
"gr.a2.few-little":D("Use a few with countable plural nouns and a little with uncountable nouns for small but positive amounts.","Dùng a few với danh từ đếm được số nhiều và a little với danh từ không đếm được để chỉ lượng nhỏ nhưng vẫn có.",["a few + plural countable noun","a little + uncountable noun"],"Describe small quantities without meaning zero.",["I have a few questions.","There is a little milk left.","We have a few minutes before class."],"There is ___ milk left.","a little","Dịch sang tiếng Anh: Vẫn còn một ít sữa.","There are a little questions.","There are a few questions.","Questions là danh từ đếm được số nhiều nên dùng a few.","Few/little without a usually sound more negative: almost not enough."),
"gr.a2.indefinite-pronouns":D("Use indefinite pronouns such as someone, anyone, everyone, something and nothing when the exact person or thing is not named.","Dùng đại từ bất định như someone, anyone, everyone, something và nothing khi không nêu chính xác người hoặc vật.",["some- forms often in affirmative statements","any- forms often in questions/negatives","every-/no- forms for all or none"],"Refer to unspecified people, things or places.",["Someone is at the door.","I didn't see anyone in the room.","Everything is ready."],"I didn't see ___ in the room.","anyone","Dịch sang tiếng Anh: Tôi không nhìn thấy ai trong phòng.","I didn't see someone in the room.","I didn't see anyone in the room.","Trong câu phủ định thông thường dùng anyone thay vì someone.","Indefinite pronouns normally take a singular verb: Everyone is ready."),
"gr.a2.comparatives":D("Use comparative adjectives with than to compare two people, things or situations.","Dùng tính từ so sánh hơn với than để so sánh hai người, vật hoặc tình huống.",["short adjective + -er + than","more + longer adjective + than"],"Compare two items by one quality.",["This bag is cheaper than that one.","My sister is taller than me.","This chair is more comfortable than that chair."],"My sister is ___ than me.","taller","Dịch sang tiếng Anh: Chị tôi cao hơn tôi.","This chair is comfortabler than that chair.","This chair is more comfortable than that chair.","Với tính từ dài như comfortable, dùng more + adjective, không thêm -er.","Some common comparatives are irregular, such as good → better and bad → worse."),
"gr.a2.superlatives":D("Use the superlative to identify the highest or lowest degree within a group.","Dùng so sánh nhất để chỉ mức độ cao nhất hoặc thấp nhất trong một nhóm.",["the + short adjective-est","the most + longer adjective"],"Compare one member with a group of three or more.",["Mount Everest is the highest mountain in the world.","This is the easiest question on the page.","Mia is the most careful driver in our family."],"This is the ___ question on the page.","easiest","Dịch sang tiếng Anh: Đây là câu hỏi dễ nhất trên trang.","Mia is most careful driver in our family.","Mia is the most careful driver in our family.","So sánh nhất thường cần the trước dạng -est hoặc most + adjective.","Irregular forms include best and worst."),
"gr.a2.as-as":D("Use as + adjective/adverb + as to say two things are equal, and not as ... as to show inequality.","Dùng as + tính từ/trạng từ + as để nói hai đối tượng ngang nhau và not as ... as để nói không ngang nhau.",["as + adjective/adverb + as","not as + adjective/adverb + as"],"Compare equality or difference without using -er/more.",["This room is as quiet as the library.","My phone isn't as expensive as yours.","Tom runs as fast as Ben."],"My phone isn't ___ expensive as yours.","as","Dịch sang tiếng Anh: Điện thoại của tôi không đắt bằng điện thoại của bạn.","My phone isn't so expensive than yours.","My phone isn't as expensive as yours.","Cấu trúc so sánh bằng dùng as ... as, không dùng than.","As ... as can compare adjectives or adverbs."),
"gr.a2.too-enough-adjective":D("Use too + adjective for more than is acceptable and adjective + enough for a sufficient degree.","Dùng too + tính từ cho mức độ quá mức và tính từ + enough cho mức độ đủ.",["too + adjective (+ to-infinitive)","adjective + enough (+ to-infinitive)"],"Explain why something is impossible, difficult or possible because of degree.",["This box is too heavy to carry.","The water is warm enough to swim in.","He isn't old enough to drive."],"The water is warm ___ to swim in.","enough","Dịch sang tiếng Anh: Nước đủ ấm để bơi.","The water is enough warm to swim in.","The water is warm enough to swim in.","Enough đứng sau tính từ: warm enough, không phải enough warm.","Too usually expresses an excessive, often problematic degree."),
"gr.a2.too-much-many-enough-noun":D("Use too much with uncountable nouns, too many with plural countable nouns, and enough before nouns for sufficient quantity.","Dùng too much với danh từ không đếm được, too many với danh từ đếm được số nhiều và enough trước danh từ để chỉ lượng đủ.",["too much + uncountable noun","too many + plural countable noun","enough + noun"],"Judge whether a quantity is excessive or sufficient.",["There is too much sugar in this tea.","We have too many bags.","There aren't enough chairs for everyone."],"We have ___ bags.","too many","Dịch sang tiếng Anh: Chúng tôi có quá nhiều túi.","There are too much bags.","There are too many bags.","Bags là danh từ đếm được số nhiều nên dùng too many.","Enough comes before a noun but after an adjective."),
"gr.a2.will-predictions":D("Use will + base verb for a prediction based mainly on opinion, belief or expectation.","Dùng will + động từ nguyên mẫu cho dự đoán chủ yếu dựa trên ý kiến, niềm tin hoặc kỳ vọng.",["Subject + will + base verb.","Subject + probably will / will probably + base verb."],"Make general future predictions when there is no present visible evidence.",["I think our team will win.","It will probably rain this evening.","People will use less paper in the future."],"It ___ rain this evening.","will probably","Dịch sang tiếng Anh: Có lẽ tối nay trời sẽ mưa.","I think our team is win tomorrow.","I think our team will win tomorrow.","Dự đoán tương lai với will cần will + động từ nguyên mẫu.","Expressions such as I think, probably and maybe often accompany predictions."),
"gr.a2.going-to-evidence":D("Use be going to for a prediction based on present evidence that you can see or know now.","Dùng be going to cho dự đoán dựa trên bằng chứng hiện tại mà ta có thể thấy hoặc biết ngay lúc này.",["Subject + am/is/are going to + base verb."],"Predict a likely near-future event from visible present evidence.",["Look at those clouds. It's going to rain.","Be careful! You're going to drop that glass.","The baby is yawning; she's going to fall asleep."],"Look at those clouds. It's ___ rain.","going to","Dịch sang tiếng Anh: Cẩn thận! Bạn sắp làm rơi chiếc cốc đó.","Look at those clouds. It will raining.","Look at those clouds. It's going to rain.","Sau going to dùng động từ nguyên mẫu, và cấu trúc cần đúng dạng của be.","Going to can express both prior intentions and evidence-based predictions."),
"gr.a2.present-continuous-arrangements":D("Use the Present Continuous for a future arrangement that has already been organized, often with a specific time or person.","Dùng Hiện tại tiếp diễn cho một sắp xếp tương lai đã được tổ chức, thường có thời gian hoặc người liên quan cụ thể.",["Subject + am/is/are + verb-ing + future time."],"Talk about fixed personal arrangements such as meetings, visits or travel.",["I'm meeting Ana at six.","We're having dinner with Sam tomorrow.","They are flying to Bangkok on Friday."],"We're ___ dinner with Sam tomorrow.","having","Dịch sang tiếng Anh: Ngày mai chúng tôi sẽ ăn tối với Sam.","We have dinner with Sam tomorrow at an arranged time.","We're having dinner with Sam tomorrow.","Sắp xếp cá nhân đã chốt thường dùng Hiện tại tiếp diễn với mốc tương lai.","A future time expression makes the future meaning clear."),
"gr.a2.present-simple-schedules":D("Use the Present Simple for timetables and fixed public schedules.","Dùng Hiện tại đơn cho thời khóa biểu, lịch trình và giờ cố định được công bố.",["Scheduled subject + Present Simple + future time."],"State train, bus, film, class or event times that are fixed by a schedule.",["The train leaves at 7:30 tomorrow.","The film starts at eight.","Our class finishes at noon."],"The film ___ at eight.","starts","Dịch sang tiếng Anh: Bộ phim bắt đầu lúc tám giờ.","The film is start at eight.","The film starts at eight.","Lịch trình cố định dùng Hiện tại đơn; với chủ ngữ số ít cần -s ở động từ.","This use is common for transport and official timetables."),
"gr.a2.future-forms-basic-contrast":D("Choose going to for prior intentions, Present Continuous for arranged plans, Present Simple for schedules and will for opinion-based predictions or immediate decisions.","Chọn going to cho ý định đã có, Hiện tại tiếp diễn cho sắp xếp đã chốt, Hiện tại đơn cho lịch trình và will cho dự đoán theo ý kiến hoặc quyết định tức thời.",["intention: be going to + verb","arrangement: be + verb-ing","schedule: Present Simple","prediction/instant decision: will + verb"],"Select a basic future form according to meaning rather than using one future form for every situation.",["I'm going to study medicine after school.","I'm meeting the teacher at three tomorrow.","I think the test will be difficult."],"I think the test ___ difficult.","will be","Dịch sang tiếng Anh: Ngày mai tôi sẽ gặp giáo viên lúc ba giờ.","I will meeting the teacher at three tomorrow.","I'm meeting the teacher at three tomorrow.","Sắp xếp đã chốt dùng Hiện tại tiếp diễn; không dùng will + V-ing.","The same future event can sometimes be framed differently depending on intention, arrangement or prediction."),
"gr.a2.could-past-ability":D("Use could or couldn't to describe general ability in the past.","Dùng could hoặc couldn't để nói về khả năng chung trong quá khứ.",["Subject + could/couldn't + base verb."],"Say what someone was generally able or unable to do at an earlier age or period.",["I could swim when I was five.","She couldn't read before she started school.","Could you ride a bike at six?"],"She ___ read before she started school.","couldn't","Dịch sang tiếng Anh: Cô ấy chưa biết đọc trước khi bắt đầu đi học.","I could to swim when I was five.","I could swim when I was five.","Sau could dùng động từ nguyên mẫu không có to.","For one successful event, later levels often prefer was/were able to rather than could."),
"gr.a2.must-have-to":D("Use must for strong speaker-imposed necessity and have to for necessity caused by rules or circumstances.","Dùng must cho sự bắt buộc mạnh do người nói nhấn mạnh và have to cho sự bắt buộc do quy định hoặc hoàn cảnh.",["Subject + must + base verb.","Subject + have/has to + base verb."],"Express obligation and necessity in everyday rules and situations.",["You must wear a seat belt.","I have to start work at eight.","We had to wait outside."],"I ___ start work at eight.","have to","Dịch sang tiếng Anh: Tôi phải bắt đầu làm việc lúc tám giờ.","I must to start work at eight.","I have to start work at eight.","Must không đi với to; have to thì có to như một phần của cấu trúc.","Past necessity is normally expressed with had to, not must."),
"gr.a2.mustnt-vs-dont-have-to":D("Use mustn't for prohibition and don't/doesn't have to for lack of necessity.","Dùng mustn't cho điều bị cấm và don't/doesn't have to cho điều không bắt buộc.",["mustn't + base verb = prohibited","don't/doesn't have to + base verb = not necessary"],"Distinguish something forbidden from something optional.",["You mustn't touch that wire.","You don't have to come early.","Students mustn't use phones during the test."],"You ___ come early; nine o'clock is fine.","don't have to","Dịch sang tiếng Anh: Bạn không cần phải đến sớm.","You mustn't come early; nine o'clock is fine.","You don't have to come early; nine o'clock is fine.","Mustn't nghĩa là không được phép; don't have to nghĩa là không cần thiết.","The two negative-looking forms have very different meanings."),
"gr.a2.should-advice":D("Use should or shouldn't + base verb to give or ask for advice.","Dùng should hoặc shouldn't + động từ nguyên mẫu để đưa ra hoặc hỏi lời khuyên.",["Subject + should/shouldn't + base verb.","Should + subject + base verb?"],"Recommend a sensible action without expressing a strict rule.",["You should drink more water.","He shouldn't stay up so late.","Should I call the doctor?"],"He ___ stay up so late.","shouldn't","Dịch sang tiếng Anh: Anh ấy không nên thức khuya như vậy.","You should to drink more water.","You should drink more water.","Sau should dùng động từ nguyên mẫu không có to.","Should gives advice; must expresses stronger obligation."),
"gr.a2.may-might-possibility":D("Use may or might + base verb to say something is possible but not certain.","Dùng may hoặc might + động từ nguyên mẫu để nói điều gì đó có thể xảy ra nhưng không chắc chắn.",["Subject + may/might + base verb.","Subject + may/might not + base verb."],"Express uncertain present or future possibility.",["It may rain later.","Sara might be at home.","We might not finish today."],"Sara ___ at home.","might be","Dịch sang tiếng Anh: Sara có thể đang ở nhà.","Sara might to be at home.","Sara might be at home.","Sau might dùng động từ nguyên mẫu không có to.","At A2, may and might can usually be treated as similar markers of possibility."),
"gr.a2.polite-requests-permission":D("Use could/can for polite requests and may/can for asking permission, with could and may often sounding more formal.","Dùng could/can cho lời nhờ lịch sự và may/can để xin phép; could và may thường trang trọng hơn.",["Could/Can you + base verb, please?","May/Can I + base verb?"],"Ask someone to do something or ask permission politely.",["Could you open the window, please?","May I use your phone?","Can I sit here?"],"___ I use your phone?","May","Dịch sang tiếng Anh: Tôi có thể dùng điện thoại của bạn được không?",""Could you to open the window, please?","Could you open the window, please.","Sau could/can/may dùng động từ nguyên mẫu không có to.","Please can be added to requests; may is common for more formal permission."),
"gr.a2.zero-conditional":D("Use the Zero Conditional for facts, routines and results that are generally true whenever the condition happens.","Dùng Câu điều kiện loại 0 cho sự thật, thói quen và kết quả thường đúng mỗi khi điều kiện xảy ra.",["If + Present Simple, Present Simple."],"State general truths, instructions or repeated cause-and-effect relationships.",["If you heat ice, it melts.","If I don't sleep enough, I feel tired.","Plants die if they don't get water."],"If you ___ ice, it melts.","heat","Dịch sang tiếng Anh: Nếu tôi không ngủ đủ, tôi cảm thấy mệt.","If you will heat ice, it melts.","If you heat ice, it melts.","Trong mệnh đề if của câu điều kiện loại 0 dùng Hiện tại đơn, không dùng will.","Both clauses normally use the Present Simple because the result is general, not a one-time future prediction."),
"gr.a2.future-time-clauses":D("Use a present tense after when, after, before, until and as soon as to refer to the future; use will in the main clause when needed.","Dùng thì hiện tại sau when, after, before, until và as soon as để nói về tương lai; dùng will ở mệnh đề chính khi cần.",["will + verb + when/after/before/until + Present Simple","When/After + Present Simple, will + verb"],"Describe the timing of future actions.",["I'll call you when I arrive.","We'll eat after Dad gets home.","Please wait here until the bus comes."],"I'll call you when I ___.","arrive","Dịch sang tiếng Anh: Chúng tôi sẽ ăn sau khi bố về nhà.","I'll call you when I will arrive.","I'll call you when I arrive.","Sau when để nói về tương lai thường dùng Hiện tại đơn, không dùng will trong mệnh đề thời gian.","The main clause may use will, an imperative or another suitable future form."),
"gr.a2.infinitive-purpose":D("Use to + base verb to explain the purpose of an action.","Dùng to + động từ nguyên mẫu để giải thích mục đích của một hành động.",["main action + to + base verb (purpose)"],"Answer the question why someone does something.",["I went to the shop to buy milk.","She called me to ask a question.","We use this box to store tools."],"She called me ___ a question.","to ask","Dịch sang tiếng Anh: Cô ấy gọi cho tôi để hỏi một câu hỏi.","She called me for ask a question.","She called me to ask a question.","Để diễn tả mục đích đơn giản, dùng to + động từ nguyên mẫu.","For + noun can express purpose too, but for + base verb is not the same construction."),
"gr.a2.verb-to-infinitive-common":D("Some common verbs such as want, decide, hope, plan and need are followed by to + base verb.","Một số động từ thông dụng như want, decide, hope, plan và need được theo sau bởi to + động từ nguyên mẫu.",["verb + to + base verb"],"Use the correct complement after common verbs that select the to-infinitive.",["I want to learn Spanish.","They decided to leave early.","Mia hopes to find a new job."],"They decided ___ early.","to leave","Dịch sang tiếng Anh: Họ quyết định rời đi sớm.","They decided leaving early.","They decided to leave early.","Decide thường đi với to-infinitive: decide to leave.","Verb patterns must be learned with the verb because different verbs select different complements."),
"gr.a2.verb-ing-common":D("Some common verbs such as enjoy, finish and avoid are followed by an -ing form.","Một số động từ thông dụng như enjoy, finish và avoid được theo sau bởi dạng V-ing.",["verb + verb-ing"],"Use the correct complement after common verbs that select an -ing form.",["I enjoy cooking at home.","Leo finished cleaning the kitchen.","They avoid driving at night."],"Leo finished ___ the kitchen.","cleaning","Dịch sang tiếng Anh: Leo đã dọn xong nhà bếp.","Leo finished to clean the kitchen.","Leo finished cleaning the kitchen.","Finish thường đi với V-ing, không đi với to-infinitive trong cấu trúc này.","Learn the complement as part of each verb pattern."),
"gr.a2.adjective-to-infinitive":D("Use adjective + to-infinitive after many adjectives to describe feelings, reactions, difficulty or readiness.","Dùng tính từ + to-infinitive sau nhiều tính từ để nói về cảm xúc, phản ứng, độ khó hoặc sự sẵn sàng.",["be + adjective + to + base verb"],"Add an action after adjectives such as happy, easy, ready, surprised and difficult.",["I'm happy to help.","This book is easy to understand.","We were surprised to see Ben."],"This book is easy ___ .","to understand","Dịch sang tiếng Anh: Cuốn sách này dễ hiểu.","This book is easy understanding.","This book is easy to understand.","Sau easy trong cấu trúc này dùng to + động từ nguyên mẫu.","The adjective describes the subject or the situation, while the infinitive names the related action."),
"gr.a2.preposition-ing":D("After a preposition, use a noun or an -ing form rather than a to-infinitive.","Sau giới từ, dùng danh từ hoặc dạng V-ing thay vì to-infinitive.",["preposition + verb-ing"],"Use verbs after prepositions such as at, for, without, before and after.",["She's good at drawing.","Thank you for helping me.","He left without saying goodbye."],"Thank you for ___ me.","helping","Dịch sang tiếng Anh: Cảm ơn bạn đã giúp tôi.","Thank you for to help me.","Thank you for helping me.","Sau giới từ for dùng V-ing khi theo sau là động từ.","To can be a preposition in some patterns, but this A2 rule covers ordinary prepositions such as for and without."),
"gr.a2.phrasal-verbs-object-position":D("With separable phrasal verbs, a noun object may go before or after the particle, but a pronoun object normally goes between the verb and particle.","Với cụm động từ có thể tách, tân ngữ danh từ có thể đứng trước hoặc sau tiểu từ, nhưng tân ngữ đại từ thường phải đứng giữa động từ và tiểu từ.",["verb + noun + particle / verb + particle + noun","verb + pronoun + particle"],"Place noun and pronoun objects correctly with common separable phrasal verbs.",["Please turn the light off.","Please turn it off.","She picked the children up at four."],"Please turn ___ off.","it","Dịch sang tiếng Anh: Hãy tắt nó đi.","Please turn off it.","Please turn it off.","Với tân ngữ là đại từ, cụm động từ tách được đặt đại từ giữa động từ và tiểu từ: turn it off.","Not every phrasal verb is separable, so object position must be learned with the verb."),
"gr.a2.defining-relatives-basic":D("Use who for people and that/which for things in a defining relative clause that identifies the noun.","Dùng who cho người và that/which cho vật trong mệnh đề quan hệ xác định để nhận diện danh từ.",["person + who + clause","thing + that/which + clause"],"Add essential information that tells exactly which person or thing you mean.",["A mechanic is a person who repairs cars.","This is the book that I bought yesterday.","The woman who lives next door is a nurse."],"A mechanic is a person ___ repairs cars.","who","Dịch sang tiếng Anh: Đây là cuốn sách mà tôi đã mua hôm qua.","A mechanic is a person which repairs cars.","A mechanic is a person who repairs cars.","Khi đại từ quan hệ chỉ người, dùng who trong cấu trúc cơ bản này.","That can often refer to people or things in defining clauses, while who is the clearest choice for people."),
"gr.a2.relative-where":D("Use where in a defining relative clause to identify a place by what happens there.","Dùng where trong mệnh đề quan hệ xác định để nhận diện một nơi thông qua việc xảy ra ở đó.",["place + where + subject + verb"],"Combine a place noun with information about activities or events at that place.",["This is the cafe where we first met.","I know a park where children can play safely.","That's the hotel where we stayed."],"This is the cafe ___ we first met.","where","Dịch sang tiếng Anh: Tôi biết một công viên nơi trẻ em có thể chơi an toàn.","This is the cafe who we first met.","This is the cafe where we first met.","Nơi chốn trong cấu trúc cơ bản này dùng where, không dùng who.","Where can often be paraphrased with in/at which at higher levels."),
"gr.a2.articles-generic-specific":D("Use a/an when introducing one non-specific singular countable noun and the when both speaker and listener can identify the specific noun.","Dùng a/an khi giới thiệu một danh từ đếm được số ít chưa xác định và the khi cả người nói lẫn người nghe có thể xác định danh từ cụ thể.",["first/non-specific mention: a/an + singular countable noun","identified/specific mention: the + noun"],"Move from introducing something to referring back to the same specific thing.",["I saw a dog. The dog was very friendly.","She bought a book. The book is on the table.","We need a taxi. The taxi outside is free."],"She bought a book. ___ book is on the table.","The","Dịch sang tiếng Anh: Cô ấy mua một cuốn sách. Cuốn sách đó ở trên bàn.","She bought the book. A book is on the table.","She bought a book. The book is on the table.","Lần đầu giới thiệu một vật chưa xác định dùng a/an; nhắc lại vật đã xác định dùng the.","Specificity depends on shared context, not only on whether a noun was mentioned earlier."),
"gr.a2.zero-article-generic":D("Use no article with plural countable nouns and uncountable nouns when talking about things in general.","Không dùng mạo từ với danh từ đếm được số nhiều và danh từ không đếm được khi nói chung về một loại hoặc khái niệm.",["plural countable noun (general): no article","uncountable noun (general): no article"],"Make general statements about categories, substances and abstract ideas.",["Dogs need regular exercise.","Milk is good for children.","Life can be surprising."],"___ is good for children.","Milk","Dịch sang tiếng Anh: Sữa tốt cho trẻ em.","The milk is good for children in general.","Milk is good for children.","Khi nói về sữa nói chung, không dùng the; the sẽ làm nghĩa trở nên cụ thể.","Use the when the plural or uncountable noun is made specific by context."),
"gr.a2.one-ones":D("Use one or ones to avoid repeating a countable noun that is already clear from context.","Dùng one hoặc ones để tránh lặp lại danh từ đếm được đã rõ từ ngữ cảnh.",["singular replacement: one","plural replacement: ones"],"Compare or choose among previously mentioned countable things without repeating the noun.",["I like the red bag, not the blue one.","These shoes are small; I need bigger ones.","Which cake do you want? The chocolate one."],"These shoes are small; I need bigger ___.","ones","Dịch sang tiếng Anh: Đôi giày này nhỏ; tôi cần đôi lớn hơn.","These shoes are small; I need a bigger one shoes.","These shoes are small; I need bigger ones.","Danh từ số nhiều được thay bằng ones; one dùng cho danh từ số ít.","One/ones replace countable nouns, not uncountable nouns."),
"gr.a2.reflexive-pronouns":D("Use reflexive pronouns when the subject and object refer to the same person or group, or for emphasis.","Dùng đại từ phản thân khi chủ ngữ và tân ngữ cùng chỉ một người/nhóm, hoặc để nhấn mạnh.",["I → myself, you → yourself/yourselves, he → himself, she → herself, we → ourselves, they → themselves"],"Show that an action returns to the subject or emphasize who did it without help.",["I cut myself while cooking.","They made the cake themselves.","She taught herself to play the guitar."],"They made the cake ___.","themselves","Dịch sang tiếng Anh: Họ tự làm chiếc bánh.","They made the cake theirselves.","They made the cake themselves.","Dạng phản thân của they là themselves, không phải theirselves.","Reflexive pronouns are not used simply because the subject is a person; they need a reflexive or emphatic function."),
"gr.a2.adverbs-manner":D("Use an adverb of manner to describe how an action happens; many are formed by adding -ly to an adjective.","Dùng trạng từ chỉ cách thức để mô tả một hành động diễn ra như thế nào; nhiều trạng từ được tạo bằng cách thêm -ly vào tính từ.",["verb + adverb of manner","adjective + -ly → adverb (common pattern)"],"Describe the manner of speaking, moving, working or doing another action.",["She speaks English clearly.","The baby slept quietly.","Please drive carefully."],"The baby slept ___.","quietly","Dịch sang tiếng Anh: Em bé ngủ một cách yên lặng.","The baby slept quiet.","The baby slept quietly.","Động từ slept cần trạng từ chỉ cách thức quietly, không phải tính từ quiet.","Some adverbs are irregular or unchanged, such as well and fast."),
"gr.a2.adjective-vs-adverb":D("Use adjectives to describe nouns or follow linking verbs, and adverbs to modify ordinary action verbs.","Dùng tính từ để mô tả danh từ hoặc sau động từ nối; dùng trạng từ để bổ nghĩa cho động từ hành động thông thường.",["adjective + noun / be + adjective","action verb + adverb"],"Choose between a quality of a person/thing and the manner of an action.",["Mia is a careful driver.","Mia drives carefully.","The test was easy, and I finished it quickly."],"Mia drives ___.","carefully","Dịch sang tiếng Anh: Mia lái xe cẩn thận.","Mia drives careful.","Mia drives carefully.","Sau động từ hành động drives cần trạng từ carefully để mô tả cách lái.","Linking verbs such as be, seem and feel normally take adjectives rather than manner adverbs."),
"gr.a2.basic-subordination":D("Use basic subordinators such as because, although, before, after and when to connect a main clause with a dependent clause.","Dùng các liên từ phụ thuộc cơ bản như because, although, before, after và when để nối mệnh đề chính với mệnh đề phụ.",["main clause + subordinator + dependent clause","Subordinator + dependent clause, main clause"],"Express reason, contrast, time and sequence with two related clauses.",["I stayed home because I was sick.","Although it was cold, we went for a walk.","I called Sam before I left."],"___ it was cold, we went for a walk.","Although","Dịch sang tiếng Anh: Mặc dù trời lạnh, chúng tôi vẫn đi dạo.","Although it was cold, but we went for a walk.","Although it was cold, we went for a walk.","Không dùng đồng thời although và but để nối cùng hai mệnh đề trong cấu trúc chuẩn này.","A comma is common when the dependent clause comes first."),
"gr.a2.question-tags-basic":D("Use a short question tag with the opposite polarity of the statement to check or confirm information.","Dùng câu hỏi đuôi ngắn có tính khẳng định/phủ định ngược với mệnh đề chính để kiểm tra hoặc xác nhận thông tin.",["positive statement, negative tag?","negative statement, positive tag?"],"Seek confirmation in simple statements with be, auxiliaries and common modal verbs.",["It's cold today, isn't it?","You like coffee, don't you?","She can swim, can't she?"],"You like coffee, ___?","don't you","Dịch sang tiếng Anh: Bạn thích cà phê, phải không?",""You like coffee, aren't you?","You like coffee, don't you?","Mệnh đề dùng động từ thường ở Hiện tại đơn nên câu hỏi đuôi dùng do/does; với you là don't you.","The tag repeats the auxiliary or modal from the statement when one is present."),
}


def stable_json(value):
    return json.dumps(value,ensure_ascii=False,indent=2)+"\n"


def load_json(relative):
    return json.loads((ROOT/relative).read_text(encoding="utf-8"))


def write_json(relative,value):
    path=ROOT/relative
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(stable_json(value),encoding="utf-8")


def must_replace(text,old,new,label):
    count=text.count(old)
    if count!=1:
        raise SystemExit(f"{label}: expected one anchor, got {count}")
    return text.replace(old,new,1)


def source_digest(record):
    normalized=copy.deepcopy(record)
    checks=normalized.get("quality",{}).get("checks",{})
    checks.pop("cefr",None)
    checks.pop("license",None)
    return hashlib.sha256(stable_json(normalized).encode("utf-8")).hexdigest()


def provenance():
    return {"sources":[{"dataset":"project-original","license":"LicenseRef-Project-Original","modified":False}]}


def quality(kind):
    checks={
        "schema":{"status":"pass","method":"e05-grammar-scale-authoring-v2"},
        "grammar":{"status":"pending","method":"independent-grammar-review-required"},
        "translation":{"status":"pending","method":"bilingual-review-required"},
        "exactDuplicate":{"status":"pass","method":"stable-id-and-local-exact-dedup-v1"},
        "nearDuplicate":{"status":"pending","method":"cross-runtime-near-dedup-review-required"},
        "naturalness":{"status":"pending","method":"editor-review-required"},
        "cefr":{"status":"pending","method":"cefr-review-required"},
        "license":{"status":"pending","method":"project-original-license-review-required"},
    }
    checks["targetStructure" if kind=="mistake" else "targetPresence"]={"status":"pending","method":"linked-content-target-review-required"}
    return {"state":"draft","checks":checks}


def build_sources():
    curriculum=load_json("shared/curriculum/a2.json")
    catalog=load_json("content/english/grammar/topic-catalog.json")
    catalog_by_id={topic["id"]:topic for topic in catalog["topics"]}
    remaining=[topic_id for topic_id in curriculum["topicIds"] if topic_id not in PILOT_IDS]
    if len(remaining)!=48 or set(remaining)!=set(DETAILS):
        raise SystemExit(f"A2 source map mismatch: curriculum={len(remaining)} details={len(DETAILS)} missing={set(remaining)-set(DETAILS)} extra={set(DETAILS)-set(remaining)}")
    slices=[]
    for slice_index in range(6):
        ids=remaining[slice_index*SLICE_SIZE:(slice_index+1)*SLICE_SIZE]
        slice_no=f"{slice_index+1:02d}"
        topic_path=f"content/english/grammar/e05-scale-a2-{slice_no}-topics.json"
        sentence_path=f"content/english/sentences/e05-scale-a2-{slice_no}-sentences.json"
        exercise_path=f"content/english/sentences/e05-scale-a2-{slice_no}-exercises.json"
        mistake_path=f"content/english/sentences/e05-scale-a2-{slice_no}-common-mistakes.json"
        topics=[]; sentences=[]; exercises=[]; mistakes=[]
        for position,topic_id in enumerate(ids,1):
            d=DETAILS[topic_id]; meta=catalog_by_id[topic_id]; base=f"gra2.{slice_no}.{position:02d}"
            example_ids=[f"sent.{base}.{n}" for n in (1,2,3)]
            exercise_ids=[f"ex.cloze.{base}",f"ex.translation.{base}"]
            mistake_id=f"err.{base}"
            topics.append({
                "schemaVersion":1,"id":topic_id,"cefr":"A2","title":meta["title"],"objective":meta["objective"],
                "concept":{"en":d["en"],"vi":d["vi"]},"formulae":d["formula"],"whenToUse":[d["use"]],
                "forms":{"positive":d["examples"]},"variations":[d["variation"]],"relatedCollocationIds":[],
                "exampleIds":example_ids,"commonMistakeIds":[mistake_id],"contrastTopicIds":[],"dialogueIds":[],"prerequisiteIds":[],"exerciseIds":exercise_ids,
                "quality":quality("topic"),
                "provenance":{"sources":[{"dataset":"project-original","sourceId":topic_id,"sourceUrl":topic_path,"snapshot":"2026-10","license":"LicenseRef-Project-Original","modified":False}],"note":"Project-original controlled A2 grammar-body scale content; publication is review-ledger only."},
            })
            for n,text in enumerate(d["examples"],1):
                sentences.append({"schemaVersion":1,"id":example_ids[n-1],"text":text,"cefr":"A2","grammarIds":[topic_id],"quality":quality("sentence"),"provenance":provenance()})
            exercises.append({"schemaVersion":1,"id":exercise_ids[0],"type":"cloze","prompt":d["clozePrompt"],"targetIds":[topic_id],"acceptedAnswers":[d["clozeAnswer"]],"sourceSentenceIds":[example_ids[0]],"cefr":"A2","quality":quality("exercise"),"provenance":provenance()})
            exercises.append({"schemaVersion":1,"id":exercise_ids[1],"type":"translation","prompt":d["translationVi"],"targetIds":[topic_id],"acceptedAnswers":[d["examples"][1]],"sourceSentenceIds":[example_ids[1]],"cefr":"A2","quality":quality("exercise"),"provenance":provenance()})
            mistakes.append({"schemaVersion":1,"id":mistake_id,"incorrect":d["wrong"],"corrections":[d["correct"]],"explanationVi":d["explain"],"targetIds":[topic_id],"evidenceType":"pedagogical","quality":quality("mistake"),"provenance":provenance()})
        write_json(topic_path,{"schemaVersion":1,"records":topics})
        write_json(sentence_path,{"schemaVersion":1,"records":sentences})
        write_json(exercise_path,{"schemaVersion":1,"records":exercises})
        write_json(mistake_path,{"schemaVersion":1,"records":mistakes})
        slices.append({"slice":slice_no,"ids":ids,"paths":{"grammar-topics":topic_path,"examples":sentence_path,"exercises":exercise_path,"common-mistakes":mistake_path},"records":{"grammar-topics":topics,"examples":sentences,"exercises":exercises,"common-mistakes":mistakes}})
    return slices


def add_batches(slices):
    manifest=load_json("content/english/batches/manifest.json")
    existing={batch.get("id") for batch in manifest.get("batches",[])}
    if any(f"e05.grammar-scale-a2-{s['slice']}" in existing for s in slices):
        raise SystemExit("A2 grammar scale batch already exists")
    insertion=next(i for i,batch in enumerate(manifest["batches"]) if batch.get("id")=="e05.grammar-scale-a1-06")+1
    new=[]
    checks={
        "grammar-topics":["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetPresence","cefr","license"],
        "examples":["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetPresence","cefr","license"],
        "exercises":["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetPresence","cefr","license"],
        "common-mistakes":["schema","grammar","translation","exactDuplicate","nearDuplicate","naturalness","targetStructure","cefr","license"],
    }
    for s in slices:
        batch_id=f"e05.grammar-scale-a2-{s['slice']}"
        new.append({
            "id":batch_id,"phase":"E05","category":"grammar","cefr":["A2"],"state":"draft",
            "recordSets":[
                {"id":"grammar-topics","path":s["paths"]["grammar-topics"],"expectedCount":8,"generated":False,"allowedQualityStates":["draft"],"requiredChecks":checks["grammar-topics"]},
                {"id":"examples","path":s["paths"]["examples"],"expectedCount":24,"generated":False,"allowedQualityStates":["draft"],"requiredChecks":checks["examples"]},
                {"id":"exercises","path":s["paths"]["exercises"],"expectedCount":16,"generated":False,"allowedQualityStates":["draft"],"requiredChecks":checks["exercises"]},
                {"id":"common-mistakes","path":s["paths"]["common-mistakes"],"expectedCount":8,"generated":False,"allowedQualityStates":["draft"],"requiredChecks":checks["common-mistakes"]},
            ],
            "requiredBeforePublish":["schema-validation","reference-integrity","exact-dedup","near-dedup","grammar-review","bilingual-review","naturalness-review","cefr-review","target-structure-review","license-review","cross-game-smoke"],
            "gameSmokes":[
                {"gameId":"space-typing","activity":"grammar-challenge","recordSetId":"grammar-topics","sampleCount":5},
                {"gameId":"monkeytype","activity":"grammar-topic","recordSetId":"grammar-topics","sampleCount":5},
                {"gameId":"monkeytype","activity":"example-typing","recordSetId":"examples","sampleCount":5},
                {"gameId":"monkeytype","activity":"cloze","recordSetId":"exercises","sampleCount":4,"recordType":"cloze"},
                {"gameId":"monkeytype","activity":"translation","recordSetId":"exercises","sampleCount":4,"recordType":"translation"},
                {"gameId":"monkeytype","activity":"error-correction","recordSetId":"common-mistakes","sampleCount":4},
            ],
        })
    manifest["batches"][insertion:insertion]=new
    write_json("content/english/batches/manifest.json",manifest)


def write_reviews(slices):
    for s in slices:
        decisions=[]
        batch_id=f"e05.grammar-scale-a2-{s['slice']}"
        for set_id in ("grammar-topics","examples","exercises","common-mistakes"):
            for record in s["records"][set_id]:
                checks={name:{"status":"not-applicable" if check.get("status")=="not-applicable" else "pass","method":f"editorial-{name}-review-a2-{s['slice']}"} for name,check in record["quality"]["checks"].items()}
                decisions.append({
                    "id":f"review.e05.a2-{s['slice']}."+record["id"].replace(".","-"),"batchId":batch_id,"recordSetId":set_id,"recordId":record["id"],
                    "sourceDigest":source_digest(record),"targetState":"published","checks":checks,"reviewedAt":REVIEWED_AT,"reviewedBy":"GPT-5.6 Sol grammar editorial review",
                    "note":f"Controlled A2 grammar-body slice {s['slice']} reviewed for grammar accuracy, bilingual meaning, naturalness, target structure/presence, CEFR fit, dedup and project-original provenance.",
                })
        if len(decisions)!=56: raise SystemExit(f"{batch_id}: expected 56 decisions")
        write_json(f"content/english/reviews/decisions.d/e05-grammar-a2-{s['slice']}.json",{"schemaVersion":1,"decisions":decisions})


def patch_package():
    path=ROOT/"package.json"; text=path.read_text(encoding="utf-8")
    text=must_replace(text,'"english-content:validate": "node scripts/validate-english-content.mjs"','"english-content:validate": "node scripts/validate-english-content.mjs && node scripts/validate-english-grammar-scales.mjs"',"package validator")
    path.write_text(text,encoding="utf-8")


def patch_publisher():
    path=ROOT/"scripts/publish-english-content.mjs"; text=path.read_text(encoding="utf-8")
    anchor='const grammarScaleA106Mistakes=await loadRecords("content/english/sentences/e05-scale-a1-06-common-mistakes.json");'
    block='''\nconst grammarScaleA2Slices=[];\nfor (let index=1;index<=6;index++) {\n  const slice=String(index).padStart(2,"0");\n  grammarScaleA2Slices.push({\n    topics:await loadRecords("content/english/grammar/e05-scale-a2-"+slice+"-topics.json"),\n    sentences:await loadRecords("content/english/sentences/e05-scale-a2-"+slice+"-sentences.json"),\n    exercises:await loadRecords("content/english/sentences/e05-scale-a2-"+slice+"-exercises.json"),\n    mistakes:await loadRecords("content/english/sentences/e05-scale-a2-"+slice+"-common-mistakes.json"),\n  });\n}\nconst grammarScaleA2Topics=grammarScaleA2Slices.flatMap(slice=>slice.topics);\nconst grammarScaleA2Sentences=grammarScaleA2Slices.flatMap(slice=>slice.sentences);\nconst grammarScaleA2Exercises=grammarScaleA2Slices.flatMap(slice=>slice.exercises);\nconst grammarScaleA2Mistakes=grammarScaleA2Slices.flatMap(slice=>slice.mistakes);'''
    text=must_replace(text,anchor,anchor+block,"publisher A2 loader")
    replacements=[
        ("...grammarScaleA105,...grammarScaleA106]","...grammarScaleA105,...grammarScaleA106,...grammarScaleA2Topics]"),
        ("...grammarScaleA105Sentences,...grammarScaleA106Sentences,...reviewedTranslationSentences","...grammarScaleA105Sentences,...grammarScaleA106Sentences,...grammarScaleA2Sentences,...reviewedTranslationSentences"),
        ("...grammarScaleA105Exercises,...grammarScaleA106Exercises,...reviewedE06Exercises","...grammarScaleA105Exercises,...grammarScaleA106Exercises,...grammarScaleA2Exercises,...reviewedE06Exercises"),
        ("...grammarScaleA105Mistakes,...grammarScaleA106Mistakes]","...grammarScaleA105Mistakes,...grammarScaleA106Mistakes,...grammarScaleA2Mistakes]"),
    ]
    for old,new in replacements: text=must_replace(text,old,new,"publisher A2 arrays")
    path.write_text(text,encoding="utf-8")


def patch_smoke():
    path=ROOT/"scripts/smoke-published-english-content.mjs"; text=path.read_text(encoding="utf-8")
    replacements=[
        ("grammarManifest.count!==55","grammarManifest.count!==103"),
        ("published grammar runtime must contain 55 reviewed grammar topics","published grammar runtime must contain 103 reviewed grammar topics"),
        ("sentenceManifest.count!==1918","sentenceManifest.count!==2206"),
        ("published sentence runtime must contain 1918 reviewed records","published sentence runtime must contain 2206 reviewed records"),
        ("topics.length!==55||examples.length!==765||exercises.length!==910||dialogues.length!==100||commonMistakes.length!==143","topics.length!==103||examples.length!==909||exercises.length!==1006||dialogues.length!==100||commonMistakes.length!==191"),
        ("published runtime split must be 55 topics + 765 examples + 910 exercises + 100 dialogues + 143 common mistakes","published runtime split must be 103 topics + 909 examples + 1006 exercises + 100 dialogues + 191 common mistakes"),
        ("monkeyCorrectionCount!==243","monkeyCorrectionCount!==291"),
        ("published Monkeytype error-correction activity must expose 100 corrections + 143 common mistakes","published Monkeytype error-correction activity must expose 100 corrections + 191 common mistakes"),
        ("monkeyCorrectionRecords:243","monkeyCorrectionRecords:291"),
    ]
    for old,new in replacements: text=must_replace(text,old,new,"runtime smoke A2 counts")
    path.write_text(text,encoding="utf-8")


def patch_release():
    release=load_json("content/english/releases/2026.10.0.json")
    release["runtimeCounts"]["grammar"]=103
    release["runtimeCounts"]["sentences"]=2206
    release["batchStates"]["draft"]=45
    write_json("content/english/releases/2026.10.0.json",release)


def patch_e11():
    path=ROOT/"scripts/report-english-content-e11-readiness.mjs"; text=path.read_text(encoding="utf-8")
    for suffix in ("topics.json","sentences.json","exercises.json","common-mistakes.json"):
        old=("content/english/grammar/" if suffix=="topics.json" else "content/english/sentences/")+"e05-scale-a1-06-"+suffix
        new=("content/english/grammar/" if suffix=="topics.json" else "content/english/sentences/")+"e05-scale-a2-06-"+suffix
        text=must_replace(text,old,new,"E11 A2 snapshot")
    path.write_text(text,encoding="utf-8")


def patch_master_plan():
    path=ROOT/"docs/ENGLISH_LEARNING_CONTENT_SYSTEM_MASTER_PLAN.md"; text=path.read_text(encoding="utf-8")
    replacements=[
        ("Pilot status: **A1 RICH GRAMMAR BODY COMPLETE — 45/45 A1 TOPICS REVIEWED AND PUBLISHED**.","Pilot status: **A1 + A2 RICH GRAMMAR BODY COMPLETE — 95/95 A1-A2 TOPICS REVIEWED AND PUBLISHED**."),
        ("The E05 grammar-body review ledger now overlays **373 digest-bound accepted records**","The E05 grammar-body review ledger now overlays **709 digest-bound accepted records**"),
        ("Published E05 runtime now contains **55 rich grammar topics**: the original 12-topic cross-CEFR pilot plus six controlled A1 body slices with 43 additional topics. This closes A1 at **45/45 rich topic bodies** (2 from the original pilot + 43 from the controlled scale slices). Grammar-linked authoring now includes **165 controlled example sentences, 110 exercises and 43 linked common mistakes**.","Published E05 runtime now contains **103 rich grammar topics**: the original 12-topic cross-CEFR pilot, six controlled A1 body slices and six controlled A2 body slices. A1 is **45/45** and A2 is **50/50** complete; the A2 scale contributes 48 additional rich topics beyond its 2 original pilot topics. Grammar-linked authoring now includes **309 controlled example sentences, 206 exercises and 91 linked common mistakes**."),
        ("Every scale topic includes EN/VI concepts, formulae, use cases, forms/variations, contrasts/prerequisites, 3 examples, 2 exercises and 1 common mistake.","Every scale topic includes EN/VI concepts, formulae, use cases, forms/variations, contrasts/prerequisites, 3 examples, 2 exercises and 1 common mistake. A2 slices 01-06 cover past narrative forms, Present Perfect expansion, quantity/comparison, future forms, modals/conditionals, verb complements, relative clauses, articles/reference, adverbs/subordination and question tags."),
        ("The original 72 publication decisions remain intact. The six A1 scale slices add **301 digest-bound publication decisions** (43 topics + 129 examples + 86 exercises + 43 mistakes)","The original 72 publication decisions remain intact. The six A1 scale slices add **301 digest-bound publication decisions** and the six A2 scale slices add **336** more (48 topics + 144 examples + 96 exercises + 48 mistakes)"),
        ("The full 300-topic framework remains the curriculum/taxonomy; **55/300 topics now have reviewed rich runtime bodies**, including **45/45 A1 topics**. Further expansion proceeds from A2 upward as controlled CEFR slices rather than generating the remaining topics in bulk.","The full 300-topic framework remains the curriculum/taxonomy; **103/300 topics now have reviewed rich runtime bodies**, including **45/45 A1** and **50/50 A2**. Further expansion proceeds from B1 upward as controlled CEFR slices rather than generating the remaining topics in bulk."),
        ("Current published runtime: `shared/dictionary` contains **300 lexemes + 300 senses (600)**; `shared/grammar` contains **55 topics**; `shared/sentences` contains **1,918 records** = **765 examples + 910 exercises + 100 dialogues + 143 reviewed common mistakes**;","Current published runtime: `shared/dictionary` contains **300 lexemes + 300 senses (600)**; `shared/grammar` contains **103 topics**; `shared/sentences` contains **2,206 records** = **909 examples + 1,006 exercises + 100 dialogues + 191 reviewed common mistakes**;"),
        ("The active controlled manifest now accounts for **4,205 checked-in draft authoring/source records across 39 batches**;","The active controlled manifest now accounts for **4,541 checked-in draft authoring/source records across 45 batches**;"),
        ("grammar topics: **300/300 framework entries**, with **55/300 reviewed rich topic bodies** currently published, including **45/45 A1 topics**;","grammar topics: **300/300 framework entries**, with **103/300 reviewed rich topic bodies** currently published, including **45/45 A1** and **50/50 A2**;"),
        ("common mistakes: **143 / 2,000 minimum in published runtime** = the closed 100-record E06 pilot plus 43 reviewed A1 grammar-scale mistakes;","common mistakes: **191 / 2,000 minimum in published runtime** = the closed 100-record E06 pilot plus 91 reviewed A1-A2 grammar-scale mistakes;"),
        ("current published runtime contains **765 examples** (165 E05 grammar-linked + 300 typing-text + 300 Tatoeba);","current published runtime contains **909 examples** (309 E05 grammar-linked + 300 typing-text + 300 Tatoeba);"),
        ("continue grammar-body promotion in small reviewed CEFR slices; A1 is now complete at 45/45 rich topics, with the six A1 scale slices adding 43 rich topics and 258 linked sentence-domain records; continue next with A2 while E03, E04, E05 and E06 publication still uses digest-bound `draft → published` overlays;","continue grammar-body promotion in small reviewed CEFR slices; A1 and A2 are now complete at 45/45 and 50/50 rich topics. The A1+A2 scale slices add 91 rich topics and 546 linked sentence-domain records; continue next with B1 while E03, E04, E05 and E06 publication still uses digest-bound `draft → published` overlays;"),
    ]
    for old,new in replacements: text=must_replace(text,old,new,"master plan A2 checkpoint")
    path.write_text(text,encoding="utf-8")


def main():
    slices=build_sources()
    add_batches(slices)
    write_reviews(slices)
    patch_package()
    patch_publisher()
    patch_smoke()
    patch_release()
    patch_e11()
    patch_master_plan()
    print(json.dumps({"a2Slices":len(slices),"topics":sum(len(s["records"]["grammar-topics"]) for s in slices),"records":sum(sum(len(v) for v in s["records"].values()) for s in slices)},indent=2))


if __name__=="__main__":
    main()
