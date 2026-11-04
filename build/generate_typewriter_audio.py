# -*- coding: utf-8 -*-
import numpy as np
import wave, struct, os, subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

sr = 48000
duration = 18.0 # 18.0 seconds exact!
total_samples = int(sr * duration)
t = np.linspace(0, duration, total_samples, endpoint=False)

audio = np.zeros(total_samples, dtype=np.float32)

# Helper for typewriter click
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

# 1. Phase 1 (0.0s - 7.0s): Academic & Creator Slate
# Line 1: 0.5s to 2.8s
# Line 2: 3.0s to 4.5s
click_times_l1 = np.linspace(0.5, 2.7, 24) + np.random.uniform(-0.015, 0.015, 24)
click_times_l2 = np.linspace(3.0, 4.4, 20) + np.random.uniform(-0.015, 0.015, 20)
for ct in np.concatenate([click_times_l1, click_times_l2]):
    add_click(audio, ct, gain=0.22)
add_bell(audio, 4.55, gain=0.25)

# 2. Phase 2 (7.0s - 11.0s): Philosophical Tone & Heartbeat
# Heartbeat / clock pulses at 7.2, 8.0, 8.8, 9.6, 10.4
for ht in [7.2, 8.0, 8.8, 9.6, 10.4]:
    idx = int(ht * sr)
    hlen = int(0.12 * sr)
    htt = np.linspace(0, 0.12, hlen)
    heartbeat = np.sin(2 * np.pi * 55 * htt) * np.exp(-htt * 35)
    audio[idx:idx+hlen] += heartbeat * 0.35

# Soft piano/synth tone at 7.0s
pt_len = int(3.5 * sr)
pt = np.linspace(0, 3.5, pt_len)
p_idx = int(7.0 * sr)
piano = (np.sin(2 * np.pi * 220 * pt) * 0.5 + np.sin(2 * np.pi * 440 * pt) * 0.3) * np.exp(-pt * 1.2)
audio[p_idx:p_idx+pt_len] += piano * 0.22

# 3. Phase 3 (11.0s - 18.0s): Cinematic Sub-Bass Impact Boom at 11.0s!
bass_start = int(11.0 * sr)
bass_len = int(4.5 * sr)
bt = np.linspace(0, 4.5, bass_len)
f_sweep = 140 * np.exp(-bt * 1.6) + 30
phase = 2 * np.pi * np.cumsum(f_sweep) / sr
impact_noise = np.random.uniform(-1, 1, int(0.22 * sr)) * np.exp(-np.linspace(0, 0.22, int(0.22 * sr)) * 30)
audio[bass_start:bass_start+int(0.22 * sr)] += impact_noise * 0.42
audio[bass_start:bass_start+bass_len] += np.sin(phase) * np.exp(-bt * 0.75) * 0.72

# 4. Glorious Orchestral Chord Swell (11.1s to 17.6s)
chord_start = int(11.1 * sr)
chord_len = int(6.6 * sr)
ct = np.linspace(0, 6.6, chord_len)
env = np.zeros_like(ct)
rise = int(2.4 * sr)
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
audio[chord_start:chord_start+chord_len] += chord * 0.58

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

print(f"Generated 18.0s master typewriter audio track: {out_wav}")
