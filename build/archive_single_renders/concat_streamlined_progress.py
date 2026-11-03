# -*- coding: utf-8 -*-
"""
Script: concat_streamlined_progress.py
Author: 柳锐凯 (Liu Ruikai)
Description:
  Removes obsolete Shot 03 (scooter 00:00 timeout) and Shot 05 (legacy web admin popup),
  creating a streamlined, contradiction-free cut:
  Shot 01 (10s) -> Shot 02A (10s) -> Shot 02B (10s) -> Shot 06 (10s) -> Shot 07 (10s) ->
  Shot 08 Full (20s) -> Shot 09 Full (20s) -> Shot 10A (10s) -> Shot 10B (10s)
  Total: ~110s (~1m 50s)
"""

import os
import subprocess
import shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base_dir = "d:/study/course/maogai/homework"
shots_dir = os.path.join(base_dir, "dist", "shots")
acts_dir = os.path.join(base_dir, "dist", "acts")
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"

shots = [
    os.path.join(shots_dir, "shot_01_final.mp4"),
    os.path.join(shots_dir, "shot_02a_final.mp4"),
    os.path.join(shots_dir, "shot_02b_final.mp4"),
    os.path.join(shots_dir, "shot_06_final.mp4"),
    os.path.join(shots_dir, "shot_07_final.mp4"),
    os.path.join(shots_dir, "shot_08_full_20s.mp4"),
    os.path.join(shots_dir, "shot_09_full_20s.mp4"),
    os.path.join(shots_dir, "shot_10a_final.mp4"),
    os.path.join(shots_dir, "shot_10b_final.mp4"),
]

output_streamlined = os.path.join(acts_dir, "current_progress_streamlined_no_shot03_05.mp4")

inputs = []
filter_inputs = ""
for i, s in enumerate(shots):
    inputs.extend(["-i", s])
    filter_inputs += f"[{i}:v][{i}:a]"

filter_complex = f"{filter_inputs}concat=n={len(shots)}:v=1:a=1[v][a]"

cmd = [
    ffmpeg, "-y",
    *inputs,
    "-filter_complex", filter_complex,
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    output_streamlined
]

print("Rendering streamlined progress cut without Shot 03 & Shot 05...")
subprocess.run(cmd, check=True)
print(f"Generated: {output_streamlined}")

# Copy to artifacts
shutil.copy2(output_streamlined, os.path.join(art_dir, "current_progress_streamlined_no_shot03_05.mp4"))
print("Copied to artifact directory!")
