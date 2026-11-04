# -*- coding: utf-8 -*-
import numpy as np
import wave, struct, os, subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

sr = 48000
duration = 12.0
total_samples = int(sr * duration)
t = np.linspace(0, duration, total_samples, endpoint=False)

audio = np.zeros(total_samples, dtype=np.float32)

# Helper to create a single mechanical typewriter click
def add_click(arr, at_time, gain=0.25):
    idx = int(at_time * sr)
    click_len = int(0.025 * sr)
    ct = np.linspace(0, 0.025, click_len)
    # Click impulse + resonant wood/metal sound
    noise = np.random.uniform(-1, 1, click_len) * np.exp(-ct * 300)
    ping = np.sin(2 * np.pi * 2400 * ct) * np.exp(-ct * 150)
    click = (noise * 0.7 + ping * 0.3) * gain
    arr[idx:idx+click_len] += click

# Helper for return ding / carriage bell
def add_bell(arr, at_time, gain=0.3):
    idx = int(at_time * sr)
    bell_len = int(0.6 * sr)
    bt = np.linspace(0, 0.6, bell_len)
    bell = (np.sin(2 * np.pi * 1760 * bt) * 0.7 + np.sin(2 * np.pi * 3520 * bt) * 0.3) * np.exp(-bt * 8)
    arr[idx:idx+bell_len] += bell * gain

# 1. Typewriter clicks for Phase 1 (0.4s to 2.8s)
# ~20 clicks distributed over text appearance
click_times = np.linspace(0.4, 2.7, 28) + np.random.uniform(-0.015, 0.015, 28)
for ct in click_times:
    add_click(audio, ct, gain=0.20)
add_bell(audio, 2.85, gain=0.22)

# 2. Philosophical Tone & Heartbeat for Phase 2 (3.4s to 6.2s)
# Low heartbeat / clock pulse at 3.5, 4.3, 5.1, 5.9
for ht in [3.5, 4.3, 5.1, 5.9]:
    idx = int(ht * sr)
    hlen = int(0.12 * sr)
    htt = np.linspace(0, 0.12, hlen)
    heartbeat = np.sin(2 * np.pi * 55 * htt) * np.exp(-htt * 35)
    audio[idx:idx+hlen] += heartbeat * 0.35

# Soft piano/synth tone at 3.5s (A minor / C major root)
pt_len = int(2.5 * sr)
pt = np.linspace(0, 2.5, pt_len)
p_idx = int(3.5 * sr)
piano = (np.sin(2 * np.pi * 220 * pt) * 0.5 + np.sin(2 * np.pi * 440 * pt) * 0.3) * np.exp(-pt * 1.5)
audio[p_idx:p_idx+pt_len] += piano * 0.20

# 3. Cinematic Sub-Bass Impact Boom at 6.4s (Poster reveal!)
bass_start = int(6.4 * sr)
bass_len = int(3.5 * sr)
bt = np.linspace(0, 3.5, bass_len)
# frequency sweep 130Hz -> 32Hz
f_sweep = 130 * np.exp(-bt * 1.8) + 32
phase = 2 * np.pi * np.cumsum(f_sweep) / sr
impact_noise = np.random.uniform(-1, 1, int(0.2 * sr)) * np.exp(-np.linspace(0, 0.2, int(0.2 * sr)) * 30)
audio[bass_start:bass_start+int(0.2 * sr)] += impact_noise * 0.4
audio[bass_start:bass_start+bass_len] += np.sin(phase) * np.exp(-bt * 0.9) * 0.65

# 4. Glorious Orchestral Chord Swell (6.5s to 11.5s)
chord_start = int(6.5 * sr)
chord_len = int(5.3 * sr)
ct = np.linspace(0, 5.3, chord_len)
env = np.zeros_like(ct)
rise = int(1.8 * sr)
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

print(f"Generated master typewriter audio track: {out_wav}")
