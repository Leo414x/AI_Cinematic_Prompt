# Parameter Reference — Full Token Library

Each parameter axis lists all available options with their Chinese and English
prompt tokens. When assembling a prompt, look up the selected option and insert
its token verbatim into the corresponding layer.

If a token is empty string (`""`), skip it entirely — do not insert a blank.

---

## 1. shot — 景别

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| establishing | 建立镜头 | 建立镜头，展示整体环境与时间氛围，人物极小或不可见 | establishing shot, full environment with atmosphere, subject barely visible |
| extreme_wide | 大远景 | 大远景，人物在画面中极其渺小，被环境吞没 | extreme wide shot, subject dwarfed by environment |
| wide | 远景 | 环境远景，人物在画面中占比很小，环境交代完整 | wide shot, subject small in frame, full environment context |
| medium_wide | 中远景 | 中远景，人物膝部以上可见，可见肢体语言与环境关系 | medium wide shot, knees up, body language in context |
| cowboy | 牛仔景 | 牛仔景，大腿中部以上取景，紧张对峙感 | cowboy shot, mid-thigh up, confrontational framing |
| medium | 中景 | 中景，腰部以上，对话和互动的标准取景 | medium shot, waist up |
| medium_close | 中近景 | 中近景，胸部以上，可见微妙表情 | medium close-up, chest up, subtle expression visible |
| close | 近景 | 近景特写，面部占据画面主要区域，情绪主导 | close-up, face fills frame, emotion-driven |
| extreme_close | 大特写 | 极致特写，仅见眼睛、嘴唇或手部细节 | extreme close-up, eyes, lips, or hand detail only |
| insert | 插入镜头 | 插入镜头，特写某个关键物件或细节（手表、信件、伤口） | insert shot, close detail of key object (watch, letter, wound) |
| two_shot | 双人景 | 双人景，两个人物同时在画面中，关系张力 | two-shot, both subjects in frame, relational tension |
| pov | 主观视角 | 第一人称主观镜头，观众即角色的视角 | POV shot, first-person perspective, audience as character |

---

## 2. aspect — 画幅

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| 2.39 | 2.39:1 宽银幕 | 2.39:1 宽银幕画幅 | 2.39:1 anamorphic widescreen |
| 2.0 | 2:1 Univisium | 2:1 Univisium 画幅 | 2:1 Univisium aspect ratio |
| 1.85 | 1.85:1 学院宽 | 1.85:1 学院宽银幕 | 1.85:1 Academy widescreen |
| 16:9 | 16:9 | 16:9 画幅 | 16:9 aspect ratio |
| 4:3 | 4:3 经典 | 4:3 经典学院画幅 | 4:3 Academy ratio |
| 9:16 | 9:16 竖屏 | 9:16 竖屏画幅 | 9:16 vertical frame |
| 2.55 | 2.55:1 CinemaScope 经典 | 2.55:1 经典 CinemaScope 画幅，比标准宽银幕更宽，好莱坞黄金时代比例 | 2.55:1 classic CinemaScope, wider than standard anamorphic, golden-age Hollywood ratio |
| 1.66 | 1.66:1 欧洲宽银幕 | 1.66:1 欧洲宽银幕画幅 | 1.66:1 European widescreen |

---

## 3. composition — 构图

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| thirds_negative | 三分法+留白 | 三分法构图，大面积负空间留白 | rule of thirds, deep negative space |
| centered | 居中 | 人物居中构图 | centered framing |
| symmetry | 对称一点透视 | 严格对称构图，一点透视，纵深线条向灭点汇聚 | symmetrical composition, one-point perspective, converging lines |
| off_center | 偏置抓拍 | 人物偏置于画面一侧，如同纪录片抓拍 | off-center framing, documentary candid |
| over_shoulder | 过肩 OTS | 过肩镜头构图，前景人物肩部虚化 | over-the-shoulder framing, foreground shoulder out of focus |
| dutch | 荷兰角 | 轻微倾斜的荷兰角构图，不安感 | subtle Dutch angle, sense of unease |
| frame_in_frame | 框中框 | 框中框构图，人物被窗户、门框、镜子或建筑结构自然框住 | frame-within-frame, subject enclosed by window, doorway, mirror, or architectural element |
| depth_staging | 纵深调度 | 用遮挡、尺度递减或分层受光组织已有的前中后景，保持背景结构可辨，不自动添加雾气 | depth staging through occlusion, scale recession, or layered exposure; preserve legible background structure and do not add fog by default |
| leading_lines | 引导线 | 强烈的引导线构图，走廊、铁轨、公路或建筑线条将视线引向主体 | strong leading lines — corridor, rails, road, or architecture guiding eye to subject |
| looking_room | 视线空间 | 人物面朝的方向留出大面积视线空间，背后紧贴画框边缘 | generous looking room ahead of subject's gaze, tight framing behind |
| voyeur_obscured | 窥探式遮挡 | 镜头被门框、墙壁、家具或物件部分遮挡，如同从隐蔽处偷窥，角色常被推到画面边缘，观众感觉在窥探一个不该看到的私密时刻 | camera partially obscured by doorframes, walls, furniture or objects, as if spying from a hidden vantage point, characters often pushed to frame edges, viewer feels they are witnessing a private moment they shouldn't see |
| tableau_painterly | 油画画框式 | 18世纪油画式对称构图，人物和场景排布如同画框内的古典画作，构图极端工整但不僵硬 | 18th-century painterly tableau composition, figures and scene arranged as if within a classical painting frame, extremely composed yet alive |

---

## 4. angle — 机位角度

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| eye_level | 平视 | 平视机位，与人物视线齐平，客观中性 | eye-level angle, neutral and objective |
| low | 仰拍 | 低角度仰拍，赋予人物力量感和压迫性 | low angle, empowering, imposing presence |
| slight_low | 微仰 | 轻微仰拍，微妙地增加人物份量感 | slightly low angle, subtly aggrandizing |
| high | 俯拍 | 高角度俯拍，人物显得渺小、脆弱或被审视 | high angle, diminishing, vulnerable, observed |
| overhead | 鸟瞰 | 正上方俯视，几何感强烈的鸟瞰视角 | overhead bird's-eye view, geometric, detached |
| worms_eye | 虫视角 | 极低虫视角，从地面仰望，极端戏剧性 | worm's-eye view, looking up from ground level, extreme drama |

---

## 5. foreground — 前景纵深

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| none | 无前景 | *(skip)* | *(skip)* |
| shoulder | 肩部/身体 | 前景有虚化的人物肩部或身体局部遮挡 | out-of-focus shoulder or body in foreground, partially obscuring |
| doorframe | 门框/窗框 | 透过门框或窗框拍摄，自然的画中画框架 | shot through doorway or window frame, natural vignetting |
| foliage | 植物/树叶 | 前景有虚化的树叶或植物枝叶 | soft-focus foliage or leaves in foreground |
| glass | 玻璃/反射 | 透过玻璃拍摄，表面带有微弱反射和折射 | shot through glass, faint reflections and refraction |
| rain_condensation | 雨水/水雾 | 前景是带有雨滴或水雾凝结的玻璃表面 | rain-streaked or condensation-covered glass in foreground |
| bars_fence | 栏杆/铁丝网 | 透过栏杆、铁丝网或栅栏拍摄，暗示禁锢 | shot through bars, fence, or grating, implying confinement |
| smoke_haze | 烟雾/薄雾（条件） | 仅当场景确有雾、烟、沙尘、蒸汽、喷雾或风雪时使用；介质分布不均并承接明确光源，保持主体轮廓与背景结构可辨 | conditional physical fog, smoke, dust, steam, spray, or snow; uneven density catches a motivated light while subject silhouette and background structure remain legible |
| object | 道具/物件 | 前景有虚化的道具或物件（杯子、文件、武器） | out-of-focus prop in foreground (cup, papers, weapon) |

---

## 6. camera — 机身

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| alexa_lf | Alexa LF | Arri Alexa LF 大画幅摄影机质感 | Arri Alexa LF large format |
| alexa_mini | Alexa Mini | Arri Alexa Mini 摄影机质感 | Arri Alexa Mini |
| red_v_raptor | RED V-Raptor | RED V-Raptor 8K 质感 | RED V-Raptor 8K |
| sony_venice | Sony Venice | Sony Venice 双感光元件质感 | Sony Venice 2 |
| film_35mm | 35mm 胶片 | 35mm 胶片摄影机实拍 | shot on 35mm film |
| film_16mm | 16mm 胶片 | 16mm 胶片摄影机实拍，粗糙纪录片质感 | shot on 16mm film, raw documentary texture |
| sony_venice2 | Sony VENICE 2 | Sony VENICE 2 全画幅数字质感，高动态范围，干净通透 | Sony VENICE 2 full-frame digital, high dynamic range, clean and transparent |
| alexa_65 | Alexa 65 | Arri Alexa 65 大画幅数字，浅景深，无广角畸变的亲密感 | Arri Alexa 65 large-format digital, shallow depth of field, distortion-free intimacy |

## 7. lens — 镜头

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| anamorphic_40 | 变形 40mm | 40mm 变形宽银幕镜头，椭圆散景，水平光晕 | Panavision anamorphic 40mm, oval bokeh, horizontal flare |
| anamorphic_75 | 变形 75mm | 75mm 变形宽银幕镜头，椭圆散景 | anamorphic 75mm, oval bokeh |
| spherical_24 | 球面 24mm | 24mm 球面广角镜头 | spherical 24mm wide angle |
| spherical_35 | 球面 35mm | 35mm 球面镜头 | spherical 35mm |
| spherical_50 | 球面 50mm | 50mm 标准球面镜头 | spherical 50mm standard |
| telephoto_85 | 85mm 人像 | 85mm 人像镜头，柔和散景 | 85mm portrait lens, soft bokeh |
| telephoto_135 | 135mm 长焦 | 135mm 长焦镜头，空间压缩感 | 135mm telephoto, spatial compression |
| telephoto_200 | 200mm 长焦 | 200mm 长焦镜头，强烈空间压缩，背景极度虚化 | 200mm telephoto, heavy compression, extreme background blur |

## 8. aperture — 光圈

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| T0.7 | f/0.7 NASA（极限浅景深） | f/0.7 极限大光圈，景深接近于零，仅约1-2厘米范围内合焦，画面柔软如油画，高光区域强烈溢出 | f/0.7 extreme aperture, near-zero depth of field, only 1-2cm in focus, image soft as oil painting, intense highlight bloom |
| T1.4 | T1.4 | T1.4 大光圈，极浅景深 | T1.4, extremely shallow depth of field |
| T2 | T2 | T2 光圈，浅景深 | T2, shallow depth of field |
| T2.8 | T2.8 | T2.8 光圈，浅景深 | T2.8, shallow depth of field |
| T4 | T4 | T4 光圈，中等景深 | T4, moderate depth of field |
| T5.6 | T5.6 | T5.6 光圈，深景深保持环境清晰 | T5.6, deep focus |


---

## 9. light_source — 光源

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| overcast_window | 阴天窗光 | 阴天窗户的冷灰色漫射光 | cold overcast window light, diffused |
| warm_window | 暖调窗光 | 温暖的午后阳光从窗户斜射入 | warm afternoon sunlight through window |
| practical_lamp | 台灯/壁灯 | 画面中的台灯或壁灯作为唯一光源 | practical lamp as sole light source |
| fluorescent | 荧光灯管 | 头顶荧光灯管发出惨白偏绿的冷光 | overhead fluorescent tubes, sickly green-white |
| golden_hour | 黄金时刻 | 黄金时刻的低角度暖光与长阴影；仅当场景明确有尘、雾或喷雾时才写可见光束 | golden-hour low-angle warm light and long shadows; add visible shafts only when the scene explicitly contains dust, fog, or spray |
| overcast | 阴天漫射 | 厚云层下均匀的冷灰漫射光 | heavy overcast, flat cool ambient light |
| moonlight | 月光 | 冷蓝色月光透过窗户 | cold blue moonlight through window |
| neon | 霓虹/招牌 | 城市霓虹灯和招牌的混合彩色光 | mixed neon and signage light, urban color spill |
| candle_fire | 烛火/壁炉 | 烛光或壁炉火焰的暖橙色跳动光源 | candlelight or firelight, warm flickering orange |
| candle_only | 纯烛光（零人工光） | 完全且仅由蜡烛照明，零人工灯光，画面仅靠烛火的暖光和其在墙壁天花板上的反射照亮 | lit exclusively by candles, zero artificial light, illumination solely from candle flames and their reflections on walls and ceilings |
| hard_sun | 赛道硬阳光 | 赛道直射硬阳光，高对比硬阴影 | harsh direct trackside sunlight, high-contrast hard shadows |
| sodium_vapor | 钠灯脏橙 | 钠灯路灯的肮脏橙色辉光，病态衰败的都市光 | dirty orange sodium-vapor streetlight glow, sickly decaying urban light |

## 10. light_style — 布光风格

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| naturalistic | 自然主义 | 低调自然主义布光，光源有明确动机 | low-key naturalistic lighting, motivated sources |
| chiaroscuro | 明暗对比 | 伦勃朗式明暗对比，面部一半沉入阴影 | chiaroscuro, Rembrandt lighting, half face in shadow |
| low_key | 低调光 | 低调暗光，大面积阴影，仅关键区域受光 | low-key, predominantly shadow, selective highlights |
| available | 可用光 | 完全依赖现场可用光，无额外补光 | available light only, no additional lighting |
| silhouette | 剪影 | 逆光剪影，人物轮廓清晰但面部不可见 | backlit silhouette, figure outlined against light |
| top_light | 顶光 | 头顶直射光，眼窝和下巴形成深沉阴影 | top-down light, deep eye socket and chin shadows |

## 11. fill — 补光比

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| no_fill | 无补光 | 无补光，保留深沉的阴影层次 | no fill light, retained deep shadows |
| minimal | 极少补光 | 极少量补光，暗部仅保留隐约细节 | minimal fill, faint shadow detail |
| moderate | 适度补光 | 适度补光，阴影仍明显但不压抑 | moderate fill, visible but present shadows |

## 12. palette — 色调

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| desaturated_earth | 去饱和大地色 | 去饱和的大地色调，暗部偏深棕 | desaturated earth tones, dark brown shadows |
| cold_corporate | 冷蓝灰企业 | 冷蓝灰色调，带有轻微的青色偏移 | cold blue-grey palette, slight cyan shift |
| sickly_green | 病态青绿灰 | 病态的青绿灰色调，几乎完全去饱和 | sickly green-grey, almost fully desaturated |
| warm_golden | 南方金黄 | 温暖但不饱和的金黄色调，像被旧茶水浸泡 | warm but muted golden, like steeped in old tea |
| cool_neutral | 冷中性 | 冷中性色调，微微偏蓝 | cool neutral palette, slight blue undertone |
| neon_contrast | 霓虹对比 | 霓虹彩色光与深沉暗部的强对比 | neon color spill against deep blacks |
| bleach_bypass | 漂白跳过 | 漂白跳过效果，高对比低饱和，银色金属质感 | bleach bypass, high contrast, metallic silver tones |
| infrared_silver | 红外银白（沙丘） | 红外摄影质感的银白色调，沙漠呈铂金色而非金色，皮肤苍白如大理石，天空深暗，整体有不属于地球的异世界色彩偏移 | infrared-photography silver palette, desert platinum not golden, marble-pale skin, deep dark sky, otherworldly color shift as if seen through infrared filter |
| magic_hour_vivid | 魔幻时刻鲜艳 | 胶片增强的鲜艳色彩，金粉蓝紫的魔幻时刻天空色，饱和但柔和而非数字锐利 | film-enhanced vivid color, golden-pink-blue-purple magic hour sky, saturated but soft, not digitally sharp |
| warm_cold_split | 冷暖双色温对立 | 暖琥珀色实用光与冰冷蓝色环境光的强烈对立，两种色温在同一画面中并存 | warm amber practicals against cold blue ambient fill, two opposing color temperatures coexisting in frame |
| dual_earth_space | 双模式（地球暖/太空冷） | 地球段落为温暖琥珀农业色调，太空段落为冷蓝黑临床色调，两套色调随叙事切换 | Earth segments warm amber agricultural tones, space segments cold blue-black clinical, dual palette switching with narrative |
| moonlight_glow | 月光发光色 | 高饱和高对比的色彩，暗部不死黑而是带有微妙的色彩光泽——"发光的黑"，暖金内景与冷蓝外景交替，黑色皮肤呈现温暖的深色光泽 | high-saturation high-contrast palette, shadows glow rather than go dead black, warm golden interiors alternating with cool blue exteriors, dark skin rendered with warm luminous sheen |
| candlelight_painting | 烛光油画 | 纯烛光照明的暖琥珀金色调，暗部极深但不死黑，高光区域有蜡烛火焰的跳动暖光，整体画面如同17-18世纪荷兰/英国油画 | pure candlelight warm amber-gold palette, deep shadows but not dead black, highlights flickering with candle flame warmth, overall image resembling 17th-18th century Dutch/English oil painting |
| wkw_jewel | 王家卫宝石色 | 以深红色为主导的宝石色调——旗袍的红、壁纸的红、窗帘的红代表被压抑的欲望，搭配深绿和暗金，饱和但深沉而非明亮 | jewel-tone palette dominated by deep red — red of qipao, red of wallpaper, red of curtains representing suppressed desire — paired with deep green and dark gold, saturated but moody not bright |
| overcast_green_grey | 阴天绿灰 | 阴天绿灰色调，苔藓般的冷绿与湿灰 | overcast green-grey, mossy cold green and damp grey |
| blood_red_system | 血红系统 | 血红图像系统主导，暗红渗透（地下/暴怒） | blood-red image system, dark red saturation bleeding through (underground/rage) |
| trauma_blue_system | 创伤蓝系统 | 创伤蓝图像系统，冷蓝渐次渗入累积 | trauma-blue image system, cold blue creeping in and accumulating |
| flashback_golden | 闪回暖金 | 回忆金色暖调，柔和琥珀阳光 | flashback golden warmth, soft amber sunlight |
| sun_drenched_natural | 阳光自然色 | 阳光直射的自然色，暖中性沥青与蓝天，车队涂装点缀 | sun-drenched natural, warm-neutral tarmac and blue sky with livery accents |
| joker_antique_teal_orange | 做旧青橙 | 做旧的青橙互补，不纯的暖青与红棕橙，底子灰暗渐转鲜艳混乱 | antique teal-orange complementaries, impure warm teal and reddish-brown orange, grim base turning vivid and chaotic |

## 13. saturation — 饱和度

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| very_low | 极低 | 几乎完全去饱和，接近黑白 | nearly desaturated, approaching monochrome |
| low | 低饱和 | 低饱和度，色彩克制 | low saturation, restrained color |
| moderate | 适度 | 适度饱和，自然但不鲜艳 | moderate saturation, natural but not vivid |

## 14. film_stock — 胶片模拟

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| kodak_500t | Kodak 500T | 柯达 Vision3 500T 胶片色彩模拟 | Kodak Vision3 500T film emulation |
| kodak_250d | Kodak 250D | 柯达 Vision3 250D 日光胶片模拟 | Kodak Vision3 250D daylight emulation |
| fuji_eterna | Fuji Eterna | 富士 Eterna 低对比柔和胶片模拟 | Fuji Eterna, low contrast, soft emulsion |
| kodachrome | Kodachrome | Kodachrome 浓郁复古色彩 | Kodachrome, rich vintage color |
| kodak_100t | Kodak 100T（极慢细颗粒钨丝灯） | 柯达 100T 极慢感光度钨丝灯胶片，颗粒极细但需要极大量光线，增冲处理后画面柔化颗粒增粗，适合烛光/极限低光场景 | Kodak 100T ultra-slow tungsten stock, extremely fine grain but demands massive light, push-processed yields softer image with increased grain, suited for candlelight and extreme low-light |
| kodak_800t | Kodak 800T（超高感光度暗光） | 柯达 Vision 800T 超高感光度钨丝灯胶片，专为极暗实用光源设计，颗粒比500T更粗更明显，暗部有独特的颗粒发光质感 | Kodak Vision 800T ultra-fast tungsten stock, designed for extremely dim practical sources, coarser grain than 500T, shadow grain has distinctive luminous texture |
| period_stock_green | 80s柯达绿 | 数字调色模拟80年代柯达胶片，暗部与高光推入绿色 | digital graded to emulate 1980s Kodak stock, green pushed into shadows and highlights |
| none | 无 | *(skip)* | *(skip)* |

## 15. grain — 颗粒

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| fine | 细腻 | 极轻微、几乎不可见的胶片颗粒，不掩盖细节 | subtle, barely perceptible film grain that never obscures detail |
| medium | 中等 | 中等胶片颗粒，质感明显 | visible film grain, textured |
| heavy | 粗颗粒 | 粗重的胶片颗粒，16mm 纪录片般的粗糙感 | heavy grain, raw 16mm documentary texture |
| none | 无 | *(skip)* | *(skip)* |
| pull_processed | 减冲柔化颗粒 | 胶片减冲一档处理，颗粒更细腻，反差更柔和，画面带有梦幻般的柔和感 | one-stop pull-processed film, finer grain, softer contrast, dreamy softness |
| pushed_soft | 增冲柔化（油画感） | 胶片增冲处理产生的明显颗粒和光学柔软度，画面柔和到接近油画质感，边缘不锐利 | push-processed grain with optical softness, image soft enough to resemble oil painting, edges never sharp |

## 16. halation — 高光溢出

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| none | 无 | *(skip)* | *(skip)* |
| subtle | 微弱光晕 | 微弱的高光溢出光晕 | subtle halation, soft highlight bloom |
| warm | 暖调光晕 | 暖色调的高光溢出，胶片感 | warm halation, filmic highlight glow |

## 17. mood — 情绪

| ID | Label | zh token | en token |
|----|-------|----------|----------|
| tense | 紧张 | 紧张不安的氛围 | tense, uneasy atmosphere |
| melancholic | 忧郁 | 安静的忧郁感 | quiet melancholy |
| ominous | 不祥 | 隐约的不祥预感 | subtle sense of dread |
| intimate | 私密 | 私密亲近的氛围 | intimate, close atmosphere |
| clinical | 冷漠临床 | 临床般的冷漠与客观 | clinical detachment |
| dreamy | 迷离 | 梦幻、空灵，以柔和高光过渡表达，不自动添加雾气 | dreamy and ethereal with gentle highlight transitions; do not add fog by default |
| oppressive | 压抑 | 令人窒息的压抑感 | suffocating, oppressive |
| contemplative | 沉思 | 沉静思索的氛围 | contemplative stillness |
| exhilarating | 亢奋热血 | 高速肾上腺素的兴奋感，紧张而热血 | high-velocity adrenaline thrill, tense and exhilarating |
