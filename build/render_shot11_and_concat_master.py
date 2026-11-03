# -*- coding: utf-8 -*-
"""
Script: render_shot11_and_concat_master.py
Author: 柳锐凯 (Liu Ruikai)
Description:
  1. Standardizes gemini_generated_video_76f81e31.mp4 -> shot_11_viral_short_video_and_awakening.mp4.
  2. Renders dist/shots/shot_11_final.mp4 with subtitles:
     - [0.5s - 4.2s] 家属：“是他救了我父亲！救命恩人不能流血又流泪啊……”
     - [4.8s - 8.5s] 弹幕：“冷血算法毫无人性！必须还救人骑手一个公道！”
     (Keeps original audio intact as user requested).
  3. Concatenates Master Progress Cut: dist/acts/current_progress_act1_to_act3_shot11.mp4 (13 shots, 150.4s / 2m30s).
  4. Copies outputs to artifacts directory.
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

# Step 1: Standardize raw video
raw_input = os.path.join(raw_dir, "gemini_generated_video_76f81e31.mp4")
raw_standard = os.path.join(raw_dir, "shot_11_viral_short_video_and_awakening.mp4")
if os.path.exists(raw_input):
    shutil.copy2(raw_input, raw_standard)
    print(f"Standardized raw video: {raw_standard}")

# Step 2: Render Shot 11 Final
shot11_out = os.path.join(shots_dir, "shot_11_final.mp4")

sub_1 = "家属：“是他救了我父亲！救命恩人不能流血又流泪啊……”"
sub_2 = "弹幕：“冷血算法毫无人性！必须还救人骑手一个公道！”"

filter_11 = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.5,4.2)',"
    f"drawtext=fontfile='{font_file}':text='{sub_2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.8,8.5)'[vout]"
)

cmd_11 = [
    ffmpeg, "-y",
    "-i", raw_standard,
    "-filter_complex", filter_11,
    "-map", "[vout]", "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "copy",
    "-t", "10.03",
    shot11_out
]

print("Rendering Shot 11 with subtitles (preserving original audio)...")
subprocess.run(cmd_11, check=True)
print(f"Shot 11 Final rendered: {shot11_out}")

# Step 3: Extract preview frames with subtitles
for t, name in [(2.0, "shot_11_final_sub1.jpg"), (6.5, "shot_11_final_sub2.jpg"), (9.5, "shot_11_final_hold.jpg")]:
    out_p = os.path.join(art_dir, name)
    subprocess.run([ffmpeg, "-y", "-ss", str(t), "-i", shot11_out, "-vframes", "1", "-q:v", "2", out_p], check=True)
print("Preview frames extracted successfully!")

# Step 4: Concatenate Master Progress Cut (Act 1 + Act 2 + Shot 11 = 13 shots, ~150s / 2m30s)
all_13_shots = [
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
    shot11_out
]

master_inputs = []
master_filter = ""
for i, s in enumerate(all_13_shots):
    master_inputs.extend(["-i", s])
    master_filter += f"[{i}:v][{i}:a]"
master_filter += f"concat=n={len(all_13_shots)}:v=1:a=1[v][a]"

master_out = os.path.join(acts_dir, "current_progress_act1_to_act3_shot11.mp4")
cmd_master = [
    ffmpeg, "-y",
    *master_inputs,
    "-filter_complex", master_filter,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    master_out
]
print("Concatenating Master Progress Cut (13 shots, 2m30s)...")
subprocess.run(cmd_master, check=True)
print(f"Master Progress Cut successfully generated: {master_out}")

# Step 5: Copy outputs to artifacts
shutil.copy2(shot11_out, os.path.join(art_dir, "shot_11_final.mp4"))
shutil.copy2(master_out, os.path.join(art_dir, "current_progress_act1_to_act3_shot11.mp4"))
# Also update current_progress_act1_to_act2_full.mp4 link/file if needed
shutil.copy2(master_out, os.path.join(acts_dir, "current_progress_full_master.mp4"))
shutil.copy2(master_out, os.path.join(art_dir, "current_progress_full_master.mp4"))
print("Copied all outputs to artifacts successfully!")
