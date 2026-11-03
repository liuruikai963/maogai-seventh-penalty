# -*- coding: utf-8 -*-
"""
Script: render_shot02c_and_concat_master.py
Author: 柳锐凯 (Liu Ruikai)
Description:
  1. Standardizes raw video gemini_generated_video_5ae16005.mp4 into shot_02c_macro_city_storm_to_dawn.mp4.
  2. Renders dist/shots/shot_02c_final.mp4 with cinema subtitles:
     - [0.6s - 3.8s] “那一晚的雨太大了……我拼了命往前赶……”
     - [4.3s - 7.5s] “可那一单，终究还是超时了……”
  3. Inserts shot_02c_final.mp4 between Shot 02B and Shot 06,
     producing the master full cut: dist/acts/current_progress_act1_to_act2_full.mp4 (120s / 2m00s).
  4. Copies key outputs to artifacts directory.
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

# Step 1: Copy/Standardize raw input
raw_input = os.path.join(raw_dir, "gemini_generated_video_5ae16005.mp4")
raw_standard = os.path.join(raw_dir, "shot_02c_macro_city_storm_to_dawn.mp4")
if os.path.exists(raw_input):
    shutil.copy2(raw_input, raw_standard)
    print(f"Standardized raw video: {raw_standard}")

# Step 2: Render Shot 02C Final with Subtitles
shot02c_out = os.path.join(shots_dir, "shot_02c_final.mp4")

sub_1 = "“那一晚的雨太大了……我拼了命往前赶……”"
sub_2 = "“可那一单，终究还是超时了……”"

filter_02c = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.6,3.8)',"
    f"drawtext=fontfile='{font_file}':text='{sub_2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.3,7.5)'[vout]"
)

cmd_02c = [
    ffmpeg, "-y",
    "-i", raw_standard,
    "-filter_complex", filter_02c,
    "-map", "[vout]", "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-t", "10.03",
    shot02c_out
]

print("Rendering Shot 02C with subtitles...")
subprocess.run(cmd_02c, check=True)
print(f"Shot 02C Final rendered: {shot02c_out}")

# Step 3: Concatenate Complete Master Full Cut (10 Shots in chronological order)
shot_files = [
    os.path.join(shots_dir, "shot_01_final.mp4"),
    os.path.join(shots_dir, "shot_02a_final.mp4"),
    os.path.join(shots_dir, "shot_02b_final.mp4"),
    shot02c_out,  # <--- Newly inserted bridge shot!
    os.path.join(shots_dir, "shot_06_final.mp4"),
    os.path.join(shots_dir, "shot_07_final.mp4"),
    os.path.join(shots_dir, "shot_08_full_20s.mp4"),
    os.path.join(shots_dir, "shot_09_full_20s.mp4"),
    os.path.join(shots_dir, "shot_10a_final.mp4"),
    os.path.join(shots_dir, "shot_10b_final.mp4")
]

inputs = []
filter_inputs = ""
for i, s in enumerate(shot_files):
    inputs.extend(["-i", s])
    filter_inputs += f"[{i}:v][{i}:a]"

filter_concat = f"{filter_inputs}concat=n={len(shot_files)}:v=1:a=1[v][a]"
master_out = os.path.join(acts_dir, "current_progress_act1_to_act2_full.mp4")

cmd_master = [
    ffmpeg, "-y",
    *inputs,
    "-filter_complex", filter_concat,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    master_out
]

print("Concatenating complete 10-shot Master Progress Cut (Act 1 + Transition + Act 2)...")
subprocess.run(cmd_master, check=True)
print(f"Master Progress Cut successfully generated: {master_out}")

# Step 4: Copy to Artifacts
shutil.copy2(shot02c_out, os.path.join(art_dir, "shot_02c_final.mp4"))
shutil.copy2(master_out, os.path.join(art_dir, "current_progress_act1_to_act2_full.mp4"))
print("Copied shot_02c_final.mp4 and master cut to artifacts directory successfully!")
