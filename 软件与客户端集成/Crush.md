---
title: Crush (极客终端 AI 助手) 深度集成指南
---

Crush 是由著名终端美化团队 Charm 打造的新一代 Terminal-based AI 编程助手。它不仅拥有极具美感的终端用户界面（TUI），还原生集成了 LSP（语言服务器协议）、MCP（模型上下文协议）以及本地文件/终端执行权限。

通过连接无限星河AI 的高可用网关，您可以让 Crush 拥有全球最聪明的大脑，在您的命令行里“呼风唤雨”。

---

## 一、 软件获取与安装

Crush 支持全平台（macOS, Linux, Windows），您可以根据自己常用的包管理器进行安装：

* **Homebrew (Mac/Linux)**:
  ```bash
  brew install charmbracelet/tap/crush
  ```
* **NPM (Node.js)**:
  ```bash
  npm install -g @charmland/crush
  ```
* **Go 环境**:
  ```bash
  go install github.com/charmbracelet/crush@latest
  ```

---

## 二、 接入无限星河AI 配置步骤

Crush 提供了非常优雅的交互式配置界面。首次运行或重新配置时，请按以下步骤操作：

### 1. 启动应用
在您的终端中输入并回车：
```bash
crush
```

### 2. 交互式配置指引
当界面弹出配置提示时，请使用键盘方向键进行选择：

1. **Select Provider (选择服务商)**: 选择 **OpenAI Compatible**（或 Custom / 自定义选项）。
2. **Base URL (接口地址)**: 输入无限星河的网关地址：
   `http://infistar.ai/v1`
3. **API Key (密钥)**: 粘贴您在无限星河后台生成的 `sk-` 密钥。
4. **Select Model (选择模型)**: 您可以直接输入 `gpt-4o`、`claude-3-7-sonnet` 或 `o1-preview` 等无限星河支持的模型 ID。

> *提示：Crush 会将您的配置安全地保存在本地（如 `~/.local/share/crush/crush.json`）。后续启动时无需再次输入。*


---

## 三、 Crush 核心黑科技与使用技巧

### 1. 终端级权限与自动化执行
与网页端 AI 不同，Crush 拥有操作您本地机器的工具集。您可以直接命令它：
* *"帮我全局搜索一下项目中所有过期的 API 调用，并把它们替换为新语法。"*
* *"运行一下当前的测试用例，如果报错了，帮我找到原因并直接修改代码。"*

### 2. 深度上下文与 LSP 集成
Crush 可以调用您本地的 LSP（如 Python 的 pyright，TS 的 tsserver）。这意味着它不仅在“看文本”，还能像真正的 IDE 一样理解您的代码跳转、类型定义和语法错误。

### 3. 会话管理 (Sessions)
Crush 支持多会话状态留存。您可以随时中途切换模型（例如：先用 `gpt-4o-mini` 快速生成骨架，再切换为 `claude-3-7-sonnet` 处理核心逻辑），而不会丢失任何聊天历史。

---

## 四、 常见问题排查 (FAQ)

### Q1：为什么执行复杂任务时容易卡住或报错中断？
* **终端工具特性**：由于 Crush 会频繁地使用 `ls`、`grep`、`cat` 等工具读取文件并与 AI 进行多轮往返对话，极度依赖模型的**“思维链连贯性”**与**“并发稳定性”**。
* **解决方案**：请务必确保您的无限星河账户余额充足，并在进行大规模重构时使用 `claude-3-7-sonnet` 等顶级长文本代码模型。

### Q2：如何更新或修改已绑定的 API Key？
* 您可以直接修改配置文件 `~/.local/share/crush/crush.json`。
* 或者在启动 Crush 后，输入系统命令（如 `/config` 或 `/provider`，具体视当前版本而定）重新唤起配置面板。

### Q3：Crush 会不经允许乱改文件吗？
* **不会**。对于文件写入 (`write`, `edit`) 和命令行执行 (`bash`) 等敏感工具调用，Crush 默认都会在终端弹出互动式的权限确认框。您可以审查它想执行的操作，确认无误后再按 `Enter` 放行。

---

## 五、 黄金模型搭配建议

* **本地探索与文件整理**：`gpt-4o-mini` (低成本，处理日常脚本极佳)
* **复杂架构与多文件重构**：`claude-3-7-sonnet` (代码推理天花板，完美兼容工具调用)
* **硬核算法与底层排错**：`o1` 或 `o3-mini` (逻辑深度极强)

