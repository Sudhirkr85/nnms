# -*- coding: utf-8 -*-
"""
Converts all 10 newly created UP NMMS practice sets (5 MAT + 5 SAT) from PPTX to PDF using PowerPoint COM automation.
Saves PDF files with the exact same base name in the exact same directories.
"""

import os
import sys
import time

if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import win32com.client

BASE_DIR = r"C:\Users\Orange\Downloads\New folder"
TARGET_DIRS = [
    os.path.join(BASE_DIR, "UP_NMMS_MAT_MahaManthan_5_Sets_SagarSir"),
    os.path.join(BASE_DIR, "UP_NMMS_SAT_MahaManthan_5_Sets_SagarSir")
]

def convert():
    ppts = []
    for d in TARGET_DIRS:
        if not os.path.exists(d):
            continue
        for f in os.listdir(d):
            if f.lower().endswith(".pptx") and not f.startswith("~$"):
                ppts.append(os.path.join(d, f))

    ppts.sort()
    total = len(ppts)
    print(f"Total PPTX decks found to convert: {total}")

    if total == 0:
        print("No PPTX files found to convert!")
        return

    print("Launching PowerPoint Application...")
    app = win32com.client.Dispatch("PowerPoint.Application")
    app.Visible = 1

    start_all = time.time()
    converted_count = 0

    try:
        for idx, ppt_path in enumerate(ppts, 1):
            pdf_path = os.path.splitext(ppt_path)[0] + ".pdf"
            ppt_name = os.path.basename(ppt_path)
            pdf_name = os.path.basename(pdf_path)

            t0 = time.time()
            print(f"[{idx}/{total}] Converting: {ppt_name} ...", end="", flush=True)

            deck = app.Presentations.Open(ppt_path, WithWindow=False)
            deck.SaveAs(pdf_path, 32)  # 32 = ppSaveAsPDF
            deck.Close()

            elapsed = time.time() - t0
            size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
            print(f" DONE in {elapsed:.1f}s ({size_mb:.2f} MB) -> {pdf_name}")
            converted_count += 1

    finally:
        app.Quit()
        total_time = time.time() - start_all
        print(f"\nAll {converted_count}/{total} files converted to PDF successfully in {total_time:.1f}s!")

if __name__ == "__main__":
    convert()
