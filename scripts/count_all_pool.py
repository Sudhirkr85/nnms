import re
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

all_qs = []
for p in all_files:
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    matches = re.findall(r'\(\s*"([^"]{10,250}\?)"\s*,\s*(\[[^\]]+\])\s*,\s*"([A-D])"\s*,\s*"([^"]+)"(?:\s*,\s*"([^"]+)")?\s*\)', content)
    fname = p.split('/')[-1]
    print(f'{fname}: {len(matches)} questions')
    all_qs.extend(matches)

unique = {}
for m in all_qs:
    q = m[0].strip()
    if q not in unique:
        unique[q] = m

print(f'\nTotal raw extracted: {len(all_qs)}')
print(f'Total UNIQUE questions: {len(unique)}')
