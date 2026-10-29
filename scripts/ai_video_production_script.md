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

### 第一幕：【起】雨夜红线与前六张罚单的重量（约 1 分钟）

#### 镜头 01（开篇·宏观全景·雨夜都市）
* **镜头类型**：大远景（Extreme Long Shot） / 慢速推进（Slow Push-in）
* **时长**：5 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：暴雨倾盆的现代超级都市夜景，密集的雨幕笼罩摩天大楼，道路上车流灯光拉出长长的红色光轨，远处是灯火辉煌的互联网大厂总部大厦，水坑倒映着霓虹灯光，电影写实动漫风，大片质感，16:9，8k分辨率。  
  > **英文**：`Cinematic wide shot of a modern cyberpunk-infused metropolis under heavy torrential rainstorm at night, towering skyscrapers obscured by misty rain, wet asphalt streets reflecting bright neon lights and red taillights, distant illuminated tech company headquarters glass tower, puddle reflections, Makoto Shinkai realistic anime style, cinematic lighting, dramatic atmosphere, 16:9, 8k.`
* **配音 / 画外音（VO）**：
  * **陆远（沉稳深思的画外音）**：“刚进大厂的那一年，我曾真诚地坚信：世界上最完美的艺术就是代码。它把现实中的一切混沌，都驯化成了绝对理性的最优解……”
* **音效 & BGM**：
  * **音效**：沉闷的远雷声、密集的暴雨拍打地面的沙沙声。
  * **BGM**：低沉、带有电子科技脉冲感的冷色调合成器长音起。

---

#### 镜头 02（雨中送单·老刘特写）
* **镜头类型**：中近景（Medium Close-up） / 跟随镜头（Tracking Shot）
* **时长**：5 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：暴雨中骑着旧电动车的中国老骑手，雨水顺着头盔面罩不断流淌，反光背心被雨水湿透发亮，后视镜摇晃，电动车在积水中艰难前行，神色焦急专注，车把上的手机屏幕发出猩红色的亮光，电影质感写实动漫，强反差光影。  
  > **英文**：`Medium tracking shot, Lao Liu, 48-year-old Chinese food delivery rider riding a weathered electric scooter through flooded city streets in torrential rain, water streaming down clear helmet visor, soaked reflective safety vest glowing in streetlights, handlebars mounted smartphone glowing brightly in crimson red, tense and determined expression, hyper-detailed anime realism, cinematic depth of field, 16:9.`
* **配音 / 画外音（VO）**：
  * **陆远（画外音）**：“……直到那个特大暴雨的深夜，我亲手见证了极致的算力，是怎样将一个具体的人，推向绝境。”
* **音效 & BGM**：
  * **音效**：电动车涉水的哗哗声、雨刮器声、急促的喘息声。

---

#### 镜头 03（手机界面·前六张罚单特写）
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

#### 镜头 06（清晨服务站·老刘的身影）
* **镜头类型**：全景（Wide Shot） / 静态构图
* **时长**：5 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：清晨微亮的大厂一楼骑手服务站大厅门口，台阶冰冷潮湿。老骑手老刘疲惫地坐在台阶边缘，头发湿漉，脚边放着裂开的头盔，他双手捧着半个干瘪的白馒头，眼神空洞而绝望地看着地面，晨光清冷，凄凉写实，现代动漫风格。  
  > **英文**：`Wide shot, early morning outside the sleek glass entrance of corporate rider service station, cold wet pavement. Lao Liu, 48yo delivery rider sitting wearily on outdoor concrete steps, messy damp hair, cracked helmet on ground, holding a cold dry steamed bun with trembling calloused hands, staring despondently at floor, pale blue morning light, poignant realism, emotional cinematic, 16:9.`
* **配音 / 画外音（VO）**：
  * **老刘（沙哑微弱的声音）**：“……要是号真没了，下周孙女的透析费……我上哪儿去借啊……”
* **音效 & BGM**：
  * **音效**：清晨偶尔驶过的汽车声、老刘沉重微弱的叹息声。
  * **BGM**：转为缓慢单调的钢琴单音，充满凄凉与无助感。

---

#### 镜头 07（陆远驻足·粗糙的手部特写）
* **镜头类型**：特写（Extreme Close-up） / 慢镜头（Slow Motion）
* **时长**：6 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：手部特写镜头。老刘的手紧紧攥着一张皱巴巴的医院透析缴费通知单，那双手手背皮肤深褐皲裂，布满细碎血口，指节粗大变形，指甲缝里满是洗不掉的深色油污。另一只穿着干净运动夹克年轻男生的手（陆远）正犹豫着伸向他，强烈的代际对比，极度写实的情感质感。  
  > **英文**：`Extreme close-up of hands. Lao Liu's weathered, heavily calloused hands clutching a crumpled white hospital dialysis bill, scarred cracked skin on knuckles with healing red cuts, dark ingrained soil under fingernails. A young clean hand (Lu Yuan) hesitantly reaching out to help him up, powerful generational visual contrast, deeply emotional anime concept art, warm natural morning light, 16:9.`
* **配音 / 画外音（VO）**：
  * **老刘（自责愧疚、声音沙哑）**：“年轻人，我真不是故意偷懒超时的……昨晚那家独居大爷突发心梗摔在地上动不了，我光顾着破门救人做心肺复苏等救护车，真没顾上看手机啊……”
  * **陆远（内心独白）**：“握住那双手的瞬间，我的心狠狠抽搐了一下。这双手——跟我老家在工地上开重卡、手上满是裂口的父亲，长得一模一样。”
* **音效 & BGM**：
  * **音效**：纸张揉皱的声音，衣物摩擦声。

---

#### 镜头 08（监控回放·暴雨夜老旧小区破门救人）
* **镜头类型**：楼道监控视角（CCTV / Security Camera View）
* **时长**：6 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：老旧小区狭窄楼道监控录像画面，画质带有轻微时间戳和噪点（‘CAM-03 5F CORRIDOR 23:38:12’）。昨夜暴雨中，浑身湿透、身穿黄色反光背心的外卖员老刘，与闻声赶来的邻居一起奋力撞开一扇生锈的防盗铁门；屋内昏暗地面上，一位独居老人昏迷倒地，老刘毫不犹豫跪在地上紧急实施心肺复苏，动作急迫而专业，随后急救医生冲上楼梯，画面纪实感人，狭窄楼道充满真实的生活质感。  
  > **英文**：`High-angle CCTV surveillance footage in a dim, retro Chinese residential walk-up corridor, slight video noise and green timestamp overlay ('CAM-03 5F CORRIDOR 23:38:12'). During last night's rainstorm, soaked delivery rider Lao Liu in yellow reflective uniform and an anxious neighbor kick open a rusted security door; inside the dim apartment, an elderly man has collapsed on the floor. Lao Liu kneels down urgently performing CPR chest compressions, before paramedics rush up the stairwell with a stretcher. Raw documentary anime realism, 16:9.`
* **配音 / 画外音（VO）**：
  * **陆远（沉思独白）**：“楼道监控不会撒谎。在紧闭的防盗门前，他毫不犹豫地停下了奔跑的脚步，为一个素不相识的倒地老人抢回了生机。”
* **音效 & BGM**：
  * **音效**：监控回放快进与暂停的轻微蜂鸣声、剧烈的撞门声与急促的急救心跳仪声。

---

#### 镜头 09（系统报错·荒诞的参数红框）
* **镜头类型**：特写（Screen Close-up）
* **时长**：5 秒
* **AI 画面提示词（Prompt）**：
  > **中文**：电脑开发界面特写，陆远正在算法底层代码中输入“申诉原因：送餐破门抢救突发心梗独居老人”。回车之后，屏幕中间弹出一个巨大的刺目红框：“错误：底层未定义实体【见义勇为/紧急救助】。有效参数仅限【时空位移】【出餐时长】【路况拥堵指数】。判定：异常长时间滞留，违背系统全局最优效率，操作已被强制拦截！”  
  > **英文**：`Screen close-up, code editor backend. Lu Yuan types input: 'Reason: Rescued collapsed elderly resident with CPR during delivery'. Pressing enter triggers a harsh red dialog box: 'ERROR: Undefined Entity [Civic Heroism / Emergency Aid]. Valid variables restricted to [Distance, Latency, Traffic Index]. Flagged: Prolonged dwell violation. Request rejected: Violates Global Efficiency Optimum.' Cyberpunk anime coding aesthetic, 16:9.`
* **配音 / 画外音（VO）**：
  * **陆远（内心自嘲与愤怒）**：“算力能识别城市里的每一道窄门、每一个红绿灯，可在长达数百万行的代码里，居然容不下‘救人’两个字。”
* **音效 & BGM**：
  * **音效**：系统冷酷的弹窗报错蜂鸣音（Buzzer error sound）。

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
