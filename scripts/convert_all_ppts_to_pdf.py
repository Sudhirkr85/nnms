import os
import sys
import time
import gc

sys.stdout.reconfigure(encoding='utf-8')

import win32com.client

ROOT_DIR = r"C:\Users\Orange\Downloads\New folder"

TARGET_FOLDERS = [
    r"UP_NMMS_MahaManthan_Nov_Exam_SagarSir",
    r"SST_Complete_Course_SagarSir",
    r"Science_Complete_Course_SagarSir",
    r"NMMS_SAT_Grand_MahaManthan_SagarSir"
]

def find_all_ppts():
    ppt_list = []
    for tf in TARGET_FOLDERS:
        full_path = os.path.join(ROOT_DIR, tf)
        if not os.path.exists(full_path):
            print(f"Warning: Folder not found: {full_path}")
            continue
        for root, dirs, files in os.walk(full_path):
            for f in files:
                if f.lower().endswith('.pptx') and not f.startswith('~$'):
                    ppt_list.append(os.path.join(root, f))
    return sorted(ppt_list)

def convert_all():
    all_ppts = find_all_ppts()
    total = len(all_ppts)
    print(f"Total PPTX files to convert to PDF: {total}")

    success_count = 0
    fail_count = 0
    skipped_count = 0

    print("Starting Microsoft PowerPoint Application COM...")
    app = win32com.client.Dispatch("PowerPoint.Application")

    start_time = time.time()

    try:
        for idx, ppt_path in enumerate(all_ppts, 1):
            pdf_path = os.path.splitext(ppt_path)[0] + ".pdf"
            rel_ppt = os.path.relpath(ppt_path, ROOT_DIR)
            rel_pdf = os.path.relpath(pdf_path, ROOT_DIR)

            # Check if PDF already exists and is non-empty
            if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 10000:
                print(f"[{idx}/{total}] SKIP (Already exists): {rel_pdf} ({os.path.getsize(pdf_path)/1024/1024:.2f} MB)")
                skipped_count += 1
                success_count += 1
                continue

            file_start = time.time()
            try:
                abs_ppt = os.path.abspath(ppt_path)
                abs_pdf = os.path.abspath(pdf_path)

                deck = app.Presentations.Open(abs_ppt, WithWindow=False)
                # 32 represents ppSaveAsPDF in PowerPoint Object Model
                deck.SaveAs(abs_pdf, 32)
                deck.Close()

                file_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
                elapsed = time.time() - file_start
                print(f"[{idx}/{total}] OK ({elapsed:.1f}s, {file_size_mb:.2f} MB): {rel_pdf}")
                success_count += 1

            except Exception as e:
                print(f"[{idx}/{total}] ERROR on {rel_ppt}: {e}")
                fail_count += 1
                # Try restarting PowerPoint if it crashed or failed
                try:
                    app.Quit()
                except Exception:
                    pass
                time.sleep(2)
                app = win32com.client.Dispatch("PowerPoint.Application")

            # Periodically force GC
            if idx % 10 == 0:
                gc.collect()

    finally:
        try:
            app.Quit()
            print("PowerPoint application closed.")
        except Exception as e:
            print(f"Note closing PowerPoint: {e}")

    total_time = time.time() - start_time
    print("\n" + "=" * 60)
    print(f"CONVERSION COMPLETE in {total_time/60:.2f} minutes")
    print(f"Total files: {total}")
    print(f"Successfully available: {success_count} (New/Converted: {success_count - skipped_count}, Skipped existing: {skipped_count})")
    print(f"Failed: {fail_count}")
    print("=" * 60)

if __name__ == "__main__":
    convert_all()
