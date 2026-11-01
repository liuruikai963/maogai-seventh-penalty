import os
import subprocess
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base_dir = "d:/study/course/maogai/homework"
raw_dir = os.path.join(base_dir, "assets", "videos", "raw_inputs")
audio_dir = os.path.join(base_dir, "assets", "audio")
dist_dir = os.path.join(base_dir, "dist")
shots_dir = os.path.join(dist_dir, "shots")
acts_dir = os.path.join(dist_dir, "acts")
os.makedirs(shots_dir, exist_ok=True)
os.makedirs(acts_dir, exist_ok=True)

font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# ==========================================
# 1. Render Shot 01 Full Topic Monologue (15.0s)
# ==========================================
raw_shot01 = os.path.join(raw_dir, "shot_01_macro_city_to_lu_yuan_monologue.mp4")
audio_lu = os.path.join(audio_dir, "shot_01_lu_yuan_full_topic.mp3")
shot01_out = os.path.join(shots_dir, "shot_01_final.mp4")

sub_lu1 = "我叫陆远，23岁，大模型调度算法架构师。"
sub_lu2 = "着眼于人工智能的创新发展，我们试图透视城市运行的底层逻辑，"
sub_lu3 = "用AI模型计算最优解……却陷入了算法决策最残酷的伦理困境。"

filter_01 = (
    f"[0:v]tpad=stop_mode=clone:stop_duration=5.0,"
    f"drawtext=fontfile='{font_file}':text='{sub_lu1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.4,4.2)',"
    f"drawtext=fontfile='{font_file}':text='{sub_lu2}':fontsize=26:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.3,9.5)',"
    f"drawtext=fontfile='{font_file}':text='{sub_lu3}':fontsize=26:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,9.6,14.7)'[vout];"
    f"[0:a]volume=0.35[bg];"
    f"[1:a]adelay=400|400,volume=1.65[vo];"
    f"[bg][vo]amix=inputs=2:duration=first:dropout_transition=2[aout]"
)

cmd_01 = [
    ffmpeg, "-y",
    "-i", raw_shot01,
    "-i", audio_lu,
    "-filter_complex", filter_01,
    "-map", "[vout]", "-map", "[aout]",
    "-t", "15.0",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    shot01_out
]
print("Rendering Shot 01 with full academic topic monologue...")
subprocess.run(cmd_01, check=True)
print(f"Shot 01 rendered: {shot01_out}")

# ==========================================
# 2. Render Shot 05 Pop-up Penalty Ban (7.0s)
# ==========================================
raw_shot05 = os.path.join(raw_dir, "shot_05_penalty_modal.mp4")
audio_shot05 = os.path.join(audio_dir, "shot_05_system_freeze.mp3")
shot05_out = os.path.join(shots_dir, "shot_05_final.mp4")

sub_shot05 = "工单处理完毕，骑手账号已永久冻结。"

# Timing: mouse clicks around 2.5s -> voice delayed 2800ms
filter_05 = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_shot05}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,2.8,6.8)'[vout];"
    f"[0:a]volume=0.3[bg];"
    f"[1:a]adelay=2800|2800,volume=1.75[vo];"
    f"[bg][vo]amix=inputs=2:duration=first:dropout_transition=2[aout]"
)

cmd_05 = [
    ffmpeg, "-y",
    "-i", raw_shot05,
    "-i", audio_shot05,
    "-filter_complex", filter_05,
    "-map", "[vout]", "-map", "[aout]",
    "-t", "7.0",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    shot05_out
]
print("Rendering Shot 05 with system voice and subtitles...")
subprocess.run(cmd_05, check=True)
print(f"Shot 05 rendered: {shot05_out}")

# ==========================================
# 3. Concatenate All Act 1 Shots into Full Act 1 Cut (Shot 01 + Shot 02 + Shot 03 + Shot 05)
# ==========================================
shot02 = os.path.join(shots_dir, "shot_02_final.mp4")
shot03 = os.path.join(shots_dir, "shot_03_final.mp4")
act1_full = os.path.join(acts_dir, "act1_complete_full_cut.mp4")

cmd_concat = [
    ffmpeg, "-y",
    "-i", shot01_out,
    "-i", shot02,
    "-i", shot03,
    "-i", shot05_out,
    "-filter_complex", "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a]concat=n=4:v=1:a=1[v][a]",
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    act1_full
]
print("Concatenating complete Act 1 (Shot 01 + 02 + 03 + 05)...")
subprocess.run(cmd_concat, check=True)
print(f"Complete Act 1 Full Cut successfully generated: {act1_full}")
