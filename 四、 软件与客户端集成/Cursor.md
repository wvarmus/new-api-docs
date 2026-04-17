# Cursor AI 代码编辑器集成指南

Cursor 是一款基于 VS Code 开发的深度集成 AI 的代码编辑器。它不仅支持基础的对话，还能理解您的整个项目代码库（Codebase），提供精准的代码补全和重构建议。通过无限星河AI，您可以让 Cursor 拥有最顶尖的推理能力。

---

## 一、 软件下载
* **官方网站**：[https://cursor.com](https://cursor.com)
* **支持平台**：Windows, macOS, Linux

---

## 二、 接入无限星河AI 配置流程

Cursor 默认使用其自带的服务，要使用无限星河AI，需要开启“覆盖模式”：

### 1. 进入模型设置
1. 打开 Cursor 界面。
2. 点击右上角的 **[设置] (齿轮图标)**，或者使用快捷键 `Cmd + Shift + J` (Mac) 或 `Ctrl + Shift + J` (Windows)。
3. 在左侧菜单中选择 **[Models]**。

### 2. 配置 API Key 与 Base URL
1. 在 **OpenAI API Key** 选项框中，填入您在无限星河生成的 `sk-` 密钥。
2. 点击下方的 **[Override OpenAI Base URL]**（覆盖默认地址）。
3. 在弹出的输入框中填入：`https://api.wxxingheai.com/v1`
4. 点击 **[Verify]** 或回车确认。

> **[图片备注：Cursor 模型设置页配置示意图]**
> 展示设置窗口中 Model 选项卡下，如何填写密钥以及点击蓝色文字“Override OpenAI Base URL”并填入中转地址的过程。

### 3. 启用特定模型
在 Models 列表中，确保勾选了您想使用的型号，例如：
* `gpt-4o`
* `claude-3-7-sonnet` (推荐，代码能力极强)
* `o1` (逻辑推理强项)

---

## 三、 Cursor 核心功能使用技巧

### 1. 对话模式 (Chat) - `Cmd/Ctrl + L`
在侧边栏直接向 AI 提问。输入 `@` 可以引用特定的文件（Files）、文件夹（Folders）或外部文档（Docs），无限星河AI 将根据这些上下文给出代码建议。

### 2. 行内编辑 (Composer) - `Cmd/Ctrl + I`
这是 Cursor 最强大的功能。您可以描述一个功能（例如：“帮我写一个登录页面的 API 接口”），AI 会直接在编辑器中生成代码，您可以点击 `Apply` 直接应用。

### 3. 代码预测 (Tab Completion)
当您开启了 API 接入后，Cursor 依然可以利用大模型的推理能力预测您的下一行代码。建议配合 `gpt-4o-mini` 使用，以获得更快的补全速度。

---

## 四、 常见问题排查 (FAQ)

### Q1：提示 "Connection Error" 或请求失败？
* **地址检查**：确保 Base URL 填入的是 `https://api.wxxingheai.com/v1`。
* **余额检查**：Cursor 的 Composer 功能消耗 Token 较快，请确保您的无限星河账户余额充足。

### Q2：如何切换到 Claude 3.7 模型？
* 在对话框底部的模型选择器中，如果找不到该模型，请在 **[Models]** 设置页的 "Add model" 处手动输入 `claude-3-7-sonnet`。

### Q3：为什么无法使用 Cursor Tab 功能？
* 注意：Cursor 的某些原生高级补全功能（Cursor Tab）可能需要订阅 Cursor Pro 才能完全解锁。但通过接入无限星河 API，您已经可以使用最核心的 Chat 和 Edit 功能。

---

## 五、 推荐配合模型方案

* **代码重构与 Debug**：`claude-3-7-sonnet` (代码逻辑最严谨)
* **复杂架构设计**：`o1` 或 `o3-mini` (擅长处理长链路逻辑)
* **日常脚本/注释生成**：`gpt-4o-mini` (高性价比之选)