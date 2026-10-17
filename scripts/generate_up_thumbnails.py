import os
import sys
from PIL import Image, ImageDraw, ImageFont

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Orange\Downloads\New folder"
TARGET_DIR = os.path.join(ROOT_DIR, "UP_NMMS_MahaManthan_Nov_Exam_SagarSir")
os.makedirs(TARGET_DIR, exist_ok=True)

LOGO_PATH = os.path.join(ROOT_DIR, "assets", "logo-circle-transparent.png")
if not os.path.exists(LOGO_PATH):
    LOGO_PATH = os.path.join(r"d:\Work\E-Learning\public", "logo-circle-transparent.png")

FONT_HINDI_BOLD = r"C:\Windows\Fonts\Nirmala.ttc"
FONT_ENG_BOLD = r"C:\Windows\Fonts\arialbd.ttf"

def draw_text_with_shadow(draw, pos, text, font, text_color, shadow_color=(0, 0, 0), offset=4):
    x, y = pos
    # Shadow
    for dx in range(-offset, offset + 1):
        for dy in range(-offset, offset + 1):
            if abs(dx) == offset or abs(dy) == offset:
                draw.text((x + dx, y + dy), text, font=font, fill=shadow_color)
    # Main text
    draw.text((x, y), text, font=font, fill=text_color)

def create_thumbnail(mode="MAT"):
    W, H = 1280, 720
    # Background Canvas
    img = Image.new("RGB", (W, H), color=(10, 15, 30))
    draw = ImageDraw.Draw(img)

    # Gradient Background Effect
    for y in range(H):
        if mode == "MAT":
            # Deep Navy to Dark Indigo / Violet
            r = int(10 + (35 - 10) * (y / H))
            g = int(15 + (15 - 15) * (y / H))
            b = int(35 + (90 - 35) * (y / H))
        elif mode == "SAT":
            # Deep Navy to Dark Crimson / Maroon
            r = int(15 + (80 - 15) * (y / H))
            g = int(15 + (10 - 15) * (y / H))
            b = int(30 + (25 - 30) * (y / H))
        else: # COMBO
            # Deep Slate to Royal Purple
            r = int(20 + (50 - 20) * (y / H))
            g = int(15 + (20 - 15) * (y / H))
            b = int(45 + (85 - 45) * (y / H))
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Outer Glowing Border
    border_color = (245, 158, 11) if mode != "SAT" else (239, 68, 68)
    draw.rectangle([(10, 10), (W - 10, H - 10)], outline=border_color, width=6)
    draw.rectangle([(18, 18), (W - 18, H - 18)], outline=(255, 255, 255), width=2)

    # Top Left: Exam Badge
    draw.rounded_rectangle([(35, 30), (450, 95)], radius=12, fill=(220, 38, 38), outline=(255, 255, 255), width=3)
    f_badge = ImageFont.truetype(FONT_ENG_BOLD, 32)
    draw.text((55, 42), "UP NMMS 2024-25", font=f_badge, fill=(255, 255, 255))

    # Top Right: Live 2-Hour Marathon Pill
    draw.rounded_rectangle([(780, 30), (1240, 95)], radius=12, fill=(217, 119, 6), outline=(255, 255, 255), width=3)
    f_live = ImageFont.truetype(FONT_HINDI_BOLD, 30)
    draw.text((800, 42), "🔴 2 घंटे+ की महा मैराथन", font=f_live, fill=(255, 255, 255))

    # Center Logo
    if os.path.exists(LOGO_PATH):
        try:
            logo = Image.open(LOGO_PATH).convert("RGBA")
            logo = logo.resize((150, 150), Image.Resampling.LANCZOS)
            img.paste(logo, (565, 110), logo)
        except Exception as e:
            print(f"Note loading logo: {e}")

    # Institute Name Ribbon
    f_inst = ImageFont.truetype(FONT_HINDI_BOLD, 28)
    draw.text((430, 265), "SAGAR COACHING CENTRE", font=ImageFont.truetype(FONT_ENG_BOLD, 28), fill=(245, 158, 11))

    # Main Mega Title
    f_main = ImageFont.truetype(FONT_HINDI_BOLD, 74)
    if mode == "MAT":
        title_text = "MAT महामंथन"
        subtitle_text = "100+ अति-महत्वपूर्ण प्रश्न • 90/90 पक्के!"
        theme_color = (250, 204, 21) # Bright Gold
    elif mode == "SAT":
        title_text = "SAT महामंथन"
        subtitle_text = "विज्ञान + सामाजिक अध्ययन + गणित (100 Q)"
        theme_color = (248, 113, 113) # Coral Red/Gold
    else:
        title_text = "GRAND महामंथन"
        subtitle_text = "MAT + SAT सम्पूर्ण पेपर • 200+ प्रश्न"
        theme_color = (192, 132, 252) # Violet Gold

    # Center Main Title
    bbox_title = draw.textbbox((0, 0), title_text, font=f_main)
    w_title = bbox_title[2] - bbox_title[0]
    draw_text_with_shadow(draw, ((W - w_title) // 2, 310), title_text, f_main, theme_color, shadow_color=(0, 0, 0), offset=6)

    # Subtitle Ribbon Card
    draw.rounded_rectangle([(80, 420), (W - 80, 505)], radius=16, fill=(255, 255, 255), outline=border_color, width=4)
    f_sub = ImageFont.truetype(FONT_HINDI_BOLD, 38)
    bbox_sub = draw.textbbox((0, 0), subtitle_text, font=f_sub)
    w_sub = bbox_sub[2] - bbox_sub[0]
    draw.text(((W - w_sub) // 2, 435), subtitle_text, font=f_sub, fill=(15, 23, 42))

    # Bottom High-CTR Hooks (Paper Out / Prediction Box)
    draw.rounded_rectangle([(80, 530), (750, 675)], radius=14, fill=(220, 38, 38), outline=(255, 255, 255), width=3)
    f_hook1 = ImageFont.truetype(FONT_HINDI_BOLD, 36)
    draw.text((110, 545), "⚡ 100% यहीं से छपेंगे प्रश्न!", font=f_hook1, fill=(255, 255, 255))
    f_hook2 = ImageFont.truetype(FONT_HINDI_BOLD, 26)
    draw.text((110, 610), "✓ UP SCERT पैटर्न पर आधारित सम्पूर्ण व्याख्या", font=f_hook2, fill=(254, 240, 138))

    # Teacher / Brand Card (Right Bottom)
    draw.rounded_rectangle([(780, 530), (W - 80, 675)], radius=14, fill=(30, 41, 59), outline=(245, 158, 11), width=3)
    f_sir = ImageFont.truetype(FONT_HINDI_BOLD, 32)
    draw.text((810, 545), "BY: सागर सर (NMMS King)", font=f_sir, fill=(245, 158, 11))
    f_sub_sir = ImageFont.truetype(FONT_HINDI_BOLD, 25)
    draw.text((810, 610), "₹48,000 की छात्रवृत्ति पक्की!", font=f_sub_sir, fill=(255, 255, 255))

    out_name = f"Thumbnail_{mode}_MahaManthan_UP_NMMS.png"
    out_path = os.path.join(TARGET_DIR, out_name)
    img.save(out_path, quality=95)
    print(f"Generated Thumbnail: {out_path} ({os.path.getsize(out_path)/1024:.1f} KB)")
    return out_path

if __name__ == "__main__":
    t1 = create_thumbnail("MAT")
    t2 = create_thumbnail("SAT")
    t3 = create_thumbnail("Grand_Combo")
    print("All 3 High-CTR YouTube Thumbnails generated successfully!")
