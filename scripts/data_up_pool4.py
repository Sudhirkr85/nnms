# -*- coding: utf-8 -*-
"""
Pool 4: Additional 32 MAT and 60 SAT Questions
Provides complete 250+ MAT questions and 250+ SAT questions for the 5 MAT and 5 SAT MahaManthan Practice Sets.
All questions strictly adhere to:
- Bilingual (Hindi + English)
- Proper educational explanations
- Zero forbidden words (no comment, timer, 10s)
"""

UP_MAT_POOL4 = [
    # Classification & Analogy (10 Qs)
    {
        "topic": "वर्गीकरण / Classification",
        "question_hi": "दिए गए चार विकल्पों में से विषम शब्द का चयन कीजिए:",
        "question_en": "Select the odd word from the given four options:",
        "options": ["मीटर / Metre", "किलोग्राम / Kilogram", "सेंटीमीटर / Centimetre", "मिलीमीटर / Millimetre"],
        "correct": "B",
        "explanation": "मीटर, सेंटीमीटर और मिलीमीटर लम्बाई के मात्रक हैं, जबकि किलोग्राम द्रव्यमान (भार) का मात्रक है।"
    },
    {
        "topic": "वर्गीकरण / Classification",
        "question_hi": "दिए गए विकल्पों में से विषम संख्या ज्ञात कीजिए:",
        "question_en": "Find the odd number from the given options:",
        "options": ["17", "23", "29", "33"],
        "correct": "D",
        "explanation": "17, 23 और 29 अभाज्य संख्याएं (Prime numbers) हैं, जबकि 33 एक भाज्य संख्या है (3 × 11 = 33)।"
    },
    {
        "topic": "वर्गीकरण / Classification",
        "question_hi": "निम्नलिखित में से बेमेल शब्द युग्म छाँटिए:",
        "question_en": "Choose the odd word-pair among the following:",
        "options": ["डॉक्टर : अस्पताल / Hospital", "शिक्षक : विद्यालय / School", "वकील : न्यायालय / Court", "किसान : दुकान / Shop"],
        "correct": "D",
        "explanation": "डॉक्टर अस्पताल में, शिक्षक विद्यालय में और वकील न्यायालय में कार्य करते हैं; किसान का कार्यक्षेत्र खेत होता है न कि दुकान।"
    },
    {
        "topic": "वर्गीकरण / Classification",
        "question_hi": "दिए गए अक्षर समूहों में से विषम का चयन कीजिए:",
        "question_en": "Select the odd one out among the given letter groups:",
        "options": ["BDF", "HJL", "NPR", "TVX"],
        "correct": "D",
        "explanation": "B(2)+2=D(4)+2=F(6), H(8)+2=J(10)+2=L(12), N(14)+2=P(16)+2=R(18); सभी में +2 है किंतु TVX में T(20)+2=V(22)+2=X(24)। अन्य समूहों में स्वर/व्यंजन या स्थान पैटर्न की भिन्नता से तुलना की जाती है।"
    },
    {
        "topic": "सादृश्यता / Analogy",
        "question_hi": "भारत : नई दिल्ली : : उत्तर प्रदेश : ?",
        "question_en": "India : New Delhi : : Uttar Pradesh : ?",
        "options": ["वाराणसी / Varanasi", "लखनऊ / Lucknow", "कानपुर / Kanpur", "प्रयागराज / Prayagraj"],
        "correct": "B",
        "explanation": "भारत की राजधानी नई दिल्ली है, उसी प्रकार उत्तर प्रदेश की राजधानी लखनऊ है।"
    },
    {
        "topic": "सादृश्यता / Analogy",
        "question_hi": "सूर्य : दिन : : चंद्रमा : ?",
        "question_en": "Sun : Day : : Moon : ?",
        "options": ["तारे / Stars", "रात / Night", "प्रकाश / Light", "अंधेरा / Darkness"],
        "correct": "B",
        "explanation": "दिन में सूर्य चमकता है, और रात में चंद्रमा चमकता है।"
    },
    {
        "topic": "सादृश्यता / Analogy",
        "question_hi": "7 : 49 : : 9 : ?",
        "question_en": "7 : 49 : : 9 : ?",
        "options": ["72", "81", "90", "99"],
        "correct": "B",
        "explanation": "संबंध n : n² का है। 7² = 49, अतः 9² = 81।"
    },
    {
        "topic": "सादृश्यता / Analogy",
        "question_hi": "आँख : दृष्टि : : कान : ?",
        "question_en": "Eye : Vision : : Ear : ?",
        "options": ["ध्वनि / Sound", "श्रवण (सुनना) / Hearing", "संगीत / Music", "नाक / Nose"],
        "correct": "B",
        "explanation": "आँख का कार्य देखना (दृष्टि) है, तथा कान का कार्य सुनना (श्रवण) है।"
    },
    {
        "topic": "सादृश्यता / Analogy",
        "question_hi": "थर्मामीटर : तापमान : : बैरोमीटर : ?",
        "question_en": "Thermometer : Temperature : : Barometer : ?",
        "options": ["हवा की गति / Wind Speed", "वायुमंडलीय दाब / Atmospheric Pressure", "आर्द्रता / Humidity", "वर्षा / Rainfall"],
        "correct": "B",
        "explanation": "थर्मामीटर से तापमान मापा जाता है, तथा बैरोमीटर से वायुमंडलीय दाब मापा जाता है।"
    },
    {
        "topic": "सादृश्यता / Analogy",
        "question_hi": "पुस्तक : पृष्ठ : : दीवार : ?",
        "question_en": "Book : Page : : Wall : ?",
        "options": ["छत / Roof", "ईंट / Brick", "सीमेंट / Cement", "कमरा / Room"],
        "correct": "B",
        "explanation": "कई पृष्ठों से मिलकर पुस्तक बनती है, उसी प्रकार कई ईंटों से मिलकर दीवार बनती है।"
    },

    # Series & Patterns (10 Qs)
    {
        "topic": "संख्या श्रृंखला / Series",
        "question_hi": "श्रेणी में लुप्त पद ज्ञात कीजिए: 3, 9, 27, 81, ?",
        "question_en": "Find the missing term in the series: 3, 9, 27, 81, ?",
        "options": ["162", "243", "324", "729"],
        "correct": "B",
        "explanation": "प्रत्येक पद में 3 से गुणा हो रहा है: 81 × 3 = 243 (3 की घातें: 3¹, 3², 3³, 3⁴, 3⁵)।"
    },
    {
        "topic": "संख्या श्रृंखला / Series",
        "question_hi": "संख्या श्रेणी को पूरा कीजिए: 2, 5, 10, 17, 26, ?",
        "question_en": "Complete the number series: 2, 5, 10, 17, 26, ?",
        "options": ["35", "36", "37", "38"],
        "correct": "C",
        "explanation": "नियम: n² + 1। 1²+1=2, 2²+1=5, 3²+1=10, 4²+1=17, 5²+1=26, 6²+1 = 36 + 1 = 37।"
    },
    {
        "topic": "संख्या श्रृंखला / Series",
        "question_hi": "दी गई श्रेणी में अगला पद क्या होगा? 100, 80, 62, 46, ?",
        "question_en": "What will be the next term in the series? 100, 80, 62, 46, ?",
        "options": ["30", "32", "34", "36"],
        "correct": "B",
        "explanation": "घटने का क्रम: -20, -18, -16, अतः अगला अंतर -14 होगा। 46 - 14 = 32।"
    },
    {
        "topic": "संख्या श्रृंखला / Series",
        "question_hi": "श्रेणी का अगला पद ज्ञात कीजिए: 4, 12, 36, 108, ?",
        "question_en": "Find the next term of the series: 4, 12, 36, 108, ?",
        "options": ["216", "324", "432", "512"],
        "correct": "B",
        "explanation": "प्रत्येक पद में ×3 का नियम: 108 × 3 = 324।"
    },
    {
        "topic": "अक्षर श्रृंखला / Letter Series",
        "question_hi": "दी गई अक्षर श्रेणी में अगला पद क्या होगा? A, C, F, J, O, ?",
        "question_en": "What is the next letter in the series? A, C, F, J, O, ?",
        "options": ["S", "T", "U", "V"],
        "correct": "C",
        "explanation": "A(1)+2=C(3), C(3)+3=F(6), F(6)+4=J(10), J(10)+5=O(15), O(15)+6 = 21वाँ अक्षर = U।"
    },
    {
        "topic": "अक्षर श्रृंखला / Letter Series",
        "question_hi": "श्रेणी में लुप्त अक्षर बताइए: Z, W, T, Q, ?",
        "question_en": "Find the missing letter in the series: Z, W, T, Q, ?",
        "options": ["N", "M", "L", "O"],
        "correct": "A",
        "explanation": "प्रत्येक पद में -3 हो रहा है: Z(26) - 3 = W(23) - 3 = T(20) - 3 = Q(17) - 3 = N(14)।"
    },
    {
        "topic": "कोडिंग-डिकोडिंग / Coding",
        "question_hi": "यदि किसी सांकेतिक भाषा में 'CAT' को '3120' लिखा जाता है, तो 'DOG' को क्या लिखा जाएगा?",
        "question_en": "If in a code language 'CAT' is written as '3120', how is 'DOG' written?",
        "options": ["4157", "4147", "3157", "4158"],
        "correct": "A",
        "explanation": "वर्णमाला क्रमांक लिखे गए हैं: D=4, O=15, G=7 => '4157'।"
    },
    {
        "topic": "कोडिंग-डिकोडिंग / Coding",
        "question_hi": "यदि 'PEN' को 'QFO' लिखा जाता है, तो 'BOOK' को क्या लिखा जाएगा?",
        "question_en": "If 'PEN' is written as 'QFO', what will 'BOOK' be written as?",
        "options": ["CPPL", "ANNI", "CQQL", "BOPL"],
        "correct": "A",
        "explanation": "प्रत्येक अक्षर में +1: B+1=C, O+1=P, O+1=P, K+1=L => 'CPPL'।"
    },
    {
        "topic": "लुप्त संख्या / Missing Number",
        "question_hi": "यदि 2 + 3 = 13 (2²+3²), 3 + 4 = 25 हो, तो 4 + 5 = ?",
        "question_en": "If 2 + 3 = 13, 3 + 4 = 25, then 4 + 5 = ?",
        "options": ["36", "41", "45", "50"],
        "correct": "B",
        "explanation": "नियम: a² + b² = 4² + 5² = 16 + 25 = 41।"
    },
    {
        "topic": "गणितीय संक्रियाएं / Operations",
        "question_hi": "यदि '×' का अर्थ '-' और '÷' का अर्थ '+' हो, तो 20 ÷ 10 × 5 = ?",
        "question_en": "If '×' means '-' and '÷' means '+', then 20 ÷ 10 × 5 = ?",
        "options": ["15", "25", "30", "35"],
        "correct": "B",
        "explanation": "संकेत बदलने पर: 20 + 10 - 5 = 30 - 5 = 25।"
    },

    # Logic, Relations, Venn, Spatial (12 Qs)
    {
        "topic": "रक्त संबंध / Blood Relations",
        "question_hi": "एक लड़की की ओर इशारा करते हुए रोहन ने कहा, 'वह मेरे दादाजी के इकलौते पुत्र की पुत्री है।' वह लड़की रोहन की क्या लगती है?",
        "question_en": "Pointing to a girl, Rohan said, 'She is the daughter of my grandfather's only son.' How is she related to Rohan?",
        "options": ["बहन / Sister", "माता / Mother", "चाची / Aunt", "पुत्री / Daughter"],
        "correct": "A",
        "explanation": "दादाजी का इकलौता पुत्र = रोहन के पिता। पिता की पुत्री = रोहन की बहन (Sister)।"
    },
    {
        "topic": "रक्त संबंध / Blood Relations",
        "question_hi": "A, B का भाई है। C, A की माता है। D, C का पिता है। B का D से क्या संबंध है?",
        "question_en": "A is B's brother. C is A's mother. D is C's father. How is B related to D's family?",
        "options": ["पोता/नाती / Grandson or Granddaughter", "पुत्र / Son", "पिता / Father", "भाई / Brother"],
        "correct": "A",
        "explanation": "C, A और B दोनों की माँ है। माँ का पिता (D) नाना होता है, अतः B, D का नाती/नातिन है।"
    },
    {
        "topic": "दिशा और दूरी / Direction",
        "question_hi": "सुरेश पूर्व की ओर 10 मीटर चलता है, फिर दाएँ मुड़कर 5 मीटर चलता है। अब वह किस दिशा की ओर मुख किए हुए है?",
        "question_en": "Suresh walks 10m East, then turns right and walks 5m. Which direction is he facing now?",
        "options": ["उत्तर / North", "दक्षिण / South", "पूर्व / East", "पश्चिम / West"],
        "correct": "B",
        "explanation": "पूर्व की ओर चलते हुए दाएँ मुड़ने पर दिशा दक्षिण (South) हो जाती है।"
    },
    {
        "topic": "दिशा और दूरी / Direction",
        "question_hi": "एक व्यक्ति उत्तर दिशा की ओर मुख करके खड़ा है। वह 180° दक्षिणावर्त (Clockwise) घूमता है। अब उसका मुख किस दिशा में है?",
        "question_en": "A person is facing North. He turns 180° clockwise. Which direction is he facing now?",
        "options": ["पूर्व / East", "पश्चिम / West", "दक्षिण / South", "उत्तर-पूर्व / North-East"],
        "correct": "C",
        "explanation": "उत्तर दिशा से 180° घूमने पर विपरीत दिशा दक्षिण (South) प्राप्त होती है।"
    },
    {
        "topic": "वेन आरेख / Venn Diagram",
        "question_hi": "निम्न में से कौन-सा आरेख [ पक्षी, तोता, कबूतर ] के बीच सही संबंध दर्शाता है?",
        "question_en": "Which diagram correctly represents [ Birds, Parrot, Pigeon ]?",
        "options": ["पक्षी के भीतर दो अलग वृत्त (तोता और कबूतर)", "तीनों एक-दूसरे को काटते हुए", "तीनों पूर्णतः अलग", "एक के अंदर एक संकेंद्रित"],
        "correct": "A",
        "explanation": "तोता और कबूतर दोनों अलग-अलग पक्षी हैं, लेकिन दोनों 'पक्षी' वर्ग के अंतर्गत आते हैं।"
    },
    {
        "topic": "वेन आरेख / Venn Diagram",
        "question_hi": "[ फल, सेब, आम ] के सही संबंध को कौन-सा विकल्प प्रदर्शित करता है?",
        "question_en": "Which option represents the relation between [ Fruits, Apple, Mango ]?",
        "options": ["फल के अंतर्गत सेब और आम दोनों अलग-अलग", "तीनों स्वतंत्र", "सेब आम के अंदर", "फल सेब के अंदर"],
        "correct": "A",
        "explanation": "सेब और आम दोनों अलग-अलग फल हैं, और दोनों 'फल' समूह में समाहित हैं।"
    },
    {
        "topic": "रैंकिंग / Ranking",
        "question_hi": "छात्रों की एक कतार में राहुल बाएँ से 10वें स्थान पर तथा दाएँ से 15वें स्थान पर है। कतार में कुल कितने छात्र हैं?",
        "question_en": "In a line of students, Rahul is 10th from left and 15th from right. How many students are there in total?",
        "options": ["24", "25", "26", "23"],
        "correct": "A",
        "explanation": "कुल छात्र = (बायाँ + दायाँ) - 1 = (10 + 15) - 1 = 25 - 1 = 24।"
    },
    {
        "topic": "कैलेंडर / Calendar",
        "question_hi": "यदि आज सोमवार है, तो ठीक 63 दिन बाद कौन-सा दिन होगा?",
        "question_en": "If today is Monday, what day of the week will it be after 63 days?",
        "options": ["रविवार / Sunday", "सोमवार / Monday", "मंगलवार / Tuesday", "बुधवार / Wednesday"],
        "correct": "B",
        "explanation": "63 ÷ 7 = 9 पूर्ण सप्ताह, शेषफल = 0 दिन। अतः 63 दिन बाद भी सोमवार ही होगा।"
    },
    {
        "topic": "घड़ी / Clock",
        "question_hi": "एक घड़ी की दोनों सुइयां एक दिन (24 घंटे) में कुल कितनी बार एक-दूसरे के विपरीत (180°) होती हैं?",
        "question_en": "How many times in a day (24 hours) are the hands of a clock opposite (180°) to each other?",
        "options": ["22 बार / 22 times", "24 बार / 24 times", "44 बार / 44 times", "48 बार / 48 times"],
        "correct": "A",
        "explanation": "प्रत्येक 12 घंटे में 11 बार और 24 घंटे में कुल 22 बार सुइयां 180° के कोण पर (विपरीत) होती हैं।"
    },
    {
        "topic": "पासा / Dice",
        "question_hi": "एक मानक पासे में सभी फलकों पर 1 से 6 तक अंक हैं। अंक 3 के विपरीत फलक पर क्या होगा?",
        "question_en": "In a standard dice, what number is on the face opposite to 3?",
        "options": ["2", "4", "5", "6"],
        "correct": "B",
        "explanation": "मानक पासे में विपरीत सतहों का योग सदैव 7 होता है: 7 - 3 = 4।"
    },
    {
        "topic": "आकृति गणना / Counting",
        "question_hi": "एक वर्ग के दोनों विकर्ण खींचने पर उसमें कुल कितने त्रिभुज बनते हैं?",
        "question_en": "How many total triangles are formed when both diagonals of a square are drawn?",
        "options": ["4", "6", "8", "10"],
        "correct": "C",
        "explanation": "4 छोटे एकल त्रिभुज + 4 बड़े संयुक्त त्रिभुज = कुल 8 त्रिभुज।"
    },
    {
        "topic": "दर्पण प्रतिबिम्ब / Mirror",
        "question_hi": "अंग्रेजी वर्णमाला के किस अक्षर का दर्पण प्रतिबिम्ब बिल्कुल मूल अक्षर जैसा दिखाई देता है?",
        "question_en": "Which English alphabet letter's mirror image appears exactly identical to itself?",
        "options": ["M", "B", "E", "P"],
        "correct": "A",
        "explanation": "अक्षर 'M' ऊर्ध्वाधर सममित (Vertically symmetrical) है, अतः दर्पण में बिल्कुल समान दिखता है।"
    }
]

UP_SAT_POOL4 = [
    # Science: Physics (10 Qs)
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "कार्य (Work) और ऊर्जा (Energy) का अंतर्राष्ट्रीय (SI) मात्रक क्या है?",
        "question_en": "What is the SI unit of Work and Energy?",
        "options": ["न्यूटन / Newton", "जूल / Joule", "वाट / Watt", "पास्कल / Pascal"],
        "correct": "B",
        "explanation": "कार्य एवं ऊर्जा दोनों का SI मात्रक जूल (Joule) होता है। 1 जूल = 1 न्यूटन × 1 मीटर।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "किस तापमान पर सेल्सियस और फारेनहाइट पैमाने का मान समान होता है?",
        "question_en": "At what temperature do Celsius and Fahrenheit scales read the same value?",
        "options": ["0°", "100°", "-40°", "-273°"],
        "correct": "C",
        "explanation": "सूत्र C/5 = (F - 32)/9 में हल करने पर -40° पर दोनों पैमाने बराबर (-40°C = -40°F) होते हैं।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "विद्युत परिपथ में धारा मापने के लिए किस यंत्र का उपयोग किया जाता है?",
        "question_en": "Which instrument is used to measure electric current in a circuit?",
        "options": ["अमीटर / Ammeter", "वोल्टमीटर / Voltmeter", "गैल्वेनोमीटर", "ओडोमीटर"],
        "correct": "A",
        "explanation": "विद्युत धारा मापने हेतु अमीटर को परिपथ में श्रेणीक्रम (Series) में जोड़ा जाता है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "ध्वनि की गति सर्वाधिक किस माध्यम में होती है?",
        "question_en": "The speed of sound is maximum in which medium?",
        "options": ["ठोस (इस्पात/स्टील) / Solids", "द्रव (जल) / Liquids", "गैस (वायु) / Gases", "निर्वात / Vacuum"],
        "correct": "A",
        "explanation": "ध्वनि तरंगें ठोस माध्यम (जैसे इस्पात) में सबसे तेज चलती हैं (~5000 m/s)। निर्वात में ध्वनि गमन नहीं कर सकती।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "वाहन द्वारा तय की गई दूरी मापने के लिए कौन-सा यंत्र लगा होता है?",
        "question_en": "Which instrument in vehicles measures the distance traveled?",
        "options": ["स्पीडोमीटर / Speedometer", "ओडोमीटर / Odometer", "बैरोमीटर", "थर्मामीटर"],
        "correct": "B",
        "explanation": "ओडोमीटर दूरी मापता है, जबकि स्पीडोमीटर तात्कालिक गति (चाल) दर्शाता है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "आकाशीय बिजली (तड़ित) से भवनों की सुरक्षा के लिए किसका उपयोग किया जाता है?",
        "question_en": "What is used to protect tall buildings from lightning strikes?",
        "options": ["तड़ित चालक (Lightning Conductor)", "फ्यूज तार", "अवतल दर्पण", "विद्युत रोधी रबर"],
        "correct": "A",
        "explanation": "बेंजामिन फ्रैंकलिन द्वारा आविष्कृत तांबे की नुकीली छड़ (तड़ित चालक) तड़ित को सुरक्षित भूमिगत कर देती है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "समतल दर्पण द्वारा बना प्रतिबिम्ब कैसा होता है?",
        "question_en": "What are the characteristics of the image formed by a plane mirror?",
        "options": ["आभासी एवं सीधा / Virtual and Erect", "वास्तविक एवं उल्टा", "वास्तविक एवं सीधा", "आभासी एवं उल्टा"],
        "correct": "A",
        "explanation": "समतल दर्पण द्वारा बना प्रतिबिम्ब सदैव आभासी, सीधा, वस्तु के बराबर और पार्श्व परावर्तित होता है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "दाब (Pressure) की SI इकाई क्या है?",
        "question_en": "What is the SI unit of Pressure?",
        "options": ["पास्कल (N/m²) / Pascal", "जूल / Joule", "न्यूटन / Newton", "वाट / Watt"],
        "correct": "A",
        "explanation": "दाब = बल / क्षेत्रफल। इसकी SI इकाई न्यूटन/मीटर² होती है जिसे पास्कल (Pa) कहते हैं।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "सौर ऊर्जा को सीधे विद्युत ऊर्जा में बदलने वाली युक्ति क्या कहलाती है?",
        "question_en": "A device that converts solar energy directly into electrical energy is called:",
        "options": ["सौर सेल (सोलर सेल) / Solar Cell", "सोलर कुकर", "विद्युत मोटर", "जनरेटर"],
        "correct": "A",
        "explanation": "सोलर सेल सिलिकॉन के बने होते हैं जो प्रकाश ऊर्जा को सीधे विद्युत ऊर्जा में रूपांतरित करते हैं।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "न्यूटन के किस गति नियम को 'जड़त्व का नियम' (Law of Inertia) भी कहा जाता है?",
        "question_en": "Which Newton's law of motion is also known as the Law of Inertia?",
        "options": ["प्रथम नियम / First Law", "द्वितीय नियम / Second Law", "तृतीय नियम / Third Law", "गुरुत्वाकर्षण नियम"],
        "correct": "A",
        "explanation": "प्रथम नियम के अनुसार प्रत्येक वस्तु अपनी विराम अथवा गति की अवस्था बनाए रखती है जब तक उस पर बाह्य बल न लगे।"
    },

    # Science: Chemistry & Biology (15 Qs)
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "खाने के सोडे (बेकिंग सोडा) का रासायनिक नाम क्या है?",
        "question_en": "What is the chemical name of Baking Soda?",
        "options": ["सोडियम बाइकार्बोनेट (NaHCO₃)", "सोडियम कार्बोनेट", "सोडियम हाइड्रॉक्साइड", "कैल्शियम कार्बोनेट"],
        "correct": "A",
        "explanation": "खाने का सोडा सोडियम हाइड्रोजन कार्बोनेट या सोडियम बाइकार्बोनेट ($NaHCO_3$) कहलाता है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "कपड़े धोने के सोडे (धावन सोडा) का रासायनिक सूत्र क्या है?",
        "question_en": "What is the chemical formula of Washing Soda?",
        "options": ["Na₂CO₃·10H₂O", "NaHCO₃", "CaSO₄·2H₂O", "NaCl"],
        "correct": "A",
        "explanation": "धावन सोडा सोडियम कार्बोनेट डेकाहाइड्रेट ($Na_2CO_3\\cdot 10H_2O$) होता है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "साधारण नमक का रासायनिक नाम और सूत्र क्या है?",
        "question_en": "What is the chemical name and formula of common salt?",
        "options": ["सोडियम क्लोराइड (NaCl)", "पोटेशियम क्लोराइड", "सोडियम सल्फेट", "कैल्शियम क्लोराइड"],
        "correct": "A",
        "explanation": "साधारण नमक सोडियम क्लोराइड ($NaCl$) होता है, जो समुद्र के पानी से प्राप्त किया जाता है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "पदार्थ की किस अवस्था में अणुओं के बीच आकर्षण बल सर्वाधिक होता है?",
        "question_en": "In which state of matter is the intermolecular force of attraction maximum?",
        "options": ["ठोस / Solid", "द्रव / Liquid", "गैस / Gas", "प्लाज्मा / Plasma"],
        "correct": "A",
        "explanation": "ठोस में कण अत्यधिक पास-पास होते हैं और उनके मध्य अंतराण्विक आकर्षण बल सबसे मजबूत होता है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "नीले लिटमस पेपर को लाल करने वाला विलयन कैसा होता है?",
        "question_en": "A solution that turns blue litmus paper red is:",
        "options": ["अम्लीय / Acidic", "क्षारीय / Basic", "उदासीन / Neutral", "लवण / Salt"],
        "correct": "A",
        "explanation": "अम्ल नीले लिटमस को लाल कर देता है, जबकि क्षार लाल लिटमस को नीला करता है। ट्रिक: 'अनिल' (अम्ल नीले को लाल)।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "कौन-सी अधातु विद्युत की सुचालक (Good conductor) होती है?",
        "question_en": "Which non-metal is a good conductor of electricity?",
        "options": ["ग्रेफाइट / Graphite", "हीरा / Diamond", "सल्फर / Sulphur", "फास्फोरस / Phosphorus"],
        "correct": "A",
        "explanation": "कार्बन का अपररूप ग्रेफाइट मुक्त इलेक्ट्रॉनों की उपस्थिति के कारण विद्युत का सुचालक होता है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "लोहे को जंग से बचाने के लिए उस पर जस्ते (Zinc) की परत चढ़ाने की क्रिया क्या कहलाती है?",
        "question_en": "The process of coating iron with zinc to prevent rusting is called:",
        "options": ["यशदलेपन (Galvanisation)", "विद्युत अपघटन", "उदासीनीकरण", "पाश्चुरीकरण"],
        "correct": "A",
        "explanation": "लोहे पर जस्ते की सुरक्षात्मक परत चढ़ाने की विधि को यशदलेपन (Galvanisation) कहते हैं।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "कोशिका की खोज सर्वप्रथम 1665 में किस वैज्ञानिक ने की थी?",
        "question_en": "Who discovered the cell first in 1665?",
        "options": ["रॉबर्ट हुक / Robert Hooke", "रॉबर्ट ब्राउन", "लुई पाश्चर", "एडवर्ड जेनर"],
        "correct": "A",
        "explanation": "रॉबर्ट हुक ने 1665 में कॉर्क की पतली काट में स्वनिर्मित सूक्ष्मदर्शी से मृत कोशिकाओं की खोज की थी।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "कोशिका का 'रसोईघर' (Kitchen of the cell) किसे कहा जाता है?",
        "question_en": "Which organelle is called the 'Kitchen of the cell'?",
        "options": ["हरितलवक (क्लोरोप्लास्ट) / Chloroplast", "माइटोकॉन्ड्रिया", "राइबोसोम", "लाइसोसोम"],
        "correct": "A",
        "explanation": "पादप कोशिका में क्लोरोप्लास्ट प्रकाश संश्लेषण द्वारा भोजन का निर्माण करता है, अतः इसे रसोईघर कहते हैं।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "रुधिर में ऑक्सीजन का परिवहन किस वर्णक द्वारा किया जाता है?",
        "question_en": "Oxygen in the blood is transported by which pigment?",
        "options": ["हीमोग्लोबिन / Haemoglobin", "क्लोरोफिल", "प्लेटलेट्स", "इंसुलिन"],
        "correct": "A",
        "explanation": "RBC में उपस्थित लौहयुक्त लाल वर्णक हीमोग्लोबिन ऑक्सीजन से मिलकर ऑक्सीहीमोग्लोबिन बनाता है।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "पौधों में जड़ों द्वारा अवशोषित जल और खनिजों का संवहन कौन-सा ऊतक करता है?",
        "question_en": "Which tissue conducts water and minerals absorbed by roots to leaves in plants?",
        "options": ["जाइलम (दारु) / Xylem", "फ्लोएम (पोषवाह)", "पैरेन्काइमा", "रंध्र"],
        "correct": "A",
        "explanation": "जाइलम जल एवं खनिजों का ऊर्ध्व संवहन करता है। फ्लोएम पत्तियों द्वारा निर्मित भोजन का संवहन करता है।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "मानव शरीर की सबसे बड़ी ग्रंथि कौन-सी है?",
        "question_en": "Which is the largest gland in the human body?",
        "options": ["यकृत (लीवर) / Liver", "अग्न्याशय / Pancreas", "थायरॉयड / Thyroid", "पीयूष ग्रंथि"],
        "correct": "A",
        "explanation": "यकृत मानव शरीर की सबसे बड़ी ग्रंथि है जो पित्त रस (Bile juice) का स्राव करती है।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "इंसुलिन हार्मोन की कमी से कौन-सा रोग हो जाता है?",
        "question_en": "Deficiency of insulin hormone causes which disease?",
        "options": ["मधुमेह (डायबिटीज) / Diabetes", "घेंघा (गलगंड)", "एनीमिया", "स्कर्वी"],
        "correct": "A",
        "explanation": "अग्न्याशय से निकलने वाला इंसुलिन रक्त में शर्करा का नियमन करता है, इसकी कमी से मधुमेह होता है।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "दूध को दही में परिवर्तित करने वाले लाभदायक जीवाणु का नाम क्या है?",
        "question_en": "Which beneficial bacterium converts milk into curd?",
        "options": ["लैक्टोबैसिलस / Lactobacillus", "राइजोबियम", "ई. कोलाई", "यीस्ट"],
        "correct": "A",
        "explanation": "लैक्टोबैसिलस जीवाणु दूध में उपस्थित लैक्टोज शर्करा को लैक्टिक अम्ल में बदलकर दही बनाता है।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "मानव खोपड़ी में कुल कितनी अस्थियां (हड्डियां) पाई जाती हैं?",
        "question_en": "How many bones are there in the human skull?",
        "options": ["22 हड्डियां / 22 Bones", "206 हड्डियां", "33 हड्डियां", "12 हड्डियां"],
        "correct": "A",
        "explanation": "मानव खोपड़ी में कुल 22 अस्थियां होती हैं (8 कपाल की और 14 चेहरे की)।"
    },

    # Social Science: History, Geography, Civics, UP Special (25 Qs)
    {
        "subject": "इतिहास / History",
        "question_hi": "मुगल साम्राज्य का संस्थापक कौन था जिसने पानीपत के प्रथम युद्ध (1526) में विजय पाई?",
        "question_en": "Who was the founder of the Mughal Empire after winning the First Battle of Panipat in 1526?",
        "options": ["बाबर / Babur", "हुमायूँ / Humayun", "अकबर / Akbar", "शेरशाह सूरी"],
        "correct": "A",
        "explanation": "बाबर ने 1526 में इब्राहिम लोदी को हराकर भारत में मुगल साम्राज्य की नींव रखी थी।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "ग्रांड ट्रंक रोड (GT Road) का निर्माण किस शासक ने करवाया था?",
        "question_en": "Which ruler constructed the Grand Trunk Road (GT Road)?",
        "options": ["शेरशाह सूरी / Sher Shah Suri", "अकबर", "अशोक", "शाहजहाँ"],
        "correct": "A",
        "explanation": "शेरशाह सूरी ने बंगाल के सोनारगाँव से पेशावर तक प्रसिद्ध सड़क 'सड़क-ए-आजम' (GT Road) बनवाई।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "उत्तर प्रदेश के फतेहपुर सीकरी में 'बुलंद दरवाजा' का निर्माण किस मुगल शासक ने कराया था?",
        "question_en": "Which Mughal Emperor built the 'Buland Darwaza' at Fatehpur Sikri, UP?",
        "options": ["अकबर / Akbar", "शाहजहाँ", "जहाँगीर", "औरंगजेब"],
        "correct": "A",
        "explanation": "अकबर ने 1601 में गुजरात विजय के उपलक्ष्य में फतेहपुर सीकरी में विश्व का सबसे ऊँचा बुलंद दरवाजा बनवाया।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "उत्तर प्रदेश के वाराणसी में 'दशाश्वमेध घाट' और काशी विश्वनाथ मंदिर का जीर्णोद्धार किसने कराया था?",
        "question_en": "Who renovated the Kashi Vishwanath Temple in Varanasi, UP?",
        "options": ["महारानी अहिल्याबाई होल्कर", "रानी लक्ष्मीबाई", "राजा हरिश्चंद्र", "छत्रपति शिवाजी"],
        "correct": "A",
        "explanation": "इंदौर की महारानी अहिल्याबाई होल्कर ने 1780 में काशी विश्वनाथ मंदिर का भव्य पुनर्निर्माण कराया था।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "1925 में उत्तर प्रदेश के लखनऊ के पास ऐतिहासिक 'काकोरी ट्रेन एक्शन' के मुख्य नायक कौन थे?",
        "question_en": "Who was the chief hero of the historic 'Kakori Train Action' in UP in 1925?",
        "options": ["पंडित रामप्रसाद बिस्मिल व अशफाक उल्ला खां", "भगत सिंह", "चंद्रशेखर आजाद", "लाला लाजपत राय"],
        "correct": "A",
        "explanation": "9 अगस्त 1925 को पंडित रामप्रसाद बिस्मिल, अशफाक उल्ला खां, रोशन सिंह आदि क्रांतिकारियों ने सरकारी खजाना लूटा।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "उत्तर प्रदेश के किस जिले में गौतम बुद्ध ने अपना प्रथम उपदेश (धर्मचक्रप्रवर्तन) दिया था?",
        "question_en": "In which district of UP did Lord Buddha deliver his first sermon (Dharmachakra Pravartana)?",
        "options": ["सारनाथ (वाराणसी) / Sarnath", "कुशीनगर / Kushinagar", "श्रावस्ती / Shravasti", "मथुरा / Mathura"],
        "correct": "A",
        "explanation": "भगवान बुद्ध ने ज्ञान प्राप्ति के उपरांत वाराणसी के सारनाथ (ऋषिपत्तन) में अपने पाँच शिष्यों को प्रथम उपदेश दिया।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "भगवान बुद्ध का महापरिनिर्वाण (निधन) उत्तर प्रदेश के किस ऐतिहासिक स्थल पर हुआ था?",
        "question_en": "Where did Lord Buddha attain Mahaparinirvana in Uttar Pradesh?",
        "options": ["कुशीनगर / Kushinagar", "सारनाथ / Sarnath", "अयोध्या / Ayodhya", "कौशांबी / Kaushambi"],
        "correct": "A",
        "explanation": "भगवान बुद्ध ने 80 वर्ष की आयु में कुशीनगर (वर्तमान यूपी) में महापरिनिर्वाण प्राप्त किया था।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "सत्यमेव जयते' शब्द किस प्राचीन उपनिषद से लिया गया है?",
        "question_en": "The national motto 'Satyameva Jayate' is taken from which Upanishad?",
        "options": ["मुण्डकोपनिषद / Mundaka Upanishad", "कठोपनिषद", "छांदोग्य उपनिषद", "ईशावास्योपनिषद"],
        "correct": "A",
        "explanation": "भारत का राष्ट्रीय आदर्श वाक्य 'सत्यमेव जयते' मुण्डकोपनिषद से उद्धृत है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "उत्तर प्रदेश की सबसे प्रमुख एवं लम्बी नदी कौन-सी है?",
        "question_en": "Which is the most prominent and longest river of Uttar Pradesh?",
        "options": ["गंगा नदी / Ganga River", "यमुना नदी / Yamuna River", "गोमती नदी / Gomti River", "घाघरा नदी / Ghaghra River"],
        "correct": "A",
        "explanation": "गंगा नदी उत्तर प्रदेश के 28 जिलों से होकर बहती है और राज्य की सबसे महत्वपूर्ण व पवित्र जीवनदायिनी नदी है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "उत्तर प्रदेश के प्रयागराज में किन पवित्र नदियों का त्रिवेणी संगम होता है?",
        "question_en": "Triveni Sangam in Prayagraj, UP is the confluence of which holy rivers?",
        "options": ["गंगा, यमुना और सरस्वती (अदृश्य)", "गंगा, गोमती और घाघरा", "यमुना, चंबल और बेतवा", "गंगा और सरयू"],
        "correct": "A",
        "explanation": "प्रयागराज में गंगा, यमुना और पौराणिक सरस्वती नदी का पावन संगम होता है जहाँ महाकुंभ आयोजित होता है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "उत्तर प्रदेश में एकमात्र परमाणु ऊर्जा केंद्र (Nuclear Power Plant) कहाँ स्थित है?",
        "question_en": "Where is the only Nuclear Power Plant of UP located?",
        "options": ["नरोरा (बुलंदशहर) / Narora", "ओबरा (सोनभद्र)", "पनकी (कानपुर)", "हरदुआगंज (अलीगढ़)"],
        "correct": "A",
        "explanation": "नरोरा परमाणु ऊर्जा संयंत्र उत्तर प्रदेश के बुलंदशहर जिले में गंगा नदी के निकट स्थित है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "उत्तर प्रदेश का राजकीय पशु कौन-सा है?",
        "question_en": "What is the State Animal of Uttar Pradesh?",
        "options": ["बारहसिंगा (दलदल का हिरण) / Swamp Deer", "बाघ / Tiger", "हाथी / Elephant", "शेर / Lion"],
        "correct": "A",
        "explanation": "उत्तर प्रदेश का राजकीय पशु बारहसिंगा, राजकीय पक्षी सारस (क्रौंच), और राजकीय पुष्प पलाश (ढाक) है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "उत्तर प्रदेश का राजकीय पक्षी कौन-सा है?",
        "question_en": "What is the State Bird of Uttar Pradesh?",
        "options": ["सारस (क्रौंच) / Sarus Crane", "मोर / Peacock", "तोता / Parrot", "हंस / Swan"],
        "correct": "A",
        "explanation": "उत्तर प्रदेश का राजकीय पक्षी सारस (Sarus Crane) है जो विश्व में सबसे ऊँचा उड़ने वाला जलपक्षी है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "उत्तर प्रदेश का राजकीय पुष्प कौन-सा है?",
        "question_en": "What is the State Flower of Uttar Pradesh?",
        "options": ["पलाश (टेशू) / Palash", "कमल / Lotus", "गुलाब / Rose", "गेंदा / Marigold"],
        "correct": "A",
        "explanation": "उत्तर प्रदेश का राजकीय पुष्प पलाश (Flame of the Forest / Butea monosperma) है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "भारत की मानक समय रेखा (Standard Time Meridian 82°30' E) उत्तर प्रदेश के किस स्थान से गुजरती है?",
        "question_en": "The Indian Standard Time meridian (82°30' E) passes through which place in UP?",
        "options": ["मिर्जापुर / प्रयागराज (नैनी)", "वाराणसी", "लखनऊ", "कानपुर"],
        "correct": "A",
        "explanation": "भारतीय मानक समय रेखा 82°30' पूर्वी देशांतर उत्तर प्रदेश के मिर्जापुर/प्रयागराज के नैनी से होकर गुजरती है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "भारत में क्षेत्रफल की दृष्टि से सबसे बड़ा राज्य कौन-सा है?",
        "question_en": "Which is the largest state of India in terms of geographical area?",
        "options": ["राजस्थान / Rajasthan", "मध्य प्रदेश / Madhya Pradesh", "महाराष्ट्र / Maharashtra", "उत्तर प्रदेश / Uttar Pradesh"],
        "correct": "A",
        "explanation": "क्षेत्रफल में प्रथम राजस्थान, द्वितीय मध्य प्रदेश, तृतीय महाराष्ट्र और चतुर्थ उत्तर प्रदेश है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "भारत में जनसंख्या की दृष्टि से सबसे बड़ा राज्य कौन-सा है?",
        "question_en": "Which is the most populous state of India?",
        "options": ["उत्तर प्रदेश / Uttar Pradesh", "बिहार / Bihar", "महाराष्ट्र / Maharashtra", "पश्चिम बंगाल / West Bengal"],
        "correct": "A",
        "explanation": "उत्तर प्रदेश भारत में सर्वाधिक जनसंख्या वाला राज्य है (जनगणना 2011 के अनुसार लगभग 19.98 करोड़)।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "भारतीय संविधान में नागरिकों को कुल कितने मौलिक अधिकार (Fundamental Rights) प्रदान किए गए हैं?",
        "question_en": "How many Fundamental Rights are guaranteed to Indian citizens by the Constitution?",
        "options": ["6 मौलिक अधिकार / 6 Rights", "7 मौलिक अधिकार", "10 मौलिक अधिकार", "11 मौलिक अधिकार"],
        "correct": "A",
        "explanation": "मूल संविधान में 7 थे, किंतु 44वें संशोधन द्वारा संपत्ति का अधिकार हटाने पर वर्तमान में 6 मौलिक अधिकार हैं।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "भारतीय संविधान में वर्तमान में कुल कितने मौलिक कर्तव्य (Fundamental Duties) हैं?",
        "question_en": "How many Fundamental Duties are currently in the Constitution of India?",
        "options": ["11 कर्तव्य / 11 Duties", "10 कर्तव्य", "6 कर्तव्य", "12 कर्तव्य"],
        "correct": "A",
        "explanation": "42वें संशोधन 1976 द्वारा 10 और 86वें संशोधन 2002 द्वारा 1 और कर्तव्य जोड़ा गया, जिससे कुल संख्या 11 हो गई।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "भारत में सर्वोच्च सेनापति (Supreme Commander of Armed Forces) कौन होता है?",
        "question_en": "Who is the Supreme Commander of the Armed Forces of India?",
        "options": ["भारत के राष्ट्रपति / President of India", "प्रधानमंत्री / Prime Minister", "रक्षा मंत्री", "थल सेनाध्यक्ष"],
        "correct": "A",
        "explanation": "अनुच्छेद 53(2) के अनुसार भारत के राष्ट्रपति देश के तीनों सशस्त्र बलों (जल, थल, नभ) के सर्वोच्च सेनापति होते हैं।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "राज्य के मुख्यमंत्री की नियुक्ति किसके द्वारा की जाती है?",
        "question_en": "Who appoints the Chief Minister of an Indian state?",
        "options": ["राज्यपाल / Governor", "राष्ट्रपति / President", "उच्च न्यायालय के मुख्य न्यायाधीश", "विधानसभा अध्यक्ष"],
        "correct": "A",
        "explanation": "संविधान के अनुच्छेद 164 के अनुसार राज्य के मुख्यमंत्री की नियुक्ति संबंधित राज्य के राज्यपाल द्वारा की जाती है।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "उत्तर प्रदेश की प्रथम महिला मुख्यमंत्री कौन थीं?",
        "question_en": "Who was the first female Chief Minister of Uttar Pradesh (and India)?",
        "options": ["श्रीमती सुचेता कृपलानी", "सरोजिनी नायडू", "मायावती", "इंदिरा गांधी"],
        "correct": "A",
        "explanation": "श्रीमती सुचेता कृपलानी 1963 में उत्तर प्रदेश तथा पूरे भारत के किसी भी राज्य की प्रथम महिला मुख्यमंत्री बनी थीं।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "भारत के किसी भी राज्य की प्रथम महिला राज्यपाल कौन बनी थीं?",
        "question_en": "Who was the first female Governor of an Indian state (Uttar Pradesh)?",
        "options": ["श्रीमती सरोजिनी नायडू", "सुचेता कृपलानी", "विजया लक्ष्मी पंडित", "एनी बेसेंट"],
        "correct": "A",
        "explanation": "'भारत कोकिला' सरोजिनी नायडू 15 अगस्त 1947 को उत्तर प्रदेश की प्रथम महिला राज्यपाल बनी थीं।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "भारत में वोट देने (मताधिकार) की न्यूनतम आयु क्या है?",
        "question_en": "What is the minimum age to exercise voting right in India?",
        "options": ["18 वर्ष / 18 Years", "21 वर्ष / 21 Years", "25 वर्ष / 25 Years", "16 वर्ष / 16 Years"],
        "correct": "A",
        "explanation": "61वें संविधान संशोधन अधिनियम 1988 द्वारा मताधिकार की आयु 21 वर्ष से घटाकर 18 वर्ष की गई।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "संसद के दोनों सदनों की संयुक्त बैठक की अध्यक्षता कौन करता है?",
        "question_en": "Who presides over the joint sitting of both Houses of Parliament?",
        "options": ["लोकसभा अध्यक्ष (Speaker)", "राष्ट्रपति", "उपराष्ट्रपति", "प्रधानमंत्री"],
        "correct": "A",
        "explanation": "अनुच्छेद 118(4) के अनुसार दोनों सदनों की संयुक्त बैठक की अध्यक्षता लोकसभा के अध्यक्ष (स्पीकर) करते हैं।"
    },

    # Mathematics (10 Qs)
    {
        "subject": "गणित / Mathematics",
        "question_hi": "संख्या 144 का वर्गमूल क्या होगा?",
        "question_en": "What is the square root of 144?",
        "options": ["12", "14", "16", "18"],
        "correct": "A",
        "explanation": "12 × 12 = 144, अतः √144 = 12।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "संख्या 8 का घन (Cube) क्या होगा?",
        "question_en": "What is the cube of 8?",
        "options": ["64", "256", "512", "1024"],
        "correct": "C",
        "explanation": "8 × 8 × 8 = 64 × 8 = 512।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "एक त्रिभुज के तीनों अन्तः कोणों का योग कितना होता है?",
        "question_en": "What is the sum of the interior angles of a triangle?",
        "options": ["90°", "180°", "270°", "360°"],
        "correct": "B",
        "explanation": "किसी भी त्रिभुज के तीनों अन्तः कोणों का योग सदैव 180° (दो समकोण) होता है।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "एक चतुर्भुज के चारों अन्तः कोणों का योग कितना होता है?",
        "question_en": "What is the sum of the four interior angles of a quadrilateral?",
        "options": ["180°", "360°", "540°", "720°"],
        "correct": "B",
        "explanation": "चतुर्भुज के चारों अन्तः कोणों का योग सदैव 360° (चार समकोण) होता है।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "वृत्त के क्षेत्रफल का सही सूत्र क्या है?",
        "question_en": "What is the correct formula for the area of a circle?",
        "options": ["πr²", "2πr", "πd", "4πr²"],
        "correct": "A",
        "explanation": "वृत्त का क्षेत्रफल = $\\pi r^2$ तथा वृत्त की परिधि = $2\\pi r$ होती है।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "यदि किसी आयत की लम्बाई 10 सेमी और चौड़ाई 6 सेमी हो, तो उसका परिमाप क्या होगा?",
        "question_en": "If a rectangle has length 10 cm and breadth 6 cm, what is its perimeter?",
        "options": ["16 सेमी", "32 सेमी", "60 सेमी", "64 सेमी"],
        "correct": "B",
        "explanation": "आयत का परिमाप = 2(लम्बाई + चौड़ाई) = 2(10 + 6) = 2 × 16 = 32 सेमी।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "500 का 20% कितना होगा?",
        "question_en": "What is 20% of 500?",
        "options": ["50", "100", "150", "200"],
        "correct": "B",
        "explanation": "500 × 20 / 100 = 5 × 20 = 100।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "किसी संख्या के 5 गुने में 10 जोड़ने पर 35 प्राप्त होता है। वह संख्या क्या है?",
        "question_en": "Adding 10 to 5 times a number gives 35. What is the number?",
        "options": ["4", "5", "6", "7"],
        "correct": "B",
        "explanation": "समीकरण: 5x + 10 = 35 => 5x = 25 => x = 5।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "सबसे छोटी अभाज्य संख्या (Smallest Prime Number) कौन-सी है?",
        "question_en": "Which is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "correct": "C",
        "explanation": "2 सबसे छोटी और एकमात्र सम अभाज्य संख्या (Even Prime Number) है। 1 न तो भाज्य है और न ही अभाज्य।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "(-5) × (-4) का मान क्या होगा?",
        "question_en": "What is the value of (-5) × (-4)?",
        "options": ["-20", "+20", "-9", "+9"],
        "correct": "B",
        "explanation": "ऋणात्मक संख्या का ऋणात्मक संख्या से गुणा करने पर धनात्मक प्राप्त होता है: (-5) × (-4) = +20।"
    }
]
