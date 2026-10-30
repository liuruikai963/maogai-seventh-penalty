# 《第七张罚单》微电影资产总表与制作进度清单

> **项目名称**：《第七张罚单》（毛概微电影实践）  
> **制作人员**：柳锐凯、芮凯  
> **视频规格**：16:9 横屏 1080P · 纯 AIGC 动态微电影（Gemini Veo 原生声画同步）

---

## 📊 资产归档规范目录结构

```text
homework/
├── docs/                               # 策划与剧作方案
│   ├── plot_concept.md                 # 核心五幕剧情构思案（起承转激合）
│   └── STYLE_CONSISTENCY_RULES.md      # 画风绝对统一与微表情铁律
├── scripts/                            # 脚本与 AI 生产提示词
│   └── ai_video_production_script.md  # 全片 23 镜头标准中英文 Prompt 与台词总表
├── assets/                             # 原创素材资产库
│   ├── images/                         # 关键帧 1080P 高清原图（Antigravity 生成）
│   ├── audio/                          # 角色对白与备用配音
│   └── videos/                         # 真实 AI 动态物理视频片段（Gemini Veo 生成）
│       ├── shot_01_macro_city_to_lu_yuan_monologue.mp4 # 镜头 01：大场景穿透切入陆远正脸独白（已完成！）
│       └── shot_02_lao_liu_scooter_rain.mp4            # 镜头 02：老刘暴雨破浪行车动态视频（已完成！）
├── build/                              # 渲染与流水线自动化脚本
│   └── render_act1_preview.py          # 音画拼接剪辑代码
└── dist/                               # 最终成片输出目录
```

---

## 🎬 分镜头制作进度跟踪表

| 镜头编号 | 场景名称 | 关键帧原图 | 真实动态视频 (Veo) | 归档文件名 |
| :---: | :--- | :---: | :---: | :--- |
| **Shot 01** | 雨夜超级都市穿透切入陆远正脸独白 | ✅ 已完成 | **✅ 已完成 (Veo原生带声画字幕)** | `assets/videos/shot_01_macro_city_to_lu_yuan_monologue.mp4` |
| **Shot 02** | 老刘暴雨涉水破浪前行 | ✅ 已完成 | **✅ 已完成 (Veo物理流体)** | `assets/videos/shot_02_lao_liu_scooter_rain.mp4` |
| **Shot 03** | 手机红色倒计时与罚单特写 | ✅ 已完成 | **✅ 已完成 (Veo物理倒计时爆闪)** | `assets/videos/shot_03_phone_countdown.mp4` |
| **Shot 04** | 恒温机房陆远冷峻调试算法 | ✅ 已完成 | 已整合入 Shot 01 | `assets/images/shot_04.jpg` |
| **Shot 05** | 系统终极风控红色封号弹窗 | ✅ 已完成 | 待生成 | `assets/images/shot_05.jpg` |
| **Shot 06** | 清晨服务站老刘啃干馒头 | ✅ 已完成 | 待生成 | `assets/images/shot_06.jpg` |
| **Shot 07** | 老刘满是老茧皲裂的双手特写 | ✅ 已完成 | 待生成 | `assets/images/shot_07.jpg` |
| **Shot 08** | 监控回放·老刘暴雨夜破门救心梗老人 | ✅ 已完成 (全新破门急救版) | 待生成 | `assets/images/shot_08.jpg` |
| **Shot 09** | 代码报错：未定义实体【见义勇为】 | ✅ 已完成 | 待生成 | `assets/images/shot_09.jpg` |
| **Shot 10** | 王总在办公室给陆远递咖啡做规训 | ✅ 已完成 | 待生成 | `assets/images/shot_10.jpg` |
| **Shot 11** | 老人家属实名致谢寻人短视频 | ✅ 已完成 | 待生成 | `assets/images/shot_11.jpg` |
| **Shot 12** | 全网舆论热搜与网友怒评弹幕 | ✅ 已完成 | 待生成 | `assets/images/shot_12.jpg` |
| **Shot 13** | 国家市场监管与人社部联合通报直播 | ✅ 已完成 | 待生成 | `assets/images/shot_13.jpg` |
| **Shot 14** | 王总满头冷汗冲进机房强令整改 | ✅ 已完成 | 待生成 | `assets/images/shot_14.jpg` |
| **Shot 15** | 陆远拍出重构方案沉着掌控大局 | 待生成 | 待生成 | `assets/images/shot_15.jpg` |
| **Shot 16** | 研发团队通宵敲代码重构底层算法 | 待生成 | 待生成 | `assets/images/shot_16.jpg` |
| **Shot 17** | 清晨破晓第一缕阳光洒在机房屏幕 | 待生成 | 待生成 | `assets/images/shot_17.jpg` |
| **Shot 18** | 老刘在街头落寞撕下外卖箱贴纸 | 待生成 | 待生成 | `assets/images/shot_18.jpg` |
| **Shot 19** | 手机弹出金色撤销罚单与救助通报 | 待生成 | 待生成 | `assets/images/shot_19.jpg` |
| **Shot 20** | 老刘通红眼眶露出踏实灿烂笑容 | 待生成 | 待生成 | `assets/images/shot_20.jpg` |
| **Shot 21** | 清晨斑马线陆远与老刘隔空相望致意 | 待生成 | 待生成 | `assets/images/shot_21.jpg` |
| **Shot 22** | 宏大俯瞰·老刘与劳动者迎着朝阳长征 | 待生成 | 待生成 | `assets/images/shot_22.jpg` |
| **Shot 23** | 黑底金字片尾·演职员表（柳锐凯、芮凯） | ✅ 已完成 | 待生成 | `assets/images/shot_23.jpg` |
