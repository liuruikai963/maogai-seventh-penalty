# -*- coding: utf-8 -*-
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg
import numpy as np

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

# Source paths
img_bg_path = 'assets/images/intro_title_bg.jpg'
img_poster_path = 'assets/images/poster_luyuan_laoliu_final.jpg'
audio_path = 'assets/audio/foley/intro_title_audio_master.wav'
output_video = 'dist/acts/intro_title_sequence.mp4'

os.makedirs('dist/acts', exist_ok=True)

# Target specs
width, height = 1280, 720
fps = 24
duration = 10.0
total_frames = int(fps * duration) # 240 frames

# Load images and resize to base
im_bg = Image.open(img_bg_path).convert('RGB')
im_poster = Image.open(img_poster_path).convert('RGB')

# Subtitle font
font_path = 'C:/Windows/Fonts/msyhbd.ttc'
sub_font = ImageFont.truetype(font_path, 34)

# Subtitle draw helper
def draw_subtitle(im, text, alpha_factor=1.0):
    if alpha_factor <= 0 or not text:
        return im
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    bbox = sub_font.getbbox(text)
    t_w = bbox[2] - bbox[0]
    x = (width - t_w) // 2
    y = height - 90
    
    alpha = int(255 * alpha_factor)
    shadow_alpha = int(220 * alpha_factor)
    
    # Black outline / drop shadow
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, 2), (-2, 2), (2, -2), (0, 3)]:
        draw.text((x + dx, y + dy), text, font=sub_font, fill=(0, 0, 0, shadow_alpha))
    draw.text((x, y), text, font=sub_font, fill=(255, 255, 255, alpha))
    
    return Image.alpha_composite(im.convert('RGBA'), overlay).convert('RGB')

# Start FFmpeg process with pipe
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

print(f"Rendering {total_frames} frames for 10.0s cinematic title sequence...")

for i in range(total_frames):
    t = i / fps
    
    # 1. Determine active base visual
    if t < 6.0:
        # Phase 1 & 2: intro_title_bg with slow zoom
        # Zoom from 1.00 at t=0 to 1.08 at t=6.0
        zoom = 1.0 + 0.08 * (t / 6.0)
        crop_w = int(im_bg.width / zoom)
        crop_h = int(im_bg.height / zoom)
        crop_x = (im_bg.width - crop_w) // 2
        crop_y = (im_bg.height - crop_h) // 2
        frame_base = im_bg.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h)).resize((width, height), Image.Resampling.BILINEAR)
        
        # Color temperature shift at 3.5s (sunrise bloom)
        if t >= 3.5:
            warm_factor = min(1.0, (t - 3.5) / 1.5)
            # Add warm golden overlay
            arr = np.array(frame_base, dtype=np.float32)
            arr[:, :, 0] = np.clip(arr[:, :, 0] + 35 * warm_factor, 0, 255) # Red
            arr[:, :, 1] = np.clip(arr[:, :, 1] + 20 * warm_factor, 0, 255) # Green
            frame_base = Image.fromarray(arr.astype(np.uint8))
            
    elif t < 7.0:
        # Crossfade between intro_title_bg and poster (6.0s to 7.0s)
        # Background frame at t=6.0
        zoom_bg = 1.08
        crop_w = int(im_bg.width / zoom_bg)
        crop_h = int(im_bg.height / zoom_bg)
        crop_x = (im_bg.width - crop_w) // 2
        crop_y = (im_bg.height - crop_h) // 2
        frame_bg = im_bg.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h)).resize((width, height), Image.Resampling.BILINEAR)
        
        # Poster frame with subtle start zoom
        zoom_p = 1.00 + 0.03 * ((t - 6.0) / 4.0)
        p_w = int(im_poster.width / zoom_p)
        p_h = int(im_poster.height / zoom_p)
        p_x = (im_poster.width - p_w) // 2
        p_y = (im_poster.height - p_h) // 2
        frame_p = im_poster.crop((p_x, p_y, p_x + p_w, p_y + p_h)).resize((width, height), Image.Resampling.BILINEAR)
        
        alpha_p = (t - 6.0) / 1.0 # 0.0 -> 1.0
        frame_base = Image.blend(frame_bg, frame_p, alpha_p)
        
    else:
        # Phase 3: Poster with slow push-in (7.0s to 10.0s)
        zoom_p = 1.0075 + 0.025 * ((t - 7.0) / 3.0)
        p_w = int(im_poster.width / zoom_p)
        p_h = int(im_poster.height / zoom_p)
        p_x = (im_poster.width - p_w) // 2
        p_y = (im_poster.height - p_h) // 2
        frame_base = im_poster.crop((p_x, p_y, p_x + p_w, p_y + p_h)).resize((width, height), Image.Resampling.BILINEAR)
        
    # 2. Subtitles for phase 1 and 2
    if 0.4 <= t < 3.4:
        # Fade in (0.4-0.8), hold (0.8-3.0), fade out (3.0-3.4)
        if t < 0.8:
            sub_alpha = (t - 0.4) / 0.4
        elif t > 3.0:
            sub_alpha = (3.4 - t) / 0.4
        else:
            sub_alpha = 1.0
        frame_base = draw_subtitle(frame_base, "“大模型算得出极致的履约效率……”", sub_alpha)
        
    elif 3.6 <= t < 6.0:
        # Fade in (3.6-4.0), hold (4.0-5.6), fade out (5.6-6.0)
        if t < 4.0:
            sub_alpha = (t - 3.6) / 0.4
        elif t > 5.6:
            sub_alpha = (6.0 - t) / 0.4
        else:
            sub_alpha = 1.0
        frame_base = draw_subtitle(frame_base, "“……却算不出真实的善意与温度。”", sub_alpha)

    # 3. Fade in from black at the very start (0.0 - 0.5s)
    if t < 0.5:
        black = Image.new('RGB', (width, height), (0, 0, 0))
        frame_base = Image.blend(black, frame_base, t / 0.5)

    # 4. Fade to black at the end (9.3 - 10.0s) to transition to Shot 01
    if t > 9.3:
        black = Image.new('RGB', (width, height), (0, 0, 0))
        frame_base = Image.blend(frame_base, black, (t - 9.3) / 0.7)

    proc.stdin.write(frame_base.tobytes())

proc.stdin.close()
proc.wait()

print(f"Render complete! Title sequence video saved to: {output_video}")
