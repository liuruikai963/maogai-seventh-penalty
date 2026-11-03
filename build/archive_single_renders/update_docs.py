# -*- coding: utf-8 -*-
"""
Script: update_docs.py
Author: 柳锐凯 (Liu Ruikai)
Description: Updates ASSET_MANIFEST.md and WORK_LOG.md with latest Shot 10B, Act 2 progress, and master concat milestones.
"""

import os

# Update ASSET_MANIFEST.md
manifest_path = "assets/ASSET_MANIFEST.md"
with open(manifest_path, "r", encoding="utf-8") as f:
    text = f.read()

# Normalize CRLF
text = text.replace("\r\n", "\n")

old_tree = """├── dist/                                       # 【最终成品输出库】
    ├── shots/                                  # 各单镜头终稿（已混音与压制中文字幕）
    │   ├── shot_01_final.mp4                   [FINAL] (10.03s, 陆远双屏工位自述，剥离原生错音+广播级青年配音)
    │   ├── shot_02a_final.mp4                  [FINAL] (10.03s, 老刘正面中景自述，剥离原生错音+沧桑配音+纯暴雨拟音)
    │   ├── shot_02b_final.mp4                  [FINAL] (10.01s, 老刘涉水狂奔动作，带雨夜破浪字幕与搏命呐喊配音)
    │   ├── shot_03_final.mp4                   [FINAL] (10.01s, 系统机械音超时红屏)
    │   └── shot_05_final.mp4                   [FINAL] (7.00s, 终极弹窗封号与系统机械声)
    ├── acts/                                   # 各幕完整连贯大片
    │   └── act1_complete_full_cut.mp4          [FINAL] (47.08s, 第一幕五连镜全镜头无缝连贯终成片！)
    └── final_film/                             # 全片 5~7 分钟终极大成片（待全片完成拼接）"""

new_tree = """├── dist/                                       # 【最终成品输出库】
    ├── shots/                                  # 各单镜头终稿（已混音与压制中文字幕）
    │   ├── shot_01_final.mp4                   [FINAL] (10.03s, 陆远双屏工位自述，剥离原生错音+广播级青年配音)
    │   ├── shot_02a_final.mp4                  [FINAL] (10.03s, 老刘正面中景自述，剥离原生错音+沧桑配音+纯暴雨拟音)
    │   ├── shot_02b_final.mp4                  [FINAL] (10.01s, 老刘涉水狂奔动作，带雨夜破浪字幕与搏命呐喊配音)
    │   ├── shot_03_final.mp4                   [FINAL] (10.01s, 系统机械音超时红屏)
    │   ├── shot_05_final.mp4                   [FINAL] (7.00s, 终极弹窗封号与系统机械声)
    │   ├── shot_06_final.mp4                   [FINAL] (10.03s, 清晨服务站老刘自述与叹息)
    │   ├── shot_07_final.mp4                   [FINAL] (10.03s, 陆远走近台阶俯身搀扶问候)
    │   ├── shot_08_full_20s.mp4                [FINAL] (20.06s, 送餐目击+破门救人打120守候全高潮)
    │   ├── shot_09_full_20s.mp4                [FINAL] (20.03s, 急救飞奔送医+急诊门前超时扣罚)
    │   ├── shot_10a_final.mp4                  [FINAL] (10.03s, 台阶现实回魂扶肩对白承诺+晨光冲刺飞奔工位)
    │   └── shot_10b_final.mp4                  [FINAL] (10.03s, 工位大模型报错强拦截+算得出效率算不出人性善意)
    ├── acts/                                   # 各幕完整连贯大片
    │   ├── act1_complete_full_cut.mp4          [FINAL] (47.08s, 第一幕五连镜全镜头无缝连贯终成片！)
    │   ├── act2_progress_cut.mp4               [PROGRESS] (80.20s, 第二幕 Shot 06 ~ 10B 连贯成片)
    │   └── current_progress_act1_to_act2_full.mp4 [MASTER] (127.36s / 2分07秒, 第一幕 + 第二幕目前已完成全量大成片！)
    ├── archive/                                # 历史中间版本与废弃测试切片
    └── final_film/                             # 全片 5~7 分钟终极大成片（待全片完成拼接）"""

old_10b = """| **Shot 10B** | 第二幕·工位申诉与大模型报错拦截 | ✅ 全新大模型双图 (`shot_10b1_ai_large_model_workstation.jpg`, `shot_10b2_ai_neural_error_rejected.jpg`) | 待生成 (Prompt已就绪) | 待合成 | `[PROMPTS_READY]` 10.0s，双屏大模型监控系统 ➡ 自然语言Prompt申诉 ➡ 屏幕爆红报错【语义对齐失败：未在预训练特征库中检索到实体【见义勇为】】 ➡ 拒绝人工覆写 |"""
new_10b = """| **Shot 10B** | 第二幕·工位申诉与大模型报错拦截 | ✅ 全新大模型双图 (`shot_10b1_ai_large_model_workstation.jpg`, `shot_10b2_ai_neural_error_rejected.jpg`) | ✅ 已入库 (`shot_10b_ai_large_model_error.mp4`) | ✅ `shot_10b_final.mp4` | `[FINAL]` 10.03s，双曲面屏AI大模型系统 ➡ 输入覆写Prompt ➡ 屏幕爆红报错【语义对齐失败·拒绝人工覆写】 ➡ 陆远震撼自语“算得出效率算不出人性的善意”，压制电影级字幕 |"""

if old_tree in text:
    text = text.replace(old_tree, new_tree)
    print("Replaced directory tree in ASSET_MANIFEST.md")
else:
    print("Warning: old_tree not found in ASSET_MANIFEST.md")

if old_10b in text:
    text = text.replace(old_10b, new_10b)
    print("Replaced Shot 10B in ASSET_MANIFEST.md")
else:
    print("Warning: old_10b not found in ASSET_MANIFEST.md")

with open(manifest_path, "w", encoding="utf-8") as f:
    f.write(text)

# Update WORK_LOG.md
worklog_path = "docs/WORK_LOG.md"
with open(worklog_path, "r", encoding="utf-8") as f:
    wlog = f.read()

new_log_entry = """
  * **00:30 - 00:46 | 镜头 10B（工位大模型报错强拦截）入库与字幕压制交付、工作区目录分层大重构、第一幕与第二幕目前进度全量串联大成片交付**：
    * **落实大模型人工智能核心意象**：针对导演（用户）“强调大模型算法人工智能，修改的是图片不是内容”的核心指导，全面重构 Shot 10B 关键帧原图，深度植入 Transformer 注意力热力图、3D 拓扑神经网络图、损失收敛曲线及猩红拒绝强警告 HUD（`OVERRIDE REJECTED: ALIGNMENT FAILURE`）；
    * **生肉视频生成与入库**：用户生成视频 `assets/videos/raw_inputs/gemini_generated_video_e9644b3b.mp4` 成功入库，规范归档为 `assets/videos/raw_inputs/shot_10b_ai_large_model_error.mp4`（10.03s，1280x720，24fps）；
    * **底纹遮罩与双层电影字幕精准压制**：针对 AI 视频自带的模糊乱字，创新采用标准半透明黑色底框滤镜完美遮盖，并在 `[4.5s - 6.8s]` 压制系统报错字幕《【大模型报错：语义对齐失败·拒绝人工覆写】》，在 `[7.0s - 9.8s]` 压制陆远震撼台词《“未定义特征实体……大模型算得出效率，却算不出人性的善意！”》，导出终成片 [shot_10b_final.mp4](file:///d:/study/course/maogai/homework/dist/shots/shot_10b_final.mp4)（10.03s）；
    * **工程化工作区目录分层大重构**：
      - 清理根目录残留的临时音频测试碎文件；
      - 建立 `dist/archive/`，将历史中间渲染与未加介绍版本安全移入归档库；
      - 规范 `assets/videos/archive_scrapped/`，彻底理顺 raw_inputs 与历史废稿层级；
    * **全量连贯串联大成片成功生成并交付**：
      - 编写执行 `build/concat_current_progress_full.py`；
      - 成功生成第二幕当前进度连贯大片 [act2_progress_cut.mp4](file:///d:/study/course/maogai/homework/dist/acts/act2_progress_cut.mp4)（80.20s，Shot 06 ~ Shot 10B）；
      - 成功生成第一幕与第二幕全量大成片 [current_progress_act1_to_act2_full.mp4](file:///d:/study/course/maogai/homework/dist/acts/current_progress_act1_to_act2_full.mp4)（127.36s / 2分07秒），全流程丝滑咬合、视听语言一气呵成；
      - 全量成果同步归档至会话交互工件区供随时回放验收。
"""

wlog = wlog.rstrip() + "\n" + new_log_entry

with open(worklog_path, "w", encoding="utf-8") as f:
    f.write(wlog)

print("Documentation updated successfully!")
