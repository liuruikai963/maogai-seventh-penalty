# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

bg_path = 'assets/images/intro_title_bg.jpg'
out_path = 'assets/images/intro_title_card_final.jpg'

im = Image.open(bg_path).convert('RGBA')
width, height = im.size

# Darken / vignette slightly at the top/center to make title pop
vignette = Image.new('RGBA', (width, height), (0, 0, 0, 0))
v_draw = ImageDraw.Draw(vignette)
# Central gradient or soft dark band
for y in range(int(height * 0.15), int(height * 0.55)):
    alpha = int(90 * (1 - abs(y - height * 0.35) / (height * 0.2)))
    v_draw.line([(0, y), (width, y)], fill=(10, 15, 25, max(0, alpha)))

im = Image.alpha_composite(im, vignette)

# Fonts
font_title_path = 'C:/Windows/Fonts/msyhbd.ttc'
font_sub_path = 'C:/Windows/Fonts/msyh.ttc'

font_title = ImageFont.truetype(font_title_path, 68)
font_en = ImageFont.truetype(font_sub_path, 22)
font_dedication = ImageFont.truetype(font_sub_path, 24)

# Texts
title_text = "《 算 法 之 外 》"
en_text = "B E Y O N D   T H E   A L G O R I T H M"
dedication_text = "谨以此片献给新时代每一位新就业形态劳动者"

# Create a separate layer for glowing shadow
glow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow_layer)

# Center positions
title_bbox = font_title.getbbox(title_text)
t_w = title_bbox[2] - title_bbox[0]
t_x = (width - t_w) // 2
t_y = int(height * 0.26)

en_bbox = font_en.getbbox(en_text)
en_w = en_bbox[2] - en_bbox[0]
en_x = (width - en_w) // 2
en_y = t_y + 92

ded_bbox = font_dedication.getbbox(dedication_text)
ded_w = ded_bbox[2] - ded_bbox[0]
ded_x = (width - ded_w) // 2
ded_y = int(height * 0.88)

# Draw deep golden-cyan glow
for offset in range(6, 0, -2):
    glow_draw.text((t_x, t_y), title_text, font=font_title, fill=(255, 215, 120, 60))
    glow_draw.text((en_x, en_y), en_text, font=font_en, fill=(100, 220, 255, 80))

glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(8))
im = Image.alpha_composite(im, glow_layer)

# Draw crisp drop shadow and main text
draw = ImageDraw.Draw(im)

# Drop shadow for title
draw.text((t_x + 3, t_y + 3), title_text, font=font_title, fill=(10, 15, 30, 240))
draw.text((t_x, t_y), title_text, font=font_title, fill=(255, 255, 255, 255))

# English subtitle
draw.text((en_x + 1, en_y + 1), en_text, font=font_en, fill=(10, 20, 30, 220))
draw.text((en_x, en_y), en_text, font=font_en, fill=(255, 235, 180, 250))

# Bottom dedication (white with black border)
for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
    draw.text((ded_x + dx, ded_y + dy), dedication_text, font=font_dedication, fill=(0, 0, 0, 220))
draw.text((ded_x, ded_y), dedication_text, font=font_dedication, fill=(255, 255, 255, 255))

final_im = im.convert('RGB')
final_im.save(out_path, quality=95)
print(f"Successfully generated title card: {out_path}")
