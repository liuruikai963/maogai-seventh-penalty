# -*- coding: utf-8 -*-
"""
Script: organize_workspace.py
Author: 柳锐凯 (Liu Ruikai)
Description:
  1. Removes scratch temporary wav files in root.
  2. Moves legacy intermediate videos in dist/ to dist/archive/.
  3. Moves legacy video root files in assets/videos/ to assets/videos/archive_scrapped/.
"""

import os
import shutil

base_dir = "d:/study/course/maogai/homework"

# 1. Clean root scratch files
root_scratch_files = ["temp_10a.wav", "temp_10b.wav", "temp_audio.wav"]
for f in root_scratch_files:
    p = os.path.join(base_dir, f)
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed root scratch file: {f}")

# 2. Organize dist/
dist_archive = os.path.join(base_dir, "dist", "archive")
os.makedirs(dist_archive, exist_ok=True)

dist_legacy_files = [
    "act1_opening_seamless_20s.mp4",
    "act1_seamless_30s.mp4",
    "act1_seamless_31s_character_intro.mp4",
    "shot_01_v2.mp4",
    "shot_02_v2.mp4",
    "shot_02_with_vo.mp4",
    "shot_03_with_vo.mp4"
]

for f in dist_legacy_files:
    p = os.path.join(base_dir, "dist", f)
    if os.path.exists(p):
        shutil.move(p, os.path.join(dist_archive, f))
        print(f"Moved dist/{f} -> dist/archive/{f}")

# 3. Organize assets/videos/
video_archive = os.path.join(base_dir, "assets", "videos", "archive_scrapped")
os.makedirs(video_archive, exist_ok=True)

video_legacy_files = [
    "shot_01_macro_city_to_lu_yuan_monologue.mp4",
    "shot_02_lao_liu_scooter_rain.mp4",
    "shot_03_phone_countdown.mp4"
]

for f in video_legacy_files:
    p = os.path.join(base_dir, "assets", "videos", f)
    if os.path.exists(p):
        shutil.move(p, os.path.join(video_archive, f))
        print(f"Moved assets/videos/{f} -> assets/videos/archive_scrapped/{f}")

print("Workspace reorganization completed successfully!")
