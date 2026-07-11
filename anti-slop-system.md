# Anti-Slop System (分级 · 主体感知 · 模型感知)

> 本文件是所有 prompt-engine skill 共享的 anti-slop 契约。每个 skill 自带一份副本,
> 组装 Layer 10 时按本规范执行。设计依据见文末"实证来源"。

## 为什么分级(核心原理)

旧版把 anti-slop 写成"每次必附的一整块固定文案",禁掉了"过度饱和、HDR、镜头光效、
广告级鲜艳、glow"。问题:**这些恰恰是很多题材的刻意签名**——
- La La Land 的 lens flare/halation 是 Sandgren 明确追求的"poetic artifacts";
- Euphoria 选 65mm 就是为 halation 抵消数字锐利;
- Avatar/环太平洋的高饱和+自发光是 DP 主创的动机光签名;

且 AI 侧实测:**长通用负向清单有害**(SDXL 输出无菌化、抹细节;arXiv 证明过早施加负向会
"反向激活"、生成被否定物),**Flux 架构上根本不吃负向**(BFL 官方:no-op)。

结论:anti-slop 必须**三层**——通用核(始终) + 题材条款(按预设选一) + 模型策略(按架构改写)。

---

## Tier A — 通用核(所有题材始终附加,主体感知)

只保留真正跨题材、任何片种都是廉价感来源的项。**不含**饱和/HDR/flare/glow(这些全部下沉到 Tier B)。

**中文:**
> 避免:塑料感与 CG 渲染/游戏引擎质感、AI 式诡异对称、畸形或多指的手部、数字过度锐化、
> 无光源动机的全局均匀补光、无物理依据的全局雾化或平铺体积光。画面中每一处亮度都必须
> 有明确来源、方向与真实衰减;雾、烟、尘与可见光束必须有介质依据且不得抹除背景结构;
> 所有材质保留真实纹理与自然瑕疵。

**English:**
> Avoid: plastic / CGI / game-engine sheen, uncanny AI symmetry, malformed or extra-finger hands,
> digital over-sharpening, unmotivated flat global fill, physically unsupported global haze or flat
> volumetric light. Every value must have a clear source, direction and real falloff; fog, smoke,
> dust and visible shafts require a plausible medium and must preserve background structure; all
> materials keep authentic texture and natural imperfection.

**含人物时追加(仅当 Layer 1 有人类):**
> 追加:避免蜡质皮肤、美颜或磨皮效果;皮肤保留真实毛孔、瑕疵与 subsurface 通透感。
> (en: add — avoid waxy skin, beauty-filter/airbrush; keep real pores, blemishes, subsurface translucency.)

---

## Tier B — 题材条款(按预设题材,只追加一条)

按当前预设查下表,取对应 clause 追加到 Tier A 之后。**签名题材放行、克制题材才禁。**

| # | 题材桶 | 适用预设 | 条款(zh) | clause (en, 精简) |
|---|--------|---------|----------|------|
| G1 | 冷峻纪实/正剧 | tlou, succession, chernobyl, sicario, dark_knight, hbo_grey_epic | 保持低饱和克制;避免失控 HDR、广告级鲜艳、以及为炫技而生的浮夸镜头光效。 | low desaturated restraint; no runaway HDR, ad-grade vividness, show-off lens flare |
| G2 | 科幻史诗 | dune_caladan, dune_arrakis, interstellar_earth, dragon_epic(非发光时) | 去饱和但保留胶片高光滚降;仅在物理介质成立且光源明确时使用有方向、有衰减的体积光，真空场景改用轮廓光、遮挡与曝光分层;避免数字锐利感与蓝橙滤镜套路。 | desaturated with filmic highlight rolloff; volumetric light only with a plausible medium, motivated source and real falloff; in vacuum use rim light, occlusion and exposure separation; no digital crispness or teal-orange preset look |
| G3 | 胶片诗意/浪漫 | la_la_land, true_detective, romantic_hbo, titanic, barry_lyndon, in_the_mood | **放行**暖调 halation、柔和镜头光斑与轻微光学畸变(诗意瑕疵);避免数字锐利与均匀提亮;flare 须柔和且有来源。 | allow warm halation, soft flare, gentle optical distortion (poetic artifacts); no digital sharpness / uniform lift; flare stays soft & motivated |
| G4 | 霓虹/高对比发光 | euphoria, moonlight | **放行**高饱和彩色光溢出与 halation(抵消数字锐利);避免美颜、避免均匀提亮暗部(暗部应发光而非死平)。 | allow high-saturation color spill + halation; no beauty-filter, no uniform shadow lift (shadows glow, not flatten) |
| G6 | 恐怖/惊悚 | (按 mood=ominous/oppressive 触发) | **放行**大面积欠曝、死黑与低饱和;避免为提高可见度而补光,避免蓝绿滤镜一刀切套路(艳色仅作点缀:血红/信号灯)。 | allow heavy underexposure, crushed blacks, low sat; no fill-for-visibility, no blanket teal-green cliché |
| G7 | 动作大片 | (按写实动作场景触发) | **放行**胶片颗粒、暖怀旧调与深阴影;避免合成感光照与绿幕感;sun flare 仅在真实动机下出现。 | allow film grain, warm nostalgia, deep shadows; no synthetic lighting / greenscreen feel; sun flare only when motivated |

**纯场景(无主体)**:用 Tier A 但**跳过"含人物"追加句**(不提皮肤),再按预设加 Tier B。

---

## Tier C — 模型负向策略(按架构改写 Layer 10 形态)

Tier A+B 组好后,按目标模型把负向"表达形态"改写。这一层决定负向**怎么写**,不改**写什么**。

| 模型 | 策略 |
|------|------|
| **Flux / Flux Dev** | 架构不支持负向(no-op)。把 Tier A+B **改写成正向反面**:不写"避免 X",改成描述想要的正面(如"空无一人的街道""克制的低饱和""柔和有来源的高光")。 |
| **SDXL / SD1.5** | 支持负向,但"像盐不像酱"。只放 Tier A 的 3–5 个核心词 + 首轮渲染后**按观察到的具体缺陷**增量加 Tier B;禁百词通用清单(会无菌化、抹细节)。 |
| **Midjourney** | 去塑料感靠 `--style raw` + 摄影正向词。`--no` 只放**单个**最突出排除项(逐词解析,勿放短语);高 `--s` 会压过负向。 |
| **GPT Image** | 负向写成**散文**融入段落("避免…、保持…"),勿关键词堆叠。 |

---

## 组装规则(Layer 10 生成流程)

```
Layer 10 = Tier A(主体感知:纯场景略过皮肤句)
         + Tier B 中按当前预设选 1 条
         → 按目标模型用 Tier C 改写形态(Flux 转正向 / MJ 转 --no 单词 / GPT 转散文)
```

**铁律**:Tier B 与 Tier A 冲突时,**Tier B 题材条款优先**(它代表该片种的作者签名)。
例:G4/G5 放行的饱和与 glow,不受任何"避免过饱和"通用措辞约束——因为通用核里本就没有这一条。

---

## 实证来源(source-extraction 级,多为 ASC/BSC 一手,未经对抗验证)

- Deakins 论 HDR "has many issues"、反炫技、motivated lighting — britishcinematographer.co.uk / rogerdeakins.com
- Sandgren "poetic artifacts"(flare/畸变/halation 刻意保留)— filmmakermagazine.com
- Fraser《沙丘》skip-bleach 去饱和 + film-out 求胶片高光厚度 — cinematography.world / indiewire
- Avatar interactive lighting、高饱和+自发光签名(执行方 **Weta FX 非 ILM**)— theasc.com(官方)
- Rév《Euphoria》选 65mm 求 halation 抵消数字锐利 — theasc.com(官方)
- Navarro《环太平洋》极致高饱和+neon=作者签名 — britishcinematographer.co.uk
- Miranda《Top Gun: Maverick》胶片颗粒/暖怀旧/深阴影=签名,合成光=廉价 — theasc.com
- AI 负向:Flux 不支持负向(BFL 官方 docs.bfl.ml)、长清单有害(diffusedalice / arxiv 2406.02965)、"盐非酱"(sider.ai)、MJ `--no` 逐词解析(docs.midjourney.com)
