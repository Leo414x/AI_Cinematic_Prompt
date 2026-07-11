# General Image Model Adapter

## Scope

Use this adapter when the user names Midjourney, Flux, GPT Image, or an
unspecified still-image model.

This file is image-only. It does not add video movement, sound design, first-frame
animation, or shot-continuity instructions.

## Image Model Noise-Fuse Terms

For GPT Image, Flux, and Midjourney, some cinematography terms can accidentally
trigger dirty noise, scanned-film artifacts, or muddy shadows. Translate or omit
them before final prompt assembly.

| Fuse term | Image prompt handling |
|-----------|-----------------------|
| Specific film stock names such as `Kodak 500T`, `250D`, `Vision3` | Translate into visible color behavior, such as "tungsten-balanced warm color science with gentle highlight roll-off". Do not keep the stock model name. |
| `film emulation`, `胶片模拟`, `胶片质感` | Omit, or fold into color science and highlight roll-off language. |
| `grain / 颗粒` at fine level | Omit for image models unless grain is the signature of the look. If retained, describe it as extremely subtle. |
| `underexposed`, `crushed blacks`, `欠曝`, `暗部厚重` | Rewrite as clean deep shadows: "dark areas are deep yet clean, with detail sinking into black without dirty noise". |
| Clarity anchor | Use a pure-positive version: "clean transparent imaging, crisp optical detail, deep clean shadows". Avoid mentioning grain or halation inside the clarity sentence. |

Camera bodies such as Alexa 65, Alexa LF, VENICE 2, and Alexa Mini are not noise
fuse terms. Keep the camera body as a realism anchor.

## Depth And Atmosphere Fuse Terms

Still-image models often interpret vague fog language as a flat milky blur that
erases the background. Translate depth intent into a visible mechanism before
final assembly.

| Input intent | Image prompt handling |
|--------------|-----------------------|
| `atmospheric haze`, `fog`, `misty`, `雾`, `朦胧` used only to make the background feel deep | Replace with distance-graded atmospheric perspective: far planes lose contrast, slightly desaturate and cool, while silhouettes, edges, and structure remain legible. Do not retain fog words. |
| Real fog, smoke, dust, steam, spray, or snow exists in the scene | Keep the physical medium, but name its source or context, uneven density, and the light it catches. It must not become a flat overlay. |
| Visible volumetric light | Require both a plausible medium and a motivated light source. State direction and falloff; preserve the subject silhouette and background structure. |
| Vacuum space or a clean sealed environment | Do not add atmospheric haze or particulate shafts. Use rim light, occlusion, scale recession, and exposure contrast unless the user supplies a local gas, exhaust, dust, or debris medium. |

Prefer one primary depth mechanism. Light/exposure separation is the safest
default for a subject; distance-graded contrast/color falloff is the safest
default for exterior scale. Do not stack fog, shallow depth of field, diffusion,
and bloom to solve the same depth problem.

## Photography Anchors

All still-image prompts should preserve photographic realism even when noise terms
are removed.

1. **Medium anchor** — place near L1 or L2:
   `电影实拍剧照，真实摄影质感，<camera body> 实拍。`
   English:
   `cinematic live-action film still, photographic realism, shot on <camera body>.`

2. **Optical bokeh anchor** — add for shallow depth of field:
   `焦外为真实镜头光学虚化，背景结构连贯可信、可辨认，绝无涂抹感与绘画笔触。`
   English:
   `smooth optical lens bokeh; out-of-focus areas stay structurally coherent and photographic, never painterly smearing.`

3. **Softening budget** — if shallow depth of field is strong, reduce physical
   fog, bloom, diffusion, or grain to subtle levels. Do not stack every softening
   token at full strength. Distance-graded contrast/color falloff does not consume
   this budget because it does not blur structure.

## Tonal Density Anchor

Always preserve cinematic tonal density:

```text
完整影调范围，高光胶片式肩部柔和滚降，中间调厚实有密度、色彩浓郁不发灰，暗部浓黑有密度且细节沉入而非发灰上浮；画面有胶片负片般的厚度与体量感。
```

English:

```text
full tonal range with a gentle filmic highlight shoulder, dense weighted midtones with rich color density, deep blacks that hold detail and sit heavy rather than lifting into grey; the tactile density of a film negative.
```

Tonal density is not the same as simply making the image darker. Keep shadows deep
and clean, with detail present inside the black.

## GPT Image Compression

GPT Image responds better when the prompt is concise and layered. Aim for:

- English: 160 words or less.
- Chinese: 400 Chinese characters or less.

Merge layers instead of deleting important signals:

```text
Sentence 1: L1 scene + subject priority.
Sentence 2: medium anchor + framing + camera/lens + one primary depth mechanism.
Sentence 3: motivated lighting.
Sentence 4: color science + saturation + visible texture.
Sentence 5: mood + material realism + pure-positive clarity + tonal density.
Sentence 6: compressed anti-slop, with only the most important constraints.
```

## Model Notes

| Model | Note |
|-------|------|
| Midjourney | Prefer concise English technical terms. Add `--style raw` and the requested aspect ratio when useful. |
| Flux | Natural language works well. Convert noise-fuse terms to positive visible descriptions. |
| GPT Image | Use the compression rules above. Natural prose beats keyword stacks. |
| Unspecified | Keep the user's language and include the photography anchors when the prompt asks for cinematic realism. |
