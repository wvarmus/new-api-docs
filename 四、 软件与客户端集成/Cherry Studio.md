# Cherry Studio 集成指南

Cherry Studio 是一款支持多平台、界面优雅且功能全面的桌面 AI 客户端。通过本指南，您可以轻松将无限星河AI 的算力接入其中。

---

## 一、 软件下载

建议您前往官方渠道下载最新版本的安装包，以获得最佳的稳定性和最新的功能支持（如联网搜索、长文本处理等）。

* **官方网站**：[https://cherry-ai.com](https://cherry-ai.com)
* **GitHub 发布页**：[https://github.com/CherryHQ/cherry-studio/releases](https://github.com/CherryHQ/cherry-studio/releases)
* **支持平台**：Windows (x64/arm64)、macOS (Intel/Apple Silicon)、Linux。

---

## 二、 基础配置步骤

配置无限星河AI 中转服务，您只需操作以下三个核心步骤：

### 1. 进入设置界面

打开 Cherry Studio 后，点击左下角的 **[设置]** 图标（齿轮形状），在弹出的侧边栏中选择 **[模型服务]**。

### 2. 添加 OpenAI 兼容服务

在模型服务列表中找到 **[OpenAI]** 选项。如果已经有默认配置，可以点击旁边的“添加”按钮新建一个配置，或者直接修改现有配置。

### 3. 填写关键参数

请严格按照以下说明填写：

* **API 密钥 (API Key)**：填入您在无限星河AI 后台生成的 `sk-` 开头的密钥。
* **API 地址 (API Base URL)**：填入本站的核心地址：`https://api.wxxingheai.com/v1`
    * *注意：Cherry Studio 必须在地址末尾加上 `/v1`。*
* **模型列表**：点击旁边的“检查”或“管理模型”按钮，您可以手动添加如 `gpt-4o`、`claude-3-5-sonnet`、`gemini-2.0-flash` 等模型名称。

> **图示说明**： 红色方框标出 API Key 填入位置和 Base URL 的完整路径。

---

## 三、 进阶技巧：模型管理

Cherry Studio 允许您为不同的任务创建不同的模型分组：

1.  **自动获取模型**：在设置好 API 地址和 Key 后，点击“检查”按钮，Cherry Studio 会尝试自动通过 `/v1/models` 接口拉取您账号下可用的所有模型。
2.  **默认模型设置**：在对话界面顶部的下拉菜单中，选择您最常用的模型作为默认开启项。

---

## 四、 常见问题排查 (FAQ)

### Q1：连接测试失败，提示 404？

* **原因**：通常是 API 地址填写不完整。
* **解决方法**：请确保地址为 `https://api.wxxingheai.com/v1`，不要漏掉结尾的 `/v1`。

### Q2：提示 401 Unauthorized？

* **原因**：API Key 填写错误，或者 Key 已经被重置。
* **解决方法**：去无限星河AI 后台重新复制一遍最新的密钥，并检查粘贴时是否带有多余的空格。

### Q3：如何启用 Claude 的思考过程 (Thinking)？

* **配置**：在模型管理中，确保填入的模型 ID 正确（如 `claude-3-7-sonnet`）。由于 Cherry Studio 深度支持原生协议，在对话设置中开启“思考”模式即可。

---

## 五、 推荐使用场景

* **长文档翻译**：配合无限星河AI 的 `claude-3.5-sonnet` 模型，可以实现极高质量的学术论文翻译。
* **代码助手**：通过配置 `o1` 或 `deepseek` 模型，在 Cherry Studio 侧边栏进行代码逻辑分析。