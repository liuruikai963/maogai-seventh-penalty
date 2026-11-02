# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

raw_src = "assets/videos/raw_inputs/gemini_generated_video_1a122154.mp4"
raw_canonical = "assets/videos/raw_inputs/shot_08b_rescue_calling_120.mp4"
output_shot08b = "dist/shots/shot_08b_final.mp4"
font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# 1. Copy to canonical if needed
if not os.path.exists(raw_canonical):
    shutil.copy2(raw_src, raw_canonical)
    print(f"Copied {raw_src} -> {raw_canonical}")

# 2. Build subtitle filter
# Lao Liu's urgent 120 rescue phone call:
# Subtitle 1: [3.0s - 4.1s] 喂！120急救中心吗？！
# Subtitle 2: [4.3s - 6.1s] 这里有位大爷摔倒了，地址是幸福家园……
# Subtitle 3: [6.3s - 8.2s] 请快派救护车过来！
sub1 = "喂！120急救中心吗？！"
sub2 = "这里有位大爷摔倒了，地址是幸福家园……"
sub3 = "请快派救护车过来！"

vf = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,3.0,4.1)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.3,6.1)',"
    f"drawtext=fontfile='{font_file}':text='{sub3}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,6.3,8.2)'[vout]"
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
    output_shot08b
]

print("Executing render command for shot_08b_final.mp4...")
subprocess.run(cmd, check=True)
print(f"Successfully rendered: {output_shot08b}")

# 3. Copy to artifact directory for preview
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"
art_dest = os.path.join(art_dir, "shot_08b_final.mp4")
shutil.copy2(output_shot08b, art_dest)
print(f"Copied to artifact dir: {art_dest}")

# 4. Extract preview check frames
f1 = os.path.join(art_dir, "shot_08b_final_sub1.jpg")
f2 = os.path.join(art_dir, "shot_08b_final_sub2.jpg")
f3 = os.path.join(art_dir, "shot_08b_final_sub3.jpg")
f4 = os.path.join(art_dir, "shot_08b_final_relief.jpg")

subprocess.run([ffmpeg, "-y", "-ss", "3.5", "-i", output_shot08b, "-frames:v", "1", f1], check=True)
subprocess.run([ffmpeg, "-y", "-ss", "5.2", "-i", output_shot08b, "-frames:v", "1", f2], check=True)
subprocess.run([ffmpeg, "-y", "-ss", "7.2", "-i", output_shot08b, "-frames:v", "1", f3], check=True)
subprocess.run([ffmpeg, "-y", "-ss", "9.2", "-i", output_shot08b, "-frames:v", "1", f4], check=True)
print("Preview check frames generated successfully.")
