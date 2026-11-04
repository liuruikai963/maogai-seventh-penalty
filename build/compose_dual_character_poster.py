# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

bg_path = 'assets/images/poster_luyuan_laoliu_clean.jpg'
out_path = 'assets/images/poster_luyuan_laoliu_final.jpg'

im = Image.open(bg_path).convert('RGBA')
width, height = im.size

# Soft cinematic vignette at top to guarantee text readability against sky
vignette = Image.new('RGBA', (width, height), (0, 0, 0, 0))
v_draw = ImageDraw.Draw(vignette)
for y in range(0, int(height * 0.40)):
    alpha = int(110 * (1 - y / (height * 0.40)))
    v_draw.line([(0, y), (width, y)], fill=(8, 15, 28, max(0, alpha)))

im = Image.alpha_composite(im, vignette)

# Fonts
font_title_path = 'C:/Windows/Fonts/msyhbd.ttc'
font_sub_path = 'C:/Windows/Fonts/msyh.ttc'

font_title = ImageFont.truetype(font_title_path, 66)
font_en = ImageFont.truetype(font_sub_path, 20)
font_slogan = ImageFont.truetype(font_title_path, 28)
font_dedication = ImageFont.truetype(font_sub_path, 21)

# Texts
title_text = "《 算 法 之 外 》"
en_text = "B E Y O N D   T H E   A L G O R I T H M"
slogan_text = "—— 算力有极限，善意无边界。"
dedication_text = "谨以此片献给新时代每一位新就业形态劳动者"

# Measure bboxes
title_bbox = font_title.getbbox(title_text)
t_w = title_bbox[2] - title_bbox[0]
t_x = (width - t_w) // 2
t_y = int(height * 0.08)

en_bbox = font_en.getbbox(en_text)
en_w = en_bbox[2] - en_bbox[0]
en_x = (width - en_w) // 2
en_y = t_y + 82

slogan_bbox = font_slogan.getbbox(slogan_text)
s_w = slogan_bbox[2] - slogan_bbox[0]
s_x = (width - s_w) // 2
s_y = en_y + 42

ded_bbox = font_dedication.getbbox(dedication_text)
d_w = ded_bbox[2] - ded_bbox[0]
d_x = (width - d_w) // 2
d_y = int(height * 0.92)

# Glow Layer
glow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow_layer)

for offset in range(5, 0, -1):
    glow_draw.text((t_x, t_y), title_text, font=font_title, fill=(255, 220, 130, 70))
    glow_draw.text((s_x, s_y), slogan_text, font=font_slogan, fill=(255, 230, 160, 60))

glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(6))
im = Image.alpha_composite(im, glow_layer)

# Crisp Text Drawing
draw = ImageDraw.Draw(im)

# Title: Drop shadow + White/Champagne fill
draw.text((t_x + 3, t_y + 3), title_text, font=font_title, fill=(10, 15, 30, 240))
draw.text((t_x, t_y), title_text, font=font_title, fill=(255, 255, 255, 255))

# English Subtitle
draw.text((en_x + 1, en_y + 1), en_text, font=font_en, fill=(10, 15, 25, 220))
draw.text((en_x, en_y), en_text, font=font_en, fill=(255, 235, 175, 250))

# Slogan: Warm golden text with black outline
for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
    draw.text((s_x + dx, s_y + dy), slogan_text, font=font_slogan, fill=(10, 15, 25, 220))
draw.text((s_x, s_y), slogan_text, font=font_slogan, fill=(255, 218, 110, 255))

# Bottom Dedication with subtle outline
for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (1, 1)]:
    draw.text((d_x + dx, d_y + dy), dedication_text, font=font_dedication, fill=(0, 0, 0, 200))
draw.text((d_x, d_y), dedication_text, font=font_dedication, fill=(250, 250, 250, 240))

final_im = im.convert('RGB')
final_im.save(out_path, quality=95)
print(f"Successfully composited final dual-character poster: {out_path}")
