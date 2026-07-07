# AI Cinematic Prompt

**Language:** English | [中文](README.zh-CN.md)

中文用户请看：[README.zh-CN.md](README.zh-CN.md)

An image-only cinematic prompt skill for AI agents. It generates HBO / prestige-TV / Hollywood-grade image prompts and LOOK transfer prompts for still-image generation.

If this project helps you, please give it a Star. It helps more creators and Agent builders discover the skill.

For Chinese workflow notes and visual examples, follow me on Douyin:

```text
Sky
ID: 28458932995
```

## What It Does

- Generates cinematic text-to-image prompts.
- Transfers a cinematographic LOOK onto a different scene.
- Uses DP-inspired presets, camera/lens/light/color parameters, and a tiered anti-slop system.
- Supports fuzzy style requests through a LOOK CARD confirmation step.
- Keeps the public edition focused on still images only.

## Installation

Choose the folder used by your agent environment.

### Claude Code

HTTPS:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Leo414x/AI_Cinematic_Prompt.git ~/.claude/skills/cinematic-prompt-engine
```

SSH:

```bash
mkdir -p ~/.claude/skills
git clone git@github.com:Leo414x/AI_Cinematic_Prompt.git ~/.claude/skills/cinematic-prompt-engine
```

Restart Claude Code after installation.

### Codex

HTTPS:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Leo414x/AI_Cinematic_Prompt.git ~/.codex/skills/cinematic-prompt-engine
```

SSH:

```bash
mkdir -p ~/.codex/skills
git clone git@github.com:Leo414x/AI_Cinematic_Prompt.git ~/.codex/skills/cinematic-prompt-engine
```

Restart Codex after installation.

### Other Agent Runtimes

Clone this repository into the runtime's skills directory, keeping `SKILL.md` at the skill root:

```text
<your-agent-skills-dir>/cinematic-prompt-engine/SKILL.md
```

## Usage

Mention the skill by name, or describe a cinematic still-image prompt task.

Single image prompt:

```text
[$cinematic-prompt-engine] Generate a Succession-style cinematic image prompt: a woman walking alone toward her car in a rainy parking lot at night.
```

LOOK transfer:

```text
[$cinematic-prompt-engine] Use the dune_arrakis LOOK to shoot a futuristic temple in morning fog.
```

Fuzzy style direction:

```text
[$cinematic-prompt-engine] Cyberpunk night scene, a courier standing under an abandoned overpass. Give me a LOOK CARD first.
```

The skill will generate a full prompt directly when a preset is clear. If the style is fuzzy, it will propose a LOOK CARD first and wait for confirmation.

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

Coming next:

This public edition starts with still-image prompts and LOOK transfer. Future updates will expand the skill system, including but not limited to:

- Text-to-video
- Image-to-video
- Multi-shot video continuity
- Character portraits / turnarounds / expression sheets
- Creature / dragon / monster design

Star the repo if you want to follow focused updates.

## Star and Follow

If you use this skill in your own Agent workflow, a GitHub Star would mean a lot. I will keep this project focused and update it around cinematic image and video prompt workflows.

For more cinematic AI workflow notes and examples, follow me on Douyin:

```text
Sky
ID: 28458932995
```

## Disclaimer

Preset names are descriptive references for cinematographic study and prompt engineering. This project is not affiliated with HBO, Warner Bros., A24, Netflix, or any named film, show, studio, camera, lens, or software brand.
