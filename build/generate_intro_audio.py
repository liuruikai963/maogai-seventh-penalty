# -*- coding: utf-8 -*-
import numpy as np
import wave, struct, os, subprocess
import imageio_ffmpeg
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

sr = 48000
duration = 10.0
total_samples = int(sr * duration)
t = np.linspace(0, duration, total_samples, endpoint=False)

audio = np.zeros(total_samples, dtype=np.float32)

# 1. Clock ticks at 0.8, 1.6, 2.4, 3.2
for tick_time in [0.8, 1.6, 2.4, 3.2]:
    idx = int(tick_time * sr)
    tick_len = int(0.04 * sr)
    tt = np.linspace(0, 0.04, tick_len)
    tick_wave = np.sin(2 * np.pi * 1800 * tt) * np.exp(-tt * 100)
    audio[idx:idx+tick_len] += tick_wave * 0.25

# 2. Cinematic Sub-Bass Drop at 3.5s (120Hz -> 38Hz)
bass_start = int(3.5 * sr)
bass_len = int(2.5 * sr)
bt = np.linspace(0, 2.5, bass_len)
# exponential frequency drop
f_sweep = 120 * np.exp(-bt * 1.5) + 38
phase = 2 * np.pi * np.cumsum(f_sweep) / sr
bass_wave = np.sin(phase) * np.exp(-bt * 1.2)
audio[bass_start:bass_start+bass_len] += bass_wave * 0.55

# 3. Resonant chime / bell at 3.5s (880Hz, 1320Hz harmonics)
bell_len = int(3.0 * sr)
belt = np.linspace(0, 3.0, bell_len)
bell_wave = (np.sin(2 * np.pi * 880 * belt) * 0.6 + 
             np.sin(2 * np.pi * 1320 * belt) * 0.3 + 
             np.sin(2 * np.pi * 1760 * belt) * 0.15) * np.exp(-belt * 2.0)
audio[bass_start:bass_start+bell_len] += bell_wave * 0.25

# 4. Uplifting cinematic chord crescendo from 5.5s to 9.5s
# D major chord: D4 (293.66), F#4 (369.99), A4 (440.0), D5 (587.33), F#5 (739.99)
chord_start = int(5.5 * sr)
chord_len = int(4.5 * sr)
ct = np.linspace(0, 4.5, chord_len)
# Envelope: rise from 0 to 1 at 2.5s (time 8.0s), then fade out by 4.5s (time 10.0s)
env = np.zeros_like(ct)
rise_len = int(2.2 * sr)
env[:rise_len] = 0.5 * (1 - np.cos(np.pi * np.linspace(0, 1, rise_len)))
fade_len = chord_len - rise_len
env[rise_len:] = 0.5 * (1 + np.cos(np.pi * np.linspace(0, 1, fade_len)))

chord_wave = (
    np.sin(2 * np.pi * 293.66 * ct) * 0.35 +
    np.sin(2 * np.pi * 369.99 * ct) * 0.30 +
    np.sin(2 * np.pi * 440.00 * ct) * 0.25 +
    np.sin(2 * np.pi * 587.33 * ct) * 0.20 +
    np.sin(2 * np.pi * 739.99 * ct) * 0.15
) * env
audio[chord_start:chord_start+chord_len] += chord_wave * 0.50

# Normalize to prevent clipping
peak = np.max(np.abs(audio))
if peak > 0:
    audio = audio / peak * 0.85

# Fade out last 0.3s
fade_out_samples = int(0.3 * sr)
audio[-fade_out_samples:] *= np.linspace(1, 0, fade_out_samples)

# Save synthesized elements
synth_wav = 'assets/audio/foley/intro_synth_elements.wav'
int_audio = (audio * 32767).astype(np.int16)
with wave.open(synth_wav, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sr)
    wf.writeframes(int_audio.tobytes())

print(f"Synthesized cinematic track saved to: {synth_wav}")

# Now mix with ambient rain foley using ffmpeg
foley_rain = 'assets/audio/foley/foley_storm_clean.wav'
mixed_wav = 'assets/audio/foley/intro_title_audio_master.wav'

if os.path.exists(foley_rain):
    cmd = [
        ffmpeg_exe, '-y',
        '-i', synth_wav,
        '-ss', '0', '-t', '10', '-i', foley_rain,
        '-filter_complex',
        '[1:a]volume=0.35,afade=t=out:st=9.0:d=1.0[rain];[0:a][rain]amix=inputs=2:duration=first:dropout_transition=2[aout]',
        '-map', '[aout]',
        '-c:a', 'pcm_s16le',
        mixed_wav
    ]
    subprocess.run(cmd, check=True)
    print(f"Final mixed intro audio saved to: {mixed_wav}")
else:
    print("Warning: foley_storm_clean.wav not found, using synth track directly.")
    mixed_wav = synth_wav
