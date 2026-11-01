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
# 1. Render Shot 02A (Lao Liu Front Medium Monologue)
# ============================================================
raw_02a = os.path.join(raw_dir, "shot_02a_lao_liu_monologue.mp4")
out_02a = os.path.join(shots_dir, "shot_02a_final.mp4")

sub1 = "我叫刘长贵，48岁，送外卖给孙女挣药费。"
sub2 = "今晚暴雨单价高，但绝不能超时……"
sub3 = "要是扣了钱，孙女的药就没了！"

filter_02a = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.3,3.5)',"
    f"drawtext=fontfile='{font_file}':text='{sub2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,3.6,6.2)',"
    f"drawtext=fontfile='{font_file}':text='{sub3}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,6.3,8.8)'[vout]"
)

cmd_02a = [
    ffmpeg, "-y",
    "-i", raw_02a,
    "-filter_complex", filter_02a,
    "-map", "[vout]",
    "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    out_02a
]

print("Rendering Shot 02A final with synchronized subtitles and native audio...")
subprocess.run(cmd_02a, check=True)
print(f"Shot 02A rendered successfully: {out_02a}")

# ============================================================
# 2. Render Shot 02B (Lao Liu Rainstorm Scooter Wading Action)
#    We use the existing high-octane wading shot with dynamic struggle
# ============================================================
out_02b = os.path.join(shots_dir, "shot_02b_final.mp4")
raw_02b = os.path.join(raw_dir, "shot_02b_lao_liu_scooter_wading.mp4")

# Lao Liu's action struggle subtitles during wading
sub_b1 = "雨再大我也得冲！冲过去……"
sub_b2 = "绝不能超时，只要这单送到，药费就有着落了！"

filter_02b = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_b1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.5,4.5)',"
    f"drawtext=fontfile='{font_file}':text='{sub_b2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,4.6,9.5)'[vout]"
)

cmd_02b = [
    ffmpeg, "-y",
    "-i", raw_02b,
    "-filter_complex", filter_02b,
    "-map", "[vout]",
    "-map", "0:a",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    out_02b
]

print("Rendering Shot 02B final with dynamic action subtitles and storm sound...")
subprocess.run(cmd_02b, check=True)
print(f"Shot 02B rendered successfully: {out_02b}")

# ============================================================
# 3. Concatenate Act 1 Full Dynamic Cut:
#    Shot 01 (10.03s, Lu Yuan Monologue & Lightning)
#    + Shot 02A (10.03s, Lao Liu Monologue & Urgency)
#    + Shot 02B (10.01s, Lao Liu Rain Wading Action)
#    + Shot 03 (10.01s, Phone Countdown Penalty)
#    + Shot 05 (7.00s, Penalty Modal Pop-up & Ban)
# ============================================================
shot01 = os.path.join(shots_dir, "shot_01_final.mp4")
shot03 = os.path.join(shots_dir, "shot_03_final.mp4")
shot05 = os.path.join(shots_dir, "shot_05_final.mp4")
act1_full = os.path.join(acts_dir, "act1_complete_full_cut.mp4")

cmd_concat = [
    ffmpeg, "-y",
    "-i", shot01,
    "-i", out_02a,
    "-i", out_02b,
    "-i", shot03,
    "-i", shot05,
    "-filter_complex", "[0:v][0:a][1:v][1:a][2:v][2:a][3:v][3:a][4:v][4:a]concat=n=5:v=1:a=1[v][a]",
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    act1_full
]

print("Concatenating complete 5-shot Act 1 cut...")
subprocess.run(cmd_concat, check=True)
print(f"Act 1 complete full cut exported: {act1_full}")
