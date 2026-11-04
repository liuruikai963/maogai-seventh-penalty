# -*- coding: utf-8 -*-
import os, subprocess, imageio_ffmpeg, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import wave

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
output_video = 'dist/acts/behind_the_scenes_featurette.mp4'
os.makedirs('dist/acts', exist_ok=True)

width, height = 1280, 720
fps = 24
duration = 52.0
total_frames = int(fps * duration) # 1248 frames

# 1. Fonts
font_song = 'C:/Windows/Fonts/STSONG.TTF' if os.path.exists('C:/Windows/Fonts/STSONG.TTF') else 'C:/Windows/Fonts/simsun.ttc'
font_fangsong = 'C:/Windows/Fonts/simfang.ttf'
font_dengb = 'C:/Windows/Fonts/Dengb.ttf' if os.path.exists('C:/Windows/Fonts/Dengb.ttf') else 'C:/Windows/Fonts/msyhbd.ttc'

f_title_big = ImageFont.truetype(font_song, 48)
f_sub = ImageFont.truetype(font_fangsong, 22)
f_banner = ImageFont.truetype(font_dengb, 24)
f_tag = ImageFont.truetype(font_dengb, 26)
f_desc = ImageFont.truetype(font_fangsong, 21)
f_funny = ImageFont.truetype(font_dengb, 32)
f_quote = ImageFont.truetype(font_fangsong, 24)

# Colors
C_GOLD = (255, 218, 110)
C_WHITE = (250, 252, 255)
C_CHAMPAGNE = (235, 215, 175)
C_RED_WARN = (255, 80, 80)
C_CYAN = (100, 220, 255)

# Load Point 1 Images
img_p1_v0 = Image.open('assets/images/scene_optimization_shot06_indoor_lobby_v0.jpg').convert('RGB')
img_p1_v1 = Image.open('assets/images/scene_optimization_shot06_office_v1.jpg').convert('RGB')
img_p1_v2 = Image.open('assets/images/scene_optimization_shot06_subway_v2.jpg').convert('RGB')

# Extract frames for Point 2 and Point 3 from blooper videos
v2_clip = 'C:/Users/27277/.gemini/antigravity/brain/f5b14212-99d2-460d-9706-e55469254373/blooper_point2_shot01_daida.mp4'
v3_clip = 'C:/Users/27277/.gemini/antigravity/brain/f5b14212-99d2-460d-9706-e55469254373/blooper_point3_shot03_spitting_rain.mp4'

tmp_v2_frames_dir = 'build/tmp_v2_frames'
tmp_v3_frames_dir = 'build/tmp_v3_frames'
os.makedirs(tmp_v2_frames_dir, exist_ok=True)
os.makedirs(tmp_v3_frames_dir, exist_ok=True)

print("Extracting frames from blooper video 2...")
subprocess.run([ffmpeg_exe, '-y', '-i', v2_clip, '-r', str(fps), os.path.join(tmp_v2_frames_dir, 'frame_%04d.jpg')], check=True, stderr=subprocess.DEVNULL)

print("Extracting frames from blooper video 3...")
subprocess.run([ffmpeg_exe, '-y', '-i', v3_clip, '-r', str(fps), os.path.join(tmp_v3_frames_dir, 'frame_%04d.jpg')], check=True, stderr=subprocess.DEVNULL)

v2_frame_files = sorted([os.path.join(tmp_v2_frames_dir, f) for f in os.listdir(tmp_v2_frames_dir) if f.endswith('.jpg')])
v3_frame_files = sorted([os.path.join(tmp_v3_frames_dir, f) for f in os.listdir(tmp_v3_frames_dir) if f.endswith('.jpg')])
print(f"Loaded {len(v2_frame_files)} frames for Point 2, {len(v3_frame_files)} frames for Point 3")

# Synthesize 52s Master Audio Track
sr = 48000
total_audio_samples = int(sr * duration)
t_audio = np.linspace(0, duration, total_audio_samples, endpoint=False)
audio_left = np.zeros(total_audio_samples, dtype=np.float32)
audio_right = np.zeros(total_audio_samples, dtype=np.float32)

# Playful, upbeat rhythmic acoustic progression throughout, softened during bloopers
chords_52s = [
    (0.0, 4.0, [261.63, 329.63, 392.00]),    # Intro Cmaj
    (4.0, 10.0, [261.63, 329.63, 392.00]),   # P1-v0 Cmaj
    (10.0, 16.0, [220.00, 261.63, 329.63]),  # P1-v1 Am
    (16.0, 22.0, [174.61, 261.63, 349.23]),  # P1-v2 Fmaj warm
    (22.0, 34.0, [196.00, 246.94, 293.66]),  # P2 Gmaj playful
    (34.0, 45.0, [220.00, 261.63, 329.63]),  # P3 Am mystery
    (45.0, 52.0, [261.63, 329.63, 392.00]),  # Outro Cmaj warm
]

for st, et, freqs in chords_52s:
    s_idx = int(st * sr)
    e_idx = int(et * sr)
    c_len = e_idx - s_idx
    ct = np.linspace(0, et - st, c_len)
    
    vol = 0.08
    if 24.5 <= st <= 33.0 or 36.5 <= st <= 44.0:
        vol = 0.025 # Duck BGM to let blooper dialogue/foley sound crisp!
        
    for f in freqs:
        wave_f = np.sin(2 * np.pi * f * ct) * vol
        audio_left[s_idx:e_idx] += wave_f
        audio_right[s_idx:e_idx] += wave_f

# Mix in blooper audio 2 at t=24.5s
def mix_wav(wav_path, start_time, gain=1.0):
    with wave.open(wav_path, 'rb') as wf:
        n_ch = wf.getnchannels()
        sw = wf.getsampwidth()
        n_f = wf.getnframes()
        data = wf.readframes(n_f)
    raw = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
    if n_ch == 2:
        raw = raw.reshape(-1, 2)
        l_wav = raw[:, 0] * gain
        r_wav = raw[:, 1] * gain
    else:
        l_wav = raw * gain
        r_wav = raw * gain
    s_idx = int(start_time * sr)
    e_idx = s_idx + len(l_wav)
    if e_idx > total_audio_samples:
        l_wav = l_wav[:total_audio_samples - s_idx]
        r_wav = r_wav[:total_audio_samples - s_idx]
        e_idx = total_audio_samples
    audio_left[s_idx:e_idx] += l_wav
    audio_right[s_idx:e_idx] += r_wav

mix_wav('assets/audio/foley/blooper_daida.wav', 24.5, gain=1.2)
mix_wav('assets/audio/foley/blooper_spitting.wav', 36.5, gain=1.1)

# Normalize
peak = max(np.max(np.abs(audio_left)), np.max(np.abs(audio_right)))
if peak > 0:
    audio_left = audio_left / peak * 0.90
    audio_right = audio_right / peak * 0.90

# Fade out at the end
fade_samples = int(1.5 * sr)
audio_left[-fade_samples:] *= np.linspace(1, 0, fade_samples)
audio_right[-fade_samples:] *= np.linspace(1, 0, fade_samples)

master_audio_path = 'assets/audio/foley/bts_master_audio.wav'
stereo_int = np.vstack(((audio_left * 32767).astype(np.int16), (audio_right * 32767).astype(np.int16))).T.flatten()
with wave.open(master_audio_path, 'wb') as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sr)
    wf.writeframes(stereo_int.tobytes())
print(f"Generated BTS master audio: {master_audio_path}")

# Helper to fit image into 1280x720 maintaining aspect ratio with letterbox/crop
def prepare_base_img(pil_img):
    w, h = pil_img.size
    aspect = w / h
    target_aspect = width / height
    if aspect > target_aspect:
        new_h = height
        new_w = int(height * aspect)
    else:
        new_w = width
        new_h = int(width / aspect)
    resized = pil_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    cx, cy = new_w // 2, new_h // 2
    return resized.crop((cx - width//2, cy - height//2, cx + width//2, cy + height//2))

base_p1_v0 = prepare_base_img(img_p1_v0)
base_p1_v1 = prepare_base_img(img_p1_v1)
base_p1_v2 = prepare_base_img(img_p1_v2)

def fit_image_fast(base_img, zoom=1.0):
    if zoom <= 1.001:
        return base_img
    zw = int(width * zoom)
    zh = int(height * zoom)
    z_img = base_img.resize((zw, zh), Image.Resampling.BILINEAR)
    cx, cy = zw // 2, zh // 2
    return z_img.crop((cx - width//2, cy - height//2, cx + width//2, cy + height//2))

# FFmpeg Rendering Process
cmd = [
    ffmpeg_exe, '-y',
    '-f', 'rawvideo',
    '-vcodec', 'rawvideo',
    '-s', f'{width}x{height}',
    '-pix_fmt', 'rgb24',
    '-r', str(fps),
    '-i', '-',
    '-i', master_audio_path,
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
print(f"Rendering {total_frames} frames for 52.0s Behind-The-Scenes Featurette...")

for i in range(total_frames):
    t = i / fps
    frame = Image.new('RGB', (width, height), (10, 14, 23))
    draw = ImageDraw.Draw(frame)
    
    # -------------------------------------------------------------
    # SECTION 0: Title Card (0.0s - 4.0s)
    # -------------------------------------------------------------
    if t < 4.0:
        # Title
        t_str = "《算法之外》幕后制作花絮"
        tb = f_title_big.getbbox(t_str)
        draw.text(((width - (tb[2]-tb[0])) // 2, 220), t_str, font=f_title_big, fill=C_GOLD)
        
        sub_str = "创作实录 · 同场景深度打磨 · AI 趣味翻车"
        sb = f_sub.getbbox(sub_str)
        draw.text(((width - (sb[2]-sb[0])) // 2, 290), sub_str, font=f_sub, fill=C_WHITE)
        
        # Division
        d_str = "电子信息学院  ·  主创团队：柳锐凯   芮凯"
        db = f_desc.getbbox(d_str)
        draw.text(((width - (db[2]-db[0])) // 2, 380), d_str, font=f_desc, fill=C_CHAMPAGNE)
        
        m_str = "“每一次翻车都是探索，每一次取舍都是温度”"
        mb = f_desc.getbbox(m_str)
        draw.text(((width - (mb[2]-mb[0])) // 2, 430), m_str, font=f_desc, fill=(160, 175, 195))
        
        # Fade in / out
        if t < 0.6:
            alpha = t / 0.6
            black = Image.new('RGB', (width, height), (0, 0, 0))
            frame = Image.blend(black, frame, alpha)
        elif t > 3.4:
            alpha = (4.0 - t) / 0.6
            black = Image.new('RGB', (width, height), (0, 0, 0))
            frame = Image.blend(black, frame, alpha)

    # -------------------------------------------------------------
    # SECTION 1: Point 1 - Three-Stage Scene Evolution (4.0s - 22.0s)
    # -------------------------------------------------------------
    elif 4.0 <= t < 22.0:
        p1_t = t - 4.0
        
        # Choose which image
        if p1_t < 6.0: # 4.0s - 10.0s: Indoor lobby
            prog = p1_t / 6.0
            zoom = 1.0 + 0.04 * prog
            base_bg = fit_image_fast(base_p1_v0, zoom)
            tag_text = "【初版构想 · 室内大堂】"
            desc_text = "老刘在公司前台焦急求情，陆远路过 —— 导演考量：脱离大厂闸机门禁现实，室内灯光冲淡风雨寒冷感"
            tag_col = (255, 180, 80)
        elif p1_t < 12.0: # 10.0s - 16.0s: Office exterior
            prog = (p1_t - 6.0) / 6.0
            zoom = 1.0 + 0.04 * prog
            base_bg = fit_image_fast(base_p1_v1, zoom)
            tag_text = "【二版探索 · 写字楼门外】"
            desc_text = "移至室外旋转门前，符合门禁 —— 导演考量：商务感依然偏重，老刘手提塑料袋，情绪表现较为平淡"
            tag_col = (100, 200, 255)
        else: # 16.0s - 22.0s: Dawn subway station (Final Pick!)
            prog = (p1_t - 12.0) / 6.0
            zoom = 1.0 + 0.04 * prog
            base_bg = fit_image_fast(base_p1_v2, zoom)
            tag_text = "【终选成片 · 清晨寒风地铁站】 ★ 质感封神"
            desc_text = "双手捧着咬开的白馒头、湿阶上的黄色头盔、泥泞裤脚 —— 现实心酸感拉满，直击人心促成陆远觉醒！"
            tag_col = C_GOLD
            
        frame.paste(base_bg, (0, 0))
        draw = ImageDraw.Draw(frame)
        
        # Top Banner
        draw.rectangle([(0, 0), (width, 52)], fill=(15, 20, 30, 220))
        b_str = "花絮点一：同场景深度挑选与艺术打磨（三重演进）"
        draw.text((30, 12), b_str, font=f_banner, fill=C_GOLD)
        
        # Tag on top right
        tb = f_tag.getbbox(tag_text)
        draw.rectangle([(width - (tb[2]-tb[0]) - 50, 10), (width - 20, 44)], fill=(0, 0, 0, 180))
        draw.text((width - (tb[2]-tb[0]) - 35, 12), tag_text, font=f_tag, fill=tag_col)
        
        # Bottom Description Card
        draw.rectangle([(0, height - 70), (width, height)], fill=(12, 16, 25, 235))
        draw.line([(0, height - 70), (width, height - 70)], fill=(80, 100, 130), width=1)
        db = f_desc.getbbox(desc_text)
        draw.text(((width - (db[2]-db[0])) // 2, height - 48), desc_text, font=f_desc, fill=C_WHITE)

    # -------------------------------------------------------------
    # SECTION 2: Point 2 - "代打" Blooper (22.0s - 34.0s)
    # -------------------------------------------------------------
    elif 22.0 <= t < 34.0:
        p2_t = t - 22.0
        
        if p2_t < 2.5: # 22.0s - 24.5s: Intro Card
            draw.rectangle([(0, 0), (width, height)], fill=(12, 16, 26))
            b_str = "【花絮点二：Shot 01 经典发音翻车 · 大厂工程师变“游戏代练”】"
            tb = f_banner.getbbox(b_str)
            draw.text(((width - (tb[2]-tb[0])) // 2, 250), b_str, font=f_banner, fill=C_GOLD)
            
            q_str = "严肃沉重的大厂算法架构师，怎么一开口……做起了兼职？！"
            qb = f_funny.getbbox(q_str)
            draw.text(((width - (qb[2]-qb[0])) // 2, 330), q_str, font=f_funny, fill=C_WHITE)
            
            hint_str = "▶ 请听原视频音频中 02.0s ~ 06.5s 处口型与发音"
            hb = f_desc.getbbox(hint_str)
            draw.text(((width - (hb[2]-hb[0])) // 2, 420), hint_str, font=f_desc, fill=C_CYAN)
        else: # 24.5s - 34.0s: Video playback
            v_t = p2_t - 2.5
            idx = min(int(v_t * fps), len(v2_frame_files) - 1)
            v_img = Image.open(v2_frame_files[idx]).convert('RGB')
            frame.paste(v_img, (0, 0))
            draw = ImageDraw.Draw(frame)
            
            # Top Header
            draw.rectangle([(0, 0), (width, 48)], fill=(15, 20, 30, 220))
            draw.text((30, 10), "花絮点二：Shot 01 原生视频台词口误实录", font=f_banner, fill=C_GOLD)
            
            # When Lu Yuan speaks "daida" around v_t ~ 1.5s - 4.5s (t ~ 26.0s - 29.0s)
            if 1.5 <= v_t <= 5.0:
                # Big funny comic banner overlay
                draw.rectangle([(width//2 - 420, 80), (width//2 + 420, 145)], fill=(220, 30, 30, 220))
                alert_text = "“等等……你说什么？！‘代码’ 念成了 ‘代打’？！”"
                ab = f_funny.getbbox(alert_text)
                draw.text(((width - (ab[2]-ab[0])) // 2, 92), alert_text, font=f_funny, fill=C_WHITE)
                
            # Bottom explanation
            draw.rectangle([(0, height - 60), (width, height)], fill=(12, 16, 25, 230))
            sub_explain = "★ 原片台词：本应为“编写的底层代码”，AI 语音一本正经念成“底层代打”！倒逼团队全面启动音画解耦！"
            sb = f_desc.getbbox(sub_explain)
            draw.text(((width - (sb[2]-sb[0])) // 2, height - 42), sub_explain, font=f_desc, fill=C_CHAMPAGNE)

    # -------------------------------------------------------------
    # SECTION 3: Point 3 - "吐口水" Rain Blooper (34.0s - 45.0s)
    # -------------------------------------------------------------
    elif 34.0 <= t < 45.0:
        p3_t = t - 34.0
        
        if p3_t < 2.5: # 34.0s - 36.5s: Intro Card
            draw.rectangle([(0, 0), (width, height)], fill=(12, 16, 26))
            b_str = "【花絮点三：Shot 03 诡异流体物理 · 手机屏幕“吐口水”】"
            tb = f_banner.getbbox(b_str)
            draw.text(((width - (tb[2]-tb[0])) // 2, 250), b_str, font=f_banner, fill=C_GOLD)
            
            q_str = "暴雨如注的黑夜……顺着手机支架流下来的到底是什么？！"
            qb = f_funny.getbbox(q_str)
            draw.text(((width - (qb[2]-qb[0])) // 2, 330), q_str, font=f_funny, fill=C_WHITE)
            
            hint_str = "▶ 请注意观察手机支架底部极其黏稠拉丝的流体动态"
            hb = f_desc.getbbox(hint_str)
            draw.text(((width - (hb[2]-hb[0])) // 2, 420), hint_str, font=f_desc, fill=C_CYAN)
        else: # 36.5s - 45.0s: Video playback
            v_t = p3_t - 2.5
            idx = min(int(v_t * fps), len(v3_frame_files) - 1)
            v_img = Image.open(v3_frame_files[idx]).convert('RGB')
            frame.paste(v_img, (0, 0))
            draw = ImageDraw.Draw(frame)
            
            # Top Header
            draw.rectangle([(0, 0), (width, 48)], fill=(15, 20, 30, 220))
            draw.text((30, 10), "花絮点三：Shot 03 手机支架雨水物理引擎离奇崩坏", font=f_banner, fill=C_GOLD)
            
            # Comic alert banner
            draw.rectangle([(width//2 - 420, 80), (width//2 + 420, 145)], fill=(180, 40, 180, 220))
            alert_text = "“ AI 物理流体大崩塌：这雨水怎么白亮黏稠，像在吐口水？！ ”"
            ab = f_funny.getbbox(alert_text)
            draw.text(((width - (ab[2]-ab[0])) // 2, 92), alert_text, font=f_funny, fill=C_WHITE)
            
            # Draw red focus box around bottom of phone where saliva-rain drips
            draw.rectangle([(width//2 - 90, height - 240), (width//2 + 90, height - 70)], outline=(255, 60, 60), width=3)
            
            # Bottom explanation
            draw.rectangle([(0, height - 60), (width, height)], fill=(12, 16, 25, 230))
            sub_explain = "★ AI 流体模拟失控：暴雨不仅没有水珠飞溅，反而在支架处拉丝下垂，生动诠释生成式 AI 的荒诞魅力！"
            sb = f_desc.getbbox(sub_explain)
            draw.text(((width - (sb[2]-sb[0])) // 2, height - 42), sub_explain, font=f_desc, fill=C_CHAMPAGNE)

    # -------------------------------------------------------------
    # SECTION 4: Outro / Summary (45.0s - 52.0s)
    # -------------------------------------------------------------
    else:
        p4_t = t - 45.0
        draw.rectangle([(0, 0), (width, height)], fill=(8, 12, 20))
        
        # Ideological Quote
        q1 = "“ 一 次 次 翻 车 是 探 索 ， 一 处 处 取 舍 是 温 度 。 ”"
        q1_b = f_quote.getbbox(q1)
        draw.text(((width - (q1_b[2]-q1_b[0])) // 2, 220), q1, font=f_quote, fill=C_GOLD)
        
        q2 = "以工科严谨驾驭生成式 AI  ·  以青年担当诠释科技向善"
        q2_b = f_desc.getbbox(q2)
        draw.text(((width - (q2_b[2]-q2_b[0])) // 2, 290), q2, font=f_desc, fill=C_WHITE)
        
        # Separation
        draw.line([(width//2 - 120, 360), (width//2 + 120, 360)], fill=(100, 120, 150), width=1)
        
        c_str = "电子信息学院《算法之外》主创团队  ·  敬献"
        cb = f_desc.getbbox(c_str)
        draw.text(((width - (cb[2]-cb[0])) // 2, 400), c_str, font=f_desc, fill=C_CHAMPAGNE)
        
        # Fade out to black at the very end (50.5s - 52.0s)
        if p4_t > 5.5:
            alpha = (p4_t - 5.5) / 1.5
            black = Image.new('RGB', (width, height), (0, 0, 0))
            frame = Image.blend(frame, black, min(1.0, alpha))

    proc.stdin.write(frame.tobytes())

proc.stdin.close()
proc.wait()

print(f"Behind-The-Scenes Featurette rendered successfully: {output_video}")

# Copy to artifacts
artifact_dir = r'C:/Users/27277/.gemini/antigravity/brain/f5b14212-99d2-460d-9706-e55469254373'
artifact_copy = os.path.join(artifact_dir, 'behind_the_scenes_featurette.mp4')
shutil.copy(output_video, artifact_copy)
print(f"Copied to artifact directory: {artifact_copy}")
