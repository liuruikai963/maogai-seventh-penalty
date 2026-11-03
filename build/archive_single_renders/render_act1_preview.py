import os
import subprocess
import imageio_ffmpeg

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

base_dir = "d:/study/course/maogai/homework"
images_dir = os.path.join(base_dir, "assets", "images")
audio_dir = os.path.join(base_dir, "assets", "audio")
output_dir = os.path.join(base_dir, "dist")
os.makedirs(output_dir, exist_ok=True)

# Durations in seconds
shots_info = [
    (1, 15.0, "zoom_in"),
    (2, 11.5, "pan_right"),
    (3, 8.0,  "zoom_in"),
    (4, 8.5,  "zoom_in"),
    (5, 4.5,  "static"),
]

clip_paths = []

for idx, duration, motion in shots_info:
    img_path = os.path.join(images_dir, f"shot_{idx:02d}.jpg")
    aud_path = os.path.join(audio_dir, f"shot_{idx:02d}.mp3")
    clip_path = os.path.join(output_dir, f"clip_{idx:02d}.mp4")
    
    fps = 30
    total_frames = int(duration * fps)
    
    if motion == "zoom_in":
        vf = f"scale=1920:1080,zoompan=z='min(zoom+0.0005,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=1920x1080:fps={fps},format=yuv420p"
    elif motion == "pan_right":
        vf = f"scale=2048:1152,crop=1920:1080:'min(t*10, 128)':0,format=yuv420p"
    else:
        vf = f"scale=1920:1080,format=yuv420p"
        
    cmd = [
        ffmpeg, "-y",
        "-loop", "1", "-i", img_path,
        "-i", aud_path,
        "-vf", vf,
        "-c:v", "libx264", "-tune", "stillimage", "-preset", "fast",
        "-c:a", "aac", "-b:a", "192k",
        "-t", str(duration),
        "-pix_fmt", "yuv420p",
        "-shortest",
        clip_path
    ]
    
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        cmd_fallback = [
            ffmpeg, "-y",
            "-loop", "1", "-i", img_path,
            "-i", aud_path,
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast",
            "-c:a", "aac", "-b:a", "192k",
            "-t", str(duration),
            "-pix_fmt", "yuv420p",
            clip_path
        ]
        subprocess.run(cmd_fallback, check=True)
        
    clip_paths.append(clip_path)

concat_txt_path = os.path.join(output_dir, "concat.txt")
with open(concat_txt_path, "w", encoding="utf-8") as f:
    for cp in clip_paths:
        f.write(f"file '{cp.replace(os.sep, '/')}'\n")

final_mp4 = os.path.join(output_dir, "act1_preview.mp4")
cmd_concat = [
    ffmpeg, "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_txt_path,
    "-c", "copy",
    final_mp4
]

subprocess.run(cmd_concat, check=True)
print(f"Generated: {final_mp4}")
