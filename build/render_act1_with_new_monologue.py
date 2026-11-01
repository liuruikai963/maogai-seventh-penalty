import os
import subprocess
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
base_dir = "d:/study/course/maogai/homework"
raw_dir = os.path.join(base_dir, "assets", "videos", "raw_inputs")
dist_dir = os.path.join(base_dir, "dist")
shots_dir = os.path.join(dist_dir, "shots")
acts_dir = os.path.join(dist_dir, "acts")
os.makedirs(shots_dir, exist_ok=True)
os.makedirs(acts_dir, exist_ok=True)

font_file = "C\\:/Windows/Fonts/msyhbd.ttc"

# ============================================================
# 1. Render New Shot 01 (Lu Yuan Workstation Monologue)
# ============================================================
raw_shot01 = os.path.join(raw_dir, "shot_01_luyuan_office_monologue.mp4")
shot01_out = os.path.join(shots_dir, "shot_01_final.mp4")

sub1 = "我叫陆远，23岁，大模型调度算法架构师。"
sub2 = "着眼于人工智能的创新发展，我们试图透视热点事件的底层逻辑，"
sub3 = "开展算法决策的伦理困境调查……直到那个特大暴雨的深夜。"

filter_sub = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.3,3.7)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=26:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,3.8,7.1)',"
    f"drawtext=fontfile='{font_file}':text='{sub3}':fontsize=26:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,7.2,9.8)'[vout]"
)

cmd_shot01 = [
    ffmpeg, "-y",
    "-i", raw_shot01,
    "-filter_complex", filter_sub,
    "-map", "[vout]",
    "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    shot01_out
]

print("Rendering Shot 01 final with synchronized subtitles and native audio...")
subprocess.run(cmd_shot01, check=True)
print(f"Shot 01 rendered successfully: {shot01_out}")

# ============================================================
# 2. Concatenate New Act 1 Full Cut:
#    Shot 01 (10.03s, Monologue & Lightning)
#    + Shot 02 (10.63s, Lao Liu Scooter in Rain)
#    + Shot 03 (10.01s, Phone Countdown Penalty)
#    + Shot 05 (7.00s, Penalty Modal Pop-up & Ban)
# ============================================================
shot02 = os.path.join(shots_dir, "shot_02_final.mp4")
shot03 = os.path.join(shots_dir, "shot_03_final.mp4")
shot05 = os.path.join(shots_dir, "shot_05_final.mp4")
act1_full = os.path.join(acts_dir, "act1_complete_full_cut.mp4")

cmd_concat = [
    ffmpeg, "-y",
    "-i", shot01_out,
    "-i", shot02,
    "-i", shot03,
    "-i", shot05,
    "-filter_complex", "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a]concat=n=4:v=1:a=1[v][a]",
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    act1_full
]

print("Concatenating Act 1 full cut with direct transition into Lao Liu...")
subprocess.run(cmd_concat, check=True)
print(f"Act 1 full cut exported successfully: {act1_full}")
