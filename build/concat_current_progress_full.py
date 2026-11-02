# -*- coding: utf-8 -*-
"""
Script: concat_current_progress_full.py
Author: 柳锐凯 (Liu Ruikai)
Description:
  1. Concatenates completed Act 2 shots (Shot 06 -> 07 -> 08_full -> 09_full -> 10A -> 10B) into dist/acts/act2_progress_cut.mp4
  2. Concatenates complete Act 1 (dist/acts/act1_complete_full_cut.mp4) + Act 2 into dist/acts/current_progress_act1_to_act2_full.mp4
  3. Copies results to conversation artifacts directory for interactive playback.
"""

import os
import subprocess
import shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base_dir = "d:/study/course/maogai/homework"
dist_dir = os.path.join(base_dir, "dist")
shots_dir = os.path.join(dist_dir, "shots")
acts_dir = os.path.join(dist_dir, "acts")
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"

os.makedirs(acts_dir, exist_ok=True)

# Act 1 Master
act1_master = os.path.join(acts_dir, "act1_complete_full_cut.mp4")

# Act 2 Shots
shot06 = os.path.join(shots_dir, "shot_06_final.mp4")
shot07 = os.path.join(shots_dir, "shot_07_final.mp4")
shot08 = os.path.join(shots_dir, "shot_08_full_20s.mp4")
shot09 = os.path.join(shots_dir, "shot_09_full_20s.mp4")
shot10a = os.path.join(shots_dir, "shot_10a_final.mp4")
shot10b = os.path.join(shots_dir, "shot_10b_final.mp4")

# Act 2 Output
act2_master = os.path.join(acts_dir, "act2_progress_cut.mp4")

# 1. Generate Act 2 Progress Cut
print(">>> Step 1: Rendering Act 2 Progress Cut (Shot 06 -> 07 -> 08 -> 09 -> 10A -> 10B)...")
cmd_act2 = [
    ffmpeg, "-y",
    "-i", shot06,
    "-i", shot07,
    "-i", shot08,
    "-i", shot09,
    "-i", shot10a,
    "-i", shot10b,
    "-filter_complex", "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a][5:v][5:a]concat=n=6:v=1:a=1[v][a]",
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    act2_master
]
subprocess.run(cmd_act2, check=True)
print(f"Act 2 Progress Cut generated: {act2_master}")

# 2. Generate Master Progress Cut (Act 1 + Act 2)
master_full = os.path.join(acts_dir, "current_progress_act1_to_act2_full.mp4")
print(">>> Step 2: Rendering Master Full Cut (Act 1 + Act 2)...")
cmd_master = [
    ffmpeg, "-y",
    "-i", act1_master,
    "-i", act2_master,
    "-filter_complex", "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]",
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    master_full
]
subprocess.run(cmd_master, check=True)
print(f"Master Full Progress Cut generated: {master_full}")

# 3. Copy to artifact directory
shutil.copy2(act2_master, os.path.join(art_dir, "act2_progress_cut.mp4"))
shutil.copy2(master_full, os.path.join(art_dir, "current_progress_act1_to_act2_full.mp4"))
print("Copied both outputs to artifact directory successfully!")
