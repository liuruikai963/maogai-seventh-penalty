# -*- coding: utf-8 -*-
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg
import numpy as np
import wave

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
output_video = 'dist/acts/outro_credits_sequence.mp4'
os.makedirs('dist/acts', exist_ok=True)

width, height = 1280, 720
fps = 24
duration = 24.0 # 24.0 seconds for smooth, dignified rolling credits!
total_frames = int(fps * duration) # 576 frames

# 1. Generate Warm, Moving Ending BGM (Cello & Piano Warm Progression)
sr = 48000
total_audio_samples = int(sr * duration)
t_audio = np.linspace(0, duration, total_audio_samples, endpoint=False)
audio = np.zeros(total_audio_samples, dtype=np.float32)

# Warm chord progression: Cmaj -> Gmaj -> Am -> Fmaj -> Cmaj
chords = [
    (0.0, 5.0, [261.63, 329.63, 392.00, 523.25]),     # C major (C4, E4, G4, C5)
    (5.0, 10.0, [196.00, 293.66, 392.00, 493.88]),    # G major (G3, D4, G4, B4)
    (10.0, 15.0, [220.00, 261.63, 329.63, 440.00]),   # A minor (A3, C4, E4, A4)
    (15.0, 20.0, [174.61, 261.63, 349.23, 440.00]),   # F major (F3, C4, F4, A4)
    (20.0, 24.0, [261.63, 329.63, 392.00, 523.25]),   # C major resolution
]

for start_t, end_t, freqs in chords:
    s_idx = int(start_t * sr)
    e_idx = int(end_t * sr)
    c_len = e_idx - s_idx
    ct = np.linspace(0, end_t - start_t, c_len)
    
    # Soft attack and decay envelope
    env = np.ones(c_len, dtype=np.float32)
    att = int(0.6 * sr)
    dec = int(0.8 * sr)
    env[:att] = np.linspace(0, 1, att)
    env[-dec:] = np.linspace(1, 0, dec)
    
    for f in freqs:
        # fundamental + soft 2nd harmonic
        wave_f = (np.sin(2 * np.pi * f * ct) * 0.7 + np.sin(4 * np.pi * f * ct) * 0.3)
        audio[s_idx:e_idx] += wave_f * env * 0.12

# Add soft piano melody notes sprinkled on top
melody_notes = [
    (1.0, 523.25), (2.5, 587.33), (4.0, 659.25),
    (6.0, 587.33), (7.5, 523.25), (9.0, 493.88),
    (11.0, 440.00), (12.5, 493.88), (14.0, 523.25),
    (16.0, 440.00), (17.5, 392.00), (19.0, 349.23),
    (20.5, 392.00), (21.5, 523.25)
]

for note_t, note_f in melody_notes:
    idx = int(note_t * sr)
    n_len = int(2.0 * sr)
    if idx + n_len > total_audio_samples:
        n_len = total_audio_samples - idx
    nt = np.linspace(0, n_len / sr, n_len)
    note_wave = (np.sin(2 * np.pi * note_f * nt) * 0.7 + np.sin(4 * np.pi * note_f * nt) * 0.3) * np.exp(-nt * 2.2)
    audio[idx:idx+n_len] += note_wave * 0.22

# Normalize and fade out
peak = np.max(np.abs(audio))
if peak > 0:
    audio = audio / peak * 0.88
fade_out_samples = int(1.5 * sr)
audio[-fade_out_samples:] *= np.linspace(1, 0, fade_out_samples)

audio_path = 'assets/audio/foley/outro_credits_audio_master.wav'
int_audio = (audio * 32767).astype(np.int16)
with wave.open(audio_path, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sr)
    wf.writeframes(int_audio.tobytes())
print(f"Generated outro audio: {audio_path}")

# 2. Build the Long Rolling Canvas Image
# Fonts
font_song = 'C:/Windows/Fonts/STSONG.TTF' if os.path.exists('C:/Windows/Fonts/STSONG.TTF') else 'C:/Windows/Fonts/simsun.ttc'
font_fangsong = 'C:/Windows/Fonts/simfang.ttf'
font_dengb = 'C:/Windows/Fonts/Dengb.ttf' if os.path.exists('C:/Windows/Fonts/Dengb.ttf') else 'C:/Windows/Fonts/msyhbd.ttc'

f_title = ImageFont.truetype(font_song, 68)
f_en = ImageFont.truetype(font_fangsong, 20)
f_slogan = ImageFont.truetype(font_dengb, 26)
f_section = ImageFont.truetype(font_song, 30)
f_role = ImageFont.truetype(font_fangsong, 24)
f_name = ImageFont.truetype(font_dengb, 24)
f_quote = ImageFont.truetype(font_fangsong, 22)
f_foot = ImageFont.truetype(font_fangsong, 20)

# Colors
C_GOLD = (255, 218, 110)
C_WHITE = (250, 252, 255)
C_CHAMPAGNE = (235, 215, 175)
C_SUBTLE = (180, 190, 205)

# Render credit items into a list of tuples: (type, text1, text2)
# 'title', 'en', 'slogan', 'sep', 'section', 'item', 'quote', 'space'
credits_script = [
    ('space', 180),
    ('title', "算  法  之  外"),
    ('en', "B E Y O N D   T H E   A L G O R I T H M"),
    ('slogan', "算力有极限 · 善意无边界"),
    ('space', 50),
    ('sep', 200),
    ('space', 40),
    ('section', "《毛泽东思想和中国特色社会主义理论体系概论》课程实践微电影"),
    ('role_name', "出品院系", "电子信息学院"),
    ('space', 40),
    ('section', "主 创 制 作 名 单"),
    ('space', 20),
    ('role_name', "导    演", "柳 锐 凯"),
    ('space', 15),
    ('role_name', "编    剧", "柳 锐 凯  ·  芮  凯"),
    ('space', 15),
    ('role_name', "第一至三幕总制作", "柳 锐 凯"),
    ('space', 15),
    ('role_name', "第四至五幕总制作", "芮  凯"),
    ('space', 15),
    ('role_name', "概念片头设计制作", "柳 锐 凯"),
    ('space', 15),
    ('role_name', "片尾思政理论总结", "柳 锐 凯"),
    ('space', 15),
    ('role_name', "幕后花絮设计制作", "柳 锐 凯"),
    ('space', 15),
    ('role_name', "角色声线与配音一致性", "芮  凯"),
    ('space', 50),
    ('sep', 200),
    ('space', 40),
    ('section', "思 政 实 践 核 心 寄 语"),
    ('space', 25),
    ('quote', "“ 一 代 人 有 一 代 人 的 长 征 。 ”"),
    ('space', 15),
    ('quote', "科技发展的根本旨归，在于人的自由全面发展，绝非对劳动者的算力异化。"),
    ('space', 10),
    ('quote', "发展新质生产力，既要算力效率的锋芒，更要筑牢制度底线的温度。"),
    ('space', 10),
    ('quote', "把见义勇为与崇高美德编译进规则，让科技向光而行，让算法拥抱善意！"),
    ('space', 50),
    ('sep', 200),
    ('space', 40),
    ('section', "特 别 鸣 谢"),
    ('space', 20),
    ('foot', "课程指导老师  ·  全体授课同窗"),
    ('space', 10),
    ('foot', "致敬全国每一位风雨无阻的新就业形态劳动者"),
    ('space', 25),
    ('foot', "电子信息学院《算法之外》主创团队 · 敬献"),
    ('space', 350) # Bottom padding so it rolls off gracefully
]

# Calculate total canvas height
canvas_h = 0
for item in credits_script:
    kind = item[0]
    if kind == 'space':
        canvas_h += item[1]
    elif kind == 'title':
        canvas_h += 85
    elif kind == 'en':
        canvas_h += 35
    elif kind == 'slogan':
        canvas_h += 45
    elif kind == 'sep':
        canvas_h += 20
    elif kind == 'section':
        canvas_h += 55
    elif kind == 'role_name':
        canvas_h += 40
    elif kind == 'quote':
        canvas_h += 38
    elif kind == 'foot':
        canvas_h += 36

print(f"Calculated credits canvas height: {canvas_h}px")

# Draw the big canvas
canvas = Image.new('RGB', (width, canvas_h), (8, 11, 18))
draw = ImageDraw.Draw(canvas)

curr_y = 0
for item in credits_script:
    kind = item[0]
    if kind == 'space':
        curr_y += item[1]
    elif kind == 'title':
        bbox = f_title.getbbox(item[1])
        w = bbox[2] - bbox[0]
        draw.text(((width - w) // 2, curr_y), item[1], font=f_title, fill=C_WHITE)
        curr_y += 85
    elif kind == 'en':
        bbox = f_en.getbbox(item[1])
        w = bbox[2] - bbox[0]
        draw.text(((width - w) // 2, curr_y), item[1], font=f_en, fill=C_CHAMPAGNE)
        curr_y += 35
    elif kind == 'slogan':
        bbox = f_slogan.getbbox(item[1])
        w = bbox[2] - bbox[0]
        draw.text(((width - w) // 2, curr_y), item[1], font=f_slogan, fill=C_GOLD)
        curr_y += 45
    elif kind == 'sep':
        line_w = item[1]
        draw.line([(width//2 - line_w//2, curr_y + 10), (width//2 + line_w//2, curr_y + 10)], fill=(120, 140, 175), width=1)
        curr_y += 20
    elif kind == 'section':
        bbox = f_section.getbbox(item[1])
        w = bbox[2] - bbox[0]
        draw.text(((width - w) // 2, curr_y), item[1], font=f_section, fill=C_GOLD)
        curr_y += 55
    elif kind == 'role_name':
        role_str = item[1]
        name_str = item[2]
        # Align: role right-aligned to center-30, name left-aligned to center+30
        r_bbox = f_role.getbbox(role_str)
        r_w = r_bbox[2] - r_bbox[0]
        draw.text((width // 2 - 30 - r_w, curr_y), role_str, font=f_role, fill=C_SUBTLE)
        draw.text((width // 2 + 30, curr_y), name_str, font=f_name, fill=C_WHITE)
        curr_y += 40
    elif kind == 'quote':
        bbox = f_quote.getbbox(item[1])
        w = bbox[2] - bbox[0]
        draw.text(((width - w) // 2, curr_y), item[1], font=f_quote, fill=C_WHITE)
        curr_y += 38
    elif kind == 'foot':
        bbox = f_foot.getbbox(item[1])
        w = bbox[2] - bbox[0]
        draw.text(((width - w) // 2, curr_y), item[1], font=f_foot, fill=C_CHAMPAGNE)
        curr_y += 36

# Render Video via FFmpeg Pipe
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
print(f"Rendering {total_frames} frames for {duration}s rolling credits video...")

# Total scroll distance = canvas_h - height
scroll_dist = canvas_h - height

for i in range(total_frames):
    t = i / fps
    
    # Progress 0.0 to 1.0 from t=1.0s to t=22.0s
    if t < 1.0:
        prog = 0.0
    elif t > 22.0:
        prog = 1.0
    else:
        prog = (t - 1.0) / 21.0
        
    y_offset = int(scroll_dist * prog)
    frame = canvas.crop((0, y_offset, width, y_offset + height))
    
    # Fade in from black at the very start (0.0s - 1.0s)
    if t < 1.0:
        black = Image.new('RGB', (width, height), (8, 11, 18))
        frame = Image.blend(black, frame, t / 1.0)
        
    # Fade out to black at the end (22.5s - 24.0s)
    if t > 22.5:
        fade = (t - 22.5) / 1.5
        black = Image.new('RGB', (width, height), (0, 0, 0))
        frame = Image.blend(frame, black, min(1.0, fade))
        
    proc.stdin.write(frame.tobytes())

proc.stdin.close()
proc.wait()

print(f"Rolling credits outro rendered successfully: {output_video}")
