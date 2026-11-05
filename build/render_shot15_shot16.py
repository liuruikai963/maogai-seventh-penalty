# -*- coding: utf-8 -*-
"""
Script: render_shot15_shot16.py
Description:
  1. Standardizes shot_15_raw.mp4 and shot_16_raw.mp4.
  2. Renders dist/shots/shot_15_final.mp4 with subtitle:
     陆远：“技术方案准备完毕，现在开始全面重构。” (2.5s - 7.5s)
  3. Renders dist/shots/shot_16_final.mp4 with subtitle:
     陆远：“底层规则重写完成，正在执行编译。” (3.0s - 7.5s)
  4. Copies to artifact directory.
"""
import os
import shutil
import subprocess
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base_dir = "d:/study/course/maogai/homework"
raw_dir = os.path.join(base_dir, "assets", "videos", "raw_inputs")
shots_dir = os.path.join(base_dir, "dist", "shots")
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"
font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

os.makedirs(shots_dir, exist_ok=True)

# Step 1: Standardize Shot 16
v16_src = os.path.join(raw_dir, "gemini_generated_video_4bd4fd4a.mp4")
v16_std = os.path.join(raw_dir, "shot_16_raw.mp4")
if os.path.exists(v16_src):
    shutil.copy2(v16_src, v16_std)
    print(f"Standardized Shot 16: {v16_std}")

# Step 2: Render Shot 15 Final
v15_std = os.path.join(raw_dir, "shot_15_raw.mp4")
s15_out = os.path.join(shots_dir, "shot_15_final.mp4")
sub_15 = "陆远：“技术方案准备完毕，现在开始全面重构。”"
filter_15 = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_15}':"
    f"fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:"
    f"x=(w-text_w)/2:y=h-70:enable='between(t,2.5,7.5)'[vout]"
)
cmd_15 = [
    ffmpeg, "-y",
    "-i", v15_std,
    "-filter_complex", filter_15,
    "-map", "[vout]", "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "copy",
    "-t", "10.03",
    s15_out
]
print("Rendering Shot 15 Final...")
subprocess.run(cmd_15, check=True)
print(f"Shot 15 rendered: {s15_out}")

# Step 3: Render Shot 16 Final
s16_out = os.path.join(shots_dir, "shot_16_final.mp4")
sub_16 = "陆远：“底层规则重写完成，正在执行编译。”"
filter_16 = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_16}':"
    f"fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:"
    f"x=(w-text_w)/2:y=h-70:enable='between(t,3.0,7.8)'[vout]"
)
cmd_16 = [
    ffmpeg, "-y",
    "-i", v16_std,
    "-filter_complex", filter_16,
    "-map", "[vout]", "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "copy",
    "-t", "10.03",
    s16_out
]
print("Rendering Shot 16 Final...")
subprocess.run(cmd_16, check=True)
print(f"Shot 16 rendered: {s16_out}")

# Step 4: Copy to artifact directory
shutil.copy2(s15_out, os.path.join(art_dir, "shot_15_final.mp4"))
shutil.copy2(s16_out, os.path.join(art_dir, "shot_16_final.mp4"))
print("Copied final shots to artifact directory successfully!")
