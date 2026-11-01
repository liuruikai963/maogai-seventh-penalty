# 《第七张罚单》AI 微电影全流程协同制作 SOP 指南

> **面向协作主创**：**芮凯**（负责第四幕、第五幕：镜头 15 ～ 镜头 23）  
> **统筹制作人**：**柳锐凯**（负责第一幕、第二幕、第三幕：镜头 01 ～ 镜头 14）  
> **项目定位**：毛概实践高质感现实主义思政 AI 微电影（16:9 横屏，Makoto Shinkai 写实动漫风）  
> **代码仓库**：[https://github.com/liuruikai963/maogai-seventh-penalty.git](https://github.com/liuruikai963/maogai-seventh-penalty.git)

---

## 📌 一、 核心分工划分表

| 制作部分 | 涵盖幕次与镜头 | 剧情核心主线 | 责任主创 | 当前进展 |
| :--- | :--- | :--- | :---: | :--- |
| **第一部分**<br>（前半程） | **第一幕【起】**（Shot 01~05）<br>**第二幕【承】**（Shot 06~10）<br>**第三幕【转】**（Shot 11~14） | 暴雨夜模型考核、老刘送餐破门救助独居老人打120守候导致超时被封、次日老刘哭求、触碰粗糙双手刺痛陆远、代码报错【未定义见义勇为】、舆论引爆热搜、国家监管雷霆通报整改。 | **柳锐凯** | • Shot 01~03 视频生成+混音字幕已连贯完成（31.6s 成片）<br>• Shot 04~14 关键帧概念图全部入库并通过审核。 |
| **第二部分**<br>（后半程） | **第四幕【激】**（Shot 15~18）<br>**第五幕【合】**（Shot 19~23） | 陆远手握制度底气发表青年宣言、团队通宵重构底层大模型（弹性时长+政务互信善举豁免+取消顶格罚款）、清晨加载人性协议、老刘收到金色撤销罚单与救助基金通报、晨光斑马线相视致意、朝阳下奔向新长征。 | **芮凯** | • Shot 23（演职员表）原图已完成<br>• Shot 15~22 待生成原图、动态视频、配音混音与成片剪辑。 |

---

## 📂 二、 资产分类规范与“废稿保留替换”机制（重要铁律）

为了防止文件混乱、丢失灵感或误删历史版本，所有视频资产严格实行**“生肉输入、废稿归档、最终成品”三级分离**，**严禁物理删除任何视频素材**！

```text
homework/
├── assets/
│   ├── images/                         # 1080P 高清关键帧参考图（.jpg）
│   ├── audio/                          # 角色配音原声、环境音效与 BGM（.mp3）
│   └── videos/
│       ├── raw_inputs/                 # 【原始素材库】Gemini / Veo 生成的生肉视频（无配音/带原生拟音）
│       │   ├── shot_01_macro_city_to_lu_yuan_monologue.mp4 [ACTIVE]
│       │   ├── shot_02_lao_liu_scooter_rain.mp4            [ACTIVE]
│       │   ├── shot_03_phone_countdown.mp4                 [ACTIVE]
│       │   └── ...
│       └── archive_scrapped/           # 【废稿与备选库】历史版本、测试稿、淘汰稿（做清晰标记，绝不删除！）
│           ├── shot_02_vo_v1_pre_character_intro.mp4       [TAG: SCRAPPED_PRE_INTRO] (无自我介绍旧版)
│           ├── act1_opening_20s_v1_pre_shot03.mp4          [TAG: SCRAPPED_PRE_SHOT03] (仅前两镜旧拼接)
│           ├── act1_seamless_30s_v1_pre_intro.mp4          [TAG: SCRAPPED_PRE_INTRO] (旧版30秒切片)
│           └── ... (如果生成了不满意的视频，重命名为 scrapped_shot_xx_原因.mp4 移入此处)
├── build/                              # 自动化 Python / FFmpeg 渲染脚本
└── dist/                               # 【最终成品交付库】
    ├── shots/                          # 各分镜单独合成成片（已精确挂接配音、音效与双语/中文字幕）
    │   ├── shot_01_final.mp4
    │   ├── shot_02_final.mp4
    │   └── shot_03_final.mp4
    ├── acts/                           # 各幕无缝连贯最终成片
    │   ├── act1_seamless_31s_final.mp4
    │   ├── act2_seamless_final.mp4     (待生成)
    │   └── ...
    └── final_film/                     # 全片总成片（待全片连缀）
```

> 💡 **废稿替换操作准则**：  
> 当你生成了一个新版本的视频替换旧版本时：  
> 1. 将旧视频移入 `assets/videos/archive_scrapped/`，文件名加上版本号与淘汰原因（如 `shot_15_v1_too_sci-fi.mp4`）；  
> 2. 将满意的新视频放入 `assets/videos/raw_inputs/shot_15_raw.mp4`；  
> 3. 在 `assets/ASSET_MANIFEST.md` 中更新标签状态。这样未来任何时候若需回退或挑取局部镜头，都能一键替换！

---

## 🛠️ 三、 芮凯实操步骤指南（一步一动 SOP）

### 第一步：查阅分镜原图与提示词规范
* 打开 `scripts/ai_video_production_script.md`，定位到自己负责的镜头（Shot 15 ～ Shot 23）。
* 牢记**美术铁律**：新海诚现代写实动漫风（Makoto Shinkai Anime Realism）。**坚决拒绝赛博朋克霓虹悬浮屏、太空舱等脱离现实的虚假科幻元素！** 一切必须扎根于真实的现代中国企业办公楼、真实居民楼与现代都市。
* **角色特征锚定词（必须严格带入 Prompt）**：
  * **男主【陆远】**：`Lu Yuan, 23-year-old Chinese male software engineer, short neat black hair, black rimmed eyeglasses, wearing dark grey casual hoodie and navy blue jacket, slender build.`
  * **骑手【老刘】**：`Lao Liu, 48-year-old Chinese food delivery rider, weathered face with wrinkles and kind tired eyes, slightly hunched back, wearing a faded and worn yellow food delivery uniform and reflective vest, rough hands.`
  * **高管【王总】**：`Director Wang, 40-year-old Chinese corporate director, slicked-back combed hair, tailored navy blue business suit, gold-rimmed watch.`

### 第二步：生成 16:9 关键帧原图并审核
* 为 Shot 15~22 依次生成 16:9 高清关键帧原图，保存至 `assets/images/shot_xx.jpg`。
* 检查画面空间透视（例如：工位电脑显示真实 VS Code 与运管 Web 后台，老人家中为真实简陋客厅水泥地）。
* 确认画风写实自然、角色五官发型一致。

### 第三步：输入 Gemini / Veo 进行“图生视频”（Image-to-Video）
1. 打开 Gemini / Google Veo 创作界面；
2. **上传第一步生成的对应 `shot_xx.jpg` 作为首帧参考图**；
3. **输入对应的动态运镜 Prompt**（参考 `ai_video_production_script.md` 中的英文动态提示词，控制镜头推进、光影变化或人物动作）；
4. 视频时长控制在 5~8 秒左右，画幅必须为 **16:9（1280×720 或 1920×1080），24fps**；
5. 生成完成后下载，重命名规范放入 `assets/videos/raw_inputs/` 目录下。

### 第四步：使用 Edge TTS 生成高品质中文配音
我们全片统一使用微软官方 Edge TTS 深度神经网络音色，免安装即用。在终端或 Python 中运行：

| 角色 / 场景 | 推荐神经网络音色 | 语速与音调调节 | 角色气质特征 |
| :--- | :--- | :--- | :--- |
| **男主陆远** | `zh-CN-YunxiNeural` | `rate="+14%"` | 理性、深思、富有良知的青年知识分子 |
| **骑手老刘** | `zh-CN-YunjianNeural` | `rate="+16%", pitch="-1Hz"` | 沧桑、沙哑、忠厚朴实的底层老父亲质感 |
| **平台系统音** | `zh-CN-XiaoxiaoNeural` | `rate="+25%", pitch="+4Hz"` | 冰冷、刺耳、毫无感情的机械算力女声 |
| **官方新闻通报** | `zh-CN-YunyangNeural` | `rate="+5%"` | 庄重、权威、浩然正气的国家新闻主播音 |

*参考生成 Python 代码*：
```python
import asyncio, edge_tts

text = "今晚，我们要把良知与劳动者的尊严，正式编译进系统的底层规则！"
asyncio.run(edge_tts.Communicate(text, "zh-CN-YunxiNeural", rate="+14%").save("assets/audio/shot_15_luyuan.mp3"))
```

### 第五步：运行脚本完成混音、字幕压制与成片连贯
参考工程内现成的 `build/render_act1_with_character_intros.py`：
* 脚本会自动读取 raw 视频与音频；
* 自动使用微软雅黑加粗字体（`C:/Windows/Fonts/msyhbd.ttc`）压制带黑边的电影级居中字幕；
* 将原生环境拟音（0.35倍音量）与声优配音（1.65倍音量）完美混音；
* 导出各镜头成片至 `dist/shots/`，并硬切无缝连缀为整幕大片至 `dist/acts/`。

### 第六步：Git 协同提交
每完成一个镜头的生成或测试，使用 Git 规范推送至 GitHub 仓库：
```bash
git add assets/ docs/ dist/
git commit -m "feat(act4): add shot 15-16 keyframes and raw video clips"
git push origin main
```

---

## 🎯 四、 芮凯负责镜头速查表（镜头 15 ～ 镜头 23）

* **镜头 15（白板前陆远的掌控大局）**：深夜研发大厅，白板上写着“以人民为中心·发展为了人民”，陆远拍出重构架构图，神情坚定。
* **镜头 16（团队通宵重构底层算法）**：群像镜头，键盘声连绵，青年程序员们合力修改“恶劣天气弹性时长”与“突发救助豁免通道”。
* **镜头 17（晨光破晓照亮机房代码）**：第一缕金色晨光穿透大厂落地窗，陆远屏幕闪烁 `Humanity Protocol Loaded`（人性协议已加载）。
* **镜头 18（老刘落寞撕下外卖箱贴纸）**：清晨街头，老刘坐在旧电动车上，神色落寞地撕下车贴准备告别职业。
* **镜头 19（手机金色通知·撤销罚单与救助）**：老刘手机爆闪整屏暖金色庆祝通知：第七张罚单已撤销，恢复接单，授予城市先锋称号，全额资助孙女治疗费！
* **镜头 20（老刘落泪·朴实欣慰的笑容）**：老刘热泪盈眶，颤抖着把手机贴在胸口，随后郑重扣紧头盔，重燃希望。
* **镜头 21（晨光斑马线·隔空致意）**：十字路口，老刘等红灯，对面买早餐的陆远与老刘目光相遇，两人隔空相视一笑。
* **镜头 22（终局升华·驶向阳光的长征）**：大俯瞰慢升镜头，老刘驶向朝阳洒满金光的大道，千千万万普通劳动者并肩前行，陆远画外音点题升华当代青年新长征！
* **镜头 23（片尾演职员表）**：黑底金色楷体大字滚动演职员表（主创：柳锐凯、芮凯；指导课程：毛概微电影实践）。
