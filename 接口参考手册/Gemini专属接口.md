---
title: Gemini 专属聊天接口
---

完全兼容 Google Gemini 原生 API 的端点设计，方便一直对接 Google 生态的开发者平滑迁移至无限星河AI 平台。

> **标准生成端点：** `POST /v1beta/models/{model}:generateContent`
> **流式生成端点：** `POST /v1beta/models/{model}:streamGenerateContent?alt=sse`
> **身份认证：** `Authorization: Bearer 您的API_KEY`

## 路径参数
* **{model}**：在 URL 路径中直接替换为您要调用的模型名称，如 `gemini-2.0-flash`。

## 核心参数说明表

在发送请求时，请在请求体中提供以下参数：

| 参数名称 | 是否必填 | 参数说明 |
| :--- | :--- | :--- |
| **contents** | **必填** | 对话的内容部件（parts），包含文本或多模态数据的对象数组。 |
| **generationConfig** | 选填 | 生成参数配置对象，内部可设置温度 (temperature)、核采样 (topP) 以及最大输出长度 (maxOutputTokens)。 |
| **systemInstruction** | 选填 | 用于预设机器人人设的系统指令对象。 |
| **safetySettings** | 选填 | 安全审查设置等级控制。 |