# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

raw_src = "assets/videos/raw_inputs/gemini_generated_video_8654c18f.mp4"
raw_canonical = "assets/videos/raw_inputs/shot_08a_laoliu_steps_to_hallway.mp4"
output_shot08a = "dist/shots/shot_08a_final.mp4"
font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# 1. Ensure canonical raw exists
if not os.path.exists(raw_canonical):
    shutil.copy2(raw_src, raw_canonical)
    print(f"Copied {raw_src} -> {raw_canonical}")

# 2. Build subtitle filter
# Lao Liu's speech on the morning station steps:
# Subtitle 1: [0.8s - 2.5s] 小兄弟，我真不是故意超时的……
# Subtitle 2: [2.7s - 5.2s] 昨晚送餐，那家老人摔在地上动不了……
sub1 = "小兄弟，我真不是故意超时的……"
sub2 = "昨晚送餐，那家老人摔在地上动不了……"

vf = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.8,2.5)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,2.7,5.2)'[vout]"
)

os.makedirs("dist/shots", exist_ok=True)

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
    output_shot08a
]

print("Executing render command for shot_08a_final.mp4...")
subprocess.run(cmd, check=True)
print(f"Successfully rendered: {output_shot08a}")

# 3. Copy to artifact directory for preview
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"
art_dest = os.path.join(art_dir, "shot_08a_final.mp4")
shutil.copy2(output_shot08a, art_dest)
print(f"Copied to artifact dir: {art_dest}")

# 4. Extract preview check frames
f1 = os.path.join(art_dir, "shot_08a_final_sub1.jpg")
f2 = os.path.join(art_dir, "shot_08a_final_sub2.jpg")
f3 = os.path.join(art_dir, "shot_08a_final_hallway.jpg")

subprocess.run([ffmpeg, "-y", "-ss", "1.6", "-i", output_shot08a, "-frames:v", "1", f1], check=True)
subprocess.run([ffmpeg, "-y", "-ss", "3.8", "-i", output_shot08a, "-frames:v", "1", f2], check=True)
subprocess.run([ffmpeg, "-y", "-ss", "8.5", "-i", output_shot08a, "-frames:v", "1", f3], check=True)
print("Preview frames generated successfully.")
