import os
import subprocess
import asyncio
import edge_tts
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base_dir = "d:/study/course/maogai/homework"
out_dir = os.path.join(base_dir, "dist")
os.makedirs(out_dir, exist_ok=True)

# 1. Generate Lao Liu's Voiceover
vo_text = "雨再大我也得冲！还差两千块，丫头还在医院等我呢……绝不能超时，只要这单送到，药费就有着落了！"
vo_audio_path = os.path.join(base_dir, "assets", "audio", "shot_02_laoliu_vo.mp3")

async def generate_vo():
    print(f"Generating Lao Liu voiceover: {vo_text}")
    communicate = edge_tts.Communicate(vo_text, "zh-CN-YunjianNeural", rate="+10%", pitch="-2Hz")
    await communicate.save(vo_audio_path)

asyncio.run(generate_vo())
print(f"Voiceover saved to {vo_audio_path}")

# 2. Render Shot 02 with VO, mixed rain audio, and subtitles
raw_shot02 = os.path.join(base_dir, "assets", "videos", "shot_02_lao_liu_scooter_rain.mp4")
shot02_with_vo = os.path.join(out_dir, "shot_02_with_vo.mp4")

font_file = "C\\:/Windows/Fonts/msyhbd.ttc"
sub1 = "雨再大我也得冲！还差两千块，丫头还在医院等我呢……"
sub2 = "绝不能超时，只要这单送到，药费就有着落了！"

# Filter complex for audio mixing (native rain @ 0.45, VO @ 1.55 delayed 500ms)
# and video subtitles (drawtext)
filter_complex = (
    f"[0:a]volume=0.45[rain];"
    f"[1:a]adelay=500|500,volume=1.55[vo];"
    f"[rain][vo]amix=inputs=2:duration=first:dropout_transition=2[aout];"
    f"[0:v]"
    f"drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.5,4.6)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.7,9.7)'[vout]"
)

cmd_shot02 = [
    ffmpeg, "-y",
    "-i", raw_shot02,
    "-i", vo_audio_path,
    "-filter_complex", filter_complex,
    "-map", "[vout]",
    "-map", "[aout]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    shot02_with_vo
]

print("Rendering Shot 02 with audio mix and subtitles...")
subprocess.run(cmd_shot02, check=True)
print(f"Shot 02 with VO successfully generated: {shot02_with_vo}")

# 3. Concatenate Shot 01 + Shot 02 directly (Seamless 20s opening)
shot01 = os.path.join(base_dir, "assets", "videos", "shot_01_macro_city_to_lu_yuan_monologue.mp4")
seamless_opening = os.path.join(out_dir, "act1_opening_seamless_20s.mp4")

cmd_concat = [
    ffmpeg, "-y",
    "-i", shot01,
    "-i", shot02_with_vo,
    "-filter_complex", "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]",
    "-map", "[v]",
    "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    seamless_opening
]

print("Concatenating Shot 01 and Shot 02 directly into seamless 20s opening...")
subprocess.run(cmd_concat, check=True)
print(f"Act 1 seamless 20s opening created: {seamless_opening}")
