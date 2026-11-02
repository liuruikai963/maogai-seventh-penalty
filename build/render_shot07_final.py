# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

raw_src = "assets/videos/raw_inputs/gemini_generated_video_5cef8a73.mp4"
raw_canonical = "assets/videos/raw_inputs/shot_07_luyuan_approach_hands.mp4"
output_shot07 = "dist/shots/shot_07_final.mp4"
font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# 1. Copy to canonical name if not already copied
if not os.path.exists(raw_canonical):
    shutil.copy2(raw_src, raw_canonical)
    print(f"Copied {raw_src} -> {raw_canonical}")

# 2. Subtitle filter
# Lu Yuan speaks from ~4.3s to ~6.2s: "大叔，您没事吧？"
sub1 = "大叔，您没事吧？"

vf = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.3,6.2)'[vout]"
)

cmd = [
    ffmpeg, "-y",
    "-i", raw_canonical,
    "-filter_complex", vf,
    "-map", "[vout]",
    "-map", "0:a",
    "-c:v", "libx264",
    "-preset", "slow",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    output_shot07
]

print("Executing render command for shot_07_final.mp4...")
subprocess.run(cmd, check=True)
print(f"Successfully rendered: {output_shot07}")

# 3. Copy to artifact directory
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"
art_dest = os.path.join(art_dir, "shot_07_final.mp4")
shutil.copy2(output_shot07, art_dest)
print(f"Copied to artifact dir: {art_dest}")
