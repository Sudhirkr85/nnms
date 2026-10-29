import os
import sys
import json
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from build_sst_base import (
    create_base_presentation,
    add_title_slide,
    add_theory_slide,
    add_interactive_mcq_pair,
    add_memory_key_slide,
    add_homework_slide,
    finalize_and_save_presentation,
    MOCK_DIR,
    HISTORY_DIR,
    GEO_DIR
)

# Load master pool of 500 questions
with open('scripts/master_500_questions_pool.json', 'r', encoding='utf-8') as f:
    master_pool = json.load(f)

print(f"Loaded Master Pool: {len(master_pool)} questions")

# Titles and themes for the 10 Mock Tests
TEST_CONFIGS = [
    {
        "num": 1,
        "title": "ऑल इंडिया NMMS संपूर्ण सामाजिक विज्ञान: फुल मॉक टेस्ट 01",
        "sub": "इतिहास, नागरिक शास्त्र एवं भूगोल का 50-प्रश्नों का संपूर्ण अभ्यास (All India Pattern)",
        "badge": "Full Mock Test 01 • सम्पूर्ण सामाजिक विज्ञान (50 प्रश्न)"
    },
    {
        "num": 2,
        "title": "ऑल इंडिया NMMS संपूर्ण सामाजिक विज्ञान: फुल मॉक टेस्ट 02",
        "sub": "इतिहास, नागरिक शास्त्र एवं भूगोल का 50-प्रश्नों का संपूर्ण अभ्यास (All India Pattern)",
        "badge": "Full Mock Test 02 • सम्पूर्ण सामाजिक विज्ञान (50 प्रश्न)"
    },
    {
        "num": 3,
        "title": "ऑल इंडिया NMMS संपूर्ण सामाजिक विज्ञान: फुल मॉक टेस्ट 03",
        "sub": "इतिहास, नागरिक शास्त्र एवं भूगोल का 50-प्रश्नों का संपूर्ण अभ्यास (All India Pattern)",
        "badge": "Full Mock Test 03 • सम्पूर्ण सामाजिक विज्ञान (50 प्रश्न)"
    },
    {
        "num": 4,
        "title": "ऑल इंडिया NMMS संपूर्ण सामाजिक विज्ञान: फुल मॉक टेस्ट 04",
        "sub": "इतिहास, नागरिक शास्त्र एवं भूगोल का 50-प्रश्नों का संपूर्ण अभ्यास (All India Pattern)",
        "badge": "Full Mock Test 04 • सम्पूर्ण सामाजिक विज्ञान (50 प्रश्न)"
    },
    {
        "num": 5,
        "title": "ऑल इंडिया NMMS संपूर्ण सामाजिक विज्ञान: फुल मॉक टेस्ट 05",
        "sub": "इतिहास, नागरिक शास्त्र एवं भूगोल का 50-प्रश्नों का संपूर्ण अभ्यास (All India Pattern)",
        "badge": "Full Mock Test 05 • सम्पूर्ण सामाजिक विज्ञान (50 प्रश्न)"
    },
    {
        "num": 6,
        "title": "ऑल इंडिया NMMS संपूर्ण सामाजिक विज्ञान: फुल मॉक टेस्ट 06",
        "sub": "इतिहास, नागरिक शास्त्र एवं भूगोल का 50-प्रश्नों का संपूर्ण अभ्यास (All India Pattern)",
        "badge": "Full Mock Test 06 • सम्पूर्ण सामाजिक विज्ञान (50 प्रश्न)"
    },
    {
        "num": 7,
        "title": "ऑल इंडिया NMMS संपूर्ण सामाजिक विज्ञान: फुल मॉक टेस्ट 07",
        "sub": "इतिहास, नागरिक शास्त्र एवं भूगोल का 50-प्रश्नों का संपूर्ण अभ्यास (All India Pattern)",
        "badge": "Full Mock Test 07 • सम्पूर्ण सामाजिक विज्ञान (50 प्रश्न)"
    },
    {
        "num": 8,
        "title": "ऑल इंडिया NMMS संपूर्ण सामाजिक विज्ञान: फुल मॉक टेस्ट 08",
        "sub": "इतिहास, नागरिक शास्त्र एवं भूगोल का 50-प्रश्नों का संपूर्ण अभ्यास (All India Pattern)",
        "badge": "Full Mock Test 08 • सम्पूर्ण सामाजिक विज्ञान (50 प्रश्न)"
    },
    {
        "num": 9,
        "title": "ऑल इंडिया NMMS संपूर्ण सामाजिक विज्ञान: फुल मॉक टेस्ट 09",
        "sub": "इतिहास, नागरिक शास्त्र एवं भूगोल का 50-प्रश्नों का संपूर्ण अभ्यास (All India Pattern)",
        "badge": "Full Mock Test 09 • सम्पूर्ण सामाजिक विज्ञान (50 प्रश्न)"
    },
    {
        "num": 10,
        "title": "ऑल इंडिया NMMS संपूर्ण सामाजिक विज्ञान: फुल मॉक टेस्ट 10",
        "sub": "इतिहास, नागरिक शास्त्र एवं भूगोल का 50-प्रश्नों का संपूर्ण अभ्यास (All India Pattern)",
        "badge": "Full Mock Test 10 • ग्रैंड फिनाले महा-मॉक टेस्ट (50 प्रश्न)"
    }
]

def build_single_50q_test(test_idx, cfg, questions_50):
    prs = create_base_presentation()
    total_slides = 104  # 1 Title + 1 Rules + 100 MCQ pairs + 1 Memory + 1 HW + 1 Closing
    
    # 1. Title Slide
    add_title_slide(
        prs,
        class_badge=cfg["badge"],
        main_title=cfg["title"],
        sub_desc=cfg["sub"],
        topics_list=[
            "इतिहास के 20 अति-महत्वपूर्ण प्रश्न",
            "नागरिक शास्त्र एवं संविधान के 15 प्रश्न",
            "भूगोल एवं पर्यावरण के 15 प्रश्न",
            "ऑल इंडिया NMMS 35 में 35 अंक की 100% तैयारी"
        ]
    )

    # 2. Exam Golden Rules Slide
    add_theory_slide(
        prs,
        title=f"मॉक टेस्ट 0{test_idx}: परीक्षा में 35/35 अंक लाने के 4 अचूक नियम",
        points=[
            "नियम 1: प्रश्न को पूरा और ध्यान से पढ़ें — कई बार प्रश्न में 'नहीं है' या 'सत्य नहीं है' छिपा होता है।",
            "नियम 2: ऑप्शन्स का एलिमिनेशन (Elimination Method) — जो विकल्प निश्चित गलत हैं, उन्हें पहले मन में काटें।",
            "नियम 3: समय प्रबंधन (Time Management) — SST के 35 प्रश्नों को हल करने में 25-30 मिनट से अधिक समय न लगाएं।",
            "नियम 4: OMR शीट सावधानी से भरें — NMMS परीक्षा में कोई निगेटिव मार्किंग (Negative Marking) नहीं है, इसलिए सभी 35 प्रश्न हल करें!",
            "नियम 5: सागर सर का मंत्र — नियमित अभ्यास, पिछले वर्षों के प्रश्न (PYQs) और आत्मविश्वास ही सफलता की चाबी है।"
        ],
        slide_num=2,
        total_slides=total_slides
    )

    # 3. 50 Interactive Question Pairs (Slides 3 to 102 = 100 slides)
    curr_slide = 3
    for q_idx, item in enumerate(questions_50):
        q = item["question"]
        opts = item["options"]
        c_opt = item["correct_opt"]
        exp = item["explanation"]
        tag = item.get("tag", "All India NMMS PYQ")

        add_interactive_mcq_pair(
            prs,
            q_num=q_idx + 1,
            question=q,
            options=opts,
            correct_opt=c_opt,
            explanation=exp,
            exam_tag=tag,
            slide_num=curr_slide,
            total_slides=total_slides
        )
        curr_slide += 2

    # 103. Memory Key Slide
    add_memory_key_slide(
        prs,
        title=f"मॉक टेस्ट 0{test_idx}: सागर सर की 1-मिनट मेमोरी चाबी (क्विक फॉर्मूला)",
        key_items=[
            "इतिहास: गजनवी (1025), तराइन (1191/92), पानीपत (1526), 1857 (मेरठ), ब्रह्म समाज (1828), आर्य समाज (1875)",
            "नागरिक शास्त्र: 2 वर्ष 11 माह 18 दिन, प्रारूप समिति (अंबेडकर), 6 मौलिक अधिकार, अनु. 32 (संविधान की आत्मा)",
            "आर.टी.ई. (RTE) = अनु. 21A (86वां संशोधन 2002) | पंचायती राज = 73वां संशोधन 1992 (नागौर, 1959)",
            "भूगोल: शुक्र (भोर का तारा/सबसे गर्म) | पृथ्वी घूर्णन = दिन-रात | परिक्रमण = ऋतुएं | 82½° पूर्व = IST",
            "वायुमंडल: क्षोभमंडल = सभी मौसम घटनाएं | समतापमंडल = हवाई जहाज उड़ान + ओजोन परत | बैरोमीटर = वायुदाब",
            "भारत का भूगोल: गंगा = 2525 किमी | सुंदरवन डेल्टा | काली (रेगुर) मिट्टी = कपास | काला सोना = पेट्रोलियम"
        ],
        slide_num=103,
        total_slides=total_slides
    )

    # 104. Homework / Revision Slide
    add_homework_slide(
        prs,
        hw_questions=[
            f"मॉक टेस्ट 0{test_idx} में आपने 50 में से कितने अंक प्राप्त किए, अपनी डायरी में नोट करें।",
            "जो प्रश्न गलत हुए, उनके सही उत्तर अपनी फेयर कॉपी में 2 बार लिखें।",
            "अगले मॉक टेस्ट के लिए इतिहास, भूगोल और नागरिक शास्त्र के शॉर्ट नोट्स दोहराएं।"
        ],
        slide_num=104,
        total_slides=total_slides
    )

    # Closing Slide (Added dynamically by finalize or as slide 105)
    add_title_slide(
        prs,
        class_badge=f"मॉक टेस्ट 0{test_idx} सम्पन्न! बधाई!",
        main_title="सागर कोचिंग सेंटर — आपकी सफलता, हमारा संकल्प!",
        sub_desc="इस टेस्ट की PDF डाउनलोड करें: sagarcoaching.tech | Helpline: +91 91101 13671",
        topics_list=[
            "YouTube: NMMS King Sagar Sir",
            "App: Sagar Coaching Centre (Play Store)",
            "Website: https://sagarcoaching.tech",
            "Helpline: +91 91101 13671"
        ]
    )

    filename = f"Mock_Test_{test_idx:02d}.pptx"
    finalize_and_save_presentation(prs, filename, MOCK_DIR)

def clean_old_mock_files():
    print("Cleaning up old mock files with question counts in filenames...")
    for f in os.listdir(MOCK_DIR):
        if f.endswith('.pptx') and not (f.startswith('Mock_Test_') and len(f) == 17):  # Mock_Test_XX.pptx is 17 chars
            old_path = os.path.join(MOCK_DIR, f)
            try:
                os.remove(old_path)
                print(f"  Removed old file: {f}")
            except Exception as e:
                print(f"  Could not remove {f}: {e}")

def update_marathon_names():
    print("Updating marathon filenames to clean names without question counts...")
    # History Marathon
    old_hist = os.path.join(HISTORY_DIR, "Class_11_History_Top_60_PYQ_Marathon.pptx")
    new_hist = os.path.join(HISTORY_DIR, "Class_11_History_Grand_Marathon.pptx")
    if os.path.exists(old_hist):
        if os.path.exists(new_hist):
            os.remove(new_hist)
        os.rename(old_hist, new_hist)
        print("  Renamed Class 11 -> Class_11_History_Grand_Marathon.pptx")

    # Geography Marathon
    old_geo = os.path.join(GEO_DIR, "Class_17_Geography_Top_50_PYQ_Marathon.pptx")
    new_geo = os.path.join(GEO_DIR, "Class_17_Geography_Grand_Marathon.pptx")
    if os.path.exists(old_geo):
        if os.path.exists(new_geo):
            os.remove(new_geo)
        os.rename(old_geo, new_geo)
        print("  Renamed Class 17 -> Class_17_Geography_Grand_Marathon.pptx")

if __name__ == "__main__":
    print("==================================================================")
    print("Generating 10 Mega Mock Tests (50 High-Yield Questions, 104 Slides Each)...")
    print("==================================================================")

    # Clean old mock files first
    clean_old_mock_files()

    # Generate 10 Tests of 50 questions each
    for i, cfg in enumerate(TEST_CONFIGS):
        start_idx = i * 50
        end_idx = start_idx + 50
        q_subset = master_pool[start_idx:end_idx]
        print(f"\nBuilding Mock Test #{cfg['num']} with {len(q_subset)} unique questions (Indices {start_idx} to {end_idx})...")
        build_single_50q_test(cfg['num'], cfg, q_subset)

    # Update marathon names
    update_marathon_names()

    print("\nSUCCESS! All 10 Mega Mock Tests (50 questions each) have been generated with clean filenames!")
