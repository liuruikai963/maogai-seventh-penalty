# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

shot09a = "dist/shots/shot_09a_final.mp4"
shot09b = "dist/shots/shot_09b_final.mp4"
output_concat = "dist/shots/shot_09_full_20s.mp4"

# Concat filter
filter_script = (
    "[0:v:0][0:a:0][1:v:0][1:a:0]concat=n=2:v=1:a=1[v][a]"
)

cmd = [
    ffmpeg, "-y",
    "-i", shot09a,
    "-i", shot09b,
    "-filter_complex", filter_script,
    "-map", "[v]",
    "-map", "[a]",
    "-c:v", "libx264",
    "-preset", "slow",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    output_concat
]

print("Concatenating Shot 09A + Shot 09B into 20s full sequence...")
subprocess.run(cmd, check=True)
print(f"Successfully generated: {output_concat}")

# Copy to artifact
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"
shutil.copy2(output_concat, os.path.join(art_dir, "shot_09_full_20s.mp4"))
print("Copied to artifact directory.")
