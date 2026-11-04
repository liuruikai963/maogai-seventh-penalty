# -*- coding: utf-8 -*-
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg
import numpy as np

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

img_poster_path = 'assets/images/poster_luyuan_laoliu_final.jpg'
audio_path = 'assets/audio/foley/intro_typewriter_audio_master.wav'
output_video = 'dist/acts/intro_title_sequence.mp4'

os.makedirs('dist/acts', exist_ok=True)

width, height = 1280, 720
fps = 24
duration = 12.0
total_frames = int(fps * duration) # 288 frames

# Fonts
font_fangsong = 'C:/Windows/Fonts/simfang.ttf'
font_song = 'C:/Windows/Fonts/STSONG.TTF' if os.path.exists('C:/Windows/Fonts/STSONG.TTF') else 'C:/Windows/Fonts/simsun.ttc'

f_p1_l1 = ImageFont.truetype(font_fangsong, 28)
f_p1_l2 = ImageFont.truetype(font_fangsong, 24)

f_p2_l1 = ImageFont.truetype(font_song, 36)
f_p2_l2 = ImageFont.truetype(font_fangsong, 26)

im_poster = Image.open(img_poster_path).convert('RGB')

# Texts for Phase 1
p1_text1 = "《毛泽东思想和中国特色社会主义理论体系概论》课程实践作品"
p1_text2 = "电子信息学院  ·  主创团队：柳锐凯   芮凯"

# Texts for Phase 2
p2_text1 = "“ 一 代 人 有 一 代 人 的 长 征 。 ”"
p2_text2 = "当算法算尽了效率与速度，谁来计算劳动者的尊严与温度？"

cmd = [
    ffmpeg_exe, '-y',
    '-f', 'rawvideo',
    '-vcodec', 'rawvideo',
    '-s', f'{width}x{height}',
    '-pix_fmt', 'rgb24',
    '-r', str(fps),
    '-i', '-',
    '-i', audio_path,
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '18',
    '-pix_fmt', 'yuv420p',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-shortest',
    output_video
]

proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

print(f"Rendering {total_frames} frames for 12.0s academic typewriter intro...")

for i in range(total_frames):
    t = i / fps
    
    # ---------------- PHASE 1: 0.0s - 3.4s ----------------
    if t < 3.4:
        frame = Image.new('RGB', (width, height), (8, 10, 16))
        draw = ImageDraw.Draw(frame)
        
        # Calculate typewriter progress
        # Line 1 types from 0.4s to 1.8s (1.4s total, 31 chars)
        if t < 0.4:
            chars1 = 0
        elif t < 1.8:
            chars1 = int(len(p1_text1) * ((t - 0.4) / 1.4))
        else:
            chars1 = len(p1_text1)
            
        # Line 2 types from 1.9s to 2.8s (0.9s total, 23 chars)
        if t < 1.9:
            chars2 = 0
        elif t < 2.8:
            chars2 = int(len(p1_text2) * ((t - 1.9) / 0.9))
        else:
            chars2 = len(p1_text2)
            
        cur_text1 = p1_text1[:chars1]
        cur_text2 = p1_text2[:chars2]
        
        # Blinking cursor
        blink = (int(t * 4) % 2 == 0) and (t < 2.9)
        cursor1 = " |" if (blink and chars1 < len(p1_text1)) else ""
        cursor2 = " |" if (blink and chars1 >= len(p1_text1) and chars2 < len(p1_text2)) else ""
        
        # Overall fade out for Phase 1 (3.0s to 3.4s)
        p1_alpha = 1.0 if t < 3.0 else max(0.0, (3.4 - t) / 0.4)
        
        # Draw line 1
        b1 = f_p1_l1.getbbox(p1_text1)
        w1 = b1[2] - b1[0]
        x1 = (width - w1) // 2
        y1 = height // 2 - 45
        c1 = int(240 * p1_alpha)
        draw.text((x1, y1), cur_text1 + cursor1, font=f_p1_l1, fill=(c1, c1, int(c1 * 0.95)))
        
        # Draw line 2 (College & Team)
        b2 = f_p1_l2.getbbox(p1_text2)
        w2 = b2[2] - b2[0]
        x2 = (width - w2) // 2
        y2 = height // 2 + 25
        c2_r = int(235 * p1_alpha)
        c2_g = int(205 * p1_alpha)
        c2_b = int(140 * p1_alpha)
        draw.text((x2, y2), cur_text2 + cursor2, font=f_p1_l2, fill=(c2_r, c2_g, c2_b))
        
    # ---------------- PHASE 2: 3.4s - 6.3s ----------------
    elif t < 6.3:
        frame = Image.new('RGB', (width, height), (8, 10, 16))
        draw = ImageDraw.Draw(frame)
        
        # Fade in line 1 from 3.6s to 4.2s
        if t < 3.6:
            a1 = 0.0
        elif t < 4.2:
            a1 = (t - 3.6) / 0.6
        elif t > 5.9:
            a1 = max(0.0, (6.3 - t) / 0.4)
        else:
            a1 = 1.0
            
        # Fade in line 2 from 4.4s to 5.0s
        if t < 4.4:
            a2 = 0.0
        elif t < 5.0:
            a2 = (t - 4.4) / 0.6
        elif t > 5.9:
            a2 = max(0.0, (6.3 - t) / 0.4)
        else:
            a2 = 1.0
            
        b1 = f_p2_l1.getbbox(p2_text1)
        w1 = b1[2] - b1[0]
        x1 = (width - w1) // 2
        y1 = height // 2 - 50
        draw.text((x1, y1), p2_text1, font=f_p2_l1, fill=(int(255 * a1), int(225 * a1), int(130 * a1)))
        
        b2 = f_p2_l2.getbbox(p2_text2)
        w2 = b2[2] - b2[0]
        x2 = (width - w2) // 2
        y2 = height // 2 + 25
        draw.text((x2, y2), p2_text2, font=f_p2_l2, fill=(int(240 * a2), int(245 * a2), int(250 * a2)))
        
    # ---------------- PHASE 3: 6.3s - 12.0s ----------------
    else:
        # Slam reveal of poster!
        zoom = 1.00 + 0.035 * ((t - 6.3) / 5.7)
        cw = int(im_poster.width / zoom)
        ch = int(im_poster.height / zoom)
        cx = (im_poster.width - cw) // 2
        cy = (im_poster.height - ch) // 2
        frame = im_poster.crop((cx, cy, cx + cw, cy + ch)).resize((width, height), Image.Resampling.BILINEAR)
        
        # Flash / brightness punch at 6.3s - 6.6s
        if t < 6.6:
            flash_factor = (6.6 - t) / 0.3 # 1.0 -> 0.0
            arr = np.array(frame, dtype=np.float32)
            arr += 120 * flash_factor
            frame = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
            
        # Final fade to black from 11.2s to 12.0s
        if t > 11.2:
            fade_out = (t - 11.2) / 0.8
            black = Image.new('RGB', (width, height), (0, 0, 0))
            frame = Image.blend(frame, black, min(1.0, fade_out))

    proc.stdin.write(frame.tobytes())

proc.stdin.close()
proc.wait()

print(f"Academic typewriter intro rendered successfully to: {output_video}")
