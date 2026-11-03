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

# ============================================================
# 1. Render Shot 01 (Lu Yuan Workstation Monologue)
#    Native AI vocal removed, replaced with clean broadcast voiceover + room/thunder ambience
# ============================================================
raw_01 = os.path.join(raw_dir, "shot_01_luyuan_office_monologue.mp4")
vo_01 = os.path.join(audio_dir, "shot_01_luyuan_clean_vo.mp3")
out_01 = os.path.join(shots_dir, "shot_01_final.mp4")

sub_01_1 = "我叫陆远，23岁，算法架构师。"
sub_01_2 = "我们试图透视人工智能的底层逻辑，开展算法伦理调查……"
sub_01_3 = "直到那个暴雨深夜。"

filter_01 = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_01_1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.3,3.3)',"
    f"drawtext=fontfile='{font_file}':text='{sub_01_2}':fontsize=26:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,3.4,6.8)',"
    f"drawtext=fontfile='{font_file}':text='{sub_01_3}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,6.9,9.4)'[vout];"
    f"[0:a]volume=0.25[bg_native];"
    f"[1:a]adelay=300|300,volume=1.7[vo];"
    f"[bg_native][vo]amix=inputs=2:duration=first:dropout_transition=2[aout]"
)

cmd_01 = [
    ffmpeg, "-y",
    "-i", raw_01,
    "-i", vo_01,
    "-filter_complex", filter_01,
    "-map", "[vout]", "-map", "[aout]",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-t", "10.03",
    out_01
]

print("Rendering Shot 01 (Lu Yuan) with clean professional studio voiceover...")
subprocess.run(cmd_01, check=True)
print(f"Shot 01 rendered: {out_01}")

# ============================================================
# 2. Render Shot 02A (Lao Liu Front Medium Monologue)
#    Native AI vocal removed, replaced with clean weathered voiceover + pure storm Foley
# ============================================================
raw_02a = os.path.join(raw_dir, "shot_02a_lao_liu_monologue.mp4")
raw_rain = os.path.join(raw_dir, "shot_02b_lao_liu_scooter_wading.mp4")
vo_02a = os.path.join(audio_dir, "shot_02a_laoliu_clean_vo.mp3")
out_02a = os.path.join(shots_dir, "shot_02a_final.mp4")

sub_02a_1 = "我叫刘长贵，48岁，送外卖给孙女挣药费。"
sub_02a_2 = "今晚暴雨单价高，但绝不能超时……"
sub_02a_3 = "要是扣了钱，孙女的药就没了！"

filter_02a = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_02a_1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.3,3.5)',"
    f"drawtext=fontfile='{font_file}':text='{sub_02a_2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,3.6,6.3)',"
    f"drawtext=fontfile='{font_file}':text='{sub_02a_3}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,6.4,9.5)'[vout];"
    f"[1:a]volume=0.45[storm_bg];"
    f"[2:a]adelay=350|350,volume=1.75[vo];"
    f"[storm_bg][vo]amix=inputs=2:duration=first:dropout_transition=2[aout]"
)

cmd_02a = [
    ffmpeg, "-y",
    "-i", raw_02a,
    "-i", raw_rain,
    "-i", vo_02a,
    "-filter_complex", filter_02a,
    "-map", "[vout]", "-map", "[aout]",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-t", "10.03",
    out_02a
]

print("Rendering Shot 02A (Lao Liu Monologue) with clean weathered voiceover and pure storm foley...")
subprocess.run(cmd_02a, check=True)
print(f"Shot 02A rendered: {out_02a}")

# ============================================================
# 3. Render Shot 02B (Lao Liu Rainstorm Scooter Wading Action)
#    Dynamic storm foley + urgent struggle shout
# ============================================================
raw_02b = os.path.join(raw_dir, "shot_02b_lao_liu_scooter_wading.mp4")
vo_02b = os.path.join(audio_dir, "shot_02b_laoliu_clean_vo.mp3")
out_02b = os.path.join(shots_dir, "shot_02b_final.mp4")

sub_02b_1 = "雨再大我也得冲！冲过去……"
sub_02b_2 = "绝不能超时，只要这单送到，药费就有着落了！"

filter_02b = (
    f"[0:v]drawtext=fontfile='{font_file}':text='{sub_02b_1}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,0.5,3.2)',"
    f"drawtext=fontfile='{font_file}':text='{sub_02b_2}':fontsize=28:fontcolor=white:bordercolor=black:borderw=3:shadowx=2:shadowy=2:x=(w-text_w)/2:y=h-70:enable='between(t,3.3,7.2)'[vout];"
    f"[0:a]volume=0.45[storm_bg];"
    f"[1:a]adelay=400|400,volume=1.7[vo];"
    f"[storm_bg][vo]amix=inputs=2:duration=first:dropout_transition=2[aout]"
)

cmd_02b = [
    ffmpeg, "-y",
    "-i", raw_02b,
    "-i", vo_02b,
    "-filter_complex", filter_02b,
    "-map", "[vout]", "-map", "[aout]",
    "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-t", "10.01",
    out_02b
]

print("Rendering Shot 02B (Lao Liu Wading) with dynamic struggle voiceover and storm sound...")
subprocess.run(cmd_02b, check=True)
print(f"Shot 02B rendered: {out_02b}")

# ============================================================
# 4. Concatenate Complete Act 1 Cut (Shot 01 + Shot 02A + Shot 02B + Shot 03 + Shot 05)
# ============================================================
shot03 = os.path.join(shots_dir, "shot_03_final.mp4")
shot05 = os.path.join(shots_dir, "shot_05_final.mp4")
act1_full = os.path.join(acts_dir, "act1_complete_full_cut.mp4")

cmd_concat = [
    ffmpeg, "-y",
    "-i", out_01,
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

print("Concatenating newly dubbed Act 1 complete full cut...")
subprocess.run(cmd_concat, check=True)
print(f"Act 1 complete full cut successfully generated: {act1_full}")
