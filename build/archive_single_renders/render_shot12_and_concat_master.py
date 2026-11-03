# -*- coding: utf-8 -*-
"""
Script: render_shot12_and_concat_master.py
Author: 柳锐凯 (Liu Ruikai)
Description:
  1. Standardizes gemini_generated_video_8b17aedf.mp4 -> shot_12_media_storm_and_wang_panic.mp4.
  2. Renders dist/shots/shot_12_final.mp4 with subtitles:
     - [0.6s - 3.8s] “【全网热搜】救人外卖员延误封号事件持续发酵，阅读量破亿！”
     - [4.2s - 7.2s] 央媒：“算法绝不能沦为冰冷枷锁，科技向善必须以人为本！”
     - [7.6s - 9.8s] 王总：“……监管部门紧急约谈？！快、快把法务叫过来！”
     (Keeps original audio intact as user requested).
  3. Concatenates Master Progress Cut: dist/acts/current_progress_act1_to_act3_shot12.mp4 (14 shots, 160.4s / 2m40s).
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
raw_input = os.path.join(raw_dir, "gemini_generated_video_8b17aedf.mp4")
raw_standard = os.path.join(raw_dir, "shot_12_media_storm_and_wang_panic.mp4")
if os.path.exists(raw_input):
    shutil.copy2(raw_input, raw_standard)
    print(f"Standardized raw video: {raw_standard}")

# Step 2: Render Shot 12 Final
shot12_out = os.path.join(shots_dir, "shot_12_final.mp4")

sub_1 = "“【全网热搜】救人外卖员延误封号事件持续发酵，阅读量破亿！”"
sub_2 = "央媒：“算法绝不能沦为冰冷枷锁，科技向善必须以人为本！”"
sub_3 = "王总：“……监管部门紧急约谈？！快、快把法务叫过来！”"

filter_12 = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.6,3.8)',"
    f"drawtext=fontfile='{font_file}':text='{sub_2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.2,7.2)',"
    f"drawtext=fontfile='{font_file}':text='{sub_3}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,7.6,9.8)'[vout]"
)

cmd_12 = [
    ffmpeg, "-y",
    "-i", raw_standard,
    "-filter_complex", filter_12,
    "-map", "[vout]", "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "copy",
    "-t", "10.03",
    shot12_out
]

print("Rendering Shot 12 with subtitles (preserving original audio)...")
subprocess.run(cmd_12, check=True)
print(f"Shot 12 Final rendered: {shot12_out}")

# Step 3: Extract preview frames with subtitles
for t, name in [(2.0, "shot_12_final_sub1.jpg"), (5.5, "shot_12_final_sub2.jpg"), (8.5, "shot_12_final_sub3.jpg")]:
    out_p = os.path.join(art_dir, name)
    subprocess.run([ffmpeg, "-y", "-ss", str(t), "-i", shot12_out, "-vframes", "1", "-q:v", "2", out_p], check=True)
print("Preview frames extracted successfully!")

# Step 4: Concatenate Master Progress Cut (Act 1 + Act 2 + Shot 11 + Shot 12 = 14 shots, ~160s / 2m40s)
all_14_shots = [
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
    shot12_out
]

master_inputs = []
master_filter = ""
for i, s in enumerate(all_14_shots):
    master_inputs.extend(["-i", s])
    master_filter += f"[{i}:v][{i}:a]"
master_filter += f"concat=n={len(all_14_shots)}:v=1:a=1[v][a]"

master_out = os.path.join(acts_dir, "current_progress_act1_to_act3_shot12.mp4")
cmd_master = [
    ffmpeg, "-y",
    *master_inputs,
    "-filter_complex", master_filter,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    master_out
]
print("Concatenating Master Progress Cut (14 shots, 2m40s)...")
subprocess.run(cmd_master, check=True)
print(f"Master Progress Cut successfully generated: {master_out}")

# Step 5: Copy outputs to artifacts
shutil.copy2(shot12_out, os.path.join(art_dir, "shot_12_final.mp4"))
shutil.copy2(master_out, os.path.join(art_dir, "current_progress_act1_to_act3_shot12.mp4"))
shutil.copy2(master_out, os.path.join(acts_dir, "current_progress_full_master.mp4"))
shutil.copy2(master_out, os.path.join(art_dir, "current_progress_full_master.mp4"))
print("Copied all outputs to artifacts successfully!")
