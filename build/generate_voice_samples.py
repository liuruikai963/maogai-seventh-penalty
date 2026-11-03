# -*- coding: utf-8 -*-
"""
Script: generate_voice_samples.py
Author: 柳锐凯 (Liu Ruikai)
Description:
  Generates audition samples for the 5 key characters:
  1. 陆远 (Lu Yuan): 23yo AI architect, clear youthful voice, righteous and calm.
  2. 老刘 (Lao Liu): 48yo delivery rider, weathered, exhausted, warm-hearted middle-aged uncle.
  3. 王总 (Director Wang): 45yo corporate tech VP, authoritative, cold efficiency, then panicked.
  4. 家属 (Hospital Daughter): 40yo middle-aged female, emotional, tearful, grateful appeal.
  5. 官方新闻发言人 (Official Anchor): dignified, authoritative broadcast cadence.
"""

import asyncio
import os
import shutil
import edge_tts
import imageio_ffmpeg
import subprocess

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
out_dir = "dist/audio_samples"
os.makedirs(out_dir, exist_ok=True)
art_dir = r"C:\Users\27277\.gemini\antigravity\brain\f5b14212-99d2-460d-9706-e55469254373"

samples = [
    {
        "id": "01_luyuan",
        "role": "陆远（23岁算法架构师·清澈沉稳青年声）",
        "voice": "zh-CN-YunxiNeural",
        "pitch": "+0Hz",
        "rate": "+2%",
        "intro": "【陆远试音】：我叫陆远，23岁，大模型调度算法架构师。王总，骑手是为了救人，大模型为什么不能撤销？！算法要的是确定性，但绝不能丢掉人的温度！"
    },
    {
        "id": "02_laoliu",
        "role": "老刘（48岁外卖骑手·沙哑沧桑大叔声）",
        "voice": "zh-CN-YunjianNeural",
        "pitch": "-14Hz",
        "rate": "-8%",
        "intro": "【老刘试音】：那一晚的雨太大了……我拼了命往前赶……可那一单，终究还是超时了……大兄弟，我就想把账号申诉回来，我孙女这个月的药费，全指望送外卖啊……"
    },
    {
        "id": "03_director_wang",
        "role": "王总（45岁平台高管·冷酷傲慢后破防）",
        "voice": "zh-CN-YunyangNeural",
        "pitch": "-5Hz",
        "rate": "+5%",
        "intro": "【王总试音】：陆远，算法要的是确定性和效率，不是同情心！……什么？！联合调查组已经进驻了？！限你们二十四小时内，把突发救助和免责规则给我改出来！"
    },
    {
        "id": "04_daughter",
        "role": "家属（被救老人家属·哽咽真诚中年女性声）",
        "voice": "zh-CN-XiaoxiaoNeural",
        "pitch": "+3Hz",
        "rate": "-4%",
        "intro": "【家属试音】：是他救了我父亲！昨晚我父亲突发心梗，要不是这位外卖师傅破门做心肺复苏又打120送医，人就没了！救命恩人不能流血又流泪啊，大家帮帮我们找到他！"
    },
    {
        "id": "05_official_news",
        "role": "官方新闻发言人（权威正气国级播音腔）",
        "voice": "zh-CN-YunyangNeural",
        "pitch": "+0Hz",
        "rate": "+0%",
        "intro": "【权威通报试音】：权威发布！互联网平台绝不是野蛮生长的法外之地。科技发展必须坚守以人民为中心的发展思想，算法绝不能凌驾于劳动者的生命健康与社会公义之上！"
    }
]

async def gen_all():
    file_list = []
    for s in samples:
        path = os.path.join(out_dir, f"{s['id']}.mp3")
        c = edge_tts.Communicate(s["intro"], s["voice"], pitch=s["pitch"], rate=s["rate"])
        await c.save(path)
        shutil.copy2(path, os.path.join(art_dir, f"{s['id']}.mp3"))
        file_list.append(path)
        print(f"Generated: {s['role']} -> {path}")

    # Concatenate into one continuous showcase mp3
    concat_txt = "build/concat_voices.txt"
    with open(concat_txt, "w", encoding="utf-8") as f:
        for p in file_list:
            f.write(f"file '{os.path.abspath(p).replace('\\', '/')}'\n")

    showcase_path = os.path.join(out_dir, "00_five_characters_voice_showcase.mp3")
    subprocess.run([
        ffmpeg, "-y", "-f", "concat", "-safe", "0", "-i", concat_txt, "-c", "copy", showcase_path
    ], check=True)
    shutil.copy2(showcase_path, os.path.join(art_dir, "00_five_characters_voice_showcase.mp3"))
    print(f"Showcase generated: {showcase_path}")

if __name__ == "__main__":
    asyncio.run(gen_all())
