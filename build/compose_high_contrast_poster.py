# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Base with widened gap
bg_path = 'assets/images/poster_wide_gap_test.jpg'
out_path = 'assets/images/poster_luyuan_laoliu_final.jpg'

im = Image.open(bg_path).convert('RGBA')
width, height = im.size

# 1. Subtle, filmic sky contrast enhancement in top-center zone
# Deepens the stormy blue clouds behind the title without touching the characters
contrast_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
c_draw = ImageDraw.Draw(contrast_layer)

# Radial or vertical smooth soft shadow mask behind text zone
for y in range(0, int(height * 0.45)):
    # Soft deep navy-indigo tint
    factor = 1.0 - (y / (height * 0.45))
    alpha = int(75 * factor)
    c_draw.line([(0, y), (width, y)], fill=(8, 16, 32, alpha))

im = Image.alpha_composite(im, contrast_layer)

# Fonts
font_song_bold = 'C:/Windows/Fonts/STSONG.TTF' if os.path.exists('C:/Windows/Fonts/STSONG.TTF') else 'C:/Windows/Fonts/simsun.ttc'
font_deng_bold = 'C:/Windows/Fonts/Dengb.ttf' if os.path.exists('C:/Windows/Fonts/Dengb.ttf') else 'C:/Windows/Fonts/msyhbd.ttc'
font_fangsong = 'C:/Windows/Fonts/simfang.ttf'
font_en = 'C:/Windows/Fonts/georgia.ttf' if os.path.exists('C:/Windows/Fonts/georgia.ttf') else 'C:/Windows/Fonts/times.ttf'

# Enlarged font sizes for dramatic visibility
f_slogan = ImageFont.truetype(font_deng_bold, 32)   # Significantly enlarged from 18 to 32!
f_title = ImageFont.truetype(font_song_bold, 78)     # Bold, grand movie title
f_en = ImageFont.truetype(font_en, 20)              # Cinematic English title
f_footer = ImageFont.truetype(font_fangsong, 18)    # Clean dedication

# Texts
slogan_text = "算 力 有 极 限  ·  善 意 无 边 界"
title_text = "算  法  之  外"
en_text = "B E Y O N D   T H E   A L G O R I T H M"
footer_text = "谨以此片献给新时代每一位新就业形态劳动者"

# BBoxes and Positioning
s_bbox = f_slogan.getbbox(slogan_text)
s_w = s_bbox[2] - s_bbox[0]
s_x = (width - s_w) // 2
s_y = 50

t_bbox = f_title.getbbox(title_text)
t_w = t_bbox[2] - t_bbox[0]
t_x = (width - t_w) // 2
t_y = s_y + 54

en_bbox = f_en.getbbox(en_text)
en_w = en_bbox[2] - en_bbox[0]
en_x = (width - en_w) // 2
en_y = t_y + 104

f_bbox = f_footer.getbbox(footer_text)
f_w = f_bbox[2] - f_bbox[0]
f_x = (width - f_w) // 2
f_y = height - 52

# 2. Multi-tier Deep Filmic Glow & Shadow for absolute readability
shadow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
s_draw = ImageDraw.Draw(shadow_layer)

# Deep atmospheric dark navy shadow drops
for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (0, 4), (0, -4), (-4, 0), (4, 0), (0, 6)]:
    s_draw.text((s_x + dx, s_y + dy), slogan_text, font=f_slogan, fill=(5, 10, 25, 160))
    s_draw.text((t_x + dx, t_y + dy), title_text, font=f_title, fill=(5, 10, 25, 200))
    s_draw.text((en_x + dx, en_y + dy), en_text, font=f_en, fill=(5, 10, 25, 150))
    s_draw.text((f_x + dx, f_y + dy), footer_text, font=f_footer, fill=(5, 10, 25, 180))

# Blur shadow layer for natural optical depth
shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(6))
im = Image.alpha_composite(im, shadow_layer)

# 3. Ambient Golden Halo Layer for Title and Slogan
glow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
g_draw = ImageDraw.Draw(glow_layer)
g_draw.text((s_x, s_y), slogan_text, font=f_slogan, fill=(255, 215, 100, 90))
g_draw.text((t_x, t_y), title_text, font=f_title, fill=(255, 230, 160, 110))
glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(8))
im = Image.alpha_composite(im, glow_layer)

# 4. Crisp Foreground Text
draw = ImageDraw.Draw(im)

# Slogan: Warm Sunrise Gold (#FFDC73), bold and razor-sharp!
draw.text((s_x + 1, s_y + 1), slogan_text, font=f_slogan, fill=(20, 25, 40, 220))
draw.text((s_x, s_y), slogan_text, font=f_slogan, fill=(255, 222, 120, 255))

# Title: Pure luminous ivory white with slight warm golden rim
draw.text((t_x + 2, t_y + 2), title_text, font=f_title, fill=(15, 20, 35, 230))
draw.text((t_x, t_y), title_text, font=f_title, fill=(255, 255, 255, 255))

# English Subtitle: Refined Champagne Gold
draw.text((en_x + 1, en_y + 1), en_text, font=f_en, fill=(15, 20, 35, 200))
draw.text((en_x, en_y), en_text, font=f_en, fill=(240, 225, 185, 255))

# Footer: Clean crisp white
draw.text((f_x + 1, f_y + 1), footer_text, font=f_footer, fill=(10, 15, 25, 220))
draw.text((f_x, f_y), footer_text, font=f_footer, fill=(250, 252, 255, 240))

# Save
final_im = im.convert('RGB')
final_im.save(out_path, quality=98)
print("Saved ultra-clear high-contrast cinema poster:", out_path)
print(f"Slogan size: 32pt (width {s_w}px)")
print(f"Title size: 78pt (width {t_w}px, centered at x={t_x})")
print(f"Clearance: left character ends around x=260, title starts at x={t_x} -> gap is {t_x - 260}px!")
