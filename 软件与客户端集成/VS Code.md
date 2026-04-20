---
title: VS Code (Continue 插件) 深度集成指南
---

对于使用 VS Code 的开发者，**Continue** 是目前功能最强大、生态最开放的 AI 编程助手插件。通过接入无限星河AI，您可以极低成本让 VS Code 获得超越 GitHub Copilot 的体验（支持代码补全、对话提问、代码重构以及读取本地整个项目代码库）。

---

## 一、 插件安装

1.  打开 VS Code。
2.  点击左侧活动栏的 **[扩展]** 图标（或使用快捷键 `Ctrl+Shift+X` / `Cmd+Shift+X`）。
3.  在搜索框中输入 **"Continue"**。
4.  找到带有 Continue 官方标志的插件并点击 **[安装]**。

---

## 二、 接入无限星河AI 配置步骤

Continue 使用 JSON 配置文件进行深度定制。请按照以下步骤配置您的专属大模型：

### 1. 打开配置文件
安装完成后，点击 VS Code 左侧活动栏新增的 **Continue** 图标。在弹出的侧边栏右下角，点击 **[齿轮 / 设置]** 图标，这会打开名为 `config.json` 的配置文件。

### 2. 添加模型配置 (Models)
在 `config.json` 文件的 `models` 数组中，添加无限星河AI 的专属节点。您可以直接复制以下 JSON 代码块替换或追加到现有配置中：

```json
"models": [
  {
    "title": "无限星河-Claude 3.7",
    "model": "claude-3-7-sonnet",
    "apiKey": "您的_SK_密钥",
    "baseUrl": "http://infistar.ai/v1",
    "provider": "openai"
  },
  {
    "title": "无限星河-GPT 4o",
    "model": "gpt-4o",
    "apiKey": "您的_SK_密钥",
    "baseUrl": "http://infistar.ai/v1",
    "provider": "openai"
  }
],
```

> *注意：由于无限星河AI 完全兼容 OpenAI 协议，这里的 `provider` 必须填写为 `openai`，无论是调用 Claude 还是 Gemini。*

### 3. 配置自动补全 (Tab Autocomplete)
如果您希望在打字时获得实时的代码自动补全建议，请在 `config.json` 中找到或添加 `tabAutocompleteModel` 字段：

```json
"tabAutocompleteModel": {
  "title": "Tab 极速补全",
  "model": "gpt-4o-mini",
  "apiKey": "您的_SK_密钥",
  "baseUrl": "http://infistar.ai/v1",
  "provider": "openai"
}
```


---

## 三、 核心工作流使用技巧

* **对话与代码解释 (Chat)**：选中一段令人费解的代码，按下 `Cmd/Ctrl + L`，这段代码会自动进入 Continue 对话框，您可以让 AI 解释逻辑或寻找 Bug。
* **行内代码生成 (Edit)**：在编辑器中按下 `Cmd/Ctrl + I`，直接输入自然语言需求（例如：“在这里写一个验证邮箱格式的正则函数”），AI 会直接在您的代码文件中生成并高亮显示变更，您可以按 `Tab` 接受或按 `Esc` 拒绝。
* **全库上下文感知 (Context)**：在对话框输入 `@` 符号，可以引用特定的文件、文件夹、终端输出报错（Terminal）甚至官方文档文档库，让 AI 结合您的业务背景给出精准答案。

---

## 四、 常见问题排查 (FAQ)

### Q1：配置后无法连接，提示 Connection Error？
* 请检查 `baseUrl` 是否完整且正确：`http://infistar.ai/v1`（不要漏掉 `https://` 和 `/v1`）。
* 确保您的 API Key 没有多余的空格或换行。

### Q2：自动代码补全 (Tab) 速度很慢？
* 自动补全功能触发极为频繁，强烈建议在 `tabAutocompleteModel` 中使用 **`gpt-4o-mini`** 或 **`gemini-2.0-flash`**。这两个模型响应极快且成本极低，不建议使用 o1 等推理模型做自动补全。

### Q3：如何让模型读取我整个项目的代码？
* 您可以在 Continue 的设置中构建本地代码库索引（Codebase Indexing）。构建完成后，在对话框输入 `@Codebase`，模型即可跨越文件寻找代码关联逻辑。

---

## 五、 推荐模型搭配方案

* **复杂架构与深层逻辑重构**：`claude-3-7-sonnet` (目前开发者公认最强)
* **烧脑算法与断点 Debug**：`o1-preview` 或 `o3-mini` (思维链深度推理)
* **实时打字自动补全**：`gpt-4o-mini` (极致性价比与响应速度)

