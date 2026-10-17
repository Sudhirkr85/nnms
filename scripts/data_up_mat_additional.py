# -*- coding: utf-8 -*-
"""
UP NMMS MahaManthan - Additional MAT Questions Pool (Set 3 to Set 5)
150 High-Yield Bilingual Questions for UP NMMS November Exam.
Topics:
- Number Series & Missing Numbers
- Analogy & Classification
- Coding-Decoding & Letter Series
- Blood Relations, Direction Sense, Venn Diagrams, Mathematical Operations, Clock & Calendar
"""

UP_MAT_ADDITIONAL = [
    # --- Classification / विजातीय (15 Qs) ---
    {
        "topic": "वर्गीकरण (शब्द) / Classification",
        "question_hi": "निम्नलिखित में से कौन-सा एक अन्य तीनों से भिन्न है?",
        "question_en": "Which one of the following is different from the other three?",
        "options": ["गंगा / Ganga", "यमुना / Yamuna", "गोदावरी / Godavari", "हिमालय / Himalaya"],
        "correct": "D",
        "explanation": "गंगा, यमुना और गोदावरी नदियाँ हैं, जबकि हिमालय एक पर्वत श्रृंखला है। (Ganga, Yamuna, Godavari are rivers, while Himalaya is a mountain range)."
    },
    {
        "topic": "वर्गीकरण (संख्या) / Number Classification",
        "question_hi": "दिए गए विकल्पों में से विषम संख्या चुनिए:",
        "question_en": "Choose the odd number from the given options:",
        "options": ["11", "13", "15", "17"],
        "correct": "C",
        "explanation": "11, 13 और 17 अभाज्य संख्याएं हैं, जबकि 15 एक भाज्य संख्या (3 × 5) है। (11, 13, 17 are prime numbers, while 15 is composite)."
    },
    {
        "topic": "वर्गीकरण (अक्षर) / Letter Classification",
        "question_hi": "निम्नलिखित अक्षर समूहों में से विषम समूह कौन-सा है?",
        "question_en": "Which of the following letter groups is the odd one out?",
        "options": ["AE", "IO", "OU", "BC"],
        "correct": "D",
        "explanation": "AE, IO और OU दोनों स्वर (Vowels) हैं, जबकि BC दोनों व्यंजन (Consonants) हैं।"
    },
    {
        "topic": "वर्गीकरण (मापन) / Measurement",
        "question_hi": "निम्नलिखित में से बेमेल मात्रक चुनिए:",
        "question_en": "Choose the mismatched unit from the following:",
        "options": ["ग्राम / Gram", "किलोग्राम / Kilogram", "क्विंटल / Quintal", "सेकंड / Second"],
        "correct": "D",
        "explanation": "ग्राम, किलोग्राम और क्विंटल द्रव्यमान/भार के मात्रक हैं, जबकि सेकंड समय का मात्रक है।"
    },
    {
        "topic": "वर्गीकरण (जीव) / Living Organisms",
        "question_hi": "दिए गए चार विकल्पों में से विषम का चयन कीजिए:",
        "question_en": "Select the odd one from the four given options:",
        "options": ["तोता / Parrot", "कौआ / Crow", "कबूतर / Pigeon", "चमगादड़ / Bat"],
        "correct": "D",
        "explanation": "तोता, कौआ और कबूतर पक्षी (Aves) वर्ग में आते हैं, जबकि चमगादड़ स्तनधारी (Mammal) प्राणी है।"
    },
    {
        "topic": "वर्गीकरण (संख्या युग्म) / Number Pair",
        "question_hi": "निम्न में से कौन-सा संख्या युग्म अन्य तीन से अलग है?",
        "question_en": "Which of the following number pairs is different from the others?",
        "options": ["2 : 8", "3 : 27", "4 : 64", "5 : 100"],
        "correct": "D",
        "explanation": "2³ = 8, 3³ = 27, 4³ = 64 (घन का सम्बन्ध)। 5³ = 125 होना चाहिए (100 दिया है)।"
    },
    {
        "topic": "वर्गीकरण (धातु/अधातु) / Science Classification",
        "question_hi": "निम्नलिखित में से विषम तत्व चुनिए:",
        "question_en": "Choose the odd element from the following:",
        "options": ["लोहा / Iron", "तांबा / Copper", "सोना / Gold", "कोयला / Coal"],
        "correct": "D",
        "explanation": "लोहा, तांबा और सोना धातुएं हैं, जबकि कोयला कार्बन का अधात्विक अपरूप है।"
    },
    {
        "topic": "वर्गीकरण (ज्यामिति) / Shapes",
        "question_hi": "निम्नलिखित में से भिन्न आकृति कौन-सी है?",
        "question_en": "Which of the following geometric figures is different?",
        "options": ["घन / Cube", "घनाभ / Cuboid", "बेलन / Cylinder", "वर्ग / Square"],
        "correct": "D",
        "explanation": "घन, घनाभ और बेलन त्रिविमीय (3D) ठोस हैं, जबकि वर्ग द्विविमीय (2D) समतल आकृति है।"
    },
    {
        "topic": "वर्गीकरण (राज्य) / States Classification",
        "question_hi": "निम्नलिखित चार में से कौन-सा एक अन्य से भिन्न है?",
        "question_en": "Which one of the following four is different from the rest?",
        "options": ["उत्तर प्रदेश / UP", "बिहार / Bihar", "मध्य प्रदेश / MP", "दिल्ली / Delhi"],
        "correct": "D",
        "explanation": "उत्तर प्रदेश, बिहार और मध्य प्रदेश पूर्ण राज्य हैं, जबकि दिल्ली एक केंद्र शासित प्रदेश (UT) व राष्ट्रीय राजधानी क्षेत्र है।"
    },
    {
        "topic": "वर्गीकरण (अंक) / Number Sum",
        "question_hi": "दिए गए विकल्पों में से विषम संख्या का चयन कीजिए:",
        "question_en": "Select the odd number from the given options:",
        "options": ["123", "234", "345", "135"],
        "correct": "D",
        "explanation": "123, 234, 345 में लगातार क्रमिक अंक हैं (1-2-3, 2-3-4, 3-4-5), जबकि 135 में विषम अंक (1, 3, 5) हैं।"
    },
    {
        "topic": "वर्गीकरण (उपकरण) / Devices",
        "question_hi": "निम्नलिखित में से विषम उपकरण कौन-सा है?",
        "question_en": "Which of the following devices is the odd one?",
        "options": ["कुल्हाड़ी / Axe", "चाकू / Knife", "आरी / Saw", "हथौड़ा / Hammer"],
        "correct": "D",
        "explanation": "कुल्हाड़ी, चाकू और आरी काटने (Cutting) के औजार हैं, जबकि हथौड़ा ठोकने या पीटने का औजार है।"
    },
    {
        "topic": "वर्गीकरण (खेल) / Sports",
        "question_hi": "दिए गए विकल्पों में से भिन्न खेल चुनिए:",
        "question_en": "Choose the different sport from the options:",
        "options": ["क्रिकेट / Cricket", "हॉकी / Hockey", "फुटबॉल / Football", "शतरंज / Chess"],
        "correct": "D",
        "explanation": "क्रिकेट, हॉकी और फुटबॉल आउटडोर (Outdoor) मैदानी खेल हैं, जबकि शतरंज एक इनडोर (Indoor) खेल है।"
    },
    {
        "topic": "वर्गीकरण (ग्रह) / Planets",
        "question_hi": "निम्नलिखित में से बेमेल खगोलीय पिंड चुनिए:",
        "question_en": "Select the mismatched celestial body:",
        "options": ["पृथ्वी / Earth", "शुक्र / Venus", "शनि / Saturn", "सूर्य / Sun"],
        "correct": "D",
        "explanation": "पृथ्वी, शुक्र और शनि ग्रह हैं, जबकि सूर्य सौरमंडल का एक तारा (Star) है।"
    },
    {
        "topic": "वर्गीकरण (संख्या अंतर) / Difference",
        "question_hi": "दिए गए संख्या युग्मों में से विषम चुनिए:",
        "question_en": "Choose the odd number pair from the options:",
        "options": ["10 - 20", "30 - 40", "50 - 60", "70 - 90"],
        "correct": "D",
        "explanation": "पहले तीन युग्मों में 10 का अंतर है, जबकि चौथे में 20 का अंतर है (70 - 90)।"
    },
    {
        "topic": "वर्गीकरण (रोग) / Diseases",
        "question_hi": "निम्नलिखित में से विषम रोग चुनिए:",
        "question_en": "Choose the odd disease from the following:",
        "options": ["रतौंधी / Night Blindness", "बेरी-बेरी / Beri-Beri", "स्कर्वी / Scurvy", "मलेरिया / Malaria"],
        "correct": "D",
        "explanation": "रतौंधी, बेरी-बेरी और स्कर्वी विटामिन की कमी से होने वाले हीनताजन्य रोग हैं, जबकि मलेरिया प्रोटोजोआ संक्रमण से होता है।"
    },

    # --- Analogy / सादृश्यता (15 Qs) ---
    {
        "topic": "सादृश्यता (देश-राजधानी) / Country-Capital",
        "question_hi": "भारत : नई दिल्ली : : जापान : ?",
        "question_en": "India : New Delhi : : Japan : ?",
        "options": ["बीजिंग / Beijing", "टोक्यो / Tokyo", "सियोल / Seoul", "बैंकॉक / Bangkok"],
        "correct": "B",
        "explanation": "भारत की राजधानी नई दिल्ली है, उसी प्रकार जापान की राजधानी टोक्यो है।"
    },
    {
        "topic": "सादृश्यता (संख्या वर्ग - 1) / Number Analogy",
        "question_hi": "4 : 15 : : 6 : ?",
        "question_en": "4 : 15 : : 6 : ?",
        "options": ["30", "34", "35", "36"],
        "correct": "C",
        "explanation": "नियम: n² - 1। 4² - 1 = 16 - 1 = 15। इसी प्रकार 6² - 1 = 36 - 1 = 35।"
    },
    {
        "topic": "सादृश्यता (अक्षर) / Letter Analogy",
        "question_hi": "AB : ZY : : CD : ?",
        "question_en": "AB : ZY : : CD : ?",
        "options": ["XW", "WX", "VU", "UV"],
        "correct": "A",
        "explanation": "विपरीत अक्षर (Opposite letters): A->Z, B->Y। इसी प्रकार C->X, D->W अर्थात 'XW'।"
    },
    {
        "topic": "सादृश्यता (विज्ञान) / Science Analogy",
        "question_hi": "हृदय : कार्डियोलॉजी : : मस्तिष्क : ?",
        "question_en": "Heart : Cardiology : : Brain : ?",
        "options": ["न्यूरोलॉजी / Neurology", "नेफ्रोलॉजी / Nephrology", "डर्मेटोलॉजी / Dermatology", "ऑप्टिक्स / Optics"],
        "correct": "A",
        "explanation": "हृदय के अध्ययन को कार्डियोलॉजी कहते हैं, तथा मस्तिष्क व तंत्रिका तंत्र के अध्ययन को न्यूरोलॉजी कहते हैं।"
    },
    {
        "topic": "सादृश्यता (संख्या घन) / Cube Analogy",
        "question_hi": "4 : 64 : : 5 : ?",
        "question_en": "4 : 64 : : 5 : ?",
        "options": ["100", "125", "150", "225"],
        "correct": "B",
        "explanation": "4³ = 64, इसी प्रकार 5³ = 125।"
    },
    {
        "topic": "सादृश्यता (कार्यकर्ता-कार्यस्थल) / Worker & Workplace",
        "question_hi": "शिक्षक : विद्यालय : : डॉक्टर : ?",
        "question_en": "Teacher : School : : Doctor : ?",
        "options": ["अदालत / Court", "अस्पताल / Hospital", "कारखाना / Factory", "स्टेडियम / Stadium"],
        "correct": "B",
        "explanation": "शिक्षक विद्यालय में कार्य करता है, उसी प्रकार डॉक्टर अस्पताल में कार्य करता है।"
    },
    {
        "topic": "सादृश्यता (अक्षर +3) / Letter Analogy",
        "question_hi": "CAT : FDW : : DOG : ?",
        "question_en": "CAT : FDW : : DOG : ?",
        "options": ["GRJ", "GPH", "FQH", "GQI"],
        "correct": "A",
        "explanation": "प्रत्येक अक्षर में +3: C(+3)=F, A(+3)=D, T(+3)=W। अतः D(+3)=G, O(+3)=R, G(+3)=J => 'GRJ'।"
    },
    {
        "topic": "सादृश्यता (मापन यंत्र) / Measuring Instrument",
        "question_hi": "ओडोमीटर : दूरी : : सिस्मोग्राफ : ?",
        "question_en": "Odometer : Distance : : Seismograph : ?",
        "options": ["तापमान / Temperature", "भूकंप की तीव्रता / Earthquake", "वर्षा / Rainfall", "वायुदाब / Pressure"],
        "correct": "B",
        "explanation": "ओडोमीटर से वाहनों द्वारा चली दूरी मापी जाती है, सिस्मोग्राफ से भूकंप की तीव्रता मापी जाती है।"
    },
    {
        "topic": "सादृश्यता (संख्या संक्रिया) / Operation Analogy",
        "question_hi": "6 : 36 : : 9 : ?",
        "question_en": "6 : 36 : : 9 : ?",
        "options": ["72", "81", "90", "99"],
        "correct": "B",
        "explanation": "6² = 36, इसी प्रकार 9² = 81।"
    },
    {
        "topic": "सादृश्यता (समानार्थी) / Synonym Analogy",
        "question_hi": "विशाल : बड़ा : : लघु : ?",
        "question_en": "Huge : Big : : Tiny : ?",
        "options": ["छोटा / Small", "लंबा / Long", "ऊँचा / High", "भारी / Heavy"],
        "correct": "A",
        "explanation": "विशाल और बड़ा समानार्थी हैं, उसी प्रकार लघु का समानार्थी छोटा (Small) है।"
    },
    {
        "topic": "सादृश्यता (संख्या दोगुना + 2) / Analogy Rule",
        "question_hi": "8 : 18 : : 12 : ?",
        "question_en": "8 : 18 : : 12 : ?",
        "options": ["24", "26", "28", "30"],
        "correct": "B",
        "explanation": "नियम: (संख्या × 2) + 2। 8 × 2 + 2 = 18। अतः 12 × 2 + 2 = 24 + 2 = 26।"
    },
    {
        "topic": "सादृश्यता (पशु-बच्चा) / Animal & Offspring",
        "question_hi": "गाय : बछड़ा : : कुत्ता : ?",
        "question_en": "Cow : Calf : : Dog : ?",
        "options": ["मेमना / Lamb", "पिल्ला / Puppy", "शावक / Cub", "बछिया / Heifer"],
        "correct": "B",
        "explanation": "गाय के बच्चे को बछड़ा कहते हैं, कुत्ते के बच्चे को पिल्ला (Puppy) कहते हैं।"
    },
    {
        "topic": "सादृश्यता (वर्णमाला स्थान) / Position Analogy",
        "question_hi": "E : 5 : : J : ?",
        "question_en": "E : 5 : : J : ?",
        "options": ["8", "9", "10", "11"],
        "correct": "C",
        "explanation": "E का वर्णमाला क्रमांक 5 है, J का वर्णमाला क्रमांक 10 है (EJOTY नियम)।"
    },
    {
        "topic": "सादृश्यता (देश-राष्ट्रीय खेल) / Sport Analogy",
        "question_hi": "भारत : हॉकी : : अमेरिका : ?",
        "question_en": "India : Hockey : : USA : ?",
        "options": ["क्रिकेट / Cricket", "बेसबॉल / Baseball", "फुटबॉल / Football", "टेनिस / Tennis"],
        "correct": "B",
        "explanation": "भारत का राष्ट्रीय खेल हॉकी माना जाता है, संयुक्त राज्य अमेरिका का राष्ट्रीय खेल बेसबॉल (Baseball) है।"
    },
    {
        "topic": "सादृश्यता (वर्गमूल) / Root Analogy",
        "question_hi": "49 : 7 : : 121 : ?",
        "question_en": "49 : 7 : : 121 : ?",
        "options": ["9", "10", "11", "12"],
        "correct": "C",
        "explanation": "√49 = 7, इसी प्रकार √121 = 11।"
    },

    # --- Number Series / संख्या श्रृंखला (15 Qs) ---
    {
        "topic": "संख्या श्रृंखला (+6) / Number Series",
        "question_hi": "दी गई श्रेणी में अगला पद ज्ञात कीजिए: 5, 11, 17, 23, 29, ?",
        "question_en": "Find the next term in the series: 5, 11, 17, 23, 29, ?",
        "options": ["33", "35", "37", "39"],
        "correct": "B",
        "explanation": "प्रत्येक पद में +6 की वृद्धि हो रही है: 29 + 6 = 35।"
    },
    {
        "topic": "संख्या श्रृंखला (तिगुना) / Tripling Series",
        "question_hi": "श्रृंखला का अगला पद क्या होगा? 2, 6, 18, 54, ?",
        "question_en": "What will be the next term in the series? 2, 6, 18, 54, ?",
        "options": ["108", "144", "162", "180"],
        "correct": "C",
        "explanation": "प्रत्येक पद 3 गुना (×3) हो रहा है: 54 × 3 = 162।"
    },
    {
        "topic": "संख्या श्रृंखला (वर्ग + 2) / n² + 2 Series",
        "question_hi": "निम्न श्रेणी में लुप्त पद बताइए: 3, 6, 11, 18, 27, ?",
        "question_en": "Find the missing term in: 3, 6, 11, 18, 27, ?",
        "options": ["36", "38", "40", "42"],
        "correct": "B",
        "explanation": "नियम: n² + 2 (1²+2=3, 2²+2=6, 3²+2=11, 4²+2=18, 5²+2=27)। अतः 6² + 2 = 38।"
    },
    {
        "topic": "संख्या श्रृंखला (घटती संख्या) / Decreasing Series",
        "question_hi": "श्रृंखला को पूरा कीजिए: 80, 72, 64, 56, 48, ?",
        "question_en": "Complete the series: 80, 72, 64, 56, 48, ?",
        "options": ["38", "40", "42", "44"],
        "correct": "B",
        "explanation": "प्रत्येक पद में से -8 घट रहा है: 48 - 8 = 40।"
    },
    {
        "topic": "संख्या श्रृंखला (एकांतर) / Alternate Series",
        "question_hi": "श्रृंखला में (?) का मान ज्ञात कीजिए: 10, 50, 15, 45, 20, 40, ?",
        "question_en": "Find the value of (?) in: 10, 50, 15, 45, 20, 40, ?",
        "options": ["22", "25", "30", "35"],
        "correct": "B",
        "explanation": "पहली श्रेणी: 10, 15, 20, 25 (+5)। दूसरी श्रेणी: 50, 45, 40 (-5)। अतः 20 + 5 = 25।"
    },
    {
        "topic": "संख्या श्रृंखला (गुणा व घटाना) / Series Pattern",
        "question_hi": "श्रेणी का अगला पद क्या होगा? 3, 5, 9, 17, 33, ?",
        "question_en": "What is the next term in the series? 3, 5, 9, 17, 33, ?",
        "options": ["55", "63", "65", "67"],
        "correct": "C",
        "explanation": "नियम: (पिछला पद × 2) - 1। 3×2-1=5, 5×2-1=9, 9×2-1=17, 17×2-1=33, 33×2-1=65।"
    },
    {
        "topic": "संख्या श्रृंखला (अंतर दुगुना) / Doubling Gap",
        "question_hi": "दी गई श्रेणी में अगला पद बताइए: 1, 3, 7, 15, 31, ?",
        "question_en": "State the next term in the series: 1, 3, 7, 15, 31, ?",
        "options": ["57", "61", "63", "65"],
        "correct": "C",
        "explanation": "अंतर क्रमशः +2, +4, +8, +16, +32 है: 31 + 32 = 63।"
    },
    {
        "topic": "संख्या श्रृंखला (घन + 1) / n³ + 1 Series",
        "question_hi": "श्रृंखला में (?) के स्थान पर संख्या ज्ञात कीजिए: 2, 9, 28, 65, ?",
        "question_en": "Find the number replacing (?) in: 2, 9, 28, 65, ?",
        "options": ["120", "124", "126", "130"],
        "correct": "C",
        "explanation": "नियम: n³ + 1 (1³+1=2, 2³+1=9, 3³+1=28, 4³+1=65)। अगला पद 5³ + 1 = 126।"
    },
    {
        "topic": "संख्या श्रृंखला (अभाज्य संख्या अंतर) / Prime Gaps",
        "question_hi": "निम्न श्रेणी को पूरा कीजिए: 2, 4, 7, 12, 19, ?",
        "question_en": "Complete the series: 2, 4, 7, 12, 19, ?",
        "options": ["28", "30", "31", "32"],
        "correct": "B",
        "explanation": "अंतर क्रमशः अभाज्य संख्याएं हैं: +2, +3, +5, +7, अगला अंतर +11 होगा: 19 + 11 = 30।"
    },
    {
        "topic": "संख्या श्रृंखला (आधा होना) / Halving Series",
        "question_hi": "श्रृंखला का अगला पद क्या होगा? 128, 64, 32, 16, 8, ?",
        "question_en": "What will be the next term? 128, 64, 32, 16, 8, ?",
        "options": ["2", "4", "6", "0"],
        "correct": "B",
        "explanation": "प्रत्येक पद 2 से विभाजित (÷2) हो रहा है: 8 ÷ 2 = 4।"
    },
    {
        "topic": "संख्या श्रृंखला (विषम संख्याएं) / Odd Series",
        "question_hi": "दी गई श्रेणी में अगला पद बताइए: 13, 17, 21, 25, 29, ?",
        "question_en": "Find the next term in: 13, 17, 21, 25, 29, ?",
        "options": ["31", "33", "35", "37"],
        "correct": "B",
        "explanation": "प्रत्येक पद में +4 जुड़ रहा है: 29 + 4 = 33।"
    },
    {
        "topic": "संख्या श्रृंखला (गुणा 2 और 3) / Alternating Multipliers",
        "question_hi": "श्रृंखला में लुप्त पद ज्ञात कीजिए: 2, 4, 12, 48, 240, ?",
        "question_en": "Find the missing term: 2, 4, 12, 48, 240, ?",
        "options": ["1200", "1440", "1680", "1920"],
        "correct": "B",
        "explanation": "गुणा क्रमशः: ×2, ×3, ×4, ×5, ×6। 240 × 6 = 1440।"
    },
    {
        "topic": "संख्या श्रृंखला (दशमलव) / Decimal Series",
        "question_hi": "निम्न श्रेणी का अगला पद क्या होगा? 0.5, 1.5, 4.5, 13.5, ?",
        "question_en": "What is the next term in: 0.5, 1.5, 4.5, 13.5, ?",
        "options": ["27.0", "35.5", "40.5", "42.0"],
        "correct": "C",
        "explanation": "प्रत्येक पद 3 गुना हो रहा है (×3): 13.5 × 3 = 40.5।"
    },
    {
        "topic": "संख्या श्रृंखला (वर्ग अंतर) / Square Differences",
        "question_hi": "श्रेणी में (?) के स्थान पर संख्या बताइए: 1, 2, 6, 15, 31, ?",
        "question_en": "State the number in place of (?): 1, 2, 6, 15, 31, ?",
        "options": ["46", "52", "56", "60"],
        "correct": "C",
        "explanation": "अंतर क्रमशः पूर्ण वर्ग संख्याएं हैं: +1², +2², +3², +4², +5² => 31 + 25 = 56।"
    },
    {
        "topic": "संख्या श्रृंखला (त्रि-पदीय योग) / Tribonacci",
        "question_hi": "श्रेणी को पूरा कीजिए: 1, 2, 3, 6, 11, 20, 37, ?",
        "question_en": "Complete the series: 1, 2, 3, 6, 11, 20, 37, ?",
        "options": ["58", "64", "68", "72"],
        "correct": "C",
        "explanation": "प्रत्येक पद पिछले तीन पदों का योग है: 11 + 20 + 37 = 68।"
    },

    # --- Letter Series & Coding-Decoding / अक्षर व कूट (15 Qs) ---
    {
        "topic": "अक्षर श्रृंखला (+3) / Letter Series",
        "question_hi": "दी गई अक्षर श्रेणी में अगला पद क्या होगा? B, E, H, K, N, ?",
        "question_en": "What is the next term in the letter series? B, E, H, K, N, ?",
        "options": ["P", "Q", "R", "S"],
        "correct": "B",
        "explanation": "प्रत्येक अक्षर में +3: N(14) + 3 = Q(17)।"
    },
    {
        "topic": "अक्षर श्रृंखला (-3) / Backward Letter Series",
        "question_hi": "श्रेणी को पूरा कीजिए: Z, W, T, Q, N, ?",
        "question_en": "Complete the series: Z, W, T, Q, N, ?",
        "options": ["J", "K", "L", "M"],
        "correct": "B",
        "explanation": "उल्टे क्रम में -3: N(14) - 3 = K(11)।"
    },
    {
        "topic": "कोडिंग-डिकोडिंग (+2) / Coding",
        "question_hi": "यदि 'BIRD' को 'DKTF' लिखा जाता है, तो उसी कूट में 'FISH' को क्या लिखा जाएगा?",
        "question_en": "If 'BIRD' is coded as 'DKTF', how will 'FISH' be coded?",
        "options": ["HKUJ", "HKTK", "HLTJ", "GKTJ"],
        "correct": "A",
        "explanation": "प्रत्येक अक्षर में +2: F(+2)=H, I(+2)=K, S(+2)=U, H(+2)=J => 'HKUJ'।"
    },
    {
        "topic": "कोडिंग (उल्टा क्रम) / Reverse Coding",
        "question_hi": "यदि 'KUMAR' को 'RAMUK' लिखा जाता है, तो 'SAGAR' को क्या लिखा जाएगा?",
        "question_en": "If 'KUMAR' is written as 'RAMUK', how will 'SAGAR' be written?",
        "options": ["RAGAS", "RAGSA", "RAGAZ", "RAGAR"],
        "correct": "A",
        "explanation": "अक्षरों को ठीक उल्टे क्रम (Reverse order) में लिखा गया है: S-A-G-A-R को उल्टा करने पर 'RAGAS'।"
    },
    {
        "topic": "कोडिंग (क्रमांक योग) / Position Sum Code",
        "question_hi": "यदि 'CAT' = 24 और 'DOG' = 26 हो, तो 'PIG' का मान क्या होगा?",
        "question_en": "If 'CAT' = 24 and 'DOG' = 26, then what is the value of 'PIG'?",
        "options": ["30", "32", "34", "36"],
        "correct": "B",
        "explanation": "अक्षर क्रमांकों का योग: P(16) + I(9) + G(7) = 32।"
    },
    {
        "topic": "अक्षर युग्म श्रृंखला / Letter Pairs",
        "question_hi": "निम्न में अगला पद बताइए: ZA, YB, XC, WD, ?",
        "question_en": "Find the next term: ZA, YB, XC, WD, ?",
        "options": ["VE", "EV", "UF", "VF"],
        "correct": "A",
        "explanation": "पहला अक्षर पीछे घट रहा है (W->V) और दूसरा आगे बढ़ रहा है (D->E) => 'VE'।"
    },
    {
        "topic": "कोडिंग (-2) / Subtraction Coding",
        "question_hi": "यदि 'COLD' को 'AMJB' लिखा जाता है, तो 'HOT' का कोड क्या होगा?",
        "question_en": "If 'COLD' is coded as 'AMJB', what is the code for 'HOT'?",
        "options": ["FMR", "FMS", "ENR", "GLS"],
        "correct": "A",
        "explanation": "प्रत्येक अक्षर में से -2: H-2=F, O-2=M, T-2=R => 'FMR'।"
    },
    {
        "topic": "अक्षर पुनरावृत्ति / Repeating Letter Pattern",
        "question_hi": "रिक्त स्थान की पूर्ति कीजिए: ab _ a _ ba _ b",
        "question_en": "Fill the blanks in pattern: ab _ a _ ba _ b",
        "options": ["b a b", "a b a", "b b a", "a a b"],
        "correct": "C",
        "explanation": "पैटर्न 'abba / abba' बनाने हेतु 'b, b, a' भरा जाएगा।"
    },
    {
        "topic": "प्रत्यक्ष कूट / Direct Coding",
        "question_hi": "यदि ROSE = 6821 और CHAIR = 73456 हो, तो SEARCH का कोड क्या होगा?",
        "question_en": "If ROSE = 6821 and CHAIR = 73456, what is the code for SEARCH?",
        "options": ["214673", "214573", "214675", "214763"],
        "correct": "A",
        "explanation": "प्रत्यक्ष मिलान: S=2, E=1, A=4, R=6, C=7, H=3 => 214673।"
    },
    {
        "topic": "अक्षर-संख्या कोड / Alphanumeric Code",
        "question_hi": "यदि C = 3 और CAT = 24 हो, तो POLICE का मान क्या होगा?",
        "question_en": "If C = 3 and CAT = 24, what is the numerical value of POLICE?",
        "options": ["56", "60", "64", "68"],
        "correct": "B",
        "explanation": "POLICE = P(16) + O(15) + L(12) + I(9) + C(3) + E(5) = 60।"
    },
    {
        "topic": "अक्षर श्रृंखला (स्वर) / Vowel Series",
        "question_hi": "दी गई श्रेणी में अगला अक्षर क्या होगा? A, E, I, O, ?",
        "question_en": "What is the next letter in the series? A, E, I, O, ?",
        "options": ["P", "T", "U", "V"],
        "correct": "C",
        "explanation": "यह अंग्रेजी वर्णमाला के पांचों स्वरों (Vowels: A, E, I, O, U) की श्रेणी है, अतः अगला 'U' होगा।"
    },
    {
        "topic": "कोडिंग (विपरीत कूट) / Reverse Code",
        "question_hi": "यदि 'BOY' को 'YLB' लिखा जाता है, तो 'GIRL' को क्या लिखा जाएगा?",
        "question_en": "If 'BOY' is coded as 'YLB', how will 'GIRL' be coded?",
        "options": ["TRIP", "TROI", "TRIO", "SQHO"],
        "correct": "C",
        "explanation": "विपरीत अक्षर (Opposites): G->T, I->R, R->I, L->O => 'TRIO'।"
    },
    {
        "topic": "अक्षर श्रृंखला (कूद श्रेणी) / Step Series",
        "question_hi": "श्रृंखला में (?) के स्थान पर क्या आएगा? A, D, I, P, ?",
        "question_en": "What replaces (?) in the series: A, D, I, P, ?",
        "options": ["W", "X", "Y", "Z"],
        "correct": "C",
        "explanation": "वर्ग स्थान: A(1=1²), D(4=2²), I(9=3²), P(16=4²), अतः अगला 25 = 5² अर्थात 'Y' होगा।"
    },
    {
        "topic": "शब्द प्रतिस्थापन / Substitution",
        "question_hi": "यदि 'पेन' को 'किताब', 'किताब' को 'मेज' और 'मेज' को 'कलम' कहें, तो हम क्या पढ़ेंगे?",
        "question_en": "If 'Pen' is 'Book', 'Book' is 'Table', what do we read?",
        "options": ["पेन / Pen", "किताब / Book", "मेज / Table", "कलम / Pencil"],
        "correct": "C",
        "explanation": "हम 'किताब' पढ़ते हैं, परंतु किताब को यहाँ 'मेज' कहा गया है। अतः उत्तर 'मेज' होगा।"
    },
    {
        "topic": "अक्षर समूह श्रृंखला / Triad Series",
        "question_hi": "श्रृंखला को पूरा कीजिए: ABC, DEF, GHI, ?",
        "question_en": "Complete the series: ABC, DEF, GHI, ?",
        "options": ["JKL", "KLM", "LMN", "IJK"],
        "correct": "A",
        "explanation": "3-3 अक्षरों के लगातार समूह: GHI के बाद JKL आएगा।"
    },

    # --- Missing Numbers & Math Operations / लुप्त संख्या व गणितीय संक्रियाएं (15 Qs) ---
    {
        "topic": "लुप्त संख्या (मैट्रिक्स योग) / Missing Number",
        "question_hi": "मैट्रिक्स में लुप्त संख्या ज्ञात कीजिए: [4, 5, 20], [6, 7, 42], [8, 9, ?]",
        "question_en": "Find the missing number in the matrix: [4, 5, 20], [6, 7, 42], [8, 9, ?]",
        "options": ["64", "72", "81", "90"],
        "correct": "B",
        "explanation": "नियम: पहली दो संख्याओं का गुणनफल = तीसरी संख्या। 8 × 9 = 72।"
    },
    {
        "topic": "लुप्त संख्या (वृत्त चक्र) / Circle Pattern",
        "question_hi": "वृत्त के चार खंडों में 3, 5, 8 और (?) लिखे हैं (अंतर +2, +3, +4)। लुप्त संख्या क्या होगी?",
        "question_en": "In a circle with segments 3, 5, 8 and (?), what is the missing number?",
        "options": ["10", "11", "12", "14"],
        "correct": "C",
        "explanation": "अंतर +2 (3+2=5), +3 (5+3=8), अगला अंतर +4 होगा: 8 + 4 = 12।"
    },
    {
        "topic": "गणितीय संक्रियाएं / BODMAS",
        "question_hi": "यदि '+' का अर्थ '×' और '×' का अर्थ '-' हो, तो 10 + 5 × 20 का मान क्या होगा?",
        "question_en": "If '+' means '×' and '×' means '-', what is the value of 10 + 5 × 20?",
        "options": ["25", "30", "35", "40"],
        "correct": "B",
        "explanation": "चिन्ह बदलने पर: 10 × 5 - 20 = 50 - 20 = 30।"
    },
    {
        "topic": "लुप्त संख्या (त्रिभुज) / Triangle Puzzle",
        "question_hi": "त्रिभुज शीर्षों 4, 5, 6 का योग 15 केंद्र में है। शीर्ष 7, 8, 9 होने पर केंद्र में क्या होगा?",
        "question_en": "Triangle with vertices 4, 5, 6 has center 15 (sum). Vertices 7, 8, 9 gives center:",
        "options": ["22", "24", "26", "28"],
        "correct": "B",
        "explanation": "तीनों शीर्षों का योग: 7 + 8 + 9 = 24।"
    },
    {
        "topic": "गणितीय संक्रियाएं (चिन्ह प्रतिस्थापन) / Symbol Operation",
        "question_hi": "यदि 'A' = '+', 'B' = '-', 'C' = '×', तो 5 C 6 A 8 B 4 का मान क्या होगा?",
        "question_en": "If 'A' = '+', 'B' = '-', 'C' = '×', what is 5 C 6 A 8 B 4?",
        "options": ["30", "32", "34", "36"],
        "correct": "C",
        "explanation": "5 × 6 + 8 - 4 = 30 + 8 - 4 = 34।"
    },
    {
        "topic": "लुप्त संख्या (वर्ग अंतर) / Square Difference",
        "question_hi": "यदि 5² - 3² = 16, 6² - 4² = 20 हो, तो 7² - 5² का मान क्या होगा?",
        "question_en": "If 5² - 3² = 16, 6² - 4² = 20, then what is 7² - 5²?",
        "options": ["22", "24", "26", "28"],
        "correct": "B",
        "explanation": "7² - 5² = 49 - 25 = 24।"
    },
    {
        "topic": "गणितीय संक्रियाएं (भाग और गुणा) / Division & Multiply",
        "question_hi": "यदि '÷' का अर्थ '+' और '+' का अर्थ '÷' हो, तो 30 + 5 ÷ 10 का मान क्या होगा?",
        "question_en": "If '÷' means '+' and '+' means '÷', what is 30 + 5 ÷ 10?",
        "options": ["12", "14", "16", "18"],
        "correct": "C",
        "explanation": "30 ÷ 5 + 10 = 6 + 10 = 16।"
    },
    {
        "topic": "लुप्त संख्या (मैट्रिक्स वर्ग) / Square Grid",
        "question_hi": "मैट्रिक्स में (?) का मान ज्ञात कीजिए: [2, 4, 16], [3, 9, 81], [4, 16, ?]",
        "question_en": "Find (?) in the matrix: [2, 4, 16], [3, 9, 81], [4, 16, ?]",
        "options": ["196", "225", "256", "289"],
        "correct": "C",
        "explanation": "दूसरी संख्या का वर्ग = तीसरी संख्या। 16² = 256।"
    },
    {
        "topic": "गणितीय संक्रियाएं (समीकरण चयन) / Equation Selection",
        "question_hi": "समीकरण 18 ? 3 ? 2 = 8 में प्रश्नचिन्हों के स्थान पर कौन-से चिन्ह उपयुक्त होंगे?",
        "question_en": "Which signs will satisfy 18 ? 3 ? 2 = 8?",
        "options": ["÷ और + / ÷ and +", "× और - / × and -", "+ और - / + and -", "- और + / - and +"],
        "correct": "A",
        "explanation": "18 ÷ 3 + 2 = 6 + 2 = 8।"
    },
    {
        "topic": "लुप्त संख्या (क्रॉस गुणन) / Cross Product",
        "question_hi": "क्रॉस में ऊपर 6, नीचे 4 (गुणा 24) और बाएँ 8, दाएँ 3 (गुणा 24) है। यदि बाएँ 12 हो तो दाएँ क्या होगा?",
        "question_en": "In a cross, 6×4=24 and 8×3=24. If left is 12, what should be on right to get 24?",
        "options": ["1", "2", "3", "4"],
        "correct": "B",
        "explanation": "12 × 2 = 24, अतः दाएँ 2 होना चाहिए।"
    },
    {
        "topic": "गणितीय संक्रियाएं / Evaluation",
        "question_hi": "यदि '-' का अर्थ 'गुणा' और '×' का अर्थ 'जोड़' हो, तो 8 - 4 × 10 = ?",
        "question_en": "If '-' means '×' and '×' means '+', then 8 - 4 × 10 = ?",
        "options": ["32", "42", "52", "62"],
        "correct": "B",
        "explanation": "8 × 4 + 10 = 32 + 10 = 42।"
    },
    {
        "topic": "लुप्त संख्या (घटाना व गुणा) / Pattern",
        "question_hi": "यदि (8 - 3) × 4 = 20, (10 - 4) × 4 = 24 हो, तो (12 - 5) × 4 = ?",
        "question_en": "If (8 - 3) × 4 = 20, (10 - 4) × 4 = 24, then (12 - 5) × 4 = ?",
        "options": ["24", "28", "32", "36"],
        "correct": "B",
        "explanation": "(12 - 5) × 4 = 7 × 4 = 28।"
    },
    {
        "topic": "गणितीय संक्रियाएं / BODMAS Order",
        "question_hi": "यदि '+' = '÷', '-' = '+', '×' = '-', '÷' = '×' हो, तो 24 + 6 ÷ 3 - 5 = ?",
        "question_en": "If '+' = '÷', '-' = '+', '×' = '-', '÷' = '×', then 24 + 6 ÷ 3 - 5 = ?",
        "options": ["15", "17", "19", "21"],
        "correct": "B",
        "explanation": "24 ÷ 6 × 3 + 5 = 4 × 3 + 5 = 12 + 5 = 17।"
    },
    {
        "topic": "लुप्त संख्या (मध्य औसत) / Mean Puzzle",
        "question_hi": "चार संख्याओं 12, 18, 24, 30 का समांतर माध्य केंद्र में है। केंद्र संख्या क्या होगी?",
        "question_en": "The arithmetic mean of 12, 18, 24, 30 is at center. What is the center number?",
        "options": ["18", "20", "21", "24"],
        "correct": "C",
        "explanation": "माध्य = (12 + 18 + 24 + 30) ÷ 4 = 84 ÷ 4 = 21।"
    },
    {
        "topic": "गणितीय संक्रियाएं / Simple Logic",
        "question_hi": "यदि 6 * 4 = 24 और 6 @ 4 = 10 हो, तो 8 * 5 @ 10 का मान क्या होगा?",
        "question_en": "If 6 * 4 = 24 and 6 @ 4 = 10, what is 8 * 5 @ 10?",
        "options": ["40", "45", "50", "60"],
        "correct": "C",
        "explanation": "* का अर्थ गुणा और @ का अर्थ जोड़ है: 8 × 5 + 10 = 40 + 10 = 50।"
    },

    # --- Relations, Direction, Venn, Clock & Non-Verbal (15 Qs) ---
    {
        "topic": "रक्त संबंध / Blood Relations",
        "question_hi": "राजीव की बहन नीता है। नीता के पिता महेश हैं। महेश का राजीव से क्या संबंध है?",
        "question_en": "Rajiv's sister is Nita. Nita's father is Mahesh. What is Mahesh to Rajiv?",
        "options": ["चाचा / Uncle", "भाई / Brother", "पिता / Father", "दादा / Grandfather"],
        "correct": "C",
        "explanation": "बहन के पिता स्वयं के भी पिता होते हैं। अतः महेश राजीव के पिता (Father) हैं।"
    },
    {
        "topic": "दिशा परीक्षण / Direction Sense",
        "question_hi": "सूर्यास्त के समय पश्चिम की ओर मुँह करके खड़े होने पर आपकी दाईं ओर कौन-सी दिशा होगी?",
        "question_en": "Facing West at sunset, which direction will be to your right?",
        "options": ["उत्तर / North", "दक्षिण / South", "पूर्व / East", "उत्तर-पश्चिम / North-West"],
        "correct": "A",
        "explanation": "पश्चिम की ओर सम्मुख खड़े होने पर दायाँ हाथ उत्तर (North) दिशा की ओर होता है।"
    },
    {
        "topic": "वेन आरेख / Venn Diagram",
        "question_hi": "[ वाहन, कार, बस ] का सही वेन आरेख कौन-सा है?",
        "question_en": "Which Venn diagram correctly represents [ Vehicles, Car, Bus ]?",
        "options": ["एक बड़े वृत्त में दो अलग वृत्त / Two separate inside one", "तीन संकेंद्रीय वृत्त / Three concentric", "तीनों प्रतिच्छेदी / Three overlapping", "तीन अलग वृत्त / Three separate"],
        "correct": "A",
        "explanation": "कार और बस दोनों अलग-अलग वाहन हैं, पर दोनों वाहन वर्ग में आते हैं।"
    },
    {
        "topic": "रैंकिंग परीक्षण / Ranking Test",
        "question_hi": "50 विद्यार्थियों की कक्षा में अजय का स्थान ऊपर से 20वाँ है। नीचे से उसका स्थान क्या होगा?",
        "question_en": "In a class of 50 students, Ajay ranks 20th from top. What is his rank from bottom?",
        "options": ["30वाँ / 30th", "31वाँ / 31st", "32वाँ / 32nd", "33वाँ / 33rd"],
        "correct": "B",
        "explanation": "नीचे से स्थान = कुल - ऊपर से स्थान + 1 = 50 - 20 + 1 = 31वाँ।"
    },
    {
        "topic": "घड़ी एवं कोण / Clock Angle",
        "question_hi": "घड़ी में ठीक 6:00 बजे दोनों सुइयों के बीच कितने अंश का कोण बनता है?",
        "question_en": "At 6:00, what is the angle between the two hands of a clock?",
        "options": ["90°", "120°", "180° (सरल रेखा)", "360°"],
        "correct": "C",
        "explanation": "6:00 बजे दोनों सुइयां बिल्कुल विपरीत दिशा में एक सीधी रेखा में होती हैं: 6 × 30° = 180°।"
    },
    {
        "topic": "कैलेंडर परीक्षण / Calendar",
        "question_hi": "यदि आज रविवार है, तो आज से ठीक 21 दिन बाद कौन-सा दिन होगा?",
        "question_en": "If today is Sunday, what day of the week will it be after 21 days?",
        "options": ["शुक्रवार / Friday", "शनिवार / Saturday", "रविवार / Sunday", "सोमवार / Monday"],
        "correct": "C",
        "explanation": "21 दिन = 3 पूर्ण सप्ताह (21 ÷ 7 = 3, शेष 0)। अतः वही दिन रविवार ही रहेगा।"
    },
    {
        "topic": "पासा परीक्षण / Dice Opposite",
        "question_hi": "एक मानक पासे पर अंक '2' के विपरीत फलक पर कौन-सा अंक होता है?",
        "question_en": "On a standard dice, what number is on the face opposite to '2'?",
        "options": ["3", "4", "5", "6"],
        "correct": "C",
        "explanation": "मानक पासे के विपरीत फलकों का योग 7 होता है: 7 - 2 = 5।"
    },
    {
        "topic": "दिशा और दूरी / Pythagoras",
        "question_hi": "एक बालक 6 मी उत्तर तथा 8 मी पूर्व में चलता है। प्रारंभिक स्थान से सीधी दूरी क्या है?",
        "question_en": "A boy walks 6m North and 8m East. What is his straight distance from starting point?",
        "options": ["10 मीटर / 10m", "12 मीटर / 12m", "14 मीटर / 14m", "16 मीटर / 16m"],
        "correct": "A",
        "explanation": "√(6² + 8²) = √(36 + 64) = √100 = 10 मीटर।"
    },
    {
        "topic": "रक्त संबंध / Pointing Puzzle",
        "question_hi": "एक तस्वीर देखकर गीता ने कहा, 'यह मेरे दादाजी के इकलौते बेटे की बेटी है।' वह लड़की गीता की क्या है?",
        "question_en": "Looking at a photo, Geeta said, 'She is the daughter of my grandfather's only son.' Who is she?",
        "options": ["गीता स्वयं या उसकी बहन / Geeta herself or sister", "माता / Mother", "चाची / Aunt", "भाभी / Sister-in-law"],
        "correct": "A",
        "explanation": "दादाजी का इकलौता बेटा = गीता के पिता। पिता की बेटी = गीता स्वयं अथवा उसकी बहन।"
    },
    {
        "topic": "वेन आरेख / Venn Relation",
        "question_hi": "[ फर्नीचर, मेज, कुर्सी ] के लिए सर्वोत्तम वेन आरेख कौन-सा है?",
        "question_en": "Which Venn diagram best represents [ Furniture, Table, Chair ]?",
        "options": ["फर्नीचर में मेज व कुर्सी दोनों / Table & Chair inside Furniture", "तीनों अलग / Three separate", "तीनों संकेंद्रीय / Concentric", "दो कटे हुए / Overlapping"],
        "correct": "A",
        "explanation": "मेज और कुर्सी दोनों अलग वस्तुएं हैं, पर दोनों 'फर्नीचर' वर्ग में आती हैं।"
    },
    {
        "topic": "दर्पण प्रतिबिम्ब / Mirror Reflection",
        "question_hi": "अक्षर 'M' का दर्पण प्रतिबिम्ब (Mirror Image) कैसा दिखेगा?",
        "question_en": "What does the mirror image of letter 'M' look like?",
        "options": ["W", "M (अपरिवर्तित / Unchanged)", "N", "E"],
        "correct": "B",
        "explanation": "अक्षर 'M' ऊर्ध्वाधर रूप से सममित (Vertically Symmetric) है, अतः दर्पण में 'M' ही दिखेगा।"
    },
    {
        "topic": "क्रम व्यवस्था / Order Logic",
        "question_hi": "पांच मित्रों में P, Q से भारी है पर R से हल्का है। सबसे भारी R है। सबसे हल्का कौन है यदि S, T से भारी और P से हल्का हो?",
        "question_en": "Among 5 friends, R is heaviest. If R > P > S > T and P > Q, who is lightest?",
        "options": ["P", "Q", "T", "S"],
        "correct": "C",
        "explanation": "क्रम के अंत में T सबसे हल्का होगा।"
    },
    {
        "topic": "घड़ी एवं सुई / Clock Reflection",
        "question_hi": "दर्पण में देखने पर घड़ी में 9:00 बजे का समय क्या दिखाई देगा?",
        "question_en": "What time will a clock show in a mirror when the actual time is 9:00?",
        "options": ["2:00", "3:00", "4:00", "6:00"],
        "correct": "B",
        "explanation": "दर्पण समय = 12:00 - वास्तविक समय = 12:00 - 9:00 = 3:00।"
    },
    {
        "topic": "वेन आरेख / Venn Geometry",
        "question_hi": "[ त्रिभुज, चतुर्भुज, बहुभुज ] का सही आरेख क्या है?",
        "question_en": "Which diagram correctly represents [ Triangle, Quadrilateral, Polygon ]?",
        "options": ["बहुभुज में त्रिभुज व चतुर्भुज / Triangle & Quad inside Polygon", "तीन अलग / Three separate", "तीनों संकेंद्रीय / Concentric", "दो कटे हुए / Linked"],
        "correct": "A",
        "explanation": "त्रिभुज (3 भुजा) और चतुर्भुज (4 भुजा) दोनों 'बहुभुज' (Polygon) के प्रकार हैं।"
    },
    {
        "topic": "आकृति गणना / Count Squares",
        "question_hi": "एक 2×2 ग्रिड में कुल कितने वर्ग (Squares) होते हैं?",
        "question_en": "How many total squares are there in a 2×2 grid?",
        "options": ["4", "5", "6", "8"],
        "correct": "B",
        "explanation": "4 छोटे वर्ग (1×1) + 1 बड़ा वर्ग (2×2) = 1² + 2² = 1 + 4 = 5 वर्ग।"
    }
]

if __name__ == "__main__":
    print(f"Total Additional MAT Questions: {len(UP_MAT_ADDITIONAL)}")
