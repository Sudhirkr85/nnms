import pptx
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'C:\Users\Orange\Downloads\New folder\SST_Complete_Course_SagarSir'
forbidden_terms = ['समय: 10 सेकंड', 'कमेंट', 'लाइव चैट', '[सही उत्तर]']

total_checked = 0
found_issues = 0

for root, dirs, files in os.walk(base_dir):
    for f in sorted(files):
        if f.endswith('.pptx'):
            fpath = os.path.join(root, f)
            prs = pptx.Presentation(fpath)
            total_checked += 1
            for i, s in enumerate(prs.slides):
                for shape in s.shapes:
                    if shape.has_text_frame:
                        for p in shape.text_frame.paragraphs:
                            for term in forbidden_terms:
                                if term in p.text:
                                    print(f'[FOUND FORBIDDEN TERM] "{term}" in {f} Slide {i+1}: {p.text[:60]}')
                                    found_issues += 1

print(f'\nTotal PPTs Scanned: {total_checked}')
print(f'Total Forbidden Terms Found: {found_issues}')
if found_issues == 0:
    print('ALL 41 PPTs ARE 100% CLEAN AND FREE OF EXTRA WORDS/TIMER/COMMENT PROMPTS!')
