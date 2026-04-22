---
title: OpenClaw (全能自治 AI 智能体) 深度集成指南
---

OpenClaw 是目前全球最火爆的开源 AI 智能体框架 (Agent Framework)。它打破了传统 AI“一问一答”的限制，可以作为您的数字分身 24/7 在后台运行，不仅能接入 Telegram、Slack、Discord 等您常用的通讯软件，还能通过技能库（Skills）帮您处理邮件、管理日历甚至运行代码。

通过无限星河AI 的高可用网关，您可以让 OpenClaw 拥有全球顶尖的逻辑驱动引擎。

---

## 一、 软件获取与安装

OpenClaw 运行在您的本地终端或服务器上。请确保您的系统已安装 Node.js（推荐 v18+）和 Docker（可选，用于运行安全沙盒）。

在终端中运行官方推荐的一键引导程序：

```bash
npx openclaw onboard
```

> *注：您也可以通过 `npm install -g openclaw` 全局安装，并在任意位置运行 `openclaw`。*

---

## 二、 接入无限星河AI 配置步骤

OpenClaw 提供了极其友好的交互式配置向导。您可以直接在引导中完成配置，也可以修改本地文件。

### 1. 终端向导配置 (Onboard 流程)
当您运行 `openclaw onboard` 后，在终端提示进行 **Inference/LLM** 设置时：

1. **Select Provider (选择提供商)**：使用方向键选择 **Custom / OpenAI Compatible**（自定义/兼容 OpenAI 协议）。
2. **Base URL (接口地址)**：填入：`https://infistar.ai/v1`
3. **API Key (密钥)**：粘贴您在无限星河后台生成的 `sk-` 密钥。
4. **Select Model (选择模型)**：手动输入 `claude-3-7-sonnet` 或 `gpt-4o`。

### 2. 修改本地配置文件 (进阶)
如果您已经完成了初始化，可以直接编辑您的工作区配置文件（通常位于 `~/.openclaw/config.yaml` 或 workspace 目录下的配置）：

```yaml
llm:
  provider: openai
  base_url: "https://infistar.ai/v1"
  api_key: "您的_SK_密钥"
  model: "claude-3-7-sonnet"
```


---

## 三、 OpenClaw 核心黑科技与玩法

### 1. 全渠道接管 (Channels)
配置完成后，您可以将 OpenClaw 绑定到您的 Telegram 机器人或 Slack 工作区。您在手机上直接给它发消息：*“帮我查一下明天去北京的航班并整理成表格发给我”*，它会在后台默默调用浏览器插件完成搜索并回复您。

### 2. 技能拓展 (ClawHub Skills)
OpenClaw 拥有庞大的插件生态。您可以为它安装各种技能，例如：
* 读取本地文件和系统命令（它甚至可以自主关闭您的电脑）。
* 自动化发送邮件。
* 定时巡检网页并提取每日新闻摘要。

### 3. 灵魂与长期记忆 (SOUL.md & Memory)
在您的 OpenClaw 工作区中，有一个 `SOUL.md` 文件。您可以在这里定义它的性格、您的偏好和长期目标。配合高上下文模型，它会真正成为一个“懂你”的专属助理。

---

## 四、 常见问题排查 (FAQ)

### Q1：为什么 Agent 在执行复杂任务时突然死循环或“产生幻觉”？
* **核心原因**：Autonomous Agent（自治智能体）在调用工具（如搜索、读文件）时会产生大量的中间思考过程，如果模型的逻辑能力不够，极易陷入死循环。
* **解决方案**：强烈建议将主力驱动模型从 `gpt-4o-mini` 切换为 **`claude-3-7-sonnet`**，Claude 在长上下文的 Agent 任务中表现目前公认最稳。

### Q2：它一直在后台运行，Token 费用会不会爆炸？
* OpenClaw 会持续监控您的频道和定时任务。为了避免不可控的消费，建议在无限星河后台为这个特定的 API Key 设置一个**每日/每月额度上限（Quota）**。

### Q3：配置完成后提示 "Connection Refused" 无法连接模型？
* 请检查配置文件中的 `base_url` 是否漏写了 `https://`，或者末尾少写了 `/v1`。

---

## 五、 黄金模型搭配建议

* **日常消息处理 & 新闻摘要**：`gpt-4o`
* **复杂工具调用 & 本地文件操作**：`claude-3-7-sonnet` (Agent 界的神级模型，必备)
* **高风险代码自动化修复**：`o1-preview`

