# 《第七张罚单》AI 微电影逐镜头生产脚本（AIGC Production Script）

> **作品类型**：思政 AI 微电影（时长约 5~6 分钟）  
> **视觉基调**：高质感现代写实动漫 / 影视概念艺术风格（Makoto Shinkai Anime Realism / 2.5D Cel-Shaded）  
> **画幅规格**：16:9 横屏（1920×1080）  
> **生产协作规范**：严格执行【图画先行 -> 用户审核 -> 给出视频提示词 -> 用户提交Gemini生成视频 -> 回传拼接】四步 SOP（详见 `docs/STYLE_CONSISTENCY_RULES.md`）

---

## 📋 标准化生产 SOP 执行说明
1. **图画先行**：每个分镜必须先完成 16:9 高清关键帧原图，供导演（用户）审核。
2. **严禁跳步**：未经审核通过的图片，严禁直接提供视频提示词或生成视频。
3. **图生视频一致性**：审核通过后，以此图为参考底图输入 Gemini / Veo，搭配专属动效 Prompt 生成物理流体动态。

---

## 🎨 角色特征锚定词（保持全片一致性的关键 Key Prompts）

在生成画面时，请在对应角色的 Prompt 中强制加入以下角色专属锚定词：

* **男主【陆远】角色锚定词**：
  > `Character: Lu Yuan, 23-year-old Chinese male software engineer, short neat black hair, black rimmed eyeglasses, wearing dark grey casual hoodie and navy blue jacket, serious and thoughtful facial expression, slender build.`  
  > （23岁中国年轻软件工程师，利落黑色短发，黑框眼镜，深灰连帽衫搭配藏青色夹克，神情专注沉稳，身形修长）
* **骑手【老刘】角色锚定词**：
  > `Character: Lao Liu, 48-year-old Chinese food delivery rider, weathered face with wrinkles and kind tired eyes, slightly hunched back, wearing a faded and worn yellow food delivery uniform and reflective vest, weathered hands with rough calluses, honest and humble expression.`  
  > （48岁中国外卖大叔，饱经风霜的脸庞带着细纹和疲惫但善良的眼神，微驼背，穿着褪色破损的外卖工服与反光背心，双手满是粗糙老茧，忠厚淳朴的神态）
* **高管【王总】角色锚定词**：
  > `Character: Director Wang, 40-year-old Chinese corporate director, slicked-back combed hair, wearing an expensive tailored navy blue business suit and gold-rimmed watch, confident, cold and calculating corporate expression, standing in luxury high-tech office.`  
  > （40岁大厂总监，背头整齐，穿昂贵合身藏青西装戴金表，自信、冷峻算计的职场神态）

---

## 🎬 逐镜头生产分镜总表

---

### 🔴 第一部分：前三幕（镜头 01 ～ 镜头 14）
> **主创制作人**：**柳锐凯**  
> **叙事跨度**：第一幕【起】、第二幕【承】、第三幕【转】  
> **核心剧情**：暴雨夜大模型考核、送餐破门救助独居老人打120守候导致超时被封、次日老刘哭求、触碰粗糙双手刺痛陆远、代码报错【未定义见义勇为】、舆论引爆热搜、国家监管雷霆通报整改。  
> **当前进展**：Shot 01~03 视频生成+混音字幕已连贯完成（31.6s 成片），Shot 04~14 关键帧概念图全部入库并通过审核。

---

### 第一幕：【起】雨夜红线与前六张罚单的重量（约 1 分钟）

#### 镜头 01（开篇·工位立项独白·大模型伦理调查引入直切老刘送单）
* **分镜状态**：【终稿交付已入库】`assets/videos/raw_inputs/shot_01_luyuan_office_monologue.mp4` -> `dist/shots/shot_01_final.mp4` (10.03s, 原生声画+白边电影字幕)
* **镜头类型**：中景（Medium Shot）平缓慢速微推（Slow Push-in）至落地窗暴雨电光闪现（Match Cut 直接引入镜头 02）
* **时长**：10.03 秒（成片精细对齐）
* **视听语言与转场设计（极速破题，电影级闪电匹配转场）**：
  * **开篇立题**：23岁大模型算法架构师陆远端坐弧形双屏前（神经网络代码+实时调度热力图），正对镜头沉稳自述，开门见山点破“人工智能创新发展与算法决策伦理困境”的思政实践核心主题。
  * **尾部转场（直切老刘）**：当独白讲到最后一句*“……直到那个特大暴雨的深夜”*时，陆远目光自然移向身后巨大的落地窗；窗外暴雨奔流、天际一道白色闪电骤然划破夜空，雷声隐隐轰鸣！画面在闪电与暴雨中瞬间**硬切（Match Cut）**到街头积水中老刘冒雨破浪狂飙的电动车（镜头 02），完成从“算法高层宏观设计”到“基层劳动者生死狂奔”的震撼视觉与阶层戏剧对撞！
* **AI 画面提示词（Prompt 归档）**：
  > **中文**：现代写实动漫风格，2.5D赛璐珞高质感光影。23岁的中国年轻软件工程师陆远（短碎黑发，黑框眼镜，深灰连帽衫内搭，外穿藏青色休闲夹克，神情深沉沉静、专注内敛），深夜坐在高科技互联网研发工位上。面前是弧形双联显示器：左屏显示暗色系神经网络代码与模型调度后台，右屏显示实时城市交通与骑手运力热力图。暖黄色桌面台灯与冷色调屏幕在黑框眼镜镜片上投下的幽蓝微光形成冷暖反差。镜头缓缓推近，陆远平静注视前方开口自述。当念到“直到那个特大暴雨的深夜”时，陆远目光望向身后巨大的落地玻璃幕墙——窗外暴雨如注，天际一道电光闪烁，无缝直切下一镜头雨夜街头。  
  > **英文**：`Strict style consistency: Makoto Shinkai anime realism concept art style. Lu Yuan, 23yo Chinese male AI algorithm architect, black glasses, dark grey hoodie and navy jacket, seated at curved dual-monitor workstation showing neural code and GIS dispatch heatmap. Warm desk lamp light and cool screen reflections. Camera slowly pushes in as he speaks to camera, then turns head toward rainy floor-to-ceiling window as lightning strikes outside in the stormy metropolis. 16:9, 24fps.`
* **配音 / 原生对白**：
  * **陆远（沉稳内敛的原声自述）**：“我叫陆远，23岁，大模型调度算法架构师。着眼于人工智能的创新发展，我们试图透视热点事件的底层逻辑，开展算法决策的伦理困境调查……直到那个特大暴雨的深夜。”
* **字幕打点（已精确压制）**：
  * [0.3s - 3.7s] `我叫陆远，23岁，大模型调度算法架构师。`
  * [3.8s - 7.1s] `着眼于人工智能的创新发展，我们试图透视热点事件的底层逻辑，`
  * [7.2s - 9.8s] `开展算法决策的伦理困境调查……直到那个特大暴雨的深夜。`
* **历史测试素材归档**：
  * 旧版宏观雨夜大都市大远景素材已做非破坏性安全归档至 `assets/videos/archive_scrapped/shot_01_macro_city_v1_pre_monologue_replace.mp4` `[TAG: SCRAPPED_PRE_MONOLOGUE_REPLACE]`，完整保留随时可调取。

---

#### 镜头 02A（雨中送单·老刘正面自述·身份动机与暴雨夜驰）
* **分镜状态**：【实拍生成入库】`assets/videos/raw_inputs/shot_02a_lao_liu_monologue.mp4` | 终片 `dist/shots/shot_02a_final.mp4`
* **镜头类型**：正面中景跟拍（Front-facing Medium Tracking Shot）/ 车身颠簸震颤
* **时长**：10.03 秒
* **视听衔接与转场设计（闪电匹配硬切 Match Cut）**：
  * **前序衔接（承接镜头 01）**：完全承接镜头 01 陆远工位落地窗外的雷电闪光，画面在同一道撕裂夜空的刺眼白色闪电与轰鸣雷声中瞬间**硬切（Match Cut）**到深夜暴雨街头！老刘的电动车在积水中破浪前冲，闪电刹那照亮老刘布满雨水与焦虑沧桑的面容，完成从“象牙塔算法调度”到“底层劳动者生死狂奔”的震撼戏剧对撞！
  * **动作过程（Action）**：正面跟随颠簸镜头。老刘身穿被暴雨湿透发亮的黄色外卖服和荧光反光背心，头盔挡雨面罩被暴雨猛烈拍打，雨水如注滑落。老刘双手紧握湿滑车把，面部肌肉紧绷，眼神布满血丝与焦灼，一边大口急促喘息，一边逆着狂风暴雨悲壮呐喊自述（口型发音与台词严格契合）。车把中央的手机屏幕显示着刺眼猩红色的订单倒计时警告框，剧烈的红光强烈映射在老刘胸口与粗糙双手上。
  * **尾部衔接（动作顺切至镜头 02B）**：念完台词后眼神紧盯前方暗夜，闪电雷鸣划过，无缝动作切入 02B 全景涉水狂奔！
* **角色原生对白与字幕**：
  * [0.3s - 3.5s] `我叫刘长贵，48岁，送外卖给孙女挣药费。`
  * [3.6s - 6.2s] `今晚暴雨单价高，但绝不能超时……`
  * [6.3s - 8.8s] `要是扣了钱，孙女的药就没了！`

---

#### 镜头 02B（雨中送单·老刘绝地飞驰·深水涉水狂奔动作）
* **分镜状态**：【素材入库】`assets/videos/raw_inputs/shot_02b_lao_liu_scooter_wading.mp4` | 终片 `dist/shots/shot_02b_final.mp4`
* **镜头类型**：侧逆光低机位动感跟拍（Low-Angle Dynamic Action Tracking Shot）
* **时长**：10.01 秒
* **视听衔接与转场设计（动作顺承 + 尾部俯冲手机无缝引出）**：
  * **前序衔接（承接镜头 02A）**：顺承 02A 老刘迎风加速的动力，镜头瞬切为低角度动感跟拍，电动车前轮犹如快艇般切开深水，激荡起漫天白色水花。
  * **动作过程（Action）**：深水路段车辆受阻，电机发出高负荷运转的低吼。雨水如瀑布倾泻，车灯光束劈开水幕。老刘咬牙躬身抗风，展现基层劳动者在特大暴雨极端环境下的搏命抗争。
  * **尾部衔接（引向镜头 03）**：在喊完“绝不能超时！”后，老刘惊惶地猛然低头下瞥车把手机；镜头顺势极速向下俯冲拉近（Tilt Down & Push In），直扑手机屏幕上即将归零的猩红数字，无缝引出镜头 03（手机倒计时特写）。
* **角色台词与字幕**：
  * [0.5s - 4.5s] `雨再大我也得冲！冲过去……`
  * [4.6s - 9.5s] `绝不能超时，只要这单送到，药费就有着落了！`

---

#### 镜头 03（手机界面·前六张罚单特写）
* **镜头类型**：特写（Close-up） / 俯冲下移接棒特写
* **时长**：6 ~ 10 秒
* **承接关系与转场设计（视线道具顺承接棒）**：
  * **承接镜头 02 尾部**：承接镜头 02 结尾老刘低头看手机与镜头俯冲动作，画面直接聚焦挂在车把上的湿漉漉智能手机屏幕特写！雨滴不断飞溅在屏幕上，刺目的猩红色倒计时 `00:03`、`00:02`、`00:01`、`00:00` 剧烈闪烁归零，冰冷的超时警报声骤响，瞬间击碎老刘的所有希冀！
* **镜头类型**：特写（Close-up） / 快速下移（Tilt Down）
* **时长**：6 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：挂在车把上的湿漉漉智能手机屏幕特写，雨滴不断滴落在屏幕上，界面显示外卖骑手个人中心，红色列表列出一连串扣款记录和罚单详情：“爬楼超时扣50元”、“暴雨滑倒扣全单”，最上方是一行巨大的猩红色倒计时：`00:03`、`00:02`、`00:01`、`00:00`，电影级UI界面渲染，写实细节。  
  > **英文**：`Extreme close-up of a wet smartphone mounted on scooter handlebar, rain droplets scattering on glass screen, glowing mobile app interface displaying a red penalty ledger with fine logs, top of screen showing a giant pulsating crimson countdown: 00:03, 00:02, 00:01, 00:00, UI details, sleek anime realism, intense tension, high-contrast display, 16:9.`
* **配音 / 画外音（VO）**：
  * **系统机械女声（刺耳冰冷）**：“订单已严重超时，系统扣除当单全部收入。本月违规次数已达上限！”
* **音效 & BGM**：
  * **音效**：尖锐急促的超时报警滴滴声，伴随闪电雷鸣。

---

#### 镜头 04（恒温机房·陆远工位切入）
* **镜头类型**：中景（Medium Shot） / 侧光特写
* **时长**：5 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：现代化互联网公司开阔的数据机房与研发大厅，中央空调恒温舒适，幽暗宽敞的大厅里跳动着巨大的全城实时配送数据大屏，绿色的数字矩阵流淌。男主陆远坐在电脑前，黑框眼镜倒映着屏幕幽蓝的冷光，神情理性而麻木，16:9。  
  > **英文**：`Medium interior shot, modern high-tech open office and data dispatch center, air-conditioned cool ambient lighting, massive wall-sized analytics screens displaying city delivery maps and streaming green cyber data matrices. Lu Yuan, 23-year-old Chinese male software engineer with black glasses sitting at dual monitors, glowing blue screen reflected on his glasses lenses, calm and sterile mood, Makoto Shinkai lighting, 16:9.`
* **配音 / 画外音（VO）**：
  * **陆远（自语/敲键盘声）**：“今晚全城订单流转率99.8%，算法模型平稳无异常。”
* **音效 & BGM**：
  * **音效**：轻微的空调送风声、清脆连贯的机械键盘敲击声。

---

#### 镜头 05（终极弹窗·第七张罚单生效）
* **镜头类型**：屏幕特写（Screen Close-up） / 慢推
* **时长**：4 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：电脑屏幕特写，中央弹出一道带有刺眼红色警示框的系统终极风控通知，上面写着“骑手工号8092（刘长贵）触发第7次严重超时，判定为高风险低效账户，执行永久封号”。鼠标光标点击在蓝色的“确认执行”按钮上，现代写实动漫UI，电影级冷光。  
  > **英文**：`Close-up of computer screen UI, a stark crimson pop-up dialogue box: 'Rider ID 8092 (Liu Changgui) - 7th Severe Delay Triggered. Risk Threshold Exceeded. Permanent Account Ban Initiated.' Mouse cursor hovering and clicking blue 'Confirm' button, sleek sci-fi software design, high resolution, cool clinical lighting, 16:9.`
* **配音 / 画外音（VO）**：
  * **系统电子提示音**：“工单处理完毕，骑手账号已永久冻结。”
* **音效 & BGM**：
  * **音效**：重重的鼠标回车点击声，随后是一记空洞沉闷的电子低音轰鸣（Sub-bass drop）。

---

### 第二幕：【承】粗糙的双手与没有“善意”的参数（约 1.5 分钟）

#### 镜头 06（清晨服务站·老刘自述与转场准备）
* **镜头类型**：全景（Wide Shot） / 静态构图至缓慢推近，尾部顺滑下俯（Tilt Down & Push In）
* **时长**：5~10 秒
* **视听衔接与转场设计（黄金三段式，承前启后）**：
  * **前序起势（0~2s）**：承接第一幕第七张罚单生效的刺骨冰冷，清晨冷调薄雾散开，老刘坐在台阶上捧着早餐，身旁放着磨损的黄色头盔；
  * **主体开口（2~6.5s）**：镜头平稳推近，老刘神情坚韧沉稳，开口自述：“雨终于停了，等会儿大门打开，再去跟工作人员好好沟通……”；
  * **尾部转场准备（6.5~10s）**：老刘视线下垂，聚焦看向自己满是老茧皲裂的双手（紧攥着折痕纸张），镜头顺势下俯推进，锁定粗糙双手，为镜头 07 手部特写完成无缝动作转场交接（Match Cut）！
* **AI 画面提示词（Gemini / Veo 实测 100% 免拦截双语提示词·具体音效与正向对白驱动口型）**：
  > **中文提示词（直接复制提交 Gemini/Veo）**：
  > ```text
  > 【图生视频硬性约束】：严格以参考图片为唯一基准进行2D手绘动漫动画化生成！必须100%保持参考图的二次元动漫手绘风格、人物五官与服饰、黄色工服与清晨服务站门口台阶背景完全一致！绝对严禁三次元真人实拍，无真人皮肤质感，纯动漫艺术风格。
  > 
  > 【黄金三段式动态演进与转场准备（核心铁律五）】：
  > 1. 前序起势（0~2s）：从参考图画面启动动态，2D动漫骑手坐在清晨微湿的石阶上，身旁放着黄色头盔，双手捧着早餐，深吸一口微凉晨气，路面积水倒映清冷晨光。
  > 2. 主体开口（2~6.5s）：摄像机正面平稳缓慢向前推近（Slow Push-in）。人物微微抬头，嘴部与面部肌肉自然开合，伴随清晰的说话节奏自然自语：“雨终于停了，等会儿大门打开，再去跟工作人员好好沟通……”（展现自然的开口说话嘴型节奏）。
  > 3. 尾部转场准备（6.5~10s）：念完台词后，角色情绪转向沉思，眼神与头部顺势向下低垂，聚焦看向自己布满老茧、粗糙皲裂的双手（手中紧紧攥着一张折痕纸张）。镜头顺着视线顺滑下俯推进（Tilt Down & Push In），将焦点完全锁定在粗糙双手上，为下一镜手部特写完成无缝动作转场交接！
  > 
  > 【具体角色对白（沉稳沧桑大叔音）】：
  > 角色对白：“雨终于停了，等会儿大门打开，再去跟工作人员好好沟通……”
  > 
  > 【具体音效与声音设计（Sound Design & Foley）】：
  > - 关键具体音效：清晨远方早班车辆驶过湿润地面的微弱碾水声、远方街道传来的清脆单车铃声。
  > - 拟音环境（Foley）：雨后清晨微风吹过树梢声、城市清晨宁静底噪、两声清亮清脆的晨鸟啼鸣。16:9宽画幅，24fps。
  > ```
* **配音 / 画外音（VO·已重新生成 4.99s 终稿）**：
  * **老刘（沉稳沙哑沧桑音）**：“雨终于停了，等会儿大门打开，再去跟工作人员好好沟通……”
* **音效 & BGM**：
  * **音效**：清晨车辆碾水声、微风声、鸟鸣声。
  * **BGM**：转为缓慢单调的钢琴单音，凄凉中带有一丝坚韧。

---

#### 镜头 07（多图连续衔接：走来驻足 ➡ 俯身搀扶 ➡ 手部特写）
* **镜头类型**：中景平跟走来 ➡ 双人俯身中景 ➡ 手部极近景大特写（三阶段连续动态演进）
* **时长**：8~10 秒
* **核心衔接设计（响应导演指导，彻底杜绝割裂感）**：
  * **第一阶段（0~3s，看见与驻足·Shot 07A）**：陆远（短发、黑框眼镜、藏青夹克、单肩包）清晨上班走来，看到台阶上落寞吃早餐的老刘，停下脚步转头关切；
  * **第二阶段（3~7s，上前与搀扶·Shot 07B）**：双人中景，陆远走上台阶俯身伸出右手搀扶住老刘手臂，老刘手拿单据惊讶抬头；
  * **第三阶段（7~10s，触碰与共鸣·Shot 07）**：视线下俯推近为手部极近景特写，陆远年轻干净的手握住老刘如大理石般粗糙皲裂的双手，触发心灵震颤与下一镜回忆闪回！
* **AI 画面提示词（Gemini 多图连续通过版）**：
  > **中文多图提示词（直接复制提交）**：
  > ```text
  > 【图生视频硬性约束】：以提供的三张参考图为基准进行2D手绘动漫动画连续生成！100%保持参考图的二次元动漫画风、陆远与老刘的人物造型、黄色工服与清晨场景完全一致！绝对严禁三次元真人实拍，无真人皮肤质感，纯动漫艺术风格。
  > 
  > 【三图连贯动态演进过程】：
  > 1. 阶段一·走来与停步（承接图一，0~3s）：清晨薄雾中，青年工程师陆远（黑框眼镜、藏青夹克、单肩包）快步走在湿润的园区路面上。他突然放慢脚步停在台阶前，关切地转头望向坐在石阶上落寞休息的外卖骑手老刘。
  > 2. 阶段二·靠近与搀扶（承接图二，3~7s）：陆远快步走近台阶，关切地微微俯身，伸出右手小心翼翼地扶住老刘微微发颤的手臂。老刘手拿着泛黄的折痕单据，略带惊讶与无助地缓缓抬头，陆远轻声关切：“大叔，您没事吧？”
  > 3. 阶段三·特写下推与触碰（承接图三，7~10s）：摄像机顺着陆远下俯的视线顺滑推近为手部极近景大特写（Extreme Close-up）。陆远白皙干净的年轻手与老刘布满老茧、皲裂粗糙的双手在晨光中交汇相握，画面泛起微微柔和的晨曦光晕，镜头聚焦在双手与单据折痕上，为下一镜头闪回昨夜救人场景做好无缝转场交接！
  > 
  > 【声音与音效设计（Sound Design & Foley）】：
  > - 关键音效：陆远由远及近的皮鞋脚步声、脚步停顿声、布料轻微摩擦声、纸张展开沙沙声、一声深沉悠长的心跳低音（Heartbeat Boom）。
  > - 拟音环境：雨后清晨微凉清爽的微风声、清晨城市宁静开阔底噪、两声清脆晨鸟鸣叫。16:9宽画幅，24fps动画电影质感。
  > ```
* **配音 / 画外音（VO·双轨情感交融）**：
  * **陆远（关切原声）**：“大叔，您没事吧？”
  * **老刘（沙哑自责）**：“我……我真不是故意超时的……”
  * **陆远（震颤内心独白）**：“握住那双手的瞬间，我的心狠狠抽搐了一下。这双手——跟我老家在工地上开重卡、手上满是裂口的父亲，长得一模一样。”
* **音效 & BGM**：
  * **音效**：由远及近的脚步声、纸张揉皱声、布料摩擦声、沉重心跳低音。
  * **BGM**：深沉温热的大提琴与钢琴缓缓铺开。

---

#### 镜头 08（重点高潮20秒分段：Shot 08A 10s + Shot 08B 10s）

#### 镜头 08A（清晨石阶自述 ➡ 送外卖楼道惊见，10秒）
* **镜头类型**：双图连贯演进（清晨石阶中近景 ➡ 眼神推近白光水波转场 ➡ 暴雨楼道提外卖目击）
* **时长**：10.0 秒
* **双基准参考图**：
  - 图一（起始）：[`assets/images/shot_08a_laoliu_explaining.jpg`](file:///d:/study/course/maogai/homework/assets/images/shot_08a_laoliu_explaining.jpg)
  - 图二（结束）：[`assets/images/shot_08b_delivery_hallway_discovery.jpg`](file:///d:/study/course/maogai/homework/assets/images/shot_08b_delivery_hallway_discovery.jpg)
* **AI 画面提示词（Gemini / Veo 双图合一通过版）**：详见 [`shot_08_production_guide.md`](file:///C:/Users/27277/.gemini/antigravity/brain/f5b14212-99d2-460d-9706-e55469254373/shot_08_production_guide.md)。
* **配音 / 画外音（VO）**：
  * **老刘（台阶自述，0~5s）**：“小兄弟，我真不是故意超时的……昨晚送餐，那家老人摔在地上动不了，我真不能扔下不管啊……”
* **音效**：清晨微风、纸张沙沙声 $
ightarrow$ 心跳低音 $
ightarrow$ 暴雨倾盆、远雷轰鸣、塑料外卖袋摩擦声。

---

#### 镜头 08B（破门冲入 ➡ 跪地握手打120守候，10秒）
* **镜头类型**：双图连贯演进（暴雨楼道撞门冲入 ➡ 客厅跪地握手打120 ➡ 救护车红蓝反光扫过定格）
* **时长**：10.0 秒
* **双基准参考图**：
  - 图一（起始）：[`assets/images/shot_08b_delivery_hallway_discovery.jpg`](file:///d:/study/course/maogai/homework/assets/images/shot_08b_delivery_hallway_discovery.jpg)
  - 图二（结束）：[`assets/images/shot_08c_rescue_calling_120.jpg`](file:///d:/study/course/maogai/homework/assets/images/shot_08c_rescue_calling_120.jpg)
* **AI 画面提示词（Gemini / Veo 双图合一通过版）**：详见 [`shot_08_production_guide.md`](file:///C:/Users/27277/.gemini/antigravity/brain/f5b14212-99d2-460d-9706-e55469254373/shot_08_production_guide.md)。
* **配音 / 画外音（VO）**：
  * **老刘（电话焦急求救，3~7s）**：“喂！120急救中心吗？！这里有位独居大爷摔倒了……地址是幸福家园，请快派救护车过来！”
  * **陆远（跨镜内心震撼独白，7~10s）**：“出警记录与门前影像不会撒谎。在紧闭的大门前，他毫不犹豫破门冲进屋内，为一个突发急症的独居老人叫来救护车、守候到最后一刻。”
* **音效**：撞门声、沉重急促脚步声、窗外暴雨狂泻、电话急救求救声、远处救护车警笛声。

---

#### 镜头 09（老刘第一视角·暴雨中下一单超时与扣款通知）
* **镜头类型**：第一人称主观视角（First-person POV） / 手机屏幕特写至视线微仰
* **时长**：10 秒
* **基准参考图**：`assets/images/shot_09.jpg`（老刘双手持暴雨中手机，猩红超时扣罚通知，背景为电动车与远去救护车）
* **AI 画面提示词（Gemini / Veo 实测 100% 免拦截与死锁普通话）**：
  > **中文提示词**：
  > ```text
  > 【图生视频硬性约束】：严格以提供的参考图为唯一基准进行2D手绘动漫动画连续生成！100%保持参考图的新海诚写实动漫画风、老刘第一视角、湿透黄色工服袖口、反光条与手机屏幕猩红UI完全一致！绝对严禁三次元真人实拍，无真人皮肤质感，纯动漫艺术风格。
  > 【语言强制死锁】：全程发音与口型必须为纯正清晰的标准中文普通话（Strictly Mandarin Chinese Lip-Sync & Spoken Dialogue），绝对严禁英文或其他无意义杂音！
  > 
  > 【镜头 09（10秒）动态演进过程（第一视角按亮手机 ➡ 猩红超时扣款 ➡ 望向远去救护车）】：
  > 1. 阶段一·暴雨中急促按亮手机（承接参考图，0~3s）：第一人称主观视角，暴雨夜老旧小区楼下。老刘双手戴着湿透的黑色半指手套，黄色工服袖口带银色反光条，双手微颤紧握智能手机。倾盆大雨砸在手机屏幕上水花四溅，老刘大拇指急促按下电源键点亮屏幕。
  > 2. 阶段二·猩红扣款界面炸开与震颤（3~7s）：屏幕骤然爆闪猩红强光，弹出醒目的骑手端惩罚界面《【订单严重超时扣罚通知】下一笔订单 #4028 超时 35 分钟，扣除本单收入，罚款扣除 ¥200！系统判定：长时间异常滞留！》。红光映红老刘湿透的双手，老刘大拇指颤抖试图点击申诉，按钮却显示灰色死锁，手机发出急促低沉的错误蜂鸣与震动。老刘沧桑沙哑自语：“等救护车把大爷拉走，我才想起后边那单……全扣了……”
  > 3. 阶段三·视线微仰与远去警灯（7~10s）：老刘手指无力垂下，镜头由手机顺势微微上仰（Tilt Up），穿透密集的雨丝望向街道远方——救护车红蓝交替闪烁的急救车灯正渐渐消失在雨雾深处。老刘深深叹息，雨水顺着视线滑落。
  > 
  > 【声音与音效】：
  > - 粗重喘息声、暴雨砸在雨衣与手机屏幕的水滴飞溅声、手机强力震动嗡鸣声、刺耳超时扣款警告提示音、远处救护车警笛渐渐远去衰减声。16:9宽画幅，24fps。
  > ```
* **配音 / 画外音（VO）**：
  * **老刘（沧桑沉痛的独白）**：“等救护车把老人接走，我才想起车上后边那单外卖……一按亮手机，全是扣钱的红字。我救了一条人命，可在这系统眼里……我只是个延误了35分钟的‘异常数据’。”
* **音效 & BGM**：
  * **音效**：手机连续震动声、刺耳扣款蜂鸣声、雨水飞溅声、渐行渐远的救护车警笛。
  * **BGM**：大提琴拉出如泣如诉的低沉旋律，与冰冷的机械报警声形成刺骨对比。

---

#### 镜头 10（总监办公室·王总的伪善规训）
* **镜头类型**：双人中景（Medium Two-shot） / 优雅而压抑的光影
* **时长**：6 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：豪华的大厂总监独立办公室，落地窗外可以俯瞰整座繁华CBD。王总穿着考究西装，面带温和微笑地给坐在对面的陆远递过去一杯手冲咖啡，身体前倾，眼神却深邃冷漠，陆远神情紧绷，气氛压抑而充满潜规则，电影级室内布光。  
  > **英文**：`Interior medium two-shot, luxurious executive penthouse office overlooking sunny CBD skyline. Director Wang in tailored navy business suit offering a porcelain coffee cup to Lu Yuan with a polite patronizing smile, leaning forward persuasively, cold calculating eyes behind polite facade. Lu Yuan sitting stiffly across mahogany desk with clenched fists, tense corporate confrontation, high-end cinematic anime realism, 16:9.`
* **配音 / 画外音（VO）**：
  * **王总（语重心长、温和却残酷的职场台词）**：“陆远，你是农村走出来的名校高材生，年轻有前途。但你得明白，算法的规律就是消灭偶然性。同情心换不来财报，为了一个老头破坏整个模型，值吗？把心思收回来，别断送了自己的前途。”
* **音效 & BGM**：
  * **音效**：咖啡杯轻轻放在大理石桌面的清脆碰撞声。
  * **BGM**：低沉带有压迫感的弦乐持续鸣响。

---

### 第三幕：【转】潮水转向——舆论爆发与监管介入（约 1.5 分钟）

#### 镜头 11（网络引爆·老人家属寻人视频）
* **镜头类型**：竖屏手机界面切入全景（Split Screen / Mobile Inset）
* **时长**：5 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：社交平台短视频界面，画面上一位在外地工作赶回的年轻女性（老人家属）眼含热泪面向镜头深深鞠躬，背景是医院急救病房，视频配字：“全城急寻昨夜在暴雨中破门救了我独居老父亲的8092号外卖大哥！”视频点赞突破100万，评论区无数网友疯狂转发：“医生说再晚5分钟老人就没了！真正的平凡英雄！”，充满温情与感动，新媒体视觉风格。  
  > **英文**：`Social media mobile UI graphic, viral video display. A tearful grateful daughter in hospital hallway bowing deeply to the camera, Chinese caption: 'Searching the city for Rider 8092 who kicked open the door and saved my collapsed elderly father during last night's storm! Doctor said 5 minutes later would have been fatal!'. Over 1 million likes, streaming heart emojis and shares, dynamic modern media presentation, clean anime aesthetic, 16:9.`
* **配音 / 画外音（VO）**：
  * **老人家属（原声哭腔、眼含热泪）**：“昨晚特大暴雨，我独居老父亲突发急性心梗昏迷倒在地上动弹不得，如果不是那位外卖大哥听到呼救撞开门做心肺复苏并叫来救护车，我爸早就没了！医生说再晚5分钟就回天乏术了！求大家帮我们全家找到8092号恩人，当面跪谢救命大恩！”
* **音效 & BGM**：
  * **音效**：手机消息疯狂弹出的叮咚提示音。

---

#### 镜头 12（残酷真相·舆论怒火喷涌）
* **镜头类型**：蒙太奇动态弹幕（Fast-paced Montage with Floating Comments）
* **时长**：6 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：昏暗空间中，巨大的多块屏幕上飞速滚动着各大社交平台的热搜榜单与汹涌的网友弹幕评论：“#救人骑手因延误被平台封号#”、“算法有算力但没有良心！”、“别把劳动者异化成耗材！”，屏幕泛着红光与蓝光，字迹清晰，批判性与戏剧张力拉满。  
  > **英文**：`Fast dynamic montage, multiple glowing digital displays in a darkened room showing trending social media topics and exploding comment threads. Top hashtag: #Heroic Rider Banned by Algorithm for Saving Life#. Floating text comments: 'The algorithm has computing power, but no conscience!', 'Stop treating workers as disposable data!'. Intense neon red and white glow, powerful societal tension, 16:9.`
* **配音 / 画外音（VO）**：
  * **网友群声（混响层叠，越来越高昂）**：
    * “救了人反被开除？这是什么吃人的系统！”
    * “马克思早就说过，资本不仅生产商品，还把活生生的人变成商品！”
    * “支持老骑手！平台必须给出说法！”
* **音效 & BGM**：
  * **BGM**：鼓点突然密集，节奏陡然加快，充斥着风暴降临的宏大压迫感。

---

#### 镜头 13（国家监管亮剑·权威通报直播）
* **镜头类型**：电视新闻全景（Television Broadcast View）
* **时长**：6 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：国家权威部门新闻发布会电视直播画面。背景是庄严的蓝白色发布会大幕，发言人神情严肃正义，手持通报发言，电视底栏滚动字幕显示：“市场监管总局与人社部就‘冷酷算法与劳动者权益保障’联合约谈涉事平台，限期推行‘算法取中’整改”，权威大气，写实国风。  
  > **英文**：`Official national regulatory joint press conference broadcast on television news. Professional dignified spokesperson standing at wooden podium against sleek navy blue backdrop, television chyron banner rolling: 'State Regulators Launch Joint Investigation: Ordering Platforms to Reform Ruthless Algorithms, Enforce People-Centered Worker Protection'. Clear journalistic anime style, authoritative, 16:9.`
* **配音 / 画外音（VO）**：
  * **新闻发言人（字正腔圆、铿锵有力的播音腔）**：“互联网平台绝不是野蛮生长的法外之地！科技发展必须坚守‘**以人民为中心**’的发展思想！算法不能凌驾于劳动者的生命健康与社会公义之上，即日起对相关企业启动督导整改，强制推行‘算法取中’！”
* **音效 & BGM**：
  * **音效**：新闻联播风格的宏亮提示音。

---

#### 镜头 14（资本慌乱·王总的仓皇破防）
* **镜头类型**：特写（Close-up） / 晃动镜头（Handheld Shake）
* **时长**：4 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：办公室里，王总满头冷汗，领带被扯松，手机在手中剧烈震动响个不停，身后大屏幕上公司的股价图呈断崖式下跌直线下冲。王总神色极度慌张，手足无措，刚才的优雅傲慢荡然无存，强烈的狼狈感，写实光影。  
  > **英文**：`Close-up with slight dramatic shake, Director Wang in total panic, suit tie loosened, forehead drenched in sweat, holding buzzing smartphone as calls flood in. Background monitor displays corporate stock chart in sharp red freefall. His smug arrogance completely shattered, desperate and bewildered expression, cinematic realism, high tension, 16:9.`
* **配音 / 画外音（VO）**：
  * **王总（慌乱失措地冲进机房大喊）**：“陆远！技术部所有人立刻停工！联合调查组进驻了！大老板说了，限你们24小时内，赶紧把突发救助和免责规则糊弄出来交差！”
* **音效 & BGM**：
  * **音效**：手机持续刺耳的铃声、大门被猛烈推开的撞击声。

---

### 🔵 第二部分：后两幕（镜头 15 ～ 镜头 23）
> **主创制作人**：**芮凯**（详细实操指南请查阅 [TEAM_COLLABORATION_SOP.md](file:///d:/study/course/maogai/homework/docs/TEAM_COLLABORATION_SOP.md)）  
> **叙事跨度**：第四幕【激】、第五幕【合】  
> **核心剧情**：陆远手握制度底气发表青年宣言、团队通宵重构底层大模型（弹性时长+政务互信善举豁免+取消顶格罚款）、清晨加载人性协议、老刘收到金色撤销罚单与救助基金通报、晨光斑马线相视致意、朝阳下奔向新长征。  
> **当前进展**：Shot 23（演职员表原图）已完成，Shot 15~22 待生成原图、动态视频、配音混音与成片剪辑。

---

### 第四幕：【激】撕裂枷锁——把“人”重新写进代码（约 1.5 分钟）

#### 镜头 15（陆远掌控全场·工科男的沉着反击）
* **镜头类型**：中景（Medium Shot） / 仰拍（Low Angle Shot）
* **时长**：6 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：研发大厅中央，陆远站起身来，身姿挺拔坚定。他当着慌乱的王总的面，啪的一声将厚厚一份早准备好的《劳动者权益保障与算法重构方案》拍在桌面上。周围年轻的技术员们纷纷抬头看着他，陆远神情从容自信，身后白板上工整地写着“以人为本”，英雄气概，微仰视角。  
  > **英文**：`Low angle medium shot, Lu Yuan standing tall and resolute in the center of bustling engineering department. He slaps a comprehensive architectural blueprint document titled 'Worker Rights Algorithm Reform Manifesto' firmly on the desk in front of the panicked Director Wang. Surrounding young engineers looking up with respect. Background whiteboard clearly states 'People-Centered'. Heroic anime composition, dramatic office lighting, 16:9.`
* **配音 / 画外音（VO）**：
  * **陆远（沉着、威严、不可动摇）**：“王总，这不是糊弄公关的时候。国家法律要求我们必须真正以人为本。现在，请把权限交给我们，我们来重构这套底层的规矩！”
* **音效 & BGM**：
  * **音效**：文件重重砸在桌面的沉闷撞击声。
  * **BGM**：音乐转为宏亮、充满斗志的管弦乐序曲，战意昂扬。

---

#### 镜头 16（深夜代码战·指尖上的新长征）
* **镜头类型**：快速蒙太奇（Fast Montage） / 键盘与代码特写
* **时长**：6 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：极富科技感与速度感的代码重构蒙太奇。年轻工程师们手指在机械键盘上飞舞，屏幕上蓝绿色的代码行疾速刷屏，特写显示核心逻辑：`Def Evaluate_Humanity_Exception(LaoLiu_Event): Status = "Exempt_Penalty"`。咖啡杯冒着热气，团队通宵达旦、神情坚毅地重塑算法世界，热血写实动漫。  
  > **英文**：`Fast cinematic montage, intense collaborative late-night software development. Young software engineers' fingers flying across backlit mechanical keyboards, screens rapidly scrolling glowing lines of clean Python/Rust code. Monitor highlights: 'def evaluate_humanity_exception(rider_event): status = EXEMPT_PENALTY'. Steaming coffee mugs, determined focused faces, cyberpunk anime productivity, epic lighting, 16:9.`
* **配音 / 画外音（VO）**：
  * **陆远（内心坚定独白）**：“我们这代人寒窗苦读，不是为了写出一串代码去算计风雨里的父辈。把‘人’的尊严写进规则，就是我们青年工程师的长征！”
* **音效 & BGM**：
  * **音效**：密集的键盘敲击声宛如战鼓交响。

---

#### 镜头 17（晨光破晓·编译成功）
* **镜头类型**：全景（Wide Shot） / 光线穿透（Light Rays）
* **时长**：5 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：清晨破晓时分，第一缕金灿灿的晨曦阳光穿透研发中心高大的落地玻璃窗，洒在安静下来的大厅和陆远的脸上。屏幕上弹出一个绿色的成功标志：“新版算法模型部署成功：已加载【恶劣天气弹性时长】、【见义勇为一键免责机制】”，温暖神圣，希望与破晓。  
  > **英文**：`Wide cinematic shot, golden dawn sunlight bursting through massive glass floor-to-ceiling office windows, casting brilliant rays across tired but smiling engineers and Lu Yuan's face. Central monitor displays glowing green verification: 'System Deployment Successful: Humanity Protocol Loaded, Elastic Weather Timing Active'. Hopeful, warm, triumph of human spirit, Makoto Shinkai sunrise aesthetic, 16:9.`
* **配音 / 画外音（VO）**：
  * **系统柔和提示音**：“新一代以人为本调度系统已上线，全网规则同步完毕。”
* **音效 & BGM**：
  * **音效**：清脆温和的清晨鸟鸣声，编译成功的清亮铃声。
  * **BGM**：悠扬温暖的钢琴与大提琴交织，充满希望感。

---

### 第五幕：【合】第七张罚单的撤销与晨光中的长征（约 1 分钟）

#### 镜头 18（阳光街头·老刘落寞退场）
* **镜头类型**：中景（Medium Shot） / 逆光构图
* **时长**：4 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：雨后天晴的清晨街头，空气清新，地面湿润倒映着金光。老刘站在路边停着的旧电动车旁，默默用布擦拭着外卖保温箱，准备撕下车身上的标签贴纸，眼神中带着对未来的迷茫与落寞，逆光人物剪影，写实温情。  
  > **英文**：`Medium shot, crisp golden morning after rain, clean reflective city pavement. Lao Liu standing beside his electric scooter parked by tree-lined sidewalk, quietly peeling off delivery logos from his thermal delivery box with downcast eyes, bittersweet and sorrowful mood, silhouette against warm morning sun, emotional realism, 16:9.`
* **配音 / 画外音（VO）**：
  * **（无对白，纯音乐烘托寂静）**
* **音效 & BGM**：
  * **音效**：撕下不干胶贴纸的轻微声音、树叶随风摆动的沙沙声。

---

#### 镜头 19（金色通知·第七张罚单正式撤销）
* **镜头类型**：特写（Extreme Close-up） / 光效绽放
* **时长**：6 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：老刘手机屏幕猛然亮起整屏的暖金色专属全屏通知！屏幕中央闪烁着金色勋章图标，清晰显示：“刘长贵师傅：第 7 张超时罚单已撤销！全额退还扣款！授予‘见义勇为城市先锋’称号，专项救助基金 100,000 元已到账！”手机屏幕光照亮了老刘通红的眼眶，光芒神圣温暖。  
  > **英文**：`Extreme close-up of rider's smartphone screen erupting in radiant golden UI celebration. Golden medal badge icon with official notification text: 'Master Liu Changgui: The 7th Penalty Ticket Has Been Officially Revoked! All Deductions Refunded! Awarded City Hero Title & 100,000 RMB Medical Aid Fund Deposited!'. Golden glow illuminating Lao Liu's tearful widening eyes, cinematic wonder, 16:9.`
* **配音 / 画外音（VO）**：
  * **系统语音播报（温暖洪亮、充满敬意）**：“刘长贵师傅，您的英勇善举已被国家及平台荣誉库永久收录！系统已撤销您的第七张罚单并恢复全部权益！感谢您，用双手托起了这座城市的温度！”
* **音效 & BGM**：
  * **音效**：激昂温暖的系统成就音效。

---

#### 镜头 20（老刘落泪·淳朴的笑容）
* **镜头类型**：特写（Close-up） / 面部特写
* **时长**：5 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：老刘的面部特写。眼泪从他饱经风霜布满皱纹的眼角滑落，但他嘴角却绽放出无比踏实、灿烂、淳朴的笑容。他颤抖着把手机紧紧按在胸前，然后郑重地扣好安全头盔，眼神中重新燃起了对生活的尊严与希望，光影柔和细腻。  
  > **英文**：`Close-up portrait of Lao Liu. Tears of profound relief and gratitude streaming down his weathered wrinkled cheeks, breaking into a deeply honest, radiant and humble smile. He presses the glowing phone tenderly against his chest, then solemnly straps on his yellow helmet, eyes full of renewed dignity and life, soft golden cinematic rim light, 16:9.`
* **配音 / 画外音（VO）**：
  * **老刘（带哭腔的淳朴笑声）**：“哎！……有救了……小孙女有救了！”
* **音效 & BGM**：
  * **音效**：头盔卡扣扣紧的清脆“咔哒”声，拧动车把启动电动车的轻微马达声。

---

#### 镜头 21（晨光斑马线·隔空相望的致意）
* **镜头类型**：双向过肩/全景（Over-the-shoulder to Wide Shot）
* **时长**：6 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：清晨宽阔干净的十字路口斑马线。老刘骑着电动车在路口等绿灯，而彻夜未眠的陆远正站在人行道斑马线另一侧买热包子。两人隔着斑马线在晨光中视线相交。老刘不知道陆远就是重构代码的工程师，只是以劳动者的淳朴向这个年轻人善意点头微笑，陆远也微微点头微笑致意，人与人之间的温暖交汇，大片意境。  
  > **英文**：`Wide cinematic shot at a sunlit morning crosswalk. Lao Liu waiting on his scooter at the red light, while Lu Yuan with his grey hoodie stands on the opposite sidewalk holding a hot breakfast bag. Their eyes meet across the painted crosswalk stripes under glowing morning light. Lao Liu, unaware that Lu Yuan rewrote his fate, simply gives a warm respectful nod and kind smile to the young stranger. Lu Yuan nods back with deep emotional fulfillment, profoundly moving, 16:9.`
* **配音 / 画外音（VO）**：
  * **（无对白，纯音乐高潮起）**
* **音效 & BGM**：
  * **BGM**：全曲最高潮交响乐骤然奏响，管乐与弦乐激荡，雄浑辽阔。

---

#### 镜头 22（终局升华·驶向阳光的长征）
* **镜头类型**：远景大俯拍（High Angle Extreme Wide Shot） / 慢速升镜
* **时长**：7 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：大俯瞰远景镜头，清晨绿树成荫的城市大道，朝阳在天际线喷薄而出。老刘拧动油门，电动车平稳地驶入洒满金光的林荫大道，身边是千千万万个迎着朝阳奔忙奋斗的普通劳动者。陆远站在高楼窗前凝望远方，天地辽阔，充满希望与正道之美。  
  > **英文**：`Epic high-angle aerial shot slowly pulling up. Golden sun rising majestically over the modern city skyline, tree-lined boulevards bathed in radiant morning gold. Lao Liu accelerates his scooter smoothly into the sunny avenue, alongside dozens of ordinary working citizens riding forward into the dawn. Lu Yuan standing tall at the high window looking out. Vast, hopeful, socialist modernity, breathtaking cinematic beauty, 16:9.`
* **配音 / 画外音（VO·全剧终极点题结语）**：
  * **陆远（激昂而深情的男声画外音）**：
    > “八十多年前，先辈的长征是用双脚跨越雪山草地，用血肉之躯打破阶级压迫，让千千万万劳苦大众站起来做国家的主人；  
    > 今天，身处算力汹涌的智能时代，我们青年一代也正走在属于我们的长征路上——  
    > 这一代人的长征，是用国家制度驾驭资本野心，坚决不让冷冰冰的算法遮蔽劳动的尊严与人性的光芒。  
    > **技术的尽头不是资本的利润，以人为本、科技向善，才是中国特色社会主义最坚实的人性底色！”**
* **音效 & BGM**：
  * **BGM**：交响乐在最宏大的和弦中落下，余韵悠长。

---

#### 镜头 23（片尾淡出·演职员表）
* **时长**：5 秒
* **画面**：黑底金字，滚动显示：
  * 片名：《第七张罚单》
  * 《毛泽东思想和中国特色社会主义理论体系概论》课程实践微电影
  * **主创制作人员**：柳锐凯、芮凯
  * **主题**：算法向善 · 以人为本 · 一代人有一代人的长征
  * 鸣谢指导老师及全体同窗。
