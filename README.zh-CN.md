# AI Cinematic Prompt

**语言选择：**中文 | [English](README.en.md)

一个面向 Agent 的电影级画面 Prompt 生成 Skill，专为生图与 LOOK 迁移打造，帮助生成具备 HBO、高端剧集与好莱坞电影质感的视觉提示词。

如果这个项目对你有帮助，欢迎点一个 GitHub Star，让更多创作者和 Agent 开发者看到它。

更多案例和工作流分享，可以在抖音关注：

```text
Sky
ID: 28458932995
SecretSky
ID: 30648023970
```

## 能做什么

- 生成电影级生图 prompt。
- 把某个电影 / 剧集 / DP 质感迁移到新场景。
- 通过 preset 固定摄影机、镜头、光线、色彩、颗粒、情绪等参数。
- 对模糊风格请求先输出 LOOK CARD，确认后再出完整 prompt。
- 用分级 anti-slop 避免塑料感、CG 感、过度锐化、无动机补光等廉价 AI 画面问题。
- 针对 GPT Image、Flux、Midjourney 等生图模型，处理胶片颗粒、暗部噪点、摄影真实感和影调厚度。

## 最新更新：v0.3.0

本版本升级了雾气、体积光与空间纵深的生成逻辑。系统会根据场景条件，在光影与曝光分层、
距离渐变空气透视、遮挡与尺度递减之间选择合适的纵深机制，不再使用通用雾化制造空间感。

- 空气透视只降低远景对比与色彩分离，保留轮廓、边缘和背景结构。
- 雾、烟、尘、蒸汽及可见光束必须具备合理介质、明确光源、方向与衰减。
- 真空太空与洁净密闭环境不会自动生成大气雾霾或悬浮微粒。
- 纵深描述服从主体优先与软化预算，避免主体稀释和多重柔化造成的画面涂抹。

完整技术变更见 [CHANGELOG.md](CHANGELOG.md)。

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

查看 [demo/README.zh-CN.md](demo/README.zh-CN.md)，里面放了霓虹人物、巨构世界、史诗龙场景和太空悬疑几组示例图。

## 当前包含

- 生图 prompt
- 电影级静帧画面
- LOOK 迁移
- preset 风格驱动
- 模糊风格 LOOK CARD
- 生图模型适配
- 构思变体方向

## 后续计划

接下来会持续支持更新，包括但不限于：

- 文生视频
- 图生视频
- 多镜头视频连续性
- 角色定妆照 / 三视图 / 表情版
- 生物 / 龙 / 怪兽形象设计

如果你想持续跟进这个项目，欢迎点一个 Star 关注后续更新。

## Star 和关注

如果你把这个 skill 用进自己的 Agent 工作流，欢迎给项目点一个 Star，关注后续更新。

抖音关注：

```text
Sky
ID: 28458932995
SecretSky
ID: 30648023970
```

## 版权与许可

本项目已注册版权。禁止转售、禁止改名再发布、禁止作为商业 SaaS 核心能力；未经作者明确书面授权，不得将本项目或其任何实质性部分用于商业 API、商业 Agent 平台、付费插件、付费模板库、付费课程素材或其他商业产品。违反者将自行承担法律责任。

完整条款见 [LICENSE](LICENSE)。

## 说明

Preset 名称只用于摄影风格学习和 prompt 工程参考。本项目与 HBO、Warner Bros.、A24、Netflix 或任何提到的电影、剧集、工作室、摄影机、镜头、软件品牌均无官方关联。
