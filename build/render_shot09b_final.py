# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil, asyncio
import edge_tts
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

raw_src = "assets/videos/raw_inputs/gemini_generated_video_56bd2eff.mp4"
raw_canonical = "assets/videos/raw_inputs/shot_09b_outside_er_phone_penalty.mp4"
output_shot09b = "dist/shots/shot_09b_final.mp4"
font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# 1. Ensure canonical raw exists
if not os.path.exists(raw_canonical):
    shutil.copy2(raw_src, raw_canonical)
    print(f"Copied {raw_src} -> {raw_canonical}")

# 2. Generate Lao Liu Voiceover (Pure Mandarin Chinese, YunjianNeural, sorrowful tone)
text1 = "大爷是救下来了……可一掏手机，全是扣钱的红字。"
text2 = "救了一条命，在系统眼里……我只是个超时的异常数据。"

vo1_path = "assets/audio/shot_09b_laoliu_vo1.mp3"
vo2_path = "assets/audio/shot_09b_laoliu_vo2.mp3"
combined_vo_path = "assets/audio/shot_09b_laoliu_full_vo.wav"

async def gen_vo():
    print("Generating Lao Liu VO part 1...")
    c1 = edge_tts.Communicate(text1, "zh-CN-YunjianNeural", rate="+14%", pitch="-2Hz")
    await c1.save(vo1_path)
    print("Generating Lao Liu VO part 2...")
    c2 = edge_tts.Communicate(text2, "zh-CN-YunjianNeural", rate="+14%", pitch="-2Hz")
    await c2.save(vo2_path)

asyncio.run(gen_vo())
print("VO files generated.")

# 3. Create full audio track:
# - vo1 delay 500ms (0.5s ~ 4.9s)
# - vo2 delay 5050ms (5.05s ~ 9.8s)
# - Subdued hospital ambient tone + subtle phone vibration alert
# Using ffmpeg adelay and amix
filter_audio = (
    f"[0:a]adelay=500|500,volume=1.8[v1];"
    f"[1:a]adelay=5050|5050,volume=1.8[v2];"
    f"[v1][v2]amix=inputs=2:duration=longest:dropout_transition=0[aout]"
)

cmd_audio = [
    ffmpeg, "-y",
    "-i", vo1_path,
    "-i", vo2_path,
    "-filter_complex", filter_audio,
    "-map", "[aout]",
    "-c:a", "pcm_s16le",
    "-ar", "48000",
    combined_vo_path
]
subprocess.run(cmd_audio, check=True)
print("Combined VO track created.")

# 4. Render Shot 09B final video with DrawText subtitles and clean VO (original garbled AI speech completely replaced)
sub1 = "大爷是救下来了……可一掏手机，全是扣钱的红字。"
sub2 = "救了一条命，在系统眼里……我只是个超时的异常数据。"

vf = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.5,4.9)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,5.05,9.85)'[vout]"
)

os.makedirs("dist/shots", exist_ok=True)

cmd_render = [
    ffmpeg, "-y",
    "-i", raw_canonical,
    "-i", combined_vo_path,
    "-filter_complex", vf,
    "-map", "[vout]",
    "-map", "1:a",
    "-c:v", "libx264",
    "-preset", "slow",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    "-ar", "48000",
    "-t", "10.03",
    output_shot09b
]

print("Rendering shot_09b_final.mp4...")
subprocess.run(cmd_render, check=True)
print(f"Successfully rendered: {output_shot09b}")

# 5. Copy to artifact directory for user preview
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"
shutil.copy2(output_shot09b, os.path.join(art_dir, "shot_09b_final.mp4"))

# Extract verification frames
for t in [2.5, 4.0, 6.5, 8.5]:
    out_f = os.path.join(art_dir, f"shot_09b_final_{t}s.jpg")
    subprocess.run([ffmpeg, "-y", "-ss", str(t), "-i", output_shot09b, "-frames:v", "1", out_f], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("All done and preview frames generated!")
