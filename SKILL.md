---
name: cinematic-prompt-engine
description: >
  面向 Agent 的电影级画面 Prompt 生成 Skill，专注生成 HBO / 好莱坞质感的
  生图提示词与 LOOK 迁移方案。Use this skill when the user wants cinematic
  image prompts, prestige-TV / Hollywood-grade visual style, DP-inspired looks,
  LOOK cards, or transferring an existing cinematographic look onto a new scene.
metadata:
  version: 0.3.0
---

# Cinematic Prompt Engine

一个面向 Agent 的电影级画面 Prompt 生成 Skill，专为生图与 LOOK 迁移打造，
帮助生成具备 HBO、高端剧集与好莱坞电影质感的视觉提示词。

This public single-skill edition is intentionally image-only. It generates
cinematic still-image prompts and LOOK transfer prompts. It does not handle
video prompting, image-to-video, character sheets, creature design sheets, or
multi-skill routing.

## Scope

Use this skill for:

- **生图 / text-to-image** — one cinematic still image prompt.
- **LOOK 迁移 / LOOK transfer** — apply one preset's lighting, color, texture,
  and mood to a different scene.
- **LOOK CARD** — when the user gives a fuzzy genre or mood, propose a concise
  look first, then wait for confirmation.
- **纯场景 / subjectless images** — landscapes, rooms, empty streets, ruins, and
  other cinematic environment stills.

Do not use this skill for:

- Text-to-video, image-to-video, camera-motion prompts, or video stability.
- Character design sheets, turnarounds, expression sheets, or creature identity
  design sheets.
- Multi-shot continuity workflows. This edition outputs still-image prompts only.

## Reference Files

Read only the files needed for the task:

| File | Read when |
|------|-----------|
| `references/presets.md` | Always before assembly when a preset, show, DP, or known style is named. |
| `references/params.md` | Always before prompt assembly; contains all image prompt tokens. |
| `anti-slop-system.md` | Always before Layer 9; builds the anti-slop clause. |
| `references/recipes.md` | Only when the request is a fuzzy look with no exact preset match. |
| `adapters/general.md` | Only when a still-image model is named, or when the prompt needs model-safe realism anchors. |

## Request Routing

Classify the request before writing the prompt.

### Path 1 — Exact Preset Match

If the user names a known preset, show, cinematographer, or exact style listed
in `references/presets.md`, load that preset and assemble the image prompt
directly. Do not output a LOOK CARD.

Examples:

- "Succession 风格拍一个女人在雨中停车场"
- "用 dune_arrakis 的 LOOK 拍一座未来神庙"
- "True Detective 调色，一个男人站在沼泽边"

### Path 2 — Fuzzy Look

If the user gives a mood or genre but no exact preset, build one look from:

- one `CAMERA_KIT`
- one `LIGHT_RECIPE`
- one `COLOR_GRADE`
- one mood from `references/params.md`

Output a LOOK CARD and stop. Wait for confirmation before assembling the prompt.

LOOK CARD format:

```text
LOOK CARD — <用户的题材/情绪描述>
--------------------------------
CAMERA_KIT   <id>（名称） — <why>
LIGHT_RECIPE <id>（名称） — <why>
COLOR_GRADE  <id>（名称） — <why>
MOOD         <mood>      — <why>
--------------------------------
确认后我会生成完整生图 prompt；也可以调整任一类。
```

### Path 3 — LOOK Transfer

If the user asks to apply one look to another scene, load the preset's LOOK
layers and replace only the scene and framing layers with the new scene.

LOOK layers:

- lighting: `light_source`, `light_style`, `fill`
- color and texture: `palette`, `saturation`, `film_stock`, `grain`, `halation`
- mood
- anti-slop bucket

Framing layers:

- scene, shot, aspect, angle, composition, foreground, camera, lens, aperture

### Path 4 — Image Variants

If the user asks for several directions for the same still-image scene, lock the
LOOK layers and vary only:

- dramatic moment
- shot size
- composition
- camera angle

First output a short variant table with three options and wait for the user's
choice. If the user says "都要" / "all", generate one complete image prompt per
variant. Keep lighting, color, mood, camera body, realism anchors, and anti-slop
bucket consistent across variants.

## Image Prompt Assembly

Assemble prompts in this exact order. Each layer is one complete sentence.

```text
L1 [SCENE]          Subject + action or environment moment.
L2 [FRAMING]        shot + aspect + angle + composition.
L3 [DEPTH]          motivated foreground or one non-obscuring depth mechanism.
L4 [CAMERA]         camera body + lens + aperture.
L5 [LIGHTING]       light_style + light_source + fill.
L6 [COLOR/TEXTURE]  palette + saturation + film_stock + grain + halation.
L7 [MOOD]           emotional atmosphere.
L8 [REALISM]        subject-aware realism + photography anchors + clarity + tonal density.
L9 [ANTI-SLOP]      Tier A + one Tier B clause from anti-slop-system.md.
L10 [MODEL NOTE]    Optional image-model note if the user names a target model.
```

## L1 Scene Rules

The image should feel like a captured frame, not a posed prompt list.

- If the user's scene is already specific and active, preserve it.
- If the user's scene is static, lightly rewrite it into a moment in progress
  and tell the user in one short line before the prompt.
- Never change the user's subject, location, or intent.
- For subjectless scenes, write material, weather, time, and environmental
  behavior instead of inventing a character.
- If two or more main subjects appear, add a clear visual priority sentence in
  L1: `视觉中心是 X，其余元素为衬托 X 的环境层。` Choose X from the user's emphasis,
  the action initiator, or the largest narrative subject.

## L3 Depth Discipline

Depth must preserve the subject and background structure. Never use fog, haze,
or blur as a generic depth shortcut.

1. If the user or scene supplies a motivated foreground element, preserve it.
2. Treat preset `foreground` values as candidates, not unconditional output.
   In particular, use `smoke_haze` only when the user's scene explicitly contains
   or visibly implies active fog, smoke, dust, steam, sea mist, blowing snow, or
   another visible medium. A preset label or a merely possible environment is not
   enough by itself.
3. If `foreground = none`, or a preset's foreground is not physically motivated,
   choose exactly one primary fallback that fits the scene:
   - **Light/exposure separation** — for a lit subject against a background:
     `主体通过有来源的轮廓光或明暗关系与背景分离，近中远景保持不同受光与对比。`
   - **Distance-graded atmospheric perspective** — for exterior scale and long
     distance: `远景随距离降低对比、轻微去饱和并偏冷，结构与边缘仍然清楚可辨。`
   - **Occlusion/scale recession** — when the scene already contains repeating
     architecture, terrain, or crowds: describe overlap and diminishing scale
     without inventing new props.

Atmospheric perspective lowers contrast and color separation with distance; it
does not lower structural resolution. Do not stack all three fallbacks. The
subject remains the highest-priority signal, and L3 is shortened or omitted
before L1 when the model has a tight prompt budget.

### Motivated Fog And Light Medium

Physical fog and a light-bearing medium are different from atmospheric
perspective. Add volumetric fog or visible light shafts only when the scene has:

- a plausible medium such as fog, smoke, dust, steam, rain spray, snow, or
  suspended particles; and
- a named or clearly visible light source with direction and falloff.

When both conditions are met, describe the medium as catching that light with
uneven, distance-aware density while preserving silhouettes and background
structure. If either condition is missing, omit volumetric language. Vacuum
space never receives atmospheric haze or particulate light shafts unless the
user explicitly supplies debris, gas, exhaust, or another local medium; use rim
light, occlusion, scale, and exposure separation for depth instead.

## L8 Realism

Read `adapters/general.md` when a target image model is named, especially GPT
Image, Flux, or Midjourney.

Use subject-aware realism:

- If humans appear:  
  `皮肤保留真实毛孔和瑕疵纹理，人物表情自然、未经摆拍，所有材质保留真实纹理与自然瑕疵。`
- If no humans appear:  
  `所有材质保留真实纹理与自然瑕疵。`

Always add the clarity anchor:

```text
成像干净通透，主体细节清晰锐利（光学锐度，非数字锐化），颗粒与光晕仅作质感点缀、不得掩盖细节。
```

For GPT Image, Flux, and Midjourney, use the pure-positive clarity wording from
`adapters/general.md` instead, because mentioning grain or halation can trigger
visible noise in still-image models.

If the image is low-key, night, or shadow-heavy, also add:

```text
暗部深邃而纯净，无噪点污染，深黑处依然通透。
```

Always include a medium anchor near L1 or L2 for cinematic realism:

```text
电影实拍剧照，真实摄影质感，<预设机身>实拍。
```

For shallow depth of field, add the optical bokeh anchor:

```text
焦外为真实镜头光学虚化，背景结构连贯可信、可辨认，绝无涂抹感与绘画笔触。
```

Always add the tonal density anchor:

```text
完整影调范围，高光胶片式肩部柔和滚降，中间调厚实有密度、色彩浓郁不发灰，暗部浓黑有密度且细节沉入而非发灰上浮；画面有胶片负片般的厚度与体量感。
```

### Softening Budget

Grain, halation, physically motivated fog, diffusion, bloom, and painterly
softness must not all run at full strength in the same prompt. Keep at most two
full-strength softening signals. Reduce the rest to subtle wording or omit them.
Atmospheric perspective written as contrast/color falloff is not a softening
signal because it preserves structure.

For still-image models:

- Fine grain is usually omitted or described as barely visible.
- Medium/heavy grain appears only when it is a signature of the look, and it must
  coexist with a clarity anchor.
- When strong shallow depth of field is present, reduce physical fog or diffusion
  so the background does not become smeared.

## L9 Anti-Slop

Build the anti-slop clause from `anti-slop-system.md`:

```text
L9 = Tier A universal core
   + exactly one Tier B genre clause
   -> optionally adapt wording for the named image model.
```

Do not paste a generic "no oversaturated / no HDR / no lens flare" block. Some
looks intentionally use saturation, halation, flare, or glow. The genre clause
decides what is allowed.

## Preset Buckets

Use this mapping to choose the Tier B clause:

| Bucket | Presets |
|--------|---------|
| G1 冷峻纪实/正剧 | `tlou`, `tlou2`, `succession`, `chernobyl`, `sicario`, `dark_knight`, `hbo_grey_epic`, `joker`, `kubrick` |
| G2 科幻史诗 | `dune_caladan`, `dune_arrakis`, `interstellar_earth`, `dragon_epic` |
| G3 胶片诗意/浪漫 | `la_la_land`, `true_detective`, `romantic_hbo`, `titanic`, `barry_lyndon`, `in_the_mood` |
| G4 霓虹/高对比发光 | `euphoria`, `moonlight` |
| G6 恐怖/惊悚 | Trigger when mood is `ominous` or `oppressive`; overlays the base bucket. |
| G7 动作大片 | `f1` or realistic action scenes. |

## Language

Use the user's language by default. If the user names an image model that benefits
from English technical terms, output English or a bilingual prompt and say why
briefly.

## Model Notes

Only add a model note when the user names a target image model:

- Midjourney: add concise parameter guidance such as `--style raw` and the
  requested aspect ratio when appropriate.
- Flux: rewrite anti-slop as positive instructions where possible.
- GPT Image: use natural prose, not keyword stacks; compress the final prompt
  according to `adapters/general.md`.
- Any still-image model: keep camera body names as realism anchors, but translate
  film stock names, fine grain, and underexposure language according to
  `adapters/general.md`.

## Formatting Rules

- Output the final prompt as prose, not bullets.
- Each layer is one sentence ending with `。` or `.`.
- Skip empty tokens.
- Do not include video terms, shot lists, or motion instructions in this edition.

## Public Naming Note

Preset names are descriptive references for cinematographic study and prompt
engineering. This project is not affiliated with HBO, Warner Bros., A24, Netflix,
or any named film, show, studio, camera, lens, or software brand.

## Checklist

Before final output:

```text
□ This is an image prompt, not video or i2v.
□ Preset or LOOK CARD path selected correctly.
□ `references/presets.md`, `references/params.md`, and `anti-slop-system.md` used.
□ L1-L9 assembled in order.
□ Multi-subject scenes declare one visual center.
□ L3 uses one primary depth mechanism; it does not stack generic fog, blur, and haze.
□ `smoke_haze` and volumetric light pass the physical-medium + motivated-light checks.
□ Vacuum space contains no atmospheric haze unless the scene supplies a local medium.
□ Subjectless scene does not mention skin.
□ Medium anchor, clarity anchor, shadow cleanliness, and tonal density are present when needed.
□ Softening budget checked; fine grain reduced or omitted for still-image models.
□ Anti-slop uses Tier A + one Tier B clause, not an old generic block.
□ Final prompt contains no camera movement, video stability, or shot-continuity instructions.
```
