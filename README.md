# Cinematic Prompt Engine

一个面向 Agent 的电影级画面 Prompt 生成 Skill，专为生图与 LOOK 迁移打造，帮助生成具备 HBO、高端剧集与好莱坞电影质感的视觉提示词。

This is a single, public, image-only Codex skill for cinematic prompt generation. It focuses on still-image prompts and LOOK transfer. Video, image-to-video, character sheets, and creature design are intentionally out of scope for now.

## What It Does

- Generates cinematic text-to-image prompts.
- Transfers one cinematographic LOOK onto a different scene.
- Uses DP-inspired presets, camera/lens/light/color parameters, and a tiered anti-slop system.
- Supports fuzzy style requests through a LOOK CARD confirmation step.

## Install

Clone this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Leo414x/cinematic_prompt.git ~/.codex/skills/cinematic-prompt-engine
```

Then restart Codex.

For SSH:

```bash
mkdir -p ~/.codex/skills
git clone git@github.com:Leo414x/cinematic_prompt.git ~/.codex/skills/cinematic-prompt-engine
```

## Examples

```text
用 Succession 风格，生成一个女人在雨夜停车场独自走向车的生图 prompt。
```

```text
用 dune_arrakis 的 LOOK，拍一座清晨雾中的未来神庙。
```

```text
赛博朋克夜景，一个快递员站在废弃高架桥下，先给我 LOOK CARD。
```

## Demo Gallery

See [demo/README.md](demo/README.md) for example images covering neon portraits, monumental worlds, dragon-scale fantasy, and grounded space suspense.

## Included Files

```text
SKILL.md
anti-slop-system.md
demo/
references/
  params.md
  presets.md
  recipes.md
examples/
  single-shot.md
  look-transfer.md
  look-card.md
```

## Scope

In scope:

- Still-image prompts
- Cinematic still frames
- LOOK transfer
- Preset-driven style
- Fuzzy LOOK CARD workflow

Out of scope for this public edition:

- Text-to-video
- Image-to-video
- Multi-shot video continuity
- Character design sheets
- Creature design sheets

## Disclaimer

Preset names are descriptive references for cinematographic study and prompt engineering. This project is not affiliated with HBO, Warner Bros., A24, Netflix, or any named film, show, studio, camera, lens, or software brand.
