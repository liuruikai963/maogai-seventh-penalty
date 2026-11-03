import os
import subprocess
import asyncio
import edge_tts
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base_dir = "d:/study/course/maogai/homework"
audio_dir = os.path.join(base_dir, "assets", "audio")
out_dir = os.path.join(base_dir, "dist")
os.makedirs(audio_dir, exist_ok=True)
os.makedirs(out_dir, exist_ok=True)

# 1. Synthesize New Voices with Academic Topic & Character Intros
text_01 = "我叫陆远，23岁，大模型AI算法架构师。着眼于人工智能的创新发展，我们透视底层逻辑，却陷入了算法决策的伦理困境。"
text_02 = "我叫刘长贵，48岁，是个被AI模型考核的外卖员。雨再大我也得冲！小孙女等钱透析，绝不能被算法判定超时！"

audio_shot01 = os.path.join(audio_dir, "shot_01_lu_yuan_intro.mp3")
audio_shot02 = os.path.join(audio_dir, "shot_02_lao_liu_intro.mp3")

async def synthesize():
    print("Synthesizing Lu Yuan monologue...")
    c1 = edge_tts.Communicate(text_01, "zh-CN-YunxiNeural", rate="+16%", pitch="-1Hz")
    await c1.save(audio_shot01)
    print("Synthesizing Lao Liu monologue...")
    c2 = edge_tts.Communicate(text_02, "zh-CN-YunjianNeural", rate="+18%", pitch="-1Hz")
    await c2.save(audio_shot02)

asyncio.run(synthesize())
print("Audio generation complete.")

# 2. Render Shot 01 (10.01s raw video padded to 11.0s, subtitle + audio mix)
raw_shot01 = os.path.join(base_dir, "assets", "videos", "shot_01_macro_city_to_lu_yuan_monologue.mp4")
shot01_v2 = os.path.join(out_dir, "shot_01_v2.mp4")
font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

sub_lu1 = "我叫陆远，23岁，大模型AI算法架构师。"
sub_lu2 = "着眼于人工智能的创新发展，我们透视底层逻辑，"
sub_lu3 = "却陷入了算法决策的伦理困境。"

filter_complex_01 = (
    f"[0:v]tpad=stop_mode=clone:stop_duration=1.2,"
    f"drawtext=fontfile='{font_file}':text='{sub_lu1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.3,3.7)',"
    f"drawtext=fontfile='{font_file}':text='{sub_lu2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,3.8,7.5)',"
    f"drawtext=fontfile='{font_file}':text='{sub_lu3}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,7.6,10.7)'[vout];"
    f"[0:a]volume=0.35[bg];"
    f"[1:a]adelay=300|300,volume=1.65[vo];"
    f"[bg][vo]amix=inputs=2:duration=first:dropout_transition=2[aout]"
)

cmd_01 = [
    ffmpeg, "-y",
    "-i", raw_shot01,
    "-i", audio_shot01,
    "-filter_complex", filter_complex_01,
    "-map", "[vout]", "-map", "[aout]",
    "-t", "11.0",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    shot01_v2
]

print("Rendering Shot 01 v2 with Lu Yuan AI theme monologue...")
subprocess.run(cmd_01, check=True)
print(f"Shot 01 v2 rendered: {shot01_v2}")

# 3. Render Shot 02 (10.01s raw video padded to 10.6s, subtitle + audio mix)
raw_shot02 = os.path.join(base_dir, "assets", "videos", "shot_02_lao_liu_scooter_rain.mp4")
shot02_v2 = os.path.join(out_dir, "shot_02_v2.mp4")

sub_liu1 = "我叫刘长贵，48岁，是个被AI模型考核的外卖员。"
sub_liu2 = "雨再大我也得冲！小孙女等钱透析，绝不能被算法判定超时！"

filter_complex_02 = (
    f"[0:v]tpad=stop_mode=clone:stop_duration=0.8,"
    f"drawtext=fontfile='{font_file}':text='{sub_liu1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.3,4.5)',"
    f"drawtext=fontfile='{font_file}':text='{sub_liu2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.6,10.2)'[vout];"
    f"[0:a]volume=0.4[rain];"
    f"[1:a]adelay=300|300,volume=1.65[vo];"
    f"[rain][vo]amix=inputs=2:duration=first:dropout_transition=2[aout]"
)

cmd_02 = [
    ffmpeg, "-y",
    "-i", raw_shot02,
    "-i", audio_shot02,
    "-filter_complex", filter_complex_02,
    "-map", "[vout]", "-map", "[aout]",
    "-t", "10.6",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    shot02_v2
]

print("Rendering Shot 02 v2 with Lao Liu intro...")
subprocess.run(cmd_02, check=True)
print(f"Shot 02 v2 rendered: {shot02_v2}")

# 4. Concatenate Shot 01 (11.0s) + Shot 02 (10.6s) + Shot 03 (10.01s) -> 31.6s Cut
shot03_vo = os.path.join(out_dir, "shot_03_with_vo.mp4")
final_31s = os.path.join(out_dir, "act1_seamless_31s_character_intro.mp4")

cmd_concat = [
    ffmpeg, "-y",
    "-i", shot01_v2,
    "-i", shot02_v2,
    "-i", shot03_vo,
    "-filter_complex", "[0:v][0:a][1:v][1:a][2:v][2:a]concat=n=3:v=1:a=1[v][a]",
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    final_31s
]

print("Concatenating Act 1 (31.6s) with character introductions...")
subprocess.run(cmd_concat, check=True)
print(f"Act 1 seamless video rendered successfully: {final_31s}")
