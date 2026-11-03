# -*- coding: utf-8 -*-
"""
Script: render_shot13_shot14_and_master.py
Author: 柳锐凯 (Liu Ruikai)
Description:
  1. Standardizes:
     - gemini_generated_video_f6c614af.mp4 -> shot_13_regulatory_announcement.mp4
     - gemini_generated_video_72a764e1.mp4 -> shot_14_wang_panic_engineering_hall.mp4
  2. Renders dist/shots/shot_13_final.mp4 with subtitles:
     - [0.6s - 4.5s] “【权威发布】多部委联合督导：限期推行‘算法取中’！”
     - [4.8s - 9.2s] 发言人：“科技必须坚守以人为本，算法绝不能凌驾于生命公义之上！”
  3. Renders dist/shots/shot_14_final.mp4 with subtitles:
     - [0.8s - 4.2s] “（大门猛推开）陆远！联合调查组进驻了！”
     - [4.8s - 9.2s] 王总：“限你们二十四小时内，把突发救助和免责规则给我改出来！”
  4. Renders Act 3 Complete Cut: dist/acts/act3_complete_full_cut.mp4 (Shot 11, 12, 13, 14, ~40s).
  5. Renders Part 1 Grand Master Cut (16 shots, 180.5s / 3m00s):
     dist/acts/liuruikai_part1_complete_master.mp4 & current_progress_full_master.mp4.
  6. Copies outputs to artifacts directory.
"""

import os
import subprocess
import shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base_dir = "d:/study/course/maogai/homework"
raw_dir = os.path.join(base_dir, "assets", "videos", "raw_inputs")
dist_dir = os.path.join(base_dir, "dist")
shots_dir = os.path.join(dist_dir, "shots")
acts_dir = os.path.join(dist_dir, "acts")
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"

font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# Step 1: Standardize raw videos
v13_raw = os.path.join(raw_dir, "gemini_generated_video_f6c614af.mp4")
v13_std = os.path.join(raw_dir, "shot_13_regulatory_announcement.mp4")
if os.path.exists(v13_raw):
    shutil.copy2(v13_raw, v13_std)
    print(f"Standardized Shot 13: {v13_std}")

v14_raw = os.path.join(raw_dir, "gemini_generated_video_72a764e1.mp4")
v14_std = os.path.join(raw_dir, "shot_14_wang_panic_engineering_hall.mp4")
if os.path.exists(v14_raw):
    shutil.copy2(v14_raw, v14_std)
    print(f"Standardized Shot 14: {v14_std}")

# Step 2: Render Shot 13 Final
shot13_out = os.path.join(shots_dir, "shot_13_final.mp4")
sub_13_1 = "“【权威发布】多部委联合督导：限期推行‘算法取中’！”"
sub_13_2 = "发言人：“科技必须坚守以人为本，算法绝不能凌驾于生命公义之上！”"

filter_13 = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_13_1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.6,4.5)',"
    f"drawtext=fontfile='{font_file}':text='{sub_13_2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.8,9.2)'[vout]"
)

cmd_13 = [
    ffmpeg, "-y",
    "-i", v13_std,
    "-filter_complex", filter_13,
    "-map", "[vout]", "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "copy",
    "-t", "10.03",
    shot13_out
]
print("Rendering Shot 13 with subtitles...")
subprocess.run(cmd_13, check=True)
print(f"Shot 13 Final rendered: {shot13_out}")

# Step 3: Render Shot 14 Final
shot14_out = os.path.join(shots_dir, "shot_14_final.mp4")
sub_14_1 = "“（大门猛推开）陆远！联合调查组进驻了！”"
sub_14_2 = "王总：“限你们二十四小时内，把突发救助和免责规则给我改出来！”"

filter_14 = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_14_1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.8,4.2)',"
    f"drawtext=fontfile='{font_file}':text='{sub_14_2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.8,9.2)'[vout]"
)

cmd_14 = [
    ffmpeg, "-y",
    "-i", v14_std,
    "-filter_complex", filter_14,
    "-map", "[vout]", "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "copy",
    "-t", "10.03",
    shot14_out
]
print("Rendering Shot 14 with subtitles...")
subprocess.run(cmd_14, check=True)
print(f"Shot 14 Final rendered: {shot14_out}")

# Step 4: Extract preview frames with subtitles
for t, name in [(2.5, "shot_13_final_sub1.jpg"), (7.0, "shot_13_final_sub2.jpg")]:
    subprocess.run([ffmpeg, "-y", "-ss", str(t), "-i", shot13_out, "-vframes", "1", "-q:v", "2", os.path.join(art_dir, name)], check=True)

for t, name in [(2.5, "shot_14_final_sub1.jpg"), (7.0, "shot_14_final_sub2.jpg")]:
    subprocess.run([ffmpeg, "-y", "-ss", str(t), "-i", shot14_out, "-vframes", "1", "-q:v", "2", os.path.join(art_dir, name)], check=True)
print("Preview frames extracted successfully!")

# Step 5: Render Act 3 Complete Cut (Shot 11, 12, 13, 14, 40s)
act3_shots = [
    os.path.join(shots_dir, "shot_11_final.mp4"),
    os.path.join(shots_dir, "shot_12_final.mp4"),
    shot13_out,
    shot14_out
]
act3_inputs = []
act3_filter = ""
for i, s in enumerate(act3_shots):
    act3_inputs.extend(["-i", s])
    act3_filter += f"[{i}:v][{i}:a]"
act3_filter += f"concat=n={len(act3_shots)}:v=1:a=1[v][a]"

act3_full = os.path.join(acts_dir, "act3_complete_full_cut.mp4")
cmd_act3 = [
    ffmpeg, "-y",
    *act3_inputs,
    "-filter_complex", act3_filter,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    act3_full
]
print("Concatenating complete Act 3 full cut (40s)...")
subprocess.run(cmd_act3, check=True)
print(f"Act 3 Complete Cut rendered: {act3_full}")

# Step 6: Render Part 1 Grand Master Cut (16 shots, 180.5s / 3m00s)
all_16_shots = [
    os.path.join(shots_dir, "shot_01_final.mp4"),
    os.path.join(shots_dir, "shot_02a_final.mp4"),
    os.path.join(shots_dir, "shot_02b_final.mp4"),
    os.path.join(shots_dir, "shot_02c_final.mp4"),
    os.path.join(shots_dir, "shot_06_final.mp4"),
    os.path.join(shots_dir, "shot_07_final.mp4"),
    os.path.join(shots_dir, "shot_08_full_20s.mp4"),
    os.path.join(shots_dir, "shot_09_full_20s.mp4"),
    os.path.join(shots_dir, "shot_10a_final.mp4"),
    os.path.join(shots_dir, "shot_10b_final.mp4"),
    os.path.join(shots_dir, "shot_10c_final.mp4"),
    os.path.join(shots_dir, "shot_10d_final.mp4"),
    os.path.join(shots_dir, "shot_11_final.mp4"),
    os.path.join(shots_dir, "shot_12_final.mp4"),
    shot13_out,
    shot14_out
]

master_inputs = []
master_filter = ""
for i, s in enumerate(all_16_shots):
    master_inputs.extend(["-i", s])
    master_filter += f"[{i}:v][{i}:a]"
master_filter += f"concat=n={len(all_16_shots)}:v=1:a=1[v][a]"

master_out = os.path.join(acts_dir, "liuruikai_part1_complete_master.mp4")
cmd_master = [
    ffmpeg, "-y",
    *master_inputs,
    "-filter_complex", master_filter,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    master_out
]
print("Concatenating Part 1 Grand Master Cut (16 shots, 3m00s)...")
subprocess.run(cmd_master, check=True)
print(f"Part 1 Grand Master Cut successfully generated: {master_out}")

# Step 7: Copy outputs to artifacts and sync general progress
shutil.copy2(shot13_out, os.path.join(art_dir, "shot_13_final.mp4"))
shutil.copy2(shot14_out, os.path.join(art_dir, "shot_14_final.mp4"))
shutil.copy2(act3_full, os.path.join(art_dir, "act3_complete_full_cut.mp4"))
shutil.copy2(master_out, os.path.join(art_dir, "liuruikai_part1_complete_master.mp4"))
shutil.copy2(master_out, os.path.join(acts_dir, "current_progress_full_master.mp4"))
shutil.copy2(master_out, os.path.join(art_dir, "current_progress_full_master.mp4"))
print("Copied all outputs to artifacts successfully!")
