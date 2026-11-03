# -*- coding: utf-8 -*-
"""
Script: reorganize_workspace_clean.py
Author: 柳锐凯 (Liu Ruikai)
Description:
  Systematically organizes workspace folders to achieve crystal-clear hierarchy:
  1. dist/acts/:
     - Keeps only the 4 canonical deliverable cuts:
       * liuruikai_part1_complete_master.mp4 (3m00s, 16 shots)
       * act1_complete_full_cut.mp4 (47s)
       * act2_complete_full_cut.mp4 (100s)
       * act3_complete_full_cut.mp4 (40s)
     - Moves intermediate progress exports to dist/acts/archive_progress/
  2. dist/shots/:
     - Keeps only the 16 active canonical shots (Shot 01 ~ Shot 14).
     - Moves scrapped/superseded sub-shots (Shot 03, Shot 05, Shot 02 merged, 08a/08b, 09a/09b) to dist/shots/archive_scrapped/.
  3. assets/audio/:
     - assets/audio/foley/ (environmental sounds: rain, storm, office, station)
     - assets/audio/voiceovers/ (character voice tracks)
     - assets/audio/archive_raw/ (raw tests, intermediate wavs)
  4. assets/images/:
     - assets/images/archive_scrapped/ (outdated prototypes: shot_00, shot_03, shot_05, etc.)
  5. build/:
     - build/archive_single_renders/ (the 30+ single-step render scripts)
     - Keeps active master pipelines at build/ root.
"""

import os
import shutil

base_dir = "d:/study/course/maogai/homework"

def safe_move(src, dst):
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
        print(f"Moved: {os.path.relpath(src, base_dir)} -> {os.path.relpath(dst, base_dir)}")

# ==========================================
# 1. Clean dist/acts/
# ==========================================
acts_archive = os.path.join(base_dir, "dist", "acts", "archive_progress")
os.makedirs(acts_archive, exist_ok=True)

intermediate_acts = [
    "current_progress_act1_to_act2_full.mp4",
    "current_progress_act1_to_act3_shot11.mp4",
    "current_progress_act1_to_act3_shot12.mp4",
    "current_progress_streamlined_no_shot03_05.mp4",
    "act1_seamless_31s_final.mp4",
    "act2_progress_cut.mp4"
]

for f in intermediate_acts:
    src = os.path.join(base_dir, "dist", "acts", f)
    dst = os.path.join(acts_archive, f)
    safe_move(src, dst)

# ==========================================
# 2. Clean dist/shots/
# ==========================================
shots_archive = os.path.join(base_dir, "dist", "shots", "archive_scrapped")
os.makedirs(shots_archive, exist_ok=True)

scrapped_shots = [
    "shot_02_final.mp4",       # superseded by 02a, 02b, 02c
    "shot_03_final.mp4",       # scrapped timeout countdown (contradicts rescue plot)
    "shot_05_final.mp4",       # scrapped generic web modal (contradicts LLM system)
    "shot_08a_final.mp4",      # merged into shot_08_full_20s.mp4
    "shot_08b_final.mp4",      # merged into shot_08_full_20s.mp4
    "shot_09a_final.mp4",      # merged into shot_09_full_20s.mp4
    "shot_09b_final.mp4",      # merged into shot_09_full_20s.mp4
]

for f in scrapped_shots:
    src = os.path.join(base_dir, "dist", "shots", f)
    dst = os.path.join(shots_archive, f)
    safe_move(src, dst)

# ==========================================
# 3. Clean assets/audio/
# ==========================================
foley_dir = os.path.join(base_dir, "assets", "audio", "foley")
vo_dir = os.path.join(base_dir, "assets", "audio", "voiceovers")
audio_raw_dir = os.path.join(base_dir, "assets", "audio", "archive_raw")

os.makedirs(foley_dir, exist_ok=True)
os.makedirs(vo_dir, exist_ok=True)
os.makedirs(audio_raw_dir, exist_ok=True)

audio_dir = os.path.join(base_dir, "assets", "audio")
for f in os.listdir(audio_dir):
    p = os.path.join(audio_dir, f)
    if os.path.isdir(p):
        continue
    if f.startswith("foley_"):
        safe_move(p, os.path.join(foley_dir, f))
    elif "gemini_raw" in f or "test_" in f:
        safe_move(p, os.path.join(audio_raw_dir, f))
    elif f.endswith(".mp3") or f.endswith(".wav"):
        safe_move(p, os.path.join(vo_dir, f))

# ==========================================
# 4. Clean assets/images/
# ==========================================
img_archive = os.path.join(base_dir, "assets", "images", "archive_scrapped")
os.makedirs(img_archive, exist_ok=True)

outdated_images = [
    "shot_00.jpg",
    "shot_03.jpg",
    "shot_05.jpg",
]

for f in outdated_images:
    src = os.path.join(base_dir, "assets", "images", f)
    dst = os.path.join(img_archive, f)
    safe_move(src, dst)

# ==========================================
# 5. Clean build/
# ==========================================
build_archive = os.path.join(base_dir, "build", "archive_single_renders")
os.makedirs(build_archive, exist_ok=True)

build_dir = os.path.join(base_dir, "build")
keep_build_scripts = [
    "generate_voice_samples.py",
    "inspect_tree.py",
    "organize_workspace.py",
    "reorganize_workspace_clean.py",
    "render_shot13_shot14_and_master.py"
]

for f in os.listdir(build_dir):
    p = os.path.join(build_dir, f)
    if os.path.isdir(p):
        continue
    if f.endswith(".py") and f not in keep_build_scripts:
        safe_move(p, os.path.join(build_archive, f))

print("\nWorkspace organization complete!")
