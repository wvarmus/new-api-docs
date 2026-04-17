# Claude Code (CLI) 全面集成指南

Claude Code 是 Anthropic 官方发布的命令行编程助手（CLI）。它不同于普通的对话插件，能够直接在您的本地终端内深入项目目录，执行代码分析、自动化 Bug 修复、运行测试并直接提交 Git 变更。通过无限星河AI 的高速网关，您可以完美激活 Claude 3.7 的“Thinking（深度思考）”模式。

---

## 一、 核心功能

* **自主式编程**：只需一个指令（如：`claude "重构这个组件并增加单元测试"`），它会自动读取文件、编写代码、运行测试并循环修复直至成功。
* **思维链支持**：支持 Claude 3.7 Sonnet 的原生推理能力，处理复杂的工程逻辑。
* **Git 工作流集成**：自动生成极具描述性的 Commit Message 并执行提交。
* **全环境感知**：它能理解您的终端报错、文件结构以及运行环境。

---

## 二、 安装指南

Claude Code 基于 Node.js 开发，请确保您的系统中已安装 Node.js (v18+)。在终端执行：

```bash
npm install -g @anthropic-ai/claude-code
```

---

## 三、 接入无限星河AI 配置流程

由于 Claude Code 默认连接官方服务器，您需要通过环境变量将其重定向至无限星河AI 的高可用网关。

### 1. 配置环境变量 (推荐)
为了确保每次启动都能自动接入，请根据您的操作系统进行配置：

* **Mac/Linux (Zsh)**:
  在 `~/.zshrc` 文件末尾添加：
  ```bash
  export ANTHROPIC_BASE_URL="https://api.wxxingheai.com/v1"
  export ANTHROPIC_API_KEY="您的_SK_密钥"
  ```
  保存后运行 `source ~/.zshrc` 生效。

* **Windows (PowerShell)**:
  ```powershell
  [Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://api.wxxingheai.com/v1", "User")
  [Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "您的_SK_密钥", "User")
  ```

### 2. 启动 Claude Code
在您的项目根目录下输入以下命令即可启动：
```bash
claude
```

> **[图片备注：Claude Code 启动与交互界面]**
> 展示终端中 Claude Code 的登录动画，以及它在“Thinking”模式下逐步拆解任务、列出计划并执行修改的交互过程。

---

## 四、 常用指令与技巧

进入 `claude` 交互界面后，您可以：

* **直接对话**：`"帮我分析一下为什么这个接口在并发时会报错？"`
* **运行命令**：输入 `/run npm test` 让 AI 执行测试并根据结果自我修正。
* **文件操作**：输入 `/search "AuthLogic"` 在项目中搜索特定逻辑。
* **提交变更**：任务完成后输入 `/commit`，AI 会自动根据修改内容写好 Commit 信息并提交。

---

## 五、 为什么选择无限星河AI 配合使用？

1. **思维链（Thinking）不降级**：我们完整透传 Claude 3.7 的 Extended Thinking 特性，让 AI 在处理难题时不再“偷懒”。
2. **极速响应**：通过分布式中转，大幅降低 CLI 工具在频繁读取文件时的往返延迟。
3. **高额并发保障**：Claude Code 在索引项目时会产生密集请求，无限星河企业级节点确保您的调用不被限流。

---

## 六、 常见问题排查 (FAQ)

### Q1：启动时提示 API 连接错误？
* 请检查 `ANTHROPIC_BASE_URL` 是否正确设置为 `https://api.wxxingheai.com/v1`。
* 确保您的 API Key 具有足够的余额，因为 Claude Code 会读取大量项目上下文，Token 消耗较快。

### Q2：如何开启/关闭“深度思考”模式？
* 您可以在启动时通过参数控制，或者在交互界面中要求 AI：`"使用 Thinking 模式处理接下来的复杂逻辑"`。

### Q3：它会修改我本地的文件吗？
* 是的，Claude Code 旨在直接修改代码。在执行写入操作前，它会展示 Diff（代码差异）并询问您的许可。

---

## 七、 推荐模型配置

* **工程重构与复杂 Debug**：`claude-3-7-sonnet` (官方钦定最强搭配)
* **日常咨询与简单修改**：`claude-3-5-haiku` (极致响应速度与低成本)