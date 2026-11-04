# -*- coding: utf-8 -*-
import os, subprocess, imageio_ffmpeg, shutil

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

intro = 'dist/acts/intro_title_sequence.mp4'
acts123 = 'dist/acts/liuruikai_part1_complete_master.mp4'
outro = 'dist/acts/outro_credits_sequence.mp4'
output_master = 'dist/acts/current_stage_full_presentation.mp4'

print(f"Concatenating current stage presentation:")
print(f"  [1] Intro Title Sequence: {intro} (18.00s)")
print(f"  [2] Acts 1-3 Master Cut : {acts123} (~180.51s)")
print(f"  [3] Outro Credits Sequence: {outro} (24.00s)")

# Use filter_complex concat to ensure perfectly uniform 1280x720 @ 24fps video and 48kHz stereo audio
cmd = [
    ffmpeg_exe, '-y',
    '-i', intro,
    '-i', acts123,
    '-i', outro,
    '-filter_complex',
    '[0:v]fps=24,scale=1280:720,setsar=1[v0];'
    '[0:a]aformat=sample_rates=48000:channel_layouts=stereo[a0];'
    '[1:v]fps=24,scale=1280:720,setsar=1[v1];'
    '[1:a]aformat=sample_rates=48000:channel_layouts=stereo[a1];'
    '[2:v]fps=24,scale=1280:720,setsar=1[v2];'
    '[2:a]aformat=sample_rates=48000:channel_layouts=stereo[a2];'
    '[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[v][a]',
    '-map', '[v]',
    '-map', '[a]',
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '18',
    '-pix_fmt', 'yuv420p',
    '-c:a', 'aac',
    '-b:a', '192k',
    output_master
]

print("Running FFmpeg concat...")
subprocess.run(cmd, check=True)
print(f"Successfully generated: {output_master}")

# Copy to artifacts directory
artifact_dir = r'C:/Users/27277/.gemini/antigravity/brain/f5b14212-99d2-460d-9706-e55469254373'
artifact_copy = os.path.join(artifact_dir, 'current_stage_full_presentation.mp4')
shutil.copy(output_master, artifact_copy)
print(f"Copied to artifact directory: {artifact_copy}")
