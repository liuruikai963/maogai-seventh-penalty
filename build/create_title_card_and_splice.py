import os
import subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

base_dir = "d:/study/course/maogai/homework"
out_dir = os.path.join(base_dir, "dist")
os.makedirs(out_dir, exist_ok=True)

# 1. Create Title Card Image (1280x720)
width, height = 1280, 720
img = Image.new("RGB", (width, height), color=(10, 10, 14))
draw = ImageDraw.Draw(img)

font_path = "C:/Windows/Fonts/msyh.ttc"
font_title = ImageFont.truetype(font_path, 32)
font_body = ImageFont.truetype(font_path, 28)

lines = [
    ("深夜，暴雨倾盆。", (210, 215, 225), font_title),
    ("48岁的外卖员老刘，正全身湿透在淹没的街道上拼命赶路。", (245, 245, 250), font_body),
    ("为了凑齐重病小孙女的透析救命钱，他必须在倒计时清零前送达。", (235, 180, 120), font_body), # Warm highlight
]

# Calculate vertical positions
line_height = 55
total_text_height = len(lines) * line_height
start_y = (height - total_text_height) // 2

for i, (text, color, font) in enumerate(lines):
    bbox = font.getbbox(text)
    text_w = bbox[2] - bbox[0]
    x = (width - text_w) // 2
    y = start_y + i * line_height
    draw.text((x, y), text, font=font, fill=color)

card_img_path = os.path.join(out_dir, "card_lao_liu.jpg")
img.save(card_img_path, quality=95)
print(f"Title card image saved to {card_img_path}")

# 2. Render Card Video (3.2 seconds, 24fps, 1280x720, AAC 48k stereo)
card_video_path = os.path.join(out_dir, "card_lao_liu.mp4")

# Using anlavfi to generate silent audio matching 48000Hz stereo
cmd_card = [
    ffmpeg, "-y",
    "-loop", "1", "-i", card_img_path,
    "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
    "-vf", "fade=in:0:12,fade=out:65:12,format=yuv420p",
    "-c:v", "libx264", "-tune", "stillimage", "-preset", "fast",
    "-c:a", "aac", "-b:a", "128k",
    "-t", "3.2",
    "-r", "24",
    "-pix_fmt", "yuv420p",
    "-shortest",
    card_video_path
]

print("Rendering title card video...")
subprocess.run(cmd_card, check=True)

# 3. Concatenate all 3 clips
video1 = os.path.join(base_dir, "assets", "videos", "shot_01_macro_city_to_lu_yuan_monologue.mp4")
video2 = card_video_path
video3 = os.path.join(base_dir, "assets", "videos", "shot_02_lao_liu_scooter_rain.mp4")
final_output = os.path.join(out_dir, "act1_opening_with_card_23s.mp4")

concat_list = os.path.join(out_dir, "concat_card.txt")
with open(concat_list, "w", encoding="utf-8") as f:
    f.write(f"file '{video1.replace(os.sep, '/')}'\n")
    f.write(f"file '{video2.replace(os.sep, '/')}'\n")
    f.write(f"file '{video3.replace(os.sep, '/')}'\n")

# Use concat demuxer or re-encode concat filter for perfect audio sync
cmd_concat = [
    ffmpeg, "-y",
    "-i", video1,
    "-i", video2,
    "-i", video3,
    "-filter_complex", "[0:v][0:a][1:v][1:a][2:v][2:a]concat=n=3:v=1:a=1[v][a]",
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "128k",
    final_output
]

print("Splicing 3 clips together...")
subprocess.run(cmd_concat, check=True)
print(f"Successfully generated: {final_output}")
