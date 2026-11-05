# 《算法之外》AI 微电影全流程协同制作 SOP 与人物防走样指南

> **面向协作主创**：**芮凯**（负责第四幕、第五幕：镜头 15 ～ 镜头 23）  
> **统筹制作人**：**柳锐凯**（负责第一幕、第二幕、第三幕：镜头 01 ～ 镜头 14）  
> **项目定位**：毛概实践高质感现实主义思政 AI 微电影（16:9 横屏，Makoto Shinkai 写实动漫风）  
> **代码仓库**：[https://github.com/liuruikai963/maogai-seventh-penalty.git](https://github.com/liuruikai963/maogai-seventh-penalty.git)

---

## 📌 一、 核心分工与责任边界

> **当前全片状态**：前三幕（Shot 01 ~ Shot 14，共 16 个镜头，成片时长 3分00秒）已由柳锐凯全量渲染并通过审核，完成了完整成片母带 `dist/acts/liuruikai_part1_complete_master.mp4`，现已全面进入第四幕与第五幕的冲刺阶段。

| 主创成员 | 负责范围 | 涵盖镜头 | 核心交付物 |
| :--- | :--- | :--- | :--- |
| **柳锐凯** | **前三幕统筹 + 全局包装** | **Shot 01 ～ 14 + 片头/片尾/花絮** | • `dist/acts/intro_title_sequence.mp4`（18s 正式片头）<br>• `dist/acts/outro_credits_sequence.mp4`（24s 滚动画卷片尾）<br>• `dist/acts/behind_the_scenes_featurette.mp4`（52s 制作花絮与废稿实录） |
| **芮凯** | **后两幕主创（反转与升华）** | **Shot 15 ～ Shot 22（共 8 个镜头）** | • 8 张 16:9 关键帧原图（`assets/images/shot_15.jpg` ~ `shot_22.jpg`）<br>• 8 段无杂音 Raw 视频（`assets/videos/raw_inputs/shot_15_raw.mp4` 等）<br>• 统一角色音色配音音频与压制成片（`dist/acts/act4_act5_seamless.mp4`） |

---

## 🛡️ 二、 人物一致性“防走样”核心图谱（核心铁律）

为了防止人物到了后半段发生“换脸”、“换衣服”、“变画风”的重大脱节，所有生成工具必须**强制使用以下官方锚点图作为首帧/垫图参考**，并**逐字带入人物锁定 Prompt 词组**！

### 1. 男主角【陆远】（贯穿 Shot 15, 16, 17, 21）
* **角色定位**：23岁互联网大厂大模型算法架构师，理性、内敛、良知未泯的青年知识分子。
* **官方标准参考图（必须作为垫图）**：
  * 面部五官与气质基准：[`assets/images/poster_luyuan_laoliu_final.jpg`](file:///d:/study/course/maogai/homework/assets/images/poster_luyuan_laoliu_final.jpg)
  * 工位与身姿基准：[`assets/images/shot_01.jpg`](file:///d:/study/course/maogai/homework/assets/images/shot_01.jpg)
  * 服装全身基准：[`assets/images/shot_10a2_luyuan_running_to_office.jpg`](file:///d:/study/course/maogai/homework/assets/images/shot_10a2_luyuan_running_to_office.jpg)
* **固定外貌特征**：
  * **发型五官**：短碎黑发、干净清爽；**必戴黑色方形半框眼镜**；冷白肤色，神情沉着冷静。
  * **固定服装（绝对严禁更换）**：**深灰色连帽卫衣（内搭） + 藏青色休闲夹克（外穿，Navy Blue Jacket）** + 深黑休闲长裤 + 深色运动鞋。
* **严禁出现的走样情况**：
  * ❌ 严禁穿西装打领带（那是王总的着装！）；
  * ❌ 严禁摘掉眼镜或变成金丝眼镜；
  * ❌ 严禁生成日系非主流黄发或夸张发型。
* **必带英文锁定 Prompt 锚块**：
  > `Strict Character Lock: Lu Yuan, 23-year-old Chinese male software architect, short neat black hair, black rimmed eyeglasses, wearing dark grey casual hoodie under navy blue jacket, dark trousers, slender build, calm and resolute facial expression, Makoto Shinkai anime realism, 16:9.`

---

### 2. 底层骑手【老刘】（贯穿 Shot 18, 19, 20, 21, 22）
* **角色定位**：48岁老实本分的外卖骑手，孙女患病，为治病拼命送单的老父亲。
* **官方标准参考图（必须作为垫图）**：
  * 面部特写与沧桑感基准：[`assets/images/poster_luyuan_laoliu_final.jpg`](file:///d:/study/course/maogai/homework/assets/images/poster_luyuan_laoliu_final.jpg)
  * 工服质感与电动车基准：[`assets/images/scene_optimization_shot06_subway_v2.jpg`](file:///d:/study/course/maogai/homework/assets/images/scene_optimization_shot06_subway_v2.jpg)
  * 手部与手机特写基准：[`assets/images/shot_09b2_phone_er_corridor.jpg`](file:///d:/study/course/maogai/homework/assets/images/shot_09b2_phone_er_corridor.jpg)
* **固定外貌特征**：
  * **发型五官**：两鬓花白凌乱，皮肤黝黑粗糙，眼角有明显皱纹，眼神疲倦但纯善；嘴唇干裂；手掌粗糙带有老茧和泥污。
  * **固定服装（绝对严禁更换）**：**磨损褪色的黄色外卖冲锋衣工服（胸前与背后带有反光银条，衣服上有深色油污和雨水痕迹）** + 深灰色旧工装裤 + 劳保短靴。
  * **固定道具**：**黄色老旧半盔（表面有划痕与褪色贴纸）**，旧款黑色踏板电动车（带方形保温箱）。
* **严禁出现的走样情况**：
  * ❌ 严禁生成 20 多岁的年轻帅哥外卖员；
  * ❌ 严禁外卖服变成崭新发亮的亮黄色无污渍制服；
  * ❌ 严禁佩戴赛博朋克发光头盔。
* **必带英文锁定 Prompt 锚块**：
  > `Strict Character Lock: Lao Liu, 48-year-old Chinese food delivery rider, weathered wrinkled face with greying temples, tired kind eyes, rough calloused hands, wearing faded worn yellow food delivery jacket with silver reflective stripes and faint stains, dark grey work pants, weathered yellow motorcycle helmet nearby, Makoto Shinkai anime realism, 16:9.`

---

### 3. 反派高管【王总】（出现在 Shot 15）
* **角色定位**：40岁平台运营总监，信奉唯效率论的资本高管。
* **官方标准参考图（衔接帧）**：
  * 状态基准（领带扯散、满头大汗）：[`assets/images/shot_14_ending_transition_reference_clean.jpg`](file:///d:/study/course/maogai/homework/assets/images/shot_14_ending_transition_reference_clean.jpg)
* **固定外貌特征**：
  * **发型五官**：梳着油光水滑的背头短发，但此时**满头冷汗直淌，头发微乱，面色惨白惊慌**。
  * **固定服装**：高端定制藏青色商务西装、白衬衫、**领带已被扯松歪斜、领口解开一颗纽扣**、手腕戴金边手表。
* **必带英文锁定 Prompt 锚块**：
  > `Strict Character Lock: Director Wang, 40-year-old Chinese corporate director, slicked-back hair slightly disheveled, sweat dripping from forehead, tailored navy business suit, white shirt with unbuttoned collar, loosened striped tie, panicked and frantic expression, Makoto Shinkai anime realism, 16:9.`

---

## ⚡ 三、 关键衔接点：Shot 14 ➔ Shot 15 严丝合缝同场景接棒规范

> **同场景铁律（绝不换房间）**：  
> • 第 14 镜：王总在自己的高管办公室（`assets/images/shot_14.jpg`），大屏显示股价暴跌 -24.8%，桌上咖啡打翻，电话被打爆，满头虚汗瘫坐在真皮大班椅上瑟瑟发抖。删去跑出办公室的多余动作！  
> • 第 15 镜：空间 100% 保持在王总高管办公室！陆远推开玻璃门大步跨入，身姿挺拔如松，将深蓝色《算法架构重构与劳动者保障白皮书》（深蓝色硬质工程文件夹）重重拍在王总桌前！正面压制：“王总，联合调查组已经到了。这不是糊弄公关的时候。请把权限交给我们！”

### 1. 对应基准关键帧
* 衔接原图：`assets/images/shot_15.jpg`（已定稿入库）

### 2. Shot 15 官方标准 Prompt
```text
Low angle medium shot inside Director Wang's corner executive office, direct spatial continuity from shot_14. Stormy lightning outside window, large monitor displaying '-24.8%' red stock crash. Panicked Director Wang with loosened tie cowering back in chair. 23yo software architect Lu Yuan, wearing black eyeglasses and navy jacket over dark grey hoodie, stands tall across the desk, firmly slamming a thick dark blue technical binder titled 'Algorithm Reform & Worker Rights Architecture' onto the mahogany desk. Cool cinematic lighting, intense confrontation, Makoto Shinkai anime realism, 16:9.
```

---

## 🎬 四、 芮凯负责镜头逐镜制作手册（Shot 15 ～ 22）

### 镜头 15（6秒）：陆远掌控全场·工科男硬核反击
* **出场人物**：陆远（藏青夹克卫衣）、王总（冷汗领带散）、工程师群像。
* **核心动作**：重重摔下深蓝色技术文件夹，双联屏幕亮起架构，全员起立。
* **配音（陆远，YunxiNeural）**：“王总，这不是糊弄公关的时候。国家法律要求我们必须真正以人为本。现在，请把根目录权限交给我们，我们来重构这套底层的规矩！”

### 镜头 16（6秒）：深夜代码战·指尖上的新长征
* **出场人物**：青年程序员群像、陆远专注敲击键盘侧影。
* **核心动作**：机械键盘敲击特写、屏幕上疾速滚动的 Python/Rust 代码流，核心高亮显示：  
  `def evaluate_humanity_exception(rider_event): status = EXEMPT_PENALTY`  
  热咖啡冒着蒸汽，窗外暴雨渐止。
* **配音（陆远画外独白，YunxiNeural）**：“我们这代人寒窗苦读，不是为了写出一串代码去算计风雨里的父辈。把‘人’的尊严写进规则，就是我们青年工程师的长征！”

### 镜头 17（5秒）：晨光破晓·人性协议加载成功
* **出场人物**：陆远（疲惫但微笑）、研发大厅全景。
* **核心动作**：第一缕金灿灿朝阳穿透大落地窗，照亮陆远的镜片与脸庞。主控屏幕弹出温润绿色弹窗：`System Deployment Successful: Humanity Protocol Loaded`（新一代以人为本调度系统已上线，已加载【恶劣天气弹性时长】与【突发救助一键免责机制】）。
* **配音（系统女声，XiaoxiaoNeural）**：“新一代以人为本调度系统已上线，全网规则同步完毕。”

### 镜头 18（4秒）：老刘落寞撕下外卖箱贴纸
* **出场人物**：老刘（黄色旧工服、头盔放在脚边）。
* **核心动作**：清晨冷清的路边，老刘坐在破旧电动车后座，神色暗淡衰老，粗糙的手默默撕下外卖箱上卷边的平台贴纸，心灰意冷准备退行。
* **配音**：无对白，仅有早晨微风与撕贴纸的沙沙声，凄凉沉郁。

### 镜头 19（6秒）：系统退款与工会短信·真实克制转折（严禁手游爆闪与送10万假剧情）
* **出场人物**：老刘粗糙满是老茧的手部特写、划痕旧手机屏幕。
* **核心动作**：手机连震两下，屏幕弹出真实质朴的骑手系统通知：  
  `【系统消息：异常订单申诉已通过】`  
  `订单8092判定为见义勇为紧急避险，免除责任。扣款 200.00 元已退回，账号恢复正常派单！`  
  随后顶部滑入真实政务横幅：`【市总工会·见义勇为基金会】救助绿色通道已对接医院……`  
  无夸张光效，晨光打在屏幕与干裂手指上，真实的纪实感。
* **配音**：无机器女声播报，仅手机真实震动“嗡嗡”与清脆系统提示音“叮”。

### 镜头 20（5秒）：老刘落泪·踏实释怀的笑容（尊严失而复得）
* **出场人物**：老刘（面部特写）。
* **核心动作**：老刘愣在原地，眼圈通红，没有大喊大叫，而是长舒一口积压数日的浊气，用破旧棉袄衣袖狠狠揩干眼角，嘴角浮现出踏实、憨厚而释怀的苦笑与欣慰。将手机揣进胸口，双手重新郑重扣紧黄色头盔卡扣！
* **配音（老刘哽咽，YunjianNeural）**：“（长吐一口气，抽吸鼻尖）……回来了……这回规矩讲道理了……小孙女有救了……”

### 镜头 21（5秒）：晨光斑马线·隔空致意（阶层和解）
* **出场人物**：老刘（骑在车上戴黄头盔）、陆远（藏青夹克黑框眼镜）。
* **核心动作**：清晨阳光斑驳的城市十字路口。老刘在斑马线前停着等红灯；路边买早餐走过来的陆远正好停下脚步转过头，两人的视线在晨曦中相撞。两人没有说一句话，只是隔着人群相视一笑。
* **核心寓意**：脑力劳动者与体力劳动者在此刻相互尊重、精神相通。

### 镜头 22（8秒）：宏大升华·驶向阳光的新长征（全片大终局）
* **出场人物**：老刘、千千万万骑手与早班劳动者、朝阳都市。
* **核心动作**：电影级大远景航拍慢速拉升！老刘拧动油门，与成百上千穿着黄色、蓝色骑手服的外卖员、环卫工人和普通奋斗者并肩驶入被金红色朝阳洒满的宽阔大道。
* **配音（陆远宏亮升华独白，全片核心理论高潮）**：  
  *“几十年前，我们的父辈在雪山草地、在风雨兼程中建立新中国；今天，在数字时代的新长征路上，技术绝不能异化为冰冷吃人的工具。让每一次劳动被看见、让每一个普通人被尊重——这就是我们这一代人的回答！”*

---

## 🎙️ 五、 全片统一人声配音规范（Edge TTS 必用参数）

为了杜绝声音忽男忽女、音色漂移，后半段配音一律使用统一音色：

| 角色 | 官方指定音色 | 推荐参数 | 角色特征与语气要求 |
| :--- | :--- | :--- | :--- |
| **陆远** | `zh-CN-YunxiNeural` | `rate="+14%"` | 坚定、沉稳、充满理想主义与正义感的工科青年 |
| **老刘** | `zh-CN-YunjianNeural` | `rate="+16%", pitch="-1Hz"` | 沧桑沙哑、忠厚纯朴的底层老父亲质感 |
| **平台系统音** | `zh-CN-XiaoxiaoNeural` | `rate="+25%", pitch="+4Hz"` | 温暖、柔和、清晰治愈的系统女声 |

---

## 📦 六、 Git 规范提交与流水线交割

芮凯完成关键帧或生成视频后，请按标准执行提交：
```bash
# 1. 提交新生成的图片与视频素材
git add assets/images/ assets/videos/raw_inputs/
git commit -m "feat(act4-5): add shot 15-22 keyframes and raw clips"

# 2. 推送至远程仓库
git push origin main
```
若有任何生成疑问或镜头拼接问题，随时在仓库 Issue 或群内沟通，柳锐凯统筹端随时提供混音与压制支持！
