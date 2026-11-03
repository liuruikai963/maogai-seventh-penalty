# -*- coding: utf-8 -*-
with open("assets/ASSET_MANIFEST.md", "r", encoding="utf-8") as f:
    text = f.read()

# Add Shot 02C entry to tree and table
old_tree_sub = "│   ├── shot_02b_final.mp4                  [FINAL] (10.01s, 老刘涉水狂奔动作，带雨夜破浪字幕与搏命呐喊配音)\n"
new_tree_sub = (
    "│   ├── shot_02b_final.mp4                  [FINAL] (10.01s, 老刘涉水狂奔动作，带雨夜破浪字幕与搏命呐喊配音)\n"
    "│   ├── shot_02c_final.mp4                  [FINAL] (10.03s, 桥梁镜头：老刘沧桑独白，雨夜极速升空宏观全景转晨曦破晓下推，电影双层字幕)\n"
)

if old_tree_sub in text:
    text = text.replace(old_tree_sub, new_tree_sub)

old_table_sub = "| **Shot 02B** | 第一幕·雨中送单·老刘深夜绝地飞驰（涉水狂奔动作） | ✅ 已完成 | ✅ 已入库 (`shot_02b_lao_liu_scooter_wading.mp4`) | ✅ `shot_02b_final.mp4` | `[FINAL]` 10.01s，动感低机位涉水，暴雨破浪动作衔接，逆风呐喊“绝不能超时” |\n"
new_table_sub = (
    "| **Shot 02B** | 第一幕·雨中送单·老刘深夜绝地飞驰（涉水狂奔动作） | ✅ 已完成 | ✅ 已入库 (`shot_02b_lao_liu_scooter_wading.mp4`) | ✅ `shot_02b_final.mp4` | `[FINAL]` 10.01s，动感低机位涉水，暴雨破浪动作衔接，逆风呐喊“绝不能超时” |\n"
    "| **Shot 02C** | 第一幕·时空过渡桥梁·雨夜都市远景至晨光破晓 | ✅ 双图已就绪 (`shot_02c1.jpg`, `shot_02c2.jpg`) | ✅ 已入库 (`shot_02c_macro_city_storm_to_dawn.mp4`) | ✅ `shot_02c_final.mp4` | `[FINAL]` 10.03s，从涉水骑行顺势拉升升空，展现实拍级雨夜都市全景，延时转入晨光破晓万道金光，老刘沧桑独白“那一晚的雨太大了……可那一单，终究还是超时了”，无缝下俯交接 Shot 06 |\n"
)

if old_table_sub in text:
    text = text.replace(old_table_sub, new_table_sub)

with open("assets/ASSET_MANIFEST.md", "w", encoding="utf-8") as f:
    f.write(text)

# Update WORK_LOG.md
with open("docs/WORK_LOG.md", "r", encoding="utf-8") as f:
    wlog = f.read()

new_log = """
  * **10:10 - 10:35 | 导演核心构思落地：新增 Shot 02C（雨夜都市全景 ➡ 晨光破晓转场）、双层电影字幕压制、全量插入连贯母带（整整 2 分钟整）交付**：
    * **采纳导演神级转场构思**：针对暴雨狂奔（Shot 02B）直切清晨台阶啃馒头（Shot 06）过于突兀的问题，采纳导演指导，增设时空过渡桥梁镜头 **Shot 02C**；
    * **视觉三阶段丝滑演进**：老刘雨夜涉水骑车（图一） ➡ 摄像机火箭式极速升空拉远，俯瞰庞大雨夜现代科技都市与雷云闪电（图二） ➡ 暴雨退去，朝霞撕裂夜空，万道金色晨光（丁达尔效应）喷薄照亮湿漉漉的城市建筑与地面（图三） ➡ 镜头平稳下俯（Tilt Down）顺滑切入 Shot 06 台阶；
    * **老刘专属第一人称自述与字幕压制**：严格遵照导演指示采用老刘第一人称疲惫沧桑的原声独白，在 `[0.6s - 3.8s]` 压制《“那一晚的雨太大了……我拼了命往前赶……”》，在 `[4.3s - 7.5s]` 压制《“可那一单，终究还是超时了……”》，导出终成片 [shot_02c_final.mp4](file:///d:/study/course/maogai/homework/dist/shots/shot_02c_final.mp4)（10.03s）；
    * **全量重新串联大成片**：将 Shot 02C 完美插入 Shot 02B 与 Shot 06 之间，导出最新完整大母带 [current_progress_act1_to_act2_full.mp4](file:///d:/study/course/maogai/homework/dist/acts/current_progress_act1_to_act2_full.mp4)（时长刚好整整 **2 分 00 秒 / 120.35s**），视听衔接浑然天成、史诗级戏剧张力拉满！
"""

wlog = wlog.rstrip() + "\n" + new_log
with open("docs/WORK_LOG.md", "w", encoding="utf-8") as f:
    f.write(wlog)

print("Updated ASSET_MANIFEST and WORK_LOG successfully!")
