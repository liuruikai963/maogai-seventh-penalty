# -*- coding: utf-8 -*-
import numpy as np
import wave, struct, os, subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

sr = 48000
duration = 14.5 # Updated to 14.5 seconds exact!
total_samples = int(sr * duration)
t = np.linspace(0, duration, total_samples, endpoint=False)

audio = np.zeros(total_samples, dtype=np.float32)

# Helper to create a single mechanical typewriter click
def add_click(arr, at_time, gain=0.22):
    idx = int(at_time * sr)
    click_len = int(0.025 * sr)
    ct = np.linspace(0, 0.025, click_len)
    noise = np.random.uniform(-1, 1, click_len) * np.exp(-ct * 300)
    ping = np.sin(2 * np.pi * 2400 * ct) * np.exp(-ct * 150)
    click = (noise * 0.7 + ping * 0.3) * gain
    arr[idx:idx+click_len] += click

# Helper for return bell
def add_bell(arr, at_time, gain=0.26):
    idx = int(at_time * sr)
    bell_len = int(0.6 * sr)
    bt = np.linspace(0, 0.6, bell_len)
    bell = (np.sin(2 * np.pi * 1760 * bt) * 0.7 + np.sin(2 * np.pi * 3520 * bt) * 0.3) * np.exp(-bt * 8)
    arr[idx:idx+bell_len] += bell * gain

# 1. Phase 1 (0.0s - 5.0s): Slower, dignified typewriter clicks
# Line 1 clicks: 0.5s to 2.8s (~24 clicks)
# Line 2 clicks: 2.9s to 4.2s (~18 clicks)
click_times_l1 = np.linspace(0.5, 2.7, 24) + np.random.uniform(-0.015, 0.015, 24)
click_times_l2 = np.linspace(2.9, 4.1, 18) + np.random.uniform(-0.015, 0.015, 18)
for ct in np.concatenate([click_times_l1, click_times_l2]):
    add_click(audio, ct, gain=0.22)
add_bell(audio, 4.25, gain=0.25)

# 2. Phase 2 (5.0s - 8.0s): Philosophical Tone & Heartbeat
# Heartbeat / clock pulses at 5.2, 5.9, 6.6, 7.3
for ht in [5.2, 5.9, 6.6, 7.3]:
    idx = int(ht * sr)
    hlen = int(0.12 * sr)
    htt = np.linspace(0, 0.12, hlen)
    heartbeat = np.sin(2 * np.pi * 55 * htt) * np.exp(-htt * 35)
    audio[idx:idx+hlen] += heartbeat * 0.35

# Soft piano/synth tone at 5.0s
pt_len = int(2.8 * sr)
pt = np.linspace(0, 2.8, pt_len)
p_idx = int(5.0 * sr)
piano = (np.sin(2 * np.pi * 220 * pt) * 0.5 + np.sin(2 * np.pi * 440 * pt) * 0.3) * np.exp(-pt * 1.5)
audio[p_idx:p_idx+pt_len] += piano * 0.22

# 3. Phase 3 (8.0s - 14.5s): Cinematic Sub-Bass Impact Boom at 8.0s!
bass_start = int(8.0 * sr)
bass_len = int(4.0 * sr)
bt = np.linspace(0, 4.0, bass_len)
f_sweep = 135 * np.exp(-bt * 1.8) + 30
phase = 2 * np.pi * np.cumsum(f_sweep) / sr
impact_noise = np.random.uniform(-1, 1, int(0.2 * sr)) * np.exp(-np.linspace(0, 0.2, int(0.2 * sr)) * 30)
audio[bass_start:bass_start+int(0.2 * sr)] += impact_noise * 0.4
audio[bass_start:bass_start+bass_len] += np.sin(phase) * np.exp(-bt * 0.85) * 0.70

# 4. Glorious Orchestral Chord Swell (8.1s to 14.2s)
chord_start = int(8.1 * sr)
chord_len = int(6.1 * sr)
ct = np.linspace(0, 6.1, chord_len)
env = np.zeros_like(ct)
rise = int(2.2 * sr)
env[:rise] = 0.5 * (1 - np.cos(np.pi * np.linspace(0, 1, rise)))
fade = chord_len - rise
env[rise:] = 0.5 * (1 + np.cos(np.pi * np.linspace(0, 1, fade)))

chord = (
    np.sin(2 * np.pi * 293.66 * ct) * 0.35 + # D4
    np.sin(2 * np.pi * 369.99 * ct) * 0.30 + # F#4
    np.sin(2 * np.pi * 440.00 * ct) * 0.25 + # A4
    np.sin(2 * np.pi * 587.33 * ct) * 0.20 + # D5
    np.sin(2 * np.pi * 739.99 * ct) * 0.15   # F#5
) * env
audio[chord_start:chord_start+chord_len] += chord * 0.55

# Normalize
peak = np.max(np.abs(audio))
if peak > 0:
    audio = audio / peak * 0.88

# Fade out last 0.3s
fade_samples = int(0.3 * sr)
audio[-fade_samples:] *= np.linspace(1, 0, fade_samples)

out_wav = 'assets/audio/foley/intro_typewriter_audio_master.wav'
int_audio = (audio * 32767).astype(np.int16)
with wave.open(out_wav, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sr)
    wf.writeframes(int_audio.tobytes())

print(f"Generated 14.5s master typewriter audio track: {out_wav}")
