---
title: NextChat (Next Web) 集成指南
---

NextChat（原名 ChatGPT Next Web）是一款拥有极简 UI 设计、跨平台且极其轻量的 AI 客户端。它不仅提供开箱即用的桌面端，还支持一键免费部署到 Vercel 等 Serverless 平台，非常适合追求纯粹对话体验的用户。

---

## 一、 软件获取与部署

您可以根据自己的需求选择桌面版或网页端：

* **桌面版下载**：[https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web/releases](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web/releases) （支持 Windows, macOS, Linux）
* **网页端在线体验**：[https://app.nextchat.dev/](https://app.nextchat.dev/)
* **私有化部署**：支持在 GitHub Fork 后一键部署至 Vercel，打造专属您个人的网页版 AI 助手。

---

## 二、 接入无限星河AI 配置步骤

1.  **进入设置**：打开 NextChat，点击页面左下角的 **[设置]**（齿轮图标）。
2.  **模型服务商**：在“模型服务商”选项中选择 **OpenAI**。
3.  **接口地址 (Endpoint)**：
    * 开启 **“自定义接口”** 开关。
    * 在输入框中填入：`https://api.wxxingheai.com`
    * *注意：NextChat 底层会自动追加 `/v1`，所以此处只需填写根域名即可。如果您部署的是自己的网页版，请确保环境变量 `BASE_URL` 填写正确。*
4.  **API Key**：填入您在无限星河后台生成的 `sk-` 密钥。
5.  **自定义模型**：由于大模型更新频繁，如果下拉列表中没有最新的模型，您可以在 **[自定义模型]** 栏中手动输入。
    * 格式要求：使用 `+` 号添加，多个模型用英文逗号隔开。
    * 示例：`+gpt-4o,+claude-3-7-sonnet,+o1-preview`

> **[图片备注：NextChat 设置界面截图]**
> 展示设置页面的“自定义接口”开关开启状态，高亮标出“接口地址”、“API Key”以及“自定义模型”的填写区域。

---

## 三、 进阶功能推荐：面具 (Masks)

NextChat 最强大的功能之一是其内置的**“面具 (Masks)”**系统，也就是预设提示词（Prompts）。

* **使用方法**：在新建对话时点击右上角的“面具”图标，您可以选择数十种预设的系统级专家身份（如：小红书写手、英翻中专家、Linux 终端模拟器等）。
* **搭配建议**：不同的面具对模型的逻辑要求不同。例如使用“代码专家”面具时，建议将顶部模型切换为 `claude-3-7-sonnet` 或 `o1` 系列，以获得最专业的解答。

---

## 四、 常见问题排查 (FAQ)

### Q1：网页端提示 "Failed to fetch" 或网络错误？
* 如果您使用的是 NextChat 网页版（非本地客户端），由于浏览器的跨域安全限制（CORS），直接在网页填入 API Key 可能会被拦截。
* **解决方案**：建议下载并使用**桌面客户端**，或者将应用私有化部署到 Vercel 等平台，通过服务端进行代理请求。

### Q2：提示 "Invalid API Key" 或 "Unauthorized"？
* 请检查 API Key 是否复制完整，确保没有多余的空格。
* 如果您是自己部署的 Vercel 服务，请检查环境变量中的 `OPENAI_API_KEY` 是否填写错误。

### Q3：聊天时模型回复突然中断？
* 可以在设置中调整 **“附带历史消息数”**，避免因为历史记录过长导致单次请求 Token 超出模型上限。

---

## 五、 推荐配合模型

* **日常面具/快速问答**：`gpt-4o-mini`
* **专业沉浸写作**：`claude-3-5-sonnet` 或 `claude-3-7-sonnet`
* **复杂数学/代码推理**：`o1-preview`