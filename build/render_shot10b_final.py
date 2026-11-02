# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

raw_src = "assets/videos/raw_inputs/gemini_generated_video_e9644b3b.mp4"
raw_canonical = "assets/videos/raw_inputs/shot_10b_ai_large_model_error.mp4"
output_shot10b = "dist/shots/shot_10b_final.mp4"
font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# 1. Ensure canonical raw exists
if not os.path.exists(raw_canonical):
    shutil.copy2(raw_src, raw_canonical)
    print(f"Copied {raw_src} -> {raw_canonical}")

# 2. Subtitles:
# Sub 1 (Screen flash): [4.5s - 6.8s] 【大模型报错：语义对齐失败·拒绝人工覆写】
# Sub 2 (Lu Yuan speech): [7.0s - 9.8s] “未定义特征实体……大模型算得出效率，却算不出人性的善意！”
sub1 = "【大模型报错：语义对齐失败·拒绝人工覆写】"
sub2 = "“未定义特征实体……大模型算得出效率，却算不出人性的善意！”"

vf = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub1}':fontsize=26:fontcolor=yellow:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.5,6.8)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=28:fontcolor=white:box=1:boxcolor=black@0.95:boxborderw=24:x=(w-text_w)/2:y=h-86:enable='between(t,7.0,9.8)'[vout]"
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
    output_shot10b
]

print("Executing render command for shot_10b_final.mp4...")
subprocess.run(cmd, check=True)
print(f"Successfully rendered: {output_shot10b}")

# 3. Copy to artifact directory for user preview
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"
shutil.copy2(output_shot10b, os.path.join(art_dir, "shot_10b_final.mp4"))

# Extract verification preview frames
for t in [2.0, 5.5, 8.5]:
    out_img = os.path.join(art_dir, f"shot_10b_final_{t}s.jpg")
    subprocess.run([ffmpeg, "-y", "-ss", str(t), "-i", output_shot10b, "-frames:v", "1", out_img], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("All preview frames generated successfully!")
