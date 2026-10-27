import os
import subprocess
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

base_dir = "d:/study/course/maogai/homework"
video1 = os.path.join(base_dir, "assets", "videos", "shot_01_macro_city_to_lu_yuan_monologue.mp4")
video2 = os.path.join(base_dir, "assets", "videos", "shot_02_lao_liu_scooter_rain.mp4")
out_dir = os.path.join(base_dir, "dist")
os.makedirs(out_dir, exist_ok=True)
output_mp4 = os.path.join(out_dir, "act1_opening_20s.mp4")

# Create concat list
concat_list = os.path.join(out_dir, "concat_opening.txt")
with open(concat_list, "w", encoding="utf-8") as f:
    f.write(f"file '{video1.replace(os.sep, '/')}'\n")
    f.write(f"file '{video2.replace(os.sep, '/')}'\n")

cmd = [
    ffmpeg, "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_list,
    "-c", "copy",
    output_mp4
]

print("Concatenating Shot 01 and Shot 02...")
subprocess.run(cmd, check=True)
print(f"Successfully created: {output_mp4}")
