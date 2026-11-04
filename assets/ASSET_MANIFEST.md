# 《算法之外》微电影资产总表与协作分工清单

> **项目名称**：《算法之外》（Beyond the Algorithm）  
> **微电影主旨**：以人民为中心 · 算法向善 · 新就业形态劳动者权益保障 · 青年科技工作者的新长征  
> **制作人员分工**：
> * **前半程制作人（第一、二、三幕：Shot 01 ～ 14）**：**柳锐凯**
> * **后半程制作人（第四、五幕：Shot 15 ～ 23）**：**芮凯**  
> **技术规格**：16:9 横屏（1280×720 / 1920×1080）、24fps、高质感动漫现实主义风格（Makoto Shinkai Anime Realism）

---

## 📂 资产目录与废稿保留结构规范

为确保视频素材与最终成品清晰分离，并**完整保留历史废稿与测试素材以备随时替换**，目录严格规划如下：

```text
homework/
├── assets/
│   ├── images/                                 # 1080P 概念关键帧原图库（.jpg）
│   ├── audio/                                  # 角色配音原声、音效与 BGM（.mp3）
│   │   ├── shot_01_luyuan_clean_vo.mp3         [ACTIVE] (陆远专业广播级无错配音，沉稳青年学者音)
│   │   ├── shot_02a_laoliu_clean_vo.mp3        [ACTIVE] (老刘专业广播级无错配音，48岁沧桑微喘中年音)
│   │   ├── shot_02b_laoliu_clean_vo.mp3        [ACTIVE] (老刘绝地狂奔涉水呐喊配音)
│   │   ├── shot_03_system_voice.mp3            [ACTIVE] (系统机械倒计时报警音)
│   │   └── shot_05_system_freeze.mp3           [ACTIVE] (系统风控永久冻结提示音)
│   └── videos/
│       ├── raw_inputs/                         # 【输入原始素材库】Gemini / Veo 生成的生肉视频片段
│       │   ├── shot_01_luyuan_office_monologue.mp4          [ACTIVE] (10.03s, 陆远工位学术自述与电光闪现)
│       │   ├── shot_02a_lao_liu_monologue.mp4               [ACTIVE] (10.03s, 老刘正面中景暴雨自述，48岁救孙女动机)
│       │   ├── shot_02b_lao_liu_scooter_wading.mp4          [ACTIVE] (10.01s, 老刘雨夜涉水绝地狂奔动作)
│       │   ├── shot_03_phone_countdown.mp4                  [ACTIVE] (10.01s, 手机倒计时归零报警)
│       │   └── shot_05_penalty_modal.mp4                    [ACTIVE] (10.03s, 弹窗封号模态框)
│       └── archive_scrapped/                   # 【废稿与备用素材库】包含历史版本、测试稿，做标签标记严禁删除！
│           ├── shot_01_macro_city_v1_pre_monologue_replace.mp4 [TAG: SCRAPPED_PRE_MONOLOGUE_REPLACE] (旧版雨夜宏观大远景测试素材)
│           ├── shot_02_vo_v1_pre_character_intro.mp4        [TAG: SCRAPPED_PRE_INTRO] (无自我介绍旧版配音)
│           ├── act1_opening_20s_v1_pre_shot03.mp4           [TAG: SCRAPPED_PRE_SHOT03] (仅前两镜旧连缀)
│           └── act1_seamless_30s_v1_pre_intro.mp4           [TAG: SCRAPPED_PRE_INTRO] (前三镜旧30秒无介绍版)
├── build/                                      # 自动化合成、音画对齐与压制脚本
│   ├── render_act1_preview.py                  # 旧版图片转视频预览脚本
│   ├── create_shot02_with_laoliu_vo_and_concat.py # 镜头 02 单独压制脚本
│   ├── render_shot03_and_concat_act1.py        # 镜头 03 压制脚本
│   ├── render_act1_full_with_shot05.py         # 第一幕历史合成脚本
│   ├── render_act1_with_new_monologue.py       # 第一幕全量 37.7s 连贯脚本
│   ├── render_shot02a_and_concat_act1.py       # 第一幕双镜头衔接历史脚本
│   └── render_act1_professional_dubbed_cut.py  # 【当前母带】第一幕 47.08s 剥离原生错音+广播级配音+纯净环境拟音终极大成片
└── dist/                                       # 【最终成品输出库】
    ├── shots/                                  # 各单镜头终稿（已混音与压制中文字幕）
    │   ├── shot_01_final.mp4                   [FINAL] (10.03s, 陆远双屏工位自述，剥离原生错音+广播级青年配音)
    │   ├── shot_02a_final.mp4                  [FINAL] (10.03s, 老刘正面中景自述，剥离原生错音+沧桑配音+纯暴雨拟音)
    │   ├── shot_02b_final.mp4                  [FINAL] (10.01s, 老刘涉水狂奔动作，带雨夜破浪字幕与搏命呐喊配音)
│   ├── shot_02c_final.mp4                  [FINAL] (10.03s, 桥梁镜头：老刘沧桑独白，雨夜极速升空宏观全景转晨曦破晓下推，电影双层字幕)
    │   ├── shot_03_final.mp4                   [FINAL] (10.01s, 系统机械音超时红屏)
    │   ├── shot_05_final.mp4                   [FINAL] (7.00s, 终极弹窗封号与系统机械声)
    │   ├── shot_06_final.mp4                   [FINAL] (10.03s, 清晨服务站老刘自述与叹息)
    │   ├── shot_07_final.mp4                   [FINAL] (10.03s, 陆远走近台阶俯身搀扶问候)
    │   ├── shot_08_full_20s.mp4                [FINAL] (20.06s, 送餐目击+破门救人打120守候全高潮)
    │   ├── shot_09_full_20s.mp4                [FINAL] (20.03s, 急救飞奔送医+急诊门前超时扣罚)
    │   ├── shot_10a_final.mp4                  [FINAL] (10.03s, 台阶现实回魂扶肩对白承诺+晨光冲刺飞奔工位)
    │   ├── shot_10b_final.mp4                  [FINAL] (10.03s, 工位大模型报错强拦截+算得出效率算不出人性善意)
│   └── shot_10c_final.mp4                  [FINAL] (10.03s, 总监办公室对质高潮：陆远质问大模型为何不能撤销+王总冷笑规训“算法要的是效率不是同情心”，电影双层字幕)
    ├── acts/                                   # 各幕完整连贯大片
    │   ├── act1_complete_full_cut.mp4          [FINAL] (47.08s, 第一幕五连镜全镜头无缝连贯终成片！)
    │   ├── act2_progress_cut.mp4               [PROGRESS] (80.20s, 第二幕 Shot 06 ~ 10B 连贯成片)
    │   └── current_progress_act1_to_act2_full.mp4 [MASTER] (127.36s / 2分07秒, 第一幕 + 第二幕目前已完成全量大成片！)
    ├── archive/                                # 历史中间版本与废弃测试切片
    └── final_film/                             # 全片 5~7 分钟终极大成片（待全片完成拼接）
```

---

## 🎬 23 镜头分工制作跟踪与资产状态表

### 第一部分：柳锐凯主创负责（第一幕至第三幕：镜头 01 ～ 镜头 14）

| 镜头编号 | 幕次与场景名称 | 关键帧原图 | 原始输入视频 (raw_inputs) | 最终合成成片 (dist/shots) | 资产标记与说明 |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **Shot 01** | 第一幕·工位立项独白·大模型伦理调查引入直切老刘送单 | ✅ 已完成 (`assets/images/shot_00.jpg`) | ✅ 已入库 (`shot_01_luyuan_office_monologue.mp4`) | ✅ `shot_01_final.mp4` | `[FINAL]` 10.03s，陆远工位原生自述、白边电影字幕、闪电匹配无缝直切老刘 |
| **Shot 02A** | 第一幕·雨中送单·老刘正面自述（身份与动机建构） | ✅ 已完成 (`assets/images/shot_02.jpg`) | ✅ 已入库 (`shot_02a_lao_liu_monologue.mp4`) | ✅ `shot_02a_final.mp4` | `[FINAL]` 10.03s，正面中景跟拍，老刘48岁自述与孙女药费动机，雷电闪烁与倒计时猩红漫反射 |
| **Shot 02B** | 第一幕·雨中送单·老刘深夜绝地飞驰（涉水狂奔动作） | ✅ 已完成 | ✅ 已入库 (`shot_02b_lao_liu_scooter_wading.mp4`) | ✅ `shot_02b_final.mp4` | `[FINAL]` 10.01s，动感低机位涉水，暴雨破浪动作衔接，逆风呐喊“绝不能超时” |
| **Shot 02C** | 第一幕·时空过渡桥梁·雨夜都市远景至晨光破晓 | ✅ 双图已就绪 (`shot_02c1.jpg`, `shot_02c2.jpg`) | ✅ 已入库 (`shot_02c_macro_city_storm_to_dawn.mp4`) | ✅ `shot_02c_final.mp4` | `[FINAL]` 10.03s，从涉水骑行顺势拉升升空，展现实拍级雨夜都市全景，延时转入晨光破晓万道金光，老刘沧桑独白“那一晚的雨太大了……可那一单，终究还是超时了”，无缝下俯交接 Shot 06 |
| **Shot 03** | 第一幕·手机倒计时归零严重超时 | ✅ 已完成 | ✅ 已入库 | ✅ `shot_03_final.mp4` | `[FINAL]` 10.0s，含系统机械女声与3.8s报警 |
| **Shot 04** | 第一幕·大厂深夜工位与双显示器系统 | ✅ 已完成 | 已整合入 Shot 01 | 已整合入 Shot 01 | `[INTEGRATED]` 实景双屏（VS Code + 运管Web系统） |
| **Shot 05** | 第一幕·系统终极风控模态框弹窗封号 | ✅ 已完成 | ✅ 已入库 (`shot_05_penalty_modal.mp4`) | ✅ `shot_05_final.mp4` | `[FINAL]` 7.0s，鼠标点击确认与系统机械音永久冻结 |
| **Shot 06** | 第二幕·清晨服务站老刘自述与转场准备 | ✅ 已完成 (`assets/images/shot_06.jpg`) | ✅ 已入库 (`shot_06_laoliu_morning_station.mp4`) | ✅ `shot_06_final.mp4` | `[FINAL]` 10.03s，Veo原音自述优质无错，白边双层电影字幕，尾部下俯 Match Cut 转场锚点就绪 |
| **Shot 07** | 第二幕·多图连续衔接（走来驻足 ➡ 俯身搀扶 ➡ 手部特写） | ✅ 三图已就绪 (`shot_07a_outdoor_consistent.jpg`, `shot_07b_luyuan_approach.jpg`, `shot_07.jpg`) | ✅ 已入库 (`shot_07_luyuan_approach_hands.mp4`) | ✅ `shot_07_final.mp4` | `[FINAL]` 10.03s，多图连续演进，保留优质原生音频（脚步声/环境风/心跳/问候），精确压制白边双层字幕“大叔，您没事吧？”，尾部双手与折痕单据极近景无缝对接 Shot 08 救人闪回 |
| **Shot 08A** | 第二幕·重点高潮前段（台阶自述 ➡ 送餐目击，10s） | ✅ 双图已就绪 (`shot_08a.jpg`, `shot_08b.jpg`) | ✅ 已入库 (`shot_08a_laoliu_steps_to_hallway.mp4`) | ✅ `shot_08a_final.mp4` | `[FINAL]` 10.03s，双图连贯：老刘清晨石阶普通话自述（口型纯正无错） ➡ 眼神推近白光涟漪 ➡ 暴雨楼道手提外卖敲闭门上帝透视惊见倒地老人，双层中文字幕压制完成 |
| **Shot 08B** | 第二幕·重点高潮后段（破门入室 ➡ 120呼救守候，10s） | ✅ 双图已就绪 (`shot_08b.jpg`, `shot_08c.jpg`) | ✅ 已入库 (`shot_08b_rescue_calling_120.mp4`) | ✅ `shot_08b_final.mp4` | `[FINAL]` 10.03s，破门冲入客厅 ➡ 跪地握老人手打120（普通话对白三段打点） ➡ 救护车红蓝警光映照与老刘热泪如释重负 |
| **Shot 08 Full** | 第二幕·重点核心高潮（20秒完整无缝连缀大成片） | ✅ 三图连贯 | ✅ Shot 08A + 08B 双素材 | ✅ `shot_08_full_20s.mp4` | `[FINAL]` 20.06s，石阶自述 ➡ 白光涟漪 ➡ 隔门惊见 ➡ 破门入室 ➡ 跪地握手打120 ➡ 救护车抵达，声画完美咬合！ |
| **Shot 09A** | 第二幕·从家里急救到医院飞奔（双图连贯转场） | ✅ 双图已就绪 (`shot_09a1_home_medics_arrival.jpg`, `shot_09a_hospital_rescue.jpg`) | ✅ 已入库 (`shot_09a_home_to_hospital_corridor.mp4`) | ✅ `shot_09a_final.mp4` | `[FINAL]` 10.03s，双图连贯：家里合力抬担架 ➡ 雨夜警灯飞驰 ➡ 医院急诊飞奔推床进抢救室，原生优质音效保留，双层中文字幕压制完成 |
| **Shot 09B** | 第二幕·抢救门前发现超时（红灯与冰冷重罚） | ✅ 双图连贯 (`shot_09b_outside_er_penalty.jpg`, `shot_09b2_phone_er_corridor.jpg`) | ✅ 已入库 (`gemini_generated_video_56bd2eff.mp4`) | ✅ `shot_09b_final.mp4` | `[FINAL]` 10.00s，AI杂音抹除，标准普通话重配（老刘沧桑音），双层中文字幕压制完成 |
| **Shot 09 Full** | 第二幕·医院急救与算法重罚（20秒完整无缝连缀大成片） | ✅ 四图连贯 | ✅ Shot 09A + 09B 双素材 | ✅ `shot_09_full_20s.mp4` | `[FINAL]` 20.03s，急救推车飞奔 ➡ 抢救室大门紧闭 ➡ 掏出手机 ➡ 第一视角扣款200元 ➡ 沧桑自省，声画完美咬合！ |
| **Shot 10A** | 第二幕·现实回魂抚慰与晨光飞奔工位 | ✅ 双图连贯 (`shot_10a1_laoliu_reality_comfort.jpg`, `shot_10a2_luyuan_running_to_office.jpg`) | ✅ 已入库 (`gemini_generated_video_d3bbc190.mp4`) | ✅ `shot_10a_final.mp4` | `[FINAL]` 10.03s，清晨台阶扶肩对白（“刘叔，您这是救人！等我，我回公司帮您撤销罚单！”） ➡ 决然转身冲刺飞奔科技大厦，100%原生音频保留，双层字幕压制完成 |
| **Shot 10B** | 第二幕·工位申诉与大模型报错拦截 | ✅ 全新大模型双图 (`shot_10b1_ai_large_model_workstation.jpg`, `shot_10b2_ai_neural_error_rejected.jpg`) | ✅ 已入库 (`shot_10b_ai_large_model_error.mp4`) | ✅ `shot_10b_final.mp4` | `[FINAL]` 10.03s，双曲面屏AI大模型系统 ➡ 输入覆写Prompt ➡ 屏幕爆红报错【语义对齐失败·拒绝人工覆写】 ➡ 陆远震撼自语“算得出效率算不出人性的善意”，压制电影级字幕 |
| **Shot 10C** | 第二幕·总监办公室理论与资本规训 | ✅ 双图连贯 (`shot_10c1.jpg`, `shot_10c2.jpg`) | ✅ 已入库 (`shot_10c_wang_office_confrontation.mp4`) | ✅ `shot_10c_final.mp4` | `[FINAL]` 10.03s，推门质问“骑手是为了救人，大模型为什么不能撤销” ➡ 王总端咖啡冷笑“算法要的是效率不是同情心” ➡ 阶级对撞定格，第二幕圆满杀青！ |
| **Shot 10 Full** | 第二幕·技术反噬与直面资本（20秒完整无缝连缀大成片） | ✅ 四图连贯 | 待 Shot 10B + 10C 生成 | 待合成 | `[PLANNED]` 20.0s，工位申诉被拒 ➡ 冲入办公室理论 ➡ 资本冷血训斥，第二幕彻底推向最高潮！ |
| **Shot 11** | 第三幕·老人家属实名致谢寻人短视频 | ✅ 已完成 | 待生成 | 待合成 | `[PENDING_VIDEO]` 手机短视频界面，家属泣不成声感谢救命恩人 |
| **Shot 12** | 第三幕·全网舆论热搜与民众愤慨群像 | ✅ 已完成 | 待生成 | 待合成 | `[PENDING_VIDEO]` 地铁/工位/咖啡馆市民怒刷“救人被封号”热搜 |
| **Shot 13** | 第三幕·市场监管与人社部联合通报直播 | ✅ 已完成 | 待生成 | 待合成 | `[PENDING_VIDEO]` 权威电视新闻直播，红头停业整顿令出台 |
| **Shot 14** | 第三幕·王总满头冷汗冲进机房强令重构 | ✅ 已完成 | 待生成 | 待合成 | `[PENDING_VIDEO]` 股价大跌，资本傲慢在国家制度前彻底坍塌 |

---

### 第二部分：芮凯主创负责（第四幕至第五幕：镜头 15 ～ 镜头 23）

| 镜头编号 | 幕次与场景名称 | 关键帧原图 | 原始输入视频 (raw_inputs) | 最终合成成片 (dist/shots) | 制作指南与要点（详见 SOP 文档） |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **Shot 15** | 第四幕·白板前陆远青年宣言掌控大局 | 待生成 | 待生成 | 待合成 | 白板书写“以人民为中心”，陆远拍出重构方案，眼神坚定 |
| **Shot 16** | 第四幕·研发团队通宵重构底层算法 | 待生成 | 待生成 | 待合成 | 程序员群像通宵敲代码，修改弹性时长与突发救助政务豁免 |
| **Shot 17** | 第四幕·晨光破晓·成功加载人性协议 | 待生成 | 待生成 | 待合成 | 金色晨光穿透落地窗，终端显示 `Humanity Protocol Loaded` |
| **Shot 18** | 第五幕·老刘落寞撕下外卖箱贴纸 | 待生成 | 待生成 | 待合成 | 晨光微露，老刘在旧电动车旁撕下箱贴，准备告别行业 |
| **Shot 19** | 第五幕·手机金色通知·撤销罚单与救助 | 待生成 | 待生成 | 待合成 | 手机爆闪暖金色专属通知，撤销罚单+金牌复权+全额资助医疗费 |
| **Shot 20** | 第五幕·老刘落泪·朴实欣慰的笑容 | 待生成 | 待生成 | 待合成 | 老刘热泪盈眶，把手机贴在胸口，郑重扣好头盔扣带重燃希望 |
| **Shot 21** | 第五幕·晨光斑马线·隔空致意 | 待生成 | 待生成 | 待合成 | 清晨十字路口，老刘等红灯与路边买早餐的陆远相视一笑 |
| **Shot 22** | 第五幕·宏大俯瞰·迎着朝阳的新长征 | 待生成 | 待生成 | 待合成 | 大俯瞰慢升镜头，老刘与千千万万劳动者并肩驶入朝阳林荫大道 |
| **Shot 23** | 第五幕·片尾演职员表（柳锐凯、芮凯） | ✅ 已完成 | 待生成 | 待合成 | 黑底金字楷体大字滚动演职员表，全片思想升华定格 |
