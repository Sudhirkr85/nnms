import re
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

all_files = [
    'scripts/generate_mega_50_practice_sets.py',
    'scripts/generate_civics_classes.py',
    'scripts/generate_history_classes_p1.py',
    'scripts/generate_history_classes_p2.py',
    'scripts/generate_history_classes.py',
    'scripts/generate_geo_classes_50min_p1.py',
    'scripts/generate_geo_classes_50min_p2.py',
    'scripts/generate_20_mock_tests.py'
]

unique_qs = {}
for p in all_files:
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    matches = re.findall(r'\(\s*"([^"]{10,250}\?)"\s*,\s*(\[[^\]]+\])\s*,\s*"([A-D])"\s*,\s*"([^"]+)"(?:\s*,\s*"([^"]+)")?\s*\)', content)
    for m in matches:
        q = m[0].strip()
        opts = eval(m[1])
        c_opt = m[2].strip()
        exp = m[3].strip()
        tag = m[4].strip() if m[4] else "All India NMMS PYQ"
        if q not in unique_qs:
            unique_qs[q] = {
                "question": q,
                "options": opts,
                "correct_opt": c_opt,
                "explanation": exp,
                "tag": tag
            }

print(f"Total Unique Questions Gathered: {len(unique_qs)}")
with open('scripts/all_unique_questions_pool.json', 'w', encoding='utf-8') as f:
    json.dump(list(unique_qs.values()), f, ensure_ascii=False, indent=2)
print("Saved to scripts/all_unique_questions_pool.json")
