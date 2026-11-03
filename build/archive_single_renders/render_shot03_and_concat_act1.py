import os
import subprocess
import asyncio
import edge_tts
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base_dir = "d:/study/course/maogai/homework"
out_dir = os.path.join(base_dir, "dist")
os.makedirs(out_dir, exist_ok=True)

# 1. Generate Cold System AI Voice
sys_text = "订单已严重超时，系统扣除当单全部收入。本月违规次数已达上限！"
sys_audio_path = os.path.join(base_dir, "assets", "audio", "shot_03_system_voice.mp3")

async def generate_sys_audio():
    print(f"Generating System AI Voice: {sys_text}")
    comm = edge_tts.Communicate(sys_text, "zh-CN-XiaoxiaoNeural", rate="+25%", pitch="+4Hz")
    await comm.save(sys_audio_path)

asyncio.run(generate_sys_audio())
print(f"System audio saved to {sys_audio_path}")

# 2. Render Shot 03 with Audio Mix & Subtitles
raw_shot03 = os.path.join(base_dir, "assets", "videos", "shot_03_phone_countdown.mp4")
shot03_with_vo = os.path.join(out_dir, "shot_03_with_vo.mp4")

font_file = "C\\:/Windows/Fonts/msyhbd.ttc"
sub1 = "订单已严重超时，系统扣除当单全部收入。"
sub2 = "本月违规次数已达上限！"

# Timing: countdown flashes 00:00 at 3.8s, "严重超时" pop-up.
# Voice delay: 3800ms
filter_complex = (
    f"[0:a]volume=0.6[sfx];"
    f"[1:a]adelay=3800|3800,volume=1.65[sys];"
    f"[sfx][sys]amix=inputs=2:duration=first:dropout_transition=2[aout];"
    f"[0:v]"
    f"drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,3.8,6.8)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,6.9,9.8)'[vout]"
)

cmd_shot03 = [
    ffmpeg, "-y",
    "-i", raw_shot03,
    "-i", sys_audio_path,
    "-filter_complex", filter_complex,
    "-map", "[vout]",
    "-map", "[aout]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    shot03_with_vo
]

print("Rendering Shot 03 with system voice and subtitles...")
subprocess.run(cmd_shot03, check=True)
print(f"Shot 03 with VO successfully rendered: {shot03_with_vo}")

# 3. Concatenate Shot 01 (10s) + Shot 02 (10s) + Shot 03 (10s) -> 30s Seamless Sequence
opening_20s = os.path.join(out_dir, "act1_opening_seamless_20s.mp4")
act1_30s = os.path.join(out_dir, "act1_seamless_30s.mp4")

cmd_concat = [
    ffmpeg, "-y",
    "-i", opening_20s,
    "-i", shot03_with_vo,
    "-filter_complex", "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]",
    "-map", "[v]",
    "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    act1_30s
]

print("Concatenating into Act 1 seamless 30s cut...")
subprocess.run(cmd_concat, check=True)
print(f"Act 1 seamless 30s video successfully created: {act1_30s}")
