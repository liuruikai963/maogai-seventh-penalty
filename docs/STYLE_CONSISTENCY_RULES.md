# 本地 Agent 生产铁律：全局视觉风格与人物一致性规范

> **适用范围**：微电影《第七张罚单》全片 23 镜头视频与图像生成  
> **核心原则**：**画风绝对统一，拒绝风格突变**

---

## 🚨 核心铁律（强制执行）

1. **绝对画风锚定（锁定为：新海诚高质感写实动漫 / 影视概念艺术）**：
   * **严禁真人实拍化**：严禁把角色渲染成三次元真人实拍皮肤质感；
   * **全片基调对齐**：必须与已成功定稿的 `assets/videos/shot_02_lao_liu_scooter_rain.mp4` 保持完全一致的二次元写实动漫质感（精致手绘感光影、赛璐珞高光、柔和动漫边缘）。

2. **每条提示词（Prompt）必带的风格硬性约束咒语**：
   未来提供的所有中英文提示词，必须在前置和后置强行注入以下锁风指令：
   * **中文必带锁**：
     > `【画风严格对齐要求】：必须严格保持与参考图片 100% 完全一致的“新海诚高质感写实动漫/影视概念艺术风格”！严禁改变画风，绝对严禁生成真人实拍质感！人物五官、发型、黑框眼镜及服饰必须与参考图完全一致。`
   * **英文必带锁**：
     > `Strict style consistency: Must strictly maintain the exact same Makoto Shinkai anime realism concept art style as the reference image. Absolutely NO photorealistic human skin, NO live-action film style. Consistent 2D/2.5D stylized anime aesthetics.`

3. **图生视频输入规范**：
   * 必须以 `assets/images/` 中已通过的 1080P 概念图作为首要参考底图；
   * 动作演算仅限在既定美术画风内进行物理流动，不破坏原生美术轮廓。
