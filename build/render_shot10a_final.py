# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

raw_src = "assets/videos/raw_inputs/gemini_generated_video_d3bbc190.mp4"
raw_canonical = "assets/videos/raw_inputs/shot_10a_steps_comfort_and_sprint.mp4"
output_shot10a = "dist/shots/shot_10a_final.mp4"
font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# 1. Ensure canonical raw exists
if not os.path.exists(raw_canonical):
    shutil.copy2(raw_src, raw_canonical)
    print(f"Copied {raw_src} -> {raw_canonical}")

# 2. Build subtitle filter
# Sub 1: [0.5s - 2.6s] “刘叔，您这是救人！”
# Sub 2: [3.5s - 5.9s] “等我，我回公司帮您撤销罚单！”
sub1 = "“刘叔，您这是救人！”"
sub2 = "“等我，我回公司帮您撤销罚单！”"

vf = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.5,2.6)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,3.5,5.9)'[vout]"
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
    output_shot10a
]

print("Executing render command for shot_10a_final.mp4...")
subprocess.run(cmd, check=True)
print(f"Successfully rendered: {output_shot10a}")

# 3. Copy to artifact directory for user preview
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"
shutil.copy2(output_shot10a, os.path.join(art_dir, "shot_10a_final.mp4"))

# Extract verification preview frames
for t in [1.5, 4.5, 8.0]:
    out_img = os.path.join(art_dir, f"shot_10a_final_{t}s.jpg")
    subprocess.run([ffmpeg, "-y", "-ss", str(t), "-i", output_shot10a, "-frames:v", "1", out_img], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("All preview frames generated successfully!")
