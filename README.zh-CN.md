# Cinematic Prompt Engine

一个面向 Agent 的电影级画面 Prompt 生成 Skill，专为生图与 LOOK 迁移打造，帮助生成具备 HBO、高端剧集与好莱坞电影质感的视觉提示词。

这是一个独立、公开、只面向生图的 Codex Skill。当前版本只做电影级静帧 prompt 和 LOOK 迁移，不包含视频、图生视频、角色设定、生物设定、多 skill 路由。

## 能做什么

- 生成电影级生图 prompt。
- 把某个电影 / 剧集 / DP 质感迁移到新场景。
- 通过 preset 固定摄影机、镜头、光线、色彩、颗粒、情绪等参数。
- 对模糊风格请求先输出 LOOK CARD，确认后再出完整 prompt。
- 用分级 anti-slop 避免塑料感、CG 感、过度锐化、无动机补光等廉价 AI 画面问题。

## 安装

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Leo414x/cinematic_prompt.git ~/.codex/skills/cinematic-prompt-engine
```

然后重启 Codex。

SSH 安装：

```bash
mkdir -p ~/.codex/skills
git clone git@github.com:Leo414x/cinematic_prompt.git ~/.codex/skills/cinematic-prompt-engine
```

## 示例

```text
用 Succession 风格，生成一个女人在雨夜停车场独自走向车的生图 prompt。
```

```text
用 dune_arrakis 的 LOOK，拍一座清晨雾中的未来神庙。
```

```text
赛博朋克夜景，一个快递员站在废弃高架桥下，先给我 LOOK CARD。
```

## 当前不包含

- 文生视频
- 图生视频
- 多镜头视频连续性
- 角色定妆照 / 三视图 / 表情版
- 生物 / 龙 / 怪兽形象设计

## 说明

Preset 名称只用于摄影风格学习和 prompt 工程参考。本项目与 HBO、Warner Bros.、A24、Netflix 或任何提到的电影、剧集、工作室、摄影机、镜头、软件品牌均无官方关联。
