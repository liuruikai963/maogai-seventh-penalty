# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

bg_path = 'assets/images/poster_wide_clean_base.jpg'
out_path = 'assets/images/poster_luyuan_laoliu_final.jpg'

im = Image.open(bg_path).convert('RGBA')
width, height = im.size

# Subtle sky gradient to guarantee 100% readability without losing cloud beauty
vignette = Image.new('RGBA', (width, height), (0, 0, 0, 0))
v_draw = ImageDraw.Draw(vignette)
for y in range(0, int(height * 0.42)):
    alpha = int(70 * (1 - y / (height * 0.42)))
    v_draw.line([(0, y), (width, y)], fill=(10, 18, 32, alpha))
im = Image.alpha_composite(im, vignette)

# Fonts
font_song_bold = 'C:/Windows/Fonts/STSONG.TTF' if os.path.exists('C:/Windows/Fonts/STSONG.TTF') else 'C:/Windows/Fonts/simsun.ttc'
font_deng_bold = 'C:/Windows/Fonts/Dengb.ttf' if os.path.exists('C:/Windows/Fonts/Dengb.ttf') else 'C:/Windows/Fonts/msyhbd.ttc'
font_fangsong = 'C:/Windows/Fonts/simfang.ttf'
font_en = 'C:/Windows/Fonts/georgia.ttf' if os.path.exists('C:/Windows/Fonts/georgia.ttf') else 'C:/Windows/Fonts/times.ttf'

# Font sizes
f_slogan = ImageFont.truetype(font_deng_bold, 34)   # Bold & Large 34pt
f_title = ImageFont.truetype(font_song_bold, 80)     # Grand 80pt
f_en = ImageFont.truetype(font_en, 20)              # Cinematic English 20pt
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
s_y = 52

t_bbox = f_title.getbbox(title_text)
t_w = t_bbox[2] - t_bbox[0]
t_x = (width - t_w) // 2
t_y = s_y + 56

en_bbox = f_en.getbbox(en_text)
en_w = en_bbox[2] - en_bbox[0]
en_x = (width - en_w) // 2
en_y = t_y + 106

f_bbox = f_footer.getbbox(footer_text)
f_w = f_bbox[2] - f_bbox[0]
f_x = (width - f_w) // 2
f_y = height - 52

# Deep Filmic Shadow & Halo (No cheap strokes, real optical film depth)
shadow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
s_draw = ImageDraw.Draw(shadow_layer)

for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (0, 4), (0, -4), (-4, 0), (4, 0), (0, 6)]:
    s_draw.text((s_x + dx, s_y + dy), slogan_text, font=f_slogan, fill=(5, 12, 28, 170))
    s_draw.text((t_x + dx, t_y + dy), title_text, font=f_title, fill=(5, 12, 28, 210))
    s_draw.text((en_x + dx, en_y + dy), en_text, font=f_en, fill=(5, 12, 28, 160))
    s_draw.text((f_x + dx, f_y + dy), footer_text, font=f_footer, fill=(5, 12, 28, 180))

shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(5))
im = Image.alpha_composite(im, shadow_layer)

# Ambient Golden Glow for Slogan and Title
glow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
g_draw = ImageDraw.Draw(glow_layer)
g_draw.text((s_x, s_y), slogan_text, font=f_slogan, fill=(255, 215, 90, 80))
g_draw.text((t_x, t_y), title_text, font=f_title, fill=(255, 230, 160, 100))
glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(8))
im = Image.alpha_composite(im, glow_layer)

# Crisp Foreground Typography
draw = ImageDraw.Draw(im)

# Slogan: Warm Sunrise Gold (#FFDE78), highly legible
draw.text((s_x + 1, s_y + 1), slogan_text, font=f_slogan, fill=(15, 22, 35, 220))
draw.text((s_x, s_y), slogan_text, font=f_slogan, fill=(255, 222, 120, 255))

# Title: Luminous Pure White with subtle warm edge
draw.text((t_x + 2, t_y + 2), title_text, font=f_title, fill=(12, 18, 30, 230))
draw.text((t_x, t_y), title_text, font=f_title, fill=(255, 255, 255, 255))

# English Subtitle: Champagne Gold
draw.text((en_x + 1, en_y + 1), en_text, font=f_en, fill=(12, 18, 30, 200))
draw.text((en_x, en_y), en_text, font=f_en, fill=(240, 225, 185, 255))

# Footer: Clean crisp white
draw.text((f_x + 1, f_y + 1), footer_text, font=f_footer, fill=(10, 15, 25, 220))
draw.text((f_x, f_y), footer_text, font=f_footer, fill=(250, 252, 255, 240))

final_im = im.convert('RGB')
final_im.save(out_path, quality=98)
print(f"Native Wide Poster created successfully at: {out_path}")
