# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

raw_src = "assets/videos/raw_inputs/gemini_generated_video_e1eb6ca3.mp4"
raw_canonical = "assets/videos/raw_inputs/shot_09a_home_to_hospital_corridor.mp4"
output_shot09a = "dist/shots/shot_09a_final.mp4"
font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# 1. Ensure canonical raw exists
if not os.path.exists(raw_canonical):
    shutil.copy2(raw_src, raw_canonical)
    print(f"Copied {raw_src} -> {raw_canonical}")

# 2. Build subtitle filter
# Phase 1 (Home lift): [0.8s - 2.6s] “慢点抬，小心头部！一二三，起！”
# Phase 2 (Hospital ER rush): [6.8s - 9.5s] “快！推抢救室！准备心电监护！”
sub1 = "“慢点抬，小心头部！一二三，起！”"
sub2 = "“快！推抢救室！准备心电监护！”"

vf = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.8,2.6)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,6.8,9.5)'[vout]"
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
    output_shot09a
]

print("Executing render command for shot_09a_final.mp4...")
subprocess.run(cmd, check=True)
print(f"Successfully rendered: {output_shot09a}")

# 3. Copy to artifact directory for preview
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"
art_dest = os.path.join(art_dir, "shot_09a_final.mp4")
shutil.copy2(output_shot09a, art_dest)
print(f"Copied to artifact dir: {art_dest}")

# 4. Extract preview check frames
f1 = os.path.join(art_dir, "shot_09a_final_sub1.jpg")
f2 = os.path.join(art_dir, "shot_09a_final_ambulance.jpg")
f3 = os.path.join(art_dir, "shot_09a_final_sub2.jpg")
f4 = os.path.join(art_dir, "shot_09a_final_doors.jpg")

subprocess.run([ffmpeg, "-y", "-ss", "1.6", "-i", output_shot09a, "-frames:v", "1", f1], check=True)
subprocess.run([ffmpeg, "-y", "-ss", "3.5", "-i", output_shot09a, "-frames:v", "1", f2], check=True)
subprocess.run([ffmpeg, "-y", "-ss", "7.8", "-i", output_shot09a, "-frames:v", "1", f3], check=True)
subprocess.run([ffmpeg, "-y", "-ss", "9.5", "-i", output_shot09a, "-frames:v", "1", f4], check=True)
print("Preview check frames generated successfully.")
