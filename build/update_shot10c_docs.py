# -*- coding: utf-8 -*-
with open("assets/ASSET_MANIFEST.md", "r", encoding="utf-8") as f:
    text = f.read()

old_tree_10c = "│   └── shot_10b_final.mp4                  [FINAL] (10.03s, 工位大模型报错强拦截+算得出效率算不出人性善意)\n"
new_tree_10c = (
    "│   ├── shot_10b_final.mp4                  [FINAL] (10.03s, 工位大模型报错强拦截+算得出效率算不出人性善意)\n"
    "│   └── shot_10c_final.mp4                  [FINAL] (10.03s, 总监办公室对质高潮：陆远质问大模型为何不能撤销+王总冷笑规训“算法要的是效率不是同情心”，电影双层字幕)\n"
)

if old_tree_10c in text:
    text = text.replace(old_tree_10c, new_tree_10c)

old_table_10c = "| **Shot 10C** | 第二幕·总监办公室理论与资本规训 | ✅ 双图连贯 (`shot_10c1_luyuan_enters_wang_office.jpg`, `shot_10c2_wang_hegemony_coffee.jpg`) | 待生成 (Prompt已就绪) | 待合成 | `[PROMPTS_READY]` 10.0s，陆远拿平板推门质问 ➡ 王总端咖啡冷笑规训“算法不需要同情心” ➡ 阶级矛盾激化 |\n"
new_table_10c = "| **Shot 10C** | 第二幕·总监办公室理论与资本规训 | ✅ 双图连贯 (`shot_10c1.jpg`, `shot_10c2.jpg`) | ✅ 已入库 (`shot_10c_wang_office_confrontation.mp4`) | ✅ `shot_10c_final.mp4` | `[FINAL]` 10.03s，推门质问“骑手是为了救人，大模型为什么不能撤销” ➡ 王总端咖啡冷笑“算法要的是效率不是同情心” ➡ 阶级对撞定格，第二幕圆满杀青！ |\n"

if old_table_10c in text:
    text = text.replace(old_table_10c, new_table_10c)

with open("assets/ASSET_MANIFEST.md", "w", encoding="utf-8") as f:
    f.write(text)

# Update WORK_LOG.md
with open("docs/WORK_LOG.md", "r", encoding="utf-8") as f:
    wlog = f.read()

new_log = """
  * **10:45 - 10:58 | 镜头 10C（总监办公室正面理论对质）生肉入库、双层电影字幕压制、第二幕全剧宣告圆满杀青、第一幕+第二幕全量大成片（2分10秒）正式交付**：
    * **生肉视频素材入库**：用户生成视频 `assets/videos/raw_inputs/gemini_generated_video_c7571d15.mp4` 成功入库，规范归档为 `assets/videos/raw_inputs/shot_10c_wang_office_confrontation.mp4`（10.03s，1280x720，24fps，立体声）；
    * **戏剧冲突与阶级对撞核验**：陆远手持红光报错平板推门质问与王总背头西装端咖啡冷笑规训的表演极为生动传神，画风 100% 严密对齐新海诚写实动漫；
    * **电影级双层字幕精准压制**：在 `[0.6s - 4.2s]` 压制陆远台词《“王总，骑手是为了救人！大模型为什么不能撤销？！”》，在 `[4.8s - 9.0s]` 压制王总台词《“陆远，算法要的是确定性和效率，不是同情心！”》，导出终成片 [shot_10c_final.mp4](file:///d:/study/course/maogai/homework/dist/shots/shot_10c_final.mp4)（10.03s）；
    * **第二幕全幕完整连贯大片交付**：编写执行 `build/render_shot10c_and_concat_master.py`，串联 Shot 06 ～ Shot 10C，导出第二幕全幕成片 [act2_complete_full_cut.mp4](file:///d:/study/course/maogai/homework/dist/acts/act2_complete_full_cut.mp4)（时长 90.23 秒）；
    * **总进度完整母带升级交付（2分10秒）**：将第一幕至第二幕全部 11 个镜头（含 Shot 02C 宏观转场）无缝串联，导出最新全量大成片 [current_progress_act1_to_act2_full.mp4](file:///d:/study/course/maogai/homework/dist/acts/current_progress_act1_to_act2_full.mp4)（时长 2 分 10 秒 / 130.38s）；
    * **柳锐凯负责前半程（第一、二、三幕）第二幕全部镜头胜利收官！**
"""

wlog = wlog.rstrip() + "\n" + new_log
with open("docs/WORK_LOG.md", "w", encoding="utf-8") as f:
    f.write(wlog)

print("Updated ASSET_MANIFEST and WORK_LOG for Shot 10C!")
