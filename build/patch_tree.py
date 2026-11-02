# -*- coding: utf-8 -*-
with open("assets/ASSET_MANIFEST.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if "└── dist/" in line:
        new_lines.append(line)
        new_lines.append("    ├── shots/                                  # 各单镜头终稿（已混音与压制中文字幕）\n")
        new_lines.append("    │   ├── shot_01_final.mp4                   [FINAL] (10.03s, 陆远双屏工位自述，剥离原生错音+广播级青年配音)\n")
        new_lines.append("    │   ├── shot_02a_final.mp4                  [FINAL] (10.03s, 老刘正面中景自述，剥离原生错音+沧桑配音+纯暴雨拟音)\n")
        new_lines.append("    │   ├── shot_02b_final.mp4                  [FINAL] (10.01s, 老刘涉水狂奔动作，带雨夜破浪字幕与搏命呐喊配音)\n")
        new_lines.append("    │   ├── shot_03_final.mp4                   [FINAL] (10.01s, 系统机械音超时红屏)\n")
        new_lines.append("    │   ├── shot_05_final.mp4                   [FINAL] (7.00s, 终极弹窗封号与系统机械声)\n")
        new_lines.append("    │   ├── shot_06_final.mp4                   [FINAL] (10.03s, 清晨服务站老刘自述与叹息)\n")
        new_lines.append("    │   ├── shot_07_final.mp4                   [FINAL] (10.03s, 陆远走近台阶俯身搀扶问候)\n")
        new_lines.append("    │   ├── shot_08_full_20s.mp4                [FINAL] (20.06s, 送餐目击+破门救人打120守候全高潮)\n")
        new_lines.append("    │   ├── shot_09_full_20s.mp4                [FINAL] (20.03s, 急救飞奔送医+急诊门前超时扣罚)\n")
        new_lines.append("    │   ├── shot_10a_final.mp4                  [FINAL] (10.03s, 台阶现实回魂扶肩对白承诺+晨光冲刺飞奔工位)\n")
        new_lines.append("    │   └── shot_10b_final.mp4                  [FINAL] (10.03s, 工位大模型报错强拦截+算得出效率算不出人性善意)\n")
        new_lines.append("    ├── acts/                                   # 各幕完整连贯大片\n")
        new_lines.append("    │   ├── act1_complete_full_cut.mp4          [FINAL] (47.08s, 第一幕五连镜全镜头无缝连贯终成片！)\n")
        new_lines.append("    │   ├── act2_progress_cut.mp4               [PROGRESS] (80.20s, 第二幕 Shot 06 ~ 10B 连贯成片)\n")
        new_lines.append("    │   └── current_progress_act1_to_act2_full.mp4 [MASTER] (127.36s / 2分07秒, 第一幕 + 第二幕目前已完成全量大成片！)\n")
        new_lines.append("    ├── archive/                                # 历史中间版本与废弃测试切片\n")
        new_lines.append("    └── final_film/                             # 全片 5~7 分钟终极大成片（待全片完成拼接）\n")
        skip = True
    elif skip and line.strip() == "```":
        skip = False
        new_lines.append(line)
    elif not skip:
        new_lines.append(line)

with open("assets/ASSET_MANIFEST.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("Tree updated successfully!")
