# Composable Recipes — Mix-and-Match LOOK Library

Recipes are reusable building blocks for the LOOK. Unlike the full DP presets in
`presets.md` (which fix all 17 parameters), a recipe fixes only one *slice* of the
look, so they can be freely combined into novel looks without writing a full preset.

Three recipe categories, covering **10 of the 17 parameters**:

- **CAMERA_KIT** → `camera` + `lens` + `aperture`
- **LIGHT_RECIPE** → `light_source` + `light_style` + `fill`
- **COLOR_GRADE** → `palette` + `saturation` + `film_stock` + `grain`

The remaining **6 parameters are NOT set by recipes**:

- LOOK layer: `mood` — choose per look (see `params.md` axis 17).
- FRAMING layers: `shot`, `aspect`, `composition`, `angle`, `foreground` — vary per shot/scene.

> A complete LOOK = **one CAMERA_KIT + one LIGHT_RECIPE + one COLOR_GRADE + a mood**.
> All recipe values are param IDs — look up each ID's zh/en token in
> `references/params.md` when assembling a prompt.

When a recipe combo is saved as a named preset (see SKILL.md → Save-as-Preset), the
10 recipe params plus the 7 settled framing/mood params expand into the full
17-parameter preset format used in `presets.md`.

---

## CAMERA_KIT — camera + lens + aperture

| ID | 名称 | camera | lens | aperture |
|----|------|--------|------|----------|
| `lf_anamorphic` | 大画幅变形宽银幕 | alexa_lf | anamorphic_40 | T2.8 |
| `intimate_portrait` | 亲密人像 | alexa_mini | telephoto_85 | T1.4 |
| `docu_telephoto` | 纪录片长焦 | alexa_mini | telephoto_200 | T2.8 |
| `raw_16mm` | 粗糙16mm | film_16mm | spherical_35 | T2.8 |
| `epic_deep` | 史诗深焦 | alexa_lf | spherical_24 | T5.6 |
| `classic_35mm` | 经典35mm | film_35mm | spherical_50 | T2 |

## LIGHT_RECIPE — light_source + light_style + fill

| ID | 名称 | light_source | light_style | fill |
|----|------|--------------|-------------|------|
| `overcast_natural` | 阴天自然主义 | overcast_window | naturalistic | no_fill |
| `practical_warm` | 实用光源暖调 | practical_lamp | chiaroscuro | minimal |
| `golden_natural` | 黄金时刻 | golden_hour | naturalistic | no_fill |
| `fluorescent_clinical` | 荧光灯临床 | fluorescent | top_light | no_fill |
| `neon_contrast` | 霓虹明暗 | neon | chiaroscuro | no_fill |
| `moonlight_cold` | 月光冷寂 | moonlight | low_key | no_fill |
| `firelight` | 火光摇曳 | candle_fire | chiaroscuro | minimal |
| `available_cold` | 冷可用光 | overcast_window | available | minimal |

## COLOR_GRADE — palette + saturation + film_stock + grain

| ID | 名称 | palette | saturation | film_stock | grain |
|----|------|---------|------------|------------|-------|
| `earth_muted` | 去饱和大地 | desaturated_earth | low | kodak_500t | fine |
| `corporate_cold` | 冷蓝灰企业 | cold_corporate | low | none | fine |
| `golden_low` | 暖金低饱和 | warm_golden | low | kodak_250d | medium |
| `sickly_desat` | 病态青绿 | sickly_green | very_low | fuji_eterna | medium |
| `bleach_grit` | 漂白跳过 | bleach_bypass | low | kodak_500t | medium |
| `neon_vivid` | 霓虹中饱和 | neon_contrast | moderate | kodak_500t | fine |
| `neutral_clean` | 冷中性干净 | cool_neutral | moderate | none | fine |
