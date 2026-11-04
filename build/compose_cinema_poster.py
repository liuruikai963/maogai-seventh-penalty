# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

bg_path = 'assets/images/poster_luyuan_laoliu_clean.jpg'
out_path = 'assets/images/poster_luyuan_laoliu_final.jpg'

im = Image.open(bg_path).convert('RGBA')
width, height = im.size

# High-end cinematic fonts
# STSONG.TTF (华文宋体) or simsun.ttc (中易宋体)
font_song_bold = 'C:/Windows/Fonts/STSONG.TTF' if os.path.exists('C:/Windows/Fonts/STSONG.TTF') else 'C:/Windows/Fonts/simsun.ttc'
font_fangsong = 'C:/Windows/Fonts/simfang.ttf'
font_en = 'C:/Windows/Fonts/georgia.ttf' if os.path.exists('C:/Windows/Fonts/georgia.ttf') else 'C:/Windows/Fonts/times.ttf'
font_dengxian = 'C:/Windows/Fonts/Deng.ttf'

# Font Sizes for refined cinematic scale
# Characters should be dominant, title should be elegant, not overbearing
f_slogan = ImageFont.truetype(font_fangsong, 18)
f_title = ImageFont.truetype(font_song_bold, 64)
f_en = ImageFont.truetype(font_en, 15)
f_footer = ImageFont.truetype(font_fangsong, 16)

# Texts
slogan_text = "算  力  有  极  限  ·  善  意  无  边  界"
title_text = "算  法  之  外"
en_text = "B E Y O N D   T H E   A L G O R I T H M"
footer_text = "谨以此片献给新时代每一位新就业形态劳动者"

# Subtle top ambient sky gradient (very gentle, filmic contrast without looking dark)
vignette = Image.new('RGBA', (width, height), (0, 0, 0, 0))
v_draw = ImageDraw.Draw(vignette)
for y in range(0, int(height * 0.35)):
    # Soft blue-navy tint matching the sky clouds
    alpha = int(45 * (1 - y / (height * 0.35)))
    v_draw.line([(0, y), (width, y)], fill=(12, 22, 38, alpha))
im = Image.alpha_composite(im, vignette)

# Bounding boxes
s_bbox = f_slogan.getbbox(slogan_text)
s_w = s_bbox[2] - s_bbox[0]
s_x = (width - s_w) // 2
s_y = 65

t_bbox = f_title.getbbox(title_text)
t_w = t_bbox[2] - t_bbox[0]
t_x = (width - t_w) // 2
t_y = s_y + 36

en_bbox = f_en.getbbox(en_text)
en_w = en_bbox[2] - en_bbox[0]
en_x = (width - en_w) // 2
en_y = t_y + 86

f_bbox = f_footer.getbbox(footer_text)
f_w = f_bbox[2] - f_bbox[0]
f_x = (width - f_w) // 2
f_y = height - 52

# Create Film Shadow & Light Bloom layer (No cheap black outlines!)
bloom_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
bloom_draw = ImageDraw.Draw(bloom_layer)

# Soft optical shadow (deep navy/slate, not pitch black)
for r in [2, 4, 8, 12]:
    bloom_draw.text((t_x, t_y + 2), title_text, font=f_title, fill=(10, 20, 35, 70))
    bloom_draw.text((s_x, s_y + 1), slogan_text, font=f_slogan, fill=(10, 20, 35, 60))
    bloom_draw.text((en_x, en_y + 1), en_text, font=f_en, fill=(10, 20, 35, 60))
    bloom_draw.text((f_x, f_y + 1), footer_text, font=f_footer, fill=(10, 20, 35, 80))

bloom_layer = bloom_layer.filter(ImageFilter.GaussianBlur(5))
im = Image.alpha_composite(im, bloom_layer)

# Crisp Text Drawing (Editorial Cinematic Treatment)
draw = ImageDraw.Draw(im)

# Slogan: Warm cream/champagne with tracked breathing room
draw.text((s_x, s_y), slogan_text, font=f_slogan, fill=(245, 235, 215, 230))

# Thin decorative line under slogan / above title (Classic film poster hallmark)
line_len = 120
line_y = s_y + 26
draw.line([(width//2 - line_len//2, line_y), (width//2 + line_len//2, line_y)], fill=(245, 225, 180, 160), width=1)

# Title: Pure luminous ivory white with slight warm sunrise ambient reflection
draw.text((t_x, t_y), title_text, font=f_title, fill=(255, 255, 255, 255))

# English Subtitle: Refined serif gold/sand tone
draw.text((en_x, en_y), en_text, font=f_en, fill=(235, 215, 175, 240))

# Bottom Dedication: Clean, unobtrusive, dignified
draw.text((f_x, f_y), footer_text, font=f_footer, fill=(245, 248, 252, 220))

# Convert and save
final_im = im.convert('RGB')
final_im.save(out_path, quality=98)
print(f"Refined cinema poster saved to {out_path}")
print(f"Title width: {t_w}px, centered at x={t_x}. Distance to edges: {t_x}px (safe clearance from both characters).")
