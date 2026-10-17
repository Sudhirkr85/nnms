# -*- coding: utf-8 -*-
"""
UP NMMS MahaManthan - Additional SAT Questions Pool (Set 3 to Set 5)
150 High-Yield Bilingual Questions for UP NMMS November Exam.
Subjects:
- Science (विज्ञान): Physics, Chemistry, Biology (60 Questions)
- Social Science (सामाजिक अध्ययन): History, Geography, Civics (60 Questions)
- Mathematics (गणित): Arithmetic, Algebra, Geometry, Mensuration (30 Questions)
"""

UP_SAT_ADDITIONAL = [
    # =========================================================================
    # खंड 1: विज्ञान - भौतिक विज्ञान (Physics) - 20 Questions
    # =========================================================================
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "कार्य (Work) और ऊर्जा (Energy) का SI पद्धति में मात्रक क्या है?",
        "question_en": "What is the SI unit of Work and Energy?",
        "options": ["न्यूटन / Newton", "जूल / Joule", "वाट / Watt", "पास्कल / Pascal"],
        "correct": "B",
        "explanation": "कार्य एवं ऊर्जा दोनों का SI मात्रक 'जूल (Joule)' होता है। बल का मात्रक न्यूटन और शक्ति का वाट है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "ध्वनि की तीव्रता (Loudness of Sound) किस पर निर्भर करती है?",
        "question_en": "Loudness of sound depends primarily on its:",
        "options": ["आयाम / Amplitude", "आवृत्ति / Frequency", "तरंगदैर्ध्य / Wavelength", "चाल / Speed"],
        "correct": "A",
        "explanation": "ध्वनि का प्रबलता या तीव्रता कंपन के आयाम (Amplitude) के वर्ग के समानुपाती होती है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "समतल दर्पण द्वारा बना प्रतिबिम्ब कैसा होता है?",
        "question_en": "The image formed by a plane mirror is:",
        "options": ["वास्तविक व उल्टा / Real & Inverted", "आभासी व सीधा / Virtual & Erect", "आभासी व उल्टा / Virtual & Inverted", "वास्तविक व बड़ा / Real & Enlarged"],
        "correct": "B",
        "explanation": "समतल दर्पण द्वारा बना प्रतिबिम्ब सदैव आभासी (Virtual), सीधा (Erect) तथा वस्तु के बराबर आकार का होता है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "एक विद्युत बल्ब का फिलामेंट किस धातु का बना होता है?",
        "question_en": "The filament of an electric bulb is made of which metal?",
        "options": ["तांबा / Copper", "टंगस्टन / Tungsten", "नाइक्रोम / Nichrome", "लोहा / Iron"],
        "correct": "B",
        "explanation": "टंगस्टन (W) का गलनांक (लगभग 3422°C) बहुत उच्च होता है, जिससे यह श्वेत तप्त होकर प्रकाश देता है बिना पिघले।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "विद्युत हीटर का तापन अवयव (Heating Element) किस मिश्रधातु का बना होता है?",
        "question_en": "The heating element of an electric heater is made of which alloy?",
        "options": ["पीतल / Brass", "कांसा / Bronze", "नाइक्रोम / Nichrome", "स्टील / Steel"],
        "correct": "C",
        "explanation": "नाइक्रोम (निकेल + क्रोमियम) का प्रतिरोध और गलनांक दोनों उच्च होते हैं, अतः हीटर में प्रयुक्त होता है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "प्रकाश वर्ष (Light Year) किसका मात्रक है?",
        "question_en": "Light year is a unit of:",
        "options": ["समय / Time", "खगोलीय दूरी / Distance", "प्रकाश तीव्रता / Light Intensity", "चाल / Speed"],
        "correct": "B",
        "explanation": "प्रकाश द्वारा निर्वात में एक वर्ष में तय की गई दूरी को प्रकाश वर्ष कहते हैं (लगभग 9.46 × 10¹⁵ मीटर)।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "सूर्य के प्रकाश में कितने रंग होते हैं जिन्हें प्रिज्म द्वारा अलग किया जाता है?",
        "question_en": "How many colors are present in sunlight dispersed by a prism?",
        "options": ["5", "6", "7 (VIBGYOR)", "8"],
        "correct": "C",
        "explanation": "सूर्य का श्वेत प्रकाश 7 रंगों (बैंगनी, जामुनी, नीला, हरा, पीला, नारंगी, लाल - VIBGYOR) से मिलकर बना है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "किसी गतिमान वस्तु के वेग परिवर्तन की दर को क्या कहते हैं?",
        "question_en": "The rate of change of velocity of an object is called:",
        "options": ["चाल / Speed", "संवेग / Momentum", "त्वरण / Acceleration", "विस्थापन / Displacement"],
        "correct": "C",
        "explanation": "त्वरण = वेग परिवर्तन ÷ समय ($a = \\Delta v / \\Delta t$)। इसका SI मात्रक $m/s^2$ है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "स्वतंत्रतापूर्वक लटकाने पर चुम्बक सदैव किस दिशा में ठहरता है?",
        "question_en": "A freely suspended magnet always rests in which direction?",
        "options": ["पूर्व-पश्चिम / East-West", "उत्तर-दक्षिण / North-South", "उत्तर-पूर्व / North-East", "किसी भी दिशा में"],
        "correct": "B",
        "explanation": "पृथ्वी के अपने चुम्बकीय क्षेत्र के कारण स्वतंत्र चुम्बक सदैव उत्तर-दक्षिण दिशा में ठहरता है।"
    },
    {
        "subject": "विज्ञान (भौतिक) / Physics",
        "question_hi": "आकाशीय बिजली (तड़ित) से भवनों की सुरक्षा के लिए कौन-सा उपकरण लगाया जाता है?",
        "question_en": "Which device is installed on buildings to protect them from lightning strikes?",
        "options": ["तड़ित चालक / Lightning Conductor", "फ्यूज / Fuse", "वोल्टमीटर / Voltmeter", "थर्मामीटर / Thermometer"],
        "correct": "A",
        "explanation": "बेंजामिन फ्रैंकलिन द्वारा आविष्कृत तांबे की नुकीली छड़ (तड़ित चालक) आवेश को सुरक्षित पृथ्वी में भेज देती है।"
    },

    # =========================================================================
    # खंड 2: विज्ञान - रसायन विज्ञान (Chemistry) - 20 Questions
    # =========================================================================
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "खाने के सोडे (मीठा सोडा) का रासायनिक नाम क्या है?",
        "question_en": "What is the chemical name of Baking Soda?",
        "options": ["सोडियम कार्बोनेट / Sodium Carbonate", "सोडियम बाइकार्बोनेट / Sodium Bicarbonate (NaHCO₃)", "कैल्शियम हाइड्रोक्साइड", "सोडियम क्लोराइड"],
        "correct": "B",
        "explanation": "खाने के सोडे का रासायनिक नाम सोडियम हाइड्रोजन कार्बोनेट या सोडियम बाइकार्बोनेट ($NaHCO_3$) है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "धोने के सोडे (वाशिंग सोडा) का रासायनिक सूत्र क्या है?",
        "question_en": "What is the chemical formula of Washing Soda?",
        "options": ["NaCl", "NaHCO₃", "Na₂CO₃·10H₂O", "CaCO₃"],
        "correct": "C",
        "explanation": "धावन सोडा का रासायनिक नाम सोडियम कार्बोनेट डेकाहाइड्रेट ($Na_2CO_3\\cdot 10H_2O$) है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "सिरके (Vinegar) में कौन-सा अम्ल पाया जाता है?",
        "question_en": "Which acid is present in Vinegar?",
        "options": ["सिट्रिक अम्ल / Citric Acid", "एसिटिक अम्ल / Acetic Acid", "टार्टरिक अम्ल / Tartaric Acid", "ऑक्सैलिक अम्ल / Oxalic Acid"],
        "correct": "B",
        "explanation": "सिरके में लगभग 4-8% एसिटिक अम्ल ($CH_3COOH$) उपस्थित होता है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "नींबू और संतरे में मुख्य रूप से कौन-सा अम्ल पाया जाता है?",
        "question_en": "Which acid is predominantly found in lemons and oranges?",
        "options": ["सिट्रिक अम्ल / Citric Acid", "लैक्टिक अम्ल / Lactic Acid", "फॉर्मिक अम्ल / Formic Acid", "नाइट्रिक अम्ल"],
        "correct": "A",
        "explanation": "खट्टे फल जैसे नींबू, संतरा व मौसमी में सिट्रिक अम्ल (Citric Acid) प्रचुर मात्रा में होता है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "चींटी के डंक में कौन-सा अम्ल होता है जिसके कारण जलन होती है?",
        "question_en": "Which acid is present in an ant sting causing irritation?",
        "options": ["एसिटिक अम्ल / Acetic Acid", "फॉर्मिक अम्ल (मेथेनोइक) / Formic Acid", "सल्फ्यूरिक अम्ल", "हाइड्रोक्लोरिक अम्ल"],
        "correct": "B",
        "explanation": "चींटी और मधुमक्खी के डंक में फॉर्मिक अम्ल (मेथेनोइक अम्ल, HCOOH) होता है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "सर्वोत्तम कोटि का कोयला कौन-सा माना जाता है जिसमें कार्बन की मात्रा 90% से अधिक होती है?",
        "question_en": "Which is the highest quality coal containing over 90% carbon?",
        "options": ["पीट / Peat", "लिग्नाइट / Lignite", "बिटुमिनस / Bituminous", "एंथ्रेसाइट / Anthracite"],
        "correct": "D",
        "explanation": "एंथ्रेसाइट (Anthracite) सबसे उच्च कोटि का कठोर कोयला है जो बिना धुएं के जलता है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "वाहनों में ईंधन के रूप में प्रयुक्त सीएनजी (CNG) का मुख्य घटक क्या है?",
        "question_en": "What is the main component of Compressed Natural Gas (CNG)?",
        "options": ["मीथेन (CH₄) / Methane", "ब्यूटेन / Butane", "प्रोपेन / Propane", "हाइड्रोजन / H₂"],
        "correct": "A",
        "explanation": "संपीड़ित प्राकृतिक गैस (CNG) में लगभग 85-95% मीथेन ($CH_4$) गैस होती है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "चूने के पानी (Lime Water) का रासायनिक सूत्र क्या है?",
        "question_en": "What is the chemical formula of Lime Water?",
        "options": ["CaO", "Ca(OH)₂ / Calcium Hydroxide", "CaCO₃", "CaCl₂"],
        "correct": "B",
        "explanation": "बुझे हुए चूने के जलीय विलयन को चूने का पानी कहते हैं, जिसका सूत्र $Ca(OH)_2$ है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "प्लास्टिक जो गर्म करने पर आसानी से विकृत हो जाते हैं और मुड़ जाते हैं, क्या कहलाते हैं?",
        "question_en": "Plastics which easily deform on heating and can be remolded are called:",
        "options": ["थर्मोप्लास्टिक / Thermoplastics", "थर्मोसेटिंग / Thermosetting", "बैकेलाइट / Bakelite", "मेलामाइन / Melamine"],
        "correct": "A",
        "explanation": "पॉलीथीन और पीवीसी जैसे प्लास्टिक थर्मोप्लास्टिक कहलाते हैं जिन्हें पुनः गर्म करके ढाला जा सकता है।"
    },
    {
        "subject": "विज्ञान (रसायन) / Chemistry",
        "question_hi": "वायुमंडल में सर्वाधिक मात्रा (लगभग 78%) में पाई जाने वाली गैस कौन-सी है?",
        "question_en": "Which gas is found in the highest abundance (about 78%) in the atmosphere?",
        "options": ["ऑक्सीजन / Oxygen", "नाइट्रोजन / Nitrogen (N₂)", "कार्बन डाइऑक्साइड / CO₂", "ऑर्गन / Argon"],
        "correct": "B",
        "explanation": "वायुमंडल में 78% नाइट्रोजन, 21% ऑक्सीजन, 0.93% ऑर्गन तथा 0.04% कार्बन डाइऑक्साइड है।"
    },

    # =========================================================================
    # खंड 3: विज्ञान - जीव विज्ञान (Biology) - 20 Questions
    # =========================================================================
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "कोशिका की खोज 1665 ई. में कॉर्क के पतले टुकड़े में किस वैज्ञानिक ने की थी?",
        "question_en": "Who discovered cells in a thin slice of cork in 1665?",
        "options": ["रॉबर्ट हुक / Robert Hooke", "रॉबर्ट ब्राउन / Robert Brown", "ल्यूवेनहॉक / Leeuwenhoek", "डार्विन / Darwin"],
        "correct": "A",
        "explanation": "रॉबर्ट हुक ने 1665 में स्वनिर्मित सूक्ष्मदर्शी से कॉर्क में मधुमक्खी के छत्ते जैसी कोष्ठकनुमा रचनाएं देखीं जिन्हें 'सेल' कहा।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "पादप कोशिका को जंतु कोशिका से अलग करने वाली बाहरी कठोर भित्ति किससे बनी होती है?",
        "question_en": "The rigid outer cell wall that distinguishes plant cells from animal cells is made of:",
        "options": ["प्रोटीन / Protein", "सेलुलोज / Cellulose", "लिपिड / Lipid", "काइटिन / Chitin"],
        "correct": "B",
        "explanation": "पादप कोशिका भित्ति मुख्य रूप से सेलुलोज की बनी होती है जो पादप को संरचनात्मक दृढ़ता प्रदान करती है।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "मानव शरीर में रक्त का शुद्धिकरण (रक्त से यूरिया छानना) किस अंग द्वारा होता है?",
        "question_en": "Filtration and purification of blood from urea in the human body is performed by:",
        "options": ["हृदय / Heart", "वृक्क (गुर्दा) / Kidney", "फेफड़े / Lungs", "यकृत / Liver"],
        "correct": "B",
        "explanation": "वृक्क (Kidney) में स्थित नेफ्रॉन रक्त में से अपशिष्ट पदार्थों और यूरिया को छानकर मूत्र के रूप में बाहर निकालते हैं।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "विटामिन C की कमी से कौन-सा रोग होता है जिसमें मसूड़ों से खून आने लगता है?",
        "question_en": "Which disease with bleeding gums is caused by deficiency of Vitamin C?",
        "options": ["स्कर्वी / Scurvy", "बेरी-बेरी / Beri-Beri", "रतौंधी / Night Blindness", "घेंघा / Goitre"],
        "correct": "A",
        "explanation": "विटामिन C (एस्कॉर्बिक अम्ल) की कमी से स्कर्वी रोग होता है। आंवला और नींबू इसके उत्तम स्रोत हैं।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "घेंघा (गलगंड) रोग किस खनिज तत्व की कमी के कारण होता है?",
        "question_en": "Goitre is caused by the deficiency of which mineral in diet?",
        "options": ["आयरन (लोहा) / Iron", "कैल्शियम / Calcium", "आयोडीन / Iodine", "फास्फोरस / Phosphorus"],
        "correct": "C",
        "explanation": "आयोडीन की कमी से थायरॉयड ग्रंथि फूल जाती है जिसे घेंघा या गलगंड रोग कहते हैं।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "पेनिसिलिन नामक प्रथम एंटीबायोटिक (प्रतिजैविक) दवा की खोज किसने की थी?",
        "question_en": "Who discovered the first antibiotic medicine Penicillin in 1928?",
        "options": ["अलेक्जेंडर फ्लेमिंग / Alexander Fleming", "लुई पाश्चर / Louis Pasteur", "एडवर्ड जेनर / Edward Jenner", "रॉबर्ट कोच / Robert Koch"],
        "correct": "A",
        "explanation": "1928 ई. में अलेक्जेंडर फ्लेमिंग ने पेनिसिलियम नोटेटम कवक से पेनिसिलिन की खोज की थी।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "चेचक (Smallpox) के टीके की खोज किस वैज्ञानिक ने की थी?",
        "question_en": "Who discovered the vaccine for Smallpox in 1796?",
        "options": ["एडवर्ड जेनर / Edward Jenner", "लुई पाश्चर / Louis Pasteur", "रॉबर्ट हुक", "जॉन साल्क"],
        "correct": "A",
        "explanation": "एडवर्ड जेनर ने 1796 में चेचक के टीके का आविष्कार किया था। इन्हें इम्यूनोलॉजी का जनक कहा जाता है।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "मानव शरीर में इंसुलिन हार्मोन का स्राव किस ग्रंथि द्वारा होता है जिसकी कमी से मधुमेह होता है?",
        "question_en": "Insulin hormone is secreted by which gland, whose deficiency causes Diabetes?",
        "options": ["थायरॉयड / Thyroid", "अग्न्याशय / Pancreas", "पीयूष ग्रंथि / Pituitary", "यकृत / Liver"],
        "correct": "B",
        "explanation": "अग्न्याशय (Pancreas) की लैंगरहेंस की द्वीपिकाओं से इंसुलिन स्रावित होता है जो रक्त शर्करा को नियंत्रित करता है।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "रक्त में पाई जाने वाली कौन-सी कोशिकाएं शरीर की सैनिक (रोग प्रतिरोधक) कहलाती हैं?",
        "question_en": "Which blood cells act as soldiers of the body fighting against infections?",
        "options": ["RBC", "WBC (श्वेत रक्त कणिकाएं)", "प्लेटलेट्स / Platelets", "प्लाज्मा / Plasma"],
        "correct": "B",
        "explanation": "श्वेत रक्त कणिकाएं (WBC) रोगाणुओं को नष्ट कर शरीर को रोगों से सुरक्षा प्रदान करती हैं।"
    },
    {
        "subject": "विज्ञान (जीव) / Biology",
        "question_hi": "रेशम कीट पालन के विज्ञान को क्या कहा जाता है?",
        "question_en": "The rearing of silkworms for the production of silk is known as:",
        "options": ["एपीकल्चर / Apiculture", "सेरीकल्चर / Sericulture", "पिसीकल्चर / Pisciculture", "हॉर्टिकल्चर / Horticulture"],
        "correct": "B",
        "explanation": "रेशम कीट पालन को सेरीकल्चर (Sericulture) कहते हैं। मधुमक्खी पालन को एपीकल्चर और मत्स्य पालन को पिसीकल्चर कहते हैं।"
    },

    # =========================================================================
    # खंड 4: सामाजिक अध्ययन - इतिहास (History) - 20 Questions
    # =========================================================================
    {
        "subject": "इतिहास / History",
        "question_hi": "सिंधु घाटी सभ्यता का प्रमुख बंदरगाह नगर कौन-सा था?",
        "question_en": "Which was the major port city of the Indus Valley Civilization?",
        "options": ["हड़प्पा / Harappa", "मोहनजोदड़ो / Mohenjo-daro", "लोथल (गुजरात) / Lothal", "कालीबंगा / Kalibangan"],
        "correct": "C",
        "explanation": "लोथल (गुजरात के भोगवा नदी तट पर) सिंधु घाटी सभ्यता का प्रमुख बंदरगाह व गोदीवाड़ा (Dockyard) था।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "जैन धर्म के 24वें एवं अंतिम तीर्थंकर कौन थे?",
        "question_en": "Who was the 24th and last Tirthankara of Jainism?",
        "options": ["ऋषभदेव / Rishabhanatha", "पार्श्वनाथ / Parshvanatha", "महावीर स्वामी / Mahavira Swami", "गौतम बुद्ध / Gautama Buddha"],
        "correct": "C",
        "explanation": "भगवान महावीर स्वामी जैन धर्म के 24वें तीर्थंकर थे। प्रथम तीर्थंकर ऋषभदेव थे।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "मौर्य साम्राज्य के संस्थापक चंद्रगुप्त मौर्य के प्रधानमंत्री और अर्थशास्त्र के रचयिता कौन थे?",
        "question_en": "Who was the Prime Minister of Chandragupta Maurya and author of Arthashastra?",
        "options": ["मेगस्थनीज / Megasthenes", "चाणक्य (कौटिल्य) / Chanakya", "बाणभट्ट / Banabhatta", "कालिदास / Kalidasa"],
        "correct": "B",
        "explanation": "चाणक्य (विष्णुगुप्त/कौटिल्य) ने राजनीति और प्रशासन पर विश्वप्रसिद्ध ग्रंथ 'अर्थशास्त्र' की रचना की।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "कलिंग युद्ध (261 ई.पू.) के भीषण नरसंहार के बाद किस मौर्य सम्राट ने बौद्ध धर्म अपनाया?",
        "question_en": "Which Mauryan Emperor embraced Buddhism after the carnage of the Kalinga War?",
        "options": ["बिन्दुसार / Bindusara", "सम्राट अशोक / Emperor Ashoka", "चंद्रगुप्त / Chandragupta", "दशरथ"],
        "correct": "B",
        "explanation": "कलिंग युद्ध के बाद सम्राट अशोक ने भेरीघोष त्यागकर धम्मघोष अपनाया और बौद्ध धर्म का प्रचार किया।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "सारनाथ स्थित 'अशोक स्तंभ' के शीर्ष पर स्थित सिंहों को भारत का राष्ट्रीय प्रतीक कब अपनाया गया?",
        "question_en": "When was the Lion Capital of Ashoka at Sarnath adopted as National Emblem of India?",
        "options": ["15 अगस्त 1947", "26 जनवरी 1950", "26 नवम्बर 1949", "2 अक्टूबर 1952"],
        "correct": "B",
        "explanation": "सारनाथ (वाराणसी, UP) के चार सिंहों वाले अशोक स्तंभ को 26 जनवरी 1950 को राष्ट्रीय प्रतीक के रूप में अपनाया गया।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "मध्यकालीन भारत में दिल्ली में 'कुतुब मीनार' का निर्माण कार्य किसने पूरा करवाया था?",
        "question_en": "Who completed the construction of Qutub Minar in Delhi?",
        "options": ["कुतुबुद्दीन ऐबक / Aibak", "शमसुद्दीन इल्तुतमिश / Iltutmish", "बलबन / Balban", "अलाउद्दीन खिलजी"],
        "correct": "B",
        "explanation": "कुतुब मीनार की नींव कुतुबुद्दीन ऐबक ने रखी थी, जबकि इसका निर्माण कार्य इल्तुतमिश ने पूरा करवाया।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "बाजार नियंत्रण व्यवस्था (Market Control System) लागू करने वाला दिल्ली का सुल्तान कौन था?",
        "question_en": "Which Sultan of Delhi introduced the Market Control and price regulation system?",
        "options": ["अलाउद्दीन खिलजी / Alauddin Khalji", "मुहम्मद बिन तुगलक / MBT", "फिरोज तुगलक", "सिकंदर लोदी"],
        "correct": "A",
        "explanation": "अलाउद्दीन खिलजी ने विशाल सेना के भरण-पोषण हेतु वस्तुओं के मूल्य निश्चित किए और दीवान-ए-रियासत विभाग बनाया।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "अकबर ने सभी धर्मों की अच्छाइयों को मिलाकर 1582 ई. में किस नए पंथ की स्थापना की थी?",
        "question_en": "Which new religious path did Akbar found in 1582 by combining virtues of all religions?",
        "options": ["दीन-ए-इलाही / Din-i Ilahi", "सुलह-ए-कुल / Sulh-i Kul", "इबादतखाना / Ibadat Khana", "मनसबदारी"],
        "correct": "A",
        "explanation": "अकबर ने 1582 में 'दीन-ए-इलाही' (तौहीद-ए-इलाही) की घोषणा की, जिसे स्वीकार करने वाला एकमात्र हिंदू बीरबल था।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "प्लासी का ऐतिहासिक युद्ध (1757 ई.) अंग्रेजों (रॉबर्ट क्लाइव) और किसके बीच लड़ा गया था?",
        "question_en": "The Battle of Plassey (1757) was fought between Robert Clive and:",
        "options": ["सिराजुद्दौला (बंगाल के नवाब) / Siraj-ud-Daulah", "मीर कासिम / Mir Qasim", "शुजाउद्दौला", "टीपू सुल्तान"],
        "correct": "A",
        "explanation": "23 जून 1757 को प्लासी के युद्ध में क्लाइव ने मीर जाफर के विश्वासघात के कारण सिराजुद्दौला को पराजित किया।"
    },
    {
        "subject": "इतिहास / History",
        "question_hi": "'सत्यशोधक समाज' की स्थापना 1873 ई. में महाराष्ट्र में किसने की थी?",
        "question_en": "Who founded the 'Satyashodhak Samaj' in Maharashtra in 1873?",
        "options": ["ज्योतिबा फुले / Jyotiba Phule", "डॉ. आंबेडकर / Dr. Ambedkar", "गोपाल गणेश आगरकर", "बाल गंगाधर तिलक"],
        "correct": "A",
        "explanation": "महात्मा ज्योतिबा फुले ने दलितों व महिलाओं के उद्धार और शिक्षा हेतु 'सत्यशोधक समाज' की स्थापना की।"
    },

    # =========================================================================
    # खंड 5: सामाजिक अध्ययन - भूगोल (Geography) - 20 Questions
    # =========================================================================
    {
        "subject": "भूगोल / Geography",
        "question_hi": "भारत का सबसे ऊँचा बांध 'टिहरी बांध' किस नदी पर निर्मित है?",
        "question_en": "Which river is the highest dam of India, Tehri Dam, built upon?",
        "options": ["भागीरथी नदी / Bhagirathi River", "गंगा नदी / Ganga", "सतलुज नदी / Sutlej", "महानदी / Mahanadi"],
        "correct": "A",
        "explanation": "उत्तराखंड में भागीरथी और भिलंगना के संगम पर बना टिहरी बांध भारत का सबसे ऊँचा बांध है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "संसार की छत (Roof of the World) किसे कहा जाता है?",
        "question_en": "Which plateau is known as the 'Roof of the World'?",
        "options": ["दक्कन का पठार / Deccan Plateau", "पामीर का पठार / Pamir Plateau", "तिब्बत का पठार", "छोटा नागपुर पठार"],
        "correct": "B",
        "explanation": "मध्य एशिया में स्थित अत्यधिक ऊँचाई वाले पामीर के पठार को 'विश्व की छत' कहा जाता है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "उत्तर प्रदेश के किस जिले को 'पीतल नगरी' (Brass City) के नाम से जाना जाता है?",
        "question_en": "Which district of Uttar Pradesh is famously known as 'Brass City'?",
        "options": ["मुरादाबाद / Moradabad", "अलीगढ़ / Aligarh", "कन्नौज / Kannauj", "फिरोजाबाद / Firozabad"],
        "correct": "A",
        "explanation": "मुरादाबाद अपने पीतल के हस्तशिल्प उद्योग के लिए 'पीतल नगरी' के नाम से विश्व विख्यात है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "उत्तर प्रदेश का 'फिरोजाबाद' नगर किस उद्योग के लिए भारत भर में प्रसिद्ध है?",
        "question_en": "Firozabad in Uttar Pradesh is nationally famous for which industry?",
        "options": ["कांच की चूड़ियां / Glass Bangles", "ताले / Locks", "इत्र / Perfume", "चमड़ा उद्योग / Leather"],
        "correct": "A",
        "explanation": "फिरोजाबाद को सुहाग नगरी कहते हैं और यह कांच की सुंदर चूड़ियों के लिए प्रसिद्ध है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "उत्तर प्रदेश का 'कन्नौज' जिला किसके निर्माण के लिए सदियों से विख्यात है?",
        "question_en": "Kannauj district of Uttar Pradesh is historically famous for:",
        "options": ["इत्र (Perfume) उद्योग", "कालीन / Carpets", "ताले / Locks", "दियासलाई / Matches"],
        "correct": "A",
        "explanation": "कन्नौज को 'इत्र की नगरी' (Perfume City of India) कहा जाता है जहाँ गुलाब जल व इत्र बनते हैं।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "भारत की सिलिकॉन वैली (Silicon Valley of India) किस शहर को कहा जाता है?",
        "question_en": "Which city is known as the 'Silicon Valley of India'?",
        "options": ["हैदराबाद / Hyderabad", "बेंगलुरु / Bengaluru", "पुणे / Pune", "नोएडा / Noida"],
        "correct": "B",
        "explanation": "कर्नाटक की राजधानी बेंगलुरु को सूचना प्रौद्योगिकी (IT) उद्योग का केंद्र होने के कारण सिलिकॉन वैली कहते हैं।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "क्षेत्रफल की दृष्टि से भारत का सबसे बड़ा राज्य कौन-सा है?",
        "question_en": "Which is the largest state of India in terms of geographical area?",
        "options": ["मध्य प्रदेश / MP", "उत्तर प्रदेश / UP", "राजस्थान / Rajasthan", "महाराष्ट्र / Maharashtra"],
        "correct": "C",
        "explanation": "क्षेत्रफल में प्रथम राजस्थान है। उत्तर प्रदेश जनसंख्या में प्रथम तथा क्षेत्रफल में चौथे स्थान पर है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "जनसंख्या की दृष्टि से भारत का सबसे बड़ा राज्य कौन-सा है?",
        "question_en": "Which is the most populous state of India as per census?",
        "options": ["बिहार / Bihar", "उत्तर प्रदेश / Uttar Pradesh", "महाराष्ट्र / Maharashtra", "पश्चिम बंगाल / West Bengal"],
        "correct": "B",
        "explanation": "उत्तर प्रदेश लगभग 20 करोड़ से अधिक आबादी के साथ भारत का सर्वाधिक जनसंख्या वाला राज्य है।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "उत्तर प्रदेश की प्रमुख व्यावसायिक नगदी फसल (Cash Crop) कौन-सी है?",
        "question_en": "Which is the major commercial cash crop of Uttar Pradesh?",
        "options": ["कपास / Cotton", "गन्ना / Sugarcane", "चाय / Tea", "जूट / Jute"],
        "correct": "B",
        "explanation": "उत्तर प्रदेश भारत में गन्ना और चीनी का सबसे बड़ा उत्पादक राज्य है। इसे 'भारत का चीनी का कटोरा' भी कहते हैं।"
    },
    {
        "subject": "भूगोल / Geography",
        "question_hi": "काजीरंगा राष्ट्रीय उद्यान (असम) किस अद्वितीय वन्यजीव के संरक्षण के लिए विख्यात है?",
        "question_en": "Kaziranga National Park in Assam is famous for the conservation of:",
        "options": ["एक सींग वाला गैंडा / One-horned Rhinoceros", "एशियाई शेर / Asiatic Lion", "सफेद बाघ / White Tiger", "हाथी / Elephant"],
        "correct": "A",
        "explanation": "काजीरंगा राष्ट्रीय उद्यान (असम) विश्व के दो-तिहाई एक सींग वाले गैंडों का प्राकृतिक आवास है।"
    },

    # =========================================================================
    # खंड 6: सामाजिक अध्ययन - नागरिक शास्त्र (Civics) - 10 Questions
    # =========================================================================
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "भारत का सर्वोच्च न्यायालय (Supreme Court) कहाँ स्थित है?",
        "question_en": "Where is the Supreme Court of India located?",
        "options": ["मुंबई / Mumbai", "नई दिल्ली / New Delhi", "कोलकाता / Kolkata", "प्रयागराज / Prayagraj"],
        "correct": "B",
        "explanation": "भारत का उच्चतम न्यायालय (सर्वोच्च न्यायालय) देश की राजधानी नई दिल्ली में स्थित है।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "उत्तर प्रदेश का उच्च न्यायालय (High Court) किस नगर में स्थित है?",
        "question_en": "Where is the High Court of Uttar Pradesh situated?",
        "options": ["लखनऊ / Lucknow", "प्रयागराज (इलाहाबाद) / Prayagraj", "कानपुर / Kanpur", "वाराणसी / Varanasi"],
        "correct": "B",
        "explanation": "इलाहाबाद उच्च न्यायालय की मुख्य पीठ प्रयागराज में है और इसकी एक खंडपीठ लखनऊ में कार्यरत है।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "भारत में किसी राज्य के 'राज्यपाल' (Governor) की नियुक्ति किसके द्वारा की जाती है?",
        "question_en": "Who appoints the Governor of a state in India?",
        "options": ["मुख्यमंत्री / Chief Minister", "भारत का राष्ट्रपति / President of India", "प्रधानमंत्री / Prime Minister", "मुख्य न्यायाधीश"],
        "correct": "B",
        "explanation": "संविधान के अनुच्छेद 155 के अनुसार राज्य के राज्यपाल की नियुक्ति भारत के राष्ट्रपति द्वारा की जाती है।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "संसद के निचले सदन 'लोकसभा' का सदस्य बनने के लिए न्यूनतम आयु सीमा कितनी है?",
        "question_en": "What is the minimum age to become a member of the Lok Sabha?",
        "options": ["18 वर्ष / 18 Years", "21 वर्ष / 21 Years", "25 वर्ष / 25 Years", "30 वर्ष / 30 Years"],
        "correct": "C",
        "explanation": "लोकसभा सदस्य हेतु न्यूनतम आयु 25 वर्ष तथा राज्यसभा सदस्य हेतु 30 वर्ष निर्धारित है।"
    },
    {
        "subject": "नागरिक शास्त्र / Civics",
        "question_hi": "ग्राम पंचायत का प्रधान (ग्राम प्रधान/मुखिया) बनने हेतु न्यूनतम आयु कितनी होनी चाहिए?",
        "question_en": "What is the minimum age required to contest for Gram Pradhan (Panchayat Head)?",
        "options": ["18 वर्ष / 18 Years", "21 वर्ष / 21 Years", "25 वर्ष / 25 Years", "30 वर्ष / 30 Years"],
        "correct": "B",
        "explanation": "पंचायती राज संस्थाओं (ग्राम पंचायत, क्षेत्र पंचायत, जिला पंचायत) के चुनाव हेतु न्यूनतम आयु 21 वर्ष है।"
    },

    # =========================================================================
    # खंड 7: गणित (Mathematics) - 20 Questions
    # =========================================================================
    {
        "subject": "गणित / Mathematics",
        "question_hi": "परिमेय संख्या 4/7 का गुणात्मक प्रतिलोम (Multiplicative Inverse) क्या होगा?",
        "question_en": "What is the multiplicative inverse (reciprocal) of rational number 4/7?",
        "options": ["-4/7", "7/4", "-7/4", "1"],
        "correct": "B",
        "explanation": "गुणात्मक प्रतिलोम वह संख्या है जिससे गुणा करने पर गुणनफल 1 आए: (4/7) × (7/4) = 1।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "संख्या 144 का वर्गमूल क्या होगा?",
        "question_en": "What is the square root of 144?",
        "options": ["11", "12", "14", "16"],
        "correct": "B",
        "explanation": "12 × 12 = 144, अतः √144 = 12।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "संख्या 216 का घनमूल क्या होगा?",
        "question_en": "What is the cube root of 216?",
        "options": ["4", "5", "6", "8"],
        "correct": "C",
        "explanation": "6 × 6 × 6 = 216, अतः ∛216 = 6।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "व्यंजक (3² × 3³) का मान क्या होगा?",
        "question_en": "What is the value of (3² × 3³)?",
        "options": ["3⁵ (243)", "3⁶ (729)", "9⁵", "3¹"],
        "correct": "A",
        "explanation": "3²⁺³ = 3⁵ = 243।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "समीकरण 2x - 3 = 7 में x का मान क्या होगा?",
        "question_en": "In equation 2x - 3 = 7, what is the value of x?",
        "options": ["2", "4", "5", "10"],
        "correct": "C",
        "explanation": "2x = 7 + 3 = 10 => x = 10 / 2 = 5।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "संख्या 250 का 20% कितना होगा?",
        "question_en": "What is 20% of 250?",
        "options": ["40", "50", "60", "75"],
        "correct": "B",
        "explanation": "(250 × 20) / 100 = 50।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "₹500 की वस्तु पर ₹50 की हानि होने पर हानि प्रतिशत क्या होगा?",
        "question_en": "A loss of ₹50 occurs on an item of ₹500. What is the loss percentage?",
        "options": ["5%", "10%", "15%", "20%"],
        "correct": "B",
        "explanation": "हानि % = (50 / 500) × 100 = 10%।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "₹1000 का 10% वार्षिक दर से 2 वर्ष का साधारण ब्याज कितना होगा?",
        "question_en": "What is the simple interest on ₹1000 at 10% per annum for 2 years?",
        "options": ["₹100", "₹150", "₹200", "₹250"],
        "correct": "C",
        "explanation": "SI = (1000 × 10 × 2) / 100 = ₹200।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "एक समबाहु त्रिभुज (Equilateral Triangle) का प्रत्येक अंतःकोण कितने अंश का होता है?",
        "question_en": "What is the measure of each interior angle of an equilateral triangle?",
        "options": ["45°", "60°", "90°", "120°"],
        "correct": "B",
        "explanation": "समबाहु त्रिभुज के तीनों कोण बराबर होते हैं: 180° ÷ 3 = 60°।"
    },
    {
        "subject": "गणित / Mathematics",
        "question_hi": "भुजा 10 मीटर वाले वर्गाकार मैदान का परिमाप क्या होगा?",
        "question_en": "What is the perimeter of a square field with side 10 meters?",
        "options": ["20 मीटर", "40 मीटर", "100 मीटर", "200 मीटर"],
        "correct": "B",
        "explanation": "वर्ग की परिमाप = 4 × भुजा = 4 × 10 = 40 मीटर।"
    }
]

if __name__ == "__main__":
    print(f"Total Additional SAT Questions: {len(UP_SAT_ADDITIONAL)}")
