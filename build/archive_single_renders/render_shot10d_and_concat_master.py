# -*- coding: utf-8 -*-
"""
Script: render_shot10d_and_concat_master.py
Author: 柳锐凯 (Liu Ruikai)
Description:
  1. Standardizes gemini_generated_video_9610064d.mp4 -> shot_10d_hallway_to_trending_alert.mp4.
  2. Renders dist/shots/shot_10d_final.mp4 with subtitles:
     - [4.2s - 7.2s] “【全网热搜】救人外卖员因延误被平台封号……”
     - [7.6s - 9.8s] “……老人家属全网寻人？！”
  3. Concatenates Act 2 complete cut: dist/acts/act2_complete_full_cut.mp4 (Shot 06 -> 10D, 8 shots, ~100s).
  4. Concatenates Master Progress Cut: dist/acts/current_progress_act1_to_act2_full.mp4 (12 shots, 2m20s / 140s).
  5. Copies outputs to artifacts directory.
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
raw_input = os.path.join(raw_dir, "gemini_generated_video_9610064d.mp4")
raw_standard = os.path.join(raw_dir, "shot_10d_hallway_to_trending_alert.mp4")
if os.path.exists(raw_input):
    shutil.copy2(raw_input, raw_standard)
    print(f"Standardized raw video: {raw_standard}")

# Step 2: Render Shot 10D Final
shot10d_out = os.path.join(shots_dir, "shot_10d_final.mp4")

sub_1 = "【全网热搜】救人外卖员因延误被平台封号……"
sub_2 = "……老人家属全网寻人？！"

filter_10d = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.2,7.2)',"
    f"drawtext=fontfile='{font_file}':text='{sub_2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,7.6,9.8)'[vout]"
)

cmd_10d = [
    ffmpeg, "-y",
    "-i", raw_standard,
    "-filter_complex", filter_10d,
    "-map", "[vout]", "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-t", "10.03",
    shot10d_out
]

print("Rendering Shot 10D with subtitles...")
subprocess.run(cmd_10d, check=True)
print(f"Shot 10D Final rendered: {shot10d_out}")

# Step 3: Render Act 2 Complete Full Cut (Shot 06 -> 07 -> 08_full -> 09_full -> 10A -> 10B -> 10C -> 10D)
act2_shots = [
    os.path.join(shots_dir, "shot_06_final.mp4"),
    os.path.join(shots_dir, "shot_07_final.mp4"),
    os.path.join(shots_dir, "shot_08_full_20s.mp4"),
    os.path.join(shots_dir, "shot_09_full_20s.mp4"),
    os.path.join(shots_dir, "shot_10a_final.mp4"),
    os.path.join(shots_dir, "shot_10b_final.mp4"),
    os.path.join(shots_dir, "shot_10c_final.mp4"),
    shot10d_out
]

act2_inputs = []
act2_filter = ""
for i, s in enumerate(act2_shots):
    act2_inputs.extend(["-i", s])
    act2_filter += f"[{i}:v][{i}:a]"
act2_filter += f"concat=n={len(act2_shots)}:v=1:a=1[v][a]"

act2_full = os.path.join(acts_dir, "act2_complete_full_cut.mp4")
cmd_act2 = [
    ffmpeg, "-y",
    *act2_inputs,
    "-filter_complex", act2_filter,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    act2_full
]
print("Concatenating complete Act 2 full cut (now including Shot 10D, 8 shots)...")
subprocess.run(cmd_act2, check=True)
print(f"Act 2 Complete Cut rendered: {act2_full}")

# Step 4: Concatenate Master Progress Cut (Act 1 + Transition + Act 2 Complete with 10D)
all_12_shots = [
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
    shot10d_out
]

master_inputs = []
master_filter = ""
for i, s in enumerate(all_12_shots):
    master_inputs.extend(["-i", s])
    master_filter += f"[{i}:v][{i}:a]"
master_filter += f"concat=n={len(all_12_shots)}:v=1:a=1[v][a]"

master_out = os.path.join(acts_dir, "current_progress_act1_to_act2_full.mp4")
cmd_master = [
    ffmpeg, "-y",
    *master_inputs,
    "-filter_complex", master_filter,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    master_out
]
print("Concatenating Master Progress Cut (12 shots, 2m20s)...")
subprocess.run(cmd_master, check=True)
print(f"Master Progress Cut successfully generated: {master_out}")

# Step 5: Extract preview frames with subtitles
for t, name in [(5.5, "shot_10d_final_sub1.jpg"), (8.5, "shot_10d_final_sub2.jpg")]:
    out_p = os.path.join(art_dir, name)
    subprocess.run([ffmpeg, "-y", "-ss", str(t), "-i", shot10d_out, "-vframes", "1", "-q:v", "2", out_p], check=True)

# Step 6: Copy outputs to artifacts
shutil.copy2(shot10d_out, os.path.join(art_dir, "shot_10d_final.mp4"))
shutil.copy2(act2_full, os.path.join(art_dir, "act2_complete_full_cut.mp4"))
shutil.copy2(master_out, os.path.join(art_dir, "current_progress_act1_to_act2_full.mp4"))
print("Copied all outputs to artifacts successfully!")
