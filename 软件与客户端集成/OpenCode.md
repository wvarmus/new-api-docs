---
title: OpenCode (开源终端编程智能体) 深度集成指南
---

[OpenCode](https://github.com/anomalyco/opencode) 是一款火爆开源社区的 AI 编程智能体。它在设计思路上直接对标 Anthropic 官方的 Claude Code，但提供了更极致的终端用户界面（TUI）、开箱即用的本地 LSP 支持，并且**完全不绑定任何大模型厂商**。

通过将 OpenCode 接入无限星河AI 的网关，您可以让它在您的终端里自主阅读代码、规划架构、运行测试并修复 Bug。

---

## 一、 核心特色与优势

* **完全开源且中立**：允许配置任何兼容 OpenAI 协议的中转服务，告别原厂高昂的定价体系。
* **原生 LSP 支持**：与普通文本分析不同，OpenCode 能像真正的 IDE 一样理解您的项目跳转、类型推导和代码结构。
* **双模式 Agent 切换**：内置 `build`（全权开发模式）和 `plan`（只读规划模式），按 `Tab` 键即可一键切换。
* **极致终端美学**：由资深 Neovim 玩家打造，终端交互体验极其流畅。

---

## 二、 软件获取与安装

OpenCode 支持全平台安装。请打开您的终端（Terminal）并选择以下任意一种方式：

* **一键安装脚本 (推荐，Mac/Linux)**:
  ```bash
  curl -fsSL https://opencode.ai/install | bash
  ```
* **使用 NPM (Node.js)**:
  ```bash
  npm i -g opencode-ai@latest
  ```
* **使用 Homebrew (Mac)**:
  ```bash
  brew install anomalyco/tap/opencode
  ```
*(注：OpenCode 目前也推出了桌面端 App (Beta 版)，您可以前往其 GitHub Releases 页面下载对应的 `.dmg` 或 `.exe` 文件。)*

---

## 三、 接入无限星河AI 配置步骤

由于 OpenCode 是纯粹的 Provider-Agnostic（提供商中立），您可以通过环境变量或启动后的图形向导来接入无限星河 API。

### 方法 1：环境变量配置 (最稳定推荐)
在您的终端配置文件（如 `~/.zshrc` 或 `~/.bashrc`）中添加以下内容：

```bash
export OPENAI_API_BASE="https://infistar.ai/v1"
export OPENAI_API_KEY="您的_SK_密钥"
export OPENAI_MODEL_NAME="claude-3-7-sonnet"  # 默认启动模型
```
保存后运行 `source ~/.zshrc`，然后在项目根目录下直接输入 `opencode` 即可唤醒。

### 方法 2：TUI 交互式配置
1. 在终端中直接运行命令启动：
   ```bash
   opencode
   ```
2. 首次启动时，界面会引导您配置 Provider。
3. 选择 **Custom / OpenAI Compatible**（自定义/兼容 OpenAI 协议）。
4. **Base URL**：填入 `https://infistar.ai/v1`
5. **API Key**：填入您的无限星河 `sk-` 密钥。


---

## 四、 核心玩法与指令建议

启动 OpenCode 后，您直接在终端里与它对话：

### 1. 安全探索未知项目 (Plan 模式)
按下 `Tab` 键切换到 **`plan`** 模式（只读）。
* **指令**：*“我是这个项目的新人，帮我分析一下整个后端的登录鉴权逻辑是在哪里实现的？画个简单的流程图。”*
* **优势**：此模式下 AI 无法修改文件，也无法运行破坏性脚本，最适合用来做代码审计和架构学习。

### 2. 全权委托开发 (Build 模式)
按下 `Tab` 键切换回默认的 **`build`** 模式（全权限）。
* **指令**：*“运行 `npm test`，根据报错信息，找到对应的组件并修复问题，修复后再次运行测试直到通过。”*
* **优势**：AI 会自主调用终端命令，进入“报错-分析-改写-验证”的闭环循环。

---

## 五、 常见问题排查 (FAQ)

### Q1：为什么运行复杂重构时感觉模型“变笨”了？
* OpenCode 在读取整个工作区时会构建庞大的上下文。如果您默认使用的是小模型（如 `gpt-4o-mini`），它极易在海量代码中“迷失”。
* **解决方案**：在应用内切换为 `claude-3-7-sonnet` 或 `o1` 系列。

### Q2：提示 "Connection Error" 无法连接？
* 请检查 Base URL 是否正确包含了 `https://` 前缀以及末尾的 `/v1`。
* 确保您的终端没有挂载冲突的网络代理（Proxy）。

### Q3：它与 Claude Code 到底有什么区别？
* Claude Code 强制绑定 Anthropic 官方计费，国内访问困难。而 OpenCode 允许您使用无限星河等高性价比中转网关，不仅可以使用 Claude，还能自由切换到 GPT-4o 或 Gemini 等其他厂商的旗舰模型。

---

## 六、 黄金模型搭配建议

* **代码审计与架构解析 (Plan 模式)**：`claude-3-7-sonnet` (长文本逻辑最严谨)
* **日常迭代与轻量重构 (Build 模式)**：`gpt-4o` (速度与准确率平衡)
* **极速询问与脚本编写**：`gemini-2.0-flash` (响应极快)

