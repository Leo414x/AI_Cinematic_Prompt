# AI Cinematic Prompt

**语言选择：**[English](README.md) | 中文

一个面向 Agent 的电影级画面 Prompt 生成 Skill，专为生图与 LOOK 迁移打造，帮助生成具备 HBO、高端剧集与好莱坞电影质感的视觉提示词。

如果这个项目对你有帮助，欢迎点一个 GitHub Star，让更多创作者和 Agent 开发者看到它。

更多案例和工作流分享，可以在抖音关注：

```text
Sky
ID: 28458932995
```

## 能做什么

- 生成电影级生图 prompt。
- 把某个电影 / 剧集 / DP 质感迁移到新场景。
- 通过 preset 固定摄影机、镜头、光线、色彩、颗粒、情绪等参数。
- 对模糊风格请求先输出 LOOK CARD，确认后再出完整 prompt。
- 用分级 anti-slop 避免塑料感、CG 感、过度锐化、无动机补光等廉价 AI 画面问题。

## 安装

根据你使用的 Agent 环境选择安装目录。

### Claude Code

HTTPS：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Leo414x/AI_Cinematic_Prompt.git ~/.claude/skills/cinematic-prompt-engine
```

SSH：

```bash
mkdir -p ~/.claude/skills
git clone git@github.com:Leo414x/AI_Cinematic_Prompt.git ~/.claude/skills/cinematic-prompt-engine
```

安装后重启 Claude Code。

### Codex

HTTPS：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Leo414x/AI_Cinematic_Prompt.git ~/.codex/skills/cinematic-prompt-engine
```

SSH：

```bash
mkdir -p ~/.codex/skills
git clone git@github.com:Leo414x/AI_Cinematic_Prompt.git ~/.codex/skills/cinematic-prompt-engine
```

安装后重启 Codex。

### 其他 Agent 环境

把仓库克隆到对应 Agent 的 skills 目录，并确保 `SKILL.md` 位于 skill 根目录：

```text
<你的-agent-skills-dir>/cinematic-prompt-engine/SKILL.md
```

## 使用方式

可以直接点名 skill，也可以直接描述电影级生图任务。

单张生图：

```text
[$cinematic-prompt-engine] 用 Succession 风格，生成一个女人在雨夜停车场独自走向车的生图 prompt。
```

LOOK 迁移：

```text
[$cinematic-prompt-engine] 用 dune_arrakis 的 LOOK，拍一座清晨雾中的未来神庙。
```

模糊风格先出 LOOK CARD：

```text
[$cinematic-prompt-engine] 赛博朋克夜景，一个快递员站在废弃高架桥下，先给我 LOOK CARD。
```

如果命中明确 preset，skill 会直接生成完整 prompt；如果是模糊风格，会先给 LOOK CARD 让你确认。

## Demo Gallery

查看 [demo/README.md](demo/README.md)，里面放了霓虹人物、巨构世界、史诗龙场景和太空悬疑几组示例图。

## 当前包含

- 生图 prompt
- 电影级静帧画面
- LOOK 迁移
- preset 风格驱动
- 模糊风格 LOOK CARD

## 当前不包含

- 文生视频
- 图生视频
- 多镜头视频连续性
- 角色定妆照 / 三视图 / 表情版
- 生物 / 龙 / 怪兽形象设计

## Star 和关注

如果你把这个 skill 用进自己的 Agent 工作流，欢迎给项目点一个 Star。

抖音关注：

```text
Sky
ID: 28458932995
```

## 说明

Preset 名称只用于摄影风格学习和 prompt 工程参考。本项目与 HBO、Warner Bros.、A24、Netflix 或任何提到的电影、剧集、工作室、摄影机、镜头、软件品牌均无官方关联。
