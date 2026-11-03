# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

raw_src = "assets/videos/raw_inputs/gemini_generated_video_5baea7f3.mp4"
raw_canonical = "assets/videos/raw_inputs/shot_06_laoliu_morning_station.mp4"
output_shot06 = "dist/shots/shot_06_final.mp4"
font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# 1. Copy to canonical name
shutil.copy2(raw_src, raw_canonical)
print(f"Copied {raw_src} -> {raw_canonical}")

# 2. Build subtitle filter
# Clause 1: [2.6s - 4.8s] 雨终于停了，等会儿大门打开，
# Clause 2: [4.9s - 6.9s] 再去跟工作人员好好沟通……
sub1 = "雨终于停了，等会儿大门打开，"
sub2 = "再去跟工作人员好好沟通……"

vf = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,2.6,4.8)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.9,6.9)'[vout]"
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
    output_shot06
]

print("Executing render command...")
subprocess.run(cmd, check=True)
print(f"Successfully rendered: {output_shot06}")

# 3. Copy to artifact directory for UI playback
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"
art_dest = os.path.join(art_dir, "shot_06_final.mp4")
shutil.copy2(output_shot06, art_dest)
print(f"Copied to artifact dir: {art_dest}")

# Also extract 3 frame cards from shot 06:
# Frame 1: at 1.0s (resting on steps)
# Frame 2: at 4.0s (speaking dialogue with subtitle)
# Frame 3: at 8.5s (looking down toward hands for transition)
f1 = os.path.join(art_dir, "shot_06_f1_rest.jpg")
f2 = os.path.join(art_dir, "shot_06_f2_speech.jpg")
f3 = os.path.join(art_dir, "shot_06_f3_transition.jpg")

subprocess.run([ffmpeg, "-y", "-ss", "1.0", "-i", output_shot06, "-frames:v", "1", f1], check=True)
subprocess.run([ffmpeg, "-y", "-ss", "4.0", "-i", output_shot06, "-frames:v", "1", f2], check=True)
subprocess.run([ffmpeg, "-y", "-ss", "8.5", "-i", output_shot06, "-frames:v", "1", f3], check=True)
print("Extracted 3 preview frames successfully!")
