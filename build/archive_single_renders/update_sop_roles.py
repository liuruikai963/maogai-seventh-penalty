# -*- coding: utf-8 -*-
with open('docs/TEAM_COLLABORATION_SOP.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the table
target_header = "## 📌 一、 核心分工划分表"
next_header = "## 📂 二、 资产分类规范"

new_section = """## 📌 一、 核心分工划分表（最新任务分工版）

> **当前状态**：前三幕（Shot 01 ~ Shot 14，共 16 个镜头，成片时长 3分00秒）已由柳锐凯全量渲染并通过质量验收。现转入新一轮深化制作与呈现分工：

| 主创成员 | 核心负责模块 | 涵盖任务与具体内容 | 交付产物与标准 |
| :--- | :--- | :--- | :--- |
| **柳锐凯**<br>（统筹 / 视效包装 / 理论升华） | **1. 震撼微电影新片头**<br>**2. 结束放映思政总结**<br>**3. AI 制作幕后花絮** | • **全新概念片头（10-15s）**：设计电影级概念片头，呈现雨夜冰冷算法数字矩阵与片名《第七张罚单》的悬念震撼碰撞。<br>• **放映结束总结（30-40s）**：结合毛概课程核心理论（“以人民为中心”、“算法向善”、“新质生产力不能异化劳动者尊严”），撰写并呈现掷地有声的答辩升华总结与结语。<br>• **幕后制作花絮（45-60s）**：精选从提示词调试、离谱AI废稿对比、音画解耦到团队协同的趣味幕后纪录，全方位展现实践成果与探索历程。 | • `dist/acts/intro_title_sequence.mp4`<br>• `dist/acts/outro_ideological_summary.mp4`<br>• `dist/acts/behind_the_scenes_featurette.mp4` |
| **芮凯**<br>（叙事打磨 / 视听一致性重构） | **1. 前情整体情节衔接**<br>**2. 全局声音一致性与情绪重构** | • **前情剧情衔接与节奏润色**：基于已完成的 Shot 01~14（3分00秒前三幕），优化各镜头之间的转场视听剪辑（暴雨转晴晨、办公楼转病房），使节奏更加紧凑动人。<br>• **解决全片语音不一致问题**：针对目前不同镜头音频音色漂移、缺乏情绪语气的问题，建立全片统一的人声声线库（陆远、老刘、王总等），使用情绪克隆/高表现力人声完成专业级音画重组。 | • `dist/acts/act1_act3_seamless_v2.mp4`（衔接精剪版）<br>• `assets/audio/voiceovers/master_consistent/`（统一声线库） |

---
"""

if target_header in content and next_header in content:
    idx1 = content.index(target_header)
    idx2 = content.index(next_header)
    content = content[:idx1] + new_section + content[idx2:]
    with open('docs/TEAM_COLLABORATION_SOP.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Updated TEAM_COLLABORATION_SOP.md")
else:
    print("Failed to locate headers")
